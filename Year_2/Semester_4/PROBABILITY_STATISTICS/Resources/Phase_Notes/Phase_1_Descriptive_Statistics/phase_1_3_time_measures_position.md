# Phase 1.3 (Time): Measures of Position for Time-Based Data

Measures of position (or quantiles) are values that divide a sorted dataset into equal parts. The most common are **Quartiles** (divided into 4 parts) and **Percentiles** (divided into 100 parts). When the data are **time-based**, quantiles become critically important in performance monitoring -- they are the **p50, p90, p95, p99 latency metrics** used in Service Level Agreements (SLAs).

---

## 1. Core Formulas (Time Context)

### Quantile Position (Ungrouped)
$$P = \frac{k(n+1)}{N_{parts}}$$
*   $k$: Quantile number (e.g., 1, 2, 3 for quartiles).
*   $n$: Total number of observations.
*   $N_{parts}$: 4 for quartiles, 100 for percentiles.

### Quantile Formula (Grouped Data)
$$Q = L + \left( \frac{\text{Position} - F_{i-1}}{f_i} \right) \cdot w$$
Where:
*   **Position** = $\frac{k \cdot n}{4}$ for quartiles or $\frac{k \cdot n}{100}$ for percentiles.
*   $L$ and $w$ are in the chosen time unit (e.g., ms, s).

> **SLA context:** The 95th percentile ($P_{95}$) of response time means 95% of requests completed within that time. If $P_{95} = 200\text{ ms}$, then only 5% of requests took longer than 200 ms.

---

## 2. Time-Specific Gotchas

### Gotcha 1: Percentile Interpretation Differs from Average

A common mistake is confusing $P_{95}$ with "95% of the mean." $P_{95}$ is the **value below which 95% of observations fall**, not a percentage of the average. For example, if the mean latency is 50 ms but $P_{95} = 200\text{ ms}$, the tail is 4x the average -- a sign of high variance in latency.

### Gotcha 2: Quantiles on Cyclic Clock Time

Just like the mean, quantiles on cyclic clock time are ill-defined without a reference point. If events span midnight (e.g., 23:50, 23:55, 00:05, 00:10), sorting them linearly places 00:05 and 00:10 "after" 23:55, but the true median is near midnight. Always define a reference epoch and convert to linear durations before computing quantiles.

### Gotcha 3: Unit Prefix and Percentile Scaling

Percentiles are in the **same unit** as the data. If data are in nanoseconds, $P_{99}$ is in nanoseconds. When converting units, the percentile value scales by the conversion factor:

$$P_{99}^{\text{ms}} = \frac{P_{99}^{\text{ns}}}{10^6}$$

Do not convert the **position** (which is a count), only the **value**.

---

## 3. Solved Exercises (10 Examples)

### Exercise 1: Quartiles for Small $n$ (Ungrouped Latency)

**Problem:** Find $Q_1, Q_2, Q_3$ for response times (ms): `5, 8, 4, 10, 15, 21, 2`.

**Solution:**
1.  Order: `2, 4, 5, 8, 10, 15, 21`. $n=7$.
2.  $Q_2$ (Median): 4th value = **8 ms**.
3.  $Q_1$: Median of lower half (`2, 4, 5`) = **4 ms**.
4.  $Q_3$: Median of upper half (`10, 15, 21`) = **15 ms**.

> **Interpretation:** $Q_3 = 15\text{ ms}$ means 75% of requests completed within 15 ms.

---

### Exercise 2: Percentile for Small $n$ (Ungrouped Duration)

**Problem:** Find $P_{80}$ for execution times (s): `10, 20, 30, 40, 50`.

**Solution:**
1.  Order: `10, 20, 30, 40, 50`. $n=5$.
2.  Position $P = \frac{80(5+1)}{100} = 4.8$.
3.  Interpolate between 4th (40 s) and 5th (50 s):
$$P_{80} = 40 + 0.8 \cdot (50 - 40) = 40 + 8 = \mathbf{48\text{ s}}$$

> **Interpretation:** 80% of executions completed within 48 seconds.

---

### Exercise 3: Grouped $Q_1$ for Latency Data (Interpolation)

**Problem:** $n=60,\ L=10\text{ ms},\ w=10\text{ ms},\ f_i=12,\ F_{i-1}=8$.

**Solution:**
1.  Position = $60/4 = 15$.
2.  $Q_1 = 10 + \left( \frac{15 - 8}{12} \right) \cdot 10 = 10 + \frac{70}{12} \approx \mathbf{15.83\text{ ms}}$.

> **Interpretation:** 25% of requests completed within 15.83 ms (the p25 latency).

---

### Exercise 4: Grouped $Q_3$ for Latency Data (Interpolation)

**Problem:** $n=60,\ L=30\text{ ms},\ w=10\text{ ms},\ f_i=15,\ F_{i-1}=40$.

**Solution:**
1.  Position = $(3 \cdot 60)/4 = 45$.
2.  $Q_3 = 30 + \left( \frac{45 - 40}{15} \right) \cdot 10 = 30 + \frac{50}{15} \approx \mathbf{33.33\text{ ms}}$.

> **Interpretation:** 75% of requests completed within 33.33 ms (the p75 latency).

---

### Exercise 5: Interquartile Range ($IQR$) for Latency

**Problem:** Using results from Ex 3 and 4 ($Q_1=15.83\text{ ms},\ Q_3=33.33\text{ ms}$), find the $IQR$.

**Solution:**
$$IQR = Q_3 - Q_1 = 33.33 - 15.83 = \mathbf{17.50\text{ ms}}$$

> **Interpretation:** The middle 50% of requests span 17.50 ms. A small IQR indicates consistent latency.

---

### Exercise 6: Percentile Rank (Grouped Latency)

**Problem:** In a latency distribution, find the 10th percentile ($P_{10}$) if $n=100$, and the first class is $[0, 20)\text{ ms}$ with $f_i=15$.

**Solution:**
1.  Position = $(10 \cdot 100)/100 = 10$.
2.  $P_{10}$ class is $[0, 20)\text{ ms}$ since $15 \ge 10$.
3.  $L=0,\ w=20,\ f_i=15,\ F_{i-1}=0$.
$$P_{10} = 0 + \left( \frac{10 - 0}{15} \right) \cdot 20 = \frac{200}{15} \approx \mathbf{13.33\text{ ms}}$$

> **Interpretation:** 10% of requests completed within 13.33 ms (the p10 latency).

---

### Exercise 7: Deciles ($D_k$) for Response Time

**Problem:** Find the 7th decile ($D_7$) for $n=50,\ L=40\text{ ms},\ w=10\text{ ms},\ f_i=8,\ F_{i-1}=30$.

**Solution:**
Deciles divide into 10 parts. $D_7 = P_{70}$.
1.  Position = $(70 \cdot 50)/100 = 35$.
2.  $D_7 = 40 + \left( \frac{35 - 30}{8} \right) \cdot 10 = 40 + 6.25 = \mathbf{46.25\text{ ms}}$.

> **Interpretation:** 70% of requests completed within 46.25 ms (the p70 latency).

---

### Exercise 8: Reverse Problem (Finding the Percentile of a Latency)

**Problem:** A response time of 45 ms falls in class $[40, 50)\text{ ms}$ where $f_i=10,\ F_{i-1}=30,\ n=50,\ w=10\text{ ms}$. What percentile is this latency?

**Solution:**
Set $P_k = 45\text{ ms}$ and solve for $k$:
$$45 = 40 + \left( \frac{\frac{k \cdot 50}{100} - 30}{10} \right) \cdot 10$$
$$5 = 0.5k - 30 \Rightarrow 0.5k = 35 \Rightarrow k = 70$$
The latency of 45 ms is at the **70th percentile** ($P_{70}$).

> **Interpretation:** A request taking 45 ms is faster than 70% of all requests.

---

### Exercise 9: Unit Conversion for Percentiles

**Problem:** The $P_{99}$ latency is measured as $2\,500\,000\text{ ns}$. Convert this to milliseconds and microseconds.

**Solution:**
1.  To microseconds: $2\,500\,000\text{ ns} / 1000 = \mathbf{2\,500\ \mu\text{s}}$.
2.  To milliseconds: $2\,500\,000\text{ ns} / 10^6 = \mathbf{2.5\text{ ms}}$.

> **Gotcha reminder:** The percentile **rank** (99) does not change when converting units. Only the **value** scales. The position calculation (a count of observations) is unit-independent.

---

### Exercise 10: R Snippet -- Computing SLA Percentiles

**Problem:** Use R to compute the p50, p90, p95, and p99 latencies for: `120, 135, 142, 120, 158, 135, 170, 142, 120, 190, 210, 95, 130, 145, 160` (ms).

**Solution:**

```r
# Response times in milliseconds
latency_ms <- c(120, 135, 142, 120, 158, 135, 170, 142, 120, 190, 210, 95, 130, 145, 160)

# Compute SLA percentiles
p50 <- quantile(latency_ms, probs = 0.50)
p90 <- quantile(latency_ms, probs = 0.90)
p95 <- quantile(latency_ms, probs = 0.95)
p99 <- quantile(latency_ms, probs = 0.99)

cat("p50 (median):", p50, "ms\n")
cat("p90:", p90, "ms\n")
cat("p95:", p95, "ms\n")
cat("p99:", p99, "ms\n")

# Five-number summary
fivenum(latency_ms)
```

**Expected output:**
```
p50 (median): 142 ms
p90: 190 ms
p95: 200 ms
p99: 209 ms
```

> **R note:** The `quantile()` function uses linear interpolation by default (type 7), which matches the manual interpolation method taught in this course. The five-number summary (`fivenum()`) gives min, $Q_1$, median, $Q_3$, max -- the components of a boxplot.

---

## Exam Tip: The Five-Number Summary (Time Context)

Many exams ask for this summary to describe a dataset:
1.  Minimum (fastest time)
2.  $Q_1$ (p25 latency)
3.  Median ($Q_2$, p50 latency)
4.  $Q_3$ (p75 latency)
5.  Maximum (slowest time)

These are also the components used to draw a **Boxplot**. In latency analysis, the boxplot visually reveals the spread of typical response times and highlights timeout outliers beyond the upper fence.