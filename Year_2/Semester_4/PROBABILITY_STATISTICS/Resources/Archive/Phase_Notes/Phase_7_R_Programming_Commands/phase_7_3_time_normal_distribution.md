# Phase 7.3 (Time): Normal Distribution in R for System Latencies

In R, analyzing normally distributed continuous time metrics—such as latency durations, system processing times, and network ping variations—relies on the core `norm` function family: `dnorm`, `pnorm`, `qnorm`, and `rnorm`.

---

## 1. R Normal Family Functions for Latency Metrics

| Function | R Signature | Description |
| :--- | :--- | :--- |
| `dnorm` | `dnorm(x, mean, sd)` | Computes continuous PDF density value $f_T(x)$ at latency $x$. |
| `pnorm` | `pnorm(q, mean, sd)` | Computes continuous CDF $P(T \le q)$ or $P(T > q)$ (using `lower.tail = FALSE`). |
| `qnorm` | `qnorm(p, mean, sd)` | Computes latency quantile (e.g., $p_{95}, p_{99}$ SLA limits). |
| `rnorm` | `rnorm(n, mean, sd)` | Generates $n$ random continuous latency observations. |

---

## 2. Time-Specific R Gotchas

### Gotcha 1: `sd` Parameter is Standard Deviation $\sigma_T$, NOT Variance $\sigma_T^2$
The R functions take standard deviation `sd = sigma`. Passing variance $\sigma_T^2$ directly (e.g., passing `sd = 100` when $\sigma_T^2 = 100$) causes standard deviation to be inflated by a factor of 10. Always pass `sd = sqrt(variance)`.

### Gotcha 2: Standardizing Latencies Using `scale()` vs Manual Z-Scores
The `scale(x)` function in R returns a matrix with attributes (`scaled:center` and `scaled:scale`). If you require a plain numeric vector of z-scores, use `as.vector(scale(x))` or `(x - mean(x)) / sd(x)`.

---

## 3. Solved R Code Examples (10 Exercises)

### Exercise 1: Cumulative Probability of Latency Below SLA Limit (`pnorm`)
**Problem:** DB query duration $T \sim N(\mu = 120\text{ ms}, \sigma = 15\text{ ms})$. Calculate $P(T \le 100\text{ ms})$ in R.

**Solution:**
```r
mu_lat <- 120
sd_lat <- 15

# Probability latency is <= 100 ms
p_below_100 <- pnorm(q = 100, mean = mu_lat, sd = sd_lat)
cat("P(T <= 100 ms):", round(p_below_100, 4), "\n")
```

---

### Exercise 2: Upper Tail Slow Request Probability ($P(T > 150\text{ ms})$)
**Problem:** For $T \sim N(120, 15^2)$, find the probability of a request taking longer than $150\text{ ms}$.

**Solution:**
```r
p_slow <- pnorm(q = 150, mean = 120, sd = 15, lower.tail = FALSE)
cat("P(T > 150 ms):", round(p_slow, 4), "\n")
```

---

### Exercise 3: Probability Over a Latency Duration Interval ($P(t_1 \le T \le t_2)$)
**Problem:** Find $P(110\text{ ms} \le T \le 140\text{ ms})$ for $T \sim N(120, 15^2)$.

**Solution:**
```r
p_interval <- pnorm(140, mean = 120, sd = 15) - pnorm(110, mean = 120, sd = 15)
cat("P(110 <= T <= 140):", round(p_interval, 4), "\n")
```

---

### Exercise 4: SLA 99th Percentile Limit ($p_{99}$) Calculation (`qnorm`)
**Problem:** Find the latency value $t_{99}$ such that $99\%$ of requests complete in under $t_{99}$ for $T \sim N(50\text{ ms}, 10^2\text{ ms}^2)$.

**Solution:**
```r
p99_threshold <- qnorm(p = 0.99, mean = 50, sd = 10)
cat("99th percentile SLA threshold:", round(p99_threshold, 2), "ms\n")
```

---

### Exercise 5: Plotting the Latency Density Curve (`dnorm`)
**Problem:** Generate points for a Normal latency PDF curve with $\mu = 100\text{ ms}, \sigma = 20\text{ ms}$ over $[40, 160]$ and compute peak height.

**Solution:**
```r
t_vals <- seq(40, 160, by = 1)
pdf_vals <- dnorm(t_vals, mean = 100, sd = 20)

cat("Peak density height at mean:", round(dnorm(100, 100, 20), 4), "\n")
# Plotting command: plot(t_vals, pdf_vals, type = "l", main = "Latency Density Curve")
```

---

### Exercise 6: Simulating $100{,}000$ Latency Logs (`rnorm`)
**Problem:** Generate $100{,}000$ random normal latency metrics ($\mu = 200\text{ ms}, \sigma = 25\text{ ms}$). Compute sample mean, sample standard deviation, and empirical 95th percentile.

**Solution:**
```r
set.seed(42)
sim_latencies <- rnorm(n = 100000, mean = 200, sd = 25)

cat("Empirical Mean:", round(mean(sim_latencies), 2), "ms\n")
cat("Empirical SD:", round(sd(sim_latencies), 2), "ms\n")
cat("Empirical p95:", round(quantile(sim_latencies, 0.95), 2), "ms\n")
```

---

### Exercise 7: Standardizing Latencies to Standard Normal Z-Scores
**Problem:** Convert a vector of raw page load times into standard z-scores in R.

**Solution:**
```r
raw_times <- c(2.1, 2.8, 1.9, 3.2, 2.5, 2.4, 2.9)
z_scores  <- as.vector(scale(raw_times))

print(data.frame(Raw = raw_times, Z = round(z_scores, 3)))
```

---

### Exercise 8: Symmetric SLA Interval Bounds Containing $95\%$ of Requests
**Problem:** Calculate the lower and upper bounds containing the central $95\%$ of latencies for $T \sim N(150, 20^2)$.

**Solution:**
- **Step 1: Use `qnorm(c(0.025, 0.975))` for outer tail bounds.**
```r
bounds_95 <- qnorm(c(0.025, 0.975), mean = 150, sd = 20)
cat("95% Symmetric Bounds:", round(bounds_95[1], 2), "ms to", round(bounds_95[2], 2), "ms\n")
```

---

### Exercise 9: Sum of Two Independent Normal Processing Stages
**Problem:** Stage 1 duration $T_1 \sim N(40, 9)$ ms and Stage 2 duration $T_2 \sim N(60, 16)$ ms. Compute $P(T_1 + T_2 \le 112\text{ ms})$ in R.

**Solution:**
```r
# Total Mean = 40 + 60 = 100, Total Var = 9 + 16 = 25 -> Total SD = 5
mu_total <- 40 + 60
sd_total <- sqrt(9 + 16)

p_sum_le_112 <- pnorm(112, mean = mu_total, sd = sd_total)
cat("P(T1 + T2 <= 112 ms):", round(p_sum_le_112, 4), "\n")
```

---

### Exercise 10: Testing Normality of Recorded Latencies (Shapiro-Wilk Test)
**Problem:** Test whether a sample of 30 recorded execution times complies with a Normal distribution using `shapiro.test()`.

**Solution:**
```r
set.seed(123)
sample_lat <- rnorm(30, mean = 100, sd = 15)

# Execute Shapiro-Wilk test
shapiro_res <- shapiro.test(sample_lat)

cat("Shapiro-Wilk W:", round(shapiro_res$statistic, 4), "\n")
cat("Shapiro-Wilk p-value:", round(shapiro_res$p.value, 4), "\n")
```
