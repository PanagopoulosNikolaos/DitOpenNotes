# Linear Algebra: Practice Examination 01

**Course**: Linear Algebra (Code: 102)  
**Duration**: 2 Hours  
**Evaluation**: Maximum 100 Points  
**Format**: Closed Book, No Calculators Allowed  

---

## Part A: Multiple Choice and Theoretical Properties (25 Points)

### Question 1 (5 Points)
Let $A$ be an $n \times n$ matrix. Which of the following conditions is **not** equivalent to the statement "$A$ is invertible"?
* A) $\det(A) \neq 0$.
* B) The columns of $A$ form a basis for $\mathbb{R}^n$.
* C) $\text{Nullity}(A) = 1$.
* D) The homogeneous system $A\mathbf{x} = \mathbf{0}$ has only the trivial solution.

### Question 2 (5 Points)
If matrix $A \in \mathbb{R}^{5 \times 7}$ has rank 4, what is the dimension of its null space $\text{Null}(A)$?
* A) 1
* B) 2
* C) 3
* D) 4

### Question 3 (5 Points)
Let $W$ be a 3-dimensional subspace of $\mathbb{R}^5$. What is the dimension of its orthogonal complement $W^\perp$?
* A) 2
* B) 3
* C) 5
* D) 8

### Question 4 (5 Points)
If $\lambda = 3$ is an eigenvalue of an invertible matrix $A$, what is an eigenvalue of $A^{-1}$?
* A) $-3$
* B) $1/3$
* C) $9$
* D) $0$

### Question 5 (5 Points)
For any real symmetric matrix $S = S^T$:
* A) All eigenvalues are strictly complex.
* B) Eigenvectors corresponding to distinct eigenvalues are mutually orthogonal.
* C) The determinant is always strictly positive.
* D) $S$ cannot be diagonalized.

---

## Part B: Linear System Analysis and Inversion (25 Points)

Consider the matrix $A$:
$$A = \begin{bmatrix}
1 & 0 & 2 \\
2 & -1 & 3 \\
4 & 1 & 8
\end{bmatrix}$$
1. Compute $\det(A)$ using cofactor expansion.
2. Determine $A^{-1}$ using the Gauss-Jordan elimination method on the augmented matrix $[A \mid I_3]$.
3. Use $A^{-1}$ to solve $A \mathbf{x} = \mathbf{b}$ for $\mathbf{b} = \begin{bmatrix} 1 \\ 0 \\ 2 \end{bmatrix}$.

---

## Part C: Subspaces and Gram-Schmidt Orthogonalization (25 Points)

Let subspace $W = \text{Span}\{\mathbf{x}_1, \mathbf{x}_2\} \subset \mathbb{R}^3$, where:
$$\mathbf{x}_1 = \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix}, \quad \mathbf{x}_2 = \begin{bmatrix} 1 \\ 0 \\ 2 \end{bmatrix}$$
1. Verify that $\{\mathbf{x}_1, \mathbf{x}_2\}$ is linearly independent.
2. Use the Gram-Schmidt process to transform $\{\mathbf{x}_1, \mathbf{x}_2\}$ into an orthogonal basis $\{\mathbf{v}_1, \mathbf{v}_2\}$ for $W$.
3. Normalize the vectors to obtain an orthonormal basis $\{\mathbf{q}_1, \mathbf{q}_2\}$.
4. Compute the orthogonal projection of $\mathbf{y} = \begin{bmatrix} 2 \\ 4 \\ 1 \end{bmatrix}$ onto subspace $W$.

---

## Part D: Eigenvalue Decomposition and Powers (25 Points)

Given the matrix $M$:
$$M = \begin{bmatrix}
1 & 4 \\
2 & 3
\end{bmatrix}$$
1. Find the characteristic equation and compute all eigenvalues of $M$.
2. Find corresponding eigenvectors and determine whether $M$ is diagonalizable.
3. If diagonalizable, write $M = P D P^{-1}$ and compute the exact matrix $M^5$.

---

## Model Solutions & Marking Rubric

### Part A Solutions
1. **C**: For an invertible $n \times n$ matrix, $\text{Nullity}(A) = 0$, not 1.
2. **C**: By the Rank-Nullity Theorem: $\text{rank}(A) + \text{nullity}(A) = n \implies 4 + \text{nullity}(A) = 7 \implies \text{nullity}(A) = 3$.
3. **A**: In $\mathbb{R}^n$, $\dim(W) + \dim(W^\perp) = n \implies 3 + \dim(W^\perp) = 5 \implies \dim(W^\perp) = 2$.
4. **B**: Since $A\mathbf{x} = \lambda \mathbf{x}$, multiplying by $A^{-1}$ yields $A^{-1}\mathbf{x} = \frac{1}{\lambda}\mathbf{x} = \frac{1}{3}\mathbf{x}$.
5. **B**: By the Spectral Theorem, eigenvectors of real symmetric matrices corresponding to distinct eigenvalues are orthogonal.

### Part B Solution
1. **Determinant**:
   $$\det(A) = 1 \cdot \begin{vmatrix} -1 & 3 \\ 1 & 8 \end{vmatrix} - 0 + 2 \cdot \begin{vmatrix} 2 & -1 \\ 4 & 1 \end{vmatrix}$$
   $$= 1(-8 - 3) + 2(2 - (-4)) = -11 + 2(6) = -11 + 12 = 1$$
   Since $\det(A) = 1 \neq 0$, $A$ is invertible.
2. **Gauss-Jordan Inversion**:
   Applying row operations on $[A \mid I_3]$ yields:
   $$A^{-1} = \begin{bmatrix}
   -11 & 2 & 2 \\
   -4 & 0 & 1 \\
   6 & -1 & -1
   \end{bmatrix}$$
3. **Solving $A\mathbf{x} = \mathbf{b}$**:
   $$\mathbf{x} = A^{-1} \mathbf{b} = \begin{bmatrix}
   -11 & 2 & 2 \\
   -4 & 0 & 1 \\
   6 & -1 & -1
   \end{bmatrix}
   \begin{bmatrix} 1 \\ 0 \\ 2 \end{bmatrix}
   = \begin{bmatrix} -11(1) + 2(0) + 2(2) \\ -4(1) + 0(0) + 1(2) \\ 6(1) - 1(0) - 1(2) \end{bmatrix}
   = \begin{bmatrix} -7 \\ -2 \\ 4 \end{bmatrix}$$

### Part C Solution
1. $\mathbf{x}_1$ and $\mathbf{x}_2$ are not scalar multiples; hence they are linearly independent.
2. **Gram-Schmidt Process**:
   $$\mathbf{v}_1 = \mathbf{x}_1 = \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix}$$
   $$\mathbf{v}_2 = \mathbf{x}_2 - \frac{\mathbf{x}_2 \cdot \mathbf{v}_1}{\mathbf{v}_1 \cdot \mathbf{v}_1} \mathbf{v}_1 = \begin{bmatrix} 1 \\ 0 \\ 2 \end{bmatrix} - \frac{1(1) + 0(1) + 2(0)}{1^2 + 1^2 + 0^2} \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix} = \begin{bmatrix} 1 \\ 0 \\ 2 \end{bmatrix} - \frac{1}{2} \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix} = \begin{bmatrix} 1/2 \\ -1/2 \\ 2 \end{bmatrix}$$
3. **Orthonormal Basis**:
   $$\|\mathbf{v}_1\| = \sqrt{1^2 + 1^2} = \sqrt{2} \implies \mathbf{q}_1 = \begin{bmatrix} 1/\sqrt{2} \\ 1/\sqrt{2} \\ 0 \end{bmatrix}$$
   $$\|\mathbf{v}_2\| = \sqrt{(1/2)^2 + (-1/2)^2 + 2^2} = \sqrt{1/4 + 1/4 + 4} = \sqrt{9/2} = \frac{3}{\sqrt{2}}$$
   $$\mathbf{q}_2 = \frac{\sqrt{2}}{3} \begin{bmatrix} 1/2 \\ -1/2 \\ 2 \end{bmatrix} = \begin{bmatrix} \sqrt{2}/6 \\ -\sqrt{2}/6 \\ 2\sqrt{2}/3 \end{bmatrix}$$
4. **Projection of $\mathbf{y}$**:
   $$\hat{\mathbf{y}} = \frac{\mathbf{y} \cdot \mathbf{v}_1}{\mathbf{v}_1 \cdot \mathbf{v}_1}\mathbf{v}_1 + \frac{\mathbf{y} \cdot \mathbf{v}_2}{\mathbf{v}_2 \cdot \mathbf{v}_2}\mathbf{v}_2$$
   $$\mathbf{y} \cdot \mathbf{v}_1 = 2(1) + 4(1) + 1(0) = 6 \implies \frac{6}{2} \mathbf{v}_1 = 3 \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix} = \begin{bmatrix} 3 \\ 3 \\ 0 \end{bmatrix}$$
   $$\mathbf{y} \cdot \mathbf{v}_2 = 2(1/2) + 4(-1/2) + 1(2) = 1 - 2 + 2 = 1 \implies \frac{1}{9/2} \mathbf{v}_2 = \frac{2}{9} \begin{bmatrix} 1/2 \\ -1/2 \\ 2 \end{bmatrix} = \begin{bmatrix} 1/9 \\ -1/9 \\ 4/9 \end{bmatrix}$$
   $$\hat{\mathbf{y}} = \begin{bmatrix} 3 + 1/9 \\ 3 - 1/9 \\ 0 + 4/9 \end{bmatrix} = \begin{bmatrix} 28/9 \\ 26/9 \\ 4/9 \end{bmatrix}$$

### Part D Solution
1. **Characteristic Polynomial**:
   $$p(\lambda) = \det(M - \lambda I) = \begin{vmatrix} 1 - \lambda & 4 \\ 2 & 3 - \lambda \end{vmatrix} = (1 - \lambda)(3 - \lambda) - 8 = \lambda^2 - 4\lambda - 5 = (\lambda - 5)(\lambda + 1) = 0$$
   Eigenvalues: $\lambda_1 = 5, \quad \lambda_2 = -1$.
2. **Eigenvectors**:
   - For $\lambda_1 = 5$: $(M - 5I)\mathbf{x} = \begin{bmatrix} -4 & 4 \\ 2 & -2 \end{bmatrix} \mathbf{x} = \mathbf{0} \implies x_1 = x_2 \implies \mathbf{v}_1 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$.
   - For $\lambda_2 = -1$: $(M + I)\mathbf{x} = \begin{bmatrix} 2 & 4 \\ 2 & 4 \end{bmatrix} \mathbf{x} = \mathbf{0} \implies x_1 = -2x_2 \implies \mathbf{v}_2 = \begin{bmatrix} -2 \\ 1 \end{bmatrix}$.
   Since the $2 \times 2$ matrix has 2 distinct eigenvalues, $M$ is diagonalizable.
3. **Diagonalization and Powers**:
   $$P = \begin{bmatrix} 1 & -2 \\ 1 & 1 \end{bmatrix}, \quad D = \begin{bmatrix} 5 & 0 \\ 0 & -1 \end{bmatrix}, \quad P^{-1} = \frac{1}{3} \begin{bmatrix} 1 & 2 \\ -1 & 1 \end{bmatrix}$$
   $$M^5 = P D^5 P^{-1} = \begin{bmatrix} 1 & -2 \\ 1 & 1 \end{bmatrix} \begin{bmatrix} 5^5 & 0 \\ 0 & (-1)^5 \end{bmatrix} \frac{1}{3} \begin{bmatrix} 1 & 2 \\ -1 & 1 \end{bmatrix}$$
   $$= \frac{1}{3} \begin{bmatrix} 1 & -2 \\ 1 & 1 \end{bmatrix} \begin{bmatrix} 3125 & 0 \\ 0 & -1 \end{bmatrix} \begin{bmatrix} 1 & 2 \\ -1 & 1 \end{bmatrix} = \frac{1}{3} \begin{bmatrix} 3125 & 2 \\ 3125 & -1 \end{bmatrix} \begin{bmatrix} 1 & 2 \\ -1 & 1 \end{bmatrix} = \begin{bmatrix} 1041 & 2084 \\ 1042 & 2083 \end{bmatrix}$$

