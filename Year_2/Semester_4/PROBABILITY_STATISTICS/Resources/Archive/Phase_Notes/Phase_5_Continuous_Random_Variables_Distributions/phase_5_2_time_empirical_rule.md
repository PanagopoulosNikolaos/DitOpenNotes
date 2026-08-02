# Phase 5.2 (Time): The Empirical Rule (68-95-99.7) for Time Data

The Empirical Rule (also known as the 3-Sigma Rule) provides quick estimates of the proportion of continuous observations falling within 1, 2, and 3 standard deviations of the mean for any bell-shaped, symmetric distribution. In time metrics—such as latency durations, manufacturing cycle times, and network round-trip times—the Empirical Rule acts as a baseline benchmark for SLA compliance and outlier detection.

---

## 1. Statement of the Empirical Rule for Time Data

If continuous time duration $T$ follows a symmetric, bell-shaped distribution with mean $\mu_T$ and standard deviation $\sigma_T$:

1. **68% Rule ($\pm 1\sigma_T$):** Approximately **68.27%** of all execution times fall within 1 standard deviation of the mean:
   $$\boxed{[\mu_T - \sigma_T, \mu_T + \sigma_T] \implies P(\mu_T - \sigma_T \le T \le \mu_T + \sigma_T) \approx 0.6827}$$

2. **95% Rule ($\pm 2\sigma_T$):** Approximately **95.45%** of all execution times fall within 2 standard deviations of the mean:
   $$\boxed{[\mu_T - 2\sigma_T, \mu_T + 2\sigma_T] \implies P(\mu_T - 2\sigma_T \le T \le \mu_T + 2\sigma_T) \approx 0.9545}$$

3. **99.7% Rule ($\pm 3\sigma_T$):** Approximately **99.73%** of all execution times fall within 3 standard deviations of the mean:
   $$\boxed{[\mu_T - 3\sigma_T, \mu_T + 3\sigma_T] \implies P(\mu_T - 3\sigma_T \le T \le \mu_T + 3\sigma_T) \approx 0.9973}$$

---

## 2. Symmetry and Tail Probabilities for Time Intervals

Because the distribution is symmetric about mean duration $\mu_T$, the outer tail probabilities outside the 3-sigma bands are halved:

| Region / Band | Inner Proportion | Total Outer Area | Single Tail Area |
| :--- | :--- | :--- | :--- |
| Outside $\mu_T \pm 1\sigma_T$ | $68.27\%$ | $31.73\%$ | $15.87\%$ (each side) |
| Outside $\mu_T \pm 2\sigma_T$ | $95.45\%$ | $4.55\%$ | $2.28\%$ (each side) |
| Outside $\mu_T \pm 3\sigma_T$ | $99.73\%$ | $0.27\%$ | $0.135\%$ (each side) |

---

## 3. Time-Specific Gotchas

### Gotcha 1: Applying the Empirical Rule to Skewed Time Distributions
Raw execution times (e.g., website load times, disk I/O latency) are often **right-skewed** (long tails due to sporadic spikes). Applying the 68-95-99.7 rule to strongly skewed distributions leads to inaccurate probabilities and negative lower bounds. Always verify symmetry (or log-transform the time data first) before using the Empirical Rule.

### Gotcha 2: Confusing Tail Areas ($T > \mu_T + 2\sigma_T$ vs $T < \mu_T - 2\sigma_T$)
In performance engineering, high latency ($T > \mu_T + 2\sigma_T$) represents a performance degradation, while low latency ($T < \mu_T - 2\sigma_T$) represents fast processing. Remember that the single upper tail for a $2\sigma_T$ bound contains $2.28\%$ of requests, NOT $4.55\%$.

---

## 4. Solved Exercises (10 Examples)

### Exercise 1: Computing 1-Sigma Time Interval
**Problem:** Server latency $T$ is symmetric and bell-shaped with mean $\mu_T = 150\text{ ms}$ and standard deviation $\sigma_T = 20\text{ ms}$. Estimate the interval containing $68\%$ of requests.

**Solution:**
- **Step 1: Apply 1-sigma bounds.**
  $$\text{Lower} = 150 - 20 = 130\text{ ms}$$
  $$\text{Upper} = 150 + 20 = 170\text{ ms}$$
- **Step 2: WIP State.**
  $$[\mu_T - \sigma_T, \mu_T + \sigma_T] = [130, 170]$$
- **Step 3: Final Result.**
  $68\%$ of request latencies lie between $130\text{ ms}$ and $170\text{ ms}$.

---

### Exercise 2: Upper Tail Slow Request Probability ($> 2\sigma_T$)
**Problem:** DB query duration $T$ has $\mu_T = 500\text{ ms}$ and $\sigma_T = 50\text{ ms}$. Estimate the percentage of queries taking longer than $600\text{ ms}$.

**Solution:**
- **Step 1: Express $600\text{ ms}$ in terms of $\sigma_T$.**
  $$600 = 500 + 2(50) = \mu_T + 2\sigma_T$$
- **Step 2: WIP State.**
  Total outside area for $\pm 2\sigma_T = 100\% - 95.45\% = 4.55\%$.
  Upper tail area = $4.55\% / 2 = ?$
- **Step 3: Final Result.**
  $$P(T > 600) \approx 2.28\%$$

---

### Exercise 3: 3-Sigma Anomaly Detection Limit
**Problem:** Packet transit time has $\mu_T = 40\text{ ms}$ and $\sigma_T = 6\text{ ms}$. Packets taking longer than $\mu_T + 3\sigma_T$ are flagged as anomalous. Calculate this threshold.

**Solution:**
- **Step 1: Compute $3\sigma_T$ bound.**
  $$\text{Threshold} = 40 + 3(6) = 40 + 18$$
- **Step 2: WIP State.**
  $$\text{Threshold} = 58\text{ ms}$$
- **Step 3: Final Result.**
  Packets exceeding $58\text{ ms}$ are flagged. Only approx $0.135\%$ of normal packets exceed this duration.

---

### Exercise 4: Number of Outlier Requests out of 10,000
**Problem:** In a sample of $10{,}000$ web requests with symmetric bell-shaped duration ($\mu_T = 2\text{ s}, \sigma_T = 0.3\text{ s}$), how many requests are expected to fall outside $[1.1\text{ s}, 2.9\text{ s}]$?

**Solution:**
- **Step 1: Convert bounds to standard deviations.**
  $$1.1 = 2 - 3(0.3) = \mu_T - 3\sigma_T$$
  $$2.9 = 2 + 3(0.3) = \mu_T + 3\sigma_T$$
- **Step 2: WIP State.**
  Proportion inside bounds $= 99.73\%$.
  Proportion outside bounds $= 100\% - 99.73\% = 0.27\% = 0.0027$.
- **Step 3: Final Result.**
  $$\text{Expected count} = 10{,}000 \times 0.0027 = 27 \text{ requests}$$

---

### Exercise 5: Probability of Duration Between $\mu_T$ and $\mu_T + 1\sigma_T$
**Problem:** Execution time $T$ is bell-shaped with mean $100\text{ ms}$ and $\sigma_T = 15\text{ ms}$. Find $P(100 \le T \le 115)$.

**Solution:**
- **Step 1: Identify interval position relative to mean.**
  Interval $[100, 115]$ represents $[\mu_T, \mu_T + 1\sigma_T]$.
- **Step 2: WIP State.**
  Total area in $[\mu_T - 1\sigma_T, \mu_T + 1\sigma_T] = 68.27\%$.
  By symmetry around mean, half of this area lies in $[\mu_T, \mu_T + 1\sigma_T]$.
  $$\text{Area} = 68.27\% / 2 = ?$$
- **Step 3: Final Result.**
  $$P(100 \le T \le 115) \approx 34.14\%$$

---

### Exercise 6: Asymmetric Duration Window ($[\mu_T - 1\sigma_T, \mu_T + 2\sigma_T]$)
**Problem:** Batch processing time $T$ has $\mu_T = 12\text{ hours}$ and $\sigma_T = 2\text{ hours}$. Estimate $P(10\text{ h} \le T \le 16\text{ h})$.

**Solution:**
- **Step 1: Decompose interval at the mean $\mu_T = 12$.**
  $$\text{Left half: } [10, 12] = [\mu_T - 1\sigma_T, \mu_T]$$
  $$\text{Right half: } [12, 16] = [\mu_T, \mu_T + 2\sigma_T]$$
- **Step 2: WIP State.**
  Left area $= 68.27\% / 2 = 34.135\%$
  Right area $= 95.45\% / 2 = 47.725\%$
  $$\text{Total probability} = 34.135\% + 47.725\% = ?$$
- **Step 3: Final Result.**
  $$P(10 \le T \le 16) \approx 81.86\%$$

---

### Exercise 7: Fast Requests Probability ($T < \mu_T - 1\sigma_T$)
**Problem:** Build duration $T$ has mean $30\text{ min}$ and $\sigma_T = 4\text{ min}$. What percentage of builds complete in less than $26\text{ min}$?

**Solution:**
- **Step 1: Express $26\text{ min}$ in terms of $\sigma_T$.**
  $$26 = 30 - 1(4) = \mu_T - 1\sigma_T$$
- **Step 2: WIP State.**
  Lower tail area $= (100\% - 68.27\%) / 2 = 31.73\% / 2 = ?$
- **Step 3: Final Result.**
  $$P(T < 26) \approx 15.87\%$$

---

### Exercise 8: Detecting Violation of Symmetry / Empirical Rule
**Problem:** Measured processing times $T$ have $\mu_T = 10\text{ ms}$ and $\sigma_T = 6\text{ ms}$. If $T$ were normal, what lower bound would correspond to $\mu_T - 2\sigma_T$? Is the empirical rule applicable?

**Solution:**
- **Step 1: Compute lower bound.**
  $$\mu_T - 2\sigma_T = 10 - 2(6) = -2\text{ ms}$$
- **Step 2: Evaluate physical validity.**
  Physical time $T$ cannot be negative ($T \ge 0$).
- **Step 3: Final Result.**
  Because $\mu_T - 2\sigma_T < 0$, the time metric is strongly right-skewed. The standard normal Empirical Rule is not directly applicable to un-transformed data.

---

### Exercise 9: Interval Containing 95% symmetrical SLAs
**Problem:** Disk write time $T$ has $\mu_T = 8\text{ ms}$ and $\sigma_T = 1\text{ ms}$. Find the range of disk write times that covers $95.45\%$ of all writes.

**Solution:**
- **Step 1: Apply 2-sigma rule.**
  $$\text{Range} = [\mu_T - 2\sigma_T, \mu_T + 2\sigma_T] = [8 - 2(1), 8 + 2(1)]$$
- **Step 2: WIP State.**
  $$\text{Range} = [6\text{ ms}, 10\text{ ms}]$$
- **Step 3: Final Result.**
  $95.45\%$ of writes occur between $6\text{ ms}$ and $10\text{ ms}$.

---

### Exercise 10: Verification in R
**Problem:** Write R code to simulate $100{,}000$ normal latency metrics ($\mu_T = 100$, $\sigma_T = 15$) and verify the Empirical Rule proportions.

**Solution:**
- **Step 1: R Script Setup.**
```r
set.seed(42)
mu_t <- 100
sd_t <- 15
t_sim <- rnorm(100000, mean = mu_t, sd = sd_t)

# Calculate empirical proportions
p1 <- mean(t_sim >= (mu_t - sd_t) & t_sim <= (mu_t + sd_t))
p2 <- mean(t_sim >= (mu_t - 2*sd_t) & t_sim <= (mu_t + 2*sd_t))
p3 <- mean(t_sim >= (mu_t - 3*sd_t) & t_sim <= (mu_t + 3*sd_t))

cat("Within 1 SD:", round(p1 * 100, 2), "%\n")
cat("Within 2 SD:", round(p2 * 100, 2), "%\n")
cat("Within 3 SD:", round(p3 * 100, 2), "%\n")
```
- **Step 2: Execution Output.**
  `Within 1 SD: 68.25 %`
  `Within 2 SD: 95.44 %`
  `Within 3 SD: 99.74 %`
