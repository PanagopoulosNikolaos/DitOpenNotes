# Orthogonality

Orthogonality extends the geometric notion of perpendicularity to arbitrary vectors and subspaces. Orthogonal and orthonormal bases simplify computations considerably, as coordinates can be obtained via dot products. The Gram-Schmidt process constructs an orthogonal basis from any basis, and the associated QR factorization is a fundamental tool in numerical linear algebra. Orthogonal projections onto subspaces and least-squares solutions address the problem of finding the best approximate solution to overdetermined systems.

---

## 1. Core Definitions

### 1.1 Orthogonal and Orthonormal Sets

A set of vectors $\{\mathbf{u}_1, \ldots, \mathbf{u}_k\}$ is **orthogonal** if $\mathbf{u}_i \cdot \mathbf{u}_j = 0$ for $i \neq j$.

It is **orthonormal** if, additionally, $\|\mathbf{u}_i\| = 1$ for all $i$.

### 1.2 Orthonormal Basis

A basis $B$ of $\mathbb{R}^n$ that is orthonormal. Coordinates relative to an orthonormal basis are:

$$
\mathbf{v} = \sum_{i=1}^{n} (\mathbf{v} \cdot \mathbf{u}_i) \mathbf{u}_i
$$

### 1.3 Fourier Expansion

For an orthonormal basis $\{\mathbf{u}_1, \ldots, \mathbf{u}_n\}$:

$$
\mathbf{v} = \sum_{i=1}^{n} (\mathbf{v} \cdot \mathbf{u}_i) \mathbf{u}_i
$$

The coefficients $c_i = \mathbf{v} \cdot \mathbf{u}_i$ are the **Fourier coefficients**.

---

## 2. Gram-Schmidt Process

Given a linearly independent set $\{\mathbf{a}_1, \ldots, \mathbf{a}_k\}$, produces an orthogonal set $\{\mathbf{v}_1, \ldots, \mathbf{v}_k\}$:

$$
\begin{aligned}
\mathbf{v}_1 &= \mathbf{a}_1 \\
\mathbf{v}_2 &= \mathbf{a}_2 - \text{proj}_{\mathbf{v}_1}(\mathbf{a}_2) \\
\mathbf{v}_3 &= \mathbf{a}_3 - \text{proj}_{\mathbf{v}_1}(\mathbf{a}_3) - \text{proj}_{\mathbf{v}_2}(\mathbf{a}_3) \\
&\vdots
\end{aligned}
$$

where $\text{proj}_{\mathbf{v}}(\mathbf{u}) = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{v}\|^2} \mathbf{v}$.

Normalize each $\mathbf{v}_i$ to obtain an orthonormal set.

---

## 3. Orthogonal Matrices

### 3.1 Definition

A square matrix $Q$ is **orthogonal** if $Q^\mathsf{T} Q = I$, equivalently $Q^{-1} = Q^\mathsf{T}$.

### 3.2 Properties

- Columns of $Q$ form an orthonormal set.
- $\|Q\mathbf{x}\| = \|\mathbf{x}\|$ (preserves length).
- $(Q\mathbf{x}) \cdot (Q\mathbf{y}) = \mathbf{x} \cdot \mathbf{y}$ (preserves angles).
- $\det(Q) = \pm 1$.

---

## 4. Orthogonal Projections

### 4.1 Projection onto a Subspace

Let $W$ be a subspace of $\mathbb{R}^n$ with orthonormal basis $\{\mathbf{u}_1, \ldots, \mathbf{u}_k\}$. The orthogonal projection of $\mathbf{v}$ onto $W$ is:

$$
\text{proj}_W(\mathbf{v}) = \sum_{i=1}^{k} (\mathbf{v} \cdot \mathbf{u}_i) \mathbf{u}_i
$$

If $A$ is a matrix whose columns form a basis for $W$, then:

$$
P = A(A^\mathsf{T} A)^{-1} A^\mathsf{T}
$$

is the projection matrix onto $\text{Col}(A)$.

### 4.2 Orthogonal Decomposition

Every $\mathbf{v} \in \mathbb{R}^n$ can be uniquely decomposed as:

$$
\mathbf{v} = \text{proj}_W(\mathbf{v}) + (\mathbf{v} - \text{proj}_W(\mathbf{v}))
$$

where the first component lies in $W$ and the second lies in $W^\perp$ (the orthogonal complement).

---

## 5. Least Squares

### 5.1 Problem Statement

For an overdetermined system $A\mathbf{x} = \mathbf{b}$ ($m > n$), there is generally no exact solution. The **least-squares solution** $\hat{\mathbf{x}}$ minimizes $\|A\mathbf{x} - \mathbf{b}\|^2$.

### 5.2 Normal Equations

The least-squares solution satisfies:

$$
A^\mathsf{T} A \hat{\mathbf{x}} = A^\mathsf{T} \mathbf{b}
$$

### 5.3 Application: Linear Regression

Given data points $(x_i, y_i)$, the line $y = \beta_0 + \beta_1 x$ that minimizes the sum of squared residuals is found by solving the normal equations.

---

## Solved Exercises

### Exercise 1: Orthogonal Set Verification

**Problem:**
Determine whether $\{(1, 2, -1), (2, 1, 4)\}$ is orthogonal.

**Solution:**
$$
(1, 2, -1) \cdot (2, 1, 4) = 1 \cdot 2 + 2 \cdot 1 + (-1) \cdot 4 = 2 + 2 - 4 = 0
$$

The dot product is zero, so the set is orthogonal.

---

### Exercise 2: Gram-Schmidt Process

**Problem:**
Apply Gram-Schmidt to $\{(1, 1, 0), (1, 0, 1), (0, 1, 1)\}$ to obtain an orthogonal basis.

**Solution:**
Let $\mathbf{a}_1 = (1, 1, 0)$, $\mathbf{a}_2 = (1, 0, 1)$, $\mathbf{a}_3 = (0, 1, 1)$.

**Step 1:** $\mathbf{v}_1 = \mathbf{a}_1 = (1, 1, 0)$.

**Step 2:**
$$
\text{proj}_{\mathbf{v}_1}(\mathbf{a}_2) = \frac{(1, 0, 1) \cdot (1, 1, 0)}{\|(1, 1, 0)\|^2} (1, 1, 0)
= \frac{1 + 0 + 0}{1 + 1 + 0} (1, 1, 0) = \frac{1}{2}(1, 1, 0) = \left(\frac{1}{2}, \frac{1}{2}, 0\right)
$$

$$
\mathbf{v}_2 = \mathbf{a}_2 - \text{proj}_{\mathbf{v}_1}(\mathbf{a}_2) = \left(1 - \frac{1}{2}, 0 - \frac{1}{2}, 1 - 0\right) = \left(\frac{1}{2}, -\frac{1}{2}, 1\right)
$$

**Step 3:**
$$
\text{proj}_{\mathbf{v}_1}(\mathbf{a}_3) = \frac{(0, 1, 1) \cdot (1, 1, 0)}{2} (1, 1, 0) = \frac{1}{2}(1, 1, 0) = \left(\frac{1}{2}, \frac{1}{2}, 0\right)
$$

$$
\text{proj}_{\mathbf{v}_2}(\mathbf{a}_3) = \frac{(0, 1, 1) \cdot \left(\frac{1}{2}, -\frac{1}{2}, 1\right)}{\|\mathbf{v}_2\|^2} \mathbf{v}_2
$$

Compute dot: $0 \cdot \frac{1}{2} + 1 \cdot \left(-\frac{1}{2}\right) + 1 \cdot 1 = -\frac{1}{2} + 1 = \frac{1}{2}$.

$\|\mathbf{v}_2\|^2 = \left(\frac{1}{2}\right)^2 + \left(-\frac{1}{2}\right)^2 + 1^2 = \frac{1}{4} + \frac{1}{4} + 1 = \frac{3}{2}$.

$$
\text{proj}_{\mathbf{v}_2}(\mathbf{a}_3) = \frac{1/2}{3/2} \mathbf{v}_2 = \frac{1}{3} \left(\frac{1}{2}, -\frac{1}{2}, 1\right) = \left(\frac{1}{6}, -\frac{1}{6}, \frac{1}{3}\right)
$$

$$
\mathbf{v}_3 = \mathbf{a}_3 - \text{proj}_{\mathbf{v}_1}(\mathbf{a}_3) - \text{proj}_{\mathbf{v}_2}(\mathbf{a}_3)
$$

$$
= (0, 1, 1) - \left(\frac{1}{2}, \frac{1}{2}, 0\right) - \left(\frac{1}{6}, -\frac{1}{6}, \frac{1}{3}\right)
$$

$$
= \left(-\frac{2}{3}, \frac{2}{3}, \frac{2}{3}\right)
$$

Orthogonal basis: $\left\{(1, 1, 0), \left(\frac{1}{2}, -\frac{1}{2}, 1\right), \left(-\frac{2}{3}, \frac{2}{3}, \frac{2}{3}\right)\right\}$.

---

### Exercise 3: Fourier Coefficients

**Problem:**
Find the coordinates of $\mathbf{v} = (3, 1, 2)$ relative to the orthonormal basis $\{\mathbf{u}_1, \mathbf{u}_2, \mathbf{u}_3\}$ where:

$$
\mathbf{u}_1 = \left(\frac{1}{\sqrt{2}}, 0, \frac{1}{\sqrt{2}}\right),\;
\mathbf{u}_2 = (0, 1, 0),\;
\mathbf{u}_3 = \left(\frac{1}{\sqrt{2}}, 0, -\frac{1}{\sqrt{2}}\right)
$$

**Solution:**
Since the basis is orthonormal, compute Fourier coefficients:

$$
c_1 = \mathbf{v} \cdot \mathbf{u}_1 = 3 \cdot \frac{1}{\sqrt{2}} + 1 \cdot 0 + 2 \cdot \frac{1}{\sqrt{2}} = \frac{5}{\sqrt{2}}
$$

$$
c_2 = \mathbf{v} \cdot \mathbf{u}_2 = 3 \cdot 0 + 1 \cdot 1 + 2 \cdot 0 = 1
$$

$$
c_3 = \mathbf{v} \cdot \mathbf{u}_3 = 3 \cdot \frac{1}{\sqrt{2}} + 1 \cdot 0 + 2 \cdot \left(-\frac{1}{\sqrt{2}}\right) = \frac{1}{\sqrt{2}}
$$

Coordinates: $[\mathbf{v}]_B = \left(\frac{5}{\sqrt{2}}, 1, \frac{1}{\sqrt{2}}\right)$.

Verification: $\frac{5}{\sqrt{2}} \mathbf{u}_1 + 1 \cdot \mathbf{u}_2 + \frac{1}{\sqrt{2}} \mathbf{u}_3 = \left(\frac{5}{2} + 0 + \frac{1}{2}, 0 + 1 + 0, \frac{5}{2} + 0 - \frac{1}{2}\right) = (3, 1, 2)$.

---

### Exercise 4: Orthogonal Matrix Verification

**Problem:**
Show that $Q = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}$ is orthogonal.

**Solution:**
Compute $Q^\mathsf{T} Q$:

$$
Q^\mathsf{T} Q = \begin{bmatrix} \cos\theta & \sin\theta \\ -\sin\theta & \cos\theta \end{bmatrix}
\begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}
$$

$$
= \begin{bmatrix}
\cos^2\theta + \sin^2\theta & -\cos\theta\sin\theta + \sin\theta\cos\theta \\
-\sin\theta\cos\theta + \cos\theta\sin\theta & \sin^2\theta + \cos^2\theta
\end{bmatrix}
= \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}
$$

$\det(Q) = \cos^2\theta + \sin^2\theta = 1$, confirming $\det(Q) = \pm 1$ (specifically $+1$ for rotation).

---

### Exercise 5: Projection onto a Subspace

**Problem:**
Find the projection of $\mathbf{v} = (1, 0, 2)$ onto the subspace spanned by $\{(1, 1, 0), (0, 1, 1)\}$.

**Solution:**
Let $A = \begin{bmatrix} 1 & 0 \\ 1 & 1 \\ 0 & 1 \end{bmatrix}$.

Compute $A^\mathsf{T} A = \begin{bmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \end{bmatrix}
\begin{bmatrix} 1 & 0 \\ 1 & 1 \\ 0 & 1 \end{bmatrix}
= \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}$.

Compute $(A^\mathsf{T} A)^{-1} = \frac{1}{4 - 1} \begin{bmatrix} 2 & -1 \\ -1 & 2 \end{bmatrix}
= \frac{1}{3} \begin{bmatrix} 2 & -1 \\ -1 & 2 \end{bmatrix}$.

Compute $A^\mathsf{T} \mathbf{b} = \begin{bmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \end{bmatrix}
\begin{pmatrix} 1 \\ 0 \\ 2 \end{pmatrix}
= \begin{pmatrix} 1 \\ 2 \end{pmatrix}$.

Least-squares coefficients: $\hat{\mathbf{x}} = (A^\mathsf{T} A)^{-1} A^\mathsf{T} \mathbf{b}
= \frac{1}{3} \begin{bmatrix} 2 & -1 \\ -1 & 2 \end{bmatrix}
\begin{pmatrix} 1 \\ 2 \end{pmatrix}
= \frac{1}{3} \begin{pmatrix} 0 \\ 3 \end{pmatrix} = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$.

Projection: $\text{proj}_W(\mathbf{v}) = A\hat{\mathbf{x}} = 0 \cdot (1, 1, 0) + 1 \cdot (0, 1, 1) = (0, 1, 1)$.

---

### Exercise 6: Least Squares Line

**Problem:**
Find the least-squares line $y = \beta_0 + \beta_1 x$ through the points $(1, 2)$, $(2, 3)$, $(3, 5)$.

**Solution:**
Set up $A\hat{\mathbf{x}} \approx \mathbf{b}$:

$$
A = \begin{bmatrix} 1 & 1 \\ 1 & 2 \\ 1 & 3 \end{bmatrix},\quad
\mathbf{b} = \begin{pmatrix} 2 \\ 3 \\ 5 \end{pmatrix},\quad
\hat{\mathbf{x}} = \begin{pmatrix} \beta_0 \\ \beta_1 \end{pmatrix}
$$

$$
A^\mathsf{T} A = \begin{bmatrix} 1 & 1 & 1 \\ 1 & 2 & 3 \end{bmatrix}
\begin{bmatrix} 1 & 1 \\ 1 & 2 \\ 1 & 3 \end{bmatrix}
= \begin{bmatrix} 3 & 6 \\ 6 & 14 \end{bmatrix}
$$

$$
A^\mathsf{T} \mathbf{b} = \begin{bmatrix} 1 & 1 & 1 \\ 1 & 2 & 3 \end{bmatrix}
\begin{pmatrix} 2 \\ 3 \\ 5 \end{pmatrix}
= \begin{pmatrix} 10 \\ 23 \end{pmatrix}
$$

Solve normal equations:

$$
\begin{bmatrix} 3 & 6 \\ 6 & 14 \end{bmatrix}
\begin{pmatrix} \beta_0 \\ \beta_1 \end{pmatrix}
= \begin{pmatrix} 10 \\ 23 \end{pmatrix}
$$

From first equation: $3\beta_0 + 6\beta_1 = 10$.
From second: $6\beta_0 + 14\beta_1 = 23$.

Multiply first by 2: $6\beta_0 + 12\beta_1 = 20$. Subtract from second:

$$
(6\beta_0 + 14\beta_1) - (6\beta_0 + 12\beta_1) = 23 - 20 \Rightarrow 2\beta_1 = 3 \Rightarrow \beta_1 = \frac{3}{2}
$$

Then $3\beta_0 + 6 \cdot \frac{3}{2} = 10 \Rightarrow 3\beta_0 + 9 = 10 \Rightarrow \beta_0 = \frac{1}{3}$.

**Least-squares line:** $y = \frac{1}{3} + \frac{3}{2}x$.

---

### Exercise 7: QR Factorization

**Problem:**
Find the QR factorization of $A = \begin{bmatrix} 1 & 1 \\ 1 & 0 \\ 0 & 1 \end{bmatrix}$.

**Solution:**
Apply Gram-Schmidt to the columns $\mathbf{a}_1 = (1, 1, 0)$, $\mathbf{a}_2 = (1, 0, 1)$.

$\mathbf{v}_1 = \mathbf{a}_1 = (1, 1, 0)$. $\|\mathbf{v}_1\| = \sqrt{2}$.
$\mathbf{q}_1 = \left(\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}, 0\right)$.

$\text{proj}_{\mathbf{v}_1}(\mathbf{a}_2) = \frac{(1, 0, 1) \cdot (1, 1, 0)}{2} (1, 1, 0) = \frac{1}{2} (1, 1, 0)$.

$\mathbf{v}_2 = (1, 0, 1) - \left(\frac{1}{2}, \frac{1}{2}, 0\right) = \left(\frac{1}{2}, -\frac{1}{2}, 1\right)$.

$\|\mathbf{v}_2\| = \sqrt{\frac{1}{4} + \frac{1}{4} + 1} = \sqrt{\frac{3}{2}} = \frac{\sqrt{6}}{2}$.

$\mathbf{q}_2 = \frac{1}{\sqrt{6}/2} \left(\frac{1}{2}, -\frac{1}{2}, 1\right) = \left(\frac{1}{\sqrt{6}}, -\frac{1}{\sqrt{6}}, \frac{2}{\sqrt{6}}\right)$.

Then $Q = \begin{bmatrix} \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{6}} \\ \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{6}} \\ 0 & \frac{2}{\sqrt{6}} \end{bmatrix}$.

$R = Q^\mathsf{T} A = \begin{bmatrix} \|v_1\| & \mathbf{q}_1 \cdot \mathbf{a}_2 \\ 0 & \|v_2\| \end{bmatrix}
= \begin{bmatrix} \sqrt{2} & \frac{1}{\sqrt{2}} \\ 0 & \frac{\sqrt{6}}{2} \end{bmatrix}$.

---

### Exercise 8: Orthogonal Complement

**Problem:**
Find $W^\perp$ for $W = \text{span}\{(1, 2, 1, 0), (0, 1, 2, 1)\} \subseteq \mathbb{R}^4$.

**Solution:**
$W^\perp$ consists of all vectors $\mathbf{x}$ orthogonal to every vector in $W$:

$$
(1, 2, 1, 0) \cdot \mathbf{x} = 0,\quad (0, 1, 2, 1) \cdot \mathbf{x} = 0
$$

This gives the system:

$$
x_1 + 2x_2 + x_3 = 0,\quad x_2 + 2x_3 + x_4 = 0
$$

Express pivot variables ($x_1$, $x_2$) in terms of free variables ($x_3 = s$, $x_4 = t$):

$x_2 = -2s - t$, $x_1 = -2x_2 - x_3 = -2(-2s - t) - s = 4s + 2t - s = 3s + 2t$.

$$
\mathbf{x} = \begin{pmatrix} 3s + 2t \\ -2s - t \\ s \\ t \end{pmatrix}
= s\begin{pmatrix} 3 \\ -2 \\ 1 \\ 0 \end{pmatrix} + t\begin{pmatrix} 2 \\ -1 \\ 0 \\ 1 \end{pmatrix}
$$

$W^\perp = \text{span}\{(3, -2, 1, 0), (2, -1, 0, 1)\}$, and $\dim(W^\perp) = 4 - 2 = 2$.

---

## Exam Tip: Normal Equations for Least Squares

When solving least-squares problems, always set up $A^\mathsf{T} A \hat{\mathbf{x}} = A^\mathsf{T} \mathbf{b}$. The matrix $A^\mathsf{T} A$ is symmetric and positive definite (if $A$ has full column rank), so its inverse exists. For linear regression, the first column of $A$ is all ones (intercept term), and the second column contains the $x_i$ values. Memorize this setup.

---