# Tutorial 01: Statistical Data Analysis and Visualization in R

This laboratory tutorial introduces R programming fundamentals for statistical data processing: creating vectors and data frames, computing summary metrics (mean, median, variance, quantiles), and generating publication-ready exploratory plots (histograms, boxplots).

---

## 1. R Data Structures and Summary Statistics

### 1.1 Vectors and Data Frames

```R
# Creating a numeric vector of measured network latencies (in ms)
latencies <- c(22.4, 25.1, 19.8, 30.5, 24.2, 28.9, 21.0, 23.5, 35.2, 26.8)

# Creating a structured data frame
telemetry <- data.frame(
  packet_id = 1:10,
  latency = latencies,
  status = factor(c("OK", "OK", "OK", "SLOW", "OK", "OK", "OK", "OK", "SLOW", "OK"))
)
```

### 1.2 Descriptive Statistical Metrics in Base R

```R
# Arithmetic Mean
mean_val <- mean(latencies)

# Median
median_val <- median(latencies)

# Sample Variance (unbiased, denominator n - 1)
var_val <- var(latencies)

# Sample Standard Deviation
sd_val <- sd(latencies)

# Five-number summary (Min, Q1, Median, Mean, Q3, Max)
summary(latencies)

# Specific Quantiles (25th, 50th, 75th, 90th percentiles)
quantile(latencies, probs = c(0.25, 0.50, 0.75, 0.90))

# Interquartile Range (IQR = Q3 - Q1)
iqr_val <- IQR(latencies)

# Coefficient of Variation (CV = (s / mean) * 100)
cv_val <- (sd_val / mean_val) * 100
```

---

## 2. Exploratory Data Visualization

### 2.1 Frequency Histogram with Density Curve

```R
# Plotting histogram with density scaling
hist(latencies,
     breaks = 5,
     col = "lightblue",
     main = "Empirical Distribution of Network Latency",
     xlab = "Latency (milliseconds)",
     ylab = "Density",
     freq = FALSE)

# Overlay kernel density estimate
lines(density(latencies), col = "darkblue", lwd = 2)

# Overlay vertical line for sample mean
abline(v = mean_val, col = "red", lwd = 2, lty = 2)
```

### 2.2 Boxplot Analysis (Outlier Detection)

```R
# Horizontal boxplot with Tukey fences
boxplot(latencies,
        horizontal = TRUE,
        col = "lightgreen",
        main = "Latency Distribution Boxplot",
        xlab = "Latency (ms)")
```

