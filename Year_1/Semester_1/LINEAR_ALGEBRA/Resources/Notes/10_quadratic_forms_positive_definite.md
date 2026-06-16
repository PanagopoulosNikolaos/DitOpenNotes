# Quadratic Forms and Positive Definite Matrices

A quadratic form is a homogeneous polynomial of degree two in several variables, expressible as $\mathbf{x}^\mathsf{T} A \mathbf{x}$ with a symmetric matrix $A$. The definiteness of a quadratic form---whether it is always positive, always negative, or changes sign---determines the nature of critical points in optimization and the stability of dynamical systems. The spectral theorem provides the canonical diagonalization of quadratic forms, and Sylvester's criterion gives a practical test for positive definiteness.

---

## 1. Core Definitions

### 1.1 Quadratic Form

A **quadratic form** in $n$ variables is:

$$
Q(\mathbf{x}) = \mathbf{x}^\mathsf{T} A \mathbf{x} = \sum_{i=1}^{n} \sum_{j=1}^{n} a_{ij} x_i x_j
$$

where $A$ is symmetric ($a_{ij} = a_{ji}$). The symmetry condition is always assumed because the anti-symmetric part contributes zero to $Q$.

### 1.2 Canonical Form via Diagonalization

By the spectral theorem, $A = Q D Q^\mathsf{T}$ with $Q$ orthogonal and $D = \text{diag}(\lambda_1, \ldots, \lambda_n)$. Let $\mathbf{y} = Q^\mathsf{T} \mathbf{x}$, then:

$$
Q(\mathbf{x}) = \mathbf{y}^\mathsf{T} D \mathbf{y} = \lambda_1 y_1^2 + \lambda_2 y_2^2 + \cdots + \lambda_n y_n^2
$$

---

## 2. Classification of Quadratic Forms

Let $A$ be symmetric. The quadratic form $Q(\mathbf{x}) = \mathbf{x}^\mathsf{T} A \mathbf{x}$ is:

| Type | Condition | Example |
| :--- | :--- | :--- |
| Positive definite | $Q(\mathbf{x}) > 0$ for all $\mathbf{x} \neq \mathbf{0}$ | $x_1^2 + x_2^2$ |
| Positive semidefinite | $Q(\mathbf{x}) \geq 0$ for all $\mathbf{x}$ | $x_1^2$ |
| Negative definite | $Q(\mathbf{x}) < 0$ for all $\mathbf{x} \neq \mathbf{0}$ | $-x_1^2 - x_2^2$ |
| Negative semidefinite | $Q(\mathbf{x}) \leq 0$ for all $\mathbf{x}$ | $-x_1^2$ |
| Indefinite | $Q$ takes both positive and negative values | $x_1^2 - x_2^2$ |

---

## 3. Positive Definite Matrices

### 3.1 Equivalent Conditions

For a symmetric $n \times n$ matrix $A$, the following are equivalent:

1. $A$ is positive definite ($\mathbf{x}^\mathsf{T} A \mathbf{x} > 0$ for $\mathbf{x} \neq \mathbf{0}$).
2. All eigenvalues of $A$ are positive ($\lambda_i > 0$).
3. All leading principal minors are positive (Sylvester's criterion).
4. $A = LL^\mathsf{T}$ for some lower triangular $L$ with positive diagonal (Cholesky factorization exists).
5. $A = B^\mathsf{T} B$ for some full-rank matrix $B$.

### 3.2 Sylvester's Criterion

Let $A_k$ denote the $k \times k$ upper-left submatrix of $A$ (the $k$-th leading principal submatrix). $A$ is positive definite iff:

$$
\det(A_1) > 0,\; \det(A_2) > 0,\; \ldots,\; \det(A_n) > 0
$$

### 3.3 Applications

- **Optimization:** At a critical point, if the Hessian matrix is positive definite, the point is a local minimum; if negative definite, a local maximum; if indefinite, a saddle point.
- **Statistics:** Covariance matrices are positive semidefinite.
- **Engineering:** Stiffness matrices in finite element analysis are positive definite.

---

## 4. Spectral Theorem (Review)

### 4.1 Statement

Every real symmetric matrix $A$ can be orthogonally diagonalized:

$$
A = Q D Q^\mathsf{T}
$$

### 4.2 Implications for Quadratic Forms

- Eigenvectors corresponding to distinct eigenvalues are orthogonal.
- The maximum and minimum of $Q(\mathbf{x})$ on the unit sphere $\|\mathbf{x}\| = 1$ are the largest and smallest eigenvalues of $A$.

---

## Solved Exercises

### Exercise 1: Classification by Eigenvalues

**Problem:**
Classify $Q(x_1, x_2) = 2x_1^2 + 4x_1x_2 + 2x_2^2$.

**Solution:**
Write in matrix form: $A = \begin{bmatrix} 2 & 2 \\ 2 & 2 \end{bmatrix}$.

Eigenvalues: $\det(A - \lambda I) = (2-\lambda)^2 - 4 = \lambda^2 - 4\lambda = \lambda(\lambda - 4)$.
$\lambda_1 = 4$, $\lambda_2 = 0$.

Since one eigenvalue is zero and the other is positive, $Q$ is **positive semidefinite**.

Check: $Q(x_1, x_2) = 2(x_1^2 + 2x_1x_2 + x_2^2) = 2(x_1 + x_2)^2 \geq 0$, with equality when $x_1 = -x_2$.

---

### Exercise 2: Sylvester's Criterion

**Problem:**
Determine if $A = \begin{bmatrix} 4 & 2 & 1 \\ 2 & 5 & 3 \\ 1 & 3 & 6 \end{bmatrix}$ is positive definite.

**Solution:**
Check leading principal minors:

$A_1 = [4]$, $\det(A_1) = 4 > 0$.

$A_2 = \begin{bmatrix} 4 & 2 \\ 2 & 5 \end{bmatrix}$, $\det(A_2) = 4 \cdot 5 - 2 \cdot 2 = 20 - 4 = 16 > 0$.

$A_3 = A$, compute determinant:

$$
\det(A) = 4 \begin{vmatrix} 5 & 3 \\ 3 & 6 \end{vmatrix}
- 2 \begin{vmatrix} 2 & 3 \\ 1 & 6 \end{vmatrix}
+ 1 \begin{vmatrix} 2 & 5 \\ 1 & 3 \end{vmatrix}
$$

$$
= 4(30 - 9) - 2(12 - 3) + 1(6 - 5) = 4 \cdot 21 - 2 \cdot 9 + 1 \cdot 1
= 84 - 18 + 1 = 67 > 0
$$

All leading principal minors are positive, so $A$ is **positive definite**.

---

### Exercise 3: Classification as Definite, Semidefinite, or Indefinite

**Problem:**
Classify $Q(x_1, x_2, x_3) = x_1^2 - 2x_1x_2 + x_2^2 - x_3^2$.

**Solution:**
Matrix form with symmetric $A$: $Q = \mathbf{x}^\mathsf{T} \begin{bmatrix} 1 & -1 & 0 \\ -1 & 1 & 0 \\ 0 & 0 & -1 \end{bmatrix} \mathbf{x}$.

Eigenvalues: $\det(A - \lambda I) = (1-\lambda)^2(-1-\lambda) - (-1)^2(-1-\lambda)$.

This simplifies: $\det = ((1-\lambda)^2 - 1)(-1-\lambda) = (\lambda^2 - 2\lambda)(-1-\lambda) = \lambda(\lambda - 2)(-\lambda - 1) = -\lambda(\lambda - 2)(\lambda + 1)$.

Eigenvalues: $\lambda = 0$, $\lambda = 2$, $\lambda = -1$.

Since there are both positive ($2$) and negative ($-1$) eigenvalues, $Q$ is **indefinite**. Note the zero eigenvalue makes it not definite in either direction.

---

### Exercise 4: Optimization Application

**Problem:**
Find and classify the critical point of $f(x, y) = x^2 + 4xy + 5y^2 - 6x - 14y$.

**Solution:**
Gradient: $\nabla f = (2x + 4y - 6, 4x + 10y - 14)$.

Set to zero:
$$
2x + 4y = 6,\quad 4x + 10y = 14
$$

Divide first by 2: $x + 2y = 3$. Second: $4x + 10y = 14$.

From the first, $x = 3 - 2y$. Substitute: $4(3 - 2y) + 10y = 12 - 8y + 10y = 12 + 2y = 14 \Rightarrow y = 1$, $x = 1$.

Critical point: $(1, 1)$.

Hessian matrix: $H = \begin{bmatrix} 2 & 4 \\ 4 & 10 \end{bmatrix}$.

Leading principal minors: $\det(H_1) = 2 > 0$, $\det(H_2) = 2 \cdot 10 - 4 \cdot 4 = 20 - 16 = 4 > 0$.

$H$ is positive definite, so $(1, 1)$ is a **local minimum**.

---

### Exercise 5: Completing the Square

**Problem:**
Write $Q(x, y) = 3x^2 + 4xy + 2y^2$ as a sum of squares.

**Solution:**
Complete the square in $x$:

$$
Q = 3\left(x^2 + \frac{4}{3}xy\right) + 2y^2
= 3\left(x^2 + \frac{4}{3}xy + \frac{4}{9}y^2\right) - 3 \cdot \frac{4}{9}y^2 + 2y^2
$$

$$
= 3\left(x + \frac{2}{3}y\right)^2 - \frac{4}{3}y^2 + 2y^2
= 3\left(x + \frac{2}{3}y\right)^2 + \frac{2}{3}y^2
$$

Both coefficients are positive, confirming $Q$ is positive definite.

---

### Exercise 6: Maximum of Quadratic Form on Unit Sphere

**Problem:**
Find the maximum and minimum of $Q(\mathbf{x}) = 3x_1^2 + 2x_1x_2 + 3x_2^2$ on the unit circle $x_1^2 + x_2^2 = 1$.

**Solution:**
Matrix: $A = \begin{bmatrix} 3 & 1 \\ 1 & 3 \end{bmatrix}$.

Eigenvalues: $(3-\lambda)^2 - 1 = \lambda^2 - 6\lambda + 8 = (\lambda - 4)(\lambda - 2)$.
$\lambda_{\max} = 4$, $\lambda_{\min} = 2$.

Maximum of $Q$ on $\|\mathbf{x}\| = 1$ is $\lambda_{\max} = 4$, minimum is $\lambda_{\min} = 2$.

The eigenvectors give the directions: $(1, 1)/\sqrt{2}$ for $\lambda = 4$, $(1, -1)/\sqrt{2}$ for $\lambda = 2$.

---

### Exercise 7: Leading Principal Minors (3x3)

**Problem:**
For what values of $k$ is $A = \begin{bmatrix} 2 & 1 & 0 \\ 1 & k & 0 \\ 0 & 0 & 5 \end{bmatrix}$ positive definite?

**Solution:**
Leading principal minors:

$\det(A_1) = 2 > 0$ (always).

$\det(A_2) = 2k - 1 = 0 \Rightarrow k = \frac{1}{2}$.

$\det(A_3) = \det(A) = 5 \cdot \det(A_2) = 5(2k - 1)$.

For $A$ positive definite: $\det(A_2) > 0 \Rightarrow k > \frac{1}{2}$, and $\det(A_3) > 0 \Rightarrow 5(2k - 1) > 0 \Rightarrow k > \frac{1}{2}$.

Thus $k > \frac{1}{2}$.

---

### Exercise 8: Indefinite Quadratic Form

**Problem:**
Show that $Q(x, y) = x^2 - 2xy + y^2 - z^2$ is indefinite.

**Solution:**
Rewrite: $Q = (x - y)^2 - z^2$.

At $(x, y, z) = (1, 1, 0)$: $Q = 0 - 0 = 0$.
At $(x, y, z) = (2, 1, 0)$: $Q = (1)^2 - 0 = 1 > 0$.
At $(x, y, z) = (1, 1, 1)$: $Q = 0 - 1 = -1 < 0$.

Since $Q$ takes both positive and negative values, it is **indefinite**.

---

## Exam Tip: Sylvester's Criterion Pitfalls

Sylvester's criterion applies only to **symmetric** matrices that are either positive definite or negative definite. For negative definiteness, check that the leading principal minors alternate in sign: $\det(A_1) < 0$, $\det(A_2) > 0$, $\det(A_3) < 0$, etc. Never use Sylvester's criterion for semidefiniteness---it can be misleading. Instead, check eigenvalues for semidefinite classification.

---