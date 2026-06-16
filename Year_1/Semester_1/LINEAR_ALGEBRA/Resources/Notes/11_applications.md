# Applications of Linear Algebra

Linear algebra provides the mathematical foundation for numerous real-world applications across science, engineering, and data analysis. Graph theory models networks via adjacency and Laplacian matrices. Markov chains describe stochastic processes through transition matrices and steady-state analysis. Cryptography uses matrix multiplication for encryption and decryption. Systems of differential equations are solved via diagonalization and matrix exponentials. In machine learning and data science, principal component analysis, linear regression, and PageRank are fundamentally linear algebraic algorithms.

---

## 1. Graphs and Networks

### 1.1 Adjacency Matrix

For a graph with $n$ vertices, the **adjacency matrix** $A$ is $n \times n$ with $A_{ij} = 1$ if there is an edge from vertex $i$ to vertex $j$, and $0$ otherwise.

### 1.2 Laplacian Matrix

The **Laplacian** $L = D - A$, where $D$ is the degree matrix (diagonal with $D_{ii} = \text{degree of vertex } i$). Properties:

- $L$ is symmetric and positive semidefinite.
- The smallest eigenvalue of $L$ is $0$ (with eigenvector $\mathbf{1}$).
- The second smallest eigenvalue measures graph connectivity (Fiedler value).

### 1.3 Kirchhoff's Laws and Network Flow

For electrical circuits, linear systems derived from Kirchhoff's current and voltage laws can be expressed as $A\mathbf{x} = \mathbf{b}$, where $A$ encodes the network structure.

---

## 2. Markov Chains

### 2.1 Stochastic Matrix

A **stochastic matrix** $P$ has non-negative entries with each column summing to $1$. It models transitions between states in a Markov chain.

### 2.2 Steady-State Distribution

The steady-state (stationary) distribution $\pi$ satisfies:

$$
P \pi = \pi
$$

i.e., $\pi$ is the eigenvector corresponding to eigenvalue $\lambda = 1$. For a regular Markov chain, $P^k$ converges to a matrix whose columns are all $\pi$.

### 2.3 Power Iteration

The convergence $P^k \mathbf{x} \to \pi$ (for any initial $\mathbf{x}$ with non-negative entries summing to $1$) follows from the eigenvalue properties of stochastic matrices.

---

## 3. Coding and Cryptography

### 3.1 Hill Cipher

Encryption: $\mathbf{c} = A \mathbf{p} \mod m$, where $\mathbf{p}$ is the plaintext vector, $A$ is an invertible key matrix, and $m$ is the modulus (typically $26$).

Decryption: $\mathbf{p} = A^{-1} \mathbf{c} \mod m$.

The matrix $A$ must be chosen so that $\det(A)$ is invertible modulo $m$.

### 3.2 Error-Correcting Codes

Linear codes use generator matrices $G$ to encode messages and parity-check matrices $H$ to detect and correct errors. The null space of $H$ gives the set of valid codewords.

---

## 4. Differential Equations

### 4.1 System of Linear ODEs

A system $\frac{d\mathbf{x}}{dt} = A\mathbf{x}$ has solution:

$$
\mathbf{x}(t) = e^{At} \mathbf{x}(0)
$$

where the matrix exponential is defined by:

$$
e^{At} = I + At + \frac{A^2 t^2}{2!} + \frac{A^3 t^3}{3!} + \cdots
$$

### 4.2 Solution via Diagonalization

If $A$ is diagonalizable, $A = PDP^{-1}$:

$$
e^{At} = P e^{Dt} P^{-1}
$$

where $e^{Dt} = \text{diag}(e^{\lambda_1 t}, e^{\lambda_2 t}, \ldots, e^{\lambda_n t})$.

### 4.3 Stability

The system is stable if all eigenvalues of $A$ have negative real parts. If any eigenvalue has a positive real part, the system is unstable.

---

## 5. Machine Learning and Data Science

### 5.1 Principal Component Analysis (PCA)

PCA finds the directions of maximum variance in a dataset. If $X$ is the centered data matrix ($n$ samples $\times$ $p$ features), the principal components are the eigenvectors of $X^\mathsf{T} X$, computed efficiently via SVD.

### 5.2 Linear Regression

The least-squares solution $\hat{\mathbf{x}} = (A^\mathsf{T} A)^{-1} A^\mathsf{T} \mathbf{b}$ is the core of linear regression, where $A$ contains the feature values and $\mathbf{b}$ contains the targets.

### 5.3 PageRank

Google's PageRank algorithm computes the stationary distribution of a modified web graph transition matrix:

$$
P = \alpha M + (1 - \alpha) \frac{1}{n} \mathbf{1} \mathbf{1}^\mathsf{T}
$$

where $M$ is the raw transition matrix and $\alpha$ is the damping factor (typically $0.85$). The PageRank vector is the eigenvector corresponding to eigenvalue $1$.

### 5.4 Neural Networks

Feedforward neural networks compute $\mathbf{h} = \sigma(W\mathbf{x} + \mathbf{b})$ repeatedly, where $W$ is a weight matrix, $\mathbf{b}$ is a bias vector, and $\sigma$ is a non-linear activation function. The matrix multiplications dominate the computation.

---

## Solved Exercises

### Exercise 1: Markov Chain Steady State

**Problem:**
Find the steady-state distribution for the transition matrix:

$$
P = \begin{bmatrix} 0.7 & 0.2 \\ 0.3 & 0.8 \end{bmatrix}
$$

**Solution:**
Solve $P\pi = \pi$, i.e., $(P - I)\pi = \mathbf{0}$:

$$
\begin{bmatrix} -0.3 & 0.2 \\ 0.3 & -0.2 \end{bmatrix}
\begin{pmatrix} \pi_1 \\ \pi_2 \end{pmatrix} = \mathbf{0}
$$

This gives $-0.3\pi_1 + 0.2\pi_2 = 0 \Rightarrow 3\pi_1 = 2\pi_2$.

With $\pi_1 + \pi_2 = 1$: $\pi_1 + \frac{3}{2}\pi_1 = 1 \Rightarrow \frac{5}{2}\pi_1 = 1 \Rightarrow \pi_1 = \frac{2}{5} = 0.4$, $\pi_2 = 0.6$.

**Steady state:** $\pi = (0.4, 0.6)$.

---

### Exercise 2: Hill Cipher Encryption

**Problem:**
Encrypt the message "HI" using the Hill cipher with key $A = \begin{bmatrix} 3 & 1 \\ 5 & 2 \end{bmatrix}$ modulo 26.

**Solution:**
Convert letters to numbers: H = 7, I = 8. Plaintext vector: $\mathbf{p} = \begin{pmatrix} 7 \\ 8 \end{pmatrix}$.

Encrypt: $\mathbf{c} = A\mathbf{p} \mod 26$:

$$
\mathbf{c} = \begin{bmatrix} 3 & 1 \\ 5 & 2 \end{bmatrix}
\begin{pmatrix} 7 \\ 8 \end{pmatrix}
= \begin{pmatrix} 3\cdot7 + 1\cdot8 \\ 5\cdot7 + 2\cdot8 \end{pmatrix}
= \begin{pmatrix} 21 + 8 \\ 35 + 16 \end{pmatrix}
= \begin{pmatrix} 29 \\ 51 \end{pmatrix}
\mod 26
$$

$29 \mod 26 = 3$, $51 \mod 26 = 25$. So $\mathbf{c} = \begin{pmatrix} 3 \\ 25 \end{pmatrix}$, which corresponds to letters "CZ".

---

### Exercise 3: Hill Cipher Decryption

**Problem:**
Decrypt the ciphertext "CZ" from Exercise 2.

**Solution:**
$A^{-1} \mod 26$: $\det(A) = 3\cdot2 - 1\cdot5 = 6 - 5 = 1$, which is invertible mod 26.

$A^{-1} = \begin{bmatrix} 2 & -1 \\ -5 & 3 \end{bmatrix} \mod 26 = \begin{bmatrix} 2 & 25 \\ 21 & 3 \end{bmatrix}$.

Decrypt: $\mathbf{p} = A^{-1}\mathbf{c} = \begin{bmatrix} 2 & 25 \\ 21 & 3 \end{bmatrix}
\begin{pmatrix} 3 \\ 25 \end{pmatrix}
= \begin{pmatrix} 2\cdot3 + 25\cdot25 \\ 21\cdot3 + 3\cdot25 \end{pmatrix}
= \begin{pmatrix} 6 + 625 \\ 63 + 75 \end{pmatrix}
= \begin{pmatrix} 631 \\ 138 \end{pmatrix}
\mod 26$.

$631 \mod 26 = 631 - 24\cdot26 = 631 - 624 = 7$.
$138 \mod 26 = 138 - 5\cdot26 = 138 - 130 = 8$.

$\mathbf{p} = \begin{pmatrix} 7 \\ 8 \end{pmatrix}$, which is "HI".

---

### Exercise 4: Solving a System of ODEs

**Problem:**
Solve $\frac{d\mathbf{x}}{dt} = A\mathbf{x}$ with $A = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}$ and $\mathbf{x}(0) = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$.

**Solution:**
From earlier eigenvalue analysis, $A = PDP^{-1}$ with $P = \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}$, $D = \begin{bmatrix} 3 & 0 \\ 0 & 1 \end{bmatrix}$.

$\mathbf{x}(t) = P e^{Dt} P^{-1} \mathbf{x}(0)$.

$e^{Dt} = \begin{bmatrix} e^{3t} & 0 \\ 0 & e^{t} \end{bmatrix}$.

$P^{-1} \mathbf{x}(0) = \begin{bmatrix} \frac{1}{2} & \frac{1}{2} \\ \frac{1}{2} & -\frac{1}{2} \end{bmatrix}
\begin{pmatrix} 1 \\ 0 \end{pmatrix}
= \begin{pmatrix} \frac{1}{2} \\ \frac{1}{2} \end{pmatrix}$.

$e^{Dt} P^{-1} \mathbf{x}(0) = \begin{pmatrix} \frac{1}{2}e^{3t} \\ \frac{1}{2}e^{t} \end{pmatrix}$.

$\mathbf{x}(t) = P \begin{pmatrix} \frac{1}{2}e^{3t} \\ \frac{1}{2}e^{t} \end{pmatrix}
= \begin{pmatrix} \frac{1}{2}e^{3t} + \frac{1}{2}e^{t} \\ \frac{1}{2}e^{3t} - \frac{1}{2}e^{t} \end{pmatrix}$.

**Solution:** $x_1(t) = \frac{1}{2}(e^{3t} + e^{t})$, $x_2(t) = \frac{1}{2}(e^{3t} - e^{t})$.

---

### Exercise 5: Graph Laplacian

**Problem:**
Find the Laplacian matrix of a graph with 3 vertices: edges (1-2) and (2-3), and no edge (1-3).

**Solution:**
Degree matrix: $D = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1 \end{bmatrix}$.

Adjacency matrix: $A = \begin{bmatrix} 0 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 0 \end{bmatrix}$.

Laplacian: $L = D - A = \begin{bmatrix} 1 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 1 \end{bmatrix}$.

Eigenvalues of $L$: $\lambda = 0, 1, 3$. The second smallest eigenvalue (Fiedler value) is $1 > 0$, indicating the graph is connected.

---

### Exercise 6: Power Iteration for Markov Chain

**Problem:**
Starting from $\mathbf{x}^{(0)} = (1, 0)$, compute $\mathbf{x}^{(3)} = P^3 \mathbf{x}^{(0)}$ for $P = \begin{bmatrix} 0.7 & 0.2 \\ 0.3 & 0.8 \end{bmatrix}$.

**Solution:**
$\mathbf{x}^{(1)} = P\mathbf{x}^{(0)} = \begin{bmatrix} 0.7 & 0.2 \\ 0.3 & 0.8 \end{bmatrix}
\begin{pmatrix} 1 \\ 0 \end{pmatrix}
= \begin{pmatrix} 0.7 \\ 0.3 \end{pmatrix}$.

$\mathbf{x}^{(2)} = P\mathbf{x}^{(1)} = \begin{bmatrix} 0.7 & 0.2 \\ 0.3 & 0.8 \end{bmatrix}
\begin{pmatrix} 0.7 \\ 0.3 \end{pmatrix}
= \begin{pmatrix} 0.7\cdot0.7 + 0.2\cdot0.3 \\ 0.3\cdot0.7 + 0.8\cdot0.3 \end{pmatrix}
= \begin{pmatrix} 0.49 + 0.06 \\ 0.21 + 0.24 \end{pmatrix}
= \begin{pmatrix} 0.55 \\ 0.45 \end{pmatrix}$.

$\mathbf{x}^{(3)} = P\mathbf{x}^{(2)} = \begin{bmatrix} 0.7 & 0.2 \\ 0.3 & 0.8 \end{bmatrix}
\begin{pmatrix} 0.55 \\ 0.45 \end{pmatrix}
= \begin{pmatrix} 0.7\cdot0.55 + 0.2\cdot0.45 \\ 0.3\cdot0.55 + 0.8\cdot0.45 \end{pmatrix}
= \begin{pmatrix} 0.385 + 0.090 \\ 0.165 + 0.360 \end{pmatrix}
= \begin{pmatrix} 0.475 \\ 0.525 \end{pmatrix}$.

The distribution is converging toward $(0.4, 0.6)$.

---

### Exercise 7: Linear Regression via Normal Equations

**Problem:**
Fit a line $y = \beta_0 + \beta_1 x$ to the points $(0, 1)$, $(1, 2)$, $(2, 3)$.

**Solution:**
$A = \begin{bmatrix} 1 & 0 \\ 1 & 1 \\ 1 & 2 \end{bmatrix}$, $\mathbf{b} = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}$.

$A^\mathsf{T} A = \begin{bmatrix} 1 & 1 & 1 \\ 0 & 1 & 2 \end{bmatrix}
\begin{bmatrix} 1 & 0 \\ 1 & 1 \\ 1 & 2 \end{bmatrix}
= \begin{bmatrix} 3 & 3 \\ 3 & 5 \end{bmatrix}$.

$A^\mathsf{T} \mathbf{b} = \begin{bmatrix} 1 & 1 & 1 \\ 0 & 1 & 2 \end{bmatrix}
\begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}
= \begin{pmatrix} 6 \\ 8 \end{pmatrix}$.

Solve $\begin{bmatrix} 3 & 3 \\ 3 & 5 \end{bmatrix}
\begin{pmatrix} \beta_0 \\ \beta_1 \end{pmatrix}
= \begin{pmatrix} 6 \\ 8 \end{pmatrix}$.

From first: $3\beta_0 + 3\beta_1 = 6 \Rightarrow \beta_0 + \beta_1 = 2$.
Second: $3\beta_0 + 5\beta_1 = 8$.

Subtract: $(3\beta_0 + 5\beta_1) - 3(\beta_0 + \beta_1) = 8 - 3\cdot2 \Rightarrow 2\beta_1 = 2 \Rightarrow \beta_1 = 1$.

Then $\beta_0 = 2 - 1 = 1$.

**Line:** $y = 1 + x$. The points $(0, 1)$, $(1, 2)$, $(2, 3)$ are collinear, so the fit is exact.

---

### Exercise 8: PageRank on a Small Graph

**Problem:**
Compute the PageRank vector for a 2-node graph where node 1 links to node 2, and node 2 links to both node 1 and node 2. Use damping factor $\alpha = 0.85$.

**Solution:**
Raw transition matrix $M$: node 1 has 1 outgoing link (to node 2), node 2 has 2 outgoing links (to 1 and 2).

$$
M = \begin{bmatrix} 0 & 0.5 \\ 1 & 0.5 \end{bmatrix}
$$

Damped matrix: $P = 0.85M + 0.15 \cdot \frac{1}{2} \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}
= 0.85 \begin{bmatrix} 0 & 0.5 \\ 1 & 0.5 \end{bmatrix} + 0.075 \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}$.

$$
P = \begin{bmatrix} 0.075 & 0.5 \\ 0.925 & 0.5 \end{bmatrix}
$$

Solve $P\pi = \pi$: $(P - I)\pi = \mathbf{0}$:

$$
\begin{bmatrix} -0.925 & 0.5 \\ 0.925 & -0.5 \end{bmatrix}
\begin{pmatrix} \pi_1 \\ \pi_2 \end{pmatrix} = \mathbf{0}
$$

$-0.925\pi_1 + 0.5\pi_2 = 0 \Rightarrow 0.925\pi_1 = 0.5\pi_2 \Rightarrow \pi_2 = 1.85\pi_1$.

With $\pi_1 + \pi_2 = 1$: $\pi_1 + 1.85\pi_1 = 1 \Rightarrow 2.85\pi_1 = 1 \Rightarrow \pi_1 \approx 0.351$, $\pi_2 \approx 0.649$.

PageRank shows node 2 has higher importance because it receives links from both nodes.

---

## Exam Tip: PCA via SVD

On exams, PCA questions often boil down to computing the SVD of the centered data matrix. The principal component directions are the right singular vectors (columns of $V$), and the variance explained by each component is proportional to the squared singular value $\sigma_i^2$. To compute PCA manually on small datasets: center the data, compute $X^\mathsf{T} X$, find its eigenvectors and eigenvalues.

---