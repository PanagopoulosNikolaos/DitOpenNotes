# Lecture 04: Eigenvalues, Eigenvectors, and Matrix Diagonalization

## Context and Grounding
This lecture addresses the spectral theory of linear operators. It examines the eigenvalue problem $A\mathbf{x} = \lambda \mathbf{x}$, characteristic polynomials, eigenspace decomposition, algebraic versus geometric multiplicity, conditions for similarity diagonalization, and the Spectral Theorem for real symmetric matrices.

---

## 1. The Eigenvalue Problem

### 1.1 Formal Definition
Let $A \in \mathbb{R}^{n \times n}$ be a square matrix. A scalar $\lambda \in \mathbb{C}$ is an **eigenvalue** of $A$ if there exists a **non-zero vector** $\mathbf{x} \in \mathbb{C}^n$ ($\mathbf{x} \neq \mathbf{0}$) such that:
$$A \mathbf{x} = \lambda \mathbf{x}$$
The non-zero vector $\mathbf{x}$ is called an **eigenvector** of $A$ corresponding to $\lambda$.

### 1.2 The Characteristic Equation
Rearranging the eigenvalue definition gives the homogeneous system:
$$(A - \lambda I_n) \mathbf{x} = \mathbf{0}$$
Non-trivial solutions ($\mathbf{x} \neq \mathbf{0}$) exist if and only if the matrix $(A - \lambda I_n)$ is singular:
$$\det(A - \lambda I_n) = 0$$
* The expression $p(\lambda) = \det(A - \lambda I_n)$ is a polynomial in $\lambda$ of degree $n$, known as the **characteristic polynomial**.
* The eigenvalues are precisely the roots of the characteristic polynomial.

### 1.3 Eigenspaces
For each eigenvalue $\lambda$, the set of all corresponding eigenvectors together with the zero vector forms a subspace of $\mathbb{R}^n$, termed the **eigenspace** $E_\lambda$:
$$E_\lambda = \text{Null}(A - \lambda I_n)$$

---

## 2. Multiplicities and Diagonalizability

### 2.1 Multiplicity Measures
For any eigenvalue $\lambda_i$:
* **Algebraic Multiplicity ($m_a(\lambda_i)$)**: The multiplicity of $\lambda_i$ as a root of the characteristic polynomial.
* **Geometric Multiplicity ($m_g(\lambda_i)$)**: The dimension of the eigenspace $E_{\lambda_i}$:
  $$m_g(\lambda_i) = \dim(\text{Null}(A - \lambda_i I_n)) = n - \text{rank}(A - \lambda_i I_n)$$
* For all eigenvalues, it always holds that:
  $$1 \le m_g(\lambda_i) \le m_a(\lambda_i)$$

### 2.2 The Diagonalization Theorem
A square matrix $A \in \mathbb{R}^{n \times n}$ is **diagonalizable** (similar to a diagonal matrix $D$) if and only if $A$ possesses $n$ linearly independent eigenvectors:
$$A = P D P^{-1}$$
where:
* $P = [\mathbf{v}_1 \mid \mathbf{v}_2 \mid \cdots \mid \mathbf{v}_n]$ is an invertible modal matrix whose columns are eigenvectors of $A$.
* $D = \text{diag}(\lambda_1, \lambda_2, \ldots, \lambda_n)$ is a diagonal matrix containing the corresponding eigenvalues.

**Diagonalizability Criterion**: $A$ is diagonalizable over $\mathbb{R}$ if and only if:
1. All roots of the characteristic polynomial are real numbers.
2. For every distinct eigenvalue, geometric multiplicity equals algebraic multiplicity:
   $$m_g(\lambda_i) = m_a(\lambda_i)$$

### 2.3 Application: Efficient Matrix Powers
Diagonalization simplifies high powers of a matrix to elementary scalar exponentiation:
$$A^k = (P D P^{-1})^k = P D^k P^{-1}$$
where $D^k = \text{diag}(\lambda_1^k, \lambda_2^k, \ldots, \lambda_n^k)$.

---

## 3. The Spectral Theorem for Symmetric Matrices

A matrix $A \in \mathbb{R}^{n \times n}$ is real symmetric if $A^T = A$.

### 3.1 Spectral Theorem
If $A$ is a real symmetric matrix:
1. All $n$ eigenvalues of $A$ are strictly **real numbers**.
2. Eigenvectors corresponding to distinct eigenvalues are mutually **orthogonal**.
3. $A$ is **orthogonally diagonalizable**: There exists an orthogonal matrix $Q$ ($Q^T Q = I$) and diagonal matrix $D$ such that:
   $$A = Q D Q^T = \sum_{i=1}^n \lambda_i \mathbf{q}_i \mathbf{q}_i^T$$
   where $\{\mathbf{q}_1, \ldots, \mathbf{q}_n\}$ forms an orthonormal basis of eigenvectors for $\mathbb{R}^n$.

### 3.2 Quadratic Forms and Definiteness
A quadratic form $Q(\mathbf{x}) = \mathbf{x}^T A \mathbf{x}$ is:
* **Positive Definite**: $Q(\mathbf{x}) > 0$ for all $\mathbf{x} \neq \mathbf{0} \iff \text{all } \lambda_i > 0$.
* **Positive Semidefinite**: $Q(\mathbf{x}) \ge 0$ for all $\mathbf{x} \iff \text{all } \lambda_i \ge 0$.
* **Negative Definite**: $Q(\mathbf{x}) < 0$ for all $\mathbf{x} \neq \mathbf{0} \iff \text{all } \lambda_i < 0$.
* **Indefinite**: $A$ has both positive and negative eigenvalues.

