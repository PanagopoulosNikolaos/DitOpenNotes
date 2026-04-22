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
