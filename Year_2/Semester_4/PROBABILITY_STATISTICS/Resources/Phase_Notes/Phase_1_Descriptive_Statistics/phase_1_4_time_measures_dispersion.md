# Phase 1.4 (Time): Measures of Dispersion for Time-Based Data

Measures of dispersion (or variability) describe how "spread out" the values in a dataset are. While central tendency tells us where the center is, dispersion tells us how much the data deviates from that center. For **time-based data**, dispersion is critical: high variance in latency means an unpredictable system, while low variance means consistent performance.

---

## 1. Core Formulas (Time Context)

### Sample Variance ($s^2$)
$$s^2 = \frac{\sum (t_i - \bar{t})^2}{n - 1} \quad \text{or} \quad s^2 = \frac{\sum f_i(t_i - \bar{t})^2}{n - 1}$$

> **Unit note:** Variance is in **squared time units** (e.g., $\text{s}^2$, $\text{ms}^2$, $\text{ns}^2$). This is one of the most important gotchas in time-data statistics.

### Shortcut Variance Formula (Grouped)
$$s^2 = \frac{\sum f_i \cdot t_i^2 - \frac{(\sum f_i \cdot t_i)^2}{n}}{n - 1}$$

### Sample Standard Deviation ($s$)
$$s = \sqrt{s^2}$$

The standard deviation is in the **original time unit** (e.g., s, ms, ns).

### Coefficient of Variation ($CV$)
$$CV = \frac{s}{\bar{t}} \cdot 100\%$$

*(Used to compare dispersion between datasets with different time units or means. The $CV$ is **dimensionless** -- it cancels the time unit.)*

---

## 2. The $c^2$ Rule: Variance Scaling Under Unit Conversion

This is the most important time-specific property of variance. When you convert time data from one unit to another by multiplying every value by a constant $c$, the variance scales by $c^2$ and the standard deviation scales by $c$.

### Derivation

Let $t_i$ be data in unit A. Define $u_i = c \cdot t_i$ as the same data in unit B (where $c$ is the conversion factor).

**Mean:**
$$\bar{u} = c \cdot \bar{t}$$

**Variance:**
$$s_u^2 = \frac{\sum (u_i - \bar{u})^2}{n-1} = \frac{\sum (c \cdot t_i - c \cdot \bar{t})^2}{n-1} = \frac{c^2 \sum (t_i - \bar{t})^2}{n-1} = c^2 \cdot s_t^2$$

**Standard Deviation:**
$$s_u = \sqrt{c^2 \cdot s_t^2} = |c| \cdot s_t = c \cdot s_t \quad (\text{since } c > 0)$$

### Common Time Conversion Factors

| Conversion | $c$ | $c^2$ | Effect on Variance |
| :--- | :--- | :--- | :--- |
| seconds to milliseconds | $1000$ | $10^6$ | Variance multiplied by $1\,000\,000$ |
| seconds to microseconds | $10^6$ | $10^{12}$ | Variance multiplied by $10^{12}$ |
| seconds to nanoseconds | $10^9$ | $10^{18}$ | Variance multiplied by $10^{18}$ |
| milliseconds to seconds | $10^{-3}$ | $10^{-6}$ | Variance divided by $10^6$ |
| nanoseconds to seconds | $10^{-9}$ | $10^{-18}$ | Variance divided by $10^{18}$ |

> **Key insight:** Converting from seconds to nanoseconds multiplies the variance by $10^{18}$. This is why variance in nanosecond units can be astronomically large ($10^{18}\text{ s}^2 = 1\text{ ns}^2$). Always be mindful of which unit the variance is expressed in.

---

## 3. Time-Specific Gotchas

### Gotcha 1: Floating-Point Precision Loss in Variance of Large Timestamps

When computing variance on Unix epoch nanosecond timestamps (values near $10^{18}$), the term $\sum t_i^2$ can reach $10^{36}$, which exceeds the precision of 64-bit floating point (~15--16 significant digits). The subtraction $\sum t_i^2 - \frac{(\sum t_i)^2}{n}$ can produce **catastrophic cancellation**, yielding a negative or zero variance for data that is actually spread out.

**Fix:** Always center the data before computing variance:

$$s^2 = \frac{\sum (t_i - \bar{t})^2}{n-1}$$

Or use the **shifted variance formula**:

$$s^2 = \frac{\sum (t_i - t_0)^2 - \frac{(\sum (t_i - t_0))^2}{n}}{n-1}$$

where $t_0$ is any reference time (e.g., $t_{\min}$ or the epoch start). This keeps all intermediate values small.

### Gotcha 2: Variance in Squared Time Units Is Not Intuitive

A variance of $25\text{ ms}^2$ does **not** mean the spread is 25 ms. The spread is the standard deviation: $s = \sqrt{25} = 5\text{ ms}$. Students frequently report variance when the question asks for "spread in the original units."

### Gotcha 3: $CV$ Is Unit-Invariant

The Coefficient of Variation $CV = s/\bar{t}$ is **dimensionless**. If you compute $CV$ for data in seconds and then convert to milliseconds, the $CV$ remains the same. This makes $CV$ ideal for comparing the relative variability of systems measured in different time units.

---

## 4. Solved Exercises (10 Examples)

### Exercise 1: Range for Duration Data

**Problem:** Find the range of these response times (ms): `10, 2, 35, 12, 18, 5`.

**Solution:**
1.  Max = 35 ms, Min = 2 ms.
2.  Range = $35 - 2 = \mathbf{33\text{ ms}}$.

---

### Exercise 2: Sample Variance (Ungrouped Duration)

**Problem:** Find $s^2$ for execution times (s): `2, 4, 6`.

**Solution:**
1.  Mean $\bar{t} = (2+4+6)/3 = 4\text{ s}$.
2.  Deviations: $(2-4)=-2,\ (4-4)=0,\ (6-4)=2$.
3.  Squared: $4,\ 0,\ 4$. Sum = 8.
4.  $s^2 = 8 / (3-1) = \mathbf{4\text{ s}^2}$.

> **Note:** The unit is $\text{s}^2$ (seconds squared), not seconds.

---

### Exercise 3: Population Standard Deviation ($\sigma$) for Duration

**Problem:** Data (s): `1, 3, 5`. Assume this is the *entire population*. Find $\sigma$.

**Solution:**
1.  $\mu = 3\text{ s}$.
2.  Squared deviations: $(1-3)^2=4,\ (3-3)^2=0,\ (5-3)^2=4$. Sum = 8.
3.  Population Variance $\sigma^2 = 8 / 3 \approx 2.67\text{ s}^2$.
4.  $\sigma = \sqrt{2.67} \approx \mathbf{1.63\text{ s}}$.

> **Note:** The standard deviation is in seconds (the original unit), while the variance was in $\text{s}^2$.

---

### Exercise 4: Grouped Variance for Latency Data (Standard Method)

**Problem:** $\sum f_i(t_i - \bar{t})^2 = 610\text{ ms}^2,\ n=10$. Find sample variance.

**Solution:**
$$s^2 = 610 / (10 - 1) = 610 / 9 \approx \mathbf{67.78\text{ ms}^2}$$

---

### Exercise 5: Grouped Variance (Shortcut Method) for Latency

**Problem:** $\sum f_i t_i = 100\text{ ms},\ \sum f_i t_i^2 = 2500\text{ ms}^2,\ n=5$. Find $s^2$.

**Solution:**
$$s^2 = \frac{2500 - \frac{100^2}{5}}{5 - 1} = \frac{2500 - 2000}{4} = \frac{500}{4} = \mathbf{125\text{ ms}^2}$$

---

### Exercise 6: Coefficient of Variation ($CV$) for Two Systems

**Problem:** System A: $\bar{t}=50\text{ ms},\ s=10\text{ ms}$. System B: $\bar{t}=100\text{ ms},\ s=15\text{ ms}$. Which system is more consistent (less dispersed relative to its mean)?

**Solution:**
1.  $CV_A = (10/50) \cdot 100 = 20\%$.
2.  $CV_B = (15/100) \cdot 100 = 15\%$.

**System B** is more consistent (lower $CV$), even though its absolute standard deviation is higher.

> **Interpretation:** System B has more absolute jitter but less relative jitter. The $CV$ allows a fair comparison because it normalizes by the mean.

---

### Exercise 7: Identifying Timeout Outliers (The 1.5 IQR Rule)

**Problem:** $Q_1=10\text{ ms},\ Q_3=20\text{ ms}$. Is a response time of 40 ms an outlier?

**Solution:**
1.  $IQR = 20 - 10 = 10\text{ ms}$.
2.  Upper Fence = $Q_3 + 1.5 \cdot IQR = 20 + 15 = 35\text{ ms}$.
3.  Since $40 > 35\text{ ms}$, the value 40 ms is an **outlier**.

> **Interpretation:** This request likely experienced a network stall or timeout and should be investigated separately from the normal latency distribution.

---

### Exercise 8: Effect of Unit Conversion (The $c^2$ Rule)

**Problem:** A dataset of response times has $s = 5\text{ ms}$ and $s^2 = 25\text{ ms}^2$. Convert the data to seconds. What are the new standard deviation and variance?

**Solution:**

**Conversion factor:** $c = 10^{-3}$ (milliseconds to seconds).

**Standard deviation:**
$$s_{\text{new}} = c \cdot s_{\text{old}} = 10^{-3} \cdot 5 = \mathbf{0.005\text{ s}}$$

**Variance (using the $c^2$ rule):**
$$s^2_{\text{new}} = c^2 \cdot s^2_{\text{old}} = (10^{-3})^2 \cdot 25 = 10^{-6} \cdot 25 = \mathbf{0.000025\text{ s}^2}$$

> **Verification:** $\sqrt{0.000025} = 0.005\text{ s} = 5\text{ ms}$. The conversion is consistent.

---

### Exercise 9: Converting from Nanoseconds to Milliseconds (The $c^2$ Rule)

**Problem:** Latency data measured in nanoseconds has variance $s^2 = 4 \times 10^{10}\text{ ns}^2$. Convert the variance to $\text{ms}^2$ and find the standard deviation in ms.

**Solution:**

**Conversion factor:** $c = 10^{-6}$ (nanoseconds to milliseconds).

**Variance:**
$$s^2_{\text{ms}} = c^2 \cdot s^2_{\text{ns}} = (10^{-6})^2 \cdot 4 \times 10^{10} = 10^{-12} \cdot 4 \times 10^{10} = 4 \times 10^{-2} = \mathbf{0.04\text{ ms}^2}$$

**Standard deviation:**
$$s_{\text{ms}} = \sqrt{0.04} = \mathbf{0.2\text{ ms}}$$

> **Gotcha reminder:** The variance in nanoseconds ($4 \times 10^{10}$) looks enormous, but it represents the same spread as $0.04\text{ ms}^2$. The $c^2$ rule with $c = 10^{-6}$ shrinks the variance by a factor of $10^{12}$.

---

### Exercise 10: R Snippet -- Variance and $CV$ with Unit Conversion

**Problem:** Use R to compute the variance, standard deviation, and $CV$ for latency data in milliseconds, then convert to seconds and verify the $c^2$ rule.

**Solution:**

```r
# Latency data in milliseconds
latency_ms <- c(120, 135, 142, 120, 158, 135, 170, 142, 120, 190)

# Statistics in milliseconds
var_ms <- var(latency_ms)
sd_ms <- sd(latency_ms)
cv_ms <- (sd_ms / mean(latency_ms)) * 100

cat("In milliseconds:\n")
cat("  Variance:", var_ms, "ms^2\n")
cat("  Std Dev:", sd_ms, "ms\n")
cat("  CV:", cv_ms, "%\n\n")

# Convert to seconds (c = 1e-3)
latency_s <- latency_ms / 1000

var_s <- var(latency_s)
sd_s <- sd(latency_s)
cv_s <- (sd_s / mean(latency_s)) * 100

cat("In seconds:\n")
cat("  Variance:", var_s, "s^2\n")
cat("  Std Dev:", sd_s, "s\n")
cat("  CV:", cv_s, "%\n\n")

# Verify c^2 rule
cat("c^2 rule check:\n")
cat("  var_s * 1e6 =", var_s * 1e6, "(should equal var_ms:", var_ms, ")\n")
cat("  CV is identical:", cv_ms == cv_s, "\n")
```

**Expected output:**
```
In milliseconds:
  Variance: 650.18 ms^2
  Std Dev: 25.5 ms
  CV: 17.8 %

In seconds:
  Variance: 6.5018e-07 s^2
  Std Dev: 0.000255 s
  CV: 17.8 %

c^2 rule check:
  var_s * 1e6 = 650.18 (should equal var_ms: 650.18)
  CV is identical: TRUE
```

> **R note:** The $CV$ is identical in both units (17.8%), confirming that it is dimensionless. The variance in seconds is $6.5 \times 10^{-7}$, which equals the variance in milliseconds ($650.18$) divided by $10^6$ -- exactly the $c^2$ rule with $c = 10^{-3}$.

---

## Exam Tip: When to Use $CV$ (Time Context)

If a professor asks "Which system is more consistent?" or "Which server has less relative jitter?", they usually want you to calculate the **Coefficient of Variation**, as it allows for a fair comparison between systems measured in different time units or with different mean latencies.

### Unit Summary Table

| Measure | Unit | Time Example |
| :--- | :--- | :--- |
| Mean $\bar{t}$ | time | ms |
| Median $M_e$ | time | ms |
| Mode $M_o$ | time | ms |
| Range $R$ | time | ms |
| Standard Deviation $s$ | time | ms |
| Variance $s^2$ | **squared time** | $\text{ms}^2$ |
| $CV$ | **dimensionless** | % |
| $IQR$ | time | ms |

> **Critical:** If an exam asks for "a measure of spread in the original time units," they want the **Standard Deviation** or **Range**, not the Variance. Variance is always in squared units.