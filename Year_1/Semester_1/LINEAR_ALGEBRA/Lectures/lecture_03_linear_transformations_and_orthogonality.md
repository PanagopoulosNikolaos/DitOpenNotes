# Lecture 03: Linear Transformations, Inner Products, and Orthogonality

## Context and Grounding
This lecture connects geometric vector operations with functional mappings. It investigates linear transformations between vector spaces, standard matrix representations, inner product spaces, orthogonal projections, the Gram-Schmidt orthogonalization algorithm, and the QR matrix factorization.

---

## 1. Linear Transformations

A mapping $T: V \to W$ between vector spaces is a **linear transformation** if and only if for all $\mathbf{u}, \mathbf{v} \in V$ and scalars $c, d \in \mathbb{R}$:
$$T(c\mathbf{u} + d\mathbf{v}) = c T(\mathbf{u}) + d T(\mathbf{v})$$

### 1.1 Standard Matrix Representation
For any linear mapping $T: \mathbb{R}^n \to \mathbb{R}^m$, there exists a unique standard matrix $A \in \mathbb{R}^{m \times n}$ such that:
$$T(\mathbf{x}) = A\mathbf{x} \quad \text{for all } \mathbf{x} \in \mathbb{R}^n$$
where the columns of $A$ are the images of the standard basis vectors $\{\mathbf{e}_1, \ldots, \mathbf{e}_n\}$:
$$A = [T(\mathbf{e}_1) \mid T(\mathbf{e}_2) \mid \cdots \mid T(\mathbf{e}_n)]$$

### 1.2 Kernel and Range
* **Kernel ($\ker(T)$)**: The set of all vectors in $V$ mapped to the zero vector in $W$:
  $$\ker(T) = \{\mathbf{v} \in V \mid T(\mathbf{v}) = \mathbf{0}\} = \text{Null}(A)$$
  $T$ is **injective (one-to-one)** if and only if $\ker(T) = \{\mathbf{0}\}$.
* **Range ($\text{range}(T)$)**: The set of all images in $W$:
  $$\text{range}(T) = \{T(\mathbf{v}) \mid \mathbf{v} \in V\} = \text{Col}(A)$$
  $T$ is **surjective (onto)** if and only if $\text{range}(T) = W$.

---

## 2. Inner Products, Norms, and Orthogonality

### 2.1 The Euclidean Inner Product (Dot Product)
For vectors $\mathbf{u}, \mathbf{v} \in \mathbb{R}^n$:
$$\mathbf{u} \cdot \mathbf{v} = \mathbf{u}^T \mathbf{v} = \sum_{i=1}^n u_i v_i$$
* **Vector Norm (Length)**: $\|\mathbf{v}\| = \sqrt{\mathbf{v} \cdot \mathbf{v}} = \sqrt{\sum v_i^2}$.
* **Cauchy-Schwarz Inequality**: $|\mathbf{u} \cdot \mathbf{v}| \le \|\mathbf{u}\| \|\mathbf{v}\|$.
* **Orthogonality**: Vectors $\mathbf{u}$ and $\mathbf{v}$ are **orthogonal** ($\mathbf{u} \perp \mathbf{v}$) if and only if:
  $$\mathbf{u} \cdot \mathbf{v} = 0$$

### 2.2 Orthogonal Complements and Fundamental Subspace Duality
Let $W$ be a subspace of $\mathbb{R}^n$. Its **orthogonal complement** $W^\perp$ is:
$$W^\perp = \{\mathbf{x} \in \mathbb{R}^n \mid \mathbf{x} \cdot \mathbf{w} = 0 \text{ for all } \mathbf{w} \in W\}$$

**Fundamental Orthogonality Theorem**: For any matrix $A \in \mathbb{R}^{m \times n}$:
$$\text{Null}(A) = (\text{Row}(A))^\perp \quad \text{and} \quad \text{Null}(A^T) = (\text{Col}(A))^\perp$$

---

## 3. Orthogonal Projections and Gram-Schmidt Process

### 3.1 Orthogonal Projection onto a Subspace
Let $W$ be a subspace with orthogonal basis $\{\mathbf{u}_1, \ldots, \mathbf{u}_p\}$. The orthogonal projection of vector $\mathbf{y} \in \mathbb{R}^n$ onto $W$ is:
$$\hat{\mathbf{y}} = \text{proj}_W(\mathbf{y}) = \sum_{i=1}^p \frac{\mathbf{y} \cdot \mathbf{u}_i}{\mathbf{u}_i \cdot \mathbf{u}_i} \mathbf{u}_i$$
* **Orthogonal Decomposition**: $\mathbf{y} = \hat{\mathbf{y}} + \mathbf{z}$, where $\hat{\mathbf{y}} \in W$ and $\mathbf{z} \in W^\perp$.
* **Best Approximation Theorem**: $\hat{\mathbf{y}}$ is the closest vector in $W$ to $\mathbf{y}$, minimizing the Euclidean distance $\|\mathbf{y} - \mathbf{w}\|$ for all $\mathbf{w} \in W$.

### 3.2 The Gram-Schmidt Orthogonalization Algorithm
Transforms any linearly independent basis $\{\mathbf{x}_1, \ldots, \mathbf{x}_p\}$ into an orthogonal basis $\{\mathbf{v}_1, \ldots, \mathbf{v}_p\}$ for the same subspace:
$$\begin{aligned}
\mathbf{v}_1 &= \mathbf{x}_1 \\
\mathbf{v}_2 &= \mathbf{x}_2 - \frac{\mathbf{x}_2 \cdot \mathbf{v}_1}{\mathbf{v}_1 \cdot \mathbf{v}_1} \mathbf{v}_1 \\
\mathbf{v}_3 &= \mathbf{x}_3 - \frac{\mathbf{x}_3 \cdot \mathbf{v}_1}{\mathbf{v}_1 \cdot \mathbf{v}_1} \mathbf{v}_1 - \frac{\mathbf{x}_3 \cdot \mathbf{v}_2}{\mathbf{v}_2 \cdot \mathbf{v}_2} \mathbf{v}_2 \\
&\quad \vdots \\
\mathbf{v}_k &= \mathbf{x}_k - \sum_{j=1}^{k-1} \frac{\mathbf{x}_k \cdot \mathbf{v}_j}{\mathbf{v}_j \cdot \mathbf{v}_j} \mathbf{v}_j
\end{aligned}$$
Normalizing each $\mathbf{q}_i = \frac{\mathbf{v}_i}{\|\mathbf{v}_i\|}$ produces an **orthonormal basis**.

---

## 4. The QR Matrix Factorization

Every matrix $A \in \mathbb{R}^{m \times n}$ with linearly independent columns can be factored as:
$$A = QR$$
where:
* $Q \in \mathbb{R}^{m \times n}$ has orthonormal columns ($Q^T Q = I_n$).
* $R \in \mathbb{R}^{n \times n}$ is an upper-triangular invertible matrix with positive diagonal entries:
  $$r_{jj} = \|\mathbf{v}_j\|, \quad r_{ij} = \mathbf{q}_i \cdot \mathbf{x}_j \quad (i < j)$$
QR decomposition is fundamental for solving least-squares problems and computing eigenvalues stably.

