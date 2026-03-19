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
*   If **Mean > Median**, the distribution is **Positively Skewed**.
