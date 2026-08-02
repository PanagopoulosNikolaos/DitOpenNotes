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
