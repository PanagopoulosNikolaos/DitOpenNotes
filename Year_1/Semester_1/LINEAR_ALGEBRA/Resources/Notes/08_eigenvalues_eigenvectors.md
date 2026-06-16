# Eigenvalues and Eigenvectors

Eigenvalues and eigenvectors reveal the intrinsic structure of a linear transformation. An eigenvector is a non-zero vector that, when transformed, scales by a factor called the eigenvalue. This decomposition diagonalizes a matrix when enough eigenvectors exist, providing the simplest possible representation of the transformation. The spectral theorem guarantees that real symmetric matrices are always orthogonally diagonalizable, a result with profound implications in optimization, data analysis, and differential equations.

---

## 1. Core Definitions

### 1.1 Eigenvalue and Eigenvector

For a square matrix $A \in \mathbb{R}^{n \times n}$, a non-zero vector $\mathbf{v} \in \mathbb{C}^n$ is an **eigenvector** with **eigenvalue** $\lambda \in \mathbb{C}$ if:

$$
A\mathbf{v} = \lambda \mathbf{v}, \quad \mathbf{v} \neq \mathbf{0}
$$

### 1.2 Characteristic Equation

$$
\det(A - \lambda I) = 0
$$

The polynomial $p(\lambda) = \det(A - \lambda I)$ is the **characteristic polynomial** of degree $n$.

---

## 2. Finding Eigenvalues and Eigenvectors

### 2.1 Procedure

1. Compute $p(\lambda) = \det(A - \lambda I)$.
2. Solve $p(\lambda) = 0$ for eigenvalues $\lambda$.
3. For each $\lambda$, solve $(A - \lambda I)\mathbf{v} = \mathbf{0}$ for eigenvectors.

### 2.2 Eigenspace

The **eigenspace** corresponding to $\lambda$ is:

$$
E_\lambda = \ker(A - \lambda I) = \{\mathbf{v} \mid (A - \lambda I)\mathbf{v} = \mathbf{0}\}
$$

### 2.3 Multiplicities

- **Algebraic multiplicity:** multiplicity of $\lambda$ as a root of $p(\lambda)$.
- **Geometric multiplicity:** $\dim(E_\lambda)$.

Always: $1 \leq \text{geometric multiplicity} \leq \text{algebraic multiplicity}$.

---

## 3. Properties of Eigenvalues

| Property | Formula |
| :--- | :--- |
| Trace | $\sum \lambda_i = \text{tr}(A)$ |
| Determinant | $\prod \lambda_i = \det(A)$ |
| Triangular matrix | Eigenvalues are the diagonal entries |
| $A^{-1}$ (if invertible) | Eigenvalues are $1/\lambda_i$ |
| $A^\mathsf{T}$ | Same eigenvalues as $A$ |
| Symmetric $A$ | All eigenvalues are real |
| $A^k$ | Eigenvalues are $\lambda_i^k$ |

---

## 4. Diagonalization

### 4.1 Definition

$A$ is **diagonalizable** if there exists an invertible $P$ and diagonal $D$ such that:

$$
A = PDP^{-1}
$$

### 4.2 Condition

$A$ is diagonalizable iff $A$ has $n$ linearly independent eigenvectors. Equivalently, the geometric multiplicity of every eigenvalue equals its algebraic multiplicity.

### 4.3 Construction

- Columns of $P$: $n$ linearly independent eigenvectors.
- $D$: corresponding eigenvalues on the diagonal.

### 4.4 Power of a Matrix

If $A = PDP^{-1}$, then:

$$
A^k = PD^k P^{-1}
$$

---

## 5. Orthogonal Diagonalization

### 5.1 Spectral Theorem

Every real symmetric matrix $A$ can be orthogonally diagonalized:

$$
A = QDQ^\mathsf{T}
$$

where $Q$ is orthogonal ($Q^{-1} = Q^\mathsf{T}$) and $D$ is diagonal with real eigenvalues.

### 5.2 Consequences

- Eigenvectors corresponding to distinct eigenvalues are orthogonal.
- A symmetric matrix is always diagonalizable.

---

## Solved Exercises

### Exercise 1: 2x2 Eigenvalues and Eigenvectors

**Problem:**
Find eigenvalues and eigenvectors of $A = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}$.

**Solution:**
Characteristic equation:

$$
\det(A - \lambda I) = \begin{vmatrix} 2-\lambda & 1 \\ 1 & 2-\lambda \end{vmatrix}
= (2-\lambda)^2 - 1 = \lambda^2 - 4\lambda + 3 = (\lambda - 3)(\lambda - 1)
$$

Eigenvalues: $\lambda_1 = 3$, $\lambda_2 = 1$.

For $\lambda = 3$: $(A - 3I)\mathbf{v} = \begin{bmatrix} -1 & 1 \\ 1 & -1 \end{bmatrix}\mathbf{v} = \mathbf{0}$.

$-v_1 + v_2 = 0 \Rightarrow v_2 = v_1$. Eigenvector: $\mathbf{v}_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$.

For $\lambda = 1$: $(A - I)\mathbf{v} = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}\mathbf{v} = \mathbf{0}$.

$v_1 + v_2 = 0 \Rightarrow v_2 = -v_1$. Eigenvector: $\mathbf{v}_2 = \begin{pmatrix} 1 \\ -1 \end{pmatrix}$.

---

### Exercise 2: Diagonalization

**Problem:**
Diagonalize $A = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}$.

**Solution:**
From Exercise 1, $P = \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}$, $D = \begin{bmatrix} 3 & 0 \\ 0 & 1 \end{bmatrix}$.

Compute $P^{-1} = \frac{1}{-2} \begin{bmatrix} -1 & -1 \\ -1 & 1 \end{bmatrix}
= \begin{bmatrix} \frac{1}{2} & \frac{1}{2} \\ \frac{1}{2} & -\frac{1}{2} \end{bmatrix}$.

Verification: $PDP^{-1} = \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}
\begin{bmatrix} 3 & 0 \\ 0 & 1 \end{bmatrix}
\begin{bmatrix} \frac{1}{2} & \frac{1}{2} \\ \frac{1}{2} & -\frac{1}{2} \end{bmatrix}
= \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}
\begin{bmatrix} \frac{3}{2} & \frac{3}{2} \\ \frac{1}{2} & -\frac{1}{2} \end{bmatrix}
= \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix} = A$.

---

### Exercise 3: Power of a Matrix

**Problem:**
Compute $A^{10}$ for $A = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}$.

**Solution:**
Using $A = PDP^{-1}$ from above:

$$
A^{10} = PD^{10}P^{-1} = \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}
\begin{bmatrix} 3^{10} & 0 \\ 0 & 1^{10} \end{bmatrix}
\begin{bmatrix} \frac{1}{2} & \frac{1}{2} \\ \frac{1}{2} & -\frac{1}{2} \end{bmatrix}
$$

$3^{10} = 59049$.

$$
A^{10} = \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}
\begin{bmatrix} 59049 & 0 \\ 0 & 1 \end{bmatrix}
\begin{bmatrix} \frac{1}{2} & \frac{1}{2} \\ \frac{1}{2} & -\frac{1}{2} \end{bmatrix}
$$

$$
= \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}
\begin{bmatrix} \frac{59049}{2} & \frac{59049}{2} \\ \frac{1}{2} & -\frac{1}{2} \end{bmatrix}
= \begin{bmatrix}
\frac{59050}{2} & \frac{59048}{2} \\
\frac{59048}{2} & \frac{59050}{2}
\end{bmatrix}
= \begin{bmatrix}
29525 & 29524 \\
29524 & 29525
\end{bmatrix}
$$

---

### Exercise 4: 3x3 with Repeated Eigenvalue

**Problem:**
Find eigenvalues and eigenvectors of $A = \begin{bmatrix} 3 & 1 & 0 \\ 0 & 3 & 1 \\ 0 & 0 & 3 \end{bmatrix}$.

**Solution:**
Since $A$ is upper triangular, eigenvalues are the diagonal entries: $\lambda = 3$ (algebraic multiplicity 3).

Eigenvectors: solve $(A - 3I)\mathbf{v} = \mathbf{0}$:

$$
\begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{bmatrix}
\begin{pmatrix} v_1 \\ v_2 \\ v_3 \end{pmatrix} = \mathbf{0}
$$

$v_2 = 0$, $v_3 = 0$, $v_1$ free. Eigenvectors are $\begin{pmatrix} t \\ 0 \\ 0 \end{pmatrix}$.

Geometric multiplicity: 1. Since geometric multiplicity < algebraic multiplicity, $A$ is **not diagonalizable**.

---

### Exercise 5: Orthogonal Diagonalization

**Problem:**
Orthogonally diagonalize $A = \begin{bmatrix} 7 & 2 \\ 2 & 4 \end{bmatrix}$.

**Solution:**
$A$ is symmetric, so it is orthogonally diagonalizable.

Characteristic: $\det(A - \lambda I) = (7-\lambda)(4-\lambda) - 4 = \lambda^2 - 11\lambda + 24
= (\lambda - 8)(\lambda - 3)$.

$\lambda_1 = 8$, $\lambda_2 = 3$.

For $\lambda = 8$: $(A - 8I) = \begin{bmatrix} -1 & 2 \\ 2 & -4 \end{bmatrix}$.
$-v_1 + 2v_2 = 0 \Rightarrow v_1 = 2v_2$. $\mathbf{v}_1 = (2, 1)$. Normalize: $\mathbf{q}_1 = \left(\frac{2}{\sqrt{5}}, \frac{1}{\sqrt{5}}\right)$.

For $\lambda = 3$: $(A - 3I) = \begin{bmatrix} 4 & 2 \\ 2 & 1 \end{bmatrix}$.
$4v_1 + 2v_2 = 0 \Rightarrow v_2 = -2v_1$. $\mathbf{v}_2 = (1, -2)$. Normalize: $\mathbf{q}_2 = \left(\frac{1}{\sqrt{5}}, -\frac{2}{\sqrt{5}}\right)$.

Check orthogonality: $\mathbf{q}_1 \cdot \mathbf{q}_2 = \frac{2}{\sqrt{5}} \cdot \frac{1}{\sqrt{5}} + \frac{1}{\sqrt{5}} \cdot \left(-\frac{2}{\sqrt{5}}\right) = \frac{2}{5} - \frac{2}{5} = 0$.

$Q = \begin{bmatrix} \frac{2}{\sqrt{5}} & \frac{1}{\sqrt{5}} \\ \frac{1}{\sqrt{5}} & -\frac{2}{\sqrt{5}} \end{bmatrix}$, $D = \begin{bmatrix} 8 & 0 \\ 0 & 3 \end{bmatrix}$.

---

### Exercise 6: Trace and Determinant from Eigenvalues

**Problem:**
A $3 \times 3$ matrix $A$ has eigenvalues $\lambda = 2, -1, 5$. Find $\det(A)$ and $\text{tr}(A)$.

**Solution:**
$\det(A) = \prod \lambda_i = 2 \cdot (-1) \cdot 5 = -10$.

$\text{tr}(A) = \sum \lambda_i = 2 + (-1) + 5 = 6$.

---

### Exercise 7: Eigenvalues of $A^{-1}$

**Problem:**
If $\lambda = 4$ is an eigenvalue of $A$ with eigenvector $\mathbf{v}$, find the corresponding eigenvalue of $A^{-1}$.

**Solution:**
$A\mathbf{v} = 4\mathbf{v}$. Multiply both sides by $A^{-1}$:

$\mathbf{v} = 4 A^{-1}\mathbf{v} \Rightarrow A^{-1}\mathbf{v} = \frac{1}{4}\mathbf{v}$.

The eigenvalue of $A^{-1}$ is $\frac{1}{4}$.

---

### Exercise 8: Symmetric Matrix with Distinct Eigenvalues

**Problem:**
Verify that the eigenvectors of $A = \begin{bmatrix} 1 & 2 \\ 2 & -2 \end{bmatrix}$ corresponding to distinct eigenvalues are orthogonal.

**Solution:**
Characteristic: $(1-\lambda)(-2-\lambda) - 4 = \lambda^2 + \lambda - 6 = (\lambda + 3)(\lambda - 2)$.

$\lambda_1 = 2$: $(A - 2I) = \begin{bmatrix} -1 & 2 \\ 2 & -4 \end{bmatrix}$. $-v_1 + 2v_2 = 0 \Rightarrow v_1 = 2v_2$. $\mathbf{v}_1 = (2, 1)$.

$\lambda_2 = -3$: $(A + 3I) = \begin{bmatrix} 4 & 2 \\ 2 & 1 \end{bmatrix}$. $4v_1 + 2v_2 = 0 \Rightarrow v_2 = -2v_1$. $\mathbf{v}_2 = (1, -2)$.

Dot product: $\mathbf{v}_1 \cdot \mathbf{v}_2 = 2 \cdot 1 + 1 \cdot (-2) = 2 - 2 = 0$. Orthogonal.

---

## Exam Tip: Recognizing Non-Diagonalizable Matrices

A matrix is non-diagonalizable when the geometric multiplicity of some eigenvalue is less than its algebraic multiplicity. The most common exam examples are Jordan blocks: triangular matrices with repeated eigenvalues and only one eigenvector per block. Check diagonalizability by counting $\dim(E_\lambda)$; if it matches the algebraic multiplicity for all eigenvalues, the matrix is diagonalizable.

---