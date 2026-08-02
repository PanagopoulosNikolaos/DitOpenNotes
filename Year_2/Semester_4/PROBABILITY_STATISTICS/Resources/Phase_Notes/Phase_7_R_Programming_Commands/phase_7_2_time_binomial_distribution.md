# Phase 7.2 (Time): Binomial Distribution in R for Time-Window Event Counts

In performance engineering, discrete event counts within time windows—such as the number of request timeouts out of $n$ trials in a 1-minute window—are evaluated using the Binomial distribution functions in R.

---

## 1. R Binomial Family Functions for Time-Windowed Counts

| Function | R Signature | Description |
| :--- | :--- | :--- |
| `dbinom` | `dbinom(x, size, prob)` | Computes exact PMF $P(X = k)$ for $k$ timeouts in $n$ requests. |
| `pbinom` | `pbinom(q, size, prob)` | Computes CDF $P(X \le q)$ or $P(X > q)$ (using `lower.tail = FALSE`). |
| `qbinom` | `qbinom(p, size, prob)` | Computes quantile (inverse CDF) for timeout SLA threshold. |
| `rbinom` | `rbinom(n, size, prob)` | Generates random Binomial variates for time-window Monte Carlo simulations. |

---

## 2. Time-Specific R Gotchas

### Gotcha 1: `lower.tail = FALSE` Calculates $P(X > q)$, NOT $P(X \ge q)$
In R, `pbinom(q, size, prob, lower.tail = FALSE)` evaluates $P(X > q)$. If you need "at least $k$ failures" ($P(X \ge k)$), you must pass `q = k - 1`:
$$\boxed{P(X \ge k) = \text{pbinom}(k - 1, \text{size}, \text{prob}, \text{lower.tail = FALSE})}$$

### Gotcha 2: Confusing Binomial Trials $n$ with Time Interval Length $t$
In a Binomial time-window setup, $n$ is the fixed number of discrete trials (e.g., $n = 100$ requests sent during interval $t$). If trials occur continuously at rate $\lambda$, use the Poisson distribution (`dpois`, `ppois`) instead.

---

## 3. Solved R Code Examples (10 Exercises)

### Exercise 1: Exact Probability of $k$ Timeouts in a Time Window (`dbinom`)
**Problem:** A network request has timeout probability $p = 0.05$. Out of $n = 20$ requests in a 10-second window, calculate $P(X = 2)$ timeouts.

**Solution:**
```r
# Parameters: n = 20 requests, p = 0.05 timeout probability
n_req <- 20
p_timeout <- 0.05

# Exact probability P(X = 2)
prob_exact <- dbinom(x = 2, size = n_req, prob = p_timeout)

cat("P(X = 2 timeouts):", round(prob_exact, 4), "\n")
```

---

### Exercise 2: Cumulative Timeout Probability Below SLA (`pbinom`)
**Problem:** Calculate the probability of observing at most 1 timeout ($P(X \le 1)$) out of $n = 50$ requests in a time window where $p = 0.02$.

**Solution:**
```r
prob_le_1 <- pbinom(q = 1, size = 50, prob = 0.02)
cat("P(X <= 1 timeout):", round(prob_le_1, 4), "\n")
```

---

### Exercise 3: At Least $k$ Failures Using Complement (`lower.tail = FALSE`)
**Problem:** Find the probability of observing at least 3 timeouts ($P(X \ge 3)$) out of $n = 100$ requests with $p = 0.01$.

**Solution:**
```r
# P(X >= 3) = P(X > 2) -> pass q = 2
prob_ge_3 <- pbinom(q = 2, size = 100, prob = 0.01, lower.tail = FALSE)
cat("P(X >= 3 timeouts):", round(prob_ge_3, 4), "\n")
```

---

### Exercise 4: 95th Percentile Maximum Timeouts (`qbinom`)
**Problem:** Determine the 95th percentile upper bound for the number of timeout failures in $n = 500$ requests when $p = 0.03$.

**Solution:**
```r
p95_failures <- qbinom(p = 0.95, size = 500, prob = 0.03)
cat("95th percentile failure cap:", p95_failures, "failures\n")
```

---

### Exercise 5: Plotting the PMF Distribution of Timeout Counts
**Problem:** Generate and plot the complete PMF vector for $0 \le k \le 10$ timeouts out of $n = 100$ requests with $p = 0.04$.

**Solution:**
```r
k_vals <- 0:10
pmf_vals <- dbinom(k_vals, size = 100, prob = 0.04)

# Create summary data frame
pmf_df <- data.frame(Timeouts = k_vals, Probability = round(pmf_vals, 4))
print(pmf_df)
```

---

### Exercise 6: Simulating 1,000 Time Windows (`rbinom`)
**Problem:** Simulate timeout counts across $1{,}000$ independent 1-minute time windows ($n = 200$ requests per window, $p = 0.02$). Compute empirical mean and variance.

**Solution:**
```r
set.seed(123)

# Simulate 1000 time windows
sim_timeouts <- rbinom(n = 1000, size = 200, prob = 0.02)

emp_mean <- mean(sim_timeouts)
emp_var  <- var(sim_timeouts)
theo_mean <- 200 * 0.02       # 4.0
theo_var  <- 200 * 0.02 * 0.98 # 3.92

cat("Empirical Mean:", emp_mean, "(Theoretical:", theo_mean, ")\n")
cat("Empirical Variance:", round(emp_var, 3), "(Theoretical:", theo_var, ")\n")
```

---

### Exercise 7: Time-Window SLA Violation Probability ($X > k_{\text{allowed}}$)
**Problem:** An SLA allows at most 5 timeouts per 1,000 requests. If $p = 0.008$, calculate the probability that a time window violates the SLA ($P(X > 5)$).

**Solution:**
```r
prob_sla_violation <- pbinom(q = 5, size = 1000, prob = 0.008, lower.tail = FALSE)
cat("SLA Violation Probability:", round(prob_sla_violation, 4), "\n")
```

---

### Exercise 8: Range Probability $P(k_1 \le X \le k_2)$
**Problem:** Calculate the probability of getting between 2 and 5 timeouts (inclusive) out of $n = 150$ requests with $p = 0.02$.

**Solution:**
```r
# P(2 <= X <= 5) = P(X <= 5) - P(X <= 1)
prob_range <- pbinom(5, size = 150, prob = 0.02) - pbinom(1, size = 150, prob = 0.02)
cat("P(2 <= X <= 5):", round(prob_range, 4), "\n")
```

---

### Exercise 9: Normal Approximation to Binomial for Large Time Windows
**Problem:** Compare exact `pbinom(60, size = 1000, prob = 0.05)` vs Normal approximation with continuity correction `pnorm(60.5, mean = np, sd = sqrt(npq))`.

**Solution:**
```r
n <- 1000
p <- 0.05
mu <- n * p           # 50
sigma <- sqrt(n*p*(1-p)) # sqrt(47.5) = 6.892

prob_exact  <- pbinom(60, size = n, prob = p)
prob_approx <- pnorm(60.5, mean = mu, sd = sigma)

cat("Exact Binomial P(X <= 60):", round(prob_exact, 5), "\n")
cat("Normal Approx P(X <= 60):", round(prob_approx, 5), "\n")
```

---

### Exercise 10: Finding Maximum Batch Size $n$ for SLA Compliance
**Problem:** Find the maximum number of requests $n$ that can be sent in a time window such that $P(\text{at least 1 failure}) \le 0.10$ when $p = 0.001$.

**Solution:**
```r
# P(X >= 1) = 1 - (1-p)^n <= 0.10 -> (0.999)^n >= 0.90
# n <= ln(0.90) / ln(0.999)

p <- 0.001
target_prob <- 0.10
max_n <- floor(log(1 - target_prob) / log(1 - p))

cat("Maximum requests n per window:", max_n, "\n")
```
