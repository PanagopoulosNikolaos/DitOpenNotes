# Euclidean Vector Spaces

Vectors in $\mathbb{R}^n$ provide the geometric foundation of linear algebra. Operations such as addition, scalar multiplication, the dot product, and the cross product allow measuring lengths, angles, and areas. Linear transformations between Euclidean spaces are represented by matrices, linking algebraic operations to geometric intuition. This section covers the core properties of $\mathbb{R}^n$, including norms, orthogonality, projections, and the geometric transformations of rotation, reflection, and shear.

---

## 1. Core Definitions

### 1.1 Vectors in $\mathbb{R}^n$

A **vector** in $\mathbb{R}^n$ is an ordered $n$-tuple of real numbers:

$$
\mathbf{v} = \begin{pmatrix} v_1 & v_2 & \cdots & v_n \end{pmatrix}^\mathsf{T}
$$

The **standard basis vectors** in $\mathbb{R}^n$ are:

$$
\mathbf{e}_1 = \begin{pmatrix}1&0&\cdots&0\end{pmatrix}^\mathsf{T},\;
\mathbf{e}_2 = \begin{pmatrix}0&1&\cdots&0\end{pmatrix}^\mathsf{T},\;
\ldots,\;
\mathbf{e}_n = \begin{pmatrix}0&0&\cdots&1\end{pmatrix}^\mathsf{T}
$$

### 1.2 Vector Operations

- **Addition:** $\mathbf{u} + \mathbf{v} = (u_1+v_1,\; u_2+v_2,\; \ldots,\; u_n+v_n)^\mathsf{T}$
- **Scalar multiplication:** $c\mathbf{v} = (c v_1,\; c v_2,\; \ldots,\; c v_n)^\mathsf{T}$

### 1.3 Norm (Length)

The **Euclidean norm** (length) of $\mathbf{v} \in \mathbb{R}^n$ is:

$$
\|\mathbf{v}\| = \sqrt{v_1^2 + v_2^2 + \cdots + v_n^2}
$$

A **unit vector** satisfies $\|\mathbf{v}\| = 1$. Any non-zero vector can be normalized:

$$
\hat{\mathbf{v}} = \frac{\mathbf{v}}{\|\mathbf{v}\|}
$$

---

## 2. Dot Product (Inner Product)

### 2.1 Definition

The **dot product** of $\mathbf{u}, \mathbf{v} \in \mathbb{R}^n$ is:

$$
\mathbf{u} \cdot \mathbf{v} = \sum_{i=1}^{n} u_i v_i = \|\mathbf{u}\| \|\mathbf{v}\| \cos\theta
$$

where $\theta$ is the angle between $\mathbf{u}$ and $\mathbf{v}$.

### 2.2 Properties

- $\mathbf{u} \cdot \mathbf{v} = \mathbf{v} \cdot \mathbf{u}$ (commutative)
- $\mathbf{u} \cdot (\mathbf{v} + \mathbf{w}) = \mathbf{u} \cdot \mathbf{v} + \mathbf{u} \cdot \mathbf{w}$ (distributive)
- $c(\mathbf{u} \cdot \mathbf{v}) = (c\mathbf{u}) \cdot \mathbf{v} = \mathbf{u} \cdot (c\mathbf{v})$
- $\mathbf{v} \cdot \mathbf{v} = \|\mathbf{v}\|^2$

### 2.3 Orthogonality

Two vectors are **orthogonal** (perpendicular) if $\mathbf{u} \cdot \mathbf{v} = 0$.

### 2.4 Projection

The **scalar projection** of $\mathbf{u}$ onto $\mathbf{v}$ is:

$$
\text{comp}_{\mathbf{v}}(\mathbf{u}) = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{v}\|}
$$

The **vector projection** of $\mathbf{u}$ onto $\mathbf{v}$ is:

$$
\text{proj}_{\mathbf{v}}(\mathbf{u}) = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{v}\|^2}\, \mathbf{v}
$$

---

## 3. Cross Product (in $\mathbb{R}^3$)

### 3.1 Definition

For $\mathbf{u}, \mathbf{v} \in \mathbb{R}^3$:

$$
\mathbf{u} \times \mathbf{v} = \begin{vmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
u_1 & u_2 & u_3 \\
v_1 & v_2 & v_3
\end{vmatrix}
= \begin{pmatrix}
u_2 v_3 - u_3 v_2 \\
u_3 v_1 - u_1 v_3 \\
u_1 v_2 - u_2 v_1
\end{pmatrix}
$$

### 3.2 Properties

- $\mathbf{u} \times \mathbf{v}$ is orthogonal to both $\mathbf{u}$ and $\mathbf{v}$.
- $\|\mathbf{u} \times \mathbf{v}\| = \|\mathbf{u}\| \|\mathbf{v}\| \sin\theta$
- $\mathbf{u} \times \mathbf{v} = -(\mathbf{v} \times \mathbf{u})$ (anti-commutative)
- The magnitude equals the area of the parallelogram spanned by $\mathbf{u}$ and $\mathbf{v}$.

### 3.3 Applications

- Computing a **normal vector** to a plane.
- Computing the **area** of a parallelogram: $\text{Area} = \|\mathbf{u} \times \mathbf{v}\|$.
- Computing the **volume** of a parallelepiped: $V = |\mathbf{u} \cdot (\mathbf{v} \times \mathbf{w})|$ (scalar triple product).

---

## 4. Linear Transformations $\mathbb{R}^n \to \mathbb{R}^m$

### 4.1 Definition

A map $T: \mathbb{R}^n \to \mathbb{R}^m$ is **linear** if for all $\mathbf{u}, \mathbf{v} \in \mathbb{R}^n$ and scalars $c$:

1. $T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})$
2. $T(c\mathbf{u}) = c\,T(\mathbf{u})$

### 4.2 Matrix Representation

Every linear transformation $T$ is represented by an $m \times n$ matrix $A$ such that $T(\mathbf{x}) = A\mathbf{x}$. Column $j$ of $A$ is $T(\mathbf{e}_j)$.

### 4.3 Kernel and Image

- **Kernel:** $\ker(T) = \{\mathbf{x} \in \mathbb{R}^n \mid T(\mathbf{x}) = \mathbf{0}\}$
- **Image:** $\text{Im}(T) = \{T(\mathbf{x}) \mid \mathbf{x} \in \mathbb{R}^n\}$
- $\dim(\ker(T)) + \dim(\text{Im}(T)) = n$

---

## Solved Exercises

### Exercise 1: Norm and Unit Vector

**Problem:**
Given $\mathbf{v} = (3, -1, 2)$, find $\|\mathbf{v}\|$ and the unit vector in the direction of $\mathbf{v}$.

**Solution:**
$$
\|\mathbf{v}\| = \sqrt{3^2 + (-1)^2 + 2^2} = \sqrt{9 + 1 + 4} = \sqrt{14}
$$

$$
\hat{\mathbf{v}} = \frac{1}{\sqrt{14}} (3, -1, 2) = \left(\frac{3}{\sqrt{14}}, -\frac{1}{\sqrt{14}}, \frac{2}{\sqrt{14}}\right)
$$

---

### Exercise 2: Dot Product and Angle

**Problem:**
Find the angle between $\mathbf{u} = (1, 2, -1)$ and $\mathbf{v} = (2, 0, 3)$.

**Solution:**
$$
\mathbf{u} \cdot \mathbf{v} = 1 \cdot 2 + 2 \cdot 0 + (-1) \cdot 3 = 2 + 0 - 3 = -1
$$

$$
\|\mathbf{u}\| = \sqrt{1 + 4 + 1} = \sqrt{6},\quad
\|\mathbf{v}\| = \sqrt{4 + 0 + 9} = \sqrt{13}
$$

$$
\cos\theta = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\| \|\mathbf{v}\|} = \frac{-1}{\sqrt{6} \cdot \sqrt{13}} = -\frac{1}{\sqrt{78}}
$$

$$
\theta = \arccos\left(-\frac{1}{\sqrt{78}}\right) \approx 96.5^\circ
$$

Since $\theta > 90^\circ$, the vectors point in generally opposite directions.

---

### Exercise 3: Vector Projection

**Problem:**
Find the projection of $\mathbf{u} = (4, 1)$ onto $\mathbf{v} = (2, 3)$.

**Solution:**
$$
\mathbf{u} \cdot \mathbf{v} = 4 \cdot 2 + 1 \cdot 3 = 8 + 3 = 11
$$

$$
\|\mathbf{v}\|^2 = 2^2 + 3^2 = 4 + 9 = 13
$$

$$
\text{proj}_{\mathbf{v}}(\mathbf{u}) = \frac{11}{13} (2, 3) = \left(\frac{22}{13}, \frac{33}{13}\right)
$$

The component of $\mathbf{u}$ orthogonal to $\mathbf{v}$ is:

$$
\mathbf{u} - \text{proj}_{\mathbf{v}}(\mathbf{u}) = \left(4 - \frac{22}{13}, \; 1 - \frac{33}{13}\right) = \left(\frac{30}{13}, -\frac{20}{13}\right)
$$

Verification: dot product of the orthogonal component with $\mathbf{v}$ should be zero:

$$
\frac{30}{13} \cdot 2 + \left(-\frac{20}{13}\right) \cdot 3 = \frac{60}{13} - \frac{60}{13} = 0
$$

---

### Exercise 4: Cross Product

**Problem:**
Compute $\mathbf{u} \times \mathbf{v}$ for $\mathbf{u} = (1, 2, 3)$ and $\mathbf{v} = (4, 5, 6)$.

**Solution:**

$$
\mathbf{u} \times \mathbf{v} = \begin{vmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
1 & 2 & 3 \\
4 & 5 & 6
\end{vmatrix}
= \mathbf{i}(2 \cdot 6 - 3 \cdot 5) - \mathbf{j}(1 \cdot 6 - 3 \cdot 4) + \mathbf{k}(1 \cdot 5 - 2 \cdot 4)
$$

$$
= \mathbf{i}(12 - 15) - \mathbf{j}(6 - 12) + \mathbf{k}(5 - 8)
= (-3, 6, -3)
$$

The area of the parallelogram spanned by $\mathbf{u}$ and $\mathbf{v}$ is:

$$
\|\mathbf{u} \times \mathbf{v}\| = \sqrt{(-3)^2 + 6^2 + (-3)^2} = \sqrt{9 + 36 + 9} = \sqrt{54} = 3\sqrt{6}
$$

---

### Exercise 5: Orthogonality Check

**Problem:**
Determine whether $\mathbf{u} = (2, -1, 3)$ and $\mathbf{v} = (1, 5, 1)$ are orthogonal.

**Solution:**
$$
\mathbf{u} \cdot \mathbf{v} = 2 \cdot 1 + (-1) \cdot 5 + 3 \cdot 1 = 2 - 5 + 3 = 0
$$

Since the dot product is zero, $\mathbf{u}$ and $\mathbf{v}$ are orthogonal.

---

### Exercise 6: Linear Transformation Matrix

**Problem:**
Find the matrix $A$ of the linear transformation $T: \mathbb{R}^2 \to \mathbb{R}^3$ defined by:

$$
T(x_1, x_2) = (2x_1 - x_2,\; x_1 + 3x_2,\; -x_1 + 4x_2)
$$

**Solution:**
The matrix $A$ is $3 \times 2$. Column 1 is $T(\mathbf{e}_1) = T(1, 0) = (2, 1, -1)^\mathsf{T}$.
Column 2 is $T(\mathbf{e}_2) = T(0, 1) = (-1, 3, 4)^\mathsf{T}$.

$$
A = \begin{bmatrix}
2 & -1 \\
1 & 3 \\
-1 & 4
\end{bmatrix}
$$

Verification: $A\mathbf{x} = \begin{bmatrix} 2 & -1 \\ 1 & 3 \\ -1 & 4 \end{bmatrix} \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = \begin{pmatrix} 2x_1 - x_2 \\ x_1 + 3x_2 \\ -x_1 + 4x_2 \end{pmatrix}$, matching $T$.

---

### Exercise 7: Kernel and Image Dimensions

**Problem:**
For $T: \mathbb{R}^4 \to \mathbb{R}^3$ with matrix $A = \begin{bmatrix} 1 & 2 & 1 & 0 \\ 0 & 1 & -1 & 1 \\ 0 & 0 & 0 & 0 \end{bmatrix}$, find $\dim(\ker(T))$ and $\dim(\text{Im}(T))$.

**Solution:**
Reduce $A$ to REF (already in REF). Pivot columns: columns 1 and 2. So $\text{rank}(A) = 2$.

$\dim(\text{Im}(T)) = \text{rank}(A) = 2$.

By the rank-nullity theorem: $\dim(\ker(T)) = n - \text{rank}(A) = 4 - 2 = 2$.

The kernel has dimension 2, meaning the null space contains two free variables.

---

### Exercise 8: Area via Cross Product

**Problem:**
Find the area of the triangle with vertices $P(1, 0, 1)$, $Q(2, 3, 1)$, $R(0, 1, 4)$.

**Solution:**
Two edge vectors:

$$
\mathbf{u} = \overrightarrow{PQ} = (2-1, 3-0, 1-1) = (1, 3, 0)
$$

$$
\mathbf{v} = \overrightarrow{PR} = (0-1, 1-0, 4-1) = (-1, 1, 3)
$$

Cross product:

$$
\mathbf{u} \times \mathbf{v} = \begin{vmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
1 & 3 & 0 \\
-1 & 1 & 3
\end{vmatrix}
= \mathbf{i}(3 \cdot 3 - 0 \cdot 1) - \mathbf{j}(1 \cdot 3 - 0 \cdot (-1)) + \mathbf{k}(1 \cdot 1 - 3 \cdot (-1))
$$

$$
= \mathbf{i}(9 - 0) - \mathbf{j}(3 - 0) + \mathbf{k}(1 + 3) = (9, -3, 4)
$$

Area of parallelogram: $\|\mathbf{u} \times \mathbf{v}\| = \sqrt{81 + 9 + 16} = \sqrt{106}$.

Area of triangle: $\frac{1}{2} \sqrt{106}$.

---

## Exam Tip: Decomposing a Vector into Parallel and Orthogonal Components

Given a vector $\mathbf{u}$ and a direction $\mathbf{v}$, the decomposition

$$
\mathbf{u} = \text{proj}_{\mathbf{v}}(\mathbf{u}) + (\mathbf{u} - \text{proj}_{\mathbf{v}}(\mathbf{u}))
$$

separates $\mathbf{u}$ into a part parallel to $\mathbf{v}$ and a part orthogonal to $\mathbf{v}$. This decomposition is central to Gram-Schmidt orthogonalization and least-squares problems. On exams, always verify orthogonality by checking that the dot product of the residual with $\mathbf{v}$ is zero.

---