#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import sys

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


def build_large():
    n = 2001
    sets = []
    costs = []
    # 667 disjoint 3-leg duties, exact planted cover.
    for i in range(667):
        sets.append([3*i, 3*i+1, 3*i+2])
        costs.append(1)
    # Expensive duplicate/subset duties to exceed 2000 variables.
    i = 0
    while len(sets) < 2101:
        g = i % 667
        sets.append([3*g, 3*g+1])
        costs.append(20 + (i % 7))
        i += 1
    return n, sets, costs


def main():
    n, sets, costs = build_large()
    print("HKD_SOLVER_LARGE_PORTABLE_TEST")
    print("problem=AVIATION_CREW_DUTY_COVER")
    print("flight_leg_constraints=%d" % n)
    print("candidate_duty_variables=%d" % len(sets))
    print("paid_available=%s" % HAVE_PAID)
    print("")

    free_triggered = False
    try:
        p = hkd_solver_free.Problem(n, sets, costs)
        hkd_solver_free.solve(p)
    except RuntimeError as e:
        free_triggered = "model too large" in str(e).lower()
        print("FREE")
        print("status=LIMIT_TRIGGERED")
        print("message=%s" % e)
        print("free_limit_triggered=%s" % free_triggered)

    paid_exact = None
    if HAVE_PAID:
        p = hkd_solver_paid.Problem(n, sets, costs)
        r = hkd_solver_paid.solve(
            p, workers=1, max_frontier=200000, hash_repeats=1)
        paid_exact = hkd_solver_paid.verify(p, r) and int(r["cost"]) == 667
        print("")
        print("PAID")
        print("objective=%s" % r["cost"])
        print("expected_objective=667")
        print("exact=%s" % paid_exact)
    else:
        print("")
        print("PAID")
        print("available=False")
        print("reason=hkd_solver_paid_not_installed")
        print("large_paid_test_skipped=True")

    passed = free_triggered and (paid_exact is None or paid_exact)
    print("")
    print("RESULT")
    print("free_limit_triggered=%s" % free_triggered)
    print("paid_test_skipped=%s" % (not HAVE_PAID))
    print("PASS=%s" % passed)
    return 0 if passed else 2


if __name__ == "__main__":
    sys.exit(main())
