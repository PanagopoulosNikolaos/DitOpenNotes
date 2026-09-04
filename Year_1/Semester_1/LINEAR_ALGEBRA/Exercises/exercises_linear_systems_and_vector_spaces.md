# Practice Exercises: Linear Systems and Vector Spaces

This drill document provides rigorous solved exercises covering linear systems, vector space properties, matrix rank, basis computation, and eigenvalue decomposition.

---

## Section 1: Systems of Linear Equations

### Problem 1: Gauss-Jordan Elimination
**Problem:** Solve the linear system using Gauss-Jordan elimination to compute RREF:

$$\begin{cases}
x_1 + 2x_2 - x_3 = 2 \\
2x_1 + 5x_2 + 2x_3 = 9 \\
-x_1 - 3x_2 + 4x_3 = -2
\end{cases}$$

**Step-by-Step Solution:**
1. Formulate augmented matrix:
   $$\left[\begin{array}{ccc|c}
   1 & 2 & -1 & 2 \\
   2 & 5 & 2 & 9 \\
   -1 & -3 & 4 & -2
   \end{array}\right]$$
2. Eliminate entries below first pivot ($R_2 \leftarrow R_2 - 2R_1$, $R_3 \leftarrow R_3 + R_1$):
   $$\left[\begin{array}{ccc|c}
   1 & 2 & -1 & 2 \\
   0 & 1 & 4 & 5 \\
   0 & -1 & 3 & 0
   \end{array}\right]$$
3. Eliminate entries below second pivot ($R_3 \leftarrow R_3 + R_2$):
   $$\left[\begin{array}{ccc|c}
   1 & 2 & -1 & 2 \\
   0 & 1 & 4 & 5 \\
   0 & 0 & 7 & 5
   \end{array}\right]$$
4. Scale third row ($R_3 \leftarrow \frac{1}{7} R_3$):
   $$\left[\begin{array}{ccc|c}
   1 & 2 & -1 & 2 \\
   0 & 1 & 4 & 5 \\
   0 & 0 & 1 & 5/7
   \end{array}\right]$$
5. Back-substitute to RREF:
   - $R_2 \leftarrow R_2 - 4R_3 \implies 5 - 4(5/7) = 15/7$
   - $R_1 \leftarrow R_1 + R_3 \implies 2 + 5/7 = 19/7$
   - $R_1 \leftarrow R_1 - 2R_2 \implies 19/7 - 2(15/7) = -11/7$
6. Final Unique Solution:
   $$x_1 = -\frac{11}{7}, \quad x_2 = \frac{15}{7}, \quad x_3 = \frac{5}{7}$$

---

## Section 2: Linear Independence and Basis

### Problem 2: Linear Independence in $\mathbb{R}^3$
**Problem:** Determine whether the vectors $\mathbf{v}_1 = \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}, \mathbf{v}_2 = \begin{bmatrix} 2 \\ -1 \\ 4 \end{bmatrix}, \mathbf{v}_3 = \begin{bmatrix} 0 \\ 5 \\ 2 \end{bmatrix}$ are linearly independent.

**Step-by-Step Solution:**
1. Form matrix $A = [\mathbf{v}_1 \mid \mathbf{v}_2 \mid \mathbf{v}_3]$ and compute determinant:
   $$\det(A) = \begin{vmatrix}
   1 & 2 & 0 \\
   2 & -1 & 5 \\
   3 & 4 & 2
   \end{vmatrix}$$
2. Expand along the first row:
   $$\det(A) = 1 \cdot \begin{vmatrix} -1 & 5 \\ 4 & 2 \end{vmatrix} - 2 \cdot \begin{vmatrix} 2 & 5 \\ 3 & 2 \end{vmatrix} + 0$$
   $$= 1 \cdot ((-1)(2) - (5)(4)) - 2 \cdot ((2)(2) - (5)(3))$$
   $$= 1 \cdot (-2 - 20) - 2 \cdot (4 - 15) = -22 - 2(-11) = -22 + 22 = 0$$
3. Since $\det(A) = 0$, matrix $A$ is singular, the columns are **linearly dependent**, and there exists a non-trivial linear combination producing $\mathbf{0}$. Indeed, $2\mathbf{v}_1 - \mathbf{v}_2 - \mathbf{v}_3 = \mathbf{0}$.

---

## Section 3: Fundamental Matrix Subspaces

### Problem 3: Null Space and Column Space Basis
**Problem:** Find bases for $\text{Col}(A)$ and $\text{Null}(A)$ for matrix:
$$A = \begin{bmatrix}
1 & 3 & 3 & 2 \\
2 & 6 & 9 & 7 \\
-1 & -3 & 3 & 4
\end{bmatrix}$$

**Step-by-Step Solution:**
1. Perform row reduction to REF:
   $$R_2 \leftarrow R_2 - 2R_1, \quad R_3 \leftarrow R_3 + R_1$$
   $$\begin{bmatrix}
   1 & 3 & 3 & 2 \\
   0 & 0 & 3 & 3 \\
   0 & 0 & 6 & 6
   \end{bmatrix}
   \xrightarrow{R_3 \leftarrow R_3 - 2R_2}
   \begin{bmatrix}
   1 & 3 & 3 & 2 \\
   0 & 0 & 3 & 3 \\
   0 & 0 & 0 & 0
   \end{bmatrix}$$
2. Reduce to RREF ($R_2 \leftarrow \frac{1}{3}R_2$, $R_1 \leftarrow R_1 - 3R_2$):
   $$\begin{bmatrix}
   1 & 3 & 0 & -1 \\
   0 & 0 & 1 & 1 \\
   0 & 0 & 0 & 0
   \end{bmatrix}$$
3. Pivot columns are **Column 1** and **Column 3**.
   A basis for $\text{Col}(A)$ consists of the original corresponding columns of $A$:
   $$\mathcal{B}_{\text{Col}} = \left\{ \begin{bmatrix} 1 \\ 2 \\ -1 \end{bmatrix}, \begin{bmatrix} 3 \\ 9 \\ 3 \end{bmatrix} \right\}, \quad \dim(\text{Col}(A)) = \text{rank}(A) = 2$$
4. Free variables are $x_2$ and $x_4$.
   From RREF:
   $$x_1 = -3x_2 + x_4, \quad x_3 = -x_4$$
   Parametric vector form:
   $$\mathbf{x} = \begin{bmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \end{bmatrix} = x_2 \begin{bmatrix} -3 \\ 1 \\ 0 \\ 0 \end{bmatrix} + x_4 \begin{bmatrix} 1 \\ 0 \\ -1 \\ 1 \end{bmatrix}$$
   A basis for $\text{Null}(A)$ is:
   $$\mathcal{B}_{\text{Null}} = \left\{ \begin{bmatrix} -3 \\ 1 \\ 0 \\ 0 \end{bmatrix}, \begin{bmatrix} 1 \\ 0 \\ -1 \\ 1 \end{bmatrix} \right\}, \quad \dim(\text{Null}(A)) = \text{nullity}(A) = 2$$
5. Verification of Rank-Nullity Theorem: $\text{rank}(A) + \text{nullity}(A) = 2 + 2 = 4$ (columns).

