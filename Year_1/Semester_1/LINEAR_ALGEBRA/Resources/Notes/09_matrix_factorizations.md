# Matrix Factorizations

Matrix factorizations (decompositions) express a matrix as a product of simpler matrices, each with special structure. The LU factorization solves linear systems efficiently for multiple right-hand sides. The QR factorization provides a numerically stable approach to least-squares problems and eigenvalue algorithms. The Singular Value Decomposition (SVD) is the most general factorization, applicable to any matrix, and reveals fundamental geometric structure. The Cholesky factorization, specialized for symmetric positive definite matrices, is computationally the most efficient.

---

## 1. LU Factorization

### 1.1 Definition

For a square matrix $A$, if no row swaps are needed during Gaussian elimination:

$$
A = LU
$$

where $L$ is unit lower triangular (1s on diagonal) and $U$ is upper triangular.

### 1.2 Solving Linear Systems

Solve $A\mathbf{x} = \mathbf{b}$ in two steps:

1. **Forward substitution:** $L\mathbf{y} = \mathbf{b}$
2. **Back substitution:** $U\mathbf{x} = \mathbf{y}$

### 1.3 PA = LU

If row swaps (pivoting) are required:

$$
PA = LU
$$

where $P$ is a permutation matrix encoding the row swaps.

---

## 2. QR Factorization

### 2.1 Definition

For an $m \times n$ matrix $A$ with full column rank:

$$
A = QR
$$

where $Q$ is $m \times n$ with orthonormal columns and $R$ is $n \times n$ upper triangular.

### 2.2 Construction via Gram-Schmidt

$Q$ is obtained by orthonormalizing the columns of $A$. $R = Q^\mathsf{T} A$ contains the coefficients.

### 2.3 Applications

- Numerically stable least-squares: solve $R\mathbf{x} = Q^\mathsf{T}\mathbf{b}$.
- QR algorithm for computing eigenvalues.

---

## 3. Singular Value Decomposition (SVD)

### 3.1 Definition

For any $m \times n$ matrix $A$ (real or complex):

$$
A = U \Sigma V^\mathsf{T}
$$

where:
- $U$ is $m \times m$ orthogonal (left singular vectors)
- $V$ is $n \times n$ orthogonal (right singular vectors)
- $\Sigma$ is $m \times n$ diagonal with singular values $\sigma_1 \geq \sigma_2 \geq \cdots \geq \sigma_r \geq 0$, where $r = \text{rank}(A)$.

### 3.2 Relation to Eigenvalues

The singular values satisfy:

$$
\sigma_i = \sqrt{\lambda_i(A^\mathsf{T} A)} = \sqrt{\lambda_i(A A^\mathsf{T})}
$$

Columns of $V$ are eigenvectors of $A^\mathsf{T} A$. Columns of $U$ are eigenvectors of $A A^\mathsf{T}$.

### 3.3 Pseudoinverse

The Moore-Penrose pseudoinverse is:

$$
A^+ = V \Sigma^+ U^\mathsf{T}
$$

where $\Sigma^+$ replaces each non-zero singular value $\sigma_i$ with $\sigma_i^{-1}$.

### 3.4 Applications

- **Best rank-$k$ approximation:** Eckart-Young theorem states that keeping the largest $k$ singular values gives the optimal rank-$k$ approximation.
- **Image compression:** store only the largest singular values and their vectors.
- **Principal Component Analysis (PCA):** centered data matrix decomposed via SVD.
- **Noise reduction:** discard small singular values as noise.

---

## 4. Cholesky Factorization

### 4.1 Definition

For a symmetric positive definite matrix $A$:

$$
A = LL^\mathsf{T}
$$

where $L$ is lower triangular with positive diagonal entries.

### 4.2 Computational Advantage

Cholesky is approximately twice as efficient as LU for symmetric positive definite matrices, requiring about $\frac{n^3}{3}$ flops versus $\frac{2n^3}{3}$ for LU.

### 4.3 Existence

$A$ is symmetric positive definite iff $A = LL^\mathsf{T}$ exists with $L$ having positive diagonal entries.

---

## Solved Exercises

### Exercise 1: LU Factorization (2x2)

**Problem:**
Find the LU factorization of $A = \begin{bmatrix} 3 & 1 \\ 6 & 5 \end{bmatrix}$ and solve $A\mathbf{x} = \begin{pmatrix} 4 \\ 14 \end{pmatrix}$.

**Solution:**
Elimination: subtract $2 \times$ row 1 from row 2 (multiplier $\ell_{21} = 2$):

$$
U = \begin{bmatrix} 3 & 1 \\ 0 & 3 \end{bmatrix},\quad
L = \begin{bmatrix} 1 & 0 \\ 2 & 1 \end{bmatrix}
$$

Forward substitution $L\mathbf{y} = \mathbf{b}$:

$$
\begin{bmatrix} 1 & 0 \\ 2 & 1 \end{bmatrix}
\begin{pmatrix} y_1 \\ y_2 \end{pmatrix}
= \begin{pmatrix} 4 \\ 14 \end{pmatrix}
\Rightarrow y_1 = 4,\; 2\cdot4 + y_2 = 14 \Rightarrow y_2 = 6
$$

Back substitution $U\mathbf{x} = \mathbf{y}$:

$$
\begin{bmatrix} 3 & 1 \\ 0 & 3 \end{bmatrix}
\begin{pmatrix} x_1 \\ x_2 \end{pmatrix}
= \begin{pmatrix} 4 \\ 6 \end{pmatrix}
\Rightarrow x_2 = 2,\; 3x_1 + 2 = 4 \Rightarrow x_1 = \frac{2}{3}
$$

**Solution:** $\mathbf{x} = \left(\frac{2}{3}, 2\right)$.

---

### Exercise 2: LU with Multiple RHS

**Problem:**
Using the LU from Exercise 1, solve $A\mathbf{x} = \begin{pmatrix} 1 \\ 5 \end{pmatrix}$.

**Solution:**
Forward: $y_1 = 1$, $2\cdot1 + y_2 = 5 \Rightarrow y_2 = 3$.

Back: $x_2 = 1$, $3x_1 + 1 = 1 \Rightarrow x_1 = 0$.

**Solution:** $\mathbf{x} = (0, 1)$.

---

### Exercise 3: QR Factorization (2x2)

**Problem:**
Find the QR factorization of $A = \begin{bmatrix} 1 & 2 \\ 2 & 1 \end{bmatrix}$.

**Solution:**
Columns: $\mathbf{a}_1 = (1, 2)$, $\mathbf{a}_2 = (2, 1)$.

Gram-Schmidt: $\mathbf{v}_1 = \mathbf{a}_1 = (1, 2)$. $\|\mathbf{v}_1\| = \sqrt{1^2 + 2^2} = \sqrt{5}$.

$\mathbf{q}_1 = \left(\frac{1}{\sqrt{5}}, \frac{2}{\sqrt{5}}\right)$.

$\text{proj}_{\mathbf{v}_1}(\mathbf{a}_2) = \frac{(2, 1) \cdot (1, 2)}{5} (1, 2) = \frac{4}{5}(1, 2) = \left(\frac{4}{5}, \frac{8}{5}\right)$.

$\mathbf{v}_2 = (2, 1) - \left(\frac{4}{5}, \frac{8}{5}\right) = \left(\frac{6}{5}, -\frac{3}{5}\right)$.

$\|\mathbf{v}_2\| = \sqrt{\frac{36}{25} + \frac{9}{25}} = \sqrt{\frac{45}{25}} = \frac{3\sqrt{5}}{5}$.

$\mathbf{q}_2 = \frac{1}{3\sqrt{5}/5} \left(\frac{6}{5}, -\frac{3}{5}\right) = \left(\frac{2}{\sqrt{5}}, -\frac{1}{\sqrt{5}}\right)$.

$Q = \begin{bmatrix} \frac{1}{\sqrt{5}} & \frac{2}{\sqrt{5}} \\ \frac{2}{\sqrt{5}} & -\frac{1}{\sqrt{5}} \end{bmatrix}$.

$R = Q^\mathsf{T} A = \begin{bmatrix} \|v_1\| & \mathbf{q}_1 \cdot \mathbf{a}_2 \\ 0 & \|v_2\| \end{bmatrix}
= \begin{bmatrix} \sqrt{5} & \frac{4}{\sqrt{5}} \\ 0 & \frac{3\sqrt{5}}{5} \end{bmatrix}$.

---

### Exercise 4: SVD of a 2x2 Matrix

**Problem:**
Find the SVD of $A = \begin{bmatrix} 3 & 0 \\ 0 & 1 \end{bmatrix}$.

**Solution:**
$A$ is already diagonal. Compute $A^\mathsf{T} A = \begin{bmatrix} 9 & 0 \\ 0 & 1 \end{bmatrix}$.

Eigenvalues of $A^\mathsf{T} A$: $\lambda_1 = 9$, $\lambda_2 = 1$.

Singular values: $\sigma_1 = 3$, $\sigma_2 = 1$.

$V = I$ (eigenvectors of $A^\mathsf{T} A$ are standard basis).

$U = I$ (eigenvectors of $A A^\mathsf{T} = A^2$ are also standard basis).

$\Sigma = \begin{bmatrix} 3 & 0 \\ 0 & 1 \end{bmatrix}$.

SVD: $A = I \cdot \Sigma \cdot I^\mathsf{T}$, which is trivially $A = \begin{bmatrix} 3 & 0 \\ 0 & 1 \end{bmatrix}$.

---

### Exercise 5: SVD of a Non-Square Matrix

**Problem:**
Find the SVD of $A = \begin{bmatrix} 1 & 0 \\ 0 & 1 \\ 1 & 1 \end{bmatrix}$.

**Solution:**
$A$ is $3 \times 2$. Compute $A^\mathsf{T} A = \begin{bmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \end{bmatrix}
\begin{bmatrix} 1 & 0 \\ 0 & 1 \\ 1 & 1 \end{bmatrix}
= \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}$.

Eigenvalues of $A^\mathsf{T} A$: $\lambda_1 = 3$, $\lambda_2 = 1$. Singular values: $\sigma_1 = \sqrt{3}$, $\sigma_2 = 1$.

Eigenvectors of $A^\mathsf{T} A$: for $\lambda = 3$, $\mathbf{v}_1 = \left(\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}\right)$; for $\lambda = 1$, $\mathbf{v}_2 = \left(\frac{1}{\sqrt{2}}, -\frac{1}{\sqrt{2}}\right)$.

$V = \begin{bmatrix} \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}} \end{bmatrix}$.

Compute $U$ from $U = A V \Sigma^{-1}$:

$\mathbf{u}_1 = \frac{1}{\sqrt{3}} A \mathbf{v}_1 = \frac{1}{\sqrt{3}} \begin{bmatrix} 1 & 0 \\ 0 & 1 \\ 1 & 1 \end{bmatrix}
\begin{pmatrix} \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \end{pmatrix}
= \frac{1}{\sqrt{3}} \begin{pmatrix} \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \\ \frac{2}{\sqrt{2}} \end{pmatrix}
= \begin{pmatrix} \frac{1}{\sqrt{6}} \\ \frac{1}{\sqrt{6}} \\ \frac{2}{\sqrt{6}} \end{pmatrix}$.

$\mathbf{u}_2 = \frac{1}{1} A \mathbf{v}_2 = \begin{bmatrix} 1 & 0 \\ 0 & 1 \\ 1 & 1 \end{bmatrix}
\begin{pmatrix} \frac{1}{\sqrt{2}} \\ -\frac{1}{\sqrt{2}} \end{pmatrix}
= \begin{pmatrix} \frac{1}{\sqrt{2}} \\ -\frac{1}{\sqrt{2}} \\ 0 \end{pmatrix}$.

$\mathbf{u}_3$ is any unit vector orthogonal to $\mathbf{u}_1$ and $\mathbf{u}_2$; by inspection, $\mathbf{u}_3 = \left(\frac{1}{\sqrt{3}}, \frac{1}{\sqrt{3}}, -\frac{1}{\sqrt{3}}\right)$.

$\Sigma = \begin{bmatrix} \sqrt{3} & 0 \\ 0 & 1 \\ 0 & 0 \end{bmatrix}$.

---

### Exercise 6: Pseudoinverse

**Problem:**
Find the pseudoinverse of $A = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}$.

**Solution:**
$A$ is rank 1. $A^\mathsf{T} A = \begin{bmatrix} 2 & 2 \\ 2 & 2 \end{bmatrix}$ with eigenvalues $\lambda_1 = 4$, $\lambda_2 = 0$.

Singular values: $\sigma_1 = 2$, $\sigma_2 = 0$.

$V$: for $\lambda = 4$, $\mathbf{v}_1 = \left(\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}\right)$; for $\lambda = 0$, $\mathbf{v}_2 = \left(\frac{1}{\sqrt{2}}, -\frac{1}{\sqrt{2}}\right)$.

$U$: $\mathbf{u}_1 = \frac{1}{2} A \mathbf{v}_1 = \frac{1}{2} \begin{pmatrix} \sqrt{2} \\ \sqrt{2} \end{pmatrix} = \left(\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}\right)$.
$\mathbf{u}_2 = \left(\frac{1}{\sqrt{2}}, -\frac{1}{\sqrt{2}}\right)$.

$\Sigma^+ = \begin{bmatrix} \frac{1}{2} & 0 \\ 0 & 0 \end{bmatrix}$.

$A^+ = V \Sigma^+ U^\mathsf{T} = \begin{bmatrix} \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}} \end{bmatrix}
\begin{bmatrix} \frac{1}{2} & 0 \\ 0 & 0 \end{bmatrix}
\begin{bmatrix} \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}} \end{bmatrix}
= \frac{1}{4} \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}$.

Check: $A A^+ A = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}
\frac{1}{4} \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}
\begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}
= \frac{1}{4} \begin{bmatrix} 2 & 2 \\ 2 & 2 \end{bmatrix}
\begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}
= \frac{1}{4} \begin{bmatrix} 4 & 4 \\ 4 & 4 \end{bmatrix}
= \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix} = A$.

---

### Exercise 7: Cholesky Factorization

**Problem:**
Find the Cholesky factorization of $A = \begin{bmatrix} 4 & 2 \\ 2 & 5 \end{bmatrix}$.

**Solution:**
Let $L = \begin{bmatrix} \ell_{11} & 0 \\ \ell_{21} & \ell_{22} \end{bmatrix}$ such that $LL^\mathsf{T} = A$.

$$
\begin{bmatrix} \ell_{11}^2 & \ell_{11}\ell_{21} \\ \ell_{11}\ell_{21} & \ell_{21}^2 + \ell_{22}^2 \end{bmatrix}
= \begin{bmatrix} 4 & 2 \\ 2 & 5 \end{bmatrix}
$$

$\ell_{11}^2 = 4 \Rightarrow \ell_{11} = 2$ (positive).

$\ell_{11}\ell_{21} = 2 \Rightarrow 2\ell_{21} = 2 \Rightarrow \ell_{21} = 1$.

$\ell_{21}^2 + \ell_{22}^2 = 5 \Rightarrow 1 + \ell_{22}^2 = 5 \Rightarrow \ell_{22}^2 = 4 \Rightarrow \ell_{22} = 2$.

$L = \begin{bmatrix} 2 & 0 \\ 1 & 2 \end{bmatrix}$, and $LL^\mathsf{T} = \begin{bmatrix} 2 & 0 \\ 1 & 2 \end{bmatrix}
\begin{bmatrix} 2 & 1 \\ 0 & 2 \end{bmatrix}
= \begin{bmatrix} 4 & 2 \\ 2 & 5 \end{bmatrix} = A$.

---

### Exercise 8: Rank-1 Approximation via SVD

**Problem:**
Find the best rank-1 approximation of $A = \begin{bmatrix} 3 & 0 \\ 0 & 1 \end{bmatrix}$.

**Solution:**
From Exercise 4, the SVD is $A = U \Sigma V^\mathsf{T}$ with $\sigma_1 = 3$, $\sigma_2 = 1$.

The best rank-1 approximation uses only $\sigma_1$:

$$
A_1 = \sigma_1 \mathbf{u}_1 \mathbf{v}_1^\mathsf{T}
$$

$U = I$, so $\mathbf{u}_1 = (1, 0)^\mathsf{T}$. $V = I$, so $\mathbf{v}_1 = (1, 0)^\mathsf{T}$.

$$
A_1 = 3 \begin{pmatrix} 1 \\ 0 \end{pmatrix}
\begin{pmatrix} 1 & 0 \end{pmatrix}
= \begin{bmatrix} 3 & 0 \\ 0 & 0 \end{bmatrix}
$$

This captures the dominant direction of the transformation.

---

## Exam Tip: Choosing the Right Factorization

When solving a problem, pick the factorization based on the matrix structure:

| Matrix Type | Best Factorization | Reason |
| :--- | :--- | :--- |
| General square | LU | Most efficient for single solves |
| Multiple RHS | LU | Reuse $L$ and $U$ |
| Symmetric PD | Cholesky | ~2x faster than LU |
| Overdetermined ($m > n$) | QR | Numerically stable least squares |
| Any matrix | SVD | Most general; reveals rank, null space, column space |
| Data analysis | SVD | PCA, low-rank approximation |

---