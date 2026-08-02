# Phase 7: R Programming Commands

## Table of Contents
1. [Descriptive Statistics](#1-descriptive-statistics)
2. [Binomial Distribution](#2-binomial-distribution)
3. [Normal Distribution](#3-normal-distribution)
4. [Additional Distributions](#4-additional-distributions)
5. [Time-Specific Gotchas](#5-time-specific-gotchas)
6. [Solved Exercises](#6-solved-exercises)
7. [Phase Summary](#phase-summary)

---

## 1. Descriptive Statistics

R provides a streamlined suite of functions to calculate descriptive statistics from data vectors.

### Core Summary Functions
*   **Mean:** `mean(x, na.rm = TRUE)` — Calculates the arithmetic average ($\bar{X}$). Use `trim = 0.05` to compute trimmed means (removes extreme 5% of data).
*   **Median:** `median(x, na.rm = TRUE)` — Finds the middle value.
*   **Variance:** `var(x, na.rm = TRUE)` — Calculates the **sample** variance ($s^2$).
*   **Standard Deviation:** `sd(x, na.rm = TRUE)` — Calculates the **sample** standard deviation ($s$).
*   **Quantiles / Percentiles:** `quantile(x, probs = c(0.25, 0.5, 0.75))` — Returns specified percentiles (e.g., SLA boundaries).
*   **Interquartile Range:** `IQR(x, na.rm = TRUE)` — Calculates $Q_3 - Q_1$.
*   **Summary:** `summary(x)` — Returns Min, $1^{\text{st}}$ Qu., Median, Mean, $3^{\text{rd}}$ Qu., Max.

### Mode in R
R does not have a built-in function for the mode. Instead, use:
```R
freq_table <- table(x)
names(freq_table)[freq_table == max(freq_table)]
```

---

## 2. Binomial Distribution

R handles probability distributions systematically using prefix notation (`d`, `p`, `q`, `r`). For the Binomial distribution, the root is `binom`.

*   **Exact Probability ($P(X = k)$):** `dbinom(x = k, size = n, prob = p)`
*   **Cumulative Probability ($P(X \le q)$):** `pbinom(q = k, size = n, prob = p)`
    * Use `lower.tail = FALSE` to compute $P(X > q)$.
*   **Quantile (Inverse CDF):** `qbinom(p = prob, size = n, prob = p)` — Finds the smallest $k$ such that $P(X \le k) \ge p$.
*   **Random Generation:** `rbinom(n = samples, size = n, prob = p)`

---

## 3. Normal Distribution

The Normal distribution relies on mean ($\mu$) and standard deviation ($\sigma$). The root is `norm`.

*   **Cumulative Probability ($P(X \le q)$):** `pnorm(q = x, mean = \mu, sd = \sigma)`
    * Default parameters are $\mu = 0$ and $\sigma = 1$ (Standard Normal).
*   **Quantile (Inverse CDF):** `qnorm(p = prob, mean = \mu, sd = \sigma)` — Finds $x$ for a given cumulative probability.
*   **Random Generation:** `rnorm(n = samples, mean = \mu, sd = \sigma)`
*   **Density Function:** `dnorm(x, mean = \mu, sd = \sigma)` — Returns the height of the PDF (used primarily for plotting).

---

## 4. Additional Distributions

### 4.1 Discrete Distributions
*   **Geometric (`geom`):** `dgeom(x, prob)` / `pgeom(q, prob)`. *Note: `x` and `q` represent the number of FAILURES before the first success, not the total number of trials.*
*   **Hypergeometric (`hyper`):** `dhyper(x, m, n, k)` / `phyper(q, m, n, k)`.
    * `m`: Number of success items in population ($K$).
    * `n`: Number of failure items in population ($N-K$).
    * `k`: Sample size ($n$).

### 4.2 Continuous Distributions
*   **Exponential (`exp`):** `dexp(x, rate = \lambda)` / `pexp(q, rate = \lambda)`. $\text{Mean} = 1/\lambda$.
*   **Gamma (`gamma`):** `dgamma(x, shape = \alpha, rate = \beta)` / `pgamma(q, shape = \alpha, rate = \beta)`.
*   **Weibull (`weibull`):** `pweibull(q, shape = k, scale = \lambda)`.
*   **Uniform (`unif`):** `punif(q, min = a, max = b)`.

### 4.3 Sampling Distributions (For Hypothesis Testing)
*   **Chi-Square (`chisq`):** `pchisq(q, df)` / `qchisq(p, df)`.
*   **Student's t (`t`):** `pt(q, df)` / `qt(p, df)`.
*   **Fisher's F (`f`):** `pf(q, df1, df2)` / `qf(p, df1, df2)`.

---

## 5. Time-Specific Gotchas

1. **`sd` Parameter vs Variance:** `pnorm()` and `rnorm()` expect the standard deviation `sd`, not the variance. If given $\sigma_T^2 = 100$, pass `sd = 10` (or `sqrt(100)`).
2. **`lower.tail = FALSE` Strict Inequality:** In R, `pbinom(q, ..., lower.tail = FALSE)` evaluates $P(X > q)$. To calculate $P(X \ge k)$, you must pass `q = k - 1`. For continuous distributions, $P(T > q) = P(T \ge q)$, so this adjustment is unnecessary.
3. **Sample vs Population Variance:** `var()` computes the sample variance (dividing by $n-1$). To get population variance, compute manually or multiply `var(x)` by $(n-1)/n$.
4. **Geometric Distribution Definition:** R strictly models the number of failures *before* success. Finding the first success on the 5th trial means $x = 4$ failures.
5. **Gamma Rate vs Scale:** Passing `rate = beta` means $E[T] = \text{shape} / \text{rate}$. If you specify `scale = theta`, then $E[T] = \text{shape} \times \text{scale}$. Always name the parameter explicitly.

---

## 6. Solved Exercises

#### Exercise 1: Basic Descriptive Statistics on Response Times
**Problem:** Vector `latencies <- c(120, 145, 110, 160, 130, 210, 125, 135, 140, 150)`. Compute mean, median, SD, and Variance.
**Solution:**
```R
latencies <- c(120, 145, 110, 160, 130, 210, 125, 135, 140, 150)
mean_lat <- mean(latencies)     # 142.5
med_lat  <- median(latencies)   # 137.5
sd_lat   <- sd(latencies)       # 27.65863
var_lat  <- var(latencies)      # 765
```

#### Exercise 2: Trimming Outliers from Latency Means
**Problem:** Compare mean vs $5\%$ trimmed mean for `raw_lat <- c(100, 102, 98, 105, 101, 99, 103, 1500)`.
**Solution:**
```R
raw_lat <- c(100, 102, 98, 105, 101, 99, 103, 1500)
mean(raw_lat)               # 276
mean(raw_lat, trim = 0.05)  # 276 (since 5% of 8 is 0.4, no elements are removed unless trim is higher)
mean(raw_lat, trim = 0.15)  # 101.3333 (removes 1 highest and 1 lowest)
```

#### Exercise 3: Binomial Exact and Cumulative Probability
**Problem:** $n = 20$ requests, $p = 0.05$ timeout probability. Calculate $P(X = 2)$ and $P(X \le 1)$.
**Solution:**
```R
dbinom(x = 2, size = 20, prob = 0.05) # 0.1886768
pbinom(q = 1, size = 20, prob = 0.05) # 0.7358395
```

#### Exercise 4: Binomial "At Least $k$" Using Complement
**Problem:** Find $P(X \ge 3)$ timeouts out of $n = 100$ requests with $p = 0.01$.
**Solution:**
```R
# P(X >= 3) = P(X > 2), so we pass q = 2
pbinom(q = 2, size = 100, prob = 0.01, lower.tail = FALSE) # 0.0793732
```

#### Exercise 5: Normal Cumulative Probability
**Problem:** DB query $T \sim N(120\text{ ms}, 15^2)$. Calculate $P(T \le 100\text{ ms})$.
**Solution:**
```R
pnorm(q = 100, mean = 120, sd = 15) # 0.09121122
```

#### Exercise 6: Normal SLA 99th Percentile Limit
**Problem:** Find $t_{99}$ for $T \sim N(50\text{ ms}, 10^2\text{ ms}^2)$.
**Solution:**
```R
qnorm(p = 0.99, mean = 50, sd = 10) # 73.26348 ms
```

#### Exercise 7: Geometric Distribution Failures
**Problem:** Probability of finding the first defective part on the 5th test ($p = 0.08$).
**Solution:**
```R
# 5th test means 4 failures before the first success.
dgeom(x = 4, prob = 0.08) # 0.05731454
```

#### Exercise 8: Exponential Component Survival
**Problem:** $T \sim \text{Exp}(\text{rate} = 0.002\text{ h}^{-1})$. Calculate $P(T > 1000\text{ hours})$.
**Solution:**
```R
pexp(q = 1000, rate = 0.002, lower.tail = FALSE) # 0.1353353
```

#### Exercise 9: Gamma Waiting Time Distribution
**Problem:** $T \sim \text{Gamma}(\text{shape}=4, \text{rate}=0.5)$. Calculate $P(T \le 10)$.
**Solution:**
```R
pgamma(q = 10, shape = 4, rate = 0.5) # 0.7349741
```

#### Exercise 10: F-test p-value
**Problem:** Calculate p-value for sample variance ratio $F = 2.80$ with $df_1 = 15, df_2 = 20$.
**Solution:**
```R
pf(q = 2.80, df1 = 15, df2 = 20, lower.tail = FALSE) # 0.01538356
```

---

## Phase Summary
Phase 7 concludes the syllabus by translating theoretical probability concepts into computational R functions. It maps the mathematical concepts learned in earlier phases (PMF, CDF, quantiles) to their functional equivalents (`d`, `p`, `q`, `r` prefixes) for key distributions (Binomial, Normal, Exponential, Geometric, etc.). Furthermore, it addresses critical language-specific quirks, such as `sd` taking standard deviation rather than variance, the geometric distribution counting *failures*, and `lower.tail = FALSE` enforcing strict inequalities. Mastering these commands equips you to efficiently compute complex percentiles, model time-window events, and perform statistical inference directly from raw log data.
