---
title: dealii example step-33
---

<https://www.dealii.org/current/doxygen/deal.II/step_33.html#Intro>

```bash
CMake Error at CMakeLists.txt:44 (MESSAGE):
  

  Error! This tutorial requires a deal.II library that was configured with
  the following options:

      DEAL_II_WITH_MUPARSER = ON
      DEAL_II_TRILINOS_WITH_SACADO = ON

  However, the deal.II library found at /usr/local was configured with these
  options

      DEAL_II_WITH_MUPARSER = ON
      DEAL_II_TRILINOS_WITH_SACADO =

  which conflict with the requirements.


-- Configuring incomplete, errors occurred!
```

```bash
cmake -DDEAL_II_TRILINOS_WITH_SACADO=ON .
make

fatal error: Sacado.hpp: No such file or directory
   70 | #include <Sacado.hpp>
      |          ^~~~~~~~~~~~
compilation terminated.
make[2]: *** [CMakeFiles/step-33.dir/build.make:63: CMakeFiles/step-33.dir/step-33.cc.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:137: CMakeFiles/step-33.dir/all] Error 2
make: *** [Makefile:84: all] Error 2

```

```bash
wsl -e cmake . | wsl -e make | wsl -e ./step-33 input.prm

----------------------------------------------------
Exception on processing:

--------------------------------------------------------
An error occurred in line <2485> of file </mnt/e/nakai/Daily/python-code/dealii-33/step-33.cc> in function
    void Step33::ConservationLaw<dim>::run() [with int dim = 2]
The violated condition was:
    nonlin_iter <= 10
Additional information:
    No convergence in nonlinear solver
--------------------------------------------------------

Aborting!
----------------------------------------------------
```
