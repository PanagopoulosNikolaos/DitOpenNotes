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
