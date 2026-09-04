# Assignment 01: Linear Systems, Subspace Decomposition, and Basis Construction

## Objective
Analyze parametrically defined systems of linear equations, calculate bases for the four fundamental matrix subspaces, verify the Rank-Nullity Theorem, and implement computational solutions in GNU Octave/MATLAB.

---

## Technical Specifications

### Problem 1: Parametric Linear System Analysis
Consider the linear system $A \mathbf{x} = \mathbf{b}$ parameterized by real constant $k \in \mathbb{R}$:

$$\left[\begin{array}{ccc}
1 & 1 & k \\
1 & k & 1 \\
k & 1 & 1
\end{array}\right]
\left[\begin{array}{c} x \\ y \\ z \end{array}\right]
=
\left[\begin{array}{c} 1 \\ 1 \\ 1 \end{array}\right]$$

1. Compute $\det(A)$ as a polynomial function of $k$.
2. Determine all values of $k$ for which the system has:
   - A unique solution (solve explicitly using Cramer's rule or row reduction).
   - Infinitely many solutions (express the solution set in parametric vector form).
   - No solution (inconsistent).

### Problem 2: Fundamental Subspaces of a Matrix
Given matrix $M \in \mathbb{R}^{4 \times 5}$:

$$M = \begin{bmatrix}
1 & -2 & 0 & 3 & 2 \\
2 & -4 & 1 & 8 & 3 \\
-1 & 2 & 2 & 1 & -8 \\
0 & 0 & 3 & 6 & -3
\end{bmatrix}$$

1. Compute $\text{RREF}(M)$ showing all row operations.
2. Determine $\text{rank}(M)$ and identify pivot columns.
3. Construct an explicit basis for the column space $\text{Col}(M)$.
4. Construct an explicit basis for the null space $\text{Null}(M)$.
5. Construct an explicit basis for the row space $\text{Row}(M)$.
6. Explicitly verify the Rank-Nullity Theorem: $\text{rank}(M) + \text{nullity}(M) = 5$.

### Problem 3: Computational Verification in GNU Octave
Write an Octave script `assignment_01_subspaces.m` that:
- Constructs matrix $M$.
- Computes `rref(M)`, `rank(M)`, and `null(M)`.
- Verifies orthogonality: tests whether any null space vector $\mathbf{v}$ satisfies $M \mathbf{v} = \mathbf{0}$.

---

## Deliverables & Evaluation Rubric

| Criterion | Target Metric | Points |
|:---|:---|:---:|
| Determinant & Parameter Classification | Exact roots and exhaustive classification of $k$ parameter cases | 30 |
| Subspace Bases & Derivation | Correct identification of pivot columns and orthogonal null space vectors | 35 |
| Rank-Nullity Theorem Verification | Explicit dimensional verification and geometric explanation | 15 |
| Octave Script & Code Quality | Error-free execution of `assignment_01_subspaces.m` confirming results | 20 |
| **Total** | | **100** |

