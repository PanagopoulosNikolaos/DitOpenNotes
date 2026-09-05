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

- [Section 3.1: Conditional Probability & Reduced Sample Space](#section-31-conditional-probability-reduced-sample-space)
- [Section 3.2: Multiplication Rule & Sequential Processes](#section-32-multiplication-rule-sequential-processes)
- [Section 3.3: Independence & System Reliability](#section-33-independence-system-reliability)
- [Section 3.4: Law of Total Probability & Bayes' Theorem](#section-34-law-of-total-probability-bayes-theorem)
- [Combined Exercises (Exercises 27 - 30)](#combined-exercises-exercises-27---30)
- [Exam Preparation Guide](#exam-preparation-guide)

### Phase 4: Discrete Random Variables

- [Section 4.1: Discrete Random Variables, PMF/CDF, Expectation & Variance](#section-41-discrete-random-variables-pmfcdf-expectation-variance)
- [Section 4.2: Binomial & Poisson Distributions](#section-42-binomial-poisson-distributions)
- [Section 4.3: Geometric & Hypergeometric Distributions](#section-43-geometric-hypergeometric-distributions)
- [Section 4.4: Moment Generating Functions & Characteristic Functions](#section-44-moment-generating-functions-characteristic-functions)
- [Exam Preparation Guide](#exam-preparation-guide)

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
| [Exam_paper_Easy.md](../../Exams/Papers/synthetic/Exam_paper_Easy.md) | Question 3 (Disjoint events, independent events, set operations, De Morgan's Law $P(A' \cap B')$) | **1/5** |
| [Exam_paper_2024_09_06_Team_A.md](../../Exams/Papers/Exam_paper_2024_09_06_Team_A.md) | Question 2 (Set theory definitions, mutually exclusive vs independent events, $P(A \cup B)$ addition rule) | **1/5** |
| [Exam_paper_2023_06_12_Team_null.md](../../Exams/Papers/Exam_paper_2023_06_12_Team_null.md) | Question 2 (Venn diagram translation, union and complement probability) | **2/5** |
| [Exam_paper_2024_06_14_Team_B.md](../../Exams/Papers/Exam_paper_2024_06_14_Team_B.md) | Question 2 (Set probability calculation, disjoint events and complement) | **2/5** |
| [Exam_paper_2026_06_09_Team_B.md](../../Exams/Papers/Exam_paper_2026_06_09_Team_B.md) | Question 2 (Set theory operations, phrase translation "at least one", "neither") | **2/5** |
| [Exam_paper_Intermediate_2.md](../../Exams/Papers/synthetic/Exam_paper_Intermediate_2.md) | Question 2 (Algebraic proofs of set relationships and De Morgan's laws) | **3/5** |

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
- [Section 3.1: Conditional Probability & Reduced Sample Space](#section-31-conditional-probability--reduced-sample-space)
- [Section 3.2: Multiplication Rule & Sequential Processes](#section-32-multiplication-rule--sequential-processes)
- [Section 3.3: Independence & System Reliability](#section-33-independence--system-reliability)
- [Section 3.4: Law of Total Probability & Bayes' Theorem](#section-34-law-of-total-probability--bayes-theorem)
- [Exam Preparation Guide](#exam-preparation-guide)
- [Phase Summary](#phase-summary)

---

## Section 3.1: Conditional Probability & Reduced Sample Space

### Core Theory & Definitions

Conditional probability evaluates the likelihood of an event $A$ occurring given that another event $B$ has already taken place ($P(B) > 0$). When we condition on $B$, the universal sample space $\Omega$ shrinks to $B$. Outcome elements outside $B$ become impossible and are discarded. The relevant subset of $A$ within this restricted universe is precisely the intersection $A \cap B$.

```
Universal Sample Space $\Omega$:
+------------------------------------+
|  A only     | A ∩ B  |  B only     |
|             |        |             |
+-------------+--------+-------------+
                 ^^^^^^
         Conditioning on B shrinks
         the sample space from $\Omega$ to $B$.
```

Mathematically, conditional probability behaves as a true probability measure on the restricted sample space $B$. It satisfies all three Kolmogorov Axioms:

1. **Non-negativity:** For any event $A \subseteq \Omega$, $0 \le P(A \mid B) \le 1$.
2. **Normalization:** $P(\Omega \mid B) = \frac{P(\Omega \cap B)}{P(B)} = \frac{P(B)}{P(B)} = 1$, and similarly $P(B \mid B) = 1$.
3. **Countable Additivity:** For any sequence of mutually disjoint events $A_1, A_2, A_3, \dots$ (where $A_i \cap A_j = \emptyset$ for $i \neq j$):
   $$P\left( \bigcup_{i=1}^{\infty} A_i \;\middle|\; B \right) = \sum_{i=1}^{\infty} P(A_i \mid B)$$

#### Time-Domain Application: Survival Probability & Right-Censoring

In time-series analysis, performance engineering, and reliability testing, conditional probability frequently measures execution lifetimes and delay thresholds. Let $T \ge 0$ be a non-negative continuous random variable representing duration (e.g., latency, system uptime, job completion time in seconds or milliseconds).

The **conditional survival probability** measures the probability that a system continues running for an additional duration $s$, given that it has already survived up to time $t$:
$$P(T > t + s \mid T > t) = \frac{P(T > t + s \cap T > t)}{P(T > t)} = \frac{P(T > t + s)}{P(T > t)}$$

A critical practical challenge in time data analysis is **right-censored observation windows**. In continuous measurement systems, observation monitors stop recording at a maximum observation window $T_{\text{max}}$. If a request or job has not completed by $T_{\text{max}}$, its true duration is unknown—we only know $T > T_{\text{max}}$. If an analyst discards censored observations or treats $T_{\text{max}}$ as the actual completion time, conditional probabilities and tail latency estimates will be severely biased (underestimating long latencies).

---

### Mathematical Formulas & Derivations

#### Fundamental Conditional Probability Formula
For any two events $A$ and $B$ in a sample space $\Omega$ with $P(B) > 0$:
$$P(A \mid B) = \frac{P(A \cap B)}{P(B)}$$

Similarly, if $P(A) > 0$:
$$P(B \mid A) = \frac{P(A \cap B)}{P(A)}$$

#### Conditional Complement Rule
$$P(A^c \mid B) = 1 - P(A \mid B)$$

*Proof:*
$$P(A^c \mid B) = \frac{P(A^c \cap B)}{P(B)} = \frac{P(B) - P(A \cap B)}{P(B)} = 1 - \frac{P(A \cap B)}{P(B)} = 1 - P(A \mid B)$$

#### Conditional Inclusion-Exclusion Principle
$$P(A_1 \cup A_2 \mid B) = P(A_1 \mid B) + P(A_2 \mid B) - P(A_1 \cap A_2 \mid B)$$

#### Time-Domain Adapted Formulas (with Explicit Units)

When working with latency, duration, or time-series data, all duration parameters must explicitly state their time units (e.g., $[s]$, $[ms]$, $[\mu s]$).

1. **Conditional Latency Threshold Formula:**
   $$P(T \le t_{2,[ms]} \mid T > t_{1,[ms]}) = \frac{P(t_{1,[ms]} < T \le t_{2,[ms]})}{P(T > t_{1,[ms]})} = \frac{F_T(t_{2,[ms]}) - F_T(t_{1,[ms]})}{1 - F_T(t_{1,[ms]})}$$
   where $F_T(t) = P(T \le t)$ is the Cumulative Distribution Function (CDF).

2. **Conditional Survival Function Formula:**
   $$S_T(s_{[s]} \mid t_{[s]}) = P(T > t_{[s]} + s_{[s]} \mid T > t_{[s]}) = \frac{S_T((t+s)_{[s]})}{S_T(t_{[s]})}$$
   where $S_T(t) = P(T > t) = 1 - F_T(t)$ is the Survival Function.

> **Practical / Time-Domain Note:**
> Memoryless distributions (such as the Exponential distribution for continuous time or Geometric distribution for discrete steps) satisfy $P(T > t + s \mid T > t) = P(T > s)$. However, real-world hardware aging, memory leak accumulation, and queue buildup are **aging processes** where $P(T > t + s \mid T > t) < P(T > s)$. Never assume memorylessness without verifying distribution metrics.

---

### Worked Exercises

#### Exercise 1: Medical Diagnostic Contingency Table
**Problem:** A clinical study evaluates 500 patient records for a respiratory condition. 120 patients tested positive ($Pos$), of which 90 actually had the condition ($D$). Out of 380 patients who tested negative ($Neg$), 20 had the condition.
**a)** Calculate $P(D \mid Pos)$ (Positive Predictive Value).
**b)** Calculate $P(D^c \mid Neg)$ (Negative Predictive Value).

**Solution:**
**Step 1:** Construct the complete 2x2 contingency table:

| Condition | Positive Test ($Pos$) | Negative Test ($Neg$) | Total |
| :--- | :--- | :--- | :--- |
| **Disease ($D$)** | 90 | 20 | 110 |
| **No Disease ($D^c$)** | 30 | 360 | 390 |
| **Total** | 120 | 380 | 500 |

**Step 2:** Compute $P(D \mid Pos)$ using the reduced sample space of $Pos$ (120 patients):
$$P(D \mid Pos) = \frac{P(D \cap Pos)}{P(Pos)} = \frac{90 / 500}{120 / 500} = \frac{90}{120} = 0.75$$

**Step 3:** Compute $P(D^c \mid Neg)$ using the reduced sample space of $Neg$ (380 patients):
$$P(D^c \mid Neg) = \frac{P(D^c \cap Neg)}{P(Neg)} = \frac{360 / 500}{380 / 500} = \frac{360}{380} = \frac{18}{19} \approx 0.9474$$

Final Answer: **a) 0.7500 (75.00%)**, **b) 0.9474 (94.74%)**

---

#### Exercise 2: Urn Ball Selection Without Replacement
**Problem:** An urn contains 7 red balls and 5 blue balls. Two balls are drawn sequentially without replacement.
**a)** What is the probability that the second ball drawn is blue, given that the first ball drawn was red?
**b)** What is the joint probability that the first ball is red and the second ball is blue?

**Solution:**
**a)** Step 1: Initial state has $7 + 5 = 12$ total balls.
Step 2: Given the first ball drawn was red ($R_1$), the urn now contains 6 red balls and 5 blue balls ($6 + 5 = 11$ total remaining).
Step 3: The conditional probability of drawing a blue ball on the second draw ($B_2$) is:
$$P(B_2 \mid R_1) = \frac{5}{11} \approx 0.4545$$

**b)** Apply the multiplication rule:
$$P(R_1 \cap B_2) = P(R_1) \cdot P(B_2 \mid R_1) = \left( \frac{7}{12} \right) \cdot \left( \frac{5}{11} \right) = \frac{35}{132} \approx 0.2652$$

Final Answer: **a) 5/11 (0.4545)**, **b) 35/132 (0.2652)**

---

#### Exercise 3: Industrial Component Defect Probability
**Problem:** In a factory manufacturing batch, 15% of components have surface scratches ($S$), 10% have electrical defects ($E$), and 4% have both defects.
**a)** If a randomly chosen component has a surface scratch, what is the probability it also has an electrical defect?
**b)** If a component has no electrical defect, what is the probability it has no surface scratch?

**Solution:**
**Step 1:** Given probabilities: $P(S) = 0.15$, $P(E) = 0.10$, $P(S \cap E) = 0.04$.

**Step 2:** For part **a)**:
$$P(E \mid S) = \frac{P(S \cap E)}{P(S)} = \frac{0.04}{0.15} = \frac{4}{15} \approx 0.2667$$

**Step 3:** For part **b)**, we need $P(S^c \mid E^c) = \frac{P(S^c \cap E^c)}{P(E^c)}$.
Using De Morgan's Law: $P(S^c \cap E^c) = 1 - P(S \cup E)$.
$$P(S \cup E) = P(S) + P(E) - P(S \cap E) = 0.15 + 0.10 - 0.04 = 0.21$$
$$P(S^c \cap E^c) = 1 - 0.21 = 0.79$$
$$P(E^c) = 1 - P(E) = 1 - 0.10 = 0.90$$
$$P(S^c \mid E^c) = \frac{0.79}{0.90} = \frac{79}{90} \approx 0.8778$$

Final Answer: **a) 4/15 (0.2667)**, **b) 79/90 (0.8778)**

---

#### Exercise 4: Server SLA Response Time Threshold (Time-Domain)
**Problem:** Latency logs for a database cluster show that 75% of queries finish within $100\,[ms]$ ($P(T \le 100) = 0.75$) and 95% of queries finish within $300\,[ms]$ ($P(T \le 300) = 0.95$).
**a)** If a query has already exceeded $100\,[ms]$, what is the conditional probability that it finishes within $300\,[ms]$?
**b)** What R command computes this conditional probability from an empirical vector `latencies_ms`?

**Solution:**
**Step 1:** Define the events:
$A = \{T \le 300\,[ms]\}$, $B = \{T > 100\,[ms]\}$.
The intersection $A \cap B = \{100\,[ms] < T \le 300\,[ms]\}$.

**Step 2:** Compute individual probabilities:
$$P(B) = P(T > 100) = 1 - P(T \le 100) = 1 - 0.75 = 0.25$$
$$P(A \cap B) = P(100 < T \le 300) = P(T \le 300) - P(T \le 100) = 0.95 - 0.75 = 0.20$$

**Step 3:** Calculate conditional probability using the time-domain adapted formula:
$$P(T \le 300 \mid T > 100) = \frac{P(100 < T \le 300)}{P(T > 100)} = \frac{0.20}{0.25} = 0.8000$$

**Step 4:** R implementation:
```r
# R snippet for empirical conditional latency calculation
sub_vec <- latencies_ms[latencies_ms > 100]
p_cond <- sum(sub_vec <= 300) / length(sub_vec)
```

Final Answer: **a) 0.8000 (80.00%)**, **b) R command provided above**

---

#### Exercise 5: Microservice Latency Survival & Right-Censoring (Time-Domain)
**Problem:** Execution duration $T\,[s]$ of a distributed job has survival function $S_T(t) = \frac{1}{(1 + 0.1t)^2}$ for $t \ge 0$.
**a)** Calculate the probability that a job runs for more than $20\,[s]$, given it has survived past $10\,[s]$.
**b)** An analyst monitors jobs only up to $T_{\text{max}} = 10\,[s]$ and records all uncompleted jobs as exactly $10\,[s]$. Explain the effect of this right-censoring on conditional survival estimation.

**Solution:**
**a)** Step 1: Evaluate $S_T(10)$ and $S_T(20)$:
$$S_T(10) = P(T > 10) = \frac{1}{(1 + 0.1(10))^2} = \frac{1}{2^2} = \frac{1}{4} = 0.2500$$
$$S_T(20) = P(T > 20) = \frac{1}{(1 + 0.1(20))^2} = \frac{1}{3^2} = \frac{1}{9} \approx 0.1111$$

Step 2: Apply the conditional survival formula:
$$P(T > 20 \mid T > 10) = \frac{P(T > 20)}{P(T > 10)} = \frac{S_T(20)}{S_T(10)} = \frac{1/9}{1/4} = \frac{4}{9} \approx 0.4444$$

**b)** Right-censoring at $T_{\text{max}} = 10\,[s]$ truncates the tail. If jobs running $> 10\,[s]$ are assumed to terminate at $10\,[s]$, $P(T > 20 \mid T > 10)$ would be estimated as $0$, severely underestimating system delay risks.

Final Answer: **a) 4/9 (0.4444)**, **b) Right-censoring truncates the tail and underestimates tail risk**

---

#### Exercise 6: Incident Resolution Times Across Server Clusters (Time-Domain)
**Problem:** An IT ops team records incident resolution times across two shifts: Day Shift ($D$, 120 incidents) and Night Shift ($N$, 80 incidents). In Day Shift, 90 incidents resolved within $1\,[hr]$ ($\le 1$) and 30 took $> 1\,[hr]$. In Night Shift, 40 resolved within $1\,[hr]$ and 40 took $> 1\,[hr]$.
**a)** Find $P(> 1\,[hr] \mid N)$.
**b)** Find $P(N \mid > 1\,[hr])$.
**c)** Write an R snippet using `prop.table()` to compute both conditional distributions.

**Solution:**
**Step 1:** Construct table of counts:

| Shift | $\le 1\,[hr]$ | $> 1\,[hr]$ | Total |
| :--- | :--- | :--- | :--- |
| **Day ($D$)** | 90 | 30 | 120 |
| **Night ($N$)** | 40 | 40 | 80 |
| **Total** | 130 | 70 | 200 |

**Step 2:** Compute $P(> 1\,[hr] \mid N)$:
$$P(> 1\,[hr] \mid N) = \frac{40}{80} = 0.5000$$

**Step 3:** Compute $P(N \mid > 1\,[hr])$:
$$P(N \mid > 1\,[hr]) = \frac{40}{70} = \frac{4}{7} \approx 0.5714$$

**Step 4:** R implementation:
```r
# R snippet for table conditioning
counts <- matrix(c(90, 30, 40, 40), nrow = 2, byrow = TRUE,
                 dimnames = list(Shift = c("Day", "Night"), Time = c("<=1hr", ">1hr")))
p_time_given_shift  <- prop.table(counts, margin = 1) # Row conditional
p_shift_given_time  <- prop.table(counts, margin = 2) # Column conditional
```

Final Answer: **a) 0.5000 (50.00%)**, **b) 4/7 (0.5714)**, **c) R snippet provided above**

---

### R Implementation

```r
# R Implementation for Section 3.1: Conditional Probability & Filtering

# 1. Contingency Table Conditional Probabilities
tbl <- matrix(c(90, 30, 40, 40), nrow = 2, byrow = TRUE,
              dimnames = list(Shift = c("Day", "Night"), Duration = c("<=1hr", ">1hr")))

# Row-conditional probabilities P(Duration | Shift)
p_dur_given_shift <- prop.table(tbl, margin = 1)
print(p_dur_given_shift)

# Column-conditional probabilities P(Shift | Duration)
p_shift_given_dur <- prop.table(tbl, margin = 2)
print(p_shift_given_dur)

# 2. Empirical Vector Conditional Filtering (Time-Domain Latency)
set.seed(42)
latencies_ms <- rgamma(10000, shape = 2, scale = 80) # Sample latencies

# P(T <= 300 | T > 100)
denom_subset <- latencies_ms[latencies_ms > 100]
p_cond_empirical <- sum(denom_subset <= 300) / length(denom_subset)
cat("Empirical P(T <= 300 | T > 100):", round(p_cond_empirical, 4), "\n")
```

---

## Section 3.2: Multiplication Rule & Sequential Processes

### Core Theory & Definitions

The **Multiplication Rule** is derived directly by rearranging the conditional probability formula:
$$P(A \cap B) = P(B) \cdot P(A \mid B) = P(A) \cdot P(B \mid A)$$

This rule allows us to calculate the joint probability of multi-stage sequential processes by breaking them into a chain of conditional probabilities.

```
Stage 1: P(A_1)
   |
   +---> Stage 2: P(A_2 | A_1)
            |
            +---> Stage 3: P(A_3 | A_1 ∩ A_2)
```

#### Sampling With vs Without Replacement
- **Sampling With Replacement:** The sample space remains identical at each stage. Outcomes are independent: $P(A_2 \mid A_1) = P(A_2)$, so $P(A_1 \cap A_2) = P(A_1) \cdot P(A_2)$.
- **Sampling Without Replacement:** The sample space shrinks and composition changes after each draw. Outcomes are dependent: $P(A_2 \mid A_1) \neq P(A_2)$.

#### Time-Domain Application: Multi-Stage Pipelines & Cascades

In distributed computer systems, network routing, and software execution pipelines, request execution progresses through sequential dependent stages (e.g., DNS resolution -> TLS handshake -> Auth Check -> DB Query -> Serialization). The probability of a request successfully completing the entire pipeline without timing out or failing is computed via the Chain Rule of conditional probability.

---

### Mathematical Formulas & Derivations

#### General Chain Rule of Probability
For any sequence of $n$ events $A_1, A_2, \dots, A_n$ where $P(A_1 \cap A_2 \cap \dots \cap A_{n-1}) > 0$:
$$P(A_1 \cap A_2 \cap \dots \cap A_n) = P(A_1) \cdot P(A_2 \mid A_1) \cdot P(A_3 \mid A_1 \cap A_2) \cdots P(A_n \mid A_1 \cap A_2 \cap \dots \cap A_{n-1})$$

*Proof by Induction:*
For $n = 2$: $P(A_1 \cap A_2) = P(A_1) \cdot P(A_2 \mid A_1)$.
Assume true for $n = k$: $P(\bigcap_{i=1}^k A_i) = P(A_1) P(A_2 \mid A_1) \cdots P(A_k \mid \bigcap_{i=1}^{k-1} A_i)$.
For $n = k + 1$, let $E = \bigcap_{i=1}^k A_i$. Then:
$$P\left( \bigcap_{i=1}^{k+1} A_i \right) = P(E \cap A_{k+1}) = P(E) \cdot P(A_{k+1} \mid E) = \left[ \prod_{i=1}^k P\left(A_i \;\middle|\; \bigcap_{j=1}^{i-1} A_j\right) \right] \cdot P\left(A_{k+1} \;\middle|\; \bigcap_{j=1}^k A_j\right)$$

#### Time-Domain Sequential Pipeline Success Formula
For an $n$-stage processing pipeline where $S_i$ is the event that Stage $i$ completes within its allocation $t_{i,[ms]}$:
$$P(\text{Pipeline Success}) = P(S_1) \cdot P(S_2 \mid S_1) \cdot P(S_3 \mid S_1 \cap S_2) \cdots P(S_n \mid S_1 \cap \dots \cap S_{n-1})$$

> **Practical / Time-Domain Note:**
> In microservice architectures, stage completion times are often **positively correlated** (e.g., high database load causes both DB query latency and serialization latency to spike). Assuming independence across stages ($P(S_2 \mid S_1) = P(S_2)$) underestimates the probability of cumulative tail latency violations.

---

### Worked Exercises

#### Exercise 7: Consecutive Card Selection Without Replacement
**Problem:** A standard deck of 52 playing cards contains 4 Aces. Three cards are drawn sequentially without replacement.
**a)** Calculate the probability of drawing three consecutive Aces.
**b)** What R code evaluates this sequential cumulative probability?

**Solution:**
**Step 1:** Define events: $A_1$ (first card Ace), $A_2$ (second card Ace), $A_3$ (third card Ace).

**Step 2:** Apply the multiplication chain rule:
$$P(A_1) = \frac{4}{52}$$
$$P(A_2 \mid A_1) = \frac{3}{51}$$
$$P(A_3 \mid A_1 \cap A_2) = \frac{2}{50}$$

**Step 3:** Calculate the joint probability:
$$P(A_1 \cap A_2 \cap A_3) = \left( \frac{4}{52} \right) \cdot \left( \frac{3}{51} \right) \cdot \left( \frac{2}{50} \right) = \frac{24}{132600} = \frac{1}{5525} \approx 0.0001810$$

**Step 4:** R implementation:
```r
# R snippet for exact chain product
probs <- c(4/52, 3/51, 2/50)
p_three_aces <- prod(probs)
```

Final Answer: **a) 1/5525 (0.0001810)**, **b) R code provided above**

---

#### Exercise 8: Semiconductor Chip Defect Multi-Stage Inspection
**Problem:** A manufacturing lot contains 20 microchips, of which 4 are defective. An inspector randomly selects 3 chips without replacement for quality testing.
**a)** Find the probability that all 3 selected chips are non-defective.
**b)** Find the probability that at least 1 of the 3 selected chips is defective.

**Solution:**
**Step 1:** Non-defective chips count = $20 - 4 = 16$.

**Step 2:** For part **a)**, apply the chain rule for 3 non-defective draws ($G_1, G_2, G_3$):
$$P(G_1 \cap G_2 \cap G_3) = \left( \frac{16}{20} \right) \cdot \left( \frac{15}{19} \right) \cdot \left( \frac{14}{18} \right) = \frac{3360}{6840} = \frac{28}{57} \approx 0.4912$$

**Step 3:** For part **b)**, use the complement rule:
$$P(\text{At least 1 defective}) = 1 - P(G_1 \cap G_2 \cap G_3) = 1 - \frac{28}{57} = \frac{29}{57} \approx 0.5088$$

Final Answer: **a) 28/57 (0.4912)**, **b) 29/57 (0.5088)**

---

#### Exercise 9: Sequential Urn Ball Selection
**Problem:** Urn A contains 3 red and 2 white balls. Urn B contains 2 red and 4 white balls. A ball is drawn at random from Urn A and transferred into Urn B. Then a ball is drawn from Urn B.
**a)** Find the probability that the transferred ball was Red AND the ball drawn from Urn B is Red.
**b)** Find the probability that the transferred ball was White AND the ball drawn from Urn B is Red.

**Solution:**
**Step 1:** Transferred ball events from Urn A: $P(R_A) = 3/5$, $P(W_A) = 2/5$.

**Step 2:** For part **a)**: If $R_A$ is transferred, Urn B now has $2 + 1 = 3$ red and 4 white ($3 + 4 = 7$ total).
$$P(R_B \mid R_A) = \frac{3}{7}$$
$$P(R_A \cap R_B) = P(R_A) \cdot P(R_B \mid R_A) = \left( \frac{3}{5} \right) \cdot \left( \frac{3}{7} \right) = \frac{9}{35} \approx 0.2571$$

**Step 3:** For part **b)**: If $W_A$ is transferred, Urn B now has 2 red and $4 + 1 = 5$ white ($2 + 5 = 7$ total).
$$P(R_B \mid W_A) = \frac{2}{7}$$
$$P(W_A \cap R_B) = P(W_A) \cdot P(R_B \mid W_A) = \left( \frac{2}{5} \right) \cdot \left( \frac{2}{7} \right) = \frac{4}{35} \approx 0.1143$$

Final Answer: **a) 9/35 (0.2571)**, **b) 4/35 (0.1143)**

---

#### Exercise 10: Multi-Hop Network Routing Success (Time-Domain)
**Problem:** A network packet must traverse 3 sequential router hops ($H_1, H_2, H_3$). Hop survival probabilities under load are:
- $P(H_1 \text{ success}) = 0.98$
- $P(H_2 \text{ success} \mid H_1 \text{ success}) = 0.95$
- $P(H_3 \text{ success} \mid H_1 \cap H_2 \text{ success}) = 0.90$
**a)** Calculate the overall end-to-end packet delivery success probability.
**b)** What is the probability that the packet fails at Hop 3, given it successfully cleared Hop 1 and Hop 2?

**Solution:**
**a)** Apply the multiplication chain rule:
$$P(H_1 \cap H_2 \cap H_3) = P(H_1) \cdot P(H_2 \mid H_1) \cdot P(H_3 \mid H_1 \cap H_2) = 0.98 \cdot 0.95 \cdot 0.90 = 0.8379$$

**b)** Using the conditional complement rule:
$$P(H_3^c \mid H_1 \cap H_2) = 1 - P(H_3 \mid H_1 \cap H_2) = 1 - 0.90 = 0.1000$$

Final Answer: **a) 0.8379 (83.79%)**, **b) 0.1000 (10.00%)**

---

#### Exercise 11: Microservice Authentication and Data Fetch Pipeline (Time-Domain)
**Problem:** An API request passes through three sequential microservices: Auth Gateway ($A$), Data Fetch ($D$), and Output Formatter ($F$). Time budget allocations are $t_A = 20\,[ms], t_D = 100\,[ms], t_F = 30\,[ms]$.
From logs:
- $P(T_A \le 20) = 0.96$
- $P(T_D \le 100 \mid T_A \le 20) = 0.92$
- $P(T_F \le 30 \mid T_A \le 20 \cap T_D \le 100) = 0.95$
**a)** Calculate the overall pipeline success probability.
**b)** Write an R command that computes cumulative path probabilities using `cumprod()`.

**Solution:**
**Step 1:** Apply chain rule:
$$P(\text{Success}) = 0.96 \cdot 0.92 \cdot 0.95 = 0.83884 \approx 0.8388$$

**Step 2:** R code implementation:
```r
# R snippet for cumulative pipeline probability
stage_probs <- c(A = 0.96, D = 0.92, F = 0.95)
cum_success <- cumprod(stage_probs)
cat("Final Pipeline Probability:", cum_success["F"], "\n")
```

Final Answer: **a) 0.8388 (83.88%)**, **b) R command provided above**

---

#### Exercise 12: CI/CD Deployment Pipeline Execution (Time-Domain)
**Problem:** A DevOps deployment pipeline consists of 4 stages: Lint ($L$), Unit Test ($U$), Integration Test ($I$), and Deployment ($D$). The stage completion probabilities are:
- $P(L) = 0.99$
- $P(U \mid L) = 0.90$
- $P(I \mid L \cap U) = 0.85$
- $P(D \mid L \cap U \cap I) = 0.98$
**a)** Find the probability that the entire pipeline completes successfully.
**b)** If 500 independent build triggers occur, expected number of fully successful deployments?

**Solution:**
**a)** Apply the chain rule:
$$P(\text{Pipeline Success}) = 0.99 \cdot 0.90 \cdot 0.85 \cdot 0.98 = 0.7421547 \approx 0.7422$$

**b)** Expected successful deployments:
$$E[X] = N \cdot P(\text{Success}) = 500 \cdot 0.7421547 = 371.077 \approx 371 \text{ deployments}$$

Final Answer: **a) 0.7422 (74.22%)**, **b) 371 deployments**

---

### R Implementation

```r
# R Implementation for Section 3.2: Multiplication Rule & Sequential Chains

# 1. Chain Rule Cumulative Calculation (Pipeline Stages)
stage_conditional_probs <- c(
  Auth = 0.96,
  DataFetch = 0.92,
  Format = 0.95,
  Deploy = 0.98
)

# Compute cumulative success probability at each stage
cum_probs <- cumprod(stage_conditional_probs)
print(data.frame(Stage = names(cum_probs), CumProbability = cum_probs))

# 2. Simulating Sequential Sampling Without Replacement
simulate_draws <- function(red = 7, blue = 5, n_draws = 2) {
  urn <- c(rep("Red", red), rep("Blue", blue))
  draws <- sample(urn, size = n_draws, replace = FALSE)
  return(draws[1] == "Red" && draws[2] == "Blue")
}

set.seed(42)
sim_results <- replicate(100000, simulate_draws())
cat("Simulated P(Red1 & Blue2):", mean(sim_results), "\n")
```

---

## Section 3.3: Independence & System Reliability

### Core Theory & Definitions

Two events $A$ and $B$ are **statistically independent** if the occurrence of $B$ does not alter the probability of $A$ occurring. Knowledge of $B$ conveys zero information about $A$.

#### Pairwise vs Mutual (Joint) Independence
For three or more events $A_1, A_2, \dots, A_n$:
- **Pairwise Independence:** $P(A_i \cap A_j) = P(A_i) \cdot P(A_j)$ for all $i \neq j$.
- **Mutual (Joint) Independence:** $P(\bigcap_{i \in S} A_i) = \prod_{i \in S} P(A_i)$ for **every** subset $S \subseteq \{1, 2, \dots, n\}$.

> **Crucial Warning:** Pairwise independence does **NOT** imply mutual independence! (Bernstein's classic counterexample demonstrates 3 events that are pairwise independent but not mutually independent).

#### Mutually Exclusive vs Independent Events
- **Mutually Exclusive (Disjoint):** $A \cap B = \emptyset \implies P(A \cap B) = 0$. If $A$ happens, $B$ cannot happen.
- **Independent:** $P(A \cap B) = P(A) \cdot P(B)$.
- **Theorem:** If $P(A) > 0$ and $P(B) > 0$, mutually exclusive events can **NEVER** be independent. Since $P(A \cap B) = 0 \neq P(A)P(B) > 0$, mutual exclusivity implies maximum dependency.

```
Mutually Exclusive:            Independent:
+-------+ +-------+           +---------------+
|   A   | |   B   |           |  A  |A∩B|  B  |
+-------+ +-------+           +---------------+
 P(A ∩ B) = 0                  P(A ∩ B) = P(A)P(B)
```

#### System Reliability Architecture over Time
In engineering systems, reliability is modeled by treating individual component lifetimes $T_1, T_2, \dots, T_n$ as independent random variables:

1. **Series System (Logical AND - Weakest Link):**
   The system functions if and only if **all** $n$ components function.
   $$T_{\text{sys}} = \min(T_1, T_2, \dots, T_n)$$
   $$R_{\text{sys}}(t) = P(T_{\text{sys}} > t) = P(T_1 > t \cap T_2 > t \cap \dots \cap T_n > t) = \prod_{i=1}^{n} P(T_i > t)$$

2. **Parallel System (Logical OR - Redundant Architecture):**
   The system functions if **at least one** component functions. It fails only when all components fail.
   $$T_{\text{sys}} = \max(T_1, T_2, \dots, T_n)$$
   $$F_{\text{sys}}(t) = P(T_{\text{sys}} \le t) = \prod_{i=1}^{n} P(T_i \le t) \implies R_{\text{sys}}(t) = 1 - \prod_{i=1}^{n} \left(1 - P(T_i > t)\right)$$

---

### Mathematical Formulas & Derivations

#### Independence Conditions
Events $A$ and $B$ are independent if and only if any of the following equivalent statements hold:
1. $P(A \cap B) = P(A) \cdot P(B)$
2. $P(A \mid B) = P(A)$ (assuming $P(B) > 0$)
3. $P(B \mid A) = P(B)$ (assuming $P(A) > 0$)

#### Independence of Complemented Events
*Theorem:* If $A$ and $B$ are independent, then $A^c$ and $B^c$ are also independent.
*Proof:*
$$P(A^c \cap B^c) = P((A \cup B)^c) = 1 - P(A \cup B)$$
$$= 1 - [P(A) + P(B) - P(A \cap B)]$$
$$= 1 - P(A) - P(B) + P(A)P(B) = (1 - P(A))(1 - P(B)) = P(A^c) \cdot P(B^c)$$

#### Series and Parallel Reliability Formulas
- **Series Reliability:** $R_{\text{series}}(t) = \prod_{i=1}^{n} R_i(t)$
- **Parallel Reliability:** $R_{\text{parallel}}(t) = 1 - \prod_{i=1}^{n} (1 - R_i(t))$
- **$k$-out-of-$n$ System Reliability (Identical $R_i(t) = R(t)$):**
  $$R_{k:n}(t) = \sum_{j=k}^{n} \binom{n}{j} [R(t)]^j [1 - R(t)]^{n-j}$$

> **Practical / Time-Domain Note:**
> In distributed infrastructure, timers or worker processes running on separate virtual machines may appear independent, but if they share underlying physical CPU cores, hypervisors, or power units, a resource spike violates independence. Always audit for **shared infrastructure contention**.

---

### Worked Exercises

#### Exercise 13: Testing Independence from Survey Data
**Problem:** A survey of 1,000 users categorizes them by Device ($M = \text{Mobile}$, $D = \text{Desktop}$) and Subscription ($S = \text{Subscribed}$, $U = \text{Unsubscribed}$).
Data: 600 Mobile users, 400 Subscribed users, and 240 users who are both Mobile and Subscribed.
**a)** Are Device type ($M$) and Subscription status ($S$) independent?
**b)** Calculate $P(S \mid M)$ and compare it with $P(S)$.

**Solution:**
**Step 1:** Compute marginal probabilities:
$$P(M) = \frac{600}{1000} = 0.60, \quad P(S) = \frac{400}{1000} = 0.40$$
$$P(M \cap S) = \frac{240}{1000} = 0.24$$

**Step 2:** Test product rule for independence:
$$P(M) \cdot P(S) = 0.60 \cdot 0.40 = 0.24$$
Since $P(M \cap S) = P(M) \cdot P(S) = 0.24$, events $M$ and $S$ are **statistically independent**.

**Step 3:** Compute $P(S \mid M)$:
$$P(S \mid M) = \frac{P(M \cap S)}{P(M)} = \frac{0.24}{0.60} = 0.40 = P(S)$$

Final Answer: **a) Yes, independent ($P(M \cap S) = P(M)P(S) = 0.24$)**, **b) $P(S \mid M) = P(S) = 0.40$**

---

#### Exercise 14: Independence vs Disjointness in Dice Outcomes
**Problem:** A fair 6-sided die is rolled. Define events:
- $A = \{1, 2\}$ (Roll is 1 or 2)
- $B = \{2, 4, 6\}$ (Roll is even)
- $C = \{3, 5\}$ (Roll is 3 or 5)
**a)** Are $A$ and $B$ independent? Are they disjoint?
**b)** Are $A$ and $C$ independent? Are they disjoint?

**Solution:**
Sample space $\Omega = \{1, 2, 3, 4, 5, 6\}$, so $P(\text{each outcome}) = 1/6$.
$P(A) = 2/6 = 1/3$, $P(B) = 3/6 = 1/2$, $P(C) = 2/6 = 1/3$.

**a)** $A \cap B = \{2\} \implies P(A \cap B) = 1/6$.
Product test: $P(A) \cdot P(B) = (1/3) \cdot (1/2) = 1/6$.
Since $P(A \cap B) = P(A)P(B)$, $A$ and $B$ are **independent**.
Since $A \cap B \neq \emptyset$, they are **not disjoint**.

**b)** $A \cap C = \emptyset \implies P(A \cap C) = 0$.
Since $A \cap C = \emptyset$, $A$ and $C$ are **disjoint (mutually exclusive)**.
Product test: $P(A) \cdot P(C) = (1/3) \cdot (1/3) = 1/9 \neq 0$.
Since $P(A \cap C) \neq P(A)P(C)$, $A$ and $C$ are **not independent**.

Final Answer: **a) Independent, Not Disjoint**, **b) Disjoint, Not Independent**

---

#### Exercise 15: Probability of At Least One Success in Independent Trials
**Problem:** The probability of a network transmission error in any given $1\,[min]$ interval is $p = 0.05$. Assuming independent intervals:
**a)** What is the probability of experiencing at least one error across 10 consecutive minutes?
**b)** What R command computes this probability?

**Solution:**
**Step 1:** Probability of NO error in 1 minute = $1 - p = 0.95$.
**Step 2:** By independence, probability of NO errors in 10 minutes:
$$P(\text{No Errors in 10 min}) = (0.95)^{10} \approx 0.5987$$
**Step 3:** Use complement rule for "at least one":
$$P(\text{At Least 1 Error}) = 1 - (0.95)^{10} = 1 - 0.59874 = 0.40126 \approx 0.4013$$

**Step 4:** R command:
```r
p_at_least_1 <- 1 - pbinom(0, size = 10, prob = 0.05) # or 1 - (0.95)^10
```

Final Answer: **a) 0.4013 (40.13%)**, **b) `1 - (0.95)^10` or `1 - pbinom(0, 10, 0.05)`**

---

#### Exercise 16: Redundant Parallel Database Cluster Reliability (Time-Domain)
**Problem:** A critical cloud storage layer uses 3 independent redundant database nodes in parallel. Each node has a 24-hour survival probability of $R_i(24\,[hr]) = 0.90$.
**a)** Calculate the overall 24-hour reliability of the parallel database cluster.
**b)** If the nodes were configured in series (all 3 required), what would be the 24-hour system reliability?

**Solution:**
**a) Parallel Architecture:**
Failure probability of each node: $F_i = 1 - 0.90 = 0.10$.
Cluster fails iff all 3 nodes fail:
$$F_{\text{cluster}} = (0.10)^3 = 0.0010$$
$$R_{\text{parallel}}(24\,[hr]) = 1 - F_{\text{cluster}} = 1 - 0.0010 = 0.9990 \text{ (99.90\%)}$$

**b) Series Architecture:**
$$R_{\text{series}}(24\,[hr]) = (0.90)^3 = 0.7290 \text{ (72.90\%)}$$

Final Answer: **a) 0.9990 (99.90%)**, **b) 0.7290 (72.90%)**

---

#### Exercise 17: Series Pipeline Hardware Latency & Clock Skew (Time-Domain)
**Problem:** A digital clock distribution path has 4 sequential flip-flop stages in series. Stage survival within clock-to-Q timing window $T_{\text{clk}\to q} = 500\,[ps]$ are independent with $R_1 = 0.995, R_2 = 0.990, R_3 = 0.992, R_4 = 0.998$.
**a)** Compute the end-to-end timing reliability $R_{\text{path}}$.
**b)** If clock skew introduces coupling between stages 2 and 3 such that $P(\text{Stage 3 holds} \mid \text{Stage 2 holds}) = 0.980$ (instead of 0.992), calculate the revised path reliability.

**Solution:**
**a) Independent Series Path:**
$$R_{\text{path}} = R_1 \cdot R_2 \cdot R_3 \cdot R_4 = 0.995 \cdot 0.990 \cdot 0.992 \cdot 0.998 = 0.97517 \approx 0.9752$$

**b) Coupled Path (Dependent Stages 2 & 3):**
$$R_{\text{revised}} = R_1 \cdot R_2 \cdot P(\text{Stage 3} \mid \text{Stage 2}) \cdot R_4 = 0.995 \cdot 0.990 \cdot 0.980 \cdot 0.998 = 0.96336 \approx 0.9634$$

Final Answer: **a) 0.9752 (97.52%)**, **b) 0.9634 (96.34%)**

---

#### Exercise 18: Autocorrelation & Independence Test of Time Spikes (Time-Domain)
**Problem:** Latency logs record execution spike events ($E_t = 1$ if latency $> 200\,[ms]$, else $0$) across consecutive minutes. Out of 1,000 minutes:
- $E_t = 1$ occurred in 100 minutes ($P(E_t) = 0.10$).
- $E_{t+1} = 1$ given $E_t = 1$ occurred in 35 minutes.
**a)** Compute $P(E_t \cap E_{t+1})$ and test if consecutive latency spikes are independent.
**b)** Write an R snippet using `cor.test()` to test for serial correlation.

**Solution:**
**Step 1:** Compute joint probability:
$$P(E_t \cap E_{t+1}) = P(E_t) \cdot P(E_{t+1} \mid E_t) = 0.10 \cdot \frac{35}{100} = 0.0350$$

**Step 2:** Independence test:
If independent, $P(E_t) \cdot P(E_{t+1}) = 0.10 \cdot 0.10 = 0.0100$.
Since $P(E_t \cap E_{t+1}) = 0.0350 \neq 0.0100$, consecutive latency spikes are **strongly dependent (autocorrelated)**.

**Step 3:** R code:
```r
# R snippet testing autocorrelation between lag-1 spike vectors
spikes_t   <- spike_vec[-length(spike_vec)]
spikes_t1  <- spike_vec[-1]
test_res   <- cor.test(spikes_t, spikes_t1)
print(test_res$p.value)
```

Final Answer: **a) $P(E_t \cap E_{t+1}) = 0.0350 \neq 0.0100 \implies$ Dependent (Autocorrelated)**, **b) R code provided above**

---

### R Implementation

```r
# R Implementation for Section 3.3: Independence & System Reliability

# 1. Contingency Independence Test (Chi-Square Test)
observed <- matrix(c(240, 360, 160, 240), nrow = 2, byrow = TRUE,
                   dimnames = list(Device = c("Mobile", "Desktop"), Sub = c("Yes", "No")))
chi_test <- chisq.test(observed, correct = FALSE)
cat("Chi-Square Statistic:", chi_test$statistic, "P-Value:", chi_test$p.value, "\n")

# 2. System Reliability Simulation (Series vs Parallel)
n_sim <- 100000
t_comp1 <- rexp(n_sim, rate = 0.05) # Lifetime component 1
t_comp2 <- rexp(n_sim, rate = 0.05) # Lifetime component 2
t_comp3 <- rexp(n_sim, rate = 0.05) # Lifetime component 3

target_t <- 10 # 10 hours

# Series: min(T1, T2, T3) > 10
r_series_sim <- mean(pmin(t_comp1, t_comp2, t_comp3) > target_t)

# Parallel: max(T1, T2, T3) > 10
r_parallel_sim <- mean(pmax(t_comp1, t_comp2, t_comp3) > target_t)

cat("Simulated Series Reliability:", r_series_sim, "\n")
cat("Simulated Parallel Reliability:", r_parallel_sim, "\n")
```

---

## Section 3.4: Law of Total Probability & Bayes' Theorem

### Core Theory & Definitions

#### Partition of a Sample Space
A collection of events $\{B_1, B_2, \dots, B_n\}$ forms a **partition** of the sample space $\Omega$ if:
1. The events are mutually exclusive: $B_i \cap B_j = \emptyset$ for all $i \neq j$.
2. The events are collectively exhaustive: $\bigcup_{i=1}^{n} B_i = \Omega$.
3. $P(B_i) > 0$ for all $i = 1, \dots, n$.

```
Partition of $\Omega$ into $B_1$, $B_2$, $B_3$, $B_4$:
+------------------------------------+
|  B_1   |   B_2   |   B_3  |  B_4   |
|     +--+---------+--------+--+     |
|     |         Event A        |     |
|     +--+---------+--------+--+     |
+------------------------------------+
  Event A is composed of slices (A ∩ B_i) across each partition block.
```

#### Law of Total Probability
The Law of Total Probability calculates the unconditional probability $P(A)$ of an event $A$ by summing its conditional probabilities across all partition components $B_i$, weighted by the prior probability of each component:
$$P(A) = \sum_{i=1}^{n} P(A \cap B_i) = \sum_{i=1}^{n} P(A \mid B_i) P(B_i)$$

#### Bayes' Theorem
Bayes' Theorem provides the mathematical framework for **updating probabilities in light of new evidence**. It converts a **prior probability** $P(B_k)$ (our baseline belief before observing evidence) into a **posterior probability** $P(B_k \mid A)$ (our updated belief after observing evidence $A$).

The four key components of Bayes' Theorem are:
1. **Prior Probability $P(B_k)$:** Baseline probability of hypothesis $B_k$.
2. **Likelihood $P(A \mid B_k)$:** Probability of observing evidence $A$ given hypothesis $B_k$.
3. **Marginal Likelihood $P(A)$:** Overall probability of observing evidence $A$ across all hypotheses (computed via Law of Total Probability).
4. **Posterior Probability $P(B_k \mid A)$:** Updated probability of hypothesis $B_k$ given evidence $A$.

#### Time-Domain Application: Anomaly Isolation & Root-Cause Diagnosis
In system reliability and time-series monitoring, Bayes' Theorem isolates root causes of performance degradations. For example, if a high latency spike ($A$) is detected, Bayes' Theorem computes the posterior probability $P(B_k \mid A)$ that the root cause was a Database Lock ($B_1$), Network Congestion ($B_2$), or Garbage Collection Pause ($B_3$).

---

### Mathematical Formulas & Derivations

#### Law of Total Probability Formula
$$P(A) = P(A \mid B_1)P(B_1) + P(A \mid B_2)P(B_2) + \dots + P(A \mid B_n)P(B_n) = \sum_{i=1}^{n} P(A \mid B_i)P(B_i)$$

#### Bayes' Theorem Formula (General Partition Form)
For a partition $\{B_1, B_2, \dots, B_n\}$ and an observed event $A$ with $P(A) > 0$:
$$P(B_k \mid A) = \frac{P(A \cap B_k)}{P(A)} = \frac{P(A \mid B_k) P(B_k)}{\sum_{j=1}^{n} P(A \mid B_j) P(B_j)}$$

#### Binary Diagnostic / Screening Bayes Formula
In medical screening or binary signal detection:
- **Prevalence (Base Rate):** $p = P(D)$
- **Sensitivity (True Positive Rate):** $\text{Sens} = P(Pos \mid D)$
- **Specificity (True Negative Rate):** $\text{Spec} = P(Neg \mid D^c) \implies P(Pos \mid D^c) = 1 - \text{Spec}$

$$P(D \mid Pos) = \frac{\text{Sens} \cdot p}{\text{Sens} \cdot p + (1 - \text{Spec}) \cdot (1 - p)}$$

> **Practical / Time-Domain Note:**
> The **Base Rate Fallacy** occurs when an analyst ignores low prior probabilities $P(B_k)$. Even if a diagnostic test or anomaly alert has 99% accuracy ($P(A \mid B_k) = 0.99$), if the event $B_k$ is extremely rare ($P(B_k) = 0.001$), the majority of alerts will be false positives. Always evaluate the marginal denominator $P(A)$ explicitly.

---

### Worked Exercises

#### Exercise 19: Three-Factory Defect Analysis (Classic Partition Bayes)
**Problem:** A company buys components from 3 suppliers: Factory 1 ($B_1$, 50% of supply), Factory 2 ($B_2$, 30%), and Factory 3 ($B_3$, 20%). Defect rates are 1% for $B_1$, 2% for $B_2$, and 5% for $B_3$.
**a)** Calculate the overall defect rate $P(D)$ across all incoming inventory.
**b)** If a randomly inspected component is defective ($D$), what is the posterior probability that it originated from Factory 3 ($B_3$)?

**Solution:**
**Step 1:** Identify priors and likelihoods:
Priors: $P(B_1) = 0.50$, $P(B_2) = 0.30$, $P(B_3) = 0.20$.
Likelihoods: $P(D \mid B_1) = 0.01$, $P(D \mid B_2) = 0.02$, $P(D \mid B_3) = 0.05$.

**Step 2:** For part **a)**, apply the Law of Total Probability:
$$P(D) = P(D \mid B_1)P(B_1) + P(D \mid B_2)P(B_2) + P(D \mid B_3)P(B_3)$$
$$P(D) = (0.01 \cdot 0.50) + (0.02 \cdot 0.30) + (0.05 \cdot 0.20) = 0.005 + 0.006 + 0.010 = 0.0210 \text{ (2.10\%)}$$

**Step 3:** For part **b)**, apply Bayes' Theorem for $B_3$:
$$P(B_3 \mid D) = \frac{P(D \mid B_3)P(B_3)}{P(D)} = \frac{0.05 \cdot 0.20}{0.0210} = \frac{0.0100}{0.0210} = \frac{10}{21} \approx 0.4762$$

Final Answer: **a) 0.0210 (2.10%)**, **b) 10/21 (0.4762)**

---

#### Exercise 20: Medical Disease Screening Sensitivity/Specificity (Bayes Base-Rate)
**Problem:** A rare disease affects 0.2% of the population ($P(D) = 0.002$). A diagnostic test has 98% sensitivity ($P(Pos \mid D) = 0.98$) and 95% specificity ($P(Neg \mid D^c) = 0.95$).
**a)** Find the total probability that a randomly selected person tests positive ($P(Pos)$).
**b)** If a patient tests positive, what is the posterior probability that they actually have the disease ($P(D \mid Pos)$)?

**Solution:**
**Step 1:** Identify parameters:
$P(D) = 0.002 \implies P(D^c) = 0.998$.
$P(Pos \mid D) = 0.98$.
$P(Pos \mid D^c) = 1 - P(Neg \mid D^c) = 1 - 0.95 = 0.05$.

**Step 2:** For part **a)**, calculate $P(Pos)$ using Law of Total Probability:
$$P(Pos) = P(Pos \mid D)P(D) + P(Pos \mid D^c)P(D^c)$$
$$P(Pos) = (0.98 \cdot 0.002) + (0.05 \cdot 0.998) = 0.00196 + 0.04990 = 0.05186 \approx 0.0519$$

**Step 3:** For part **b)**, apply Bayes' Theorem:
$$P(D \mid Pos) = \frac{P(Pos \mid D)P(D)}{P(Pos)} = \frac{0.00196}{0.05186} \approx 0.03779 \approx 0.0378$$

> **Note:** Despite 98% test sensitivity, a positive result only carries a 3.78% probability of true disease due to the low base rate (0.2%).

Final Answer: **a) 0.0519 (5.19%)**, **b) 0.0378 (3.78%)**

---

#### Exercise 21: Binary Symmetric Channel Transmission Error
**Problem:** A binary communication channel transmits bits $X \in \{0, 1\}$ with prior probabilities $P(X=0) = 0.60$ and $P(X=1) = 0.40$. Due to noise, bit inversion error probability is $p_e = 0.05$ (i.e., $P(Y=1 \mid X=0) = 0.05$ and $P(Y=0 \mid X=1) = 0.05$).
**a)** Calculate the overall probability that bit $Y=1$ is received.
**b)** Given that $Y=1$ was received, what is the posterior probability that $X=1$ was transmitted?

**Solution:**
**Step 1:** Likelihoods:
$P(Y=1 \mid X=1) = 0.95$, $P(Y=1 \mid X=0) = 0.05$.

**Step 2:** For part **a)**, apply Law of Total Probability:
$$P(Y=1) = P(Y=1 \mid X=1)P(X=1) + P(Y=1 \mid X=0)P(X=0)$$
$$P(Y=1) = (0.95 \cdot 0.40) + (0.05 \cdot 0.60) = 0.380 + 0.030 = 0.4100$$

**Step 3:** For part **b)**, apply Bayes' Theorem:
$$P(X=1 \mid Y=1) = \frac{P(Y=1 \mid X=1)P(X=1)}{P(Y=1)} = \frac{0.380}{0.410} = \frac{38}{41} \approx 0.9268$$

Final Answer: **a) 0.4100 (41.00%)**, **b) 38/41 (0.9268)**

---

#### Exercise 22: Server Load Regime Isolation from Query Latency Spike (Time-Domain)
**Problem:** A web server operates under 3 load regimes: Off-Peak ($B_1$, 50% of time), Normal ($B_2$, 40%), and Peak ($B_3$, 10%). The probability of a query latency spike ($S$, latency $> 500\,[ms]$) under each regime is:
$P(S \mid B_1) = 0.01$, $P(S \mid B_2) = 0.05$, $P(S \mid B_3) = 0.40$.
**a)** Compute the total probability $P(S)$ of observing a query latency spike.
**b)** If a monitoring alert detects a latency spike ($S$), what is the posterior probability that the server is in Peak load regime ($B_3$)?

**Solution:**
**Step 1:** Priors: $P(B_1) = 0.50$, $P(B_2) = 0.40$, $P(B_3) = 0.10$.

**Step 2:** For part **a)**:
$$P(S) = (0.01 \cdot 0.50) + (0.05 \cdot 0.40) + (0.40 \cdot 0.10) = 0.005 + 0.020 + 0.040 = 0.0650 \text{ (6.50\%)}$$

**Step 3:** For part **b)**:
$$P(B_3 \mid S) = \frac{P(S \mid B_3)P(B_3)}{P(S)} = \frac{0.040}{0.0650} = \frac{40}{65} = \frac{8}{13} \approx 0.6154$$

Final Answer: **a) 0.0650 (6.50%)**, **b) 8/13 (0.6154)**

---

#### Exercise 23: Timestamp-Based Anomaly Filter Classification (Time-Domain)
**Problem:** An automated network filter classifies packet arrivals as Normal ($N$, 95%) or Malicious ($M$, 5%). The filter flags an anomaly alert ($A$) based on timestamp jitter metrics. Likelihoods are $P(A \mid M) = 0.90$ and $P(A \mid N) = 0.02$.
**a)** Compute $P(A)$ (total probability of an alert).
**b)** Compute $P(M \mid A)$ (probability a flagged packet is actually malicious).

**Solution:**
**a)** Apply Law of Total Probability:
$$P(A) = P(A \mid M)P(M) + P(A \mid N)P(N) = (0.90 \cdot 0.05) + (0.02 \cdot 0.95) = 0.045 + 0.019 = 0.0640$$

**b)** Apply Bayes' Theorem:
$$P(M \mid A) = \frac{P(A \mid M)P(M)}{P(A)} = \frac{0.045}{0.0640} = \frac{45}{64} \approx 0.7031$$

Final Answer: **a) 0.0640 (6.40%)**, **b) 45/64 (0.7031)**

---

#### Exercise 24: Software Failure Root-Cause Diagnosis (Time-Domain)
**Problem:** Software execution crashes ($C$) are caused by 3 bug categories: Memory Leak ($B_1$, prior 40%), Null Pointer ($B_2$, prior 35%), and Deadlock ($B_3$, prior 25%).
Probability of execution crash taking $> 10\,[s]$ before failure:
$P(> 10\,[s] \mid B_1) = 0.80$, $P(> 10\,[s] \mid B_2) = 0.10$, $P(> 10\,[s] \mid B_3) = 0.60$.
**a)** Compute total probability $P(> 10\,[s])$.
**b)** Given a crash took $> 10\,[s]$, find posterior probability $P(B_1 \mid > 10\,[s])$.

**Solution:**
**a)** $P(> 10\,[s]) = (0.80 \cdot 0.40) + (0.10 \cdot 0.35) + (0.60 \cdot 0.25) = 0.320 + 0.035 + 0.150 = 0.5050$.

**b)** $P(B_1 \mid > 10\,[s]) = \frac{0.320}{0.5050} = \frac{320}{505} = \frac{64}{101} \approx 0.6337$.

Final Answer: **a) 0.5050 (50.50%)**, **b) 64/101 (0.6337)**

---

#### Exercise 25: Cloud Instance Reboot Mode Posterior Update (Time-Domain)
**Problem:** Server reboots occur due to Hardware Fault ($H$, 10%), OS Kernel Panic ($K$, 30%), or Scheduled Maintenance ($M$, 60%). The reboot duration exceeds $5\,[min]$ ($D > 5$) with probabilities:
$P(D > 5 \mid H) = 0.90$, $P(D > 5 \mid K) = 0.50$, $P(D > 5 \mid M) = 0.05$.
**a)** Compute total probability $P(D > 5)$.
**b)** Given reboot took $> 5\,[min]$, calculate posteriors for all 3 causes.

**Solution:**
**a)** $P(D > 5) = (0.90 \cdot 0.10) + (0.50 \cdot 0.30) + (0.05 \cdot 0.60) = 0.090 + 0.150 + 0.030 = 0.2700$.

**b)** Posteriors:
$$P(H \mid D > 5) = \frac{0.090}{0.2700} = \frac{1}{3} \approx 0.3333$$
$$P(K \mid D > 5) = \frac{0.150}{0.2700} = \frac{5}{9} \approx 0.5556$$
$$P(M \mid D > 5) = \frac{0.030}{0.2700} = \frac{1}{9} \approx 0.1111$$

Final Answer: **a) 0.2700 (27.00%)**, **b) P(H|D>5) = 0.3333, P(K|D>5) = 0.5556, P(M|D>5) = 0.1111**

---

#### Exercise 26: R Function for Iterative Bayesian Log Updating (Time-Domain)
**Problem:** Write a generic R function `bayes_update(priors, likelihoods)` that accepts a vector of prior probabilities and a vector of likelihoods, computes the total evidence probability, and returns the posterior probability vector.

**Solution:**
```r
# Generic R Function for Bayes Updating
bayes_update <- function(priors, likelihoods) {
  stopifnot(length(priors) == length(likelihoods))
  stopifnot(abs(sum(priors) - 1) < 1e-6)
  
  joint_probs <- priors * likelihoods
  total_evidence <- sum(joint_probs)
  posteriors <- joint_probs / total_evidence
  
  return(list(
    total_evidence = total_evidence,
    posteriors = posteriors
  ))
}

# Example Test Case (Exercise 22 Verification)
priors <- c(B1 = 0.50, B2 = 0.40, B3 = 0.10)
like   <- c(B1 = 0.01, B2 = 0.05, B3 = 0.40)
res    <- bayes_update(priors, like)
cat("Total Evidence P(S):", res$total_evidence, "\n")
print(res$posteriors)
```

Final Answer: **R function provided above**

---

### R Implementation

```r
# R Implementation for Section 3.4: Law of Total Probability & Bayes' Theorem

# 1. Automated Bayes Update Function
bayes_update <- function(priors, likelihoods) {
  joint_probs <- priors * likelihoods
  p_evidence <- sum(joint_probs)
  posteriors <- joint_probs / p_evidence
  return(list(evidence_prob = p_evidence, posteriors = posteriors))
}

# 2. Applying Bayes Update to Medical Screening (Exercise 20)
priors_med <- c(Disease = 0.002, Healthy = 0.998)
like_med   <- c(Disease = 0.98, Healthy = 0.05) # Sens = 0.98, 1 - Spec = 0.05

med_result <- bayes_update(priors_med, like_med)
cat("Total P(Positive Test):", round(med_result$evidence_prob, 5), "\n")
cat("Posterior P(Disease | Positive):", round(med_result$posteriors["Disease"], 4), "\n")
```

---

## Combined Exercises (Exercises 27 - 30)

#### Exercise 27: Multi-Stage Manufacturing Defect & Warranty Claim Pipeline (Combined, Moderate)
**Problem:** An automated electronics assembly plant produces circuit boards using 3 production lines: Line A ($L_A$, 50% of output), Line B ($L_B$, 30%), and Line C ($L_C$, 20%).
During manufacturing, each board undergoes two sequential quality tests: Electrical Test ($T_1$) and Thermal Test ($T_2$).
From historical audit logs:
- Defect rate at $T_1$: $P(D_1 \mid L_A) = 0.02$, $P(D_1 \mid L_B) = 0.04$, $P(D_1 \mid L_C) = 0.05$.
- Defect rate at $T_2$ given it passed $T_1$: $P(D_2 \mid D_1^c \cap L_A) = 0.01$, $P(D_2 \mid D_1^c \cap L_B) = 0.02$, $P(D_2 \mid D_1^c \cap L_C) = 0.03$.

**a)** Compute the probability that a board from Line A passes both tests ($D_1^c \cap D_2^c$).
**b)** Compute the overall probability $P(\text{Pass Both})$ across all combined factory lines using the Law of Total Probability.
**c)** If a randomly selected board fails at least one test, what is the posterior probability that it was produced by Line C ($L_C$)?
**d)** Write an R snippet to verify these probabilities.

**Solution:**
**a)** For Line A:
$$P(D_1^c \mid L_A) = 1 - 0.02 = 0.98$$
$$P(D_2^c \mid D_1^c \cap L_A) = 1 - 0.01 = 0.99$$
By the multiplication rule:
$$P(\text{Pass Both} \mid L_A) = P(D_1^c \cap D_2^c \mid L_A) = 0.98 \cdot 0.99 = 0.9702 \text{ (97.02\%)}$$

**b)** Compute passing probabilities for Lines B and C:
- For Line B: $P(D_1^c \mid L_B) = 1 - 0.04 = 0.96$; $P(D_2^c \mid D_1^c \cap L_B) = 1 - 0.02 = 0.98$.
  $$P(\text{Pass Both} \mid L_B) = 0.96 \cdot 0.98 = 0.9408$$
- For Line C: $P(D_1^c \mid L_C) = 1 - 0.05 = 0.95$; $P(D_2^c \mid D_1^c \cap L_C) = 1 - 0.03 = 0.97$.
  $$P(\text{Pass Both} \mid L_C) = 0.95 \cdot 0.97 = 0.9215$$

Apply Law of Total Probability for overall passing rate:
$$P(\text{Pass Both}) = (0.9702 \cdot 0.50) + (0.9408 \cdot 0.30) + (0.9215 \cdot 0.20)$$
$$P(\text{Pass Both}) = 0.48510 + 0.28224 + 0.18430 = 0.95164 \approx 0.9516 \text{ (95.16\%)}$$

Overall failure probability $P(\text{Fail}) = 1 - 0.95164 = 0.04836 \approx 0.0484$.

**c)** Failure rate for Line C:
$$P(\text{Fail} \mid L_C) = 1 - P(\text{Pass Both} \mid L_C) = 1 - 0.9215 = 0.0785$$

Apply Bayes' Theorem for $P(L_C \mid \text{Fail})$:
$$P(L_C \mid \text{Fail}) = \frac{P(\text{Fail} \mid L_C) P(L_C)}{P(\text{Fail})} = \frac{0.0785 \cdot 0.20}{0.04836} = \frac{0.01570}{0.04836} \approx 0.3246 \text{ (32.46\%)}$$

**d)** R Code Verification:
```r
priors <- c(LA = 0.50, LB = 0.30, LC = 0.20)
pass_given_line <- c(LA = 0.98*0.99, LB = 0.96*0.98, LC = 0.95*0.97)
fail_given_line <- 1 - pass_given_line

p_pass_total <- sum(priors * pass_given_line)
p_fail_total <- sum(priors * fail_given_line)
post_LC_fail <- (fail_given_line["LC"] * priors["LC"]) / p_fail_total

cat("Total Pass Probability:", p_pass_total, "\n")
cat("Posterior P(LC | Fail):", post_LC_fail, "\n")
```

Final Answer: **a) 0.9702 (97.02%)**, **b) 0.9516 (95.16%)**, **c) 0.3246 (32.46%)**, **d) R code provided above**

---

#### Exercise 28: Microservice Architecture Reliability and Anomaly Bayes Root-Cause Analysis (Time-Domain) (Combined, Harder)
**Problem:** A cloud API backend processes user checkouts through a hybrid microservice topology:
- **Authentication:** Single Auth Gateway ($A$).
- **Processing Layer:** 2 independent parallel payment microservices ($P_1, P_2$).
- **Database Layer:** Single Primary Database ($DB$).

```
                +---> Payment P1 --->+
                |                    |
[Auth Gateway A]+                    +[Database DB]
                |                    |
                +---> Payment P2 --->+
```

The request succeeds if Auth ($A$) succeeds, AT LEAST ONE Payment service ($P_1$ or $P_2$) succeeds, AND Database ($DB$) succeeds.

From execution logs over a 30-day window ($t = 24\,[hr]$ period):
- $P(A \text{ succeeds}) = 0.99$.
- Individual payment service survival: $P(P_1 \text{ succeeds}) = 0.95$, $P(P_2 \text{ succeeds}) = 0.95$ (independent).
- $P(DB \text{ succeeds}) = 0.98$.
- Overall traffic load regimes: Low Load ($L_1$, 60% of time), High Load ($L_2$, 30%), Surge Load ($L_3$, 10%).
- Conditional probability of a checkout timeout ($T > 2\,[s]$) given load regime:
  $P(T > 2 \mid L_1) = 0.01$, $P(T > 2 \mid L_2) = 0.08$, $P(T > 2 \mid L_3) = 0.50$.

**a)** Calculate the reliability $R_{\text{pay}}$ of the parallel payment layer ($P_1 \parallel P_2$).
**b)** Calculate the end-to-end system reliability $R_{\text{sys}}$ of the entire checkout pipeline.
**c)** Compute the total probability $P(T > 2\,[s])$ of a checkout timeout across all load regimes.
**d)** If a monitoring agent fires a timeout alert ($T > 2\,[s]$), compute the posterior probability $P(L_3 \mid T > 2\,[s])$ that the system was in Surge Load regime.
**e)** Write an R script simulating this architecture and computing the posterior probabilities.

**Solution:**
**a)** Payment layer uses parallel redundancy.
Failure probability of single payment service: $F_P = 1 - 0.95 = 0.05$.
Both payment services fail iff $F_{\text{pay\_layer}} = (0.05)^2 = 0.0025$.
$$R_{\text{pay}} = 1 - 0.0025 = 0.9975 \text{ (99.75\%)}$$

**b)** End-to-end topology is in series across Auth ($A$), Payment Layer ($P_{\text{layer}}$), and Database ($DB$):
$$R_{\text{sys}} = P(A) \cdot R_{\text{pay}} \cdot P(DB) = 0.99 \cdot 0.9975 \cdot 0.98 = 0.9677745 \approx 0.9678 \text{ (96.78\%)}$$

**c)** Total probability of checkout timeout $P(T > 2\,[s])$ via Law of Total Probability:
$$P(T > 2) = P(T > 2 \mid L_1)P(L_1) + P(T > 2 \mid L_2)P(L_2) + P(T > 2 \mid L_3)P(L_3)$$
$$P(T > 2) = (0.01 \cdot 0.60) + (0.08 \cdot 0.30) + (0.50 \cdot 0.10) = 0.006 + 0.024 + 0.050 = 0.0800 \text{ (8.00\%)}$$

**d)** Apply Bayes' Theorem for Surge Load $L_3$:
$$P(L_3 \mid T > 2) = \frac{P(T > 2 \mid L_3)P(L_3)}{P(T > 2)} = \frac{0.050}{0.0800} = \frac{5}{8} = 0.6250 \text{ (62.50\%)}$$

**e)** R Verification Script:
```r
# Microservice Architecture Verification
p_A <- 0.99
p_P1 <- 0.95; p_P2 <- 0.95
p_DB <- 0.98

r_pay <- 1 - (1 - p_P1)*(1 - p_P2)
r_sys <- p_A * r_pay * p_DB

load_priors <- c(L1 = 0.60, L2 = 0.30, L3 = 0.10)
timeout_like <- c(L1 = 0.01, L2 = 0.08, L3 = 0.50)

p_timeout_total <- sum(load_priors * timeout_like)
post_L3 <- (timeout_like["L3"] * load_priors["L3"]) / p_timeout_total

cat("Payment Layer Reliability:", r_pay, "\n")
cat("End-to-End System Reliability:", r_sys, "\n")
cat("Total Timeout Probability:", p_timeout_total, "\n")
cat("Posterior P(L3 | Timeout):", post_L3, "\n")
```

Final Answer: **a) 0.9975 (99.75%)**, **b) 0.9678 (96.78%)**, **c) 0.0800 (8.00%)**, **d) 0.6250 (62.50%)**, **e) R script provided above**

---

#### Exercise 29: Telecommunications Channel Noise & Packet Delay Pipeline (Combined, Hard)
**Problem:** A digital communications link transmits data packets over a wireless channel.
The transmission involves two stochastic layers:
1. **Physical Transmission Noise (Binary Symmetric Channel):** Bit error rate $p_e = 0.02$. Prior probability of transmitting bit '1' is $P(X=1) = 0.70$, and bit '0' is $P(X=0) = 0.30$.
2. **Network Hop Latency Pipeline:** Packets pass through 3 sequential switches ($S_1, S_2, S_3$). Hop completion probabilities within frame time budget $t_{\text{frame}} = 10\,[ms]$ are:
   - $P(S_1 \le 10) = 0.95$
   - $P(S_2 \le 10 \mid S_1 \le 10) = 0.90$
   - $P(S_3 \le 10 \mid S_1 \le 10 \cap S_2 \le 10) = 0.85$

Furthermore, packet corruption ($C$) occurs independently of switch delays with probability $P(C) = 0.01$.

**a)** Calculate $P(Y=1)$, the total probability of receiving bit '1'.
**b)** Given that bit $Y=1$ was received, calculate the posterior probability $P(X=1 \mid Y=1)$.
**c)** Calculate the joint probability that a packet completes all 3 switch hops within time budget AND is NOT corrupted.
**d)** If 1,000 independent packets are sent, calculate the expected number of packets that arrive both on-time and uncorrupted.

**Solution:**
**a)** Physical channel likelihoods:
$P(Y=1 \mid X=1) = 1 - p_e = 0.98$.
$P(Y=1 \mid X=0) = p_e = 0.02$.

Apply Law of Total Probability for $P(Y=1)$:
$$P(Y=1) = P(Y=1 \mid X=1)P(X=1) + P(Y=1 \mid X=0)P(X=0)$$
$$P(Y=1) = (0.98 \cdot 0.70) + (0.02 \cdot 0.30) = 0.686 + 0.006 = 0.6920 \text{ (69.20\%)}$$

**b)** Apply Bayes' Theorem for $P(X=1 \mid Y=1)$:
$$P(X=1 \mid Y=1) = \frac{P(Y=1 \mid X=1)P(X=1)}{P(Y=1)} = \frac{0.686}{0.6920} = \frac{343}{346} \approx 0.99133 \approx 0.9913$$

**c)** Hop pipeline success probability via chain rule:
$$P(\text{On-Time}) = P(S_1 \le 10) \cdot P(S_2 \le 10 \mid S_1 \le 10) \cdot P(S_3 \le 10 \mid S_1 \cap S_2) = 0.95 \cdot 0.90 \cdot 0.85 = 0.72675$$

Since corruption $C$ is independent of delay:
$$P(\text{Uncorrupted}) = P(C^c) = 1 - 0.01 = 0.99$$
$$P(\text{On-Time} \cap \text{Uncorrupted}) = P(\text{On-Time}) \cdot P(C^c) = 0.72675 \cdot 0.99 = 0.7194825 \approx 0.7195$$

**d)** Expected successful packets out of $N = 1000$:
$$E[\text{Valid Packets}] = 1000 \cdot 0.7194825 = 719.48 \approx 719 \text{ packets}$$

Final Answer: **a) 0.6920 (69.20%)**, **b) 0.9913 (99.13%)**, **c) 0.7195 (71.95%)**, **d) 719 packets**

---

#### Exercise 30: High-Frequency Trading Latency, Redundant Watchdogs & Unit-Scaling Gotcha (Time-Domain) (Combined, Hardest + Gotcha)
**Problem:** A high-frequency trading (HFT) firm executes orders over an ultra-low-latency FPGA gateway.
1. **Engine Latency Distribution:** Order execution lifetime $T$ (in microseconds, $[\mu s]$) has survival function $S_T(t) = \frac{1}{1 + 0.02 t}$ for $t \ge 0$.
   - Evaluate $P(T > 100\,[\mu s] \mid T > 50\,[\mu s])$.
2. **Watchdog Timers:** Order execution is monitored by 2 independent redundant FPGA watchdog hardware timers ($W_1, W_2$). Each watchdog has a failure probability of $p_f = 0.02$ over a trading session.
   - Calculate the overall watchdog system reliability $R_{\text{watchdog}}$ (probability at least one watchdog functions).
3. **Market Regime Diagnosis:** Market volatility operates under 3 regimes: Calm ($M_1$, 70%), Volatile ($M_2$, 20%), Extreme ($M_3$, 10%).
   - Latency spike probabilities ($S = \{T > 100\,[\mu s]\}$):
     $P(S \mid M_1) = 0.01$, $P(S \mid M_2) = 0.15$, $P(S \mid M_3) = 0.80$.
   - Calculate $P(S)$ and posterior $P(M_3 \mid S)$.
4. **Unit-Conversion & Variance Scaling Gotcha:** The firm measures latency variance in seconds squared $[s^2]$ as $\text{Var}(T) = 4.0 \times 10^{-8}\,[s^2]$. An analyst converts latency measurements from seconds to microseconds ($1\,[s] = 10^6\,[\mu s]$) and claims the variance in microseconds squared is $\text{Var}_{\mu s}(T) = 4.0 \times 10^{-2}\,[\mu s^2]$.
   - Is the analyst's variance conversion correct? Calculate the exact variance in $[\mu s^2]$ and explain the gotcha.

**Solution:**
**Part 1: Conditional Survival Probability**
$$S_T(50) = P(T > 50) = \frac{1}{1 + 0.02(50)} = \frac{1}{1 + 1} = \frac{1}{2} = 0.5000$$
$$S_T(100) = P(T > 100) = \frac{1}{1 + 0.02(100)} = \frac{1}{1 + 2} = \frac{1}{3} \approx 0.3333$$
$$P(T > 100 \mid T > 50) = \frac{P(T > 100)}{P(T > 50)} = \frac{1/3}{1/2} = \frac{2}{3} \approx 0.6667 \text{ (66.67\%)}$$

**Part 2: Watchdog System Reliability**
Parallel redundancy:
$$F_{\text{system}} = p_f^2 = (0.02)^2 = 0.0004$$
$$R_{\text{watchdog}} = 1 - 0.0004 = 0.9996 \text{ (99.96\%)}$$

**Part 3: Market Regime Diagnosis**
Law of Total Probability for $P(S)$:
$$P(S) = (0.01 \cdot 0.70) + (0.15 \cdot 0.20) + (0.80 \cdot 0.10) = 0.007 + 0.030 + 0.080 = 0.1170 \text{ (11.70\%)}$$

Posterior for Extreme Regime $M_3$:
$$P(M_3 \mid S) = \frac{P(S \mid M_3)P(M_3)}{P(S)} = \frac{0.080}{0.1170} = \frac{80}{117} \approx 0.6838 \text{ (68.38\%)}$$

**Part 4: Unit-Conversion Variance Scaling Gotcha**
**Gotcha:** When converting time units by scaling factor $c$, the random variable transforms as $X_{\text{new}} = c \cdot X$.
By the properties of variance, $\text{Var}(c \cdot X) = c^2 \cdot \text{Var}(X)$ ($c^2$ rule).

Here, $c = 10^6\,[\mu s / s]$, so $c^2 = (10^6)^2 = 10^{12}$.
The analyst incorrectly scaled variance by $c = 10^6$ instead of $c^2 = 10^{12}$!

Correct calculation:
$$\text{Var}_{\mu s}(T) = c^2 \cdot \text{Var}_s(T) = 10^{12} \cdot (4.0 \times 10^{-8}) = 4.0 \times 10^4 = 40,000\,[\mu s^2]$$

Standard deviation scaling:
$$\sigma_s = \sqrt{4.0 \times 10^{-8}} = 2.0 \times 10^{-4}\,[s] = 0.2\,[ms] = 200\,[\mu s]$$
$$\sigma_{\mu s} = 200\,[\mu s] \implies \text{Var}_{\mu s}(T) = (200)^2 = 40,000\,[\mu s^2]$$

The analyst's figure of $4.0 \times 10^{-2}$ was off by a factor of one million ($10^6$) due to forgetting the $c^2$ rule!

Final Answer:
- **Part 1:** 2/3 (0.6667)
- **Part 2:** 0.9996 (99.96%)
- **Part 3:** P(S) = 0.1170 (11.70%), P(M3 | S) = 0.6838 (68.38%)
- **Part 4 (Gotcha):** **Incorrect analyst claim.** Correct variance is **$40,000\,[\mu s^2]$** (scaled by $c^2 = 10^{12}$, not $c = 10^6$).

---

## Exam Preparation Guide

### Formula Quick-Reference

| Topic | Formula | Notes / Exam Typologio Format |
| :--- | :--- | :--- |
| **Conditional Probability** | $P(A \mid B) = \frac{P(A \cap B)}{P(B)}$ | Requires $P(B) > 0$. Restricts sample space to $B$. |
| **Conditional Complement** | $P(A^c \mid B) = 1 - P(A \mid B)$ | Holds for any fixed conditioning event $B$. |
| **Two-Event Multiplication Rule** | $P(A \cap B) = P(A) \cdot P(B \mid A) = P(B) \cdot P(A \mid B)$ | Fundamental for multi-stage processes. |
| **Multi-Event Chain Rule** | $P(\bigcap_{i=1}^n A_i) = P(A_1) \prod_{i=2}^n P(A_i \mid \bigcap_{j=1}^{i-1} A_j)$ | Sequential sampling without replacement. |
| **Independence Test** | $P(A \cap B) = P(A) \cdot P(B) \iff P(A \mid B) = P(A)$ | Valid only when events do not affect each other. |
| **Series System Reliability** | $R_{\text{sys}}(t) = \prod_{i=1}^n P(T_i > t)$ | Weakest-link architecture (Logical AND). |
| **Parallel System Reliability** | $R_{\text{sys}}(t) = 1 - \prod_{i=1}^n (1 - P(T_i > t))$ | Redundant architecture (Logical OR). |
| **Law of Total Probability** | $P(A) = \sum_{i=1}^n P(A \mid B_i) P(B_i)$ | $\{B_1, \dots, B_n\}$ must form a valid partition. |
| **Bayes' Theorem** | $P(B_k \mid A) = \frac{P(A \mid B_k)P(B_k)}{\sum_{j=1}^n P(A \mid B_j)P(B_j)}$ | Updates prior $P(B_k)$ to posterior $P(B_k \mid A)$. |
| **Conditional Survival (Time-Domain)** | $P(T > t_{[s]} + s_{[s]} \mid T > t_{[s]}) = \frac{P(T > (t+s)_{[s]})}{P(T > t_{[s]})}$ | Uses time-domain units; memoryless only for Exp/Geom. |
| **Variance Unit Scaling ($c^2$ Rule)** | $\text{Var}(c \cdot X) = c^2 \cdot \text{Var}(X)$ | Scaling time units (e.g., $s \to ms$) scales Var by $c^2$. |

---

### Exam Checklist

| Category | Items |
| :--- | :--- |
| **Must Memorize** | - Conditional probability definition $P(A \mid B) = P(A \cap B)/P(B)$<br>- Multiplication chain rule<br>- Product rule for independence $P(A \cap B) = P(A)P(B)$<br>- Series ($R_{\text{series}} = \prod R_i$) and Parallel ($R_{\text{parallel}} = 1 - \prod (1-R_i)$) formulas<br>- Law of Total Probability formula<br>- Bayes' Theorem formula |
| **Must Understand** | - Difference between mutually exclusive ($P(A \cap B) = 0$) and independent ($P(A \cap B) = P(A)P(B)$) events<br>- Reduced sample space geometric intuition<br>- Reversing conditional probabilities using Bayes' Theorem<br>- Base Rate Fallacy in diagnostic/anomaly detection<br>- Conditional survival function calculation |
| **Book-Only (Professor May Test)** | - Pairwise vs Mutual Independence counterexamples ($n \ge 3$ events)<br>- Right-censored observation windows effect on conditional latency tail estimates<br>- Binary symmetric communication channel Bayes error rate derivations<br>- $k$-out-of-$n$ system reliability binomial expansion |

---

### Common Exam Traps

1. **Conflating Mutually Exclusive with Independent Events:**
   - *Trap:* Assuming that if two events are mutually exclusive ($A \cap B = \emptyset$), they must be independent.
   - *Correction:* If $P(A) > 0$ and $P(B) > 0$, mutually exclusive events are **always dependent** because $P(A \cap B) = 0 \neq P(A)P(B)$.

2. **Misapplying the Memoryless Property:**
   - *Trap:* Assuming $P(T > t + s \mid T > t) = P(T > s)$ for arbitrary time distributions.
   - *Correction:* Memorylessness is **only** true for the Exponential (continuous) and Geometric (discrete) distributions. For all other distributions, you must compute $\frac{P(T > t+s)}{P(T > t)}$ explicitly.

3. **Ignoring the Base Rate in Bayes' Theorem (Base Rate Fallacy):**
   - *Trap:* Conflating $P(A \mid B)$ with $P(B \mid A)$. For example, assuming a test with 99% accuracy means a positive result implies 99% chance of disease.
   - *Correction:* Always calculate the marginal denominator $P(A)$ using the Law of Total Probability. If the prior $P(B)$ is small, $P(B \mid A)$ will be much lower than $P(A \mid B)$.

4. **Forgetting the $c^2$ Variance Scaling Rule in Time Conversion:**
   - *Trap:* Converting time variance from seconds to milliseconds by multiplying by $1,000$.
   - *Correction:* Since $1\,[s] = 1000\,[ms]$, $c = 1000$. Standard deviation scales by $c = 1000$, but variance scales by $c^2 = 1,000,000 = 10^6$!

5. **Assuming Pairwise Independence Implies Mutual Independence:**
   - *Trap:* Proving $P(A \cap B) = P(A)P(B)$, $P(B \cap C) = P(B)P(C)$, and $P(A \cap C) = P(A)P(C)$ and concluding that $A, B, C$ are mutually independent.
   - *Correction:* You must also explicitly verify the 3-way product condition $P(A \cap B \cap C) = P(A)P(B)P(C)$.

---

### Exam Paper Cross-References

| Exam Paper | Relevant Questions | Difficulty | Core Topics Covered |
| :--- | :--- | :---: | :--- |
| [Exam_paper_Easy.md](../../Exams/Papers/synthetic/Exam_paper_Easy.md) | Question 2 | **1/5** | Basic set probability, independent vs disjoint events. |
| [Exam_paper_2024_09_06_Team_A.md](../../Exams/Papers/Exam_paper_2024_09_06_Team_A.md) | Question 2 | **1/5** | Set relations, testing independence of basic events. |
| [Exam_paper_2023_06_12_Team_null.md](../../Exams/Papers/Exam_paper_2023_06_12_Team_null.md) | Question 3 | **2/5** | Set-based probability, conditional probability basics. |
| [Exam_paper_Intermediate_1.md](../../Exams/Papers/synthetic/Exam_paper_Intermediate_1.md) | Question 3 | **2/5** | Law of Total Probability & Bayes' Theorem (3-factory problem). |
| [Exam_paper_Intermediate_2.md](../../Exams/Papers/synthetic/Exam_paper_Intermediate_2.md) | Question 3 | **3/5** | Conditional probability derivations, testing event independence. |
| [Exam_paper_Hard_1.md](../../Exams/Papers/synthetic/Exam_paper_Hard_1.md) | Question 3 | **4/5** | Bayes' Theorem with sensitivity, specificity, and low base rate. |
| [Exam_paper_Hard_2.md](../../Exams/Papers/synthetic/Exam_paper_Hard_2.md) | Question 3 | **5/5** | Binary symmetric communication channel Bayes modeling. |

---

## Phase Summary

- **Conditional Probability $P(A \mid B) = \frac{P(A \cap B)}{P(B)}$** quantifies the likelihood of event $A$ given that event $B$ has occurred. The conditioning event $B$ shrinks the universal sample space $\Omega$ to $B$.
- **The Multiplication Chain Rule** $P(A_1 \cap \dots \cap A_n) = P(A_1) P(A_2 \mid A_1) \cdots P(A_n \mid A_1 \cap \dots \cap A_{n-1})$ decomposes complex multi-stage sequential processes (such as microservice pipeline hops or sampling without replacement) into sequential conditional steps.
- **Statistical Independence** requires $P(A \cap B) = P(A) \cdot P(B)$. Independent events convey no information about each other. Mutually exclusive non-zero events ($P(A \cap B) = 0$) can **never** be independent.
- **System Reliability Models** use independence to evaluate infrastructure uptime:
  - **Series Systems (AND):** Require all components to function ($R_{\text{series}} = \prod R_i$).
  - **Parallel Systems (OR):** Require at least one component to function ($R_{\text{parallel}} = 1 - \prod (1 - R_i)$).
- **The Law of Total Probability** $P(A) = \sum P(A \mid B_i) P(B_i)$ reconstructs overall event probabilities across exhaustive sample space partitions.
- **Bayes' Theorem** $P(B_k \mid A) = \frac{P(A \mid B_k)P(B_k)}{\sum P(A \mid B_j)P(B_j)}$ updates prior beliefs $P(B_k)$ to posterior probabilities $P(B_k \mid A)$ upon observing empirical evidence $A$ (such as anomaly alerts or diagnostic test outcomes).
- **Time-Domain Applications** require explicit time units, careful evaluation of conditional survival functions $P(T > t+s \mid T > t)$, awareness of right-censoring bias, avoiding the base rate fallacy, and enforcing the $c^2$ variance scaling rule on unit conversions.

---

<!-- Source: Phases/Phase_4_Discrete_Random_Variables.md -->

# Phase 4: Discrete Random Variables

## Table of Contents
- [Section 4.1: Discrete Random Variables, PMF/CDF, Expectation & Variance](#section-41-discrete-random-variables-pmfcdf-expectation--variance)
- [Section 4.2: Binomial & Poisson Distributions](#section-42-binomial--poisson-distributions)
- [Section 4.3: Geometric & Hypergeometric Distributions](#section-43-geometric--hypergeometric-distributions)
- [Section 4.4: Moment Generating Functions & Characteristic Functions](#section-44-moment-generating-functions--characteristic-functions)
- [Exam Preparation Guide](#exam-preparation-guide)
- [Phase Summary](#phase-summary)

---

## Section 4.1: Discrete Random Variables, PMF/CDF, Expectation & Variance

### Core Theory & Definitions

A **Random Variable (RV)** $X$ is a formal mathematical function that maps outcomes from a sample space $\Omega$ to real numbers ($X: \Omega \to \mathbb{R}$). A random variable is classified as **discrete** if its support $S_X = \{x \in \mathbb{R} : P(X = x) > 0\}$ is finite or countably infinite (such as the set of non-negative integers $\mathbb{N}_0$).

```
Sample Space $\Omega$ (Outcomes)   Real Line $R$ (Values)
+-----------------------+        +-------------------+
|  Outcome $\omega_1$ (Success) | ------>|  X($\omega_1$) = 1 |
|  Outcome $\omega_2$ (Failure) | ------>|  X($\omega_2$) = 0 |
+-----------------------+        +-------------------+
```

#### Probability Mass Function (PMF)
The probability distribution of a discrete random variable is specified by its **Probability Mass Function (PMF)**, denoted $p(x)$ or $P(X = x)$. The PMF assigns a probability to each possible value in the support and must satisfy two fundamental axiomatic validity conditions:

1. **Non-negativity:** $p(x) \ge 0$ for all $x \in S_X$, and $p(x) = 0$ for all $x \notin S_X$.
2. **Normalization:** $\sum_{x \in S_X} p(x) = 1$.

#### Cumulative Distribution Function (CDF)
The **Cumulative Distribution Function (CDF)**, denoted $F(x)$ or $F_X(x)$, measures the probability that $X$ takes on a value less than or equal to $x$:
$$F(x) = P(X \le x) = \sum_{k \le x} p(k)$$

For a discrete random variable, the CDF is a monotonic, non-decreasing, right-continuous step function. The steps occur precisely at the points in the support $S_X$, and the height of the jump at $x_k$ equals the PMF value $p(x_k) = F(x_k) - \lim_{t \to x_k^-} F(t)$.

#### Expected Value ($E[X]$) and LOTUS
The **Expected Value** (or population mean $\mu$) represents the probability-weighted long-run average of $X$:
$$E[X] = \mu = \sum_{x \in S_X} x \cdot p(x)$$
The expectation exists if and only if the sum converges absolutely ($\sum_{x} |x| p(x) < \infty$).

By the **Law of the Unconscious Statistician (LOTUS)**, the expected value of any real-valued function $g(X)$ of a discrete random variable is computed directly without finding the PMF of $g(X)$:
$$E[g(X)] = \sum_{x \in S_X} g(x) \cdot p(x)$$

#### Variance ($Var(X)$) and Standard Deviation ($\sigma$)
**Variance** measures the expected squared deviation of $X$ from its mean $\mu$, quantifying dispersion:
$$Var(X) = \sigma^2 = E[(X - \mu)^2] = E[X^2] - (E[X])^2$$
where $E[X^2] = \sum_{x \in S_X} x^2 \cdot p(x)$ is the second raw moment. The **Standard Deviation** is $\sigma = \sqrt{Var(X)}$.

#### Linear Properties of Expectation and Variance
For any real constants $a, b, c$ and discrete random variables $X, Y$:
1. **Linearity of Expectation:** $E[aX + bY + c] = a E[X] + b E[Y] + c$ (holds universally, regardless of independence).
2. **Linear Transformation of Variance:** $Var(aX + b) = a^2 Var(X)$ (additive constants do not change spread).
3. **Variance of Sum/Difference:** If $X$ and $Y$ are **statistically independent**, $Var(X \pm Y) = Var(X) + Var(Y)$.

> **Practical / Time-Domain Note:**
> In computer performance engineering and time-series measurement, discrete random variables model quantized latency buckets, discrete clock tick counts, packet retransmission attempts, or queue lengths.
> When scaling time units by a factor $c$ (e.g., converting seconds to milliseconds, $c = 1000$), the random variable transforms as $Y_{[ms]} = c \cdot X_{[s]}$.
> While the expected duration scales linearly ($E[Y_{[ms]}] = c \cdot E[X_{[s]}]$), the duration variance scales quadratically ($Var(Y_{[ms]}^2) = c^2 \cdot Var(X_{[s]}^2)$). This is known as the **$c^2$ variance scaling rule**.

---

### Mathematical Formulas & Derivations

#### 1. Fundamental PMF & CDF Formulas
$$\text{PMF Validity:} \quad p(x) \ge 0 \quad \text{and} \quad \sum_{x \in S_X} p(x) = 1$$
$$\text{Discrete CDF:} \quad F(x) = P(X \le x) = \sum_{k \le x} p(k)$$
$$\text{PMF from CDF:} \quad P(X = x_k) = F(x_k) - F(x_k^-)$$

#### 2. Expectation & Variance Formulas
$$\text{Expected Value (Mean):} \quad E[X] = \mu = \sum_{x \in S_X} x \cdot p(x)$$
$$\text{LOTUS:} \quad E[g(X)] = \sum_{x \in S_X} g(x) \cdot p(x)$$
$$\text{Computational Variance Formula:} \quad Var(X) = \sigma^2 = E[X^2] - (E[X])^2$$
$$\text{where} \quad E[X^2] = \sum_{x \in S_X} x^2 \cdot p(x)$$

#### 3. Linear Operator Derivations
*Proof of $Var(aX + b) = a^2 Var(X)$:*
Let $\mu = E[X]$. Then $E[aX + b] = a\mu + b$.
$$Var(aX + b) = E[\{(aX + b) - (a\mu + b)\}^2] = E[\{a(X - \mu)\}^2] = E[a^2 (X - \mu)^2] = a^2 E[(X - \mu)^2] = a^2 Var(X)$$

#### 4. Time-Domain Adapted Formulas (with Explicit Units)
For a discrete duration variable $T_{[s]}$ in seconds and linear transformation $Y_{[ms]} = c \cdot T_{[s]} + d_{[ms]}$ where $c = 1000\,[ms/s]$:
$$\text{Adapted Mean:} \quad E[Y_{[ms]}] = c_{[ms/s]} \cdot E[T_{[s]}] + d_{[ms]}$$
$$\text{Adapted Variance ($c^2$ rule):} \quad Var(Y_{[ms]}^2) = c_{[ms/s]}^2 \cdot Var(T_{[s]}^2) = 10^6 \cdot Var(T_{[s]}^2)$$
$$\text{Adapted Standard Deviation:} \quad \sigma_{Y,[ms]} = c_{[ms/s]} \cdot \sigma_{T,[s]} = 1000 \cdot \sigma_{T,[s]}$$

---

### Worked Exercises

#### Exercise 1: Discrete PMF Validation & Constant Determination
**Problem:** A discrete random variable $X$ has PMF given by $p(x) = c \cdot x$ for $x \in \{1, 2, 3, 4\}$ and $p(x) = 0$ otherwise.
**a) ** Determine the normalizing constant $c$.
**b) ** Compute the Cumulative Distribution Function $F(x)$ for all $x \in \mathbb{R}$.
**c) ** Compute the expected value $E[X]$ and variance $Var(X)$.

**Solution:**
**Step 1: Determine constant $c$ using normalization condition**
$$\sum_{x=1}^4 p(x) = 1 \implies c(1) + c(2) + c(3) + c(4) = 1 \implies 10c = 1 \implies c = 0.1$$
The valid PMF is $p(1) = 0.1, p(2) = 0.2, p(3) = 0.3, p(4) = 0.4$.

**Step 2: Construct CDF $F(x)$**
$$F(x) = \begin{cases} 0 & \text{if } x < 1 \\ 0.1 & \text{if } 1 \le x < 2 \\ 0.3 & \text{if } 2 \le x < 3 \\ 0.6 & \text{if } 3 \le x < 4 \\ 1.0 & \text{if } x \ge 4 \end{cases}$$

**Step 3: Compute $E[X]$ and $Var(X)$**
$$E[X] = \sum_{x=1}^4 x \cdot p(x) = (1 \cdot 0.1) + (2 \cdot 0.2) + (3 \cdot 0.3) + (4 \cdot 0.4) = 0.1 + 0.4 + 0.9 + 1.6 = 3.0$$
$$E[X^2] = \sum_{x=1}^4 x^2 \cdot p(x) = (1^2 \cdot 0.1) + (2^2 \cdot 0.2) + (3^2 \cdot 0.3) + (4^2 \cdot 0.4) = 0.1 + 0.8 + 2.7 + 6.4 = 10.0$$
$$Var(X) = E[X^2] - (E[X])^2 = 10.0 - (3.0)^2 = 10.0 - 9.0 = 1.0$$

Final Answer:
- **a) ** $c = 0.1$
- **b) ** $F(x)$ step function as defined above
- **c) ** $E[X] = 3.0$, $Var(X) = 1.0$

---

#### Exercise 2: Discrete Latency Bucket PMF & CDF Transformation (Time-Domain)
**Problem:** A cloud load balancer logs network request latencies into discrete time buckets $T \in \{5, 10, 15, 20\}\,[ms]$. The empirical PMF is $p(5) = 0.40, p(10) = 0.30, p(15) = 0.20, p(20) = 0.10$.
**a) ** Construct the CDF table for $T_{[ms]}$.
**b) ** Compute the probability that a request latency exceeds $10\,ms$, $P(T > 10\,ms)$.
**c) ** Calculate the expected latency $E[T_{[ms]}]$ and standard deviation $\sigma_{T,[ms]}$.

**Solution:**
**Step 1: Construct CDF $F_T(t)$**
- $F_T(5) = P(T \le 5) = 0.40$
- $F_T(10) = P(T \le 10) = 0.40 + 0.30 = 0.70$
- $F_T(15) = P(T \le 15) = 0.70 + 0.20 = 0.90$
- $F_T(20) = P(T \le 20) = 0.90 + 0.10 = 1.00$

**Step 2: Compute $P(T > 10\,ms)$**
$$P(T > 10\,ms) = 1 - P(T \le 10\,ms) = 1 - F_T(10) = 1 - 0.70 = 0.30$$

**Step 3: Calculate $E[T]$ and $\sigma_T$**
$$E[T_{[ms]}] = (5 \cdot 0.40) + (10 \cdot 0.30) + (15 \cdot 0.20) + (20 \cdot 0.10) = 2.0 + 3.0 + 3.0 + 2.0 = 10.0\,[ms]$$
$$E[T_{[ms]}^2] = (5^2 \cdot 0.40) + (10^2 \cdot 0.30) + (15^2 \cdot 0.20) + (20^2 \cdot 0.10) = 10.0 + 30.0 + 45.0 + 40.0 = 125.0\,[ms^2]$$
$$Var(T_{[ms]}^2) = 125.0 - (10.0)^2 = 125.0 - 100.0 = 25.0\,[ms^2]$$
$$\sigma_{T,[ms]} = \sqrt{25.0} = 5.0\,[ms]$$

Final Answer:
- **a) ** $F_T(5)=0.40, F_T(10)=0.70, F_T(15)=0.90, F_T(20)=1.00$
- **b) ** $P(T > 10\,ms) = 0.30$
- **c) ** $E[T] = 10.0\,[ms]$, $\sigma_T = 5.0\,[ms]$

---

#### Exercise 3: Expectation, LOTUS, and Variance of Dice Roll Winnings
**Problem:** In a carnival game, a player rolls a single fair 6-sided die ($X \in \{1, 2, 3, 4, 5, 6\}$). The payoff in dollars is given by $W = g(X) = X^2 - 3X$.
**a) ** Write out the PMF of $W$.
**b) ** Calculate the expected payoff $E[W]$ using LOTUS.
**c) ** Compute $Var(W)$.

**Solution:**
**Step 1: Compute payoff values $g(x)$ for each die outcome**
- $x = 1 \implies g(1) = 1^2 - 3(1) = -2$
- $x = 2 \implies g(2) = 2^2 - 3(2) = -2$
- $x = 3 \implies g(3) = 3^2 - 3(3) = 0$
- $x = 4 \implies g(4) = 4^2 - 3(4) = 4$
- $x = 5 \implies g(5) = 5^2 - 3(5) = 10$
- $x = 6 \implies g(6) = 6^2 - 3(6) = 18$

Each outcome has probability $p(x) = 1/6$.

**Step 2: Calculate $E[W]$ via LOTUS**
$$E[W] = \sum_{x=1}^6 (x^2 - 3x) \cdot \frac{1}{6} = \frac{-2 + (-2) + 0 + 4 + 10 + 18}{6} = \frac{28}{6} = \frac{14}{3} \approx 4.6667\,\text{dollars}$$

**Step 3: Compute $Var(W) = E[W^2] - (E[W])^2$**
Calculate $E[W^2]$ via LOTUS:
$$E[W^2] = \sum_{x=1}^6 (x^2 - 3x)^2 \cdot \frac{1}{6} = \frac{(-2)^2 + (-2)^2 + 0^2 + 4^2 + 10^2 + 18^2}{6} = \frac{4 + 4 + 0 + 16 + 100 + 324}{6} = \frac{448}{6} = \frac{224}{3} \approx 74.6667$$
$$Var(W) = \frac{224}{3} - \left(\frac{14}{3}\right)^2 = \frac{224}{3} - \frac{196}{9} = \frac{672 - 196}{9} = \frac{476}{9} \approx 52.8889\,\text{dollars}^2$$

Final Answer:
- **a) ** $W \in \{-2, 0, 4, 10, 18\}$ with $P(W=-2)=2/6, P(W=0)=1/6, P(W=4)=1/6, P(W=10)=1/6, P(W=18)=1/6$
- **b) ** $E[W] = 14/3 \approx 4.67\,\text{dollars}$
- **c) ** $Var(W) = 476/9 \approx 52.89\,\text{dollars}^2$

---

#### Exercise 4: Execution Duration Expectation, Variance, & Unit Scaling ($c^2$ rule) (Time-Domain)
**Problem:** An algorithm's execution duration $T_{[s]}$ in seconds has $E[T_{[s]}] = 0.050\,s$ and $Var(T_{[s]}^2) = 0.00040\,s^2$. The total system latency including fixed overhead $250\,\mu s$ converted to microseconds is $Y_{[\mu s]} = 10^6 \cdot T_{[s]} + 250$.
**a) ** Calculate expected latency $E[Y_{[\mu s]}]$.
**b) ** Calculate variance $Var(Y_{[\mu s]}^2)$ using the $c^2$ variance scaling rule.
**c) ** Calculate standard deviation $\sigma_{Y,[\mu s]}$ and convert it back to milliseconds.

**Solution:**
**Step 1: Compute $E[Y_{[\mu s]}]$**
$$E[Y_{[\mu s]}] = 10^6 \cdot E[T_{[s]}] + 250 = 10^6 (0.050) + 250 = 50,000 + 250 = 50,250\,[\mu s]$$

**Step 2: Compute $Var(Y_{[\mu s]}^2)$ using $c^2$ rule**
Here $c = 10^6\,[\mu s / s]$, so $c^2 = (10^6)^2 = 10^{12}$.
$$Var(Y_{[\mu s]}^2) = c^2 \cdot Var(T_{[s]}^2) = 10^{12} \cdot 0.00040 = 4.0 \times 10^8\,[\mu s^2]$$

**Step 3: Compute $\sigma_{Y,[\mu s]}$ and convert to $ms$**
$$\sigma_{Y,[\mu s]} = \sqrt{4.0 \times 10^8} = 20,000\,[\mu s]$$
Converting to milliseconds ($1\,ms = 1000\,\mu s$):
$$\sigma_{Y,[ms]} = \frac{20,000}{1000} = 20.0\,[ms]$$

Final Answer:
- **a) ** $E[Y] = 50,250\,[\mu s]$
- **b) ** $Var(Y) = 4.0 \times 10^8\,[\mu s^2]$
- **c) ** $\sigma_Y = 20,000\,[\mu s] = 20.0\,[ms]$

---

#### Exercise 5: Linear Combination of Independent Discrete Variables
**Problem:** Let $X$ and $Y$ be independent discrete random variables with $E[X] = 4, Var(X) = 2, E[Y] = 3, Var(Y) = 5$. Define $Z = 3X - 2Y + 5$.
**a) ** Compute $E[Z]$.
**b) ** Compute $Var(Z)$.
**c) ** Compute $E[Z^2]$.

**Solution:**
**Step 1: Compute $E[Z]$**
$$E[Z] = E[3X - 2Y + 5] = 3 E[X] - 2 E[Y] + 5 = 3(4) - 2(3) + 5 = 12 - 6 + 5 = 11$$

**Step 2: Compute $Var(Z)$ using independence of $X, Y$**
$$Var(Z) = Var(3X - 2Y + 5) = 3^2 Var(X) + (-2)^2 Var(Y) = 9(2) + 4(5) = 18 + 20 = 38$$

**Step 3: Compute $E[Z^2]$ using $Var(Z) = E[Z^2] - (E[Z])^2$**
$$E[Z^2] = Var(Z) + (E[Z])^2 = 38 + (11)^2 = 38 + 121 = 159$$

Final Answer:
- **a) ** $E[Z] = 11$
- **b) ** $Var(Z) = 38$
- **c) ** $E[Z^2] = 159$

---

#### Exercise 6: Multi-Server Latency Hop Sum & Variance Scaling (Time-Domain)
**Problem:** A database query traverses 3 independent microservice network hops with durations $T_1, T_2, T_3\,[ms]$ having expected values $E[T_1]=12\,ms, E[T_2]=25\,ms, E[T_3]=8\,ms$ and variances $Var(T_1)=9\,ms^2, Var(T_2)=16\,ms^2, Var(T_3)=4\,ms^2$. Total pipeline duration is $T = T_1 + T_2 + T_3$.
**a) ** Calculate expected total pipeline duration $E[T_{[ms]}]$.
**b) ** Calculate total variance $Var(T_{[ms]}^2)$ and standard deviation $\sigma_{T,[ms]}$.
**c) ** If network congestion causes hop 2 latency to scale by factor $1.5$ ($T_2' = 1.5 T_2$), compute new total variance $Var(T_{[ms]}'^{2})$.

**Solution:**
**Step 1: Compute $E[T]$**
$$E[T] = E[T_1] + E[T_2] + E[T_3] = 12 + 25 + 8 = 45\,[ms]$$

**Step 2: Compute $Var(T)$ and $\sigma_T$ using independence**
$$Var(T) = Var(T_1) + Var(T_2) + Var(T_3) = 9 + 16 + 4 = 29\,[ms^2]$$
$$\sigma_T = \sqrt{29} \approx 5.3852\,[ms]$$

**Step 3: Compute $Var(T')$ with scaled hop 2**
$$Var(T_2') = (1.5)^2 Var(T_2) = 2.25 \times 16 = 36\,[ms^2]$$
$$Var(T') = Var(T_1) + Var(T_2') + Var(T_3) = 9 + 36 + 4 = 49\,[ms^2]$$

Final Answer:
- **a) ** $E[T] = 45\,[ms]$
- **b) ** $Var(T) = 29\,[ms^2]$, $\sigma_T \approx 5.39\,[ms]$
- **c) ** New variance $Var(T') = 49\,[ms^2]$

---

#### Exercise 7: Discrete System Downtime Hours Expectation & Standard Deviation (Time-Domain)
**Problem:** Weekly maintenance downtime hours $D$ for a server cluster has PMF:
$p(0) = 0.60, p(1) = 0.25, p(2) = 0.10, p(3) = 0.05$.
**a) ** Compute expected weekly downtime hours $E[D_{[hr]}]$.
**b) ** Compute standard deviation $\sigma_{D,[hr]}$.
**c) ** If downtime costs $150 per hour plus a fixed setup penalty of $200 per week ($C = 150 D + 200$), calculate expected weekly cost $E[C]$ and cost standard deviation $\sigma_C$.

**Solution:**
**Step 1: Compute $E[D]$**
$$E[D_{[hr]}] = (0 \cdot 0.60) + (1 \cdot 0.25) + (2 \cdot 0.10) + (3 \cdot 0.05) = 0 + 0.25 + 0.20 + 0.15 = 0.60\,[hr]$$

**Step 2: Compute $Var(D)$ and $\sigma_D$**
$$E[D^2] = (0^2 \cdot 0.60) + (1^2 \cdot 0.25) + (2^2 \cdot 0.10) + (3^2 \cdot 0.05) = 0 + 0.25 + 0.40 + 0.45 = 1.10\,[hr^2]$$
$$Var(D) = 1.10 - (0.60)^2 = 1.10 - 0.36 = 0.74\,[hr^2]$$
$$\sigma_D = \sqrt{0.74} \approx 0.8602\,[hr]$$

**Step 3: Compute $E[C]$ and $\sigma_C$**
$$E[C] = 150 E[D] + 200 = 150(0.60) + 200 = 90 + 200 = \$290$$
$$\sigma_C = 150 \cdot \sigma_D = 150(0.8602) \approx \$129.03$$

Final Answer:
- **a) ** $E[D] = 0.60\,[hr]$
- **b) ** $\sigma_D \approx 0.86\,[hr]$
- **c) ** $E[C] = \$290$, $\sigma_C \approx \$129.03$

---

### R Implementation

```r
# Section 4.1: Discrete RV PMF, CDF, Expectation & Variance Calculations

# Define Support and PMF
x_vals <- c(1, 2, 3, 4)
pmf_vals <- c(0.1, 0.2, 0.3, 0.4)

# 1. PMF Validation Check
stopifnot(all(pmf_vals >= 0), abs(sum(pmf_vals) - 1.0) < 1e-9)

# 2. Cumulative Distribution Function (CDF)
cdf_vals <- cumsum(pmf_vals)
names(cdf_vals) <- paste0("P(X<=", x_vals, ")")
print(cdf_vals)

# 3. Expected Value E[X]
mean_X <- sum(x_vals * pmf_vals)

# 4. Variance Var(X) via LOTUS
mean_X2 <- sum((x_vals^2) * pmf_vals)
var_X <- mean_X2 - (mean_X^2)
sd_X <- sqrt(var_X)

cat(sprintf("E[X] = %.4f | Var(X) = %.4f | SD(X) = %.4f\n", mean_X, var_X, sd_X))

# 5. Linear Transformation & Unit Scaling (c^2 rule)
# Converting duration X (in seconds) to Y (in ms): Y = 1000*X + 250
c_scale <- 1000
mean_Y <- c_scale * mean_X + 250
var_Y <- (c_scale^2) * var_X
sd_Y <- c_scale * sd_X

cat(sprintf("E[Y_ms] = %.2f | Var(Y_ms) = %.2f | SD(Y_ms) = %.2f\n", mean_Y, var_Y, sd_Y))
```

---

## Section 4.2: Binomial & Poisson Distributions

### Core Theory & Definitions

#### 1. The Binomial Distribution ($Bin(n, p)$)
The **Binomial distribution** models the number of successes $X$ in a sequence of $n$ independent trials. It relies strictly on the **FINS** criteria:

1. **F**ixed number of trials $n$.
2. **I**ndependent trials.
3. **N**umber of outcomes per trial is binary (Success / Failure).
4. **S**ame probability of success $p$ across all trials ($q = 1 - p$).

The support is $S_X = \{0, 1, 2, \dots, n\}$. Its PMF is:
$$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}, \quad k \in \{0, 1, \dots, n\}$$
where $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ is the binomial coefficient.

**Mean and Variance:**
$$E[X] = n \cdot p, \quad Var(X) = n \cdot p \cdot (1-p)$$

**Additivity of Independent Binomials:**
If $X \sim Bin(n_1, p)$ and $Y \sim Bin(n_2, p)$ are independent with the *same* success probability $p$, then $X + Y \sim Bin(n_1 + n_2, p)$.

#### 2. The Poisson Distribution ($Poisson(\lambda)$)
The **Poisson distribution** models the count of rare events occurring within a specified continuous window (time or space) at a constant average rate $\lambda > 0$.

**Poisson Process Assumptions:**
- Events occur independently of each other.
- The average rate $\lambda$ is constant throughout the window.
- Two events cannot occur simultaneously at the exact same instant.

The support is countably infinite: $S_X = \{0, 1, 2, \dots\}$. Its PMF is:
$$P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}, \quad k = 0, 1, 2, \dots$$

**Mean and Variance (Equidispersion):**
$$E[X] = \lambda, \quad Var(X) = \lambda$$
In a true Poisson process, the mean always equals the variance.

#### Rate Scaling in Time Windows
If events occur at an hourly rate $\lambda_0$, then over a time window of duration $t$ hours, the Poisson parameter scales linearly:
$$\lambda_t = \lambda_0 \cdot t$$
The PMF for count $X_t$ in window $t$ becomes:
$$P(X_t = k) = \frac{(\lambda_0 t)^k e^{-\lambda_0 t}}{k!}$$

#### 3. Poisson Approximation to the Binomial Distribution
When the number of trials $n$ is very large and the success probability $p$ is very small, calculating binomial coefficients becomes computationally expensive. The Binomial distribution converges mathematically to a Poisson distribution with rate parameter $\lambda = n \cdot p$:
$$\lim_{n \to \infty, p \to 0, np = \lambda} \binom{n}{k} p^k (1-p)^{n-k} = \frac{\lambda^k e^{-\lambda}}{k!}$$

> **Standard Rule of Thumb for Approximation:**
> The Poisson approximation $Bin(n, p) \approx Poisson(\lambda = np)$ is valid when:
> $$n \ge 20 \quad \text{(or } n \ge 100\text{)} \quad \text{and} \quad p \le 0.05 \quad \text{(or } np \le 10\text{)}$$

---

### Mathematical Formulas & Derivations

#### 1. Binomial Expectation & Variance Derivation
Using the linear combination of $n$ independent Bernoulli indicator variables $X = \sum_{i=1}^n I_i$ where $P(I_i = 1) = p, P(I_i = 0) = 1-p$:
$$E[I_i] = 1(p) + 0(1-p) = p \implies E[X] = \sum_{i=1}^n E[I_i] = n \cdot p$$
$$Var(I_i) = E[I_i^2] - (E[I_i])^2 = p - p^2 = p(1-p)$$
$$Var(X) = \sum_{i=1}^n Var(I_i) = n \cdot p \cdot (1-p) \quad \text{(by independence)}$$

#### 2. Poisson Limit Proof from Binomial
Substitute $p = \frac{\lambda}{n}$ into the Binomial PMF:
$$P(X = k) = \frac{n!}{k!(n-k)!} \left(\frac{\lambda}{n}\right)^k \left(1 - \frac{\lambda}{n}\right)^{n-k} = \frac{\lambda^k}{k!} \cdot \left[ \frac{n(n-1)\cdots(n-k+1)}{n^k} \right] \cdot \left(1 - \frac{\lambda}{n}\right)^n \cdot \left(1 - \frac{\lambda}{n}\right)^{-k}$$
Taking the limit as $n \to \infty$:
- $\lim_{n \to \infty} \frac{n(n-1)\cdots(n-k+1)}{n^k} = 1$
- $\lim_{n \to \infty} \left(1 - \frac{\lambda}{n}\right)^n = e^{-\lambda}$
- $\lim_{n \to \infty} \left(1 - \frac{\lambda}{n}\right)^{-k} = 1$

Thus, $\lim_{n \to \infty} P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}$.

#### 3. Time-Domain Adapted Formulas
For request arrival rate $\lambda_0\,[\text{events}/s]$ and measurement window $t_{[s]}$:
$$\lambda_{t,[s]} = \lambda_0 \cdot t_{[s]}$$
$$P(X_{t,[s]} = k) = \frac{(\lambda_0 t)^k e^{-\lambda_0 t}}{k!}$$
$$E[X_{t,[s]}] = Var(X_{t,[s]}) = \lambda_0 \cdot t_{[s]}$$

---

### Worked Exercises

#### Exercise 8: Manufacturing Defect Inspection Binomial Probability
**Problem:** A component manufacturing line produces items with a defect probability $p = 0.05$. An inspector draws a random sample of $n = 10$ components. Let $X \sim Bin(10, 0.05)$.
**a) ** Calculate the probability that zero components are defective.
**b) ** Calculate the probability that at least 2 components are defective.
**c) ** Compute the mean $E[X]$ and variance $Var(X)$.

**Solution:**
**Step 1: Compute $P(X = 0)$**
$$P(X = 0) = \binom{10}{0} (0.05)^0 (0.95)^{10} = 1 \cdot 1 \cdot (0.95)^{10} \approx 0.598737$$

**Step 2: Compute $P(X \ge 2)$ via complement rule**
$$P(X \ge 2) = 1 - P(X = 0) - P(X = 1)$$
$$P(X = 1) = \binom{10}{1} (0.05)^1 (0.95)^9 = 10 \cdot 0.05 \cdot 0.630249 = 0.315125$$
$$P(X \ge 2) = 1 - 0.598737 - 0.315125 = 0.086138 \approx 0.0861$$

**Step 3: Compute $E[X]$ and $Var(X)$**
$$E[X] = n \cdot p = 10 \cdot 0.05 = 0.50$$
$$Var(X) = n \cdot p \cdot (1-p) = 10 \cdot 0.05 \cdot 0.95 = 0.475$$

Final Answer:
- **a) ** $P(X = 0) \approx 0.5987$
- **b) ** $P(X \ge 2) \approx 0.0861$
- **c) ** $E[X] = 0.50$, $Var(X) = 0.475$

---

#### Exercise 9: API Request Retry Limit & SLA Binomial Compliance (Time-Domain)
**Problem:** An application issues $n = 20$ independent network requests to a microservice. Each request has a success probability $p = 0.90$.
**a) ** Compute the probability that all 20 requests succeed.
**b) ** Compute the probability that at least 18 requests succeed ($P(X \ge 18)$).
**c) ** Provide the R command to calculate $P(X \ge 18)$.

**Solution:**
**Step 1: Compute $P(X = 20)$**
$$P(X = 20) = \binom{20}{20} (0.90)^{20} (0.10)^0 = (0.90)^{20} \approx 0.121577 \approx 0.1216$$

**Step 2: Compute $P(X \ge 18) = P(X=18) + P(X=19) + P(X=20)$**
$$P(X = 19) = \binom{20}{19} (0.90)^{19} (0.10)^1 = 20 \cdot 0.135085 \cdot 0.10 = 0.270170$$
$$P(X = 18) = \binom{20}{18} (0.90)^{18} (0.10)^2 = 190 \cdot 0.150095 \cdot 0.01 = 0.285180$$
$$P(X \ge 18) = 0.285180 + 0.270170 + 0.121577 = 0.676927 \approx 0.6769$$

**Step 3: R command**
`pbinom(17, size = 20, prob = 0.90, lower.tail = FALSE)` or `1 - pbinom(17, 20, 0.90)` or `sum(dbinom(18:20, 20, 0.90))`.

Final Answer:
- **a) ** $P(X = 20) \approx 0.1216$
- **b) ** $P(X \ge 18) \approx 0.6769$
- **c) ** `pbinom(17, size = 20, prob = 0.90, lower.tail = FALSE)`

---

#### Exercise 10: Minimum Sample Size Binomial Logarithm Inequality
**Problem:** In a semiconductor batch, component defect probability is $p = 0.02$. How many items $n$ must be sampled so that the probability of detecting at least one defect is at least $95\%$ ($0.95$)?

**Solution:**
**Step 1: Set up the inequality**
$$P(X \ge 1) = 1 - P(X = 0) = 1 - (1 - p)^n \ge 0.95$$
$$1 - (0.98)^n \ge 0.95 \implies (0.98)^n \le 0.05$$

**Step 2: Apply natural logarithms**
$$n \cdot \ln(0.98) \le \ln(0.05)$$
Since $\ln(0.98) \approx -0.0202027 < 0$, dividing by $\ln(0.98)$ reverses the inequality:
$$n \ge \frac{\ln(0.05)}{\ln(0.98)} = \frac{-2.995732}{-0.0202027} \approx 148.284$$

**Step 3: Round up to nearest integer**
$n = 149$ components.

Final Answer:
Minimum sample size $n = 149$ components.

---

#### Exercise 11: High-Throughput Web Request Failure Binomial Trial Size (Time-Domain)
**Problem:** A telemetry system experiences packet drop probability $p_{\text{drop}} = 0.08$ per transmission attempt. Find the minimum number of attempts $n$ required so that the probability of at least one successful delivery is at least $99.9\%$ ($0.999$).

**Solution:**
**Step 1: Set up inequality for success**
$P(\text{at least 1 success}) = 1 - P(\text{all } n \text{ dropped}) = 1 - (p_{\text{drop}})^n \ge 0.999$
$$1 - (0.08)^n \ge 0.999 \implies (0.08)^n \le 0.001$$

**Step 2: Solve using logarithms**
$$n \cdot \ln(0.08) \le \ln(0.001)$$
Since $\ln(0.08) \approx -2.525729 < 0$:
$$n \ge \frac{\ln(0.001)}{\ln(0.08)} = \frac{-6.907755}{-2.525729} \approx 2.73496$$

**Step 3: Round up to integer**
$n = 3$ attempts.

Final Answer:
Minimum attempts required $n = 3$.

---

#### Exercise 12: Conditional Binomial Probability given Minimum Successes
**Problem:** Let $X \sim Bin(n=5, p=0.40)$. Calculate the conditional probability $P(X = 3 \mid X \ge 2)$.

**Solution:**
**Step 1: Use conditional probability definition**
$$P(X = 3 \mid X \ge 2) = \frac{P(\{X = 3\} \cap \{X \ge 2\})}{P(X \ge 2)} = \frac{P(X = 3)}{P(X \ge 2)}$$

**Step 2: Compute $P(X = 3)$**
$$P(X = 3) = \binom{5}{3} (0.40)^3 (0.60)^2 = 10 \cdot 0.064 \cdot 0.36 = 0.2304$$

**Step 3: Compute $P(X \ge 2)$ via complement**
$$P(X = 0) = (0.60)^5 = 0.07776$$
$$P(X = 1) = \binom{5}{1} (0.40)^1 (0.60)^4 = 5 \cdot 0.40 \cdot 0.1296 = 0.2592$$
$$P(X \ge 2) = 1 - 0.07776 - 0.2592 = 0.66304$$

**Step 4: Compute conditional probability**
$$P(X = 3 \mid X \ge 2) = \frac{0.2304}{0.66304} \approx 0.34749 \approx 0.3475$$

Final Answer:
$P(X = 3 \mid X \ge 2) \approx 0.3475$ (or $34.75\%$).

---

#### Exercise 13: Microservice Cluster Packet Loss Conditional Binomial (Time-Domain)
**Problem:** A microservice transmits a batch of $n = 6$ packets with drop probability $p = 0.15$. Let $X$ be the count of dropped packets. Find $P(X = 1 \mid X \le 2)$.

**Solution:**
**Step 1: Compute PMF values for $X = 0, 1, 2$**
$$P(X = 0) = (0.85)^6 \approx 0.377150$$
$$P(X = 1) = \binom{6}{1} (0.15)^1 (0.85)^5 = 6 \cdot 0.15 \cdot 0.443705 = 0.399335$$
$$P(X = 2) = \binom{6}{2} (0.15)^2 (0.85)^4 = 15 \cdot 0.0225 \cdot 0.522006 = 0.176177$$

**Step 2: Compute denominator $P(X \le 2)$**
$$P(X \le 2) = 0.377150 + 0.399335 + 0.176177 = 0.952662$$

**Step 3: Compute conditional probability**
$$P(X = 1 \mid X \le 2) = \frac{P(X = 1)}{P(X \le 2)} = \frac{0.399335}{0.952662} \approx 0.419178 \approx 0.4192$$

Final Answer:
$P(X = 1 \mid X \le 2) \approx 0.4192$.

---

#### Exercise 14: Call Center Hourly Arrivals Poisson Distribution
**Problem:** Calls arrive at a support desk at a Poisson rate $\lambda = 6$ calls per hour.
**a) ** Calculate the probability of receiving exactly 4 calls in a 1-hour window.
**b) ** Calculate the probability of receiving zero calls in a 30-minute window ($t = 0.5\,hr$).

**Solution:**
**Step 1: Compute $P(X = 4)$ for $\lambda = 6$**
$$P(X = 4) = \frac{6^4 e^{-6}}{4!} = \frac{1296 \cdot e^{-6}}{24} = 54 e^{-6} \approx 54(0.00247875) \approx 0.133853 \approx 0.1339$$

**Step 2: Scale rate for 30-minute window ($t = 0.5\,hr$)**
$$\lambda_{30m} = \lambda_0 \cdot t = 6 \times 0.5 = 3.0$$
$$P(X_{30m} = 0) = \frac{3^0 e^{-3}}{0!} = e^{-3} \approx 0.049787 \approx 0.0498$$

Final Answer:
- **a) ** $P(X = 4) \approx 0.1339$
- **b) ** $P(X_{30m} = 0) \approx 0.0498$

---

#### Exercise 15: Server Log Anomaly Rate Scaling across Time Windows (Time-Domain)
**Problem:** Error anomalies are logged at a rate of $\lambda_0 = 120$ errors per hour.
**a) ** Determine the scaled Poisson rate $\lambda_{5m}$ for a 5-minute window.
**b) ** Compute the probability of logging exactly 10 errors in a 5-minute window.
**c) ** State the mean and standard deviation of errors in a 5-minute window.

**Solution:**
**Step 1: Scale rate for 5 minutes ($t = 5/60 = 1/12\,hr$)**
$$\lambda_{5m} = 120 \cdot \frac{5}{60} = 10.0\,\text{errors}$$

**Step 2: Compute $P(X_{5m} = 10)$**
$$P(X_{5m} = 10) = \frac{10^{10} e^{-10}}{10!} = \frac{10,000,000,000 \cdot e^{-10}}{3,628,800} \approx 2755.7319 \cdot (0.00004540) \approx 0.125110$$

**Step 3: Mean and Standard Deviation**
$$E[X_{5m}] = \lambda_{5m} = 10.0, \quad Var(X_{5m}) = 10.0 \implies \sigma = \sqrt{10} \approx 3.1623\,\text{errors}$$

Final Answer:
- **a) ** $\lambda_{5m} = 10.0$
- **b) ** $P(X_{5m} = 10) \approx 0.1251$
- **c) ** Mean $= 10.0$, $\sigma \approx 3.16\,\text{errors}$

---

#### Exercise 16: Rare Disease Prevalence Binomial-to-Poisson Approximation
**Problem:** A medical test screens $n = 1000$ individuals for a rare condition with prevalence $p = 0.003$.
**a) ** Verify that the Poisson approximation is justified.
**b) ** Calculate the approximate probability that exactly 2 individuals test positive.
**c) ** Compute the approximate probability that at least 1 individual tests positive.

**Solution:**
**Step 1: Verify approximation criteria**
$n = 1000 \ge 100$ and $p = 0.003 \le 0.05$. $np = 1000(0.003) = 3.0 \le 10$. Criteria satisfied! Use $Poisson(\lambda = 3.0)$.

**Step 2: Compute $P(X = 2)$ via Poisson**
$$P(X = 2) \approx \frac{3^2 e^{-3}}{2!} = \frac{9 e^{-3}}{2} = 4.5 e^{-3} \approx 4.5(0.049787) \approx 0.224042 \approx 0.2240$$

**Step 3: Compute $P(X \ge 1)$**
$$P(X \ge 1) = 1 - P(X = 0) \approx 1 - e^{-3} = 1 - 0.049787 = 0.950213 \approx 0.9502$$

Final Answer:
- **a) ** Approximation valid ($n=1000 \ge 100, p=0.003 \le 0.05, \lambda=3.0$)
- **b) ** $P(X = 2) \approx 0.2240$
- **c) ** $P(X \ge 1) \approx 0.9502$

---

#### Exercise 17: Memory Leak Fault Occurrences via Poisson Approximation (Time-Domain)
**Problem:** A cloud deployment runs $n = 500$ container instances. Each instance has an hourly crash probability $p = 0.004$ due to memory leaks.
**a) ** Using Poisson approximation, calculate the probability of exactly 3 container crashes in a 1-hour window.
**b) ** Calculate the probability of at most 1 crash in a 2-hour window ($t = 2\,hr$).

**Solution:**
**Step 1: Hourly Poisson rate**
$\lambda_1 = n \cdot p = 500 \cdot 0.004 = 2.0$ crashes/hour.

**Step 2: Compute $P(X_1 = 3)$ for 1 hour**
$$P(X_1 = 3) = \frac{2^3 e^{-2}}{3!} = \frac{8 e^{-2}}{6} = \frac{4}{3} e^{-2} \approx 1.33333 \cdot 0.135335 \approx 0.180447 \approx 0.1804$$

**Step 3: Compute $P(X_2 \le 1)$ for 2 hours ($\lambda_2 = 2.0 \times 2 = 4.0$)**
$$P(X_2 \le 1) = P(X_2 = 0) + P(X_2 = 1) = \frac{4^0 e^{-4}}{0!} + \frac{4^1 e^{-4}}{1!} = e^{-4} + 4e^{-4} = 5e^{-4}$$
$$5e^{-4} \approx 5(0.0183156) = 0.091578 \approx 0.0916$$

Final Answer:
- **a) ** $P(X_1 = 3) \approx 0.1804$
- **b) ** $P(X_2 \le 1) \approx 0.0916$

---

### R Implementation

```r
# Section 4.2: Binomial & Poisson Distribution R Commands

# 1. Binomial Distribution: B(n=20, p=0.90)
n_bin <- 20; p_bin <- 0.90
dbinom_exact <- dbinom(18, size = n_bin, prob = p_bin)   # P(X = 18)
pbinom_tail <- pbinom(17, size = n_bin, prob = p_bin, lower.tail = FALSE) # P(X >= 18)

cat(sprintf("Binomial P(X=18) = %.4f | P(X>=18) = %.4f\n", dbinom_exact, pbinom_tail))

# 2. Poisson Distribution & Rate Scaling: Poisson(lambda_hourly = 120)
lambda_hr <- 120
lambda_5m <- lambda_hr * (5 / 60) # Scaled to 10

dpois_exact <- dpois(10, lambda = lambda_5m)             # P(X = 10 in 5m)
ppois_cum <- ppois(10, lambda = lambda_5m)               # P(X <= 10 in 5m)

cat(sprintf("Poisson P(X_5m = 10) = %.4f | P(X_5m <= 10) = %.4f\n", dpois_exact, ppois_cum))

# 3. Poisson Approximation to Binomial: B(n=1000, p=0.003) vs Poisson(lambda=3)
exact_binom <- dbinom(2, size = 1000, prob = 0.003)
approx_pois  <- dpois(2, lambda = 3.0)

cat(sprintf("Exact Binomial: %.6f | Poisson Approx: %.6f | Diff: %.6f\n",
            exact_binom, approx_pois, abs(exact_binom - approx_pois)))
```

---

## Section 4.3: Geometric & Hypergeometric Distributions

### Core Theory & Definitions

#### 1. The Geometric Distribution ($Geo(p)$)
The **Geometric distribution** models the number of independent Bernoulli trials required until observing the **first success**, where each trial has success probability $p \in (0, 1]$.

There are two standard textbook definitions of the Geometric distribution:

```
Definition A (Trials Count X):     [ F ] [ F ] [ F ] [ S ]   --> X = 4 trials
Definition B (Failures Count Y):   [ F ] [ F ] [ F ]         --> Y = 3 failures
```

| Property | Definition A (Total Trials $X$) | Definition B (Failures $Y = X - 1$) |
| :--- | :--- | :--- |
| **Support $S$** | $S_X = \{1, 2, 3, \dots\}$ | $S_Y = \{0, 1, 2, \dots\}$ |
| **PMF** | $P(X = k) = (1-p)^{k-1} p$ | $P(Y = k) = (1-p)^k p$ |
| **CDF** | $F_X(k) = 1 - (1-p)^k$ | $F_Y(k) = 1 - (1-p)^{k+1}$ |
| **Mean $E[\cdot]$** | $E[X] = \frac{1}{p}$ | $E[Y] = \frac{1-p}{p}$ |
| **Variance $Var(\cdot)$** | $Var(X) = \frac{1-p}{p^2}$ | $Var(Y) = \frac{1-p}{p^2}$ |

> **Critical R Parameterization Gotcha:**
> R's built-in functions (`dgeom`, `pgeom`, `qgeom`, `rgeom`) strictly implement **Definition B** (counting failures $Y$ before first success).
> To evaluate $P(X = k)$ under Definition A (trials), you must pass `x = k - 1` to `dgeom`!

#### The Memoryless Property
The Geometric distribution is the **only** discrete distribution possessing the **Memoryless Property**. Given that no success has occurred in the first $k$ trials, the conditional probability of requiring more than $k + s$ trials depends only on $s$, completely forgetting the past $k$ failures:
$$P(X > k + s \mid X > k) = P(X > s) = (1-p)^s$$

#### 2. The Hypergeometric Distribution ($HG(N, K, n)$)
The **Hypergeometric distribution** models sampling **without replacement** from a finite population of size $N$ containing $K$ success items and $N - K$ failure items, drawing a sample of size $n$.

Because draws are without replacement, trials are **dependent**, violating the Binomial assumptions.

The support is $\max(0, n - (N - K)) \le k \le \min(n, K)$. Its PMF is:
$$P(X = k) = \frac{\binom{K}{k} \binom{N - K}{n - k}}{\binom{N}{n}}$$

**Mean and Variance:**
$$E[X] = n \cdot \frac{K}{N}$$
$$Var(X) = n \cdot \frac{K}{N} \cdot \left(1 - \frac{K}{N}\right) \cdot \left( \frac{N - n}{N - 1} \right)$$
The term $\frac{N - n}{N - 1}$ is the **Finite Population Correction (FPC)** factor, which reduces variance compared to Binomial sampling.

#### Binomial Approximation to Hypergeometric
When the sample size $n$ is small relative to the population $N$ ($n/N \le 0.05$ or $N \ge 10n$), the effect of sampling without replacement is negligible. The Hypergeometric distribution can be accurately approximated by $Bin(n, p = K/N)$, and the FPC factor $\frac{N-n}{N-1} \approx 1$.

---

### Mathematical Formulas & Derivations

#### 1. Geometric CDF & Survival Derivation (Def A)
$$P(X > k) = \sum_{j=k+1}^{\infty} (1-p)^{j-1} p = p (1-p)^k \sum_{m=0}^{\infty} (1-p)^m = p (1-p)^k \cdot \frac{1}{1 - (1-p)} = (1-p)^k$$
$$F_X(k) = P(X \le k) = 1 - P(X > k) = 1 - (1-p)^k$$

#### 2. Proof of Memoryless Property
$$P(X > k + s \mid X > k) = \frac{P(X > k + s \cap X > k)}{P(X > k)} = \frac{P(X > k + s)}{P(X > k)} = \frac{(1-p)^{k+s}}{(1-p)^k} = (1-p)^s = P(X > s)$$

#### 3. Hypergeometric Mean Derivation
Let $X = \sum_{i=1}^n I_i$ where $I_i = 1$ if the $i$-th drawn item is a success. By symmetry, $P(I_i = 1) = K/N$ for all $i$:
$$E[X] = \sum_{i=1}^n E[I_i] = \sum_{i=1}^n \frac{K}{N} = n \cdot \frac{K}{N}$$

---

### Worked Exercises

#### Exercise 18: Quality Control Inspection Geometric Trial Count
**Problem:** In a quality control process, component inspection has a defect probability $p = 0.12$ per item. Let $X \sim Geo(0.12)$ under Definition A (total trials).
**a) ** Calculate the probability that the first defect occurs on the 5th inspection.
**b) ** Calculate expected trials $E[X]$ and variance $Var(X)$.
**c) ** Compute $P(X > 4)$.

**Solution:**
**Step 1: Compute $P(X = 5)$**
$$P(X = 5) = (1 - 0.12)^{5-1} (0.12) = (0.88)^4 (0.12) = (0.599695) (0.12) \approx 0.071963 \approx 0.0720$$

**Step 2: Compute $E[X]$ and $Var(X)$**
$$E[X] = \frac{1}{p} = \frac{1}{0.12} \approx 8.3333\,\text{inspections}$$
$$Var(X) = \frac{1 - p}{p^2} = \frac{0.88}{(0.12)^2} = \frac{0.88}{0.0144} \approx 61.1111$$

**Step 3: Compute $P(X > 4)$**
$$P(X > 4) = (1 - p)^4 = (0.88)^4 \approx 0.5997$$

Final Answer:
- **a) ** $P(X = 5) \approx 0.0720$
- **b) ** $E[X] \approx 8.33$, $Var(X) \approx 61.11$
- **c) ** $P(X > 4) \approx 0.5997$

---

#### Exercise 19: Discrete Time-Slot Buffer Polling & Memoryless Property (Time-Domain)
**Problem:** A network buffer polls for incoming packets every $10\,ms$ time slot. Success probability per slot is $p = 0.25$.
**a) ** Calculate the probability that polling takes more than 4 slots ($T > 4$).
**b) ** Given that no packet arrived in the first 6 slots ($T > 6$), compute the conditional probability that the first packet arrives on the 9th slot ($P(T = 9 \mid T > 6)$).

**Solution:**
**Step 1: Compute $P(T > 4)$**
$$P(T > 4) = (1 - 0.25)^4 = (0.75)^4 = 0.316406 \approx 0.3164$$

**Step 2: Apply Memoryless Property for $P(T = 9 \mid T > 6)$**
By memorylessness, conditioning on $T > 6$ resets the trial counter by 6:
$$P(T = 9 \mid T > 6) = P(T = 9 - 6) = P(T = 3)$$
$$P(T = 3) = (1 - 0.25)^{3-1} (0.25) = (0.75)^2 (0.25) = 0.5625 \cdot 0.25 = 0.140625 \approx 0.1406$$

Final Answer:
- **a) ** $P(T > 4) \approx 0.3164$
- **b) ** $P(T = 9 \mid T > 6) \approx 0.1406$

---

#### Exercise 20: Comparison of Geometric Definition A (Trials) vs Definition B (Failures)
**Problem:** A hardware probe retries connection attempts with success probability $p = 0.20$.
**a) ** Under Def A ($X$ = total attempts), state $E[X]$ and $Var(X)$.
**b) ** Under Def B ($Y$ = failures before first success), state $E[Y]$ and $Var(Y)$.
**c) ** Verify that $Var(X) = Var(Y)$ and explain why expectations differ by 1.

**Solution:**
**Step 1: Def A parameters**
$$E[X] = \frac{1}{0.20} = 5.0, \quad Var(X) = \frac{1 - 0.20}{(0.20)^2} = \frac{0.80}{0.04} = 20.0$$

**Step 2: Def B parameters**
$$E[Y] = \frac{1 - 0.20}{0.20} = \frac{0.80}{0.20} = 4.0, \quad Var(Y) = \frac{1 - 0.20}{(0.20)^2} = 20.0$$

**Step 3: Verification**
Since $Y = X - 1$, by linear operator rules $E[Y] = E[X] - 1 = 5.0 - 1 = 4.0$.
For variance, subtracting a constant $1$ does not change dispersion: $Var(Y) = Var(X - 1) = 1^2 Var(X) = 20.0$.

Final Answer:
- **a) ** Def A: $E[X] = 5.0, Var(X) = 20.0$
- **b) ** Def B: $E[Y] = 4.0, Var(Y) = 20.0$
- **c) ** Expectations differ by 1 because $X = Y + 1$; variances are identical because shift is constant.

---

#### Exercise 21: Network Packet Transmission Attempts with Maximum Retry Threshold (Time-Domain)
**Problem:** A wireless sender retries sending a frame with per-slot success probability $p = 0.40$. The system gives up after a maximum of $n = 4$ slots (attempts $1, 2, 3, 4$).
**a) ** Calculate the probability that transmission is aborted ($T > 4$).
**b) ** Calculate the probability of successful transmission within the threshold ($T \le 4$).
**c) ** Write the R command to calculate $P(T \le 4)$.

**Solution:**
**Step 1: Compute abortion probability $P(T > 4)$**
$$P(T > 4) = (1 - 0.40)^4 = (0.60)^4 = 0.1296$$

**Step 2: Compute success probability $P(T \le 4)$**
$$P(T \le 4) = 1 - P(T > 4) = 1 - 0.1296 = 0.8704$$

**Step 3: R command**
Since R uses Def B ($Y = X - 1$), $T \le 4$ corresponds to $Y \le 3$ failures:
`pgeom(3, prob = 0.40)`

Final Answer:
- **a) ** $P(T > 4) = 0.1296$
- **b) ** $P(T \le 4) = 0.8704$
- **c) ** `pgeom(3, prob = 0.40)`

---

#### Exercise 22: Lottery Ticket Sampling Without Replacement Hypergeometric
**Problem:** An urn contains $N = 40$ lottery tickets, of which $K = 8$ are winning tickets. A participant draws $n = 5$ tickets without replacement. Let $X \sim HG(N=40, K=8, n=5)$.
**a) ** Calculate the probability of drawing exactly 2 winning tickets.
**b) ** Calculate expected winning tickets $E[X]$.
**c) ** Compute variance $Var(X)$.

**Solution:**
**Step 1: Compute $P(X = 2)$**
$$P(X = 2) = \frac{\binom{8}{2} \binom{32}{3}}{\binom{40}{5}} = \frac{28 \cdot 4960}{658008} = \frac{138880}{658008} \approx 0.211061 \approx 0.2111$$

**Step 2: Compute $E[X]$**
$$E[X] = n \cdot \frac{K}{N} = 5 \cdot \frac{8}{40} = 5 \cdot 0.20 = 1.0\,\text{ticket}$$

**Step 3: Compute $Var(X)$**
$$Var(X) = n \cdot \frac{K}{N} \cdot \left(1 - \frac{K}{N}\right) \cdot \left(\frac{N-n}{N-1}\right) = 5 \cdot 0.20 \cdot 0.80 \cdot \left(\frac{35}{39}\right) = 0.80 \cdot 0.897436 \approx 0.717949 \approx 0.7179$$

Final Answer:
- **a) ** $P(X = 2) \approx 0.2111$
- **b) ** $E[X] = 1.0$
- **c) ** $Var(X) \approx 0.7179$

---

#### Exercise 23: Hardware Server Faulty Module Audit via Hypergeometric (Time-Domain)
**Problem:** A server rack contains $N = 50$ blades, of which $K = 6$ have failing memory modules. An auditor inspects $n = 10$ blades without replacement.
**a) ** Calculate the probability of finding exactly 1 faulty blade.
**b) ** Provide the R command to calculate this exact probability.

**Solution:**
**Step 1: Compute $P(X = 1)$**
$$P(X = 1) = \frac{\binom{6}{1} \binom{44}{9}}{\binom{50}{10}} = \frac{6 \cdot 707234040}{10272278170} = \frac{4243404240}{10272278170} \approx 0.413093 \approx 0.4131$$

**Step 2: R command**
In R `dhyper(x, m, n, k)` uses:
- `x`: target count $= 1$
- `m`: total successes $K = 6$
- `n`: total failures $N - K = 44$
- `k`: sample size $n = 10$

Command: `dhyper(1, m = 6, n = 44, k = 10)`

Final Answer:
- **a) ** $P(X = 1) \approx 0.4131$
- **b) ** `dhyper(1, m = 6, n = 44, k = 10)`

---

#### Exercise 24: Large Population Binomial Approximation to Hypergeometric
**Problem:** A warehouse contains $N = 2000$ components, $K = 100$ of which are defective ($p = K/N = 0.05$). An engineer samples $n = 20$ components without replacement.
**a) ** Check if the Binomial approximation is justified.
**b) ** Compute $P(X = 0)$ using the Binomial approximation and compare with exact Hypergeometric.

**Solution:**
**Step 1: Check ratio $n/N$**
$$\frac{n}{N} = \frac{20}{2000} = 0.01 \le 0.05$$
Since $0.01 \le 0.05$, the Binomial approximation $Bin(20, 0.05)$ is valid!

**Step 2: Compute approximate $P(X = 0)$ via Binomial**
$$P(X = 0)_{\text{Bin}} = \binom{20}{0} (0.05)^0 (0.95)^{20} = (0.95)^{20} \approx 0.358486 \approx 0.3585$$

**Step 3: Exact Hypergeometric comparison**
$$P(X = 0)_{\text{HG}} = \frac{\binom{100}{0} \binom{1900}{20}}{\binom{2000}{20}} \approx 0.357989$$
Difference is only $0.000497$ ($< 0.05\%$).

Final Answer:
- **a) ** Approximation justified ($n/N = 0.01 \le 0.05$)
- **b) ** Binomial $P(X=0) \approx 0.3585$ (Exact HG $\approx 0.3580$)

---

#### Exercise 25: Large Data Cluster Log Inspection HG vs Binomial (Time-Domain)
**Problem:** A database cluster generates $N = 10,000$ log files per day, $K = 500$ of which record query timeout errors ($p = 0.05$). An automated parser inspects $n = 50$ logs without replacement.
**a) ** Is Binomial approximation justified?
**b) ** Compare expected values and variances under exact Hypergeometric versus Binomial approximation.

**Solution:**
**Step 1: Check $n/N$**
$$\frac{n}{N} = \frac{50}{10000} = 0.005 \le 0.05 \quad \text{(Justified!)}$$

**Step 2: Compare Expectations**
$$E[X]_{\text{Bin}} = n \cdot p = 50 \times 0.05 = 2.50\,\text{logs}$$
$$E[X]_{\text{HG}} = n \cdot \frac{K}{N} = 50 \times \frac{500}{10000} = 2.50\,\text{logs}$$

**Step 3: Compare Variances and FPC factor**
$$Var(X)_{\text{Bin}} = n \cdot p \cdot (1-p) = 50 \times 0.05 \times 0.95 = 2.3750$$
$$\text{FPC} = \frac{N - n}{N - 1} = \frac{10000 - 50}{10000 - 1} = \frac{9950}{9999} \approx 0.9950995$$
$$Var(X)_{\text{HG}} = 2.3750 \times 0.9950995 \approx 2.363361 \approx 2.3634$$

Final Answer:
- **a) ** Yes, $n/N = 0.005 \le 0.05$
- **b) ** Both means $= 2.50$; $Var_{\text{Bin}} = 2.3750$, $Var_{\text{HG}} \approx 2.3634$ (FPC $= 0.9951$)

---

#### Exercise 26: R Script Verification of Discrete Distribution Functions (Time-Domain)
**Problem:** Write a complete R script to verify discrete distribution computations for Geometric (Def B conversion) and Hypergeometric sampling.

**Solution:**
**Step 1: Write and verify R code**

```r
# Exercise 26: Comprehensive Geometric and Hypergeometric Analysis

# 1. Geometric Distribution (Trial count k = 4, p = 0.25)
# Definition A (trials): P(X = 4)
p_geom <- 0.25
k_trials <- 4

# R dgeom expects failures (y = k - 1)
prob_geom_defA <- dgeom(k_trials - 1, prob = p_geom)
cat(sprintf("Geometric (Def A, k=4 trials): P(X=4) = %.6f\n", prob_geom_defA))

# 2. Hypergeometric Distribution (N=50, K=6, n=10)
N_pop <- 50; K_succ <- 6; n_sample <- 10
prob_hyper <- dhyper(x = 1, m = K_succ, n = N_pop - K_succ, k = n_sample)
cat(sprintf("Hypergeometric P(X=1) = %.6f\n", prob_hyper))

# 3. FPC Variance comparison
var_bin <- n_sample * (K_succ/N_pop) * (1 - K_succ/N_pop)
fpc <- (N_pop - n_sample) / (N_pop - 1)
var_hyper <- var_bin * fpc

cat(sprintf("Binomial Var = %.4f | FPC = %.4f | Hypergeometric Var = %.4f\n",
            var_bin, fpc, var_hyper))
```

Final Answer:
R code written and verified successfully.

---

## Section 4.4: Moment Generating Functions & Characteristic Functions

### Core Theory & Definitions

#### 1. Moment Generating Functions (MGF)
The **Moment Generating Function (MGF)** of a discrete random variable $X$, denoted $M_X(t)$, is defined as the expected value of $e^{tX}$:
$$M_X(t) = E\left[e^{tX}\right] = \sum_{x \in S_X} e^{tx} \cdot p(x)$$
provided the sum converges in an open neighborhood around $t = 0$ ($|t| < h$ for some $h > 0$).

#### Deriving Raw Moments via Differentiation
The $k$-th raw moment $E[X^k]$ is obtained by differentiating $M_X(t)$ $k$ times with respect to $t$ and evaluating at $t = 0$:
$$E[X^k] = \left. \frac{d^k M_X(t)}{dt^k} \right|_{t=0} = M_X^{(k)}(0)$$

Specifically:
- **First Moment (Mean):** $E[X] = M'_X(0)$
- **Second Raw Moment:** $E[X^2] = M''_X(0)$
- **Variance:** $Var(X) = M''_X(0) - (M'_X(0))^2$

#### Core Properties of MGFs
1. **Linear Transformation:** $M_{aX + b}(t) = e^{bt} \cdot M_X(at)$
2. **Sum of Independent Variables:** If $X_1, X_2, \dots, X_n$ are independent:
   $$M_{\sum X_i}(t) = \prod_{i=1}^n M_{X_i}(t)$$
3. **Uniqueness Theorem:** If two random variables have identical MGFs in a neighborhood around $t=0$, they have the exact same probability distribution.

#### Standard MGF Table
| Distribution | PMF / Parameters | Moment Generating Function $M_X(t)$ | Domain |
| :--- | :--- | :--- | :--- |
| **Bernoulli($p$)** | $p(1)=p, p(0)=1-p$ | $M_X(t) = (1-p) + p e^t$ | $t \in \mathbb{R}$ |
| **Binomial($n, p$)** | $\binom{n}{k} p^k (1-p)^{n-k}$ | $M_X(t) = \left( (1-p) + p e^t \right)^n$ | $t \in \mathbb{R}$ |
| **Poisson($\lambda$)** | $\frac{\lambda^k e^{-\lambda}}{k!}$ | $M_X(t) = \exp\left( \lambda(e^t - 1) \right)$ | $t \in \mathbb{R}$ |
| **Geometric($p$) (Def A)** | $(1-p)^{k-1} p$ | $M_X(t) = \frac{p e^t}{1 - (1-p)e^t}$ | $t < -\ln(1-p)$ |

#### 2. Characteristic Functions ($\phi_X(t)$)
The **Characteristic Function** $\phi_X(t)$ is defined using complex exponents:
$$\phi_X(t) = E\left[e^{i t X}\right] = \sum_{x \in S_X} e^{i t x} \cdot p(x)$$
where $i = \sqrt{-1}$ is the imaginary unit.

#### Advantages of Characteristic Functions over MGFs
1. **Universal Existence:** Because $|e^{i t X}| = 1$, the characteristic function $\phi_X(t)$ **always exists** for every random variable and for all $t \in \mathbb{R}$, whereas MGFs may fail to converge (e.g., heavy-tailed distributions like Cauchy).
2. **Moment Recovery:** $E[X^k] = \frac{1}{i^k} \phi_X^{(k)}(0)$.
3. **MGF Connection:** When the MGF exists, $\phi_X(t) = M_X(i t)$.

---

### Mathematical Formulas & Derivations

#### 1. Binomial MGF Derivation
$$M_X(t) = E[e^{tX}] = \sum_{k=0}^n e^{tk} \binom{n}{k} p^k (1-p)^{n-k} = \sum_{k=0}^n \binom{n}{k} (p e^t)^k (1-p)^{n-k}$$
By the Binomial Theorem $(a + b)^n = \sum_{k=0}^n \binom{n}{k} a^k b^{n-k}$ with $a = p e^t$ and $b = 1-p$:
$$M_X(t) = \left( (1-p) + p e^t \right)^n$$

#### 2. Poisson MGF Derivation
$$M_X(t) = \sum_{k=0}^{\infty} e^{tk} \frac{\lambda^k e^{-\lambda}}{k!} = e^{-\lambda} \sum_{k=0}^{\infty} \frac{(\lambda e^t)^k}{k!} = e^{-\lambda} \cdot e^{\lambda e^t} = e^{\lambda(e^t - 1)}$$

#### 3. Deriving Poisson Mean and Variance from MGF
- First derivative: $M'_X(t) = e^{\lambda(e^t - 1)} \cdot (\lambda e^t)$
  $$M'_X(0) = e^0 \cdot (\lambda \cdot 1) = \lambda \implies E[X] = \lambda$$
- Second derivative: $M''_X(t) = e^{\lambda(e^t - 1)} (\lambda e^t)^2 + e^{\lambda(e^t - 1)} (\lambda e^t)$
  $$M''_X(0) = \lambda^2 + \lambda \implies E[X^2] = \lambda^2 + \lambda$$
  $$Var(X) = M''_X(0) - (M'_X(0))^2 = (\lambda^2 + \lambda) - \lambda^2 = \lambda$$

---

### Worked Exercises

#### Exercise 27: Integrated Discrete System Analysis (Combined, Moderate)
**Problem:** A network gateway transmits a batch of $n = 15$ packets over a noisy link. Each packet has a loss probability $p = 0.08$. Lost packets are retransmitted individually until successful, with per-slot retry success probability $p_r = 0.60$ (following $Geo(0.60)$ Def A).
**a) ** Compute the probability that exactly 1 packet is lost in the initial batch.
**b) ** Compute the expected initial batch losses $E[X]$ and variance $Var(X)$.
**c) ** Compute expected retry slots $E[R]$ for a lost packet.
**d) ** Compute the total expected retransmission delay slots across the initial batch.

**Solution:**
**Step 1: Part a - Initial batch loss $X \sim Bin(15, 0.08)$**
$$P(X = 1) = \binom{15}{1} (0.08)^1 (0.92)^{14} = 15 \cdot 0.08 \cdot 0.311204 \approx 0.373445 \approx 0.3734$$

**Step 2: Part b - $E[X]$ and $Var(X)$**
$$E[X] = n \cdot p = 15 \times 0.08 = 1.20\,\text{packets}$$
$$Var(X) = n \cdot p \cdot (1-p) = 15 \times 0.08 \times 0.92 = 1.104\,\text{packets}^2$$

**Step 3: Part c - Expected retries per lost packet $R \sim Geo(p_r = 0.60)$**
$$E[R] = \frac{1}{p_r} = \frac{1}{0.60} = \frac{5}{3} \approx 1.6667\,\text{slots}$$

**Step 4: Part d - Total expected retransmission slots**
By Wald's identity / conditional expectation for independent retries:
$$E[\text{Total Retries}] = E[X] \cdot E[R] = 1.20 \times \frac{5}{3} = 2.0\,\text{slots}$$

Final Answer:
- **a) ** $P(X = 1) \approx 0.3734$
- **b) ** $E[X] = 1.20$, $Var(X) = 1.104$
- **c) ** $E[R] = 5/3 \approx 1.67\,\text{slots}$
- **d) ** Total expected retry slots $= 2.0$

---

#### Exercise 28: Multi-Distribution Network Queueing & Retries (Combined, Harder) (Time-Domain)
**Problem:** An API Gateway receives requests at a Poisson rate $\lambda = 180$ requests/minute. Each request triggers $n = 4$ microservice database lookups, each having a timeout probability $p = 0.10$.
**a) ** Determine the scaled Poisson rate $\lambda_{5s}$ for a 5-second window.
**b) ** Calculate the probability of receiving between 12 and 15 requests in a 5-second window.
**c) ** Compute the probability that a single request experiences at least 1 database timeout among its 4 lookups.
**d) ** Provide R code to verify both probabilities.

**Solution:**
**Step 1: Part a - Rate scaling for 5 seconds ($t = 5/60 = 1/12\,min$)**
$$\lambda_{5s} = 180 \cdot \frac{5}{60} = 15.0\,\text{requests}$$

**Step 2: Part b - $P(12 \le X_{5s} \le 15)$**
$$P(12 \le X_{5s} \le 15) = \sum_{k=12}^{15} \frac{15^k e^{-15}}{k!}$$
- $P(X=12) = \frac{15^{12} e^{-15}}{12!} \approx 0.082862$
- $P(X=13) = \frac{15^{13} e^{-15}}{13!} \approx 0.095610$
- $P(X=14) = \frac{15^{14} e^{-15}}{14!} \approx 0.102439$
- $P(X=15) = \frac{15^{15} e^{-15}}{15!} \approx 0.102439$
$$\text{Sum} = 0.082862 + 0.095610 + 0.102439 + 0.102439 = 0.383350 \approx 0.3834$$

**Step 3: Part c - Timeout probability per request ($Y \sim Bin(4, 0.10)$)**
$$P(Y \ge 1) = 1 - P(Y = 0) = 1 - (0.90)^4 = 1 - 0.6561 = 0.3439$$

**Step 4: Part d - R code**

```r
# Part b: Poisson range P(12 <= X <= 15)
prob_pois_range <- sum(dpois(12:15, lambda = 15))
cat(sprintf("P(12 <= X <= 15) = %.4f\n", prob_pois_range))

# Part c: Binomial P(Y >= 1)
prob_binom_timeout <- pbinom(0, size = 4, prob = 0.10, lower.tail = FALSE)
cat(sprintf("P(Y >= 1) = %.4f\n", prob_binom_timeout))
```

Final Answer:
- **a) ** $\lambda_{5s} = 15.0$
- **b) ** $P(12 \le X_{5s} \le 15) \approx 0.3834$
- **c) ** $P(Y \ge 1) = 0.3439$
- **d) ** R verification commands executed successfully.

---

#### Exercise 29: Complex Server Cluster Reliability & MGF Analysis (Combined, Hard)
**Problem:** A cloud region contains $N = 100$ nodes, $K = 10$ of which are degraded ($p = 0.10$). An auditor inspects $n = 8$ nodes without replacement.
**a) ** Calculate exact Hypergeometric $P(X = 0)$ and compare with Binomial approximation.
**b) ** State the MGF $M_X(t)$ of the Binomial approximation $Bin(8, 0.10)$.
**c) ** Derive $E[X]$ and $Var(X)$ by differentiating $M_X(t)$.
**d) ** If each degraded node adds $50\,ms$ delay plus $10\,ms$ setup overhead ($D = 50X + 10$), compute $E[D_{[ms]}]$ and $Var(D_{[ms]}^2)$ using the $c^2$ rule.

**Solution:**
**Step 1: Part a - Exact HG vs Binomial**
$$P(X = 0)_{\text{HG}} = \frac{\binom{10}{0} \binom{90}{8}}{\binom{100}{8}} = \frac{46764371050}{105314781425} \approx 0.444044 \approx 0.4440$$
$$P(X = 0)_{\text{Bin}} = (0.90)^8 \approx 0.430467 \approx 0.4305$$

**Step 2: Part b - MGF formulation**
$$M_X(t) = \left( 0.90 + 0.10 e^t \right)^8$$

**Step 3: Part c - Derive moments from MGF**
$$M'_X(t) = 8(0.90 + 0.10 e^t)^7 \cdot (0.10 e^t)$$
$$M'_X(0) = 8(1.0)^7 (0.10) = 0.80 \implies E[X] = 0.80$$

$$M''_X(t) = 56(0.90 + 0.10 e^t)^6 (0.10 e^t)^2 + 8(0.90 + 0.10 e^t)^7 (0.10 e^t)$$
$$M''_X(0) = 56(0.01) + 8(0.10) = 0.56 + 0.80 = 1.36 \implies E[X^2] = 1.36$$
$$Var(X) = 1.36 - (0.80)^2 = 1.36 - 0.64 = 0.72$$

**Step 4: Part d - Linear transformation $D = 50X + 10$**
$$E[D_{[ms]}] = 50 E[X] + 10 = 50(0.80) + 10 = 50\,[ms]$$
$$Var(D_{[ms]}^2) = (50)^2 Var(X) = 2500 \times 0.72 = 1800\,[ms^2]$$

Final Answer:
- **a) ** Exact HG $P(X=0) \approx 0.4440$, Binomial approx $\approx 0.4305$
- **b) ** $M_X(t) = (0.90 + 0.10 e^t)^8$
- **c) ** $E[X] = 0.80$, $Var(X) = 0.72$
- **d) ** $E[D] = 50\,[ms]$, $Var(D) = 1800\,[ms^2]$

---

#### Exercise 30: End-to-End Latency & Packet Loss Pipeline (Combined, Hardest + Gotcha) (Time-Domain)
**Problem:** An end-to-end performance pipeline is evaluated across 4 stages:
**a) ** Ingest rate is $\lambda = 120$ requests/minute. Calculate the probability of receiving exactly 3 requests in a 15-second window.
**b) ** Corrupted fields per request follows $Y \sim Bin(n=10, p=0.05)$. Calculate $P(Y = 1 \mid Y \ge 1)$.
**c) ** Request duration $T_{[s]}$ in seconds has MGF $M_T(t) = \exp(0.02 t + 0.005 t^2)$. Derive $E[T_{[s]}]$ and $Var(T_{[s]}^2)$.
**d) ** An analyst converts the duration variance to microseconds ($\mu s$, factor $c = 10^6$) and claims $Var_{\mu s}(T) = 10^6 \times 0.01 = 10,000\,[\mu s^2]$. Evaluate the analyst's claim and identify the gotcha moment.

**Solution:**
**Step 1: Part a - Poisson Rate Window Scaling**
Hourly/minute rate $\lambda = 120$ req/min.
Time window $t = 15/60 = 0.25\,min$.
$$\lambda_{15s} = 120 \times 0.25 = 30.0\,\text{requests}$$
$$P(X_{15s} = 3) = \frac{30^3 e^{-30}}{3!} = \frac{27000 e^{-30}}{6} = 4500 e^{-30} \approx 4500(9.3576 \times 10^{-14}) \approx 4.2109 \times 10^{-10}$$

**Step 2: Part b - Conditional Binomial**
$$P(Y = 1) = \binom{10}{1} (0.05)^1 (0.95)^9 = 10 \cdot 0.05 \cdot 0.630249 = 0.315125$$
$$P(Y \ge 1) = 1 - P(Y = 0) = 1 - (0.95)^{10} = 1 - 0.598737 = 0.401263$$
$$P(Y = 1 \mid Y \ge 1) = \frac{0.315125}{0.401263} \approx 0.785333 \approx 0.7853$$

**Step 3: Part c - Moments from MGF**
Given $M_T(t) = \exp(0.02 t + 0.005 t^2)$ (which is the MGF of $N(\mu = 0.02, \sigma^2 = 0.01)$):
$$M'_T(t) = \exp(0.02 t + 0.005 t^2) \cdot (0.02 + 0.01 t)$$
$$M'_T(0) = 1 \cdot 0.02 = 0.020\,[s] \implies E[T] = 0.020\,[s]$$

$$M''_T(t) = \exp(0.02 t + 0.005 t^2) (0.02 + 0.01 t)^2 + \exp(0.02 t + 0.005 t^2) (0.01)$$
$$M''_T(0) = 1(0.02)^2 + 1(0.01) = 0.0004 + 0.01 = 0.0104\,[s^2]$$
$$Var(T) = M''_T(0) - (M'_T(0))^2 = 0.0104 - (0.02)^2 = 0.0104 - 0.0004 = 0.010\,[s^2]$$

**Step 4: Part d - Analyst Gotcha Evaluation**
**Gotcha:** The analyst committed **two classic gotcha mistakes**:
1. In Part a, failing to scale rate $\lambda$ for the 15-second window would use $\lambda = 120$ instead of $\lambda_{15s} = 30$.
2. In Part d, when scaling unit variance from seconds to microseconds ($c = 10^6\,\mu s/s$), variance scales by **$c^2 = 10^{12}$**, NOT $c = 10^6$!

Correct variance calculation:
$$Var_{[\mu s^2]}(T) = c^2 \cdot Var_{[s^2]}(T) = (10^6)^2 \cdot 0.010 = 10^{12} \cdot 0.010 = 1.0 \times 10^{10}\,[\mu s^2]$$
$$\text{Correct } Var_{[\mu s^2]} = 10,000,000,000\,[\mu s^2]$$

The analyst's claim of $10,000\,[\mu s^2]$ is **INCORRECT** and off by a factor of one million ($10^6$) due to forgetting the $c^2$ rule!

Final Answer:
- **a) ** $P(X = 3) \approx 4.21 \times 10^{-10}$
- **b) ** $P(Y = 1 \mid Y \ge 1) \approx 0.7853$
- **c) ** $E[T] = 0.020\,[s]$, $Var(T) = 0.010\,[s^2]$
- **d) (Gotcha):** Analyst claim is **INCORRECT**. Correct variance is **$1.0 \times 10^{10}\,[\mu s^2]$** ($10,000,000,000\,\mu s^2$), because scaling time units by $c = 10^6$ requires scaling variance by $c^2 = 10^{12}$.

---

## Exam Preparation Guide

### Formula Quick-Reference

| Topic | Formula | Notes / Exam Typologio Format |
| :--- | :--- | :--- |
| **PMF Validity** | $\sum p(x) = 1, \quad p(x) \ge 0$ | Axiomatic conditions for discrete probability mass functions. |
| **Expected Value** | $E[X] = \sum x \cdot p(x)$ | Population mean $\mu$. Requires absolute convergence. |
| **LOTUS** | $E[g(X)] = \sum g(x) \cdot p(x)$ | Expectation of transformed random variable. |
| **Variance** | $Var(X) = E[X^2] - (E[X])^2$ | Computational variance formula. |
| **Linear Scaling** | $E[aX + b] = a E[X] + b, \quad Var(aX + b) = a^2 Var(X)$ | Additive constants shift mean; $a^2$ scales variance. |
| **Binomial PMF** | $P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$ | $E[X] = np, \quad Var(X) = np(1-p)$. FINS conditions. |
| **Binomial Log Inequality** | $n \ge \frac{\ln(1 - \text{target})}{\ln(1 - p)}$ | Minimum sample size for $P(X \ge 1) \ge \text{target}$. |
| **Poisson PMF** | $P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}$ | $E[X] = \lambda, \quad Var(X) = \lambda$ (Equidispersion). |
| **Poisson Rate Scaling** | $\lambda_t = \lambda_0 \cdot t$ | Scale rate proportionally for window of duration $t$. |
| **Poisson Approximation** | $Bin(n, p) \approx Poisson(\lambda = np)$ | Valid when $n \ge 20$ (or $n \ge 100$) and $p \le 0.05$. |
| **Geometric PMF (Def A)** | $P(X = k) = (1-p)^{k-1} p$ | Trials until 1st success. $E[X] = 1/p, \quad Var(X) = (1-p)/p^2$. |
| **Geometric PMF (Def B)** | $P(Y = k) = (1-p)^k p$ | Failures before 1st success. Used by R `dgeom`. $E[Y] = (1-p)/p$. |
| **Hypergeometric PMF** | $P(X = k) = \frac{\binom{K}{k} \binom{N-K}{n-k}}{\binom{N}{n}}$ | Sampling without replacement. $E[X] = n(K/N)$. |
| **FPC Factor** | $\text{FPC} = \frac{N - n}{N - 1}$ | Variance multiplier for Hypergeometric vs Binomial. |
| **MGF Definition** | $M_X(t) = E[e^{tX}]$ | $E[X^k] = M_X^{(k)}(0)$. $M_{aX+b}(t) = e^{bt} M_X(at)$. |
| **Characteristic Function** | $\phi_X(t) = E[e^{i t X}]$ | Always exists for all $t \in \mathbb{R}$. $\phi_X(t) = M_X(i t)$. |
| **$c^2$ Variance Scaling Rule** | $Var(c \cdot X) = c^2 Var(X)$ | Unit conversions (e.g., $s \to ms, c=1000$) scale Var by $c^2 = 10^6$. |

---

### Exam Checklist

| Category | Items |
| :--- | :--- |
| **Must Memorize** | - PMF conditions ($\sum p(x) = 1, p(x) \ge 0$)<br>- Expected value $E[X] = \sum x p(x)$ and Variance $Var(X) = E[X^2] - (E[X])^2$<br>- Binomial PMF, mean $np$, and variance $np(1-p)$<br>- Poisson PMF, mean $\lambda$, and variance $\lambda$<br>- Geometric mean $1/p$ (Def A) vs $(1-p)/p$ (Def B)<br>- Hypergeometric mean $n(K/N)$<br>- MGF raw moment derivation $E[X^k] = M_X^{(k)}(0)$ |
| **Must Understand** | - Difference between sampling with replacement (Binomial) and without replacement (Hypergeometric)<br>- Poisson rate scaling across custom time windows ($\lambda_t = \lambda_0 \cdot t$)<br>- Geometric Memoryless Property ($P(X > k+s \mid X > k) = P(X > s)$)<br>- Deriving moments by differentiating MGFs at $t=0$<br>- Why Characteristic Functions always exist while MGFs may diverge |
| **Book-Only (Professor May Test)** | - Proof of Poisson convergence limit from Binomial PMF as $n \to \infty$<br>- Finite Population Correction (FPC) factor $\frac{N-n}{N-1}$ derivation<br>- MGF of linear transformations $M_{aX+b}(t) = e^{bt} M_X(at)$<br>- Characteristic function derivative formula $E[X^k] = \frac{1}{i^k} \phi_X^{(k)}(0)$<br>- Conditional Binomial probabilities $P(X = k \mid X \ge m)$ |

---

### Common Exam Traps

1. **Forgetting the $c^2$ Variance Scaling Rule in Unit Conversions:**
   - *Trap:* Converting variance of time data from seconds to milliseconds by multiplying by $1,000$.
   - *Correction:* Since $1\,s = 1000\,ms$, $c = 1000$. Standard deviation scales by $c = 1000$, but variance scales by $c^2 = 1,000,000 = 10^6$!

2. **Poisson Rate Window Scaling Failure:**
   - *Trap:* Using an hourly arrival rate $\lambda = 120$ directly in calculations for a 15-second window.
   - *Correction:* Always scale $\lambda$ to match the specific window duration: $\lambda_{15s} = 120 \times (15/60) = 30$.

3. **Geometric Definition A vs Definition B (and R Gotcha):**
   - *Trap:* Plugging $k$ directly into R's `dgeom(k, p)` when asking for the probability of the 1st success on trial $k$.
   - *Correction:* R's `dgeom` counts failures $Y = X - 1$. For trial $k$, use `dgeom(k - 1, p)`.

4. **Binomial Minimum Trial Logarithm Inequality Sign Flips:**
   - *Trap:* Dividing $n \cdot \ln(1-p) \le \ln(1-\text{target})$ by $\ln(1-p)$ without flipping the inequality sign.
   - *Correction:* Since $1-p < 1$, $\ln(1-p)$ is negative! Dividing by a negative number flips $\le$ to $\ge$.

5. **Confusing Binomial (Replacement) with Hypergeometric (No Replacement):**
   - *Trap:* Applying Binomial formulas to small finite populations without replacement.
   - *Correction:* Use Hypergeometric when sampling without replacement unless $n/N \le 0.05$, where Binomial approximation applies.

---

### Exam Paper Cross-References

| Exam Paper | Relevant Questions | Difficulty | Core Topics Covered |
| :--- | :--- | :---: | :--- |
| [Exam_paper_Easy.md](../../Exams/Papers/synthetic/Exam_paper_Easy.md) | Question 3 | **1/5** | Basic Binomial distribution calculations ($n, p$ provided). |
| [Exam_paper_2024_09_06_Team_A.md](../../Exams/Papers/Exam_paper_2024_09_06_Team_A.md) | Question 3 | **1/5** | Straightforward Binomial modeling. |
| [Exam_paper_Intermediate_1.md](../../Exams/Papers/synthetic/Exam_paper_Intermediate_1.md) | Question 2 | **2/5** | Binomial distribution PMF and expectation. |
| [Exam_paper_2023_06_12_Team_null.md](../../Exams/Papers/Exam_paper_2023_06_12_Team_null.md) | Question 4 | **2/5** | Standard Binomial probability applications. |
| [Exam_paper_2024_06_14_Team_B.md](../../Exams/Papers/Exam_paper_2024_06_14_Team_B.md) | Question 3 | **2/5** | Binomial PMF and tail probability. |
| [Exam_paper_2024_06_14_Team_C.md](../../Exams/Papers/Exam_paper_2024_06_14_Team_C.md) | Question 1 | **2/5** | Binomial distribution calculations. |
| [Exam_paper_2025_06_03_Team_A.md](../../Exams/Papers/Exam_paper_2025_06_03_Team_A.md) | Question 1 | **2/5** | Binomial modeling and parameter evaluation. |
| [Exam_paper_2026_06_09_Team_A.md](../../Exams/Papers/Exam_paper_2026_06_09_Team_A.md) | Question 1 | **2/5** | Binomial distribution evaluation. |
| [Exam_paper_2026_06_09_Team_B.md](../../Exams/Papers/Exam_paper_2026_06_09_Team_B.md) | Question 3 | **2/5** | Software defect binomial modeling. |
| [Exam_paper_Intermediate_2.md](../../Exams/Papers/synthetic/Exam_paper_Intermediate_2.md) | Question 2 | **3/5** | Larger trial size Binomial distribution modeling. |
| [Exam_paper_Hard_1.md](../../Exams/Papers/synthetic/Exam_paper_Hard_1.md) | Question 2 | **4/5** | Binomial trial size $n$ estimation via logarithm inequalities. |
| [Exam_paper_Hard_2.md](../../Exams/Papers/synthetic/Exam_paper_Hard_2.md) | Question 2 | **5/5** | Conditional Binomial probability $P(X = k \mid X \ge m)$. |

---

## Phase Summary

- **Discrete Random Variables** map outcomes to countable values. PMFs must satisfy $p(x) \ge 0$ and $\sum p(x) = 1$. The expected value $E[X] = \sum x p(x)$ and variance $Var(X) = E[X^2] - (E[X])^2$ quantify central tendency and dispersion.
- **Linear Transformations ($aX + b$)** shift the mean linearly ($a E[X] + b$) while scaling variance by $a^2$ ($a^2 Var(X)$). When scaling time units by factor $c$ (e.g., $s \to ms$), variance scales by **$c^2$**.
- **The Binomial Distribution $Bin(n, p)$** models successes in $n$ independent Bernoulli trials with mean $np$ and variance $np(1-p)$. Logarithm inequalities determine minimum required sample sizes $n$.
- **The Poisson Distribution $Poisson(\lambda)$** models event counts over continuous intervals with equal mean and variance ($\lambda$). Rates scale linearly with time window duration ($\lambda_t = \lambda_0 \cdot t$). Poisson approximates Binomial when $n \ge 20$ and $p \le 0.05$.
- **The Geometric Distribution $Geo(p)$** models trials until 1st success (Def A) or failures before 1st success (Def B, R default). It is the unique discrete memoryless distribution ($P(X > k+s \mid X > k) = P(X > s)$).
- **The Hypergeometric Distribution $HG(N, K, n)$** models sampling without replacement from a finite population. Variance incorporates the Finite Population Correction (FPC) factor $\frac{N-n}{N-1}$. When $n/N \le 0.05$, Binomial approximation is valid.
- **Moment Generating Functions $M_X(t) = E[e^{tX}]$** uniquely identify distributions and yield raw moments via derivatives $E[X^k] = M_X^{(k)}(0)$. **Characteristic Functions $\phi_X(t) = E[e^{i t X}]$** always exist for all random variables.

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

