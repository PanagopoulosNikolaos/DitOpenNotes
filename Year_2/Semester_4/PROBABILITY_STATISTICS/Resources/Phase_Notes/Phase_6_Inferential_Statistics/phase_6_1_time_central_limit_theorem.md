# Phase 6.1 (Time): Central Limit Theorem (CLT) for Time Data Metrics

The Central Limit Theorem (CLT) is the foundation of inferential statistics for performance engineering. It states that the sample mean $\bar{T}$ of $n$ independent and identically distributed (i.i.d.) random time metrics—regardless of the underlying latency distribution (exponential, uniform, skewed)—approaches a Normal distribution as sample size $n$ grows large ($n \ge 30$).

---

## 1. Statement of the Central Limit Theorem for Time Samples

Let $T_1, T_2, \dots, T_n$ be an i.i.d. sample of size $n$ drawn from an execution time population with finite mean $\mu_T$ and finite variance $\sigma_T^2$.

### 1.1 Sampling Distribution of Sample Mean Time $\bar{T}$
The sample mean duration $\bar{T} = \frac{1}{n} \sum_{i=1}^n T_i$ has:
* **Expected Value:** $E[\bar{T}] = \mu_T$
* **Variance:** $V(\bar{T}) = \frac{\sigma_T^2}{n}$
* **Standard Error (SE):** $\sigma_{\bar{T}} = \frac{\sigma_T}{\sqrt{n}}$

As $n \to \infty$ (practically $n \ge 30$), the distribution of $\bar{T}$ converges to:

$$\boxed{\bar{T} \xrightarrow{d} N\left(\mu_T, \frac{\sigma_T^2}{n}\right)}$$

### 1.2 Standardized Z-Score for Sample Means
To compute probabilities for sample mean duration $\bar{T}$:

$$\boxed{Z = \frac{\bar{T} - \mu_T}{\sigma_T / \sqrt{n}} \sim N(0, 1)}$$

---

## 2. Sampling Distribution of Total Time Sum $S_n$

For total cumulative execution duration $S_n = \sum_{i=1}^n T_i$:
* **Expected Value:** $E[S_n] = n \mu_T$
* **Variance:** $V(S_n) = n \sigma_T^2 \implies SD(S_n) = \sqrt{n} \sigma_T$

$$\boxed{S_n \xrightarrow{d} N(n \mu_T, n \sigma_T^2)}$$

---

## 3. Time-Specific Gotchas

### Gotcha 1: Confusing Population Standard Deviation $\sigma_T$ with Standard Error $\sigma_{\bar{T}}$
A frequent error is calculating probabilities for an *average* latency $\bar{T}$ using individual request standard deviation $\sigma_T$ instead of standard error $\sigma_{\bar{T}} = \sigma_T / \sqrt{n}$. As sample size $n$ increases, the variability of the *average* time decreases by $\sqrt{n}$.

### Gotcha 2: Applying CLT to Small Samples ($n < 30$) from Skewed Distributions
Raw individual latency metrics are typically right-skewed (Exponential or Gamma). For $n = 5$ or $n = 10$, $\bar{T}$ remains skewed! The rule of thumb $n \ge 30$ (or even $n \ge 50$ for extreme tail skewness) must be satisfied before assuming $\bar{T} \sim N(\mu_T, \sigma_T^2 / n)$.

---

## 4. Solved Exercises (10 Examples)

### Exercise 1: Standard Error of Mean Latency
**Problem:** DB query duration has population mean $\mu_T = 150\text{ ms}$ and standard deviation $\sigma_T = 40\text{ ms}$. Calculate the standard error of the mean for sample sizes $n = 16, 64, 400$.

**Solution:**
- **Step 1: Formula $\sigma_{\bar{T}} = \sigma_T / \sqrt{n}$.**
- **Step 2: WIP State.**
  For $n = 16$: $\sigma_{\bar{T}} = 40 / \sqrt{16} = 40 / 4 = 10\text{ ms}$
  For $n = 64$: $\sigma_{\bar{T}} = 40 / \sqrt{64} = 40 / 8 = 5\text{ ms}$
  For $n = 400$: $\sigma_{\bar{T}} = 40 / \sqrt{400} = 40 / 20 = 2\text{ ms}$
- **Step 3: Final Result.**
  Standard errors are $10\text{ ms}$, $5\text{ ms}$, and $2\text{ ms}$ respectively.

---

### Exercise 2: Probability of Sample Mean Ping Duration Exceeding Bound
**Problem:** Ping times have mean $\mu_T = 45\text{ ms}$ and $\sigma_T = 12\text{ ms}$. A sample of $n = 36$ pings is measured. Find $P(\bar{T} > 48\text{ ms})$.

**Solution:**
- **Step 1: Compute Standard Error.**
  $$\sigma_{\bar{T}} = \frac{12}{\sqrt{36}} = \frac{12}{6} = 2\text{ ms}$$
- **Step 2: Calculate z-score.**
  $$z = \frac{48 - 45}{2} = 1.50$$
- **Step 3: WIP State and Final Result.**
  $$P(\bar{T} > 48) = 1 - \Phi(1.50) = 1 - 0.9332 = 0.0668 \text{ (6.68\%)}$$

---

### Exercise 3: Total Execution Duration of $n = 100$ Tasks
**Problem:** Execution time of individual tasks has mean $\mu_T = 5\text{ seconds}$ and $\sigma_T = 1.5\text{ seconds}$. Find $P(S_{100} \le 520\text{ seconds})$ for a batch of $n = 100$ tasks.

**Solution:**
- **Step 1: Determine mean and standard deviation of $S_{100}$.**
  $$E[S_{100}] = 100 \times 5 = 500\text{ seconds}$$
  $$SD(S_{100}) = \sqrt{100} \times 1.5 = 10 \times 1.5 = 15\text{ seconds}$$
- **Step 2: Calculate z-score.**
  $$z = \frac{520 - 500}{15} = \frac{20}{15} = 1.333$$
- **Step 3: WIP State and Final Result.**
  $$P(S_{100} \le 520) = \Phi(1.333) \approx 0.9088 \text{ (90.88\%)}$$

---

### Exercise 4: CLT Applied to Exponentially Distributed Time Metrics
**Problem:** Server log arrival interval $T \sim \text{Exp}(\lambda = 0.1\text{ s}^{-1})$ (so $\mu_T = 10\text{ s}, \sigma_T = 10\text{ s}$). For a sample of $n = 100$ log intervals, find $P(9\text{ s} \le \bar{T} \le 11\text{ s})$.

**Solution:**
- **Step 1: Compute Standard Error.**
  $$\sigma_{\bar{T}} = \frac{10}{\sqrt{100}} = \frac{10}{10} = 1\text{ s}$$
- **Step 2: Calculate z-scores.**
  $$z_1 = \frac{9 - 10}{1} = -1.00, \quad z_2 = \frac{11 - 10}{1} = +1.00$$
- **Step 3: WIP State and Final Result.**
  $$P(9 \le \bar{T} \le 11) = \Phi(1.00) - \Phi(-1.00) = 0.8413 - 0.1587 = 0.6826 \text{ (68.26\%)}$$

---

### Exercise 5: Sample Size Determination for Targeted Latency Margin
**Problem:** Individual network delay has $\sigma_T = 30\text{ ms}$. How many sample pings $n$ are needed so that the sample mean $\bar{T}$ lies within $\pm 3\text{ ms}$ of true mean $\mu_T$ with $95\%$ probability?

**Solution:**
- **Step 1: Identify margin of error formula $E = z_{0.975} \cdot \frac{\sigma_T}{\sqrt{n}}$.**
  $$3 = 1.96 \cdot \frac{30}{\sqrt{n}}$$
- **Step 2: Solve for $\sqrt{n}$ and $n$.**
  $$\sqrt{n} = \frac{1.96 \times 30}{3} = 1.96 \times 10 = 19.6$$
  $$n = (19.6)^2 = 384.16$$
- **Step 3: Final Result.**
  Round up to $n = 385$ pings.

---

### Exercise 6: CLT Applied to Uniform Random Backoff
**Problem:** Retransmission delay $T \sim U(0, 20)$ ms ($\mu_T = 10\text{ ms}, \sigma_T^2 = 400/12 = 33.333\text{ ms}^2$). For $n = 40$ retransmissions, find $P(\bar{T} \ge 11\text{ ms})$.

**Solution:**
- **Step 1: Compute Standard Error.**
  $$\sigma_{\bar{T}} = \sqrt{\frac{33.333}{40}} = \sqrt{0.8333} \approx 0.9129\text{ ms}$$
- **Step 2: Calculate z-score.**
  $$z = \frac{11 - 10}{0.9129} = 1.095 \approx 1.10$$
- **Step 3: WIP State and Final Result.**
  $$P(\bar{T} \ge 11) = 1 - \Phi(1.10) = 1 - 0.8643 = 0.1357 \text{ (13.57\%)}$$

---

### Exercise 7: Symmetric Bounds for Sample Mean Execution Time
**Problem:** Execution time population has $\mu_T = 200\text{ ms}$ and $\sigma_T = 50\text{ ms}$. For $n = 100$ measurements, find the interval $[\mu_T - c, \mu_T + c]$ containing $99\%$ of sample means $\bar{T}$.

**Solution:**
- **Step 1: Compute Standard Error and find $z_{0.995}$.**
  $$\sigma_{\bar{T}} = \frac{50}{\sqrt{100}} = 5\text{ ms}, \quad z_{0.995} = 2.576$$
- **Step 2: Compute margin $c$.**
  $$c = 2.576 \times 5 = 12.88\text{ ms}$$
- **Step 3: Final Result.**
  $$\text{Interval} = [200 - 12.88, 200 + 12.88] = [187.12\text{ ms}, 212.88\text{ ms}]$$

---

### Exercise 8: Comparing Individual vs Sample Mean Tail Probabilities
**Problem:** Latency $T \sim N(100, 400)$ in ms ($\mu_T = 100, \sigma_T = 20$). Compare $P(T > 110)$ for a single request vs $P(\bar{T} > 110)$ for a sample average of $n = 25$ requests.

**Solution:**
- **Step 1: Single request $P(T > 110)$.**
  $$z_1 = \frac{110 - 100}{20} = 0.50 \implies P(T > 110) = 1 - \Phi(0.50) = 0.3085 \text{ (30.85\%)}$$
- **Step 2: Sample mean $P(\bar{T} > 110)$ with $n = 25$.**
  $$\sigma_{\bar{T}} = 20 / \sqrt{25} = 4\text{ ms}$$
  $$z_{25} = \frac{110 - 100}{4} = 2.50 \implies P(\bar{T} > 110) = 1 - \Phi(2.50) = 0.0062 \text{ (0.62\%)}$$
- **Step 3: Final Result.**
  Single request has $30.85\%$ chance of exceeding $110\text{ ms}$, whereas the sample average of $25$ requests has only $0.62\%$ chance.

---

### Exercise 9: Difference Between Two Independent Sample Means ($\bar{T}_1 - \bar{T}_2$)
**Problem:** Microservice A latency has $\mu_1 = 80\text{ ms}, \sigma_1 = 15\text{ ms}, n_1 = 36$. Microservice B has $\mu_2 = 75\text{ ms}, \sigma_2 = 20\text{ ms}, n_2 = 64$. Find $P(\bar{T}_1 - \bar{T}_2 > 10\text{ ms})$.

**Solution:**
- **Step 1: Compute mean and variance of difference.**
  $$E[\bar{T}_1 - \bar{T}_2] = 80 - 75 = 5\text{ ms}$$
  $$V(\bar{T}_1 - \bar{T}_2) = \frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2} = \frac{225}{36} + \frac{400}{64} = 6.25 + 6.25 = 12.5\text{ ms}^2$$
  $$SD = \sqrt{12.5} \approx 3.5355\text{ ms}$$
- **Step 2: WIP State.**
  $$z = \frac{10 - 5}{3.5355} = \frac{5}{3.5355} = 1.414 \approx 1.41$$
  $$P(\bar{T}_1 - \bar{T}_2 > 10) = 1 - \Phi(1.41) = 1 - 0.9207 = 0.0793$$
- **Step 3: Final Result.**
  $$P(\bar{T}_1 - \bar{T}_2 > 10) = 0.0793 \text{ (7.93\%)}$$

---

### Exercise 10: R Code Simulation of CLT Convergence for Skewed Latencies
**Problem:** Write an R script simulating sample means of size $n = 5$ and $n = 50$ drawn from an Exponential latency distribution $\text{Exp}(\lambda = 0.1)$ to demonstrate CLT convergence.

**Solution:**
- **Step 1: R Script Setup.**
```r
set.seed(123)
N <- 100000

# Draw sample means from Exp(0.1) where mu = 10, sd = 10
means_n5  <- replicate(N, mean(rexp(5, rate = 0.1)))
means_n50 <- replicate(N, mean(rexp(50, rate = 0.1)))

cat("n = 5  Sample Mean SD:", round(sd(means_n5), 3), "(Theoretical:", round(10/sqrt(5), 3), ")\n")
cat("n = 50 Sample Mean SD:", round(sd(means_n50), 3), "(Theoretical:", round(10/sqrt(50), 3), ")\n")

# Empirical P(9 <= T_bar <= 11) for n = 50
p_emp <- mean(means_n50 >= 9 & means_n50 <= 11)
cat("n = 50 P(9 <= T_bar <= 11):", round(p_emp, 4), "\n")
```
- **Step 2: Execution Output.**
  `n = 5  Sample Mean SD: 4.471 (Theoretical: 4.472)`
  `n = 50 Sample Mean SD: 1.413 (Theoretical: 1.414)`
  `n = 50 P(9 <= T_bar <= 11): 0.5218`
