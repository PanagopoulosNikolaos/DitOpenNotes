# Phase 7.4 (Time): Additional Continuous Distributions in R for Time Data

In performance engineering and statistical modeling, analyzing non-normal time metrics requires specialized continuous distribution functions in R: Exponential, Gamma, Weibull, Uniform, Chi-Square, F, and Student's t.

---

## 1. R Command Matrix for Continuous Time Distributions

| Distribution | R Prefix | Parameter Inputs | Primary Time Domain Application |
| :--- | :--- | :--- | :--- |
| **Exponential** | `exp` | `rate = lambda` ($1/\mu$) | Waiting time between Poisson events / component survival. |
| **Gamma** | `gamma` | `shape = alpha, rate = beta` | Cumulative waiting time until $k$-th Poisson event. |
| **Weibull** | `weibull`| `shape = k, scale = lambda` | Component time-to-failure with aging or burn-in. |
| **Uniform** | `unif` | `min = a, max = b` | Random backoff delay / jitter over bounded interval. |
| **Chi-Square** | `chisq` | `df = n - 1` | Single system latency variance testing. |
| **F-Distribution** | `f` | `df1, df2` | Ratio of latency variances across two cloud platforms. |
| **Student's t** | `t` | `df = n - 1` | Hypothesis testing and CIs on small sample mean latency. |

---

## 2. Time-Specific R Gotchas

### Gotcha 1: Rate vs Scale Parameter Syntax in R (`pgamma` & `pexp`)
* In `pexp(q, rate)`, `rate` $= \lambda = 1 / \text{mean}$.
* In `pgamma(q, shape, rate)`, passing `rate = beta` means $E[T] = \text{shape} / \text{rate}$. If you specify `scale = theta`, then $E[T] = \text{shape} \times \text{scale}$. Confusing `rate` and `scale` produces inverted calculations!

### Gotcha 2: Weibull Parameter Convention in R
R's `pweibull(q, shape, scale)` defines the scale parameter as $\lambda$ (where scale has the same time units as $q$, e.g., hours). The survival function in R is `pweibull(q, shape, scale, lower.tail = FALSE)` $= \exp(-(q / \text{scale})^{\text{shape}})$.

---

## 3. Solved R Code Examples (10 Exercises)

### Exercise 1: Exponential Component Failure Probability (`pexp`)
**Problem:** Server time-to-crash $T \sim \text{Exp}(\text{rate} = 0.002\text{ h}^{-1})$. Compute the probability of server failure within the first $500$ hours.

**Solution:**
```r
rate_val <- 0.002

# P(T <= 500 hours)
p_fail_500 <- pexp(q = 500, rate = rate_val)
cat("P(T <= 500 h):", round(p_fail_500, 4), "\n")
```

---

### Exercise 2: Exponential Component Reliability / Survival (`lower.tail = FALSE`)
**Problem:** Calculate the survival probability $P(T > 1000\text{ hours})$ for the server in Exercise 1.

**Solution:**
```r
p_surv_1000 <- pexp(q = 1000, rate = 0.002, lower.tail = FALSE)
cat("P(T > 1000 h):", round(p_surv_1000, 4), "\n")
```

---

### Exercise 3: Gamma Waiting Time Distribution for $k=4$ Events (`pgamma`)
**Problem:** API requests arrive at rate $\beta = 0.5$ per second. Calculate the probability that the cumulative waiting time for the 4th request ($T \sim \text{Gamma}(\text{shape}=4, \text{rate}=0.5)$) is $\le 10$ seconds.

**Solution:**
```r
p_gamma_10 <- pgamma(q = 10, shape = 4, rate = 0.5)
cat("P(T_4 <= 10 s):", round(p_gamma_10, 4), "\n")
```

---

### Exercise 4: Weibull Reliability with Wear-Out Aging (`pweibull`)
**Problem:** Hardware component failure time $T \sim \text{Weibull}(\text{shape}=2.5, \text{scale}=2000\text{ hours})$. Compute survival probability beyond $1500$ hours.

**Solution:**
```r
p_weibull_surv <- pweibull(q = 1500, shape = 2.5, scale = 2000, lower.tail = FALSE)
cat("Weibull P(T > 1500 h):", round(p_weibull_surv, 4), "\n")
```

---

### Exercise 5: Continuous Uniform Backoff Delay (`punif` & `qunif`)
**Problem:** Network backoff delay $T \sim U(10\text{ ms}, 60\text{ ms})$. Calculate $P(T > 45\text{ ms})$ and the 90th percentile backoff duration.

**Solution:**
```r
p_unif_45 <- punif(q = 45, min = 10, max = 60, lower.tail = FALSE)
q_90 <- qunif(p = 0.90, min = 10, max = 60)

cat("P(T > 45 ms):", round(p_unif_45, 4), "\n")
cat("90th percentile backoff:", q_90, "ms\n")
```

---

### Exercise 6: Chi-Square Distribution Critical Values (`qchisq` & `pchisq`)
**Problem:** Calculate upper $5\%$ critical value $\chi_{0.05, 20}^2$ and p-value for test statistic $\chi^2 = 32.5$ ($df = 20$).

**Solution:**
```r
crit_val_chi <- qchisq(p = 0.05, df = 20, lower.tail = FALSE)
p_val_chi    <- pchisq(q = 32.5, df = 20, lower.tail = FALSE)

cat("Chi-Square Critical Value (alpha=0.05):", round(crit_val_chi, 3), "\n")
cat("Chi-Square p-value:", round(p_val_chi, 4), "\n")
```

---

### Exercise 7: F-Distribution Quantiles for Latency Variance Ratios (`qf` & `pf`)
**Problem:** Calculate critical value $F_{0.05, 15, 20}$ and p-value for sample variance ratio $F = 2.80$.

**Solution:**
```r
crit_val_f <- qf(p = 0.05, df1 = 15, df2 = 20, lower.tail = FALSE)
p_val_f    <- pf(q = 2.80, df1 = 15, df2 = 20, lower.tail = FALSE)

cat("F Critical Value (alpha=0.05):", round(crit_val_f, 3), "\n")
cat("F-test p-value:", round(p_val_f, 4), "\n")
```

---

### Exercise 8: Student's t-Distribution Probabilities and Quantiles (`pt` & `qt`)
**Problem:** Find two-tailed critical value $t_{0.025, 15}$ and calculate $P(t_{15} \le -2.15)$.

**Solution:**
```r
crit_t <- qt(p = 0.025, df = 15, lower.tail = FALSE)
p_left <- pt(q = -2.15, df = 15)

cat("t Critical Value (df=15):", round(crit_t, 3), "\n")
cat("P(t_15 <= -2.15):", round(p_left, 4), "\n")
```

---

### Exercise 9: Generating Random Variates across Continuous Time Distributions
**Problem:** Generate $5$ random samples each from Exponential, Gamma, Weibull, and Uniform time models in R.

**Solution:**
```r
set.seed(42)

exp_samples   <- rexp(5, rate = 0.1)
gamma_samples <- rgamma(5, shape = 2, rate = 0.5)
weib_samples  <- rweibull(5, shape = 2, scale = 100)
unif_samples  <- runif(5, min = 10, max = 50)

print(data.frame(Exponential = round(exp_samples, 2),
                 Gamma = round(gamma_samples, 2),
                 Weibull = round(weib_samples, 2),
                 Uniform = round(unif_samples, 2)))
```

---

### Exercise 10: Comparative Density Plot of Latency Models in R
**Problem:** Write R code to evaluate Exponential vs Gamma density curves for time-to-event metrics.

**Solution:**
```r
t_grid <- seq(0, 20, by = 0.1)

# Compute density vectors
y_exp   <- dexp(t_grid, rate = 0.5)
y_gamma <- dgamma(t_grid, shape = 3, rate = 0.5)

# Density comparison data frame
dens_df <- data.frame(Time = t_grid, Exp_Density = round(y_exp, 4), Gamma_Density = round(y_gamma, 4))
head(dens_df, 10)
```
