# Linear Systems

A system of linear equations consists of $m$ equations in $n$ unknowns. Solving such systems is the central problem of linear algebra. The solution set may contain zero, one, or infinitely many solutions, determined by the structure of the coefficient matrix. The methods of Gaussian elimination and Gauss-Jordan elimination provide systematic algorithms for finding all solutions.

---

## 1. Core Definitions

### 1.1 Linear Equation

A **linear equation** in the variables $x_1, x_2, \ldots, x_n$ is an equation of the form

$$
a_1 x_1 + a_2 x_2 + \cdots + a_n x_n = b
$$

where $a_1, a_2, \ldots, a_n$ and $b$ are real or complex constants, and the $x_i$ appear only to the first power.

### 1.2 System of Linear Equations

A **system of $m$ linear equations in $n$ unknowns** is written as

$$
\begin{cases}
a_{11} x_1 + a_{12} x_2 + \cdots + a_{1n} x_n = b_1 \\
a_{21} x_1 + a_{22} x_2 + \cdots + a_{2n} x_n = b_2 \\
\quad\vdots \\
a_{m1} x_1 + a_{m2} x_2 + \cdots + a_{mn} x_n = b_m
\end{cases}
$$

In matrix form:

$$
A \mathbf{x} = \mathbf{b}
$$

where $A \in \mathbb{R}^{m \times n}$ is the coefficient matrix, $\mathbf{x} \in \mathbb{R}^n$ is the vector of unknowns, and $\mathbf{b} \in \mathbb{R}^m$ is the right-hand side vector.

### 1.3 Homogeneous vs. Non-Homogeneous Systems

- **Homogeneous:** $\mathbf{b} = \mathbf{0}$, i.e., $A\mathbf{x} = \mathbf{0}$. Always has at least the trivial solution $\mathbf{x} = \mathbf{0}$.
- **Non-homogeneous:** $\mathbf{b} \neq \mathbf{0}$, i.e., $A\mathbf{x} = \mathbf{b}$.

---

## 2. Solution Structure

### 2.1 Existence and Uniqueness

A linear system has either:
- **No solution** (inconsistent system)
- **Exactly one solution** (consistent system with full rank)
- **Infinitely many solutions** (consistent system with free variables)

### 2.2 Geometric Interpretation

In $\mathbb{R}^2$, each equation represents a line. The solution set is their intersection: a point (unique solution), a line (infinitely many), or empty (parallel lines). In $\mathbb{R}^3$, each equation represents a plane.

---

## 3. Gaussian Elimination (Row Echelon Form)

### 3.1 Elementary Row Operations

Three operations that preserve the solution set:

1. **Swap** two rows: $R_i \leftrightarrow R_j$
2. **Scale** a row by a non-zero constant: $R_i \rightarrow cR_i$, $c \neq 0$
3. **Add a multiple** of one row to another: $R_i \rightarrow R_i + cR_j$

### 3.2 Row Echelon Form (REF)

A matrix is in **row echelon form** when:
- All non-zero rows are above any rows of all zeros.
- The leading coefficient (pivot) of a non-zero row is strictly to the right of the pivot of the row above it.
- All entries below a pivot are zero.

### 3.3 Reduced Row Echelon Form (RREF)

Additionally:
- The pivot in each non-zero row is 1.
- Each pivot is the only non-zero entry in its column.

### 3.4 Back Substitution

After obtaining REF, solve from the bottom row upward, substituting known values.

---

## 4. Gauss-Jordan Elimination

The system $[A \mid \mathbf{b}]$ is transformed to $[I \mid \mathbf{x}]$ through row operations. This yields the solution directly without back substitution.

### 4.1 Pivot and Free Variables

- **Pivot variables:** correspond to columns containing pivots.
- **Free variables:** columns without pivots. Their values can be chosen arbitrarily, parameterizing the infinite solution set.

### 4.2 General Solution

For a consistent system, the general solution is

$$
\mathbf{x} = \mathbf{x}_p + \mathbf{x}_h
$$

where $\mathbf{x}_p$ is a particular solution to $A\mathbf{x} = \mathbf{b}$, and $\mathbf{x}_h$ is the general solution to the homogeneous system $A\mathbf{x} = \mathbf{0}$.

---

## 5. Homogeneous Systems

### 5.1 Trivial and Non-Trivial Solutions

- The **trivial solution** is $\mathbf{x} = \mathbf{0}$, always exists.
- A **non-trivial solution** exists iff the system has at least one free variable, i.e., $\text{rank}(A) < n$.

### 5.2 Parametric Form

If $x_3$ is a free variable, write $x_3 = t$, then express $x_1, x_2$ in terms of $t$.

---

## Solved Exercises

### Exercise 1: Solving a 2x2 System by Back Substitution

**Problem:**
Solve the system using Gaussian elimination:

$$
\begin{cases}
2x_1 + 3x_2 = 7 \\
4x_1 - x_2 = 1
\end{cases}
$$

**Solution:**
Write the augmented matrix:

$$
\left[\begin{array}{cc|c}
2 & 3 & 7 \\
4 & -1 & 1
\end{array}\right]
$$

Perform $R_2 \rightarrow R_2 - 2R_1$:

$$
\left[\begin{array}{cc|c}
2 & 3 & 7 \\
0 & -7 & -13
\end{array}\right]
$$

This is in REF. From row 2: $-7x_2 = -13 \Rightarrow x_2 = \frac{13}{7}$.

Back substitute into row 1: $2x_1 + 3\left(\frac{13}{7}\right) = 7 \Rightarrow 2x_1 = 7 - \frac{39}{7} = \frac{49 - 39}{7} = \frac{10}{7} \Rightarrow x_1 = \frac{5}{7}$.

**Solution:** $(x_1, x_2) = \left(\frac{5}{7}, \frac{13}{7}\right)$.

---

### Exercise 2: Gauss-Jordan on a 3x3 System

**Problem:**
Solve using Gauss-Jordan elimination:

$$
\begin{cases}
x_1 + 2x_2 + x_3 = 8 \\
2x_1 - x_2 + x_3 = 3 \\
3x_1 + x_2 - x_3 = 2
\end{cases}
$$

**Solution:**
Augmented matrix:

$$
\left[\begin{array}{ccc|c}
1 & 2 & 1 & 8 \\
2 & -1 & 1 & 3 \\
3 & 1 & -1 & 2
\end{array}\right]
$$

$R_2 \rightarrow R_2 - 2R_1$, $R_3 \rightarrow R_3 - 3R_1$:

$$
\left[\begin{array}{ccc|c}
1 & 2 & 1 & 8 \\
0 & -5 & -1 & -13 \\
0 & -5 & -4 & -22
\end{array}\right]
$$

$R_3 \rightarrow R_3 - R_2$:

$$
\left[\begin{array}{ccc|c}
1 & 2 & 1 & 8 \\
0 & -5 & -1 & -13 \\
0 & 0 & -3 & -9
\end{array}\right]
$$

Divide rows: $R_2 \rightarrow -\frac{1}{5}R_2$, $R_3 \rightarrow -\frac{1}{3}R_3$:

$$
\left[\begin{array}{ccc|c}
1 & 2 & 1 & 8 \\
0 & 1 & \frac{1}{5} & \frac{13}{5} \\
0 & 0 & 1 & 3
\end{array}\right]
$$

Now back substitute (or eliminate upwards). $R_2 \rightarrow R_2 - \frac{1}{5}R_3$, $R_1 \rightarrow R_1 - R_3$:

$$
\left[\begin{array}{ccc|c}
1 & 2 & 0 & 5 \\
0 & 1 & 0 & 2 \\
0 & 0 & 1 & 3
\end{array}\right]
$$

$R_1 \rightarrow R_1 - 2R_2$:

$$
\left[\begin{array}{ccc|c}
1 & 0 & 0 & 1 \\
0 & 1 & 0 & 2 \\
0 & 0 & 1 & 3
\end{array}\right]
$$

**Solution:** $(x_1, x_2, x_3) = (1, 2, 3)$.

---

### Exercise 3: System with Infinitely Many Solutions

**Problem:**
Solve:

$$
\begin{cases}
x_1 + 2x_2 - x_3 = 1 \\
2x_1 + 4x_2 - 2x_3 = 2 \\
-x_1 - 2x_2 + x_3 = -1
\end{cases}
$$

**Solution:**
Augmented matrix:

$$
\left[\begin{array}{ccc|c}
1 & 2 & -1 & 1 \\
2 & 4 & -2 & 2 \\
-1 & -2 & 1 & -1
\end{array}\right]
$$

$R_2 \rightarrow R_2 - 2R_1$, $R_3 \rightarrow R_3 + R_1$:

$$
\left[\begin{array}{ccc|c}
1 & 2 & -1 & 1 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0
\end{array}\right]
$$

The second and third rows are all zeros. Only one equation remains: $x_1 + 2x_2 - x_3 = 1$.

Pivot variables: $x_1$ (column 1 has pivot). Free variables: $x_2$, $x_3$.

Set $x_2 = s$, $x_3 = t$ (free parameters). Then:

$$
x_1 = 1 - 2s + t
$$

**General solution:**

$$
\begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} + s \begin{pmatrix} -2 \\ 1 \\ 0 \end{pmatrix} + t \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix}
$$

---

### Exercise 4: Inconsistent (No Solution) System

**Problem:**
Solve:

$$
\begin{cases}
x_1 + x_2 = 3 \\
2x_1 + 2x_2 = 5
\end{cases}
$$

**Solution:**
Augmented matrix:

$$
\left[\begin{array}{cc|c}
1 & 1 & 3 \\
2 & 2 & 5
\end{array}\right]
$$

$R_2 \rightarrow R_2 - 2R_1$:

$$
\left[\begin{array}{cc|c}
1 & 1 & 3 \\
0 & 0 & -1
\end{array}\right]
$$

The second row translates to $0 = -1$, which is a contradiction. Therefore the system is **inconsistent** and has **no solution**.

---

### Exercise 5: Homogeneous System with Non-Trivial Solution

**Problem:**
Find all solutions to:

$$
\begin{cases}
x_1 + 2x_2 - x_3 = 0 \\
2x_1 + 5x_2 + x_3 = 0 \\
x_1 + x_2 - 4x_3 = 0
\end{cases}
$$

**Solution:**
Augmented matrix (the zero RHS column is usually omitted for homogeneous systems):

$$
\left[\begin{array}{ccc}
1 & 2 & -1 \\
2 & 5 & 1 \\
1 & 1 & -4
\end{array}\right]
$$

$R_2 \rightarrow R_2 - 2R_1$, $R_3 \rightarrow R_3 - R_1$:

$$
\left[\begin{array}{ccc}
1 & 2 & -1 \\
0 & 1 & 3 \\
0 & -1 & -3
\end{array}\right]
$$

$R_3 \rightarrow R_3 + R_2$:

$$
\left[\begin{array}{ccc}
1 & 2 & -1 \\
0 & 1 & 3 \\
0 & 0 & 0
\end{array}\right]
$$

$R_1 \rightarrow R_1 - 2R_2$:

$$
\left[\begin{array}{ccc}
1 & 0 & -7 \\
0 & 1 & 3 \\
0 & 0 & 0
\end{array}\right]
$$

Free variable: $x_3 = t$. Then $x_1 = 7t$, $x_2 = -3t$.

**Solution:**

$$
\begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} = t \begin{pmatrix} 7 \\ -3 \\ 1 \end{pmatrix}
$$

---

### Exercise 6: 4x3 System with Unique Solution

**Problem:**
Solve:

$$
\begin{cases}
x_1 + x_2 + x_3 = 6 \\
2x_1 - x_2 + x_3 = 3 \\
x_1 + 2x_2 - x_3 = 2 \\
3x_1 + x_2 + 2x_3 = 11
\end{cases}
$$

**Solution:**
Augmented matrix:

$$
\left[\begin{array}{ccc|c}
1 & 1 & 1 & 6 \\
2 & -1 & 1 & 3 \\
1 & 2 & -1 & 2 \\
3 & 1 & 2 & 11
\end{array}\right]
$$

$R_2 \rightarrow R_2 - 2R_1$, $R_3 \rightarrow R_3 - R_1$, $R_4 \rightarrow R_4 - 3R_1$:

$$
\left[\begin{array}{ccc|c}
1 & 1 & 1 & 6 \\
0 & -3 & -1 & -9 \\
0 & 1 & -2 & -4 \\
0 & -2 & -1 & -7
\end{array}\right]
$$

Swap $R_2 \leftrightarrow R_3$:

$$
\left[\begin{array}{ccc|c}
1 & 1 & 1 & 6 \\
0 & 1 & -2 & -4 \\
0 & -3 & -1 & -9 \\
0 & -2 & -1 & -7
\end{array}\right]
$$

$R_3 \rightarrow R_3 + 3R_2$, $R_4 \rightarrow R_4 + 2R_2$:

$$
\left[\begin{array}{ccc|c}
1 & 1 & 1 & 6 \\
0 & 1 & -2 & -4 \\
0 & 0 & -7 & -21 \\
0 & 0 & -5 & -15
\end{array}\right]
$$

$R_3 \rightarrow -\frac{1}{7}R_3$:

$$
\left[\begin{array}{ccc|c}
1 & 1 & 1 & 6 \\
0 & 1 & -2 & -4 \\
0 & 0 & 1 & 3 \\
0 & 0 & -5 & -15
\end{array}\right]
$$

$R_4 \rightarrow R_4 + 5R_3$:

$$
\left[\begin{array}{ccc|c}
1 & 1 & 1 & 6 \\
0 & 1 & -2 & -4 \\
0 & 0 & 1 & 3 \\
0 & 0 & 0 & 0
\end{array}\right]
$$

Back substitute: $x_3 = 3$, from $R_2$: $x_2 - 2(3) = -4 \Rightarrow x_2 = 2$, from $R_1$: $x_1 + 2 + 3 = 6 \Rightarrow x_1 = 1$.

**Solution:** $(x_1, x_2, x_3) = (1, 2, 3)$. The fourth row reduced to $0=0$, consistent.

---

### Exercise 7: Parameterized Family

**Problem:**
For what value(s) of $k$ does the following system have (a) a unique solution, (b) no solution, (c) infinitely many solutions?

$$
\begin{cases}
x + y = 3 \\
2x + ky = 6
\end{cases}
$$

**Solution:**
Augmented matrix:

$$
\left[\begin{array}{cc|c}
1 & 1 & 3 \\
2 & k & 6
\end{array}\right]
$$

$R_2 \rightarrow R_2 - 2R_1$:

$$
\left[\begin{array}{cc|c}
1 & 1 & 3 \\
0 & k-2 & 0
\end{array}\right]
$$

- **Unique solution:** $k - 2 \neq 0 \Rightarrow k \neq 2$. Then $x_2 = 0$, $x_1 = 3$.
- **Infinitely many solutions:** $k - 2 = 0$ and $0 = 0$ (no contradiction), i.e., $k = 2$. Then $x + y = 3$, $y$ free.
- **No solution:** $k - 2 = 0$ and $0 \neq 0$. Since RHS is 0, the case of no solution does not occur here. But if the RHS of row 2 were non-zero, then $k = 2$ would give inconsistency.

---

### Exercise 8: Homogeneous 3x3 with Only Trivial Solution

**Problem:**
Show that the only solution is trivial:

$$
\begin{cases}
x_1 + x_2 = 0 \\
x_1 - x_2 + x_3 = 0 \\
2x_1 + 3x_2 - x_3 = 0
\end{cases}
$$

**Solution:**
Matrix:

$$
\left[\begin{array}{ccc}
1 & 1 & 0 \\
1 & -1 & 1 \\
2 & 3 & -1
\end{array}\right]
$$

$R_2 \rightarrow R_2 - R_1$, $R_3 \rightarrow R_3 - 2R_1$:

$$
\left[\begin{array}{ccc}
1 & 1 & 0 \\
0 & -2 & 1 \\
0 & 1 & -1
\end{array}\right]
$$

$R_3 \rightarrow R_3 + \frac{1}{2}R_2$:

$$
\left[\begin{array}{ccc}
1 & 1 & 0 \\
0 & -2 & 1 \\
0 & 0 & -\frac{1}{2}
\end{array}\right]
$$

All three columns have pivots, so no free variables. Back substitution: $-\frac{1}{2}x_3 = 0 \Rightarrow x_3 = 0$, then $-2x_2 = 0 \Rightarrow x_2 = 0$, then $x_1 = 0$. Only the **trivial solution**.

---

## Exam Tip: Recognizing Free Variables and Consistency

When reducing to REF, two checks determine everything:

- **Consistency:** If any row has the form $[0 \; 0 \; \cdots \; 0 \; | \; c]$ with $c \neq 0$, the system is **inconsistent** -- stop.
- **Free variables:** Count pivots. If $\text{number of pivots} < \text{number of variables}$, the system has free variables. Each free variable introduces one parameter in the general solution.

On exams, systems with free variables often appear with trailing zeros in the RHS (homogeneous-like) or with parameterized coefficients (like Exercise 7). For the latter, set up the augmented matrix, reduce, and consider the critical parameter values that make pivot coefficients zero.

---