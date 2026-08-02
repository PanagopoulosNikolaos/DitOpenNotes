# Phase 1.5 (Time): Core Formulas Summary (Grouped Time Data)

This file serves as a quick-reference guide for the mathematical foundation of Descriptive Statistics when dealing with **Grouped Time-Based Data**. All formulas are identical to the general case, but the variables now represent time measurements, and special attention is given to **unit consistency and the $c^2$ scaling rule**.

---

## 1. Data Organization (Time Context)

*   **Class Mark ($t_i$):**
    $$t_i = \frac{L_{inf} + L_{sup}}{2}$$
    *(Midpoint of a time interval, e.g., the midpoint of $[10, 20)\text{ ms}$ is $15\text{ ms}$.)*

*   **Relative Frequency ($h_i$):**
    $$h_i = \frac{f_i}{n}$$
    *(Unit-independent: a proportion, not a time value.)*

*   **Sturges' Rule (Number of Classes $k$):**
    $$k = 1 + 3.322 \cdot \log_{10}(n)$$
    *(Unit-independent: depends only on $n$, not on the time unit.)*

*   **Class Width ($w$):**
    $$w = \frac{R}{k} = \frac{t_{max} - t_{min}}{k}$$
    *(In the chosen time unit. Always round up.)*

---

## 2. Measures of Central Tendency (Time Context)

*   **Mean ($\bar{t}$):**
    $$\bar{t} = \frac{\sum f_i \cdot t_i}{n}$$
    *(In the same time unit as $t_i$.)*

*   **Median ($M_e$):**
    $$M_e = L + \left( \frac{\frac{n}{2} - F_{i-1}}{f_i} \right) \cdot w$$
    *(In the same time unit as $L$ and $w$.)*

*   **Mode ($M_o$):**
    $$M_o = L + \left( \frac{f_i - f_{i-1}}{(f_i - f_{i-1}) + (f_i - f_{i+1})} \right) \cdot w$$
    *(In the same time unit as $L$ and $w$.)*

> **Cyclic time warning:** The mean, median, and mode formulas above are valid only for **linear time data** (durations, timestamps relative to an epoch). For cyclic clock time, use the circular mean instead of the arithmetic mean.

---

## 3. Measures of Position (Quantiles for Time Data)

*   **General Percentile ($P_k$):**
    $$P_k = L + \left( \frac{\frac{k \cdot n}{100} - F_{i-1}}{f_i} \right) \cdot w$$
    *(In the same time unit as $L$ and $w$.)*

*   **Quartiles:** Use $k=25$ for $Q_1$ (p25), $k=50$ for $Q_2$ (p50/median), and $k=75$ for $Q_3$ (p75).

> **SLA relevance:** $P_{95}$ and $P_{99}$ are the most commonly reported latency percentiles in Service Level Agreements. They tell you the worst-case experience for the slowest 5% and 1% of requests, respectively.

---

## 4. Measures of Dispersion (Time Context)

*   **Sample Variance ($s^2$):**
    $$s^2 = \frac{\sum f_i \cdot (t_i - \bar{t})^2}{n - 1}$$
    *(In **squared time units**, e.g., $\text{ms}^2$, $\text{s}^2$.)*

*   **Shortcut Variance Formula:**
    $$s^2 = \frac{\sum f_i \cdot t_i^2 - \frac{(\sum f_i \cdot t_i)^2}{n}}{n - 1}$$
    *(In **squared time units**.)*

*   **Sample Standard Deviation ($s$):**
    $$s = \sqrt{s^2}$$
    *(In the **original time unit**, e.g., ms, s.)*

*   **Range ($R$):**
    $$R = t_{max} - t_{min}$$
    *(In the original time unit.)*

*   **Coefficient of Variation ($CV$):**
    $$CV = \frac{s}{\bar{t}} \cdot 100\%$$
    *(**Dimensionless** -- the time unit cancels out.)*

---

## 5. The $c^2$ Rule: Unit Conversion Scaling

When converting time data by a factor $c$ (e.g., $c = 1000$ for seconds to milliseconds):

| Statistic | Scaling | Formula |
| :--- | :--- | :--- |
| Mean $\bar{t}$ | Scales by $c$ | $\bar{t}_{\text{new}} = c \cdot \bar{t}_{\text{old}}$ |
| Median $M_e$ | Scales by $c$ | $M_{e,\text{new}} = c \cdot M_{e,\text{old}}$ |
| Mode $M_o$ | Scales by $c$ | $M_{o,\text{new}} = c \cdot M_{o,\text{old}}$ |
| Range $R$ | Scales by $c$ | $R_{\text{new}} = c \cdot R_{\text{old}}$ |
| Standard Deviation $s$ | Scales by $c$ | $s_{\text{new}} = c \cdot s_{\text{old}}$ |
| Variance $s^2$ | Scales by $c^2$ | $s^2_{\text{new}} = c^2 \cdot s^2_{\text{old}}$ |
| $CV$ | **No change** | $CV_{\text{new}} = CV_{\text{old}}$ |
| Percentiles $P_k$ | Scales by $c$ | $P_{k,\text{new}} = c \cdot P_{k,\text{old}}$ |
| $IQR$ | Scales by $c$ | $IQR_{\text{new}} = c \cdot IQR_{\text{old}}$ |

### Common Conversion Factors

| From | To | $c$ | $c^2$ |
| :--- | :--- | :--- | :--- |
| seconds (s) | milliseconds (ms) | $10^3$ | $10^6$ |
| seconds (s) | microseconds ($\mu$s) | $10^6$ | $10^{12}$ |
| seconds (s) | nanoseconds (ns) | $10^9$ | $10^{18}$ |
| milliseconds (ms) | seconds (s) | $10^{-3}$ | $10^{-6}$ |
| milliseconds (ms) | microseconds ($\mu$s) | $10^3$ | $10^6$ |
| nanoseconds (ns) | milliseconds (ms) | $10^{-6}$ | $10^{-12}$ |
| nanoseconds (ns) | seconds (s) | $10^{-9}$ | $10^{-18}$ |

---

## 6. Time-Specific Gotchas Summary

| Gotcha | Impact | Fix |
| :--- | :--- | :--- |
| Floating-point precision with large epoch ns timestamps | Variance computation yields 0 or negative due to catastrophic cancellation | Center data: subtract $t_{\min}$ before computing |
| Cyclic clock time (23:59 vs 00:01) | Mean and quantiles are meaningless on raw clock values | Use circular mean; convert to linear durations from a reference |
| Mixed unit prefixes in raw data | A single $1000\text{ ms}$ read as $1000\text{ s}$ destroys the distribution | Normalize all values to a single unit before any computation |
| Variance in squared units | Reporting $25\text{ ms}^2$ as "spread of 25 ms" is wrong | Standard deviation $s = \sqrt{s^2}$ gives spread in original units |
| $c^2$ scaling under unit conversion | Forgetting that variance scales by $c^2$, not $c$ | Always apply $c^2$ to variance, $c$ to standard deviation |

---

## Exam Tip: Unit Consistency (Time Context)

Always remember that **Variance** is in squared time units (e.g., $\text{ms}^2$), while **Mean**, **Median**, **Mode**, **Standard Deviation**, **Range**, **Percentiles**, and **IQR** are in the original time units (e.g., ms). The **Coefficient of Variation** is dimensionless.

If an exam asks for "a measure of spread in the original time units," they are asking for the **Standard Deviation** or **Range** -- never the Variance.

If an exam involves unit conversion, remember:
*   Linear measures (mean, median, SD, percentiles) scale by $c$.
*   Variance scales by $c^2$.
*   $CV$ does not change.