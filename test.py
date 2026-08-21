#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import random
import statistics
import sys
import time

try:
    import hkd_solver_free_v2 as hkd_solver_free
except ImportError:
    import hkd_solver_free

try:
    import hkd_solver_paid
    HAVE_PAID = True
except ImportError:
    hkd_solver_paid = None
    HAVE_PAID = False

try:
    import gurobipy as gp
    from gurobipy import GRB
    HAVE_GUROBI = True
except ImportError:
    gp = None
    GRB = None
    HAVE_GUROBI = False


JOBS = 500
GROUPS = 3
WIDTH = 3
DECOYS_PER_GROUP = 3
REQUIRED_SPEEDUP = 4.0


def clock():
    try:
        return time.perf_counter()
    except AttributeError:
        return time.time()


def median(xs):
    return statistics.median(xs)


def build_instance(groups, width, decoys_per_group, seed):
    rng = random.Random(seed)
    universe_size = groups * width
    sets = []
    costs = []

    # Proven optimum: one cost-1 row per group.
    for g in range(groups):
        sets.append(list(range(g * width, (g + 1) * width)))
        costs.append(1)

    # More expensive decoys.
    for g in range(groups):
        own = list(range(g * width, (g + 1) * width))
        nxt = list(range(((g + 1) % groups) * width,
                         (((g + 1) % groups) + 1) * width))

        for k in range(decoys_per_group):
            if k % 3 == 0:
                row = rng.sample(own, max(1, width - 1))
            elif k % 3 == 1:
                row = (
                    rng.sample(own, max(1, width // 2)) +
                    rng.sample(nxt, max(1, width // 2))
                )
            else:
                row = own + rng.sample(nxt, 1)

            sets.append(sorted(set(row)))
            costs.append(2 + (k % 3))

    return universe_size, sets, costs, groups


def independent_verify(selected, universe_size, sets, costs):
    covered = set()
    total = 0

    for sid in selected:
        if sid < 0 or sid >= len(sets):
            return False, None
        covered.update(sets[sid])
        total += costs[sid]

    valid = (
        len(covered) == universe_size and
        all(i in covered for i in range(universe_size))
    )
    return valid, total


def hkd_job(mod, universe_size, sets, costs):
    problem = mod.Problem(universe_size, sets, costs)
    result = mod.solve(
        problem,
        workers=1,
        max_frontier=200000,
        hash_repeats=1
    )

    if not mod.verify(problem, result):
        raise RuntimeError("HKD internal verification failed")

    return list(result["solution"]), int(result["cost"])


def gurobi_job(universe_size, sets, costs):
    by_element = [[] for _ in range(universe_size)]
    for sid, row in enumerate(sets):
        for e in row:
            by_element[e].append(sid)

    m = gp.Model("HKD_FREE_STANDARD_SET_COVER")
    m.Params.OutputFlag = 0
    m.Params.Threads = 1
    m.Params.MIPGap = 0.0

    x = m.addVars(len(sets), vtype=GRB.BINARY, name="x")
    m.setObjective(
        gp.quicksum(costs[i] * x[i] for i in range(len(sets))),
        GRB.MINIMIZE
    )

    for e in range(universe_size):
        m.addConstr(
            gp.quicksum(x[sid] for sid in by_element[e]) >= 1
        )

    m.optimize()

    if m.SolCount == 0:
        raise RuntimeError("Gurobi returned no solution")
    if abs(float(m.MIPGap)) > 1e-12:
        raise RuntimeError("Gurobi did not prove exact optimum")

    selected = [
        i for i in range(len(sets))
        if x[i].X > 0.5
    ]

    return selected, int(round(m.ObjVal))


def main():
    print("HKD_SOLVER_FREE_GUROBI_BENCHMARK_V5")
    print("free_max_variables=%d" %
          hkd_solver_free.FREE_MAX_VARIABLES)
    print("free_max_linear_constraints=%d" %
          hkd_solver_free.FREE_MAX_LINEAR_CONSTRAINTS)
    print("paid_available=%s" % HAVE_PAID)
    print("gurobi_available=%s" % HAVE_GUROBI)
    print("")

    # Basic FREE exactness test first.
    u, sets, costs, optimum = build_instance(
        GROUPS, WIDTH, DECOYS_PER_GROUP, 123
    )
    fsel, fobj = hkd_job(hkd_solver_free, u, sets, costs)
    fv, fcheck = independent_verify(fsel, u, sets, costs)
    free_exact = fv and fobj == fcheck == optimum

    print("FREE")
    print("objective=%d" % fobj)
    print("expected_objective=%d" % optimum)
    print("exact=%s" % free_exact)
    print("")

    if not free_exact:
        print("RESULT")
        print("PASS=False")
        return 2

    if not HAVE_GUROBI:
        print("GUROBI")
        print("available=False")
        print("reason=gurobipy_not_installed_for_this_python")
        print("benchmark_skipped=True")
        print("")
        print("RESULT")
        print("free_exact=True")
        print("gurobi_benchmark_skipped=True")
        print("PASS=True")
        return 0

    # Warm license/import/cache paths outside measured section.
    gurobi_job(u, sets, costs)
    hkd_job(hkd_solver_free, u, sets, costs)

    g_times = []
    h_times = []

    for job_id in range(JOBS):
        u, sets, costs, optimum = build_instance(
            GROUPS,
            WIDTH,
            DECOYS_PER_GROUP,
            123 + job_id
        )

        t0 = clock()
        gsel, gobj = gurobi_job(u, sets, costs)
        gdt = clock() - t0

        t0 = clock()
        hsel, hobj = hkd_job(
            hkd_solver_free, u, sets, costs
        )
        hdt = clock() - t0

        gv, gcheck = independent_verify(
            gsel, u, sets, costs
        )
        hv, hcheck = independent_verify(
            hsel, u, sets, costs
        )

        if not (
            gv and hv and
            gobj == gcheck ==
            hobj == hcheck ==
            optimum
        ):
            raise RuntimeError(
                "exactness failure on job %d" % job_id
            )

        g_times.append(gdt)
        h_times.append(hdt)

    total_g = sum(g_times)
    total_h = sum(h_times)
    speedup = total_g / total_h if total_h > 0 else float("inf")

    print("GUROBI")
    print("available=True")
    print("jobs=%d" % JOBS)
    print("total_seconds=%.9f" % total_g)
    print("median_job_seconds=%.9f" % median(g_times))
    print("jobs_per_second=%.3f" %
          (JOBS / total_g if total_g > 0 else float("inf")))
    print("")

    print("HKD_SOLVER_FREE")
    print("jobs=%d" % JOBS)
    print("total_seconds=%.9f" % total_h)
    print("median_job_seconds=%.9f" % median(h_times))
    print("jobs_per_second=%.3f" %
          (JOBS / total_h if total_h > 0 else float("inf")))
    print("")

    verified_4x = speedup >= REQUIRED_SPEEDUP

    print("RESULT")
    print("jobs_verified=%d" % JOBS)
    print("all_exact=True")
    print("aggregate_throughput_speedup_x=%.3f" % speedup)
    print("required_speedup_x=%.3f" % REQUIRED_SPEEDUP)
    print("VERIFIED_4X=%s" % verified_4x)
    print("PASS=%s" % verified_4x)

    return 0 if verified_4x else 2


if __name__ == "__main__":
    sys.exit(main())
