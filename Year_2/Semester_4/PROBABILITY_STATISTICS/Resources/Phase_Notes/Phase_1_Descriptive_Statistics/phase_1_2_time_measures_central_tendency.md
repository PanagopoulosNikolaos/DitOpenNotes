# Phase 1.2 (Time): Measures of Central Tendency for Time-Based Data

Measures of central tendency are statistical values that represent the "center" or "typical" value of a dataset. The three most common measures are the **Mean**, **Median**, and **Mode**. When the data are **time-based** (durations, latencies, timestamps), these measures require careful handling of **units, linear vs. cyclic time, and floating-point precision**.

---

## 1. Core Formulas (Time Context)

### Mean ($\bar{t}$)
*   **Ungrouped:** $\bar{t} = \frac{\sum t_i}{n}$ (average duration / average timestamp)
*   **Grouped:** $\bar{t} = \frac{\sum f_i \cdot t_i}{n}$ where $t_i$ is the class mark (midpoint time)

> **Cyclic time gotcha:** The arithmetic mean is **invalid for cyclic (circular) clock times**. Averaging 23:00 and 01:00 naively gives 12:00 (noon), but the true circular mean is 00:00 (midnight). For cyclic time, use the **circular mean** (see Gotcha 2 below).

### Median ($M_e$)
*   **Ungrouped:** Middle value (or average of two middle values) in an ordered list of time measurements.
*   **Grouped (Interpolation):** $M_e = L + \left( \frac{\frac{n}{2} - F_{i-1}}{f_i} \right) \cdot w$ where $L$ and $w$ are in the chosen time unit.

> The median is robust for time data: it represents the "typical" duration and is unaffected by extreme latency outliers.

### Mode ($M_o$)
*   **Ungrouped:** Most frequent time value (e.g., the most common response time).
*   **Grouped (Interpolation):** $M_o = L + \left( \frac{f_i - f_{i-1}}{(f_i - f_{i-1}) + (f_i - f_{i+1})} \right) \cdot w$

---

## 2. Time-Specific Gotchas

### Gotcha 1: Arithmetic Mean Fails on Cyclic Clock Time

Clock times live on a 24-hour circle. The naive arithmetic mean of 23:00 and 01:00 is:

$$\frac{23 + 1}{2} = 12 \text{ (noon)}$$

But the correct answer is **00:00 (midnight)** -- the two times are 2 hours apart, centered at midnight. The fix is the **circular mean**:

1.  Convert each clock time to an angle: $\theta_i = \frac{2\pi \cdot t_i}{24}$ (for 24-hour format).
2.  Compute: $\bar{\theta} = \text{atan2}\left(\sum \sin\theta_i,\ \sum \cos\theta_i\right)$
3.  Convert back: $\bar{t} = \frac{24 \cdot \bar{\theta}}{2\pi}$ (mod 24).

### Gotcha 2: Floating-Point Precision in Mean of Large Timestamps

When averaging Unix epoch nanosecond timestamps (values near $10^{18}$), the sum $\sum t_i$ can overflow or lose precision. Always **center** the data first:

$$\bar{t} = t_{\min} + \frac{\sum (t_i - t_{\min})}{n}$$

This keeps intermediate values small and preserves sub-nanosecond precision.

### Gotcha 3: Mean of Durations with Mixed Units

If some durations are recorded in seconds and others in milliseconds, the mean will be meaningless. **Normalize all durations to a single unit** before computing $\bar{t}$.

---

## 3. Solved Exercises (10 Examples)

### Exercise 1: Simple Mean Duration with Missing Value

**Problem:** The mean processing time of five tasks is 10 seconds. Four of the tasks took 8 s, 12 s, 7 s, and 11 s. Find the fifth task's duration.

**Solution:**
1.  Sum of 5 durations = $5 \cdot 10 = 50\text{ s}$.
2.  Sum of 4 known durations = $8 + 12 + 7 + 11 = 38\text{ s}$.
3.  Fifth duration = $50 - 38 = \mathbf{12\text{ s}}$.

---

### Exercise 2: Median for Odd vs. Even $n$ (Response Times)

**Problem:** Find the median response time (in ms) for:
A) `3, 10, 2, 8, 5`
B) `3, 10, 2, 8, 5, 12`

**Solution:**
A) Order: `2, 3, 5, 8, 10`. $n=5$ (odd). Median is the 3rd value: **5 ms**.
B) Order: `2, 3, 5, 8, 10, 12`. $n=6$ (even). Median is average of 3rd and 4th: $(5+8)/2 = \mathbf{6.5\text{ ms}}$.

---

### Exercise 3: Multimodal Duration Data

**Problem:** Find the mode of these execution times (in seconds): `1, 2, 2, 3, 4, 4, 5`.

**Solution:**
Values 2 and 4 both appear twice. This dataset is **bimodal**. Modes are **2 s and 4 s**.

> **Interpretation:** The system has two typical execution time clusters -- possibly a "fast path" (2 s) and a "slow path" (4 s).

---

### Exercise 4: Grouped Mean for Duration Data (Weighted Average)

**Problem:** Calculate the mean response time from this table (class marks in ms):

| $t_i$ (Midpoint, ms) | $f_i$ |
| :--- | :--- |
| 10 | 2 |
| 20 | 5 |
| 30 | 3 |

**Solution:**
1.  $\sum f_i \cdot t_i = (10 \cdot 2) + (20 \cdot 5) + (30 \cdot 3) = 20 + 100 + 90 = 210$.
2.  $n = 2 + 5 + 3 = 10$.
3.  $\bar{t} = 210 / 10 = \mathbf{21\text{ ms}}$.

---

### Exercise 5: Grouped Median for Latency Data (Interpolation)

**Problem:** Find $M_e$ for latency data with $n=40,\ w=10\text{ ms},\ L=20\text{ ms},\ f_i=12,\ F_{i-1}=8$.

**Solution:**
1.  $n/2 = 20$.
2.  $M_e = 20 + \left( \frac{20 - 8}{12} \right) \cdot 10 = 20 + (1) \cdot 10 = \mathbf{30\text{ ms}}$.

> **Interpretation:** Half of the requests completed within 30 ms.

---

### Exercise 6: Grouped Mode for Latency Data (Interpolation)

**Problem:** The modal latency class is $[30, 40)\text{ ms}$. $L=30\text{ ms},\ w=10\text{ ms},\ f_i=20,\ f_{i-1}=12,\ f_{i+1}=10$.

**Solution:**
$$M_o = 30 + \left( \frac{20 - 12}{(20-12) + (20-10)} \right) \cdot 10$$
$$M_o = 30 + \left( \frac{8}{8 + 10} \right) \cdot 10 = 30 + 4.44 = \mathbf{34.44\text{ ms}}$$

---

### Exercise 7: Effect of Outliers on Latency Data

**Problem:** Response times (ms): `10, 10, 11, 12, 100`. Compare Mean and Median.

**Solution:**
1.  Mean = $(10+10+11+12+100)/5 = 28.6\text{ ms}$.
2.  Median = Order: `10, 10, 11, 12, 100` $\Rightarrow$ **11 ms**.

**Observation:** The outlier (100 ms, possibly a network stall) pulled the mean far from the central cluster, while the median remained representative of the typical latency.

> **Practical tip:** In latency monitoring, the **median** (often called p50) is preferred over the mean because a single slow request should not distort the "typical" experience.

---

### Exercise 8: Finding Mean Duration from Relative Frequencies

**Problem:** Given duration values $t_i = [1, 2, 3]\text{ s}$ and relative frequencies $h_i = [0.2, 0.5, 0.3]$. Find $\bar{t}$.

**Solution:**
For relative frequencies, the mean formula is $\bar{t} = \sum t_i \cdot h_i$.
$$\bar{t} = (1 \cdot 0.2) + (2 \cdot 0.5) + (3 \cdot 0.3)$$
$$\bar{t} = 0.2 + 1.0 + 0.9 = \mathbf{2.1\text{ s}}$$

---

### Exercise 9: Circular Mean of Clock Times

**Problem:** Three events occur at clock times 23:00, 01:00, and 00:00. Compute both the naive arithmetic mean and the correct circular mean.

**Solution:**

**Naive (incorrect) arithmetic mean:**
$$\frac{23 + 1 + 0}{3} = \frac{24}{3} = 8 \text{ (08:00)}$$

This is wrong -- 08:00 is 7 hours from 23:00 and 7 hours from 01:00, but 00:00 is only 1 hour from 23:00 and 1 hour from 01:00.

**Circular mean (correct):**

**Step 1:** Convert to angles ($\theta_i = \frac{2\pi \cdot t_i}{24}$):
*   $t_1 = 23 \Rightarrow \theta_1 = \frac{2\pi \cdot 23}{24}$
*   $t_2 = 1 \Rightarrow \theta_2 = \frac{2\pi \cdot 1}{24}$
*   $t_3 = 0 \Rightarrow \theta_3 = 0$

**Step 2:** Compute sums:
$$S = \sin\theta_1 + \sin\theta_2 + \sin\theta_3 \approx -0.261 + 0.261 + 0 = 0$$
$$C = \cos\theta_1 + \cos\theta_2 + \cos\theta_3 \approx -0.966 + 0.966 + 1 = 1$$

**Step 3:** $\bar{\theta} = \text{atan2}(0, 1) = 0$

**Step 4:** $\bar{t} = \frac{24 \cdot 0}{2\pi} = \mathbf{0 \text{ (00:00, midnight)}}$

This is the correct result: midnight is the circular center of 23:00, 01:00, and 00:00.

---

### Exercise 10: R Snippet -- Mean and Median of Latency Data

**Problem:** Use R to compute the mean, median, and mode of these response times (ms): `120, 135, 142, 120, 158, 135, 170, 142, 120, 190`.

**Solution:**

```r
# Response times in milliseconds
latency_ms <- c(120, 135, 142, 120, 158, 135, 170, 142, 120, 190)

# Mean and median
mean_latency <- mean(latency_ms)
median_latency <- median(latency_ms)

# Mode (most frequent value)
freq <- table(latency_ms)
mode_latency <- as.numeric(names(freq)[which.max(freq)])

cat("Mean:", mean_latency, "ms\n")
cat("Median:", median_latency, "ms\n")
cat("Mode:", mode_latency, "ms\n")
```

**Expected output:**
```
Mean: 143.2 ms
Median: 138.5 ms
Mode: 120 ms
```

> **R note:** The mean (143.2 ms) is higher than the median (138.5 ms) because the outlier at 190 ms pulls the mean upward. This indicates a **right-skewed** latency distribution, which is typical in real-world response time data.

---

## Exam Tip: Choosing the Best Measure (Time Context)

*   **Mean:** Best for symmetrical duration data without outliers. Use the **circular mean** for cyclic clock times.
*   **Median:** Best for skewed latency data or data with extreme timeout outliers. This is the p50 latency in performance monitoring.
*   **Mode:** Best for categorical time data (e.g., most common hour of day for requests).

### Skewness Relationship (Time Data)
| Condition | Distribution Shape | Time Interpretation |
| :--- | :--- | :--- |
| **Mean > Median** | **Positively Skewed** (right tail longer) | A few very slow requests stretch the tail |
| **Mean < Median** | **Negatively Skewed** (left tail longer) | A few very fast requests (cache hits) stretch the left |
| **Mean = Median** | **Symmetric** | Latencies evenly distributed around the center |