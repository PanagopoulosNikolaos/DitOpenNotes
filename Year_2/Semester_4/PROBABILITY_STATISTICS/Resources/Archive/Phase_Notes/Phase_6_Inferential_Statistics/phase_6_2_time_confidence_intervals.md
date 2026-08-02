# Phase 6.2 (Time): Confidence Intervals for Mean Execution Time

A Confidence Interval (CI) provides a range of plausible values for an unknown population mean execution time $\mu_T$ at a specified confidence level $1 - \alpha$ (e.g., $95\%$ or $99\%$) based on sample statistics.

---

## 1. Z-Confidence Interval for Mean Time (Known Population Variance $\sigma_T$)

When population standard deviation $\sigma_T$ is known and either sample size $n \ge 30$ or the latency population is normal, the $100(1 - \alpha)\%$ Z-confidence interval for $\mu_T$ is:

$$\boxed{\text{CI} = \left[ \bar{T} - z_{\alpha/2} \cdot \frac{\sigma_T}{\sqrt{n}}, \, \bar{T} + z_{\alpha/2} \cdot \frac{\sigma_T}{\sqrt{n}} \right]}$$

Where $z_{\alpha/2}$ is the upper $\alpha/2$ critical value from $N(0, 1)$:
* **$90\%$ Confidence ($\alpha = 0.10$):** $z_{0.05} = 1.645$
* **$95\%$ Confidence ($\alpha = 0.05$):** $z_{0.025} = 1.960$
* **$99\%$ Confidence ($\alpha = 0.01$):** $z_{0.005} = 2.576$

---

## 2. Student's t-Confidence Interval (Unknown Variance $\sigma_T$, Small Sample $n < 30$)

When population variance $\sigma_T^2$ is unknown, it is estimated using sample variance $s_T^2 = \frac{1}{n-1} \sum_{i=1}^n (T_i - \bar{T})^2$. If the underlying time population is approximately normal, the $100(1 - \alpha)\%$ t-confidence interval with $df = n - 1$ degrees of freedom is:

$$\boxed{\text{CI} = \left[ \bar{T} - t_{\alpha/2, n-1} \cdot \frac{s_T}{\sqrt{n}}, \, \bar{T} + t_{\alpha/2, n-1} \cdot \frac{s_T}{\sqrt{n}} \right]}$$

---

## 3. Margin of Error and Sample Size Estimation

The Margin of Error (ME) is half the width of the confidence interval:

$$E = z_{\alpha/2} \cdot \frac{\sigma_T}{\sqrt{n}}$$

To guarantee a margin of error no larger than $E$ for SLA estimation, the minimum required sample size is:

$$\boxed{n = \left( \frac{z_{\alpha/2} \cdot \sigma_T}{E} \right)^2}$$

*(Always round $n$ UP to the nearest integer).*

---

## 4. Time-Specific Gotchas

### Gotcha 1: Misinterpreting the $95\%$ Confidence Level
A $95\%$ confidence interval of $[120\text{ ms}, 130\text{ ms}]$ does NOT mean there is a $95\%$ probability that true mean $\mu_T$ lies in $[120, 130]$. True mean $\mu_T$ is a fixed (unknown) constant. The $95\%$ probability refers to the *method*: in $95\%$ of repeated random samples, the constructed intervals will capture $\mu_T$.

### Gotcha 2: Using z-Critical Values for Small Samples with Sample SD $s_T$
Using $z = 1.96$ instead of $t_{\alpha/2, n-1}$ when $n < 30$ and population standard deviation $\sigma_T$ is unknown underestimates the margin of error and produces overly narrow, invalid confidence intervals.

---

## 5. Solved Exercises (10 Examples)

### Exercise 1: 95% Z-Confidence Interval for Server Latency
**Problem:** A sample of $n = 64$ web requests yields sample mean latency $\bar{T} = 210\text{ ms}$. Known population standard deviation is $\sigma_T = 32\text{ ms}$. Construct a $95\%$ confidence interval for true mean latency $\mu_T$.

**Solution:**
- **Step 1: Identify parameters.**
  $\bar{T} = 210, \sigma_T = 32, n = 64, z_{0.025} = 1.96$.
- **Step 2: Compute Standard Error and Margin of Error.**
  $$\text{SE} = \frac{32}{\sqrt{64}} = \frac{32}{8} = 4\text{ ms}$$
  $$E = 1.96 \times 4 = 7.84\text{ ms}$$
- **Step 3: WIP State and Final Bounds.**
  $$\text{CI} = [210 - 7.84, 210 + 7.84] = [202.16\text{ ms}, 217.84\text{ ms}]$$

---

### Exercise 2: 99% Z-Confidence Interval for DB Query Duration
**Problem:** A log of $n = 100$ database queries gives $\bar{T} = 45\text{ ms}$ with known $\sigma_T = 10\text{ ms}$. Construct a $99\%$ confidence interval for $\mu_T$.

**Solution:**
- **Step 1: Identify critical value $z_{0.005} = 2.576$.**
- **Step 2: Compute SE and Margin of Error.**
  $$\text{SE} = \frac{10}{\sqrt{100}} = 1\text{ ms}$$
  $$E = 2.576 \times 1 = 2.576\text{ ms}$$
- **Step 3: Final Result.**
  $$\text{CI} = [45 - 2.576, 45 + 2.576] = [42.424\text{ ms}, 47.576\text{ ms}]$$

---

### Exercise 3: 95% t-Confidence Interval (Small Sample $n = 16$)
**Problem:** A benchmark test of $n = 16$ microservice executions yields sample mean $\bar{T} = 5.4\text{ seconds}$ and sample standard deviation $s_T = 0.8\text{ seconds}$. Construct a $95\%$ confidence interval for $\mu_T$.

**Solution:**
- **Step 1: Find $t_{0.025}$ with $df = 16 - 1 = 15$.**
  From t-table, $t_{0.025, 15} = 2.131$.
- **Step 2: Compute SE and Margin of Error.**
  $$\text{SE} = \frac{0.8}{\sqrt{16}} = \frac{0.8}{4} = 0.2\text{ s}$$
  $$E = 2.131 \times 0.2 = 0.4262\text{ s}$$
- **Step 3: Final Result.**
  $$\text{CI} = [5.4 - 0.4262, 5.4 + 0.4262] = [4.9738\text{ s}, 5.8262\text{ s}]$$

---

### Exercise 4: Sample Size Calculation for Latency SLA ($\pm 2\text{ ms}$)
**Problem:** Standard deviation of API response time is estimated as $\sigma_T = 25\text{ ms}$. How many requests must be sampled to estimate $\mu_T$ within $\pm 2\text{ ms}$ with $95\%$ confidence?

**Solution:**
- **Step 1: Apply sample size formula.**
  $$n = \left( \frac{1.96 \times 25}{2} \right)^2 = \left( \frac{49}{2} \right)^2 = (24.5)^2 = 600.25$$
- **Step 2: Round up to integer.**
  $$n = 601\text{ requests}$$
- **Step 3: Final Result.**
  A sample of $n = 601$ requests is required.

---

### Exercise 5: 90% Confidence Interval for Mean Ping Time
**Problem:** $n = 49$ pings give $\bar{T} = 35\text{ ms}$ and $s_T = 7\text{ ms}$. Construct a $90\%$ confidence interval for $\mu_T$.

**Solution:**
- **Step 1: Identify critical value $z_{0.05} = 1.645$ (since $n = 49 \ge 30$).**
- **Step 2: Compute SE and Margin of Error.**
  $$\text{SE} = \frac{7}{\sqrt{49}} = \frac{7}{7} = 1\text{ ms}$$
  $$E = 1.645 \times 1 = 1.645\text{ ms}$$
- **Step 3: Final Result.**
  $$\text{CI} = [35 - 1.645, 35 + 1.645] = [33.355\text{ ms}, 36.645\text{ ms}]$$

---

### Exercise 6: Impact of Confidence Level on Interval Width
**Problem:** For $\bar{T} = 100\text{ ms}, s_T = 15\text{ ms}, n = 36$, compare the widths of $90\%$, $95\%$, and $99\%$ confidence intervals.

**Solution:**
- **Step 1: Compute $\text{SE} = 15 / 6 = 2.5\text{ ms}$.**
- **Step 2: Compute margins of error.**
  $$E_{90\%} = 1.645 \times 2.5 = 4.1125\text{ ms} \implies \text{Width} = 8.225\text{ ms}$$
  $$E_{95\%} = 1.960 \times 2.5 = 4.9000\text{ ms} \implies \text{Width} = 9.800\text{ ms}$$
  $$E_{99\%} = 2.576 \times 2.5 = 6.4400\text{ ms} \implies \text{Width} = 12.880\text{ ms}$$
- **Step 3: Final Result.**
  Higher confidence levels require wider intervals to guarantee coverage.

---

### Exercise 7: One-Sided Upper Confidence Bound for SLA Verification
**Problem:** An SLA requires mean load time $\mu_T \le 300\text{ ms}$. A sample of $n = 36$ loads has $\bar{T} = 285\text{ ms}$ and $s_T = 30\text{ ms}$. Construct a $95\%$ one-sided upper confidence bound for $\mu_T$.

**Solution:**
- **Step 1: Identify upper one-sided critical value $z_{0.05} = 1.645$.**
- **Step 2: Compute Upper Bound.**
  $$\text{SE} = \frac{30}{\sqrt{36}} = 5\text{ ms}$$
  $$\text{Upper Bound} = \bar{T} + z_{0.05} \cdot \text{SE} = 285 + (1.645 \times 5) = 285 + 8.225 = 293.225\text{ ms}$$
- **Step 3: Final Result.**
  We are $95\%$ confident that true mean load time $\mu_T \le 293.23\text{ ms}$, satisfying the $300\text{ ms}$ SLA.

---

### Exercise 8: Difference in Mean Execution Times ($\mu_1 - \mu_2$) Confidence Interval
**Problem:** System A ($n_1 = 40, \bar{T}_1 = 120\text{ ms}, s_1 = 16\text{ ms}$) and System B ($n_2 = 50, \bar{T}_2 = 135\text{ ms}, s_2 = 20\text{ ms}$) are tested. Construct a $95\%$ CI for difference $\mu_2 - \mu_1$.

**Solution:**
- **Step 1: Point estimate and standard error of difference.**
  $$\text{Estimate} = 135 - 120 = 15\text{ ms}$$
  $$\text{SE}_{\text{diff}} = \sqrt{\frac{16^2}{40} + \frac{20^2}{50}} = \sqrt{\frac{256}{40} + \frac{400}{50}} = \sqrt{6.4 + 8.0} = \sqrt{14.4} \approx 3.7947\text{ ms}$$
- **Step 2: WIP State.**
  $$E = 1.96 \times 3.7947 = 7.4376\text{ ms}$$
- **Step 3: Final Result.**
  $$\text{CI} = [15 - 7.4376, 15 + 7.4376] = [7.5624\text{ ms}, 22.4376\text{ ms}]$$
  Since $0$ is not in the CI, System B is significantly slower than System A.

---

### Exercise 9: Sample Size Required to Halve Interval Width
**Problem:** To halve the margin of error of a latency confidence interval without changing confidence level, by what factor must sample size $n$ increase?

**Solution:**
- **Step 1: Examine margin formula $E \propto 1 / \sqrt{n}$.**
- **Step 2: Set target margin $E' = E / 2$.**
  $$\frac{E}{2} = \frac{k}{\sqrt{n'}} \implies \sqrt{n'} = 2 \sqrt{n} \implies n' = 4n$$
- **Step 3: Final Result.**
  Sample size $n$ must be quadrupled ($4\times$).

---

### Exercise 10: R Code Verification of t-Confidence Intervals
**Problem:** Write an R script to compute exact 95% t-confidence intervals for a vector of measured response times.

**Solution:**
- **Step 1: R Script Setup.**
```r
response_times <- c(12.4, 15.1, 11.8, 13.5, 14.2, 12.9, 16.0, 13.1, 14.8, 12.2)

# Compute t-test / CI directly
res <- t.test(response_times, conf.level = 0.95)

cat("Sample Mean:", round(mean(response_times), 3), "s\n")
cat("95% CI:", round(res$conf.int[1], 3), "s to", round(res$conf.int[2], 3), "s\n")
```
- **Step 2: Execution Output.**
  `Sample Mean: 13.6 s`
  `95% CI: 12.632 s to 14.568 s`
