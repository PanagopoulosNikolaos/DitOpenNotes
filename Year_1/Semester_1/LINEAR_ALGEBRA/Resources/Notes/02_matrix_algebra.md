# Matrix Algebra

Matrix algebra provides the formal language for expressing and manipulating linear systems. A matrix is a rectangular array of numbers that compactly represents linear transformations. Operations such as addition, multiplication, inversion, and transposition enable solving systems, decomposing transformations, and computing quantities like the determinant. This section covers the definitions, algebraic rules, and key matrix types encountered throughout linear algebra.

---

## 1. Core Definitions

### 1.1 Matrix

A **matrix** $A$ of size $m \times n$ is a rectangular array with $m$ rows and $n$ columns:

$$
A = \begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{bmatrix}
$$

The entry at row $i$, column $j$ is denoted $a_{ij}$ or $A_{ij}$.

### 1.2 Special Types of Matrices

- **Square matrix:** $m = n$
- **Diagonal matrix:** $a_{ij} = 0$ for $i \neq j$, often written $\text{diag}(d_1, d_2, \ldots, d_n)$
- **Identity matrix $I_n$:** diagonal matrix with $d_i = 1$ for all $i$
- **Zero matrix $0_{m \times n}$:** all entries are zero
- **Upper triangular:** $a_{ij} = 0$ for $i > j$
- **Lower triangular:** $a_{ij} = 0$ for $i < j$
- **Symmetric:** $A = A^\mathsf{T}$
- **Skew-symmetric:** $A = -A^\mathsf{T}$

---

## 2. Matrix Operations

### 2.1 Addition and Scalar Multiplication

For $A, B$ of the same size $m \times n$ and scalar $c$:

$$
(A + B)_{ij} = a_{ij} + b_{ij}, \qquad (cA)_{ij} = c \cdot a_{ij}
$$

**Properties:**
- $A + B = B + A$ (commutative)
- $(A + B) + C = A + (B + C)$ (associative)
- $c(A + B) = cA + cB$ (distributive)
- $A + 0 = A$

### 2.2 Matrix Multiplication

If $A$ is $m \times n$ and $B$ is $n \times p$, then $C = AB$ is $m \times p$ with

$$
c_{ij} = \sum_{k=1}^{n} a_{ik} b_{kj}
$$

**Important:** Matrix multiplication is **not commutative**. $AB \neq BA$ in general.

**Properties:**
- $(AB)C = A(BC)$ (associative)
- $A(B + C) = AB + AC$ (left distributive)
- $(B + C)A = BA + CA$ (right distributive)
- $AI = IA = A$

### 2.3 Transpose

The **transpose** of $A$ ($m \times n$) is $A^\mathsf{T}$ ($n \times m$) where $(A^\mathsf{T})_{ij} = A_{ji}$.

**Properties:**
- $(A^\mathsf{T})^\mathsf{T} = A$
- $(A + B)^\mathsf{T} = A^\mathsf{T} + B^\mathsf{T}$
- $(cA)^\mathsf{T} = c A^\mathsf{T}$
- $(AB)^\mathsf{T} = B^\mathsf{T} A^\mathsf{T}$

---

## 3. Inverse Matrix

### 3.1 Definition

A square matrix $A$ is **invertible** (or non-singular) if there exists a matrix $A^{-1}$ such that

$$
A A^{-1} = A^{-1} A = I
$$

If no such matrix exists, $A$ is **singular**.

### 3.2 Existence Condition

$A$ is invertible iff $\det(A) \neq 0$.

### 3.3 Inverse of a 2x2 Matrix

For $A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$,

$$
A^{-1} = \frac{1}{ad - bc} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}
$$

provided $ad - bc \neq 0$.

### 3.4 Finding Inverse via Gauss-Jordan

Form the augmented matrix $[A \mid I]$ and apply row operations until the left block is $I$. The right block is $A^{-1}$:

$$
[A \mid I] \xrightarrow{\text{Gauss-Jordan}} [I \mid A^{-1}]
$$

### 3.5 Properties of Inverses

- $(A^{-1})^{-1} = A$
- $(AB)^{-1} = B^{-1} A^{-1}$ (if both invertible)
- $(A^\mathsf{T})^{-1} = (A^{-1})^\mathsf{T}$
- $(cA)^{-1} = \frac{1}{c} A^{-1}$, $c \neq 0$

---

## 4. Elementary Matrices and LU Decomposition

### 4.1 Elementary Matrices

An **elementary matrix** represents a single row operation. Multiplying $A$ on the left by an elementary matrix performs that operation.

- $E_{\text{swap}}$: swaps two rows
- $E_{\text{scale}}$: scales a row by a non-zero constant
- $E_{\text{add}}$: adds a multiple of one row to another

Every elementary matrix is invertible.

### 4.2 LU Decomposition

For a square matrix $A$ without row swaps, there exists a lower triangular $L$ and an upper triangular $U$ such that

$$
A = LU
$$

$L$ has 1s on the diagonal and records the multipliers from Gaussian elimination. $U$ is the REF of $A$.

Solving $A\mathbf{x} = \mathbf{b}$ via LU:
1. Solve $L\mathbf{y} = \mathbf{b}$ (forward substitution)
2. Solve $U\mathbf{x} = \mathbf{y}$ (back substitution)

If row swaps are needed, $PA = LU$ where $P$ is a permutation matrix.

---

## Solved Exercises

### Exercise 1: Matrix Multiplication

**Problem:**
Compute $AB$ for:

$$
A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}, \quad
B = \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix}
$$

**Solution:**
$AB$ is $2 \times 2$. Compute each entry:

$$
c_{11} = 1 \cdot 5 + 2 \cdot 7 = 5 + 14 = 19
$$

$$
c_{12} = 1 \cdot 6 + 2 \cdot 8 = 6 + 16 = 22
$$

$$
c_{21} = 3 \cdot 5 + 4 \cdot 7 = 15 + 28 = 43
$$

$$
c_{22} = 3 \cdot 6 + 4 \cdot 8 = 18 + 32 = 50
$$

$$
AB = \begin{bmatrix} 19 & 22 \\ 43 & 50 \end{bmatrix}
$$

---

### Exercise 2: Non-Commutativity

**Problem:**
Compute $BA$ for the same matrices and compare.

**Solution:**

$$
BA = \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix}
\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}
$$

$$
(BA)_{11} = 5 \cdot 1 + 6 \cdot 3 = 5 + 18 = 23
$$

$$
(BA)_{12} = 5 \cdot 2 + 6 \cdot 4 = 10 + 24 = 34
$$

$$
(BA)_{21} = 7 \cdot 1 + 8 \cdot 3 = 7 + 24 = 31
$$

$$
(BA)_{22} = 7 \cdot 2 + 8 \cdot 4 = 14 + 32 = 46
$$

$$
BA = \begin{bmatrix} 23 & 34 \\ 31 & 46 \end{bmatrix} \neq AB
$$

---

### Exercise 3: Inverse of a 2x2 Matrix

**Problem:**
Find $A^{-1}$ for $A = \begin{bmatrix} 2 & 3 \\ 1 & 4 \end{bmatrix}$.

**Solution:**
Compute $\det(A) = 2 \cdot 4 - 3 \cdot 1 = 8 - 3 = 5 \neq 0$, so $A$ is invertible.

$$
A^{-1} = \frac{1}{5} \begin{bmatrix} 4 & -3 \\ -1 & 2 \end{bmatrix}
= \begin{bmatrix} \frac{4}{5} & -\frac{3}{5} \\ -\frac{1}{5} & \frac{2}{5} \end{bmatrix}
$$

**Verification:**

$$
A A^{-1} = \begin{bmatrix} 2 & 3 \\ 1 & 4 \end{bmatrix}
\begin{bmatrix} \frac{4}{5} & -\frac{3}{5} \\ -\frac{1}{5} & \frac{2}{5} \end{bmatrix}
= \begin{bmatrix} \frac{8}{5} - \frac{3}{5} & -\frac{6}{5} + \frac{6}{5} \\
\frac{4}{5} - \frac{4}{5} & -\frac{3}{5} + \frac{8}{5} \end{bmatrix}
= \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}
$$

---

### Exercise 4: Inverse of a 3x3 via Gauss-Jordan

**Problem:**
Find $A^{-1}$ for $A = \begin{bmatrix} 1 & 1 & 4 \\ 2 & 5 & 1 \\ 1 & 1 & 2 \end{bmatrix}$.

**Solution:**
Form $[A \mid I]$:

$$
\left[\begin{array}{ccc|ccc}
1 & 1 & 4 & 1 & 0 & 0 \\
2 & 5 & 1 & 0 & 1 & 0 \\
1 & 1 & 2 & 0 & 0 & 1
\end{array}\right]
$$

$R_2 \rightarrow R_2 - 2R_1$, $R_3 \rightarrow R_3 - R_1$:

$$
\left[\begin{array}{ccc|ccc}
1 & 1 & 4 & 1 & 0 & 0 \\
0 & 3 & -7 & -2 & 1 & 0 \\
0 & 0 & -2 & -1 & 0 & 1
\end{array}\right]
$$

$R_2 \rightarrow \frac{1}{3}R_2$:

$$
\left[\begin{array}{ccc|ccc}
1 & 1 & 4 & 1 & 0 & 0 \\
0 & 1 & -\frac{7}{3} & -\frac{2}{3} & \frac{1}{3} & 0 \\
0 & 0 & -2 & -1 & 0 & 1
\end{array}\right]
$$

$R_1 \rightarrow R_1 - R_2$:

$$
\left[\begin{array}{ccc|ccc}
1 & 0 & \frac{19}{3} & \frac{5}{3} & -\frac{1}{3} & 0 \\
0 & 1 & -\frac{7}{3} & -\frac{2}{3} & \frac{1}{3} & 0 \\
0 & 0 & -2 & -1 & 0 & 1
\end{array}\right]
$$

$R_3 \rightarrow -\frac{1}{2}R_3$:

$$
\left[\begin{array}{ccc|ccc}
1 & 0 & \frac{19}{3} & \frac{5}{3} & -\frac{1}{3} & 0 \\
0 & 1 & -\frac{7}{3} & -\frac{2}{3} & \frac{1}{3} & 0 \\
0 & 0 & 1 & \frac{1}{2} & 0 & -\frac{1}{2}
\end{array}\right]
$$

$R_1 \rightarrow R_1 - \frac{19}{3}R_3$, $R_2 \rightarrow R_2 + \frac{7}{3}R_3$:

$$
\left[\begin{array}{ccc|ccc}
1 & 0 & 0 & -\frac{3}{2} & -\frac{1}{3} & \frac{19}{6} \\
0 & 1 & 0 & \frac{1}{2} & \frac{1}{3} & -\frac{7}{6} \\
0 & 0 & 1 & \frac{1}{2} & 0 & -\frac{1}{2}
\end{array}\right]
$$

Thus:

$$
A^{-1} = \begin{bmatrix}
-\frac{3}{2} & -\frac{1}{3} & \frac{19}{6} \\
\frac{1}{2} & \frac{1}{3} & -\frac{7}{6} \\
\frac{1}{2} & 0 & -\frac{1}{2}
\end{bmatrix}
$$

---

### Exercise 5: Inverse of a Diagonal Matrix

**Problem:**
Find the inverse of $D = \begin{bmatrix} 2 & 0 & 0 \\ 0 & -3 & 0 \\ 0 & 0 & 5 \end{bmatrix}$.

**Solution:**
The inverse of a diagonal matrix is the diagonal matrix of reciprocals:

$$
D^{-1} = \begin{bmatrix}
\frac{1}{2} & 0 & 0 \\
0 & -\frac{1}{3} & 0 \\
0 & 0 & \frac{1}{5}
\end{bmatrix}
$$

**Verification:** $D D^{-1} = I_3$.

---

### Exercise 6: Singular Matrix

**Problem:**
Show that $A = \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}$ is singular.

**Solution:**
Compute $\det(A) = 1 \cdot 4 - 2 \cdot 2 = 4 - 4 = 0$. Since $\det(A) = 0$, $A$ is not invertible. Indeed, the rows are linearly dependent: $R_2 = 2R_1$.

---

### Exercise 7: Transpose Properties

**Problem:**
Verify $(AB)^\mathsf{T} = B^\mathsf{T} A^\mathsf{T}$ for

$$
A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix},\quad
B = \begin{bmatrix} 0 & 1 \\ 2 & 3 \end{bmatrix}
$$

**Solution:**
First compute $AB$:

$$
AB = \begin{bmatrix} 1\cdot0+2\cdot2 & 1\cdot1+2\cdot3 \\ 3\cdot0+4\cdot2 & 3\cdot1+4\cdot3 \\ 5\cdot0+6\cdot2 & 5\cdot1+6\cdot3 \end{bmatrix}
= \begin{bmatrix} 4 & 7 \\ 8 & 15 \\ 12 & 23 \end{bmatrix}
$$

$(AB)^\mathsf{T} = \begin{bmatrix} 4 & 8 & 12 \\ 7 & 15 & 23 \end{bmatrix}$.

Now compute $B^\mathsf{T} A^\mathsf{T}$:

$$
B^\mathsf{T} = \begin{bmatrix} 0 & 2 \\ 1 & 3 \end{bmatrix},\quad
A^\mathsf{T} = \begin{bmatrix} 1 & 3 & 5 \\ 2 & 4 & 6 \end{bmatrix}
$$

$$
B^\mathsf{T} A^\mathsf{T} = \begin{bmatrix}
0\cdot1+2\cdot2 & 0\cdot3+2\cdot4 & 0\cdot5+2\cdot6 \\
1\cdot1+3\cdot2 & 1\cdot3+3\cdot4 & 1\cdot5+3\cdot6
\end{bmatrix}
= \begin{bmatrix} 4 & 8 & 12 \\ 7 & 15 & 23 \end{bmatrix}
$$

They match, verifying the identity.

---

### Exercise 8: LU Decomposition

**Problem:**
Find the LU decomposition of $A = \begin{bmatrix} 2 & 1 \\ 4 & 5 \end{bmatrix}$ and solve $A\mathbf{x} = \begin{bmatrix} 3 \\ 11 \end{bmatrix}$.

**Solution:**
Perform Gaussian elimination: subtract $2 \times$ row 1 from row 2 ($\ell_{21} = 2$):

$$
U = \begin{bmatrix} 2 & 1 \\ 0 & 3 \end{bmatrix},\quad
L = \begin{bmatrix} 1 & 0 \\ 2 & 1 \end{bmatrix}
$$

Check: $LU = \begin{bmatrix} 1 & 0 \\ 2 & 1 \end{bmatrix}
\begin{bmatrix} 2 & 1 \\ 0 & 3 \end{bmatrix}
= \begin{bmatrix} 2 & 1 \\ 4 & 5 \end{bmatrix} = A$.

Solve $L\mathbf{y} = \mathbf{b}$:

$$
\begin{bmatrix} 1 & 0 \\ 2 & 1 \end{bmatrix}
\begin{bmatrix} y_1 \\ y_2 \end{bmatrix}
= \begin{bmatrix} 3 \\ 11 \end{bmatrix}
\Rightarrow y_1 = 3,\; 2\cdot3 + y_2 = 11 \Rightarrow y_2 = 5
$$

Solve $U\mathbf{x} = \mathbf{y}$:

$$
\begin{bmatrix} 2 & 1 \\ 0 & 3 \end{bmatrix}
\begin{bmatrix} x_1 \\ x_2 \end{bmatrix}
= \begin{bmatrix} 3 \\ 5 \end{bmatrix}
\Rightarrow x_2 = \frac{5}{3},\; 2x_1 + \frac{5}{3} = 3 \Rightarrow 2x_1 = \frac{4}{3} \Rightarrow x_1 = \frac{2}{3}
$$

**Solution:** $\mathbf{x} = \left(\frac{2}{3}, \frac{5}{3}\right)$.

---

## Exam Tip: Invertibility Shortcuts

Three quick ways to detect singular matrices:

1. **Zero determinant:** $\det(A) = 0$ means $A^{-1}$ does not exist.
2. **Linearly dependent rows/columns:** if one row is a multiple of another, $A$ is singular.
3. **Zero row or column:** a row or column of all zeros makes $\det(A) = 0$.

On exams, checking determinants is often the fastest path. For $2 \times 2$ inverses, memorize the formula; for larger matrices, Gauss-Jordan is the standard method.

---