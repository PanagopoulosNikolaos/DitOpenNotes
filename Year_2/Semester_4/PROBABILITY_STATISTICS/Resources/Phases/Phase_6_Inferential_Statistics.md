# Phase 6: Inferential Statistics

## Table of Contents
1. [Probability Inequalities and Laws of Large Numbers](#1-probability-inequalities-and-laws-of-large-numbers)
2. [Sampling Distributions](#2-sampling-distributions)
3. [Central Limit Theorem (CLT)](#3-central-limit-theorem-clt)
4. [Confidence Intervals](#4-confidence-intervals)
5. [Hypothesis Testing](#5-hypothesis-testing)
6. [Time-Specific Gotchas](#6-time-specific-gotchas)
7. [Solved Exercises](#7-solved-exercises)
8. [Phase Summary](#phase-summary)

---

## 1. Probability Inequalities and Laws of Large Numbers

When detailed probability density functions $f_T(t)$ are unknown, mathematical inequalities provide guaranteed non-parametric upper bounds on latency tail probabilities.

### Markov's Inequality
For a non-negative continuous time random variable $T \ge 0$, and constant $a > 0$:
$$P(T \ge a) \le \frac{E[T]}{a}$$

### Chebyshev's Inequality
For any random variable $T$ with finite mean $\mu_T$ and finite variance $\sigma_T^2$, the probability of deviating from the mean by $k$ standard deviations ($k > 0$) is bounded:
$$P(|T - \mu_T| \ge k \sigma_T) \le \frac{1}{k^2}$$

### Laws of Large Numbers (LLN)
Let $T_1, T_2, \dots, T_n$ be i.i.d. execution time measurements with mean $\mu_T$. The sample mean duration $\bar{T}_n = \frac{1}{n} \sum_{i=1}^n T_i$ converges in probability (Weak Law) and almost surely (Strong Law) to true population mean $\mu_T$ as $n \to \infty$.

---

## 2. Sampling Distributions

Sample statistics are random variables with their own probability distributions.

### Distribution of the Sample Variance ($S^2$)
For a random sample from a Normal population $N(\mu, \sigma^2)$, the scaled sample variance follows a Chi-square ($\chi^2$) distribution with $\nu = n-1$ degrees of freedom:
$$\frac{(n-1)S^2}{\sigma^2} \sim \chi^2_{n-1}$$

### Student's t-Distribution
Arises when estimating the mean of a normally distributed population when $n < 30$ and $\sigma$ is unknown, replacing $\sigma$ with sample standard deviation $s$.

### Fisher-Snedecor F-Distribution
Models the ratio of scaled variances from two independent normal populations. Under $H_0: \sigma_1^2 = \sigma_2^2$, the test statistic $F = s_1^2 / s_2^2$ follows $F_{n_1-1, n_2-1}$.

---

## 3. Central Limit Theorem (CLT)

The CLT states that the sample mean $\bar{T}$ of $n$ independent and identically distributed random time metrics approaches a Normal distribution as sample size $n$ grows large ($n \ge 30$), regardless of the underlying latency distribution.

$$\bar{T} \xrightarrow{d} N\left(\mu_T, \frac{\sigma_T^2}{n}\right)$$

### Standardized Z-Score for Sample Means
$$Z = \frac{\bar{T} - \mu_T}{\sigma_T / \sqrt{n}} \sim N(0, 1)$$

---

## 4. Confidence Intervals

A Confidence Interval (CI) provides a range of plausible values for an unknown population parameter with a specified confidence level $1 - \alpha$.

### Confidence Interval for Population Mean ($\mu_T$)
* **Known $\sigma_T$ (or $n \ge 30$):** $CI = \bar{T} \pm z_{\alpha/2} \frac{\sigma_T}{\sqrt{n}}$
* **Unknown $\sigma_T$ ($n < 30$):** $CI = \bar{T} \pm t_{\alpha/2, n-1} \frac{s_T}{\sqrt{n}}$

### Confidence Interval for Population Variance ($\sigma_T^2$)
$$CI = \left[ \frac{(n - 1) s_T^2}{\chi_{\alpha/2, n-1}^2}, \, \frac{(n - 1) s_T^2}{\chi_{1 - \alpha/2, n-1}^2} \right]$$

---

## 5. Hypothesis Testing

Hypothesis testing evaluates empirical evidence against a default status quo assertion ($H_0$).

*   **Null Hypothesis ($H_0$):** Status quo assertion (e.g., $\mu \le \mu_0$).
*   **Alternative Hypothesis ($H_1$):** Research hypothesis (e.g., $\mu > \mu_0$).
*   **Type I Error ($\alpha$):** Rejecting $H_0$ when it is true (False Alarm).
*   **Type II Error ($\beta$):** Failing to reject $H_0$ when $H_1$ is true (Missed Detection).
*   **Power of the Test ($1 - \beta$):** Probability of correctly rejecting a false $H_0$.

### Decision Rules
* **Critical Value Approach:** Reject $H_0$ if the test statistic falls into the rejection region (determined by $z_{\alpha}$, $t_{\alpha}$, etc.).
* **p-Value Approach:** Reject $H_0$ if $p\text{-value} \le \alpha$.

---

## 6. Time-Specific Gotchas

1. **Confusing Population SD ($\sigma_T$) with Standard Error ($\sigma_{\bar{T}}$):** The variability of the *average* time is $\sigma_{\bar{T}} = \sigma_T / \sqrt{n}$, not $\sigma_T$.
2. **Applying CLT to Small Samples ($n < 30$) from Skewed Distributions:** For skewed metrics like latency, $\bar{T}$ remains skewed for small $n$. Wait for $n \ge 30$.
3. **Misinterpreting the $95\%$ Confidence Level:** It does not mean a $95\%$ chance that true mean $\mu_T$ lies in the calculated interval. It means the *method* works $95\%$ of the time.
4. **Confounding Practical vs Statistical Significance:** A $0.001\text{ ms}$ latency drop can be statistically significant with large $n$, but practically meaningless.
5. **Sensitivity of $\chi^2$ and $F$ Tests:** Unlike $t$-tests, variance tests are extremely sensitive to non-normality. Do not blindly use them on right-skewed latency data.

---

## 7. Solved Exercises

#### Exercise 1: Standard Error of Mean Latency
**Problem:** DB query duration has population mean $\mu_T = 150\text{ ms}$ and standard deviation $\sigma_T = 40\text{ ms}$. Calculate standard error of the mean for $n = 16$.
**Solution:**
$$\sigma_{\bar{T}} = \frac{40}{\sqrt{16}} = \frac{40}{4} = 10\text{ ms}$$

#### Exercise 2: Sample Size Determination for Targeted Latency Margin
**Problem:** Individual network delay has $\sigma_T = 30\text{ ms}$. How many sample pings $n$ are needed so that the sample mean $\bar{T}$ lies within $\pm 3\text{ ms}$ of true mean $\mu_T$ with $95\%$ probability?
**Solution:**
$$n = \left( \frac{z_{0.025} \cdot \sigma_T}{E} \right)^2 = \left( \frac{1.96 \cdot 30}{3} \right)^2 = (19.6)^2 = 384.16$$
Round up to $n = 385$ pings.

#### Exercise 3: Comparing Individual vs Sample Mean Tail Probabilities
**Problem:** Latency $T \sim N(100, 400)$ ($\mu_T = 100, \sigma_T = 20$). Compare $P(T > 110)$ for a single request vs $P(\bar{T} > 110)$ for $n = 25$ requests.
**Solution:**
Single request: $z = \frac{110 - 100}{20} = 0.50 \implies P(T > 110) = 1 - \Phi(0.50) = 0.3085 \text{ (30.85\%)}$.
Sample mean ($n=25$): $\sigma_{\bar{T}} = \frac{20}{5} = 4$. $z = \frac{110 - 100}{4} = 2.50 \implies P(\bar{T} > 110) = 1 - \Phi(2.50) = 0.0062 \text{ (0.62\%)}$.

#### Exercise 4: 95% t-Confidence Interval (Small Sample $n = 16$)
**Problem:** Benchmark of $n = 16$ microservice executions yields $\bar{T} = 5.4\text{ s}$ and $s_T = 0.8\text{ s}$. Construct a $95\%$ CI for $\mu_T$.
**Solution:**
$t_{0.025, 15} = 2.131$. $\text{SE} = \frac{0.8}{\sqrt{16}} = 0.2\text{ s}$.
Margin of Error $E = 2.131 \times 0.2 = 0.4262\text{ s}$.
$\text{CI} = [5.4 - 0.4262, 5.4 + 0.4262] = [4.9738\text{ s}, 5.8262\text{ s}]$.

#### Exercise 5: Difference in Mean Execution Times Confidence Interval
**Problem:** System A ($n_1 = 40, \bar{T}_1 = 120\text{ ms}, s_1 = 16\text{ ms}$) and System B ($n_2 = 50, \bar{T}_2 = 135\text{ ms}, s_2 = 20\text{ ms}$). Construct a $95\%$ CI for $\mu_2 - \mu_1$.
**Solution:**
Estimate $= 135 - 120 = 15\text{ ms}$.
$\text{SE}_{\text{diff}} = \sqrt{\frac{16^2}{40} + \frac{20^2}{50}} = \sqrt{6.4 + 8.0} = \sqrt{14.4} \approx 3.7947\text{ ms}$.
$E = 1.96 \times 3.7947 = 7.4376\text{ ms}$.
$\text{CI} = [15 - 7.4376, 15 + 7.4376] = [7.5624\text{ ms}, 22.4376\text{ ms}]$.

#### Exercise 6: One-Sample Z-Test for Latency SLA Benchmark
**Problem:** SLA mandates mean response time $\mu_T \le 100\text{ ms}$. A sample of $n = 64$ requests has $\bar{T} = 105\text{ ms}$ with known $\sigma_T = 16\text{ ms}$. Test at $\alpha = 0.05$ whether SLA is violated ($H_1: \mu_T > 100$).
**Solution:**
$\text{SE} = \frac{16}{\sqrt{64}} = 2\text{ ms}$. $Z = \frac{105 - 100}{2} = 2.50$.
Critical value $z_{0.05} = 1.645$. Since $Z = 2.50 > 1.645$, reject $H_0$. Strong evidence SLA is violated.

#### Exercise 7: Two-Sample Welch's t-Test Comparing Cloud Regions
**Problem:** Region A ($n_1 = 36, \bar{T}_1 = 82, s_1 = 12$) and Region B ($n_2 = 36, \bar{T}_2 = 90, s_2 = 15$). Test at $\alpha = 0.05$ whether mean latencies differ ($H_1: \mu_1 \neq \mu_2$).
**Solution:**
$\text{SE}_{\text{diff}} = \sqrt{\frac{144}{36} + \frac{225}{36}} = \sqrt{10.25} \approx 3.2016$.
$t = \frac{82 - 90}{3.2016} \approx -2.50$.
Critical value $z_{0.025} = 1.96$ ($df \approx 66$). Since $|t| = 2.50 > 1.96$, reject $H_0$.

#### Exercise 8: Statistical Power ($1 - \beta$) Calculation for Latency
**Problem:** Testing $H_0: \mu_T = 100\text{ ms}$ vs $H_1: \mu_T = 90\text{ ms}$ with $\sigma_T = 20\text{ ms}, n = 25, \alpha = 0.05$ (left-tailed). Calculate test power.
**Solution:**
$\text{SE} = 4\text{ ms}$. Rejection cutoff $\bar{T}_{\text{crit}} = 100 - 1.645(4) = 93.42\text{ ms}$.
Under $H_1: \mu_T = 90$, $z = \frac{93.42 - 90}{4} = 0.855 \approx 0.86$.
Power $= \Phi(0.86) = 0.8051$ (approx $80.51\%$).

#### Exercise 9: 95% Confidence Interval for Population Variance $\sigma_T^2$
**Problem:** $n = 25$ measurements yield $s_T^2 = 16\text{ ms}^2$. Construct $95\%$ CI for $\sigma_T^2$.
**Solution:**
$df = 24$. $\chi_{0.025, 24}^2 = 39.36, \chi_{0.975, 24}^2 = 12.40$.
Lower $= \frac{24 \times 16}{39.36} \approx 9.756$. Upper $= \frac{24 \times 16}{12.40} \approx 30.968$.
$\text{CI} = [9.76\text{ ms}^2, 30.97\text{ ms}^2]$.

#### Exercise 10: Markov's Inequality Upper Bound on Severe Latency
**Problem:** API mean latency is $E[T] = 50\text{ ms}$. Find an upper bound on $P(T \ge 200\text{ ms})$.
**Solution:**
By Markov: $P(T \ge 200) \le \frac{50}{200} = 0.25 \text{ (25\%)}$.

#### Exercise 11: Chebyshev Bound for 3-Sigma Latency Outliers
**Problem:** Latency $T$ has $\mu_T = 120\text{ ms}$ and $\sigma_T = 15\text{ ms}$. Find upper bound on $P(|T - 120| \ge 45)$.
**Solution:**
$45 = 3\sigma_T$. By Chebyshev: $P(|T - 120| \ge 3\sigma_T) \le \frac{1}{3^2} = \frac{1}{9} \approx 0.1111 \text{ (11.11\%)}$.

#### Exercise 12: R Code Verification of WLLN Convergence
**Problem:** Write R code demonstrating the convergence of sample mean execution time to true mean $\mu_T = 10$ as sample size grows to $10{,}000$.
**Solution:**
```r
set.seed(42)
latencies <- rexp(10000, rate = 0.1) # mu = 10
cum_means <- cumsum(latencies) / (1:10000)
cat("Sample mean at n = 10000:", round(cum_means[10000], 3), "\n") # approaches 10.000
```

---

## Phase Summary
Phase 6 pivots from pure probability to Inferential Statistics, forming the bridge between raw latency samples and definitive architectural conclusions. The theoretical engine driving this is the Central Limit Theorem (CLT), which proves that average latencies ($\bar{T}$) distribute normally even when individual execution times are wildly skewed. Laws of Large Numbers and Chebyshev’s Inequality guarantee that sample statistics aggressively converge to true parameters as $N$ scales. Practically, Confidence Intervals replace fragile single-point estimates with robust, statistically sound latency ranges. Hypothesis Testing formalizes A/B testing (e.g., did the new index *actually* reduce query times?), carefully balancing Type I Errors (false optimization claims) against Type II Errors (missed speedups) and incorporating the $t$, $\chi^2$, and $F$-distributions to accurately assess means and variances from limited operational data.
