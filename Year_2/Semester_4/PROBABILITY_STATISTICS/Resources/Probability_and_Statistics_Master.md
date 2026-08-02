# Probability and Statistics - Master Notes

*Generated: 2026-08-02*

---

## Master Table of Contents

### Phase 1: Descriptive Statistics

- [Section 1.1: Data Organization & Frequency Tables](#section-11-data-organization-frequency-tables)
- [Section 1.2: Measures of Central Tendency & Skewness](#section-12-measures-of-central-tendency-skewness)
- [Section 1.3: Measures of Position & Boxplots](#section-13-measures-of-position-boxplots)
- [Section 1.4: Measures of Dispersion & Data Transformations](#section-14-measures-of-dispersion-data-transformations)
- [Exam Preparation Guide](#exam-preparation-guide)

### Phase 2: Probability Theory

- [Section 2.1: Set Theory & Sample Spaces](#section-21-set-theory-sample-spaces)
- [Section 2.2: Venn Diagrams & Phrase Translations](#section-22-venn-diagrams-phrase-translations)
- [Section 2.3: Probability Axioms, Rules & De Morgan's Laws](#section-23-probability-axioms-rules-de-morgans-laws)
- [Section 2.4: Combinatorics & Counting Methods](#section-24-combinatorics-counting-methods)
- [Exam Preparation Guide](#exam-preparation-guide)

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
| [Exam_paper_Easy.md](file:///home/ice/Documents/CodeHub/GitHub-Projects/Public/DitOpenNotes/Year_2/Semester_4/PROBABILITY_STATISTICS/Exams/Papers/Exam_paper_Easy.md) | Question 1 (Ungrouped stats, mean, median, sample variance) | **1/5** |
| [Exam_paper_2024_09_06_Team_A.md](file:///home/ice/Documents/CodeHub/GitHub-Projects/Public/DitOpenNotes/Year_2/Semester_4/PROBABILITY_STATISTICS/Exams/Papers/Exam_paper_2024_09_06_Team_A.md) | Question 1 (Ungrouped data table, mean, variance, standard deviation) | **1/5** |
| [Exam_paper_Intermediate_1.md](file:///home/ice/Documents/CodeHub/GitHub-Projects/Public/DitOpenNotes/Year_2/Semester_4/PROBABILITY_STATISTICS/Exams/Papers/Exam_paper_Intermediate_1.md) | Question 1 (Grouped frequency table, Sturges' rule, grouped mean, interpolated median) | **2/5** |
| [Exam_paper_2023_06_12_Team_null.md](file:///home/ice/Documents/CodeHub/GitHub-Projects/Public/DitOpenNotes/Year_2/Semester_4/PROBABILITY_STATISTICS/Exams/Papers/Exam_paper_2023_06_12_Team_null.md) | Question 1 (Grouped frequency distribution, grouped variance, mode calculation) | **2/5** |
| [Exam_paper_2024_06_14_Team_B.md](file:///home/ice/Documents/CodeHub/GitHub-Projects/Public/DitOpenNotes/Year_2/Semester_4/PROBABILITY_STATISTICS/Exams/Papers/Exam_paper_2024_06_14_Team_B.md) | Question 1 (5-class grouped frequency table, grouped mean and variance) | **2/5** |
| [Exam_paper_2026_06_09_Team_B.md](file:///home/ice/Documents/CodeHub/GitHub-Projects/Public/DitOpenNotes/Year_2/Semester_4/PROBABILITY_STATISTICS/Exams/Papers/Exam_paper_2026_06_09_Team_B.md) | Question 1 (Grouped frequency table, percentile interpolation) | **2/5** |
| [Exam_paper_Hard_1.md](file:///home/ice/Documents/CodeHub/GitHub-Projects/Public/DitOpenNotes/Year_2/Semester_4/PROBABILITY_STATISTICS/Exams/Papers/Exam_paper_Hard_1.md) | Question 1 (Grouped data with missing frequency $f_i$ equation solving) | **4/5** |
| [Exam_paper_Hard_2.md](file:///home/ice/Documents/CodeHub/GitHub-Projects/Public/DitOpenNotes/Year_2/Semester_4/PROBABILITY_STATISTICS/Exams/Papers/Exam_paper_Hard_2.md) | Question 1 (Pooled statistics across multiple datasets, overall pooled mean and variance) | **5/5** |

---

## Phase Summary

Phase 1 provides the mathematical framework for organizing raw data and calculating core descriptive measures: Central Tendency, Position, and Dispersion.

*   **Data Organization:** Continuous data are grouped into $k$ class intervals using Sturges' Rule ($k = 1 + 3.322 \log_{10} n$). Frequency distribution tables track absolute ($f_i$), relative ($h_i$), cumulative absolute ($F_i$), and cumulative relative ($H_i$) frequencies.
*   **Central Tendency & Skewness:** Metrics include Arithmetic Mean ($\bar{x}$), Median ($M_e$), and Mode ($M_o$). While the mean represents the center of mass, it is vulnerable to extreme outliers. The median is robust and serves as the primary central metric for right-skewed latency data. Cyclic clock times require Trigonometric Circular Means. Skewness ($SK_1, SK_2$) quantifies distribution asymmetry.
*   **Position Metrics:** Quartiles ($Q_1, Q_2, Q_3$), Deciles ($D_k$), and Percentiles ($P_k$) partition ordered data. In performance engineering, SLA targets are specified via tail percentiles (p50, p90, p95, p99). The Five-Number Summary ($\text{Min}, Q_1, Q_2, Q_3, \text{Max}$) anchors Boxplot construction.
*   **Dispersion & Scale Rules:** Dispersion is measured via Range ($R$), Interquartile Range ($IQR = Q_3 - Q_1$), Sample Variance ($s^2$, dividing by $n-1$), Standard Deviation ($s$), and Coefficient of Variation ($CV$). Under linear transformations ($Y = aX + b$), mean scales as $\bar{y} = a\bar{x} + b$, standard deviation scales as $s_y = |a|s_x$, and variance scales by $a^2$. For time unit conversions ($X_{\text{new}} = c \cdot X_{\text{old}}$), the **$c^2$ Rule** dictates that variance scales by factor $c^2$, whereas standard deviation and percentiles scale by $c$.

---

<!-- Source: Phases/Phase_2_Probability_Theory.md -->

# Phase 2: Probability Theory

## Table of Contents
- [Section 2.1: Set Theory & Sample Spaces](#section-21-set-theory--sample-spaces)
- [Section 2.2: Venn Diagrams & Phrase Translations](#section-22-venn-diagrams--phrase-translations)
- [Section 2.3: Probability Axioms, Rules & De Morgan's Laws](#section-23-probability-axioms-rules--de-morgans-laws)
- [Section 2.4: Combinatorics & Counting Methods](#section-24-combinatorics--counting-methods)
- [Exam Preparation Guide](#exam-preparation-guide)
- [Phase Summary](#phase-summary)

---

## Section 2.1: Set Theory & Sample Spaces

### Core Theory & Definitions

Probability Theory provides the formal mathematical framework for modeling uncertainty. Every random experiment or non-deterministic physical process begins with a precise specification of its **Sample Space** and the associated **Events**.

1.  **Sample Space ($\Omega$ or $S$):** The set of all conceivable, mutually exclusive, and collectively exhaustive outcomes of a random experiment.
    *   **Discrete Sample Space:** Contains a finite or countably infinite number of distinct elements (e.g., tossing a coin $N$ times, counting network packet retransmissions).
    *   **Continuous Sample Space:** Contains an uncountably infinite continuum of outcomes (e.g., measuring server response latency $T \in [0, \infty)$ seconds).

2.  **Event ($A \subseteq \Omega$):** Any well-defined subset of the sample space. An event occurs if the actual outcome of the experiment belongs to $A$.
    *   **Elementary (Simple) Event:** A single individual outcome $\{\omega\}$.
    *   **Compound Event:** A set containing two or more outcomes (e.g., rolling an even number $\{2, 4, 6\}$).
    *   **Impossible Event ($\emptyset$):** The empty set containing zero outcomes. Its probability is always $P(\emptyset) = 0$.
    *   **Certain Event ($\Omega$):** The entire sample space. Its probability is always $P(\Omega) = 1$.

3.  **Fundamental Set Operations:**
    *   **Union ($A \cup B$):** The set of outcomes belonging to $A$, $B$, or both. Represents the logical **OR**.
        $$A \cup B = \{\omega \in \Omega : \omega \in A \text{ or } \omega \in B\}$$
    *   **Intersection ($A \cap B$):** The set of outcomes belonging to both $A$ and $B$ simultaneously. Represents the logical **AND**.
        $$A \cap B = \{\omega \in \Omega : \omega \in A \text{ and } \omega \in B\}$$
    *   **Complement ($A'$ or $A^c$):** The set of all outcomes in $\Omega$ that do not belong to $A$. Represents the logical **NOT**.
        $$A' = \{\omega \in \Omega : \omega \notin A\}$$

4.  **Mutual Exclusivity (Disjoint Events):** Two events $A$ and $B$ are **mutually exclusive** if they cannot occur at the same time:
    $$A \cap B = \emptyset$$

> **Practical / Time-Domain Note:**
> In performance engineering and real-time systems, sample spaces often mix continuous time bounds and discrete categorical states.
> **Gotcha 1 (Point Probability in Continuous Time):** For a continuous time variable $T \in [0, \infty)\text{ s}$, the probability of measuring any exact single point timestamp is zero: $P(T = t_0) = 0$. Probabilities are defined exclusively over non-zero duration time intervals $P(t_1 \le T \le t_2)$.
> **Gotcha 2 (Mutually Exclusive Time Windows vs Independent Time Events):** If Event $A$ represents "latency $< 10\text{ ms}$" and Event $B$ represents "latency $> 100\text{ ms}$", they are mutually exclusive ($A \cap B = \emptyset$). Being mutually exclusive means they are **maximally dependent**, because if $A$ occurs, $B$ cannot possibly occur ($P(B|A) = 0$).

### Mathematical Formulas & Derivations

1.  **Fundamental Complement Identity:**
    $$A \cup A' = \Omega \quad \text{and} \quad A \cap A' = \emptyset$$
    Taking probabilities yields:
    $$P(A \cup A') = P(\Omega) \implies P(A) + P(A') = 1 \implies \boxed{P(A') = 1 - P(A)}$$

2.  **Subset Probability Monotonicity:**
    If $A \subseteq B$, then every outcome in $A$ is contained in $B$. Thus:
    $$P(A) \le P(B) \quad \text{and} \quad A \cap B = A$$

3.  **Disjoint Addition Property:**
    If events $A_1, A_2, \dots, A_k$ are pairwise disjoint ($A_i \cap A_j = \emptyset$ for $i \neq j$):
    $$P\left(\bigcup_{i=1}^k A_i\right) = \sum_{i=1}^k P(A_i)$$

> **Practical / Time-Domain Adapted Formula:**
> When continuous execution latency $T$ is bounded within a continuous sample space $\Omega = [0, T_{\max}]\text{ s}$, continuous sub-interval probabilities carry explicit time units:
> $$A = [t_1, t_2]\text{ s} \implies P(A) = P(t_1 \le T \le t_2)$$
> For uniform continuous arrival times over total duration $T_{\max}\text{ s}$:
> $$P(t_1 \le T \le t_2) = \frac{t_{2, [s]} - t_{1, [s]}}{T_{\max, [s]}}$$

### Worked Exercises

#### Exercise 1: Sample Space and Event Specification (Die Roll & Coin)
**Problem:** A fair six-sided die is rolled and a fair coin is flipped.
**a) ** Write out the sample space $\Omega$.
**b) ** Define event $A$ = "rolling a prime number and landing Heads".
**c) ** Compute $P(A)$.

**Solution:**
**a) ** Outcomes are ordered pairs $(d, c)$ where $d \in \{1, 2, 3, 4, 5, 6\}$ and $c \in \{H, T\}$:
$$\Omega = \{(1,H), (1,T), (2,H), (2,T), (3,H), (3,T), (4,H), (4,T), (5,H), (5,T), (6,H), (6,T)\}$$
Total outcomes $|\Omega| = 6 \times 2 = 12$.

**b) ** Prime die rolls are $\{2, 3, 5\}$. Thus:
$$A = \{(2,H), (3,H), (5,H)\}$$

**c) ** $|A| = 3$. Since all outcomes are equally likely:
$$P(A) = \frac{|A|}{|\Omega|} = \frac{3}{12} = \frac{1}{4} = 0.25$$

**Final Answer:** $P(A) = \mathbf{0.25}$.

#### Exercise 2: Sample Space and Event Specification (Time-Domain)
**Problem:** An automated monitoring script tracks server boot duration $T$ in seconds up to a maximum timeout of $60\text{ s}$.
**a) ** Specify the continuous sample space $\Omega$.
**b) ** Define event $A$ = "boot takes strictly between $15\text{ s}$ and $35\text{ s}$" and event $B$ = "boot takes at least $30\text{ s}$".
**c) ** Find $A \cap B$ and $A \cup B$.

**Solution:**
**a) ** Continuous time sample space:
$$\Omega = [0, 60]\text{ s}$$

**b) ** Expressing intervals:
$$A = (15, 35)\text{ s}, \quad B = [30, 60]\text{ s}$$

**c) ** Intersection and Union:
$$A \cap B = (15, 35) \cap [30, 60] = [30, 35)\text{ s}$$
$$A \cup B = (15, 35) \cup [30, 60] = (15, 60]\text{ s}$$

**Final Answer:** $A \cap B = \mathbf{[30, 35)\ s}$, $A \cup B = \mathbf{(15, 60]\ s}$.

#### Exercise 3: Operations on Discrete Events
**Problem:** Let $\Omega = \{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\}$. Let $A = \{2, 4, 6, 8, 10\}$ (evens) and $B = \{3, 6, 9\}$ (multiples of 3).
**a) ** Find $A \cup B$, $A \cap B$, $A'$, and $B'$.
**b) ** Verify that $(A \cup B)' = A' \cap B'$.

**Solution:**
**a) ** Set operations:
*   $A \cup B = \{2, 3, 4, 6, 8, 9, 10\}$
*   $A \cap B = \{6\}$
*   $A' = \{1, 3, 5, 7, 9\}$
*   $B' = \{1, 2, 4, 5, 7, 8, 10\}$

**b) ** Left-hand side:
$A \cup B = \{2, 3, 4, 6, 8, 9, 10\} \implies (A \cup B)' = \{1, 5, 7\}$
Right-hand side:
$A' \cap B' = \{1, 3, 5, 7, 9\} \cap \{1, 2, 4, 5, 7, 8, 10\} = \{1, 5, 7\}$
Both sides match identically.

**Final Answer:** Verification complete: $(A \cup B)' = A' \cap B' = \mathbf{\{1, 5, 7\}}$.

#### Exercise 4: Operations on Continuous Latency Intervals (Time-Domain)
**Problem:** In a database query benchmark with max duration $1000\text{ ms}$, let $A = [0, 250)\text{ ms}$, $B = [200, 600)\text{ ms}$, and $C = [500, 1000]\text{ ms}$.
**a) ** Compute $A \cap B$ and $B \cap C$.
**b) ** Are $A$ and $C$ mutually exclusive?
**c) ** Compute $(A \cup B \cup C)'$.

**Solution:**
**a) ** Intersections:
$$A \cap B = [0, 250) \cap [200, 600) = [200, 250)\text{ ms}$$
$$B \cap C = [200, 600) \cap [500, 1000] = [500, 600)\text{ ms}$$

**b) ** Check $A \cap C$:
$$A \cap C = [0, 250) \cap [500, 1000] = \emptyset$$
Yes, $A$ and $C$ are mutually exclusive.

**c) ** Total union:
$$A \cup B \cup C = [0, 250) \cup [200, 600) \cup [500, 1000] = [0, 1000]\text{ ms} = \Omega$$
Complement of total union:
$$(A \cup B \cup C)' = \Omega' = \mathbf{\emptyset}$$

**Final Answer:** $A \cap B = \mathbf{[200, 250)\ ms}$, $A$ and $C$ are mutually exclusive, $(A \cup B \cup C)' = \mathbf{\emptyset}$.

#### Exercise 5: Disjoint vs Intersecting Events
**Problem:** A card is drawn from a standard 52-card deck. Let $A$ = "drawing a King", $B$ = "drawing a Heart", and $C$ = "drawing a Spade".
**a) ** Are $A$ and $B$ mutually exclusive?
**b) ** Are $B$ and $C$ mutually exclusive?
**c) ** Calculate $P(A \cap B)$ and $P(B \cap C)$.

**Solution:**
**a) ** $A \cap B$ contains the King of Hearts. Thus $A \cap B \neq \emptyset \implies$ NOT mutually exclusive.
**b) ** A single card cannot be both a Heart and a Spade simultaneously. Thus $B \cap C = \emptyset \implies$ Mutually exclusive.

**c) ** Probabilities:
$$P(A \cap B) = \frac{|\text{King of Hearts}|}{52} = \frac{1}{52} \approx 0.0192$$
$$P(B \cap C) = \frac{0}{52} = 0$$

**Final Answer:** $A, B$ not disjoint; $B, C$ disjoint; $P(A \cap B) = \mathbf{1/52}$, $P(B \cap C) = \mathbf{0}$.

#### Exercise 6: Overlapping Server Maintenance & SLA Windows (Time-Domain)
**Problem:** A cloud provider schedules routine disk maintenance during interval $M = [02:00, 05:00]$ and network upgrades during interval $N = [04:00, 08:00]$ on a 24-hour clock $\Omega = [00:00, 24:00]$.
**a) ** Express intervals $M$ and $N$ in hours from midnight.
**b) ** Determine the window during which BOTH maintenance tasks occur ($M \cap N$).
**c) ** Determine the total maintenance window during which AT LEAST ONE task occurs ($M \cup N$).
**d) ** Determine the fully operational window with NO maintenance ($(M \cup N)'$).

**Solution:**
**a) ** $M = [2, 5]\text{ h}, \quad N = [4, 8]\text{ h}$.

**b) ** Both tasks active:
$$M \cap N = [2, 5] \cap [4, 8] = [4, 5]\text{ h} \quad (04:00 \text{ to } 05:00)$$

**c) ** At least one task active:
$$M \cup N = [2, 5] \cup [4, 8] = [2, 8]\text{ h} \quad (02:00 \text{ to } 08:00)$$

**d) ** No maintenance active:
$$(M \cup N)' = [0, 2) \cup (8, 24]\text{ h} \quad (00:00 \text{ to } 02:00 \text{ and } 08:00 \text{ to } 24:00)$$

**Final Answer:** Both: $\mathbf{[04:00, 05:00]}$; Any: $\mathbf{[02:00, 08:00]}$; None: $\mathbf{[00:00, 02:00) \cup (08:00, 24:00]}$.

#### Exercise 7: Multi-Slot Task Scheduling Sample Space (Time-Domain)
**Problem:** Two batch jobs $J_1$ and $J_2$ are each assigned to one of three time slots: Morning (M), Afternoon (A), or Night (N).
**a) ** List all elements of the sample space $\Omega$ as ordered pairs $(J_1, J_2)$.
**b) ** Express event $E_1$ = "both jobs run in the same time slot".
**c) ** Express event $E_2$ = "$J_1$ runs strictly before $J_2$" (assuming chronological order $M < A < N$).
**d) ** Compute $P(E_1)$ and $P(E_2)$ assuming all schedule assignments are equally likely.

**Solution:**
**a) ** $\Omega = \{(M,M), (M,A), (M,N), (A,M), (A,A), (A,N), (N,M), (N,A), (N,N)\}$. Total $|\Omega| = 3^2 = 9$.

**b) ** $E_1 = \{(M,M), (A,A), (N,N)\}$.

**c) ** $J_1 < J_2 \implies E_2 = \{(M,A), (M,N), (A,N)\}$.

**d) ** Probabilities:
$$P(E_1) = \frac{|E_1|}{|\Omega|} = \frac{3}{9} = \frac{1}{3} \approx 0.3333$$
$$P(E_2) = \frac{|E_2|}{|\Omega|} = \frac{3}{9} = \frac{1}{3} \approx 0.3333$$

**Final Answer:** $|\Omega| = \mathbf{9}$, $P(E_1) = \mathbf{1/3}$, $P(E_2) = \mathbf{1/3}$.

### R Implementation

In R, discrete sets are represented as vectors. Standard R functions perform exact set operations:

```r
# Define sample space and subsets
omega <- 1:10
A <- c(2, 4, 6, 8, 10)
B <- c(3, 6, 9)

# Set Operations
union_AB <- union(A, B)        # A u B
intersect_AB <- intersect(A, B)# A n B
comp_A <- setdiff(omega, A)    # A' (Omega \ A)
comp_B <- setdiff(omega, B)    # B'

# De Morgan's First Law Verification: (A u B)' == A' n B'
lhs <- setdiff(omega, union_AB)
rhs <- intersect(comp_A, comp_B)

cat("LHS (A u B)':", lhs, "\n")
cat("RHS A' n B':", rhs, "\n")
cat("Equal?", setequal(lhs, rhs), "\n")
```

---

## Section 2.2: Venn Diagrams & Phrase Translations

### Core Theory & Definitions

Venn Diagrams represent sample spaces visually as bounded planar regions (typically rectangles for $\Omega$) containing overlapping shapes (circles) for events. They bridge natural language problem statements and formal set-theoretic logic.

#### The 4-Region Decomposition (2 Events)
For any two events $A$ and $B$, the sample space $\Omega$ is partitioned into exactly four non-overlapping, mutually exclusive regions:

| Region Index | Set Notation | English Meaning | Systems / Latency Context |
| :---: | :--- | :--- | :--- |
| **Region 1** | $A \cap B'$ | Only $A$ occurs ($A$ without $B$) | Latency exceeds SLA, but CPU load is normal |
| **Region 2** | $A \cap B$ | Both $A$ and $B$ occur simultaneously | Latency exceeds SLA AND CPU load is high |
| **Region 3** | $A' \cap B$ | Only $B$ occurs ($B$ without $A$) | CPU load is high, but latency remains normal |
| **Region 4** | $A' \cap B'$ | Neither $A$ nor $B$ occurs | Normal latency AND normal CPU load |

```
+-------------------------------------------------------+
| Sample Space (Omega)                                  |
|   +-------------------+   +-------------------+       |
|   | Event A           |   | Event B           |       |
|   |  [Region 1]       |   |  [Region 3]       |       |
|   |  (A n B')         |   |  (A' n B)         |       |
|   |           +-------+---+-------+            |       |
|   |           |    [Region 2]    |            |       |
|   |           |     (A n B)      |            |       |
|   +-----------+------------------+------------+       |
|                                                       |
|                     [Region 4]                        |
|                     (A' n B')                         |
+-------------------------------------------------------+
```

#### The Fundamental Venn Partition Axiom
Because the four regions form a complete partition of $\Omega$:
$$\boxed{P(A \cap B') + P(A \cap B) + P(A' \cap B) + P(A' \cap B') = 1.0}$$

#### English Phrase to Set Notation Translation Matrix

| Natural Language Phrase | Set Expression | Venn Region Formula |
| :--- | :--- | :--- |
| "Event A occurs" | $A$ | $(A \cap B') \cup (A \cap B)$ |
| "Event A does not occur" | $A'$ | $(A' \cap B) \cup (A' \cap B')$ |
| "Both A and B occur" | $A \cap B$ | Region 2 |
| "At least one of A or B occurs" | $A \cup B$ | Region 1 + Region 2 + Region 3 |
| "Neither A nor B occurs" | $A' \cap B' = (A \cup B)'$ | Region 4 = $1 - P(A \cup B)$ |
| "Only A occurs" / "A but not B" | $A \cap B'$ | Region 1 = $P(A) - P(A \cap B)$ |
| "Only B occurs" / "B but not A" | $A' \cap B$ | Region 3 = $P(B) - P(A \cap B)$ |
| "Exactly one of A or B occurs" | $(A \cap B') \cup (A' \cap B)$ | Region 1 + Region 3 = $P(A \cup B) - P(A \cap B)$ |
| "At most one of A or B occurs" | $(A \cap B)' = A' \cup B'$ | Region 1 + Region 3 + Region 4 = $1 - P(A \cap B)$ |

> **Practical / Time-Domain Note:**
> When translating system requirements into Venn diagrams:
> - "High latency OR packet drop" translates to $L \cup D$.
> - "High latency WITHOUT packet drop" translates to $L \cap D'$.
> - "SLA compliance" often means NEITHER error state occurs: $L' \cap D' = (L \cup D)'$.

### Mathematical Formulas & Derivations

1.  **Only Event A Probability:**
    Since $A = (A \cap B') \cup (A \cap B)$ and these two components are disjoint:
    $$P(A) = P(A \cap B') + P(A \cap B) \implies \boxed{P(A \cap B') = P(A) - P(A \cap B)}$$

2.  **Exactly One Event Probability:**
    $$\begin{aligned}
    P(\text{Exactly One}) &= P(A \cap B') + P(A' \cap B) \\
    &= [P(A) - P(A \cap B)] + [P(B) - P(A \cap B)] \\
    &= \boxed{P(A) + P(B) - 2P(A \cap B)} = P(A \cup B) - P(A \cap B)
    \end{aligned}$$

3.  **Three-Event Venn Partition (8 Regions):**
    For events $A, B, C$, $\Omega$ splits into 8 disjoint regions:
    $$P(\Omega) = P(A \cap B' \cap C') + P(A' \cap B \cap C') + P(A' \cap B' \cap C) + P(A \cap B \cap C') + P(A \cap B' \cap C) + P(A' \cap B \cap C) + P(A \cap B \cap C) + P(A' \cap B' \cap C') = 1$$

### Worked Exercises

#### Exercise 8: 4-Region Decomposition from Survey Data
**Problem:** In a survey of 100 computer science students, 65 take Java ($J$), 45 take Python ($P$), and 20 take both Java and Python.
**a) ** Find the number of students in each of the 4 Venn regions.
**b) ** Find the probability that a randomly chosen student takes Python but not Java.

**Solution:**
**a) ** Calculate regional counts:
*   Both Java and Python ($J \cap P$): $n_2 = 20$
*   Only Java ($J \cap P'$): $n_1 = n(J) - n_2 = 65 - 20 = 45$
*   Only Python ($J' \cap P$): $n_3 = n(P) - n_2 = 45 - 20 = 25$
*   Neither ($J' \cap P'$): $n_4 = 100 - (n_1 + n_2 + n_3) = 100 - (45 + 20 + 25) = 10$

**b) ** Probability of "Only Python":
$$P(J' \cap P) = \frac{n_3}{N} = \frac{25}{100} = 0.25$$

**Final Answer:** Regions: Only J=$\mathbf{45}$, Both=$\mathbf{20}$, Only P=$\mathbf{25}$, Neither=$\mathbf{10}$. $P(\text{Only P}) = \mathbf{0.25}$.

#### Exercise 9: 4-Region Latency & Peak Load Decomposition (Time-Domain)
**Problem:** A monitoring log of 500 web requests shows that 150 experienced high latency ($L$), 200 arrived during peak traffic hours ($H$), and 350 experienced neither high latency nor peak traffic hours.
**a) ** Compute the number of requests that experienced BOTH high latency and peak traffic ($L \cap H$).
**b) ** Compute $P(L \cap H')$.

**Solution:**
**a) ** Total $N = 500$. Neither region $n(L' \cap H') = 350$.
At least one region:
$$n(L \cup H) = N - n(L' \cap H') = 500 - 350 = 150$$
Using the frequency addition rule $n(L \cup H) = n(L) + n(H) - n(L \cap H)$:
$$150 = 150 + 200 - n(L \cap H)$$
$$n(L \cap H) = 350 - 150 = 200 \implies 200\text{ requests both}.$$

**b) ** Compute "Only High Latency":
$$n(L \cap H') = n(L) - n(L \cap H) = 150 - 200$$
Wait! Notice that $n(L \cap H) = 200 > n(L) = 150$. This calculation yields a negative count ($-50$), which violates Axiom 1!
Let's check the given numbers: if $n(L)=150$ and $n(L \cup H)=150$, then since $L \subseteq L \cup H$ and $n(L)=150$, we MUST have $L \cup H = L$. Thus $H \subseteq L$, meaning $n(H)$ cannot exceed 150. But $n(H)=200$, which is impossible!
Therefore, the log data is **inconsistent with probability axioms**.

**Final Answer:** The given parameters ($n(L)=150, n(H)=200, n(\text{Neither})=350$) are **mathematically inconsistent** because they imply $n(L \cap H) = \mathbf{200} > n(L)$, violating Kolmogorov's First Axiom.

#### Exercise 10: Multi-Part Phrase Translation & Region Mapping
**Problem:** Two independent automated tests $T_1$ and $T_2$ are run. $P(T_1) = 0.40$, $P(T_2) = 0.30$, and $P(T_1 \cap T_2) = 0.12$. Express the following phrases in set notation and calculate their probabilities:
**a) ** "At least one test passes"
**b) ** "Neither test passes"
**c) ** "Exactly one test passes"
**d) ** "At most one test passes"

**Solution:**
**a) ** "At least one": $T_1 \cup T_2$
$$P(T_1 \cup T_2) = P(T_1) + P(T_2) - P(T_1 \cap T_2) = 0.40 + 0.30 - 0.12 = 0.58$$

**b) ** "Neither": $T_1' \cap T_2' = (T_1 \cup T_2)'$
$$P(T_1' \cap T_2') = 1 - P(T_1 \cup T_2) = 1 - 0.58 = 0.42$$

**c) ** "Exactly one": $(T_1 \cap T_2') \cup (T_1' \cap T_2)$
$$P(\text{Exactly One}) = P(T_1 \cup T_2) - P(T_1 \cap T_2) = 0.58 - 0.12 = 0.46$$

**d) ** "At most one": $(T_1 \cap T_2)'$
$$P((T_1 \cap T_2)') = 1 - P(T_1 \cap T_2) = 1 - 0.12 = 0.88$$

**Final Answer:** **a) ** $\mathbf{0.58}$, **b) ** $\mathbf{0.42}$, **c) ** $\mathbf{0.46}$, **d) ** $\mathbf{0.88}$.

#### Exercise 11: Multi-Part System Outage & Database Lock Phrases (Time-Domain)
**Problem:** In a database server, event $A$ = "read queue delay $> 50\text{ ms}$" ($P(A) = 0.25$) and event $B$ = "write lock contention" ($P(B) = 0.15$). The joint probability of both is $P(A \cap B) = 0.05$.
**a) ** Calculate the probability of $A \cap B'$ and state its time-domain meaning.
**b) ** Calculate the probability of $A' \cap B$ and state its time-domain meaning.
**c) ** Calculate the probability that the server experiences either queue delay or write lock contention, but not both.
**d) ** Calculate the probability of complete normal operation ($(A \cup B)'$).

**Solution:**
**a) ** $P(A \cap B') = P(A) - P(A \cap B) = 0.25 - 0.05 = 0.20$.
*Meaning:* Read queue delay exceeds $50\text{ ms}$ while write locks remain uncontended.

**b) ** $P(A' \cap B) = P(B) - P(A \cap B) = 0.15 - 0.05 = 0.10$.
*Meaning:* Write lock contention occurs while read queue delay remains $\le 50\text{ ms}$.

**c) ** Either but not both (Exactly One):
$$P(\text{Exactly One}) = P(A \cap B') + P(A' \cap B) = 0.20 + 0.10 = 0.30$$

**d) ** Normal operation:
$$P(A \cup B) = 0.25 + 0.15 - 0.05 = 0.35$$
$$P((A \cup B)') = 1 - 0.35 = 0.65$$

**Final Answer:** **a) ** $\mathbf{0.20}$, **b) ** $\mathbf{0.10}$, **c) ** $\mathbf{0.30}$, **d) ** $\mathbf{0.65}$.

#### Exercise 12: 3-Event Venn Diagram Region Tallying
**Problem:** A survey of 120 developers tracks knowledge of C++ ($A$), Java ($B$), and Python ($C$).
- $n(A) = 60, n(B) = 50, n(C) = 45$
- $n(A \cap B) = 20, n(A \cap C) = 15, n(B \cap C) = 15$
- $n(A \cap B \cap C) = 8$
Compute the number of developers who know:
**a) ** All three languages
**b) ** Exactly two languages
**c) ** C++ only
**d) ** None of the three languages

**Solution:**
**a) ** Given directly: $n(A \cap B \cap C) = 8$.

**b) ** Two-language overlaps (excluding all three):
*   Only C++ and Java: $n(A \cap B \cap C') = 20 - 8 = 12$
*   Only C++ and Python: $n(A \cap C \cap B') = 15 - 8 = 7$
*   Only Java and Python: $n(B \cap C \cap A') = 15 - 8 = 7$
Total knowing exactly two: $12 + 7 + 7 = 26$.

**c) ** Only C++ ($A \cap B' \cap C'$):
$$n(A \cap B' \cap C') = n(A) - [12 + 7 + 8] = 60 - 27 = 33$$

**d) ** Total union $n(A \cup B \cup C)$:
$$n(A \cup B \cup C) = 60 + 50 + 45 - 20 - 15 - 15 + 8 = 113$$
None ($A' \cap B' \cap C'$):
$$n(\text{None}) = 120 - 113 = 7$$

**Final Answer:** **a) ** $\mathbf{8}$, **b) ** $\mathbf{26}$, **c) ** $\mathbf{33}$, **d) ** $\mathbf{7}$.

#### Exercise 13: 3-Component Microservice Jitter Breakdown (Time-Domain)
**Problem:** A distributed system consists of 3 microservices $M_1, M_2, M_3$. Jitter spikes occur with probabilities $P(M_1) = 0.10, P(M_2) = 0.12, P(M_3) = 0.08$. Pairwise joint jitter probabilities are $P(M_1 \cap M_2) = 0.03, P(M_1 \cap M_3) = 0.02, P(M_2 \cap M_3) = 0.02$, and all three experience simultaneous jitter with probability $P(M_1 \cap M_2 \cap M_3) = 0.01$.
**a) ** Compute the probability that at least one microservice experiences a jitter spike.
**b) ** Compute the probability that ONLY $M_1$ experiences a jitter spike.
**c) ** Compute the probability that NO microservice experiences a jitter spike.

**Solution:**
**a) ** Apply Inclusion-Exclusion for 3 events:
$$\begin{aligned}
P(M_1 \cup M_2 \cup M_3) &= (0.10 + 0.12 + 0.08) - (0.03 + 0.02 + 0.02) + 0.01 \\
&= 0.30 - 0.07 + 0.01 = 0.24
\end{aligned}$$

**b) ** Only $M_1$ ($M_1 \cap M_2' \cap M_3'$):
$$P(M_1 \cap M_2' \cap M_3') = P(M_1) - P(M_1 \cap M_2) - P(M_1 \cap M_3) + P(M_1 \cap M_2 \cap M_3)$$
$$P(M_1 \cap M_2' \cap M_3') = 0.10 - 0.03 - 0.02 + 0.01 = 0.06$$

**c) ** No jitter spike:
$$P(M_1' \cap M_2' \cap M_3') = 1 - P(M_1 \cup M_2 \cup M_3) = 1 - 0.24 = 0.76$$

**Final Answer:** **a) ** $\mathbf{0.24}$, **b) ** $\mathbf{0.06}$, **c) ** $\mathbf{0.76}$.

#### Exercise 14: R Code for 4-Region Venn Diagram Counts (Time-Domain)
**Problem:** Write an R function `venn_4regions(N, nA, nB, nAB)` that accepts total request count $N$, count of high-latency requests $nA$, count of peak-hour requests $nB$, and joint count $nAB$. The function must output a named vector with the 4 region counts and print a warning if the counts violate probability axioms.

**Solution:**
```r
venn_4regions <- function(N, nA, nB, nAB) {
  only_A <- nA - nAB
  only_B <- nB - nAB
  both   <- nAB
  neither <- N - (only_A + only_B + both)
  
  # Axiom verification
  if (only_A < 0 || only_B < 0 || both < 0 || neither < 0) {
    warning("Input parameters violate Kolmogorov Axioms (negative region count detected)!")
  }
  
  regions <- c(Only_A = only_A, Both = both, Only_B = only_B, Neither = neither)
  return(regions)
}

# Test execution with valid input
res <- venn_4regions(N = 500, nA = 150, nB = 200, nAB = 50)
print(res)
```

**Final Answer:** R command snippet provided and verified.

### R Implementation

Using the R script above, we can compute regional probabilities for any 2-event scenario:

```r
# Define parameters
N <- 1000
p_A <- 0.25; p_B <- 0.15; p_AB <- 0.05

# Region Probabilities
p_onlyA <- p_A - p_AB
p_onlyB <- p_B - p_AB
p_both  <- p_AB
p_neither <- 1 - (p_onlyA + p_onlyB + p_both)

cat("P(Only A):", p_onlyA, "\n")
cat("P(Only B):", p_onlyB, "\n")
cat("P(Both):", p_both, "\n")
cat("P(Neither):", p_neither, "\n")
cat("Sum of regions:", sum(p_onlyA, p_onlyB, p_both, p_neither), "\n")
```

---

## Section 2.3: Probability Axioms, Rules & De Morgan's Laws

### Core Theory & Definitions

Modern probability theory rests upon the three **Kolmogorov Axioms** established by Andrey Kolmogorov in 1933. All valid probability rules, bounds, and identity theorems are derived directly from these three axioms.

#### Kolmogorov's Axioms

1.  **Axiom 1 (Non-Negativity):** For any event $A \subseteq \Omega$, the assigned probability is non-negative:
    $$\boxed{P(A) \ge 0}$$

2.  **Axiom 2 (Normalization):** The probability of the entire sample space $\Omega$ equals unity:
    $$\boxed{P(\Omega) = 1.0}$$

3.  **Axiom 3 (Countable Additivity):** If $A_1, A_2, A_3, \dots$ is a sequence of pairwise disjoint events ($A_i \cap A_j = \emptyset$ for all $i \neq j$), then:
    $$\boxed{P\left(\bigcup_{i=1}^\infty A_i\right) = \sum_{i=1}^\infty P(A_i)}$$

#### The General Addition Rule
For any two arbitrary events $A$ and $B$ (whether disjoint or overlapping):
$$\boxed{P(A \cup B) = P(A) + P(B) - P(A \cap B)}$$
*Intuition:* Adding $P(A)$ and $P(B)$ counts the intersection $A \cap B$ twice. Subtracting $P(A \cap B)$ corrects the double-counting.

#### The Inclusion-Exclusion Principle (3 Events)
For any three arbitrary events $A, B, C$:
$$\boxed{P(A \cup B \cup C) = P(A) + P(B) + P(C) - P(A \cap B) - P(A \cap C) - P(B \cap C) + P(A \cap B \cap C)}$$

#### De Morgan's Laws
De Morgan's Laws describe how complement operators interact with unions and intersections:

1.  **First Law (Complement of Union):**
    $$(A \cup B)' = A' \cap B'$$
    In probability form:
    $$\boxed{P((A \cup B)') = P(A' \cap B') = 1 - P(A \cup B)}$$
    *Reading:* "NOT (A or B)" is logically equivalent to "(NOT A) AND (NOT B)". Neither event occurs.

2.  **Second Law (Complement of Intersection):**
    $$(A \cap B)' = A' \cup B'$$
    In probability form:
    $$\boxed{P((A \cap B)') = P(A' \cup B') = 1 - P(A \cap B)}$$
    *Reading:* "NOT (A and B)" is logically equivalent to "(NOT A) OR (NOT B)". At least one event fails to occur.

> **Practical / Time-Domain Note:**
> In distributed systems reliability, De Morgan's Laws evaluate overall system operational bounds.
> If $F_1, F_2, \dots, F_k$ represent component failure events:
> - System survival (all components working) is $F_1' \cap F_2' \cap \dots \cap F_k' = (F_1 \cup F_2 \cup \dots \cup F_k)'$.
> - System failure (at least one component down) is $F_1 \cup F_2 \cup \dots \cup F_k$.

### Mathematical Formulas & Derivations

1.  **Derivation of General Addition Rule:**
    Partition $A \cup B$ into three mutually exclusive regions:
    $$A \cup B = (A \cap B') \cup (A \cap B) \cup (A' \cap B)$$
    By Axiom 3:
    $$P(A \cup B) = P(A \cap B') + P(A \cap B) + P(A' \cap B)$$
    Substitute $P(A \cap B') = P(A) - P(A \cap B)$ and $P(A' \cap B) = P(B) - P(A \cap B)$:
    $$P(A \cup B) = [P(A) - P(A \cap B)] + P(A \cap B) + [P(B) - P(A \cap B)] = P(A) + P(B) - P(A \cap B) \quad \blacksquare$$

2.  **Probability Bounds (Boole's and Bonferroni's Inequalities):**
    *   **Boole's Inequality (Union Bound):** $P(A \cup B) \le P(A) + P(B)$
    *   **Bonferroni's Inequality:** $P(A \cap B) \ge P(A) + P(B) - 1$

### Worked Exercises

#### Exercise 15: Kolmogorov Axioms Consistency Check
**Problem:** A researcher proposes the following assignment for events $A$ and $B$: $P(A) = 0.70$, $P(B) = 0.50$, and $P(A \cup B) = 0.90$.
**a) ** Compute $P(A \cap B)$.
**b) ** Check if this probability assignment satisfies all Kolmogorov Axioms.

**Solution:**
**a) ** Apply the Addition Rule:
$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$
$$0.90 = 0.70 + 0.50 - P(A \cap B) \implies P(A \cap B) = 1.20 - 0.90 = 0.30$$

**b) ** Verify Kolmogorov Axioms:
1.  **Non-negativity:** $P(A)=0.70 \ge 0, P(B)=0.50 \ge 0, P(A \cap B)=0.30 \ge 0, P(A \cup B)=0.90 \ge 0$. Region probabilities: $P(A \cap B') = 0.40 \ge 0$, $P(A' \cap B) = 0.20 \ge 0$, $P(A' \cap B') = 0.10 \ge 0$. All $\ge 0 \checkmark$.
2.  **Normalization:** $P(\Omega) = P(A \cup B) + P((A \cup B)') = 0.90 + 0.10 = 1.00 \checkmark$.
3.  **Additivity:** All composite probabilities match disjoint region sums $\checkmark$.

**Final Answer:** $P(A \cap B) = \mathbf{0.30}$. The assignment is **fully consistent** with all axioms.

#### Exercise 16: Verification of Axioms on Buffer Overflow Bounds (Time-Domain)
**Problem:** A network router tracks buffer overflow ($O$) and packet corruption ($C$). An engineer claims: $P(O) = 0.15$, $P(C) = 0.10$, and $P(O \cap C) = 0.20$. Show why this violates probability theory.

**Solution:**
Recall that $O \cap C \subseteq O$. By subset monotonicity:
$$P(O \cap C) \le P(O)$$
Here, $P(O \cap C) = 0.20 > P(O) = 0.15$.
Furthermore, computing "Only Overflow":
$$P(O \cap C') = P(O) - P(O \cap C) = 0.15 - 0.20 = -0.05 < 0$$
This yields a negative probability, directly violating **Axiom 1 (Non-Negativity)**.

**Final Answer:** The claim is invalid because $P(O \cap C) > P(O)$, causing $P(O \cap C') = \mathbf{-0.05}$, which violates **Axiom 1**.

#### Exercise 17: Addition Rule & Complementary Probability
**Problem:** A student has a $0.60$ chance of passing Math ($M$) and a $0.50$ chance of passing Physics ($P$). The probability of passing both is $0.30$.
**a) ** Find the probability of passing at least one subject.
**b) ** Find the probability of failing both subjects.

**Solution:**
**a) ** At least one:
$$P(M \cup P) = P(M) + P(P) - P(M \cap P) = 0.60 + 0.50 - 0.30 = 0.80$$

**b) ** Failing both:
$$P(M' \cap P') = 1 - P(M \cup P) = 1 - 0.80 = 0.20$$

**Final Answer:** **a) ** $\mathbf{0.80}$, **b) ** $\mathbf{0.20}$.

#### Exercise 18: Addition Rule for Network Packet Dropping & Timeouts (Time-Domain)
**Problem:** During peak routing hours, packet drop probability is $P(D) = 0.08$, timeout probability is $P(T) = 0.05$, and the probability of experiencing both is $P(D \cap T) = 0.02$.
**a) ** Compute the probability of experiencing a packet drop, a timeout, or both.
**b) ** Compute the probability of successful transmission with neither issue.

**Solution:**
**a) ** Apply Addition Rule:
$$P(D \cup T) = P(D) + P(T) - P(D \cap T) = 0.08 + 0.05 - 0.02 = 0.11$$

**b) ** Successful transmission:
$$P(D' \cap T') = 1 - P(D \cup T) = 1 - 0.11 = 0.89$$

**Final Answer:** **a) ** $\mathbf{0.11}$, **b) ** $\mathbf{0.89}$.

#### Exercise 19: De Morgan's Laws Application
**Problem:** Given $P(A) = 0.55$, $P(B) = 0.40$, and $P(A \cup B) = 0.75$.
**a) ** Calculate $P(A \cap B)$.
**b) ** Apply De Morgan's First Law to calculate $P(A' \cap B')$.
**c) ** Apply De Morgan's Second Law to calculate $P(A' \cup B')$.

**Solution:**
**a) ** $P(A \cap B) = P(A) + P(B) - P(A \cup B) = 0.55 + 0.40 - 0.75 = 0.20$.

**b) ** First Law: $(A \cup B)' = A' \cap B'$
$$P(A' \cap B') = 1 - P(A \cup B) = 1 - 0.75 = 0.25$$

**c) ** Second Law: $(A \cap B)' = A' \cup B'$
$$P(A' \cup B') = 1 - P(A \cap B) = 1 - 0.20 = 0.80$$

**Final Answer:** **a) ** $\mathbf{0.20}$, **b) ** $\mathbf{0.25}$, **c) ** $\mathbf{0.80}$.

#### Exercise 20: De Morgan's Laws on System Heartbeat & Ping Failures (Time-Domain)
**Problem:** Two ping monitors check a remote server. Monitor 1 misses heartbeat ($M_1$) with probability $0.04$. Monitor 2 misses heartbeat ($M_2$) with probability $0.06$. Both miss simultaneously with probability $0.01$.
**a) ** What is the probability that AT LEAST ONE monitor misses the heartbeat?
**b) ** Use De Morgan's Law to find the probability that BOTH monitors receive the heartbeat.
**c) ** What is the probability that AT LEAST ONE monitor successfully receives the heartbeat?

**Solution:**
**a) ** At least one misses:
$$P(M_1 \cup M_2) = P(M_1) + P(M_2) - P(M_1 \cap M_2) = 0.04 + 0.06 - 0.01 = 0.09$$

**b) ** Both receive heartbeat:
By De Morgan's First Law, $M_1' \cap M_2' = (M_1 \cup M_2)'$:
$$P(M_1' \cap M_2') = 1 - P(M_1 \cup M_2) = 1 - 0.09 = 0.91$$

**c) ** At least one receives heartbeat:
By De Morgan's Second Law, $M_1' \cup M_2' = (M_1 \cap M_2)'$:
$$P(M_1' \cup M_2') = 1 - P(M_1 \cap M_2) = 1 - 0.01 = 0.99$$

**Final Answer:** **a) ** $\mathbf{0.09}$, **b) ** $\mathbf{0.91}$, **c) ** $\mathbf{0.99}$.

#### Exercise 21: 3-Event Inclusion-Exclusion Principle
**Problem:** In a factory, machines $A, B, C$ produce defective parts with probabilities $P(A)=0.10, P(B)=0.12, P(C)=0.15$. Pairwise joint defects are $P(A \cap B)=0.04, P(A \cap C)=0.03, P(B \cap C)=0.05$. All three defect simultaneously with probability $0.02$. Find the probability that a part has at least one defect.

**Solution:**
Apply 3-event Inclusion-Exclusion:
$$\begin{aligned}
P(A \cup B \cup C) &= (0.10 + 0.12 + 0.15) - (0.04 + 0.03 + 0.05) + 0.02 \\
&= 0.37 - 0.12 + 0.02 = 0.27
\end{aligned}$$

**Final Answer:** $P(A \cup B \cup C) = \mathbf{0.27}$.

#### Exercise 22: 3-Node Distributed Consensus Inclusion-Exclusion (Time-Domain)
**Problem:** A distributed database requires consensus among 3 nodes $N_1, N_2, N_3$. Node timeout probabilities are $P(N_1)=0.05, P(N_2)=0.05, P(N_3)=0.05$. Pairwise timeout probabilities are $P(N_i \cap N_j)=0.01$ for all pairs, and $P(N_1 \cap N_2 \cap N_3)=0.002$.
**a) ** Compute the probability that at least one node times out.
**b) ** Compute the probability that all three nodes respond without timeout.

**Solution:**
**a) ** At least one timeout:
$$P(N_1 \cup N_2 \cup N_3) = 3(0.05) - 3(0.01) + 0.002 = 0.15 - 0.03 + 0.002 = 0.122$$

**b) ** All respond:
$$P(N_1' \cap N_2' \cap N_3') = 1 - P(N_1 \cup N_2 \cup N_3) = 1 - 0.122 = 0.878$$

**Final Answer:** **a) ** $\mathbf{0.122}$, **b) ** $\mathbf{0.878}$.

#### Exercise 23: R Code for Inclusion-Exclusion & Axiom Verification (Time-Domain)
**Problem:** Write R code to verify the 3-event Inclusion-Exclusion principle and check Bonferroni's inequality for $P(A)=0.7, P(B)=0.8, P(A \cap B)=0.6$.

**Solution:**
```r
# Given probabilities
pA <- 0.7; pB <- 0.8; pAB <- 0.6

# 1. Addition Rule check
pA_union_B <- pA + pB - pAB
cat("P(A u B):", pA_union_B, "\n")

# 2. Bonferroni's Inequality check: P(A n B) >= P(A) + P(B) - 1
bonferroni_bound <- pA + pB - 1
cat("Bonferroni Lower Bound:", bonferroni_bound, "\n")
cat("P(A n B) >= Bound?", pAB >= bonferroni_bound, "\n")

# 3. Axiom Check
stopifnot(pA_union_B <= 1.0, pA_union_B >= 0.0)
cat("Axiom checks passed successfully!\n")
```

**Final Answer:** R code executed and Bonferroni bound verified ($0.6 \ge 0.5$).

### R Implementation

R script for verifying Bonferroni bounds and De Morgan's laws:

```r
# Verify De Morgan's Law via simulation
set.seed(42)
N <- 1e6
event_A <- runif(N) < 0.4
event_B <- runif(N) < 0.3

# Empirical probabilities
p_A_or_B <- mean(event_A | event_B)
p_notA_and_notB <- mean(!event_A & !event_B)

cat("Empirical P((A u B)'):", 1 - p_A_or_B, "\n")
cat("Empirical P(A' n B'):", p_notA_and_notB, "\n")
cat("Difference:", abs((1 - p_A_or_B) - p_notA_and_notB), "\n")
```

---

## Section 2.4: Combinatorics & Counting Methods

### Core Theory & Definitions

When all outcomes in a finite sample space $\Omega$ are **equally likely** (laplacian sample space), calculating the probability of an event $A$ reduces to a pure counting problem:
$$P(A) = \frac{|A|}{|\Omega|} = \frac{\text{Number of Favorable Outcomes}}{\text{Total Number of Possible Outcomes}}$$

Combinatorics provides the rigorous rules for counting large sample spaces without exhaustive enumeration.

#### 1. Fundamental Principles of Counting
*   **Product Rule (Multiplication Principle):** If a procedure can be broken into $k$ sequential stages, where stage 1 has $n_1$ outcomes, stage 2 has $n_2$ outcomes, ..., and stage $k$ has $n_k$ outcomes, the total number of composite outcomes is:
    $$N = n_1 \cdot n_2 \cdot \dots \cdot n_k$$
*   **Sum Rule (Addition Principle):** If an choice can be made either from set 1 with $n_1$ options OR from set 2 with $n_2$ options (where the sets are disjoint), the total number of choices is:
    $$N = n_1 + n_2$$

#### 2. Permutations (Order Matters)
An ordered arrangement of $r$ objects selected from a set of $n$ distinct objects.
*   **Without Repetition:**
    $$P(n, r) = \frac{n!}{(n-r)!}$$
    *Special case ($r=n$):* Arranging all $n$ distinct objects requires $P(n, n) = n!$ ways.
*   **Permutations with Repetition (Identical Objects):** Arranging $n$ total objects where $n_1$ are identical of type 1, $n_2$ identical of type 2, ..., $n_k$ identical of type $k$:
    $$P(n; n_1, n_2, \dots, n_k) = \frac{n!}{n_1! \cdot n_2! \dots n_k!}$$
*   **Circular Permutations:** Arranging $n$ distinct objects around a closed circle (where rotational shifts are considered identical):
    $$P_{\text{circular}} = (n - 1)!$$

#### 3. Combinations (Order Does NOT Matter)
An unordered selection of $r$ objects chosen from $n$ distinct objects.
*   **Without Replacement:**
    $$C(n, r) = \binom{n}{r} = \frac{n!}{r!(n-r)!}$$
*   **Combinations with Replacement (Stars and Bars):** Selecting $r$ items from $n$ distinct categories where items may be selected repeatedly:
    $$C^R(n, r) = \binom{n + r - 1}{r} = \frac{(n + r - 1)!}{r!(n - 1)!}$$

#### 4. Multinomial Coefficients
Partitioning $n$ distinct objects into $k$ distinct groups of specified sizes $r_1, r_2, \dots, r_k$ (where $\sum r_i = n$):
$$\binom{n}{r_1, r_2, \dots, r_k} = \frac{n!}{r_1! \cdot r_2! \dots r_k!}$$

> **Practical / Time-Domain Note:**
> In computer systems and networks:
> - **Permutations** model sequential execution order, pipeline stages, network packet routing paths, and priority queues.
> - **Combinations** model server pool selections, quorum voting nodes, parallel thread allocations, and memory buffer partitioning.
> - **Combinations with replacement** model assigning identical requests across server queues or allocating CPU cycles to processes.

### Mathematical Formulas & Derivations

1.  **Derivation of Circular Permutation Formula:**
    Linear arrangements of $n$ distinct objects equal $n!$. Around a circle, every valid arrangement can be rotated into $n$ equivalent configurations. Dividing linear permutations by $n$ rotational symmetries gives:
    $$P_{\text{circular}} = \frac{n!}{n} = (n - 1)! \quad \blacksquare$$

2.  **Stars and Bars Derivation (Combinations with Replacement):**
    To distribute $r$ identical items into $n$ distinct bins, place $r$ stars ($\star$) and $n-1$ dividers ($|$). Total symbols = $r + n - 1$. Selecting positions for the $r$ stars out of $r + n - 1$ total symbol positions yields $\binom{n+r-1}{r}$.

### Worked Exercises

#### Exercise 24: Permutations and Combinations in Quality Control
**Problem:** A batch of 20 manufactured circuit boards contains 4 defective boards. A sample of 5 boards is selected at random without replacement.
**a) ** How many total samples of 5 boards can be formed?
**b) ** How many samples contain exactly 2 defective boards?
**c) ** What is the probability that a sample contains at least 1 defective board?

**Solution:**
**a) ** Total possible samples $|\Omega|$:
$$|\Omega| = \binom{20}{5} = \frac{20 \cdot 19 \cdot 18 \cdot 17 \cdot 16}{5 \cdot 4 \cdot 3 \cdot 2 \cdot 1} = 15,504$$

**b) ** Choose 2 defective from 4, and 3 non-defective from 16:
$$|E_{\text{2 def}}| = \binom{4}{2} \cdot \binom{16}{3} = 6 \cdot \frac{16 \cdot 15 \cdot 14}{3 \cdot 2 \cdot 1} = 6 \cdot 560 = 3,360$$

**c) ** Complementary probability (0 defective):
$$|E_{\text{0 def}}| = \binom{4}{0} \cdot \binom{16}{5} = 1 \cdot 4,368 = 4,368$$
$$P(\text{0 def}) = \frac{4,368}{15,504} \approx 0.2817$$
$$P(\text{at least 1 def}) = 1 - P(\text{0 def}) = 1 - 0.2817 = 0.7183$$

**Final Answer:** **a) ** $\mathbf{15,504}$, **b) ** $\mathbf{3,360}$, **c) ** $\mathbf{0.7183}$.

#### Exercise 25: License Plate Permutations & Product Rule
**Problem:** A state formats vehicle license plates with 3 uppercase letters followed by 4 digits.
**a) ** How many total plates exist if repetition is allowed?
**b) ** How many total plates exist if NO repetition of letters or digits is allowed?
**c) ** What is the probability that a randomly assigned plate starts with the letter 'A' and ends with an even digit (repetition allowed)?

**Solution:**
**a) ** Repetition allowed:
$$N = 26^3 \cdot 10^4 = 17,576 \cdot 10,000 = 175,760,000$$

**b) ** No repetition:
$$N_{\text{no rep}} = (26 \cdot 25 \cdot 24) \cdot (10 \cdot 9 \cdot 8 \cdot 7) = 15,600 \cdot 5,040 = 78,624,000$$

**c) ** Starts with 'A' (1 option), next 2 letters (26 options each); ends with even digit $\{0,2,4,6,8\}$ (5 options), first 3 digits (10 options each):
$$|F| = (1 \cdot 26 \cdot 26) \cdot (10 \cdot 10 \cdot 10 \cdot 5) = 676 \cdot 5,000 = 3,380,000$$
$$P = \frac{3,380,000}{175,760,000} = \frac{1}{26} \cdot \frac{5}{10} = \frac{1}{26} \cdot \frac{1}{2} = \frac{1}{52} \approx 0.01923$$

**Final Answer:** **a) ** $\mathbf{175,760,000}$, **b) ** $\mathbf{78,624,000}$, **c) ** $\mathbf{1/52 \approx 0.01923}$.

#### Exercise 26: Server Task Scheduling Timeline & Permutations (Time-Domain)
**Problem:** An operating system scheduler must execute 8 processes: 3 real-time audio tasks, 3 database queries, and 2 background backups.
**a) ** How many total linear execution sequences exist?
**b) ** How many sequences execute all 3 audio tasks consecutively?
**c) ** How many sequences group tasks of the same type together?

**Solution:**
**a) ** Linear permutations of 8 distinct tasks:
$$P(8, 8) = 8! = 40,320$$

**b) ** Treat the 3 audio tasks as 1 super-task. Total objects to arrange = $1 + 3 + 2 = 6$.
Internal arrangements of audio tasks = $3! = 6$.
$$N = 6! \cdot 3! = 720 \cdot 6 = 4,320$$

**c) ** Arrange the 3 task categories: $3! = 6$ ways.
Arrange within categories: Audio ($3!$), Database ($3!$), Backup ($2!$).
$$N_{\text{grouped}} = 3! \cdot (3! \cdot 3! \cdot 2!) = 6 \cdot (6 \cdot 6 \cdot 2) = 6 \cdot 72 = 432$$

**Final Answer:** **a) ** $\mathbf{40,320}$, **b) ** $\mathbf{4,320}$, **c) ** $\mathbf{432}$.

#### Exercise 27: Multi-Tier Card Deck & Urn Selection (Combined, Moderate)
**Problem:** An urn contains 10 red balls, 8 blue balls, and 6 green balls (total 24 balls). A player draws 4 balls simultaneously at random.
**a) ** Calculate the total size of the sample space $|\Omega|$.
**b) ** Calculate the probability of drawing exactly 2 red and 2 blue balls.
**c) ** Calculate the probability of drawing all 4 balls of the same color.
**d) ** Calculate the probability of drawing at least 1 green ball.

**Solution:**
**a) ** Sample space:
$$|\Omega| = \binom{24}{4} = \frac{24 \cdot 23 \cdot 22 \cdot 21}{4 \cdot 3 \cdot 2 \cdot 1} = 10,626$$

**b) ** 2 Red ($\binom{10}{2}$), 2 Blue ($\binom{8}{2}$), 0 Green ($\binom{6}{0}$):
$$|E_b| = \binom{10}{2} \cdot \binom{8}{2} = 45 \cdot 28 = 1,260$$
$$P(E_b) = \frac{1,260}{10,626} = \frac{210}{1,771} \approx 0.1186$$

**c) ** Same color: All Red ($\binom{10}{4}$), All Blue ($\binom{8}{4}$), or All Green ($\binom{6}{4}$):
$$|E_c| = \binom{10}{4} + \binom{8}{4} + \binom{6}{4} = 210 + 70 + 15 = 295$$
$$P(E_c) = \frac{295}{10,626} \approx 0.02776$$

**d) ** At least 1 green = $1 - P(\text{0 green})$:
0 Green means drawing 4 balls from 18 non-green (10 Red + 8 Blue):
$$|E_{\text{no green}}| = \binom{18}{4} = 3,060$$
$$P(\text{at least 1 green}) = 1 - \frac{3,060}{10,626} = 1 - 0.28797 = 0.71203$$

**Final Answer:** **a) ** $\mathbf{10,626}$, **b) ** $\mathbf{0.1186}$, **c) ** $\mathbf{0.02776}$, **d) ** $\mathbf{0.71203}$.

#### Exercise 28: Multi-Channel Signal Routing & Permutations (Time-Domain) (Combined, Harder)
**Problem:** A network switch routes packets across 12 distinct physical channels. 5 channels carry high-priority video streams, 4 carry VoIP audio, and 3 carry data traffic.
**a) ** In how many distinct ways can the 12 channels be assigned to 3 processing cores if Core 1 receives 5 channels, Core 2 receives 4 channels, and Core 3 receives 3 channels?
**b) ** If 4 channels are selected at random without replacement, what is the probability that all 4 are video channels?
**c) ** If channels are routed sequentially one by one, what is the probability that the first 3 routed channels are all video streams?
**d) ** What R command computes the multinomial partitioning count from part a?

**Solution:**
**a) ** Apply Multinomial Coefficient:
$$\binom{12}{5, 4, 3} = \frac{12!}{5! \cdot 4! \cdot 3!} = \frac{479,001,600}{120 \cdot 24 \cdot 6} = \frac{479,001,600}{17,280} = 27,720$$

**b) ** Choose 4 video from 5 video; total channels 12:
$$P = \frac{\binom{5}{4}}{\binom{12}{4}} = \frac{5}{495} = \frac{1}{99} \approx 0.01010$$

**c) ** Sequential routing without replacement (first 3 video):
$$P = \frac{5}{12} \cdot \frac{4}{11} \cdot \frac{3}{10} = \frac{60}{1320} = \frac{1}{22} \approx 0.04545$$

**d) ** R command snippet:
```r
factorial(12) / (factorial(5) * factorial(4) * factorial(3))
```

**Final Answer:** **a) ** $\mathbf{27,720}$, **b) ** $\mathbf{1/99 \approx 0.01010}$, **c) ** $\mathbf{1/22 \approx 0.04545}$, **d) ** R command: `factorial(12) / (factorial(5)*factorial(4)*factorial(3))`.

#### Exercise 29: 3-Stage Microservice Queueing Delay & Venn Breakdown (Time-Domain) (Combined, Hard)
**Problem:** A complex transaction traverses 3 microservices $S_1, S_2, S_3$. Latency exceeding $100\text{ ms}$ occurs at $S_1$ with $P(S_1)=0.20$, at $S_2$ with $P(S_2)=0.25$, and at $S_3$ with $P(S_3)=0.15$.
Intersections: $P(S_1 \cap S_2) = 0.08$, $P(S_1 \cap S_3) = 0.05$, $P(S_2 \cap S_3) = 0.06$, and all three exceed delay simultaneously with $P(S_1 \cap S_2 \cap S_3) = 0.02$.
**a) ** Calculate the probability that the transaction experiences high latency at AT LEAST ONE microservice.
**b) ** Calculate the probability that the transaction completes within $100\text{ ms}$ across ALL 3 microservices.
**c) ** Calculate the probability that ONLY service $S_2$ experiences high latency.
**d) ** Calculate the probability that EXACTLY TWO microservices experience high latency.
**e) ** Write an R script using `choose()` or set logic to verify the total union probability.

**Solution:**
**a) ** Inclusion-Exclusion for 3 events:
$$\begin{aligned}
P(S_1 \cup S_2 \cup S_3) &= (0.20 + 0.25 + 0.15) - (0.08 + 0.05 + 0.06) + 0.02 \\
&= 0.60 - 0.19 + 0.02 = 0.43
\end{aligned}$$

**b) ** Complete SLA compliance across all 3:
$$P(S_1' \cap S_2' \cap S_3') = 1 - P(S_1 \cup S_2 \cup S_3) = 1 - 0.43 = 0.57$$

**c) ** Only $S_2$ ($S_2 \cap S_1' \cap S_3'$):
$$\begin{aligned}
P(\text{Only } S_2) &= P(S_2) - P(S_1 \cap S_2) - P(S_2 \cap S_3) + P(S_1 \cap S_2 \cap S_3) \\
&= 0.25 - 0.08 - 0.06 + 0.02 = 0.13
\end{aligned}$$

**d) ** Exactly two microservices:
*   Only $S_1$ and $S_2$: $0.08 - 0.02 = 0.06$
*   Only $S_1$ and $S_3$: $0.05 - 0.02 = 0.03$
*   Only $S_2$ and $S_3$: $0.06 - 0.02 = 0.04$
Total = $0.06 + 0.03 + 0.04 = 0.13$.

**e) ** R Verification snippet:
```r
p1 <- 0.20; p2 <- 0.25; p3 <- 0.15
p12 <- 0.08; p13 <- 0.05; p23 <- 0.06
p123 <- 0.02

union_3 <- p1 + p2 + p3 - (p12 + p13 + p23) + p123
cat("Total Union Probability:", union_3, "\n")
```

**Final Answer:** **a) ** $\mathbf{0.43}$, **b) ** $\mathbf{0.57}$, **c) ** $\mathbf{0.13}$, **d) ** $\mathbf{0.13}$, **e) ** Verified via R.

#### Exercise 30: Circular Clock Rotation & Combinations with Replacement (Time-Domain) (Combined, Hardest + Gotcha)
**Problem:** A system clock rotates through 6 scheduling time slots $\{T_1, T_2, T_3, T_4, T_5, T_6\}$ arranged in a continuous circular ring.
**a) ** In how many distinct circular arrangements can 6 distinct server workers be assigned to these 6 time slots?
**b) ** A system administrator selects 4 execution tasks to assign across the 6 time slots. Tasks are identical, and any time slot can accept multiple tasks. How many ways can the 4 tasks be distributed?
**c) ** Suppose 2 specific slots $T_1$ and $T_2$ are critical windows. If 4 tasks are distributed randomly with replacement across the 6 slots (each slot equally likely for each task), what is the probability that AT LEAST ONE task is assigned to $T_1$?
**d) ** An analyst computes the average slot index for events occurring at slot $T_6$ ($23:00\text{ h}$) and slot $T_1$ ($01:00\text{ h}$) using arithmetic mean: $\bar{t} = (23 + 1)/2 = 12:00\text{ h}$. Identify the flaw in this calculation, state the gotcha, and compute the true circular mean time.
**e) ** Write an R command to compute the combinations with replacement count from part b.

**Solution:**
**a) ** Circular permutations of 6 distinct workers:
$$P_{\text{circular}} = (6 - 1)! = 5! = 120\text{ ways}$$

**b) ** Combinations with replacement: $n = 6$ categories (slots), $r = 4$ identical tasks.
$$C^R(6, 4) = \binom{6 + 4 - 1}{4} = \binom{9}{4} = \frac{9 \cdot 8 \cdot 7 \cdot 6}{4 \cdot 3 \cdot 2 \cdot 1} = 126\text{ ways}$$

**c) ** Complement: 0 tasks in $T_1$. For each task, probability of NOT choosing $T_1$ is $5/6$.
$$P(\text{0 in } T_1) = \left(\frac{5}{6}\right)^4 = \frac{625}{1296} \approx 0.48225$$
$$P(\text{at least 1 in } T_1) = 1 - \frac{625}{1296} = \frac{671}{1296} \approx 0.51775$$

**d) ** **Gotcha Analysis:**
**Gotcha:** Applying the naive arithmetic mean to cyclic/circular time data produces completely erroneous mid-day results ($12:00\text{ h}$) for events wrapping around midnight!
*Correct Circular Mean:* Convert hours $t_i$ to angles $\theta_i = \frac{2\pi \cdot t_i}{24}$:
*   $t_1 = 23\text{ h} \implies \theta_1 = \frac{23 \cdot 2\pi}{24} = \frac{23\pi}{12} \text{ rad} \equiv -\frac{\pi}{12} \text{ rad}$
*   $t_2 = 1\text{ h} \implies \theta_2 = \frac{1 \cdot 2\pi}{24} = \frac{\pi}{12} \text{ rad}$
Compute vector sums:
$$\bar{S} = \sin(-\pi/12) + \sin(\pi/12) = 0, \quad \bar{C} = \cos(-\pi/12) + \cos(\pi/12) = 2 \cos(\pi/12) > 0$$
$$\bar{\theta} = \text{atan2}(0, 2\cos(\pi/12)) = 0\text{ rad} \implies \bar{t} = \frac{24 \cdot 0}{2\pi} = 00:00\text{ h (Midnight)!}$$

**e) ** R Command for combinations with replacement:
```r
choose(6 + 4 - 1, 4)  # returns 126
```

**Final Answer:** **a) ** $\mathbf{120}$, **b) ** $\mathbf{126}$, **c) ** $\mathbf{671/1296 \approx 0.51775}$, **d) ** **Gotcha:** Arithmetic mean fails on cyclic time. True circular mean = $\mathbf{00:00\ h}$, **e) ** `choose(9, 4)`.

### R Implementation

R script for combinatorics calculations:

```r
# Combinations & Permutations in R
n <- 6; r <- 4

# Combinations without replacement nCr
nCr <- choose(n, r)

# Combinations with replacement (Stars & Bars)
nCr_rep <- choose(n + r - 1, r)

# Permutations nPr
nPr <- factorial(n) / factorial(n - r)

cat("nCr (no rep):", nCr, "\n")
cat("nCr (with rep):", nCr_rep, "\n")
cat("nPr:", nPr, "\n")
```

---

## Exam Preparation Guide

### Formula Quick-Reference

| Topic | General Formula | Time-Domain Adapted Formula | Typologio / Exam Style |
| :--- | :--- | :--- | :--- |
| **Complement Rule** | $P(A') = 1 - P(A)$ | $P(T > t) = 1 - P(T \le t)$ | $P(A') = 1 - P(A)$ |
| **Disjoint Addition** | $P(A \cup B) = P(A) + P(B)$ | $P(T \in [t_1,t_2] \cup [t_3,t_4]) = P_1 + P_2$ | $P(A \cup B) = P(A) + P(B)$ |
| **General Addition** | $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ | $P(L \cup D) = P(L) + P(D) - P(L \cap D)$ | $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ |
| **3-Event Incl.-Excl.** | $P(A \cup B \cup C) = \sum P_i - \sum P_{ij} + P_{123}$ | $P(\bigcup M_i) = \sum P(M_i) - \sum P_{ij} + P_{123}$ | $P(A \cup B \cup C) = \sum P(A) - \sum P(A \cap B) + P(A \cap B \cap C)$ |
| **De Morgan's 1st Law** | $P((A \cup B)') = P(A' \cap B')$ | $P(\text{Neither latency nor drop}) = 1 - P(L \cup D)$ | $P(A' \cap B') = 1 - P(A \cup B)$ |
| **De Morgan's 2nd Law** | $P((A \cap B)') = P(A' \cup B')$ | $P(\text{Not both delayed}) = 1 - P(L_1 \cap L_2)$ | $P(A' \cup B') = 1 - P(A \cap B)$ |
| **Only A Probability** | $P(A \cap B') = P(A) - P(A \cap B)$ | $P(L \cap D') = P(L) - P(L \cap D)$ | $P(A \cap B') = P(A) - P(A \cap B)$ |
| **Exactly One Event** | $P(A \cup B) - P(A \cap B)$ | $P(L \cup D) - P(L \cap D)$ | $P(A) + P(B) - 2P(A \cap B)$ |
| **Permutations** | $P(n, r) = \frac{n!}{(n-r)!}$ | $P(N_{\text{tasks}}, K_{\text{slots}}) = \frac{N!}{(N-K)!}$ | $P(n, r) = \frac{n!}{(n-r)!}$ |
| **Circular Perms** | $P_{\text{circ}} = (n-1)!$ | $P_{\text{circ}} = (N_{\text{workers}}-1)!$ | $P_{\text{circ}} = (n-1)!$ |
| **Combinations** | $C(n, r) = \binom{n}{r} = \frac{n!}{r!(n-r)!}$ | $C(N_{\text{servers}}, K_{\text{nodes}}) = \binom{N}{K}$ | $\binom{n}{r} = \frac{n!}{r!(n-r)!}$ |
| **Comb. with Replacement** | $C^R(n, r) = \binom{n+r-1}{r}$ | $C^R(N_{\text{slots}}, K_{\text{tasks}}) = \binom{N+K-1}{K}$ | $\binom{n+r-1}{r}$ |
| **Multinomial** | $\binom{n}{r_1, \dots, r_k} = \frac{n!}{r_1! \dots r_k!}$ | $\binom{N}{K_1, K_2, K_3} = \frac{N!}{K_1! K_2! K_3!}$ | $\frac{n!}{r_1! r_2! \dots r_k!}$ |

---

### Exam Checklist

| Category | Items |
| :--- | :--- |
| **Must Memorize** | - Kolmogorov's Axioms ($P(A) \ge 0, P(\Omega)=1, P(\bigcup A_i) = \sum P(A_i)$)<br>- General Addition Rule: $P(A \cup B) = P(A) + P(B) - P(A \cap B)$<br>- De Morgan's Laws: $(A \cup B)' = A' \cap B'$ and $(A \cap B)' = A' \cup B'$<br>- Permutation formula $P(n,r) = \frac{n!}{(n-r)!}$ and Combination formula $\binom{n}{r} = \frac{n!}{r!(n-r)!}$<br>- Circular Permutations formula: $(n-1)!$ |
| **Must Understand** | - Distinction between Mutually Exclusive ($A \cap B = \emptyset$) and Independent ($P(A \cap B) = P(A)P(B)$) events<br>- Translation of English phrases ("at least one", "exactly one", "neither", "only A") into Venn region logic<br>- Classical probability rule $P(A) = |A| / |\Omega|$ for equiprobable outcomes<br>- The 4-region and 8-region Venn partition completeness rules |
| **Book-Only (Professor May Test)** | - **Combinations with Replacement (Stars and Bars):** Formula $\binom{n+r-1}{r}$ for selecting identical items into categories<br>- **Multinomial Coefficient Partitioning:** Distributing $n$ items into $k$ specific group sizes $\frac{n!}{r_1! r_2! \dots r_k!}$<br>- **Continuous Single-Point Zero Probability:** $P(T = t_0) = 0$ for continuous latency variables<br>- **Circular Mean on Cyclic Clock Times:** Why naive arithmetic mean fails on $23:00$ and $01:00$ |

---

### Common Exam Traps

1.  **Mutually Exclusive vs. Independent Confusion:**
    *   *Trap:* Assuming that mutually exclusive events ($A \cap B = \emptyset$) are independent.
    *   *Fix:* If $A$ and $B$ are mutually exclusive with $P(A) > 0$ and $P(B) > 0$, then $P(A \cap B) = 0 \neq P(A)P(B)$. Mutually exclusive events are **strongly dependent**!
2.  **At Least One vs. Exactly One Complement Trap:**
    *   *Trap:* Computing $1 - P(A \cap B)$ when asked for "neither $A$ nor $B$".
    *   *Fix:* "Neither $A$ nor $B$" is $P(A' \cap B') = 1 - P(A \cup B)$. "At most one" is $1 - P(A \cap B)$.
3.  **Circular Permutations Rotation Shift Trap:**
    *   *Trap:* Using $n!$ instead of $(n-1)!$ for items arranged in a circle.
    *   *Fix:* Always subtract 1 to fix the rotational reference point when arrangements are circular.
4.  **Combinations with Replacement Index Shift ($n$ vs $r$):**
    *   *Trap:* Swapping $n$ (categories) and $r$ (items) in $\binom{n+r-1}{r}$.
    *   *Fix:* $n$ is the number of distinct destination bins/categories, while $r$ is the number of items being selected/distributed.
5.  **Axiom Non-Negativity Violation in Region Subtraction:**
    *   *Trap:* Subtracting $P(A \cap B)$ without checking if $P(A \cap B) \le P(A)$.
    *   *Fix:* Verify that joint probabilities never exceed marginal probabilities ($P(A \cap B) \le \min(P(A), P(B))$).

---

### Exam Paper Cross-References

| Exam Paper | Relevant Questions | Difficulty |
| :--- | :--- | :---: |
| [Exam_paper_Easy.md](file:///home/ice/Documents/CodeHub/GitHub-Projects/Public/DitOpenNotes/Year_2/Semester_4/PROBABILITY_STATISTICS/Exams/Papers/Exam_paper_Easy.md) | Question 3 (Disjoint events, independent events, set operations, De Morgan's Law $P(A' \cap B')$) | **1/5** |
| [Exam_paper_2024_09_06_Team_A.md](file:///home/ice/Documents/CodeHub/GitHub-Projects/Public/DitOpenNotes/Year_2/Semester_4/PROBABILITY_STATISTICS/Exams/Papers/Exam_paper_2024_09_06_Team_A.md) | Question 2 (Set theory definitions, mutually exclusive vs independent events, $P(A \cup B)$ addition rule) | **1/5** |
| [Exam_paper_2023_06_12_Team_null.md](file:///home/ice/Documents/CodeHub/GitHub-Projects/Public/DitOpenNotes/Year_2/Semester_4/PROBABILITY_STATISTICS/Exams/Papers/Exam_paper_2023_06_12_Team_null.md) | Question 2 (Venn diagram translation, union and complement probability) | **2/5** |
| [Exam_paper_2024_06_14_Team_B.md](file:///home/ice/Documents/CodeHub/GitHub-Projects/Public/DitOpenNotes/Year_2/Semester_4/PROBABILITY_STATISTICS/Exams/Papers/Exam_paper_2024_06_14_Team_B.md) | Question 2 (Set probability calculation, disjoint events and complement) | **2/5** |
| [Exam_paper_2026_06_09_Team_B.md](file:///home/ice/Documents/CodeHub/GitHub-Projects/Public/DitOpenNotes/Year_2/Semester_4/PROBABILITY_STATISTICS/Exams/Papers/Exam_paper_2026_06_09_Team_B.md) | Question 2 (Set theory operations, phrase translation "at least one", "neither") | **2/5** |
| [Exam_paper_Intermediate_2.md](file:///home/ice/Documents/CodeHub/GitHub-Projects/Public/DitOpenNotes/Year_2/Semester_4/PROBABILITY_STATISTICS/Exams/Papers/Exam_paper_Intermediate_2.md) | Question 2 (Algebraic proofs of set relationships and De Morgan's laws) | **3/5** |

---

## Phase Summary

Phase 2 builds the formal set-theoretic foundation of Probability Theory:

*   **Set Theory & Sample Spaces:** Random experiments are defined on sample spaces ($\Omega$). Events are subsets $A \subseteq \Omega$. Fundamental operations include Union ($A \cup B$, logical OR), Intersection ($A \cap B$, logical AND), and Complement ($A'$, logical NOT). Mutually exclusive events satisfy $A \cap B = \emptyset$. Continuous time spaces $\Omega = [0, T]$ carry zero single-point probability ($P(T = t_0) = 0$).
*   **Venn Diagrams & Phrase Translation:** Venn diagrams partition sample spaces into 4 mutually exclusive regions for 2 events ($A \cap B', A \cap B, A' \cap B, A' \cap B'$) or 8 regions for 3 events. The partition probabilities sum to 1. Natural language expressions map directly to set operations: "at least one" $\rightarrow A \cup B$, "neither" $\rightarrow (A \cup B)' = A' \cap B'$, "only A" $\rightarrow A \cap B' = A - (A \cap B)$, and "exactly one" $\rightarrow P(A) + P(B) - 2P(A \cap B)$.
*   **Kolmogorov Axioms & Probability Rules:** Probability assignments must satisfy Kolmogorov's Axioms: Non-negativity ($P(A) \ge 0$), Normalization ($P(\Omega) = 1$), and Countable Additivity for disjoint events. The General Addition Rule handles overlapping events: $P(A \cup B) = P(A) + P(B) - P(A \cap B)$. De Morgan's Laws push complements inside set operations: $(A \cup B)' = A' \cap B'$ and $(A \cap B)' = A' \cup B'$.
*   **Combinatorics & Counting Methods:** For equiprobable outcomes, $P(A) = |A| / |\Omega|$. The Product Rule multiplies sequential stage choices, while the Sum Rule adds disjoint options. Permutations ($P(n, r) = \frac{n!}{(n-r)!}$) count ordered arrangements. Circular Permutations ($(n-1)!$) account for rotational symmetry. Combinations ($C(n, r) = \binom{n}{r} = \frac{n!}{r!(n-r)!}$) count unordered selections. Combinations with Replacement ($C^R(n, r) = \binom{n+r-1}{r}$) use Stars and Bars. Multinomial coefficients ($\frac{n!}{r_1! \dots r_k!}$) partition $n$ items into distinct group sizes.

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

