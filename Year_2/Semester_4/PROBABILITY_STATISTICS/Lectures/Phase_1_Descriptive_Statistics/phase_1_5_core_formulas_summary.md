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
