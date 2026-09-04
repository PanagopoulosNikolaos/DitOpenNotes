# Lecture 01: Systems of Linear Equations and Matrix Algebra

## Context and Grounding
This lecture establishes the algebraic foundations of linear algebra. It develops systematic algorithms for solving arbitrary systems of linear equations via Gaussian and Gauss-Jordan elimination, analyzes coefficient matrices and augmented matrices, and formalizes matrix arithmetic and matrix inversions.

---

## 1. Linear Equations and Systems

### 1.1 Formal Definition
A system of $m$ linear equations in $n$ unknown scalar variables $x_1, x_2, \ldots, x_n$ is expressed as:

$$\begin{cases}
a_{11} x_1 + a_{12} x_2 + \cdots + a_{1n} x_n = b_1 \\
a_{21} x_1 + a_{22} x_2 + \cdots + a_{2n} x_n = b_2 \\
\quad \vdots \\
a_{m1} x_1 + a_{m2} x_2 + \cdots + a_{mn} x_n = b_m
\end{cases}$$

In compact matrix-vector notation:
$$A \mathbf{x} = \mathbf{b}$$
where $A \in \mathbb{R}^{m \times n}$ is the coefficient matrix, $\mathbf{x} \in \mathbb{R}^n$ is the unknown vector, and $\mathbf{b} \in \mathbb{R}^m$ is the constant vector.

### 1.2 Augmented Matrix Representation
The complete system is captured in the augmented matrix $[A \mid \mathbf{b}]$:
$$[A \mid \mathbf{b}] = \left[\begin{array}{cccc|c}
a_{11} & a_{12} & \cdots & a_{1n} & b_1 \\
a_{21} & a_{22} & \cdots & a_{2n} & b_2 \\
\vdots & \vdots & \ddots & \vdots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn} & b_m
\end{array}\right]$$

---

## 2. Row Reduction and Echelon Forms

### 2.1 Elementary Row Operations (EROs)
Applying EROs preserves the solution space of the linear system:
1. **Row Swap ($R_i \leftrightarrow R_j$)**: Interchange two rows.
2. **Row Scaling ($R_i \leftarrow k R_i, k \neq 0$)**: Multiply all elements in a row by a non-zero scalar.
3. **Row Addition ($R_i \leftarrow R_i + k R_j$)**: Add a scalar multiple of one row to another row.

### 2.2 Row Echelon Form (REF) vs. Reduced Row Echelon Form (RREF)
A matrix is in **Row Echelon Form (REF)** if:
1. All zero rows are at the bottom of the matrix.
2. The leading entry (pivot) of each non-zero row occurs strictly to the right of the pivot in the row above it.
3. All entries in a column below a pivot are zero.

A matrix is in **Reduced Row Echelon Form (RREF)** if, additionally:
4. Every leading pivot entry equals $1$.
5. Each pivot is the sole non-zero entry in its column.

### 2.3 Characterization of Solutions
* **Inconsistent System (0 solutions)**: The echelon form contains a row of the form $[0 \; 0 \; \cdots \; 0 \mid c]$ with $c \neq 0$ ($0 = c$).
* **Unique Solution**: The system is consistent and every column of $A$ contains a pivot (no free variables).
* **Infinitely Many Solutions**: The system is consistent and there is at least one non-pivot column (free variable).

---

## 3. Matrix Algebra and Inverse Matrices

### 3.1 Matrix Multiplication
For $A \in \mathbb{R}^{m \times p}$ and $B \in \mathbb{R}^{p \times n}$, the product $C = AB \in \mathbb{R}^{m \times n}$ has entries:
$$c_{ij} = \sum_{k=1}^{p} a_{ik} b_{kj}$$
Matrix multiplication is associative ($A(BC) = (AB)C$) and distributive, but **generally non-commutative** ($AB \neq BA$).

### 3.2 Transpose and Symmetry
* The transpose $A^T$ swaps rows and columns: $(A^T)_{ij} = A_{ji}$.
* Product transpose property: $(AB)^T = B^T A^T$.
* A square matrix is **symmetric** if $A^T = A$, and **skew-symmetric** if $A^T = -A$.

### 3.3 The Matrix Inverse ($A^{-1}$)
A square matrix $A \in \mathbb{R}^{n \times n}$ is **invertible (non-singular)** if there exists $A^{-1} \in \mathbb{R}^{n \times n}$ such that:
$$A A^{-1} = A^{-1} A = I_n$$

#### Gauss-Jordan Inversion Algorithm:
Construct the block matrix $[A \mid I_n]$ and apply EROs until the left block achieves RREF:
$$[A \mid I_n] \xrightarrow{\text{EROs}} [I_n \mid A^{-1}]$$
If the left block cannot be reduced to $I_n$, $A$ is singular and has no inverse.

