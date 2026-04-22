# Statistics Notes - Full Compilation

Generated from individual lecture phases.

---

<!-- Source: Phase_1_Descriptive_Statistics/phase_1_1_data_organization.md -->
# Phase 1.1: Data Organization

Data organization is the first step in descriptive statistics. It involves transforming raw data into a structured format, primarily through **Frequency Tables**. This allows us to see patterns, distributions, and summary characteristics of the dataset.

## 1. Core Concepts and Notation

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

---

## 2. Essential Formulas for Grouping Data
When datasets are large or continuous, we group them into **Class Intervals**.

1.  **Range ($R$):** $R = x_{max} - x_{min}$
2.  **Number of Classes ($k$):** (Sturges' Rule) $k = 1 + 3.322 \cdot \log_{10}(n)$
3.  **Class Width ($w$):** $w = \frac{R}{k}$ (Always round up for convenience in manual tables).
4.  **Class Mark ($x_i$):** Midpoint of the interval: $x_i = \frac{\text{Lower} + \text{Upper}}{2}$

---

## 3. Solved Exercises (8 Examples)

### Exercise 1: Categorical Data (Qualitative)
**Problem:** A survey of 15 people asked for their favorite color among: Red (R), Blue (B), and Green (G). The results: `R, B, B, G, R, B, G, G, B, B, R, G, B, B, R`. Create a frequency table.

**Solution:**
1.  **Count:** Red (4), Blue (7), Green (4). Total $n=15$.
2.  **Relative Frequency:** $h_{Red} = 4/15 \approx 0.267$.

| Color | $f_i$ | $h_i$ | $F_i$ | $H_i$ |
| :--- | :--- | :--- | :--- | :--- |
| Red | 4 | 0.267 | 4 | 0.267 |
| Blue | 7 | 0.467 | 11 | 0.734 |
| Green | 4 | 0.267 | 15 | 1.001 |

*(Note: The $H_i$ column sums to 1.001 due to rounding each $h_i$ to 3 decimal places. This is a standard rounding artifact — see the Exam Tip at the end of this file.)*

---

### Exercise 2: Discrete Data (Ungrouped)
**Problem:** Number of siblings for 10 students: `0, 1, 2, 1, 0, 3, 2, 1, 1, 2`.

**Solution:**
Identify unique values: 0, 1, 2, 3.

| Siblings ($x_i$) | $f_i$ | $h_i$ | $F_i$ |
| :--- | :--- | :--- | :--- |
| 0 | 2 | 0.2 | 2 |
| 1 | 4 | 0.4 | 6 |
| 2 | 3 | 0.3 | 9 |
| 3 | 1 | 0.1 | 10 |

---

### Exercise 3: Finding Missing Frequencies
**Problem:** A table has $n=20$. Given $f_1=5, f_2=?, f_3=8, f_4=2$. Find $f_2$ and $h_2$.

**Solution:**
1.  Sum condition: $5 + f_2 + 8 + 2 = 20$
2.  $15 + f_2 = 20 \Rightarrow f_2 = 5$
3.  $h_2 = 5/20 = 0.25$.

---

### Exercise 4: Grouping Continuous Data (Manual Range)
**Problem:** Group these 10 heights (cm) into 2 classes starting at 150: `152, 158, 161, 164, 165, 168, 172, 175, 177, 180`. Class width $w=15$.

**Solution:**
Intervals: `[150, 165)` and `[165, 180]`.
*   `[150, 165)`: 152, 158, 161, 164 (4 values)
*   `[165, 180]`: 165, 168, 172, 175, 177, 180 (6 values)

| Interval | $x_i$ | $f_i$ | $F_i$ |
| :--- | :--- | :--- | :--- |
| [150, 165) | 157.5 | 4 | 4 |
| [165, 180] | 172.5 | 6 | 10 |

---

### Exercise 5: Applying Sturges' Rule
**Problem:** For $n=40$ observations, find the ideal number of classes $k$.

**Solution:**
$$k = 1 + 3.322 \cdot \log_{10}(40)$$
$$k = 1 + 3.322 \cdot (1.602) \approx 1 + 5.32 = 6.32$$
Rounding up (as per the convention stated above), we use **7 classes**.

---

### Exercise 6: Interpreting Cumulative Frequency
**Problem:** In a table, $F_3 = 18$ and $F_2 = 12$. What is $f_3$?

**Solution:**
Since $F_3 = f_1 + f_2 + f_3$ and $F_2 = f_1 + f_2$:
$$f_3 = F_3 - F_2 = 18 - 12 = 6$$

---

### Exercise 7: Percentage Distribution
**Problem:** Convert relative frequencies $h_i = [0.15, 0.35, 0.50]$ into a percentage frequency table.

**Solution:**
Multiply $h_i$ by 100.

| Value | $h_i$ | Frequency % |
| :--- | :--- | :--- |
| A | 0.15 | 15% |
| B | 0.35 | 35% |
| C | 0.50 | 50% |

---

### Exercise 8: Full Table Construction (Work-in-Progress style)
**Problem:** Data: `10, 12, 15, 18, 20, 22, 25, 28, 30, 35`. Group into 3 classes with $w=10$, starting at 10.

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

---

## Exam Tip: The "Sum to One" Rule
If your relative frequencies ($h_i$) sum to 0.99 or 1.01 due to rounding, usually it is acceptable in exams, but try to use more decimal places (3 is standard) to get as close to **1.000** as possible.


---

<!-- Source: Phase_1_Descriptive_Statistics/phase_1_2_measures_central_tendency.md -->
# Phase 1.2: Measures of Central Tendency

Measures of central tendency are statistical values that represent the "center" or "typical" value of a dataset. The three most common measures are the **Mean**, **Median**, and **Mode**.

---

## 1. Core Formulas

### Mean ($\bar{x}$)
*   **Ungrouped:** $\bar{x} = \frac{\sum x_i}{n}$
*   **Grouped:** $\bar{x} = \frac{\sum f_i \cdot x_i}{n}$

### Median ($M_e$)
*   **Ungrouped:** Middle value (or average of two middle values) in an ordered list.
*   **Grouped (Interpolation):** $M_e = L + \left( \frac{\frac{n}{2} - F_{i-1}}{f_i} \right) \cdot w$

### Mode ($M_o$)
*   **Ungrouped:** Most frequent value.
*   **Grouped (Interpolation):** $M_o = L + \left( \frac{f_i - f_{i-1}}{(f_i - f_{i-1}) + (f_i - f_{i+1})} \right) \cdot w$

---

## 2. Solved Exercises (8 Examples)

### Exercise 1: Simple Mean with Missing Value
**Problem:** The mean of five numbers is 10. Four of the numbers are 8, 12, 7, and 11. Find the fifth number.

**Solution:**
1.  Sum of 5 numbers = $5 \cdot 10 = 50$.
2.  Sum of 4 known numbers = $8 + 12 + 7 + 11 = 38$.
3.  Fifth number = $50 - 38 = 12$.

---

### Exercise 2: Median for Odd vs. Even $n$
**Problem:** Find the median for:
A) `3, 10, 2, 8, 5`
B) `3, 10, 2, 8, 5, 12`

**Solution:**
A) Order: `2, 3, 5, 8, 10`. $n=5$ (odd). Median is the 3rd value: **5**.
B) Order: `2, 3, 5, 8, 10, 12`. $n=6$ (even). Median is average of 3rd and 4th: $(5+8)/2 = \mathbf{6.5}$.

---

### Exercise 3: Multimodal Data
**Problem:** Find the mode of: `1, 2, 2, 3, 4, 4, 5`.

**Solution:**
Values 2 and 4 both appear twice. This dataset is **bimodal**. Modes are **2 and 4**.

---

### Exercise 4: Grouped Mean (Weighted Average)
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

---

### Exercise 5: Grouped Median (Interpolation)
**Problem:** Find $M_e$ for $n=40, w=10, L=20, f_i=12, F_{i-1}=8$.

**Solution:**
1.  $n/2 = 20$.
2.  $M_e = 20 + \left( \frac{20 - 8}{12} \right) \cdot 10 = 20 + (1) \cdot 10 = \mathbf{30}$.

---

### Exercise 6: Grouped Mode (Interpolation)
**Problem:** Modal class is [30, 40). $L=30, w=10, f_i=20, f_{i-1}=12, f_{i+1}=10$.

**Solution:**
$$M_o = 30 + \left( \frac{20 - 12}{(20-12) + (20-10)} \right) \cdot 10$$
$$M_o = 30 + \left( \frac{8}{8 + 10} \right) \cdot 10 = 30 + 4.44 = \mathbf{34.44}$$

---

### Exercise 7: Effect of Outliers
**Problem:** Data: `10, 10, 11, 12, 100`. Compare Mean and Median.

**Solution:**
1.  Mean = $(10+10+11+12+100)/5 = 28.6$.
2.  Median = Order: `10, 10, 11, 12, 100` $\Rightarrow$ **11**.
**Observation:** The outlier (100) pulled the mean far from the central cluster, while the median remained representative.

---

### Exercise 8: Finding Mean from Relative Frequencies
**Problem:** Given values $x_i = [1, 2, 3]$ and relative frequencies $h_i = [0.2, 0.5, 0.3]$. Find $\bar{x}$.

**Solution:**
For relative frequencies, the mean formula is $\bar{x} = \sum x_i \cdot h_i$.
$$\bar{x} = (1 \cdot 0.2) + (2 \cdot 0.5) + (3 \cdot 0.3)$$
$$\bar{x} = 0.2 + 1.0 + 0.9 = \mathbf{2.1}$$

---

## Exam Tip: Choosing the Best Measure
*   **Mean:** Best for symmetrical data without outliers.
*   **Median:** Best for skewed data or data with extreme outliers.
*   **Mode:** Best for categorical (qualitative) data.

### Skewness Relationship
| Condition | Distribution Shape |
| :--- | :--- |
| **Mean > Median** | **Positively Skewed** (right tail is longer) |
| **Mean < Median** | **Negatively Skewed** (left tail is longer) |
| **Mean = Median** | **Symmetric** (e.g., Normal distribution) |


---

<!-- Source: Phase_1_Descriptive_Statistics/phase_1_3_measures_position.md -->
# Phase 1.3: Measures of Position

Measures of position (or quantiles) are values that divide a sorted dataset into equal parts. The most common are **Quartiles** (divided into 4 parts) and **Percentiles** (divided into 100 parts).

---

## 1. Core Formulas

### Quantile Position (Ungrouped)
$$P = \frac{k(n+1)}{N_{parts}}$$
*   $k$: Quantile number (e.g., 1, 2, 3 for quartiles).
*   $n$: Total number of observations.
*   $N_{parts}$: 4 for quartiles, 100 for percentiles.

### Quantile Formula (Grouped Data)
$$Q = L + \left( \frac{\text{Position} - F_{i-1}}{f_i} \right) \cdot w$$
Where:
*   **Position** = $\frac{k \cdot n}{4}$ for quartiles or $\frac{k \cdot n}{100}$ for percentiles.

---

## 2. Solved Exercises (8 Examples)

### Exercise 1: Quartiles for Small $n$ (Ungrouped)
**Problem:** Find $Q_1, Q_2, Q_3$ for: `5, 8, 4, 10, 15, 21, 2`.

**Solution:**
1.  Order: `2, 4, 5, 8, 10, 15, 21`. $n=7$.
2.  $Q_2$ (Median): 4th value = **8**.
3.  $Q_1$: Median of lower half (`2, 4, 5`) = **4**.
4.  $Q_3$: Median of upper half (`10, 15, 21`) = **15**.

---

### Exercise 2: Percentile for Small $n$ (Ungrouped)
**Problem:** Find $P_{80}$ for: `10, 20, 30, 40, 50`.

**Solution:**
1.  Order: `10, 20, 30, 40, 50`. $n=5$.
2.  Position $P = \frac{80(5+1)}{100} = 4.8$.
3.  Interpolate between 4th (40) and 5th (50):
$$P_{80} = 40 + 0.8 \cdot (50 - 40) = 40 + 8 = \mathbf{48}$$

---

### Exercise 3: Grouped $Q_1$ (Interpolation)
**Problem:** $n=60, L=10, w=10, f_i=12, F_{i-1}=8$.

**Solution:**
1.  Position = $60/4 = 15$.
2.  $Q_1 = 10 + \left( \frac{15 - 8}{12} \right) \cdot 10 = 10 + \frac{70}{12} \approx \mathbf{15.83}$.

---

### Exercise 4: Grouped $Q_3$ (Interpolation)
**Problem:** $n=60, L=30, w=10, f_i=15, F_{i-1}=40$.

**Solution:**
1.  Position = $(3 \cdot 60)/4 = 45$.
2.  $Q_3 = 30 + \left( \frac{45 - 40}{15} \right) \cdot 10 = 30 + \frac{50}{15} \approx \mathbf{33.33}$.

---

### Exercise 5: Interquartile Range ($IQR$)
**Problem:** Using results from Ex 3 and 4 ($Q_1=15.83, Q_3=33.33$), find the $IQR$.

**Solution:**
$$IQR = Q_3 - Q_1 = 33.33 - 15.83 = \mathbf{17.50}$$

---

### Exercise 6: Percentile Rank (Grouped)
**Problem:** In a distribution, find the 10th percentile ($P_{10}$) if $n=100$, and the first class is [0, 20) with $f_i=15$.

**Solution:**
1.  Position = $(10 \cdot 100)/100 = 10$.
2.  $P_{10}$ class is [0, 20) since $15 \ge 10$.
3.  $L=0, w=20, f_i=15, F_{i-1}=0$.
$$P_{10} = 0 + \left( \frac{10 - 0}{15} \right) \cdot 20 = \frac{200}{15} \approx \mathbf{13.33}$$

---

### Exercise 7: Deciles ($D_k$)
**Problem:** Find the 7th decile ($D_7$) for $n=50, L=40, w=10, f_i=8, F_{i-1}=30$.

**Solution:**
Deciles divide into 10 parts. $D_7 = P_{70}$.
1.  Position = $(70 \cdot 50)/100 = 35$.
2.  $D_7 = 40 + \left( \frac{35 - 30}{8} \right) \cdot 10 = 40 + 6.25 = \mathbf{46.25}$.

---

### Exercise 8: Reverse Problem (Finding the Percentile)
**Problem:** A score of 45 falls in class [40, 50) where $f_i=10, F_{i-1}=30, n=50, w=10$. What percentile is this score?

**Solution:**
Set $P_k = 45$ and solve for $k$:
$$45 = 40 + \left( \frac{\frac{k \cdot 50}{100} - 30}{10} \right) \cdot 10$$
$$5 = 0.5k - 30 \Rightarrow 0.5k = 35 \Rightarrow k = 70$$
The score 45 is at the **70th percentile** ($P_{70}$).

---

## Exam Tip: The Five-Number Summary
Many exams ask for this summary to describe a dataset:
1.  Minimum
2.  $Q_1$
3.  Median ($Q_2$)
4.  $Q_3$
5.  Maximum
These are also the components used to draw a **Boxplot**.


---

<!-- Source: Phase_1_Descriptive_Statistics/phase_1_4_measures_dispersion.md -->
# Phase 1.4: Measures of Dispersion

Measures of dispersion (or variability) describe how "spread out" the values in a dataset are. While central tendency tells us where the center is, dispersion tells us how much the data deviates from that center.

---

## 1. Core Formulas

### Sample Variance ($s^2$)
$$s^2 = \frac{\sum (x_i - \bar{x})^2}{n - 1} \quad \text{or} \quad s^2 = \frac{\sum f_i(x_i - \bar{x})^2}{n - 1}$$

### Shortcut Variance Formula (Grouped)
$$s^2 = \frac{\sum f_i \cdot x_i^2 - \frac{(\sum f_i \cdot x_i)^2}{n}}{n - 1}$$

### Coefficient of Variation ($CV$)
$$CV = \frac{s}{\bar{x}} \cdot 100\%$$
*(Used to compare dispersion between datasets with different units or means.)*

---

## 2. Solved Exercises (8 Examples)

### Exercise 1: Range for Discrete Data
**Problem:** Find the range of: `10, 2, 35, 12, 18, 5`.

**Solution:**
1.  Max = 35, Min = 2.
2.  Range = $35 - 2 = \mathbf{33}$.

---

### Exercise 2: Sample Variance (Ungrouped)
**Problem:** Find $s^2$ for: `2, 4, 6`.

**Solution:**
1.  Mean $\bar{x} = (2+4+6)/3 = 4$.
2.  Deviations: $(2-4)=-2, (4-4)=0, (6-4)=2$.
3.  Squared: $4, 0, 4$. Sum = 8.
4.  $s^2 = 8 / (3-1) = \mathbf{4}$.

---

### Exercise 3: Population Standard Deviation ($\sigma$)
**Problem:** Data: `1, 3, 5`. Assume this is the *entire population*. Find $\sigma$.

**Solution:**
1.  $\mu = 3$.
2.  Squared deviations: $(1-3)^2=4, (3-3)^2=0, (5-3)^2=4$. Sum = 8.
3.  Population Variance $\sigma^2 = 8 / 3 \approx 2.67$.
4.  $\sigma = \sqrt{2.67} \approx \mathbf{1.63}$.

---

### Exercise 4: Grouped Variance (Standard Method)
**Problem:** $\sum f_i(x_i - \bar{x})^2 = 610, n=10$. Find sample variance.

**Solution:**
$$s^2 = 610 / (10 - 1) = 610 / 9 \approx \mathbf{67.78}$$

---

### Exercise 5: Grouped Variance (Shortcut Method)
**Problem:** $\sum f_i x_i = 100, \sum f_i x_i^2 = 2500, n=5$. Find $s^2$.

**Solution:**
$$s^2 = \frac{2500 - \frac{100^2}{5}}{5 - 1} = \frac{2500 - 2000}{4} = \frac{500}{4} = \mathbf{125}$$

---

### Exercise 6: Coefficient of Variation ($CV$)
**Problem:** Group A: $\bar{x}=50, s=10$. Group B: $\bar{x}=100, s=15$. Which group is more dispersed relative to its mean?

**Solution:**
1.  $CV_A = (10/50) \cdot 100 = 20\%$.
2.  $CV_B = (15/100) \cdot 100 = 15\%$.
**Group A** is more dispersed.

---

### Exercise 7: Identifying Outliers (The 1.5 IQR Rule)
**Problem:** $Q_1=10, Q_3=20$. Is the value 40 an outlier?

**Solution:**
1.  $IQR = 20 - 10 = 10$.
2.  Upper Fence = $Q_3 + 1.5 \cdot IQR = 20 + 15 = 35$.
3.  Since $40 > 35$, the value 40 is an **outlier**.

---

### Exercise 8: Effect of Transformation
**Problem:** Dataset $X$ has $s=5$. If every value is multiplied by 3 and then 10 is added ($Y = 3X + 10$), what is the new standard deviation?

**Solution:**
1.  Adding a constant (10) does **not** change dispersion.
2.  Multiplying by a constant (3) multiplies the standard deviation by that constant.
3.  $s_{new} = 3 \cdot 5 = \mathbf{15}$.

---

## Exam Tip: When to use CV
If a professor asks "Which stock is riskier?" or "Which machine is more consistent?", they usually want you to calculate the **Coefficient of Variation**, as it allows for a fair comparison between different scales.


---

<!-- Source: Phase_1_Descriptive_Statistics/phase_1_5_core_formulas_summary.md -->
# Phase 1.5: Core Formulas Summary (Grouped Data)

This file serves as a quick-reference guide for the mathematical foundation of Descriptive Statistics when dealing with **Grouped Data**.

---

## 1. Data Organization

*   **Class Mark ($x_i$):**
    $$x_i = \frac{L_{inf} + L_{sup}}{2}$$
*   **Relative Frequency ($h_i$):**
    $$h_i = \frac{f_i}{n}$$
*   **Sturges' Rule (Number of Classes $k$):**
    $$k = 1 + 3.322 \cdot \log_{10}(n)$$

---

## 2. Measures of Central Tendency

*   **Mean ($\bar{x}$):**
    $$\bar{x} = \frac{\sum f_i \cdot x_i}{n}$$
*   **Median ($M_e$):**
    $$M_e = L + \left( \frac{\frac{n}{2} - F_{i-1}}{f_i} \right) \cdot w$$
*   **Mode ($M_o$):**
    $$M_o = L + \left( \frac{f_i - f_{i-1}}{(f_i - f_{i-1}) + (f_i - f_{i+1})} \right) \cdot w$$

---

## 3. Measures of Position (Quantiles)

*   **General Percentile ($P_k$):**
    $$P_k = L + \left( \frac{\frac{k \cdot n}{100} - F_{i-1}}{f_i} \right) \cdot w$$
*   **Quartiles:** Use $k=25$ for $Q_1$, $k=50$ for $Q_2$, and $k=75$ for $Q_3$.

---

## 4. Measures of Dispersion

*   **Sample Variance ($s^2$):**
    $$s^2 = \frac{\sum f_i \cdot (x_i - \bar{x})^2}{n - 1}$$
*   **Shortcut Variance Formula:**
    $$s^2 = \frac{\sum f_i \cdot x_i^2 - \frac{(\sum f_i \cdot x_i)^2}{n}}{n - 1}$$
*   **Sample Standard Deviation ($s$):**
    $$s = \sqrt{s^2}$$
*   **Range ($R$):**
    $$R = x_{max} - x_{min}$$

---

## Exam Tip: Unit Consistency
Always remember that **Variance** is in squared units (e.g., $kg^2$), while **Mean**, **Median**, **Mode**, and **Standard Deviation** are in the original units (e.g., $kg$). If an exam asks for a "measure of spread in the original units," they are asking for the Standard Deviation or Range.


---

<!-- Source: Phase_2_Probability_Theory/phase_2_1_set_theory_fundamentals.md -->
# Phase 2.1: Set Theory Fundamentals

Set Theory provides the mathematical language used to define and manipulate probability. Every probability problem is, at its core, a question about sets. Understanding the formal notation and operations is the foundation upon which all probability rules are built.

---

## 1. Core Definitions

### Sample Space ($\Omega$)

The **Sample Space** $\Omega$ (also written $S$) is the set of **all possible outcomes** of a random experiment. Every outcome that could conceivably occur must be listed exactly once.

$$\Omega = \{ \text{all possible outcomes} \}$$

**Key rule:** The sample space is always exhaustive (covers everything) and mutually exclusive (no outcome appears twice).

### Event

An **Event** is any subset of the sample space. It is a collection of one or more outcomes. We typically label events with capital letters $A$, $B$, $C$, etc.

$$A \subseteq \Omega$$

*   **Elementary event:** A single outcome, e.g., $\{3\}$ when rolling a die.
*   **Compound event:** A collection of outcomes, e.g., $\{2, 4, 6\}$ (rolling an even number).
*   **Impossible event ($\emptyset$):** The empty set. An event with no outcomes that can never occur.
*   **Certain event ($\Omega$):** The entire sample space. This event always occurs.

---

## 2. Set Operations

These three operations are the building blocks of all probability expressions.

### Union ($\cup$)

The union $A \cup B$ is the event that **at least one** of $A$ or $B$ occurs. It contains every outcome in $A$, every outcome in $B$, or both.

$$A \cup B = \{ \omega \in \Omega : \omega \in A \text{ or } \omega \in B \}$$

> Think of $\cup$ as the logical **OR**.

### Intersection ($\cap$)

The intersection $A \cap B$ is the event that **both** $A$ and $B$ occur simultaneously. It contains only outcomes that are in $A$ AND in $B$.

$$A \cap B = \{ \omega \in \Omega : \omega \in A \text{ and } \omega \in B \}$$

> Think of $\cap$ as the logical **AND**.

### Complement ($A'$ or $A^c$)

The complement $A'$ is the event that $A$ does **not** occur. It contains all outcomes in $\Omega$ that are not in $A$.

$$A' = \{ \omega \in \Omega : \omega \notin A \}$$

A fundamental identity:

$$A \cup A' = \Omega \quad \text{and} \quad A \cap A' = \emptyset$$

$$P(A') = 1 - P(A)$$

---

## 3. Mutual Exclusivity (Disjoint Events)

Two events $A$ and $B$ are **mutually exclusive** (or disjoint) if they cannot both occur at the same time:

$$A \cap B = \emptyset$$

This is a crucial property. When $A$ and $B$ are mutually exclusive, the addition rule simplifies significantly:

$$P(A \cup B) = P(A) + P(B) \quad \text{(only when } A \cap B = \emptyset \text{)}$$

---

## 4. Summary of Notation

| Notation | Read as | Meaning |
| :--- | :--- | :--- |
| $\Omega$ | Sample space | All possible outcomes |
| $\emptyset$ | Empty set | Impossible event |
| $A \cup B$ | A union B | A or B (at least one) |
| $A \cap B$ | A intersect B | A and B (both) |
| $A'$ | A complement | Not A |
| $A \subseteq B$ | A is a subset of B | Every outcome in A is also in B |
| $A \cap B = \emptyset$ | A and B are disjoint | A and B cannot both occur |

---

## 5. Solved Exercises

### Exercise 1: Identifying the Sample Space (Die Roll)

**Problem:** A fair six-sided die is rolled once. Define the sample space and the event $A$ = "rolling a number greater than 4".

**Solution:**

$$\Omega = \{1, 2, 3, 4, 5, 6\}$$

$$A = \{5, 6\}$$

$$A' = \{1, 2, 3, 4\} \quad \text{(not rolling greater than 4)}$$

---

### Exercise 2: Identifying the Sample Space (Two Coin Tosses)

**Problem:** Two coins are tossed. Write out $\Omega$ using ordered pairs where H = Heads, T = Tails. Define event $B$ = "at least one Head".

**Solution:**

$$\Omega = \{(H,H), (H,T), (T,H), (T,T)\}$$

$$B = \{(H,H), (H,T), (T,H)\}$$

$$B' = \{(T,T)\} \quad \text{(no heads, i.e., both tails)}$$

---

### Exercise 3: Computing Union and Intersection

**Problem:** From the die-roll sample space $\Omega = \{1,2,3,4,5,6\}$, let:
- $A$ = "even number" = $\{2, 4, 6\}$
- $B$ = "number greater than 3" = $\{4, 5, 6\}$

Find $A \cup B$ and $A \cap B$.

**Solution:**

$$A \cup B = \{2, 4, 5, 6\} \quad \text{(all outcomes in either A or B)}$$

$$A \cap B = \{4, 6\} \quad \text{(outcomes in both: even AND greater than 3)}$$

---

### Exercise 4: Computing the Complement

**Problem:** Using $A = \{2, 4, 6\}$ from Exercise 3, find $A'$ and verify the fundamental identity.

**Solution:**

$$A' = \{1, 3, 5\}$$

**Verification:**

$$A \cup A' = \{2,4,6\} \cup \{1,3,5\} = \{1,2,3,4,5,6\} = \Omega \checkmark$$

$$A \cap A' = \{2,4,6\} \cap \{1,3,5\} = \emptyset \checkmark$$

---

### Exercise 5: Mutually Exclusive Check

**Problem:** From the die-roll experiment, are $A$ = "rolling 1 or 2" and $B$ = "rolling 5 or 6" mutually exclusive?

**Solution:**

$$A = \{1, 2\}, \quad B = \{5, 6\}$$

$$A \cap B = \emptyset$$

Yes, $A$ and $B$ are mutually exclusive. Rolling a 1 or 2 and simultaneously rolling a 5 or 6 is impossible in a single roll.

---

### Exercise 6: Three Events - Union and Intersection

**Problem:** A card is drawn from a standard 52-card deck. Define:
- $A$ = "card is a Heart"
- $B$ = "card is a King"
- $C$ = "card is red"

Describe $A \cap B$, $A \cup B$, and $B \cap C'$.

**Solution:**

*   $A \cap B$ = "Heart AND King" = $\{K\heartsuit\}$ — exactly 1 card.
*   $A \cup B$ = "Heart OR King" = all 13 Hearts plus the 3 remaining Kings (of Clubs, Diamonds, Spades) = 16 cards.
*   $B \cap C'$ = "King AND NOT red" = King of black suits = $\{K\clubsuit, K\spadesuit\}$ — 2 cards.

---

### Exercise 7: Subset Relationship

**Problem:** A number is picked from $\{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\}$. Let:
- $A$ = "multiple of 4" = $\{4, 8\}$
- $B$ = "even number" = $\{2, 4, 6, 8, 10\}$

Is $A$ a subset of $B$? What does this imply?

**Solution:**

Every element of $A$ ($4$ and $8$) is also in $B$, so $A \subseteq B$.

This means: if event $A$ occurs, then event $B$ must also occur. Knowing a number is a multiple of 4 guarantees it is also even. Formally: $A \subseteq B \Rightarrow A \cap B = A$.

---

### Exercise 8: Complement of a Compound Event

**Problem:** Continuing from Exercise 7, find $(A \cup B)'$.

**Solution:**

First, compute the union:

$$A \cup B = \{2, 4, 6, 8, 10\} = B \quad \text{(since } A \subseteq B \text{)}$$

The full sample space is $\Omega = \{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\}$.

$$(A \cup B)' = B' = \{1, 3, 5, 7, 9\} \quad \text{(all odd numbers)}$$

This is the set of outcomes where neither event A nor event B occurs. This outcome connects directly to De Morgan's Law: $(A \cup B)' = A' \cap B'$, which will be covered in Phase 2.3.

---

## Exam Tip: Listing vs. Describing Events

In exam problems, you may be asked to either **list** the outcomes of an event (e.g., $A = \{2, 4, 6\}$) or **describe** it in words. Practise translating freely between both forms. The most common error is forgetting to account for overlapping outcomes when computing unions — always check whether an element appears in both sets before listing it.


---

<!-- Source: Phase_2_Probability_Theory/phase_2_2_venn_diagrams.md -->
# Phase 2.2: Venn Diagrams & Translating Worded Problems

Venn Diagrams are a visual tool that maps relationships between events onto overlapping circles. Their primary purpose in probability is to **translate English language problem descriptions into precise set notation**, which can then be evaluated using formulas. Mastering this translation is one of the highest-leverage skills for exams.

---

## 1. Standard Venn Diagram Layout

For two events $A$ and $B$ within a sample space $\Omega$, the diagram divides the space into four mutually exclusive regions:

```
 ___________________________________
|              Omega                |
|   ___________   ___________       |
|  |           | |           |      |
|  |  A only   |A|   B only  |      |
|  |  (A∩B')   |∩|   (A'∩B)  |      |
|  |___________|B|___________|      |
|                                   |
|         (A∪B)' = A'∩B'            |
|___________________________________|
```

| Region | Set Notation | Meaning |
| :--- | :--- | :--- |
| Left circle only | $A \cap B'$ | A occurs, B does not |
| Overlapping center | $A \cap B$ | Both A and B occur |
| Right circle only | $A' \cap B$ | B occurs, A does not |
| Outside both circles | $A' \cap B'$ | Neither A nor B occurs |

The **fundamental partition rule**: the four regions are mutually exclusive and collectively exhaustive. Their probabilities sum to 1.

$$P(A \cap B') + P(A \cap B) + P(A' \cap B) + P(A' \cap B') = 1$$

---

## 2. Translating Key Phrases into Set Notation

This table is the most important reference in this file. Memorise these translations.

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
| "A but not B" | $A \cap B'$ | Same as "only A" |
| "At most one of A, B" | $(A \cap B)'$ = $A' \cup B'$ | Not both simultaneously |

> **Critical insight:** "At least one" means $A \cup B$. "Exactly one" means $A \cup B$ minus the case where both occur, i.e., $(A \cup B) \setminus (A \cap B)$.

---

## 3. Extending to Three Events

For three events $A$, $B$, $C$, the Venn Diagram has **8 mutually exclusive regions**. Key phrases extend naturally:

| Phrase | Set Notation |
| :--- | :--- |
| "All three occur" | $A \cap B \cap C$ |
| "At least one occurs" | $A \cup B \cup C$ |
| "None occur" | $A' \cap B' \cap C'$ = $(A \cup B \cup C)'$ |
| "Exactly one occurs" | $(A \cap B' \cap C') \cup (A' \cap B \cap C') \cup (A' \cap B' \cap C)$ |
| "At least two occur" | $(A \cap B \cap C') \cup (A \cap B' \cap C) \cup (A' \cap B \cap C) \cup (A \cap B \cap C)$ |

---

## 4. Reading Probabilities from a Filled Venn Diagram

When a Venn Diagram is given with numerical values already filled in, the values represent the probabilities (or counts) of each region. The key skill is to identify which regions belong to the event you are asked about, then sum them.

**Reading strategy:**
1. Identify all regions that satisfy the event description.
2. Sum the values in those regions.

---

## 5. Solved Exercises

### Exercise 1: Building a Venn Diagram from Counts

**Problem:** In a class of 50 students, 30 study Mathematics ($M$), 25 study Physics ($P$), and 15 study both. Find the number of students who study only Mathematics, only Physics, and neither subject.

**Solution:**

**Step 1:** Find the overlap region first.
$$|M \cap P| = 15$$

**Step 2:** Find "only Mathematics":
$$|M \cap P'| = |M| - |M \cap P| = 30 - 15 = 15$$

**Step 3:** Find "only Physics":
$$|M' \cap P| = |P| - |M \cap P| = 25 - 15 = 10$$

**Step 4:** Find "neither":
$$|M' \cap P'| = 50 - 15 - 15 - 10 = 10$$

**Filled Diagram regions:** Only M = 15, Both = 15, Only P = 10, Neither = 10. Total = 50. Verified.

---

### Exercise 2: Translating "At Least One"

**Problem:** $P(A) = 0.5$, $P(B) = 0.4$, $P(A \cap B) = 0.2$. Find the probability that at least one of $A$ or $B$ occurs.

**Solution:**

"At least one" translates to $A \cup B$.

$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

$$P(A \cup B) = 0.5 + 0.4 - 0.2 = 0.7$$

---

### Exercise 3: Translating "Neither"

**Problem:** Using the values from Exercise 2, find the probability that neither $A$ nor $B$ occurs.

**Solution:**

"Neither" translates to $A' \cap B' = (A \cup B)'$.

$$P((A \cup B)') = 1 - P(A \cup B) = 1 - 0.7 = 0.3$$

---

### Exercise 4: Translating "Exactly One"

**Problem:** Using the values from Exercise 2, find the probability that exactly one of $A$ or $B$ occurs.

**Solution:**

"Exactly one" = $(A \cap B') \cup (A' \cap B)$

**Method:** Total in at least one minus the overlap (where both occur):

$$P(\text{exactly one}) = P(A \cup B) - P(A \cap B)$$

$$P(\text{exactly one}) = 0.7 - 0.2 = 0.5$$

**Alternative breakdown:**
*   $P(A \cap B') = P(A) - P(A \cap B) = 0.5 - 0.2 = 0.3$
*   $P(A' \cap B) = P(B) - P(A \cap B) = 0.4 - 0.2 = 0.2$
*   $P(\text{exactly one}) = 0.3 + 0.2 = 0.5$ (same result)

---

### Exercise 5: Translating "Only A"

**Problem:** A survey shows $P(A) = 0.6$, $P(B) = 0.5$, $P(A \cup B) = 0.8$. Find $P(\text{only } A)$.

**Solution:**

**Step 1:** Find $P(A \cap B)$ using the addition rule:

$$P(A \cap B) = P(A) + P(B) - P(A \cup B) = 0.6 + 0.5 - 0.8 = 0.3$$

**Step 2:** "Only A" = $A \cap B'$:

$$P(A \cap B') = P(A) - P(A \cap B) = 0.6 - 0.3 = 0.3$$

---

### Exercise 6: Reading a Filled Venn Diagram

**Problem:** The regions of a Venn Diagram for events $A$ and $B$ are filled with the following probabilities:

| Region | Probability |
| :--- | :--- |
| Only $A$ ($A \cap B'$) | 0.25 |
| Both ($A \cap B$) | 0.15 |
| Only $B$ ($A' \cap B$) | 0.30 |
| Neither ($A' \cap B'$) | 0.30 |

Find: (a) $P(A)$, (b) $P(B)$, (c) $P(A \cup B)$, (d) $P(\text{exactly one})$.

**Solution:**

(a) $P(A) = P(A \cap B') + P(A \cap B) = 0.25 + 0.15 = 0.40$

(b) $P(B) = P(A' \cap B) + P(A \cap B) = 0.30 + 0.15 = 0.45$

(c) $P(A \cup B) = 0.25 + 0.15 + 0.30 = 0.70$

(d) $P(\text{exactly one}) = P(A \cap B') + P(A' \cap B) = 0.25 + 0.30 = 0.55$

**Verification:** $0.25 + 0.15 + 0.30 + 0.30 = 1.00$ (all regions sum to 1).

---

### Exercise 7: Three Events - "None"

**Problem:** $P(A \cup B \cup C) = 0.85$. Find the probability that none of the three events occur.

**Solution:**

"None occur" = $(A \cup B \cup C)'$

$$P(A' \cap B' \cap C') = 1 - P(A \cup B \cup C) = 1 - 0.85 = 0.15$$

---

### Exercise 8: Backward Problem - Finding an Unknown

**Problem:** Given $P(A) = 0.45$, $P(B) = 0.30$, and $P(\text{exactly one of } A, B) = 0.55$. Find $P(A \cap B)$.

**Solution:**

"Exactly one" can be written as:

$$P(\text{exactly one}) = P(A) + P(B) - 2 \cdot P(A \cap B)$$

This is derived from:

$$P(\text{exactly one}) = [P(A) - P(A \cap B)] + [P(B) - P(A \cap B)]$$

Substituting known values:

$$0.55 = 0.45 + 0.30 - 2 \cdot P(A \cap B)$$

$$0.55 = 0.75 - 2 \cdot P(A \cap B)$$

$$P(A \cap B) = \frac{0.75 - 0.55}{2} = \frac{0.20}{2} = 0.10$$

---

## Exam Tip: The Four-Region Decomposition

**Always decompose** a Venn Diagram into its four mutually exclusive regions at the start of a problem:

$$P(A \cap B'), \quad P(A \cap B), \quad P(A' \cap B), \quad P(A' \cap B')$$

Once these four values are known, **any probability expression** involving $A$ and $B$ can be computed by summing the appropriate regions. This method is infallible and prevents double-counting errors.


---

<!-- Source: Phase_2_Probability_Theory/phase_2_3_probability_axioms_rules.md -->
# Phase 2.3: Probability Axioms & Rules

The **Probability Axioms** (Kolmogorov's Axioms) are the three foundational rules from which all of probability theory is derived. The **Addition Rule** and **De Morgan's Laws** are the most practically important tools built on top of these axioms for computing probabilities in exam problems.

---

## 1. Kolmogorov's Axioms

For any event $A$ in a sample space $\Omega$, probability $P$ is a function that satisfies three axioms:

**Axiom 1 (Non-negativity):**

$$P(A) \geq 0$$

The probability of any event is always a non-negative real number.

**Axiom 2 (Normalization):**

$$P(\Omega) = 1$$

The probability of the certain event (something must happen) is exactly 1.

**Axiom 3 (Countable Additivity):**

If $A$ and $B$ are mutually exclusive ($A \cap B = \emptyset$):

$$P(A \cup B) = P(A) + P(B)$$

More generally, for any finite collection of mutually exclusive events $A_1, A_2, \ldots, A_n$:

$$P\left(\bigcup_{i=1}^{n} A_i\right) = \sum_{i=1}^{n} P(A_i)$$

---

## 2. Derived Properties (Consequences of the Axioms)

These results follow directly from the three axioms:

| Property | Formula | Derivation |
| :--- | :--- | :--- |
| Complement Rule | $P(A') = 1 - P(A)$ | From $P(A) + P(A') = P(\Omega) = 1$ |
| Impossible event | $P(\emptyset) = 0$ | From $\emptyset = \Omega'$ |
| Probability bounds | $0 \leq P(A) \leq 1$ | From Axioms 1 and 2 |
| Monotonicity | If $A \subseteq B$, then $P(A) \leq P(B)$ | B covers A plus more outcomes |

---

## 3. The Addition Rule (General)

For any two events $A$ and $B$ (not necessarily mutually exclusive):

$$\boxed{P(A \cup B) = P(A) + P(B) - P(A \cap B)}$$

**Why subtract?** When computing $P(A) + P(B)$, the overlap region $A \cap B$ is counted twice (once in $P(A)$ and once in $P(B)$). Subtracting $P(A \cap B)$ corrects for this double-counting.

**Special case — Mutually Exclusive:** When $A \cap B = \emptyset$:

$$P(A \cup B) = P(A) + P(B) - 0 = P(A) + P(B)$$

**Extension to three events:**

$$P(A \cup B \cup C) = P(A) + P(B) + P(C) - P(A \cap B) - P(A \cap C) - P(B \cap C) + P(A \cap B \cap C)$$

This pattern is called the **Inclusion-Exclusion Principle**.

---

## 4. De Morgan's Laws

De Morgan's Laws describe the complement of a union or intersection. They are one of the most tested identities in probability exams.

**First Law:**

$$\boxed{(A \cup B)' = A' \cap B'}$$

In probability:

$$P((A \cup B)') = P(A' \cap B')$$

Reading: "NOT (A or B)" is the same as "(NOT A) AND (NOT B)". Neither event occurs.

**Second Law:**

$$\boxed{(A \cap B)' = A' \cup B'}$$

In probability:

$$P((A \cap B)') = P(A' \cup B')$$

Reading: "NOT (A and B)" is the same as "(NOT A) OR (NOT B)". At least one event fails to occur.

**Intuition:** De Morgan's Laws "push the complement inside" while swapping the operator between $\cup$ and $\cap$.

| Operation | After applying De Morgan | Operator swap |
| :--- | :--- | :--- |
| $(A \cup B)'$ | $A' \cap B'$ | $\cup \to \cap$ |
| $(A \cap B)'$ | $A' \cup B'$ | $\cap \to \cup$ |

---

## 5. Computing $P(A' \cap B')$ and $P(A' \cup B')$

These are the two most common forms asked in problems:

**Computing "neither" $P(A' \cap B')$:**

Apply De Morgan's First Law, then use the complement rule:

$$P(A' \cap B') = P((A \cup B)') = 1 - P(A \cup B)$$

**Computing "not both" $P(A' \cup B')$:**

Apply De Morgan's Second Law, then use the complement rule:

$$P(A' \cup B') = P((A \cap B)') = 1 - P(A \cap B)$$

---

## 6. Solved Exercises

### Exercise 1: Direct Application of Addition Rule

**Problem:** $P(A) = 0.6$, $P(B) = 0.4$, $P(A \cap B) = 0.2$. Find $P(A \cup B)$.

**Solution:**

$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

$$P(A \cup B) = 0.6 + 0.4 - 0.2 = 0.8$$

---

### Exercise 2: Finding $P(A \cap B)$ from the Addition Rule

**Problem:** $P(A) = 0.5$, $P(B) = 0.45$, $P(A \cup B) = 0.7$. Find $P(A \cap B)$.

**Solution:**

Rearrange the addition rule to solve for the intersection:

$$P(A \cap B) = P(A) + P(B) - P(A \cup B)$$

$$P(A \cap B) = 0.5 + 0.45 - 0.7 = 0.25$$

---

### Exercise 3: Applying De Morgan's First Law

**Problem:** $P(A) = 0.5$, $P(B) = 0.4$, $P(A \cap B) = 0.2$. Find $P(A' \cap B')$.

**Solution:**

**Step 1:** Apply De Morgan's First Law:

$$P(A' \cap B') = P((A \cup B)')$$

**Step 2:** Compute $P(A \cup B)$ using the addition rule:

$$P(A \cup B) = 0.5 + 0.4 - 0.2 = 0.7$$

**Step 3:** Apply the complement rule:

$$P((A \cup B)') = 1 - 0.7 = 0.3$$

Therefore $P(A' \cap B') = 0.3$.

---

### Exercise 4: Applying De Morgan's Second Law

**Problem:** Using the same values as Exercise 3, find $P(A' \cup B')$.

**Solution:**

**Step 1:** Apply De Morgan's Second Law:

$$P(A' \cup B') = P((A \cap B)')$$

**Step 2:** Apply the complement rule:

$$P((A \cap B)') = 1 - P(A \cap B) = 1 - 0.2 = 0.8$$

Therefore $P(A' \cup B') = 0.8$.

---

### Exercise 5: Mutually Exclusive Events

**Problem:** Two events $A$ and $B$ are mutually exclusive. $P(A) = 0.35$, $P(B) = 0.25$. Find: (a) $P(A \cup B)$, (b) $P(A' \cap B')$.

**Solution:**

Since $A \cap B = \emptyset$, we have $P(A \cap B) = 0$.

(a) $P(A \cup B) = P(A) + P(B) = 0.35 + 0.25 = 0.60$

(b) $P(A' \cap B') = 1 - P(A \cup B) = 1 - 0.60 = 0.40$

---

### Exercise 6: Checking Axiom Compliance

**Problem:** A student claims: $P(A) = 0.7$, $P(B) = 0.6$, $P(A \cup B) = 0.8$. Is this consistent with the probability axioms?

**Solution:**

Compute $P(A \cap B)$ from the addition rule:

$$P(A \cap B) = 0.7 + 0.6 - 0.8 = 0.5$$

**Check 1:** Is $P(A \cap B) \geq 0$? Yes, $0.5 \geq 0$.

**Check 2:** Is $P(A \cap B) \leq P(A)$ and $P(A \cap B) \leq P(B)$? Yes, $0.5 \leq 0.7$ and $0.5 \leq 0.6$.

**Check 3:** Is $P(A \cup B) \leq 1$? Yes, $0.8 \leq 1$.

All axiom requirements are satisfied. The assignment is **consistent**.

---

### Exercise 7: Three-Event Inclusion-Exclusion

**Problem:** $P(A) = 0.4$, $P(B) = 0.3$, $P(C) = 0.5$, $P(A \cap B) = 0.1$, $P(A \cap C) = 0.15$, $P(B \cap C) = 0.1$, $P(A \cap B \cap C) = 0.05$. Find $P(A \cup B \cup C)$.

**Solution:**

$$P(A \cup B \cup C) = P(A) + P(B) + P(C) - P(A \cap B) - P(A \cap C) - P(B \cap C) + P(A \cap B \cap C)$$

$$= 0.4 + 0.3 + 0.5 - 0.1 - 0.15 - 0.1 + 0.05$$

$$= 1.2 - 0.35 + 0.05 = 0.90$$

---

### Exercise 8: Full Multi-Step Problem

**Problem:** In a group of 100 people, 60 own a car ($C$), 45 own a motorbike ($M$), and 20 own neither. Find: (a) the number who own both, (b) $P(C' \cap M')$, (c) $P(C' \cup M')$.

**Solution:**

**Step 1:** Number owning at least one = $100 - 20 = 80$, so $P(C \cup M) = 0.80$.

**Step 2:** Apply the addition rule to find $P(C \cap M)$:

$$P(C \cap M) = P(C) + P(M) - P(C \cup M)$$

$$P(C \cap M) = 0.60 + 0.45 - 0.80 = 0.25$$

Number owning both = $0.25 \times 100 = \mathbf{25}$.

**Step 3:** (b) "Neither" using De Morgan's First Law:

$$P(C' \cap M') = 1 - P(C \cup M) = 1 - 0.80 = 0.20$$

**Step 4:** (c) "Not both" using De Morgan's Second Law:

$$P(C' \cup M') = 1 - P(C \cap M) = 1 - 0.25 = 0.75$$

---

## 7. Core Formulas Summary

| Formula | Name | When to Use |
| :--- | :--- | :--- |
| $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ | Addition Rule | Finding union of any two events |
| $P(A') = 1 - P(A)$ | Complement Rule | Finding probability of "not A" |
| $(A \cup B)' = A' \cap B'$ | De Morgan's First Law | "Neither" problems |
| $(A \cap B)' = A' \cup B'$ | De Morgan's Second Law | "Not both" problems |
| $P(A' \cap B') = 1 - P(A \cup B)$ | Neither (derived) | Quickest path to "neither" |
| $P(A' \cup B') = 1 - P(A \cap B)$ | Not both (derived) | Quickest path to "not both" |

---

## Exam Tip: The De Morgan Shortcut

Whenever you see $P(A' \cap B')$ or $P(A' \cup B')$ in an exam, do not attempt to compute complements directly. Instead, apply De Morgan's Law immediately:

*   $P(A' \cap B') \xrightarrow{\text{De Morgan}} 1 - P(A \cup B)$: compute the union first, then subtract from 1.
*   $P(A' \cup B') \xrightarrow{\text{De Morgan}} 1 - P(A \cap B)$: compute the intersection first, then subtract from 1.

This two-step method is the fastest and most reliable approach and reduces complex complement expressions to standard addition rule problems.


---

<!-- Source: Phase_3_Conditional_Probability_Independence/phase_3_1_conditional_probability.md -->
# Phase 3.1: Conditional Probability

Conditional probability is a fundamental concept in statistics that measures the likelihood of an event occurring, given that another event has already taken place. This "given" information effectively restricts the sample space to a specific subset.

## 1. Theoretical Foundation

### Definition
The conditional probability of an event $A$ given that event $B$ has occurred is the probability that $A$ happens within the restricted sample space defined by $B$.

### The Fundamental Formula
If $P(B) > 0$, the conditional probability of $A$ given $B$ is defined as:

$$P(A|B) = \frac{P(A \cap B)}{P(B)}$$

Where:
*   $P(A|B)$: Probability of $A$ occurring given $B$ has occurred.
*   $P(A \cap B)$: Probability that both $A$ and $B$ occur (Intersection).
*   $P(B)$: Probability of the conditioning event $B$.

### Intuitive Understanding: Reducing the Sample Space
Imagine a sample space $S$. When we say "given $B$", we are throwing away any part of $S$ that is not $B$. The new sample space becomes $B$. We then look for the portion of $A$ that survived this "filtering" process, which is exactly $A \cap B$.

### The Multiplication Rule
By rearranging the formula, we get the Multiplication Rule, which is used to find the probability of an intersection:

$$P(A \cap B) = P(B) \cdot P(A|B)$$
$$P(A \cap B) = P(A) \cdot P(B|A)$$

---

## 2. Solved Examples

### Example 1: Drawing Balls from an Urn
An urn contains 6 Red balls and 4 Blue balls. Two balls are drawn sequentially without replacement. What is the probability that the second ball is Red, given that the first ball was Blue?

**Step 1: Define the events.**
*   $B_1$: First ball is Blue.
*   $R_2$: Second ball is Red.

**Step 2: Analyze the initial state.**
Total balls = 10 (6R, 4B).
$P(B_1) = \frac{4}{10}$.

**Step 3: Work-in-Progress (WIP) State.**
If the first ball drawn is Blue ($B_1$ occurs), we must update the contents of the urn:
*   Total balls remaining: $10 - 1 = 9$
*   Red balls remaining: ?
*   Blue balls remaining: $4 - 1 = 3$

**Step 4: Final Calculation.**
Since we drew a Blue ball, the number of Red balls remains 6.
$$P(R_2|B_1) = \frac{\text{Red balls remaining}}{\text{Total balls remaining}} = \frac{6}{9} = \frac{2}{3}$$
$P(R_2|B_1) \approx 0.6667$.

---

### Example 2: Two-Way Frequency Table
A survey of 100 students asked about their preferred study environment.

| Gender | Library | Coffee Shop | Total |
| :--- | :---: | :---: | :---: |
| Male | 30 | 20 | 50 |
| Female | 25 | 25 | 50 |
| **Total** | **55** | **45** | **100** |

Find the probability that a student prefers the Library, given they are Female.

**Step 1: Define events.**
*   $L$: Prefers Library.
*   $F$: Is Female.

**Step 2: Identify values from the table.**
*   $n(F) = 50$
*   $n(L \cap F) = 25$

**Step 3: WIP State.**
We are calculating $P(L|F)$.
$$P(L|F) = \frac{n(L \cap F)}{n(F)} = \frac{25}{?}$$

**Step 4: Final Calculation.**
$$P(L|F) = \frac{25}{50} = 0.5$$

---

### Example 3: Rolling Two Dice
Two fair dice are rolled. What is the probability that the sum is 8, given that the first die shows a 5?

**Step 1: Define events.**
*   $S_8$: Sum is 8.
*   $D_5$: First die is 5.

**Step 2: Identify the reduced sample space (Event $D_5$).**
If the first die is 5, the possible outcomes are:
$(5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6)$.
Total outcomes in $D_5 = 6$.

**Step 3: WIP State.**
Which of these outcomes result in a sum of 8?
*   $5 + ? = 8 \implies ? = 3$
Outcome: $(5, 3)$.

**Step 4: Final Calculation.**
There is only 1 favorable outcome in the reduced sample space of 6.
$$P(S_8|D_5) = \frac{1}{6} \approx 0.1667$$

---

### Example 4: Card Drawing
A card is drawn from a standard deck of 52 cards. What is the probability it is an Ace, given that it is a Spade?

**Step 1: Define events.**
*   $A$: Card is an Ace.
*   $S$: Card is a Spade.

**Step 2: Identify counts.**
*   $n(S) = 13$ (Spades in a deck)
*   $n(A \cap S) = 1$ (The Ace of Spades)

**Step 3: WIP State.**
$$P(A|S) = \frac{P(A \cap S)}{P(S)} = \frac{1/52}{?/52}$$

**Step 4: Final Calculation.**
$$P(A|S) = \frac{1}{13} \approx 0.0769$$

---

### Example 5: Family with Two Children
A family has two children. Given that at least one is a girl, what is the probability that both are girls? (Assume $P(G) = P(B) = 0.5$).

**Step 1: Define the sample space $S$.**
$S = \{BB, BG, GB, GG\}$ where $B$ is Boy and $G$ is Girl.

**Step 2: Define the conditioning event $E$.**
$E$: At least one girl.
$E = \{BG, GB, GG\}$.
$n(E) = 3$.

**Step 3: WIP State.**
We want the probability of $GG$ given $E$.
The favorable outcome is $\{GG\}$.
$n(GG \cap E) = 1$.

**Step 4: Final Calculation.**
$$P(GG|E) = \frac{1}{3} \approx 0.3333$$

---

### Example 6: Weather and Traffic
The probability that it rains is 0.3. The probability of heavy traffic is 0.4. The probability that it rains and there is heavy traffic is 0.2. What is the probability of heavy traffic given that it is raining?

**Step 1: Define events.**
*   $R$: It rains. $P(R) = 0.3$.
*   $T$: Heavy traffic. $P(T) = 0.4$.
*   $P(R \cap T) = 0.2$.

**Step 2: Apply the formula.**
$$P(T|R) = \frac{P(T \cap R)}{P(R)}$$

**Step 3: WIP State.**
$$P(T|R) = \frac{0.2}{?}$$

**Step 4: Final Calculation.**
$$P(T|R) = \frac{0.2}{0.3} = \frac{2}{3} \approx 0.6667$$

---

### Example 7: Students Passing Exams
In a class, 70% of students passed Math, and 60% passed Physics. 50% passed both. If a student is chosen at random and we know they passed Math, what is the probability they also passed Physics?

**Step 1: Define events.**
*   $M$: Passed Math. $P(M) = 0.70$.
*   $Ph$: Passed Physics. $P(Ph) = 0.60$.
*   $P(M \cap Ph) = 0.50$.

**Step 2: Apply formula.**
$$P(Ph|M) = \frac{P(Ph \cap M)}{P(M)}$$

**Step 3: WIP State.**
$$P(Ph|M) = \frac{0.50}{0.70} = ?$$

**Step 4: Final Calculation.**
$$P(Ph|M) = \frac{5}{7} \approx 0.7143$$

---

### Example 8: Assembly Line Defects
A factory has two assembly lines, A and B. Line A produces 60% of the products and Line B produces 40%. Line A has a 5% defect rate. A product is chosen from Line A. What is the probability it is defective?

**Step 1: Identify the given information.**
*   $P(A) = 0.60$
*   $P(B) = 0.40$
*   $P(D|A) = 0.05$ (This is already a conditional probability!)

**Step 2: Rephrase the question.**
The question asks for the probability that a product is defective *given* it came from Line A.

**Step 3: WIP State.**
The value is directly provided in the problem description as the "defect rate of Line A".

**Step 4: Final Calculation.**
$$P(D|A) = 0.05$$

*Note: This example illustrates that in many word problems, the conditional probability is the "starting point" or "rate" provided for a specific subgroup.*


---

<!-- Source: Phase_3_Conditional_Probability_Independence/phase_3_2_independence.md -->
# Phase 3.2: Independence

Independence is a statistical property where the occurrence of one event does not affect the probability of another event occurring. Understanding independence is crucial for simplifying complex probability calculations.

## 1. Theoretical Foundation

### Definition
Two events $A$ and $B$ are **independent** if the knowledge that $B$ has occurred does not change the probability of $A$ occurring.

### Mathematical Condition
The most common way to test for independence is the **Product Rule**:
Two events $A$ and $B$ are independent if and only if:
$$P(A \cap B) = P(A) \cdot P(B)$$

Alternatively, using conditional probability, $A$ and $B$ are independent if:
1. $P(A|B) = P(A)$
2. $P(B|A) = P(B)$

### Independence vs. Mutually Exclusive
It is a common mistake to confuse these two concepts:
*   **Mutually Exclusive (Disjoint):** Events *cannot* happen at the same time ($P(A \cap B) = 0$). If $A$ happens, $B$ definitely cannot happen.
*   **Independent:** Events *can* happen at the same time, but they don't influence each other.

> **Shortcut:** If $A$ and $B$ have non-zero probabilities and are mutually exclusive, they **cannot** be independent.

---

## 2. Solved Examples

### Example 1: Flipping Two Coins
If you flip a fair coin twice, what is the probability of getting two Heads?

**Step 1: Define events.**
*   $H_1$: Head on the first flip. $P(H_1) = 0.5$.
*   $H_2$: Head on the second flip. $P(H_2) = 0.5$.

**Step 2: Determine if they are independent.**
The outcome of the first flip does not affect the second. They are independent.

**Step 3: WIP State.**
Apply the product rule:
$$P(H_1 \cap H_2) = P(H_1) \cdot P(H_2) = 0.5 \cdot ?$$

**Step 4: Final Calculation.**
$$P(H_1 \cap H_2) = 0.5 \cdot 0.5 = 0.25$$

---

### Example 2: Drawing Cards with Replacement
You draw a card from a 52-card deck, look at it, put it back, shuffle, and draw again. What is the probability that both cards are Hearts?

**Step 1: Define events.**
*   $H_1$: First card is Heart. $P(H_1) = 13/52 = 0.25$.
*   $H_2$: Second card is Heart. $P(H_2) = 13/52 = 0.25$.

**Step 2: Analyze independence.**
Because of "replacement", the state of the deck is the same for both draws. The events are independent.

**Step 3: WIP State.**
$$P(H_1 \cap H_2) = 0.25 \cdot ?$$

**Step 4: Final Calculation.**
$$P(H_1 \cap H_2) = 0.0625$$

---

### Example 3: Shooting at a Target
Two archers, Alice and Bob, shoot at a target. Alice hits the target with probability 0.7, and Bob hits it with probability 0.4. If they both shoot, what is the probability they both hit?

**Step 1: Define events.**
*   $A$: Alice hits. $P(A) = 0.7$.
*   $B$: Bob hits. $P(B) = 0.4$.

**Step 2: Assume independence.**
Usually, in such problems, the performance of one person is independent of the other.

**Step 3: WIP State.**
$$P(A \cap B) = P(A) \cdot P(B) = 0.7 \cdot 0.4 = ?$$

**Step 4: Final Calculation.**
$$P(A \cap B) = 0.28$$

---

### Example 4: Testing for Independence (Dice)
A fair six-sided die is rolled. Let $A = \{1, 2, 3\}$ and $B = \{2, 4, 6\}$. Are $A$ and $B$ independent?

**Step 1: Calculate individual probabilities.**
*   $P(A) = 3/6 = 0.5$
*   $P(B) = 3/6 = 0.5$

**Step 2: Identify the intersection.**
$A \cap B = \{2\}$.
$P(A \cap B) = 1/6 \approx 0.1667$.

**Step 3: WIP State.**
Check the product: $P(A) \cdot P(B) = 0.5 \cdot 0.5 = 0.25$.
Does $P(A \cap B) = P(A) \cdot P(B)$?
$? = ?$

**Step 4: Final Calculation.**
$0.1667 \neq 0.25$.
Therefore, events $A$ and $B$ are **not independent** (they are dependent).

---

### Example 5: Weather in Two Cities
The probability of rain in London is 0.4. The probability of rain in Tokyo is 0.3. Assuming these are independent, what is the probability it rains in at least one city?

**Step 1: Define events.**
*   $L$: Rain in London. $P(L) = 0.4$.
*   $T$: Rain in Tokyo. $P(T) = 0.3$.

**Step 2: Identify the method.**
"At least one" is best solved using the complement: $1 - P(\text{None})$.
$P(L^c) = 0.6$, $P(T^c) = 0.7$.

**Step 3: WIP State.**
$P(\text{Neither rains}) = P(L^c \cap T^c) = 0.6 \cdot ?$

**Step 4: Final Calculation.**
$P(L^c \cap T^c) = 0.6 \cdot 0.7 = 0.42$.
$P(\text{At least one}) = 1 - 0.42 = 0.58$.

---

### Example 6: Three Independent Events
Three different light bulbs have probabilities 0.1, 0.2, and 0.05 of failing in the first year. What is the probability all three fail?

**Step 1: Define events.**
$F_1, F_2, F_3$ with $P(F_1)=0.1, P(F_2)=0.2, P(F_3)=0.05$.

**Step 2: Extend the product rule.**
For independent events, $P(A \cap B \cap C) = P(A) \cdot P(B) \cdot P(C)$.

**Step 3: WIP State.**
$P(F_1 \cap F_2 \cap F_3) = 0.1 \cdot 0.2 \cdot ?$

**Step 4: Final Calculation.**
$P(F_1 \cap F_2 \cap F_3) = 0.001$.

---

### Example 7: System Reliability (Parallel)
A system consists of two independent components in parallel. The system works if at least one component works. $P(C_1 \text{ works}) = 0.95$ and $P(C_2 \text{ works}) = 0.90$. Find the probability the system works.

**Step 1: Find failure probabilities.**
$P(C_1^c) = 0.05$.
$P(C_2^c) = 0.10$.

**Step 2: Calculate probability both fail.**
$P(\text{Both fail}) = 0.05 \cdot 0.10 = 0.005$.

**Step 3: WIP State.**
$P(\text{System works}) = 1 - P(\text{Both fail}) = 1 - ?$

**Step 4: Final Calculation.**
$P(\text{System works}) = 0.995$.

---

### Example 8: Probability of Exactly One
Given two independent events $A$ and $B$ with $P(A)=0.6$ and $P(B)=0.4$. What is the probability that **exactly one** of them occurs?

**Step 1: Identify the two scenarios.**
1. $A$ occurs and $B$ does not: $P(A \cap B^c)$.
2. $B$ occurs and $A$ does not: $P(B \cap A^c)$.

**Step 2: Calculate each using independence.**
$P(A \cap B^c) = 0.6 \cdot (1 - 0.4) = 0.6 \cdot 0.6 = 0.36$.
$P(B \cap A^c) = 0.4 \cdot (1 - 0.6) = 0.4 \cdot 0.4 = 0.16$.

**Step 3: WIP State.**
Add the two probabilities (since they are mutually exclusive):
$P(\text{Exactly one}) = 0.36 + ?$

**Step 4: Final Calculation.**
$P(\text{Exactly one}) = 0.52$.


---

<!-- Source: Phase_3_Conditional_Probability_Independence/phase_3_3_total_probability_bayes_theorem.md -->
# Phase 3.3: Law of Total Probability & Bayes' Theorem

These two theorems are the most powerful tools in probability for handling multi-stage processes and updating beliefs based on new evidence.

## 1. Theoretical Foundation

### Law of Total Probability
If we have a set of events $B_1, B_2, \dots, B_n$ that **partition** the sample space (meaning they are mutually exclusive and their union is the whole space), then for any event $A$:

$$P(A) = P(A|B_1)P(B_1) + P(A|B_2)P(B_2) + \dots + P(A|B_n)P(B_n)$$

**Intuition:** To find the total probability of $A$, you sum up the probability of $A$ occurring under each possible "branch" of the sample space.

### Bayes' Theorem
Bayes' Theorem allows us to "reverse" conditional probabilities. If we know $P(A|B)$, we can find $P(B|A)$.

$$P(B_i|A) = \frac{P(A|B_i)P(B_i)}{P(A)}$$

By substituting the Law of Total Probability for the denominator $P(A)$, we get the expanded form:

$$P(B_i|A) = \frac{P(A|B_i)P(B_i)}{\sum_{j=1}^{n} P(A|B_j)P(B_j)}$$

---

## 2. Solved Examples

### Example 1: Factory Production (Total Probability)
A factory uses three machines. $M_1$ produces 50%, $M_2$ produces 30%, and $M_3$ produces 20% of the total output. The defect rates are 1%, 2%, and 5% respectively. What is the probability a random product is defective?

**Step 1: Define events.**
*   $M_i$: Product from machine $i$.
*   $D$: Product is defective.

**Step 2: List given probabilities.**
*   $P(M_1)=0.5, P(D|M_1)=0.01$
*   $P(M_2)=0.3, P(D|M_2)=0.02$
*   $P(M_3)=0.2, P(D|M_3)=0.05$

**Step 3: WIP State.**
Apply Law of Total Probability:
$P(D) = (0.5 \cdot 0.01) + (0.3 \cdot 0.02) + (0.2 \cdot ?)$

**Step 4: Final Calculation.**
$P(D) = 0.005 + 0.006 + 0.010 = 0.021$.
The probability is **2.1%**.

---

### Example 2: Medical Diagnostic Test (Bayes)
A disease affects 1% of the population. A test is 95% accurate for those with the disease (sensitivity) and 90% accurate for those without (specificity). If a person tests positive, what is the probability they have the disease?

**Step 1: Define events.**
*   $H$: Has disease. $P(H) = 0.01$.
*   $H^c$: Healthy. $P(H^c) = 0.99$.
*   $Pos$: Tests positive.

**Step 2: List conditionals.**
*   $P(Pos|H) = 0.95$
*   $P(Pos|H^c) = 1 - 0.90 = 0.10$ (False Positive)

**Step 3: WIP State.**
Calculate total probability of testing positive $P(Pos)$:
$P(Pos) = (0.95 \cdot 0.01) + (0.10 \cdot 0.99) = 0.0095 + ?$

**Step 4: Final Calculation.**
$P(Pos) = 0.1085$.
$P(H|Pos) = \frac{P(Pos|H)P(H)}{P(Pos)} = \frac{0.0095}{0.1085} \approx 0.0876$.
The probability is only **8.76%**.

---

### Example 3: Two Urns (Multi-stage)
Urn A has 2 Red and 3 Blue balls. Urn B has 4 Red and 1 Blue ball. A fair coin is flipped; if Heads, a ball is drawn from Urn A. If Tails, from Urn B. What is the probability a Red ball is drawn?

**Step 1: Define events.**
*   $H$: Heads (Urn A). $P(H) = 0.5$.
*   $T$: Tails (Urn B). $P(T) = 0.5$.
*   $R$: Red ball.

**Step 2: Find conditionals.**
*   $P(R|H) = 2/5 = 0.4$
*   $P(R|T) = 4/5 = 0.8$

**Step 3: WIP State.**
$P(R) = P(R|H)P(H) + P(R|T)P(T) = (0.4 \cdot 0.5) + ?$

**Step 4: Final Calculation.**
$P(R) = 0.2 + 0.4 = 0.6$.

---

### Example 4: Identifying the Urn (Bayes)
Using the setup from Example 3: If a Red ball was drawn, what is the probability it came from Urn B?

**Step 1: Use previous results.**
*   $P(R) = 0.6$
*   $P(R|T)P(T) = 0.4$

**Step 2: Apply Bayes' Theorem.**
$P(T|R) = \frac{P(R|T)P(T)}{P(R)}$

**Step 3: WIP State.**
$P(T|R) = \frac{0.4}{?}$

**Step 4: Final Calculation.**
$P(T|R) = \frac{0.4}{0.6} = \frac{2}{3} \approx 0.6667$.

---

### Example 5: Spam Filter
A spam filter finds that 90% of spam emails contain the word "Offer", while only 5% of non-spam emails contain it. 20% of all emails are spam. If an email contains "Offer", what is the probability it is spam?

**Step 1: Define events.**
*   $S$: Spam. $P(S) = 0.2$.
*   $O$: Contains "Offer".
*   $P(O|S) = 0.9, P(O|S^c) = 0.05$.

**Step 2: Total probability of "Offer".**
$P(O) = (0.9 \cdot 0.2) + (0.05 \cdot 0.8) = 0.18 + 0.04 = 0.22$.

**Step 3: WIP State.**
$P(S|O) = \frac{0.18}{?}$

**Step 4: Final Calculation.**
$P(S|O) = \frac{0.18}{0.22} \approx 0.8182$.

---

### Example 6: Witness Reliability
A taxi was involved in a hit-and-run accident at night. Two companies, Green and Blue, operate in the city. 85% of taxis are Green and 15% are Blue. A witness identifies the taxi as Blue. The court tests the witness and finds they correctly identify the color 80% of the time. What is the probability the taxi was actually Blue?

**Step 1: Define events.**
*   $B$: Taxi was Blue. $P(B) = 0.15$.
*   $G$: Taxi was Green. $P(G) = 0.85$.
*   $W_B$: Witness says "Blue".

**Step 2: Conditionals.**
*   $P(W_B|B) = 0.80$ (Correct)
*   $P(W_B|G) = 0.20$ (Incorrect - says Blue when it's Green)

**Step 3: WIP State.**
Total probability witness says Blue:
$P(W_B) = (0.80 \cdot 0.15) + (0.20 \cdot 0.85) = 0.12 + ?$

**Step 4: Final Calculation.**
$P(W_B) = 0.12 + 0.17 = 0.29$.
$P(B|W_B) = \frac{0.12}{0.29} \approx 0.4138$.
Despite the witness, it's more likely the taxi was Green (58.62%)!

---

### Example 7: Flight Delays
The probability that it is a holiday is 0.1. During holidays, the probability of a flight delay is 0.6. On non-holidays, the probability of delay is 0.2. What is the probability a flight is delayed?

**Step 1: Define events.**
*   $H$: Holiday. $P(H) = 0.1$.
*   $D$: Delayed.
*   $P(D|H) = 0.6, P(D|H^c) = 0.2$.

**Step 2: WIP State.**
$P(D) = (0.6 \cdot 0.1) + (0.2 \cdot ?)$

**Step 3: Final Calculation.**
$P(D) = 0.06 + 0.18 = 0.24$.

---

### Example 8: Supplier Quality
A company buys chips from two suppliers, X (70%) and Y (30%). 2% of X's chips are defective, and 1% of Y's are defective. A chip is found to be defective. What is the probability it came from supplier X?

**Step 1: Total Defect Probability.**
$P(D) = (0.02 \cdot 0.7) + (0.01 \cdot 0.3) = 0.014 + 0.003 = 0.017$.

**Step 2: Apply Bayes.**
$P(X|D) = \frac{P(D|X)P(X)}{P(D)}$

**Step 3: WIP State.**
$P(X|D) = \frac{0.014}{?}$

**Step 4: Final Calculation.**
$P(X|D) = \frac{0.014}{0.017} \approx 0.8235$.
There is an 82.35% chance it came from Supplier X.


---

<!-- Source: Phase_4_Discrete_Random_Variables/phase_4_1_discrete_rv_fundamentals.md -->
# Phase 4.1: Discrete Random Variables — Fundamentals

A **Random Variable** maps each outcome of a random experiment to a number. A **Discrete Random Variable** takes on a finite or countably infinite set of values. The three pillars of this topic — the PMF, the Expected Value, and the Variance — completely characterise the distribution's shape, centre, and spread.

---

## 1. Probability Mass Function (PMF)

The **PMF** of a discrete random variable $X$ is a function $p(x)$ that assigns a probability to each possible value $x$:

$$p(x) = P(X = x)$$

### Validity Conditions

Any function claiming to be a PMF must satisfy two conditions simultaneously:

**Condition 1 (Non-negativity):**

$$p(x) \geq 0 \quad \text{for all } x$$

**Condition 2 (Normalisation):**

$$\sum_{\text{all } x} p(x) = 1$$

If either condition fails, the function is not a valid PMF. These conditions are directly analogous to Kolmogorov's Axioms from Phase 2.

### Standard PMF Table Format

A PMF is most clearly presented as a table:

| $x$ | $x_1$ | $x_2$ | $\cdots$ | $x_k$ |
| :--- | :--- | :--- | :--- | :--- |
| $P(X=x)$ | $p_1$ | $p_2$ | $\cdots$ | $p_k$ |

The bottom row must sum to 1.

---

## 2. Expected Value $E[X]$

The **Expected Value** (also called the **mean** or **expectation**) is the probability-weighted average of all values $X$ can take. It represents the long-run average outcome over many repetitions of the experiment.

$$\boxed{E[X] = \mu = \sum_{\text{all } x} x \cdot p(x)}$$

### Key Properties of Expectation

These properties hold without any condition on the distribution:

| Property | Formula |
| :--- | :--- |
| Linearity | $E[aX + b] = a \cdot E[X] + b$ |
| Constant | $E[c] = c$ |
| Sum of variables | $E[X + Y] = E[X] + E[Y]$ |

---

## 3. Variance $V(X)$

The **Variance** measures the average squared deviation of $X$ from its mean. A higher variance means the distribution is more spread out.

**Definition formula:**

$$V(X) = E\left[(X - \mu)^2\right] = \sum_{\text{all } x} (x - \mu)^2 \cdot p(x)$$

**Computational shortcut formula** (always use this in practice — it avoids working with $\mu$ repeatedly):

$$\boxed{V(X) = E[X^2] - (E[X])^2}$$

where $E[X^2] = \sum_{\text{all } x} x^2 \cdot p(x)$.

**Standard Deviation:**

$$\sigma = SD(X) = \sqrt{V(X)}$$

### Key Properties of Variance

| Property | Formula | Note |
| :--- | :--- | :--- |
| Scaling | $V(aX) = a^2 \cdot V(X)$ | The square of $a$ appears |
| Shift | $V(X + b) = V(X)$ | Constants do not affect spread |
| Combined | $V(aX + b) = a^2 \cdot V(X)$ | $b$ disappears entirely |

> **Critical rule:** $V(aX + b) = a^2 \cdot V(X)$. The constant $b$ has **zero effect** on variance. This is the most common source of errors on exams.

---

## 4. Solved Exercises

### Exercise 1: Verifying a PMF

**Problem:** Determine whether the following is a valid PMF for $X \in \{1, 2, 3, 4\}$:

| $x$ | 1 | 2 | 3 | 4 |
| :--- | :--- | :--- | :--- | :--- |
| $P(X=x)$ | 0.1 | 0.3 | 0.4 | 0.2 |

**Solution:**

**Check 1 (Non-negativity):** All values are $\geq 0$. Passed.

**Check 2 (Normalisation):** $0.1 + 0.3 + 0.4 + 0.2 = 1.0$. Passed.

This is a valid PMF.

---

### Exercise 2: Finding a Missing Probability

**Problem:** The PMF of $X$ is given below. Find the value of $c$.

| $x$ | 0 | 1 | 2 | 3 |
| :--- | :--- | :--- | :--- | :--- |
| $P(X=x)$ | $c$ | $2c$ | $3c$ | $4c$ |

**Solution:**

Apply the normalisation condition:

$$c + 2c + 3c + 4c = 1$$

$$10c = 1 \implies c = 0.1$$

The completed PMF:

| $x$ | 0 | 1 | 2 | 3 |
| :--- | :--- | :--- | :--- | :--- |
| $P(X=x)$ | 0.1 | 0.2 | 0.3 | 0.4 |

---

### Exercise 3: Computing $E[X]$

**Problem:** Using the PMF from Exercise 2, compute $E[X]$.

**Solution:**

$$E[X] = \sum x \cdot p(x) = 0(0.1) + 1(0.2) + 2(0.3) + 3(0.4)$$

$$E[X] = 0 + 0.2 + 0.6 + 1.2 = 2.0$$

---

### Exercise 4: Computing $V(X)$ using the Shortcut

**Problem:** Using the PMF from Exercise 2 and $E[X] = 2.0$, compute $V(X)$ and $SD(X)$.

**Solution:**

**Step 1:** Compute $E[X^2]$:

$$E[X^2] = 0^2(0.1) + 1^2(0.2) + 2^2(0.3) + 3^2(0.4)$$

$$E[X^2] = 0 + 0.2 + 1.2 + 3.6 = 5.0$$

**Step 2:** Apply the shortcut formula:

$$V(X) = E[X^2] - (E[X])^2 = 5.0 - (2.0)^2 = 5.0 - 4.0 = 1.0$$

$$SD(X) = \sqrt{1.0} = 1.0$$

---

### Exercise 5: Applying Linearity of Expectation

**Problem:** A random variable $X$ has $E[X] = 3$ and $V(X) = 4$. Find $E[2X + 5]$ and $V(2X + 5)$.

**Solution:**

$$E[2X + 5] = 2 \cdot E[X] + 5 = 2(3) + 5 = 11$$

$$V(2X + 5) = 2^2 \cdot V(X) = 4 \cdot 4 = 16$$

Note that the constant $+5$ contributes nothing to the variance.

---

### Exercise 6: Computing a Probability from the PMF

**Problem:** Using the PMF from Exercise 2, find $P(X \geq 2)$ and $P(1 \leq X \leq 3)$.

**Solution:**

$$P(X \geq 2) = P(X=2) + P(X=3) = 0.3 + 0.4 = 0.7$$

$$P(1 \leq X \leq 3) = P(X=1) + P(X=2) + P(X=3) = 0.2 + 0.3 + 0.4 = 0.9$$

---

### Exercise 7: Building a PMF from a Word Problem

**Problem:** A fair die is rolled. Let $X$ = the number of dots showing. Build the PMF table and compute $E[X]$ and $V(X)$.

**Solution:**

Each face has probability $\frac{1}{6}$.

| $x$ | 1 | 2 | 3 | 4 | 5 | 6 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $P(X=x)$ | $\frac{1}{6}$ | $\frac{1}{6}$ | $\frac{1}{6}$ | $\frac{1}{6}$ | $\frac{1}{6}$ | $\frac{1}{6}$ |

$$E[X] = \frac{1+2+3+4+5+6}{6} = \frac{21}{6} = 3.5$$

$$E[X^2] = \frac{1+4+9+16+25+36}{6} = \frac{91}{6} \approx 15.167$$

$$V(X) = E[X^2] - (E[X])^2 = \frac{91}{6} - (3.5)^2 = \frac{91}{6} - \frac{49}{4} = \frac{182}{12} - \frac{147}{12} = \frac{35}{12} \approx 2.917$$

---

### Exercise 8: The Gotcha — Variance of a Difference

**Problem:** Two independent random variables $X$ and $Y$ have $E[X] = 4$, $V(X) = 3$, $E[Y] = 2$, $V(Y) = 5$. A student computes $V(X - Y)$ and writes:

$$V(X - Y) = V(X) - V(Y) = 3 - 5 = -2$$

Find the error and compute the correct answer.

**Solution:**

**The error:** The student subtracted the variances. Variance **cannot be subtracted** — it is always additive for independent variables, regardless of whether the operation on $X$ and $Y$ is addition or subtraction.

The correct rule for independent $X$ and $Y$:

$$V(X - Y) = V(X) + (-1)^2 \cdot V(Y) = V(X) + V(Y)$$

This follows from the scaling property $V(aY) = a^2 V(Y)$ with $a = -1$:

$$V(X - Y) = V(X) + V(-Y) = V(X) + (-1)^2 V(Y) = 3 + 5 = 8$$

**The general rule:**

$$V(aX + bY) = a^2 V(X) + b^2 V(Y) \quad \text{(for independent } X, Y\text{)}$$

A negative sign on a variable **always becomes a positive** in the variance calculation because it is squared.

---

## Exam Tip: The Shortcut Formula is Non-Negotiable

Always use $V(X) = E[X^2] - (E[X])^2$ rather than the definition formula $\sum (x-\mu)^2 p(x)$. The definition requires computing $\mu$, then subtracting it from each value, squaring, and multiplying — every step is a potential arithmetic error. The shortcut reduces this to two sums that can be computed in a single pass through the table.


---

<!-- Source: Phase_4_Discrete_Random_Variables/phase_4_2_binomial_distribution.md -->
# Phase 4.2: Binomial Distribution

The Binomial Distribution models the number of **successes** in a fixed sequence of independent trials where each trial has exactly two possible outcomes (success or failure) and the probability of success is constant. It is the most frequently examined discrete distribution at the university level.

---

## 1. The Four Conditions (FINS)

A random variable $X$ follows a Binomial Distribution **only if all four conditions hold**:

1. **F**ixed number of trials: $n$ is known and constant.
2. **I**ndependence: each trial's outcome does not affect any other.
3. **N**o more than two outcomes: each trial is either "success" or "failure".
4. **S**ame probability: $p$ (probability of success) is constant across all trials.

If any single condition fails, the Binomial model is invalid and a different distribution must be used.

---

## 2. The PMF Formula

If $X \sim B(n, p)$, then the probability of exactly $k$ successes in $n$ trials is:

$$\boxed{P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}, \quad k = 0, 1, 2, \ldots, n}$$

Where:
- $n$ = total number of trials
- $k$ = number of successes (the value you are computing for)
- $p$ = probability of success on a single trial
- $1-p = q$ = probability of failure on a single trial
- $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ = the binomial coefficient (number of ways to choose $k$ from $n$)

---

## 3. Mean and Variance

For $X \sim B(n, p)$, the mean and variance have elegant closed-form expressions derived from the general definitions:

$$\boxed{E[X] = n \cdot p}$$

$$\boxed{V(X) = n \cdot p \cdot (1-p)}$$

$$SD(X) = \sqrt{n \cdot p \cdot (1-p)}$$

These formulas must be memorised. Deriving them from the PMF during an exam wastes significant time.

---

## 4. Cumulative Probability

For "at most $k$" or "at least $k$" questions, sum the individual PMF values:

$$P(X \leq k) = \sum_{i=0}^{k} \binom{n}{i} p^i (1-p)^{n-i}$$

$$P(X \geq k) = 1 - P(X \leq k-1)$$

The complement rule $P(X \geq k) = 1 - P(X \leq k-1)$ is almost always faster than summing many terms directly.

---

## 5. Solved Exercises

### Exercise 1: Identifying Parameters

**Problem:** A fair coin is tossed 8 times. Let $X$ be the number of Heads. Identify the distribution, state all parameters, and verify the four conditions.

**Solution:**

- **Fixed $n$:** 8 tosses — fixed. Passed.
- **Independence:** Each toss is independent. Passed.
- **Two outcomes:** Head (success) or Tail (failure). Passed.
- **Constant $p$:** $p = 0.5$ for every toss. Passed.

$$X \sim B(8, 0.5)$$

$$E[X] = 8 \times 0.5 = 4, \quad V(X) = 8 \times 0.5 \times 0.5 = 2$$

---

### Exercise 2: Computing a Single PMF Value

**Problem:** A factory produces items where 20% are defective. A quality inspector picks 5 items at random. Find the probability that exactly 2 are defective.

**Solution:**

$$X \sim B(5, 0.2), \quad P(X = 2) = \binom{5}{2}(0.2)^2(0.8)^3$$

$$\binom{5}{2} = \frac{5!}{2! \cdot 3!} = 10$$

$$P(X=2) = 10 \times 0.04 \times 0.512 = 10 \times 0.02048 = 0.2048$$

---

### Exercise 3: Computing $P(X = 0)$ — The "None" Case

**Problem:** Using the same factory setting ($n=5$, $p=0.2$), find the probability that no items are defective.

**Solution:**

$$P(X=0) = \binom{5}{0}(0.2)^0(0.8)^5 = 1 \times 1 \times 0.32768 = 0.3277$$

> **Note:** $(0.2)^0 = 1$ and $\binom{5}{0} = 1$. Students often hesitate here — both are always exactly 1.

---

### Exercise 4: Computing $P(X = n)$ — The "All" Case

**Problem:** Find the probability that all 5 items are defective ($n=5$, $p=0.2$).

**Solution:**

$$P(X=5) = \binom{5}{5}(0.2)^5(0.8)^0 = 1 \times 0.00032 \times 1 = 0.00032$$

This confirms that all 5 being defective at a 20% rate is extremely unlikely.

---

### Exercise 5: "At Least One" Using the Complement

**Problem:** From the factory example ($n=5$, $p=0.2$), find the probability of **at least one** defective item.

**Solution:**

Direct computation would require summing $P(X=1)$ through $P(X=5)$. The complement is far faster:

$$P(X \geq 1) = 1 - P(X = 0) = 1 - 0.3277 = 0.6723$$

> **Exam shortcut:** "At least one" always equals $1 - P(X=0)$. Compute $P(X=0)$ and subtract from 1. Never sum the remaining terms.

---

### Exercise 6: "At Most" Cumulative Probability

**Problem:** For $X \sim B(6, 0.3)$, find $P(X \leq 2)$.

**Solution:**

$$P(X=0) = \binom{6}{0}(0.3)^0(0.7)^6 = 0.117649$$

$$P(X=1) = \binom{6}{1}(0.3)^1(0.7)^5 = 6 \times 0.3 \times 0.16807 = 0.302526$$

$$P(X=2) = \binom{6}{2}(0.3)^2(0.7)^4 = 15 \times 0.09 \times 0.2401 = 0.324135$$

$$P(X \leq 2) = 0.117649 + 0.302526 + 0.324135 = 0.7443$$

---

### Exercise 7: Working Backwards — Finding $n$

**Problem:** A multiple-choice test has 4 options per question, only one of which is correct. A student guesses randomly. If $E[X] = 5$, how many questions are on the test?

**Solution:**

$$p = \frac{1}{4} = 0.25, \quad E[X] = n \cdot p = 5$$

$$n = \frac{5}{0.25} = 20 \text{ questions}$$

$$V(X) = 20 \times 0.25 \times 0.75 = 3.75$$

---

### Exercise 8: Full Distribution Table Construction

**Problem:** For $X \sim B(4, 0.5)$, construct the full PMF table and verify that it sums to 1.

**Solution:**

| $k$ | $\binom{4}{k}$ | $(0.5)^k$ | $(0.5)^{4-k}$ | $P(X=k)$ |
| :--- | :--- | :--- | :--- | :--- |
| 0 | 1 | 1 | 0.0625 | 0.0625 |
| 1 | 4 | 0.5 | 0.125 | 0.2500 |
| 2 | 6 | 0.25 | 0.25 | 0.3750 |
| 3 | 4 | 0.125 | 0.5 | 0.2500 |
| 4 | 1 | 0.0625 | 1 | 0.0625 |

**Sum:** $0.0625 + 0.2500 + 0.3750 + 0.2500 + 0.0625 = 1.0000$. Verified.

---

### Exercise 9: The Gotcha — "At Least" Requires Careful Indexing

**Problem:** A call centre receives calls independently. The probability that any given call results in a sale is 0.3. In a batch of 10 calls, find the probability that **more than 8 calls** result in a sale.

A student sets up the calculation as:

$$P(X \geq 8) = 1 - P(X \leq 8)$$

Identify the error and compute the correct answer.

**Solution:**

**The error:** The phrase "more than 8" translates to $X > 8$, which is equivalent to $X \geq 9$.

The student wrote $P(X \geq 8) = 1 - P(X \leq 8)$. There are **two simultaneous errors** here:
- **Label error:** The event should be labelled $P(X \geq 9)$, not $P(X \geq 8)$.
- **Formula error for the label used:** If the student truly wanted $P(X \geq 8)$, the correct complement would be $1 - P(X \leq 7)$, not $1 - P(X \leq 8)$.

By coincidence, the formula $1 - P(X \leq 8)$ happens to give the numerically correct answer for the original question ($P(X > 8)$), but the reasoning is wrong because the student is conflating "more than 8" with "at least 8." The correct, unambiguous setup is:

$$P(X > 8) = P(X \geq 9) = 1 - P(X \leq 8)$$

**Correct computation** for $P(X > 8)$ with $X \sim B(10, 0.3)$:

$$P(X = 9) = \binom{10}{9}(0.3)^9(0.7)^1 = 10 \times 0.000019683 \times 0.7 = 0.0001378$$

$$P(X = 10) = \binom{10}{10}(0.3)^{10}(0.7)^0 = 1 \times 0.0000059049 \times 1 = 0.0000059$$

$$P(X > 8) = P(X=9) + P(X=10) \approx 0.0001378 + 0.0000059 = 0.0001437$$

This is an extremely small probability, which makes intuitive sense: achieving 9 or 10 sales when the success probability is only 0.3 is very unlikely over 10 calls.

**Key lesson:** Always translate the English phrase to a mathematical inequality **before** writing a complement expression:

| Phrase | Inequality | Complement Setup |
| :--- | :--- | :--- |
| "more than $k$" | $X > k$ | $1 - P(X \leq k)$ |
| "at least $k$" | $X \geq k$ | $1 - P(X \leq k-1)$ |
| "fewer than $k$" | $X < k$ | $P(X \leq k-1)$ |
| "at most $k$" | $X \leq k$ | Direct sum or table |

---

## Exam Tip: Recognising the Binomial Setup

The words "independent", "fixed number of trials", "probability of success", and "how many" in a problem are strong signals for the Binomial model. The moment you confirm all four FINS conditions, write $X \sim B(n, p)$ explicitly and use $E[X] = np$ and $V(X) = np(1-p)$ without re-deriving them.


---

<!-- Source: Phase_4_Discrete_Random_Variables/phase_4_3_poisson_distribution.md -->
# Phase 4.3: Poisson Distribution

The Poisson Distribution models the number of times a **rare event** occurs within a fixed interval of time, space, or volume, given a known average rate. It fills the gap in the discrete distribution toolkit: where the Binomial requires a fixed, finite $n$, the Poisson handles situations where the number of "trials" is very large (or effectively infinite) and the individual probability of each event is very small.

---

## 1. When to Use the Poisson Distribution

Apply the Poisson model when the problem describes:

- A **count** of events (not a proportion or ratio) over a continuous interval.
- A known **average rate** $\lambda$ (lambda) per unit interval.
- Events occur **independently** of each other.
- Events occur **one at a time** (two events cannot happen at the exact same instant).

**Common real-world contexts:**
- Number of phone calls arriving at a switchboard per hour.
- Number of defects per metre of fabric.
- Number of accidents at an intersection per month.
- Number of radioactive particle emissions per second.

---

## 2. The PMF Formula

If $X \sim Po(\lambda)$, the probability of exactly $k$ events is:

$$\boxed{P(X = k) = \frac{\lambda^k \cdot e^{-\lambda}}{k!}, \quad k = 0, 1, 2, 3, \ldots}$$

Where:
- $\lambda > 0$ is the average rate (mean number of events per interval)
- $e \approx 2.71828$ is Euler's number
- $k!$ is the factorial of $k$

The Poisson distribution has **no upper bound** on $k$ — theoretically, any non-negative integer is possible.

---

## 3. Mean and Variance

A defining and elegant property of the Poisson distribution is that **the mean and variance are equal**:

$$\boxed{E[X] = \lambda}$$

$$\boxed{V(X) = \lambda}$$

$$SD(X) = \sqrt{\lambda}$$

If a problem gives you only one value and calls it the "average rate" or "expected number of events", that single value is $\lambda$, and it serves as both the mean and the variance.

---

## 4. Scaling the Rate to a Different Interval

This is one of the most important practical skills for the Poisson distribution. If the rate is given for one interval length but the question asks about a different interval length, scale $\lambda$ proportionally.

**Rule:** If $\lambda$ is the rate per unit time and you want the rate over $t$ units of time:

$$\lambda_t = \lambda \cdot t$$

Then $X_t \sim Po(\lambda \cdot t)$.

**Example:** If calls arrive at 3 per hour ($\lambda = 3$), then over 2 hours the rate is $\lambda_{2h} = 3 \times 2 = 6$.

---

## 5. Poisson as an Approximation to Binomial

When $n$ is large and $p$ is small (rule of thumb: $n \geq 20$ and $p \leq 0.05$), the Binomial distribution $B(n,p)$ is well approximated by $Po(\lambda)$ where:

$$\lambda = n \cdot p$$

This approximation avoids computing large binomial coefficients.

---

## 6. Solved Exercises

### Exercise 1: Basic PMF Calculation

**Problem:** Customers arrive at a bank at an average rate of 4 per hour. Find the probability that exactly 3 customers arrive in a given hour.

**Solution:**

$$X \sim Po(4), \quad P(X=3) = \frac{4^3 \cdot e^{-4}}{3!}$$

$$= \frac{64 \times 0.018316}{6} = \frac{1.17222}{6} \approx 0.1954$$

---

### Exercise 2: Computing $P(X = 0)$

**Problem:** Using the same bank setting ($\lambda = 4$), find the probability that no customers arrive in a given hour.

**Solution:**

$$P(X=0) = \frac{4^0 \cdot e^{-4}}{0!} = \frac{1 \times 0.018316}{1} = 0.0183$$

There is approximately a 1.83% chance of a completely quiet hour.

> **Recall:** $4^0 = 1$ and $0! = 1$. So $P(X=0) = e^{-\lambda}$ always.

---

### Exercise 3: "At Least One" Using the Complement

**Problem:** A Geiger counter detects on average 2 radioactive particles per second. Find the probability of detecting at least one particle in a given second.

**Solution:**

$$X \sim Po(2), \quad P(X \geq 1) = 1 - P(X=0) = 1 - e^{-2}$$

$$P(X \geq 1) = 1 - 0.1353 = 0.8647$$

---

### Exercise 4: Scaling the Interval

**Problem:** A call centre receives calls at an average rate of 5 per hour. Find the probability of receiving exactly 2 calls in a 30-minute window.

**Solution:**

**Step 1:** Convert the rate to the interval of interest.

30 minutes = 0.5 hours, so:

$$\lambda_{30\min} = 5 \times 0.5 = 2.5$$

**Step 2:** Apply the Poisson PMF with $\lambda = 2.5$:

$$P(X=2) = \frac{2.5^2 \cdot e^{-2.5}}{2!} = \frac{6.25 \times 0.082085}{2} = \frac{0.513}{2} \approx 0.2565$$

---

### Exercise 5: Cumulative Probability — "Fewer Than"

**Problem:** For $X \sim Po(3)$, find $P(X < 3)$.

**Solution:**

"Fewer than 3" means $X \leq 2$:

$$P(X=0) = \frac{3^0 e^{-3}}{0!} = e^{-3} \approx 0.049787$$

$$P(X=1) = \frac{3^1 e^{-3}}{1!} = 3e^{-3} \approx 0.149361$$

$$P(X=2) = \frac{3^2 e^{-3}}{2!} = \frac{9e^{-3}}{2} \approx 0.224042$$

$$P(X < 3) = 0.049787 + 0.149361 + 0.224042 = 0.4232$$

---

### Exercise 6: Using Poisson to Approximate Binomial

**Problem:** A manufacturing process produces bolts where the probability of a defect is $p = 0.02$. A batch of 200 bolts is inspected. Approximate the probability of exactly 3 defective bolts using the Poisson distribution.

**Solution:**

**Check conditions:** $n = 200 \geq 20$ and $p = 0.02 \leq 0.05$. Approximation is valid.

$$\lambda = n \cdot p = 200 \times 0.02 = 4$$

$$P(X=3) \approx \frac{4^3 e^{-4}}{3!} = \frac{64 \times 0.018316}{6} \approx 0.1954$$

---

### Exercise 7: Finding $\lambda$ from Given Information

**Problem:** A Poisson random variable $X$ has $V(X) = 6.25$. Find $E[X]$, $P(X=0)$, and $P(X \geq 2)$.

**Solution:**

Since $V(X) = \lambda$ for a Poisson distribution:

$$\lambda = 6.25, \quad E[X] = 6.25$$

$$P(X=0) = e^{-6.25} \approx 0.001930$$

$$P(X=1) = \frac{6.25^1 e^{-6.25}}{1!} = 6.25 \times 0.001930 \approx 0.012063$$

$$P(X \geq 2) = 1 - P(X=0) - P(X=1) = 1 - 0.001930 - 0.012063 = 0.986007$$

---

### Exercise 8: Full Distribution — Comparing Two Intervals

**Problem:** Accidents at a busy intersection follow a Poisson distribution with an average of 6 per month. Management claims that in any given week, the probability of zero accidents is over 20%. Verify this claim.

**Solution:**

**Step 1:** Convert the rate from monthly to weekly.

Assuming a month has approximately 4 weeks:

$$\lambda_{\text{week}} = \frac{6}{4} = 1.5$$

**Step 2:** Compute $P(X=0)$ for a weekly window:

$$P(X=0) = e^{-1.5} \approx 0.2231$$

**Conclusion:** $P(X=0) \approx 22.31\% > 20\%$. The management's claim is **verified**.

---

### Exercise 9: The Gotcha — Rate Change Disguised as a Different Problem

**Problem:** Typos in a manuscript follow a Poisson distribution at a rate of 2 per page. An editor reviews a **half-page excerpt** and then a **full 3-page section** on the same day.

(a) Find the probability of exactly 1 typo in the half-page excerpt.

(b) Find the probability of **at most 2** typos in the 3-page section.

(c) A student argues: "Since we already know there was 1 typo in the half-page, the expected number of typos in the remaining 2.5 pages of the 3-page section is $2 \times 2.5 - 1 = 4$." Identify the error in this reasoning.

**Solution:**

**Part (a): Half-page**

$$\lambda_{0.5} = 2 \times 0.5 = 1$$

$$P(X=1) = \frac{1^1 e^{-1}}{1!} = e^{-1} \approx 0.3679$$

**Part (b): 3-page section**

$$\lambda_3 = 2 \times 3 = 6$$

$$P(X=0) = e^{-6} \approx 0.002479$$

$$P(X=1) = 6e^{-6} \approx 0.014873$$

$$P(X=2) = \frac{36 e^{-6}}{2} \approx 0.044618$$

$$P(X \leq 2) = 0.002479 + 0.014873 + 0.044618 = 0.0620$$

**Part (c): The error**

The student committed two mistakes in one step:

**Mistake 1 — Conditioning on a past outcome:** The Poisson distribution assumes events are **independent**. The outcome in the half-page excerpt has absolutely no effect on the expected count in the remaining pages. You cannot "subtract" a count from one sub-interval when computing the rate for another. Each interval is modelled independently with its own $\lambda$.

**Mistake 2 — Subtracting observed counts from expected rates:** Even if conditioning were valid, subtracting a realised count (1 typo) from an expected rate ($2 \times 2.5 = 5$) confuses two different quantities. The expected number of typos in the remaining 2.5 pages is simply $\lambda_{2.5} = 2 \times 2.5 = 5$, regardless of what was observed anywhere else.

The correct approach treats each interval as an independent Poisson random variable with its own scaled rate. The half-page result is irrelevant to the 3-page section calculation.

---

## 7. Core Formulas Summary

| Formula | Description |
| :--- | :--- |
| $P(X=k) = \frac{\lambda^k e^{-\lambda}}{k!}$ | Poisson PMF |
| $E[X] = \lambda$ | Mean equals rate |
| $V(X) = \lambda$ | Variance equals rate |
| $P(X=0) = e^{-\lambda}$ | Probability of zero events (simplification) |
| $P(X \geq 1) = 1 - e^{-\lambda}$ | At least one event (complement shortcut) |
| $\lambda_t = \lambda \cdot t$ | Rate scaling to a different interval of length $t$ |
| $\lambda \approx n \cdot p$ | Binomial-to-Poisson approximation |

---

## Exam Tip: Always Scale $\lambda$ Before Substituting

The most common Poisson exam error is substituting the wrong rate into the formula. Before writing down the PMF, always ask: "Is the rate given for the same interval length as the question asks about?" If not, scale first. Label your scaled rate explicitly (e.g., $\lambda_{2h} = 6$) to avoid confusion during multi-part problems.


---

<!-- Source: Phase_5_Continuous_Random_Variables_Distributions/phase_5_1_normal_distribution.md -->
# Phase 5.1: Normal Distribution

The Normal Distribution ($X \sim N(\mu, \sigma^2)$) is the most important continuous distribution in statistics. It is characterized by its symmetric, bell-shaped curve, where the mean, median, and mode are all equal and located at the center.

## 1. Theoretical Foundation

### The Standardization Process
Since there are infinitely many normal distributions (different $\mu$ and $\sigma$), we use the **Standard Normal Distribution** ($Z \sim N(0, 1)$) as a universal reference. We transform any value $x$ into a $Z$-score using the formula:

$$Z = \frac{X - \mu}{\sigma}$$

*   **$Z$**: The number of standard deviations a value is from the mean.
*   **$\mu$**: The population mean.
*   **$\sigma$**: The population standard deviation (**Note:** If given variance $\sigma^2$, you must take the square root!).

### Reading the Z-Table
Z-tables typically provide the "area to the left" of a given $z$, denoted as $P(Z \le z)$ or $\Phi(z)$.

### Symmetry & Complement Rules
Because the curve is perfectly symmetric:
1.  **Lower Tail:** $P(Z \le -z) = 1 - P(Z \le z)$.
2.  **Upper Tail:** $P(Z \ge z) = 1 - P(Z \le z)$.
3.  **Intervals:** $P(a \le Z \le b) = P(Z \le b) - P(Z \le a)$.
4.  **Equality:** For any continuous distribution, $P(X = x) = 0$. Therefore, $P(X < x)$ is the same as $P(X \le x)$.

---

## 2. Solved Examples

### Example 1: Basic Standardization
A variable $X$ follows $N(100, 25)$. Find the $Z$-score for $x = 110$.

**Step 1: Identify parameters.**
*   $\mu = 100$
*   $\sigma^2 = 25 \implies \sigma = \sqrt{25} = 5$.

**Step 2: WIP State.**
Apply the formula:
$$Z = \frac{110 - 100}{?}$$

**Step 3: Final Calculation.**
$$Z = \frac{10}{5} = 2.0$$
The value 110 is **2 standard deviations** above the mean.

---

### Example 2: Finding Probability (Less Than)
Given $X \sim N(50, 100)$, find $P(X < 45)$.

**Step 1: Standardize.**
*   $\mu = 50, \sigma = 10$.
*   $z = \frac{45 - 50}{10} = -0.5$.

**Step 2: WIP State.**
We need $P(Z < -0.5)$. Using symmetry:
$$P(Z < -0.5) = 1 - P(Z < 0.5)$$

**Step 3: Final Calculation.**
Look up $z = 0.5$ in the table: $\Phi(0.5) = 0.6915$.
$$P(Z < -0.5) = 1 - 0.6915 = 0.3085$$

---

### Example 3: Finding Probability (Greater Than)
In a population with $N(170, 64)$, find the probability a value is greater than 182.

**Step 1: Standardize.**
*   $\mu = 170, \sigma = 8$.
*   $z = \frac{182 - 170}{8} = \frac{12}{8} = 1.5$.

**Step 2: WIP State.**
We want $P(Z > 1.5)$.
$$P(Z > 1.5) = 1 - P(Z \le 1.5)$$

**Step 3: Final Calculation.**
Look up $z = 1.5$: $\Phi(1.5) = 0.9332$.
$$1 - 0.9332 = 0.0668$$

---

### Example 4: Interval Probability
Weights of apples follow $N(150, 400)$. Find $P(140 < X < 170)$.

**Step 1: Standardize both bounds.**
*   $\mu = 150, \sigma = 20$.
*   $z_1 = \frac{140 - 150}{20} = -0.5$.
*   $z_2 = \frac{170 - 150}{20} = 1.0$.

**Step 2: WIP State.**
$$P(-0.5 < Z < 1.0) = \Phi(1.0) - \Phi(-0.5)$$
$$0.8413 - (1 - \Phi(0.5))$$

**Step 3: Final Calculation.**
$0.8413 - (1 - 0.6915) = 0.8413 - 0.3085 = 0.5328$.

---

### Example 5: Finding the 95th Percentile
For $X \sim N(200, 100)$, find the value $x$ such that only 5% of values are larger.

**Step 1: Determine the target probability.**
If 5% are larger, then 95% are smaller. $P(Z < z) = 0.95$.

**Step 2: WIP State.**
Look up $0.9500$ in the Z-table. It lies between $z=1.64$ and $z=1.65$. Usually, we use $z = 1.645$.
$$x = \mu + (z \cdot \sigma) = 200 + (1.645 \cdot 10)$$

**Step 3: Final Calculation.**
$$x = 200 + (1.645 \cdot 10) = 200 + 16.45 = 216.45$$

---

### Example 6: Finding the Middle 50%
Find the range $(a, b)$ symmetric about the mean for $N(0, 1)$ that contains 50% of the data.

**Step 1: Analyze the tails.**
If the middle is 50%, each tail contains $(100\% - 50\%) / 2 = 25\%$.
We need $P(Z < z) = 0.75$.

**Step 2: WIP State.**
Look up $0.7500$ in the table. $z \approx 0.67$.

**Step 3: Final Calculation.**
The range is $(-0.67, 0.67)$.

---

### Example 7: IQ Scores
IQ scores are $N(100, 225)$. What is the probability a person has an IQ between 85 and 115?

**Step 1: Standardize.**
*   $\mu = 100, \sigma = 15$.
*   $z_1 = \frac{85 - 100}{15} = -1.0$.
*   $z_2 = \frac{115 - 100}{15} = 1.0$.

**Step 2: WIP State.**
$$P(-1 < Z < 1) = \Phi(1) - \Phi(-1)$$

**Step 3: Final Calculation.**
$0.8413 - (1 - 0.8413) = 0.8413 - 0.1587 = 0.6826$.
(This matches the Empirical Rule!)

---

### Example 8: Reverse Lookup for Variance
In a normal distribution with $\mu = 50$, we know that $P(X < 60) = 0.9772$. Find the standard deviation.

**Step 1: Find the Z-score.**
Look up $0.9772$ in the Z-table. It corresponds exactly to $z = 2.0$.

**Step 2: WIP State.**
Substitute into the formula:
$$2.0 = \frac{60 - 50}{\sigma}$$
$$2.0 = \frac{10}{?}$$

**Step 3: Final Calculation.**
$2.0 \cdot \sigma = 10 \implies \sigma = 5$.
The standard deviation is **5**.


---

<!-- Source: Phase_5_Continuous_Random_Variables_Distributions/phase_5_2_empirical_rule.md -->
# Phase 5.2: The Empirical Rule (68-95-99.7 Rule)

The Empirical Rule is a quick way to estimate probabilities for any normal distribution without needing a Z-table. It describes the percentage of data that falls within specific standard deviation intervals from the mean.

## 1. Theoretical Foundation

For any normal distribution $X \sim N(\mu, \sigma^2)$:
1.  **68%** of the data falls within **1 standard deviation** $(\mu \pm 1\sigma)$.
2.  **95%** of the data falls within **2 standard deviations** $(\mu \pm 2\sigma)$.
3.  **99.7%** of the data falls within **3 standard deviations** $(\mu \pm 3\sigma)$.

### Breakdown of Areas
Since the normal curve is symmetric, we can split these intervals:
*   $\mu$ to $\mu + 1\sigma$: **34%**
*   $\mu + 1\sigma$ to $\mu + 2\sigma$: **13.5%** ($ (95 - 68) / 2 $)
*   $\mu + 2\sigma$ to $\mu + 3\sigma$: **2.35%** ($ (99.7 - 95) / 2 $)
*   Beyond $\mu + 3\sigma$: **0.15%**

> **Shortcut:** Use the Empirical Rule for "clean" multiples of $\sigma$. If the value is not exactly 1, 2, or 3 standard deviations away, you **must** use the Z-table.

---

## 2. Solved Examples

### Example 1: Basic Application
Heights of students are $N(170, 25)$. What percentage of students are between 165 cm and 175 cm?

**Step 1: Identify $\mu$ and $\sigma$.**
*   $\mu = 170, \sigma = 5$.

**Step 2: WIP State.**
Check the distances from the mean:
*   $175 = \mu + 1\sigma$
*   $165 = \mu - ?$

**Step 3: Final Calculation.**
The interval is exactly $\mu \pm 1\sigma$.
According to the Empirical Rule, this covers **68%** of the data.

---

### Example 2: The 95% Range
The lifespan of a battery is $N(50, 4)$ months. Between what two values do 95% of battery lifespans fall?

**Step 1: Identify parameters.**
$\mu = 50, \sigma = 2$.

**Step 2: WIP State.**
95% corresponds to $\mu \pm 2\sigma$.
*   Lower bound: $50 - 2(2) = ?$
*   Upper bound: $50 + 2(2) = ?$

**Step 3: Final Calculation.**
The range is **46 to 54 months**.

---

### Example 3: Tail Probability (Greater Than)
A test has $N(70, 100)$. What percentage of students scored above 90?

**Step 1: Find the number of standard deviations.**
$\mu = 70, \sigma = 10$.
$90 = 70 + 2(10)$. So, 90 is at $\mu + 2\sigma$.

**Step 2: WIP State.**
We know 95% is within $\mu \pm 2\sigma$.
This leaves 5% in the two tails combined ($x < 50$ and $x > 90$).

**Step 3: Final Calculation.**
By symmetry, the upper tail ($x > 90$) contains $5\% / 2 = 2.5\%$.

---

### Example 4: Half-Interval
If $X \sim N(10, 4)$, what is $P(10 < X < 16)$?

**Step 1: Identify parameters.**
$\mu = 10, \sigma = 2$.

**Step 2: WIP State.**
16 is $\mu + 3\sigma$.
The interval $\mu \pm 3\sigma$ covers 99.7%.
The interval from $\mu$ to $\mu + 3\sigma$ covers half of that.

**Step 3: Final Calculation.**
$99.7\% / 2 = 49.85\%$.

---

### Example 5: Combining Segments
For $N(100, 100)$, find $P(90 < X < 120)$.

**Step 1: Identify bounds.**
$\mu = 100, \sigma = 10$.
*   $90 = \mu - 1\sigma$
*   $120 = \mu + 2\sigma$

**Step 2: WIP State.**
*   Area from $\mu - 1\sigma$ to $\mu$: 34%
*   Area from $\mu$ to $\mu + 2\sigma$: ?%

**Step 3: Final Calculation.**
Area from $\mu$ to $\mu + 2\sigma$ is $95\% / 2 = 47.5\%$.
Total: $34\% + 47.5\% = 81.5\%$.

---

### Example 6: Sample Size Estimation
In a town of 10,000 people, the weight is $N(70, 100)$. How many people weigh more than 100 kg?

**Step 1: Identify standard deviations.**
$100 = 70 + 3(10)$. This is $\mu + 3\sigma$.

**Step 2: WIP State.**
The area above $\mu + 3\sigma$ is $0.15\%$.
Calculate: $10,000 \times 0.0015 = ?$

**Step 3: Final Calculation.**
$10,000 \times 0.0015 = 15$ people.

---

### Example 7: Defect Detection
A bolt diameter is $N(10, 0.0001)$. A bolt is defective if its diameter is outside $[9.98, 10.02]$. What is the defect rate?

**Step 1: Check the bounds.**
$\mu = 10, \sigma = \sqrt{0.0001} = 0.01$.
Range is $\mu \pm 2\sigma = 10 \pm 2(0.01) = [9.98, 10.02]$.

**Step 2: WIP State.**
The percentage of "good" bolts is 95%.

**Step 3: Final Calculation.**
Defect rate = $100\% - 95\% = 5\%$.

---

### Example 8: Comparing Groups
Group A is $N(50, 25)$ and Group B is $N(60, 4)$. Which group has a higher percentage of values above 65?

**Step 1: Check Group A.**
$\sigma_A = \sqrt{25} = 5$.
$65 = 50 + 3(5) \implies \mu_A + 3\sigma_A$.
Percentage $> 65 = 0.15\%$.

**Step 2: WIP State.**
Check Group B:
$\sigma_B = \sqrt{4} = 2$.
$65 = 60 + 2.5(2) \implies \mu_B + 2.5\sigma_B$.

**Step 3: Final Calculation.**
Since 2.5 is less than 3, the value 65 is "closer" to the mean in Group B than in Group A.
Being closer to the mean (in standard deviation units) means a **larger upper tail**. Therefore, Group B has a higher percentage of values above 65.
*(Note: We would need a Z-table for the exact value of Group B, but the comparison is clear via the Empirical Rule logic.)*


---

<!-- Source: Phase_5_Continuous_Random_Variables_Distributions/phase_5_3_other_continuous_distributions.md -->
# Phase 5.3: Other Continuous Distributions

While the Normal distribution is the most famous, other continuous distributions like the **Uniform** and **Exponential** are essential for modeling specific real-world phenomena like wait times and equally likely outcomes over an interval.

## 1. Uniform Distribution ($X \sim U(a, b)$)
A distribution where all intervals of the same length are equally likely.

*   **PDF:** $f(x) = \frac{1}{b - a}$ for $a \le x \le b$.
*   **Mean:** $E[X] = \frac{a + b}{2}$
*   **Variance:** $Var(X) = \frac{(b - a)^2}{12}$
*   **Probability:** $P(x_1 < X < x_2) = \frac{x_2 - x_1}{b - a}$

## 2. Exponential Distribution ($X \sim Exp(\lambda)$)
Used to model the time between events in a Poisson process.

*   **PDF:** $f(x) = \lambda e^{-\lambda x}$ for $x \ge 0$.
*   **CDF:** $P(X \le x) = 1 - e^{-\lambda x}$
*   **Mean:** $E[X] = \frac{1}{\lambda}$
*   **Variance:** $Var(X) = \frac{1}{\lambda^2}$
*   **Complement Rule:** $P(X > x) = e^{-\lambda x}$ (very useful for "wait time longer than" problems).

---

## 3. Solved Examples

### Example 1: Uniform Probability
A bus arrives at a stop every 20 minutes. A person's wait time $X$ is $U(0, 20)$. What is the probability they wait more than 15 minutes?

**Step 1: Identify bounds.**
$a = 0, b = 20$.

**Step 2: WIP State.**
$P(X > 15) = \frac{b - 15}{b - a} = \frac{20 - 15}{?}$

**Step 3: Final Calculation.**
$P(X > 15) = \frac{5}{20} = 0.25$.

---

### Example 2: Uniform Mean and Variance
For $X \sim U(5, 15)$, find the expected value and variance.

**Step 1: Apply Mean formula.**
$E[X] = (5 + 15) / 2 = 10$.

**Step 2: WIP State.**
$Var(X) = \frac{(15 - 5)^2}{12} = \frac{10^2}{?}$

**Step 3: Final Calculation.**
$Var(X) = 100 / 12 = 8.3333$.

---

### Example 3: Exponential Wait Time
The time between arrivals at a bank follows an exponential distribution with $\lambda = 2$ arrivals per hour. What is the probability that the next arrival occurs within 30 minutes?

**Step 1: Convert units.**
$\lambda = 2$ per hour. 30 minutes is $0.5$ hours.

**Step 2: WIP State.**
Use the CDF: $P(X \le 0.5) = 1 - e^{-2(0.5)}$
$P(X \le 0.5) = 1 - e^{-?}$

**Step 3: Final Calculation.**
$1 - e^{-1} \approx 1 - 0.3679 = 0.6321$.

---

### Example 4: Exponential - Longer Than
If the average lifespan of a lightbulb is 1000 hours (exponentially distributed), what is the probability it lasts more than 1500 hours?

**Step 1: Find $\lambda$.**
Mean $E[X] = 1/\lambda = 1000 \implies \lambda = 0.001$.

**Step 2: WIP State.**
Use the complement rule: $P(X > 1500) = e^{-0.001(1500)}$

**Step 3: Final Calculation.**
$e^{-1.5} \approx 0.2231$.

---

### Example 5: Median of Exponential
Find the median time for the lightbulb in Example 4.

**Step 1: Set CDF to 0.5.**
$1 - e^{-\lambda x} = 0.5 \implies e^{-\lambda x} = 0.5$.

**Step 2: WIP State.**
$-\lambda x = \ln(0.5)$
$x = \frac{-\ln(0.5)}{0.001} = \frac{\ln(2)}{?}$

**Step 3: Final Calculation.**
$x = 0.693 / 0.001 = 693$ hours.
*(Note: The median is less than the mean in an exponential distribution!)*

---

### Example 6: Uniform Interval
$X \sim U(-5, 5)$. Find $P(|X| < 2)$.

**Step 1: Rewrite the inequality.**
$-2 < X < 2$.

**Step 2: WIP State.**
Length of interval $= 2 - (-2) = 4$.
Length of total range $= 5 - (-5) = ?$.

**Step 3: Final Calculation.**
$P = 4 / 10 = 0.4$.

---

### Example 7: Combined Probability
If $X \sim U(0, 10)$, find $P(X > 2 | X < 8)$.

**Step 1: Use the conditional probability formula.**
$P(A|B) = \frac{P(A \cap B)}{P(B)}$
$P(X > 2 \cap X < 8) = P(2 < X < 8) = \frac{8 - 2}{10} = 0.6$.

**Step 2: WIP State.**
$P(X < 8) = \frac{8 - 0}{10} = 0.8$.
$P = 0.6 / ?$

**Step 3: Final Calculation.**
$P = 0.6 / 0.8 = 0.75$.

---

## 4. The "Gotcha" Section (Hard Example)

### Example 8: The Memoryless Property Trap
The time $X$ you spend waiting for a server to respond is exponentially distributed with a mean of 5 seconds. You have already waited 10 seconds. What is the probability you will have to wait at least another 5 seconds?

**The "Gotcha":**
Many students try to calculate $P(X > 15 | X > 10)$ using complex integrals or the conditional probability formula. They think that since they have already waited a long time, the event "must happen soon."

**The Reality (The Memoryless Property):**
The Exponential distribution is **memoryless**. This means:
$$P(X > s + t | X > s) = P(X > t)$$
The fact that you waited 10 seconds ($s$) is completely irrelevant to the *additional* time ($t$) you will wait.

**Step 1: Identify the additional wait time.**
We want the probability of waiting *at least another* 5 seconds. So $t = 5$.

**Step 2: WIP State.**
The probability is simply $P(X > 5)$.
Mean = 5, so $\lambda = 1/5 = 0.2$.

**Step 3: Final Calculation.**
$$P(X > 5) = e^{-0.2(5)} = e^{-1} \approx 0.3679$$

**Result:** The probability is **0.3679**, exactly the same as if you had just started waiting! This is counter-intuitive but a key property of the Exponential distribution.
*(Warning: This property ONLY applies to the Exponential distribution in the continuous world!)*


---

<!-- Source: Phase_6_Inferential_Statistics/phase_6_1_central_limit_theorem.md -->
# Phase 6: Inferential Statistics - Central Limit Theorem (CLT)

## 1. Theoretical Foundation

The Central Limit Theorem (CLT) is one of the most fundamental concepts in probability and statistics. It states that, given certain conditions, the sampling distribution of the sample mean will approach a normal distribution as the sample size gets larger, regardless of the shape of the population distribution.

### 1.1 Core Concept

Let $X_1, X_2, \dots, X_n$ be a random sample of size $n$ drawn from a population with an overall mean $\mu$ and a finite variance $\sigma^2$. Let $\bar{X}$ be the sample mean.

According to the CLT, if $n$ is sufficiently large (typically $n \ge 30$), the distribution of the sample mean $\bar{X}$ is approximately normal:

$$ \bar{X} \sim N\left(\mu, \frac{\sigma^2}{n}\right) $$

**Key parameters of the sampling distribution:**
*   **Mean of the sample means:** $\mu_{\bar{X}} = \mu$
*   **Variance of the sample means:** $\sigma_{\bar{X}}^2 = \frac{\sigma^2}{n}$
*   **Standard Error (Standard deviation of the sample means):** $\sigma_{\bar{X}} = \frac{\sigma}{\sqrt{n}}$

### 1.2 The Standard Normal Transformation (Z-Score)

To calculate probabilities involving $\bar{X}$, we standardize it to the standard normal distribution $Z \sim N(0, 1)$ using the formula:

$$ Z = \frac{\bar{X} - \mu}{\frac{\sigma}{\sqrt{n}}} $$

### 1.3 Sum of Random Variables

The CLT also applies to the sum of the sample observations, $S_n = X_1 + X_2 + \dots + X_n$. As $n$ increases, the distribution of $S_n$ approaches a normal distribution:

$$ S_n \sim N(n\mu, n\sigma^2) $$

Standardizing the sum gives:

$$ Z = \frac{S_n - n\mu}{\sigma\sqrt{n}} $$

### 1.4 Important Caveats and Rules of Thumb
*   **Sample Size:** A general rule of thumb is that $n \ge 30$ is "sufficiently large" for the CLT to apply, even if the underlying population is highly skewed.
*   **Normal Population:** If the underlying population is *already* normally distributed, then the sample mean $\bar{X}$ is exactly normally distributed for *any* sample size $n$.
*   **Independence:** The sampled observations must be independent.

---

## 2. Step-by-Step Examples

### Example 1: Basic Application of CLT
Suppose the average weight of a certain species of fish is $\mu = 40$ kg with a standard deviation of $\sigma = 8$ kg. A sample of $n = 35$ fish is caught. What is the probability that the average weight of the sample is strictly less than $42$ kg?

**Step 1: Identify given information**
*   $\mu = 40$
*   $\sigma = 8$
*   $n = 35$

**Step 2: Calculate Standard Error**
$$ \sigma_{\bar{X}} = \frac{\sigma}{\sqrt{n}} = \frac{8}{\sqrt{35}} \approx 1.352 $$

**Step 3: Calculate Z-score**
We want $P(\bar{X} < 42)$. Let's standardize $42$:
$$ Z = \frac{42 - 40}{1.352} = \frac{2}{1.352} \approx 1.48 $$

**Step 4: Find the probability**
$$ P(\bar{X} < 42) = P(Z < 1.48) = 0.9306 $$

### Example 2: Probability Between Two Values
An elevator has a maximum weight limit. The weights of people using the elevator have a mean $\mu = 75$ kg and a standard deviation $\sigma = 15$ kg. If 40 people enter the elevator, what is the probability that their average weight is between $70$ kg and $78$ kg?

**Step 1: Standard Error**
$$ \sigma_{\bar{X}} = \frac{15}{\sqrt{40}} \approx 2.37 $$

**Step 2: Z-scores for boundaries**
For $70$: $Z_1 = \frac{70 - 75}{2.37} = -2.11$
For $78$: $Z_2 = \frac{78 - 75}{2.37} = 1.27$

**Step 3: Compute Probability**
$$ P(70 < \bar{X} < 78) = P(-2.11 < Z < 1.27) = P(Z < 1.27) - P(Z < -2.11) $$
$$ = 0.8980 - 0.0174 = 0.8806 $$

### Example 3: Finding a Threshold Value (Inverse Normal)
The mean time to complete a test is 50 minutes with a standard deviation of 10 minutes. For a class of 36 students, what is the average time $x$ such that there is only a 5% chance the class mean exceeds $x$?

**Step 1: Set up the problem**
We want $P(\bar{X} > x) = 0.05$. This implies $P(\bar{X} < x) = 0.95$.

**Step 2: Find corresponding Z-score**
Using a standard normal table, the Z-score for an area of $0.95$ is approximately $1.645$.

**Step 3: Solve for $x$**
$$ 1.645 = \frac{x - 50}{\frac{10}{\sqrt{36}}} $$
$$ 1.645 = \frac{x - 50}{1.667} $$
$$ x - 50 = 2.74 $$
$$ x = 52.74 \text{ minutes} $$

### Example 4: Applying CLT to a Sum
A shipping company loads 50 boxes onto a truck. The weight of each box has a mean of 20 kg and a standard deviation of 4 kg. What is the probability that the total weight of the boxes exceeds 1050 kg?

**Step 1: Identify Sum parameters**
*   $n = 50$, $\mu = 20$, $\sigma = 4$
*   Mean of sum: $n\mu = 50 \times 20 = 1000$
*   Standard deviation of sum: $\sigma\sqrt{n} = 4\sqrt{50} \approx 28.28$

**Step 2: Calculate Z-score**
We want $P(S_n > 1050)$.
$$ Z = \frac{1050 - 1000}{28.28} = \frac{50}{28.28} \approx 1.77 $$

**Step 3: Compute Probability**
$$ P(S_n > 1050) = P(Z > 1.77) = 1 - P(Z \le 1.77) = 1 - 0.9616 = 0.0384 $$

### Example 5: CLT with Unknown Underlying Distribution (Uniform)
A random variable $X$ follows a continuous uniform distribution between 0 and 10. A sample of $n = 45$ is drawn. Find the probability that the sample mean is less than 4.5.

**Step 1: Find Population Mean and Variance**
For a uniform distribution $U(a,b)$:
$$ \mu = \frac{a+b}{2} = \frac{0+10}{2} = 5 $$
$$ \sigma^2 = \frac{(b-a)^2}{12} = \frac{100}{12} = 8.33 $$
$$ \sigma = \sqrt{8.33} \approx 2.89 $$

**Step 2: Calculate Standard Error**
$$ \sigma_{\bar{X}} = \frac{2.89}{\sqrt{45}} \approx 0.43 $$

**Step 3: Z-score and Probability**
$$ Z = \frac{4.5 - 5}{0.43} = -1.16 $$
$$ P(\bar{X} < 4.5) = P(Z < -1.16) = 0.1230 $$

### Example 6: Determining Minimum Sample Size
A lightbulb manufacturer knows that the lifespan of its bulbs has a standard deviation of $\sigma = 50$ hours. How large of a sample is needed to ensure that there is at least a 99% probability that the sample mean is within 15 hours of the true population mean?

**Step 1: Set up the probability statement**
We want $P(|\bar{X} - \mu| \le 15) \ge 0.99$.
This is equivalent to $P(-15 \le \bar{X} - \mu \le 15) \ge 0.99$.

**Step 2: Convert to Z-scores**
Divide the inequality by $\sigma_{\bar{X}} = \frac{50}{\sqrt{n}}$:
$$ P\left(\frac{-15}{50/\sqrt{n}} \le Z \le \frac{15}{50/\sqrt{n}}\right) \ge 0.99 $$
Let $Z_c = \frac{15\sqrt{n}}{50}$. We want the area between $-Z_c$ and $Z_c$ to be 0.99.

**Step 3: Find critical Z-value**
For a central area of 0.99, the tails have $0.005$ each. The $Z$-score for an area of $0.995$ to the left is approximately $2.576$.
So, $Z_c = 2.576$.

**Step 4: Solve for $n$**
$$ \frac{15\sqrt{n}}{50} \ge 2.576 $$
$$ \sqrt{n} \ge \frac{50 \times 2.576}{15} \approx 8.587 $$
$$ n \ge (8.587)^2 \approx 73.7 $$
Since sample size must be an integer, we round up to $n = 74$.

---

### Example 7: The "Single Observation vs. Sample Mean" Trap (Gotcha Moment)
The resting heart rate of adults is normally distributed with a mean of 72 beats per minute (bpm) and a standard deviation of 8 bpm. 
**Part A:** What is the probability that a *randomly selected individual* has a heart rate above 75 bpm?
**Part B:** What is the probability that a *random sample of 16 adults* has a sample mean heart rate above 75 bpm?

#### Gotcha Section Analysis
A very common mistake in exams is confusing the distribution of the population with the distribution of the sample mean. If the question asks about ONE individual, you do not use the CLT adjustment ($\sqrt{n}$). If it asks about a SAMPLE, you must divide the standard deviation by $\sqrt{n}$. Furthermore, $n=16$ is less than 30, but because the underlying population is explicitly stated to be *normally distributed*, the sampling distribution of the mean is exactly normal regardless of sample size.

**Solution Part A (Single Individual):**
We are looking for $P(X > 75)$. We use the population standard deviation $\sigma = 8$.
$$ Z = \frac{75 - 72}{8} = 0.375 $$
$$ P(X > 75) = P(Z > 0.375) = 1 - P(Z \le 0.375) = 1 - 0.6462 = 0.3538 $$

**Solution Part B (Sample Mean):**
We are looking for $P(\bar{X} > 75)$. We use the standard error $\sigma_{\bar{X}} = \frac{8}{\sqrt{16}} = \frac{8}{4} = 2$.
$$ Z = \frac{75 - 72}{2} = 1.5 $$
$$ P(\bar{X} > 75) = P(Z > 1.5) = 1 - P(Z \le 1.5) = 1 - 0.9332 = 0.0668 $$

Notice how drastically different the probabilities are. It is much harder for a group average to deviate from the true mean than it is for a single individual.

---

### Example 8: Sum vs. Mean Trap combined with Proportions (Gotcha Moment)
A biased coin has a probability $p = 0.6$ of landing heads. You flip the coin 400 times. What is the probability that the number of heads obtained is exactly 240? What is the probability that the *proportion* of heads is greater than 0.65?

#### Gotcha Section Analysis
There are two distinct traps here:
1. **Continuity Correction:** When using the CLT to approximate a discrete distribution (like the Binomial distribution) with a continuous Normal distribution, you MUST apply the continuity correction if you are asking for an exact value or specific bounds.
2. **Proportion vs Sum:** A binomial variable $X$ is a sum of Bernoulli trials. The sample proportion $\hat{p}$ is the sample mean of Bernoulli trials ($\hat{p} = \frac{X}{n}$). You must use the correct parameters for each.

**Solution Part A (Exact Value using Continuity Correction):**
The number of heads $X \sim Binomial(n=400, p=0.6)$.
Using normal approximation:
*   Mean: $\mu = np = 400(0.6) = 240$
*   Standard Deviation: $\sigma = \sqrt{np(1-p)} = \sqrt{400(0.6)(0.4)} = \sqrt{96} \approx 9.798$

To find $P(X = 240)$, we must use the interval $(239.5, 240.5)$ because $X$ is discrete.
$$ Z_1 = \frac{239.5 - 240}{9.798} \approx -0.05 $$
$$ Z_2 = \frac{240.5 - 240}{9.798} \approx 0.05 $$
$$ P(X = 240) \approx P(-0.05 < Z < 0.05) = 0.5199 - 0.4801 = 0.0398 $$
*(Without continuity correction, the probability of an exact value in a continuous distribution is 0, which is a fatal error!)*

**Solution Part B (Proportions):**
We want the probability that the sample proportion $\hat{p} > 0.65$.
According to the CLT for proportions, $\hat{p} \sim N\left(p, \frac{p(1-p)}{n}\right)$.
*   Mean: $\mu_{\hat{p}} = p = 0.6$
*   Standard Error: $\sigma_{\hat{p}} = \sqrt{\frac{p(1-p)}{n}} = \sqrt{\frac{0.6(0.4)}{400}} = \sqrt{\frac{0.24}{400}} = 0.0245$

Without correction (commonly accepted for very large $n$ in proportion tests):
$$ Z = \frac{0.65 - 0.6}{0.0245} \approx 2.04 $$
$$ P(\hat{p} > 0.65) = P(Z > 2.04) = 1 - 0.9793 = 0.0207 $$
*(Always check if your professor requires continuity correction for proportions!)*


---

<!-- Source: Phase_6_Inferential_Statistics/phase_6_2_confidence_intervals.md -->
# Phase 6: Inferential Statistics - Confidence Intervals

## 1. Theoretical Foundation

A **Confidence Interval (CI)** provides a range of plausible values for an unknown population parameter (like the mean $\mu$ or proportion $p$). Instead of a single point estimate (like $\bar{X}$ or $\hat{p}$), a confidence interval gives a margin of error around the point estimate, along with a specified level of confidence that the true parameter lies within that interval.

### 1.1 Core Concept

The general formula for a confidence interval is:
$$ \text{Point Estimate} \pm \text{Margin of Error} $$
$$ \text{Point Estimate} \pm (\text{Critical Value}) \times (\text{Standard Error}) $$

The **Confidence Level** is denoted by $(1 - \alpha) \times 100\%$, where $\alpha$ is the significance level. For example, a 95% confidence level means $\alpha = 0.05$. The critical value separates the tail area $\alpha/2$ from the central area.

### 1.2 Confidence Interval for Population Mean ($\mu$)

#### Case A: Population Standard Deviation ($\sigma$) is KNOWN
When $\sigma$ is known and either the population is normal or $n \ge 30$, we use the Standard Normal (Z) distribution.
$$ CI = \bar{X} \pm Z_{\alpha/2} \left( \frac{\sigma}{\sqrt{n}} \right) $$
*   $\bar{X}$ = Sample mean
*   $Z_{\alpha/2}$ = Z critical value (e.g., 1.96 for 95% confidence)
*   $\frac{\sigma}{\sqrt{n}}$ = Standard Error

#### Case B: Population Standard Deviation ($\sigma$) is UNKNOWN
When $\sigma$ is unknown, we estimate it using the sample standard deviation $s$. We must use the Student's t-distribution with $n - 1$ degrees of freedom ($df$).
$$ CI = \bar{X} \pm t_{\alpha/2, n-1} \left( \frac{s}{\sqrt{n}} \right) $$
*   $s$ = Sample standard deviation
*   $t_{\alpha/2, n-1}$ = t critical value with $df = n - 1$

### 1.3 Confidence Interval for Population Proportion ($p$)

When dealing with proportions (e.g., "what percentage of voters favor candidate A?"), we use the sample proportion $\hat{p} = \frac{x}{n}$ (where $x$ is the number of successes).
Assuming large sample sizes ($n\hat{p} \ge 10$ and $n(1-\hat{p}) \ge 10$), we use the Z-distribution:
$$ CI = \hat{p} \pm Z_{\alpha/2} \sqrt{ \frac{\hat{p}(1-\hat{p})}{n} } $$

### 1.4 Sample Size Determination
To achieve a specific Margin of Error ($E$) at a given confidence level:
**For Mean:**
$$ n = \left( \frac{Z_{\alpha/2} \cdot \sigma}{E} \right)^2 $$
**For Proportion:**
$$ n = \hat{p}(1-\hat{p}) \left( \frac{Z_{\alpha/2}}{E} \right)^2 $$
*(If $\hat{p}$ is completely unknown, use $\hat{p} = 0.5$ for the most conservative (largest) sample size).*

---

## 2. Step-by-Step Examples

### Example 1: CI for Mean ($\sigma$ known)
A random sample of 50 apples has a mean weight of 150g. The population standard deviation is known to be 10g. Construct a 95% confidence interval for the true mean weight of all apples.

**Step 1: Identify Given Information**
*   $n = 50$, $\bar{X} = 150$, $\sigma = 10$
*   Confidence level = 95%, so $\alpha = 0.05$ and $\alpha/2 = 0.025$

**Step 2: Find Critical Value**
For a 95% CI, $Z_{0.025} = 1.96$ (from standard normal table).

**Step 3: Calculate Margin of Error (E)**
$$ E = Z_{\alpha/2} \left( \frac{\sigma}{\sqrt{n}} \right) = 1.96 \left( \frac{10}{\sqrt{50}} \right) = 1.96 \times 1.414 \approx 2.77 $$

**Step 4: Construct Interval**
$$ CI = 150 \pm 2.77 = [147.23, 152.77] $$

### Example 2: CI for Mean ($\sigma$ unknown)
A sample of 16 laptop batteries has a mean life of 4.5 hours with a sample standard deviation of 0.8 hours. Assume the population is normally distributed. Find a 99% CI for the true mean battery life.

**Step 1: Identify Given Information**
*   $n = 16$, $\bar{X} = 4.5$, $s = 0.8$
*   Since $\sigma$ is unknown, use t-distribution. $df = n - 1 = 15$.
*   Confidence level = 99%, $\alpha = 0.01$, $\alpha/2 = 0.005$.

**Step 2: Find Critical Value**
From t-table for $df=15$ and tail area 0.005: $t_{0.005, 15} = 2.947$.

**Step 3: Calculate Margin of Error (E)**
$$ E = 2.947 \left( \frac{0.8}{\sqrt{16}} \right) = 2.947 \times 0.2 = 0.5894 $$

**Step 4: Construct Interval**
$$ CI = 4.5 \pm 0.5894 = [3.91, 5.09] $$

### Example 3: CI for Proportion
In a survey of 400 randomly selected adults, 250 said they drink coffee daily. Construct a 90% confidence interval for the true proportion of adults who drink coffee daily.

**Step 1: Calculate Sample Proportion**
$$ \hat{p} = \frac{x}{n} = \frac{250}{400} = 0.625 $$

**Step 2: Find Critical Value**
For 90% confidence, $\alpha = 0.10$, $\alpha/2 = 0.05$. $Z_{0.05} = 1.645$.

**Step 3: Calculate Margin of Error (E)**
$$ E = 1.645 \sqrt{ \frac{0.625(1-0.625)}{400} } = 1.645 \sqrt{\frac{0.234375}{400}} \approx 1.645 \times 0.0242 \approx 0.0398 $$

**Step 4: Construct Interval**
$$ CI = 0.625 \pm 0.0398 = [0.5852, 0.6648] $$

### Example 4: Finding Required Sample Size (Mean)
We want to estimate the mean height of students in a university to within 2 cm with 95% confidence. The population standard deviation is estimated to be 8 cm. How large of a sample is required?

**Step 1: Identify Given Information**
*   $E = 2$ (Margin of error)
*   $\sigma = 8$
*   $Z_{\alpha/2}$ for 95% is $1.96$

**Step 2: Apply Sample Size Formula**
$$ n = \left( \frac{1.96 \times 8}{2} \right)^2 = (1.96 \times 4)^2 = (7.84)^2 = 61.4656 $$

**Step 3: Round Up**
Always round sample size *up* to the next whole number. $n = 62$.

### Example 5: Changing Confidence Levels
Using the data from Example 1 ($n=50, \bar{X}=150, \sigma=10$), what happens to the confidence interval if we increase the confidence level to 99%?

**Step 1: New Critical Value**
For 99%, $Z_{0.005} = 2.576$.

**Step 2: New Margin of Error**
$$ E = 2.576 \left( \frac{10}{\sqrt{50}} \right) \approx 3.64 $$

**Step 3: New Interval**
$$ CI = 150 \pm 3.64 = [146.36, 153.64] $$
*Observation: Higher confidence requires a wider interval.*

### Example 6: Extracting Information from an Interval
A 95% confidence interval for a population mean is given as $[45, 55]$. What was the sample mean and the margin of error?

**Step 1: Find the Sample Mean**
The sample mean is exactly in the middle of the interval.
$$ \bar{X} = \frac{\text{Upper} + \text{Lower}}{2} = \frac{55 + 45}{2} = 50 $$

**Step 2: Find the Margin of Error**
The margin of error is half the width of the interval.
$$ E = \frac{\text{Upper} - \text{Lower}}{2} = \frac{55 - 45}{2} = 5 $$

---

### Example 7: The "Z vs. t" Trap and Degrees of Freedom (Gotcha Moment)
A researcher measures the lifespan of 25 fruit flies. The sample mean is 14 days and the *sample variance* is 16 days squared. Construct a 95% confidence interval for the population mean lifespan.

#### Gotcha Section Analysis
There are three common traps here:
1. **Variance vs. Standard Deviation:** The problem gives the sample *variance* ($s^2 = 16$), not standard deviation. You must take the square root ($s = 4$).
2. **t vs Z:** Many students automatically use $Z=1.96$ because it is a 95% interval. However, because we only have the *sample* variance (and $n < 30$), we MUST use the t-distribution.
3. **Degrees of Freedom:** For $n=25$, degrees of freedom is $df = 24$, not 25.

**Step 1: Extract Correct Values**
*   $n = 25 \implies df = 24$
*   $\bar{X} = 14$
*   $s^2 = 16 \implies s = 4$

**Step 2: Find the correct Critical Value (t-distribution)**
For 95% confidence ($\alpha = 0.05, \alpha/2 = 0.025$) and $df = 24$:
$t_{0.025, 24} = 2.064$ (NOT 1.96!)

**Step 3: Calculate Margin of Error and CI**
$$ E = 2.064 \left( \frac{4}{\sqrt{25}} \right) = 2.064 \left( \frac{4}{5} \right) = 2.064 \times 0.8 = 1.6512 $$
$$ CI = 14 \pm 1.6512 = [12.3488, 15.6512] $$

---

### Example 8: Worst-Case Proportion Sample Size Trap (Gotcha Moment)
You are planning a survey to estimate the proportion of students who prefer online exams. You want the estimate to be accurate within 4 percentage points with 95% confidence. Previous studies suggest the proportion is somewhere between 20% and 30%. What sample size should you use?

#### Gotcha Section Analysis
There are two traps here:
1. **"Within 4 percentage points":** This means the Margin of Error $E = 0.04$. Do not use $E=4$.
2. **Which $\hat{p}$ to use?** The sample size formula for proportions is $n = \hat{p}(1-\hat{p}) \left( \frac{Z}{E} \right)^2$. If no proportion is known, you use $\hat{p} = 0.5$ because it maximizes $\hat{p}(1-\hat{p})$ to $0.25$, yielding the safest (largest) sample size. However, here you are given a *range* (20% to 30%). You must pick the value in the range that is *closest to 50%* because that will maximize the variance and ensure your sample is large enough.

**Step 1: Determine the conservative $\hat{p}$**
The range is $0.20$ to $0.30$. The value closest to $0.50$ is $0.30$.
Let's check the product $\hat{p}(1-\hat{p})$:
*   If $p=0.20 \implies 0.20 \times 0.80 = 0.16$
*   If $p=0.30 \implies 0.30 \times 0.70 = 0.21$
Since $0.21 > 0.16$, using $p=0.30$ guarantees a large enough sample.

**Step 2: Calculate Sample Size**
*   $Z_{0.025} = 1.96$
*   $E = 0.04$
*   $\hat{p} = 0.30$

$$ n = 0.30(1 - 0.30) \left( \frac{1.96}{0.04} \right)^2 $$
$$ n = 0.30(0.70) \left( 49 \right)^2 $$
$$ n = 0.21 \times 2401 = 504.21 $$

**Step 3: Round Up**
You must always round *up* to the nearest integer to ensure the margin of error is *strictly within* 4%.
$n = 505$.
*(If you used $p=0.5$ blindly without looking at the known range, you would get $n=601$, meaning you would waste time and money surveying 96 extra people unnecessarily!)*


---

<!-- Source: Phase_6_Inferential_Statistics/phase_6_3_hypothesis_testing.md -->
# Phase 6: Inferential Statistics - Hypothesis Testing

## 1. Theoretical Foundation

Hypothesis testing is a formal procedure used to evaluate a claim about a population parameter based on sample data. We compare two competing hypotheses and determine if there is enough statistical evidence to reject the default assumption.

### 1.1 The Hypotheses
*   **Null Hypothesis ($H_0$):** The default assumption, representing "no effect," "no difference," or "status quo." It always contains an equality sign ($=, \le, \ge$).
*   **Alternative Hypothesis ($H_1$ or $H_A$):** The claim we are trying to prove. It contains an inequality sign ($\ne, <, >$). The direction of the inequality determines the type of test:
    *   $\ne$ : Two-tailed test
    *   $<$ : Left-tailed test
    *   $>$ : Right-tailed test

### 1.2 Errors in Hypothesis Testing
*   **Type I Error ($\alpha$):** Rejecting $H_0$ when it is actually true (False Positive). $\alpha$ is the significance level of the test.
*   **Type II Error ($\beta$):** Failing to reject $H_0$ when $H_1$ is actually true (False Negative).
*   **Power of the Test ($1 - \beta$):** The probability of correctly rejecting a false $H_0$.

### 1.3 Test Statistics

The test statistic measures how far our sample statistic is from the hypothesized population parameter, standardized by the standard error.

**1. Test for Mean ($\mu$) with KNOWN Population Variance ($\sigma^2$):**
$$ Z_{stat} = \frac{\bar{X} - \mu_0}{\frac{\sigma}{\sqrt{n}}} $$

**2. Test for Mean ($\mu$) with UNKNOWN Population Variance — Large Sample ($n \ge 30$):**
By the CLT, the sample standard deviation $s$ is a reliable estimate of $\sigma$, so $s$ is substituted into the Z-formula:
$$ Z_{stat} = \frac{\bar{X} - \mu_0}{\frac{s}{\sqrt{n}}} $$
> **Note:** Most courses accept using the t-statistic here as well (with $df = n-1$). Because $t_{n-1} \approx Z$ for large $n$, both approaches give virtually identical results. Confirm which convention your course prefers.

**3. Test for Mean ($\mu$) with UNKNOWN Population Variance — Small Sample ($n < 30$):**
Must use the t-distribution with $df = n - 1$ degrees of freedom:
$$ t_{stat} = \frac{\bar{X} - \mu_0}{\frac{s}{\sqrt{n}}} $$
*(This requires the population to be approximately normally distributed.)*

**4. Test for Proportion ($p$):**
$$ Z_{stat} = \frac{\hat{p} - p_0}{\sqrt{\frac{p_0(1-p_0)}{n}}} $$

### 1.4 Decision Rules

There are two equivalent ways to make a decision:

**1. Critical Value Approach:**
*   Determine the critical value(s) ($Z_{crit}$ or $t_{crit}$) based on $\alpha$ and the tail(s) of the test.
*   If the test statistic falls into the **rejection region** (beyond the critical value), reject $H_0$.

**2. P-Value Approach:**
*   The **p-value** is the probability of observing a test statistic as extreme as, or more extreme than, the one calculated, assuming $H_0$ is true.
*   **Rule:** If $p\text{-value} \le \alpha$, reject $H_0$. If $p\text{-value} > \alpha$, fail to reject $H_0$.

---

## 2. Step-by-Step Examples

### Example 1: Right-Tailed Z-Test for Mean ($\sigma$ known)
A company claims that its new light bulbs last *more than* 1000 hours on average. A sample of 40 bulbs has an average lifespan of 1020 hours. The population standard deviation is known to be 80 hours. Test the claim at a 5% significance level.

**Step 1: State Hypotheses**
*   $H_0: \mu \le 1000$ (Status quo)
*   $H_1: \mu > 1000$ (Claim, right-tailed)

**Step 2: Calculate Test Statistic**
*   $n = 40, \bar{X} = 1020, \mu_0 = 1000, \sigma = 80$
$$ Z_{stat} = \frac{1020 - 1000}{\frac{80}{\sqrt{40}}} = \frac{20}{12.65} \approx 1.58 $$

**Step 3: Determine Critical Value & Decision**
*   $\alpha = 0.05$, right-tailed. $Z_{crit} = 1.645$.
*   Since $1.58 < 1.645$, the statistic is NOT in the rejection region.
*   **Conclusion:** Fail to reject $H_0$. There is not enough evidence to support the claim that the bulbs last more than 1000 hours.

### Example 2: Two-Tailed t-Test for Mean ($\sigma$ unknown)
A machine is supposed to fill bottles with exactly 500ml of water. A random sample of 15 bottles shows a mean of 496ml and a standard deviation of 8ml. Test if the machine is out of calibration at the $\alpha = 0.01$ level.

**Step 1: State Hypotheses**
*   $H_0: \mu = 500$
*   $H_1: \mu \ne 500$ (Two-tailed)

**Step 2: Calculate Test Statistic**
*   $n = 15, \bar{X} = 496, \mu_0 = 500, s = 8$. Use t-test ($df = 14$).
$$ t_{stat} = \frac{496 - 500}{\frac{8}{\sqrt{15}}} = \frac{-4}{2.066} \approx -1.94 $$

**Step 3: Determine Critical Value & Decision**
*   $\alpha = 0.01$, two-tailed. $\alpha/2 = 0.005$.
*   From t-table, $df=14, t_{crit} = \pm 2.977$.
*   Since $-2.977 < -1.94 < 2.977$, it does not fall in the rejection regions.
*   **Conclusion:** Fail to reject $H_0$. No significant evidence the machine is out of calibration.

### Example 3: Left-Tailed Z-Test for Proportion
A politician claims that *less than* 30% of the population opposes a new policy. In a sample of 500 people, 135 oppose the policy. Test the claim at $\alpha = 0.05$.

**Step 1: State Hypotheses**
*   $H_0: p \ge 0.30$
*   $H_1: p < 0.30$ (Claim, left-tailed)

**Step 2: Calculate Test Statistic**
*   $\hat{p} = \frac{135}{500} = 0.27, p_0 = 0.30, n = 500$
$$ Z_{stat} = \frac{0.27 - 0.30}{\sqrt{\frac{0.30(0.70)}{500}}} = \frac{-0.03}{\sqrt{0.00042}} = \frac{-0.03}{0.0205} \approx -1.46 $$

**Step 3: P-Value Approach & Decision**
*   $p\text{-value} = P(Z < -1.46) = 0.0721$
*   Since $0.0721 > 0.05 (\alpha)$, we **Fail to reject $H_0$**.
*   **Conclusion:** Not enough evidence to say less than 30% oppose it.

### Example 4: Calculating Type I Error ($\alpha$)
Given a test where $H_0: \mu = 50$ and we reject $H_0$ if our sample mean $\bar{X} > 52$. We have $n=36, \sigma = 6$. What is the probability of a Type I error?

**Step 1: Define Type I Error**
Type I Error = Rejecting $H_0$ given $H_0$ is true.
$\alpha = P(\bar{X} > 52 \mid \mu = 50)$

**Step 2: Standardize to Z**
$$ Z = \frac{52 - 50}{\frac{6}{\sqrt{36}}} = \frac{2}{1} = 2.0 $$

**Step 3: Find Probability**
$$ \alpha = P(Z > 2.0) = 1 - 0.9772 = 0.0228 $$

### Example 5: Calculating Type II Error ($\beta$)
Following Example 4, what is the probability of a Type II error ($\beta$) if the *true* population mean is actually $\mu_A = 53$?

**Step 1: Define Type II Error**
Type II Error = Failing to reject $H_0$ given $H_1$ is true.
We fail to reject if $\bar{X} \le 52$.
$\beta = P(\bar{X} \le 52 \mid \mu = 53)$

**Step 2: Standardize using the TRUE mean ($\mu_A = 53$)**
$$ Z = \frac{52 - 53}{\frac{6}{\sqrt{36}}} = \frac{-1}{1} = -1.0 $$

**Step 3: Find Probability**
$$ \beta = P(Z \le -1.0) = 0.1587 $$
*(The Power of the test against $\mu_A = 53$ is $1 - \beta = 0.8413$)*

### Example 6: The Connection between CI and Two-Tailed Tests
You have a 95% confidence interval for $\mu$ given as $[12.5, 18.2]$. If you run a two-tailed hypothesis test $H_0: \mu = 19$ vs $H_1: \mu \ne 19$ at $\alpha = 0.05$, what will the conclusion be?

**Step 1: Analyze the Rule**
A two-tailed hypothesis test at significance level $\alpha$ will reject $H_0$ if the hypothesized value $\mu_0$ is *outside* the corresponding $(1-\alpha)\times 100\%$ confidence interval.

**Step 2: Check the Value**
Is 19 inside the interval $[12.5, 18.2]$? No.

**Step 3: Conclusion**
Since 19 is outside the 95% confidence interval, we will **Reject $H_0$** at the 5% significance level.

---

### Example 7: The "P-value Doubling" Trap in Two-Tailed Tests (Gotcha Moment)
A researcher wants to test if a new tutoring method changes exam scores (previously known mean $\mu = 70$, $\sigma = 12$). A sample of 36 students scores an average of 73.5. Calculate the p-value for this test. Is it significant at $\alpha = 0.05$?

#### Gotcha Section Analysis
The key word here is **changes** (not "increases" or "decreases"). This means it is a **two-tailed test** ($H_0: \mu = 70$, $H_1: \mu \ne 70$). A very common mistake is calculating the area in just *one* tail and calling it the p-value. For a two-tailed test, the p-value is the area in BOTH tails combined!

**Step 1: Calculate the Test Statistic**
$$ Z_{stat} = \frac{73.5 - 70}{\frac{12}{\sqrt{36}}} = \frac{3.5}{2} = 1.75 $$

**Step 2: Calculate the Area in One Tail**
Since $Z = 1.75$ is positive, we look at the right tail.
$P(Z > 1.75) = 1 - P(Z \le 1.75) = 1 - 0.9599 = 0.0401$

**Step 3: Calculate the TRUE P-value (The Gotcha)**
Because it is a two-tailed test, we must account for the possibility of extreme results in the other direction.
$$ p\text{-value} = 2 \times P(Z > |Z_{stat}|) $$
$$ p\text{-value} = 2 \times 0.0401 = 0.0802 $$

**Step 4: Decision**
If a student forgot to multiply by 2, they would compare $0.0401 < 0.05$ and incorrectly Reject $H_0$.
Correct comparison: $0.0802 > 0.05$. Therefore, we **Fail to reject $H_0$**. The change is not statistically significant.

---

### Example 8: $H_0$ Phrasing and the Status Quo Trap (Gotcha Moment)
An environmental agency asserts that a local river is polluted, claiming that the average concentration of a toxin is *greater than* the safe limit of 5 ppm. To test this, you take 50 water samples, find a mean of 5.2 ppm, and standard deviation of 0.8 ppm. Formulate the hypotheses and explain what a Type I error means in this specific physical context.

#### Gotcha Section Analysis
There is a massive trap in how the claim is presented. Students often mistakenly put the *researcher's claim* into $H_0$.
**Rule:** $H_0$ MUST contain the equality ($=$ or $\le$ or $\ge$). $H_1$ contains the strictly greater than or less than sign ($>$ or $<$). If the claim is "greater than", the claim itself is $H_1$.
Another trap is contextualizing the error. It's not enough to say "rejecting $H_0$ when true"; you must map it to the physical reality of the river.

**Step 1: Formulate Hypotheses**
*   The claim is $\mu > 5$. This does not contain equality, so it is $H_1$.
*   $H_0: \mu \le 5$ (The river is safe / status quo)
*   $H_1: \mu > 5$ (The river is polluted / agency's claim)

**Step 2: Define Type I Error in Context**
*   **Statistical Definition:** Rejecting $H_0$ when $H_0$ is true.
*   **Physical Translation:** We conclude that $H_1$ is true (the river is polluted) when in reality $H_0$ is true (the river is perfectly safe).
*   **Consequence:** The town might spend millions of dollars cleaning up a river that is not actually polluted, causing a massive waste of resources.

**Step 3: Define Type II Error in Context (Bonus Analysis)**
*   **Statistical Definition:** Failing to reject $H_0$ when $H_1$ is true.
*   **Physical Translation:** We conclude the river is safe ($H_0$), when in reality it IS polluted ($H_1$).
*   **Consequence:** People drink poisoned water, causing a massive public health crisis.
*(In this scenario, a Type II error is far more dangerous to human life than a Type I error, which is why the agency might push for a higher $\alpha$ level to reduce $\beta$!)*


---

<!-- Source: Phase_7_R_Programming_Commands/phase_7_1_descriptive_stats.md -->
# Phase 7: R Programming Commands - Descriptive Stats

## 1. Theoretical Foundation

R provides a powerful and streamlined suite of functions to calculate descriptive statistics directly from data vectors. Understanding how to use these base R functions is critical for quickly analyzing datasets without manual calculation.

### 1.1 Central Tendency and Dispersion

Given a numeric vector `x`, you can calculate its fundamental descriptive statistics using the following built-in functions:

*   **Mean:** Calculates the arithmetic average ($\bar{X}$).
    `mean(x)`
*   **Median:** Finds the middle value when the data is ordered.
    `median(x)`
*   **Variance:** Calculates the **sample** variance ($s^2$).
    `var(x)`
*   **Standard Deviation:** Calculates the **sample** standard deviation ($s$).
    `sd(x)`

### 1.2 Quantiles and Percentiles

To find specific percentiles or quartiles, R uses the `quantile()` function. It takes the data vector and a vector of probabilities `probs` indicating the desired percentiles.

*   **Syntax:** `quantile(x, probs = c(...))`
*   **Example for Quartiles:** To find $Q_1, Q_2$ (Median), and $Q_3$, use `probs = c(0.25, 0.5, 0.75)`.

### 1.3 Mode in R

Unlike the mean and median, R does **not** have a built-in function to find the mode (the most frequently occurring value). A common implementation requires combining the `table()` function (which creates a frequency count) and the `max()` function.

*   **Implementation pattern:**
    ```R
    get_mode <- function(v) {
      uniqv <- unique(v)
      uniqv[which.max(tabulate(match(v, uniqv)))]
    }
    ```
    Alternatively, for a quick console check:
    ```R
    freq_table <- table(x)
    names(freq_table)[freq_table == max(freq_table)]
    ```

---

## 2. Step-by-Step Examples

### Example 1: Basic Mean and Median
Calculate the mean and median for the dataset: 12, 15, 18, 20, 22, 25.

**Step 1: Create the vector in R**
```R
data_vec <- c(12, 15, 18, 20, 22, 25)
```

**Step 2: Calculate Mean**
```R
avg_val <- mean(data_vec)
# Result: 18.66667
```

**Step 3: Calculate Median**
```R
med_val <- median(data_vec)
# Result: 19
```

### Example 2: Variance and Standard Deviation
Find the sample variance and standard deviation for: 4, 8, 6, 5, 3, 2, 8, 9, 2, 5.

**Step 1: Create the vector**
```R
x <- c(4, 8, 6, 5, 3, 2, 8, 9, 2, 5)
```

**Step 2: Calculate Variance ($s^2$)**
```R
variance_val <- var(x)
# Result: 6.4
```

**Step 3: Calculate Standard Deviation ($s$)**
```R
sd_val <- sd(x)
# Result: 2.529822
```
*(Notice that `sd(x)` is precisely equal to `sqrt(var(x))`)*.

### Example 3: Extracting Specific Quartiles
From a random sample of 100 observations generated from a normal distribution, extract the 25th, 50th, and 75th percentiles.

**Step 1: Generate Data**
```R
set.seed(123)
obs <- rnorm(100, mean = 50, sd = 10)
```

**Step 2: Use quantile function**
```R
target_probs <- c(0.25, 0.5, 0.75)
quartiles <- quantile(obs, probs = target_probs)
print(quartiles)
```
**Output:**
```R
      25%       50%       75% 
45.06014  50.61868  56.55173 
```

### Example 4: Finding the Interquartile Range (IQR)
Using the `quantile()` function, compute the IQR for `x <- c(10, 20, 30, 40, 50, 60, 70, 80, 90)`.

**Step 1: Calculate $Q_1$ and $Q_3$**
```R
x <- c(10, 20, 30, 40, 50, 60, 70, 80, 90)
q_vals <- quantile(x, probs = c(0.25, 0.75))
```

**Step 2: Subtract $Q_1$ from $Q_3$**
```R
iqr_val <- q_vals[2] - q_vals[1]
# Note: R also has a built-in IQR() function that does exactly this: IQR(x)
```

### Example 5: Creating a Mode Function
You are given a categorical numeric vector `votes <- c(1, 2, 2, 3, 1, 2, 4, 5, 2, 1)`. Find the mode.

**Step 1: Create frequency table**
```R
votes <- c(1, 2, 2, 3, 1, 2, 4, 5, 2, 1)
freq <- table(votes)
print(freq)
# votes
# 1 2 3 4 5 
# 3 4 1 1 1 
```

**Step 2: Extract the mode**
```R
# Find the maximum frequency
max_freq <- max(freq)

# Identify the name (the actual value) that corresponds to max frequency
mode_val <- names(freq)[freq == max_freq]
print(mode_val) 
# Result: "2"
```

### Example 6: Coefficient of Variation (CV)
Calculate the Coefficient of Variation ($CV = \frac{SD}{Mean}$) for a given sample `y <- c(100, 110, 95, 105, 120, 90)`.

**Step 1: Assign variable**
```R
y <- c(100, 110, 95, 105, 120, 90)
```

**Step 2: Calculate Mean and SD**
```R
m_y <- mean(y)
sd_y <- sd(y)
```

**Step 3: Compute CV**
```R
cv_y <- sd_y / m_y
# Result: 0.1045261 (or roughly 10.45%)
```

---

### Example 7: The "NA" Trap (Gotcha Moment)
You receive a dataset of student test scores, but one student was absent, resulting in an `NA` (Not Available) value in the data vector: `scores <- c(85, 90, 78, NA, 92, 88)`. Calculate the mean.

#### Gotcha Section Analysis
A very common trap in R is forgetting how statistical functions handle missing values. By default, if there is even a single `NA` in a vector, functions like `mean()`, `median()`, `sd()`, and `var()` will return `NA` for the entire dataset, because mathematically, the average of a known set plus an unknown value is unknown.

**Step 1: The Incorrect Approach**
```R
scores <- c(85, 90, 78, NA, 92, 88)
mean(scores)
# Result: NA
```

**Step 2: The Correct Approach (Using na.rm)**
You must explicitly tell R to remove the `NA` values before performing the calculation by using the `na.rm = TRUE` argument.
```R
mean(scores, na.rm = TRUE)
# Result: 86.6
```
*(Always check your datasets for NAs or preemptively use `na.rm = TRUE` during exploratory analysis!)*

---

### Example 8: Population vs. Sample Variance Trap (Gotcha Moment)
A problem explicitly asks you to calculate the **population** variance ($\sigma^2$) for the dataset `population_ages <- c(25, 30, 35, 40, 45)`. You use the `var()` function.

#### Gotcha Section Analysis
The R `var()` and `sd()` functions are strictly designed for **sample** statistics. They divide the sum of squared differences by $n - 1$ (degrees of freedom). If you are working with an entire population, dividing by $n - 1$ is statistically incorrect; you must divide by $n$. R does not have a built-in `pop.var()` function.

**Step 1: The Incorrect Approach (Sample Variance)**
```R
pop_ages <- c(25, 30, 35, 40, 45)
var(pop_ages)
# R computes: sum((x - mean)^2) / 4
# Result: 62.5
```

**Step 2: The Correct Approach (Manual Adjustment)**
To get the population variance, you must either calculate it manually, or multiply the sample variance by $\frac{n-1}{n}$.

*Manual Calculation:*
```R
n <- length(pop_ages)
mu <- mean(pop_ages)
pop_var_manual <- sum((pop_ages - mu)^2) / n
# Result: 50
```

*Adjustment Method:*
```R
n <- length(pop_ages)
pop_var_adjusted <- var(pop_ages) * ((n - 1) / n)
# Result: 62.5 * (4 / 5) = 50
```
*(Whenever a question specifies "Population Variance" or "Population Standard Deviation", never use `var()` or `sd()` directly without making this adjustment!)*


---

<!-- Source: Phase_7_R_Programming_Commands/phase_7_2_binomial_distribution.md -->
# Phase 7: R Programming Commands - Binomial Distribution

## 1. Theoretical Foundation

The binomial distribution measures the number of successes in a sequence of $n$ independent experiments (trials), each asking a yes-no question, with a fixed probability of success $p$.

R handles distributions systematically using a consistent prefix notation. For the Binomial distribution, the root is `binom`.
*   **`d` prefix (Density/Mass):** Returns the exact probability $P(X = k)$.
*   **`p` prefix (Probability/Cumulative):** Returns the cumulative probability $P(X \le k)$.
*   **`q` prefix (Quantile):** The inverse of `pbinom`. Returns the value $k$ for a given cumulative probability.
*   **`r` prefix (Random):** Generates random observations from the distribution.

### 1.1 Exact Probabilities: `dbinom()`
Calculates the Probability Mass Function (PMF), $P(X = k)$.
*   **Syntax:** `dbinom(x = k, size = n, prob = p)`
*   **Arguments:**
    *   `x`: The target number of successes ($k$). Can also be a vector (e.g., `0:5`).
    *   `size`: The total number of trials ($n$).
    *   `prob`: The probability of success on each trial ($p$).

### 1.2 Cumulative Probabilities: `pbinom()`
Calculates the Cumulative Distribution Function (CDF), $P(X \le k)$.
*   **Syntax:** `pbinom(q = k, size = n, prob = p, lower.tail = TRUE)`
*   **Arguments:**
    *   `q`: The quantile or upper bound of successes ($k$).
    *   `lower.tail`: If `TRUE` (default), calculates $P(X \le k)$. If `FALSE`, calculates $P(X > k)$.

---

## 2. Step-by-Step Examples

### Example 1: Exact Probability ($P(X = k)$)
A biased coin has a 60% chance of landing on Heads. If you flip it 10 times, what is the exact probability of getting exactly 7 Heads?

**Step 1: Identify Parameters**
*   $k = 7$ (Target successes)
*   $n = 10$ (Total trials)
*   $p = 0.60$ (Probability of success)

**Step 2: Use `dbinom`**
```R
ans <- dbinom(x = 7, size = 10, prob = 0.6)
# Result: 0.2149908
```

### Example 2: Cumulative Probability ($P(X \le k)$)
Using the same coin ($n=10, p=0.6$), what is the probability of getting 4 or fewer Heads?

**Step 1: Identify Parameters**
We want $P(X \le 4)$.

**Step 2: Use `pbinom`**
```R
ans <- pbinom(q = 4, size = 10, prob = 0.6)
# Result: 0.1662386
```

### Example 3: Probability of a Range ($P(a \le X \le b)$)
A pharmaceutical drug has an 80% success rate. If given to 20 patients, what is the probability that between 12 and 16 patients (inclusive) recover?

**Step 1: Formulate the Math**
We want $P(12 \le X \le 16)$.
Mathematically, this is $P(X \le 16) - P(X \le 11)$. *(Notice we subtract $P(X \le 11)$, not 12, so we don't accidentally remove 12 from the interval).*

**Step 2: Use `pbinom` difference**
```R
upper_bound <- pbinom(16, size = 20, prob = 0.8)
lower_bound <- pbinom(11, size = 20, prob = 0.8)
ans <- upper_bound - lower_bound
# Result: 0.5785692
```

### Example 4: Range Probability (Alternative method)
Solve Example 3 using `dbinom` and `sum`.

**Step 1: Generate a vector of target successes**
We want exactly 12, 13, 14, 15, and 16 successes.
```R
targets <- 12:16
```

**Step 2: Calculate all exact probabilities and sum them**
```R
probs <- dbinom(targets, size = 20, prob = 0.8)
ans <- sum(probs)
# Result: 0.5785692
```
*(This is often easier to read and less prone to the "off-by-one" error seen in cumulative subtraction).*

### Example 5: Generating Random Binomial Variables
Simulate flipping a fair coin 5 times, and record the number of heads. Repeat this experiment 100 times.

**Step 1: Use `rbinom`**
*   `n = 100` (Number of experiments)
*   `size = 5` (Trials per experiment)
*   `prob = 0.5`
```R
simulations <- rbinom(n = 100, size = 5, prob = 0.5)
```
*(This will output a vector of 100 numbers, where each number is between 0 and 5, representing the number of heads in that specific experiment).*

---

### Example 6: Finding the Minimum Threshold with `qbinom()`
A quality control manager uses $X \sim B(20, 0.15)$ to model the number of defective units in a batch. What is the smallest number $k$ such that the cumulative probability $P(X \leq k) \geq 0.90$? In other words, what is the 90th percentile of the distribution?

**Step 1: Identify Parameters**
*   $n = 20$, $p = 0.15$, target cumulative probability $= 0.90$.

**Step 2: Use `qbinom`**
`qbinom()` is the inverse of `pbinom`. Given a cumulative probability, it returns the smallest integer $k$ satisfying $P(X \leq k) \geq p$.
```R
threshold <- qbinom(p = 0.90, size = 20, prob = 0.15)
# Result: 5
```

**Step 3: Verify the result**
```R
pbinom(4, size = 20, prob = 0.15)  # P(X <= 4)
# Result: 0.8298 (less than 0.90, so k=4 is insufficient)
pbinom(5, size = 20, prob = 0.15)  # P(X <= 5)
# Result: 0.9327 (>= 0.90, so k=5 is the answer)
```
The manager can be 90% confident that no more than **5** units in a batch of 20 will be defective.

---

### Example 7: The "Strictly Less Than" Trap (Gotcha Moment)
A multiple-choice test has 50 questions, each with 4 options (meaning the chance of guessing correctly is 25%). What is the probability of a student guessing *strictly less than* 15 questions correctly? 

#### Gotcha Section Analysis
Students often see "less than 15" and instinctively type `pbinom(15, size=50, prob=0.25)`. However, `pbinom(q)` calculates $P(X \le q)$, meaning it includes 15! Because the binomial distribution is discrete, "strictly less than 15" ($X < 15$) is mathematically equivalent to "less than or equal to 14" ($X \le 14$).

**Step 1: The Incorrect Approach**
```R
wrong_ans <- pbinom(15, size = 50, prob = 0.25)
# This calculates P(X <= 15)
```

**Step 2: The Correct Approach**
Adjust the quantile down by 1.
```R
correct_ans <- pbinom(14, size = 50, prob = 0.25)
# This calculates P(X <= 14), which is P(X < 15).
```

---

### Example 8: The "Greater Than" and `lower.tail` Trap (Gotcha Moment)
A factory produces light bulbs with a 5% defect rate. In a batch of 200 bulbs, what is the probability of finding *at least* 15 defective bulbs?

#### Gotcha Section Analysis
"At least 15" means $P(X \ge 15)$. 
There are two common traps here:
1. **Using Complement Rule Incorrectly:** If you do `1 - pbinom(15, ...)`, you are calculating $1 - P(X \le 15) = P(X > 15) = P(X \ge 16)$. You accidentally excluded 15 from your final answer!
2. **Using `lower.tail = FALSE` Incorrectly:** In R, `lower.tail = FALSE` strictly calculates $P(X > q)$. It does NOT calculate $P(X \ge q)$. 

**Step 1: Formulate the correct Complement**
$P(X \ge 15) = 1 - P(X \le 14)$.
```R
ans_complement <- 1 - pbinom(14, size = 200, prob = 0.05)
```

**Step 2: The `lower.tail` Method**
If you want to use the built-in R feature to avoid subtracting from 1, you must pass 14 as the quantile, because `lower.tail = FALSE` computes $P(X > q)$. So, $P(X > 14)$ is equivalent to $P(X \ge 15)$.
```R
ans_lower_tail <- pbinom(14, size = 200, prob = 0.05, lower.tail = FALSE)
```
*(Both `ans_complement` and `ans_lower_tail` will yield the correct result. Never pass 15 into `pbinom` for an "at least 15" question!)*


---

<!-- Source: Phase_7_R_Programming_Commands/phase_7_3_normal_distribution.md -->
# Phase 7: R Programming Commands - Normal Distribution

## 1. Theoretical Foundation

The Normal (Gaussian) distribution is continuous and completely defined by its mean ($\mu$) and standard deviation ($\sigma$). R provides a similar family of functions for the normal distribution as it does for the binomial, using the root `norm`.

Unlike the discrete binomial distribution, the probability of an exact, specific value in a continuous normal distribution is strictly zero ($P(X = x) = 0$). Therefore, we are almost exclusively concerned with cumulative probabilities (ranges) or inverse probabilities.

### 1.1 Cumulative Probabilities: `pnorm()`
Calculates the area under the normal curve up to a given value, $P(X \le x)$.
*   **Syntax:** `pnorm(q = x, mean = \mu, sd = \sigma, lower.tail = TRUE)`
*   **Arguments:**
    *   `q`: The value you are checking ($x$).
    *   `mean`: The population mean ($\mu$). Default is 0.
    *   `sd`: The population standard deviation ($\sigma$). Default is 1.

*(Note: Because the distribution is continuous, $P(X \le x)$ is exactly equal to $P(X < x)$. You do not need to adjust the boundaries like you do in the binomial distribution).*

### 1.2 Inverse Probabilities (Quantiles): `qnorm()`
Finds the value $x$ corresponding to a specific cumulative probability $p$. This answers the question: "What value separates the bottom $p\%$ of the data from the rest?"
*   **Syntax:** `qnorm(p = prob, mean = \mu, sd = \sigma)`

### 1.3 Other Normal Functions
*   **`rnorm(n, mean, sd)`:** Generates $n$ random numbers from the specified normal distribution.
*   **`dnorm(x, mean, sd)`:** Returns the height of the probability density function (PDF) curve at $x$. This does **not** give a probability; it is mostly used for drawing the bell curve.

---

## 2. Step-by-Step Examples

### Example 1: Basic Cumulative Probability ($P(X < x)$)
Human heights are normally distributed with $\mu = 170$ cm and $\sigma = 10$ cm. What is the probability that a randomly selected person is shorter than 185 cm?

**Step 1: Identify Parameters**
*   $q = 185$
*   $\mu = 170$
*   $\sigma = 10$

**Step 2: Use `pnorm`**
```R
ans <- pnorm(q = 185, mean = 170, sd = 10)
# Result: 0.9331928
```

### Example 2: Right-Tail Probability ($P(X > x)$)
Using the same height distribution ($\mu = 170, \sigma = 10$), what is the probability a person is taller than 190 cm?

**Step 1: Formulate the Problem**
We want $P(X > 190)$.

**Step 2: Calculate in R**
You can use the complement rule or `lower.tail = FALSE`.
```R
# Method 1 (Complement)
ans_comp <- 1 - pnorm(190, mean = 170, sd = 10)

# Method 2 (lower.tail)
ans_tail <- pnorm(190, mean = 170, sd = 10, lower.tail = FALSE)
# Result: 0.02275013
```

### Example 3: Probability Between Two Values ($P(a < X < b)$)
What is the probability a person's height is between 160 cm and 180 cm?

**Step 1: Formulate the Math**
$P(160 < X < 180) = P(X < 180) - P(X < 160)$.

**Step 2: Use `pnorm` subtraction**
```R
ans <- pnorm(180, mean = 170, sd = 10) - pnorm(160, mean = 170, sd = 10)
# Result: 0.6826895
```
*(Notice this matches the empirical rule: approximately 68% of data falls within 1 standard deviation of the mean).*

### Example 4: Using the Standard Normal Distribution (Z)
If you have a Z-score of $Z = 1.96$, what is the cumulative probability?

**Step 1: Understand Default Parameters**
For the standard normal distribution, $\mu = 0$ and $\sigma = 1$. R uses these as defaults, so you don't need to explicitly declare them.

**Step 2: Use `pnorm`**
```R
ans <- pnorm(1.96)
# Result: 0.9750021
```

### Example 5: Finding a Percentile with `qnorm()`
Scores on a test are normally distributed with $\mu = 500$ and $\sigma = 100$. What score marks the 90th percentile?

**Step 1: Identify Parameters**
*   We want the bottom 90%, so probability $p = 0.90$.

**Step 2: Use `qnorm`**
```R
ans <- qnorm(p = 0.90, mean = 500, sd = 100)
# Result: 628.1552
```

### Example 6: Generating Random Data
Simulate the grades of a classroom of 30 students, where the class average is 75 with a standard deviation of 8.

**Step 1: Use `rnorm`**
```R
grades <- rnorm(n = 30, mean = 75, sd = 8)
```
*(This returns a vector of 30 randomized grades based on the distribution).*

---

### Example 7: The "Variance vs Standard Deviation" Trap (Gotcha Moment)
A problem states: "The weights of boxes are normally distributed, $X \sim N(50, 16)$. Find $P(X < 55)$."

#### Gotcha Section Analysis
The standard mathematical notation for a normal distribution is $X \sim N(\mu, \sigma^2)$, where the second parameter is the **Variance**. However, the R function `pnorm(q, mean, sd)` strictly requires the **Standard Deviation**. A very common mistake is plugging the number 16 directly into the `sd` argument.

**Step 1: The Incorrect Approach**
```R
wrong_ans <- pnorm(55, mean = 50, sd = 16)
# This calculates based on standard deviation = 16.
```

**Step 2: The Correct Approach**
You must extract the standard deviation by taking the square root of the variance given in the problem statement.
$\sigma = \sqrt{16} = 4$.
```R
correct_ans <- pnorm(55, mean = 50, sd = 4)
# Result: 0.8943502
```

---

### Example 8: The "Top X%" Quantile Trap (Gotcha Moment)
A university accepts only the top 5% of applicants based on an entrance exam ($\mu = 100, \sigma = 15$). What is the minimum score required to be accepted?

#### Gotcha Section Analysis
The phrase "top 5%" naturally leads students to type `qnorm(0.05, ...)`. However, `qnorm(p)` expects the cumulative area from the *left* tail. The "top 5%" corresponds to the upper tail. If you put 0.05 into `qnorm`, you will find the score separating the *bottom* 5% (the worst scores!).

**Step 1: The Incorrect Approach**
```R
wrong_score <- qnorm(0.05, mean = 100, sd = 15)
# Result: 75.32 (This is a terrible score!)
```

**Step 2: The Correct Approach (Using Complement Probability)**
If you are in the top 5%, you scored higher than 95% of people. Therefore, the area to the left is 0.95.
```R
correct_score_1 <- qnorm(0.95, mean = 100, sd = 15)
# Result: 124.6728
```

**Step 3: The Alternative Correct Approach (Using lower.tail)**
You can use the `lower.tail = FALSE` argument to tell `qnorm` you are providing the upper area.
```R
correct_score_2 <- qnorm(0.05, mean = 100, sd = 15, lower.tail = FALSE)
# Result: 124.6728
```
*(Always draw a quick sketch of the bell curve to visually verify if the answer makes logical sense!)*


---

