# Probability and Statistics - Master Notes

*Generated: 2026-08-02*

---

## Master Table of Contents

### Phase 1: Descriptive Statistics

- [Section 1.1: Data Organization](#section-11-data-organization)
- [Section 1.2: Measures of Central Tendency](#section-12-measures-of-central-tendency)
- [Section 1.3: Measures of Position](#section-13-measures-of-position)
- [Section 1.4: Measures of Dispersion](#section-14-measures-of-dispersion)
- [Section 1.5: Core Formulas Summary (Grouped Data)](#section-15-core-formulas-summary-grouped-data)

### Phase 2: Probability Theory

- [1. Core Definitions & Set Operations](#1-core-definitions-set-operations)
- [2. Venn Diagrams & Translating Worded Problems](#2-venn-diagrams-translating-worded-problems)
- [3. Probability Axioms & Rules](#3-probability-axioms-rules)
- [4. Combinatorics and Counting Methods](#4-combinatorics-and-counting-methods)
- [5. Time-Specific Gotchas](#5-time-specific-gotchas)
- [6. Solved Exercises](#6-solved-exercises)

### Phase 3: Conditional Probability & Independence

- [1. Conditional Probability](#1-conditional-probability)
- [2. Independence](#2-independence)
- [3. Law of Total Probability & Bayes' Theorem](#3-law-of-total-probability-bayes-theorem)
- [4. Time-Specific Gotchas](#4-time-specific-gotchas)
- [5. Solved Exercises](#5-solved-exercises)

### Phase 4: Discrete Random Variables

- [1. Discrete RV Fundamentals](#1-discrete-rv-fundamentals)
- [2. Binomial Distribution](#2-binomial-distribution)
- [3. Poisson Distribution](#3-poisson-distribution)
- [4. Geometric and Hypergeometric Distributions](#4-geometric-and-hypergeometric-distributions)
- [5. Moment Generating Functions](#5-moment-generating-functions)
- [6. Time-Specific Gotchas](#6-time-specific-gotchas)
- [7. Solved Exercises](#7-solved-exercises)

### Phase 5: Continuous Random Variables & Distributions

- [1. Normal Distribution](#1-normal-distribution)
- [2. The Empirical Rule](#2-the-empirical-rule)
- [3. Continuous Uniform and Exponential Distributions](#3-continuous-uniform-and-exponential-distributions)
- [4. Gamma, Weibull, and Erlang Distributions](#4-gamma-weibull-and-erlang-distributions)
- [5. Transformations of Random Variables](#5-transformations-of-random-variables)
- [6. Time-Specific Gotchas](#6-time-specific-gotchas)
- [7. Solved Exercises](#7-solved-exercises)

### Phase 5B: Multivariate Random Variables

- [1. Multivariate Random Variables - Fundamentals](#1-multivariate-random-variables---fundamentals)
- [2. Multivariate Moments, Covariance, and Conditional Expectation](#2-multivariate-moments-covariance-and-conditional-expectation)
- [3. Functions of Multiple Random Variables & Order Statistics](#3-functions-of-multiple-random-variables-order-statistics)
- [4. Time-Specific Gotchas](#4-time-specific-gotchas)
- [5. Solved Exercises](#5-solved-exercises)

### Phase 6: Inferential Statistics

- [1. Probability Inequalities and Laws of Large Numbers](#1-probability-inequalities-and-laws-of-large-numbers)
- [2. Sampling Distributions](#2-sampling-distributions)
- [3. Central Limit Theorem (CLT)](#3-central-limit-theorem-clt)
- [4. Confidence Intervals](#4-confidence-intervals)
- [5. Hypothesis Testing](#5-hypothesis-testing)
- [6. Time-Specific Gotchas](#6-time-specific-gotchas)
- [7. Solved Exercises](#7-solved-exercises)

### Phase 7: R Programming Commands

- [1. Descriptive Statistics](#1-descriptive-statistics)
- [2. Binomial Distribution](#2-binomial-distribution)
- [3. Normal Distribution](#3-normal-distribution)
- [4. Additional Distributions](#4-additional-distributions)
- [5. Time-Specific Gotchas](#5-time-specific-gotchas)
- [6. Solved Exercises](#6-solved-exercises)

---

<!-- Source: Phases/Phase_1_Descriptive_Statistics.md -->

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

---

<!-- Source: Phases/Phase_2_Probability_Theory.md -->

# Phase 2: Probability Theory

## Table of Contents
1. [Core Definitions & Set Operations](#1-core-definitions--set-operations)
2. [Venn Diagrams & Translating Worded Problems](#2-venn-diagrams--translating-worded-problems)
3. [Probability Axioms & Rules](#3-probability-axioms--rules)
4. [Combinatorics and Counting Methods](#4-combinatorics-and-counting-methods)
5. [Time-Specific Gotchas](#5-time-specific-gotchas)
6. [Solved Exercises](#6-solved-exercises)
7. [Phase Summary](#7-phase-summary)

---

## 1. Core Definitions & Set Operations

Set Theory provides the mathematical language used to define and manipulate probability. Every probability problem is, at its core, a question about sets.

### Sample Space ($\Omega$)
The **Sample Space** $\Omega$ (also written $S$) is the set of **all possible outcomes** of a random experiment. Every outcome that could conceivably occur must be listed exactly once.
- **Standard Example:** $\Omega = \{1, 2, 3, 4, 5, 6\}$ (rolling a die).
- **Time Context Example:** $\Omega = [0, 5]\text{ s}$ (response time of a server, a continuous sample space).

**Key rule:** The sample space is always exhaustive (covers everything) and mutually exclusive (no outcome appears twice).

### Event
An **Event** is any subset of the sample space. It is a collection of one or more outcomes. We typically label events with capital letters $A$, $B$, $C$, etc.
$$A \subseteq \Omega$$
- **Elementary event:** A single outcome, e.g., $\{3\}$ when rolling a die, or $\{1.5\text{ s}\}$ for a specific response time.
- **Compound event:** A collection of outcomes, e.g., $\{2, 4, 6\}$ (even number), or $\{t : 1\text{ s} \le t < 2\text{ s}\}$.
- **Impossible event ($\emptyset$):** The empty set. An event with no outcomes.
- **Certain event ($\Omega$):** The entire sample space.

### Set Operations

These operations are the building blocks of all probability expressions.

#### Union ($\cup$)
The union $A \cup B$ is the event that **at least one** of $A$ or $B$ occurs.
$$A \cup B = \{ \omega \in \Omega : \omega \in A \text{ or } \omega \in B \}$$
> Think of $\cup$ as the logical **OR**.

#### Intersection ($\cap$)
The intersection $A \cap B$ is the event that **both** $A$ and $B$ occur simultaneously.
$$A \cap B = \{ \omega \in \Omega : \omega \in A \text{ and } \omega \in B \}$$
> Think of $\cap$ as the logical **AND**.

#### Complement ($A'$ or $A^c$)
The complement $A'$ is the event that $A$ does **not** occur.
$$A' = \{ \omega \in \Omega : \omega \notin A \}$$

A fundamental identity:
$$A \cup A' = \Omega \quad \text{and} \quad A \cap A' = \emptyset$$
$$P(A') = 1 - P(A)$$

### Mutual Exclusivity (Disjoint Events)
Two events $A$ and $B$ are **mutually exclusive** (or disjoint) if they cannot both occur at the same time:
$$A \cap B = \emptyset$$
When $A$ and $B$ are mutually exclusive, the addition rule simplifies:
$$P(A \cup B) = P(A) + P(B) \quad \text{(only when } A \cap B = \emptyset \text{)}$$

---

## 2. Venn Diagrams & Translating Worded Problems

Venn Diagrams are a visual tool that maps relationships between events onto overlapping circles. They **translate English language problem descriptions into precise set notation**.

### Standard Venn Diagram Layout

For two events $A$ and $B$ within a sample space $\Omega$, the diagram divides the space into four mutually exclusive regions:

| Region | Set Notation | Meaning | Time Meaning |
| :--- | :--- | :--- | :--- |
| Left circle only | $A \cap B'$ | A occurs, B does not | A occurs, B does not |
| Overlapping center | $A \cap B$ | Both A and B occur | Both A and B occur |
| Right circle only | $A' \cap B$ | B occurs, A does not | B occurs, A does not |
| Outside both circles | $A' \cap B'$ | Neither A nor B occurs | Neither A nor B occurs |

The **fundamental partition rule**: the four regions are mutually exclusive and collectively exhaustive. Their probabilities sum to 1.
$$P(A \cap B') + P(A \cap B) + P(A' \cap B) + P(A' \cap B') = 1$$

### Translating Key Phrases into Set Notation

| English Phrase | Set Notation | Notes |
| :--- | :--- | :--- |
| "A occurs" | $A$ | Direct |
| "A does not occur" | $A'$ | Complement |
| "Both A and B occur" | $A \cap B$ | Intersection |
| "At least one of A, B occurs" | $A \cup B$ | Union (includes both) |
| "Exactly one of A, B occurs" | $(A \cap B') \cup (A' \cap B)$ | Union minus the overlap |
| "Only A occurs" | $A \cap B'$ | A but not B |
| "Only B occurs" | $A' \cap B$ | B but not A |
| "Neither A nor B occurs" | $A' \cap B'$ = $(A \cup B)'$ | Outside both circles |
| "At most one of A, B" | $(A \cap B)'$ = $A' \cup B'$ | Not both simultaneously |

> **Critical insight:** "At least one" means $A \cup B$. "Exactly one" means $A \cup B$ minus the case where both occur, i.e., $(A \cup B) \setminus (A \cap B)$.

### Extending to Three Events

For three events $A$, $B$, $C$, the Venn Diagram has **8 mutually exclusive regions**.
- **All three occur:** $A \cap B \cap C$
- **At least one occurs:** $A \cup B \cup C$
- **None occur:** $A' \cap B' \cap C' = (A \cup B \cup C)'$

---

## 3. Probability Axioms & Rules

The **Probability Axioms** (Kolmogorov's Axioms) are the three foundational rules from which all of probability theory is derived.

### Kolmogorov's Axioms

**Axiom 1 (Non-negativity):**
$$P(A) \geq 0$$

**Axiom 2 (Normalization):**
$$P(\Omega) = 1$$

**Axiom 3 (Countable Additivity):**
If $A$ and $B$ are mutually exclusive ($A \cap B = \emptyset$):
$$P(A \cup B) = P(A) + P(B)$$

### The Addition Rule (General)

For any two events $A$ and $B$ (not necessarily mutually exclusive):
$$\boxed{P(A \cup B) = P(A) + P(B) - P(A \cap B)}$$

**Extension to three events (Inclusion-Exclusion Principle):**
$$P(A \cup B \cup C) = P(A) + P(B) + P(C) - P(A \cap B) - P(A \cap C) - P(B \cap C) + P(A \cap B \cap C)$$

### De Morgan's Laws

De Morgan's Laws describe the complement of a union or intersection. They "push the complement inside" while swapping the operator between $\cup$ and $\cap$.

**First Law:**
$$\boxed{(A \cup B)' = A' \cap B'}$$
$$P((A \cup B)') = P(A' \cap B')$$
(Reading: "NOT (A or B)" is the same as "(NOT A) AND (NOT B)". Neither event occurs.)

**Second Law:**
$$\boxed{(A \cap B)' = A' \cup B'}$$
$$P((A \cap B)') = P(A' \cup B')$$
(Reading: "NOT (A and B)" is the same as "(NOT A) OR (NOT B)". At least one event fails to occur.)

---

## 4. Combinatorics and Counting Methods

When outcomes in a sample space $\Omega$ are equally likely, the probability of an event $A$ is:
$$P(A) = \frac{|A|}{|\Omega|}$$

### Fundamental Principles of Counting
- **Multiplication Rule (Product Rule):** Sequence of operations. $N = n_1 \cdot n_2 \cdot \dots \cdot n_k$
- **Addition Rule (Sum Rule):** Disjoint operations. $N = n_1 + n_2$

### Permutations
An ordered arrangement. The order of selection matters.
- **Distinct Objects:** $P(n, r) = \frac{n!}{(n-r)!}$
- **With Repetition (Identical Objects):** $P(n; n_1, \dots, n_k) = \frac{n!}{n_1! \dots n_k!}$
- **Circular Permutations:** $(n - 1)!$

### Combinations
A selection without regard to order.
- **Distinct Objects (Without Replacement):** $C(n, r) = \binom{n}{r} = \frac{n!}{r!(n-r)!}$
- **With Replacement:** $C^{R}(n, r) = \binom{n + r - 1}{r} = \frac{(n + r - 1)!}{r!(n - 1)!}$

### Partitions & Multinomial Coefficients
Partition $n$ distinct objects into $k$ groups of sizes $r_1, r_2, \ldots, r_k$:
$$\binom{n}{r_1, r_2, \dots, r_k} = \frac{n!}{r_1! \cdot r_2! \dots r_k!}$$

---

## 5. Time-Specific Gotchas

When dealing with time-based sample spaces, several specific rules apply:

1. **Continuous vs. Discrete Time:** Time can be continuous ($\Omega = [0, T]$) or discrete ($\Omega = \{t_1, t_2\}$). Boundaries matter in discrete time, but the probability of an exact boundary point in continuous time is $0$ (i.e., $P(T = t_0) = 0$).
2. **Overlapping Time Intervals:** For $A = [0, 100)\text{ ms}$ and $B = [50, 150)\text{ ms}$, the overlap $A \cap B = [50, 100)\text{ ms}$ is non-empty. They are not mutually exclusive.
3. **Cyclic Time (Wrap-Around):** On a 24-hour clock, an event like "between 22:00 and 02:00" wraps around midnight and forms a union of two intervals: $A = [22, 24) \cup [0, 2)$.
4. **Mutually Exclusive Time Events Are Maximally Dependent:** If $A$ = "response $< 50\text{ ms}$" and $B$ = "response $> 200\text{ ms}$", they are mutually exclusive. Knowing $A$ occurred means $B$ definitely did not. They are not independent.
5. **Time Slots are Labeled:** 9:00 is not identical to 10:00. Combinatorially, they are distinct objects.

---

## 6. Solved Exercises

#### Exercise 1: Identifying the Sample Space (Die Roll)
**Problem:** A fair six-sided die is rolled once. Define the sample space and the event $A$ = "rolling a number greater than 4".
**Solution:**
$$\Omega = \{1, 2, 3, 4, 5, 6\}$$
$$A = \{5, 6\}$$
$$A' = \{1, 2, 3, 4\} \quad \text{(not rolling greater than 4)}$$

#### Exercise 2: Identifying the Sample Space (Response Time)
**Problem:** A server responds to a request in at most 5 seconds. The response time $T$ is measured. Define the sample space and the event $A$ = "response time greater than 3 seconds".
**Solution:**
$$\Omega = [0, 5]\text{ s}$$
$$A = (3, 5]\text{ s}$$
$$A' = [0, 3]\text{ s} \quad \text{(response time at most 3 seconds)}$$

#### Exercise 3: Identifying the Sample Space (Two Time Slots)
**Problem:** A task is scheduled in one of two time slots: Morning (M) or Afternoon (A). Write out $\Omega$ using ordered pairs where the first element is the first task's slot and the second is the second task's slot. Define event $B$ = "at least one task is in the Morning".
**Solution:**
$$\Omega = \{(M,M), (M,A), (A,M), (A,A)\}$$
$$B = \{(M,M), (M,A), (A,M)\}$$
$$B' = \{(A,A)\} \quad \text{(both tasks in the Afternoon)}$$

#### Exercise 4: Computing Union and Intersection of Time Events
**Problem:** From the response-time sample space $\Omega = [0, 10]\text{ s}$, let:
- $A$ = "response time less than 4 seconds" = $[0, 4)\text{ s}$
- $B$ = "response time greater than 3 seconds" = $(3, 10]\text{ s}$
Find $A \cup B$ and $A \cap B$.
**Solution:**
$$A \cup B = [0, 10]\text{ s} = \Omega \quad \text{(every response time is either < 4 or > 3)}$$
$$A \cap B = (3, 4)\text{ s} \quad \text{(response times between 3 and 4 seconds)}$$
> **Note:** $A$ and $B$ are **not** mutually exclusive because $A \cap B = (3, 4)\text{ s} \neq \emptyset$.

#### Exercise 5: Computing the Complement of a Time Event
**Problem:** Using $A = [0, 4)\text{ s}$ from Exercise 4, find $A'$ and verify the fundamental identity.
**Solution:**
$$A' = [4, 10]\text{ s}$$
**Verification:**
$$A \cup A' = [0, 4) \cup [4, 10] = [0, 10] = \Omega \checkmark$$
$$A \cap A' = [0, 4) \cap [4, 10] = \emptyset \checkmark$$

#### Exercise 6: Mutually Exclusive Time Events
**Problem:** A request can be classified by response time category: $A$ = "fast ($< 50\text{ ms}$)" and $B$ = "slow ($> 200\text{ ms}$)". Are $A$ and $B$ mutually exclusive?
**Solution:**
$$A = [0, 50)\text{ ms}, \quad B = (200, \infty)\text{ ms}$$
$$A \cap B = \emptyset$$
Yes, $A$ and $B$ are mutually exclusive. A single response cannot be both fast and slow simultaneously.

#### Exercise 7: Three Time Events - Union and Intersection
**Problem:** A request is monitored across three time thresholds. Define:
- $A$ = "response time $< 100\text{ ms}$"
- $B$ = "response time $> 50\text{ ms}$"
- $C$ = "response time $< 200\text{ ms}$"
With $\Omega = [0, 500]\text{ ms}$, describe $A \cap B$, $A \cup C$, and $B \cap C'$.
**Solution:**
*   $A \cap B$ = $(50, 100)\text{ ms}$.
*   $A \cup C$ = $[0, 200)\text{ ms}$ (since $A \subseteq C$, the union is just $C$).
*   $C'$ = $[200, 500]\text{ ms}$.
*   $B \cap C'$ = $[200, 500]\text{ ms}$.

#### Exercise 8: Subset Relationship for Time Events
**Problem:** A response time $T$ is measured in $\Omega = [0, 10]\text{ s}$. Let:
- $A$ = "response time $< 1\text{ s}$" = $[0, 1)\text{ s}$
- $B$ = "response time $< 5\text{ s}$" = $[0, 5)\text{ s}$
Is $A$ a subset of $B$? What does this imply?
**Solution:**
Every time value in $A$ ($0 \le t < 1$) is also in $B$ ($0 \le t < 5$), so $A \subseteq B$.
This means: if event $A$ occurs, then event $B$ must also occur. Formally: $A \subseteq B \Rightarrow A \cap B = A$.

#### Exercise 9: Cyclic Time Event (Wrap-Around Midnight)
**Problem:** A maintenance window is defined as "between 22:00 and 02:00" on a 24-hour clock. Express this event as a set on $\Omega = [0, 24)\text{ h}$.
**Solution:**
The event wraps around midnight, so it is a **union of two intervals**:
$$A = [22, 24) \cup [0, 2) \text{ (hours)}$$
The complement (no maintenance) is:
$$A' = [2, 22) \text{ (hours)}$$

#### Exercise 10: Building a Venn Diagram from Time-Based Counts
**Problem:** In a sample of 50 requests, 30 had response time $< 100\text{ ms}$ ($F$), 25 arrived during peak hours ($P$), and 15 were both fast and during peak. Find the number of requests that were only fast, only during peak, and neither.
**Solution:**
**Step 1:** Find the overlap region first: $|F \cap P| = 15$
**Step 2:** Find "only fast": $|F \cap P'| = |F| - |F \cap P| = 30 - 15 = 15$
**Step 3:** Find "only peak": $|F' \cap P| = |P| - |F \cap P| = 25 - 15 = 10$
**Step 4:** Find "neither": $|F' \cap P'| = 50 - 15 - 15 - 10 = 10$

#### Exercise 11: Translating "At Least One" (Time Events)
**Problem:** $P(A) = 0.5$ (request timed out), $P(B) = 0.4$ (request retried), $P(A \cap B) = 0.2$ (timed out and retried). Find the probability that at least one of $A$ or $B$ occurs.
**Solution:**
"At least one" translates to $A \cup B$.
$$P(A \cup B) = P(A) + P(B) - P(A \cap B) = 0.5 + 0.4 - 0.2 = 0.7$$

#### Exercise 12: Translating "Neither" (Time Events)
**Problem:** Using the values from Exercise 11, find the probability that neither $A$ nor $B$ occurs.
**Solution:**
"Neither" translates to $A' \cap B' = (A \cup B)'$.
$$P((A \cup B)') = 1 - P(A \cup B) = 1 - 0.7 = 0.3$$

#### Exercise 13: Translating "Exactly One" (Time Events)
**Problem:** Using the values from Exercise 11, find the probability that exactly one of $A$ or $B$ occurs.
**Solution:**
"Exactly one" = $(A \cap B') \cup (A' \cap B)$.
$$P(\text{exactly one}) = P(A \cup B) - P(A \cap B) = 0.7 - 0.2 = 0.5$$

#### Exercise 14: Translating "Only A" (Time Events)
**Problem:** $P(A) = 0.6$ (slow response), $P(B) = 0.5$ (high CPU load), $P(A \cup B) = 0.8$. Find $P(\text{only } A)$.
**Solution:**
**Step 1:** $P(A \cap B) = P(A) + P(B) - P(A \cup B) = 0.6 + 0.5 - 0.8 = 0.3$
**Step 2:** $P(A \cap B') = P(A) - P(A \cap B) = 0.6 - 0.3 = 0.3$

#### Exercise 15: Backward Problem - Finding an Unknown (Time Events)
**Problem:** Given $P(A) = 0.45$, $P(B) = 0.30$, and $P(\text{exactly one of } A, B) = 0.55$. Find $P(A \cap B)$.
**Solution:**
$$P(\text{exactly one}) = P(A) + P(B) - 2 \cdot P(A \cap B)$$
$$0.55 = 0.45 + 0.30 - 2 \cdot P(A \cap B)$$
$$2 \cdot P(A \cap B) = 0.75 - 0.55 = 0.20 \implies P(A \cap B) = 0.10$$

#### Exercise 16: Applying De Morgan's Laws (Time Events)
**Problem:** $P(A) = 0.5$ (timeout), $P(B) = 0.4$ (retry), $P(A \cap B) = 0.2$ (both). Find $P(A' \cap B')$ and $P(A' \cup B')$.
**Solution:**
**Step 1:** $P(A \cup B) = 0.5 + 0.4 - 0.2 = 0.7$
**Step 2 (De Morgan's First Law):** $P(A' \cap B') = P((A \cup B)') = 1 - 0.7 = 0.3$
**Step 3 (De Morgan's Second Law):** $P(A' \cup B') = P((A \cap B)') = 1 - 0.2 = 0.8$

#### Exercise 17: Mutually Exclusive Time Events
**Problem:** Two time events $A$ and $B$ are mutually exclusive. $P(A) = 0.35$, $P(B) = 0.25$. Find $P(A \cup B)$ and $P(A' \cap B')$.
**Solution:**
Since $A \cap B = \emptyset$, $P(A \cap B) = 0$.
$P(A \cup B) = 0.35 + 0.25 = 0.60$
$P(A' \cap B') = 1 - 0.60 = 0.40$

#### Exercise 18: Checking Axiom Compliance (Time Events)
**Problem:** A student claims: $P(A) = 0.7$, $P(B) = 0.6$, $P(A \cup B) = 0.8$. Is this consistent with the probability axioms?
**Solution:**
$P(A \cap B) = 0.7 + 0.6 - 0.8 = 0.5$.
Check 1: $0.5 \ge 0$.
Check 2: $0.5 \le 0.7$ and $0.5 \le 0.6$.
Check 3: $0.8 \le 1$.
All axioms satisfied. The assignment is consistent.

#### Exercise 19: Full Multi-Step Problem (Time Events)
**Problem:** In a group of 100 requests, 60 had response time $< 100\text{ ms}$ ($F$), 45 arrived during peak hours ($P$), and 20 were neither. Find: (a) number both fast and during peak, (b) $P(F' \cup P')$.
**Solution:**
**Step 1:** $P(F \cup P) = 0.80$ (since 20 were neither).
**Step 2:** $P(F \cap P) = 0.60 + 0.45 - 0.80 = 0.25 \implies 25\text{ requests}$.
**Step 3:** $P(F' \cup P') = 1 - P(F \cap P) = 1 - 0.25 = 0.75$.

#### Exercise 20: License Plate Codes (Multiplication Rule)
**Problem:** A license plate contains 3 letters followed by 3 digits. Letters cannot be repeated, but digits can. How many distinct plates?
**Solution:**
Letters: $26 \cdot 25 \cdot 24$ choices.
Digits: $10 \cdot 10 \cdot 10$ choices.
Total $= 26 \cdot 25 \cdot 24 \cdot 10 \cdot 10 \cdot 10 = 15,600,000$.

#### Exercise 21: Arranging Tasks in a Timeline (Permutations)
**Problem:** There are 4 monitoring tasks, 3 backup tasks, and 2 cleanup tasks. In how many ways can they be arranged in a 9-slot timeline if tasks of the same type must be consecutive?
**Solution:**
Arrange 3 task types: $3! = 6$ ways.
Arrange within types: $4! \cdot 3! \cdot 2! = 24 \cdot 6 \cdot 2 = 288$ ways.
Total $= 6 \cdot 288 = 1728$ ways.

#### Exercise 22: Selecting Time Slots for Maintenance (Combinations)
**Problem:** From 8 available hourly time slots, choose 3 slots for maintenance. How many ways?
**Solution:**
Order does not matter.
$$\binom{8}{3} = \frac{8!}{3! \cdot 5!} = \frac{8 \cdot 7 \cdot 6}{3 \cdot 2 \cdot 1} = 56 \text{ ways.}$$

#### Exercise 23: Distributing Time Slots Among Servers (Multinomial)
**Problem:** In how many ways can 10 distinct time slots be distributed among 3 servers if server A receives 5, B receives 3, and C receives 2?
**Solution:**
$$\binom{10}{5, 3, 2} = \frac{10!}{5! \cdot 3! \cdot 2!} = 2520 \text{ ways.}$$

#### Exercise 24: Circular Scheduling (Round-the-Clock Shifts)
**Problem:** In how many ways can 6 servers be arranged in a circular 24-hour shift rotation?
**Solution:**
For circular permutations: $(n-1)!$
$(6 - 1)! = 5! = 120 \text{ ways.}$

#### Exercise 25: Standard Poker Hands (Combination)
**Problem:** Probability of being dealt a "Four of a Kind" (4 cards of one rank, 1 card of another) in a 5-card hand from a 52-card deck?
**Solution:**
$$|\Omega| = \binom{52}{5} = 2,598,960$$
Favorable: $\binom{13}{1}$ for rank, $\binom{4}{4}$ for cards of rank, $\binom{48}{1}$ for last card.
$$|A| = 13 \cdot 1 \cdot 48 = 624$$
$$P = \frac{624}{2,598,960} \approx 0.00024$$

#### Exercise 26: Pathfinding on a Grid
**Problem:** A grid has coordinates from $(0,0)$ to $(5,4)$. A path moves only step-by-step to the right or up. How many paths exist?
**Solution:**
Total moves $n = 9$. We must choose which 5 are Right (R).
$$\binom{9}{5} = \frac{9!}{5! \cdot 4!} = 126 \text{ paths.}$$

#### Exercise 27: Selecting Time Intervals with Repetition
**Problem:** A system has 4 types of maintenance intervals. Select 6 intervals for a workday (repetition allowed).
**Solution:**
$$\binom{n + r - 1}{r} = \binom{4 + 6 - 1}{6} = \binom{9}{6} = 84 \text{ ways.}$$

#### Exercise 28: Probability of Execution Time Sum
**Problem:** Three tasks are randomly assigned execution times of 1, 2, 3, 4, 5, or 6 seconds each. What is the probability that the total time is exactly 5 seconds?
**Solution:**
$|\Omega| = 6^3 = 216$.
Partitions of 5 into 3 positive integers: $\{3,1,1\}$ (3 ways) and $\{2,2,1\}$ (3 ways).
$|A| = 6$.
$P = \frac{6}{216} = \frac{1}{36}$.

#### Exercise 29: R Snippet -- Venn Diagram Counts
**Problem:** R code for computing 4 Venn diagram regions for 50 requests (30 fast, 25 peak, 15 both).
**Solution:**
```r
n <- 50; n_F <- 30; n_P <- 25; both <- 15
only_F <- n_F - both
only_P <- n_P - both
neither <- n - only_F - only_P - both
cat("Only F:", only_F, "Only P:", only_P, "Both:", both, "Neither:", neither, "\n")
```

#### Exercise 30: R Snippet -- Combinatorics
**Problem:** R code to choose 3 slots from 8, and distribute 10 slots among servers (5, 3, 2).
**Solution:**
```r
choose(8, 3) # 56
factorial(10) / (factorial(5) * factorial(3) * factorial(2)) # 2520
```

---

## Phase Summary
- Set theory forms the foundation of probability. Events are subsets of the sample space $\Omega$.
- Union ($\cup$) represents logical OR, Intersection ($\cap$) represents logical AND, and Complement ($A'$) represents logical NOT.
- Mutually exclusive events cannot occur simultaneously ($A \cap B = \emptyset$).
- Venn diagrams provide a visual method to translate worded probability problems into precise regions, fundamentally relying on the rule: $P(A \cap B') + P(A \cap B) + P(A' \cap B) + P(A' \cap B') = 1$.
- Kolmogorov's axioms state probabilities are non-negative, the sample space probability is 1, and the probability of mutually exclusive unions is the sum of their individual probabilities.
- The General Addition Rule handles non-mutually exclusive events: $P(A \cup B) = P(A) + P(B) - P(A \cap B)$.
- De Morgan's Laws simplify complement expressions: $(A \cup B)' = A' \cap B'$ and $(A \cap B)' = A' \cup B'$.
- Combinatorics provides counting rules essential for equally likely outcomes: $P(A) = \frac{|A|}{|\Omega|}$.
- Permutations count ordered arrangements, whereas Combinations count unordered selections.
- Time-based problems introduce unique gotchas, such as continuous boundary overlap ($P(T = t) = 0$), cyclic wrap-around considerations, and properly differentiating between permutations and combinations when scheduling time slots.

---

<!-- Source: Phases/Phase_3_Conditional_Probability_Independence.md -->

# Phase 3: Conditional Probability & Independence

## Table of Contents
1. [Conditional Probability](#1-conditional-probability)
2. [Independence](#2-independence)
3. [Law of Total Probability & Bayes' Theorem](#3-law-of-total-probability--bayes-theorem)
4. [Time-Specific Gotchas](#4-time-specific-gotchas)
5. [Solved Exercises](#5-solved-exercises)
6. [Phase Summary](#phase-summary)

---

## 1. Conditional Probability

Conditional probability measures the likelihood of an event occurring, given that another event has already taken place. This "given" information effectively restricts the sample space to a specific subset.

### The Fundamental Formula
If $P(B) > 0$, the conditional probability of $A$ given $B$ is defined as:
$$P(A|B) = \frac{P(A \cap B)}{P(B)}$$

Where:
*   $P(A|B)$: Probability of $A$ occurring given $B$ has occurred.
*   $P(A \cap B)$: Probability that both $A$ and $B$ occur (Intersection).
*   $P(B)$: Probability of the conditioning event $B$.

**Intuitive Understanding (Reducing the Sample Space):**
Imagine a sample space $S$. When we say "given $B$", we are throwing away any part of $S$ that is not $B$. The new sample space becomes $B$. We then look for the portion of $A$ that survived this "filtering" process, which is exactly $A \cap B$.

### Conditional Probability in Time-Based Systems
In time-based systems, the conditioning event is frequently defined by elapsed durations, surviving times, or timestamp thresholds. Let $T$ be a non-negative random variable representing a duration.
The conditional probability that an operation completes before time $t_2$, given that it has already surpassed time $t_1$ (where $t_2 > t_1$), is:
$$P(T \le t_2 \mid T > t_1) = \frac{P(t_1 < T \le t_2)}{P(T > t_1)}$$

Similarly, the conditional survival probability (surviving an additional duration $s$ after surviving up to time $t$) is:
$$P(T > t + s \mid T > t) = \frac{P(T > t + s)}{P(T > t)}$$

### The Multiplication Rule
By rearranging the formula, we get the Multiplication Rule to find the probability of an intersection:
$$P(A \cap B) = P(B) \cdot P(A|B) = P(A) \cdot P(B|A)$$
For multi-stage sequential processes:
$$P(A_1 \cap A_2 \cap \dots \cap A_n) = P(A_1) \cdot P(A_2 \mid A_1) \dots P(A_n \mid A_1 \cap \dots \cap A_{n-1})$$

---

## 2. Independence

Independence is a statistical property where the occurrence of one event does not affect the probability of another event occurring.

### Mathematical Condition
Two events $A$ and $B$ are **independent** if the knowledge that $B$ has occurred does not change the probability of $A$. The **Product Rule** defines this:
$$P(A \cap B) = P(A) \cdot P(B)$$
Equivalently: $P(A|B) = P(A)$ and $P(B|A) = P(B)$.

### Independence vs. Mutually Exclusive
*   **Mutually Exclusive (Disjoint):** Events *cannot* happen at the same time ($P(A \cap B) = 0$). If $A$ happens, $B$ definitely cannot happen.
*   **Independent:** Events *can* happen at the same time, but they don't influence each other.
> **Shortcut:** If $A$ and $B$ have non-zero probabilities and are mutually exclusive, they **cannot** be independent.

### System Reliability over Execution Time
Consider $n$ components with independent lifetimes $T_1, T_2, \dots, T_n$:
1. **Series System (Requires all components to run):**
   $$P(T_{\text{sys}} > t) = \prod_{i=1}^{n} P(T_i > t)$$
2. **Parallel System (Requires at least one component to run):**
   $$P(T_{\text{sys}} \le t) = \prod_{i=1}^{n} P(T_i \le t)$$

---

## 3. Law of Total Probability & Bayes' Theorem

These two theorems are the most powerful tools in probability for handling multi-stage processes and updating beliefs based on new evidence.

### Law of Total Probability
If we have a set of events $B_1, B_2, \dots, B_n$ that **partition** the sample space (mutually exclusive and their union is the whole space), then for any event $A$:
$$P(A) = \sum_{i=1}^{n} P(A|B_i)P(B_i) = P(A|B_1)P(B_1) + \dots + P(A|B_n)P(B_n)$$

### Bayes' Theorem
Bayes' Theorem allows us to "reverse" conditional probabilities. If we know $P(A|B)$, we can find $P(B|A)$:
$$P(B_k|A) = \frac{P(A|B_k)P(B_k)}{P(A)} = \frac{P(A|B_k)P(B_k)}{\sum_{j=1}^{n} P(A|B_j)P(B_j)}$$
- **Prior Probability $P(B_k)$:** The baseline probability of state $B_k$.
- **Likelihood $P(A \mid B_k)$:** The probability of observing event $A$ given state $B_k$.
- **Posterior Probability $P(B_k \mid A)$:** The updated probability of state $B_k$ given event $A$ occurred.

---

## 4. Time-Specific Gotchas

1. **Conflating Elapsed Time with Remaining Time:** Assuming $P(T > t + s \mid T > t) = P(T > s)$ is only true for memoryless distributions (like the Exponential distribution). For aging systems, always evaluate the denominator $P(T > t)$ explicitly.
2. **Right-Censored Observation Windows:** If a process hasn't finished by a max window $T_{\text{max}}$, its duration is unknown. Not accounting for this under-estimates long latencies.
3. **Mixed Unit Prefixes:** When calculating $P(A \cap B) / P(B)$, ensure both use identical time units (e.g., ms vs seconds).
4. **Consecutive Time Windows (Autocorrelation):** Treating consecutive time intervals (e.g., minute $t$ and $t+1$) as independent often fails because they are correlated.
5. **Shared Infrastructure Contention:** Two timers on separate VMs may seem independent but could share a physical clock or hypervisor, violating independence during host overload.
6. **Non-Exhaustive Time Partitions:** When using Total Probability, the time fractions must sum to 1.
7. **Confusing Prior Duration with Posterior Probabilities:** If a system is in High-Load 10% of the time, the probability it was in High-Load *given* a timeout occurred is a posterior probability, which will be much higher than 10%.

---

## 5. Solved Exercises

#### Exercise 1: Medical Diagnostic Test (Classic Bayes)
**Problem:** A disease affects 1% of the population. A test is 95% accurate for those with the disease and 90% accurate for those without. If a person tests positive, what is the probability they have the disease?
**Solution:**
- $P(H) = 0.01, P(H^c) = 0.99$
- $P(Pos|H) = 0.95, P(Pos|H^c) = 1 - 0.90 = 0.10$
- Total probability $P(Pos) = (0.95 \cdot 0.01) + (0.10 \cdot 0.99) = 0.0095 + 0.0990 = 0.1085$.
- Bayes: $P(H|Pos) = \frac{0.0095}{0.1085} \approx 0.0876 \text{ (8.76\%)}$.

#### Exercise 2: System Uptime Survival Probability
**Problem:** The probability a cloud instance functions past 10 hours is 0.85, and past 24 hours is 0.60. Given it has run for 10 hours, what is the probability it reaches 24 hours?
**Solution:**
$$P(T > 24 \mid T > 10) = \frac{P(T > 24 \cap T > 10)}{P(T > 10)} = \frac{P(T > 24)}{P(T > 10)} = \frac{0.60}{0.85} \approx 0.7059$$

#### Exercise 3: Server Response Time SLA
**Problem:** A service records response times $T$ in ms. $P(T \le 100) = 0.70$ and $P(T \le 300) = 0.95$. If a request has not completed within 100 ms, what is the probability it completes within 300 ms?
**Solution:**
$P(T > 100) = 0.30$.
$P(100 < T \le 300) = 0.95 - 0.70 = 0.25$.
$$P(T \le 300 \mid T > 100) = \frac{0.25}{0.30} \approx 0.8333$$

#### Exercise 4: Two-Way Frequency Table of Incident Resolution Times
**Problem:** Out of 200 incidents, Day Shift had 90 $\le 1\text{ hr}$ and 30 $>1\text{ hr}$. Night Shift had 40 $\le 1\text{ hr}$ and 40 $>1\text{ hr}$. Find probability an incident took $>1\text{ hr}$ given Night shift.
**Solution:**
Night Shift Total = 80. Night Shift $>1\text{ hr}$ = 40.
$$P(>1\text{ hr} \mid N) = \frac{40}{80} = 0.50$$

#### Exercise 5: Sequential Network Hops
**Problem:** Packet passes Router 1 with 0.98. Given R1, it passes R2 with 0.95. Given R1 and R2, passes R3 with 0.90. What is the probability it completes the path?
**Solution:**
$$P(R_1 \cap R_2 \cap R_3) = 0.98 \cdot 0.95 \cdot 0.90 = 0.8379$$

#### Exercise 6: Microservice Timeout Cascade
**Problem:** Service A takes $T_A$ ms, B takes $T_B$ ms. $P(T_A \le 50) = 0.80$. $P(T_B \le 50 \mid T_A \le 50) = 0.90$. Find the probability both finish within 50 ms.
**Solution:**
$$P(T_A \le 50 \cap T_B \le 50) = 0.80 \cdot 0.90 = 0.72$$

#### Exercise 7: Independent Server Timeout Events
**Problem:** Two isolated servers have independent timeout probabilities: $P(T_1) = 0.04$ and $P(T_2) = 0.05$. Probability both timeout?
**Solution:**
$$P(T_1 \cap T_2) = 0.04 \cdot 0.05 = 0.0020 \text{ (0.2\%)}$$

#### Exercise 8: Parallel Redundant Watchdog Timers
**Problem:** Two independent hardware timers have failure probability $0.02$ each over 24 hours. Probability system works (at least one works)?
**Solution:**
$P(F_1 \cap F_2) = 0.02 \cdot 0.02 = 0.0004$.
$P(\text{System Works}) = 1 - 0.0004 = 0.9996 \text{ (99.96\%)}$.

#### Exercise 9: Series Pipeline Lifetime
**Problem:** 3 sequential stages operate independently. Survival probabilities $P(T_1 > 8) = 0.95, P(T_2 > 8) = 0.90, P(T_3 > 8) = 0.98$. Pipeline survival?
**Solution:**
$$P(T_{\text{sys}} > 8) = 0.95 \cdot 0.90 \cdot 0.98 = 0.8379$$

#### Exercise 10: Testing Independence of Latency Spikes
**Problem:** Service A spikes in 100/1000 mins ($0.10$). B spikes in 150/1000 mins ($0.15$). Both spike in 30/1000 mins ($0.03$). Are they independent?
**Solution:**
$P(A) \cdot P(B) = 0.10 \cdot 0.15 = 0.015$.
Since $P(A \cap B) = 0.03 \neq 0.015$, they are dependent.

#### Exercise 11: Probability of At Least One Outage
**Problem:** Probability of network glitch in 1 hour is 0.10. Across 4 independent hours, find probability of at least one glitch.
**Solution:**
$P(\text{No glitch in 1 hr}) = 0.90$.
$P(\text{No glitches in 4 hrs}) = (0.90)^4 = 0.6561$.
$P(\text{At least 1}) = 1 - 0.6561 = 0.3439 \text{ (34.39\%)}$.

#### Exercise 12: Probability of Exactly One Service Timeout
**Problem:** Independent microservices have timeouts $P(T_A) = 0.15, P(T_B) = 0.10$. Probability exactly one times out?
**Solution:**
$P(T_A \cap T_B^c) = 0.15 \cdot 0.90 = 0.135$.
$P(T_B \cap T_A^c) = 0.10 \cdot 0.85 = 0.085$.
$P(\text{Exactly one}) = 0.135 + 0.085 = 0.220$.

#### Exercise 13: Overall Latency Spike Probability (Total Probability)
**Problem:** Morning Peak (40%), Afternoon (40%), Night (20%). Probability query $>100\text{ ms}$ is 0.15, 0.05, 0.01 respectively. Find total probability.
**Solution:**
$$P(A) = (0.15 \cdot 0.40) + (0.05 \cdot 0.40) + (0.01 \cdot 0.20) = 0.060 + 0.020 + 0.002 = 0.082 \text{ (8.2\%)}$$

#### Exercise 14: Diagnosing Load Regime from Latency Spike (Bayes)
**Problem:** Using Exercise 13, if a query takes $>100\text{ ms}$, what is the posterior probability it was Morning Peak?
**Solution:**
$$P(B_1 \mid A) = \frac{0.15 \cdot 0.40}{0.082} = \frac{0.060}{0.082} \approx 0.7317 \text{ (73.17\%)}$$

#### Exercise 15: Software Bug Discovery Timing
**Problem:** Bugs found in Unit Test (50%), Integration (30%), Production (20%). Prob bug takes $>24\text{h}$ to resolve is 0.10, 0.40, 0.90 respectively. Total probability a bug takes $>24\text{h}$?
**Solution:**
$$P(>24\text{h}) = (0.10 \cdot 0.50) + (0.40 \cdot 0.30) + (0.90 \cdot 0.20) = 0.05 + 0.12 + 0.18 = 0.350$$

#### Exercise 16: Cloud Server Crash Diagnosis
**Problem:** Reboots due to Memory Leaks (50%), Power Spikes (30%), OS Updates (20%). Reboot $>5\text{m}$ probability is 0.90, 0.10, 0.30 respectively. Given reboot $>5\text{m}$, probability it was Memory Leak?
**Solution:**
$$P(>5\text{m}) = (0.90 \cdot 0.50) + (0.10 \cdot 0.30) + (0.30 \cdot 0.20) = 0.45 + 0.03 + 0.06 = 0.54$$
$$P(\text{Leak} \mid >5\text{m}) = \frac{0.45}{0.54} = \frac{5}{6} \approx 0.8333$$

#### Exercise 17: R Code Snippet -- Empirical Conditional Latency Calculation
**Problem:** R code to calculate conditional probability $P(T \le 250 \mid T > 100)$.
**Solution:**
```r
latencies_ms <- rgamma(1000, shape = 2, scale = 80)
conditioned_subset <- latencies_ms[latencies_ms > 100]
p_cond <- sum(conditioned_subset <= 250) / length(conditioned_subset)
```

#### Exercise 18: R Code Snippet -- Testing Independence
**Problem:** R code to test whether delays in two consecutive steps are statistically independent.
**Solution:**
```r
cor_val <- cor(t1, t2)
test_res <- cor.test(t1, t2)
```

#### Exercise 19: R Code Snippet -- Bayes Updating
**Problem:** R function for Bayes' updating.
**Solution:**
```r
bayes_time_update <- function(priors, likelihoods) {
  p_total <- sum(priors * likelihoods)
  posteriors <- (priors * likelihoods) / p_total
  return(list(total_prob = p_total, posteriors = posteriors))
}
```

---

## Phase Summary
- Conditional Probability $P(A|B) = \frac{P(A \cap B)}{P(B)}$ measures the probability of $A$ in the restricted sample space where $B$ has already occurred.
- The Multiplication Rule is derived from conditional probability and is essential for evaluating intersections of sequential events.
- Events are Independent if $P(A \cap B) = P(A)P(B)$. Independence implies that the occurrence of one event provides no information about the other.
- Mutually exclusive non-zero events are never independent (they are maximally dependent).
- For independent components, Series Systems survive if all components survive ($\prod P(T_i > t)$), and Parallel Systems fail if all components fail ($\prod P(T_i \le t)$).
- The Law of Total Probability computes the overall probability of an event by summing its occurrence across all mutually exclusive and exhaustive partitions of the sample space.
- Bayes' Theorem $P(B_k|A) = \frac{P(A|B_k)P(B_k)}{P(A)}$ provides the mechanism to reverse conditional probabilities, updating prior beliefs (e.g., time regime probabilities) based on new evidence (e.g., an observed anomaly).
- When applying these concepts to time series or system logs, right-censoring, correlated consecutive intervals, and unnormalized rates are the most common sources of error.

---

<!-- Source: Phases/Phase_4_Discrete_Random_Variables.md -->

# Phase 4: Discrete Random Variables

## Table of Contents
1. [Discrete RV Fundamentals](#1-discrete-rv-fundamentals)
2. [Binomial Distribution](#2-binomial-distribution)
3. [Poisson Distribution](#3-poisson-distribution)
4. [Geometric and Hypergeometric Distributions](#4-geometric-and-hypergeometric-distributions)
5. [Moment Generating Functions](#5-moment-generating-functions)
6. [Time-Specific Gotchas](#6-time-specific-gotchas)
7. [Solved Exercises](#7-solved-exercises)
8. [Phase Summary](#phase-summary)

---

## 1. Discrete RV Fundamentals

A **Discrete Random Variable** takes on a finite or countably infinite set of values. In a time context, it maps time-based outcomes (clock tick counts, discrete delay steps) to numerical values.

### Probability Mass Function (PMF)
The PMF is $p(x) = P(X = x)$. It must satisfy:
1. $p(x) \geq 0$
2. $\sum p(x) = 1$

### Expected Value $E[X]$
The Expected Value (mean) is the probability-weighted average:
$$E[X] = \mu = \sum x \cdot p(x)$$
Linearity: $E[aX + b] = a \cdot E[X] + b$

### Variance $V(X)$
Variance measures spread:
$$V(X) = E[X^2] - (E[X])^2$$
where $E[X^2] = \sum x^2 \cdot p(x)$.
Properties: $V(aX + b) = a^2 \cdot V(X)$

---

## 2. Binomial Distribution

Models the number of successes in a fixed sequence of independent trials.

### The Four Conditions (FINS)
1. **F**ixed number of trials $n$.
2. **I**ndependence between trials.
3. **N**o more than two outcomes (success/failure).
4. **S**ame probability of success $p$ for all trials.

### Formulae
*   **PMF:** $P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$
*   **Mean:** $E[X] = n \cdot p$
*   **Variance:** $V(X) = n \cdot p \cdot (1-p)$

---

## 3. Poisson Distribution

Models the count of rare, independent events occurring within a fixed time window at a constant average rate $\lambda$.

### Formulae
*   **PMF:** $P(X_t = k) = \frac{(\lambda \cdot t)^k \cdot e^{-\lambda \cdot t}}{k!}$
*   **Mean:** $E[X_t] = \lambda \cdot t$
*   **Variance:** $V(X_t) = \lambda \cdot t$

Note: To change the time interval, scale $\lambda$ proportionally ($\lambda_t = \lambda \cdot t$).

---

## 4. Geometric and Hypergeometric Distributions

### Geometric Distribution
Models the number of discrete time slots until the first success.
*   **Definition A (Counting total slots):** $P(T = k) = (1-p)^{k-1} p$, $E[T] = 1/p$, $V(T) = (1-p)/p^2$
*   **Definition B (Counting failures before success):** $P(Y = k) = (1-p)^k p$, $E[Y] = (1-p)/p$, $V(Y) = (1-p)/p^2$
*   **Memoryless Property:** $P(T > k + s \mid T > k) = P(T > s)$

### Hypergeometric Distribution
Models sampling **without replacement** from a finite population.
*   **PMF:** $P(X = k) = \frac{\binom{K}{k} \binom{N-K}{n-k}}{\binom{N}{n}}$
*   **Mean:** $E[X] = n \cdot \frac{K}{N}$
*   **Variance:** $V(X) = n \cdot \frac{K}{N} \cdot (1 - \frac{K}{N}) \cdot \frac{N - n}{N - 1}$

---

## 5. Moment Generating Functions

The Moment Generating Function $M_X(t)$ is:
$$M_X(t) = E\left[e^{tX}\right]$$
Moments can be found by differentiating:
$E[X^n] = M_X^{(n)}(0)$
*   $E[X] = M'_X(0)$
*   $V(X) = M''_X(0) - (M'_X(0))^2$

**Linear Transformation:** $M_{aX+b}(t) = e^{bt} \cdot M_X(at)$
**Sums of Independent RVs:** $M_{X+Y}(t) = M_X(t) \cdot M_Y(t)$

---

## 6. Time-Specific Gotchas

1. **Unit Scaling Multiplier on Variance:** If you convert seconds to ms ($a=1000$), $V(1000T) = 1,000,000 \cdot V(T)$. Don't forget to square $a$.
2. **Variance of Difference:** $V(T_1 - T_2) = V(T_1) + V(T_2)$. Variance is never subtracted.
3. **Binomial Time Slots vs Duration:** $n$ in Binomial is the number of time slots, not the total elapsed time.
4. **Poisson Rate Scaling:** If rate is 120/hr, and window is 1 min, you must scale $\lambda$ to 2/min before calculating.
5. **Memorylessness:** Geometric and Exponential are the only memoryless distributions.
6. **MGF Linear Scaling:** $M_{aT+b}(t) = e^{bt} M_T(at)$. Note that $a$ multiplies $t$ inside $M_T(\cdot)$, and $b$ becomes an exponential term $e^{bt}$.

---

## 7. Solved Exercises

#### Exercise 1: Computing Expected Processing Duration $E[T]$
**Problem:** Connection retry counts $T \in \{0, 1, 2, 3\}\text{ s}$ have PMF $p(t) = [0.1, 0.2, 0.3, 0.4]$. Find $E[T]$.
**Solution:**
$$E[T] = \sum t \cdot p(t) = (0 \cdot 0.1) + (1 \cdot 0.2) + (2 \cdot 0.3) + (3 \cdot 0.4) = 0 + 0.2 + 0.6 + 1.2 = 2.0\text{ s}$$

#### Exercise 2: Computing Duration Variance $V(T)$
**Problem:** Using PMF from Ex 1 ($E[T] = 2.0$), compute $V(T)$.
**Solution:**
$$E[T^2] = (0^2 \cdot 0.1) + (1^2 \cdot 0.2) + (2^2 \cdot 0.3) + (3^2 \cdot 0.4) = 0 + 0.2 + 1.2 + 3.6 = 5.0$$
$$V(T) = E[T^2] - (E[T])^2 = 5.0 - (2.0)^2 = 1.0\text{ s}^2$$

#### Exercise 3: Unit Scaling and Constant Overhead
**Problem:** $T$ in seconds has $E[T] = 2.5\text{ s}$ and $V(T) = 1.44\text{ s}^2$. Total response time in ms is $Y = 1000T + 40$. Find $E[Y]$ and $V[Y]$.
**Solution:**
$$E[Y] = 1000 \cdot E[T] + 40 = 2500 + 40 = 2540\text{ ms}$$
$$V[Y] = 1000^2 \cdot V(T) = 1,000,000 \cdot 1.44 = 1,440,000\text{ ms}^2$$

#### Exercise 4: Computing PMF for Exact Number of Time Slots
**Problem:** Inspect 5 slots. Prob of bottleneck per slot is $p = 0.20$. Prob of exactly 2 bottlenecks?
**Solution:**
$$P(X=2) = \binom{5}{2} (0.20)^2 (0.80)^3 = 10 \cdot 0.04 \cdot 0.512 = 0.2048$$

#### Exercise 5: "At Least One" Failed Time Slot
**Problem:** Server checks health for $n=6$ slots. Prob of outage is $p=0.05$. Find prob of at least 1 outage.
**Solution:**
$$P(X \ge 1) = 1 - P(X=0) = 1 - \binom{6}{0} (0.05)^0 (0.95)^6 = 1 - (0.95)^6 = 1 - 0.7351 = 0.2649$$

#### Exercise 6: Basic Arrival Count in 1 Hour Window (Poisson)
**Problem:** API calls arrive at $\lambda = 4$ per hour. Find prob of exactly 3 requests in a 1-hour window.
**Solution:**
$$P(X=3) = \frac{4^3 \cdot e^{-4}}{3!} = \frac{64 \cdot e^{-4}}{6} \approx \frac{1.1722}{6} \approx 0.1954$$

#### Exercise 7: Scaling Rate from Hours to Minutes
**Problem:** Queries arrive at $\lambda = 6$ per hour. Find prob of exactly 2 queries in a 30-minute window.
**Solution:**
$\lambda_{30\min} = 6 \times 0.5 = 3$.
$$P(X=2) = \frac{3^2 \cdot e^{-3}}{2!} = \frac{9 \cdot e^{-3}}{2} \approx 0.2240$$

#### Exercise 8: First Connection Success on 4th Time Slot (Geometric)
**Problem:** A modem connects in discrete 1-second slots with $p = 0.70$. Find prob that first success is on 4th slot.
**Solution:**
Using Definition A:
$$P(T = 4) = (1 - 0.70)^{4-1} (0.70) = (0.30)^3 \cdot 0.70 = 0.027 \cdot 0.70 = 0.0189$$

#### Exercise 9: Memoryless Property of Time Slots
**Problem:** Defect probability $p = 0.10$. Given first 5 slots were error-free, find prob that first defect is on 8th slot.
**Solution:**
$$P(T = 8 \mid T > 5) = P(T = 8 - 5) = P(T = 3) = (0.90)^2 \cdot 0.10 = 0.081$$

#### Exercise 10: Time Log Audit (Hypergeometric)
**Problem:** Batch of $N = 52$ logs, $K = 4$ contain alerts. Sample $n = 5$ without replacement. Prob of exactly 3 alerts?
**Solution:**
$$P(X = 3) = \frac{\binom{4}{3} \binom{48}{2}}{\binom{52}{5}} = \frac{4 \cdot 1128}{2598960} \approx 0.001736$$

#### Exercise 11: Finding Mean and Variance from a Duration MGF
**Problem:** Response time $T$ has $M_T(t) = (1 - 2t)^{-1}$. Find $E[T]$ and $V(T)$.
**Solution:**
$M'_T(t) = 2(1 - 2t)^{-2}$. Evaluate at $t=0$: $E[T] = 2$.
$M''_T(t) = 8(1 - 2t)^{-3}$. Evaluate at $t=0$: $E[T^2] = 8$.
$V(T) = 8 - 2^2 = 4$.

#### Exercise 12: MGF Linear Transformation of Latency
**Problem:** Execution time $T$ has $M_T(t) = e^{2t + 8t^2}$. Find MGF of $Y = 3T - 5$.
**Solution:**
$$M_Y(t) = e^{-5t} M_T(3t) = e^{-5t} e^{2(3t) + 8(3t)^2} = e^{-5t + 6t + 72t^2} = e^{t + 72t^2}$$

#### Exercise 13: Sum of Independent Binomial Time Slots
**Problem:** $X \sim B(n, p)$ and $Y \sim B(m, p)$ are independent. Find $M_{X+Y}(t)$.
**Solution:**
$$M_{X+Y}(t) = M_X(t) \cdot M_Y(t) = (q + p e^t)^n \cdot (q + p e^t)^m = (q + p e^t)^{n+m}$$

#### Exercise 14: R Code Snippet -- Empirical Discrete Duration Analysis
**Problem:** R code to compute PMF table, expected value, and variance.
**Solution:**
```r
durations <- c(1, 2, 2, 3, 1, 4, 2, 3, 3, 2)
val_counts <- table(durations)
pmf <- val_counts / length(durations)
t_vals <- as.numeric(names(pmf))

e_T <- sum(t_vals * pmf)
e_T2 <- sum((t_vals^2) * pmf)
var_T <- e_T2 - (e_T^2)
```

#### Exercise 15: R Code Snippet -- Time Slot Reliability (Binomial)
**Problem:** R code for cumulative and exact Binomial prob.
**Solution:**
```r
n_slots <- 20; p_fail <- 0.15
p_exact_3 <- dbinom(3, size = n_slots, prob = p_fail)
p_at_most_3 <- pbinom(3, size = n_slots, prob = p_fail)
```

#### Exercise 16: R Code Snippet -- Poisson Time Window Rate Analysis
**Problem:** Scale rate and compute Poisson prob in R.
**Solution:**
```r
lambda_hourly <- 12
lambda_15min <- lambda_hourly * (15 / 60)
p_2_in_15min <- dpois(2, lambda = lambda_15min)
p_atmost_20_in_2hr <- ppois(20, lambda = lambda_hourly * 2)
```

#### Exercise 17: R Code Snippet -- Geometric & Hypergeometric
**Problem:** Calculate probabilities for Geometric (Def A) and Hypergeometric.
**Solution:**
```r
p_success <- 0.20; k_trial <- 4
# R uses failures before success (Def B)
p_geom_defA <- dgeom(k_trial - 1, prob = p_success)

N_pop <- 52; K_succ <- 4; n_sample <- 5; k_target <- 3
p_hyper <- dhyper(k_target, m = K_succ, n = N_pop - K_succ, k = n_sample)
```

---

## Phase Summary
- Discrete Random Variables map outcomes to numerical values. Expected value is $\sum x p(x)$ and Variance is $E[X^2] - (E[X])^2$.
- The Binomial Distribution $B(n, p)$ models the number of successes in $n$ fixed, independent trials. Mean is $np$, variance is $np(1-p)$.
- The Poisson Distribution $Po(\lambda)$ models counts over an interval with constant rate $\lambda$. Mean and variance both equal $\lambda$.
- The Geometric Distribution models trials until first success. Hypergeometric models sampling without replacement.
- Moment Generating Functions $M_X(t) = E[e^{tX}]$ generate raw moments via derivatives at $t=0$. They uniquely identify distributions and are useful for linear transformations and sums of independent variables.
- Time context introduces gotchas like scaling unit multipliers on variance, ensuring time interval scaling in Poisson, and understanding memoryless properties of Geometric variables.

---

<!-- Source: Phases/Phase_5_Continuous_Random_Variables_Distributions.md -->

# Phase 5: Continuous Random Variables & Distributions

## Table of Contents
1. [Normal Distribution](#1-normal-distribution)
2. [The Empirical Rule](#2-the-empirical-rule)
3. [Continuous Uniform and Exponential Distributions](#3-continuous-uniform-and-exponential-distributions)
4. [Gamma, Weibull, and Erlang Distributions](#4-gamma-weibull-and-erlang-distributions)
5. [Transformations of Random Variables](#5-transformations-of-random-variables)
6. [Time-Specific Gotchas](#6-time-specific-gotchas)
7. [Solved Exercises](#7-solved-exercises)
8. [Phase Summary](#phase-summary)

---

## 1. Normal Distribution

The Normal (Gaussian) Distribution $N(\mu, \sigma^2)$ is characterized by a symmetric, bell-shaped probability density function (PDF).

### Probability Density Function (PDF)
$$f_T(t) = \frac{1}{\sigma_T \sqrt{2\pi}} \exp\left( -\frac{(t - \mu_T)^2}{2\sigma_T^2} \right), \quad -\infty < t < \infty$$

### Standard Normal Transformation
We standardise any normal random variable to $Z \sim N(0, 1)$ using the $Z$-score:
$$Z = \frac{T - \mu_T}{\sigma_T}$$
Then $P(T \le t) = \Phi(Z)$.

---

## 2. The Empirical Rule

For any symmetric, bell-shaped distribution (like the Normal distribution):
1. **68% Rule:** $\sim 68.27\%$ of values fall within $\mu_T \pm 1\sigma_T$.
2. **95% Rule:** $\sim 95.45\%$ of values fall within $\mu_T \pm 2\sigma_T$.
3. **99.7% Rule:** $\sim 99.73\%$ of values fall within $\mu_T \pm 3\sigma_T$.

---

## 3. Continuous Uniform and Exponential Distributions

### Continuous Uniform Distribution $U(a, b)$
Models equal probability over an interval.
*   **PDF:** $f_T(t) = \frac{1}{b - a}$ for $a \le t \le b$
*   **Mean:** $E[T] = \frac{a + b}{2}$, **Variance:** $V(T) = \frac{(b - a)^2}{12}$

### Exponential Distribution $Exp(\lambda)$
Models time between Poisson events. It is the **only memoryless** continuous distribution.
*   **PDF:** $f_T(t) = \lambda e^{-\lambda t}$ for $t \ge 0$
*   **Reliability / Survival:** $P(T > t) = e^{-\lambda t}$
*   **Mean:** $E[T] = 1/\lambda$, **Variance:** $V(T) = 1/\lambda^2$
*   **Memoryless Property:** $P(T > s + t \mid T > s) = P(T > t) = e^{-\lambda t}$

---

## 4. Gamma, Weibull, and Erlang Distributions

### Gamma Distribution $Gamma(\alpha, \beta)$
Models the time until $\alpha$ events occur in a Poisson process. If $\alpha = k$ (integer), it's the **Erlang** distribution.
*   **PDF:** $f_T(t) = \frac{\beta^\alpha}{\Gamma(\alpha)} t^{\alpha - 1} e^{-\beta t}$
*   **Mean:** $E[T] = \frac{\alpha}{\beta}$, **Variance:** $V(T) = \frac{\alpha}{\beta^2}$

### Weibull Distribution
Models time-to-failure with changing hazard rates.
*   **Reliability / Survival:** $S_T(t) = P(T > t) = e^{-(t/\lambda)^k}$
*   **$k < 1$**: Infant mortality. **$k = 1$**: Constant rate (Exponential). **$k > 1$**: Wear-out.

---

## 5. Transformations of Random Variables

For a continuous RV $T$ and transformation $Y = g(T)$:

### Linear Transformation ($Y = aT + b$)
*   $E[Y] = aE[T] + b$, $V(Y) = a^2 V(T)$
*   $f_Y(y) = \frac{1}{|a|} f_T\left(\frac{y-b}{a}\right)$

### Monotonic Non-Linear Transformation
Using the Jacobian derivative:
$$f_Y(y) = f_T\left( g^{-1}(y) \right) \cdot \left| \frac{d}{dy} g^{-1}(y) \right|$$

---

## 6. Time-Specific Gotchas

1. **Negative Time in Normal Models:** The Normal domain is $(-\infty, \infty)$. If $\mu_T < 3\sigma_T$, the model predicts negative time. Use Log-Normal or truncated normal in high-precision cases.
2. **Scaling Variance:** Converting seconds to ms multiplies values by 1000, but **variance** by $1{,}000{,}000$.
3. **Throughput Fallacy:** Average throughput $E[1/T]$ is strictly greater than $1/E[T]$ due to Jensen's Inequality.
4. **Memoryless Assumption:** Only the Exponential distribution is memoryless. Gamma and Weibull (with $k \ne 1$) are memoryful.
5. **Erlang Sum Property:** Adding Exponentials gives an Erlang ONLY if all stages have the EXACT same rate $\beta$.

---

## 7. Solved Exercises

#### Exercise 1: Finding the 99th Percentile SLA Benchmark ($p_{99}$)
**Problem:** Microservice processing time $T \sim N(50, 100)$ in ms ($\mu_T = 50$, $\sigma_T = 10$). Find $t_{99}$.
**Solution:**
From z-tables, $\Phi(2.326) = 0.99$.
$$t_{99} = \mu_T + z_{0.99} \cdot \sigma_T = 50 + (2.326)(10) = 50 + 23.26 = 73.26\text{ ms}$$

#### Exercise 2: Probability of Timeout Failure ($T > t_{\text{timeout}}$)
**Problem:** Network ping $T \sim N(45, 25)$ in ms. Times out if $T > 60\text{ ms}$. Find timeout prob.
**Solution:**
$z = (60 - 45) / 5 = 3.00$.
$$P(T > 60) = 1 - \Phi(3.00) = 1 - 0.99865 = 0.00135 \text{ (0.135\%)}$$

#### Exercise 3: Sum of Two Independent Normal Delay Stages
**Problem:** Stage 1 $T_1 \sim N(30, 9)$ ms and Stage 2 $T_2 \sim N(50, 16)$ ms. Find $P(T_1 + T_2 \le 90)$.
**Solution:**
$\mu_{tot} = 30 + 50 = 80$, $\sigma_{tot}^2 = 9 + 16 = 25 \implies \sigma_{tot} = 5$.
$z = (90 - 80) / 5 = 2.00$.
$P \le 90 = \Phi(2.00) = 0.9772 \text{ (97.72\%)}$.

#### Exercise 4: Number of Outlier Requests out of 10,000 (Empirical Rule)
**Problem:** Out of $10{,}000$ requests with $T \sim N(2, 0.09)$ (in s), how many fall outside $[1.1, 2.9]$?
**Solution:**
$1.1$ and $2.9$ are $\mu_T \pm 3\sigma_T$.
Outside area $= 100\% - 99.73\% = 0.27\% = 0.0027$.
$10{,}000 \times 0.0027 = 27 \text{ requests}$.

#### Exercise 5: Asymmetric Duration Window
**Problem:** Batch processing $T \sim N(12, 4)$ in hours. Estimate $P(10 \le T \le 16)$.
**Solution:**
$10$ is $\mu_T - 1\sigma_T$. $16$ is $\mu_T + 2\sigma_T$.
Left half (0 to -1) $= 34.135\%$. Right half (0 to 2) $= 47.725\%$.
Total $= 81.86\%$.

#### Exercise 6: Uniform Random Backoff Time
**Problem:** $T \sim U(10, 50)$ ms. Find $P(T > 35)$.
**Solution:**
$$P(T > 35) = \frac{50 - 35}{50 - 10} = \frac{15}{40} = 0.375 \text{ (37.5\%)}$$

#### Exercise 7: Exponential Component Survival
**Problem:** Hard drive $\lambda = 0.0001\text{ h}^{-1}$. Prob it survives beyond $5{,}000$ hours?
**Solution:**
$$P(T > 5000) = e^{-(0.0001)(5000)} = e^{-0.5} \approx 0.6065$$

#### Exercise 8: Minimum of Independent Exponential Durations
**Problem:** Components fail at $T_1 \sim Exp(0.02)$, $T_2 \sim Exp(0.03)$. System fails when FIRST component fails. Expected time to failure?
**Solution:**
$T_{min} \sim Exp(0.02 + 0.03) = Exp(0.05)$.
$E[T_{min}] = 1 / 0.05 = 20\text{ hours}$.

#### Exercise 9: Waiting Time for $k = 3$ API Requests (Erlang)
**Problem:** Poisson requests at $\beta = 2\text{ s}^{-1}$. Waiting time $T$ until 3rd request. Find mean and variance.
**Solution:**
$T \sim Gamma(\alpha=3, \beta=2)$.
$E[T] = 3/2 = 1.5\text{ s}$. $V(T) = 3/2^2 = 0.75\text{ s}^2$.

#### Exercise 10: Weibull Survival Probability with Wear-Out
**Problem:** Pump failure $T \sim Weibull(k=2, \lambda=1000\text{ h})$. Prob of survival beyond 1500 hours.
**Solution:**
$$P(T > 1500) = e^{-(1500/1000)^2} = e^{-2.25} \approx 0.1054$$

#### Exercise 11: Sum of Independent Exponential Stage Times
**Problem:** 4 stages, each $X_i \sim Exp(0.5\text{ ms}^{-1})$. Distribution of total $T$?
**Solution:**
Since they share the same rate, sum is Erlang/Gamma: $T \sim Gamma(4, 0.5)$.

#### Exercise 12: Reciprocal Transformation ($Y = 1/T$) for Throughput
**Problem:** Time $T \sim U(0.5, 2.0)$. Find PDF of throughput $Y = 1/T$.
**Solution:**
$y = 1/t \implies t = 1/y$. $|dt/dy| = 1/y^2$.
$f_T(t) = 1/(2.0 - 0.5) = 2/3$.
$$f_Y(y) = \frac{2}{3} \cdot \frac{1}{y^2} = \frac{2}{3y^2} \quad \text{for } 0.5 \le y \le 2.0$$

#### Exercise 13: Log-Normal Mean Calculation
**Problem:** $Y = \ln T \sim N(3, 0.25)$. Find $E[T]$.
**Solution:**
$E[T] = \exp(\mu + \sigma^2/2) = \exp(3 + 0.125) = e^{3.125} \approx 22.76$.

#### Exercise 14: Non-Monotonic Transformation Symmetry ($Y = T^2$)
**Problem:** Latency error $T \sim N(0, \sigma^2)$. PDF of $Y = T^2$?
**Solution:**
$F_Y(y) = P(-\sqrt{y} \le T \le \sqrt{y}) = F_T(\sqrt{y}) - F_T(-\sqrt{y})$.
$f_Y(y) = f_T(\sqrt{y}) \frac{1}{2\sqrt{y}} + f_T(-\sqrt{y}) \frac{1}{2\sqrt{y}} = \frac{1}{\sqrt{y}} f_T(\sqrt{y})$.
$$f_Y(y) = \frac{1}{\sigma \sqrt{2\pi y}} e^{-y / 2\sigma^2} \quad (y > 0)$$

#### Exercise 15: R Code Verification of Latency Quantiles
**Problem:** Compute $P(T \le 115)$ and $p_{95}$ for $T \sim N(100, 64)$.
**Solution:**
```r
mean_t <- 100; sd_t <- 8
p_115 <- pnorm(q = 115, mean = mean_t, sd = sd_t)
p95_limit <- qnorm(p = 0.95, mean = mean_t, sd = sd_t)
```

#### Exercise 16: R Code Verification for Exponential and Uniform
**Problem:** Calc prob for $U(10, 50)$ and $Exp(0.0001)$.
**Solution:**
```r
p_unif <- punif(q = 35, min = 10, max = 50, lower.tail = FALSE)
p_exp_fail <- pexp(q = 2000, rate = 0.0001)
p_exp_surv <- pexp(q = 5000, rate = 0.0001, lower.tail = FALSE)
```

---

## Phase Summary
Phase 5 introduces continuous probability distributions and the critical methodology of random variable transformations. The Normal distribution $N(\mu, \sigma^2)$ is foundational, accompanied by the Empirical Rule (68-95-99.7) for quick tail probability estimates. In the time domain, Uniform $U(a,b)$ models random jitter/backoff, while the Exponential distribution uniquely offers memoryless inter-arrival times. To model complex cumulative delays or changing hazard rates (aging), the Gamma, Erlang, and Weibull distributions are utilized. Transformations, evaluated via the Jacobian derivative $|g'(t)|^{-1}$, allow translation between latency and throughput ($1/T$) or derivation of skewed Log-Normal metrics ($e^Y$). Critical real-world gotchas include the expectation reciprocal fallacy ($E[1/T] > 1/E[T]$) and tracking rate vs. scale parameterizations in Gamma implementations.

---

<!-- Source: Phases/Phase_5B_Multivariate_Random_Variables.md -->

# Phase 5B: Multivariate Random Variables

## Table of Contents
1. [Multivariate Random Variables - Fundamentals](#1-multivariate-random-variables---fundamentals)
2. [Multivariate Moments, Covariance, and Conditional Expectation](#2-multivariate-moments-covariance-and-conditional-expectation)
3. [Functions of Multiple Random Variables & Order Statistics](#3-functions-of-multiple-random-variables--order-statistics)
4. [Time-Specific Gotchas](#4-time-specific-gotchas)
5. [Solved Exercises](#5-solved-exercises)
6. [Phase Summary](#phase-summary)

---

## 1. Multivariate Random Variables - Fundamentals

Multivariate variables model the joint behavior of multiple execution metrics (e.g., $T_1$ and $T_2$).

### Joint PDF and Normalization
$$\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f_{T_1, T_2}(t_1, t_2) \, dt_1 \, dt_2 = 1$$
Probability over a region $R$: $P((T_1, T_2) \in R) = \iint_R f(t_1, t_2) \, dt_1 \, dt_2$.

### Marginal and Conditional PDFs
**Marginal:** $f_{T_1}(t_1) = \int_{-\infty}^{\infty} f_{T_1, T_2}(t_1, t_2) \, dt_2$.
**Conditional:** $f_{T_2 \mid T_1}(t_2 \mid t_1) = \frac{f_{T_1, T_2}(t_1, t_2)}{f_{T_1}(t_1)}$.

### Independence
$T_1$ and $T_2$ are independent iff $f(t_1, t_2) = f_{T_1}(t_1) \cdot f_{T_2}(t_2)$ for all regions.

---

## 2. Multivariate Moments, Covariance, and Conditional Expectation

### Covariance and Correlation
**Covariance** measures linear dependence:
$$\text{Cov}(T_1, T_2) = E[T_1 T_2] - E[T_1] E[T_2]$$
**Correlation ($\rho$):**
$$\rho_{T_1, T_2} = \frac{\text{Cov}(T_1, T_2)}{\sigma_{T_1} \sigma_{T_2}}$$

### Variance of Sums
For constants $a, b$:
$$V(a T_1 + b T_2) = a^2 V(T_1) + b^2 V(T_2) + 2 a b \text{Cov}(T_1, T_2)$$
If $T_1, T_2$ are independent, $\text{Cov} = 0$, so $V(T_1 + T_2) = V(T_1) + V(T_2)$.

### Conditional Expectation
Law of Total Expectation: $E[T_1] = E_{T_2} \left[ E_{T_1 \mid T_2}(T_1 \mid T_2) \right]$.

---

## 3. Functions of Multiple Random Variables & Order Statistics

### Convolution (Sums)
For independent $T_1, T_2$, the PDF of $Y = T_1 + T_2$ is:
$$f_Y(y) = \int_{-\infty}^{\infty} f_{T_1}(t) \, f_{T_2}(y - t) \, dt$$

### Order Statistics (Min and Max)
For $n$ i.i.d. variables with CDF $F(t)$ and PDF $f(t)$:
*   **Max (Parallel Bottleneck):** $F_{\max}(t) = [F(t)]^n$, $f_{\max}(t) = n[F(t)]^{n-1}f(t)$
*   **Min (First to Finish):** $F_{\min}(t) = 1 - [1 - F(t)]^n$

---

## 4. Time-Specific Gotchas

1. **Dependent Support Regions:** If integration bounds for $T_1$ depend on $T_2$ (e.g., $0 \le t_1 \le t_2 \le 1$), the variables are **dependent**, even if the PDF is constant.
2. **Uncorrelated $\neq$ Independent:** For non-Gaussian variables, zero covariance does not guarantee independence.
3. **Variance of Total Processing:** Always include $2\text{Cov}(T_1, T_2)$ when computing $V(T_1 + T_2)$ if components share resources.
4. **Underestimating Parallel Latency:** Average parallel execution time $E[\max(T_1, \dots, T_n)]$ is strictly greater than the single-task average $E[T]$.
5. **Sum of Exponentials with Different Rates:** It is a Hypoexponential distribution, not a Gamma distribution.

---

## 5. Solved Exercises

#### Exercise 1: Finding Normalizing Constant $k$ for Joint Processing Times
**Problem:** $f(t_1, t_2) = k \cdot t_1 t_2$ for $0 \le t_1 \le 2$ and $0 \le t_2 \le 3$. Find $k$.
**Solution:**
$$\int_{0}^{2} \int_{0}^{3} k t_1 t_2 \, dt_2 \, dt_1 = k \left[ \frac{t_1^2}{2} \right]_0^2 \left[ \frac{t_2^2}{2} \right]_0^3 = k (2) (4.5) = 9k = 1 \implies k = 1/9$$

#### Exercise 2: Computing Marginal PDFs
**Problem:** Find $f_{T_1}(t_1)$ for $f(t_1, t_2) = \frac{1}{9} t_1 t_2$ on $[0, 2] \times [0, 3]$.
**Solution:**
$$f_{T_1}(t_1) = \int_{0}^{3} \frac{1}{9} t_1 t_2 \, dt_2 = \frac{t_1}{9} \left[ \frac{t_2^2}{2} \right]_0^3 = \frac{4.5 t_1}{9} = \frac{t_1}{2}, \quad 0 \le t_1 \le 2$$

#### Exercise 3: Testing Independence of Time Variables
**Problem:** Are $T_1$ and $T_2$ from Exercise 2 independent?
**Solution:**
$f_{T_2}(t_2) = \frac{2t_2}{9}$. Product $= (\frac{t_1}{2})(\frac{2t_2}{9}) = \frac{t_1 t_2}{9} = f(t_1, t_2)$. Yes, independent.

#### Exercise 4: Conditional PDF $f_{T_1 \mid T_2}(t_1 \mid t_2)$
**Problem:** $f(t_1, t_2) = 8 t_1 t_2$ on $0 \le t_1 \le t_2 \le 1$. Find $f_{T_1 \mid T_2}(t_1 \mid 0.5)$.
**Solution:**
$f_{T_2}(t_2) = \int_0^{t_2} 8 t_1 t_2 dt_1 = 4 t_2^3$.
$$f_{T_1 \mid T_2}(t_1 \mid t_2) = \frac{8 t_1 t_2}{4 t_2^3} = \frac{2 t_1}{t_2^2}$$
For $t_2 = 0.5$, $f(t_1 \mid 0.5) = \frac{2 t_1}{0.25} = 8 t_1$ for $0 \le t_1 \le 0.5$.

#### Exercise 5: Joint Product Moment $E[T_1 T_2]$
**Problem:** $f(t_1, t_2) = \frac{1}{9} t_1 t_2$ on $[0, 2] \times [0, 3]$. Calculate $E[T_1 T_2]$.
**Solution:**
$$E[T_1 T_2] = \int_0^2 \int_0^3 t_1 t_2 \left( \frac{1}{9} t_1 t_2 \right) dt_2 dt_1 = \frac{1}{9} \left[\frac{t_1^3}{3}\right]_0^2 \left[\frac{t_2^3}{3}\right]_0^3 = \frac{1}{9} \times \frac{8}{3} \times 9 = \frac{8}{3}$$

#### Exercise 6: Pearson Correlation Coefficient $\rho$
**Problem:** $V(T_1) = 11/225$, $V(T_2) = 2/75$, $\text{Cov} = 11/300$. Find $\rho$.
**Solution:**
$$\sigma_1 \sigma_2 = \sqrt{\frac{11}{225} \cdot \frac{2}{75}} \approx 0.036055$$
$$\rho = \frac{11/300}{0.036055} \approx \frac{0.036667}{0.036055} \approx 0.9574$$

#### Exercise 7: Variance of Sum with Positive Correlation
**Problem:** $V(T_1) = 25$, $V(T_2) = 36$, $\text{Cov}(T_1, T_2) = 10$. Find $V(T_1 + T_2)$.
**Solution:**
$$V(T_1 + T_2) = 25 + 36 + 2(10) = 81$$

#### Exercise 8: Conditional Expectation for Bivariate Normal Latency
**Problem:** $T_1 \sim N(100, 100), T_2 \sim N(150, 400), \rho = 0.8$. Find $E[T_1 \mid T_2 = 170]$.
**Solution:**
$$E[T_1 \mid T_2 = 170] = 100 + 0.8 \left(\frac{10}{20}\right) (170 - 150) = 100 + 8 = 108$$

#### Exercise 9: Convolution of Two Independent Uniform Stage Times
**Problem:** $T_1, T_2 \sim U(0, 1)$. Find PDF of $Y = T_1 + T_2$.
**Solution:**
$f_Y(y) = \int_0^1 f_{T_1}(t) f_{T_2}(y - t) dt$.
$f_Y(y) = y$ for $0 \le y \le 1$, and $f_Y(y) = 2 - y$ for $1 < y \le 2$.

#### Exercise 10: Parallel Task Bottleneck (Maximum of 3 Uniform RVs)
**Problem:** 3 tasks $T_i \sim U(0, 10)$. Find PDF of $Y_{\max}$.
**Solution:**
$F(t) = t/10$. $F_{(3)}(t) = (t/10)^3 = t^3/1000$.
$f_{(3)}(t) = 3t^2/1000$ for $0 \le t \le 10$.

#### Exercise 11: Expected Parallel Completion Time
**Problem:** Find $E[Y_{\max}]$ from Exercise 10.
**Solution:**
$$E[Y_{\max}] = \int_0^{10} t \left(\frac{3t^2}{1000}\right) dt = \frac{3}{1000} \left[ \frac{t^4}{4} \right]_0^{10} = \frac{30}{4} = 7.5\text{ s}$$

#### Exercise 12: Difference Between Two Normal Execution Times
**Problem:** $T_1 \sim N(100, 25)$ and $T_2 \sim N(90, 16)$, independent. $P(T_1 < T_2)$?
**Solution:**
$D = T_1 - T_2 \sim N(10, 41)$. $z = (0 - 10) / \sqrt{41} = -1.56$.
$P(D < 0) = \Phi(-1.56) = 0.0594 \text{ (5.94\%)}$.

#### Exercise 13: R Code Verification of Order Statistics for Parallel Tasks
**Problem:** Calculate empirical mean of max of 3 uniform $U(0, 10)$ variables.
**Solution:**
```r
t1 <- runif(1000000, 0, 10)
t2 <- runif(1000000, 0, 10)
t3 <- runif(1000000, 0, 10)
t_max <- pmax(t1, t2, t3)
cat("Empirical E:", mean(t_max), "\n") # approx 7.5
```

---

## Phase Summary
Phase 5B extends the statistical toolkit to Multivariate Random Variables, focusing heavily on the interdependencies between operational metrics like sequential phase delays or parallel completion times. Key tools include the Joint PDF for regional probability, and Marginal/Conditional densities to isolate variable behavior. The Covariance and Pearson Correlation ($\rho$) definitively quantify linear co-movement, directly affecting the Variance of Sums (total system jitter increases if stages are positively correlated). Order statistics explicitly model the critical paths: the Maximum ($Y_{\max}$) maps to parallel execution bottlenecks, demonstrating that average system completion time scales strictly worse than single-task averages. Finally, convolution seamlessly provides the probability density of sequential processing times.

---

<!-- Source: Phases/Phase_6_Inferential_Statistics.md -->

# Phase 6: Inferential Statistics

## Table of Contents
1. [Probability Inequalities and Laws of Large Numbers](#1-probability-inequalities-and-laws-of-large-numbers)
2. [Sampling Distributions](#2-sampling-distributions)
3. [Central Limit Theorem (CLT)](#3-central-limit-theorem-clt)
4. [Confidence Intervals](#4-confidence-intervals)
5. [Hypothesis Testing](#5-hypothesis-testing)
6. [Time-Specific Gotchas](#6-time-specific-gotchas)
7. [Solved Exercises](#7-solved-exercises)
8. [Phase Summary](#phase-summary)

---

## 1. Probability Inequalities and Laws of Large Numbers

When detailed probability density functions $f_T(t)$ are unknown, mathematical inequalities provide guaranteed non-parametric upper bounds on latency tail probabilities.

### Markov's Inequality
For a non-negative continuous time random variable $T \ge 0$, and constant $a > 0$:
$$P(T \ge a) \le \frac{E[T]}{a}$$

### Chebyshev's Inequality
For any random variable $T$ with finite mean $\mu_T$ and finite variance $\sigma_T^2$, the probability of deviating from the mean by $k$ standard deviations ($k > 0$) is bounded:
$$P(|T - \mu_T| \ge k \sigma_T) \le \frac{1}{k^2}$$

### Laws of Large Numbers (LLN)
Let $T_1, T_2, \dots, T_n$ be i.i.d. execution time measurements with mean $\mu_T$. The sample mean duration $\bar{T}_n = \frac{1}{n} \sum_{i=1}^n T_i$ converges in probability (Weak Law) and almost surely (Strong Law) to true population mean $\mu_T$ as $n \to \infty$.

---

## 2. Sampling Distributions

Sample statistics are random variables with their own probability distributions.

### Distribution of the Sample Variance ($S^2$)
For a random sample from a Normal population $N(\mu, \sigma^2)$, the scaled sample variance follows a Chi-square ($\chi^2$) distribution with $\nu = n-1$ degrees of freedom:
$$\frac{(n-1)S^2}{\sigma^2} \sim \chi^2_{n-1}$$

### Student's t-Distribution
Arises when estimating the mean of a normally distributed population when $n < 30$ and $\sigma$ is unknown, replacing $\sigma$ with sample standard deviation $s$.

### Fisher-Snedecor F-Distribution
Models the ratio of scaled variances from two independent normal populations. Under $H_0: \sigma_1^2 = \sigma_2^2$, the test statistic $F = s_1^2 / s_2^2$ follows $F_{n_1-1, n_2-1}$.

---

## 3. Central Limit Theorem (CLT)

The CLT states that the sample mean $\bar{T}$ of $n$ independent and identically distributed random time metrics approaches a Normal distribution as sample size $n$ grows large ($n \ge 30$), regardless of the underlying latency distribution.

$$\bar{T} \xrightarrow{d} N\left(\mu_T, \frac{\sigma_T^2}{n}\right)$$

### Standardized Z-Score for Sample Means
$$Z = \frac{\bar{T} - \mu_T}{\sigma_T / \sqrt{n}} \sim N(0, 1)$$

---

## 4. Confidence Intervals

A Confidence Interval (CI) provides a range of plausible values for an unknown population parameter with a specified confidence level $1 - \alpha$.

### Confidence Interval for Population Mean ($\mu_T$)
* **Known $\sigma_T$ (or $n \ge 30$):** $CI = \bar{T} \pm z_{\alpha/2} \frac{\sigma_T}{\sqrt{n}}$
* **Unknown $\sigma_T$ ($n < 30$):** $CI = \bar{T} \pm t_{\alpha/2, n-1} \frac{s_T}{\sqrt{n}}$

### Confidence Interval for Population Variance ($\sigma_T^2$)
$$CI = \left[ \frac{(n - 1) s_T^2}{\chi_{\alpha/2, n-1}^2}, \, \frac{(n - 1) s_T^2}{\chi_{1 - \alpha/2, n-1}^2} \right]$$

---

## 5. Hypothesis Testing

Hypothesis testing evaluates empirical evidence against a default status quo assertion ($H_0$).

*   **Null Hypothesis ($H_0$):** Status quo assertion (e.g., $\mu \le \mu_0$).
*   **Alternative Hypothesis ($H_1$):** Research hypothesis (e.g., $\mu > \mu_0$).
*   **Type I Error ($\alpha$):** Rejecting $H_0$ when it is true (False Alarm).
*   **Type II Error ($\beta$):** Failing to reject $H_0$ when $H_1$ is true (Missed Detection).
*   **Power of the Test ($1 - \beta$):** Probability of correctly rejecting a false $H_0$.

### Decision Rules
* **Critical Value Approach:** Reject $H_0$ if the test statistic falls into the rejection region (determined by $z_{\alpha}$, $t_{\alpha}$, etc.).
* **p-Value Approach:** Reject $H_0$ if $p\text{-value} \le \alpha$.

---

## 6. Time-Specific Gotchas

1. **Confusing Population SD ($\sigma_T$) with Standard Error ($\sigma_{\bar{T}}$):** The variability of the *average* time is $\sigma_{\bar{T}} = \sigma_T / \sqrt{n}$, not $\sigma_T$.
2. **Applying CLT to Small Samples ($n < 30$) from Skewed Distributions:** For skewed metrics like latency, $\bar{T}$ remains skewed for small $n$. Wait for $n \ge 30$.
3. **Misinterpreting the $95\%$ Confidence Level:** It does not mean a $95\%$ chance that true mean $\mu_T$ lies in the calculated interval. It means the *method* works $95\%$ of the time.
4. **Confounding Practical vs Statistical Significance:** A $0.001\text{ ms}$ latency drop can be statistically significant with large $n$, but practically meaningless.
5. **Sensitivity of $\chi^2$ and $F$ Tests:** Unlike $t$-tests, variance tests are extremely sensitive to non-normality. Do not blindly use them on right-skewed latency data.

---

## 7. Solved Exercises

#### Exercise 1: Standard Error of Mean Latency
**Problem:** DB query duration has population mean $\mu_T = 150\text{ ms}$ and standard deviation $\sigma_T = 40\text{ ms}$. Calculate standard error of the mean for $n = 16$.
**Solution:**
$$\sigma_{\bar{T}} = \frac{40}{\sqrt{16}} = \frac{40}{4} = 10\text{ ms}$$

#### Exercise 2: Sample Size Determination for Targeted Latency Margin
**Problem:** Individual network delay has $\sigma_T = 30\text{ ms}$. How many sample pings $n$ are needed so that the sample mean $\bar{T}$ lies within $\pm 3\text{ ms}$ of true mean $\mu_T$ with $95\%$ probability?
**Solution:**
$$n = \left( \frac{z_{0.025} \cdot \sigma_T}{E} \right)^2 = \left( \frac{1.96 \cdot 30}{3} \right)^2 = (19.6)^2 = 384.16$$
Round up to $n = 385$ pings.

#### Exercise 3: Comparing Individual vs Sample Mean Tail Probabilities
**Problem:** Latency $T \sim N(100, 400)$ ($\mu_T = 100, \sigma_T = 20$). Compare $P(T > 110)$ for a single request vs $P(\bar{T} > 110)$ for $n = 25$ requests.
**Solution:**
Single request: $z = \frac{110 - 100}{20} = 0.50 \implies P(T > 110) = 1 - \Phi(0.50) = 0.3085 \text{ (30.85\%)}$.
Sample mean ($n=25$): $\sigma_{\bar{T}} = \frac{20}{5} = 4$. $z = \frac{110 - 100}{4} = 2.50 \implies P(\bar{T} > 110) = 1 - \Phi(2.50) = 0.0062 \text{ (0.62\%)}$.

#### Exercise 4: 95% t-Confidence Interval (Small Sample $n = 16$)
**Problem:** Benchmark of $n = 16$ microservice executions yields $\bar{T} = 5.4\text{ s}$ and $s_T = 0.8\text{ s}$. Construct a $95\%$ CI for $\mu_T$.
**Solution:**
$t_{0.025, 15} = 2.131$. $\text{SE} = \frac{0.8}{\sqrt{16}} = 0.2\text{ s}$.
Margin of Error $E = 2.131 \times 0.2 = 0.4262\text{ s}$.
$\text{CI} = [5.4 - 0.4262, 5.4 + 0.4262] = [4.9738\text{ s}, 5.8262\text{ s}]$.

#### Exercise 5: Difference in Mean Execution Times Confidence Interval
**Problem:** System A ($n_1 = 40, \bar{T}_1 = 120\text{ ms}, s_1 = 16\text{ ms}$) and System B ($n_2 = 50, \bar{T}_2 = 135\text{ ms}, s_2 = 20\text{ ms}$). Construct a $95\%$ CI for $\mu_2 - \mu_1$.
**Solution:**
Estimate $= 135 - 120 = 15\text{ ms}$.
$\text{SE}_{\text{diff}} = \sqrt{\frac{16^2}{40} + \frac{20^2}{50}} = \sqrt{6.4 + 8.0} = \sqrt{14.4} \approx 3.7947\text{ ms}$.
$E = 1.96 \times 3.7947 = 7.4376\text{ ms}$.
$\text{CI} = [15 - 7.4376, 15 + 7.4376] = [7.5624\text{ ms}, 22.4376\text{ ms}]$.

#### Exercise 6: One-Sample Z-Test for Latency SLA Benchmark
**Problem:** SLA mandates mean response time $\mu_T \le 100\text{ ms}$. A sample of $n = 64$ requests has $\bar{T} = 105\text{ ms}$ with known $\sigma_T = 16\text{ ms}$. Test at $\alpha = 0.05$ whether SLA is violated ($H_1: \mu_T > 100$).
**Solution:**
$\text{SE} = \frac{16}{\sqrt{64}} = 2\text{ ms}$. $Z = \frac{105 - 100}{2} = 2.50$.
Critical value $z_{0.05} = 1.645$. Since $Z = 2.50 > 1.645$, reject $H_0$. Strong evidence SLA is violated.

#### Exercise 7: Two-Sample Welch's t-Test Comparing Cloud Regions
**Problem:** Region A ($n_1 = 36, \bar{T}_1 = 82, s_1 = 12$) and Region B ($n_2 = 36, \bar{T}_2 = 90, s_2 = 15$). Test at $\alpha = 0.05$ whether mean latencies differ ($H_1: \mu_1 \neq \mu_2$).
**Solution:**
$\text{SE}_{\text{diff}} = \sqrt{\frac{144}{36} + \frac{225}{36}} = \sqrt{10.25} \approx 3.2016$.
$t = \frac{82 - 90}{3.2016} \approx -2.50$.
Critical value $z_{0.025} = 1.96$ ($df \approx 66$). Since $|t| = 2.50 > 1.96$, reject $H_0$.

#### Exercise 8: Statistical Power ($1 - \beta$) Calculation for Latency
**Problem:** Testing $H_0: \mu_T = 100\text{ ms}$ vs $H_1: \mu_T = 90\text{ ms}$ with $\sigma_T = 20\text{ ms}, n = 25, \alpha = 0.05$ (left-tailed). Calculate test power.
**Solution:**
$\text{SE} = 4\text{ ms}$. Rejection cutoff $\bar{T}_{\text{crit}} = 100 - 1.645(4) = 93.42\text{ ms}$.
Under $H_1: \mu_T = 90$, $z = \frac{93.42 - 90}{4} = 0.855 \approx 0.86$.
Power $= \Phi(0.86) = 0.8051$ (approx $80.51\%$).

#### Exercise 9: 95% Confidence Interval for Population Variance $\sigma_T^2$
**Problem:** $n = 25$ measurements yield $s_T^2 = 16\text{ ms}^2$. Construct $95\%$ CI for $\sigma_T^2$.
**Solution:**
$df = 24$. $\chi_{0.025, 24}^2 = 39.36, \chi_{0.975, 24}^2 = 12.40$.
Lower $= \frac{24 \times 16}{39.36} \approx 9.756$. Upper $= \frac{24 \times 16}{12.40} \approx 30.968$.
$\text{CI} = [9.76\text{ ms}^2, 30.97\text{ ms}^2]$.

#### Exercise 10: Markov's Inequality Upper Bound on Severe Latency
**Problem:** API mean latency is $E[T] = 50\text{ ms}$. Find an upper bound on $P(T \ge 200\text{ ms})$.
**Solution:**
By Markov: $P(T \ge 200) \le \frac{50}{200} = 0.25 \text{ (25\%)}$.

#### Exercise 11: Chebyshev Bound for 3-Sigma Latency Outliers
**Problem:** Latency $T$ has $\mu_T = 120\text{ ms}$ and $\sigma_T = 15\text{ ms}$. Find upper bound on $P(|T - 120| \ge 45)$.
**Solution:**
$45 = 3\sigma_T$. By Chebyshev: $P(|T - 120| \ge 3\sigma_T) \le \frac{1}{3^2} = \frac{1}{9} \approx 0.1111 \text{ (11.11\%)}$.

#### Exercise 12: R Code Verification of WLLN Convergence
**Problem:** Write R code demonstrating the convergence of sample mean execution time to true mean $\mu_T = 10$ as sample size grows to $10{,}000$.
**Solution:**
```r
set.seed(42)
latencies <- rexp(10000, rate = 0.1) # mu = 10
cum_means <- cumsum(latencies) / (1:10000)
cat("Sample mean at n = 10000:", round(cum_means[10000], 3), "\n") # approaches 10.000
```

---

## Phase Summary
Phase 6 pivots from pure probability to Inferential Statistics, forming the bridge between raw latency samples and definitive architectural conclusions. The theoretical engine driving this is the Central Limit Theorem (CLT), which proves that average latencies ($\bar{T}$) distribute normally even when individual execution times are wildly skewed. Laws of Large Numbers and Chebyshev’s Inequality guarantee that sample statistics aggressively converge to true parameters as $N$ scales. Practically, Confidence Intervals replace fragile single-point estimates with robust, statistically sound latency ranges. Hypothesis Testing formalizes A/B testing (e.g., did the new index *actually* reduce query times?), carefully balancing Type I Errors (false optimization claims) against Type II Errors (missed speedups) and incorporating the $t$, $\chi^2$, and $F$-distributions to accurately assess means and variances from limited operational data.

---

<!-- Source: Phases/Phase_7_R_Programming_Commands.md -->

# Phase 7: R Programming Commands

## Table of Contents
1. [Descriptive Statistics](#1-descriptive-statistics)
2. [Binomial Distribution](#2-binomial-distribution)
3. [Normal Distribution](#3-normal-distribution)
4. [Additional Distributions](#4-additional-distributions)
5. [Time-Specific Gotchas](#5-time-specific-gotchas)
6. [Solved Exercises](#6-solved-exercises)
7. [Phase Summary](#phase-summary)

---

## 1. Descriptive Statistics

R provides a streamlined suite of functions to calculate descriptive statistics from data vectors.

### Core Summary Functions
*   **Mean:** `mean(x, na.rm = TRUE)` — Calculates the arithmetic average ($\bar{X}$). Use `trim = 0.05` to compute trimmed means (removes extreme 5% of data).
*   **Median:** `median(x, na.rm = TRUE)` — Finds the middle value.
*   **Variance:** `var(x, na.rm = TRUE)` — Calculates the **sample** variance ($s^2$).
*   **Standard Deviation:** `sd(x, na.rm = TRUE)` — Calculates the **sample** standard deviation ($s$).
*   **Quantiles / Percentiles:** `quantile(x, probs = c(0.25, 0.5, 0.75))` — Returns specified percentiles (e.g., SLA boundaries).
*   **Interquartile Range:** `IQR(x, na.rm = TRUE)` — Calculates $Q_3 - Q_1$.
*   **Summary:** `summary(x)` — Returns Min, $1^{\text{st}}$ Qu., Median, Mean, $3^{\text{rd}}$ Qu., Max.

### Mode in R
R does not have a built-in function for the mode. Instead, use:
```R
freq_table <- table(x)
names(freq_table)[freq_table == max(freq_table)]
```

---

## 2. Binomial Distribution

R handles probability distributions systematically using prefix notation (`d`, `p`, `q`, `r`). For the Binomial distribution, the root is `binom`.

*   **Exact Probability ($P(X = k)$):** `dbinom(x = k, size = n, prob = p)`
*   **Cumulative Probability ($P(X \le q)$):** `pbinom(q = k, size = n, prob = p)`
    * Use `lower.tail = FALSE` to compute $P(X > q)$.
*   **Quantile (Inverse CDF):** `qbinom(p = prob, size = n, prob = p)` — Finds the smallest $k$ such that $P(X \le k) \ge p$.
*   **Random Generation:** `rbinom(n = samples, size = n, prob = p)`

---

## 3. Normal Distribution

The Normal distribution relies on mean ($\mu$) and standard deviation ($\sigma$). The root is `norm`.

*   **Cumulative Probability ($P(X \le q)$):** `pnorm(q = x, mean = \mu, sd = \sigma)`
    * Default parameters are $\mu = 0$ and $\sigma = 1$ (Standard Normal).
*   **Quantile (Inverse CDF):** `qnorm(p = prob, mean = \mu, sd = \sigma)` — Finds $x$ for a given cumulative probability.
*   **Random Generation:** `rnorm(n = samples, mean = \mu, sd = \sigma)`
*   **Density Function:** `dnorm(x, mean = \mu, sd = \sigma)` — Returns the height of the PDF (used primarily for plotting).

---

## 4. Additional Distributions

### 4.1 Discrete Distributions
*   **Geometric (`geom`):** `dgeom(x, prob)` / `pgeom(q, prob)`. *Note: `x` and `q` represent the number of FAILURES before the first success, not the total number of trials.*
*   **Hypergeometric (`hyper`):** `dhyper(x, m, n, k)` / `phyper(q, m, n, k)`.
    * `m`: Number of success items in population ($K$).
    * `n`: Number of failure items in population ($N-K$).
    * `k`: Sample size ($n$).

### 4.2 Continuous Distributions
*   **Exponential (`exp`):** `dexp(x, rate = \lambda)` / `pexp(q, rate = \lambda)`. $\text{Mean} = 1/\lambda$.
*   **Gamma (`gamma`):** `dgamma(x, shape = \alpha, rate = \beta)` / `pgamma(q, shape = \alpha, rate = \beta)`.
*   **Weibull (`weibull`):** `pweibull(q, shape = k, scale = \lambda)`.
*   **Uniform (`unif`):** `punif(q, min = a, max = b)`.

### 4.3 Sampling Distributions (For Hypothesis Testing)
*   **Chi-Square (`chisq`):** `pchisq(q, df)` / `qchisq(p, df)`.
*   **Student's t (`t`):** `pt(q, df)` / `qt(p, df)`.
*   **Fisher's F (`f`):** `pf(q, df1, df2)` / `qf(p, df1, df2)`.

---

## 5. Time-Specific Gotchas

1. **`sd` Parameter vs Variance:** `pnorm()` and `rnorm()` expect the standard deviation `sd`, not the variance. If given $\sigma_T^2 = 100$, pass `sd = 10` (or `sqrt(100)`).
2. **`lower.tail = FALSE` Strict Inequality:** In R, `pbinom(q, ..., lower.tail = FALSE)` evaluates $P(X > q)$. To calculate $P(X \ge k)$, you must pass `q = k - 1`. For continuous distributions, $P(T > q) = P(T \ge q)$, so this adjustment is unnecessary.
3. **Sample vs Population Variance:** `var()` computes the sample variance (dividing by $n-1$). To get population variance, compute manually or multiply `var(x)` by $(n-1)/n$.
4. **Geometric Distribution Definition:** R strictly models the number of failures *before* success. Finding the first success on the 5th trial means $x = 4$ failures.
5. **Gamma Rate vs Scale:** Passing `rate = beta` means $E[T] = \text{shape} / \text{rate}$. If you specify `scale = theta`, then $E[T] = \text{shape} \times \text{scale}$. Always name the parameter explicitly.

---

## 6. Solved Exercises

#### Exercise 1: Basic Descriptive Statistics on Response Times
**Problem:** Vector `latencies <- c(120, 145, 110, 160, 130, 210, 125, 135, 140, 150)`. Compute mean, median, SD, and Variance.
**Solution:**
```R
latencies <- c(120, 145, 110, 160, 130, 210, 125, 135, 140, 150)
mean_lat <- mean(latencies)     # 142.5
med_lat  <- median(latencies)   # 137.5
sd_lat   <- sd(latencies)       # 27.65863
var_lat  <- var(latencies)      # 765
```

#### Exercise 2: Trimming Outliers from Latency Means
**Problem:** Compare mean vs $5\%$ trimmed mean for `raw_lat <- c(100, 102, 98, 105, 101, 99, 103, 1500)`.
**Solution:**
```R
raw_lat <- c(100, 102, 98, 105, 101, 99, 103, 1500)
mean(raw_lat)               # 276
mean(raw_lat, trim = 0.05)  # 276 (since 5% of 8 is 0.4, no elements are removed unless trim is higher)
mean(raw_lat, trim = 0.15)  # 101.3333 (removes 1 highest and 1 lowest)
```

#### Exercise 3: Binomial Exact and Cumulative Probability
**Problem:** $n = 20$ requests, $p = 0.05$ timeout probability. Calculate $P(X = 2)$ and $P(X \le 1)$.
**Solution:**
```R
dbinom(x = 2, size = 20, prob = 0.05) # 0.1886768
pbinom(q = 1, size = 20, prob = 0.05) # 0.7358395
```

#### Exercise 4: Binomial "At Least $k$" Using Complement
**Problem:** Find $P(X \ge 3)$ timeouts out of $n = 100$ requests with $p = 0.01$.
**Solution:**
```R
# P(X >= 3) = P(X > 2), so we pass q = 2
pbinom(q = 2, size = 100, prob = 0.01, lower.tail = FALSE) # 0.0793732
```

#### Exercise 5: Normal Cumulative Probability
**Problem:** DB query $T \sim N(120\text{ ms}, 15^2)$. Calculate $P(T \le 100\text{ ms})$.
**Solution:**
```R
pnorm(q = 100, mean = 120, sd = 15) # 0.09121122
```

#### Exercise 6: Normal SLA 99th Percentile Limit
**Problem:** Find $t_{99}$ for $T \sim N(50\text{ ms}, 10^2\text{ ms}^2)$.
**Solution:**
```R
qnorm(p = 0.99, mean = 50, sd = 10) # 73.26348 ms
```

#### Exercise 7: Geometric Distribution Failures
**Problem:** Probability of finding the first defective part on the 5th test ($p = 0.08$).
**Solution:**
```R
# 5th test means 4 failures before the first success.
dgeom(x = 4, prob = 0.08) # 0.05731454
```

#### Exercise 8: Exponential Component Survival
**Problem:** $T \sim \text{Exp}(\text{rate} = 0.002\text{ h}^{-1})$. Calculate $P(T > 1000\text{ hours})$.
**Solution:**
```R
pexp(q = 1000, rate = 0.002, lower.tail = FALSE) # 0.1353353
```

#### Exercise 9: Gamma Waiting Time Distribution
**Problem:** $T \sim \text{Gamma}(\text{shape}=4, \text{rate}=0.5)$. Calculate $P(T \le 10)$.
**Solution:**
```R
pgamma(q = 10, shape = 4, rate = 0.5) # 0.7349741
```

#### Exercise 10: F-test p-value
**Problem:** Calculate p-value for sample variance ratio $F = 2.80$ with $df_1 = 15, df_2 = 20$.
**Solution:**
```R
pf(q = 2.80, df1 = 15, df2 = 20, lower.tail = FALSE) # 0.01538356
```

---

## Phase Summary
Phase 7 concludes the syllabus by translating theoretical probability concepts into computational R functions. It maps the mathematical concepts learned in earlier phases (PMF, CDF, quantiles) to their functional equivalents (`d`, `p`, `q`, `r` prefixes) for key distributions (Binomial, Normal, Exponential, Geometric, etc.). Furthermore, it addresses critical language-specific quirks, such as `sd` taking standard deviation rather than variance, the geometric distribution counting *failures*, and `lower.tail = FALSE` enforcing strict inequalities. Mastering these commands equips you to efficiently compute complex percentiles, model time-window events, and perform statistical inference directly from raw log data.

---

