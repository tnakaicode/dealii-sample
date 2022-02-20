---
title: dealii example step-56
---

Tesnor Example

<https://www.dealii.org/current/doxygen/deal.II/step_56.html>

```bash
Now running with Multigrid
Refinement cycle 0
   Set-up...
        Number of active cells: 512
        Number of degrees of freedom: 15468 (14739+729)
   Assembling...
   Assembling Multigrid...
   Solving...
        Number of FGMRES iterations: 21
        Total number of iterations used for approximation of A inverse: 67
        Total number of iterations used for approximation of S inverse: 22

   Note: The mean value was adjusted by -1.28101e-14

   Velocity L2 Error: 0.000670888
   Pressure L2 Error: 0.0036533
   Velocity H1 Error: 0.0414704
   VM Peak: 0


+---------------------------------------------+------------+------------+
| Total wallclock time elapsed since start    |       172s |            |
|                                             |            |            |
| Section                         | no. calls |  wall time | % of total |
+---------------------------------+-----------+------------+------------+
| (Multigrid specific)            |         3 |      14.3s |       8.3% |
| Assemble                        |         1 |        15s |       8.7% |
| Assemble Multigrid              |         1 |      10.7s |       6.2% |
| Setup                           |         1 |      4.13s |       2.4% |
| Setup - Multigrid               |         1 |      2.79s |       1.6% |
| Solve                           |         1 |       138s |        80% |
| Solve - FGMRES                  |         1 |       137s |        80% |
| Solve - Set-up Preconditioner   |         1 |     0.848s |      0.49% |
+---------------------------------+-----------+------------+------------+

Refinement cycle 1
...
Refinement cycle 3
   Set-up...
        Number of active cells: 262144
        Number of degrees of freedom: 6714692 (6440067+274625)
Segmentation fault (core dumped)
```
