# Determinants

The determinant is a scalar function defined on square matrices that encodes key structural properties. A non-zero determinant indicates an invertible matrix with full rank, while a zero determinant signals singularity and linear dependence. Determinants also appear in volume computations, eigenvalue theory, and the explicit formula for matrix inverses via Cramer's rule.

---

## 1. Core Definitions

### 1.1 Determinant of a Square Matrix

The determinant of $A \in \mathbb{R}^{n \times n}$ is denoted $\det(A)$ or $|A|$. It satisfies:

- For $n=1$: $\det([a]) = a$
- For $n=2$: $\det\begin{pmatrix} a & b \\ c & d \end{pmatrix} = ad - bc$
- For $n \ge 3$: defined via cofactor expansion.

### 1.2 Cofactor Expansion (Laplace Expansion)

Let $A_{ij}$ denote the $(n-1) \times (n-1)$ submatrix obtained by removing row $i$ and column $j$. The **minor** $M_{ij} = \det(A_{ij})$, and the **cofactor** is

$$
C_{ij} = (-1)^{i+j} M_{ij}
$$

The determinant along row $i$:

$$
\det(A) = \sum_{j=1}^{n} a_{ij} C_{ij} = \sum_{j=1}^{n} a_{ij} (-1)^{i+j} M_{ij}
$$

Equivalently along column $j$:

$$
\det(A) = \sum_{i=1}^{n} a_{ij} C_{ij}
$$

---

## 2. Properties of Determinants

### 2.1 Fundamental Rules

| Operation | Effect on $\det(A)$ |
| :--- | :--- |
| Swap two rows | $\det$ changes sign |
| Multiply a row by $c$ | $\det$ multiplied by $c$ |
| Add a multiple of one row to another | $\det$ unchanged |
| $A$ has a zero row | $\det(A) = 0$ |
| $A$ has two identical rows | $\det(A) = 0$ |
| $A$ is triangular | $\det(A) = \prod a_{ii}$ |
| $A$ is diagonal | $\det(A) = \prod a_{ii}$ |

### 2.2 Multiplicative Property

For square matrices $A, B$ of the same size:

$$
\det(AB) = \det(A) \cdot \det(B)
$$

### 2.3 Transpose and Inverse

- $\det(A^\mathsf{T}) = \det(A)$
- $\det(A^{-1}) = \frac{1}{\det(A)}$ (when $A$ is invertible)
- $\det(cA) = c^n \det(A)$ for $A \in \mathbb{R}^{n \times n}$

### 2.4 Block Matrices

For a block triangular matrix:

$$
\det\begin{pmatrix} A & B \\ 0 & C \end{pmatrix} = \det(A) \det(C)
$$

---

## 3. Cramer's Rule

For a system $A\mathbf{x} = \mathbf{b}$ with $\det(A) \neq 0$, each unknown $x_i$ is:

$$
x_i = \frac{\det(A_i)}{\det(A)}
$$

where $A_i$ is $A$ with column $i$ replaced by $\mathbf{b}$.

**Practical note:** Cramer's rule is mainly of theoretical interest and is computationally inefficient for large systems compared to Gaussian elimination.

---

## 4. Adjugate Matrix

The **adjugate** (or classical adjoint) of $A$ is $\text{adj}(A)$, where

$$
\text{adj}(A)_{ij} = C_{ji}
$$

(the transpose of the cofactor matrix). Then:

$$
A^{-1} = \frac{\text{adj}(A)}{\det(A)}
$$

This formula is useful for theoretical derivations but is rarely used in numerical computation.

---

## Solved Exercises

### Exercise 1: Determinant of a 2x2

**Problem:**
Compute $\det(A)$ for $A = \begin{bmatrix} 5 & 2 \\ -3 & 4 \end{bmatrix}$.

**Solution:**
$$
\det(A) = 5 \cdot 4 - 2 \cdot (-3) = 20 + 6 = 26
$$

---

### Exercise 2: Determinant of a 3x3 via Cofactor Expansion

**Problem:**
Compute $\det(A)$ for $A = \begin{bmatrix} 1 & 0 & 2 \\ -1 & 3 & 1 \\ 2 & 1 & -2 \end{bmatrix}$ using expansion along row 1.

**Solution:**
Expand along row 1 ($i = 1$):

$$
\det(A) = a_{11}C_{11} + a_{12}C_{12} + a_{13}C_{13}
$$

$$
C_{11} = (-1)^{1+1} \det\begin{bmatrix} 3 & 1 \\ 1 & -2 \end{bmatrix} = (1)(3 \cdot (-2) - 1 \cdot 1) = -6 - 1 = -7
$$

$$
C_{12} = (-1)^{1+2} \det\begin{bmatrix} -1 & 1 \\ 2 & -2 \end{bmatrix} = (-1)((-1)(-2) - 1 \cdot 2) = -1(2 - 2) = 0
$$

$$
C_{13} = (-1)^{1+3} \det\begin{bmatrix} -1 & 3 \\ 2 & 1 \end{bmatrix} = (1)((-1) \cdot 1 - 3 \cdot 2) = -1 - 6 = -7
$$

$$
\det(A) = 1 \cdot (-7) + 0 \cdot 0 + 2 \cdot (-7) = -7 - 14 = -21
$$

---

### Exercise 3: Triangular Matrix Determinant

**Problem:**
Compute $\det(A)$ for $A = \begin{bmatrix} 2 & 3 & 1 & 0 \\ 0 & -1 & 4 & 2 \\ 0 & 0 & 5 & 1 \\ 0 & 0 & 0 & 3 \end{bmatrix}$.

**Solution:**
Since $A$ is upper triangular, the determinant is the product of the diagonal entries:

$$
\det(A) = 2 \cdot (-1) \cdot 5 \cdot 3 = -30
$$

---

### Exercise 4: Using Row Operations

**Problem:**
Compute $\det(A)$ for $A = \begin{bmatrix} 1 & 2 & 3 \\ 2 & 5 & 7 \\ 3 & 7 & 11 \end{bmatrix}$ by row reducing to triangular form.

**Solution:**
$R_2 \rightarrow R_2 - 2R_1$ (det unchanged):

$$
\begin{vmatrix} 1 & 2 & 3 \\ 0 & 1 & 1 \\ 3 & 7 & 11 \end{vmatrix}
$$

$R_3 \rightarrow R_3 - 3R_1$ (det unchanged):

$$
\begin{vmatrix} 1 & 2 & 3 \\ 0 & 1 & 1 \\ 0 & 1 & 2 \end{vmatrix}
$$

$R_3 \rightarrow R_3 - R_2$ (det unchanged):

$$
\begin{vmatrix} 1 & 2 & 3 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{vmatrix}
$$

Now triangular: $\det(A) = 1 \cdot 1 \cdot 1 = 1$.

---

### Exercise 5: Cramer's Rule for a 2x2 System

**Problem:**
Solve using Cramer's rule:

$$
\begin{cases}
2x + 3y = 7 \\
4x - y = 1
\end{cases}
$$

**Solution:**
$A = \begin{bmatrix} 2 & 3 \\ 4 & -1 \end{bmatrix}$, $\det(A) = 2(-1) - 3(4) = -2 - 12 = -14$.

$$
\det(A_x) = \begin{vmatrix} 7 & 3 \\ 1 & -1 \end{vmatrix} = 7(-1) - 3(1) = -7 - 3 = -10
$$

$$
\det(A_y) = \begin{vmatrix} 2 & 7 \\ 4 & 1 \end{vmatrix} = 2(1) - 7(4) = 2 - 28 = -26
$$

$$
x = \frac{\det(A_x)}{\det(A)} = \frac{-10}{-14} = \frac{5}{7}, \quad
y = \frac{\det(A_y)}{\det(A)} = \frac{-26}{-14} = \frac{13}{7}
$$

Matches the result from Gaussian elimination.

---

### Exercise 6: Cramer's Rule for a 3x3 System

**Problem:**
Solve using Cramer's rule:

$$
\begin{cases}
x_1 + 2x_2 + x_3 = 8 \\
2x_1 - x_2 + x_3 = 3 \\
3x_1 + x_2 - x_3 = 2
\end{cases}
$$

**Solution:**
$A = \begin{bmatrix} 1 & 2 & 1 \\ 2 & -1 & 1 \\ 3 & 1 & -1 \end{bmatrix}$.

Compute $\det(A)$ (expand along row 1):

$$
\det(A) = 1 \cdot \det\begin{bmatrix} -1 & 1 \\ 1 & -1 \end{bmatrix} - 2 \cdot \det\begin{bmatrix} 2 & 1 \\ 3 & -1 \end{bmatrix} + 1 \cdot \det\begin{bmatrix} 2 & -1 \\ 3 & 1 \end{bmatrix}
$$

$$
= 1(1 - 1) - 2(-2 - 3) + 1(2 + 3) = 0 - 2(-5) + 5 = 10 + 5 = 15
$$

$A_1$ (replace column 1 with $\mathbf{b}$):

$$
A_1 = \begin{bmatrix} 8 & 2 & 1 \\ 3 & -1 & 1 \\ 2 & 1 & -1 \end{bmatrix}
$$

$$
\det(A_1) = 8 \cdot \det\begin{bmatrix} -1 & 1 \\ 1 & -1 \end{bmatrix} - 2 \cdot \det\begin{bmatrix} 3 & 1 \\ 2 & -1 \end{bmatrix} + 1 \cdot \det\begin{bmatrix} 3 & -1 \\ 2 & 1 \end{bmatrix}
$$

$$
= 8(1 - 1) - 2(-3 - 2) + 1(3 + 2) = 0 - 2(-5) + 5 = 10 + 5 = 15
$$

$x_1 = 15 / 15 = 1$.

$A_2$ (replace column 2):

$$
A_2 = \begin{bmatrix} 1 & 8 & 1 \\ 2 & 3 & 1 \\ 3 & 2 & -1 \end{bmatrix}
$$

$$
\det(A_2) = 1 \cdot \det\begin{bmatrix} 3 & 1 \\ 2 & -1 \end{bmatrix} - 8 \cdot \det\begin{bmatrix} 2 & 1 \\ 3 & -1 \end{bmatrix} + 1 \cdot \det\begin{bmatrix} 2 & 3 \\ 3 & 2 \end{bmatrix}
$$

$$
= 1(-3 - 2) - 8(-2 - 3) + 1(4 - 9) = -5 - 8(-5) + (-5) = -5 + 40 - 5 = 30
$$

$x_2 = 30 / 15 = 2$.

$A_3$ (replace column 3):

$$
A_3 = \begin{bmatrix} 1 & 2 & 8 \\ 2 & -1 & 3 \\ 3 & 1 & 2 \end{bmatrix}
$$

$$
\det(A_3) = 1 \cdot \det\begin{bmatrix} -1 & 3 \\ 1 & 2 \end{bmatrix} - 2 \cdot \det\begin{bmatrix} 2 & 3 \\ 3 & 2 \end{bmatrix} + 8 \cdot \det\begin{bmatrix} 2 & -1 \\ 3 & 1 \end{bmatrix}
$$

$$
= 1(-2 - 3) - 2(4 - 9) + 8(2 + 3) = -5 - 2(-5) + 8(5) = -5 + 10 + 40 = 45
$$

$x_3 = 45 / 15 = 3$.

**Solution:** $(x_1, x_2, x_3) = (1, 2, 3)$.

---

### Exercise 7: Determinant of a Singular Matrix

**Problem:**
Show that $A = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 5 & 7 & 9 \end{bmatrix}$ is singular.

**Solution:**
Compute $\det(A)$ by row operations. $R_2 \rightarrow R_2 - 4R_1$, $R_3 \rightarrow R_3 - 5R_1$:

$$
\begin{vmatrix} 1 & 2 & 3 \\ 0 & -3 & -6 \\ 0 & -3 & -6 \end{vmatrix}
$$

$R_3 \rightarrow R_3 - R_2$:

$$
\begin{vmatrix} 1 & 2 & 3 \\ 0 & -3 & -6 \\ 0 & 0 & 0 \end{vmatrix} = 0
$$

$\det(A) = 0$, confirming $A$ is singular.

---

### Exercise 8: Effects of Row Operations

**Problem:**
Let $A$ be a $3 \times 3$ matrix with $\det(A) = 4$. Find $\det(B)$ where $B$ is obtained from $A$ by:
(a) swapping rows 1 and 2,
(b) multiplying row 3 by 2,
(c) adding 3 times row 1 to row 2,
(d) performing all three operations sequentially.

**Solution:**
(a) One row swap changes sign: $\det(B_a) = -4$.
(b) One row scaled by 2: $\det(B_b) = 2 \cdot 4 = 8$.
(c) Adding a multiple of one row to another: $\det(B_c) = 4$ (unchanged).
(d) Sequential: swap ($\times -1$), scale ($\times 2$), add ($\times 1$): $\det(B) = 4 \cdot (-1) \cdot 2 \cdot 1 = -8$.

---

## Exam Tip: Strategic Cofactor Expansion

Always expand along the row or column with the most zeros to minimize computation. For example, for

$$
A = \begin{bmatrix}
3 & 0 & 0 & 1 \\
0 & 2 & 0 & 4 \\
1 & 0 & 5 & 0 \\
0 & 0 & 3 & 2
\end{bmatrix}
$$

expanding along column 2 (two zeros) significantly reduces the number of $3 \times 3$ subdeterminants needed. Conversely, never expand along a dense row when a sparse one exists.

---