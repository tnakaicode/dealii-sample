---
title: dealii example
---

```bash
git clone https://github.com/dealii/dealii.git
cd dealii
mkdir build

# build
cmake -DDEAL_II_WITH_PETSC=OFF -DDEAL_II_PETSC_WITH_COMPLEX=OFF -DDEAL_II_WITH_P4EST=OFF -DDEAL_II_WITH_TRILINOS=OFF -DDEAL_II_TRILINOS_WITH_SACADO=OFF -DDEAL_II_COMPONENT_DOCUMENTATION=ON ..

###
#
#  deal.II configuration:
#        CMAKE_BUILD_TYPE:       DebugRelease
#        BUILD_SHARED_LIBS:      ON
#        CMAKE_INSTALL_PREFIX:   /usr/local
#        CMAKE_SOURCE_DIR:       /mnt/e/ubuntu2004/dealii
#                                (version 9.3.0-pre, shortrev 4abc4a1666)
#        CMAKE_BINARY_DIR:       /mnt/e/ubuntu2004/dealii/build
#        CMAKE_CXX_COMPILER:     GNU 9.3.0 on platform Linux x86_64
#                                /usr/bin/c++
#        CMAKE_C_COMPILER:       /usr/bin/cc
#        CMAKE_Fortran_COMPILER: /usr/bin/gfortran
#        CMAKE_GENERATOR:        Unix Makefiles
#
#  Base configuration (prior to feature configuration):
#        DEAL_II_CXX_FLAGS:            -pedantic -fPIC -Wall -Wextra -Woverloaded-virtual -Wpointer-arith -Wsign-compare -Wsuggest-override -Wswitch -Wsynth -Wwrite-strings -Wno-placement-new -Wno-deprecated-declarations -Wno-literal-suffix -Wno-psabi -Wno-class-memaccess -fopenmp-simd
#        DEAL_II_CXX_FLAGS_RELEASE:    -O2 -funroll-loops -funroll-all-loops -fstrict-aliasing -Wno-unused-local-typedefs
#        DEAL_II_CXX_FLAGS_DEBUG:      -O0 -ggdb -Wa,--compress-debug-sections
#        DEAL_II_LINKER_FLAGS:         -Wl,--as-needed -rdynamic -fuse-ld=gold -lpthread
#        DEAL_II_LINKER_FLAGS_RELEASE:
#        DEAL_II_LINKER_FLAGS_DEBUG:   -ggdb
#        DEAL_II_DEFINITIONS:
#        DEAL_II_DEFINITIONS_RELEASE:  
#        DEAL_II_DEFINITIONS_DEBUG:    DEBUG
#        DEAL_II_USER_DEFINITIONS:
#        DEAL_II_USER_DEFINITIONS_REL:
#        DEAL_II_USER_DEFINITIONS_DEB: DEBUG
#        DEAL_II_INCLUDE_DIRS
#        DEAL_II_USER_INCLUDE_DIRS:
#        DEAL_II_BUNDLED_INCLUDE_DIRS:
#        DEAL_II_LIBRARIES:
#        DEAL_II_LIBRARIES_RELEASE:
#        DEAL_II_LIBRARIES_DEBUG:
#        DEAL_II_VECTORIZATION_WIDTH_IN_BITS: 128
#        DEAL_II_HAVE_CXX14
#
#  Configured Features (DEAL_II_ALLOW_BUNDLED = ON, DEAL_II_ALLOW_AUTODETECTION = ON):
#      ( DEAL_II_WITH_64BIT_INDICES = OFF )
#      ( DEAL_II_WITH_ADOLC = OFF )
#      ( DEAL_II_WITH_ARPACK = OFF )
#      ( DEAL_II_WITH_ASSIMP = OFF )
#        DEAL_II_WITH_BOOST set up with external dependencies
#            BOOST_VERSION = 1.71.0
#            BOOST_CXX_FLAGS = -Wno-unused-local-typedefs
#            BOOST_DEFINITIONS = BOOST_NO_AUTO_PTR
#            BOOST_USER_DEFINITIONS = BOOST_NO_AUTO_PTR
#            BOOST_INCLUDE_DIRS = /usr/include
#            BOOST_USER_INCLUDE_DIRS = /usr/include
#            BOOST_LIBRARIES = /usr/lib/x86_64-linux-gnu/libboost_iostreams.so;/usr/lib/x86_64-linux-gnu/libboost_serialization.so;/usr/lib/x86_64-linux-gnu/libboost_system.so;/usr/lib/x86_64-linux-gnu/libboost_thread.so;/usr/lib/x86_64-linux-gnu/libboost_regex.so;/usr/lib/x86_64-linux-gnu/libboost_chrono.so;/usr/lib/x86_64-linux-gnu/libboost_date_time.so;/usr/lib/x86_64-linux-gnu/libboost_atomic.so
#        DEAL_II_WITH_COMPLEX_VALUES = ON
#      ( DEAL_II_WITH_CUDA = OFF )
#      ( DEAL_II_WITH_GINKGO = OFF )
#        DEAL_II_WITH_GMSH set up with external dependencies
#            GMSH_EXE = /usr/bin/gmsh
#      ( DEAL_II_WITH_GSL = OFF )
#      ( DEAL_II_WITH_HDF5 = OFF )
#        DEAL_II_WITH_LAPACK set up with external dependencies
#            LAPACK_WITH_64BIT_BLAS_INDICES = OFF
#            LAPACK_LINKER_FLAGS =
#            LAPACK_INCLUDE_DIRS =
#            LAPACK_USER_INCLUDE_DIRS =
#            LAPACK_LIBRARIES = /usr/lib/x86_64-linux-gnu/libopenblas.so;gfortran;quadmath;m;gcc_s;gcc
#      ( DEAL_II_WITH_METIS = OFF )
#      ( DEAL_II_WITH_MPI = OFF )
#        DEAL_II_WITH_MUPARSER set up with bundled packages
#            MUPARSER_BUNDLED_INCLUDE_DIRS = /mnt/e/ubuntu2004/dealii/bundled/muparser_v2_2_4//include
#        DEAL_II_WITH_OPENCASCADE set up with external dependencies
#            OPENCASCADE_VERSION = 6.9.1
#            OPENCASCADE_INCLUDE_DIRS = /usr/include/oce
#            OPENCASCADE_USER_INCLUDE_DIRS = /usr/include/oce
#            OPENCASCADE_LIBRARIES = /usr/lib/x86_64-linux-gnu/libTKBO.so;/usr/lib/x86_64-linux-gnu/libTKBool.so;/usr/lib/x86_64-linux-gnu/libTKBRep.so;/usr/lib/x86_64-linux-gnu/libTKernel.so;/usr/lib/x86_64-linux-gnu/libTKFeat.so;/usr/lib/x86_64-linux-gnu/libTKFillet.so;/usr/lib/x86_64-linux-gnu/libTKG2d.so;/usr/lib/x86_64-linux-gnu/libTKG3d.so;/usr/lib/x86_64-linux-gnu/libTKGeomAlgo.so;/usr/lib/x86_64-linux-gnu/libTKGeomBase.so;/usr/lib/x86_64-linux-gnu/libTKHLR.so;/usr/lib/x86_64-linux-gnu/libTKIGES.so;/usr/lib/x86_64-linux-gnu/libTKMath.so;/usr/lib/x86_64-linux-gnu/libTKMesh.so;/usr/lib/x86_64-linux-gnu/libTKOffset.so;/usr/lib/x86_64-linux-gnu/libTKPrim.so;/usr/lib/x86_64-linux-gnu/libTKShHealing.so;/usr/lib/x86_64-linux-gnu/libTKSTEP.so;/usr/lib/x86_64-linux-gnu/libTKSTEPAttr.so;/usr/lib/x86_64-linux-gnu/libTKSTEPBase.so;/usr/lib/x86_64-linux-gnu/libTKSTEP209.so;/usr/lib/x86_64-linux-gnu/libTKSTL.so;/usr/lib/x86_64-linux-gnu/libTKTopAlgo.so;/usr/lib/x86_64-linux-gnu/libTKXSBase.so
#      ( DEAL_II_WITH_P4EST = OFF )
#      ( DEAL_II_WITH_PETSC = OFF )
#      ( DEAL_II_WITH_SCALAPACK = OFF )
#      ( DEAL_II_WITH_SIMPLEX_SUPPORT = OFF )
#      ( DEAL_II_WITH_SLEPC = OFF )
#      ( DEAL_II_WITH_SUNDIALS = OFF )
#      ( DEAL_II_WITH_SYMENGINE = OFF )
#        DEAL_II_WITH_TASKFLOW set up with bundled packages
#            TASKFLOW_BUNDLED_INCLUDE_DIRS = /mnt/e/ubuntu2004/dealii/bundled/taskflow-2.5.0/include
#        DEAL_II_WITH_TBB set up with external dependencies
#            TBB_VERSION = 2020.1
#            TBB_INCLUDE_DIRS = /usr/include
#            TBB_USER_INCLUDE_DIRS = /usr/include
#            TBB_LIBRARIES = /usr/lib/x86_64-linux-gnu/libtbb.so
#      ( DEAL_II_WITH_TRILINOS = OFF )
#        DEAL_II_WITH_UMFPACK set up with external dependencies
#            UMFPACK_VERSION = 5.7.8
#            UMFPACK_LINKER_FLAGS =
#            UMFPACK_INCLUDE_DIRS = /usr/include/suitesparse
#            UMFPACK_USER_INCLUDE_DIRS = /usr/include/suitesparse
#            UMFPACK_LIBRARIES = /usr/lib/x86_64-linux-gnu/libumfpack.so;/usr/lib/x86_64-linux-gnu/libcholmod.so;/usr/lib/x86_64-linux-gnu/libccolamd.so;/usr/lib/x86_64-linux-gnu/libcolamd.so;/usr/lib/x86_64-linux-gnu/libcamd.so;/usr/lib/x86_64-linux-gnu/libsuitesparseconfig.so;/usr/lib/x86_64-linux-gnu/libamd.so;/usr/lib/x86_64-linux-gnu/libopenblas.so;gfortran;quadmath;m;gcc_s;gcc;rt
#        DEAL_II_WITH_ZLIB set up with external dependencies
#            ZLIB_VERSION = 1.2.11
#            ZLIB_INCLUDE_DIRS = /usr/include
#            ZLIB_LIBRARIES = /usr/lib/x86_64-linux-gnu/libz.so
#
#  Component configuration:
#        DEAL_II_COMPONENT_DOCUMENTATION
#        DEAL_II_COMPONENT_EXAMPLES
#      ( DEAL_II_COMPONENT_PACKAGE = OFF )
#      ( DEAL_II_COMPONENT_PYTHON_BINDINGS = OFF )
#
###
```

Error

```bash
[  0%] Building code-gallery.h
[  0%] Built target build_code-gallery_h
[  0%] Built target code-gallery
[  0%] Built target obj_sundials_inst
[  0%] Generating data_out_faces.inst
Invalid instantiation list: missing 'for'
make[2]: *** [source/numerics/CMakeFiles/obj_numerics_inst.dir/build.make:115: source/numerics/data_out_faces.inst] Error 1
make[1]: *** [CMakeFiles/Makefile2:4244:
make: *** [Makefile:118: all] Error 2

# error
cd /mnt/e/ubuntu2004/dealii/build/source/numerics && ../../bin/expand_instantiations /mnt/e/ubuntu2004/dealii/build/share/deal.II/template-arguments < /mnt/e/ubuntu2004/dealii/source/numerics/data_out_faces.inst.in

// This file is automatically generated from corresponding .inst.in, do not edit.

#ifdef SPLIT_INSTANTIATIONS_COUNT
  #define SPLIT_INSTANTIATIONS_CHECK(C) (((C) % SPLIT_INSTANTIATIONS_COUNT) == SPLIT_INSTANTIATIONS_INDEX)
#else
  #define SPLIT_INSTANTIATIONS_CHECK(C) (1)
#endif

Invalid instantiation list: missing 'for'

# non error
cd /mnt/e/ubuntu2004/dealii/build/source/numerics && ../../bin/expand_instantiations /mnt/e/ubuntu2004/dealii/build/share/deal.II/template-arguments < /mnt/e/ubuntu2004/dealii/source/numerics/data_out_dof_data_codim.inst.in
```

/mnt/e/ubuntu2004/dealii/source/numerics/data_out_faces.inst.in

```c++
for (deal_II_dimension : DIMENSIONS)
  {
    // don't instantiate anything for the 1d
#if deal_II_dimension >= 2
    template class DataOutFaces<deal_II_dimension,
                                DoFHandler<deal_II_dimension>>;
#endif
  }

```

/mnt/e/ubuntu2004/dealii/source/numerics/data_out_dof_data_codim.inst.in

```c++
for (VEC : REAL_VECTOR_TYPES; DH : DOFHANDLER_TEMPLATES;
     deal_II_dimension : DIMENSIONS;
     deal_II_space_dimension : DIMENSIONS)
    {
      ...
    }
```

```bash
git clone https://github.com/dealii/dealii.git dealii-win
cd dealii-win
mkdir build

# build
cmake -DDEAL_II_WITH_PETSC=OFF -DDEAL_II_PETSC_WITH_COMPLEX=OFF -DDEAL_II_WITH_P4EST=OFF -DDEAL_II_WITH_TRILINOS=OFF -DDEAL_II_TRILINOS_WITH_SACADO=OFF -DDEAL_II_COMPONENT_DOCUMENTATION=OFF ..

###
#
#  deal.II configuration:
#        CMAKE_BUILD_TYPE:       DebugRelease
#        BUILD_SHARED_LIBS:      OFF
#        CMAKE_INSTALL_PREFIX:   C:/Program Files (x86)/deal.II
#        CMAKE_SOURCE_DIR:       E:/nakai/dealii-win
#                                (version 9.3.0-pre, shortrev abbbcf2cde)
#        CMAKE_BINARY_DIR:       E:/nakai/dealii-win/build
#        CMAKE_CXX_COMPILER:     MSVC 19.26.28806.0 on platform Windows AMD64
#                                C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/VC/Tools/MSVC/14.26.28801/bin/Hostx64/x64/cl.exe
#        CMAKE_C_COMPILER:       C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/VC/Tools/MSVC/14.26.28801/bin/Hostx64/x64/cl.exe
#        CMAKE_GENERATOR:        Visual Studio 16 2019
#
#  Base configuration (prior to feature configuration):
#        DEAL_II_CXX_FLAGS:            /EHsc /bigobj /W3 /wd4068 /wd4244 /wd4267 /wd4996 /wd4355 /wd4800 /wd4146 /wd4667 /wd4520 /wd4700 /wd4789 /wd4808 /wd5037
#        DEAL_II_CXX_FLAGS_RELEASE:    /O2
#        DEAL_II_CXX_FLAGS_DEBUG:      /Zi /MDd /Od
#        DEAL_II_LINKER_FLAGS:
#        DEAL_II_LINKER_FLAGS_RELEASE:
#        DEAL_II_LINKER_FLAGS_DEBUG:
#        DEAL_II_DEFINITIONS:          NOMINMAX
#        DEAL_II_DEFINITIONS_RELEASE:  
#        DEAL_II_DEFINITIONS_DEBUG:    DEBUG
#        DEAL_II_USER_DEFINITIONS:     NOMINMAX
#        DEAL_II_USER_DEFINITIONS_REL:
#        DEAL_II_USER_DEFINITIONS_DEB: DEBUG
#        DEAL_II_INCLUDE_DIRS
#        DEAL_II_USER_INCLUDE_DIRS:
#        DEAL_II_BUNDLED_INCLUDE_DIRS:
#        DEAL_II_LIBRARIES:
#        DEAL_II_LIBRARIES_RELEASE:
#        DEAL_II_LIBRARIES_DEBUG:
#        DEAL_II_VECTORIZATION_WIDTH_IN_BITS: 0
#        DEAL_II_HAVE_CXX14
#
#  Configured Features (DEAL_II_ALLOW_BUNDLED = ON, DEAL_II_ALLOW_AUTODETECTION = ON):
#      ( DEAL_II_WITH_64BIT_INDICES = OFF )
#      ( DEAL_II_WITH_ADOLC = OFF )
#      ( DEAL_II_WITH_ARPACK = OFF )
#      ( DEAL_II_WITH_ASSIMP = OFF )
#        DEAL_II_WITH_BOOST set up with bundled packages
#            BOOST_DEFINITIONS = BOOST_ALL_NO_LIB
#            BOOST_USER_DEFINITIONS = BOOST_ALL_NO_LIB
#            BOOST_BUNDLED_INCLUDE_DIRS = E:/nakai/dealii-win/bundled/boost-1.70.0/include
#        DEAL_II_WITH_COMPLEX_VALUES = ON
#      ( DEAL_II_WITH_CUDA = OFF )
#      ( DEAL_II_WITH_GINKGO = OFF )
#      ( DEAL_II_WITH_GMSH = OFF )
#      ( DEAL_II_WITH_GSL = OFF )
#        DEAL_II_WITH_HDF5 set up with external dependencies
#            HDF5_INCLUDE_DIRS = E:/nakai/anaconda3/Library/include
#            HDF5_USER_INCLUDE_DIRS = E:/nakai/anaconda3/Library/include
#            HDF5_LIBRARIES = E:/nakai/anaconda3/Library/lib/hdf5_hl.lib;E:/nakai/anaconda3/Library/lib/hdf5.lib
#      ( DEAL_II_WITH_LAPACK = OFF )
#      ( DEAL_II_WITH_METIS = OFF )
#      ( DEAL_II_WITH_MPI = OFF )
#        DEAL_II_WITH_MUPARSER set up with bundled packages
#            MUPARSER_BUNDLED_INCLUDE_DIRS = E:/nakai/dealii-win/bundled/muparser_v2_2_4//include
#        DEAL_II_WITH_OPENCASCADE set up with external dependencies
#            OPENCASCADE_VERSION = 7.4.0
#            OPENCASCADE_INCLUDE_DIRS = E:/nakai/anaconda3/Library/include/opencascade
#            OPENCASCADE_USER_INCLUDE_DIRS = E:/nakai/anaconda3/Library/include/opencascade
#            OPENCASCADE_LIBRARIES = E:/nakai/anaconda3/Library/lib/TKBO.lib;E:/nakai/anaconda3/Library/lib/TKBool.lib;E:/nakai/anaconda3/Library/lib/TKBRep.lib;E:/nakai/anaconda3/Library/lib/TKernel.lib;E:/nakai/anaconda3/Library/lib/TKFeat.lib;E:/nakai/anaconda3/Library/lib/TKFillet.lib;E:/nakai/anaconda3/Library/lib/TKG2d.lib;E:/nakai/anaconda3/Library/lib/TKG3d.lib;E:/nakai/anaconda3/Library/lib/TKGeomAlgo.lib;E:/nakai/anaconda3/Library/lib/TKGeomBase.lib;E:/nakai/anaconda3/Library/lib/TKHLR.lib;E:/nakai/anaconda3/Library/lib/TKIGES.lib;E:/nakai/anaconda3/Library/lib/TKMath.lib;E:/nakai/anaconda3/Library/lib/TKMesh.lib;E:/nakai/anaconda3/Library/lib/TKOffset.lib;E:/nakai/anaconda3/Library/lib/TKPrim.lib;E:/nakai/anaconda3/Library/lib/TKShHealing.lib;E:/nakai/anaconda3/Library/lib/TKSTEP.lib;E:/nakai/anaconda3/Library/lib/TKSTEPAttr.lib;E:/nakai/anaconda3/Library/lib/TKSTEPBase.lib;E:/nakai/anaconda3/Library/lib/TKSTEP209.lib;E:/nakai/anaconda3/Library/lib/TKSTL.lib;E:/nakai/anaconda3/Library/lib/TKTopAlgo.lib;E:/nakai/anaconda3/Library/lib/TKXSBase.lib
#      ( DEAL_II_WITH_P4EST = OFF )
#      ( DEAL_II_WITH_PETSC = OFF )
#      ( DEAL_II_WITH_SCALAPACK = OFF )
#      ( DEAL_II_WITH_SIMPLEX_SUPPORT = OFF )
#      ( DEAL_II_WITH_SLEPC = OFF )
#      ( DEAL_II_WITH_SUNDIALS = OFF )
#      ( DEAL_II_WITH_SYMENGINE = OFF )
#        DEAL_II_WITH_TASKFLOW set up with bundled packages
#            TASKFLOW_BUNDLED_INCLUDE_DIRS = E:/nakai/dealii-win/bundled/taskflow-2.5.0/include
#      ( DEAL_II_WITH_TBB = OFF )
#      ( DEAL_II_WITH_TRILINOS = OFF )
#      ( DEAL_II_WITH_UMFPACK = OFF )
#        DEAL_II_WITH_ZLIB set up with external dependencies
#            ZLIB_VERSION = 1.2.11
#            ZLIB_INCLUDE_DIRS = E:/nakai/anaconda3/Library/include
#            ZLIB_LIBRARIES = E:/nakai/anaconda3/Library/lib/z.lib
#
#  Component configuration:
#      ( DEAL_II_COMPONENT_DOCUMENTATION = OFF )
#        DEAL_II_COMPONENT_EXAMPLES
#      ( DEAL_II_COMPONENT_PACKAGE = OFF )
#      ( DEAL_II_COMPONENT_PYTHON_BINDINGS = OFF )
#
###

cmake --build .
```

## Step-33 Euler flow

<https://www.dealii.org/current/doxygen/deal.II/step_33.html>

The code solves the basic Euler equations of gas dynamics,
by using a fully implicit Newton iteration (inspired by Sandia's Aria code).

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

## Step-34 The incompressible motion of an inviscid fluid past a body

<https://www.dealii.org/current/doxygen/deal.II/step_34.html>

## Step-44 nonlinear kinematics

<https://www.dealii.org/current/doxygen/deal.II/step_51.html>

- quasi-static problem
- various key stress measures are introduced and the constitutive model described
- the three-field formulation in detail
  - prior to explaining the structure of the class used to manage the material
- the problem of elasticity in three dimensions.
- While the space dimension could be changed in the main() routine, care needs to be taken.
- fourth-order tensors as linear operators mapping second-order tensors (matrices) onto themselves
  - There are various fourth-order unit tensors that will be required in the forthcoming presentation.

## Step-51 Hybridizable discontinuous Galerkin methods

<https://www.dealii.org/current/doxygen/deal.II/step_51.html>

- the convection-diffusion equation.
- against the use of discontinuous Galerkin elements is the large number of globally coupled degrees of freedom
  - discontinuous elements there is one degree of freedom at each vertex for each of the adjacent elements
- the computational cost of solving such large linear systems
  - the hybridizable discontinuous Galerkin (HDG) methodology was introduced by Cockburn and co-workers
  - <https://www.sciencedirect.com/science/article/pii/S0021999112001544?via%3Dihub>
- The HDG method achieves this goal by formulating the mathematical problem
  - using Dirichlet-to-Neumann mappings
  - The partial differential equations are first written as a first order system,
  - and each field is then discretized via a DG method
  - the single-valued "trace" values on the skeleton of the mesh
  - element faces, are taken to be independent unknown quantities
- The Dirichlet-to-Neumann map
  - Use local element interior data to enforce a Neumann condition on the skeleton of the triangulation.
  - Use the known skeleton values as Dirichlet data for solving local element-level solutions

## Step-56 Stokes Problem

<https://www.dealii.org/current/doxygen/deal.II/step_56.html>

- create an efficient linear solver for the Stokes equation and compare it to alternative approaches.
  - FGMRES with geometric multigrid as a preconditioner velocity block

## Step-58 Nonlinear Schrödinger Equation (NLSE)

<https://www.dealii.org/current/doxygen/deal.II/step_58.html>

$$ \begin{aligned}
  -i \frac{\partial \phi}{\partial t} - \frac{1}{2}\Delta\phi + V\phi + \kappa|\phi|^2\phi &= 0 (\Omega \times (0,T)) \\
  \phi(x, 0) &= \phi_0(x) (\Omega) \\
  \phi(x, t) &= 0 (\partial\Omega\times(0,T))
\end{aligned} $$

- $V(x)=0$
  - to describe the propagation light in optical fiber
- $V(x)\ne0$
  - Gross-Pitaevskii-eq
  - model the time dependent behavior of Bose-Einstein condensate

## Step-61 Weak Galerkin scheme

<https://www.dealii.org/current/doxygen/deal.II/step_61.html>

Zhuoran Wang, Graham Harper, Patrick O'Leary, Jiangguo Liu, and Simon Tavener. deal.II implementation of a weak galerkin finite element solver for darcy flow. In Lecture Notes in Computer Science, pages 495–509. Springer International Publishing, 2019.

"weak Galerkin" finite element method for the Poisson equation

We would like to consider discontinuous shape functions,
but then need to address the fact that the resulting problem has a much larger number of degrees of freedom
compared to the usual continuous Galerkin method
(because, for example, each vertex carries as many degrees of freedom as there are adjacent cells).

Weak Galerkin Finite Element Methods (WGFEMs)
use discrete weak functions to approximate scalar unknowns,
and discrete weak gradients to approximate classical gradients.

## Tutorial programs grouped by topics

<https://www.dealii.org/current/doxygen/deal.II/Tutorial.html>

- Basic techniques
  - Creating a grid. A simple way to write it to a file
    - step-1
  - Degrees of freedom
    - step-2
  - Solving the Laplace equation
    - step-3
  - Dimension independent programming, non-zero data
    - step-4
  - Computing on uniformly refined meshes
    - step-5
  - Adaptivity
    - step-6, step-26
  - Evaluating errors
    - step-7
  - Nonlinear problems, Newton's method
    - step-15
- Advanced techniques
  - Multithreading
    - step-9, step-28, step-32, step-44, step-48, step-51, step-69
  - Block solvers and preconditioners
    - step-20, step-21, step-22, step-31, step-32, step-43, step-44
    - step-55, step-56, step-57, step-60, step-70
  - Using Trilinos
    - step-31, step-32, step-33, step-40, step-41, step-42, step-43
    - step-50, step-55
  - Parallelization via PETSc and MPI
    - step-17, step-18, step-40, step-50, step-55
  - Parallelization via Trilinos and MPI
    - step-32, step-40, step-42, step-50, step-55, step-70
  - Parallelization via MUMPS and MPI
    - step-62
  - Parallelization via CUDA and MPI
    - step-64
  - Parallelization on very large numbers of processors
    - step-32, step-37, step-40, step-42, step-50
    - step-55, step-59, step-67, step-69, step-70
  - Input parameter handling
    - step-28, step-29, step-32, step-33, step-34
    - step-35, step-36, step-42, step-44, step-60
    - step-62, step-69, step-70
  - Higher order mappings
    - step-10, step-11, step-32, step-60, step-65, step-67
  - Error indicators and estimators
    - step-6, step-9, step-14, step-39, step-50
  - Transferring solutions across mesh refinement
    - step-15, step-28, step-31, step-32, step-33
    - step-42, step-43, step-57, step-70
  - Discontinuous Galerkin methods
    - step-12, step-21, step-39, step-46, step-47
    - step-51, step-59, step-61, step-67
  - hp finite elements
    - step-27, step-46
  - Anisotropic refinement for DG finite element methods
    - step-30
  - Computing Jacobians from residuals, automatic differentiation
    - step-33
  - Operator splitting
    - step-21, step-31, step-32, step-58
  - Boundary element methods, curved manifolds
    - step-32, step-34, step-38, step-53, step-54, step-65
  - Periodic boundary conditions
    - step-45, step-59
  - Matrix-free methods with sum factorization
    - step-37, step-48, step-59, step-64, step-67
  - Advanced meshes and geometries
    - step-49, step-53, step-54, step-65
  - Non matching algorithms
    - step-60, step-70
  - HDF5 and Python
    - step-62
- Linear solvers
  - Conjugate Gradient solver
    - step-3
  - Preconditioned CG solver
    - step-5
  - BiCGStab
    - step-9
  - Direct solvers
    - step-29, step-44, step-47, step-46, step-58, step-62
  - Multilevel preconditioners
    - step-16, step-16b step-31, step-32, step-37, step-39
    - step-41, step-42, step-43, step-50, step-56, step-59, step-63
  - Parallel solvers
    - step-17, step-18, step-32, step-37, step-40, step-42
    - step-50, step-55, step-59
  - Block and Schur complement solvers
    - step-20, step-21, step-22, step-31, step-32, step-43
    - step-55, step-56, step-57, step-60, step-70
  - Decoupled projection solvers
    - step-35
  - Linear Newton systems from nonlinear equations
    - step-33, step-41, step-42, step-44, step-57
  - Eigenvalue solvers
    - step-36
  - Linear operators
    - step-44, step-60, step-70
- Other equations
  - Helmholtz equation
    - step-7, step-29, step-62, step-64
  - Elasticity and elasto-plasticity equations
    - step-8, step-42, step-46, step-62
  - Heat equation
    - step-26
  - Minimal surface equation
    - step-15
  - Quasi-static elasticity equations
    - step-18, step-44
  - Transport (advection) equations
    - step-9, step-21, step-31, step-32, step-43, step-51
  - The nonlinear hyperbolic Euler system of compressible gas dynamics
    - step-33, step-67, step-69
  - Mixed Laplace, Darcy, Porous media
    - step-20, step-21, step-43
  - Stokes and incompressible Navier-Stokes flow
    - step-22, step-31, step-32, step-35, step-46
    - step-55, step-56, step-57, step-70
  - The wave equation, in linear and nonlinear variants
    - step-23, step-24, step-25, step-48, step-58
  - A multigroup diffusion problem in neutron transport
    - step-28
  - Irrotational flow
    - step-34
  - An eigenspectrum problem
    - step-36
  - Fourth-order biharmonic equation
    - step-47
  - The obstacle problem, a variational inequality
    - step-41, step-42
  - The nonlinear Schrödinger equation
    - step-58
  - Coupling different equations in different parts of the domain
    - step-46
- Vector problems
  - Elasticity and elasto-plasticity equations
    - step-8, step-42
  - Mixed Laplace
    - step-20
  - Mixed Laplace plus an advection equation
    - step-21, step-43
  - Incompressible Stokes and Navier-Stokes flow
    - step-22, step-31, step-32, step-35, step-55, step-56, step-57, step-70
  - A complex-valued Helmholtz problem
    - step-29
  - The Euler equations of compressible gas dynamics
    - step-33, step-67, step-69
  - Coupling different equations in different parts of the domain
    - step-46
- Time dependent problems
  - The heat equation
    - step-26
  - Quasi-static elasticity
    - step-18, step-44
  - Porous media flow
    - step-21, step-43
  - The wave equation, in linear and nonlinear variants
    - step-23, step-24, step-25, step-48, step-58
  - Time dependent Stokes flow driven by buoyancy
    - step-31, step-32
  - The Euler equations of compressible gas dynamics
    - step-33, step-67, step-69
  - The nonlinear Schrödinger equation
    - step-58
  - Time dependent neutron diffusion equation
    - step-52
  - Time dependent fluid structure interaction problems
    - step-70

- step-1
  - Creating a grid. A simple way to write it to a file.
  - Keywords: Triangulation, GridGenerator::hyper_cube(), GridGenerator::hyper_shell(), GridOut, Triangulation::execute_coarsening_and_refinement()
- step-2
  - Associate degrees of freedom to each vertex and compute the resulting sparsity pattern of matrices.
  - Show that renumbering reduces the bandwidth of matrices significantly,
  - i.e. clusters nonzero entries around the diagonal.
  - Keywords: FE_Q, DynamicSparsityPattern, DoFTools::make_sparsity_pattern(), DoFHandler::distribute_dofs(), DoFRenumbering, SparsityPattern
- step-3
  - Actually solve Laplace's problem. Object-orientation. Assembling matrices and vectors.
  - Boundary values.
  - Keywords: FEValues, VectorTools::interpolate_boundary_values(), MatrixTools::apply_boundary_values(), SolverCG, Vector, SparseMatrix, DataOut
- step-4
  - This example is programmed in a way that it is independent of the dimension for
  - which we want to solve Laplace's equation;
  - we will solve the equation in 2D and 3D, although the program is exactly the same.
  - Non-constant right hand side function. Non-homogeneous boundary values.
  - Keywords: VectorTools::point_value(), VectorTools::compute_mean_value()
- step-5
  - Computations on successively refined grids.
  - Reading a grid from disk. Some optimizations. Using assertions.
  - Non-constant coefficient in the elliptic operator (yielding the extended Poisson equation).
  - Preconditioning the CG solver for the linear system of equations.
  - Keywords: PreconditionSSOR, GridIn, SphericalManifold
- step-6
  - Adaptive local refinement.
  - Handling of hanging nodes. Higher order elements.
  - Catching exceptions in the main function.
  - Keywords: DoFTools::make_hanging_node_constraints(), AffineConstraints::distribute_local_to_global(), KellyErrorEstimator, GridRefinement::refine_and_coarsen_fixed_number()
- step-7
  - Helmholtz equation.
  - Non-homogeneous Neumann boundary conditions and boundary integrals.
  - Verification of correctness of computed solutions.
  - Computing the error between exact and numerical solution and output of the data in tables.
  - Using counted pointers.
  - Keywords: FEFaceValues, VectorTools::integrate_difference(), VectorTools::compute_global_error(), TableHandler
- step-8
  - The elasticity equations will be solved instead of Laplace's equation.
  - The solution is vector-valued and the equations form a system with
  - as many equations as the dimension of the space in which it is posed.
  - Keywords: FESystem
- step-9
  - Linear advection equation, assembling the system of equations in parallel using multi-threading,
  - implementing a refinement criterion based on a finite difference approximation of the gradient.
  - Keywords: TensorFunction, WorkStream::run(), SolverGMRES
- step-10
  - Higher order mappings.
  - Do not solve equations, but rather compute the value of pi to high accuracy.
  - Keywords: MappingQ, FE_Nothing, ConvergenceTable, GridOut, FEFaceValues
- step-11
  - Solving a Laplace problem with higher order mappings.
  - Using mean value constraints and intermediate representations of sparsity patterns.
  - Keywords: AffineConstraints, DoFTools::extract_boundary_dofs(), TableHandler
- step-12
  - Discontinuous Galerkin methods for linear advection problems.
  - Keywords: FEInterfaceValues, MeshWorker::mesh_loop(), DoFTools::make_flux_sparsity_pattern()
- step-13
  - Software design questions and
  - how to write a modular, extensible finite element program.
- step-14
  - Duality based error estimators, more strategies to write a modular, extensible finite element program.
  - Keywords: KellyErrorEstimator
- step-15
  - A nonlinear elliptic problem:
  - The minimal surface equation.
  - Newton's method.
  - Transferring a solution across mesh refinement.
  - Keywords: SolutionTransfer
- step-16
  - Multigrid preconditioning of the Laplace equation on adaptive meshes.
  - Keywords: Multigrid, PreconditionMG, mg::Matrix, MGTransferPrebuilt, MeshWorker::mesh_loop(), MGLevelObject, MGConstrainedDoFs
- step-16b
  - A variant of step-16 but with MeshWorker for assembly:
  - Multigrid preconditioning of the Laplace equation on adaptive meshes.
- step-17
  - Using PETSc for linear algebra; running in parallel on clusters of computers linked together by MPI.
  - Keywords: PETScWrappers::MPI::SparseMatrix, ConditionalOStream, PETScWrappers::PreconditionBlockJacobi
- step-18
  - A time dependent problem;
  - using a much simplified version of implementing elasticity;
  - moving meshes; handling large scale output of parallel programs.
  - Simple implicit (backward Euler) time stepping.
  - Keywords: parallel::shared::Triangulation, DataOutInterface::write_vtu_with_pvtu_record()
- step-20
  - Mixed finite elements.
  - Using block matrices and block vectors to define more complicated solvers
  - and preconditioners working on the Schur complement.
  - Keywords: FEValuesExtractors, LinearOperator, TensorFunction, FE_RaviartThomas
- step-21
  - The time dependent two-phase flow in porous media.
  - Extensions of mixed Laplace discretizations.
  - More complicated block solvers. Simple explicit (forward Euler) time stepping.
  - Keywords: TensorFunction, FE_RaviartThomas, VectorTools::project(), DiscreteTime
- step-22
  - Solving the Stokes equations of slow fluid flow on adaptive meshes.
  - More on Schur complement solvers. Advanced use of the AffineConstraints class.
  - Keywords: AffineConstraints, VectorTools::compute_no_normal_flux_constraints(), SparseILU, SparseDirectUMFPACK, BlockDynamicSparsityPattern
- step-23
  - Finally a "real" time dependent problem, the wave equation.
  - Fractional time stepping (explicit, fully implicit and Crank-Nicholson method).
  - Keywords: MatrixCreator, VectorTools::project()
- step-24
  - A variant of step-23 with absorbing boundary conditions,
  - and extracting practically useful data. Implicit time stepping.
  - Keywords: VectorTools::point_value()
- step-25
  - The sine-Gordon soliton equation,
  - which is a nonlinear variant of the time dependent wave equation covered in step-23 and step-24.
  - Fractional time stepping.
  - Keywords: FunctionTime, VectorTools::integrate_difference()
- step-26
  - The heat equation, solved on a mesh that is adapted every few time steps.
  - Fractional time stepping.
  - Keywords: KellyErrorEstimator, SolutionTransfer, VectorTools::interpolate(), VectorTools::create_right_hand_side()
- step-27
  - The hp finite element method.
  - Keywords: hp::DoFHandler, hp::FECollection, hp::QCollection, FESeries::Fourier, Triangulation::create_triangulation()
- step-28
  - Multiple grids for solving a multigroup diffusion equation
  - in nuclear physics simulating a nuclear reactor core.
- step-29
  - Solving a complex-valued Helmholtz equation.
  - Sparse direct solvers. Dealing with parameter files.
- step-30
  - Anisotropic refinement for DG finite element methods.
- step-31
  - Time-dependent Stokes flow driven by temperature differences in a fluid.
  - Adaptive meshes that change between time steps.
  - Implicit/explicit time stepping.
- step-32
  - A massively parallel solver for time-dependent Stokes flow
  - driven by temperature differences in a fluid.
  - Adapting methods for real-world equations.
  - Implicit/explicit time stepping.
- step-33
  - A nonlinear hyperbolic conservation law:
  - The Euler equations of compressible gas dynamics.
  - Fractional time stepping.
- step-34
  - Boundary element methods (BEM) of low order:
  - Exterior irrotational flow.
  - The ParsedFunction class.
- step-35
  - A projection solver for the Navier–Stokes equations.
- step-36
  - Using SLEPc for linear algebra; solving an eigenspectrum problem.
  - The Schrödinger wave equation.
- step-37
  - Solving a Poisson problem with a multilevel preconditioner
  - without explicitly storing the matrix (a matrix-free method) in a massively parallel context.
- step-38
  - Solving the Laplace-Beltrami equation on curved manifolds
  - embedded in higher dimensional spaces.
- step-39
  - Solving Poisson's equation once more,
  - this time with the interior penalty method,
  - one of the discontinuous Galerkin methods developed for this problem.
  - Error estimator, adaptive meshes, and multigrid preconditioner, all using the MeshWorker framework.
- step-40
  - Techniques for the massively parallel solution of the Laplace equation (up to 10,000s of processors).
- step-41
  - Solving the obstacle problem, a variational inequality.
- step-42
  - A solver for an elasto-plastic contact problem,
  - running on parallel machines.
- step-43
  - Advanced techniques for the simulation of porous media flow.
  - Explicit time stepping.
- step-44
  - Finite strain hyperelasticity based on a three-field formulation.
  - Implicit time stepping.
  - Keywords: CellDataStorage, FEValuesExtractors, WorkStream::run, BlockSparseMatrix, BlockVector, ComponentSelectFunction, Physics::Elasticity, FullMatrix::extract_submatrix_from(), FullMatrix::scatter_matrix_to(), LinearOperator, SolverSelector, PreconditionSelector, ReductionControl, MappingQEulerian
- step-45
  - Periodic boundary conditions.
  - Keywords: GridTools::collect_periodic_faces(), GridTools::PeriodicFacePair, Triangulation::add_periodicity()
- step-46
  - Coupling different kinds of equations in different parts of the domain.
- step-47
  - Solving the fourth-order biharmonic equation using the C0 Interior Penalty (C0IP) method.
  - Keywords: FEInterfaceValues
- step-48
  - Explicit time stepping for the Sine–Gordon equation
  - based on a diagonal mass matrix.
  - Efficient implementation of (nonlinear) finite element operators.
- step-49
  - Advanced mesh creation and manipulation techniques.
- step-50
  - Geometric multigrid on adaptive meshes distributed in parallel.
  - Keywords: Multigrid, MGLevelObject, MGConstrainedDoFs, IndexSet, MGTools, PreconditionMG, MatrixFree, FEInterfaceValues, MeshWorker::mesh_loop()
- step-51
  - Solving the convection-diffusion equation
  - with a hybridizable discontinuous Galerkin method using face elements.
- step-52
  - Solving the time dependent neutron diffusion equation
  - using Runge-Kutta methods.
  - Explicit and implicit time stepping.
- step-53
  - Describing the geometry of complex domains and curved boundaries.
- step-54
  - Using CAD files to describe the boundary of your domain.
  - Keywords: Manifold, OpenCASCADE::read_IGES(), OpenCASCADE::NormalProjectionBoundary
- step-55
  - Solving the Stokes problem in parallel.
- step-56
  - Geometric Multigrid for Stokes.
- step-57
  - Incompressible, stationary Navier Stokes equations.
- step-58
  - The nonlinear Schrödinger equation.
- step-59
  - Solving a Poisson problem discretized
  - with an interior penalty DG method and a multilevel preconditioner
  - in a matrix-free fashion using a massively parallel implementation.
- step-60
  - Distributed Lagrange multipliers for the solution of Poisson problems
  - in complex domains with constraints defined on non-matching grids.
- step-61
  - Solving the Poisson problem with the "weak Galerkin" finite element method.
- step-62
  - Resonance frequency and bandgap of a phononic crystal.
  - Elastic wave equation in the frequency domain
  - with Perfectly Matched Layer boundary conditions.
  - Parallelization via MUMPS and MPI.
- step-63
  - Block smoothers for geometric multigrid.
  - A scalar convection diffusion equation is solved
  - with different additive or multiplicative multigrid smoothers.
  - Keywords: Multigrid, MeshWorker::mesh_loop(), MGSmootherPrecondition, RelaxationBlock, DoFRenumbering::downstream()
- step-64
  - Solving a Helmholtz problem
  - using matrix-free methods on the GPU with MPI parallelization.
- step-65
  - The TransfiniteInterpolationManifold and MappingQCache classes
  - for advanced manifold operations.
- step-67
  - Solving the Euler equations of compressible gas dynamics
  - with an explicit time integrator and high-order discontinuous Galerkin methods
  - based on matrix-free implementations.
- step-69
  - Hyperbolic conservation laws:
  - a first-order guaranteed maximum wavespeed method
  - for the compressible Euler equations.
  - Explicit time stepping.
- step-70
  - A fluid structure interaction problem
  - on fully distributed non-matching grids,
  - using penalty methods, and a coupling constructed through a ParticleHandler object.

## satify example

```bash
Scanning dependencies of target step-1.debug
Scanning dependencies of target step-2.debug
Scanning dependencies of target step-3.debug
Scanning dependencies of target step-4.debug
Scanning dependencies of target step-5.debug
Scanning dependencies of target step-6.debug
Scanning dependencies of target step-7.debug
Scanning dependencies of target step-8.debug
Scanning dependencies of target step-9.debug
Scanning dependencies of target step-10.debug
Scanning dependencies of target step-11.debug
Scanning dependencies of target step-12.debug
Scanning dependencies of target step-12b.debug
Scanning dependencies of target step-13.debug
Scanning dependencies of target step-14.debug
Scanning dependencies of target step-15.debug
Scanning dependencies of target step-16.debug
Scanning dependencies of target step-16b.debug
17, 18, 19
Scanning dependencies of target step-20.debug
Scanning dependencies of target step-21.debug
Scanning dependencies of target step-22.debug
Scanning dependencies of target step-23.debug
Scanning dependencies of target step-24.debug
Scanning dependencies of target step-25.debug
Scanning dependencies of target step-26.debug
Scanning dependencies of target step-27.debug
Scanning dependencies of target step-28.debug
Scanning dependencies of target step-29.debug
Scanning dependencies of target step-30.debug
31, 32, 33
Scanning dependencies of target step-34.debug
Scanning dependencies of target step-35.debug
36
Scanning dependencies of target step-37.debug
Scanning dependencies of target step-38.debug
Scanning dependencies of target step-39.debug
40, 41, 42, 43
Scanning dependencies of target step-44.debug
45
Scanning dependencies of target step-46.debug
Scanning dependencies of target step-47.debug
Scanning dependencies of target step-48.debug
Scanning dependencies of target step-49.debug
50
Scanning dependencies of target step-51.debug
Scanning dependencies of target step-52.debug
Scanning dependencies of target step-53.debug
54, 55
Scanning dependencies of target step-56.debug
Scanning dependencies of target step-57.debug
Scanning dependencies of target step-58.debug
Scanning dependencies of target step-59.debug
Scanning dependencies of target step-60.debug
Scanning dependencies of target step-61.debug
62
Scanning dependencies of target step-63.debug
64
Scanning dependencies of target step-65.debug
66
Scanning dependencies of target step-67.debug
68, 69, 70

DEAL_II_WITH_MPI = OFF
PETSC_WITH_MPI   = (NOT FALSE)
```

## *.inst.in Error
