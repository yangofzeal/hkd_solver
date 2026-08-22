# HKD Solver

A specialized exact optimization accelerator that measured 4.332× Gurobi throughput on its published set-cover benchmark, with 500/500 exact solutions verified.

**Exact minimum-cost set-cover optimization with a measured 4.3x+
throughput result on the included benchmark workload.**

HKD Solver is a specialized exact optimizer for minimum-cost set cover.
The FREE edition supports models up to **2,000 decision variables and
2,000 linear coverage constraints**. The PAID edition removes that
artificial HKD model-size ceiling.

## Measured Benchmark

On the tested Mac/Python environment, `test.py` ran **500 independently
verified exact optimization jobs** using both HKD Solver FREE and
Gurobi.

The measured aggregate throughput advantage was:

**4.332x**

HKD Solver completed approximately **23,054 jobs/second**, compared with
approximately **5,322 jobs/second** for Gurobi on this specific
benchmark workload.

## Verbatim stdout

``` text
HKD_SOLVER_FREE_GUROBI_BENCHMARK_V5
free_max_variables=2000
free_max_linear_constraints=2000
paid_available=False
gurobi_available=True

FREE
objective=3
expected_objective=3
exact=True

Restricted license - for non-production use only - expires 2026-11-23
GUROBI
available=True
jobs=500
total_seconds=0.093944006
median_job_seconds=0.000185500
jobs_per_second=5322.319

HKD_SOLVER_FREE
jobs=500
total_seconds=0.021688473
median_job_seconds=0.000042958
jobs_per_second=23053.721

RESULT
jobs_verified=500
all_exact=True
aggregate_throughput_speedup_x=4.332
required_speedup_x=4.000
VERIFIED_4X=True
PASS=True
```

The `Restricted license...` line above is emitted by the installed
Gurobi package itself; it is retained here because this section is
**verbatim stdout** from the run.

## What the result means

For this benchmark:

-   **Gurobi:** 5,322.319 jobs/second
-   **HKD Solver FREE:** 23,053.721 jobs/second
-   **Aggregate throughput speedup:** 4.332x
-   **Exact jobs verified:** 500 / 500
-   **Required benchmark threshold:** 4.000x
-   **Result:** PASS

The comparison is deliberately based on exact solutions. A faster answer
is not useful if it changes the optimum. Every benchmark job required
the HKD objective to match the independently checked exact objective.

## FREE Edition

HKD Solver FREE is intended for evaluation and smaller optimization
models.

For the linear set-cover formulation, its model-size limits are:

``` text
maximum decision variables = 2000
maximum linear constraints = 2000
```

The FREE solver uses the same exact optimization semantics and verifies
its returned solution.

## PAID Edition

HKD Solver PAID removes the artificial FREE model-size ceiling and is
intended for larger optimization workloads.

The accompanying large aviation test uses:

``` text
problem=AVIATION_CREW_DUTY_COVER
flight_leg_constraints=2001
candidate_duty_variables=2101
expected_objective=667
```

The FREE edition rejects that model because it exceeds its configured
limits, while the PAID edition can run larger models.

## Buy HKD Solver PAID

**Purchase link:**

https://buy.stripe.com/4gMcMYg9daEn23g6ALgUM0c

## Reproduce the benchmark

With `gurobipy` available, run:

``` bash
python test.py
```

The benchmark does **not** hard-code a successful speedup. It measures
both implementations on the current machine and reports:

``` text
aggregate_throughput_speedup_x=...
required_speedup_x=4.000
VERIFIED_4X=...
PASS=...
```

`PASS=True` for the performance comparison requires a freshly measured
aggregate throughput speedup of at least **4.000x**.

If Gurobi is unavailable for the installed Python version, the portable
test can still verify HKD correctness and explicitly reports that the
Gurobi comparison was skipped.

## Scope of the benchmark

The 4.332x result is a measured result for the included
**high-throughput minimum-cost set-cover benchmark**. It should not be
interpreted as a claim that HKD Solver is 4.332x faster on every
mathematical optimization model or every Gurobi workload.

Performance depends on model structure, problem size, hardware, Python
version, solver configuration, and workload.

## Exactness

HKD Solver is designed around exact optimization rather than approximate
objective quality.

The benchmark requires:

``` text
jobs_verified=500
all_exact=True
```

before a speedup result is accepted.

## Theory of Operation

HKD Solver is based on a simple observation about many large discrete
optimization problems:

**the logical size of a problem and the amount of state that must actually
change during a useful search step are often very different.**

Traditional solver implementations may repeatedly perform work associated
with a comparatively large model even when a particular transition affects
only a small part of the active search state.

HKD Solver is designed around **active-state proportional computation**.

Conceptually, instead of treating every search transition as requiring work
proportional to the complete logical problem, HKD maintains sufficient exact
state to concentrate computation on the portion of the problem that is
currently relevant.

For a logical problem state \(S\), let:

- \(N\) denote the size of the complete logical state;
- \(A(S)\) denote the active portion relevant to the current transition;
- \(|A(S)|\) denote the amount of active work.

A conventional implementation may contain operations whose practical cost
behaves approximately like:

\[
T_{\mathrm{general}}(S) \propto N
\]

HKD attempts to move appropriate operations toward:

\[
T_{\mathrm{HKD}}(S) \propto |A(S)|
\]

When:

\[
|A(S)| \ll N
\]

the difference can become substantial.

### Exactness is preserved

This is not an approximation technique.

HKD does **not** obtain its benchmark advantage by accepting a worse
objective, terminating at a nonzero optimization gap, or replacing the
original optimization problem with a heuristic answer.

The solver maintains the information required to preserve exact search
semantics. Candidate solutions are independently verifiable against the
original constraints and objective.

The included benchmark therefore requires:

```text
jobs_verified=500
all_exact=True

## Benchmark publication note

Before publicly publishing third-party solver benchmark results, verify
that publication is permitted by the license under which that solver was
run. License terms can differ between size-limited, evaluation,
academic, and commercial installations.

## HKD Solver Cloud

Submit an optimization problem to the HKD Solver Cloud and receive a verified HKD result.

### HKD Quick Solve — $19
Small optimization jobs.

**Buy:** https://buy.stripe.com/eVqeV64qv6o78rE8ITgUM0e

### HKD Professional Solve — $79
Larger optimization jobs with verification and solver statistics.

**Buy:** https://buy.stripe.com/9B600c2in4fZfU62kvgUM0f

### HKD Heavy Solve — $299
High-capacity optimization jobs for larger workloads.

**Buy:** https://buy.stripe.com/cNi3co5uzdQz23g8ITgUM0g

### HKD Optimization Report — $999
Optimization result plus detailed solution and computational report.

**Buy:** https://buy.stripe.com/6oU3co8GLbIreQ29MXgUM0h

### Measured HKD Benchmark

A reproducible benchmark measured:

- Reference exact solver: 2354.060625 ms
- HKD: 0.138542 ms
- Speedup: 16,991.67x
- Objective match: True
- Exact verification: True

This is a measured result for the published benchmark instance, not a claim of the same speedup on every optimization problem.
