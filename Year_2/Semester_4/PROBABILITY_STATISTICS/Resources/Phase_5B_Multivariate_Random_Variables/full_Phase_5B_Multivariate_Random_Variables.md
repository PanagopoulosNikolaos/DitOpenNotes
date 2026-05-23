# Phase 5.6: Multivariate Random Variables - Fundamentals

Multivariate random variables model scenarios where multiple outcomes are observed simultaneously from the same random experiment. We study joint, marginal, and conditional distributions for both discrete and continuous cases.

---

## 1. Joint and Marginal Distributions

### 1.1 Discrete Random Variables
Let $X$ and $Y$ be discrete random variables defined on the same sample space.

*   **Joint Probability Mass Function (Joint PMF):**
    $$p_{X,Y}(x, y) = P(X = x, Y = y)$$
    Subject to:
    $$\sum_{x} \sum_{y} p_{X,Y}(x, y) = 1$$
*   **Marginal PMFs:** To find the probability distribution of one variable alone, sum out the other variable:
    $$p_X(x) = \sum_{y} p_{X,Y}(x, y) \quad \text{and} \quad p_Y(y) = \sum_{x} p_{X,Y}(x, y)$$

### 1.2 Continuous Random Variables
Let $X$ and $Y$ be continuous random variables.

*   **Joint Probability Density Function (Joint PDF):**
    A function $f(x, y)$ such that:
    $$P((X, Y) \in A) = \iint_A f(x, y) \, dx \, dy$$
    Subject to:
    $$\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x, y) \, dx \, dy = 1 \quad \text{and} \quad f(x,y) \ge 0$$
*   **Marginal PDFs:** Integrate out the other variable:
    $$f_X(x) = \int_{-\infty}^{\infty} f(x, y) \, dy \quad \text{and} \quad f_Y(y) = \int_{-\infty}^{\infty} f(x, y) \, dx$$

---

## 2. Conditional Distributions

Conditional distributions describe the behavior of one random variable when the value of the other is known.

*   **Discrete Case:**
    $$p_{X|Y}(x | y) = P(X = x | Y = y) = \frac{p_{X,Y}(x, y)}{p_Y(y)} \quad (\text{provided } p_Y(y) > 0)$$
*   **Continuous Case:**
    $$f_{X|Y}(x | y) = \frac{f(x, y)}{f_Y(y)} \quad (\text{provided } f_Y(y) > 0)$$

---

## 3. Independence of Random Variables

Two random variables $X$ and $Y$ are independent if their joint distribution is the product of their marginal distributions for all values of $x$ and $y$.

*   **Discrete:** $p_{X,Y}(x, y) = p_X(x) \cdot p_Y(y)$
*   **Continuous:** $f(x, y) = f_X(x) \cdot f_Y(y)$

If this product relation fails for even a single coordinate in the domain, the variables are dependent.

---

## 4. Solved Exercises (9 Examples)

### Exercise 1: Discrete Joint PMF Table
**Problem:** The joint PMF of $X$ and $Y$ is given by the table below. Find the marginal PMF of $X$ and $Y$, and compute $P(X \le 1, Y \ge 1)$.

| $X \setminus Y$ | 0 | 1 | 2 |
| :--- | :--- | :--- | :--- |
| **0** | 0.1 | 0.2 | 0.05 |
| **1** | 0.15 | 0.1 | 0.15 |
| **2** | 0.05 | 0.1 | 0.1 |

**Solution:**
- **Step 1: Calculate marginals by summing rows and columns.**
  - Row sums (Marginal PMF of $X$):
    - $P(X=0) = 0.1 + 0.2 + 0.05 = 0.35$
    - $P(X=1) = 0.15 + 0.1 + 0.15 = 0.40$
    - $P(X=2) = 0.05 + 0.1 + 0.1 = ?$
- **Step 2: WIP State.**
  - $P(X=2) = 0.25$.
  - Column sums (Marginal PMF of $Y$):
    - $P(Y=0) = 0.1 + 0.15 + 0.05 = 0.30$
    - $P(Y=1) = 0.2 + 0.1 + 0.1 = 0.40$
    - $P(Y=2) = 0.05 + 0.15 + 0.1 = ?$
- **Step 3: Final Calculation.**
  - $P(Y=2) = 0.30$.
  - To find $P(X \le 1, Y \ge 1)$, sum cells where $X \in \{0, 1\}$ and $Y \in \{1, 2\}$:
    $$P(X \le 1, Y \ge 1) = p(0,1) + p(0,2) + p(1,1) + p(1,2)$$
    $$P(X \le 1, Y \ge 1) = 0.2 + 0.05 + 0.1 + 0.15 = 0.50.$$

---

### Exercise 2: Discrete Independence Check
**Problem:** Using the joint PMF table from Exercise 1, determine if $X$ and $Y$ are independent.

**Solution:**
- **Step 1: Check the independence condition $P(X=x, Y=y) = P(X=x)P(Y=y)$ for a specific cell.**
  Let's check the cell $(0,0)$.
  From the table: $P(X=0, Y=0) = 0.1$.
- **Step 2: WIP State.**
  From Exercise 1: $P(X=0) = 0.35$ and $P(Y=0) = 0.30$.
  $$P(X=0) \cdot P(Y=0) = 0.35 \cdot 0.30 = ?$$
- **Step 3: Final Calculation.**
  $$P(X=0) \cdot P(Y=0) = 0.105$$
  Since $0.1 \ne 0.105$, the independence condition fails.
  Therefore, $X$ and $Y$ are **dependent**.

---

### Exercise 3: Continuous Normalising Constant
**Problem:** Find the constant $c$ such that $f(x, y) = c(x + 2y)$ is a valid PDF on $0 < x < 1, 0 < y < 1$.

**Solution:**
- **Step 1: Set up the double integral equal to 1.**
  $$\int_{0}^{1} \int_{0}^{1} c(x + 2y) \, dy \, dx = 1$$
- **Step 2: WIP State.**
  Integrate with respect to $y$ first:
  $$\int_{0}^{1} \left[ c\left(xy + y^2\right) \right]_{0}^{1} \, dx = c \int_{0}^{1} (x + 1) \, dx$$
  Now integrate with respect to $x$:
  $$c \left[ \frac{x^2}{2} + x \right]_{0}^{1} = c \left( \frac{1}{2} + 1 \right) = c \cdot \frac{3}{2}$$
  Set this equal to 1:
  $$c \cdot \frac{3}{2} = 1 \implies c = ?$$
- **Step 3: Final Calculation.**
  $$c = \frac{2}{3}.$$

---

### Exercise 4: Continuous Marginal PDFs
**Problem:** For the joint PDF $f(x, y) = \frac{2}{3}(x + 2y)$ on $0 < x < 1, 0 < y < 1$, find the marginal PDFs of $X$ and $Y$.

**Solution:**
- **Step 1: Integrate out $y$ to find $f_X(x)$.**
  $$f_X(x) = \int_{0}^{1} \frac{2}{3}(x + 2y) \, dy = \frac{2}{3} \left[ xy + y^2 \right]_{0}^{1} = \frac{2}{3}(x + 1), \quad 0 < x < 1$$
- **Step 2: WIP State for $f_Y(y)$.**
  Integrate out $x$ to find $f_Y(y)$:
  $$f_Y(y) = \int_{0}^{1} \frac{2}{3}(x + 2y) \, dx = \frac{2}{3} \left[ \frac{x^2}{2} + 2xy \right]_{0}^{1} = \frac{2}{3}\left( \frac{1}{2} + ? \right)$$
- **Step 3: Final Calculation.**
  $$f_Y(y) = \frac{2}{3}\left( \frac{1}{2} + 2y \right) = \frac{1}{3} + \frac{4}{3}y, \quad 0 < y < 1.$$

---

### Exercise 5: Continuous Conditional PDF
**Problem:** Using the joint PDF from Exercise 4, find the conditional PDF of $X$ given $Y = y$, $f_{X|Y}(x | y)$.

**Solution:**
- **Step 1: Recall the conditional PDF formula.**
  $$f_{X|Y}(x | y) = \frac{f(x, y)}{f_Y(y)}$$
- **Step 2: WIP State.**
  From Exercise 4, $f_Y(y) = \frac{1 + 4y}{3}$ and $f(x, y) = \frac{2(x + 2y)}{3}$.
  Substitute these into the formula:
  $$f_{X|Y}(x | y) = \frac{\frac{2(x + 2y)}{3}}{\frac{1 + 4y}{3}} = \frac{2(x + 2y)}{?}$$
- **Step 3: Final Calculation.**
  $$f_{X|Y}(x | y) = \frac{2(x + 2y)}{1 + 4y}, \quad 0 < x < 1$$
  *(Note: For any fixed value of $y$, this is a valid 1D PDF for $X$ on $0 < x < 1$).*

---

### Exercise 6: Continuous Independence Check
**Problem:** Determine if $X$ and $Y$ with joint PDF $f(x, y) = 4xy$ for $0 < x < 1, 0 < y < 1$ are independent.

**Solution:**
- **Step 1: Find marginal PDFs.**
  $$f_X(x) = \int_{0}^{1} 4xy \, dy = \left[ 2xy^2 \right]_{0}^{1} = 2x, \quad 0 < x < 1$$
- **Step 2: WIP State.**
  $$f_Y(y) = \int_{0}^{1} 4xy \, dx = \left[ 2x^2y \right]_{0}^{1} = 2y, \quad 0 < y < 1$$
  Check if $f_X(x) \cdot f_Y(y) = f(x, y)$:
  $$f_X(x) \cdot f_Y(y) = 2x \cdot 2y = ?$$
- **Step 3: Final Calculation.**
  $$2x \cdot 2y = 4xy = f(x, y)$$
  Since the product of the marginals equals the joint PDF over the entire domain, $X$ and $Y$ are **independent**.
  *(Exam tip: If the joint PDF can be written as $g(x)h(y)$ and the domain is rectangular, the variables are always independent!).*

---

### Exercise 7: Non-Rectangular Domain (Gotcha Moment)
**Problem:** Let $f(x, y) = 8xy$ on the domain $0 < x < y < 1$. Are $X$ and $Y$ independent?

**Solution:**
- **Step 1: Analyze the domain boundary.**
  The domain is a triangle ($0 < x < y < 1$). The bounds of $x$ depend directly on $y$.
- **Step 2: WIP State.**
  Calculate the marginal of $X$ (integrate over $y$ from $x$ to 1):
  $$f_X(x) = \int_{x}^{1} 8xy \, dy = \left[ 4xy^2 \right]_{x}^{1} = 4x(1 - x^2), \quad 0 < x < 1$$
  Calculate the marginal of $Y$ (integrate over $x$ from 0 to $y$):
  $$f_Y(y) = \int_{0}^{y} 8xy \, dx = \left[ 4x^2y \right]_{0}^{y} = 4y^3, \quad 0 < y < 1$$
  Check product:
  $$f_X(x) \cdot f_Y(y) = 4x(1-x^2) \cdot 4y^3 = 16xy^3(1-x^2) \neq 8xy$$
- **Step 3: Final Calculation.**
  The variables are **dependent**.
  **Gotcha Rule:** If the domain is non-rectangular (e.g., $x < y$), the random variables are **always dependent**, regardless of the PDF formula, because the range of one variable is restricted by the value of the other.

---

### Exercise 8: Joint CDF to PDF
**Problem:** The joint CDF of $X$ and $Y$ is $F(x, y) = (1 - e^{-x})(1 - e^{-2y})$ for $x > 0, y > 0$. Find the joint PDF $f(x, y)$.

**Solution:**
- **Step 1: Set up the partial derivatives.**
  $$f(x, y) = \frac{\partial^2}{\partial x \partial y} F(x, y)$$
- **Step 2: WIP State.**
  Differentiate with respect to $x$ first:
  $$\frac{\partial}{\partial x} F(x, y) = e^{-x} (1 - e^{-2y})$$
  Now, differentiate this result with respect to $y$:
  $$\frac{\partial}{\partial y} \left( e^{-x} (1 - e^{-2y}) \right) = e^{-x} \cdot (2e^{-2y}) = ?$$
- **Step 3: Final Calculation.**
  $$f(x, y) = 2 e^{-x - 2y}, \quad x > 0, y > 0.$$

---

### Exercise 9: Probability on a Region
**Problem:** Let $X$ and $Y$ have joint PDF $f(x, y) = x + y$ on $0 < x < 1, 0 < y < 1$. Find $P(X + Y < 1)$.

**Solution:**
- **Step 1: Set up the bounds for integration.**
  The condition $x + y < 1$ translates to $y < 1 - x$.
  Thus, $x$ ranges from 0 to 1, and for a fixed $x$, $y$ ranges from 0 to $1 - x$.
- **Step 2: WIP State.**
  $$P(X + Y < 1) = \int_{0}^{1} \int_{0}^{1-x} (x + y) \, dy \, dx$$
  Integrate with respect to $y$:
  $$\int_{0}^{1-x} (x + y) \, dy = \left[ xy + \frac{y^2}{2} \right]_{0}^{1-x} = x(1-x) + \frac{(1-x)^2}{2} = x - x^2 + \frac{1 - 2x + x^2}{2} = \frac{1 - x^2}{2}$$
  Now integrate with respect to $x$:
  $$\int_{0}^{1} \frac{1 - x^2}{2} \, dx = \left[ \frac{x}{2} - \frac{x^3}{6} \right]_{0}^{1} = \frac{1}{2} - ?$$
- **Step 3: Final Calculation.**
  $$\text{Fraction} = \frac{1}{6}$$
  $$P(X + Y < 1) = \frac{1}{2} - \frac{1}{6} = \frac{1}{3} \approx 0.3333.$$


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


# Phase 5.8: Distributions of Functions of Multiple Random Variables

This file details the techniques for finding the probability distribution of a new random variable $Z$ which is defined as a function of multiple random variables, $Z = g(X, Y)$.

---

## 1. The CDF Method (First Principles)

Like the single-variable case, the CDF method is highly reliable and works by finding the region of the joint PDF that satisfies the inequality $g(X, Y) \le z$.

$$F_Z(z) = P(g(X, Y) \le z) = \iint_{g(x,y) \le z} f(x, y) \, dx \, dy$$

Once $F_Z(z)$ is found, the PDF is obtained by differentiating: $f_Z(z) = F'_Z(z)$.

---

## 2. Convolution (Sum of Independent Variables)

If $X$ and $Y$ are independent, the distribution of their sum $Z = X + Y$ is called the **convolution** of their individual distributions.

*   **Discrete Case:**
    $$p_Z(z) = P(X + Y = z) = \sum_{x} p_X(x) \cdot p_Y(z - x)$$
*   **Continuous Case:**
    $$f_Z(z) = \int_{-\infty}^{\infty} f_X(x) \cdot f_Y(z - x) \, dx$$

---

## 3. The bivariate Change of Variables (Jacobian Method)

If we have two random variables $X_1, X_2$ with joint PDF $f_{X_1, X_2}(x_1, x_2)$, and we define two new variables:
$$Y_1 = g_1(X_1, X_2) \quad \text{and} \quad Y_2 = g_2(X_1, X_2)$$

If this transformation is a one-to-one (bijective) mapping, we can solve for $X_1$ and $X_2$ in terms of $Y_1, Y_2$:
$$X_1 = h_1(Y_1, Y_2) \quad \text{and} \quad X_2 = h_2(Y_1, Y_2)$$

The joint PDF of $Y_1$ and $Y_2$ is:
$$f_{Y_1, Y_2}(y_1, y_2) = f_{X_1, X_2}(h_1(y_1, y_2), h_2(y_1, y_2)) \cdot |J|$$

where $J$ is the Jacobian determinant of the inverse transformation:
$$J = \det \begin{pmatrix} \frac{\partial x_1}{\partial y_1} & \frac{\partial x_1}{\partial y_2} \\ \frac{\partial x_2}{\partial y_1} & \frac{\partial x_2}{\partial y_2} \end{pmatrix} = \frac{\partial x_1}{\partial y_1} \frac{\partial x_2}{\partial y_2} - \frac{\partial x_1}{\partial y_2} \frac{\partial x_2}{\partial y_1}$$

> **Exam Shortcut:** If you only want the distribution of a single function $Y_1 = g_1(X_1, X_2)$, you can define a dummy variable (e.g., $Y_2 = X_1$ or $Y_2 = X_2$), apply the 2D Jacobian method to find $f_{Y_1, Y_2}(y_1, y_2)$, and then integrate out $Y_2$ to find the marginal PDF $f_{Y_1}(y_1)$.

---

## 4. Order Statistics: Min and Max of Independent Variables

Let $X_1, X_2, \dots, X_n$ be independent, identically distributed (i.i.d.) random variables with CDF $F_X(x)$ and PDF $f_X(x)$.

### 4.1 Distribution of the Maximum ($Y_{max} = \max(X_1, \dots, X_n)$)
For the maximum to be less than $y$, **all** individual variables must be less than $y$:
$$F_{Y_{max}}(y) = P(X_1 \le y, \dots, X_n \le y) = [F_X(y)]^n$$
Differentiating gives the PDF:
$$f_{Y_{max}}(y) = n \cdot [F_X(y)]^{n-1} \cdot f_X(y)$$

### 4.2 Distribution of the Minimum ($Y_{min} = \min(X_1, \dots, X_n)$)
For the minimum to be greater than $y$, **all** individual variables must be greater than $y$:
$$P(Y_{min} > y) = P(X_1 > y, \dots, X_n > y) = [1 - F_X(y)]^n$$
$$F_{Y_{min}}(y) = 1 - [1 - F_X(y)]^n$$
Differentiating gives the PDF:
$$f_{Y_{min}}(y) = n \cdot [1 - F_X(y)]^{n-1} \cdot f_X(y)$$

---

## 5. Solved Exercises (9 Examples)

### Exercise 1: Sum of Two Independent Uniform Variables (Convolution)
**Problem:** Let $X \sim U(0, 1)$ and $Y \sim U(0, 1)$ be independent. Find the PDF of $Z = X + Y$.

**Solution:**
- **Step 1: Set up the convolution integral.**
  The PDFs are $f_X(x) = 1$ for $0 < x < 1$ and $f_Y(y) = 1$ for $0 < y < 1$.
  $$f_Z(z) = \int_{-\infty}^{\infty} f_X(x) f_Y(z-x) \, dx = \int_{0}^{1} 1 \cdot f_Y(z-x) \, dx$$
- **Step 2: WIP State.**
  The term $f_Y(z-x)$ is 1 only when $0 < z - x < 1 \implies z - 1 < x < z$.
  We split the analysis into two cases based on the value of $z \in (0, 2)$:
  - **Case 1: $0 < z \le 1$.**
    Here, the overlap region is $0 < x < z$.
    $$f_Z(z) = \int_{0}^{z} 1 \, dx = z$$
  - **Case 2: $1 < z < 2$.**
    Here, the overlap region is $z - 1 < x < 1$.
    $$f_Z(z) = \int_{z-1}^{1} 1 \, dx = 1 - (z-1) = ?$$
- **Step 3: Final Calculation.**
  - Case 2 value $= 2 - z$.
  - This results in a triangular PDF:
    $$f_Z(z) = \begin{cases} z, & 0 < z \le 1 \\ 2 - z, & 1 < z < 2 \\ 0, & \text{otherwise} \end{cases}$$

---

### Exercise 2: Ratio of Two Independent Exponentials (CDF Method)
**Problem:** Let $X \sim Exp(1)$ and $Y \sim Exp(1)$ be independent. Find the PDF of $Z = \frac{Y}{X}$.

**Solution:**
- **Step 1: Write down the CDF of $Z$ for $z > 0$.**
  $$F_Z(z) = P\left(\frac{Y}{X} \le z\right) = P(Y \le zX)$$
- **Step 2: WIP State.**
  Integrate over the region $y \le zx$ in the first quadrant:
  $$F_Z(z) = \int_{0}^{\infty} \int_{0}^{zx} e^{-x} e^{-y} \, dy \, dx = \int_{0}^{\infty} e^{-x} \left( 1 - e^{-zx} \right) \, dx$$
  $$F_Z(z) = \int_{0}^{\infty} \left( e^{-x} - e^{-(1+z)x} \right) \, dx = 1 - \frac{1}{?}$$
- **Step 3: Final Calculation.**
  - Integral of $e^{-(1+z)x}$ is $\frac{1}{1+z}$.
  - $F_Z(z) = 1 - \frac{1}{1+z} = \frac{z}{1+z}$.
  Differentiating with respect to $z$:
  $$f_Z(z) = \frac{d}{dz}\left(1 - (1+z)^{-1}\right) = (1+z)^{-2} = \frac{1}{(1+z)^2}, \quad z > 0.$$

---

### Exercise 3: Dummy Variable and 2D Jacobian Method
**Problem:** Let $X_1, X_2$ be independent random variables with joint PDF $f(x_1, x_2) = e^{-x_1 - x_2}$ for $x_1 > 0, x_2 > 0$. Find the joint PDF of $Y_1 = X_1 + X_2$ and $Y_2 = \frac{X_1}{X_2}$.

**Solution:**
- **Step 1: Solve for the inverse transformation.**
  We have:
  - $y_1 = x_1 + x_2$
  - $y_2 = \frac{x_1}{x_2} \implies x_1 = y_2 x_2$
  Substitute $x_1$ into $y_1$:
  $y_1 = y_2 x_2 + x_2 = x_2(1 + y_2) \implies x_2 = \frac{y_1}{1 + y_2}$.
  Then:
  $x_1 = \frac{y_1 y_2}{1 + y_2}$.
- **Step 2: WIP State for the Jacobian.**
  Compute partial derivatives:
  - $\frac{\partial x_1}{\partial y_1} = \frac{y_2}{1+y_2}$, $\frac{\partial x_1}{\partial y_2} = \frac{y_1(1+y_2) - y_1 y_2}{(1+y_2)^2} = \frac{y_1}{(1+y_2)^2}$
  - $\frac{\partial x_2}{\partial y_1} = \frac{1}{1+y_2}$, $\frac{\partial x_2}{\partial y_2} = -\frac{y_1}{(1+y_2)^2}$
  Determinant:
  $$J = \det \begin{pmatrix} \frac{y_2}{1+y_2} & \frac{y_1}{(1+y_2)^2} \\ \frac{1}{1+y_2} & -\frac{y_1}{(1+y_2)^2} \end{pmatrix} = \left(\frac{y_2}{1+y_2}\right)\left(-\frac{y_1}{(1+y_2)^2}\right) - \left(\frac{y_1}{(1+y_2)^2}\right)\left(\frac{1}{1+y_2}\right)$$
  $$J = \frac{-y_1 y_2 - y_1}{(1+y_2)^3} = \frac{-y_1(y_2 + 1)}{(1+y_2)^3} = -\frac{y_1}{?}$$
- **Step 3: Final Calculation.**
  - Denominator $= (1 + y_2)^2$.
  - $|J| = \frac{y_1}{(1+y_2)^2}$.
  Apply the transformation formula:
  $$f_{Y_1, Y_2}(y_1, y_2) = e^{-(x_1 + x_2)} \cdot |J| = e^{-y_1} \cdot \frac{y_1}{(1 + y_2)^2}, \quad y_1 > 0, y_2 > 0.$$

---

### Exercise 4: Marginal PDF from Joint Jacobian Result
**Problem:** Using the joint PDF of $Y_1, Y_2$ found in Exercise 3, find the marginal PDF of $Y_1$ and $Y_2$ to show they are independent.

**Solution:**
- **Step 1: Integrate out $y_2$ to find the marginal of $Y_1$.**
  $$f_{Y_1}(y_1) = \int_{0}^{\infty} y_1 e^{-y_1} \frac{1}{(1 + y_2)^2} \, dy_2 = y_1 e^{-y_1} \left[ -\frac{1}{1 + y_2} \right]_{0}^{\infty} = y_1 e^{-y_1}, \quad y_1 > 0$$
- **Step 2: WIP State.**
  Integrate out $y_1$ to find the marginal of $Y_2$:
  $$f_{Y_2}(y_2) = \int_{0}^{\infty} \frac{1}{(1 + y_2)^2} y_1 e^{-y_1} \, dy_1 = \frac{1}{(1 + y_2)^2} \int_{0}^{\infty} y_1 e^{-y_1} \, dy_1$$
  Notice that $\int_{0}^{\infty} y_1 e^{-y_1} \, dy_1$ is $\Gamma(2) = 1! = 1$.
  So $f_{Y_2}(y_2) = \frac{1}{(1 + y_2)^2}$ for $y_2 > 0$.
  Check product:
  $$f_{Y_1}(y_1) f_{Y_2}(y_2) = y_1 e^{-y_1} \cdot \frac{1}{(1+y_2)^2} = ?$$
- **Step 3: Final Calculation.**
  - Product $= f_{Y_1, Y_2}(y_1, y_2)$.
  Thus, $Y_1$ and $Y_2$ are independent random variables.

---

### Exercise 5: Minimum of Independent Exponentials
**Problem:** Let $X_1, X_2, \dots, X_n$ be i.i.d. random variables with $X_i \sim Exp(\lambda)$. Find the distribution of $W = \min(X_1, \dots, X_n)$.

**Solution:**
- **Step 1: Recall the continuous minimum CDF formula.**
  $$F_W(w) = 1 - [1 - F_X(w)]^n$$
- **Step 2: WIP State.**
  For $X_i \sim Exp(\lambda)$, the CDF is $F_X(w) = 1 - e^{-\lambda w}$.
  Substitute this into the formula:
  $$F_W(w) = 1 - \left[1 - \left(1 - e^{-\lambda w}\right)\right]^n = 1 - \left[e^{-\lambda w}\right]^n = 1 - e^{-?}$$
- **Step 3: Final Calculation.**
  - Exponent $= n\lambda w$.
  - $F_W(w) = 1 - e^{-n\lambda w}$.
  This is the CDF of an Exponential distribution with rate parameter $n\lambda$.
  Thus, $\min(X_1, \dots, X_n) \sim Exp(n\lambda)$.
  *(Exam shortcut: The minimum of $n$ independent Exponentials is always Exponential, and its rate is simply the sum of the individual rates!).*

---

### Exercise 6: Maximum of Independent Uniforms
**Problem:** Let $X_1, X_2, \dots, X_n$ be i.i.d. $U(0, 1)$ random variables. Find the PDF of $Y = \max(X_1, \dots, X_n)$.

**Solution:**
- **Step 1: Write down the CDF of $U(0, 1)$.**
  $F_X(x) = x$ for $0 < x < 1$.
- **Step 2: WIP State.**
  Apply maximum CDF formula:
  $$F_Y(y) = [F_X(y)]^n = y^n, \quad 0 < y < 1$$
  Differentiate to obtain PDF:
  $$f_Y(y) = \frac{d}{dy}\left(y^n\right) = ?$$
- **Step 3: Final Calculation.**
  $$f_Y(y) = n y^{n-1}, \quad 0 < y < 1.$$

---

### Exercise 7: Distribution of a Product (Continuous)
**Problem:** Let $X$ and $Y$ be independent random variables, both distributed as $U(0, 1)$. Find the PDF of their product $Z = XY$.

**Solution:**
- **Step 1: Set up the CDF equation for $0 < z < 1$.**
  $$F_Z(z) = P(XY \le z) = \iint_{xy \le z} 1 \, dx \, dy$$
- **Step 2: WIP State.**
  Split the unit square region:
  - If $x \le z$, then $y$ can take any value in $[0, 1]$.
  - If $x > z$, then $y$ must be $\le z/x$.
  $$F_Z(z) = \int_{0}^{z} \left( \int_{0}^{1} 1 \, dy \right) \, dx + \int_{z}^{1} \left( \int_{0}^{z/x} 1 \, dy \right) \, dx$$
  $$F_Z(z) = \int_{0}^{z} 1 \, dx + \int_{z}^{1} \frac{z}{x} \, dx = z + z \left[ \ln(x) \right]_{z}^{1} = z + z(0 - \ln(z)) = z - z\ln(z)$$
  Now, differentiate with respect to $z$:
  $$f_Z(z) = \frac{d}{dz}\left(z - z\ln(z)\right) = 1 - \left( 1 \cdot \ln(z) + z \cdot \frac{1}{z} \right) = ?$$
- **Step 3: Final Calculation.**
  $$f_Z(z) = 1 - \ln(z) - 1 = -\ln(z), \quad 0 < z < 1.$$

---

### Exercise 8: Sum of Independent Normal Variables (MGF Method)
**Problem:** Let $X \sim N(\mu_1, \sigma_1^2)$ and $Y \sim N(\mu_2, \sigma_2^2)$ be independent. Prove that $W = X + Y \sim N(\mu_1 + \mu_2, \sigma_1^2 + \sigma_2^2)$ using MGFs.

**Solution:**
- **Step 1: Set up MGF product.**
  $$M_W(t) = M_X(t) \cdot M_Y(t)$$
- **Step 2: WIP State.**
  $$M_X(t) = e^{\mu_1 t + \frac{1}{2}\sigma_1^2 t^2}, \quad M_Y(t) = e^{\mu_2 t + \frac{1}{2}\sigma_2^2 t^2}$$
  $$M_W(t) = e^{\mu_1 t + \frac{1}{2}\sigma_1^2 t^2} \cdot e^{\mu_2 t + \frac{1}{2}\sigma_2^2 t^2} = e^{?}$$
- **Step 3: Final Calculation.**
  $$M_W(t) = e^{(\mu_1 + \mu_2)t + \frac{1}{2}(\sigma_1^2 + \sigma_2^2)t^2}$$
  By uniqueness of the MGF, this represents a Normal distribution:
  $$W \sim N(\mu_1 + \mu_2, \sigma_1^2 + \sigma_2^2).$$

---

### Exercise 9: Box-Muller Transform (Advanced Jacobian)
**Problem:** Let $U_1, U_2$ be independent $U(0, 1)$ variables. Define:
$$Z_0 = \sqrt{-2\ln U_1} \cos(2\pi U_2) \quad \text{and} \quad Z_1 = \sqrt{-2\ln U_1} \sin(2\pi U_2)$$
Find the joint PDF of $Z_0$ and $Z_1$.

**Solution:**
- **Step 1: Solve for $U_1, U_2$.**
  Squaring and adding:
  $$Z_0^2 + Z_1^2 = -2\ln U_1 \implies U_1 = e^{-\frac{Z_0^2 + Z_1^2}{2}}$$
  Dividing:
  $$\frac{Z_1}{Z_0} = \tan(2\pi U_2) \implies U_2 = \frac{1}{2\pi} \arctan\left(\frac{Z_1}{Z_0}\right)$$
- **Step 2: WIP State for the Jacobian.**
  Compute the Jacobian $J$ of the transformation from $(Z_0, Z_1)$ to $(U_1, U_2)$:
  $$J = \det \begin{pmatrix} \frac{\partial u_1}{\partial z_0} & \frac{\partial u_1}{\partial z_1} \\ \frac{\partial u_2}{\partial z_0} & \frac{\partial u_2}{\partial z_1} \end{pmatrix}$$
  After differentiation and simplification:
  $$|J| = \frac{1}{2\pi} e^{-\frac{z_0^2 + z_1^2}{2}}$$
  Since $U_1, U_2$ are independent $U(0, 1)$, their joint PDF is $f(u_1, u_2) = 1$.
  Apply transformation:
  $$f_{Z_0, Z_1}(z_0, z_1) = 1 \cdot |J| = ?$$
- **Step 3: Final Calculation.**
  $$f_{Z_0, Z_1}(z_0, z_1) = \left( \frac{1}{\sqrt{2\pi}} e^{-z_0^2/2} \right) \cdot \left( \frac{1}{\sqrt{2\pi}} e^{-z_1^2/2} \right)$$
  This factors into the product of two standard normal PDFs, proving that $Z_0$ and $Z_1$ are independent standard normal variables!
