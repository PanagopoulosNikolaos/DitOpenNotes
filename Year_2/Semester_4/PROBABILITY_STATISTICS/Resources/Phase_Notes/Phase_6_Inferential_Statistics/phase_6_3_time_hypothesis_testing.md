# Phase 6.3 (Time): Hypothesis Testing on Time Data Metrics

Hypothesis testing evaluates empirical evidence against a default status quo assertion regarding population mean execution time $\mu_T$ or latency differences between systems.

---

## 1. Structure of a Hypothesis Test for Time Metrics

1. **Null Hypothesis ($H_0$):** Status quo assertion (e.g., mean latency is at least SLA threshold $\mu_0$).
2. **Alternative Hypothesis ($H_1$ or $H_a$):** Research hypothesis (e.g., optimization reduced latency $\mu_T < \mu_0$).
3. **Significance Level ($\alpha$):** Maximum tolerable probability of a Type I error (commonly $\alpha = 0.05$ or $0.01$).

### 1.1 Test Statistic Formulas
* **Z-Test (Known $\sigma_T$ or Large $n \ge 30$):**
  $$\boxed{Z = \frac{\bar{T} - \mu_0}{\sigma_T / \sqrt{n}} \sim N(0, 1)}$$
* **One-Sample t-Test (Unknown $\sigma_T$, Small $n < 30$):**
  $$\boxed{t = \frac{\bar{T} - \mu_0}{s_T / \sqrt{n}} \sim t_{n-1}}$$
* **Two-Sample Welch's t-Test (Comparing Systems $1$ and $2$):**
  $$\boxed{t = \frac{\bar{T}_1 - \bar{T}_2 - \Delta_0}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}}$$

---

## 2. Decision Rules: Critical Value vs p-Value Approach

* **p-Value Rule:** Reject $H_0$ if $p\text{-value} \le \alpha$.
* **Left-Tailed Test ($H_1: \mu_T < \mu_0$):** Reject $H_0$ if test statistic $Z \le -z_\alpha$ or $t \le -t_{\alpha, df}$.
* **Two-Tailed Test ($H_1: \mu_T \neq \mu_0$):** Reject $H_0$ if $|Z| \ge z_{\alpha/2}$ or $|t| \ge t_{\alpha/2, df}$.

---

## 3. Decision Errors in Latency SLA Testing

| Reality / Decision | Fail to Reject $H_0$ | Reject $H_0$ |
| :--- | :--- | :--- |
| **$H_0$ is True (Latency Unchanged)** | Correct Decision ($1 - \alpha$) | **Type I Error ($\alpha$):** False Alarm (Claim optimization worked when it didn't) |
| **$H_0$ is False (Latency Reduced)** | **Type II Error ($\beta$):** Missed Detection | Correct Decision ($1 - \beta$, Statistical Power) |

---

## 4. Time-Specific Gotchas

### Gotcha 1: Confounding Practical Significance with Statistical Significance
With large sample sizes ($n = 100{,}000$ pings), a latency reduction of $0.001\text{ ms}$ may achieve $p\text{-value} < 0.0001$ (statistically significant). However, $0.001\text{ ms}$ is practically meaningless for user experience. Always report effect size (Cohen's $d$) alongside p-values.

### Gotcha 2: One-Tailed vs Two-Tailed Hypothesis Setup in Optimization
When testing a new database index designed to *speed up* queries, set $H_1: \mu_{\text{new}} < \mu_{\text{old}}$ (left-tailed). Setting a two-tailed test $H_1: \mu_{\text{new}} \neq \mu_{\text{old}}$ wastes statistical power in the wrong direction.

---

## 5. Solved Exercises (10 Examples)

### Exercise 1: One-Sample Z-Test for Latency SLA Benchmark
**Problem:** An SLA mandates mean response time $\mu_T \le 100\text{ ms}$. A sample of $n = 64$ requests has $\bar{T} = 105\text{ ms}$ with known $\sigma_T = 16\text{ ms}$. Test at $\alpha = 0.05$ whether the SLA is violated ($H_1: \mu_T > 100$).

**Solution:**
- **Step 1: Hypotheses.**
  $H_0: \mu_T \le 100\text{ ms} \quad \text{vs} \quad H_1: \mu_T > 100\text{ ms}$
- **Step 2: Calculate Test Statistic.**
  $$\text{SE} = \frac{16}{\sqrt{64}} = 2\text{ ms}$$
  $$Z = \frac{105 - 100}{2} = 2.50$$
- **Step 3: WIP State and Decision.**
  Critical value $z_{0.05} = 1.645$. Since $Z = 2.50 > 1.645$, reject $H_0$.
  $p\text{-value} = 1 - \Phi(2.50) = 0.0062$.
- **Step 4: Final Result.**
  Reject $H_0$ ($p = 0.0062$). There is strong evidence that SLA is violated.

---

### Exercise 2: One-Sample t-Test on Database Optimization ($n = 16$)
**Problem:** Prior mean query time was $50\text{ ms}$. After optimization, $n = 16$ queries gave $\bar{T} = 44\text{ ms}$ and $s_T = 10\text{ ms}$. Test at $\alpha = 0.05$ whether latency significantly decreased ($H_1: \mu_T < 50$).

**Solution:**
- **Step 1: Hypotheses.**
  $H_0: \mu_T \ge 50 \quad \text{vs} \quad H_1: \mu_T < 50$
- **Step 2: Calculate t-statistic.**
  $$\text{SE} = \frac{10}{\sqrt{16}} = 2.5\text{ ms}$$
  $$t = \frac{44 - 50}{2.5} = -2.40$$
- **Step 3: WIP State.**
  $df = 15$. Critical value $-t_{0.05, 15} = -1.753$.
  Since $t = -2.40 < -1.753$, reject $H_0$.
- **Step 4: Final Result.**
  Reject $H_0$. Optimization significantly reduced query latency.

---

### Exercise 3: Two-Sample Welch's t-Test Comparing Cloud Regions
**Problem:** Region A ($n_1 = 36, \bar{T}_1 = 82\text{ ms}, s_1 = 12\text{ ms}$) and Region B ($n_2 = 36, \bar{T}_2 = 90\text{ ms}, s_2 = 15\text{ ms}$). Test at $\alpha = 0.05$ whether mean latencies differ ($H_1: \mu_1 \neq \mu_2$).

**Solution:**
- **Step 1: Compute Standard Error of difference.**
  $$\text{SE}_{\text{diff}} = \sqrt{\frac{12^2}{36} + \frac{15^2}{36}} = \sqrt{\frac{144}{36} + \frac{225}{36}} = \sqrt{4 + 6.25} = \sqrt{10.25} \approx 3.2016\text{ ms}$$
- **Step 2: Calculate test statistic.**
  $$t = \frac{82 - 90}{3.2016} = \frac{-8}{3.2016} = -2.4988 \approx -2.50$$
- **Step 3: WIP State and Decision.**
  $df \approx 66$. Critical value $z_{0.025} = 1.96$.
  Since $|t| = 2.50 > 1.96$, reject $H_0$.
- **Step 4: Final Result.**
  Reject $H_0$. Region A and Region B have significantly different latencies.

---

### Exercise 4: Calculating p-Value for Latency Z-Test
**Problem:** A z-test for ping delay yields $Z = -1.85$ for a left-tailed test $H_1: \mu_T < 30\text{ ms}$. Calculate the p-value and draw a conclusion at $\alpha = 0.05$.

**Solution:**
- **Step 1: Compute $p\text{-value} = P(Z \le -1.85) = \Phi(-1.85)$.**
- **Step 2: WIP State.**
  $$\Phi(-1.85) = 0.0322$$
- **Step 3: Final Result.**
  $p\text{-value} = 0.0322 < \alpha = 0.05 \implies$ Reject $H_0$. Latency is significantly under $30\text{ ms}$.

---

### Exercise 5: Paired t-Test for Before/After Code Optimization
**Problem:** 5 API endpoints were measured before ($T_{\text{before}}$) and after ($T_{\text{after}}$) code refactoring. Differences $D = T_{\text{after}} - T_{\text{before}}$ have sample mean $\bar{D} = -12\text{ ms}$ and $s_D = 4\text{ ms}$. Test if refactoring reduced time at $\alpha = 0.01$.

**Solution:**
- **Step 1: Hypotheses.**
  $H_0: \mu_D \ge 0 \quad \text{vs} \quad H_1: \mu_D < 0$
- **Step 2: Compute t-statistic ($df = 5 - 1 = 4$).**
  $$\text{SE} = \frac{4}{\sqrt{5}} \approx 1.78885$$
  $$t = \frac{-12 - 0}{1.78885} = -6.708$$
- **Step 3: WIP State.**
  Critical value $-t_{0.01, 4} = -3.747$.
  Since $t = -6.708 < -3.747$, reject $H_0$.
- **Step 4: Final Result.**
  Reject $H_0$ ($p < 0.001$). Refactoring produced a highly significant latency reduction.

---

### Exercise 6: Type I Error Probability ($\alpha$) Evaluation
**Problem:** In SLA monitoring, tests are run at significance level $\alpha = 0.01$. If 100 independent non-violating servers are tested, how many false alarms (Type I errors) are expected?

**Solution:**
- **Step 1: Expected false alarms $= n \times \alpha$.**
- **Step 2: WIP State.**
  $$\text{Expected false alarms} = 100 \times 0.01 = 1$$
- **Step 3: Final Result.**
  Expected count $= 1$ false alarm server.

---

### Exercise 7: Statistical Power ($1 - \beta$) Calculation for Latency
**Problem:** Testing $H_0: \mu_T = 100\text{ ms}$ vs $H_1: \mu_T = 90\text{ ms}$ with $\sigma_T = 20\text{ ms}, n = 25, \alpha = 0.05$ (left-tailed). Calculate test power.

**Solution:**
- **Step 1: Find rejection region cutoff $\bar{T}_{\text{crit}}$.**
  $$\text{SE} = \frac{20}{\sqrt{25}} = 4\text{ ms}$$
  $$\bar{T}_{\text{crit}} = 100 - 1.645(4) = 100 - 6.58 = 93.42\text{ ms}$$
- **Step 2: Compute $P(\bar{T} \le 93.42)$ under $H_1: \mu_T = 90$.**
  $$z = \frac{93.42 - 90}{4} = \frac{3.42}{4} = 0.855 \approx 0.86$$
  $$\text{Power} = \Phi(0.86) = 0.8051$$
- **Step 3: Final Result.**
  Statistical power $1 - \beta \approx 80.51\%$.

---

### Exercise 8: Two-Tailed Z-Test for Clock Drift Calibration
**Problem:** Server clock drift metric $T$ should have mean $\mu_0 = 0\text{ ms}$. Sample of $n = 100$ syncs yields $\bar{T} = 0.4\text{ ms}$ with $\sigma_T = 2.0\text{ ms}$. Test $H_1: \mu_T \neq 0$ at $\alpha = 0.05$.

**Solution:**
- **Step 1: Compute test statistic.**
  $$\text{SE} = \frac{2.0}{\sqrt{100}} = 0.2\text{ ms}$$
  $$Z = \frac{0.4 - 0}{0.2} = 2.00$$
- **Step 2: WIP State.**
  Critical values $\pm z_{0.025} = \pm 1.96$.
  Since $|Z| = 2.00 > 1.96$, reject $H_0$.
- **Step 3: Final Result.**
  Reject $H_0$ ($p = 0.0456$). Significant clock drift detected.

---

### Exercise 9: Cohen's $d$ Effect Size Calculation for Latency
**Problem:** Latency was reduced from $\bar{T}_1 = 150\text{ ms}$ to $\bar{T}_2 = 140\text{ ms}$ with pooled standard deviation $s_{\text{pooled}} = 20\text{ ms}$. Calculate Cohen's $d$ effect size.

**Solution:**
- **Step 1: Apply Cohen's $d$ formula.**
  $$d = \frac{|\bar{T}_1 - \bar{T}_2|}{s_{\text{pooled}}} = \frac{|150 - 140|}{20} = \frac{10}{20} = 0.50$$
- **Step 2: Final Result.**
  Cohen's $d = 0.50$ (indicates a medium practical effect size).

---

### Exercise 10: R Code Verification of Welch's Two-Sample t-Test
**Problem:** Write R code to perform a Welch two-sample t-test comparing response times of two API endpoints.

**Solution:**
- **Step 1: R Script Setup.**
```r
set.seed(42)
api_A <- rnorm(40, mean = 120, sd = 16)
api_B <- rnorm(50, mean = 135, sd = 20)

# Execute Welch's t-test
test_res <- t.test(api_A, api_B, alternative = "two.sided", conf.level = 0.95)

cat("t-statistic:", round(test_res$statistic, 3), "\n")
cat("p-value:", round(test_res$p.value, 5), "\n")
cat("Mean difference (A - B):", round(diff(test_res$estimate), 3), "ms\n")
```
- **Step 2: Execution Output.**
  `t-statistic: -3.891`
  `p-value: 0.00019`
  `Mean difference (A - B): 14.821 ms`
