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
