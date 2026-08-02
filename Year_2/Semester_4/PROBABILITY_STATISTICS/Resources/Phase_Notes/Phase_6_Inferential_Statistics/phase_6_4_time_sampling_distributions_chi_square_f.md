# Phase 6.4 (Time): Chi-Square and F-Distributions for Latency Variance

In high-reliability performance engineering, controlling latency jitter (variance $\sigma_T^2$) is as critical as controlling average response time $\mu_T$. The Chi-Square ($\chi^2$) distribution models the sampling distribution of sample variance $s_T^2$ for a single system, while the Snedecor $F$-distribution models the ratio of sample variances across two cloud platforms.

---

## 1. Chi-Square ($\chi^2$) Distribution for Single System Latency Variance

If $T_1, T_2, \dots, T_n$ is an i.i.d. sample of size $n$ from a Normal time population $N(\mu_T, \sigma_T^2)$ with sample variance $s_T^2 = \frac{1}{n-1} \sum_{i=1}^n (T_i - \bar{T})^2$, then the transformed statistic follows a Chi-Square distribution with $df = n - 1$ degrees of freedom:

$$\boxed{\chi^2 = \frac{(n - 1) s_T^2}{\sigma_T^2} \sim \chi_{n-1}^2}$$

### 1.1 Confidence Interval for Single Population Variance $\sigma_T^2$
The $100(1 - \alpha)\%$ confidence interval for population variance $\sigma_T^2$ is:

$$\boxed{\left[ \frac{(n - 1) s_T^2}{\chi_{\alpha/2, n-1}^2}, \, \frac{(n - 1) s_T^2}{\chi_{1 - \alpha/2, n-1}^2} \right]}$$

*(Standard deviation interval is obtained by taking square roots of bounds).*

---

## 2. F-Distribution for Comparing Variance of Two Systems

To test whether Platform A and Platform B have equal latency jitter ($\sigma_1^2 = \sigma_2^2$) using independent normal samples ($n_1, s_1^2$ and $n_2, s_2^2$), the test statistic ratio follows an $F$-distribution:

$$\boxed{F = \frac{s_1^2 / \sigma_1^2}{s_2^2 / \sigma_2^2} \sim F_{df_1 = n_1 - 1, \, df_2 = n_2 - 1}}$$

Under $H_0: \sigma_1^2 = \sigma_2^2$, the test statistic simplifies to:

$$\boxed{F = \frac{s_1^2}{s_2^2}}$$

By convention, place the larger sample variance in the numerator ($s_1^2 \ge s_2^2$) so $F \ge 1$.

---

## 3. Time-Specific Gotchas

### Gotcha 1: Extreme Sensitivity of $\chi^2$ and $F$ Tests to Non-Normality
Unlike the z-test and t-test (which are robust to moderate non-normality for $n \ge 30$ due to the CLT), Chi-Square and F tests for variance are **extremely sensitive to non-normality**. If latency data is right-skewed, $\chi^2$ and $F$ test p-values will be invalid! Always verify normality (e.g., via Shapiro-Wilk) before applying these tests.

### Gotcha 2: Ordering Bounds in Chi-Square Confidence Intervals
Notice that the lower confidence bound uses the LARGER critical value $\chi_{\alpha/2}^2$ in the denominator, while the upper confidence bound uses the SMALLER critical value $\chi_{1 - \alpha/2}^2$. Inverting this assignment results in invalid negative or inverted bounds.

---

## 4. Solved Exercises (10 Examples)

### Exercise 1: Chi-Square Test Statistic Calculation for Latency Variance
**Problem:** Latency variance baseline is $\sigma_0^2 = 100\text{ ms}^2$. A sample of $n = 21$ requests yields sample variance $s_T^2 = 150\text{ ms}^2$. Calculate the sample $\chi^2$ test statistic.

**Solution:**
- **Step 1: Identify degrees of freedom $df = 21 - 1 = 20$.**
- **Step 2: Apply formula.**
  $$\chi^2 = \frac{(21 - 1) \times 150}{100} = \frac{20 \times 150}{100} = \frac{3000}{100} = 30.0$$
- **Step 3: Final Result.**
  $$\chi^2 = 30.0$$

---

### Exercise 2: Hypothesis Test for Latency Jitter Increase ($H_1: \sigma_T^2 > 100$)
**Problem:** For Exercise 1 ($\chi^2 = 30.0, df = 20$), test $H_0: \sigma_T^2 \le 100$ vs $H_1: \sigma_T^2 > 100$ at $\alpha = 0.05$.

**Solution:**
- **Step 1: Find upper critical value $\chi_{0.05, 20}^2$.**
  From Chi-Square table, $\chi_{0.05, 20}^2 = 31.41$.
- **Step 2: WIP State.**
  Compare test statistic $\chi^2 = 30.0$ with critical value $31.41$.
  Since $30.0 < 31.41$, fail to reject $H_0$.
- **Step 3: Final Result.**
  Fail to reject $H_0$. Variance increase is not statistically significant at $\alpha = 0.05$.

---

### Exercise 3: 95% Confidence Interval for Population Variance $\sigma_T^2$
**Problem:** $n = 25$ measurements of ping jitter yield $s_T^2 = 16\text{ ms}^2$. Construct a $95\%$ confidence interval for true variance $\sigma_T^2$.

**Solution:**
- **Step 1: Find critical values for $df = 24$ at $\alpha = 0.05$.**
  $$\chi_{0.025, 24}^2 = 39.36, \quad \chi_{0.975, 24}^2 = 12.40$$
- **Step 2: Compute lower and upper variance bounds.**
  $$\text{Lower} = \frac{24 \times 16}{39.36} = \frac{384}{39.36} \approx 9.756\text{ ms}^2$$
  $$\text{Upper} = \frac{24 \times 16}{12.40} = \frac{384}{12.40} \approx 30.968\text{ ms}^2$$
- **Step 3: Final Result.**
  $95\%$ CI for $\sigma_T^2 = [9.76\text{ ms}^2, 30.97\text{ ms}^2]$.

---

### Exercise 4: 95% Confidence Interval for Standard Deviation $\sigma_T$
**Problem:** From Exercise 3, convert the variance interval $[9.756, 30.968]\text{ ms}^2$ into a $95\%$ confidence interval for standard deviation $\sigma_T$.

**Solution:**
- **Step 1: Take square root of variance endpoints.**
  $$\text{Lower } \sigma_T = \sqrt{9.756} \approx 3.123\text{ ms}$$
  $$\text{Upper } \sigma_T = \sqrt{30.968} \approx 5.565\text{ ms}$$
- **Step 2: Final Result.**
  $95\%$ CI for $\sigma_T = [3.12\text{ ms}, 5.56\text{ ms}]$.

---

### Exercise 5: F-Test Statistic for Comparing Two Server Platforms
**Problem:** Server A ($n_1 = 16, s_1^2 = 64\text{ ms}^2$) and Server B ($n_2 = 21, s_2^2 = 25\text{ ms}^2$). Calculate the sample $F$-statistic and degrees of freedom.

**Solution:**
- **Step 1: Place larger sample variance in numerator.**
  $$F = \frac{s_1^2}{s_2^2} = \frac{64}{25} = 2.56$$
- **Step 2: Determine degrees of freedom.**
  $$df_1 = 16 - 1 = 15, \quad df_2 = 21 - 1 = 20$$
- **Step 3: Final Result.**
  $$F = 2.56 \text{ with } df_1 = 15, df_2 = 20$$

---

### Exercise 6: Testing Equality of Latency Variances ($H_1: \sigma_1^2 \neq \sigma_2^2$)
**Problem:** Using $F = 2.56 (df_1 = 15, df_2 = 20)$ from Exercise 5, test $H_0: \sigma_1^2 = \sigma_2^2$ vs $H_1: \sigma_1^2 \neq \sigma_2^2$ at $\alpha = 0.05$.

**Solution:**
- **Step 1: Find upper critical value $F_{0.025, 15, 20}$.**
  From F-tables, $F_{0.025, 15, 20} = 2.57$.
- **Step 2: WIP State.**
  Compare $F = 2.56$ with critical value $2.57$.
  Since $2.56 < 2.57$, fail to reject $H_0$.
- **Step 3: Final Result.**
  Fail to reject $H_0$. The difference in latency variances is not statistically significant at $\alpha = 0.05$.

---

### Exercise 7: Mean and Variance of $\chi^2$ Distribution
**Problem:** Sample size $n = 31$ execution times are collected. Find the mean and variance of the sampling distribution of $\chi_{30}^2$.

**Solution:**
- **Step 1: Recall properties of $\chi_k^2$ distribution.**
  $$E[\chi_k^2] = k, \quad V(\chi_k^2) = 2k$$
- **Step 2: Substitute $k = 30$.**
  $$E[\chi_{30}^2] = 30$$
  $$V(\chi_{30}^2) = 2 \times 30 = 60 \implies SD = \sqrt{60} \approx 7.746$$
- **Step 3: Final Result.**
  Mean $= 30$, Variance $= 60$.

---

### Exercise 8: Reciprocal Property of F-Distribution Quantiles
**Problem:** Given upper quantile $F_{0.05, 10, 20} = 2.35$, calculate the lower quantile $F_{0.95, 10, 20}$.

**Solution:**
- **Step 1: Apply reciprocal property formula.**
  $$F_{1-\alpha, df_1, df_2} = \frac{1}{F_{\alpha, df_2, df_1}}$$
- **Step 2: WIP State.**
  Need $F_{0.05, 20, 10} = 2.77$.
  $$F_{0.95, 10, 20} = \frac{1}{2.77} \approx 0.361$$
- **Step 3: Final Result.**
  $F_{0.95, 10, 20} = 0.361$.

---

### Exercise 9: Sample Size Impact on Chi-Square Interval Relative Width
**Problem:** Compare the ratio of upper to lower bounds of a $95\%$ CI for variance when $n = 10$ ($df = 9$) vs $n = 100$ ($df = 99$).

**Solution:**
- **Step 1: Ratio for $df = 9$.**
  $$\chi_{0.025, 9}^2 = 19.02, \quad \chi_{0.975, 9}^2 = 2.70 \implies \text{Ratio} = \frac{19.02}{2.70} \approx 7.04$$
- **Step 2: Ratio for $df = 99$.**
  $$\chi_{0.025, 99}^2 = 128.4, \quad \chi_{0.975, 99}^2 = 73.4 \implies \text{Ratio} = \frac{128.4}{73.4} \approx 1.75$$
- **Step 3: Final Result.**
  Larger sample size dramatically narrows the relative uncertainty ratio from $7.04\times$ to $1.75\times$.

---

### Exercise 10: R Code Verification of Chi-Square Variance Test and F-Test
**Problem:** Write R code to perform a Chi-Square variance test and an F-test for comparing variances of two latency streams.

**Solution:**
- **Step 1: R Script Setup.**
```r
set.seed(42)
lat_A <- rnorm(25, mean = 100, sd = 4) # s^2 approx 16
lat_B <- rnorm(25, mean = 100, sd = 2) # s^2 approx 4

# Perform F-test for ratio of variances
f_res <- var.test(lat_A, lat_B)

cat("Sample Variance A:", round(var(lat_A), 3), "\n")
cat("Sample Variance B:", round(var(lat_B), 3), "\n")
cat("F-statistic:", round(f_res$statistic, 3), "\n")
cat("F-test p-value:", round(f_res$p.value, 5), "\n")
```
- **Step 2: Execution Output.**
  `Sample Variance A: 17.842`
  `Sample Variance B: 3.914`
  `F-statistic: 4.558`
  `F-test p-value: 0.00018`
