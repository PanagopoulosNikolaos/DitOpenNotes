# General Vector Spaces

General vector spaces abstract the key properties of $\mathbb{R}^n$ to arbitrary algebraic structures. A vector space is any set closed under addition and scalar multiplication satisfying ten axioms. This framework unifies seemingly distinct objects---polynomials, matrices, functions---under a single algebraic theory. Within a vector space, the concepts of subspaces, linear independence, basis, and dimension form the foundation for understanding linear transformations and their matrix representations.

---

## 1. Core Definitions

### 1.1 Vector Space Axioms

A **vector space** over a field $\mathbb{F}$ (typically $\mathbb{R}$ or $\mathbb{C}$) is a set $V$ with two operations:

- **Vector addition:** $+: V \times V \to V$
- **Scalar multiplication:** $\cdot: \mathbb{F} \times V \to V$

satisfying for all $\mathbf{u}, \mathbf{v}, \mathbf{w} \in V$ and $c, d \in \mathbb{F}$:

| Axiom | Property |
| :--- | :--- |
| Closure under addition | $\mathbf{u} + \mathbf{v} \in V$ |
| Associativity | $(\mathbf{u} + \mathbf{v}) + \mathbf{w} = \mathbf{u} + (\mathbf{v} + \mathbf{w})$ |
| Commutativity | $\mathbf{u} + \mathbf{v} = \mathbf{v} + \mathbf{u}$ |
| Zero vector | $\exists \mathbf{0} \in V$ such that $\mathbf{v} + \mathbf{0} = \mathbf{v}$ |
| Additive inverse | $\exists (-\mathbf{v}) \in V$ such that $\mathbf{v} + (-\mathbf{v}) = \mathbf{0}$ |
| Closure under scalar multiplication | $c\mathbf{v} \in V$ |
| Distributive (scalar) | $c(\mathbf{u} + \mathbf{v}) = c\mathbf{u} + c\mathbf{v}$ |
| Distributive (vector) | $(c + d)\mathbf{v} = c\mathbf{v} + d\mathbf{v}$ |
| Compatibility | $c(d\mathbf{v}) = (cd)\mathbf{v}$ |
| Identity | $1\mathbf{v} = \mathbf{v}$ |

### 1.2 Examples of Vector Spaces

- $\mathbb{R}^n$: $n$-tuples of real numbers
- $M_{m \times n}(\mathbb{R})$: $m \times n$ matrices
- $P_n$: polynomials of degree at most $n$, $p(t) = a_0 + a_1 t + \cdots + a_n t^n$
- $\mathcal{F}(\mathbb{R})$: real-valued functions on $\mathbb{R}$
- $\mathcal{C}[a, b]$: continuous functions on $[a, b]$

---

## 2. Subspaces

### 2.1 Definition

A non-empty subset $W \subseteq V$ is a **subspace** if:

1. $\mathbf{0} \in W$
2. For all $\mathbf{u}, \mathbf{v} \in W$: $\mathbf{u} + \mathbf{v} \in W$
3. For all $c \in \mathbb{F}$, $\mathbf{v} \in W$: $c\mathbf{v} \in W$

### 2.2 Common Subspaces Associated with a Matrix

For $A \in \mathbb{R}^{m \times n}$:

- **Null space (kernel):** $N(A) = \{\mathbf{x} \in \mathbb{R}^n \mid A\mathbf{x} = \mathbf{0}\}$
- **Column space:** $\text{Col}(A) = \text{span}\{\text{columns of } A\} \subseteq \mathbb{R}^m$
- **Row space:** $\text{Row}(A) = \text{span}\{\text{rows of } A\} \subseteq \mathbb{R}^n$

---

## 3. Linear Independence

### 3.1 Definition

A set of vectors $\{\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_k\} \subset V$ is **linearly independent** if

$$
c_1 \mathbf{v}_1 + c_2 \mathbf{v}_2 + \cdots + c_k \mathbf{v}_k = \mathbf{0}
$$

implies $c_1 = c_2 = \cdots = c_k = 0$. Otherwise, the set is **linearly dependent**.

### 3.2 Testing Linear Independence

- For vectors in $\mathbb{R}^n$: form a matrix and check if $\det(A) \neq 0$ (square case) or if all columns are pivot columns (general case).
- For polynomials or functions: check if the only solution to the linear combination is the trivial one.

---

## 4. Basis and Dimension

### 4.1 Basis

A set $B = \{\mathbf{b}_1, \ldots, \mathbf{b}_n\} \subseteq V$ is a **basis** for $V$ if:

1. $B$ is linearly independent
2. $B$ spans $V$ (every $\mathbf{v} \in V$ is a linear combination of $B$)

### 4.2 Dimension

The **dimension** of $V$, denoted $\dim(V)$, is the number of vectors in any basis. All bases of a finite-dimensional vector space have the same cardinality.

### 4.3 Standard Bases

| Space | Standard Basis | Dimension |
| :--- | :--- | :--- |
| $\mathbb{R}^n$ | $\{\mathbf{e}_1, \ldots, \mathbf{e}_n\}$ | $n$ |
| $M_{m \times n}$ | $\{E_{ij}\}$ (1 at $(i,j)$, 0 elsewhere) | $mn$ |
| $P_n$ | $\{1, t, t^2, \ldots, t^n\}$ | $n+1$ |

---

## 5. Rank and Nullity

### 5.1 Definitions

- **Rank:** $\text{rank}(A) = \dim(\text{Col}(A)) = \dim(\text{Row}(A))$
- **Nullity:** $\text{nullity}(A) = \dim(N(A))$

### 5.2 Rank-Nullity Theorem

For $A \in \mathbb{R}^{m \times n}$:

$$
\text{rank}(A) + \text{nullity}(A) = n
$$

### 5.3 Row Rank Equals Column Rank

The dimension of the row space equals the dimension of the column space.

---

## 6. Change of Basis

### 6.1 Change of Basis Matrix

Let $B = \{\mathbf{b}_1, \ldots, \mathbf{b}_n\}$ and $C = \{\mathbf{c}_1, \ldots, \mathbf{c}_n\}$ be two bases for $V$. The **change of basis matrix** from $B$ to $C$, denoted $P_{C \leftarrow B}$, satisfies:

$$
[\mathbf{v}]_C = P_{C \leftarrow B} [\mathbf{v}]_B
$$

Column $j$ of $P_{C \leftarrow B}$ is $[\mathbf{b}_j]_C$.

### 6.2 Inverse Relationship

$$
P_{B \leftarrow C} = (P_{C \leftarrow B})^{-1}
$$

---

## Solved Exercises

### Exercise 1: Testing Subspace

**Problem:**
Determine whether $W = \{(x, y) \in \mathbb{R}^2 \mid x = 2y\}$ is a subspace of $\mathbb{R}^2$.

**Solution:**
Check the three conditions:

1. **Zero vector:** $(0, 0)$ satisfies $0 = 2 \cdot 0$, so $\mathbf{0} \in W$.
2. **Closure under addition:** Let $\mathbf{u} = (2y_1, y_1)$, $\mathbf{v} = (2y_2, y_2)$. Then $\mathbf{u} + \mathbf{v} = (2(y_1 + y_2), y_1 + y_2)$, which is of the form $(2y, y)$ with $y = y_1 + y_2$. So $\mathbf{u} + \mathbf{v} \in W$.
3. **Closure under scalar multiplication:** For $c \in \mathbb{R}$, $c\mathbf{u} = (2cy_1, cy_1)$, which is of the form $(2y, y)$ with $y = cy_1$. So $c\mathbf{u} \in W$.

All conditions hold. $W$ is a subspace.

---

### Exercise 2: Non-Subspace Example

**Problem:**
Determine whether $W = \{(x, y) \in \mathbb{R}^2 \mid x + y = 1\}$ is a subspace.

**Solution:**
Check: $(0, 0)$ gives $0 + 0 = 0 \neq 1$, so $\mathbf{0} \notin W$. Therefore $W$ is **not** a subspace.

---

### Exercise 3: Linear Independence of Polynomials

**Problem:**
Determine whether $\{1 + t, 1 - t, 2t\}$ in $P_1$ is linearly independent.

**Solution:**
Set $c_1(1 + t) + c_2(1 - t) + c_3(2t) = 0$ (the zero polynomial):

$$
(c_1 + c_2) + (c_1 - c_2 + 2c_3)t = 0 + 0t
$$

This gives the system:

$$
c_1 + c_2 = 0,\quad c_1 - c_2 + 2c_3 = 0
$$

From the first: $c_2 = -c_1$. Substitute into the second:

$$
c_1 + c_1 + 2c_3 = 0 \Rightarrow 2c_1 + 2c_3 = 0 \Rightarrow c_1 = -c_3
$$

A non-trivial solution exists: choose $c_1 = 1$, then $c_2 = -1$, $c_3 = -1$:

$$
1(1 + t) + (-1)(1 - t) + (-1)(2t) = (1 - 1) + (t + t - 2t) = 0
$$

The set is **linearly dependent**.

---

### Exercise 4: Basis for a Null Space

**Problem:**
Find a basis for the null space of $A = \begin{bmatrix} 1 & 2 & -1 \\ 2 & 5 & 1 \end{bmatrix}$.

**Solution:**
Solve $A\mathbf{x} = \mathbf{0}$. Augmented matrix:

$$
\left[\begin{array}{ccc|c}
1 & 2 & -1 & 0 \\
2 & 5 & 1 & 0
\end{array}\right]
$$

$R_2 \rightarrow R_2 - 2R_1$:

$$
\left[\begin{array}{ccc|c}
1 & 2 & -1 & 0 \\
0 & 1 & 3 & 0
\end{array}\right]
$$

$R_1 \rightarrow R_1 - 2R_2$:

$$
\left[\begin{array}{ccc|c}
1 & 0 & -7 & 0 \\
0 & 1 & 3 & 0
\end{array}\right]
$$

Free variable: $x_3 = t$. Then $x_1 = 7t$, $x_2 = -3t$.

Null space: $\{ t(7, -3, 1) \mid t \in \mathbb{R} \}$. A basis: $\{(7, -3, 1)\}$.

---

### Exercise 5: Rank and Nullity

**Problem:**
Find $\text{rank}(A)$ and $\text{nullity}(A)$ for $A = \begin{bmatrix} 1 & 2 & 1 & 0 \\ 2 & 4 & 3 & 1 \\ 3 & 6 & 4 & 1 \end{bmatrix}$.

**Solution:**
Reduce to REF:

$$
\left[\begin{array}{cccc}
1 & 2 & 1 & 0 \\
2 & 4 & 3 & 1 \\
3 & 6 & 4 & 1
\end{array}\right]
$$

$R_2 \rightarrow R_2 - 2R_1$, $R_3 \rightarrow R_3 - 3R_1$:

$$
\left[\begin{array}{cccc}
1 & 2 & 1 & 0 \\
0 & 0 & 1 & 1 \\
0 & 0 & 1 & 1
\end{array}\right]
$$

$R_3 \rightarrow R_3 - R_2$:

$$
\left[\begin{array}{cccc}
1 & 2 & 1 & 0 \\
0 & 0 & 1 & 1 \\
0 & 0 & 0 & 0
\end{array}\right]
$$

Pivot columns: columns 1 and 3. Thus $\text{rank}(A) = 2$.

$\text{nullity}(A) = n - \text{rank}(A) = 4 - 2 = 2$.

---

### Exercise 6: Change of Basis in $\mathbb{R}^2$

**Problem:**
Let $B = \{(1, 1), (1, -1)\}$ and $C = \{(2, 0), (0, 3)\}$. Find $P_{C \leftarrow B}$.

**Solution:**
Express each $B$-vector in the $C$-basis.

For $\mathbf{b}_1 = (1, 1)$: solve $c_1(2, 0) + c_2(0, 3) = (1, 1)$.

$$
2c_1 = 1 \Rightarrow c_1 = \frac{1}{2},\quad 3c_2 = 1 \Rightarrow c_2 = \frac{1}{3}
$$

So $[\mathbf{b}_1]_C = \left(\frac{1}{2}, \frac{1}{3}\right)$.

For $\mathbf{b}_2 = (1, -1)$: $2c_1 = 1 \Rightarrow c_1 = \frac{1}{2}$, $3c_2 = -1 \Rightarrow c_2 = -\frac{1}{3}$.

So $[\mathbf{b}_2]_C = \left(\frac{1}{2}, -\frac{1}{3}\right)$.

Thus:

$$
P_{C \leftarrow B} = \begin{bmatrix}
\frac{1}{2} & \frac{1}{2} \\
\frac{1}{3} & -\frac{1}{3}
\end{bmatrix}
$$

---

### Exercise 7: Basis for a Polynomial Space

**Problem:**
Determine whether $B = \{1 - t, 1 + t^2, t - t^2\}$ is a basis for $P_2$.

**Solution:**
Check linear independence. Set:

$$
c_1(1 - t) + c_2(1 + t^2) + c_3(t - t^2) = 0
$$

Group by powers:

$$
(c_1 + c_2) + (-c_1 + c_3)t + (c_2 - c_3)t^2 = 0
$$

System:

$$
c_1 + c_2 = 0,\quad -c_1 + c_3 = 0,\quad c_2 - c_3 = 0
$$

From $c_2 = c_3$ and $c_1 = c_3$, the first gives $c_3 + c_3 = 2c_3 = 0 \Rightarrow c_3 = 0$. Thus $c_1 = c_2 = c_3 = 0$. The set is linearly independent.

Since $P_2$ has dimension 3, any set of 3 linearly independent vectors forms a basis. $B$ is a basis for $P_2$.

---

### Exercise 8: Column Space Basis

**Problem:**
Find a basis for $\text{Col}(A)$ where $A = \begin{bmatrix} 1 & 2 & 0 \\ 2 & 4 & 1 \\ 0 & 0 & 2 \end{bmatrix}$.

**Solution:**
Reduce to REF:

$$
\left[\begin{array}{ccc}
1 & 2 & 0 \\
2 & 4 & 1 \\
0 & 0 & 2
\end{array}\right]
$$

$R_2 \rightarrow R_2 - 2R_1$:

$$
\left[\begin{array}{ccc}
1 & 2 & 0 \\
0 & 0 & 1 \\
0 & 0 & 2
\end{array}\right]
$$

$R_3 \rightarrow R_3 - 2R_2$:

$$
\left[\begin{array}{ccc}
1 & 2 & 0 \\
0 & 0 & 1 \\
0 & 0 & 0
\end{array}\right]
$$

Pivot columns: columns 1 and 3. A basis for $\text{Col}(A)$ consists of the corresponding columns from the original matrix:

$$
\left\{ \begin{pmatrix} 1 \\ 2 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \\ 2 \end{pmatrix} \right\}
$$

---

## Exam Tip: Identifying Pivot vs. Free Variables

When finding bases for column space and null space:

- **Column space basis:** take the original columns corresponding to pivot columns in REF.
- **Null space basis:** solve for pivot variables in terms of free variables; assign one free variable to 1 and the rest to 0 for each basis vector.

This distinction is frequently tested. Do not use the REF columns for column space basis --- use the original matrix columns.

---