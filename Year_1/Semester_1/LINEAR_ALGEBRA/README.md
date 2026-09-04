# Linear Algebra

## Course Overview
This course provides a comprehensive introduction to the foundational concepts and algorithmic methods of linear algebra. It establishes mathematical frameworks essential for computer graphics, signal processing, data analysis, machine learning, and scientific computing.

## Course Code
102 (LINEAR ALGEBRA)

## Prerequisites
None (High school algebra and analytic geometry)

---

## Topics Covered
* **Systems of Linear Equations**: Augmented matrices, elementary row operations, Gaussian elimination, Gauss-Jordan elimination, row echelon forms, solution sets (unique, infinite, inconsistent).
* **Matrix Algebra**: Matrix operations, transpose, identity matrices, inverse matrices via row reduction and adjugate formulas, block matrices.
* **Determinants**: Axiomatic properties, cofactor expansion, determinant of triangular matrices, Cramer's rule.
* **Vector Spaces and Subspaces**: Axioms of real vector spaces ($\mathbb{R}^n$ and function spaces), subspaces, linear combinations, span, linear independence, basis, dimension.
* **Fundamental Matrix Subspaces**: Column space $\text{Col}(A)$, null space $\text{Null}(A)$, row space $\text{Row}(A)$, left null space $\text{Null}(A^T)$, Rank-Nullity theorem.
* **Linear Transformations**: Kernel, range, matrix representation relative to standard and arbitrary bases, composition, isomorphisms.
* **Inner Product Spaces and Orthogonality**: Dot products, norms, Cauchy-Schwarz inequality, orthogonal complements, projections, Gram-Schmidt orthogonalization process, QR factorization.
* **Eigenvalues, Eigenvectors, and Diagonalization**: Characteristic polynomial, algebraic and geometric multiplicities, diagonalization condition ($A = PDP^{-1}$), symmetric matrices and spectral theorem.
* **Applications**: Least-squares data fitting, Google PageRank algorithm, Markov chains, quadratic forms.

---

## Learning Objectives
* Solve arbitrary systems of linear equations using systematic Gaussian elimination.
* Compute matrix determinants, inverses, rank, and nullity.
* Identify vector spaces, verify linear independence, and construct orthonormal bases.
* Diagonalize diagonalizable matrices and compute high matrix powers efficiently.
* Formulate least-squares approximations for overdetermined systems.
* Implement linear algebraic computations and visualizations using GNU Octave and MATLAB.

---

## Directory Structure

| Directory | Description |
|:---|:---|
| [`Lectures/`](Lectures/) | Structured theory lecture modules covering vector spaces, linear systems, and eigenspaces |
| [`Exercises/`](Exercises/) | Practice drills and step-by-step solved problem sets on matrix algebra |
| [`Examples/`](Examples/) | Executable GNU Octave/MATLAB scripts demonstrating matrix operations and algorithms |
| [`Assignments/`](Assignments/) | Rigorous coursework assignments with computational problems and rubrics |
| [`Tutorials/`](Tutorials/) | Hands-on guide to matrix computations and plotting in GNU Octave |
| [`Projects/`](Projects/) | Capstone design project (PageRank and Least Squares Regression) |
| [`Exams/`](Exams/) | Practice mock examinations and archival exam materials |
| [`Resources/`](Resources/) | Granular chapter notes, reference textbook PDF, and curriculum mindmaps |

---

## Computational Tools

The practical component of this course utilizes **GNU Octave** (or MATLAB). Executable demonstration scripts are located in [`Examples/Matlab_Octave_Code/`](Examples/Matlab_Octave_Code/). For setup instructions and basic commands, refer to [`Tutorials/tutorial_01_octave_matlab_matrix_computations.md`](Tutorials/tutorial_01_octave_matlab_matrix_computations.md).
