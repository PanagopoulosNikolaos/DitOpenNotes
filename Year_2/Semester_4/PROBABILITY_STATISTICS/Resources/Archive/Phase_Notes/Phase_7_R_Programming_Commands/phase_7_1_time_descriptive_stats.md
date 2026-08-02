# Phase 7.1 (Time): Descriptive Statistics in R for Time-Series Data

In R, analyzing time metrics—such as request latencies, processing durations, and system timestamps—requires specialized commands for summary statistics, percentile estimation, and dispersion calculations.

---

## 1. Core Summary Functions for Continuous Time Data

| Metric / Function | R Command | Description |
| :--- | :--- | :--- |
| **Mean Duration** | `mean(x, na.rm = TRUE)` | Calculates sample mean latency $\bar{T}$. |
| **Median Duration** | `median(x, na.rm = TRUE)` | Calculates 50th percentile response time. |
| **Variance** | `var(x, na.rm = TRUE)` | Calculates sample variance $s_T^2$ (with $n-1$ denominator). |
| **Standard Deviation** | `sd(x, na.rm = TRUE)` | Calculates sample standard deviation $s_T$. |
| **Interquartile Range** | `IQR(x, na.rm = TRUE)` | Calculates $Q_3 - Q_1$ (middle $50\%$ spread). |
| **Percentiles / Quantiles**| `quantile(x, probs = c(...))` | Calculates specified percentile SLA thresholds. |
| **Summary Vector** | `summary(x)` | Returns Min, $Q_1$, Median, Mean, $Q_3$, Max. |

---

## 2. Handling Time Data Vectors and Outliers

When parsing raw performance logs:
1. **Missing Data (`NA`):** Always set `na.rm = TRUE` to prevent `NA` propagation.
2. **Filtering Outlier Latencies:** Trim extreme spikes using quantile bounds or the `trim` argument in `mean(x, trim = 0.05)`.

---

## 3. Time-Specific R Gotchas

### Gotcha 1: Sample Variance Uses $n-1$ (Unbiased Estimator)
R's `var()` and `sd()` functions divide by $n - 1$ (sample variance $s_T^2$). If you require population variance $\sigma_T^2$ (divided by $n$), you must multiply the result by $\frac{n - 1}{n}$.

### Gotcha 2: Datetime Vector Format (`POSIXct` vs Numeric Durations)
When working with timestamps, `difftime()` objects have units (seconds, minutes, hours). Convert them to explicit numeric values using `as.numeric(d, units = "secs")` before applying mathematical operations.

---

## 4. Solved R Code Examples (10 Exercises)

### Exercise 1: Basic Descriptive Statistics on Response Times
**Problem:** Given a numeric vector of 10 microservice response times in milliseconds, compute the sample mean, median, standard deviation, and variance in R.

**Solution:**
```r
# Input latency metrics in milliseconds
latencies <- c(120, 145, 110, 160, 130, 210, 125, 135, 140, 150)

# Calculate descriptive statistics
mean_lat <- mean(latencies)
med_lat  <- median(latencies)
sd_lat   <- sd(latencies)
var_lat  <- var(latencies)

cat("Mean Latency:", mean_lat, "ms\n")
cat("Median Latency:", med_lat, "ms\n")
cat("Standard Deviation:", round(sd_lat, 2), "ms\n")
cat("Variance:", round(var_lat, 2), "ms^2\n")
```

---

### Exercise 2: Percentile SLA Calculations ($p_{50}, p_{90}, p_{95}, p_{99}$)
**Problem:** Calculate the 50th, 90th, 95th, and 99th percentile SLA bounds for a sample of 20 log durations.

**Solution:**
```r
# Sample log durations in seconds
durations <- c(1.2, 1.5, 1.1, 1.8, 1.3, 2.5, 1.4, 1.6, 1.7, 1.2,
               1.9, 2.1, 1.3, 1.4, 3.8, 1.5, 1.6, 1.7, 2.0, 4.5)

# Calculate specified quantiles
sla_quantiles <- quantile(durations, probs = c(0.50, 0.90, 0.95, 0.99))
print(sla_quantiles)
```

---

### Exercise 3: Interquartile Range (IQR) and Boxplot Boundaries
**Problem:** Compute $Q_1$, $Q_3$, and $IQR$ for ping delays and identify the upper fence for outlier detection ($Q_3 + 1.5 \times IQR$).

**Solution:**
```r
pings <- c(35, 38, 42, 40, 37, 39, 41, 36, 45, 85, 38, 40)

q1 <- quantile(pings, 0.25)
q3 <- quantile(pings, 0.75)
iqr_val <- IQR(pings)

upper_fence <- q3 + 1.5 * iqr_val

cat("Q1:", q1, "ms\n")
cat("Q3:", q3, "ms\n")
cat("IQR:", iqr_val, "ms\n")
cat("Outlier Upper Fence:", upper_fence, "ms\n")
```

---

### Exercise 4: Trimming Outlier Latencies from Means
**Problem:** Compare the standard mean vs the $5\%$ trimmed mean (`trim = 0.05`) for latency data containing extreme spikes.

**Solution:**
```r
raw_latencies <- c(100, 102, 98, 105, 101, 99, 103, 1500) # 1500 is a spike

standard_mean <- mean(raw_latencies)
trimmed_mean  <- mean(raw_latencies, trim = 0.05)

cat("Standard Mean:", standard_mean, "ms\n")
cat("Trimmed Mean:", trimmed_mean, "ms\n")
```

---

### Exercise 5: Converting Datetime Differences to Numeric Durations
**Problem:** Compute elapsed time between start and end timestamps in seconds and compute mean duration.

**Solution:**
```r
start_times <- as.POSIXct(c("2026-08-02 10:00:00", "2026-08-02 10:05:00", "2026-08-02 10:10:00"))
end_times   <- as.POSIXct(c("2026-08-02 10:00:15", "2026-08-02 10:05:42", "2026-08-02 10:11:05"))

# Compute differences in seconds
durations_sec <- as.numeric(difftime(end_times, start_times, units = "secs"))

cat("Durations (s):", durations_sec, "\n")
cat("Mean Duration (s):", mean(durations_sec), "\n")
```

---

### Exercise 6: Converting Sample Variance to Population Variance
**Problem:** Write an R snippet to compute population variance $\sigma_T^2$ (dividing by $n$) from sample variance `var()`.

**Solution:**
```r
latencies <- c(50, 55, 60, 45, 50)
n <- length(latencies)

sample_var <- var(latencies)
pop_var    <- sample_var * ((n - 1) / n)

cat("Sample Variance (n-1):", sample_var, "\n")
cat("Population Variance (n):", pop_var, "\n")
```

---

### Exercise 7: Five-Number Summary and Standardized Z-Scores
**Problem:** Compute standardized z-scores $Z = (T - \bar{T}) / s_T$ for a vector of request durations.

**Solution:**
```r
durations <- c(10, 12, 11, 15, 20, 9, 13)

# Calculate z-scores
z_scores <- (durations - mean(durations)) / sd(durations)

# Alternatively using R scale() function
z_scores_scale <- as.vector(scale(durations))

print(data.frame(Duration = durations, Z_Score = round(z_scores, 3)))
```

---

### Exercise 8: Handling Missing Log Values (`NA`)
**Problem:** Compute mean and standard deviation for a latency vector containing `NA` values.

**Solution:**
```r
log_times <- c(120, NA, 135, 110, NA, 140, 125)

mean_clean <- mean(log_times, na.rm = TRUE)
sd_clean   <- sd(log_times, na.rm = TRUE)

cat("Clean Mean:", round(mean_clean, 2), "ms\n")
cat("Clean SD:", round(sd_clean, 2), "ms\n")
```

---

### Exercise 9: Grouped Descriptive Statistics by Region
**Problem:** Compute mean and $p_{95}$ latency grouped by server region using base R `aggregate()`.

**Solution:**
```r
df <- data.frame(
  region = c("US", "US", "US", "EU", "EU", "EU"),
  latency = c(45, 50, 48, 120, 135, 115)
)

# Mean latency by region
mean_by_reg <- aggregate(latency ~ region, data = df, FUN = mean)
p95_by_reg  <- aggregate(latency ~ region, data = df, FUN = function(x) quantile(x, 0.95))

print(mean_by_reg)
print(p95_by_reg)
```

---

### Exercise 10: Coefficient of Variation ($CV = s_T / \bar{T}$) for Latency Stability
**Problem:** Compute the Coefficient of Variation ($CV$) to compare latency relative volatility between System A and System B.

**Solution:**
```r
sys_A <- c(100, 105, 95, 102, 98)  # Mean = 100
sys_B <- c(10, 15, 5, 12, 8)       # Mean = 10

cv_A <- sd(sys_A) / mean(sys_A)
cv_B <- sd(sys_B) / mean(sys_B)

cat("System A CV:", round(cv_A, 4), "\n")
cat("System B CV:", round(cv_B, 4), "\n")
```
