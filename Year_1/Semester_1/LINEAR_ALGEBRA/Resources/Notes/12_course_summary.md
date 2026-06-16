# Course Summary

This summary integrates the central ideas of linear algebra into a coherent framework, connecting the core concepts of linear systems, vector spaces, eigenvalues, and matrix factorizations. The fundamental relationships---Gaussian elimination linking to rank, rank linking to bases, diagonalization linking to eigenvalues, and factorizations linking to applications---form the backbone of the subject. This section recaps the essential formulas and thematic connections that appear across the entire course.

---

## 1. Central Ideas

### 1.1 The Unified View

Linear algebra revolves around a single equation:

$$
A\mathbf{x} = \mathbf{b}
$$

This equation represents:
- A system of linear equations (Chapter 1)
- A matrix transformation (Chapter 4, 6)
- A data-fitting problem via least squares (Chapter 7)
- A differential system via $d\mathbf{x}/dt = A\mathbf{x}$ (Chapter 11)

### 1.2 Rank-Nullity as the Central Theorem

The rank-nullity theorem $\text{rank}(A) + \text{nullity}(A) = n$ connects:
- The number of pivot columns (rank) with the number of free variables (nullity)
- The dimension of the image with the dimension of the kernel of a linear transformation
- The column space dimension with the null space dimension

### 1.3 Eigenvalues as the "DNA" of a Matrix

For a square matrix $A$, the eigenvalues $\lambda_i$ and eigenvectors $\mathbf{v}_i$ satisfy $A\mathbf{v}_i = \lambda_i \mathbf{v}_i$. They encode:
- The trace: $\sum \lambda_i = \text{tr}(A)$
- The determinant: $\prod \lambda_i = \det(A)$
- Diagonalizability: existence of $n$ independent eigenvectors
- Stability: sign of real parts determines long-term behavior

---

## 2. Essential Formulas

### 2.1 Linear Systems and Matrices

| Concept | Formula |
| :--- | :--- |
| Linear system | $A\mathbf{x} = \mathbf{b}$ |
| Gaussian elimination | $[A \mid \mathbf{b}] \to \text{REF} \to \text{RREF}$ |
| Matrix multiplication | $(AB)_{ij} = \sum_k a_{ik} b_{kj}$ |
| Inverse (2x2) | $A^{-1} = \frac{1}{ad-bc}\begin{bmatrix} d & -b \\ -c & a \end{bmatrix}$ |

### 2.2 Determinants

| Concept | Formula |
| :--- | :--- |
| 2x2 determinant | $\det(A) = ad - bc$ |
| Laplace expansion | $\det(A) = \sum_j a_{ij}(-1)^{i+j}M_{ij}$ |
| Product rule | $\det(AB) = \det(A)\det(B)$ |
| Cramer's rule | $x_i = \det(A_i) / \det(A)$ |

### 2.3 Vector Spaces

| Concept | Formula |
| :--- | :--- |
| Rank-nullity | $\text{rank}(A) + \text{nullity}(A) = n$ |
| Change of basis | $[\mathbf{v}]_C = P_{C \leftarrow B} [\mathbf{v}]_B$ |
| Dot product | $\mathbf{u} \cdot \mathbf{v} = \|\mathbf{u}\|\|\mathbf{v}\|\cos\theta$ |
| Projection | $\text{proj}_{\mathbf{v}}(\mathbf{u}) = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{v}\|^2} \mathbf{v}$ |

### 2.4 Orthogonality and Least Squares

| Concept | Formula |
| :--- | :--- |
| Orthogonal matrix | $Q^\mathsf{T} Q = I$, $Q^{-1} = Q^\mathsf{T}$ |
| Gram-Schmidt | $\mathbf{v}_k = \mathbf{a}_k - \sum_{i < k} \text{proj}_{\mathbf{v}_i}(\mathbf{a}_k)$ |
| Normal equations | $A^\mathsf{T} A \hat{\mathbf{x}} = A^\mathsf{T} \mathbf{b}$ |
| Projection matrix | $P = A(A^\mathsf{T} A)^{-1} A^\mathsf{T}$ |

### 2.5 Eigenvalues

| Concept | Formula |
| :--- | :--- |
| Characteristic equation | $\det(A - \lambda I) = 0$ |
| Diagonalization | $A = PDP^{-1}$ |
| Spectral theorem | $A = QDQ^\mathsf{T}$ (symmetric $A$) |
| Power of matrix | $A^k = PD^k P^{-1}$ |

### 2.6 Factorizations

| Factorization | Form | Applies To |
| :--- | :--- | :--- |
| LU | $A = LU$ | Square invertible |
| QR | $A = QR$ | Any full column rank |
| SVD | $A = U\Sigma V^\mathsf{T}$ | Any matrix |
| Cholesky | $A = LL^\mathsf{T}$ | Symmetric positive definite |

---

## 3. Thematic Connections

### 3.1 Gauss to Eigenvalues

The flow of ideas follows a clear path:

$$
\text{Gaussian elimination} \to \text{rank} \to \text{bases} \to \text{eigenvalues}
$$

Gaussian elimination produces REF, from which we read the rank. The rank determines the dimensions of the fundamental subspaces. Bases for these subspaces lead to eigenvalue problems for square matrices.

### 3.2 Gram-Schmidt to SVD

$$
\text{Gram-Schmidt} \to \text{QR} \to \text{SVD}
$$

Gram-Schmidt orthogonalizes a basis, producing the QR factorization. The QR algorithm powers eigenvalue computation. The SVD generalizes eigenvalue decomposition to non-square matrices.

### 3.3 Diagonalization to Optimization

$$
\text{Diagonalization} \to \text{quadratic forms} \to \text{optimization}
$$

Diagonalizing a symmetric matrix reveals the nature of the corresponding quadratic form. Positive definiteness (all eigenvalues positive) identifies local minima in multivariable calculus optimization problems.

### 3.4 From Theory to Applications

| Theoretical Concept | Application |
| :--- | :--- |
| Eigenvalues | PageRank, stability of ODEs |
| SVD | PCA, image compression, noise reduction |
| Least squares | Linear regression, data fitting |
| LU factorization | Solving systems with multiple RHS |
| Graph Laplacian | Network analysis, spectral clustering |

---

## 4. Key Problem-Solving Strategies

### 4.1 Solving Linear Systems
1. Form the augmented matrix $[A \mid \mathbf{b}]$.
2. Reduce to REF (Gaussian elimination) or RREF (Gauss-Jordan).
3. Check for consistency: no row $[0 \; \cdots \; 0 \mid c]$ with $c \neq 0$.
4. Identify pivot and free variables; write parametric solution.

### 4.2 Finding Bases
- **Column space:** pivot columns of the original matrix.
- **Null space:** solve $A\mathbf{x} = \mathbf{0}$, express pivots in terms of free variables.
- **Row space:** non-zero rows of REF (or original rows corresponding to pivot columns).

### 4.3 Checking Diagonalizability
1. Find eigenvalues by solving $\det(A - \lambda I) = 0$.
2. For each eigenvalue $\lambda$, find $\dim(E_\lambda) = \dim(\ker(A - \lambda I))$.
3. If $\dim(E_\lambda)$ equals the algebraic multiplicity for all $\lambda$, $A$ is diagonalizable.

### 4.4 Computing Matrix Powers
If $A$ is diagonalizable, $A^k = P D^k P^{-1}$. For non-diagonalizable matrices, use the Jordan form or compute directly.

### 4.5 Solving Least Squares
1. Set up $A\hat{\mathbf{x}} \approx \mathbf{b}$ with $A$ containing the feature columns.
2. Compute $A^\mathsf{T} A$ and $A^\mathsf{T} \mathbf{b}$.
3. Solve $A^\mathsf{T} A \hat{\mathbf{x}} = A^\mathsf{T} \mathbf{b}$ (normal equations).

---

## 5. Common Pitfalls

1. **Matrix multiplication order:** $AB \neq BA$ in general. Always verify dimensions match.
2. **Inverse existence:** $\det(A) = 0$ means $A^{-1}$ does not exist. Do not attempt to compute it.
3. **Column space vs. row space:** column space uses original columns of $A$ corresponding to pivot columns; row space uses REF rows.
4. **Eigenvalues of sums:** $\lambda_i(A + B) \neq \lambda_i(A) + \lambda_i(B)$ in general. Only trace and determinant have simple formulas.
5. **Sylvester's criterion:** only applies to symmetric matrices; does not detect semidefiniteness.

---

## Exam Tip: The Big Picture

On a comprehensive exam, identify which of the four main operations the problem requires:

1. **Solve a system** $\to$ Gaussian elimination or LU
2. **Find a basis or dimension** $\to$ REF, pivot columns, rank-nullity
3. **Diagonalize or compute powers** $\to$ eigenvalues, eigenvectors
4. **Approximate or fit data** $\to$ least squares (normal equations) or SVD

Most problems reduce to one of these four tasks. Recognizing the pattern saves time and reduces errors.

---