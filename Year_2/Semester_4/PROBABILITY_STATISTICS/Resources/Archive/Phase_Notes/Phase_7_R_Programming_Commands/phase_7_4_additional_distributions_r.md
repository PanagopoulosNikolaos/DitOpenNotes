# Phase 7.4: R Programming Commands - Additional Distributions and Statistical Functions

This file provides the R syntax, parameters, and exam gotchas for the remaining discrete and continuous probability distributions (Geometric, Hypergeometric, Exponential, Uniform, Gamma, Chi-Square, Student's t, and Fisher's F).

---

## 1. Geometric Distribution (`*geom`)

R functions: `dgeom()`, `pgeom()`, `qgeom()`, `rgeom()`.

> **CRITICAL EXAM GOTCHA:** R's geometric functions strictly model **Definition B** (the number of failures *before* the first success). 
> If a problem asks for the probability that the first success is on the 4th trial, this means there were exactly 3 failures. In R, you must use `x = 3`, not `4`!
> *   $P(X = 4 \text{ trials}) = \text{`dgeom(3, prob)`}$
> *   $P(X \le 4 \text{ trials}) = P(\text{failures} \le 3) = \text{`pgeom(3, prob)`}$

---

## 2. Hypergeometric Distribution (`*hyper`)

R functions: `dhyper()`, `phyper()`, `qhyper()`, `rhyper()`.

> **CRITICAL EXAM GOTCHA:** R's naming convention for hypergeometric parameters is completely different from standard textbook notation ($N, K, n$).
> *   R syntax: `dhyper(x, m, n, k)`
> *   Parameter Mapping:
>     *   `x`: Number of successes in the sample ($k$).
>     *   `m`: Number of success items in the population ($K$).
>     *   `n`: Number of **failure** items in the population ($N - K$). *(Do not pass the total population $N$ here!)*
>     *   `k`: The sample size ($n$).

---

## 3. Other Continuous Distributions (`*exp`, `*unif`, `*gamma`)

### 3.1 Exponential: `dexp(x, rate)`, `pexp(q, rate)`
*   `rate` is $\lambda$ (where mean $= 1/\lambda$).

### 3.2 Uniform: `dunif(x, min, max)`, `punif(q, min, max)`
*   `min` and `max` are the lower ($a$) and upper ($b$) boundaries.

### 3.3 Gamma: `dgamma(x, shape, rate, scale = 1/rate)`
*   R accepts both the rate parameter $\beta$ (`rate`) and scale parameter $\theta$ (`scale`). 
*   **Safety Tip:** Always explicitly name the parameter in the function call to avoid using the wrong parameterization: e.g., `dgamma(x, shape = 3, rate = 2)`.

---

## 4. Sampling Distributions (`*chisq`, `*t`, `*f`)

These functions are primarily used to find critical values (using `q*`) and p-values (using `p*`) for hypothesis testing.

*   **Chi-Square:** `pchisq(q, df)`, `qchisq(p, df)`
*   **Student's t:** `pt(q, df)`, `qt(p, df)`
*   **Fisher's F:** `pf(q, df1, df2)`, `qf(p, df1, df2)`

---

## 5. Solved Exercises (9 Examples)

### Example 1: Geometric Probability (Trials vs. Failures)
**Problem:** A machine produces defective parts with probability $p = 0.08$. Write the R command to calculate the probability that the first defective part is found on the 5th test.

**Solution:**
- **Step 1: Translate trials to failures.**
  Finding the first success on the 5th test means the first 4 tests were failures.
- **Step 2: WIP State.**
  We want 4 failures before the first success.
  R function call:
  `dgeom(x = 4, prob = ?)`
- **Step 3: Final Calculation.**
  `dgeom(x = 4, prob = 0.08)`
  *(Result: 0.0573)*

---

### Example 2: Hypergeometric Probability Mapping
**Problem:** A deck of 52 cards contains 4 Aces. If we draw 5 cards without replacement, write the R command to find the probability of getting exactly 2 Aces.

**Solution:**
- **Step 1: Map standard parameters to R parameters.**
  - Successes in sample $x = 2$
  - Successes in population $m = 4$
  - Failures in population $n = 52 - 4 = 48$ *(not 52!)*
  - Sample size $k = 5$
- **Step 2: WIP State.**
  `dhyper(x = 2, m = 4, n = 48, k = ?)`
- **Step 3: Final Calculation.**
  `dhyper(x = 2, m = 4, n = 48, k = 5)`
  *(Result: 0.0399)*

---

### Example 3: Uniform Distribution Wait Time
**Problem:** A bus arrives randomly between 10:00 and 10:30. Write the R command to find the probability that a passenger waiting since 10:00 waits more than 20 minutes.

**Solution:**
- **Step 1: Identify bounds.**
  Let time $X \sim U(0, 30)$. We want $P(X > 20) = 1 - P(X \le 20)$.
- **Step 2: WIP State.**
  Using `punif`:
  `1 - punif(q = 20, min = 0, max = 30)`
  Alternatively, using `lower.tail = FALSE`:
  `punif(q = 20, min = 0, max = 30, lower.tail = ?)`
- **Step 3: Final Calculation.**
  `punif(q = 20, min = 0, max = 30, lower.tail = FALSE)`
  *(Result: 0.3333)*

---

### Example 4: Exponential Wait Time
**Problem:** The lifetime of a light bulb is exponentially distributed with a mean of 1000 hours. Write the R command to find the probability that a bulb lasts less than 800 hours.

**Solution:**
- **Step 1: Calculate rate parameter.**
  Mean $= 1000 \implies \lambda = 1/1000 = 0.001$.
- **Step 2: WIP State.**
  We want $P(X < 800)$.
  `pexp(q = 800, rate = ?)`
- **Step 3: Final Calculation.**
  `pexp(q = 800, rate = 0.001)`
  *(Result: 0.5507)*

---

### Example 5: Gamma Wait Time
**Problem:** A service center receives calls where the wait time between calls is exponentially distributed with a mean of 2 minutes. Write the R command to find the probability that it takes more than 15 minutes to receive 5 calls.

**Solution:**
- **Step 1: Map to Gamma parameters.**
  The sum of 5 independent $Exp(0.5)$ variables follows $Gamma(\alpha = 5, \beta = 0.5)$.
  - `shape` $= 5$
  - `rate` $= 1/2 = 0.5$
- **Step 2: WIP State.**
  We want $P(X > 15)$, so we use `lower.tail = FALSE`:
  `pgamma(q = 15, shape = 5, rate = 0.5, lower.tail = ?)`
- **Step 3: Final Calculation.**
  `pgamma(q = 15, shape = 5, rate = 0.5, lower.tail = FALSE)`
  *(Result: 0.1334)*

---

### Example 6: Finding Chi-Square Critical Values
**Problem:** Find the critical value $\chi^2_{\alpha}$ such that the area in the right tail is $0.05$ for a Chi-square distribution with 14 degrees of freedom.

**Solution:**
- **Step 1: Identify quantile function and area.**
  An upper-tail area of $0.05$ means the cumulative area from the left is $0.95$.
- **Step 2: WIP State.**
  `qchisq(p = 0.95, df = 14)`
  Or, using the upper tail:
  `qchisq(p = 0.05, df = 14, lower.tail = ?)`
- **Step 3: Final Calculation.**
  `qchisq(p = 0.05, df = 14, lower.tail = FALSE)`
  *(Result: 23.68)*

---

### Example 7: Student's t Hypothesis p-value
**Problem:** A researcher computes a t-statistic of $t = -2.15$ with $df = 18$ for a two-tailed test. Write the R command to calculate the p-value.

**Solution:**
- **Step 1: Recall two-tailed p-value formula.**
  $$\text{p-value} = 2 \cdot P(T \le -|t|)$$
- **Step 2: WIP State.**
  Since $t = -2.15$ is negative, the left tail probability is `pt(-2.15, df = 18)`.
  Multiply this by 2 to get both tails:
  `2 * pt(q = -2.15, df = ?)`
- **Step 3: Final Calculation.**
  `2 * pt(q = -2.15, df = 18)`
  *(Result: 0.0454)*

---

### Example 8: F-Distribution Quantiles for ANOVA
**Problem:** In an ANOVA test, the numerator degrees of freedom is 3 and the denominator degrees of freedom is 20. Find the critical F-value for a significance level of $\alpha = 0.01$.

**Solution:**
- **Step 1: Map parameters.**
  We want the 99th percentile of $F_{3, 20}$.
- **Step 2: WIP State.**
  `qf(p = 0.99, df1 = 3, df2 = 20)`
  Or, using the upper tail:
  `qf(p = 0.01, df1 = 3, df2 = 20, lower.tail = ?)`
- **Step 3: Final Calculation.**
  `qf(p = 0.01, df1 = 3, df2 = 20, lower.tail = FALSE)`
  *(Result: 4.938)*

---

### Example 9: Sample Variance Probability Calculation
**Problem:** For a sample of size $n = 16$ from a normal population with $\sigma^2 = 25$, write the R command to find the probability that the sample variance $S^2$ exceeds 35.

**Solution:**
- **Step 1: Relate $S^2$ to the Chi-square distribution.**
  $$P(S^2 > 35) = P\left(\frac{15 S^2}{25} > \frac{15 \cdot 35}{25}\right) = P\left(\chi^2_{15} > 21\right)$$
- **Step 2: WIP State.**
  Compute the right tail of $\chi^2_{15}$ at 21:
  `pchisq(q = 21, df = 15, lower.tail = ?)`
- **Step 3: Final Calculation.**
  `pchisq(q = 21, df = 15, lower.tail = FALSE)`
  *(Result: 0.1369)*
