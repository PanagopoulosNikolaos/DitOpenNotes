# Term Project: Google PageRank & Multivariate Least-Squares Regression

## Project Overview
This capstone computational project combines two cornerstone applications of modern linear algebra:
1. **The PageRank Algorithm**: Modeling the web as a directed graph and computing stationary authority probability vectors via the power iteration method on stochastic matrices.
2. **Multivariate Polynomial Regression**: Formulating overdetermined system modeling, normal equations, QR matrix factorizations, and condition number analysis to fit multidimensional empirical data.

---

## 1. Module 1: The Google PageRank Algorithm

### 1.1 Mathematical Formulation
Consider a web network of $n$ interconnected pages represented by directed graph $G = (V, E)$.
* Define adjacency matrix $A$, where $A_{ij} = 1$ if page $j$ links to page $i$, and $0$ otherwise.
* Construct the column-stochastic transition probability matrix $P$:
  $$P_{ij} = \begin{cases} \frac{A_{ij}}{c_j}, & c_j > 0 \\ \frac{1}{n}, & c_j = 0 \text{ (dangling node fix)} \end{cases}$$
  where $c_j = \sum_{k=1}^n A_{kj}$ is the out-degree of page $j$.
* To guarantee irreducibility and aperiodicity (satisfying the **Perron-Frobenius Theorem**), incorporate damping factor $d = 0.85$:
  $$M = d P + \frac{1 - d}{n} \mathbf{E}$$
  where $\mathbf{E} = \mathbf{1}_{n \times n}$ is the matrix of all ones.

### 1.2 Power Iteration Algorithm
The steady-state PageRank vector $\mathbf{r}$ is the dominant eigenvector corresponding to eigenvalue $\lambda = 1$:
$$M \mathbf{r} = \mathbf{r}, \quad \|\mathbf{r}\|_1 = 1$$
Compute $\mathbf{r}$ via iterative power iteration:
$$\mathbf{r}^{(k+1)} = M \mathbf{r}^{(k)}$$
terminating when $\|\mathbf{r}^{(k+1)} - \mathbf{r}^{(k)}\|_2 < 10^{-8}$.

---

## 2. Module 2: Multivariate Least-Squares Regression

Given a multivariate observation matrix $X \in \mathbb{R}^{m \times p}$ and target vector $\mathbf{y} \in \mathbb{R}^m$ ($m > p$):
1. **Normal Equations Approach**:
   Solve for regression weights $\hat{\mathbf{w}}$:
   $$(X^T X) \hat{\mathbf{w}} = X^T \mathbf{y} \implies \hat{\mathbf{w}} = (X^T X)^{-1} X^T \mathbf{y}$$
2. **Numerically Stable QR Decomposition Approach**:
   Factor $X = QR$, where $Q^T Q = I_p$ and $R$ is upper triangular:
   $$R \hat{\mathbf{w}} = Q^T \mathbf{y}$$
   Solve for $\hat{\mathbf{w}}$ via back-substitution, avoiding the squaring of matrix condition numbers ($\kappa(X^T X) = \kappa(X)^2$).

---

## 3. Implementation Requirements (GNU Octave)

Develop modular, documented Octave scripts:
* `pagerank.m`: Accepts network link matrix, computes PageRank ranking, and identifies most influential nodes.
* `multivariate_regression.m`: Ingests multi-feature dataset, computes optimal weights via both Normal Equations and QR decomposition, reports mean squared error (MSE), and plots residuals.
* `run_benchmarks.m`: Tests computational performance and iteration convergence rates.

---

## 4. Evaluation Rubric

| Component | Target Metric | Points |
|:---|:---|:---:|
| PageRank Matrix Construction | Flawless handling of dangling nodes and damping factor $d=0.85$ | 25 |
| Power Iteration Convergence | Accurate convergence to eigenvalue $\lambda=1$ dominant eigenvector | 20 |
| Least-Squares Formulations | Mathematically correct Normal Equations and QR decomposition solvers | 25 |
| Numerical Stability Comparison | Detailed analysis comparing condition numbers and error norms | 15 |
| Documentation & Code Quality | Clean comments, modular functions, and reproducible sample datasets | 15 |
| **Total** | | **100** |

