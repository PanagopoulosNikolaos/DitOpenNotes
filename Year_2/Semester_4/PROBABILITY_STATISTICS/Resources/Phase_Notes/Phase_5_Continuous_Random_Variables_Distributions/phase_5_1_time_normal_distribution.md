# Phase 5.1 (Time): Normal Distribution in Continuous Time Metrics

The Normal (Gaussian) Distribution is a continuous probability distribution defined by a bell-shaped probability density function (PDF). In time-series analysis and performance engineering, continuous time metrics—such as network latency, execution duration, system uptime, and server response times—frequently follow or are modeled by the Normal distribution when governed by numerous additive, independent delay components.

---

## 1. Mathematical Foundation of the Normal Distribution

A continuous random variable $T$ representing a time metric (e.g., duration in milliseconds) follows a Normal distribution with mean parameter $\mu_T \in (-\infty, \infty)$ and variance parameter $\sigma_T^2 > 0$, denoted as $T \sim N(\mu_T, \sigma_T^2)$.

### 1.1 Probability Density Function (PDF)
The probability density function $f_T(t)$ for execution time $t$ is:

$$\boxed{f_T(t) = \frac{1}{\sigma_T \sqrt{2\pi}} \exp\left( -\frac{(t - \mu_T)^2}{2\sigma_T^2} \right), \quad -\infty < t < \infty}$$

Where:
* $\mu_T$ is the mean execution time (center of the duration density).
* $\sigma_T$ is the standard deviation of latency (spread/jitter).
* $\pi \approx 3.14159$ and $e \approx 2.71828$.

### 1.2 Cumulative Distribution Function (CDF) and Standard Normal Transformation
The probability that execution time $T$ does not exceed a threshold duration $t$ is:

$$F_T(t) = P(T \le t) = \int_{-\infty}^{t} \frac{1}{\sigma_T \sqrt{2\pi}} \exp\left( -\frac{(u - \mu_T)^2}{2\sigma_T^2} \right) du$$

Because this integral has no closed-form elementary solution, any time random variable $T \sim N(\mu_T, \sigma_T^2)$ is standardized to the Standard Normal variable $Z \sim N(0, 1)$ via:

$$\boxed{Z = \frac{T - \mu_T}{\sigma_T}}$$

The standardized probability is expressed using the Standard Normal CDF $\Phi(z)$:

$$P(T \le t) = P\left(Z \le \frac{t - \mu_T}{\sigma_T}\right) = \Phi(z)$$

---

## 2. Key Properties of Continuous Time Normal RVs

1. **Symmetry:** The density curve is symmetric around $t = \mu_T$. $P(T \le \mu_T) = P(T \ge \mu_T) = 0.5$.
2. **Linear Transformation:** If $T \sim N(\mu_T, \sigma_T^2)$ is scaled by a constant factor $a$ (e.g., converting seconds to milliseconds via $a = 1000$) and shifted by $b$, then:
   $$Y = aT + b \sim N(a\mu_T + b, a^2 \sigma_T^2)$$
3. **Probability of Exact Points:** For any continuous RV $T$, $P(T = t) = 0$ for any specific timestamp $t$. Probabilities are non-zero only over duration intervals $[t_1, t_2]$.

---

## 3. Time-Specific Gotchas

### Gotcha 1: Negative Time Values from Theoretical Bounds
The mathematical domain of $N(\mu_T, \sigma_T^2)$ spans $(-\infty, \infty)$. Physical execution time $T$ cannot be negative ($T \ge 0$). When $\mu_T < 3\sigma_T$, the model assigns non-negligible probability to $T < 0$. Always verify that $\mu_T \ge 3\sigma_T$ or use a truncated Normal / Log-Normal model.

### Gotcha 2: Scaling Variance vs Standard Deviation for Time Units
When converting time units (e.g., seconds to milliseconds, $a = 1000$):
* Mean scales linearly: $\mu_{\text{ms}} = 1000 \cdot \mu_{\text{sec}}$
* Standard deviation scales linearly: $\sigma_{\text{ms}} = 1000 \cdot \sigma_{\text{sec}}$
* **Variance scales quadratically:** $\sigma_{\text{ms}}^2 = 1000^2 \cdot \sigma_{\text{sec}}^2 = 1{,}000{,}000 \cdot \sigma_{\text{sec}}^2$

---

## 4. Solved Exercises (10 Examples)

### Exercise 1: Probability of Latency Below SLA Limit
**Problem:** Database query response time $T$ (in ms) is normally distributed with $\mu_T = 120\text{ ms}$ and $\sigma_T = 15\text{ ms}$. Find the probability that a query completes in under $100\text{ ms}$.

**Solution:**
- **Step 1: Compute z-score.**
  $$z = \frac{100 - 120}{15} = \frac{-20}{15} = -1.333$$
- **Step 2: WIP State.**
  $$P(T \le 100) = \Phi(-1.33) \approx 0.0918$$
- **Step 3: Final Result.**
  $$P(T \le 100) = 0.0918 \text{ (9.18\%)}$$

---

### Exercise 2: Probability of Latency Between Two Bounds
**Problem:** Web page load time $T \sim N(2.5, 0.16)$ in seconds (so $\mu_T = 2.5$, $\sigma_T = 0.4$). Find $P(2.0 \le T \le 3.1)$.

**Solution:**
- **Step 1: Compute z-scores for both endpoints.**
  $$z_1 = \frac{2.0 - 2.5}{0.4} = -1.25$$
  $$z_2 = \frac{3.1 - 2.5}{0.4} = +1.50$$
- **Step 2: WIP State.**
  $$\Phi(1.50) = 0.9332, \quad \Phi(-1.25) = 0.1056$$
  $$P(2.0 \le T \le 3.1) = \Phi(1.50) - \Phi(-1.25) = 0.9332 - 0.1056$$
- **Step 3: Final Result.**
  $$P(2.0 \le T \le 3.1) = 0.8276 \text{ (82.76\%)}$$

---

### Exercise 3: Finding the 99th Percentile SLA Benchmark ($p_{99}$)
**Problem:** Microservice processing time $T \sim N(50, 100)$ in milliseconds ($\mu_T = 50$, $\sigma_T = 10$). Find the 99th percentile threshold $t_{99}$ such that $P(T \le t_{99}) = 0.99$.

**Solution:**
- **Step 1: Find standard normal quantile $z_{0.99}$.**
  From z-tables, $\Phi(2.326) = 0.99$.
- **Step 2: WIP State.**
  $$t_{99} = \mu_T + z_{0.99} \cdot \sigma_T = 50 + (2.326)(10)$$
  $$t_{99} = 50 + 23.26 = ?$$
- **Step 3: Final Result.**
  $$t_{99} = 73.26\text{ ms}$$

---

### Exercise 4: Unit Conversion (Seconds to Milliseconds)
**Problem:** Server boot duration $T_{\text{sec}} \sim N(12, 4)$ in seconds ($\mu = 12\text{ s}$, $\sigma = 2\text{ s}$). Express $T_{\text{ms}}$ in milliseconds and calculate $P(T_{\text{ms}} > 15{,}000\text{ ms})$.

**Solution:**
- **Step 1: Transform parameters.**
  $$\mu_{\text{ms}} = 12 \times 1000 = 12{,}000\text{ ms}$$
  $$\sigma_{\text{ms}} = 2 \times 1000 = 2{,}000\text{ ms}$$
- **Step 2: WIP State.**
  $$z = \frac{15{,}000 - 12{,}000}{2{,}000} = \frac{3000}{2000} = 1.50$$
  $$P(T_{\text{ms}} > 15{,}000) = 1 - \Phi(1.50) = 1 - 0.9332$$
- **Step 3: Final Result.**
  $$P(T_{\text{ms}} > 15{,}000) = 0.0668 \text{ (6.68\%)}$$

---

### Exercise 5: Probability of Timeout Failure ($T > t_{\text{timeout}}$)
**Problem:** Network ping duration $T \sim N(45, 25)$ in ms ($\mu_T = 45$, $\sigma_T = 5$). A request times out if $T > 60\text{ ms}$. Find the timeout probability.

**Solution:**
- **Step 1: Calculate z-score.**
  $$z = \frac{60 - 45}{5} = 3.00$$
- **Step 2: WIP State.**
  $$P(T > 60) = 1 - \Phi(3.00) = 1 - 0.99865$$
- **Step 3: Final Result.**
  $$P(T > 60) = 0.00135 \text{ (0.135\%)}$$

---

### Exercise 6: Proportion of Latencies Within Half Standard Deviation
**Problem:** Execution time $T \sim N(\mu, \sigma^2)$. What proportion of execution times fall within $\mu \pm 0.5\sigma$?

**Solution:**
- **Step 1: Set up interval bounds.**
  $$z_1 = -0.5, \quad z_2 = +0.5$$
- **Step 2: WIP State.**
  $$\Phi(0.5) = 0.6915, \quad \Phi(-0.5) = 0.3085$$
  $$P(\mu - 0.5\sigma \le T \le \mu + 0.5\sigma) = 0.6915 - 0.3085$$
- **Step 3: Final Result.**
  $$P(\text{within } \pm 0.5\sigma) = 0.3830 \text{ (38.30\%)}$$

---

### Exercise 7: Symmetric Central Time Window
**Problem:** Latency $T \sim N(200, 400)$ in ms ($\mu_T = 200$, $\sigma_T = 20$). Find a symmetric interval $[200 - c, 200 + c]$ that contains $95\%$ of all latencies.

**Solution:**
- **Step 1: Identify outer tail areas.**
  Each tail contains $\frac{1 - 0.95}{2} = 0.025$. Thus $z_{0.975} = 1.96$.
- **Step 2: WIP State.**
  $$c = z \cdot \sigma_T = 1.96 \times 20 = 39.2\text{ ms}$$
  $$\text{Interval} = [200 - 39.2, 200 + 39.2]$$
- **Step 3: Final Result.**
  $$\text{Interval} = [160.8\text{ ms}, 239.2\text{ ms}]$$

---

### Exercise 8: Sum of Two Independent Normal Delay Stages
**Problem:** Processing involves Stage 1 delay $T_1 \sim N(30, 9)$ ms and Stage 2 delay $T_2 \sim N(50, 16)$ ms, independently. Find $P(T_{\text{total}} \le 90\text{ ms})$ where $T_{\text{total}} = T_1 + T_2$.

**Solution:**
- **Step 1: Compute total mean and variance.**
  $$\mu_{\text{total}} = 30 + 50 = 80\text{ ms}$$
  $$\sigma_{\text{total}}^2 = 9 + 16 = 25 \implies \sigma_{\text{total}} = 5\text{ ms}$$
- **Step 2: WIP State.**
  $$z = \frac{90 - 80}{5} = \frac{10}{5} = 2.00$$
  $$P(T_{\text{total}} \le 90) = \Phi(2.00) = 0.9772$$
- **Step 3: Final Result.**
  $$P(T_{\text{total}} \le 90) = 0.9772 \text{ (97.72\%)}$$

---

### Exercise 9: Checking Negative Probability Non-Negligibility
**Problem:** Algorithm execution time is modeled as $T \sim N(10, 16)$ in milliseconds ($\mu_T = 10$, $\sigma_T = 4$). Calculate the theoretical probability $P(T < 0)$ to evaluate model validity.

**Solution:**
- **Step 1: Calculate z-score at $t = 0$.**
  $$z = \frac{0 - 10}{4} = -2.50$$
- **Step 2: WIP State.**
  $$P(T < 0) = \Phi(-2.50) = 0.0062$$
- **Step 3: Final Result.**
  $$P(T < 0) = 0.0062 \text{ (0.62\%)}$$
  *Conclusion:* Because $0.62\%$ is non-zero, $0.62\%$ of probability weight falls in physically impossible negative time. A truncated model should be considered if high precision is required.

---

### Exercise 10: R Code Verification of Latency Quantiles
**Problem:** Demonstrate how to compute the 95th percentile latency and cumulative probability of latency $\le 115\text{ ms}$ for $T \sim N(100, 64)$ in R.

**Solution:**
- **Step 1: Identify parameters.**
  Mean `mean_t = 100`, Standard Deviation `sd_t = 8`.
- **Step 2: R Code Implementation.**
```r
# Parameters for response time in ms
mean_t <- 100
sd_t <- 8

# Cumulative probability P(T <= 115)
p_115 <- pnorm(q = 115, mean = mean_t, sd = sd_t)
cat("P(T <= 115 ms):", round(p_115, 4), "\n")

# 95th percentile SLA limit (p95)
p95_limit <- qnorm(p = 0.95, mean = mean_t, sd = sd_t)
cat("95th percentile limit:", round(p95_limit, 2), "ms\n")
```
- **Step 3: Output Execution.**
  `P(T <= 115 ms): 0.9699`
  `95th percentile limit: 113.16 ms`
