# Assignment 01: Descriptive Statistical Analysis and Grouped Data Modeling

This assignment evaluates practical and mathematical understanding of descriptive statistics: grouped frequency tables, class midpoints, cumulative distributions, central tendency, sample dispersion, and linear transformations.

---

## 1. Problem Specification

A telecommunications laboratory measures the ping response latencies (in milliseconds) across $n = 50$ test packets transmitted over an experimental cellular link:

```text
28, 31, 34, 37, 40, 42, 43, 45, 46, 47,
48, 49, 50, 51, 52, 53, 54, 55, 56, 57,
58, 59, 60, 61, 62, 63, 64, 65, 66, 67,
68, 69, 70, 71, 72, 73, 74, 75, 76, 77,
78, 80, 82, 85, 87, 90, 92, 95, 98, 104
```

---

## 2. Analytical Tasks

### Task 1: Frequency Distribution Construction (25 Points)
Group the observations into $k = 5$ equal-width class intervals starting at lower boundary $25$ with class width $w = 16$ (intervals: $[25, 41), [41, 57), [57, 73), [73, 89), [89, 105)$).
Construct a complete frequency table containing:
1. Class interval $[L_i, U_i)$
2. Class midpoint $m_i = \frac{L_i + U_i}{2}$
3. Absolute frequency $f_i$
4. Relative frequency $h_i$
5. Cumulative absolute frequency $F_i$
6. Cumulative relative frequency $H_i$

### Task 2: Grouped Measures of Location and Spread (35 Points)
Using your grouped frequency table from Task 1:
1. Compute the grouped sample mean $\bar{x} = \sum_{i=1}^{k} h_i m_i$.
2. Compute the grouped sample variance $s^2 = \frac{1}{n-1} \sum_{i=1}^{k} f_i (m_i - \bar{x})^2$ and standard deviation $s$.
3. Compute the grouped median $\tilde{x}$ using the linear interpolation formula:
   $$\tilde{x} = L_m + \left( \frac{n/2 - F_{m-1}}{f_m} \right) \cdot w$$
4. Compute the Coefficient of Variation ($CV = \frac{s}{\bar{x}} \times 100\%$) and state whether the dataset exhibits homogeneity ($CV \le 10\%$).

### Task 3: Linear Transformation Analysis (20 Points)
Suppose an engineer applies an amplification filter to the raw data: $Y = 1.25 X - 10$.
1. Compute the new mean $\bar{y}$ without recalculating individual data values.
2. Compute the new standard deviation $s_y$.
3. Compute the new variance $s_y^2$.

### Task 4: R Script Implementation (20 Points)
Write an R script (`descriptive_analysis.R`) that imports the 50 observations, executes Tasks 1–3 programmatically, and generates a formatted histogram with an overlaid kernel density line.

---

## 3. Evaluation Rubric

| Criteria | Points |
|---|---|
| Frequency table calculation precision | 25 |
| Grouped mean, median, variance, and standard deviation derivations | 35 |
| Mathematical application of linear transformation theorems | 20 |
| Reproducible R script and clear visualization layout | 20 |

