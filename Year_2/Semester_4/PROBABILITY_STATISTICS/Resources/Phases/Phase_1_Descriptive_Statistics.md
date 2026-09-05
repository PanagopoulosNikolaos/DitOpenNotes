# Phase 1: Descriptive Statistics

## Table of Contents
- [Section 1.1: Data Organization & Frequency Tables](#section-11-data-organization--frequency-tables)
- [Section 1.2: Measures of Central Tendency & Skewness](#section-12-measures-of-central-tendency--skewness)
- [Section 1.3: Measures of Position & Boxplots](#section-13-measures-of-position--boxplots)
- [Section 1.4: Measures of Dispersion & Data Transformations](#section-14-measures-of-dispersion--data-transformations)
- [Exam Preparation Guide](#exam-preparation-guide)
- [Phase Summary](#phase-summary)

---

## Section 1.1: Data Organization & Frequency Tables

### Core Theory & Definitions
Data organization is the foundational phase of descriptive statistics. Raw observations -- whether survey responses, measurement heights, or system performance metrics -- are transformed into structured formats, primarily **Frequency Tables**. Organizing data makes underlying patterns, central groupings, spread, and anomalies visible.

When organizing quantitative data, observations are partitioned into either discrete value classes or continuous interval classes. Frequency distribution tables track four principal metrics:

*   **Absolute Frequency ($f_i$):** The total number of observations occurring within class $i$. The sum of all absolute frequencies equals the total sample size $n$:
    $$\sum_{i=1}^{k} f_i = n$$
*   **Relative Frequency ($h_i$):** The proportion of total observations represented by class $i$:
    $$h_i = \frac{f_i}{n}$$
    The sum of relative frequencies across all $k$ classes must equal exactly 1:
    $$\sum_{i=1}^{k} h_i = 1$$
*   **Cumulative Absolute Frequency ($F_i$):** The running total of absolute frequencies up to and including class $i$:
    $$F_i = \sum_{j=1}^{i} f_j = f_1 + f_2 + \dots + f_i$$
    By definition, $F_k = n$.
*   **Cumulative Relative Frequency ($H_i$):** The running total of relative frequencies up to and including class $i$:
    $$H_i = \sum_{j=1}^{i} h_j = \frac{F_i}{n}$$
    By definition, $H_k = 1.0$.

> **Practical / Time-Domain Note:**
> Cumulative frequencies carry direct operational meaning for latency and time-domain data. $F_i$ represents the count of requests that completed in **at most** the upper boundary time of class $i$, while $H_i$ represents the empirical probability $P(T \le U_i)$ that a system task finishes within that time limit.
> **Gotcha 1 (Epoch Timestamps):** Subtract the minimum timestamp $t_{min}$ to center high-precision epoch timestamps before computing class midpoints; raw double-precision floats lose sub-millisecond precision on numbers around $1.7 \times 10^{12}$ ms.
> **Gotcha 2 (Unit Normalization):** Mixed time metrics (e.g., nanoseconds, milliseconds, seconds) must be converted to a uniform scale prior to binning.

### Mathematical Formulas & Derivations
When grouping continuous data into $k$ intervals, standard class construction parameters are calculated as follows:

1.  **Range ($R$):**
    $$R = x_{max} - x_{min}$$
2.  **Number of Classes ($k$) via Sturges' Rule:**
    $$k = 1 + 3.322 \cdot \log_{10}(n)$$
    *(Note: $k$ is rounded to the nearest integer or rounded up to ensure complete coverage).*
3.  **Class Width ($w$):**
    $$w = \frac{R}{k}$$
    In practical tabular construction, $w$ is often rounded up slightly to a convenient round number.
4.  **Class Mark / Midpoint ($x_i$):**
    $$x_i = \frac{L_i + U_i}{2}$$
    where $L_i$ and $U_i$ are the lower and upper boundaries of class interval $i$.

> **Practical / Time-Domain Adapted Formula:**
> For time-domain intervals measured in seconds, milliseconds, or nanoseconds, every class mark carries explicit time units:
> $$x_{i, [s]} = \frac{L_{i, [s]} + U_{i, [s]}}{2}, \quad w_{[s]} = \frac{R_{[s]}}{k}$$
> Class boundaries and midpoints scale linearly when changing time units.

### Worked Exercises

#### Exercise 1: Categorical Frequency Table Construction
**Problem:** A QA engineer inspects 20 production components and records defect types: None (N), Surface (S), Electrical (E), and Structural (T). The sample data are: `N, S, N, N, E, N, S, T, N, E, N, N, S, N, E, N, T, N, S, N`. Construct the absolute and relative frequency table.

**Solution:**
1.  **Count Absolute Frequencies ($f_i$):**
    *   None (N): 11
    *   Surface (S): 4
    *   Electrical (E): 3
    *   Structural (T): 2
    *   Total $n = 11 + 4 + 3 + 2 = 20$.
2.  **Compute Relative Frequencies ($h_i = f_i / 20$):**
    *   $h_N = 11/20 = 0.55$
    *   $h_S = 4/20 = 0.20$
    *   $h_E = 3/20 = 0.15$
    *   $h_T = 2/20 = 0.10$

| Defect Type | $f_i$ | $h_i$ | $F_i$ | $H_i$ |
| :--- | :--- | :--- | :--- | :--- |
| None (N) | 11 | 0.55 | 11 | 0.55 |
| Surface (S) | 4 | 0.20 | 15 | 0.75 |
| Electrical (E) | 3 | 0.15 | 18 | 0.90 |
| Structural (T) | 2 | 0.10 | 20 | 1.00 |

**Final Answer:** Table complete. $\sum f_i = \mathbf{20}$, $\sum h_i = \mathbf{1.00}$.

#### Exercise 2: Discrete Frequency Table and Relative Proportions
**Problem:** The number of software bugs reported per module across 15 modules is recorded: `0, 1, 2, 1, 0, 3, 2, 1, 1, 2, 0, 4, 1, 2, 1`. Construct an ungrouped frequency distribution table.

**Solution:**
Unique values present: 0, 1, 2, 3, 4.

| Bugs ($x_i$) | $f_i$ | $h_i$ | $F_i$ | $H_i$ |
| :--- | :--- | :--- | :--- | :--- |
| 0 | 3 | $3/15 \approx 0.200$ | 3 | 0.200 |
| 1 | 6 | $6/15 = 0.400$ | 9 | 0.600 |
| 2 | 4 | $4/15 \approx 0.267$ | 13 | 0.867 |
| 3 | 1 | $1/15 \approx 0.067$ | 14 | 0.934 |
| 4 | 1 | $1/15 \approx 0.067$ | 15 | 1.001 |

**Final Answer:** Un-grouped frequency table compiled ($n=\mathbf{15}$).

#### Exercise 3: Sturges' Rule and Continuous Data Binning
**Problem:** A dataset consists of $n = 50$ continuous student exam scores ranging from $x_{min} = 42$ to $x_{max} = 98$. Determine the optimal number of classes $k$ using Sturges' Rule and find the recommended class width $w$.

**Solution:**
1.  **Apply Sturges' Rule:**
    $$k = 1 + 3.322 \cdot \log_{10}(50)$$
    $$\log_{10}(50) \approx 1.69897$$
    $$k = 1 + 3.322 \cdot (1.69897) = 1 + 5.644 = 6.644$$
    Rounding to the nearest integer gives $k = 7$ classes.
2.  **Compute Range ($R$):**
    $$R = 98 - 42 = 56$$
3.  **Compute Class Width ($w$):**
    $$w = \frac{56}{7} = 8$$

**Final Answer:** Optimal number of classes $k = \mathbf{7}$, recommended class width $w = \mathbf{8}$.

#### Exercise 4: Grouped Frequency Table Construction & Cumulative Ratios
**Problem:** Given 12 raw test measurements: `14, 17, 18, 22, 25, 26, 29, 31, 33, 35, 38, 41`. Group the data into 3 equal-width classes starting at $L_1 = 10$ with width $w = 11$.
**a)** Determine the class intervals and midpoints ($x_i$).
**b)** Calculate absolute ($f_i$) and relative ($h_i$) frequencies.
**c)** Compute cumulative relative frequencies ($H_i$) and interpret $H_2$.

**Solution:**
**a)** Class Intervals and Midpoints:
*   Class 1: $[10, 21)$, midpoint $x_1 = (10 + 21)/2 = 15.5$
*   Class 2: $[21, 32)$, midpoint $x_2 = (21 + 32)/2 = 26.5$
*   Class 3: $[32, 43]$, midpoint $x_3 = (32 + 43)/2 = 37.5$

**b)** Tally Frequencies:
*   $[10, 21)$: `14, 17, 18` $\rightarrow f_1 = 3$, $h_1 = 3/12 = 0.25$
*   $[21, 32)$: `22, 25, 26, 29, 31` $\rightarrow f_2 = 5$, $h_2 = 5/12 \approx 0.4167$
*   $[32, 43]$: `33, 35, 38, 41` $\rightarrow f_3 = 4$, $h_3 = 4/12 \approx 0.3333$

| Interval | $x_i$ | $f_i$ | $h_i$ | $F_i$ | $H_i$ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| $[10, 21)$ | 15.5 | 3 | 0.2500 | 3 | 0.2500 |
| $[21, 32)$ | 26.5 | 5 | 0.4167 | 8 | 0.6667 |
| $[32, 43]$ | 37.5 | 4 | 0.3333 | 12 | 1.0000 |

**c)** Interpretation of $H_2$:
$$H_2 = 0.6667 \quad (66.67\%)$$
Exactly $66.67\%$ of the observations are strictly less than $32$.

**Final Answer:** $H_2 = \mathbf{0.6667}$; two-thirds of measurements fall below 32.

#### Exercise 5: Web Server Request Processing Latency Binning (Time-Domain)
**Problem:** A web server logs 10 execution durations (in milliseconds): `105, 112, 118, 125, 128, 134, 140, 145, 152, 168`. Group the data into 3 classes starting at $100\text{ ms}$ with class width $w = 25\text{ ms}$. Compute $f_i$ and $F_i$.

**Solution:**
1.  **Class Intervals:**
    *   Class 1: $[100, 125)\text{ ms}$, Midpoint $x_1 = 112.5\text{ ms}$
    *   Class 2: $[125, 150)\text{ ms}$, Midpoint $x_2 = 137.5\text{ ms}$
    *   Class 3: $[150, 175]\text{ ms}$, Midpoint $x_3 = 162.5\text{ ms}$
2.  **Tally Values:**
    *   $[100, 125)\text{ ms}$: `105, 112, 118` $\Rightarrow f_1 = 3$, $F_1 = 3$
    *   $[125, 150)\text{ ms}$: `125, 128, 134, 140, 145` $\Rightarrow f_2 = 5$, $F_2 = 8$
    *   $[150, 175]\text{ ms}$: `152, 168` $\Rightarrow f_3 = 2$, $F_3 = 10$

| Latency Interval (ms) | $x_{i, [ms]}$ | $f_i$ | $F_i$ |
| :--- | :--- | :--- | :--- |
| $[100, 125)$ | 112.5 | 3 | 3 |
| $[125, 150)$ | 137.5 | 5 | 8 |
| $[150, 175]$ | 162.5 | 2 | 10 |

**Final Answer:** Table constructed. $F_3 = \mathbf{10}$ requests total.

#### Exercise 6: Epoch Timestamp Centering and Frequency Mapping (Time-Domain)
**Problem:** High-precision timestamps (in seconds from midnight) are recorded for 6 incoming API calls: `43200.002, 43200.005, 43200.012, 43200.018, 43200.022, 43200.029`.
**a)** Center the data by subtracting $t_0 = 43200.000\text{ s}$ to express offset $\Delta t$ in milliseconds.
**b)** Group the offsets into 3 classes of width $w = 10\text{ ms}$ starting at $0\text{ ms}$.

**Solution:**
**a)** Subtract $43200.000\text{ s}$ and multiply by $1000\text{ ms/s}$:
*   `43200.002` $\rightarrow 0.002\text{ s} = 2\text{ ms}$
*   `43200.005` $\rightarrow 0.005\text{ s} = 5\text{ ms}$
*   `43200.012` $\rightarrow 0.012\text{ s} = 12\text{ ms}$
*   `43200.018` $\rightarrow 0.018\text{ s} = 18\text{ ms}$
*   `43200.022` $\rightarrow 0.022\text{ s} = 22\text{ ms}$
*   `43200.029` $\rightarrow 0.029\text{ s} = 29\text{ ms}$

**b)** Intervals $[0, 10)\text{ ms}$, $[10, 20)\text{ ms}$, $[20, 30]\text{ ms}$:
*   $[0, 10)\text{ ms}$: `2, 5` $\Rightarrow f_1 = 2$
*   $[10, 20)\text{ ms}$: `12, 18` $\Rightarrow f_2 = 2$
*   $[20, 30]\text{ ms}$: `22, 29` $\Rightarrow f_3 = 2$

**Final Answer:** Centered offsets: `2, 5, 12, 18, 22, 29` ms. Equal frequency $f_i = \mathbf{2}$ across all 3 classes.

#### Exercise 7: Multi-Part Network Packet Interval Frequency Analysis (Time-Domain)
**Problem:** Inter-arrival times between network packets (in microseconds) for 16 packets are: `120, 150, 180, 210, 240, 250, 270, 300, 310, 330, 360, 400, 420, 450, 480, 510`.
**a)** Apply Sturges' rule to find the number of classes $k$.
**b)** Construct the grouped frequency table using lower bound $L_1 = 100\ \mu\text{s}$ and uniform width $w = 100\ \mu\text{s}$.
**c)** Write an R command snippet to calculate the cumulative relative frequencies from the raw vector `intervals_us`.

**Solution:**
**a)** $k = 1 + 3.322 \cdot \log_{10}(16) = 1 + 3.322 \cdot (1.2041) = 1 + 4.000 = 5$ classes.
**b)** Grouping with $w = 100\ \mu\text{s}$:
*   $[100, 200)\ \mu\text{s}$: `120, 150, 180` $\Rightarrow f_1 = 3, h_1 = 3/16 = 0.1875, F_1 = 3, H_1 = 0.1875$
*   $[200, 300)\ \mu\text{s}$: `210, 240, 250, 270` $\Rightarrow f_2 = 4, h_2 = 4/16 = 0.2500, F_2 = 7, H_2 = 0.4375$
*   $[300, 400)\ \mu\text{s}$: `300, 310, 330, 360` $\Rightarrow f_3 = 4, h_3 = 4/16 = 0.2500, F_3 = 11, H_3 = 0.6875$
*   $[400, 500)\ \mu\text{s}$: `400, 420, 450, 480` $\Rightarrow f_4 = 4, h_4 = 4/16 = 0.2500, F_4 = 15, H_4 = 0.9375$
*   $[500, 600]\ \mu\text{s}$: `510` $\Rightarrow f_5 = 1, h_5 = 1/16 = 0.0625, F_5 = 16, H_5 = 1.0000$

**c)** R Code:
```r
intervals_us <- c(120, 150, 180, 210, 240, 250, 270, 300, 310, 330, 360, 400, 420, 450, 480, 510)
bins <- seq(100, 600, by = 100)
counts <- table(cut(intervals_us, breaks = bins, right = FALSE))
H_i <- cumsum(counts) / length(intervals_us)
print(H_i)
```

**Final Answer:** $k = \mathbf{5}$; table compiled; R code produces vector `c(0.1875, 0.4375, 0.6875, 0.9375, 1.0000)`.

#### Exercise 8: Sub-Millisecond Database Query Latency Grouping (Time-Domain)
**Problem:** Latency values (in milliseconds) for 10 queries are: `0.12, 0.18, 0.25, 0.31, 0.38, 0.42, 0.55, 0.68, 0.75, 0.92`. Group the data into 4 equal classes spanning $[0.10, 0.90]\text{ ms}$ with width $w = 0.20\text{ ms}$.

**Solution:**
Intervals: $[0.10, 0.30)$, $[0.30, 0.50)$, $[0.50, 0.70)$, $[0.70, 0.90]$. (Note: $0.92$ falls in an overflow class $[0.90, 1.10]$).
*   $[0.10, 0.30)\text{ ms}$: `0.12, 0.18, 0.25` $\Rightarrow f_1 = 3$
*   $[0.30, 0.50)\text{ ms}$: `0.31, 0.38, 0.42` $\Rightarrow f_2 = 3$
*   $[0.50, 0.70)\text{ ms}$: `0.55, 0.68` $\Rightarrow f_3 = 2$
*   $[0.70, 0.90)\text{ ms}$: `0.75` $\Rightarrow f_4 = 1$
*   $[0.90, 1.10]\text{ ms}$: `0.92` $\Rightarrow f_5 = 1$

**Final Answer:** Frequencies per interval: $f_1=\mathbf{3}, f_2=\mathbf{3}, f_3=\mathbf{2}, f_4=\mathbf{1}, f_5=\mathbf{1}$.

### R Implementation
```r
# Section 1.1: Data Organization & Frequency Tables
# Constructing complete frequency distribution table in R
latency_ms <- c(105, 112, 118, 125, 128, 134, 140, 145, 152, 168)

# Define breaks and create frequency table
breaks <- seq(100, 175, by = 25)
freq_table <- data.frame(Interval = levels(cut(latency_ms, breaks = breaks, right = FALSE)))
freq_table$f_i <- as.vector(table(cut(latency_ms, breaks = breaks, right = FALSE)))
freq_table$h_i <- freq_table$f_i / sum(freq_table$f_i)
freq_table$F_i <- cumsum(freq_table$f_i)
freq_table$H_i <- cumsum(freq_table$h_i)

print(freq_table)
```

---

## Section 1.2: Measures of Central Tendency & Skewness

### Core Theory & Definitions
Measures of central tendency quantify the location of the "center" or modal cluster of a dataset. The three primary metrics are:

1.  **Arithmetic Mean ($\bar{x}$):** The sum of all numerical values divided by the total count $n$. It represents the physical "center of mass" of the distribution. It is sensitive to extreme outliers.
2.  **Median ($M_e$):** The middle value when data points are arranged in ascending order. If $n$ is even, it is the average of the two central values. The median is robust to extreme outliers.
3.  **Mode ($M_o$):** The value or class midpoint that appears with the maximum frequency. A dataset may be unimodal, bimodal, or multimodal.

#### Skewness & Distribution Asymmetry
Skewness describes the asymmetry of a real-valued random variable's probability distribution around its mean:
*   **Symmetric Distribution:** Mean = Median = Mode.
*   **Positive (Right) Skewness:** Distribution extends a long tail toward higher positive values. Mode < Median < Mean.
*   **Negative (Left) Skewness:** Distribution extends a long tail toward lower negative values. Mean < Median < Mode.

Pearson's First Coefficient of Skewness ($SK_1$) and Second Coefficient ($SK_2$) quantify this relationship:
$$SK_1 = \frac{\bar{x} - M_o}{s}, \quad SK_2 = \frac{3(\bar{x} - M_e)}{s}$$

> **Practical / Time-Domain Note:**
> Systems and execution latencies almost universally exhibit **strong positive skewness** due to long-tail queueing delays, garbage collection pauses, or retransmissions. Consequently, the **Mean** overstates typical performance, whereas the **Median ($M_e$)** accurately reflects typical user experience.
> **Gotcha (Circular Clock Times):** The standard arithmetic mean fails completely for cyclic time metrics (e.g., timestamps recorded near 23:59 and 00:01). The arithmetic average of $23\text{h}$ and $1\text{h}$ is $12\text{h}$ (noon), which is completely wrong. Cyclic times require the **Circular Mean**.

### Mathematical Formulas & Derivations

#### Ungrouped Formulas
*   **Arithmetic Mean:** $\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i$
*   **Median:**
    $$M_e = \begin{cases} x_{\left(\frac{n+1}{2}\right)}, & \text{if } n \text{ is odd} \\ \frac{x_{\left(\frac{n}{2}\right)} + x_{\left(\frac{n}{2}+1\right)}}{2}, & \text{if } n \text{ is even} \end{cases}$$

#### Grouped Data Formulas (Interpolation)
*   **Grouped Mean:**
    $$\bar{x} = \frac{\sum_{i=1}^{k} f_i \cdot x_i}{n}$$
*   **Grouped Median ($M_e$):**
    $$M_e = L_m + \left( \frac{\frac{n}{2} - F_{m-1}}{f_m} \right) \cdot w$$
    where $L_m$ is the lower boundary of the median class (the first class where $F_i \ge n/2$), $F_{m-1}$ is the cumulative frequency of the preceding class, $f_m$ is the median class frequency, and $w$ is class width.
*   **Grouped Mode ($M_o$):**
    $$M_o = L_o + \left( \frac{f_o - f_{o-1}}{(f_o - f_{o-1}) + (f_o - f_{o+1})} \right) \cdot w$$
    where $L_o$ is the lower boundary of the modal class (class with highest $f_i$), $f_o$ is modal frequency, $f_{o-1}$ is frequency of the preceding class, and $f_{o+1}$ is frequency of the succeeding class.

> **Time-Domain Adapted Formulas:**
> When applied to continuous time data in seconds, all interpolated quantities retain time units $[s]$:
> $$\bar{x}_{[s]} = \frac{\sum f_i \cdot x_{i, [s]}}{n}$$
> $$M_{e, [s]} = L_{m, [s]} + \left( \frac{\frac{n}{2} - F_{m-1}}{f_m} \right) \cdot w_{[s]}$$
> $$M_{o, [s]} = L_{o, [s]} + \left( \frac{f_o - f_{o-1}}{(f_o - f_{o-1}) + (f_o - f_{o+1})} \right) \cdot w_{[s]}$$

#### Circular Mean for Cyclic Clock Times
For clock times $t_i \in [0, 24)$ hours, map each time to an angle $\theta_i = \frac{2\pi \cdot t_i}{24}$ radians:
$$\bar{S} = \frac{1}{n} \sum_{i=1}^{n} \sin(\theta_i), \quad \bar{C} = \frac{1}{n} \sum_{i=1}^{n} \cos(\theta_i)$$
$$\bar{\theta} = \text{atan2}(\bar{S}, \bar{C})$$
$$\bar{t}_{\text{circular}} = \frac{24 \cdot \bar{\theta}}{2\pi} \pmod{24}$$

### Worked Exercises

#### Exercise 9: Central Tendency Comparison for Salary Data
**Problem:** Annual salaries (in thousands of dollars) for 7 employees in a small firm are: `28, 32, 35, 38, 42, 45, 210`. Compute the Mean, Median, and Mode.

**Solution:**
1.  **Mean ($\bar{x}$):**
    $$\bar{x} = \frac{28 + 32 + 35 + 38 + 42 + 45 + 210}{7} = \frac{430}{7} \approx \mathbf{61.43}$$
2.  **Median ($M_e$):**
    Ordered sample ($n=7$, odd): position $(7+1)/2 = 4$th element.
    $$M_e = \mathbf{38.00}$$
3.  **Mode ($M_o$):**
    All values appear once. **No unique mode**.

**Final Answer:** Mean = $\mathbf{61.43}$, Median = $\mathbf{38.00}$, Mode = **None**. (Outlier \$210k inflates the mean well above the upper quartile).

#### Exercise 10: Grouped Mean and Interpolated Median Calculation
**Problem:** Given the grouped frequency table ($n=40$):

| Interval | $x_i$ | $f_i$ | $F_i$ |
| :--- | :--- | :--- | :--- |
| $[10, 20)$ | 15 | 6 | 6 |
| $[20, 30)$ | 25 | 14 | 20 |
| $[30, 40)$ | 35 | 12 | 32 |
| $[40, 50]$ | 45 | 8 | 40 |

Compute **a)** Grouped Mean $\bar{x}$, **b)** Grouped Median $M_e$.

**Solution:**
**a) Grouped Mean ($\bar{x}$):**
$$\sum f_i x_i = (6 \cdot 15) + (14 \cdot 25) + (12 \cdot 35) + (8 \cdot 45) = 90 + 350 + 420 + 360 = 1220$$
$$\bar{x} = \frac{1220}{40} = \mathbf{30.50}$$

**b) Grouped Median ($M_e$):**
Position $n/2 = 40/2 = 20$.
Looking at $F_i$, class $[20, 30)$ has $F_2 = 20 \ge 20$. Thus, median class is $[20, 30)$.
$L_m = 20, w = 10, f_m = 14, F_{m-1} = 6$.
$$M_e = 20 + \left( \frac{20 - 6}{14} \right) \cdot 10 = 20 + \left( \frac{14}{14} \right) \cdot 10 = 20 + 10 = \mathbf{30.00}$$

**Final Answer:** Grouped Mean $\bar{x} = \mathbf{30.50}$, Grouped Median $M_e = \mathbf{30.00}$.

#### Exercise 11: Grouped Mode and Skewness Coefficient Analysis
**Problem:** Using the dataset from Exercise 10 ($n=40, \bar{x} = 30.50, M_e = 30.00$, sample standard deviation $s = 9.80$):
**a)** Compute the grouped Mode $M_o$.
**b)** Calculate Pearson's second coefficient of skewness $SK_2$.
**c)** State the directional skewness of the distribution.

**Solution:**
**a) Grouped Mode ($M_o$):**
Modal class is $[20, 30)$ because it has maximum frequency $f_o = 14$.
$L_o = 20, w = 10, f_o = 14, f_{o-1} = 6, f_{o+1} = 12$.
$$M_o = 20 + \left( \frac{14 - 6}{(14 - 6) + (14 - 12)} \right) \cdot 10 = 20 + \left( \frac{8}{8 + 2} \right) \cdot 10 = 20 + 8 = \mathbf{28.00}$$

**b) Pearson's Second Skewness Coefficient ($SK_2$):**
$$SK_2 = \frac{3(\bar{x} - M_e)}{s} = \frac{3(30.50 - 30.00)}{9.80} = \frac{1.50}{9.80} \approx \mathbf{0.1531}$$

**c) Directional Skewness:**
Since $M_o (28.00) < M_e (30.00) < \bar{x} (30.50)$ and $SK_2 > 0$, the distribution exhibits **slight positive (right) skewness**.

**Final Answer:** Mode $M_o = \mathbf{28.00}$, $SK_2 = \mathbf{0.1531}$ (**Slight Positive Skewness**).

#### Exercise 12: Effect of Extreme Outliers on Mean vs Median
**Problem:** Consider 5 test scores: `70, 72, 75, 78, 80`.
**a)** Compute Mean and Median.
**b)** If the score 80 is replaced by an extreme recording error of `800`, recalculate Mean and Median.

**Solution:**
**a) Original:**
*   $\bar{x} = (70 + 72 + 75 + 78 + 80)/5 = 375/5 = \mathbf{75.00}$
*   $M_e = \mathbf{75.00}$ (3rd element)

**b) Contaminated (`800`):**
*   $\bar{x}_{new} = (70 + 72 + 75 + 78 + 800)/5 = 1095/5 = \mathbf{219.00}$
*   $M_e = \mathbf{75.00}$ (Unchanged!)

**Final Answer:** Original Mean & Median = $\mathbf{75.00}$. Contaminated Mean = $\mathbf{219.00}$, Median = $\mathbf{75.00}$ (demonstrating median resistance).

#### Exercise 13: Microservice API Response Time Central Metrics (Time-Domain)
**Problem:** Execution latency values (in ms) for 6 API calls are: `12.4, 13.1, 12.8, 14.5, 12.4, 85.0`. Calculate Mean and Median response times.

**Solution:**
1.  **Mean ($\bar{x}$):**
    $$\bar{x} = \frac{12.4 + 13.1 + 12.8 + 14.5 + 12.4 + 85.0}{6} = \frac{150.2}{6} \approx \mathbf{25.033\text{ ms}}$$
2.  **Median ($M_e$):**
    Ordered values: `12.4, 12.4, 12.8, 13.1, 14.5, 85.0` ($n=6$, even).
    $$M_e = \frac{x_{(3)} + x_{(4)}}{2} = \frac{12.8 + 13.1}{2} = \mathbf{12.95\text{ ms}}$$

**Final Answer:** Mean = $\mathbf{25.033\text{ ms}}$, Median = $\mathbf{12.95\text{ ms}}$. The 85ms latency spike heavily skews the mean.

#### Exercise 14: Grouped Mean and Mode for Server Response Durations (Time-Domain)
**Problem:** Latencies (in ms) for $n=100$ requests are binned into:

| Interval (ms) | $x_{i, [ms]}$ | $f_i$ |
| :--- | :--- | :--- |
| $[0, 50)$ | 25 | 20 |
| $[50, 100)$ | 75 | 50 |
| $[100, 150)$ | 125 | 20 |
| $[150, 200]$ | 175 | 10 |

Compute the grouped mean latency $\bar{x}_{[ms]}$ and interpolated mode $M_{o, [ms]}$.

**Solution:**
1.  **Grouped Mean ($\bar{x}_{[ms]}$):**
    $$\sum f_i x_i = (20 \cdot 25) + (50 \cdot 75) + (20 \cdot 125) + (10 \cdot 175) = 500 + 3750 + 2500 + 1750 = 8500$$
    $$\bar{x}_{[ms]} = \frac{8500}{100} = \mathbf{85.00\text{ ms}}$$
2.  **Grouped Mode ($M_{o, [ms]}$):**
    Modal class is $[50, 100)\text{ ms}$ ($f_o = 50$).
    $L_o = 50, w = 50, f_o = 50, f_{o-1} = 20, f_{o+1} = 20$.
    $$M_{o, [ms]} = 50 + \left( \frac{50 - 20}{(50 - 20) + (50 - 20)} \right) \cdot 50 = 50 + \left( \frac{30}{60} \right) \cdot 50 = 50 + 25 = \mathbf{75.00\text{ ms}}$$

**Final Answer:** Grouped Mean = $\mathbf{85.00\text{ ms}}$, Grouped Mode = $\mathbf{75.00\text{ ms}}$.

#### Exercise 15: Circular Mean Calculation for Daily Server Backup Timestamps (Time-Domain)
**Problem:** Four automated backup jobs complete at clock times: $23.0\text{h}$ (23:00), $23.5\text{h}$ (23:30), $0.5\text{h}$ (00:30), and $1.0\text{h}$ (01:00).
**a)** Show why the naive arithmetic mean gives an invalid result.
**b)** Compute the true circular mean time $\bar{t}_{\text{circular}}$.

**Solution:**
**a) Naive Arithmetic Mean:**
$$\bar{t}_{\text{naive}} = \frac{23.0 + 23.5 + 0.5 + 1.0}{4} = \frac{48.0}{4} = 12.0\text{h} \quad (12:00 \text{ Noon})$$
This is absurd because all jobs ran near midnight ($00:00$), not at noon.

**b) Circular Mean:**
Convert times $t_i$ to angles $\theta_i = \frac{2\pi \cdot t_i}{24}$:
*   $t_1 = 23.0 \Rightarrow \theta_1 = \frac{2\pi(23)}{24} = \frac{23\pi}{12} \text{ rad} \approx 6.0214 \Rightarrow \sin\theta_1 \approx -0.2588, \cos\theta_1 \approx 0.9659$
*   $t_2 = 23.5 \Rightarrow \theta_2 = \frac{2\pi(23.5)}{24} = \frac{47\pi}{24} \text{ rad} \approx 6.1523 \Rightarrow \sin\theta_2 \approx -0.1305, \cos\theta_2 \approx 0.9914$
*   $t_3 = 0.5 \Rightarrow \theta_3 = \frac{2\pi(0.5)}{24} = \frac{\pi}{24} \text{ rad} \approx 0.1309 \Rightarrow \sin\theta_3 \approx 0.1305, \cos\theta_3 \approx 0.9914$
*   $t_4 = 1.0 \Rightarrow \theta_4 = \frac{2\pi(1.0)}{24} = \frac{\pi}{12} \text{ rad} \approx 0.2618 \Rightarrow \sin\theta_4 \approx 0.2588, \cos\theta_4 \approx 0.9659$

Sum components:
$$\sum \sin\theta_i = -0.2588 - 0.1305 + 0.1305 + 0.2588 = 0.0000$$
$$\sum \cos\theta_i = 0.9659 + 0.9914 + 0.9914 + 0.9659 = 3.9146$$
$$\bar{\theta} = \text{atan2}(0.0000, 3.9146) = 0.0000 \text{ rad}$$
$$\bar{t}_{\text{circular}} = \frac{24 \cdot 0.0000}{2\pi} = \mathbf{0.00\text{h}} \quad (00:00 \text{ Midnight})$$

**Final Answer:** Naive Mean = $12.0\text{h}$ (Invalid); Circular Mean $\bar{t}_{\text{circular}} = \mathbf{0.00\text{h}}$ ($00:00$ Midnight).

#### Exercise 16: Skewness Analysis in Microservice High-Tail Latencies (Time-Domain)
**Problem:** Latency audit of $n=1000$ microservice calls yields $\bar{x} = 45.0\text{ ms}, M_e = 20.0\text{ ms}, M_o = 15.0\text{ ms}$, and $s = 40.0\text{ ms}$.
**a)** Calculate Pearson's First and Second Skewness Coefficients ($SK_1, SK_2$).
**b)** Interpret the system behavior based on these metrics.
**c)** Write an R command snippet to compute the sample skewness using the `e1071` library.

**Solution:**
**a) Skewness Coefficients:**
$$SK_1 = \frac{\bar{x} - M_o}{s} = \frac{45.0 - 15.0}{40.0} = \frac{30.0}{40.0} = \mathbf{0.7500}$$
$$SK_2 = \frac{3(\bar{x} - M_e)}{s} = \frac{3(45.0 - 20.0)}{40.0} = \frac{75.0}{40.0} = \mathbf{1.8750}$$

**b) System Interpretation:**
Both $SK_1 > 0$ and $SK_2 > 0$ with $M_o < M_e < \bar{x}$. The API has **strong positive skewness**, indicating that while most requests finish quickly ($15-20\text{ ms}$), severe tail latency bottlenecks pull the arithmetic mean up to $45\text{ ms}$.

**c) R Snippet:**
```r
# R command for skewness calculation
library(e1071)
latencies <- c(15, 20, 45, 120, 18, 22, 16) # Sample vector
skewness_val <- skewness(latencies, type = 2) # Type 2 maps to SAS/SPSS formula
cat("Sample Skewness:", skewness_val)
```

**Final Answer:** $SK_1 = \mathbf{0.7500}, SK_2 = \mathbf{1.8750}$; strong right-skewed tail distribution.

### R Implementation
```r
# Section 1.2: Central Tendency & Skewness in R
library(e1071)

latencies_ms <- c(12.4, 12.4, 12.8, 13.1, 14.5, 85.0)

mean_val <- mean(latencies_ms)
median_val <- median(latencies_ms)

# Custom Mode function
get_mode <- function(v) {
   uniqv <- unique(v)
   uniqv[which.max(tabulate(match(v, uniqv)))]
}
mode_val <- get_mode(latencies_ms)
skew_val <- skewness(latencies_ms)

cat("Mean:", mean_val, "\nMedian:", median_val, "\nMode:", mode_val, "\nSkewness:", skew_val, "\n")
```

---

## Section 1.3: Measures of Position & Boxplots

### Core Theory & Definitions
Measures of position divide an ordered dataset into equal portions:

*   **Quartiles ($Q_1, Q_2, Q_3$):** Divide ordered data into 4 equal quarters ($25\%, 50\%, 75\%$). $Q_2$ equals the Median $M_e$.
*   **Deciles ($D_1, \dots, D_9$):** Divide ordered data into 10 equal parts ($10\%, 20\%, \dots, 90\%$).
*   **Percentiles ($P_1, \dots, P_{99}$):** Divide ordered data into 100 equal parts. $P_{50} = Q_2 = M_e$.
*   **Interquartile Range ($IQR$):** The spread of the middle $50\%$ of the data:
    $$IQR = Q_3 - Q_1$$

#### Five-Number Summary & Boxplot Construction
The Five-Number Summary consists of: $\mathbf{\text{Min}, Q_1, Q_2, Q_3, \text{Max}}$.
A **Boxplot** visually encodes this summary:
1.  A central box spans from $Q_1$ to $Q_3$ (length = $IQR$).
2.  A vertical line inside the box marks $Q_2$ (Median).
3.  **Inner Fences:** $[Q_1 - 1.5 \cdot IQR, Q_3 + 1.5 \cdot IQR]$. Values outside these fences are flagged as **Outliers**.
4.  **Whiskers:** Extend from $Q_1$ and $Q_3$ to the lowest and highest observations *within* the inner fences.

> **Practical / Time-Domain Note:**
> In engineering and SLA performance monitoring, percentiles are the standard metric for compliance:
> *   $\mathbf{p50}$ ($P_{50}$): Median response time.
> *   $\mathbf{p90}, \mathbf{p95}, \mathbf{p99}$ ($P_{90}, P_{95}, P_{99}$): Tail latency thresholds. An SLA stating "p99 $< 200\text{ ms}$" guarantees $99\%$ of requests complete within $200\text{ ms}$.
> **Gotcha:** Percentile ranks (e.g., $99$th percentile) are dimensionless positions; percentile values carry the physical unit of the metric ($ms$).

### Mathematical Formulas & Derivations

#### Ungrouped Quantile Position ($P_{pos}$)
For sample size $n$ ordered observations:
$$P_{pos} = \frac{k \cdot (n + 1)}{N_{parts}}$$
where $N_{parts} = 4$ for Quartiles, $10$ for Deciles, $100$ for Percentiles.

#### Grouped Quantile Interpolation Formula
To compute quantile $Q_k$ or $P_k$ from a grouped frequency table:
$$\text{Position} = \frac{k \cdot n}{N_{parts}}$$
$$Q_k = L_q + \left( \frac{\text{Position} - F_{q-1}}{f_q} \right) \cdot w$$
where $L_q$ is lower boundary of quantile class, $F_{q-1}$ is cumulative frequency before quantile class, $f_q$ is class frequency, and $w$ is class width.

### Worked Exercises

#### Exercise 17: Quartiles, Deciles, and Percentiles for Exam Scores
**Problem:** Ordered dataset of $n=11$ student scores: `52, 58, 63, 66, 71, 75, 79, 82, 88, 91, 95`. Find **a)** $Q_1, Q_3$, **b)** Interquartile Range $IQR$, **c)** $D_6$ (6th decile), **d)** $P_{80}$ (80th percentile).

**Solution:**
**a) Quartiles $Q_1, Q_3$:**
*   $Q_1$ position: $\frac{1(11+1)}{4} = 3$rd element $\Rightarrow Q_1 = \mathbf{63.00}$
*   $Q_3$ position: $\frac{3(11+1)}{4} = 9$th element $\Rightarrow Q_3 = \mathbf{88.00}$

**b) Interquartile Range ($IQR$):**
$$IQR = Q_3 - Q_1 = 88.00 - 63.00 = \mathbf{25.00}$$

**c) Decile $D_6$:**
Position = $\frac{6(11+1)}{10} = \frac{72}{10} = 7.2$.
Interpolate between 7th (79) and 8th (82) elements:
$$D_6 = x_{(7)} + 0.2(x_{(8)} - x_{(7)}) = 79 + 0.2(82 - 79) = 79 + 0.6 = \mathbf{79.60}$$

**d) Percentile $P_{80}$:**
Position = $\frac{80(11+1)}{100} = \frac{960}{100} = 9.6$.
Interpolate between 9th (88) and 10th (91) elements:
$$P_{80} = x_{(9)} + 0.6(x_{(10)} - x_{(9)}) = 88 + 0.6(91 - 88) = 88 + 1.8 = \mathbf{89.80}$$

**Final Answer:** $Q_1 = \mathbf{63.00}, Q_3 = \mathbf{88.00}, IQR = \mathbf{25.00}, D_6 = \mathbf{79.60}, P_{80} = \mathbf{89.80}$.

#### Exercise 18: Grouped Percentile Interpolation and Five-Number Summary
**Problem:** Given grouped frequency data ($n=100$):

| Interval | $f_i$ | $F_i$ |
| :--- | :--- | :--- |
| $[0, 20)$ | 15 | 15 |
| $[20, 40)$ | 35 | 50 |
| $[40, 60)$ | 30 | 80 |
| $[60, 80]$ | 20 | 100 |

**a)** Compute $Q_1, Q_2, Q_3$.
**b)** Compute the $IQR$ and inner fence boundaries.
**c)** State the Five-Number Summary.

**Solution:**
**a) Quantiles:**
*   **$Q_1$ (25th percentile):** Position $= 100/4 = 25$.
    Class $[20, 40)$ ($F_2 = 50 \ge 25$). $L_q = 20, w = 20, f_q = 35, F_{q-1} = 15$.
    $$Q_1 = 20 + \left( \frac{25 - 15}{35} \right) \cdot 20 = 20 + \left( \frac{10}{35} \right) \cdot 20 = 20 + 5.714 = \mathbf{25.714}$$
*   **$Q_2$ (Median, 50th percentile):** Position $= 50$.
    Class $[20, 40)$ ($F_2 = 50$). $L_q = 20, w = 20, f_q = 35, F_{q-1} = 15$.
    $$Q_2 = 20 + \left( \frac{50 - 15}{35} \right) \cdot 20 = 20 + \left( \frac{35}{35} \right) \cdot 20 = 20 + 20 = \mathbf{40.000}$$
*   **$Q_3$ (75th percentile):** Position $= (3 \cdot 100)/4 = 75$.
    Class $[40, 60)$ ($F_3 = 80 \ge 75$). $L_q = 40, w = 20, f_q = 30, F_{q-1} = 50$.
    $$Q_3 = 40 + \left( \frac{75 - 50}{30} \right) \cdot 20 = 40 + \left( \frac{25}{30} \right) \cdot 20 = 40 + 16.667 = \mathbf{56.667}$$

**b) $IQR$ & Fences:**
$$IQR = Q_3 - Q_1 = 56.667 - 25.714 = \mathbf{30.953}$$
*   Lower Inner Fence $= Q_1 - 1.5(IQR) = 25.714 - 1.5(30.953) = 25.714 - 46.430 = \mathbf{-20.716}$
*   Upper Inner Fence $= Q_3 + 1.5(IQR) = 56.667 + 46.430 = \mathbf{103.097}$

**c) Five-Number Summary:**
$\text{Min} = 0, Q_1 = \mathbf{25.714}, Q_2 = \mathbf{40.000}, Q_3 = \mathbf{56.667}, \text{Max} = 80$.

**Final Answer:** $Q_1 = \mathbf{25.714}, Q_2 = \mathbf{40.000}, Q_3 = \mathbf{56.667}, IQR = \mathbf{30.953}$; Fences $= [\mathbf{-20.716}, \mathbf{103.097}]$.

#### Exercise 19: SLA Service Latency Percentile Computation (Time-Domain)
**Problem:** Latency log of 20 API calls (in ms): `10, 12, 14, 15, 16, 18, 20, 22, 25, 28, 30, 32, 35, 40, 45, 50, 60, 80, 120, 250`. Find SLA compliance metrics **p50, p90, p95**.

**Solution:**
Ordered sample $n=20$.
1.  **p50 ($P_{50}$):** Position $= \frac{50(20+1)}{100} = 10.5$.
    $$p50 = \frac{x_{(10)} + x_{(11)}}{2} = \frac{28 + 30}{2} = \mathbf{29.0\text{ ms}}$$
2.  **p90 ($P_{90}$):** Position $= \frac{90(20+1)}{100} = 18.9$.
    $$p90 = x_{(18)} + 0.9(x_{(19)} - x_{(18)}) = 80 + 0.9(120 - 80) = 80 + 36 = \mathbf{116.0\text{ ms}}$$
3.  **p95 ($P_{95}$):** Position $= \frac{95(20+1)}{100} = 19.95$.
    $$p95 = x_{(19)} + 0.95(x_{(20)} - x_{(19)}) = 120 + 0.95(250 - 120) = 120 + 0.95(130) = 120 + 123.5 = \mathbf{243.5\text{ ms}}$$

**Final Answer:** $\text{p50} = \mathbf{29.0\text{ ms}}, \text{p90} = \mathbf{116.0\text{ ms}}, \text{p95} = \mathbf{243.5\text{ ms}}$.

#### Exercise 20: Grouped Quantiles and SLA Latency Profile (Time-Domain)
**Problem:** For $n=500$ server response durations binned into intervals:

| Interval (ms) | $f_i$ | $F_i$ |
| :--- | :--- | :--- |
| $[0, 100)$ | 300 | 300 |
| $[100, 200)$ | 150 | 450 |
| $[200, 300]$ | 50 | 500 |

Calculate interpolated **p90** ($P_{90}$) in ms. Write an R command to extract quantiles directly.

**Solution:**
1.  **Position for p90:** $\frac{90 \cdot 500}{100} = 450$.
    Class $[100, 200)\text{ ms}$ has $F_2 = 450 \ge 450$. Thus, class $[100, 200)\text{ ms}$ contains p90.
    $L_q = 100, w = 100, f_q = 150, F_{q-1} = 300$.
    $$\text{p90} = 100 + \left( \frac{450 - 300}{150} \right) \cdot 100 = 100 + \left( \frac{150}{150} \right) \cdot 100 = 100 + 100 = \mathbf{200.00\text{ ms}}$$

2.  **R Code:**
```r
# R command for quantile extraction
quantile(latency_vector, probs = 0.90)
```

**Final Answer:** $\text{p90} = \mathbf{200.00\text{ ms}}$. Exactly $90\%$ of requests finish in $\le 200\text{ ms}$.

#### Exercise 21: Unit Conversion Impact on Quantiles and Percentile Ranks (Time-Domain)
**Problem:** An SLA audit reports $P_{95} = 4,500,000\text{ ns}$ for database query latencies.
**a)** Convert $P_{95}$ to milliseconds.
**b)** Does the percentile rank ($95$) change after unit conversion? Explain.

**Solution:**
**a) Convert to ms:**
$$P_{95, [ms]} = \frac{4,500,000\text{ ns}}{1,000,000\text{ ns/ms}} = \mathbf{4.5\text{ ms}}$$

**b) Percentile Rank Impact:**
No. Monotonic linear scaling ($x_{ms} = x_{ns} / 10^6$) preserves relative order completely. The percentile rank remains **95th percentile**.

**Final Answer:** $P_{95} = \mathbf{4.5\text{ ms}}$; percentile rank remains **95**.

### R Implementation
```r
# Section 1.3: Measures of Position & Boxplots in R
latency_ms <- c(10, 12, 14, 15, 16, 18, 20, 22, 25, 28, 30, 32, 35, 40, 45, 50, 60, 80, 120, 250)

# SLA Percentiles
sla_metrics <- quantile(latency_ms, probs = c(0.50, 0.90, 0.95, 0.99))
print(sla_metrics)

# Five-number summary and boxplot stats
fivenum_summary <- fivenum(latency_ms)
cat("Five-number summary:", fivenum_summary, "\n")
boxplot.stats(latency_ms)$out # Outliers
```

---

## Section 1.4: Measures of Dispersion & Data Transformations

### Core Theory & Definitions
Measures of dispersion quantify the variability, spread, or instability within a dataset around its central value.

1.  **Range ($R$):** The total distance between maximum and minimum values ($R = x_{max} - x_{min}$).
2.  **Sample Variance ($s^2$):** The average squared deviation from the sample mean $\bar{x}$, using Bessel's correction ($n-1$) to provide an unbiased estimator of population variance $\sigma^2$.
3.  **Sample Standard Deviation ($s$):** The square root of sample variance ($s = \sqrt{s^2}$). It restores the metric to original physical units.
4.  **Population Variance ($\sigma^2$) and Standard Deviation ($\sigma$):** Computed dividing by total population size $N$.
5.  **Coefficient of Variation ($CV$):** A dimensionless measure of relative variability expressed as a percentage:
    $$CV = \frac{s}{\bar{x}} \cdot 100\%$$

#### Data Transformations & Linear Properties
When a linear transformation $Y = aX + b$ is applied to random variable $X$:
*   $\bar{y} = a\bar{x} + b$
*   $s_y = |a| s_x$
*   $s_y^2 = a^2 s_x^2$
*(Note: Shifting by constant $b$ changes central location but leaves dispersion completely unchanged).*

#### The $c^2$ Rule for Unit Conversions
When converting measurements by constant factor $c$ ($X_{\text{new}} = c \cdot X_{\text{old}}$):
*   Mean: $\bar{x}_{\text{new}} = c \cdot \bar{x}_{\text{old}}$
*   Standard Deviation: $s_{\text{new}} = c \cdot s_{\text{old}}$
*   **Variance ($c^2$ Rule):** $s^2_{\text{new}} = c^2 \cdot s^2_{\text{old}}$
*   Coefficient of Variation: $CV_{\text{new}} = CV_{\text{old}}$ (Invariant under unit scale conversion).

> **Practical / Time-Domain Note:**
> **Gotcha (The $c^2$ Rule):** When scaling latency data from seconds to milliseconds ($c = 1000$), standard deviation increases by $10^3$, but variance increases by $c^2 = 10^6$! For example, $s^2 = 0.04\text{ s}^2 \Rightarrow s^2 = 40,000\text{ ms}^2$.

### Mathematical Formulas & Derivations

#### Sample Variance Formulas
*   **Ungrouped Standard Formula:**
    $$s^2 = \frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n - 1}$$
*   **Ungrouped Computational / Shortcut Formula:**
    $$s^2 = \frac{\sum_{i=1}^{n} x_i^2 - \frac{(\sum x_i)^2}{n}}{n - 1}$$
*   **Grouped Shortcut Formula:**
    $$s^2 = \frac{\sum_{i=1}^{k} f_i x_i^2 - \frac{(\sum f_i x_i)^2}{n}}{n - 1}$$

### Worked Exercises

#### Exercise 22: Sample Variance vs Population Variance Calculation
**Problem:** Small dataset: `4, 7, 10`.
**a)** Compute Sample Mean $\bar{x}$.
**b)** Calculate Sample Variance $s^2$ and Sample Standard Deviation $s$.
**c)** Calculate Population Variance $\sigma^2$ assuming this set constitutes the complete population.

**Solution:**
**a) Mean:** $\bar{x} = (4 + 7 + 10)/3 = 21/3 = \mathbf{7.00}$.
**b) Sample Variance & SD:**
Deviations $(x_i - 7)$: $-3, 0, 3$. Squared deviations: $9, 0, 9$. Sum $= 18$.
$$s^2 = \frac{18}{3 - 1} = \frac{18}{2} = \mathbf{9.00}, \quad s = \sqrt{9.00} = \mathbf{3.00}$$

**c) Population Variance:**
$$\sigma^2 = \frac{18}{N} = \frac{18}{3} = \mathbf{6.00}, \quad \sigma = \sqrt{6.00} \approx \mathbf{2.449}$$

**Final Answer:** Sample $s^2 = \mathbf{9.00}, s = \mathbf{3.00}$; Population $\sigma^2 = \mathbf{6.00}, \sigma = \mathbf{2.449}$.

#### Exercise 23: Grouped Variance, Standard Deviation & Coefficient of Variation
**Problem:** Given grouped data ($n=20$):

| Interval | $x_i$ | $f_i$ |
| :--- | :--- | :--- |
| $[0, 10)$ | 5 | 4 |
| $[10, 20)$ | 15 | 10 |
| $[20, 30]$ | 25 | 6 |

Calculate **a)** Grouped Mean $\bar{x}$, **b)** Sample Variance $s^2$ using shortcut formula, **c)** Coefficient of Variation $CV$.

**Solution:**
**a) Mean ($\bar{x}$):**
$$\sum f_i x_i = (4 \cdot 5) + (10 \cdot 15) + (6 \cdot 25) = 20 + 150 + 150 = 320$$
$$\bar{x} = \frac{320}{20} = \mathbf{16.00}$$

**b) Shortcut Sample Variance ($s^2$):**
$$\sum f_i x_i^2 = (4 \cdot 25) + (10 \cdot 225) + (6 \cdot 625) = 100 + 2250 + 3750 = 6100$$
$$s^2 = \frac{\sum f_i x_i^2 - \frac{(\sum f_i x_i)^2}{n}}{n - 1} = \frac{6100 - \frac{320^2}{20}}{19} = \frac{6100 - \frac{102400}{20}}{19} = \frac{6100 - 5120}{19} = \frac{980}{19} \approx \mathbf{51.579}$$
$$s = \sqrt{51.579} \approx \mathbf{7.182}$$

**c) Coefficient of Variation ($CV$):**
$$CV = \frac{s}{\bar{x}} \cdot 100\% = \frac{7.182}{16.00} \cdot 100\% \approx \mathbf{44.89\%}$$

**Final Answer:** $\bar{x} = \mathbf{16.00}, s^2 = \mathbf{51.579}, s = \mathbf{7.182}, CV = \mathbf{44.89\%}$.

#### Exercise 24: Linear Data Transformation Properties
**Problem:** Variable $X$ has mean $\bar{x} = 50$, variance $s_x^2 = 16$, standard deviation $s_x = 4$.
A transformed variable is defined as $Y = -3X + 25$.
Compute **a)** $\bar{y}$, **b)** $s_y$, **c)** $s_y^2$.

**Solution:**
**a) Transformed Mean ($\bar{y}$):**
$$\bar{y} = a\bar{x} + b = -3(50) + 25 = -150 + 25 = \mathbf{-125.00}$$

**b) Transformed Standard Deviation ($s_y$):**
$$s_y = |a| s_x = |-3| \cdot 4 = 3 \cdot 4 = \mathbf{12.00}$$

**c) Transformed Variance ($s_y^2$):**
$$s_y^2 = a^2 s_x^2 = (-3)^2 \cdot 16 = 9 \cdot 16 = \mathbf{144.00}$$

**Final Answer:** $\bar{y} = \mathbf{-125.00}, s_y = \mathbf{12.00}, s_y^2 = \mathbf{144.00}$.

#### Exercise 25: Applying the c^2 Rule to Latency Unit Conversions (Time-Domain)
**Problem:** A latency dataset measured in seconds has mean $\bar{x} = 0.050\text{ s}$, standard deviation $s = 0.012\text{ s}$, and variance $s^2 = 0.000144\text{ s}^2$.
Convert the dataset to milliseconds ($c = 1000\text{ ms/s}$).
Compute the new mean $\bar{x}_{[ms]}$, standard deviation $s_{[ms]}$, and variance $s^2_{[ms]}$.

**Solution:**
1.  **New Mean:**
    $$\bar{x}_{[ms]} = c \cdot \bar{x} = 1000 \cdot 0.050 = \mathbf{50.00\text{ ms}}$$
2.  **New Standard Deviation:**
    $$s_{[ms]} = c \cdot s = 1000 \cdot 0.012 = \mathbf{12.00\text{ ms}}$$
3.  **New Variance ($c^2$ Rule):**
    $$s^2_{[ms]} = c^2 \cdot s^2 = (1000)^2 \cdot 0.000144 = 1,000,000 \cdot 0.000144 = \mathbf{144.00\text{ ms}^2}$$

**Final Answer:** $\bar{x}_{[ms]} = \mathbf{50.00\text{ ms}}, s_{[ms]} = \mathbf{12.00\text{ ms}}, s^2_{[ms]} = \mathbf{144.00\text{ ms}^2}$.

#### Exercise 26: Outlier Detection using 1.5 IQR Rule on Execution Times (Time-Domain)
**Problem:** Execution times (in ms) yield $Q_1 = 120\text{ ms}$ and $Q_3 = 180\text{ ms}$.
Evaluate whether latencies of $20\text{ ms}$ and $280\text{ ms}$ are statistical outliers under the $1.5 \cdot IQR$ rule.

**Solution:**
1.  **Compute $IQR$:**
    $$IQR = Q_3 - Q_1 = 180 - 120 = 60\text{ ms}$$
2.  **Compute Fences:**
    *   Lower Inner Fence $= Q_1 - 1.5(IQR) = 120 - 1.5(60) = 120 - 90 = \mathbf{30\text{ ms}}$
    *   Upper Inner Fence $= Q_3 + 1.5(IQR) = 180 + 1.5(60) = 180 + 90 = \mathbf{270\text{ ms}}$
3.  **Evaluate Points:**
    *   Measurement $20\text{ ms} < 30\text{ ms}$ (Below lower fence) $\Rightarrow$ **Outlier**.
    *   Measurement $280\text{ ms} > 270\text{ ms}$ (Above upper fence) $\Rightarrow$ **Outlier**.

**Final Answer:** Both $20\text{ ms}$ and $280\text{ ms}$ fall outside $[30\text{ ms}, 270\text{ ms}]$ and are confirmed **Outliers**.

---

### Combined Exercises (Exercises 27–30)

#### Exercise 27: Multi-Metric Analysis of Manufacturing Output (Combined, Moderate)
**Problem:** A factory quality control process collects 20 daily output counts: `102, 105, 108, 110, 112, 115, 115, 118, 120, 120, 122, 125, 128, 130, 132, 135, 138, 140, 145, 190`.
**a)** Compute the Mean, Median, and Mode.
**b)** Compute the $IQR$ and identify any outliers via the 1.5 IQR rule.
**c)** Compute Sample Variance $s^2$ and Standard Deviation $s$.
**d)** If a linear calibration adjustment $Y = 1.1X - 5$ is applied, find the new mean $\bar{y}$ and standard deviation $s_y$.

**Solution:**
**a) Central Tendency:**
*   $\bar{x} = \frac{2530}{20} = \mathbf{126.50}$
*   $n=20$ (even): $M_e = \frac{x_{(10)} + x_{(11)}}{2} = \frac{120 + 122}{2} = \mathbf{121.00}$
*   Modes: Values `115, 120` both appear twice. Modes = $\mathbf{115, 120}$.

**b) Position & Outliers:**
*   $Q_1$ (5.25th position) $= x_{(5)} + 0.25(x_{(6)} - x_{(5)}) = 112 + 0.25(115 - 112) = \mathbf{112.75}$
*   $Q_3$ (15.75th position) $= x_{(15)} + 0.75(x_{(16)} - x_{(15)}) = 132 + 0.75(135 - 132) = \mathbf{134.25}$
*   $IQR = 134.25 - 112.75 = \mathbf{21.50}$
*   Fences: $[112.75 - 1.5(21.50), 134.25 + 1.5(21.50)] = [112.75 - 32.25, 134.25 + 32.25] = [\mathbf{80.50}, \mathbf{166.50}]$
*   Value $190 > 166.50$ is an **Outlier**.

**c) Variance & Standard Deviation:**
$\sum x_i = 2530, \sum x_i^2 = 327,614$.
$$s^2 = \frac{327,614 - \frac{2530^2}{20}}{19} = \frac{327,614 - 320,045}{19} = \frac{7569}{19} \approx \mathbf{398.368}$$
$$s = \sqrt{398.368} \approx \mathbf{19.959}$$

**d) Linear Transformation ($Y = 1.1X - 5$):**
*   $\bar{y} = 1.1(126.50) - 5 = 139.15 - 5 = \mathbf{134.15}$
*   $s_y = 1.1(19.959) = \mathbf{21.955}$

**Final Answer:**
**a)** Mean $= \mathbf{126.50}$, Median $= \mathbf{121.00}$, Modes $= \mathbf{115, 120}$.
**b)** $IQR = \mathbf{21.50}$, Outlier $= \mathbf{190}$.
**c)** $s^2 = \mathbf{398.368}, s = \mathbf{19.959}$.
**d)** $\bar{y} = \mathbf{134.15}, s_y = \mathbf{21.955}$.

#### Exercise 28: Complex Survey & Grouped Data Audit with Missing Values (Combined, Harder)
**Problem:** An incomplete grouped frequency distribution of $n=50$ survey responses is provided:

| Interval | $x_i$ | $f_i$ | $f_i x_i$ | $f_i x_i^2$ |
| :--- | :--- | :--- | :--- | :--- |
| $[10, 20)$ | 15 | 10 | 150 | 2250 |
| $[20, 30)$ | 25 | $f_2 = ?$ | ? | ? |
| $[30, 40)$ | 35 | 15 | 525 | 18375 |
| $[40, 50]$ | 45 | 5 | 225 | 10125 |

**a)** Determine the missing frequency $f_2$.
**b)** Calculate the Grouped Mean $\bar{x}$ and Grouped Median $M_e$.
**c)** Calculate the Sample Variance $s^2$ and Coefficient of Variation $CV$.
**d)** Calculate Pearson's second skewness coefficient $SK_2$.

**Solution:**
**a) Missing Frequency $f_2$:**
$$\sum f_i = 10 + f_2 + 15 + 5 = 50 \Rightarrow 30 + f_2 = 50 \Rightarrow f_2 = \mathbf{20}$$

**b) Grouped Mean & Median:**
*   $f_2 x_2 = 20 \cdot 25 = 500$, $f_2 x_2^2 = 20 \cdot 625 = 12500$.
*   $\sum f_i x_i = 150 + 500 + 525 + 225 = 1400$
    $$\bar{x} = \frac{1400}{50} = \mathbf{28.00}$$
*   Position $n/2 = 25$. $F_1 = 10, F_2 = 30 \ge 25$. Median class is $[20, 30)$.
    $$M_e = 20 + \left( \frac{25 - 10}{20} \right) \cdot 10 = 20 + \left( \frac{15}{20} \right) \cdot 10 = 20 + 7.5 = \mathbf{27.50}$$

**c) Sample Variance & $CV$:**
$\sum f_i x_i^2 = 2250 + 12500 + 18375 + 10125 = 43250$.
$$s^2 = \frac{43250 - \frac{1400^2}{50}}{49} = \frac{43250 - \frac{1960000}{50}}{49} = \frac{43250 - 39200}{49} = \frac{4050}{49} \approx \mathbf{82.653}$$
$$s = \sqrt{82.653} \approx \mathbf{9.091}$$
$$CV = \frac{9.091}{28.00} \cdot 100\% \approx \mathbf{32.47\%}$$

**d) Pearson's Skewness ($SK_2$):**
$$SK_2 = \frac{3(\bar{x} - M_e)}{s} = \frac{3(28.00 - 27.50)}{9.091} = \frac{1.50}{9.091} \approx \mathbf{0.1650}$$

**Final Answer:**
**a)** $f_2 = \mathbf{20}$.
**b)** Mean $\bar{x} = \mathbf{28.00}$, Median $M_e = \mathbf{27.50}$.
**c)** $s^2 = \mathbf{82.653}, CV = \mathbf{32.47\%}$.
**d)** $SK_2 = \mathbf{0.1650}$ (Slight positive skewness).

#### Exercise 29: Complete System SLA Latency Audit & Unit Conversion (Combined, Hard) (Time-Domain)
**Problem:** A system performance team logs $n=200$ query response times (in seconds). The binned frequency data are:

| Interval (s) | Midpoint $x_i$ (s) | $f_i$ | $F_i$ |
| :--- | :--- | :--- | :--- |
| $[0.00, 0.10)$ | 0.05 | 120 | 120 |
| $[0.10, 0.20)$ | 0.15 | 50 | 170 |
| $[0.20, 0.30)$ | 0.25 | 20 | 190 |
| $[0.30, 0.40]$ | 0.35 | 10 | 200 |

**a)** Compute the Grouped Mean $\bar{x}_{[s]}$ and interpolated **p95** percentile ($P_{95}$) in seconds.
**b)** Compute the Sample Variance $s^2_{[s]}$ and Standard Deviation $s_{[s]}$ in seconds.
**c)** Convert all results ($\bar{x}, P_{95}, s, s^2$) to milliseconds ($c = 1000\text{ ms/s}$), applying the $c^2$ rule for variance.
**d)** Write an R command script to compute the grouped mean and standard deviation from these frequencies.

**Solution:**
**a) Grouped Mean & p95 in Seconds:**
*   $\sum f_i x_i = (120 \cdot 0.05) + (50 \cdot 0.15) + (20 \cdot 0.25) + (10 \cdot 0.35) = 6.0 + 7.5 + 5.0 + 3.5 = 22.0\text{ s}$
    $$\bar{x}_{[s]} = \frac{22.0}{200} = \mathbf{0.110\text{ s}}$$
*   **p95 Position:** $\frac{95 \cdot 200}{100} = 190$.
    Looking at $F_i$, Class 3 $[0.20, 0.30)\text{ s}$ has $F_3 = 190 \ge 190$.
    $L_q = 0.20, w = 0.10, f_q = 20, F_{q-1} = 170$.
    $$P_{95, [s]} = 0.20 + \left( \frac{190 - 170}{20} \right) \cdot 0.10 = 0.20 + \left( \frac{20}{20} \right) \cdot 0.10 = 0.20 + 0.10 = \mathbf{0.300\text{ s}}$$

**b) Variance & Standard Deviation in Seconds:**
*   $\sum f_i x_i^2 = (120 \cdot 0.0025) + (50 \cdot 0.0225) + (20 \cdot 0.0625) + (10 \cdot 0.1225) = 0.30 + 1.125 + 1.25 + 1.225 = 3.90\text{ s}^2$
    $$s^2_{[s]} = \frac{3.90 - \frac{22.0^2}{200}}{199} = \frac{3.90 - \frac{484.0}{200}}{199} = \frac{3.90 - 2.42}{199} = \frac{1.48}{199} \approx \mathbf{0.007437\text{ s}^2}$$
    $$s_{[s]} = \sqrt{0.007437} \approx \mathbf{0.08624\text{ s}}$$

**c) Unit Conversion to Milliseconds ($c = 1000$):**
*   $\bar{x}_{[ms]} = 1000 \cdot 0.110 = \mathbf{110.00\text{ ms}}$
*   $P_{95, [ms]} = 1000 \cdot 0.300 = \mathbf{300.00\text{ ms}}$
*   $s_{[ms]} = 1000 \cdot 0.08624 = \mathbf{86.24\text{ ms}}$
*   **$c^2$ Variance Scaling:**
    $$s^2_{[ms]} = c^2 \cdot s^2_{[s]} = (1000)^2 \cdot 0.007437 = 1,000,000 \cdot 0.007437 = \mathbf{7,437.00\text{ ms}^2}$$

**d) R Script:**
```r
# R execution script for grouped SLA audit
midpoints <- c(0.05, 0.15, 0.25, 0.35)
freqs <- c(120, 50, 20, 10)
n <- sum(freqs)

mean_s <- sum(freqs * midpoints) / n
var_s <- (sum(freqs * midpoints^2) - n * mean_s^2) / (n - 1)
sd_ms <- sqrt(var_s) * 1000
var_ms <- var_s * (1000^2)

cat("Mean (ms):", mean_s * 1000, "\nSD (ms):", sd_ms, "\nVar (ms^2):", var_ms, "\n")
```

**Final Answer:**
**a)** $\bar{x} = \mathbf{0.110\text{ s}}, P_{95} = \mathbf{0.300\text{ s}}$.
**b)** $s^2 = \mathbf{0.007437\text{ s}^2}, s = \mathbf{0.08624\text{ s}}$.
**c)** In ms: $\bar{x} = \mathbf{110.00\text{ ms}}, P_{95} = \mathbf{300.00\text{ ms}}, s = \mathbf{86.24\text{ ms}}, s^2 = \mathbf{7,437.00\text{ ms}^2}$.

#### Exercise 30: Distributed Microservice Execution & Clock Sync Audit (Combined, Hardest + Gotcha) (Time-Domain)
**Problem:** A distributed system audit measures daily synchronization times (recorded near midnight) and process execution latencies across 4 microservice nodes.
**Part 1 (Clock Sync):** Nodes report scheduled trigger times: $23.8\text{h}, 23.9\text{h}, 0.1\text{h}, 0.2\text{h}$.
**a)** Calculate the true Circular Mean execution time $\bar{t}_{\text{circular}}$.
**Part 2 (Latency Audit):** Process execution latencies (in seconds) for $n=10$ tasks are: `0.010, 0.012, 0.015, 0.018, 0.020, 0.022, 0.025, 0.028, 0.030, 0.500`.
**b)** Compute the Sample Mean $\bar{x}_{[s]}$ and Median $M_{e, [s]}$.
**c)** Compute Sample Variance $s^2_{[s]}$ in seconds.
**d)** Convert the variance to milliseconds squared ($s^2_{[ms]}$).
**e)** Identify the deliberate "Gotcha" pitfalls in this audit and explain how to prevent them.

**Solution:**
**a) Part 1: Circular Mean:**
Times $t_i \in \{23.8, 23.9, 0.1, 0.2\}$.
Convert to angles $\theta_i = \frac{2\pi \cdot t_i}{24}$:
*   $\theta_1 = \frac{47.6\pi}{24} \approx 6.2308 \text{ rad} \Rightarrow \sin\theta_1 \approx -0.0523, \cos\theta_1 \approx 0.9986$
*   $\theta_2 = \frac{47.8\pi}{24} \approx 6.2570 \text{ rad} \Rightarrow \sin\theta_2 \approx -0.0262, \cos\theta_2 \approx 0.9997$
*   $\theta_3 = \frac{0.2\pi}{24} \approx 0.0262 \text{ rad} \Rightarrow \sin\theta_3 \approx 0.0262, \cos\theta_3 \approx 0.9997$
*   $\theta_4 = \frac{0.4\pi}{24} \approx 0.0524 \text{ rad} \Rightarrow \sin\theta_4 \approx 0.0523, \cos\theta_4 \approx 0.9986$

Sum components:
$$\sum \sin\theta_i = 0.0000, \quad \sum \cos\theta_i = 3.9966$$
$$\bar{\theta} = \text{atan2}(0.0000, 3.9966) = 0.0000 \text{ rad}$$
$$\bar{t}_{\text{circular}} = \frac{24 \cdot 0.0000}{2\pi} = \mathbf{0.00\text{h}} \quad (00:00 \text{ Midnight})$$

**b) Part 2: Mean & Median:**
*   $\sum x_i = 0.670\text{ s} \Rightarrow \bar{x}_{[s]} = \frac{0.670}{10} = \mathbf{0.0670\text{ s}} \quad (67.0\text{ ms})$
*   Ordered sample ($n=10$, even): $M_{e, [s]} = \frac{x_{(5)} + x_{(6)}}{2} = \frac{0.020 + 0.022}{2} = \mathbf{0.0210\text{ s}} \quad (21.0\text{ ms})$

**c) Part 2: Sample Variance in $s^2$:**
$\sum x_i^2 = (0.010^2 + \dots + 0.030^2) + 0.500^2 = 0.003626 + 0.250000 = 0.253626\text{ s}^2$.
$$s^2_{[s]} = \frac{0.253626 - \frac{0.670^2}{10}}{9} = \frac{0.253626 - 0.044890}{9} = \frac{0.208736}{9} \approx \mathbf{0.023193\text{ s}^2}$$

**d) Part 2: Convert Variance to $\text{ms}^2$ ($c^2$ Rule):**
$$s^2_{[ms]} = (1000)^2 \cdot s^2_{[s]} = 1,000,000 \cdot 0.023193 = \mathbf{23,193.00\text{ ms}^2}$$

**e) Gotcha Moment Analysis:**
> **Gotcha:**
> 1.  **Gotcha 1 (Naive Clock Mean Trap):** Taking the naive arithmetic mean of $23.8, 23.9, 0.1, 0.2$ gives $\bar{t}_{\text{naive}} = 12.0\text{h}$ (Noon), misinterpreting midnight tasks as occurring in mid-day. The Circular Mean correct answer is **00:00 Midnight**.
> 2.  **Gotcha 2 (Linear Variance Scaling Trap):** Multiplying variance by $c = 1000$ instead of $c^2 = 1,000,000$ when converting seconds to milliseconds. The correct variance is $23,193.00\text{ ms}^2$, NOT $23.193\text{ ms}^2$.
> 3.  **Gotcha 3 (Mean Inflation by Outlier):** Reporting mean latency ($67\text{ ms}$) as typical performance when $90\%$ of tasks finish in $\le 30\text{ ms}$. Median ($21\text{ ms}$) must be used.

**Final Answer:**
**a)** Circular Mean $= \mathbf{0.00\text{h}}$ (Midnight).
**b)** Mean $= \mathbf{0.0670\text{ s}}$, Median $= \mathbf{0.0210\text{ s}}$.
**c)** $s^2 = \mathbf{0.023193\text{ s}^2}$.
**d)** $s^2_{[ms]} = \mathbf{23,193.00\text{ ms}^2}$.
**e)** Gotchas documented and resolved.

### R Implementation
```r
# Section 1.4: Dispersion, Transformations & Gotchas in R
# Gotcha verification: c^2 variance scaling
s2_sec <- 0.023193
c_factor <- 1000

s2_ms <- (c_factor^2) * s2_sec
cat("Correct Variance in ms^2:", s2_ms, "\n")

# Transformation Y = 1.1X - 5
x <- c(102, 105, 108, 110, 112, 115, 115, 118, 120, 120, 122, 125, 128, 130, 132, 135, 138, 140, 145, 190)
y <- 1.1 * x - 5

cat("Mean Y:", mean(y), "\nSD Y:", sd(y), "\n")
```

---

## Exam Preparation Guide

### Formula Quick-Reference

| Topic | General Formula | Time-Domain Adapted Formula | Typologio / Exam Style |
| :--- | :--- | :--- | :--- |
| **Class Mark** | $x_i = \frac{L_i + U_i}{2}$ | $x_{i, [s]} = \frac{L_{i, [s]} + U_{i, [s]}}{2}$ | $x_i = \frac{L_i + U_i}{2}$ |
| **Relative Freq.** | $h_i = \frac{f_i}{n}$ | $h_i = \frac{f_i}{n}$ | $h_i = f_i / n$ |
| **Sturges' Rule** | $k = 1 + 3.322 \log_{10}(n)$ | $k = 1 + 3.322 \log_{10}(n)$ | $k = 1 + 3.322 \log_{10} n$ |
| **Grouped Mean** | $\bar{x} = \frac{\sum f_i x_i}{n}$ | $\bar{x}_{[s]} = \frac{\sum f_i x_{i, [s]}}{n}$ | $\bar{x} = \frac{\sum f_i x_i}{n}$ |
| **Grouped Median** | $M_e = L_m + \left( \frac{\frac{n}{2} - F_{m-1}}{f_m} \right) w$ | $M_{e, [s]} = L_{m, [s]} + \left( \frac{\frac{n}{2} - F_{m-1}}{f_m} \right) w_{[s]}$ | $M_e = L + \frac{n/2 - F_{i-1}}{f_i} \cdot w$ |
| **Grouped Mode** | $M_o = L_o + \left( \frac{f_o - f_{o-1}}{(f_o - f_{o-1}) + (f_o - f_{o+1})} \right) w$ | $M_{o, [s]} = L_{o, [s]} + \left( \frac{f_o - f_{o-1}}{(f_o - f_{o-1}) + (f_o - f_{o+1})} \right) w_{[s]}$ | $M_o = L + \frac{\Delta_1}{\Delta_1 + \Delta_2} \cdot w$ |
| **Grouped Percentile** | $P_k = L_q + \left( \frac{\frac{k \cdot n}{100} - F_{q-1}}{f_q} \right) w$ | $P_{k, [s]} = L_{q, [s]} + \left( \frac{\frac{k \cdot n}{100} - F_{q-1}}{f_q} \right) w_{[s]}$ | $P_k = L + \frac{\frac{kn}{100} - F_{i-1}}{f_i} \cdot w$ |
| **Sample Variance** | $s^2 = \frac{\sum f_i x_i^2 - \frac{(\sum f_i x_i)^2}{n}}{n - 1}$ | $s^2_{[s]} = \frac{\sum f_i x_{i, [s]}^2 - \frac{(\sum f_i x_{i, [s]})^2}{n}}{n - 1}$ | $s^2 = \frac{\sum f_i x_i^2 - n\bar{x}^2}{n - 1}$ |
| **$c^2$ Variance Scaling** | $s^2_y = a^2 s^2_x$ | $s^2_{[ms]} = c^2 \cdot s^2_{[s]}$ | $s^2_{new} = c^2 s^2_{old}$ |
| **Coef. of Variation** | $CV = \frac{s}{\bar{x}} \cdot 100\%$ | $CV = \frac{s_{[s]}}{\bar{x}_{[s]}} \cdot 100\%$ | $CV = \frac{s}{\bar{x}} \cdot 100\%$ |
| **Circular Mean** | $\bar{\theta} = \text{atan2}(\bar{S}, \bar{C})$ | $\bar{t} = \frac{24 \cdot \text{atan2}(\sum \sin\theta_i, \sum \cos\theta_i)}{2\pi}$ | N/A (Systems application) |

---

### Exam Checklist

| Category | Items |
| :--- | :--- |
| **Must Memorize** | - Sturges' Rule formula: $k = 1 + 3.322 \log_{10}(n)$<br>- Grouped Median and Mode interpolation formulas<br>- Grouped Variance shortcut formula ($n-1$ denominator)<br>- The $c^2$ Rule for variance unit conversions ($s^2_{\text{new}} = c^2 s^2_{\text{old}}$)<br>- 1.5 IQR Outlier Fences: $[Q_1 - 1.5 IQR, Q_3 + 1.5 IQR]$ |
| **Must Understand** | - Resistance of Median vs. sensitivity of Mean to extreme outliers<br>- Relationship between Skewness, Mean, Median, and Mode ($SK_1, SK_2$ signs)<br>- Linear transformation properties: $Y = aX + b \Rightarrow \bar{y} = a\bar{x} + b, s_y = \|a\| s_x, s_y^2 = a^2 s_x^2$<br>- Physical distinction between sample variance $s^2$ (unbiased, $n-1$) and population variance $\sigma^2$ ($N$) |
| **Book-Only (Professor May Test)** | - **Circular Mean for Cyclic Clock Times:** Mathematical failure of naive arithmetic mean on 24h clock values<br>- **Epoch Timestamp Centering:** Loss of floating-point precision when binning $1.7 \times 10^{12}\text{ ms}$ timestamps<br>- **Pearson's Skewness Coefficients:** Explicit formula calculations for $SK_1$ and $SK_2$<br>- **Decile Interpolation:** Calculating $D_k$ using $N_{parts} = 10$ |

---

### Common Exam Traps

1.  **Bessel's Correction Error ($n$ vs $n-1$):**
    *   *Trap:* Using $n$ in the denominator when calculating sample variance $s^2$.
    *   *Fix:* Always divide by $n-1$ for sample variance $s^2$. Only divide by $N$ if explicitly asked for population variance $\sigma^2$.
2.  **Linear Variance Scaling Trap ($c$ vs $c^2$):**
    *   *Trap:* Multiplying variance by $c$ when converting measurement units (e.g. multiplying variance in seconds by 1000 to get variance in ms).
    *   *Fix:* Standard deviation scales by $c$, but variance scales by $c^2 = 1000^2 = 1,000,000$.
3.  **Circular Clock Time Trap:**
    *   *Trap:* Computing arithmetic mean on times like 23:30 and 00:30 and getting 12:00.
    *   *Fix:* Recognize cyclic metrics and apply circular trigonometric averaging ($\bar{S}, \bar{C}$).
4.  **Percentile Rank vs Percentile Value Confusion:**
    *   *Trap:* Confusing the position rank (e.g., $95$th percentile) with the physical value (e.g., $240\text{ ms}$).
    *   *Fix:* Position rank is a percentage location ($0-100\%$), while percentile value carries physical metric units.
5.  **Cumulative Frequency Indexing ($F_{i-1}$):**
    *   *Trap:* Plugging the cumulative frequency of the *current* class $F_i$ into the median/quantile interpolation formula instead of the *preceding* class $F_{i-1}$.
    *   *Fix:* Double check that $F_{i-1}$ strictly represents cumulative frequency *before* the target quantile class.

---

### Exam Paper Cross-References

| Exam Paper | Relevant Questions | Difficulty |
| :--- | :--- | :---: |
| [Exam_paper_Easy.md](../../Exams/Papers/synthetic/Exam_paper_Easy.md) | Question 1 (Ungrouped stats, mean, median, sample variance) | **1/5** |
| [Exam_paper_2024_09_06_Team_A.md](../../Exams/Papers/Exam_paper_2024_09_06_Team_A.md) | Question 1 (Ungrouped data table, mean, variance, standard deviation) | **1/5** |
| [Exam_paper_Intermediate_1.md](../../Exams/Papers/synthetic/Exam_paper_Intermediate_1.md) | Question 1 (Grouped frequency table, Sturges' rule, grouped mean, interpolated median) | **2/5** |
| [Exam_paper_2023_06_12_Team_null.md](../../Exams/Papers/Exam_paper_2023_06_12_Team_null.md) | Question 1 (Grouped frequency distribution, grouped variance, mode calculation) | **2/5** |
| [Exam_paper_2024_06_14_Team_B.md](../../Exams/Papers/Exam_paper_2024_06_14_Team_B.md) | Question 1 (5-class grouped frequency table, grouped mean and variance) | **2/5** |
| [Exam_paper_2026_06_09_Team_B.md](../../Exams/Papers/Exam_paper_2026_06_09_Team_B.md) | Question 1 (Grouped frequency table, percentile interpolation) | **2/5** |
| [Exam_paper_Hard_1.md](../../Exams/Papers/synthetic/Exam_paper_Hard_1.md) | Question 1 (Grouped data with missing frequency $f_i$ equation solving) | **4/5** |
| [Exam_paper_Hard_2.md](../../Exams/Papers/synthetic/Exam_paper_Hard_2.md) | Question 1 (Pooled statistics across multiple datasets, overall pooled mean and variance) | **5/5** |

---

## Phase Summary

Phase 1 provides the mathematical framework for organizing raw data and calculating core descriptive measures: Central Tendency, Position, and Dispersion.

*   **Data Organization:** Continuous data are grouped into $k$ class intervals using Sturges' Rule ($k = 1 + 3.322 \log_{10} n$). Frequency distribution tables track absolute ($f_i$), relative ($h_i$), cumulative absolute ($F_i$), and cumulative relative ($H_i$) frequencies.
*   **Central Tendency & Skewness:** Metrics include Arithmetic Mean ($\bar{x}$), Median ($M_e$), and Mode ($M_o$). While the mean represents the center of mass, it is vulnerable to extreme outliers. The median is robust and serves as the primary central metric for right-skewed latency data. Cyclic clock times require Trigonometric Circular Means. Skewness ($SK_1, SK_2$) quantifies distribution asymmetry.
*   **Position Metrics:** Quartiles ($Q_1, Q_2, Q_3$), Deciles ($D_k$), and Percentiles ($P_k$) partition ordered data. In performance engineering, SLA targets are specified via tail percentiles (p50, p90, p95, p99). The Five-Number Summary ($\text{Min}, Q_1, Q_2, Q_3, \text{Max}$) anchors Boxplot construction.
*   **Dispersion & Scale Rules:** Dispersion is measured via Range ($R$), Interquartile Range ($IQR = Q_3 - Q_1$), Sample Variance ($s^2$, dividing by $n-1$), Standard Deviation ($s$), and Coefficient of Variation ($CV$). Under linear transformations ($Y = aX + b$), mean scales as $\bar{y} = a\bar{x} + b$, standard deviation scales as $s_y = |a|s_x$, and variance scales by $a^2$. For time unit conversions ($X_{\text{new}} = c \cdot X_{\text{old}}$), the **$c^2$ Rule** dictates that variance scales by factor $c^2$, whereas standard deviation and percentiles scale by $c$.
