---
title: dealii example step-67 High-order discontinuous Galerkin for the exa-scale
---

<https://www.dealii.org/current/doxygen/deal.II/step_67.html>

```bash
Running with 1 MPI processes
Vectorization over 2 doubles = 128 bits (SSE2)
Number of degrees of freedom: 147456 ( = 4 [vars] x 1024 [cells] x 36 [dofs/cell/var] )
Time step size: 0.00689325, minimal h: 0.3125, initial transport scaling: 0.102759

Time:       0, dt:   0.0069, error rho:   2.76e-07, rho * u:  1.259e-06, energy: 2.987e-06
Time:    1.01, dt:   0.0069, error rho:   1.37e-06, rho * u:  2.252e-06, energy: 4.153e-06
...
Time:      10, dt:   0.0096, error rho:  7.231e-07, rho * u:  2.666e-07, energy: 2.074e-06

+-------------------------------------------+------------------+------------+------------------+
| Total wallclock time elapsed              |     688.4s     0 |     688.4s |     688.4s     0 |
|                                           |                  |                               |
| Section                       | no. calls |   min time  rank |   avg time |   max time  rank |
+-------------------------------------------+------------------+------------+------------------+
| compute errors                |        11 |    0.3828s     0 |    0.3828s |    0.3828s     0 |
| compute transport speed       |       258 |     10.29s     0 |     10.29s |     10.29s     0 |
| output                        |        11 |     39.25s     0 |     39.25s |     39.25s     0 |
| rk time stepping total        |      1283 |     638.1s     0 |     638.1s |     638.1s     0 |
| rk_stage - integrals L_h      |      6415 |     398.7s     0 |     398.7s |     398.7s     0 |
| rk_stage - inv mass + vec upd |      6415 |     239.2s     0 |     239.2s |     239.2s     0 |
+-------------------------------------------+------------------+------------+------------------+
```
