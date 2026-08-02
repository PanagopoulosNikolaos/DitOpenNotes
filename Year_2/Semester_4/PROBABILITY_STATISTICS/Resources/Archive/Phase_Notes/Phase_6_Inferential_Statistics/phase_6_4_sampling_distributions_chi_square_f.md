# Phase 6.4: Sampling Distributions, Chi-Square, t, and F Distributions

In inferential statistics, we use sample statistics (like the sample mean $\bar{X}$ or sample variance $S^2$) to estimate population parameters (like $\mu$ or $\sigma^2$). The probability distributions of these statistics are called **sampling distributions**.

---

## 1. Distribution of the Sample Variance ($S^2$)

Let $X_1, X_2, \dots, X_n$ be a random sample of size $n$ from a **Normal population** $N(\mu, \sigma^2)$. The sample variance is defined as:

$$S^2 = \frac{1}{n - 1} \sum_{i=1}^{n} (X_i - \bar{X})^2$$

A fundamental theorem in statistics states that:

$$\frac{(n-1)S^2}{\sigma^2} \sim \chi^2_{n-1}$$

This means that the scaled sample variance follows a Chi-square distribution with $\nu = n-1$ degrees of freedom. Furthermore, $\bar{X}$ and $S^2$ are independent random variables when sampling from a normal population.

---

## 2. The Chi-Square ($\chi^2$) Distribution

The Chi-square distribution with $\nu$ degrees of freedom is the distribution of the sum of squares of $\nu$ independent standard normal variables:

$$\chi^2_\nu = \sum_{i=1}^{\nu} Z_i^2, \quad \text{where } Z_i \sim N(0, 1) \text{ i.i.d.}$$

### Properties
*   **Domain:** $x \ge 0$
*   **Mean:** $E[\chi^2_\nu] = \nu$
*   **Variance:** $Var(\chi^2_\nu) = 2\nu$
*   **Additivity:** If $U \sim \chi^2_{\nu_1}$ and $V \sim \chi^2_{\nu_2}$ are independent, then:
    $$U + V \sim \chi^2_{\nu_1 + \nu_2}$$

---

## 3. Student's t-Distribution

The t-distribution arises when estimating the mean of a normally distributed population when the sample size is small ($n < 30$) and the population standard deviation $\sigma$ is unknown.

### Definition
If $Z \sim N(0, 1)$ and $W \sim \chi^2_\nu$ are independent, then the random variable:

$$T = \frac{Z}{\sqrt{W / \nu}} \sim t_\nu$$

follows Student's t-distribution with $\nu$ degrees of freedom.

### Properties
*   Symmetric and bell-shaped around 0 (like the standard normal, but with heavier tails).
*   As $\nu \to \infty$, the t-distribution converges to the standard normal distribution $N(0, 1)$.

---

## 4. Fisher-Snedecor F-Distribution

The F-distribution is used to compare the variances of two independent normal populations (e.g., in ANOVA or two-sample variance tests).

### Definition
If $U \sim \chi^2_{d_1}$ and $V \sim \chi^2_{d_2}$ are independent, then the ratio of their scaled variables:

$$F = \frac{U / d_1}{V / d_2} \sim F_{d_1, d_2}$$

follows the F-distribution with $d_1$ (numerator) and $d_2$ (denominator) degrees of freedom.

### Properties
*   **Domain:** $x > 0$
*   **Reciprocal Property:** If $F \sim F_{d_1, d_2}$, then:
    $$\frac{1}{F} \sim F_{d_2, d_1}$$

---

## 5. Solved Exercises (9 Examples)

### Exercise 1: Probability of Sample Variance
**Problem:** A random sample of size $n = 10$ is taken from a normal population with variance $\sigma^2 = 4$. Find the probability that the sample variance $S^2$ is less than 5.25. (Use the Chi-square table values: $P(\chi^2_9 \le 11.81) = 0.77$, $P(\chi^2_9 \le 16.92) = 0.95$).

**Solution:**
- **Step 1: Set up the Chi-square transformation.**
  We know that $\frac{(n-1)S^2}{\sigma^2} \sim \chi^2_{n-1}$.
  Substitute $n = 10$ and $\sigma^2 = 4$:
  $$\frac{9 S^2}{4} \sim \chi^2_9$$
- **Step 2: WIP State.**
  We want to find $P(S^2 < 5.25)$:
  $$P(S^2 < 5.25) = P\left(\frac{9 S^2}{4} < \frac{9 \cdot 5.25}{4}\right) = P\left(\chi^2_9 < \frac{47.25}{4}\right)$$
  Compute the fraction:
  $$\frac{47.25}{4} = ?$$
- **Step 3: Final Calculation.**
  - $\frac{47.25}{4} = 11.8125 \approx 11.81$.
  - $P(S^2 < 5.25) \approx P(\chi^2_9 < 11.81) = 0.77$.

---

### Exercise 2: Expected Value and Variance of Sample Variance
**Problem:** A sample of size $n = 25$ is drawn from a normal population with variance $\sigma^2 = 8$. Find the mean and variance of the sample variance $S^2$.

**Solution:**
- **Step 1: Express $S^2$ in terms of a Chi-square variable.**
  Let $Y = \frac{(n-1)S^2}{\sigma^2} \sim \chi^2_{n-1}$.
  So, $S^2 = \frac{\sigma^2}{n-1} Y$.
- **Step 2: WIP State.**
  Compute the mean:
  $$E[S^2] = E\left[ \frac{\sigma^2}{n-1} Y \right] = \frac{\sigma^2}{n-1} E[Y]$$
  Since $Y \sim \chi^2_{n-1}$, $E[Y] = n-1 = 24$.
  $$E[S^2] = \frac{8}{24} \cdot 24 = 8$$
  Compute the variance:
  $$Var(S^2) = Var\left( \frac{\sigma^2}{n-1} Y \right) = \left( \frac{\sigma^2}{n-1} \right)^2 Var(Y)$$
  Since $Y \sim \chi^2_{n-1}$, $Var(Y) = 2(n-1) = 48$.
  $$Var(S^2) = \left(\frac{8}{24}\right)^2 \cdot 48 = \left(\frac{1}{3}\right)^2 \cdot 48 = \frac{48}{?}$$
- **Step 3: Final Calculation.**
  - Denominator $= 9$.
  - $Var(S^2) = \frac{48}{9} = \frac{16}{3} \approx 5.3333$.
  *(Important check: Notice that $E[S^2] = \sigma^2$, which proves that the sample variance is an unbiased estimator of the population variance!).*

---

### Exercise 3: Sum of Independent Chi-Squares
**Problem:** Let $U \sim \chi^2_{10}$ and $V \sim \chi^2_{15}$ be independent. What is the distribution of $W = U + V$? Find $E[W]$ and $Var(W)$.

**Solution:**
- **Step 1: Identify the distribution of the sum.**
  By the additivity property of independent Chi-square variables:
  $$W = U + V \sim \chi^2_{10 + 15} \implies W \sim \chi^2_{25}$$
- **Step 2: WIP State.**
  For a Chi-square variable with $\nu = 25$ degrees of freedom:
  - $E[W] = \nu = 25$.
  - $Var(W) = 2\nu = 2 \cdot ?$.
- **Step 3: Final Calculation.**
  - $Var(W) = 50$.

---

### Exercise 4: Constructing a t-Statistic (Gotcha Moment)
**Problem:** Let $Z \sim N(0, 1)$ and $U \sim \chi^2_9$ be independent. Does $T = \frac{Z}{\sqrt{U}}$ follow a t-distribution? If not, modify it so it does.

**Solution:**
- **Step 1: Match the t-distribution definition.**
  The definition of a t-variable is:
  $$T = \frac{Z}{\sqrt{W / \nu}}$$
- **Step 2: WIP State.**
  Looking at $T = \frac{Z}{\sqrt{U}}$, the Chi-square variable $U$ (which has $\nu = 9$) is not divided by its degrees of freedom.
  Therefore, $T$ does **not** follow a t-distribution.
- **Step 3: Final Calculation.**
  To correct it, we must divide $U$ by 9 under the square root:
  $$T_{correct} = \frac{Z}{\sqrt{U / 9}} \sim t_9.$$

---

### Exercise 5: F-Distribution Bounds Transformation
**Problem:** Let $F \sim F_{5, 8}$. Find the value of $c$ such that $P(F > c) = 0.05$, given that for a variable $Y \sim F_{8, 5}$, we have $P(Y \le 4.82) = 0.95$.

**Solution:**
- **Step 1: Use the reciprocal property of the F-distribution.**
  If $F \sim F_{5, 8}$, then $\frac{1}{F} \sim F_{8, 5}$.
- **Step 2: WIP State.**
  We write the probability statement:
  $$P(F > c) = 0.05 \implies P\left(\frac{1}{F} < \frac{1}{c}\right) = 0.05$$
  Since $\frac{1}{F} \sim F_{8, 5}$, this is equivalent to:
  $$P\left(Y < \frac{1}{c}\right) = 0.05 \implies P\left(Y \ge \frac{1}{c}\right) = 0.95$$
  Wait, the problem states $P(Y \le 4.82) = 0.95 \implies P(Y > 4.82) = 0.05$.
  Let's reformulate:
  $$P(F > c) = 0.05 \implies P\left(\frac{1}{F} < \frac{1}{c}\right) = 0.05$$
  This means the left-tail probability of $Y = 1/F$ is 0.05.
  We know that for $Y \sim F_{8, 5}$, $P(Y > 4.82) = 0.05 \implies P(Y \le 4.82) = 0.95$.
  By reciprocal properties of critical values:
  $$c = F_{0.05}(5, 8) = \frac{1}{F_{0.95}(8, 5)} = \frac{1}{?}$$
- **Step 3: Final Calculation.**
  - $F_{0.95}(8, 5) = 4.82$.
  - $c = \frac{1}{4.82} \approx 0.2075$.

---

### Exercise 6: Normal Approximation of Chi-Square
**Problem:** For a Chi-square variable $X \sim \chi^2_{100}$, use the Central Limit Theorem to approximate $P(X \le 120)$. (Recall $\Phi(2) = 0.9772$).

**Solution:**
- **Step 1: Find the mean and variance of $X$.**
  - $\mu = \nu = 100$
  - $\sigma^2 = 2\nu = 200 \implies \sigma = \sqrt{200} \approx 14.14$.
- **Step 2: WIP State.**
  Standardize the variable:
  $$P(X \le 120) = P\left(\frac{X - 100}{14.14} \le \frac{120 - 100}{14.14}\right) \approx P\left(Z \le \frac{20}{14.14}\right)$$
  Compute the fraction:
  $$\frac{20}{14.14} = ?$$
- **Step 3: Final Calculation.**
  - $\frac{20}{14.14} \approx 1.414$ (which is exactly $\sqrt{2}$).
  - $P(Z \le 1.41) = \Phi(1.41) \approx 0.9207$.

---

### Exercise 7: Mean of F-Distribution
**Problem:** Calculate the expected value of $F \sim F_{d_1, d_2}$ where $d_2 > 2$. Use the fact that if $V \sim \chi^2_{d_2}$, then $E\left[\frac{1}{V}\right] = \frac{1}{d_2 - 2}$.

**Solution:**
- **Step 1: Write $F$ in terms of $U$ and $V$.**
  $$F = \frac{U / d_1}{V / d_2} = \frac{d_2}{d_1} \cdot U \cdot \frac{1}{V}$$
- **Step 2: WIP State.**
  Since $U \sim \chi^2_{d_1}$ and $V \sim \chi^2_{d_2}$ are independent:
  $$E[F] = \frac{d_2}{d_1} \cdot E[U] \cdot E\left[\frac{1}{V}\right]$$
  We know $E[U] = d_1$ and $E\left[\frac{1}{V}\right] = \frac{1}{d_2 - 2}$.
  $$E[F] = \frac{d_2}{d_1} \cdot d_1 \cdot \frac{1}{?}$$
- **Step 3: Final Calculation.**
  - Denominator $= d_2 - 2$.
  - $E[F] = \frac{d_2}{d_2 - 2}$.
  *(Note: The mean of an F-distribution depends solely on the denominator degrees of freedom $d_2$!).*

---

### Exercise 8: Sample Variance Ratio (ANOVA Precursor)
**Problem:** We draw a sample of size $n_1 = 6$ from population 1 ($N(\mu_1, \sigma^2)$) and a sample of size $n_2 = 11$ from population 2 ($N(\mu_2, \sigma^2)$). Find the distribution of the ratio of their sample variances, $\frac{S_1^2}{S_2^2}$.

**Solution:**
- **Step 2: WIP State.**
  We know that:
  - $U = \frac{(n_1 - 1)S_1^2}{\sigma^2} \sim \chi^2_{n_1 - 1} \implies U \sim \chi^2_5$
  - $V = \frac{(n_2 - 1)S_2^2}{\sigma^2} \sim \chi^2_{n_2 - 1} \implies V \sim \chi^2_{10}$
  By the definition of the F-distribution:
  $$\frac{U / 5}{V / 10} \sim F_{5, 10}$$
  Substitute the expressions for $U$ and $V$:
  $$\frac{\frac{(n_1 - 1)S_1^2}{\sigma^2} \cdot \frac{1}{n_1 - 1}}{\frac{(n_2 - 1)S_2^2}{\sigma^2} \cdot \frac{1}{n_2 - 1}} = \frac{\frac{S_1^2}{\sigma^2}}{\frac{S_2^2}{\sigma^2}} = ?$$
- **Step 3: Final Calculation.**
  - The ratio simplifies to $\frac{S_1^2}{S_2^2}$.
  - Thus, $\frac{S_1^2}{S_2^2} \sim F_{5, 10}$.

---

### Exercise 9: Probability Bounds for t-Distribution
**Problem:** Let $T \sim t_{15}$. If $P(T > 2.131) = 0.025$, find $P(-2.131 < T < 2.131)$.

**Solution:**
- **Step 1: Use symmetry of the t-distribution.**
  Since the t-distribution is symmetric about 0:
  $$P(T < -2.131) = P(T > 2.131) = 0.025$$
- **Step 2: WIP State.**
  The total area under the PDF is 1. The two tails combined contain:
  $$P(T \le -2.131) + P(T \ge 2.131) = 0.025 + 0.025 = 0.05$$
  The area in the middle is the complement:
  $$P(-2.131 < T < 2.131) = 1 - 0.05 = ?$$
- **Step 3: Final Calculation.**
  $$P(-2.131 < T < 2.131) = 0.95.$$
