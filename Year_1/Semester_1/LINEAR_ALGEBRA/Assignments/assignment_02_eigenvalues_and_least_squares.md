# Assignment 02: Eigenvalues, Diagonalization, and Least-Squares Fitting

## Objective
Implement eigensystem decomposition and orthogonal least-squares polynomial regression. Analyze discrete matrix power sequences and implement automated data fitting in GNU Octave/MATLAB.

---

## Technical Specifications

### Problem 1: Diagonalization and Discrete Matrix Evolution
Consider matrix $A \in \mathbb{R}^{3 \times 3}$:

$$A = \begin{bmatrix}
3 & -1 & 1 \\
-1 & 5 & -1 \\
1 & -1 & 3
\end{bmatrix}$$

1. Determine the characteristic polynomial $p(\lambda) = \det(A - \lambda I_3)$ and find all eigenvalues.
2. For each eigenvalue, find a basis for its eigenspace and determine algebraic and geometric multiplicities.
3. Show that $A$ is orthogonally diagonalizable:
   - Construct orthogonal matrix $P$ whose columns are normalized eigenvectors.
   - Form diagonal matrix $D$ such that $A = P D P^T$.
4. Compute an exact closed-form expression for $A^k$ for arbitrary integer $k \ge 1$.

### Problem 2: Orthogonal Projections and Least-Squares Curve Fitting
Consider the following experimental data points $(x_i, y_i)$:
$$\{(1, 2.1), (2, 3.9), (3, 6.2), (4, 7.8), (5, 10.1)\}$$

1. Formulate the overdetermined linear system $X \mathbf{w} = \mathbf{y}$ for a linear model $\hat{y} = w_1 x + w_0$.
2. Formulate the **Normal Equations**:
   $$X^T X \mathbf{w} = X^T \mathbf{y}$$
3. Solve for optimal parameter vector $\hat{\mathbf{w}} = (X^T X)^{-1} X^T \mathbf{y}$.
4. Compute the residual error vector $\mathbf{r} = \mathbf{y} - X \hat{\mathbf{w}}$ and verify orthogonality: $X^T \mathbf{r} = \mathbf{0}$.
5. Calculate the total sum of squared errors $S = \|\mathbf{r}\|^2$.

### Problem 3: Octave Implementation
Write an Octave script `assignment_02_fitting.m` that:
- Computes $P$ and $D$ using `[V, D] = eig(A)`.
- Solves the least-squares system via normal equations and backslash operator `X \ y`.
- Generates a plot showing raw data points and the fitted regression line.

---

## Deliverables & Evaluation Rubric

| Criterion | Target Metric | Points |
|:---|:---|:---:|
| Characteristic Equation & Multiplicities | Accurate eigenvalue derivations and eigenspace bases | 30 |
| Orthogonal Diagonalization & $A^k$ | Correct construction of orthogonal matrix $P$ and closed form of $A^k$ | 30 |
| Least-Squares Formulation & Residuals | Flawless normal equation setup, parameter solution, and error norm | 25 |
| Octave Script & Visualization | Functional script with clear plotting of regression line and data | 15 |
| **Total** | | **100** |

