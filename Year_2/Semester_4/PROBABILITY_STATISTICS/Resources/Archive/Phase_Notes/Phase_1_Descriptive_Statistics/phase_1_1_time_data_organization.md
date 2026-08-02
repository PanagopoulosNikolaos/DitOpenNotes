# Phase 1.1 (Time): Data Organization for Time-Based Data

Data organization is the first step in descriptive statistics. It involves transforming raw data into a structured format, primarily through **Frequency Tables**. When the data consist of **time-based observations** -- timestamps, durations, latencies, intervals, or cyclic clock times -- the same organizational principles apply, but special attention must be paid to **units, prefixes, and the cyclic nature of clock time**.

---

## 1. Core Concepts and Notation (Time Context)

Before building a table, we must understand the four types of frequencies. The notation is identical to the general case, but the values $x_i$ now represent **time measurements** (e.g., seconds, milliseconds, nanoseconds).

*   **Absolute Frequency ($f_i$):** The number of times a specific time value or time interval occurs. The sum of all absolute frequencies equals the total number of observations ($n$):
    $$\sum_{i=1}^{k} f_i = n$$
*   **Relative Frequency ($h_i$):** The proportion or percentage of the total data that a time value represents:
    $$h_i = \frac{f_i}{n}$$
    The sum of all relative frequencies must always equal 1 (or 100%): $\sum h_i = 1$.
*   **Cumulative Absolute Frequency ($F_i$):** The running total of absolute frequencies up to a certain point:
    $$F_i = f_1 + f_2 + \dots + f_i$$
*   **Cumulative Relative Frequency ($H_i$):** The running total of relative frequencies:
    $$H_i = h_1 + h_2 + \dots + h_i \quad \text{or} \quad H_i = \frac{F_i}{n}$$

> **Time-specific note:** Cumulative frequency is especially meaningful for duration data. $F_i$ tells us how many events took **at most** the upper boundary of class $i$ to complete. $H_i$ gives the proportion of events that finished within that time bound.

---

## 2. Essential Formulas for Grouping Time Data

When time datasets are large or continuous (as is typical with sub-second measurements), we group them into **Class Intervals**.

1.  **Range ($R$):** $R = t_{max} - t_{min}$ (expressed in the chosen time unit)
2.  **Number of Classes ($k$):** (Sturges' Rule) $k = 1 + 3.322 \cdot \log_{10}(n)$
3.  **Class Width ($w$):** $w = \frac{R}{k}$ (Always round up for convenience in manual tables.)
4.  **Class Mark ($x_i$):** Midpoint of the time interval: $x_i = \frac{\text{Lower} + \text{Upper}}{2}$

> **Unit prefix gotcha:** When the range spans very small units (e.g., nanoseconds), the class width $w$ may be a fraction of a nanosecond. Always choose a unit where $w$ is a manageable number. For example, if $R = 0.005\text{ s}$ and $k = 7$, then $w \approx 0.000714\text{ s}$. Converting to milliseconds: $R = 5\text{ ms}$, $w \approx 0.714\text{ ms}$, which is far easier to work with.

---

## 3. Time-Specific Gotchas

### Gotcha 1: Floating-Point Precision with Large Epoch Timestamps

Unix epoch timestamps in **nanoseconds** can exceed $10^{18}$ (for dates far in the future). When computing class marks or sums, standard double-precision floating point (64-bit IEEE 754) has only ~15--16 significant decimal digits. This means:

$$1\,700\,000\,000\,000\,000\,000 + 0.5 \approx 1\,700\,000\,000\,000\,000\,000$$

The $0.5\text{ ns}$ addition is **lost**. Always **center** timestamp data by subtracting the minimum (or a reference epoch) before computing frequencies, variances, or class marks:

$$t_i^{\text{centered}} = t_i - t_{\min}$$

### Gotcha 2: Cyclic Clock Time Is Not Linear

Clock times (e.g., 23:59 and 00:01) are **circular**, not linear. A simple frequency table that sorts by raw clock value will place 00:01 "after" 23:59, but the two are only 2 minutes apart on a 24-hour cycle. For cyclic time data:

*   Do not compute a naive range as $t_{max} - t_{min}$ without checking for wrap-around.
*   Consider converting to a circular representation (radians) before grouping, or define a reference point and measure angular distance.

### Gotcha 3: Mixed Unit Prefixes in Raw Data

Real-world time logs may mix units (e.g., some entries in seconds, others in milliseconds). **Always normalize all values to a single unit** before building a frequency table. A single mislabeled $1000\text{ ms}$ entry read as $1000\text{ s}$ will destroy the distribution.

---

## 4. Solved Exercises (10 Examples)

### Exercise 1: Categorical Time Data (Qualitative)

**Problem:** A server logs the time-of-day category for 15 incoming requests: `Morning (M), Afternoon (A), Afternoon (A), Night (N), Morning (M), Afternoon (A), Night (N), Night (N), Afternoon (A), Afternoon (A), Morning (M), Night (N), Afternoon (A), Afternoon (A), Morning (M)`. Create a frequency table.

**Solution:**
1.  **Count:** Morning (4), Afternoon (7), Night (4). Total $n=15$.
2.  **Relative Frequency:** $h_{Morning} = 4/15 \approx 0.267$.

| Time Category | $f_i$ | $h_i$ | $F_i$ | $H_i$ |
| :--- | :--- | :--- | :--- | :--- |
| Morning | 4 | 0.267 | 4 | 0.267 |
| Afternoon | 7 | 0.467 | 11 | 0.734 |
| Night | 4 | 0.267 | 15 | 1.001 |

*(Note: The $H_i$ column sums to 1.001 due to rounding each $h_i$ to 3 decimal places. This is a standard rounding artifact.)*

---

### Exercise 2: Discrete Duration Data (Ungrouped)

**Problem:** Number of retries (a count derived from timeout events) for 10 connections: `0, 1, 2, 1, 0, 3, 2, 1, 1, 2` retries. Create a frequency table.

**Solution:**
Identify unique values: 0, 1, 2, 3.

| Retries ($x_i$) | $f_i$ | $h_i$ | $F_i$ |
| :--- | :--- | :--- | :--- |
| 0 | 2 | 0.2 | 2 |
| 1 | 4 | 0.4 | 6 |
| 2 | 3 | 0.3 | 9 |
| 3 | 1 | 0.1 | 10 |

> **Interpretation:** $F_2 = 9$ means 9 out of 10 connections experienced at most 2 retries.

---

### Exercise 3: Finding Missing Frequencies in Latency Data

**Problem:** A latency table has $n=20$ observations across 4 latency classes. Given $f_1=5, f_2=?, f_3=8, f_4=2$. Find $f_2$ and $h_2$.

**Solution:**
1.  Sum condition: $5 + f_2 + 8 + 2 = 20$
2.  $15 + f_2 = 20 \Rightarrow f_2 = 5$
3.  $h_2 = 5/20 = 0.25$.

---

### Exercise 4: Grouping Continuous Duration Data (Manual Range)

**Problem:** Group these 10 response times (in milliseconds) into 2 classes starting at 150 ms: `152, 158, 161, 164, 165, 168, 172, 175, 177, 180`. Class width $w=15\text{ ms}$.

**Solution:**
Intervals: $[150, 165)\text{ ms}$ and $[165, 180]\text{ ms}$.
*   $[150, 165)$: 152, 158, 161, 164 (4 values)
*   $[165, 180]$: 165, 168, 172, 175, 177, 180 (6 values)

| Interval (ms) | $x_i$ (ms) | $f_i$ | $F_i$ |
| :--- | :--- | :--- | :--- |
| $[150, 165)$ | 157.5 | 4 | 4 |
| $[165, 180]$ | 172.5 | 6 | 10 |

> **Interpretation:** $F_1 = 4$ means 4 requests had response times below 165 ms.

---

### Exercise 5: Applying Sturges' Rule to Execution Time Data

**Problem:** For $n=40$ execution time observations (in seconds), find the ideal number of classes $k$.

**Solution:**
$$k = 1 + 3.322 \cdot \log_{10}(40)$$
$$k = 1 + 3.322 \cdot (1.602) \approx 1 + 5.32 = 6.32$$
Rounding up, we use **7 classes**.

> **Time note:** Once $k$ is determined, compute $w = R/k$ in the chosen time unit. If execution times range from $0.1\text{ s}$ to $2.5\text{ s}$, then $R = 2.4\text{ s}$ and $w = 2.4/7 \approx 0.343\text{ s}$. Rounding up to $0.35\text{ s}$ gives clean intervals.

---

### Exercise 6: Interpreting Cumulative Frequency for Duration Data

**Problem:** In a response-time table, $F_3 = 18$ and $F_2 = 12$. What is $f_3$? Interpret the result.

**Solution:**
Since $F_3 = f_1 + f_2 + f_3$ and $F_2 = f_1 + f_2$:
$$f_3 = F_3 - F_2 = 18 - 12 = 6$$

**Interpretation:** 6 observations fell into the third time interval. If the third interval is $[200, 300)\text{ ms}$, then 6 requests had response times between 200 and 300 ms.

---

### Exercise 7: Percentage Distribution for Timeout Data

**Problem:** Convert relative frequencies $h_i = [0.15, 0.35, 0.50]$ for three timeout categories into a percentage frequency table.

**Solution:**
Multiply $h_i$ by 100.

| Timeout Category | $h_i$ | Frequency % |
| :--- | :--- | :--- |
| No timeout | 0.15 | 15% |
| Soft timeout | 0.35 | 35% |
| Hard timeout | 0.50 | 50% |

---

### Exercise 8: Full Table Construction for Processing Times (Work-in-Progress style)

**Problem:** Processing times (in seconds): `10, 12, 15, 18, 20, 22, 25, 28, 30, 35`. Group into 3 classes with $w=10\text{ s}$, starting at 10 s.

**Step 1: Identify Intervals**
$[10, 20)\text{ s},\ [20, 30)\text{ s},\ [30, 40]\text{ s}$

**Step 2: Calculate Midpoints ($x_i$)**
$x_1 = (10+20)/2 = 15\text{ s}$

**Step 3: Tally Frequencies**
*   $[10, 20)$: 10, 12, 15, 18 $\Rightarrow f_1 = 4$
*   $[20, 30)$: 20, 22, 25, 28 $\Rightarrow f_2 = 4$
*   $[30, 40]$: 30, 35 $\Rightarrow f_3 = 2$

**Final Table:**

| Interval (s) | $x_i$ (s) | $f_i$ | $h_i$ | $F_i$ |
| :--- | :--- | :--- | :--- | :--- |
| $[10, 20)$ | 15 | 4 | 0.4 | 4 |
| $[20, 30)$ | 25 | 4 | 0.4 | 8 |
| $[30, 40]$ | 35 | 2 | 0.2 | 10 |

> **Interpretation:** $H_2 = 0.8$ means 80% of processes completed within 30 seconds.

---

### Exercise 9: Unit Conversion Before Tabulation

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

> **Gotcha reminder:** The choice of unit does not change the frequencies or relative frequencies -- only the labels on the intervals change. However, choosing the right unit prevents precision loss and makes manual computation feasible.

---

### Exercise 10: R Snippet -- Building a Frequency Table for Time Data

**Problem:** Use R to construct a frequency table for the following response times (ms): `120, 135, 142, 120, 158, 135, 170, 142, 120, 190`.

**Solution:**

```r
# Response times in milliseconds
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

**Expected output:**

| Time_ms | $f_i$ | $h_i$ | $F_i$ | $H_i$ |
| :--- | :--- | :--- | :--- | :--- |
| 120 | 3 | 0.3 | 3 | 0.3 |
| 135 | 2 | 0.2 | 5 | 0.5 |
| 142 | 2 | 0.2 | 7 | 0.7 |
| 158 | 1 | 0.1 | 8 | 0.8 |
| 170 | 1 | 0.1 | 9 | 0.9 |
| 190 | 1 | 0.1 | 10 | 1.0 |

> **R note:** The `table()` function automatically sorts the unique values in ascending order, which is the correct ordering for linear time data. For cyclic clock-time data, additional preprocessing would be required.

---

## Exam Tip: The "Sum to One" Rule (Time Context)

If your relative frequencies ($h_i$) sum to 0.99 or 1.01 due to rounding, this is usually acceptable in exams. Use 3 decimal places as a standard to get as close to **1.000** as possible. This rounding artifact is independent of the time unit chosen -- it is purely a numerical effect.