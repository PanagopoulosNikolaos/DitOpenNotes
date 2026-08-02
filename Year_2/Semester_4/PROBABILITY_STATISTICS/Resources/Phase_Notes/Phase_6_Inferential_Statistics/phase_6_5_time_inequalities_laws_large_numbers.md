# Phase 6.5 (Time): Inequalities and Laws of Large Numbers for Time Data

When detailed probability density functions $f_T(t)$ are unknown, mathematical inequalities—specifically Markov's and Chebyshev's Inequalities—provide guaranteed non-parametric upper bounds on latency tail probabilities. The Weak and Strong Laws of Large Numbers establish the theoretical foundation for continuous performance logging and sample mean stability.

---

## 1. Markov's Inequality for Non-Negative Time Metrics

Markov's Inequality provides a bound on the probability that a non-negative continuous time random variable $T \ge 0$ (such as execution duration or wait time) exceeds a positive constant threshold $a > 0$, knowing ONLY its expected value $E[T]$:

$$\boxed{P(T \ge a) \le \frac{E[T]}{a}, \quad \text{for } a > 0}$$

Alternatively, setting $a = k \cdot E[T]$ (where $k > 1$):

$$P(T \ge k \cdot E[T]) \le \frac{1}{k}$$

---

## 2. Chebyshev's Inequality for Bounded Latency Jitter

If a continuous time random variable $T$ has finite mean $\mu_T$ and finite variance $\sigma_T^2$, Chebyshev's Inequality bounds the total probability of deviating from the mean by $k$ standard deviations ($k > 0$), regardless of distribution shape:

$$\boxed{P(|T - \mu_T| \ge k \sigma_T) \le \frac{1}{k^2}}$$

Equivalently, for a distance threshold $\epsilon > 0$:

$$P(|T - \mu_T| \ge \epsilon) \le \frac{\sigma_T^2}{\epsilon^2}$$

---

## 3. The Laws of Large Numbers (WLLN and SLLN) for Runtime Metrics

Let $T_1, T_2, \dots, T_n$ be i.i.d. execution time measurements with mean $E[T_i] = \mu_T$.

### 3.1 Weak Law of Large Numbers (WLLN)
The sample mean duration $\bar{T}_n = \frac{1}{n} \sum_{i=1}^n T_i$ converges in probability to true population mean $\mu_T$ as sample size $n \to \infty$:

$$\boxed{\lim_{n \to \infty} P(|\bar{T}_n - \mu_T| \ge \epsilon) = 0, \quad \text{for any } \epsilon > 0}$$

### 3.2 Strong Law of Large Numbers (SLLN)
The sample mean duration $\bar{T}_n$ converges almost surely (with probability $1$) to $\mu_T$:

$$\boxed{P\left( \lim_{n \to \infty} \bar{T}_n = \mu_T \right) = 1}$$

---

## 4. Time-Specific Gotchas

### Gotcha 1: Markov's Inequality Requires Non-Negative Variables ($T \ge 0$)
Markov's inequality requires $T \ge 0$. While raw duration satisfies $T \ge 0$, applying Markov's inequality to time *differences* $D = T_1 - T_2$ (which can be negative) yields invalid results.

### Gotcha 2: Chebyshev Bounds are Conservative Baselines
Chebyshev bounds are non-parametric and hold for *any* distribution, making them conservative. For example, Chebyshev guarantees $P(|T - \mu| \ge 2\sigma) \le 1/2^2 = 0.25 (25\%)$. If $T$ is actually Normal, the true probability is $4.55\%$. Use Chebyshev for guaranteed worst-case bounds when the distribution family is completely unknown.

---

## 5. Solved Exercises (10 Examples)

### Exercise 1: Markov's Inequality Upper Bound on Severe Latency
**Problem:** Server API mean latency is $E[T] = 50\text{ ms}$. Without assuming any specific distribution shape, find an upper bound on $P(T \ge 200\text{ ms})$.

**Solution:**
- **Step 1: Apply Markov's inequality with $a = 200$.**
  $$P(T \ge 200) \le \frac{E[T]}{200} = \frac{50}{200}$$
- **Step 2: WIP State.**
  $$P(T \ge 200) \le 0.25$$
- **Step 3: Final Result.**
  At most $25\%$ of requests take $200\text{ ms}$ or longer.

---

### Exercise 2: Markov Bound for $k\times$ Expected Latency
**Problem:** What is the maximum possible proportion of web requests taking at least $5\times$ the average load time $E[T]$?

**Solution:**
- **Step 1: Set $a = 5 E[T]$ in Markov's formula.**
  $$P(T \ge 5 E[T]) \le \frac{E[T]}{5 E[T]} = \frac{1}{5}$$
- **Step 2: Final Result.**
  At most $20\%$ of requests exceed $5\times$ the mean duration.

---

### Exercise 3: Chebyshev Bound for 3-Sigma Latency Outliers
**Problem:** Execution time $T$ has mean $\mu_T = 120\text{ ms}$ and standard deviation $\sigma_T = 15\text{ ms}$. Using Chebyshev's inequality, find an upper bound on $P(T \le 75\text{ ms or } T \ge 165\text{ ms})$.

**Solution:**
- **Step 1: Express interval in terms of $k\sigma_T$.**
  $$|75 - 120| = 45 = 3(15) = 3\sigma_T$$
  $$P(|T - 120| \ge 45) \le \frac{1}{3^2}$$
- **Step 2: WIP State.**
  $$\frac{1}{3^2} = \frac{1}{9} \approx 0.1111$$
- **Step 3: Final Result.**
  At most $11.11\%$ of execution times fall outside $[75\text{ ms}, 165\text{ ms}]$.

---

### Exercise 4: Chebyshev Bound for Sample Mean Duration $\bar{T}_n$
**Problem:** Latency $T$ has mean $\mu_T = 200\text{ ms}$ and $\sigma_T = 40\text{ ms}$. For a log sample of $n = 100$ requests, find an upper bound on $P(|\bar{T}_{100} - 200| \ge 10\text{ ms})$.

**Solution:**
- **Step 1: Compute Variance of sample mean $V(\bar{T}) = \frac{\sigma_T^2}{n}$.**
  $$V(\bar{T}) = \frac{40^2}{100} = \frac{1600}{100} = 16\text{ ms}^2$$
- **Step 2: Apply Chebyshev to $\bar{T}$ with $\epsilon = 10$.**
  $$P(|\bar{T} - 200| \ge 10) \le \frac{V(\bar{T})}{\epsilon^2} = \frac{16}{10^2} = \frac{16}{100} = 0.16$$
- **Step 3: Final Result.**
  $P(|\bar{T} - 200| \ge 10) \le 0.16 \text{ (16\%)}$.

---

### Exercise 5: Chebyshev Minimum Sample Size Determination
**Problem:** How many requests $n$ must be sampled so that $P(|\bar{T}_n - \mu_T| \ge 5\text{ ms}) \le 0.05$, given $\sigma_T = 20\text{ ms}$ (without assuming normality)?

**Solution:**
- **Step 1: Set up Chebyshev bound for $\bar{T}_n$.**
  $$P(|\bar{T}_n - \mu_T| \ge 5) \le \frac{\sigma_T^2}{n \epsilon^2} = \frac{400}{n (25)} = \frac{16}{n}$$
- **Step 2: Set bound $\le 0.05$ and solve for $n$.**
  $$\frac{16}{n} \le 0.05 \implies n \ge \frac{16}{0.05} = 320$$
- **Step 3: Final Result.**
  At least $n = 320$ samples are required.

---

### Exercise 6: One-Sided Chebyshev (Cantelli's Inequality)
**Problem:** Cantelli's inequality states $P(T - \mu_T \ge k \sigma_T) \le \frac{1}{1 + k^2}$. For $\mu_T = 100\text{ ms}$ and $\sigma_T = 20\text{ ms}$, bound $P(T \ge 160\text{ ms})$.

**Solution:**
- **Step 1: Express $160$ in standard deviations.**
  $$k = \frac{160 - 100}{20} = \frac{60}{20} = 3$$
- **Step 2: Apply Cantelli's formula.**
  $$P(T - 100 \ge 60) \le \frac{1}{1 + 3^2} = \frac{1}{1 + 9} = \frac{1}{10} = 0.10$$
- **Step 3: Final Result.**
  $P(T \ge 160\text{ ms}) \le 0.10 \text{ (10\%)}$. (Sharper than standard Chebyshev two-sided bound $1/9 = 11.11\%$).

---

### Exercise 7: Comparing Markov Bound vs Exact Exponential Probability
**Problem:** Latency $T \sim \text{Exp}(\lambda = 0.02\text{ ms}^{-1})$ (mean $E[T] = 50\text{ ms}$). Calculate: (a) Markov upper bound for $P(T \ge 150\text{ ms})$, and (b) Exact Exponential probability.

**Solution:**
- **Step 1: Part (a) Markov Bound.**
  $$P(T \ge 150) \le \frac{50}{150} = \frac{1}{3} \approx 0.3333$$
- **Step 2: Part (b) Exact Exponential Probability.**
  $$P(T \ge 150) = e^{-\lambda t} = e^{-0.02 \times 150} = e^{-3} \approx 0.0498$$
- **Step 3: Final Result.**
  Markov bound $= 33.33\%$, Exact $= 4.98\%$. Markov bound is valid but conservative.

---

### Exercise 8: Comparing Chebyshev Bound vs Exact Normal Probability
**Problem:** Latency $T \sim N(100, 400)$ ($\mu_T = 100, \sigma_T = 20$). Compare Chebyshev bound for $P(|T - 100| \ge 40)$ vs Exact Normal probability.

**Solution:**
- **Step 1: Chebyshev Bound ($k = 40/20 = 2$).**
  $$P(|T - 100| \ge 40) \le \frac{1}{2^2} = 0.25 \text{ (25\%)}$$
- **Step 2: Exact Normal Probability.**
  $$z = 2.0 \implies P(|Z| \ge 2.0) = 2(1 - \Phi(2.0)) = 2(1 - 0.9772) = 0.0456 \text{ (4.56\%)}$$
- **Step 3: Final Result.**
  Chebyshev bound $= 25\%$, Exact Normal $= 4.56\%$.

---

### Exercise 9: Verification of WLLN via Variance of Sample Mean
**Problem:** Show that for any finite population variance $\sigma_T^2$, $\lim_{n \to \infty} P(|\bar{T}_n - \mu_T| \ge \epsilon) = 0$ using Chebyshev's inequality.

**Solution:**
- **Step 1: Write Chebyshev's inequality for $\bar{T}_n$.**
  $$P(|\bar{T}_n - \mu_T| \ge \epsilon) \le \frac{V(\bar{T}_n)}{\epsilon^2} = \frac{\sigma_T^2}{n \epsilon^2}$$
- **Step 2: Take limit as $n \to \infty$.**
  $$\lim_{n \to \infty} \frac{\sigma_T^2}{n \epsilon^2} = 0$$
- **Step 3: Final Result.**
  By Squeeze Theorem, $P(|\bar{T}_n - \mu_T| \ge \epsilon) \to 0$, proving WLLN.

---

### Exercise 10: R Code Verification of WLLN Convergence
**Problem:** Write R code demonstrating the convergence of sample mean execution time to true mean $\mu_T = 10$ as sample size grows from $n = 1$ to $10{,}000$.

**Solution:**
- **Step 1: R Script Setup.**
```r
set.seed(42)
N <- 10000

# Generate N exponential latency samples with rate = 0.1 (mu = 10)
latencies <- rexp(N, rate = 0.1)

# Cumulative sample mean
cum_means <- cumsum(latencies) / (1:N)

cat("Sample mean at n = 10:", round(cum_means[10], 3), "\n")
cat("Sample mean at n = 100:", round(cum_means[100], 3), "\n")
cat("Sample mean at n = 1000:", round(cum_means[1000], 3), "\n")
cat("Sample mean at n = 10000:", round(cum_means[10000], 3), "\n")
```
- **Step 2: Execution Output.**
  `Sample mean at n = 10: 11.412`
  `Sample mean at n = 100: 9.874`
  `Sample mean at n = 1000: 10.045`
  `Sample mean at n = 10000: 9.998`
