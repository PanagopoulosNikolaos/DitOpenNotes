# Phase 5.5: Transformations of Random Variables

In probability theory, we often need to find the probability distribution of a new random variable $Y$ that is a function of an existing random variable $X$, written as $Y = g(X)$. This process is called a **transformation**.

---

## 1. Discrete Random Variables

For a discrete random variable $X$ with probability mass function $p_X(x)$, the PMF of $Y = g(X)$ is obtained by summing the probabilities of all $x$ values that map to $y$:

$$p_Y(y) = P(Y = y) = \sum_{x : g(x) = y} p_X(x)$$

---

## 2. Continuous Random Variables

There are two primary methods for finding the PDF of $Y = g(X)$ when $X$ is continuous.

### 2.1 The CDF Method (First Principles)
This is the most robust method and works for both monotonic and non-monotonic functions (like $Y = X^2$).

1.  Write the cumulative distribution function (CDF) of $Y$:
    $$F_Y(y) = P(Y \le y) = P(g(X) \le y)$$
2.  Rewrite the inequality in terms of $X$.
3.  Express $F_Y(y)$ in terms of the CDF of $X$, $F_X(x)$.
4.  Differentiate $F_Y(y)$ with respect to $y$ to get the PDF $f_Y(y)$:
    $$f_Y(y) = \frac{d}{dy} F_Y(y)$$

### 2.2 The Change of Variables Formula (Jacobian Method)
If $g(x)$ is **strictly monotonic** (either strictly increasing or strictly decreasing) and differentiable, the PDF of $Y$ can be computed directly using:

$$f_Y(y) = f_X(x) \cdot \left| \frac{dx}{dy} \right| \quad \text{where } x = g^{-1}(y)$$

Or written equivalently as:

$$f_Y(y) = f_X(g^{-1}(y)) \cdot \left| \frac{d}{dy} g^{-1}(y) \right|$$

> **Exam Warning:** Always specify the **domain (range of validity)** of the new PDF $f_Y(y)$ by mapping the original boundaries of $X$ through the function $g(x)$. Leaving out the domain is a guaranteed way to lose marks.

---

## 3. Solved Exercises (9 Examples)

### Exercise 1: Discrete Transformation
**Problem:** Let $X$ have PMF:
*   $P(X = -1) = 0.2$
*   $P(X = 0) = 0.3$
*   $P(X = 1) = 0.4$
*   $P(X = 2) = 0.1$

Find the PMF of $Y = X^2$.

**Solution:**
- **Step 1: Map the values of $X$ to $Y$.**
  - If $x = -1 \implies y = (-1)^2 = 1$
  - If $x = 0 \implies y = 0^2 = 0$
  - If $x = 1 \implies y = 1^2 = 1$
  - If $x = 2 \implies y = 2^2 = 4$
  The possible values for $Y$ are $\{0, 1, 4\}$.
- **Step 2: WIP State.**
  Sum probabilities for each unique $y$:
  - $P(Y = 0) = P(X = 0) = 0.3$
  - $P(Y = 1) = P(X = -1) + P(X = 1) = 0.2 + 0.4 = 0.6$
  - $P(Y = 4) = P(X = ?) = ?$
- **Step 3: Final Calculation.**
  - $P(Y = 4) = P(X = 2) = 0.1$.
  - PMF Table:
    | $y$ | 0 | 1 | 4 |
    | :--- | :--- | :--- | :--- |
    | $P(Y = y)$ | 0.3 | 0.6 | 0.1 |
  Check sum: $0.3 + 0.6 + 0.1 = 1.0$.

---

### Exercise 2: Monotonic Linear Transformation (Continuous)
**Problem:** Let $X$ be a continuous random variable with PDF $f_X(x) = 2x$ for $0 < x < 1$. Find the PDF of $Y = 3X + 2$.

**Solution:**
- **Step 1: Find the inverse function and its derivative.**
  Let $y = 3x + 2 \implies x = \frac{y - 2}{3}$.
  $$\frac{dx}{dy} = \frac{1}{3}$$
- **Step 2: WIP State.**
  Find the new domain for $Y$:
  - When $x = 0 \implies y = 3(0) + 2 = 2$.
  - When $x = 1 \implies y = 3(1) + 2 = 5$.
  So the domain of $Y$ is $2 < y < 5$.
  Apply the Change of Variables formula:
  $$f_Y(y) = f_X(x) \cdot \left| \frac{dx}{dy} \right| = 2 \cdot \left(\frac{y-2}{3}\right) \cdot ?$$
- **Step 3: Final Calculation.**
  $$f_Y(y) = 2 \cdot \left(\frac{y - 2}{3}\right) \cdot \frac{1}{3} = \frac{2(y - 2)}{9}$$
  So, the final PDF is:
  $$f_Y(y) = \frac{2(y - 2)}{9}, \quad 2 < y < 5$$

---

### Exercise 3: Non-Monotonic Transformation ($Y = X^2$)
**Problem:** Let $X \sim U(-1, 2)$. Find the PDF of $Y = X^2$.

**Solution:**
- **Step 1: Write original PDF and find domain.**
  $$f_X(x) = \frac{1}{2 - (-1)} = \frac{1}{3}, \quad -1 < x < 2$$
  Since $Y = X^2$, the range of $Y$ is $[0, 4]$.
- **Step 2: WIP State (Apply CDF method).**
  For $0 < y < 1$, the values of $X$ that satisfy $X^2 \le y$ are $-\sqrt{y} \le X \le \sqrt{y}$.
  $$F_Y(y) = P(X^2 \le y) = P(-\sqrt{y} \le X \le \sqrt{y}) = F_X(\sqrt{y}) - F_X(-\sqrt{y})$$
  Differentiating:
  $$f_Y(y) = \frac{d}{dy}\left(F_X(\sqrt{y}) - F_X(-\sqrt{y})\right) = f_X(\sqrt{y}) \cdot \frac{1}{2\sqrt{y}} - f_X(-\sqrt{y}) \cdot \left(-\frac{1}{2\sqrt{y}}\right)$$
  $$f_Y(y) = \frac{1}{2\sqrt{y}} \left( f_X(\sqrt{y}) + f_X(-\sqrt{y}) \right)$$
  For $1 \le y < 4$, $X$ can only be positive because the lower boundary of $X$ is $-1$ (which squares to $1$). Thus, $X^2 \le y$ implies $-1 < X \le \sqrt{y}$.
  $$F_Y(y) = P(-1 < X \le \sqrt{y}) = F_X(\sqrt{y}) - F_X(-1)$$
  Differentiating:
  $$f_Y(y) = f_X(\sqrt{y}) \cdot \frac{1}{2\sqrt{y}} = \frac{1}{3} \cdot \frac{1}{2\sqrt{y}} = ?$$
- **Step 3: Final Calculation.**
  - For $0 < y < 1$: Both $\sqrt{y}$ and $-\sqrt{y}$ lie in the domain of $X$ ($-1 < x < 2$).
    $$f_Y(y) = \frac{1}{2\sqrt{y}} \left( \frac{1}{3} + \frac{1}{3} \right) = \frac{1}{3\sqrt{y}}$$
  - For $1 \le y < 4$: Only $\sqrt{y}$ lies in the domain of $X$.
    $$f_Y(y) = \frac{1}{6\sqrt{y}}$$
  Final piecewise PDF:
  $$f_Y(y) = \begin{cases} \frac{1}{3\sqrt{y}}, & 0 < y < 1 \\ \frac{1}{6\sqrt{y}}, & 1 \le y < 4 \\ 0, & \text{otherwise} \end{cases}$$

---

### Exercise 4: Exponential from Uniform
**Problem:** Let $X \sim U(0, 1)$. Find the PDF of $Y = -\ln(X)$.

**Solution:**
- **Step 1: Inverse function and derivative.**
  Let $y = -\ln(x) \implies -y = \ln(x) \implies x = e^{-y}$.
  $$\frac{dx}{dy} = -e^{-y} \implies \left| \frac{dx}{dy} \right| = e^{-y}$$
- **Step 2: WIP State.**
  Domain mapping:
  - As $x \to 0^+ \implies y \to \infty$.
  - As $x \to 1^- \implies y \to 0$.
  So the domain of $Y$ is $y > 0$.
  Apply formula:
  $$f_Y(y) = f_X(x) \cdot \left| \frac{dx}{dy} \right|$$
  Since $X \sim U(0, 1)$, $f_X(x) = 1$ on $(0, 1)$.
  $$f_Y(y) = 1 \cdot e^{-y} = ?$$
- **Step 3: Final Calculation.**
  $$f_Y(y) = e^{-y}, \quad y > 0$$
  *(Note: This is exactly the PDF of an Exponential distribution with parameter $\lambda = 1$. This is the basis of the Inverse Transform Method for generating random variables!)*

---

### Exercise 5: Transformation of a Normal Variable to Log-Normal
**Problem:** Let $X \sim N(\mu, \sigma^2)$. Find the PDF of $Y = e^X$.

**Solution:**
- **Step 1: Inverse and derivative.**
  Let $y = e^x \implies x = \ln(y)$ (for $y > 0$).
  $$\frac{dx}{dy} = \frac{1}{y}$$
- **Step 2: WIP State.**
  Domain: Since $x \in (-\infty, \infty)$, $y = e^x \in (0, \infty)$.
  Recall the Normal PDF:
  $$f_X(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x - \mu)^2}{2\sigma^2}}$$
  Apply Change of Variables formula:
  $$f_Y(y) = f_X(\ln(y)) \cdot \left| \frac{dx}{dy} \right| = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(\ln(y) - \mu)^2}{2\sigma^2}} \cdot ?$$
- **Step 3: Final Calculation.**
  $$f_Y(y) = \frac{1}{y \sigma \sqrt{2\pi}} e^{-\frac{(\ln(y) - \mu)^2}{2\sigma^2}}, \quad y > 0$$
  This is the PDF of the **Log-Normal distribution**.

---

### Exercise 6: CDF Method for a Square Root Function
**Problem:** Let $X \sim Exp(\lambda)$. Find the PDF of $Y = \sqrt{X}$.

**Solution:**
- **Step 1: Use the CDF method.**
  For $y > 0$:
  $$F_Y(y) = P(Y \le y) = P(\sqrt{X} \le y) = P(X \le y^2) = F_X(y^2)$$
- **Step 2: WIP State.**
  Since $X \sim Exp(\lambda)$, its CDF is $F_X(x) = 1 - e^{-\lambda x}$ for $x > 0$.
  $$F_Y(y) = 1 - e^{-\lambda y^2}$$
  Differentiate with respect to $y$ using the chain rule:
  $$f_Y(y) = \frac{d}{dy}\left(1 - e^{-\lambda y^2}\right) = -e^{-\lambda y^2} \cdot (-2\lambda y) = ?$$
- **Step 3: Final Calculation.**
  $$f_Y(y) = 2\lambda y e^{-\lambda y^2}, \quad y > 0$$
  *(Note: This is the Weibull distribution with shape parameter 2).*

---

### Exercise 7: Monotonic Decreasing Transformation
**Problem:** Let $X$ have PDF $f_X(x) = 3x^2$ for $0 < x < 1$. Find the PDF of $Y = \frac{1}{X}$.

**Solution:**
- **Step 1: Find inverse and derivative.**
  Let $y = 1/x \implies x = 1/y$.
  $$\frac{dx}{dy} = -\frac{1}{y^2} \implies \left| \frac{dx}{dy} \right| = \frac{1}{y^2}$$
- **Step 2: WIP State.**
  Domain mapping:
  - When $x = 0^+ \implies y \to \infty$.
  - When $x = 1 \implies y = 1$.
  So the domain of $Y$ is $y > 1$.
  Apply formula:
  $$f_Y(y) = f_X\left(\frac{1}{y}\right) \cdot \left| \frac{dx}{dy} \right| = 3\left(\frac{1}{y}\right)^2 \cdot ?$$
- **Step 3: Final Calculation.**
  $$f_Y(y) = \frac{3}{y^2} \cdot \frac{1}{y^2} = \frac{3}{y^4}, \quad y > 1$$

---

### Exercise 8: The Linear Scaling Gotcha
**Problem:** Let $X$ follow a distribution with PDF $f_X(x)$. If $Y = aX$, write the PDF $f_Y(y)$ using $f_X$.

**Solution:**
- **Step 1: Find inverse and derivative.**
  Let $y = ax \implies x = y/a$.
  $$\frac{dx}{dy} = \frac{1}{a} \implies \left| \frac{dx}{dy} \right| = \frac{1}{|a|}$$
- **Step 2: WIP State.**
  Apply formula:
  $$f_Y(y) = f_X\left(\frac{y}{a}\right) \cdot ?$$
- **Step 3: Final Calculation.**
  $$f_Y(y) = \frac{1}{|a|} f_X\left(\frac{y}{a}\right)$$
  *(Gotcha check: Students frequently write $f_Y(y) = f_X(y/a)$ and forget the division by $|a|$. This constant factor is mathematically required so that the PDF integrates to 1).*

---

### Exercise 9: Cauchy from Uniform (The tangent transformation)
**Problem:** Let $X \sim U\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$. Find the PDF of $Y = \tan(X)$.

**Solution:**
- **Step 1: Inverse function and derivative.**
  Let $y = \tan(x) \implies x = \arctan(y)$.
  $$\frac{dx}{dy} = \frac{1}{1 + y^2}$$
- **Step 2: WIP State.**
  Domain mapping:
  - When $x \to -\frac{\pi}{2}^+ \implies y \to -\infty$.
  - When $x \to \frac{\pi}{2}^- \implies y \to \infty$.
  So the domain of $Y$ is $-\infty < y < \infty$.
  The PDF of $X$ is $f_X(x) = \frac{1}{\frac{\pi}{2} - (-\frac{\pi}{2})} = \frac{1}{\pi}$ on its interval.
  Apply formula:
  $$f_Y(y) = f_X(\arctan(y)) \cdot \left| \frac{dx}{dy} \right| = \frac{1}{\pi} \cdot ?$$
- **Step 3: Final Calculation.**
  $$f_Y(y) = \frac{1}{\pi(1 + y^2)}, \quad -\infty < y < \infty$$
  This is the PDF of the standard **Cauchy distribution**.
