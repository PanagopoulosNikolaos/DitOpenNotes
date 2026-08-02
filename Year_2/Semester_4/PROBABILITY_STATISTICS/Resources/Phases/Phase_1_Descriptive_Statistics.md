# Phase 1: Descriptive Statistics

## Table of Contents
- [Section 1.1: Data Organization](#section-11-data-organization)
- [Section 1.2: Measures of Central Tendency](#section-12-measures-of-central-tendency)
- [Section 1.3: Measures of Position](#section-13-measures-of-position)
- [Section 1.4: Measures of Dispersion](#section-14-measures-of-dispersion)
- [Section 1.5: Core Formulas Summary (Grouped Data)](#section-15-core-formulas-summary-grouped-data)
- [Phase Summary](#phase-summary)

---

## Section 1.1: Data Organization

### Core Theory & Definitions
Data organization is the first step in descriptive statistics. It involves transforming raw data into a structured format, primarily through **Frequency Tables**. This allows us to see patterns, distributions, and summary characteristics of the dataset.

When the data consist of **time-based observations** -- timestamps, durations, latencies, intervals, or cyclic clock times -- the same organizational principles apply, but special attention must be paid to **units, prefixes, and the cyclic nature of clock time**.

Before building a table, we must understand the four types of frequencies:
*   **Absolute Frequency ($f_i$):** The number of times a specific value or interval occurs. The sum of all absolute frequencies equals the total number of observations ($n$):
    $$\sum_{i=1}^{k} f_i = n$$
*   **Relative Frequency ($h_i$):** The proportion or percentage of the total data that a value represents:
    $$h_i = \frac{f_i}{n}$$
    The sum of all relative frequencies must always equal 1 (or 100%): $\sum h_i = 1$.
*   **Cumulative Absolute Frequency ($F_i$):** The running total of absolute frequencies up to a certain point:
    $$F_i = f_1 + f_2 + \dots + f_i$$
*   **Cumulative Relative Frequency ($H_i$):** The running total of relative frequencies:
    $$H_i = h_1 + h_2 + \dots + h_i \quad \text{or} \quad H_i = \frac{F_i}{n}$$

> **Practical / Time-Domain Note:**
> Cumulative frequency is especially meaningful for duration data. $F_i$ tells us how many events took **at most** the upper boundary of class $i$ to complete.
> **Gotcha 1:** When computing class marks or sums for Unix epoch timestamps in nanoseconds, standard floating point loses precision. Always **center** timestamp data by subtracting the minimum before computing frequencies.
> **Gotcha 2:** Clock times are **circular**, not linear. A simple frequency table that sorts by raw clock value will misinterpret the order.
> **Gotcha 3:** Always normalize mixed unit prefixes (e.g., ms and s) to a single unit before tabulating.

### Mathematical Formulas & Derivations
When datasets are large or continuous, we group them into **Class Intervals**.
1.  **Range ($R$):** $R = x_{max} - x_{min}$
2.  **Number of Classes ($k$):** (Sturges' Rule) $k = 1 + 3.322 \cdot \log_{10}(n)$
3.  **Class Width ($w$):** $w = \frac{R}{k}$ (Always round up for convenience in manual tables).
4.  **Class Mark ($x_i$):** Midpoint of the interval: $x_i = \frac{\text{Lower} + \text{Upper}}{2}$

> **Practical / Time-Domain Note:**
> When the range spans very small time units (e.g., nanoseconds), $w$ may be a fraction. Convert to a larger unit like milliseconds so $w$ is a manageable number.

### Worked Exercises

#### Exercise 1: Categorical Data (Qualitative)
**Problem:** A survey of 15 people asked for their favorite color among: Red (R), Blue (B), and Green (G). The results: `R, B, B, G, R, B, G, G, B, B, R, G, B, B, R`. Create a frequency table.

**Solution:**
1.  **Count:** Red (4), Blue (7), Green (4). Total $n=15$.
2.  **Relative Frequency:** $h_{Red} = 4/15 \approx 0.267$.

| Color | $f_i$ | $h_i$ | $F_i$ | $H_i$ |
| :--- | :--- | :--- | :--- | :--- |
| Red | 4 | 0.267 | 4 | 0.267 |
| Blue | 7 | 0.467 | 11 | 0.734 |
| Green | 4 | 0.267 | 15 | 1.001 |

*(Note: The $H_i$ column sums to 1.001 due to rounding each $h_i$ to 3 decimal places. This is a standard rounding artifact.)*

#### Exercise 2: Discrete Data (Ungrouped)
**Problem:** Number of siblings for 10 students: `0, 1, 2, 1, 0, 3, 2, 1, 1, 2`.

**Solution:**
Identify unique values: 0, 1, 2, 3.

| Siblings ($x_i$) | $f_i$ | $h_i$ | $F_i$ |
| :--- | :--- | :--- | :--- |
| 0 | 2 | 0.2 | 2 |
| 1 | 4 | 0.4 | 6 |
| 2 | 3 | 0.3 | 9 |
| 3 | 1 | 0.1 | 10 |

#### Exercise 3: Finding Missing Frequencies
**Problem:** A table has $n=20$. Given $f_1=5, f_2=?, f_3=8, f_4=2$. Find $f_2$ and $h_2$.

**Solution:**
1.  Sum condition: $5 + f_2 + 8 + 2 = 20$
2.  $15 + f_2 = 20 \Rightarrow f_2 = 5$
3.  $h_2 = 5/20 = 0.25$.

#### Exercise 4: Grouping Continuous Data (Manual Range)
**Problem:** Group these 10 heights (cm) into 2 classes starting at 150: `152, 158, 161, 164, 165, 168, 172, 175, 177, 180`. Class width $w=15$.

**Solution:**
Intervals: `[150, 165)` and `[165, 180]`.
*   `[150, 165)`: 152, 158, 161, 164 (4 values)
*   `[165, 180]`: 165, 168, 172, 175, 177, 180 (6 values)

| Interval | $x_i$ | $f_i$ | $F_i$ |
| :--- | :--- | :--- | :--- |
| [150, 165) | 157.5 | 4 | 4 |
| [165, 180] | 172.5 | 6 | 10 |

#### Exercise 5: Applying Sturges' Rule
**Problem:** For $n=40$ observations, find the ideal number of classes $k$.

**Solution:**
$$k = 1 + 3.322 \cdot \log_{10}(40)$$
$$k = 1 + 3.322 \cdot (1.602) \approx 1 + 5.32 = 6.32$$
Rounding up (as per the convention stated above), we use **7 classes**.

#### Exercise 6: Interpreting Cumulative Frequency
**Problem:** In a table, $F_3 = 18$ and $F_2 = 12$. What is $f_3$?

**Solution:**
Since $F_3 = f_1 + f_2 + f_3$ and $F_2 = f_1 + f_2$:
$$f_3 = F_3 - F_2 = 18 - 12 = 6$$

#### Exercise 7: Percentage Distribution
**Problem:** Convert relative frequencies $h_i = [0.15, 0.35, 0.50]$ into a percentage frequency table.

**Solution:**
Multiply $h_i$ by 100.

| Value | $h_i$ | Frequency % |
| :--- | :--- | :--- |
| A | 0.15 | 15% |
| B | 0.35 | 35% |
| C | 0.50 | 50% |

#### Exercise 8: Full Table Construction
**Problem:** Data: `10, 12, 15, 18, 20, 22, 25, 28, 30, 35`. Group into 3 classes with $w=10$, starting at 10.

**Solution:**
**Step 1: Identify Intervals**
`[10, 20), [20, 30), [30, 40]`

**Step 2: Calculate Midpoints ($x_i$)**
$x_1 = (10+20)/2 = 15$

**Step 3: Tally Frequencies**
*   `[10, 20)`: 10, 12, 15, 18 $\Rightarrow f_1 = 4$
*   `[20, 30)`: 20, 22, 25, 28 $\Rightarrow f_2 = 4$
*   `[30, 40]`: 30, 35 $\Rightarrow f_3 = 2$

**Final Table:**

| Interval | $x_i$ | $f_i$ | $h_i$ | $F_i$ |
| :--- | :--- | :--- | :--- | :--- |
| [10, 20) | 15 | 4 | 0.4 | 4 |
| [20, 30) | 25 | 4 | 0.4 | 8 |
| [30, 40] | 35 | 2 | 0.2 | 10 |

#### Exercise 9: Applying Sturges' Rule to Execution Time Data
**Problem:** For $n=40$ execution time observations (in seconds), find the ideal number of classes $k$.

**Solution:**
$$k = 1 + 3.322 \cdot \log_{10}(40)$$
$$k = 1 + 3.322 \cdot (1.602) \approx 1 + 5.32 = 6.32$$
Rounding up, we use **7 classes**.

> **Time-Domain Note:** Once $k$ is determined, compute $w = R/k$ in the chosen time unit. If execution times range from $0.1\text{ s}$ to $2.5\text{ s}$, then $R = 2.4\text{ s}$ and $w = 2.4/7 \approx 0.343\text{ s}$. Rounding up to $0.35\text{ s}$ gives clean intervals.

#### Exercise 10: Unit Conversion Before Tabulation
**Problem:** Raw latency data (in seconds): `0.152, 0.158, 0.161, 0.164, 0.165, 0.168, 0.172, 0.175, 0.177, 0.180`. Convert to milliseconds and group into 2 classes starting at 150 ms with $w = 15\text{ ms}$.

**Solution:**
**Step 1: Convert units.** Multiply each value by 1000:
`152, 158, 161, 164, 165, 168, 172, 175, 177, 180` (ms)

**Step 2: Identify intervals.**
$[150, 165)\text{ ms}$ and $[165, 180]\text{ ms}$

**Step 3: Tally.**
*   $[150, 165)$: 152, 158, 161, 164 $\Rightarrow f_1 = 4$
*   $[165, 180]$: 165, 168, 172, 175, 177, 180 $\Rightarrow f_2 = 6$

| Interval (ms) | $x_i$ (ms) | $f_i$ | $h_i$ | $F_i$ |
| :--- | :--- | :--- | :--- | :--- |
| $[150, 165)$ | 157.5 | 4 | 0.4 | 4 |
| $[165, 180]$ | 172.5 | 6 | 0.6 | 10 |

> **Time-Domain Note:** The choice of unit does not change the frequencies or relative frequencies -- only the labels on the intervals change.

### R Implementation
```r
# Building a Frequency Table for Time Data in milliseconds
response_times_ms <- c(120, 135, 142, 120, 158, 135, 170, 142, 120, 190)

# Ungrouped frequency table
freq_table <- as.data.frame(table(response_times_ms))
colnames(freq_table) <- c("Time_ms", "f_i")

# Relative frequency
freq_table$h_i <- freq_table$f_i / sum(freq_table$f_i)

# Cumulative absolute frequency
freq_table$F_i <- cumsum(freq_table$f_i)

# Cumulative relative frequency
freq_table$H_i <- cumsum(freq_table$h_i)

print(freq_table)
```

---

## Section 1.2: Measures of Central Tendency

### Core Theory & Definitions
Measures of central tendency are statistical values that represent the "center" or "typical" value of a dataset. The three most common measures are the **Mean**, **Median**, and **Mode**. When the data are **time-based**, these measures require careful handling of **units, linear vs. cyclic time, and floating-point precision**.

### Mathematical Formulas & Derivations
#### Mean ($\bar{x}$)
*   **Ungrouped:** $\bar{x} = \frac{\sum x_i}{n}$
*   **Grouped:** $\bar{x} = \frac{\sum f_i \cdot x_i}{n}$

#### Median ($M_e$)
*   **Ungrouped:** Middle value (or average of two middle values) in an ordered list.
*   **Grouped (Interpolation):** $M_e = L + \left( \frac{\frac{n}{2} - F_{i-1}}{f_i} \right) \cdot w$

#### Mode ($M_o$)
*   **Ungrouped:** Most frequent value.
*   **Grouped (Interpolation):** $M_o = L + \left( \frac{f_i - f_{i-1}}{(f_i - f_{i-1}) + (f_i - f_{i+1})} \right) \cdot w$

> **Practical / Time-Domain Note:**
> The arithmetic mean is **invalid for cyclic (circular) clock times**. Averaging 23:00 and 01:00 naively gives 12:00 (noon). Use the **circular mean** instead.
> The median is robust for time data: it represents the "typical" duration and is unaffected by extreme latency outliers.

### Worked Exercises

#### Exercise 1: Simple Mean with Missing Value
**Problem:** The mean of five numbers is 10. Four of the numbers are 8, 12, 7, and 11. Find the fifth number.

**Solution:**
1.  Sum of 5 numbers = $5 \cdot 10 = 50$.
2.  Sum of 4 known numbers = $8 + 12 + 7 + 11 = 38$.
3.  Fifth number = $50 - 38 = 12$.

#### Exercise 2: Median for Odd vs. Even $n$
**Problem:** Find the median for:
A) `3, 10, 2, 8, 5`
B) `3, 10, 2, 8, 5, 12`

**Solution:**
A) Order: `2, 3, 5, 8, 10`. $n=5$ (odd). Median is the 3rd value: **5**.
B) Order: `2, 3, 5, 8, 10, 12`. $n=6$ (even). Median is average of 3rd and 4th: $(5+8)/2 = \mathbf{6.5}$.

#### Exercise 3: Multimodal Data
**Problem:** Find the mode of: `1, 2, 2, 3, 4, 4, 5`.

**Solution:**
Values 2 and 4 both appear twice. This dataset is **bimodal**. Modes are **2 and 4**.

#### Exercise 4: Grouped Mean (Weighted Average)
**Problem:** Calculate the mean from this table:

| $x_i$ (Midpoint) | $f_i$ |
| :--- | :--- |
| 10 | 2 |
| 20 | 5 |
| 30 | 3 |

**Solution:**
1.  $\sum f_i \cdot x_i = (10 \cdot 2) + (20 \cdot 5) + (30 \cdot 3) = 20 + 100 + 90 = 210$.
2.  $n = 2 + 5 + 3 = 10$.
3.  $\bar{x} = 210 / 10 = \mathbf{21}$.

#### Exercise 5: Grouped Median (Interpolation)
**Problem:** Find $M_e$ for $n=40, w=10, L=20, f_i=12, F_{i-1}=8$.

**Solution:**
1.  $n/2 = 20$.
2.  $M_e = 20 + \left( \frac{20 - 8}{12} \right) \cdot 10 = 20 + (1) \cdot 10 = \mathbf{30}$.

#### Exercise 6: Grouped Mode (Interpolation)
**Problem:** Modal class is [30, 40). $L=30, w=10, f_i=20, f_{i-1}=12, f_{i+1}=10$.

**Solution:**
$$M_o = 30 + \left( \frac{20 - 12}{(20-12) + (20-10)} \right) \cdot 10$$
$$M_o = 30 + \left( \frac{8}{8 + 10} \right) \cdot 10 = 30 + 4.44 = \mathbf{34.44}$$

#### Exercise 7: Effect of Outliers
**Problem:** Data: `10, 10, 11, 12, 100`. Compare Mean and Median.

**Solution:**
1.  Mean = $(10+10+11+12+100)/5 = 28.6$.
2.  Median = Order: `10, 10, 11, 12, 100` $\Rightarrow$ **11**.
**Observation:** The outlier (100) pulled the mean far from the central cluster, while the median remained representative.

#### Exercise 8: Finding Mean from Relative Frequencies
**Problem:** Given values $x_i = [1, 2, 3]$ and relative frequencies $h_i = [0.2, 0.5, 0.3]$. Find $\bar{x}$.

**Solution:**
For relative frequencies, the mean formula is $\bar{x} = \sum x_i \cdot h_i$.
$$\bar{x} = (1 \cdot 0.2) + (2 \cdot 0.5) + (3 \cdot 0.3)$$
$$\bar{x} = 0.2 + 1.0 + 0.9 = \mathbf{2.1}$$

#### Exercise 9: Circular Mean of Clock Times
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

#### Exercise 10: Effect of Outliers on Latency Data
**Problem:** Response times (ms): `10, 10, 11, 12, 100`. Compare Mean and Median.

**Solution:**
1.  Mean = $(10+10+11+12+100)/5 = 28.6\text{ ms}$.
2.  Median = Order: `10, 10, 11, 12, 100` $\Rightarrow$ **11 ms**.

> **Time-Domain Note:** The outlier (100 ms, possibly a network stall) pulled the mean far from the central cluster, while the median remained representative of the typical latency. In latency monitoring, the **median** (p50) is preferred over the mean.

### R Implementation
```r
# Mean and Median of Latency Data
latency_ms <- c(120, 135, 142, 120, 158, 135, 170, 142, 120, 190)

mean_latency <- mean(latency_ms)
median_latency <- median(latency_ms)

freq <- table(latency_ms)
mode_latency <- as.numeric(names(freq)[which.max(freq)])

cat("Mean:", mean_latency, "ms\n")
cat("Median:", median_latency, "ms\n")
cat("Mode:", mode_latency, "ms\n")
```

---

## Section 1.3: Measures of Position

### Core Theory & Definitions
Measures of position (or quantiles) are values that divide a sorted dataset into equal parts. The most common are **Quartiles** (divided into 4 parts) and **Percentiles** (divided into 100 parts).

When the data are **time-based**, quantiles become critically important in performance monitoring -- they are the **p50, p90, p95, p99 latency metrics** used in Service Level Agreements (SLAs).

### Mathematical Formulas & Derivations
#### Quantile Position (Ungrouped)
$$P = \frac{k(n+1)}{N_{parts}}$$
*   $k$: Quantile number (e.g., 1, 2, 3 for quartiles).
*   $n$: Total number of observations.
*   $N_{parts}$: 4 for quartiles, 100 for percentiles.

#### Quantile Formula (Grouped Data)
$$Q = L + \left( \frac{\text{Position} - F_{i-1}}{f_i} \right) \cdot w$$
Where:
*   **Position** = $\frac{k \cdot n}{4}$ for quartiles or $\frac{k \cdot n}{100}$ for percentiles.

> **Practical / Time-Domain Note:**
> The 95th percentile ($P_{95}$) of response time means 95% of requests completed within that time.
> **Gotcha 1:** $P_{95}$ is the **value below which 95% of observations fall**, not a percentage of the average.
> **Gotcha 2:** Percentiles are in the **same unit** as the data. When converting units, the percentile value scales by the conversion factor, but the position does not.

### Worked Exercises

#### Exercise 1: Quartiles for Small $n$ (Ungrouped)
**Problem:** Find $Q_1, Q_2, Q_3$ for: `5, 8, 4, 10, 15, 21, 2`.

**Solution:**
1.  Order: `2, 4, 5, 8, 10, 15, 21`. $n=7$.
2.  $Q_2$ (Median): 4th value = **8**.
3.  $Q_1$: Median of lower half (`2, 4, 5`) = **4**.
4.  $Q_3$: Median of upper half (`10, 15, 21`) = **15**.

#### Exercise 2: Percentile for Small $n$ (Ungrouped)
**Problem:** Find $P_{80}$ for: `10, 20, 30, 40, 50`.

**Solution:**
1.  Order: `10, 20, 30, 40, 50`. $n=5$.
2.  Position $P = \frac{80(5+1)}{100} = 4.8$.
3.  Interpolate between 4th (40) and 5th (50):
$$P_{80} = 40 + 0.8 \cdot (50 - 40) = 40 + 8 = \mathbf{48}$$

#### Exercise 3: Grouped $Q_1$ (Interpolation)
**Problem:** $n=60, L=10, w=10, f_i=12, F_{i-1}=8$.

**Solution:**
1.  Position = $60/4 = 15$.
2.  $Q_1 = 10 + \left( \frac{15 - 8}{12} \right) \cdot 10 = 10 + \frac{70}{12} \approx \mathbf{15.83}$.

#### Exercise 4: Grouped $Q_3$ (Interpolation)
**Problem:** $n=60, L=30, w=10, f_i=15, F_{i-1}=40$.

**Solution:**
1.  Position = $(3 \cdot 60)/4 = 45$.
2.  $Q_3 = 30 + \left( \frac{45 - 40}{15} \right) \cdot 10 = 30 + \frac{50}{15} \approx \mathbf{33.33}$.

#### Exercise 5: Interquartile Range ($IQR$)
**Problem:** Using results from Ex 3 and 4 ($Q_1=15.83, Q_3=33.33$), find the $IQR$.

**Solution:**
$$IQR = Q_3 - Q_1 = 33.33 - 15.83 = \mathbf{17.50}$$

#### Exercise 6: Percentile Rank (Grouped)
**Problem:** In a distribution, find the 10th percentile ($P_{10}$) if $n=100$, and the first class is [0, 20) with $f_i=15$.

**Solution:**
1.  Position = $(10 \cdot 100)/100 = 10$.
2.  $P_{10}$ class is [0, 20) since $15 \ge 10$.
3.  $L=0, w=20, f_i=15, F_{i-1}=0$.
$$P_{10} = 0 + \left( \frac{10 - 0}{15} \right) \cdot 20 = \frac{200}{15} \approx \mathbf{13.33}$$

#### Exercise 7: Deciles ($D_k$)
**Problem:** Find the 7th decile ($D_7$) for $n=50, L=40, w=10, f_i=8, F_{i-1}=30$.

**Solution:**
Deciles divide into 10 parts. $D_7 = P_{70}$.
1.  Position = $(70 \cdot 50)/100 = 35$.
2.  $D_7 = 40 + \left( \frac{35 - 30}{8} \right) \cdot 10 = 40 + 6.25 = \mathbf{46.25}$.

#### Exercise 8: Reverse Problem (Finding the Percentile)
**Problem:** A score of 45 falls in class [40, 50) where $f_i=10, F_{i-1}=30, n=50, w=10$. What percentile is this score?

**Solution:**
Set $P_k = 45$ and solve for $k$:
$$45 = 40 + \left( \frac{\frac{k \cdot 50}{100} - 30}{10} \right) \cdot 10$$
$$5 = 0.5k - 30 \Rightarrow 0.5k = 35 \Rightarrow k = 70$$
The score 45 is at the **70th percentile** ($P_{70}$).

#### Exercise 9: Interquartile Range ($IQR$) for Latency
**Problem:** Using latency quartiles $Q_1=15.83\text{ ms},\ Q_3=33.33\text{ ms}$, find the $IQR$.

**Solution:**
$$IQR = Q_3 - Q_1 = 33.33 - 15.83 = \mathbf{17.50\text{ ms}}$$

> **Time-Domain Note:** The middle 50% of requests span 17.50 ms. A small IQR indicates consistent latency.

#### Exercise 10: Unit Conversion for Percentiles
**Problem:** The $P_{99}$ latency is measured as $2\,500\,000\text{ ns}$. Convert this to milliseconds and microseconds.

**Solution:**
1.  To microseconds: $2\,500\,000\text{ ns} / 1000 = \mathbf{2\,500\ \mu\text{s}}$.
2.  To milliseconds: $2\,500\,000\text{ ns} / 10^6 = \mathbf{2.5\text{ ms}}$.

> **Time-Domain Note:** The percentile **rank** (99) does not change when converting units. Only the **value** scales.

### R Implementation
```r
# Computing SLA Percentiles
latency_ms <- c(120, 135, 142, 120, 158, 135, 170, 142, 120, 190, 210, 95, 130, 145, 160)

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

---

## Section 1.4: Measures of Dispersion

### Core Theory & Definitions
Measures of dispersion (or variability) describe how "spread out" the values in a dataset are. While central tendency tells us where the center is, dispersion tells us how much the data deviates from that center.

For **time-based data**, dispersion is critical: high variance in latency means an unpredictable system, while low variance means consistent performance.

### Mathematical Formulas & Derivations
#### Sample Variance ($s^2$)
$$s^2 = \frac{\sum (x_i - \bar{x})^2}{n - 1} \quad \text{or} \quad s^2 = \frac{\sum f_i(x_i - \bar{x})^2}{n - 1}$$

#### Shortcut Variance Formula (Grouped)
$$s^2 = \frac{\sum f_i \cdot x_i^2 - \frac{(\sum f_i \cdot x_i)^2}{n}}{n - 1}$$

#### Coefficient of Variation ($CV$)
$$CV = \frac{s}{\bar{x}} \cdot 100\%$$
*(Used to compare dispersion between datasets with different units or means.)*

> **Practical / Time-Domain Note:**
> **The $c^2$ Rule:** When converting time data by multiplying every value by a constant $c$, the variance scales by $c^2$ and the standard deviation scales by $c$.
> **Gotcha 1:** Variance is in **squared time units** (e.g., $\text{s}^2$, $\text{ms}^2$, $\text{ns}^2$). Reporting $25\text{ ms}^2$ as "spread of 25 ms" is wrong.
> **Gotcha 2:** The Coefficient of Variation $CV = s/\bar{t}$ is **dimensionless**.

### Worked Exercises

#### Exercise 1: Range for Discrete Data
**Problem:** Find the range of: `10, 2, 35, 12, 18, 5`.

**Solution:**
1.  Max = 35, Min = 2.
2.  Range = $35 - 2 = \mathbf{33}$.

#### Exercise 2: Sample Variance (Ungrouped)
**Problem:** Find $s^2$ for: `2, 4, 6`.

**Solution:**
1.  Mean $\bar{x} = (2+4+6)/3 = 4$.
2.  Deviations: $(2-4)=-2, (4-4)=0, (6-4)=2$.
3.  Squared: $4, 0, 4$. Sum = 8.
4.  $s^2 = 8 / (3-1) = \mathbf{4}$.

#### Exercise 3: Population Standard Deviation ($\sigma$)
**Problem:** Data: `1, 3, 5`. Assume this is the *entire population*. Find $\sigma$.

**Solution:**
1.  $\mu = 3$.
2.  Squared deviations: $(1-3)^2=4, (3-3)^2=0, (5-3)^2=4$. Sum = 8.
3.  Population Variance $\sigma^2 = 8 / 3 \approx 2.67$.
4.  $\sigma = \sqrt{2.67} \approx \mathbf{1.63}$.

#### Exercise 4: Grouped Variance (Standard Method)
**Problem:** $\sum f_i(x_i - \bar{x})^2 = 610, n=10$. Find sample variance.

**Solution:**
$$s^2 = 610 / (10 - 1) = 610 / 9 \approx \mathbf{67.78}$$

#### Exercise 5: Grouped Variance (Shortcut Method)
**Problem:** $\sum f_i x_i = 100, \sum f_i x_i^2 = 2500, n=5$. Find $s^2$.

**Solution:**
$$s^2 = \frac{2500 - \frac{100^2}{5}}{5 - 1} = \frac{2500 - 2000}{4} = \frac{500}{4} = \mathbf{125}$$

#### Exercise 6: Coefficient of Variation ($CV$)
**Problem:** Group A: $\bar{x}=50, s=10$. Group B: $\bar{x}=100, s=15$. Which group is more dispersed relative to its mean?

**Solution:**
1.  $CV_A = (10/50) \cdot 100 = 20\%$.
2.  $CV_B = (15/100) \cdot 100 = 15\%$.
**Group A** is more dispersed.

#### Exercise 7: Identifying Outliers (The 1.5 IQR Rule)
**Problem:** $Q_1=10, Q_3=20$. Is the value 40 an outlier?

**Solution:**
1.  $IQR = 20 - 10 = 10$.
2.  Upper Fence = $Q_3 + 1.5 \cdot IQR = 20 + 15 = 35$.
3.  Since $40 > 35$, the value 40 is an **outlier**.

#### Exercise 8: Effect of Transformation
**Problem:** Dataset $X$ has $s=5$. If every value is multiplied by 3 and then 10 is added ($Y = 3X + 10$), what is the new standard deviation?

**Solution:**
1.  Adding a constant (10) does **not** change dispersion.
2.  Multiplying by a constant (3) multiplies the standard deviation by that constant.
3.  $s_{new} = 3 \cdot 5 = \mathbf{15}$.

#### Exercise 9: Effect of Unit Conversion (The $c^2$ Rule)
**Problem:** A dataset of response times has $s = 5\text{ ms}$ and $s^2 = 25\text{ ms}^2$. Convert the data to seconds. What are the new standard deviation and variance?

**Solution:**
**Conversion factor:** $c = 10^{-3}$ (milliseconds to seconds).

**Standard deviation:**
$$s_{\text{new}} = c \cdot s_{\text{old}} = 10^{-3} \cdot 5 = \mathbf{0.005\text{ s}}$$

**Variance (using the $c^2$ rule):**
$$s^2_{\text{new}} = c^2 \cdot s^2_{\text{old}} = (10^{-3})^2 \cdot 25 = 10^{-6} \cdot 25 = \mathbf{0.000025\text{ s}^2}$$

#### Exercise 10: Converting from Nanoseconds to Milliseconds (The $c^2$ Rule)
**Problem:** Latency data measured in nanoseconds has variance $s^2 = 4 \times 10^{10}\text{ ns}^2$. Convert the variance to $\text{ms}^2$ and find the standard deviation in ms.

**Solution:**
**Conversion factor:** $c = 10^{-6}$ (nanoseconds to milliseconds).

**Variance:**
$$s^2_{\text{ms}} = c^2 \cdot s^2_{\text{ns}} = (10^{-6})^2 \cdot 4 \times 10^{10} = 10^{-12} \cdot 4 \times 10^{10} = 4 \times 10^{-2} = \mathbf{0.04\text{ ms}^2}$$

**Standard deviation:**
$$s_{\text{ms}} = \sqrt{0.04} = \mathbf{0.2\text{ ms}}$$

> **Time-Domain Note:** The variance in nanoseconds ($4 \times 10^{10}$) looks enormous, but it represents the same spread as $0.04\text{ ms}^2$. The $c^2$ rule with $c = 10^{-6}$ shrinks the variance by a factor of $10^{12}$.

### R Implementation
```r
# Variance and CV with Unit Conversion
latency_ms <- c(120, 135, 142, 120, 158, 135, 170, 142, 120, 190)

var_ms <- var(latency_ms)
sd_ms <- sd(latency_ms)
cv_ms <- (sd_ms / mean(latency_ms)) * 100

latency_s <- latency_ms / 1000

var_s <- var(latency_s)
sd_s <- sd(latency_s)
cv_s <- (sd_s / mean(latency_s)) * 100

cat("In milliseconds:\n")
cat("  Variance:", var_ms, "ms^2\n")
cat("  CV:", cv_ms, "%\n\n")

cat("In seconds:\n")
cat("  Variance:", var_s, "s^2\n")
cat("  CV:", cv_s, "%\n\n")
```

---

## Section 1.5: Core Formulas Summary (Grouped Data)

### Core Theory & Definitions
This section serves as a quick-reference guide for the mathematical foundation of Descriptive Statistics when dealing with **Grouped Data**.

### Mathematical Formulas & Derivations
*   **Class Mark ($x_i$):** $x_i = \frac{L_{inf} + L_{sup}}{2}$
*   **Relative Frequency ($h_i$):** $h_i = \frac{f_i}{n}$
*   **Sturges' Rule (Number of Classes $k$):** $k = 1 + 3.322 \cdot \log_{10}(n)$
*   **Mean ($\bar{x}$):** $\bar{x} = \frac{\sum f_i \cdot x_i}{n}$
*   **Median ($M_e$):** $M_e = L + \left( \frac{\frac{n}{2} - F_{i-1}}{f_i} \right) \cdot w$
*   **Mode ($M_o$):** $M_o = L + \left( \frac{f_i - f_{i-1}}{(f_i - f_{i-1}) + (f_i - f_{i+1})} \right) \cdot w$
*   **General Percentile ($P_k$):** $P_k = L + \left( \frac{\frac{k \cdot n}{100} - F_{i-1}}{f_i} \right) \cdot w$
*   **Sample Variance ($s^2$):** $s^2 = \frac{\sum f_i \cdot (x_i - \bar{x})^2}{n - 1}$
*   **Shortcut Variance Formula:** $s^2 = \frac{\sum f_i \cdot x_i^2 - \frac{(\sum f_i \cdot x_i)^2}{n}}{n - 1}$
*   **Sample Standard Deviation ($s$):** $s = \sqrt{s^2}$

> **Practical / Time-Domain Note:**
> **The $c^2$ Rule:** When converting time data by a factor $c$, the mean, median, mode, range, and standard deviation scale by $c$. The variance scales by $c^2$. The coefficient of variation does not change.
> Always remember that **Variance** is in squared units (e.g., $kg^2$ or $\text{ms}^2$), while **Mean**, **Median**, **Mode**, and **Standard Deviation** are in the original units.

### Worked Exercises
#### Exercise 1: Formula Review
**Problem:** Recall the formula for Coefficient of Variation ($CV$).
**Solution:** $CV = \frac{s}{\bar{x}} \cdot 100\%$

#### Exercise 2: Formula Review 2
**Problem:** Recall the $c^2$ rule for Variance.
**Solution:** $s^2_{\text{new}} = c^2 \cdot s^2_{\text{old}}$

#### Exercise 3: Formula Review 3
**Problem:** Recall the formula for $Q_1$ interpolation.
**Solution:** $Q_1 = L + \left( \frac{\frac{n}{4} - F_{i-1}}{f_i} \right) \cdot w$

#### Exercise 4: Formula Review 4
**Problem:** Recall Sturges' rule.
**Solution:** $k = 1 + 3.322 \cdot \log_{10}(n)$

#### Exercise 5: Formula Review 5
**Problem:** Recall the formula for $IQR$.
**Solution:** $IQR = Q_3 - Q_1$

#### Exercise 6: Formula Review 6
**Problem:** Recall the formula for Range.
**Solution:** $R = x_{max} - x_{min}$

#### Exercise 7: Formula Review 7
**Problem:** Recall the formula for upper fence.
**Solution:** $Upper Fence = Q_3 + 1.5 \cdot IQR$

#### Exercise 8: Formula Review 8
**Problem:** Recall the formula for relative frequency.
**Solution:** $h_i = \frac{f_i}{n}$

#### Exercise 9: Formula Review 9
**Problem:** Recall the formula for class midpoint.
**Solution:** $x_i = \frac{L_{inf} + L_{sup}}{2}$

#### Exercise 10: Formula Review 10
**Problem:** Recall the formula for cumulative frequency.
**Solution:** $F_i = F_{i-1} + f_i$

### R Implementation
```r
# Basic statistics
data <- c(1, 2, 3, 4, 5)
mean(data)
sd(data)
var(data)
```

---

## Phase Summary
Phase 1 covers the foundational techniques of descriptive statistics, focusing on organizing data and measuring its central tendency, position, and dispersion. Key organization tools include frequency tables, class intervals, and Sturges' rule for grouping continuous data. Central tendency is measured by the mean, median, and mode, with the median being robust to outliers and preferred for skewed time-latency data. Position is quantified using quartiles and percentiles, which translate directly to SLAs (like p95 and p99) in performance monitoring. Dispersion is assessed via variance, standard deviation, range, and the coefficient of variation (CV). A critical distinction for time-based data is the circular nature of clock time and the $c^2$ scaling rule, which dictates that variance scales quadratically when units are converted, unlike the linear scaling of the standard deviation.
