# Phase 5.4: Gamma Distribution

The Gamma Distribution is a continuous probability distribution that generalizes the Exponential distribution. It is widely used to model wait times for multiple independent events to occur.

---

## 1. The Gamma Function ($\Gamma(\alpha)$)

Before defining the Gamma distribution, we must define the **Gamma Function**, which acts as a continuous generalization of the factorial function:

$$\Gamma(\alpha) = \int_{0}^{\infty} y^{\alpha-1} e^{-y} \, dy \quad \text{for } \alpha > 0$$

### Key Properties of the Gamma Function
1.  **Recursive Relation:** $\Gamma(\alpha + 1) = \alpha \cdot \Gamma(\alpha)$
2.  **Factorial Relation:** For any positive integer $n$:
    $$\Gamma(n) = (n-1)!$$
3.  **Special Value:** $\Gamma\left(\frac{1}{2}\right) = \sqrt{\pi}$
4.  **Base Case:** $\Gamma(1) = 0! = 1$

---

## 2. The Gamma Distribution

There are two common parameterisations of the Gamma distribution. Confusing them in an exam is a common mistake.

### 2.1 Rate Parameterisation (Standard in most syllabus structures)
If $X \sim Gamma(\alpha, \beta)$, where $\alpha > 0$ is the **shape parameter** and $\beta > 0$ is the **rate parameter**:

*   **PDF:**
    $$f(x) = \frac{\beta^\alpha}{\Gamma(\alpha)} x^{\alpha-1} e^{-\beta x}, \quad x > 0$$
*   **Mean:** $E[X] = \frac{\alpha}{\beta}$
*   **Variance:** $Var(X) = \frac{\alpha}{\beta^2}$
*   **MGF:** $M_X(t) = \left(1 - \frac{t}{\beta}\right)^{-\alpha} \quad (\text{for } t < \beta)$

### 2.2 Scale Parameterisation (Alternative)
Using the **scale parameter** $\theta = \frac{1}{\beta}$:
*   **PDF:** $f(x) = \frac{1}{\Gamma(\alpha)\theta^\alpha} x^{\alpha-1} e^{-x/\theta}$
*   **Mean:** $E[X] = \alpha\theta$
*   **Variance:** $Var(X) = \alpha\theta^2$

---

## 3. Relationships to Other Distributions

1.  **Exponential Distribution:** A Gamma distribution with shape $\alpha = 1$ is exactly the Exponential distribution:
    $$Gamma(1, \beta) \equiv Exp(\beta)$$
2.  **Sum of Independent Exponentials:** If $X_1, X_2, \dots, X_n$ are independent, identically distributed random variables with $X_i \sim Exp(\beta)$, then their sum follows a Gamma distribution (sometimes called the Erlang distribution):
    $$\sum_{i=1}^{n} X_i \sim Gamma(n, \beta)$$
3.  **Chi-Square Distribution:** The Chi-square distribution with $\nu$ degrees of freedom is a special case of the Gamma distribution:
    $$\chi^2_\nu \equiv Gamma\left(\frac{\nu}{2}, \frac{1}{2}\right)$$

---

## 4. Solved Exercises (9 Examples)

### Exercise 1: Evaluating the Gamma Function
**Problem:** Calculate the exact value of $\Gamma\left(\frac{5}{2}\right)$.

**Solution:**
- **Step 1: Apply the recursive formula $\Gamma(\alpha + 1) = \alpha \Gamma(\alpha)$.**
  $$\Gamma\left(\frac{5}{2}\right) = \Gamma\left(\frac{3}{2} + 1\right) = \frac{3}{2} \cdot \Gamma\left(\frac{3}{2}\right)$$
- **Step 2: WIP State.**
  Apply the recursive formula again:
  $$\Gamma\left(\frac{3}{2}\right) = \Gamma\left(\frac{1}{2} + 1\right) = \frac{1}{2} \cdot \Gamma\left(\frac{1}{2}\right)$$
  Recall that $\Gamma\left(\frac{1}{2}\right) = \sqrt{\pi}$.
  So, $\Gamma\left(\frac{5}{2}\right) = \frac{3}{2} \cdot \left(\frac{1}{2} \cdot ?\right)$
- **Step 3: Final Calculation.**
  $$\Gamma\left(\frac{5}{2}\right) = \frac{3}{2} \cdot \frac{1}{2} \cdot \sqrt{\pi} = \frac{3}{4}\sqrt{\pi}.$$

---

### Exercise 2: Identifying Shape and Rate
**Problem:** A wait time $X$ has PDF $f(x) = 4 x e^{-2x}$ for $x > 0$. Identify the distribution and calculate its mean and variance.

**Solution:**
- **Step 1: Match the PDF structure with the Gamma PDF.**
  $$f(x) = \frac{\beta^\alpha}{\Gamma(\alpha)} x^{\alpha-1} e^{-\beta x}$$
  Looking at $e^{-2x}$, we get $\beta = 2$.
  Looking at $x = x^1$, we get $\alpha - 1 = 1 \implies \alpha = 2$.
- **Step 2: WIP State.**
  Verify the constant coefficient:
  $$\frac{\beta^\alpha}{\Gamma(\alpha)} = \frac{2^2}{\Gamma(2)} = \frac{4}{1!} = 4$$
  This matches the coefficient in the problem.
  Therefore, $X \sim Gamma(\alpha = 2, \beta = 2)$.
  Mean: $E[X] = \frac{\alpha}{\beta} = \frac{2}{2} = 1$.
  Variance: $Var(X) = \frac{\alpha}{\beta^2} = \frac{2}{?}$
- **Step 3: Final Calculation.**
  $$Var(X) = \frac{2}{4} = 0.5.$$

---

### Exercise 3: Sum of Wait Times
**Problem:** The time (in hours) to repair a server is exponentially distributed with a mean of 0.5 hours. If a technician has 4 independent server repairs scheduled, find the probability distribution of the total repair time $Y$. What is the expected total repair time and its variance?

**Solution:**
- **Step 1: Identify individual parameters.**
  Each repair $X_i \sim Exp(\lambda)$.
  Since the mean is $0.5$, $\frac{1}{\lambda} = 0.5 \implies \lambda = 2$.
- **Step 2: WIP State.**
  Since $Y = \sum_{i=1}^{4} X_i$ is a sum of $n=4$ independent exponential variables, it follows a Gamma distribution:
  $$Y \sim Gamma(\alpha = 4, \beta = 2)$$
  Expected total repair time: $E[Y] = \frac{\alpha}{\beta} = \frac{4}{2} = 2$ hours.
  Variance: $Var(Y) = \frac{4}{?}$
- **Step 3: Final Calculation.**
  $$Var(Y) = \frac{4}{2^2} = \frac{4}{4} = 1.$$

---

### Exercise 4: Integrating a Gamma PDF to Find Constants
**Problem:** Find the value of the constant $c$ such that $f(x) = c x^2 e^{-3x}$ for $x > 0$ is a valid PDF.

**Solution:**
- **Step 1: Identify parameters.**
  This matches a Gamma PDF with $\alpha - 1 = 2 \implies \alpha = 3$ and $\beta = 3$.
- **Step 2: WIP State.**
  The normalisation constant for a Gamma distribution requires that the total area equals 1:
  $$c = \frac{\beta^\alpha}{\Gamma(\alpha)} = \frac{3^3}{\Gamma(3)} = \frac{27}{?}$$
- **Step 3: Final Calculation.**
  $$\Gamma(3) = 2! = 2$$
  $$c = \frac{27}{2} = 13.5.$$

---

### Exercise 5: Deriving Mean using MGF
**Problem:** Find the expected value of $X \sim Gamma(\alpha, \beta)$ by differentiating its MGF.

**Solution:**
- **Step 1: Set up the derivative.**
  $$M_X(t) = \left(1 - \frac{t}{\beta}\right)^{-\alpha}$$
  Use the chain rule:
  $$M'_X(t) = -\alpha \left(1 - \frac{t}{\beta}\right)^{-\alpha-1} \cdot \left(-\frac{1}{\beta}\right)$$
- **Step 2: WIP State.**
  Simplify the derivative:
  $$M'_X(t) = \frac{\alpha}{\beta} \left(1 - \frac{t}{\beta}\right)^{-\alpha-1}$$
  Evaluate at $t=0$:
  $$E[X] = M'_X(0) = \frac{\alpha}{\beta} (1 - 0)^{-( \alpha + 1 )} = ?$$
- **Step 3: Final Calculation.**
  $$E[X] = \frac{\alpha}{\beta}.$$

---

### Exercise 6: Sum of Independent Gammas
**Problem:** Let $X \sim Gamma(2, 5)$ and $Y \sim Gamma(3, 5)$ be independent random variables. Find the distribution of $W = X + Y$.

**Solution:**
- **Step 1: Recall MGF of Gamma.**
  $$M_X(t) = \left(1 - \frac{t}{5}\right)^{-2}, \quad M_Y(t) = \left(1 - \frac{t}{5}\right)^{-3}$$
- **Step 2: WIP State.**
  Since they are independent:
  $$M_W(t) = M_X(t) \cdot M_Y(t) = \left(1 - \frac{t}{5}\right)^{-2} \cdot \left(1 - \frac{t}{5}\right)^{-3} = \left(1 - \frac{t}{5}\right)^{?}$$
- **Step 3: Final Calculation.**
  $$M_W(t) = \left(1 - \frac{t}{5}\right)^{-5}$$
  By uniqueness of the MGF, $W \sim Gamma(5, 5)$.
  *(Exam note: You can add independent Gamma variables ONLY if they share the same rate parameter $\beta$!)*

---

### Exercise 7: Connection to Chi-Square
**Problem:** Show that the Chi-square distribution with $\nu$ degrees of freedom is a special case of the Gamma distribution by comparing their MGFs. Recall that the MGF of a Chi-square variable is $M_{\chi^2}(t) = (1 - 2t)^{-\nu/2}$.

**Solution:**
- **Step 1: Look at the Gamma MGF.**
  $$M_{Gamma}(t) = \left(1 - \frac{t}{\beta}\right)^{-\alpha}$$
- **Step 2: WIP State.**
  We want to set:
  $$\left(1 - \frac{t}{\beta}\right)^{-\alpha} = (1 - 2t)^{-\nu/2}$$
  Matching the terms:
  - Exponent: $-\alpha = -\frac{\nu}{2} \implies \alpha = \frac{\nu}{2}$.
  - Fraction: $\frac{t}{\beta} = 2t \implies \beta = ?$.
- **Step 3: Final Calculation.**
  $$\beta = \frac{1}{2}$$
  Thus, a Chi-square distribution with $\nu$ degrees of freedom is exactly equivalent to $Gamma\left(\alpha = \frac{\nu}{2}, \beta = \frac{1}{2}\right)$.

---

### Exercise 8: Expected Value of a Reciprocal
**Problem:** Let $X \sim Gamma(\alpha, \beta)$ with $\alpha > 1$. Find the expected value of the reciprocal of $X$, $E\left[\frac{1}{X}\right]$.

**Solution:**
- **Step 1: Set up the integral.**
  $$E\left[\frac{1}{X}\right] = \int_{0}^{\infty} \frac{1}{x} \cdot f(x) \, dx = \int_{0}^{\infty} \frac{1}{x} \cdot \frac{\beta^\alpha}{\Gamma(\alpha)} x^{\alpha-1} e^{-\beta x} \, dx$$
- **Step 2: WIP State.**
  Simplify the integrand:
  $$E\left[\frac{1}{X}\right] = \frac{\beta^\alpha}{\Gamma(\alpha)} \int_{0}^{\infty} x^{\alpha-2} e^{-\beta x} \, dx$$
  Notice that the integral is almost the integral of a Gamma PDF with shape parameter $\alpha' = \alpha - 1$ and rate parameter $\beta' = \beta$.
  $$\int_{0}^{\infty} x^{(\alpha-1)-1} e^{-\beta x} \, dx = \frac{\Gamma(\alpha-1)}{\beta^{\alpha-1}}$$
  Substituting this back:
  $$E\left[\frac{1}{X}\right] = \frac{\beta^\alpha}{\Gamma(\alpha)} \cdot \frac{\Gamma(\alpha-1)}{\beta^{\alpha-1}} = \beta \cdot \frac{\Gamma(\alpha-1)}{?}$$
- **Step 3: Final Calculation.**
  Recall that $\Gamma(\alpha) = (\alpha - 1) \cdot \Gamma(\alpha - 1)$.
  $$E\left[\frac{1}{X}\right] = \beta \cdot \frac{\Gamma(\alpha-1)}{(\alpha-1)\Gamma(\alpha-1)} = \frac{\beta}{\alpha - 1}.$$

---

### Exercise 9: Linear Transformation (Gotcha Moment)
**Problem:** If $X \sim Gamma(\alpha, \beta)$, does $Y = cX$ (where $c > 0$) follow a Gamma distribution? If so, what are its parameters?

**Solution:**
- **Step 1: Use the MGF method.**
  $$M_Y(t) = M_{cX}(t) = M_X(ct)$$
- **Step 2: WIP State.**
  Substitute $ct$ into the MGF of $X$:
  $$M_Y(t) = \left(1 - \frac{ct}{\beta}\right)^{-\alpha} = \left(1 - \frac{t}{\beta/c}\right)^{?}$$
- **Step 3: Final Calculation.**
  $$M_Y(t) = \left(1 - \frac{t}{\beta/c}\right)^{-\alpha}$$
  By uniqueness of the MGF, this represents a Gamma distribution:
  $$Y \sim Gamma\left(\alpha, \frac{\beta}{c}\right)$$
  *(Gotcha check: Scaling a Gamma variable changes its rate parameter to $\beta/c$ while keeping the shape parameter $\alpha$ unchanged. If you scale by 2, the rate is cut in half, which makes physical sense as the variable becomes twice as spread out!)*
