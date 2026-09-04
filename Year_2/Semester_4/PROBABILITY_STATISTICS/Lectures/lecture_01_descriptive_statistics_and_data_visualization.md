# Lecture 01: Descriptive Statistics and Data Visualization

This lecture covers empirical data classification, frequency distribution tables, measures of central tendency (mean, median, mode), measures of dispersion (variance, standard deviation, IQR), and linear data transformations.

---

## 1. Classification of Data Types

Statistical variables represent characteristics observed across experimental populations:
- **Qualitative (Categorical):** Non-numerical properties.
  - *Nominal:* Labels without natural ordering (e.g., Blood type, Gender, Department).
  - *Ordinal:* Categories possessing meaningful intrinsic order (e.g., Academic grade: Excellent, Good, Pass).
- **Quantitative (Numerical):** Measured numerical quantities.
  - *Discrete:* Countable values resulting from counting processes (e.g., Number of network errors, Student count).
  - *Continuous:* Uncountable values over an interval resulting from measurement (e.g., Latency, Temperature, Salary).

---

## 2. Organization of Data: Frequency Distributions

For a dataset of $n$ observations grouped into $k$ distinct values or class intervals:

### 2.1 Frequency Definitions
- **Absolute Frequency ($f_i$):** Number of times value $x_i$ appears:
  $$\sum_{i=1}^{k} f_i = n$$
- **Relative Frequency ($h_i$):** Proportion of total data:
  $$h_i = \frac{f_i}{n}, \quad \sum_{i=1}^{k} h_i = 1.0$$
- **Cumulative Absolute Frequency ($F_i$):** Running sum of frequencies:
  $$F_i = \sum_{j=1}^{i} f_j$$
- **Cumulative Relative Frequency ($H_i$):** Running proportion:
  $$H_i = \sum_{j=1}^{i} h_j = \frac{F_i}{n}$$

---

## 3. Measures of Central Tendency

Measures of location summarize the central position of an empirical data distribution.

### 3.1 Arithmetic Mean ($\bar{x}$)
For raw ungrouped data:

$$
\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i
$$

For grouped frequency data with class midpoints $m_i$:

$$
\bar{x} = \frac{1}{n} \sum_{i=1}^{k} f_i \cdot m_i = \sum_{i=1}^{k} h_i \cdot m_i
$$

### 3.2 Median ($\tilde{x}$)
The value dividing an ordered dataset into two equal halves ($50\%$ below, $50\%$ above).
- For ordered sample $x_{(1)} \le x_{(2)} \le \dots \le x_{(n)}$:
  - If $n$ is odd: $\tilde{x} = x_{\left(\frac{n+1}{2}\right)}$
  - If $n$ is even: $\tilde{x} = \frac{x_{\left(\frac{n}{2}\right)} + x_{\left(\frac{n}{2} + 1\right)}}{2}$

### 3.3 Mode ($M_o$)
The most frequently occurring observation in the dataset. A distribution may be unimodal, bimodal, or multimodal.

---

## 4. Measures of Dispersion

Dispersion quantifies the degree of spread or variability of observations around their central tendency.

### 4.1 Sample Variance ($s^2$) and Standard Deviation ($s$)
Using Bessel's correction for unbiased sample variance:

$$
s^2 = \frac{1}{n - 1} \sum_{i=1}^{n} (x_i - \bar{x})^2 = \frac{1}{n - 1} \left( \sum_{i=1}^{n} x_i^2 - n \bar{x}^2 \right)
$$

The **Sample Standard Deviation** $s$ restores units to original dimensions:

$$
s = \sqrt{s^2}
$$

### 4.2 Interquartile Range (IQR)
Measures the spread of the middle $50\%$ of observations:

$$
\text{IQR} = Q_3 - Q_1
$$

Outlier detection threshold (Tukey's Fences): Observations outside $[Q_1 - 1.5 \cdot \text{IQR}, \ Q_3 + 1.5 \cdot \text{IQR}]$.

### 4.3 Coefficient of Variation ($CV$)
Dimensionless relative dispersion metric:

$$
CV = \frac{s}{\bar{x}} \times 100\%
$$

A dataset is considered homogeneous if $CV \le 10\%$.

---

## 5. Linear Transformations of Data

If a random sample $X$ undergoes a linear transformation $Y = aX + b$ (where $a, b \in \mathbb{R}$ are constants):
- **Mean Transformation:**
  $$\bar{y} = a\bar{x} + b$$
- **Variance Transformation:**
  $$s_y^2 = a^2 \cdot s_x^2$$
- **Standard Deviation Transformation:**
  $$s_y = |a| \cdot s_x$$

