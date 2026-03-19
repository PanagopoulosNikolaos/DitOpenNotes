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
