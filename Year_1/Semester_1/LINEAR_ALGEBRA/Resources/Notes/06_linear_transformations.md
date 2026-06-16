# Linear Transformations

A linear transformation is a map between vector spaces that preserves the operations of addition and scalar multiplication. This structure-preserving property makes linear transformations the natural morphisms in the category of vector spaces. Every linear transformation corresponds to a matrix once bases are chosen for the domain and codomain, and the kernel-image (rank-nullity) theorem governs the dimensions involved. Isomorphisms, composition, and geometric transformations such as rotation and reflection are special cases within this framework.

---

## 1. Core Definitions

### 1.1 Linear Transformation

Let $V$ and $W$ be vector spaces over $\mathbb{F}$. A map $T: V \to W$ is **linear** if:

1. $T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})$ for all $\mathbf{u}, \mathbf{v} \in V$
2. $T(c\mathbf{u}) = c\,T(\mathbf{u})$ for all $c \in \mathbb{F}$, $\mathbf{u} \in V$

### 1.2 Immediate Consequences

- $T(\mathbf{0}_V) = \mathbf{0}_W$
- $T(-\mathbf{v}) = -T(\mathbf{v})$
- $T(c_1\mathbf{v}_1 + \cdots + c_k\mathbf{v}_k) = c_1 T(\mathbf{v}_1) + \cdots + c_k T(\mathbf{v}_k)$

---

## 2. Kernel and Image

### 2.1 Kernel (Null Space)

$$
\ker(T) = \{\mathbf{v} \in V \mid T(\mathbf{v}) = \mathbf{0}\} \subseteq V
$$

$\ker(T)$ is a subspace of $V$.

### 2.2 Image (Range)

$$
\text{Im}(T) = \{T(\mathbf{v}) \mid \mathbf{v} \in V\} \subseteq W
$$

$\text{Im}(T)$ is a subspace of $W$.

### 2.3 Rank-Nullity Theorem for Linear Transformations

If $V$ is finite-dimensional:

$$
\dim(\ker(T)) + \dim(\text{Im}(T)) = \dim(V)
$$

---

## 3. Isomorphism

### 3.1 Definitions

- **Injective (one-to-one):** $T(\mathbf{u}) = T(\mathbf{v})$ implies $\mathbf{u} = \mathbf{v}$. Equivalently, $\ker(T) = \{\mathbf{0}\}$.
- **Surjective (onto):** $\text{Im}(T) = W$.
- **Isomorphism:** a linear transformation that is both injective and surjective (bijective).

### 3.2 Finite-Dimensional Classification

If $\dim(V) = \dim(W)$, then $T$ is injective iff it is surjective (the rank-nullity theorem forces the equivalence).

---

## 4. Matrix Representation

### 4.1 Standard Matrix

Given bases $B = \{\mathbf{b}_1, \ldots, \mathbf{b}_n\}$ for $V$ and $C = \{\mathbf{c}_1, \ldots, \mathbf{c}_m\}$ for $W$, the matrix $[T]_{C \leftarrow B}$ is $m \times n$ with column $j$ equal to $[T(\mathbf{b}_j)]_C$.

For $V = \mathbb{R}^n$, $W = \mathbb{R}^m$ with standard bases, $[T] = A$ simply satisfies $T(\mathbf{x}) = A\mathbf{x}$.

### 4.2 Composition

If $T: V \to W$ and $S: W \to U$ are linear, then $S \circ T: V \to U$ is linear and:

$$
[S \circ T] = [S][T]
$$

(matrix multiplication of the representations).

### 4.3 Similarity

If $A$ and $B$ represent the same linear transformation under different bases, then $B = P^{-1}AP$ for some invertible change-of-basis matrix $P$. Matrices related this way are called **similar**.

---

## 5. Geometric Transformations in $\mathbb{R}^2$

### 5.1 Rotation by $\theta$

$$
R_\theta = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}
$$

### 5.2 Reflection across the $x$-axis

$$
\text{Refl}_x = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}
$$

### 5.3 Reflection across the line $y = x$

$$
\text{Refl}_{y=x} = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}
$$

### 5.4 Shear in the $x$-direction

$$
\text{Shear}_x(k) = \begin{bmatrix} 1 & k \\ 0 & 1 \end{bmatrix}
$$

### 5.5 Orthogonal Projection onto the $x$-axis

$$
P_x = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}
$$

---

## Solved Exercises

### Exercise 1: Checking Linearity

**Problem:**
Determine whether $T: \mathbb{R}^2 \to \mathbb{R}^2$, $T(x, y) = (x + 2y, 3x)$ is linear.

**Solution:**
Check additivity: let $\mathbf{u} = (u_1, u_2)$, $\mathbf{v} = (v_1, v_2)$.

$$
T(\mathbf{u} + \mathbf{v}) = T(u_1 + v_1, u_2 + v_2) = (u_1 + v_1 + 2(u_2 + v_2), 3(u_1 + v_1))
$$

$$
= (u_1 + 2u_2 + v_1 + 2v_2, 3u_1 + 3v_1)
$$

$$
T(\mathbf{u}) + T(\mathbf{v}) = (u_1 + 2u_2, 3u_1) + (v_1 + 2v_2, 3v_1) = (u_1 + 2u_2 + v_1 + 2v_2, 3u_1 + 3v_1)
$$

They match. Check homogeneity: $T(c\mathbf{u}) = (cu_1 + 2cu_2, 3cu_1) = c(u_1 + 2u_2, 3u_1) = c T(\mathbf{u})$. Both conditions hold. $T$ is linear.

---

### Exercise 2: Non-Linear Map

**Problem:**
Show that $T: \mathbb{R} \to \mathbb{R}$, $T(x) = x^2$ is not linear.

**Solution:**
Check homogeneity: $T(cx) = (cx)^2 = c^2 x^2 \neq c\,T(x) = c x^2$ for $c \neq 0, 1$. For example, $T(2 \cdot 3) = 36 \neq 2 \cdot T(3) = 18$. Not linear.

---

### Exercise 3: Kernel and Image

**Problem:**
Find $\ker(T)$ and $\text{Im}(T)$ for $T: \mathbb{R}^3 \to \mathbb{R}^2$, $T(x, y, z) = (x + y, y - z)$.

**Solution:**
**Kernel:** Solve $T(x, y, z) = (0, 0)$:

$$
x + y = 0,\quad y - z = 0 \Rightarrow z = y,\; x = -y
$$

Set $y = t$: $(x, y, z) = (-t, t, t) = t(-1, 1, 1)$.

$$
\ker(T) = \text{span}\{(-1, 1, 1)\},\quad \dim(\ker) = 1
$$

**Image:** $T(x, y, z) = (x + y, y - z)$. Any vector in $\mathbb{R}^2$ can be written as $(a, b)$ by choosing $x, y, z$ appropriately. For any $(a, b) \in \mathbb{R}^2$, set $y = 0$, $z = -b$, $x = a$. Then $T(a, 0, -b) = (a, b)$. So $\text{Im}(T) = \mathbb{R}^2$, $\dim(\text{Im}) = 2$.

Verify rank-nullity: $1 + 2 = 3 = \dim(\mathbb{R}^3)$.

---

### Exercise 4: Matrix of a Linear Transformation

**Problem:**
Find the matrix $A$ of $T: \mathbb{R}^3 \to \mathbb{R}^2$, $T(x, y, z) = (2x - y, x + 3y + z)$ using standard bases.

**Solution:**
$T(\mathbf{e}_1) = T(1, 0, 0) = (2, 1)^\mathsf{T}$.
$T(\mathbf{e}_2) = T(0, 1, 0) = (-1, 3)^\mathsf{T}$.
$T(\mathbf{e}_3) = T(0, 0, 1) = (0, 1)^\mathsf{T}$.

$$
A = \begin{bmatrix} 2 & -1 & 0 \\ 1 & 3 & 1 \end{bmatrix}
$$

Verification: $A \begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 2x - y \\ x + 3y + z \end{pmatrix}$.

---

### Exercise 5: Composition of Transformations

**Problem:**
Let $T: \mathbb{R}^2 \to \mathbb{R}^2$ be rotation by $90^\circ$ and $S: \mathbb{R}^2 \to \mathbb{R}^2$ be reflection across the $x$-axis. Find $[S \circ T]$.

**Solution:**
Rotation by $90^\circ$: $R_{90} = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$.
Reflection across $x$-axis: $R_x = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}$.

$$
[S \circ T] = R_x \cdot R_{90} = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}
\begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}
= \begin{bmatrix} 0 & -1 \\ -1 & 0 \end{bmatrix}
$$

This is reflection across the line $y = -x$. Check: $T(1, 0) = (0, 1)$, then $S(0, 1) = (0, -1)$. Direct: $(S \circ T)(1, 0) = (0, -1)$, and $A(1, 0)^\mathsf{T} = (0, -1)^\mathsf{T}$, correct.

---

### Exercise 6: Injectivity and Surjectivity

**Problem:**
Determine if $T: \mathbb{R}^2 \to \mathbb{R}^2$, $T(x, y) = (x + 2y, 2x + 4y)$ is injective and/or surjective.

**Solution:**
The matrix is $A = \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}$. $\det(A) = 1 \cdot 4 - 2 \cdot 2 = 0$. $A$ is singular.

**Kernel:** Solve $A\mathbf{x} = \mathbf{0}$: $x + 2y = 0$, $2x + 4y = 0$. The second equation is $2 \times$ the first. So $x = -2y$. Non-zero vectors exist (e.g., $(-2, 1)$), so $\ker(T) \neq \{\mathbf{0}\}$. $T$ is **not injective**.

**Image:** $\text{rank}(A) = 1$ (only one pivot), but $\dim(\mathbb{R}^2) = 2$. So $\text{Im}(T) \neq \mathbb{R}^2$. $T$ is **not surjective**.

---

### Exercise 7: Similarity

**Problem:**
Show that $A = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}$ and $B = \begin{bmatrix} 3 & 0 \\ 0 & 1 \end{bmatrix}$ are similar.

**Solution:**
Find eigenvectors of $A$. $\det(A - \lambda I) = (2 - \lambda)^2 - 1 = \lambda^2 - 4\lambda + 3 = (\lambda - 3)(\lambda - 1)$. Eigenvalues $\lambda = 3, 1$.

For $\lambda = 3$: $(A - 3I)\mathbf{v} = \begin{bmatrix} -1 & 1 \\ 1 & -1 \end{bmatrix}\mathbf{v} = \mathbf{0} \Rightarrow \mathbf{v} = (1, 1)$.

For $\lambda = 1$: $(A - I)\mathbf{v} = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}\mathbf{v} = \mathbf{0} \Rightarrow \mathbf{v} = (1, -1)$.

Let $P = \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}$ (eigenvectors as columns). Then $P^{-1}AP = \begin{bmatrix} 3 & 0 \\ 0 & 1 \end{bmatrix} = B$. Thus $A$ and $B$ are similar.

---

### Exercise 8: Geometric Transformation Composition

**Problem:**
Find the matrix for rotation by $45^\circ$ followed by reflection across the $y$-axis.

**Solution:**
Rotation by $45^\circ$: $R_{45} = \begin{bmatrix} \cos 45^\circ & -\sin 45^\circ \\ \sin 45^\circ & \cos 45^\circ \end{bmatrix} = \frac{1}{\sqrt{2}} \begin{bmatrix} 1 & -1 \\ 1 & 1 \end{bmatrix}$.

Reflection across $y$-axis: $\text{Refl}_y = \begin{bmatrix} -1 & 0 \\ 0 & 1 \end{bmatrix}$.

Composition: $\text{Refl}_y \circ R_{45}$:

$$
A = \begin{bmatrix} -1 & 0 \\ 0 & 1 \end{bmatrix} \cdot \frac{1}{\sqrt{2}} \begin{bmatrix} 1 & -1 \\ 1 & 1 \end{bmatrix} = \frac{1}{\sqrt{2}} \begin{bmatrix} -1 & 1 \\ 1 & 1 \end{bmatrix}
$$

---

## Exam Tip: Kernel Membership Check

To test if a vector $\mathbf{v}$ is in $\ker(T)$, simply apply $T$ and verify the result is $\mathbf{0}$. For $\text{Im}(T)$ membership, solve $T(\mathbf{x}) = \mathbf{b}$ for $\mathbf{x}$; if consistent, $\mathbf{b} \in \text{Im}(T)$. On exams, the rank-nullity theorem is often needed to determine dimensions without full computation.

---