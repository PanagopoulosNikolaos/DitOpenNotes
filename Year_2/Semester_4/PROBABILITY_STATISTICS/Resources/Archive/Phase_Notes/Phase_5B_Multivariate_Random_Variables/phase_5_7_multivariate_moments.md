# Phase 5.7: Multivariate Random Variables - Moments and Joint Expectations

This file covers moments of joint distributions, including joint expectation, covariance, correlation, conditional expectation, and the properties of variances of sums of random variables.

---

## 1. Joint Expectations

The expected value of a function of two random variables, $g(X, Y)$, is defined as:

*   **Discrete Case:**
    $$E[g(X, Y)] = \sum_{x} \sum_{y} g(x, y) \cdot p_{X,Y}(x, y)$$
*   **Continuous Case:**
    $$E[g(X, Y)] = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} g(x, y) \cdot f(x, y) \, dx \, dy$$

### Linearity of Expectation
Expectation is always linear, regardless of whether $X$ and $Y$ are independent:

$$E[aX + bY + c] = aE[X] + bE[Y] + c$$

---

## 2. Covariance and Correlation

### 2.1 Covariance ($Cov(X, Y)$)
Covariance measures the strength of the linear relationship between two random variables.

*   **Definition:**
    $$Cov(X, Y) = E[(X - E[X])(Y - E[Y])] = E[XY] - E[X]E[Y]$$
*   **Key Properties:**
    1.  $Cov(X, X) = Var(X)$
    2.  $Cov(X, Y) = Cov(Y, X)$
    3.  $Cov(aX + b, cY + d) = ac \cdot Cov(X, Y)$
    4.  **Independence:** If $X$ and $Y$ are independent, then $E[XY] = E[X]E[Y]$, which implies:
        $$Cov(X, Y) = 0$$

> **Exam Warning (True/False Gotcha):** If $Cov(X, Y) = 0$, $X$ and $Y$ are **not necessarily independent**. They are only uncorrelated. There can still be non-linear relationships.

### 2.2 Correlation Coefficient ($\rho_{X,Y}$)
Correlation scale-normalizes covariance to a value between $-1$ and $+1$.

$$\rho_{X,Y} = \frac{Cov(X, Y)}{\sigma_X \sigma_Y} = \frac{Cov(X, Y)}{\sqrt{Var(X) Var(Y)}}$$

*   $\rho = 1$: Perfect positive linear relationship.
*   $\rho = -1$: Perfect negative linear relationship.
*   $\rho = 0$: No linear relationship (uncorrelated).

---

## 3. Variance of a Linear Combination

For any random variables $X$ and $Y$:

$$Var(aX + bY) = a^2 Var(X) + b^2 Var(Y) + 2ab \cdot Cov(X, Y)$$

If $X$ and $Y$ are **independent** (or simply uncorrelated):

$$Var(aX + bY) = a^2 Var(X) + b^2 Var(Y)$$

Specifically, $Var(X - Y) = Var(X) + Var(Y)$ for independent variables. A very common exam mistake is writing $Var(X - Y) = Var(X) - Var(Y)$.

---

## 4. Conditional Expectation and Variance

### 4.1 Conditional Expectation ($E[X | Y]$)
*   **Discrete:** $E[X | Y = y] = \sum_{x} x \cdot p_{X|Y}(x | y)$
*   **Continuous:** $E[X | Y = y] = \int_{-\infty}^{\infty} x \cdot f_{X|Y}(x | y) \, dx$

### 4.2 Law of Total Expectation (Adam's Law)
The overall expected value of $X$ can be found by taking the expected value of the conditional expectation:

$$E[E[X|Y]] = E[X]$$

### 4.3 Law of Total Variance (Eve's Law)
The overall variance of $X$ is divided into the expectation of conditional variance and the variance of conditional expectation:

$$Var(X) = E[Var(X|Y)] + Var(E[X|Y])$$

---

## 5. Solved Exercises (9 Examples)

### Exercise 1: Discrete Covariance
**Problem:** Calculate $Cov(X, Y)$ using the joint PMF table from Phase 5.6 Exercise 1:

| $X \setminus Y$ | 0 | 1 | 2 |
| :--- | :--- | :--- | :--- |
| **0** | 0.1 | 0.2 | 0.05 |
| **1** | 0.15 | 0.1 | 0.15 |
| **2** | 0.05 | 0.1 | 0.1 |

Recall from marginals: $E[X] = 0.9$ and $E[Y] = 1.0$.

**Solution:**
- **Step 1: Calculate $E[XY]$.**
  $$E[XY] = \sum_x \sum_y x y \cdot p(x, y)$$
  Terms with 0 can be ignored:
  $$E[XY] = (1)(1)(0.1) + (1)(2)(0.15) + (2)(1)(0.1) + (2)(2)(0.1) = 0.1 + 0.3 + 0.2 + ?$$
- **Step 2: WIP State.**
  - Last term $= 0.4$.
  - $E[XY] = 0.1 + 0.3 + 0.2 + 0.4 = 1.0$.
  Apply the covariance shortcut formula:
  $$Cov(X, Y) = E[XY] - E[X]E[Y] = 1.0 - (0.9)(1.0) = ?$$
- **Step 3: Final Calculation.**
  $$Cov(X, Y) = 1.0 - 0.9 = 0.1.$$

---

### Exercise 2: Continuous Expectation $E[XY]$
**Problem:** Let $X$ and $Y$ have joint PDF $f(x, y) = x + y$ on $0 < x < 1, 0 < y < 1$. Find $E[XY]$.

**Solution:**
- **Step 1: Set up the double integral.**
  $$E[XY] = \int_{0}^{1} \int_{0}^{1} xy(x + y) \, dy \, dx = \int_{0}^{1} \int_{0}^{1} \left( x^2 y + x y^2 \right) \, dy \, dx$$
- **Step 2: WIP State.**
  Integrate with respect to $y$ first:
  $$\int_{0}^{1} \left( x^2 y + x y^2 \right) \, dy = \left[ x^2 \frac{y^2}{2} + x \frac{y^3}{3} \right]_{0}^{1} = \frac{x^2}{2} + \frac{x}{3}$$
  Now integrate with respect to $x$:
  $$\int_{0}^{1} \left( \frac{x^2}{2} + \frac{x}{3} \right) \, dx = \left[ \frac{x^3}{6} + \frac{x^2}{6} \right]_{0}^{1} = \frac{1}{6} + ?$$
- **Step 3: Final Calculation.**
  $$\text{Second term} = \frac{1}{6}$$
  $$E[XY] = \frac{1}{6} + \frac{1}{6} = \frac{1}{3} \approx 0.3333.$$

---

### Exercise 3: Correlation Calculation
**Problem:** For the setup in Exercise 2, given that $E[X] = E[Y] = \frac{7}{12}$ and $Var(X) = Var(Y) = \frac{11}{144}$, find the correlation coefficient $\rho_{X,Y}$.

**Solution:**
- **Step 1: Find covariance first.**
  $$Cov(X, Y) = E[XY] - E[X]E[Y] = \frac{1}{3} - \left(\frac{7}{12}\right)^2 = \frac{1}{3} - \frac{49}{144}$$
- **Step 2: WIP State.**
  - Common denominator for covariance: $\frac{1}{3} = \frac{48}{144}$.
  - $Cov(X, Y) = \frac{48}{144} - \frac{49}{144} = -\frac{1}{144}$.
  Now apply the correlation formula:
  $$\rho_{X,Y} = \frac{Cov(X, Y)}{\sqrt{Var(X) Var(Y)}} = \frac{-\frac{1}{144}}{\sqrt{\frac{11}{144} \cdot \frac{11}{144}}} = \frac{-\frac{1}{144}}{?}$$
- **Step 3: Final Calculation.**
  $$\text{Denominator} = \frac{11}{144}$$
  $$\rho_{X,Y} = \frac{-1/144}{11/144} = -\frac{1}{11} \approx -0.0909.$$

---

### Exercise 4: Uncorrelated but Dependent (Classic Exam Question)
**Problem:** Let $X \sim U(-1, 1)$ and $Y = X^2$. Show that $Cov(X, Y) = 0$, even though $X$ and $Y$ are completely dependent.

**Solution:**
- **Step 1: Find $E[X]$ and $E[XY]$.**
  Since $X \sim U(-1, 1)$, $E[X] = 0$.
  $$E[XY] = E[X \cdot X^2] = E[X^3]$$
- **Step 2: WIP State.**
  For any symmetric distribution around 0, odd moments are 0.
  $$E[X^3] = \int_{-1}^{1} x^3 \cdot \frac{1}{2} \, dx = \left[ \frac{x^4}{8} \right]_{-1}^{1} = \frac{1}{8} - ?$$
- **Step 3: Final Calculation.**
  $$\text{Second term} = \frac{1}{8}$$
  $$E[X^3] = 0$$
  $$Cov(X, Y) = E[XY] - E[X]E[Y] = 0 - (0)E[Y] = 0$$
  This proves they are uncorrelated, yet they are functionally dependent since $Y = X^2$.

---

### Exercise 5: Variance of a Sum
**Problem:** Let $X$ and $Y$ be random variables with $Var(X) = 9$, $Var(Y) = 16$, and $\rho_{X,Y} = 0.5$. Find $Var(2X - 3Y)$.

**Solution:**
- **Step 1: Compute standard deviations and covariance.**
  - $\sigma_X = \sqrt{9} = 3$
  - $\sigma_Y = \sqrt{16} = 4$
  - $Cov(X, Y) = \rho_{X,Y} \cdot \sigma_X \sigma_Y = 0.5 \cdot 3 \cdot 4 = 6$.
- **Step 2: WIP State.**
  Apply the variance formula:
  $$Var(2X - 3Y) = (2)^2 Var(X) + (-3)^2 Var(Y) + 2(2)(-3) \cdot Cov(X, Y)$$
  $$Var(2X - 3Y) = 4(9) + 9(16) - 12(6) = 36 + 144 - ?$$
- **Step 3: Final Calculation.**
  - $12 \cdot 6 = 72$.
  - $Var(2X - 3Y) = 180 - 72 = 108$.

---

### Exercise 6: Conditional Expectation (Continuous)
**Problem:** Let $f(x, y) = \frac{2}{3}(x + 2y)$ on $0 < x < 1, 0 < y < 1$. Find $E[X | Y = y]$.

**Solution:**
- **Step 1: Write down the conditional PDF.**
  From Phase 5.6 Exercise 5, we have:
  $$f_{X|Y}(x | y) = \frac{2(x + 2y)}{1 + 4y}, \quad 0 < x < 1$$
- **Step 2: WIP State.**
  Integrate $x \cdot f_{X|Y}(x | y)$:
  $$E[X | Y = y] = \int_{0}^{1} x \cdot \frac{2(x + 2y)}{1 + 4y} \, dx = \frac{2}{1 + 4y} \int_{0}^{1} (x^2 + 2xy) \, dx$$
  Evaluate the integral:
  $$\int_{0}^{1} (x^2 + 2xy) \, dx = \left[ \frac{x^3}{3} + x^2 y \right]_{0}^{1} = \frac{1}{3} + ?$$
- **Step 3: Final Calculation.**
  - Integral value $= \frac{1}{3} + y = \frac{1 + 3y}{3}$.
  - $E[X | Y = y] = \frac{2}{1 + 4y} \cdot \frac{1 + 3y}{3} = \frac{2(1 + 3y)}{3(1 + 4y)}$.

---

### Exercise 7: Applying Adam's Law (Law of Total Expectation)
**Problem:** A hen lays $N$ eggs, where $N \sim Po(\lambda)$. Each egg hatches with probability $p$ independently. Let $X$ be the number of hatched chicks. Find $E[X]$.

**Solution:**
- **Step 1: Identify conditional distribution.**
  Given $N = n$ eggs, the number of hatched chicks $X$ follows a Binomial distribution:
  $$X | N = n \sim B(n, p)$$
  Therefore, $E[X | N] = Np$.
- **Step 2: WIP State.**
  Apply Adam's Law:
  $$E[X] = E[E[X | N]] = E[Np] = p \cdot E[?]$$
- **Step 3: Final Calculation.**
  - Since $N \sim Po(\lambda)$, $E[N] = \lambda$.
  - $E[X] = p\lambda$.

---

### Exercise 8: Applying Eve's Law (Law of Total Variance)
**Problem:** For the egg hatching problem in Exercise 7, find the variance $Var(X)$.

**Solution:**
- **Step 1: Identify conditional moments.**
  - $E[X | N] = Np$
  - $Var(X | N) = Np(1-p)$
- **Step 2: WIP State.**
  Apply Eve's Law:
  $$Var(X) = E[Var(X|N)] + Var(E[X|N])$$
  $$Var(X) = E[Np(1-p)] + Var(Np) = p(1-p)E[N] + p^2 Var(N)$$
  Recall that for $N \sim Po(\lambda)$, $E[N] = Var(N) = \lambda$.
  $$Var(X) = p(1-p)\lambda + p^2 \cdot ?$$
- **Step 3: Final Calculation.**
  - $Var(N) = \lambda$.
  - $Var(X) = p\lambda - p^2\lambda + p^2\lambda = p\lambda$.
  *(Interesting result: Both $E[X]$ and $Var(X)$ equal $p\lambda$, suggesting $X$ itself is Poisson distributed, which is indeed true!).*

---

### Exercise 9: Covariance of Sums (General Property)
**Problem:** Prove that for any random variables $X, Y, Z$ and constants $a, b$:
$$Cov(aX + bY, Z) = a \cdot Cov(X, Z) + b \cdot Cov(Y, Z)$$

**Solution:**
- **Step 1: Use the covariance definition.**
  $$Cov(aX + bY, Z) = E[(aX + bY)Z] - E[aX + bY]E[Z]$$
- **Step 2: WIP State.**
  Distribute and apply linearity of expectation:
  $$E[aXZ + bYZ] - (aE[X] + bE[Y])E[Z] = aE[XZ] + bE[YZ] - aE[X]E[Z] - bE[Y]E[Z]$$
  Group the terms by constants $a$ and $b$:
  $$a \left( E[XZ] - E[X]E[Z] \right) + b \left( ? \right)$$
- **Step 3: Final Calculation.**
  - The second grouped term is $E[YZ] - E[Y]E[Z]$.
  - Rewrite using covariance definition:
    $$Cov(aX + bY, Z) = a \cdot Cov(X, Z) + b \cdot Cov(Y, Z).$$
