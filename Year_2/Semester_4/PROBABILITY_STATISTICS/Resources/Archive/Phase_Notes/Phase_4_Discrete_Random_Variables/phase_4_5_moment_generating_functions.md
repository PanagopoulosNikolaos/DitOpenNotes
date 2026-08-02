# Phase 4.5: Moment Generating Functions and Characteristic Functions

This file introduces **Moment Generating Functions (MGFs)** and **Characteristic Functions**, which are powerful tools for finding moments (mean, variance, etc.) and identifying the distributions of sums of independent random variables.

---

## 1. Moment Generating Function (MGF)

### 1.1 Definition
The Moment Generating Function $M_X(t)$ of a random variable $X$ is defined for all real values of $t$ for which the expected value exists in an open interval around $t = 0$:

$$M_X(t) = E\left[e^{tX}\right]$$

*   **Discrete RV:** $M_X(t) = \sum_{x} e^{tx} \cdot P(X = x)$
*   **Continuous RV:** $M_X(t) = \int_{-\infty}^{\infty} e^{tx} \cdot f(x) \, dx$

### 1.2 Finding Moments via Differentiation
The term "moment generating" comes from the fact that we can generate any $n$-th raw moment $E[X^n]$ by taking the $n$-th derivative of $M_X(t)$ with respect to $t$ and evaluating it at $t = 0$:

$$E[X^n] = \left. \frac{d^n}{dt^n} M_X(t) \right|_{t=0} = M_X^{(n)}(0)$$

Specifically:
*   **Mean:** $E[X] = M'_X(0)$
*   **Variance:** $Var(X) = E[X^2] - (E[X])^2 = M''_X(0) - (M'_X(0))^2$

### 1.3 Key Properties
1.  **Linear Transformation:** If $Y = aX + b$, then:
    $$M_Y(t) = M_{aX+b}(t) = e^{bt} \cdot M_X(at)$$
2.  **Sum of Independent RVs:** If $X$ and $Y$ are independent random variables, the MGF of their sum is the product of their individual MGFs:
    $$M_{X+Y}(t) = M_X(t) \cdot M_Y(t)$$
3.  **Uniqueness Theorem:** If two random variables have the same MGF in an interval containing 0, they have the exact same probability distribution.

---

## 2. Common MGFs

| Distribution | parameters | MGF $M_X(t)$ |
| :--- | :--- | :--- |
| **Bernoulli** | $p$ | $q + p e^t \quad (\text{where } q = 1-p)$ |
| **Binomial** | $n, p$ | $(q + p e^t)^n$ |
| **Poisson** | $\lambda$ | $e^{\lambda (e^t - 1)}$ |
| **Geometric** (Definition A) | $p$ | $\frac{p e^t}{1 - q e^t} \quad (\text{for } t < -\ln q)$ |
| **Exponential** | $\lambda$ | $\frac{\lambda}{\lambda - t} \quad (\text{for } t < \lambda)$ |
| **Normal** | $\mu, \sigma^2$ | $e^{\mu t + \frac{1}{2}\sigma^2 t^2}$ |

---

## 3. Characteristic Function ($\phi_X(t)$)

The MGF of a random variable might not exist if the integral or sum does not converge for $t \neq 0$ (e.g., Cauchy distribution). To guarantee existence, we define the **Characteristic Function** using complex numbers:

$$\phi_X(t) = E\left[e^{itX}\right] = E[\cos(tX)] + i \cdot E[\sin(tX)]$$

Since $|e^{itX}| = 1$ for all real $t$ and $X$, the expectation $\phi_X(t)$ is **guaranteed to exist** for all random variables. The properties of characteristic functions are identical to MGFs, replacing $t$ with $it$.

---

## 4. Solved Exercises (9 Examples)

### Exercise 1: Finding moments from an MGF
**Problem:** The MGF of a random variable $X$ is $M_X(t) = \frac{1}{1 - 2t}$ for $t < 0.5$. Find the mean and variance of $X$.

**Solution:**
- **Step 1: Compute the first derivative.**
  $$M_X(t) = (1 - 2t)^{-1}$$
  $$M'_X(t) = -1 \cdot (1 - 2t)^{-2} \cdot (-2) = 2 \cdot (1 - 2t)^{-2}$$
- **Step 2: WIP State for mean.**
  Evaluate at $t=0$:
  $$E[X] = M'_X(0) = 2 \cdot (1 - 0)^{-2} = ?$$
- **Step 3: Compute the second derivative and variance.**
  - Mean $E[X] = 2$.
  - Second derivative:
    $$M''_X(t) = 2 \cdot (-2) \cdot (1 - 2t)^{-3} \cdot (-2) = 8 \cdot (1 - 2t)^{-3}$$
  - Evaluate at $t=0$: $E[X^2] = M''_X(0) = 8 \cdot (1)^{-3} = 8$.
  - Variance:
    $$Var(X) = E[X^2] - (E[X])^2 = 8 - 2^2 = 8 - 4 = 4.$$

---

### Exercise 2: Deriving the MGF of a Bernoulli Distribution
**Problem:** Derive the MGF of a Bernoulli random variable $X$ with success probability $p$.

**Solution:**
- **Step 1: Set up the sum.**
  A Bernoulli variable takes value 1 with probability $p$ and 0 with probability $q = 1-p$.
- **Step 2: WIP State.**
  $$M_X(t) = E\left[e^{tX}\right] = e^{t(0)} \cdot P(X=0) + e^{t(1)} \cdot P(X=1) = 1 \cdot q + ?$$
- **Step 3: Final Calculation.**
  $$M_X(t) = q + p e^t.$$

---

### Exercise 3: Sum of Independent Poissons
**Problem:** Let $X \sim Po(\lambda_1)$ and $Y \sim Po(\lambda_2)$ be independent random variables. Find the distribution of $W = X + Y$.

**Solution:**
- **Step 1: Set up the MGF multiplication.**
  Since $X$ and $Y$ are independent, $M_W(t) = M_X(t) \cdot M_Y(t)$.
- **Step 2: WIP State.**
  $$M_X(t) = e^{\lambda_1 (e^t - 1)}, \quad M_Y(t) = e^{\lambda_2 (e^t - 1)}$$
  $$M_W(t) = e^{\lambda_1 (e^t - 1)} \cdot e^{\lambda_2 (e^t - 1)} = e^{?}$$
- **Step 3: Final Calculation.**
  $$M_W(t) = e^{(\lambda_1 + \lambda_2)(e^t - 1)}$$
  By the uniqueness theorem, this is the MGF of a Poisson distribution with parameter $\lambda_1 + \lambda_2$.
  Thus, $W \sim Po(\lambda_1 + \lambda_2)$.

---

### Exercise 4: MGF Linear Transformation
**Problem:** If $X$ has MGF $M_X(t) = e^{2t + 8t^2}$, find the MGF of $Y = 3X - 5$.

**Solution:**
- **Step 1: Use the linear transformation formula.**
  $$M_Y(t) = e^{-5t} \cdot M_X(3t)$$
- **Step 2: WIP State.**
  Substitute $3t$ for $t$ in $M_X(t)$:
  $$M_X(3t) = e^{2(3t) + 8(3t)^2} = e^{6t + 8(9t^2)} = e^{6t + ?}$$
- **Step 3: Final Calculation.**
  $$M_X(3t) = e^{6t + 72t^2}$$
  $$M_Y(t) = e^{-5t} \cdot e^{6t + 72t^2} = e^{(-5t + 6t + 72t^2)} = e^{t + 72t^2}$$
  *(Exam note: Since the MGF of a normal variable is $e^{\mu t + \frac{1}{2}\sigma^2 t^2}$, this proves $Y \sim N(1, 144)$ because $\mu = 1$ and $\frac{1}{2}\sigma^2 = 72 \Rightarrow \sigma^2 = 144$.)*

---

### Exercise 5: Expected value from discrete probability generating MGF
**Problem:** A discrete random variable $X$ has PMF $P(X=1) = 0.2$, $P(X=2) = 0.5$, $P(X=3) = 0.3$. Write its MGF and compute the mean.

**Solution:**
- **Step 1: Write the MGF expression.**
  $$M_X(t) = \sum e^{tx} P(X=x) = 0.2 e^t + 0.5 e^{2t} + 0.3 e^{3t}$$
- **Step 2: WIP State for derivative.**
  $$M'_X(t) = \frac{d}{dt}\left(0.2 e^t + 0.5 e^{2t} + 0.3 e^{3t}\right) = 0.2 e^t + 1.0 e^{2t} + ?$$
- **Step 3: Final Calculation.**
  $$M'_X(t) = 0.2 e^t + 1.0 e^{2t} + 0.9 e^{3t}$$
  Evaluate at $t=0$:
  $$E[X] = M'_X(0) = 0.2 + 1.0 + 0.9 = 2.1.$$

---

### Exercise 6: Sum of Independent Binomials
**Problem:** Let $X \sim B(n, p)$ and $Y \sim B(m, p)$ be independent random variables. Find the distribution of $W = X + Y$.

**Solution:**
- **Step 1: Recall MGF formulas.**
  $$M_X(t) = (q + p e^t)^n, \quad M_Y(t) = (q + p e^t)^m$$
- **Step 2: WIP State.**
  $$M_W(t) = M_X(t) \cdot M_Y(t) = (q + p e^t)^n \cdot (q + p e^t)^m = (q + p e^t)^{?}$$
- **Step 3: Final Calculation.**
  $$M_W(t) = (q + p e^t)^{n+m}$$
  By the uniqueness theorem, this matches the MGF of a Binomial distribution with parameters $n+m$ and $p$.
  Thus, $W \sim B(n + m, p)$.
  *(Warning: This property ONLY holds if the success probability $p$ is identical for both variables!)*

---

### Exercise 7: Deriving Exponential MGF
**Problem:** Derive the MGF of $X \sim Exp(\lambda)$.

**Solution:**
- **Step 1: Set up the integral.**
  The PDF is $f(x) = \lambda e^{-\lambda x}$ for $x \ge 0$.
  $$M_X(t) = \int_{0}^{\infty} e^{tx} \cdot \lambda e^{-\lambda x} \, dx = \lambda \int_{0}^{\infty} e^{(t - \lambda)x} \, dx$$
- **Step 2: WIP State.**
  Evaluate the integral (assuming $t < \lambda$ for convergence):
  $$\int_{0}^{\infty} e^{(t - \lambda)x} \, dx = \left[ \frac{e^{(t - \lambda)x}}{t - \lambda} \right]_{0}^{\infty} = 0 - \frac{1}{?}$$
- **Step 3: Final Calculation.**
  $$\text{Denominator} = t - \lambda$$
  $$M_X(t) = \lambda \cdot \left( \frac{-1}{t - \lambda} \right) = \frac{\lambda}{\lambda - t} \quad (\text{for } t < \lambda).$$

---

### Exercise 8: Expansion of MGF to find moments
**Problem:** If the MGF of $X$ is $M_X(t) = e^{t^2/2}$, find $E[X^4]$ using Taylor expansion.

**Solution:**
- **Step 1: Recall the Taylor series for $e^u$.**
  $$e^u = 1 + u + \frac{u^2}{2!} + \frac{u^3}{3!} + \dots$$
- **Step 2: WIP State.**
  Substitute $u = t^2/2$:
  $$M_X(t) = 1 + \left(\frac{t^2}{2}\right) + \frac{\left(\frac{t^2}{2}\right)^2}{2!} + \frac{\left(\frac{t^2}{2}\right)^3}{3!} + \dots$$
  $$M_X(t) = 1 + \frac{t^2}{2} + \frac{t^4}{8} + \dots$$
  Recall the general definition of MGF as a power series of moments:
  $$M_X(t) = \sum_{k=0}^{\infty} \frac{E[X^k]}{k!} t^k = 1 + E[X]t + \frac{E[X^2]}{2!} t^2 + \frac{E[X^3]}{3!} t^3 + \frac{E[X^4]}{4!} t^4 + \dots$$
- **Step 3: Final Calculation.**
  Compare coefficients of $t^4$:
  $$\frac{E[X^4]}{4!} = \frac{1}{8} \implies E[X^4] = \frac{4!}{8} = \frac{24}{8} = 3.$$

---

### Exercise 9: Characteristic function of a symmetric distribution
**Problem:** Show that if a random variable $X$ is symmetric about 0 (i.e. $X$ and $-X$ have the same distribution), then its characteristic function $\phi_X(t)$ is purely real.

**Solution:**
- **Step 1: Relate $\phi_X(t)$ to $\phi_{-X}(t)$.**
  $$\phi_{-X}(t) = E\left[e^{it(-X)}\right] = \phi_X(-t)$$
- **Step 2: WIP State.**
  Since $X$ is symmetric, $X \sim -X$, meaning their characteristic functions must be identical:
  $$\phi_X(t) = \phi_{-X}(t) \implies \phi_X(t) = \phi_X(-t)$$
  Also, recall that the complex conjugate is:
  $$\overline{\phi_X(t)} = \overline{E[\cos(tX) + i\sin(tX)]} = E[\cos(tX)] - i E[\sin(tX)] = \phi_X(-t)$$
- **Step 3: Final Calculation.**
  Combining these yields:
  $$\overline{\phi_X(t)} = \phi_X(t)$$
  Any complex number equal to its own conjugate must be purely real. Thus, $\phi_X(t)$ is purely real (and specifically, $E[\sin(tX)] = 0$).
