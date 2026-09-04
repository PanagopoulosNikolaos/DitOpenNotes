# Lecture 02: Vector Spaces, Subspaces, Basis, and Dimension

## Context and Grounding
This lecture develops the axiomatic theory of real vector spaces. It investigates linear combinations, spanning sets, linear independence, coordinate systems, bases, and dimensions, culminating in the formal characterization of the four fundamental matrix subspaces and the Rank-Nullity Theorem.

---

## 1. Vector Spaces and Subspaces

### 1.1 Axiomatic Definition of a Real Vector Space
A vector space $(V, +, \cdot)$ over $\mathbb{R}$ is a set of objects equipped with addition and scalar multiplication satisfying ten closure and algebraic axioms:
1. $\mathbf{u} + \mathbf{v} \in V$ (Closure under addition)
2. $\mathbf{u} + \mathbf{v} = \mathbf{v} + \mathbf{u}$ (Commutativity)
3. $(\mathbf{u} + \mathbf{v}) + \mathbf{w} = \mathbf{u} + (\mathbf{v} + \mathbf{w})$ (Associativity)
4. $\exists \mathbf{0} \in V$ such that $\mathbf{u} + \mathbf{0} = \mathbf{u}$ (Additive identity)
5. $\forall \mathbf{u} \in V, \exists (-\mathbf{u}) \in V$ such that $\mathbf{u} + (-\mathbf{u}) = \mathbf{0}$ (Additive inverse)
6. $c \mathbf{u} \in V$ for all $c \in \mathbb{R}$ (Closure under scalar multiplication)
7. $c(\mathbf{u} + \mathbf{v}) = c\mathbf{u} + c\mathbf{v}$ (Distributivity over vector addition)
8. $(c + d)\mathbf{u} = c\mathbf{u} + d\mathbf{u}$ (Distributivity over scalar addition)
9. $c(d\mathbf{u}) = (cd)\mathbf{u}$ (Scalar associativity)
10. $1 \cdot \mathbf{u} = \mathbf{u}$ (Multiplicative unit identity)

### 1.2 Subspaces
A subset $H \subseteq V$ is a **subspace** of $V$ if and only if it satisfies three criteria:
1. $\mathbf{0} \in H$ (Contains the zero vector).
2. $\mathbf{u}, \mathbf{v} \in H \implies \mathbf{u} + \mathbf{v} \in H$ (Closed under addition).
3. $\mathbf{u} \in H, c \in \mathbb{R} \implies c\mathbf{u} \in H$ (Closed under scalar multiplication).

---

## 2. Span and Linear Independence

### 2.1 Linear Combinations and Span
Given vectors $\{\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_k\} \subset V$, a **linear combination** is any expression of the form:
$$\mathbf{y} = c_1 \mathbf{v}_1 + c_2 \mathbf{v}_2 + \cdots + c_k \mathbf{v}_k \quad (c_i \in \mathbb{R})$$
The **span** $\text{Span}\{\mathbf{v}_1, \ldots, \mathbf{v}_k\}$ is the set of all possible linear combinations. The span is guaranteed to be a valid subspace of $V$.

### 2.2 Linear Independence
A set of vectors $\{\mathbf{v}_1, \ldots, \mathbf{v}_k\}$ is **linearly independent** if the homogeneous vector equation:
$$c_1 \mathbf{v}_1 + c_2 \mathbf{v}_2 + \cdots + c_k \mathbf{v}_k = \mathbf{0}$$
admits **only the trivial solution** $c_1 = c_2 = \cdots = c_k = 0$.
If non-trivial weights exist where at least one $c_i \neq 0$, the set is **linearly dependent**.

* Computational test in $\mathbb{R}^n$: Assemble vectors into columns of matrix $A = [\mathbf{v}_1 \mid \cdots \mid \mathbf{v}_k]$. The set is linearly independent if and only if every column of $A$ is a pivot column in $\text{RREF}(A)$ ($\text{rank}(A) = k$).

---

## 3. Basis and Dimension

### 3.1 Basis
An ordered set of vectors $\mathcal{B} = \{\mathbf{b}_1, \ldots, \mathbf{b}_n\}$ in vector space $V$ is a **basis** for $V$ if:
1. $\mathcal{B}$ is linearly independent.
2. $\text{Span}(\mathcal{B}) = V$.

**Unique Representation Theorem**: If $\mathcal{B}$ is a basis for $V$, every $\mathbf{x} \in V$ can be represented uniquely as:
$$\mathbf{x} = c_1 \mathbf{b}_1 + \cdots + c_n \mathbf{b}_n$$
The coordinate vector of $\mathbf{x}$ relative to $\mathcal{B}$ is denoted $[\mathbf{x}]_{\mathcal{B}} = [c_1, \ldots, c_n]^T \in \mathbb{R}^n$.

### 3.2 Dimension
The **dimension** $\dim(V)$ is the cardinal number of vectors in any basis of $V$.

---

## 4. The Fundamental Subspaces and the Rank-Nullity Theorem

For any matrix $A \in \mathbb{R}^{m \times n}$:

| Subspace | Definition | Ambient Space | Dimension |
|:---|:---|:---:|:---:|
| **Column Space $\text{Col}(A)$** | $\text{Span}\{\text{columns of } A\}$ | $\mathbb{R}^m$ | $\text{rank}(A) = r$ |
| **Row Space $\text{Row}(A)$** | $\text{Col}(A^T) = \text{Span}\{\text{rows of } A\}$ | $\mathbb{R}^n$ | $\text{rank}(A) = r$ |
| **Null Space $\text{Null}(A)$** | $\{\mathbf{x} \in \mathbb{R}^n \mid A\mathbf{x} = \mathbf{0}\}$ | $\mathbb{R}^n$ | $\text{nullity}(A) = n - r$ |
| **Left Null Space $\text{Null}(A^T)$** | $\{\mathbf{y} \in \mathbb{R}^m \mid A^T \mathbf{y} = \mathbf{0}\}$ | $\mathbb{R}^m$ | $m - r$ |

### 4.1 The Rank-Nullity Theorem
For any matrix $A$ with $n$ columns:
$$\text{rank}(A) + \text{nullity}(A) = n$$
The number of pivot columns ($\text{rank}$) plus the number of free variables ($\text{nullity}$) equals the total number of variable columns ($n$).

