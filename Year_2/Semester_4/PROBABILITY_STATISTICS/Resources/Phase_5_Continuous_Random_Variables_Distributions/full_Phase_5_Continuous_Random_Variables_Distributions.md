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


# Phase 5.3: Other Continuous Distributions

While the Normal distribution is the most famous, other continuous distributions like the **Uniform** and **Exponential** are essential for modeling specific real-world phenomena like wait times and equally likely outcomes over an interval.

## 1. Uniform Distribution ($X \sim U(a, b)$)
A distribution where all intervals of the same length are equally likely.

*   **PDF:** $f(x) = \frac{1}{b - a}$ for $a \le x \le b$.
*   **Mean:** $E[X] = \frac{a + b}{2}$
*   **Variance:** $Var(X) = \frac{(b - a)^2}{12}$
*   **Probability:** $P(x_1 < X < x_2) = \frac{x_2 - x_1}{b - a}$

## 2. Exponential Distribution ($X \sim Exp(\lambda)$)
Used to model the time between events in a Poisson process.

*   **PDF:** $f(x) = \lambda e^{-\lambda x}$ for $x \ge 0$.
*   **CDF:** $P(X \le x) = 1 - e^{-\lambda x}$
*   **Mean:** $E[X] = \frac{1}{\lambda}$
*   **Variance:** $Var(X) = \frac{1}{\lambda^2}$
*   **Complement Rule:** $P(X > x) = e^{-\lambda x}$ (very useful for "wait time longer than" problems).

---

## 3. Solved Examples

### Example 1: Uniform Probability
A bus arrives at a stop every 20 minutes. A person's wait time $X$ is $U(0, 20)$. What is the probability they wait more than 15 minutes?

**Step 1: Identify bounds.**
$a = 0, b = 20$.

**Step 2: WIP State.**
$P(X > 15) = \frac{b - 15}{b - a} = \frac{20 - 15}{?}$

**Step 3: Final Calculation.**
$P(X > 15) = \frac{5}{20} = 0.25$.

---

### Example 2: Uniform Mean and Variance
For $X \sim U(5, 15)$, find the expected value and variance.

**Step 1: Apply Mean formula.**
$E[X] = (5 + 15) / 2 = 10$.

**Step 2: WIP State.**
$Var(X) = \frac{(15 - 5)^2}{12} = \frac{10^2}{?}$

**Step 3: Final Calculation.**
$Var(X) = 100 / 12 = 8.3333$.

---

### Example 3: Exponential Wait Time
The time between arrivals at a bank follows an exponential distribution with $\lambda = 2$ arrivals per hour. What is the probability that the next arrival occurs within 30 minutes?

**Step 1: Convert units.**
$\lambda = 2$ per hour. 30 minutes is $0.5$ hours.

**Step 2: WIP State.**
Use the CDF: $P(X \le 0.5) = 1 - e^{-2(0.5)}$
$P(X \le 0.5) = 1 - e^{-?}$

**Step 3: Final Calculation.**
$1 - e^{-1} \approx 1 - 0.3679 = 0.6321$.

---

### Example 4: Exponential - Longer Than
If the average lifespan of a lightbulb is 1000 hours (exponentially distributed), what is the probability it lasts more than 1500 hours?

**Step 1: Find $\lambda$.**
Mean $E[X] = 1/\lambda = 1000 \implies \lambda = 0.001$.

**Step 2: WIP State.**
Use the complement rule: $P(X > 1500) = e^{-0.001(1500)}$

**Step 3: Final Calculation.**
$e^{-1.5} \approx 0.2231$.

---

### Example 5: Median of Exponential
Find the median time for the lightbulb in Example 4.

**Step 1: Set CDF to 0.5.**
$1 - e^{-\lambda x} = 0.5 \implies e^{-\lambda x} = 0.5$.

**Step 2: WIP State.**
$-\lambda x = \ln(0.5)$
$x = \frac{-\ln(0.5)}{0.001} = \frac{\ln(2)}{?}$

**Step 3: Final Calculation.**
$x = 0.693 / 0.001 = 693$ hours.
*(Note: The median is less than the mean in an exponential distribution!)*

---

### Example 6: Uniform Interval
$X \sim U(-5, 5)$. Find $P(|X| < 2)$.

**Step 1: Rewrite the inequality.**
$-2 < X < 2$.

**Step 2: WIP State.**
Length of interval $= 2 - (-2) = 4$.
Length of total range $= 5 - (-5) = ?$.

**Step 3: Final Calculation.**
$P = 4 / 10 = 0.4$.

---

### Example 7: Combined Probability
If $X \sim U(0, 10)$, find $P(X > 2 | X < 8)$.

**Step 1: Use the conditional probability formula.**
$P(A|B) = \frac{P(A \cap B)}{P(B)}$
$P(X > 2 \cap X < 8) = P(2 < X < 8) = \frac{8 - 2}{10} = 0.6$.

**Step 2: WIP State.**
$P(X < 8) = \frac{8 - 0}{10} = 0.8$.
$P = 0.6 / ?$

**Step 3: Final Calculation.**
$P = 0.6 / 0.8 = 0.75$.

---

## 4. The "Gotcha" Section (Hard Example)

### Example 8: The Memoryless Property Trap
The time $X$ you spend waiting for a server to respond is exponentially distributed with a mean of 5 seconds. You have already waited 10 seconds. What is the probability you will have to wait at least another 5 seconds?

**The "Gotcha":**
Many students try to calculate $P(X > 15 | X > 10)$ using complex integrals or the conditional probability formula. They think that since they have already waited a long time, the event "must happen soon."

**The Reality (The Memoryless Property):**
The Exponential distribution is **memoryless**. This means:
$$P(X > s + t | X > s) = P(X > t)$$
The fact that you waited 10 seconds ($s$) is completely irrelevant to the *additional* time ($t$) you will wait.

**Step 1: Identify the additional wait time.**
We want the probability of waiting *at least another* 5 seconds. So $t = 5$.

**Step 2: WIP State.**
The probability is simply $P(X > 5)$.
Mean = 5, so $\lambda = 1/5 = 0.2$.

**Step 3: Final Calculation.**
$$P(X > 5) = e^{-0.2(5)} = e^{-1} \approx 0.3679$$

**Result:** The probability is **0.3679**, exactly the same as if you had just started waiting! This is counter-intuitive but a key property of the Exponential distribution.
*(Warning: This property ONLY applies to the Exponential distribution in the continuous world!)*


# Phase 5.4: Gamma Distribution

The Gamma Distribution is a continuous probability distribution that generalizes the Exponential distribution. It is widely used to model wait times for multiple independent events to occur.

---

## 1. The Gamma Function ($\Gamma(\alpha)$)

Before defining the Gamma distribution, we must define the **Gamma Function**, which acts as a continuous generalization of the factorial function:

$$\Gamma(\alpha) = \int_{0}^{\infty} y^{\alpha-1} e^{-y} \, dy \quad \text{for } \alpha > 0$$

### Key Properties of the Gamma Function
1.  **Recursive Relation:** $\Gamma(\alpha + 1) = \alpha \cdot \Gamma(\alpha)$
2.  **Factorial Relation:** For any positive integer $n$:
    $$\Gamma(n) = (n-1)!$$
3.  **Special Value:** $\Gamma\left(\frac{1}{2}\right) = \sqrt{\pi}$
4.  **Base Case:** $\Gamma(1) = 0! = 1$

---

## 2. The Gamma Distribution

There are two common parameterisations of the Gamma distribution. Confusing them in an exam is a common mistake.

### 2.1 Rate Parameterisation (Standard in most syllabus structures)
If $X \sim Gamma(\alpha, \beta)$, where $\alpha > 0$ is the **shape parameter** and $\beta > 0$ is the **rate parameter**:

*   **PDF:**
    $$f(x) = \frac{\beta^\alpha}{\Gamma(\alpha)} x^{\alpha-1} e^{-\beta x}, \quad x > 0$$
*   **Mean:** $E[X] = \frac{\alpha}{\beta}$
*   **Variance:** $Var(X) = \frac{\alpha}{\beta^2}$
*   **MGF:** $M_X(t) = \left(1 - \frac{t}{\beta}\right)^{-\alpha} \quad (\text{for } t < \beta)$

### 2.2 Scale Parameterisation (Alternative)
Using the **scale parameter** $\theta = \frac{1}{\beta}$:
*   **PDF:** $f(x) = \frac{1}{\Gamma(\alpha)\theta^\alpha} x^{\alpha-1} e^{-x/\theta}$
*   **Mean:** $E[X] = \alpha\theta$
*   **Variance:** $Var(X) = \alpha\theta^2$

---

## 3. Relationships to Other Distributions

1.  **Exponential Distribution:** A Gamma distribution with shape $\alpha = 1$ is exactly the Exponential distribution:
    $$Gamma(1, \beta) \equiv Exp(\beta)$$
2.  **Sum of Independent Exponentials:** If $X_1, X_2, \dots, X_n$ are independent, identically distributed random variables with $X_i \sim Exp(\beta)$, then their sum follows a Gamma distribution (sometimes called the Erlang distribution):
    $$\sum_{i=1}^{n} X_i \sim Gamma(n, \beta)$$
3.  **Chi-Square Distribution:** The Chi-square distribution with $\nu$ degrees of freedom is a special case of the Gamma distribution:
    $$\chi^2_\nu \equiv Gamma\left(\frac{\nu}{2}, \frac{1}{2}\right)$$

---

## 4. Solved Exercises (9 Examples)

### Exercise 1: Evaluating the Gamma Function
**Problem:** Calculate the exact value of $\Gamma\left(\frac{5}{2}\right)$.

**Solution:**
- **Step 1: Apply the recursive formula $\Gamma(\alpha + 1) = \alpha \Gamma(\alpha)$.**
  $$\Gamma\left(\frac{5}{2}\right) = \Gamma\left(\frac{3}{2} + 1\right) = \frac{3}{2} \cdot \Gamma\left(\frac{3}{2}\right)$$
- **Step 2: WIP State.**
  Apply the recursive formula again:
  $$\Gamma\left(\frac{3}{2}\right) = \Gamma\left(\frac{1}{2} + 1\right) = \frac{1}{2} \cdot \Gamma\left(\frac{1}{2}\right)$$
  Recall that $\Gamma\left(\frac{1}{2}\right) = \sqrt{\pi}$.
  So, $\Gamma\left(\frac{5}{2}\right) = \frac{3}{2} \cdot \left(\frac{1}{2} \cdot ?\right)$
- **Step 3: Final Calculation.**
  $$\Gamma\left(\frac{5}{2}\right) = \frac{3}{2} \cdot \frac{1}{2} \cdot \sqrt{\pi} = \frac{3}{4}\sqrt{\pi}.$$

---

### Exercise 2: Identifying Shape and Rate
**Problem:** A wait time $X$ has PDF $f(x) = 4 x e^{-2x}$ for $x > 0$. Identify the distribution and calculate its mean and variance.

**Solution:**
- **Step 1: Match the PDF structure with the Gamma PDF.**
  $$f(x) = \frac{\beta^\alpha}{\Gamma(\alpha)} x^{\alpha-1} e^{-\beta x}$$
  Looking at $e^{-2x}$, we get $\beta = 2$.
  Looking at $x = x^1$, we get $\alpha - 1 = 1 \implies \alpha = 2$.
- **Step 2: WIP State.**
  Verify the constant coefficient:
  $$\frac{\beta^\alpha}{\Gamma(\alpha)} = \frac{2^2}{\Gamma(2)} = \frac{4}{1!} = 4$$
  This matches the coefficient in the problem.
  Therefore, $X \sim Gamma(\alpha = 2, \beta = 2)$.
  Mean: $E[X] = \frac{\alpha}{\beta} = \frac{2}{2} = 1$.
  Variance: $Var(X) = \frac{\alpha}{\beta^2} = \frac{2}{?}$
- **Step 3: Final Calculation.**
  $$Var(X) = \frac{2}{4} = 0.5.$$

---

### Exercise 3: Sum of Wait Times
**Problem:** The time (in hours) to repair a server is exponentially distributed with a mean of 0.5 hours. If a technician has 4 independent server repairs scheduled, find the probability distribution of the total repair time $Y$. What is the expected total repair time and its variance?

**Solution:**
- **Step 1: Identify individual parameters.**
  Each repair $X_i \sim Exp(\lambda)$.
  Since the mean is $0.5$, $\frac{1}{\lambda} = 0.5 \implies \lambda = 2$.
- **Step 2: WIP State.**
  Since $Y = \sum_{i=1}^{4} X_i$ is a sum of $n=4$ independent exponential variables, it follows a Gamma distribution:
  $$Y \sim Gamma(\alpha = 4, \beta = 2)$$
  Expected total repair time: $E[Y] = \frac{\alpha}{\beta} = \frac{4}{2} = 2$ hours.
  Variance: $Var(Y) = \frac{4}{?}$
- **Step 3: Final Calculation.**
  $$Var(Y) = \frac{4}{2^2} = \frac{4}{4} = 1.$$

---

### Exercise 4: Integrating a Gamma PDF to Find Constants
**Problem:** Find the value of the constant $c$ such that $f(x) = c x^2 e^{-3x}$ for $x > 0$ is a valid PDF.

**Solution:**
- **Step 1: Identify parameters.**
  This matches a Gamma PDF with $\alpha - 1 = 2 \implies \alpha = 3$ and $\beta = 3$.
- **Step 2: WIP State.**
  The normalisation constant for a Gamma distribution requires that the total area equals 1:
  $$c = \frac{\beta^\alpha}{\Gamma(\alpha)} = \frac{3^3}{\Gamma(3)} = \frac{27}{?}$$
- **Step 3: Final Calculation.**
  $$\Gamma(3) = 2! = 2$$
  $$c = \frac{27}{2} = 13.5.$$

---

### Exercise 5: Deriving Mean using MGF
**Problem:** Find the expected value of $X \sim Gamma(\alpha, \beta)$ by differentiating its MGF.

**Solution:**
- **Step 1: Set up the derivative.**
  $$M_X(t) = \left(1 - \frac{t}{\beta}\right)^{-\alpha}$$
  Use the chain rule:
  $$M'_X(t) = -\alpha \left(1 - \frac{t}{\beta}\right)^{-\alpha-1} \cdot \left(-\frac{1}{\beta}\right)$$
- **Step 2: WIP State.**
  Simplify the derivative:
  $$M'_X(t) = \frac{\alpha}{\beta} \left(1 - \frac{t}{\beta}\right)^{-\alpha-1}$$
  Evaluate at $t=0$:
  $$E[X] = M'_X(0) = \frac{\alpha}{\beta} (1 - 0)^{-( \alpha + 1 )} = ?$$
- **Step 3: Final Calculation.**
  $$E[X] = \frac{\alpha}{\beta}.$$

---

### Exercise 6: Sum of Independent Gammas
**Problem:** Let $X \sim Gamma(2, 5)$ and $Y \sim Gamma(3, 5)$ be independent random variables. Find the distribution of $W = X + Y$.

**Solution:**
- **Step 1: Recall MGF of Gamma.**
  $$M_X(t) = \left(1 - \frac{t}{5}\right)^{-2}, \quad M_Y(t) = \left(1 - \frac{t}{5}\right)^{-3}$$
- **Step 2: WIP State.**
  Since they are independent:
  $$M_W(t) = M_X(t) \cdot M_Y(t) = \left(1 - \frac{t}{5}\right)^{-2} \cdot \left(1 - \frac{t}{5}\right)^{-3} = \left(1 - \frac{t}{5}\right)^{?}$$
- **Step 3: Final Calculation.**
  $$M_W(t) = \left(1 - \frac{t}{5}\right)^{-5}$$
  By uniqueness of the MGF, $W \sim Gamma(5, 5)$.
  *(Exam note: You can add independent Gamma variables ONLY if they share the same rate parameter $\beta$!)*

---

### Exercise 7: Connection to Chi-Square
**Problem:** Show that the Chi-square distribution with $\nu$ degrees of freedom is a special case of the Gamma distribution by comparing their MGFs. Recall that the MGF of a Chi-square variable is $M_{\chi^2}(t) = (1 - 2t)^{-\nu/2}$.

**Solution:**
- **Step 1: Look at the Gamma MGF.**
  $$M_{Gamma}(t) = \left(1 - \frac{t}{\beta}\right)^{-\alpha}$$
- **Step 2: WIP State.**
  We want to set:
  $$\left(1 - \frac{t}{\beta}\right)^{-\alpha} = (1 - 2t)^{-\nu/2}$$
  Matching the terms:
  - Exponent: $-\alpha = -\frac{\nu}{2} \implies \alpha = \frac{\nu}{2}$.
  - Fraction: $\frac{t}{\beta} = 2t \implies \beta = ?$.
- **Step 3: Final Calculation.**
  $$\beta = \frac{1}{2}$$
  Thus, a Chi-square distribution with $\nu$ degrees of freedom is exactly equivalent to $Gamma\left(\alpha = \frac{\nu}{2}, \beta = \frac{1}{2}\right)$.

---

### Exercise 8: Expected Value of a Reciprocal
**Problem:** Let $X \sim Gamma(\alpha, \beta)$ with $\alpha > 1$. Find the expected value of the reciprocal of $X$, $E\left[\frac{1}{X}\right]$.

**Solution:**
- **Step 1: Set up the integral.**
  $$E\left[\frac{1}{X}\right] = \int_{0}^{\infty} \frac{1}{x} \cdot f(x) \, dx = \int_{0}^{\infty} \frac{1}{x} \cdot \frac{\beta^\alpha}{\Gamma(\alpha)} x^{\alpha-1} e^{-\beta x} \, dx$$
- **Step 2: WIP State.**
  Simplify the integrand:
  $$E\left[\frac{1}{X}\right] = \frac{\beta^\alpha}{\Gamma(\alpha)} \int_{0}^{\infty} x^{\alpha-2} e^{-\beta x} \, dx$$
  Notice that the integral is almost the integral of a Gamma PDF with shape parameter $\alpha' = \alpha - 1$ and rate parameter $\beta' = \beta$.
  $$\int_{0}^{\infty} x^{(\alpha-1)-1} e^{-\beta x} \, dx = \frac{\Gamma(\alpha-1)}{\beta^{\alpha-1}}$$
  Substituting this back:
  $$E\left[\frac{1}{X}\right] = \frac{\beta^\alpha}{\Gamma(\alpha)} \cdot \frac{\Gamma(\alpha-1)}{\beta^{\alpha-1}} = \beta \cdot \frac{\Gamma(\alpha-1)}{?}$$
- **Step 3: Final Calculation.**
  Recall that $\Gamma(\alpha) = (\alpha - 1) \cdot \Gamma(\alpha - 1)$.
  $$E\left[\frac{1}{X}\right] = \beta \cdot \frac{\Gamma(\alpha-1)}{(\alpha-1)\Gamma(\alpha-1)} = \frac{\beta}{\alpha - 1}.$$

---

### Exercise 9: Linear Transformation (Gotcha Moment)
**Problem:** If $X \sim Gamma(\alpha, \beta)$, does $Y = cX$ (where $c > 0$) follow a Gamma distribution? If so, what are its parameters?

**Solution:**
- **Step 1: Use the MGF method.**
  $$M_Y(t) = M_{cX}(t) = M_X(ct)$$
- **Step 2: WIP State.**
  Substitute $ct$ into the MGF of $X$:
  $$M_Y(t) = \left(1 - \frac{ct}{\beta}\right)^{-\alpha} = \left(1 - \frac{t}{\beta/c}\right)^{?}$$
- **Step 3: Final Calculation.**
  $$M_Y(t) = \left(1 - \frac{t}{\beta/c}\right)^{-\alpha}$$
  By uniqueness of the MGF, this represents a Gamma distribution:
  $$Y \sim Gamma\left(\alpha, \frac{\beta}{c}\right)$$
  *(Gotcha check: Scaling a Gamma variable changes its rate parameter to $\beta/c$ while keeping the shape parameter $\alpha$ unchanged. If you scale by 2, the rate is cut in half, which makes physical sense as the variable becomes twice as spread out!)*


# Phase 5.5: Transformations of Random Variables

In probability theory, we often need to find the probability distribution of a new random variable $Y$ that is a function of an existing random variable $X$, written as $Y = g(X)$. This process is called a **transformation**.

---

## 1. Discrete Random Variables

For a discrete random variable $X$ with probability mass function $p_X(x)$, the PMF of $Y = g(X)$ is obtained by summing the probabilities of all $x$ values that map to $y$:

$$p_Y(y) = P(Y = y) = \sum_{x : g(x) = y} p_X(x)$$

---

## 2. Continuous Random Variables

There are two primary methods for finding the PDF of $Y = g(X)$ when $X$ is continuous.

### 2.1 The CDF Method (First Principles)
This is the most robust method and works for both monotonic and non-monotonic functions (like $Y = X^2$).

1.  Write the cumulative distribution function (CDF) of $Y$:
    $$F_Y(y) = P(Y \le y) = P(g(X) \le y)$$
2.  Rewrite the inequality in terms of $X$.
3.  Express $F_Y(y)$ in terms of the CDF of $X$, $F_X(x)$.
4.  Differentiate $F_Y(y)$ with respect to $y$ to get the PDF $f_Y(y)$:
    $$f_Y(y) = \frac{d}{dy} F_Y(y)$$

### 2.2 The Change of Variables Formula (Jacobian Method)
If $g(x)$ is **strictly monotonic** (either strictly increasing or strictly decreasing) and differentiable, the PDF of $Y$ can be computed directly using:

$$f_Y(y) = f_X(x) \cdot \left| \frac{dx}{dy} \right| \quad \text{where } x = g^{-1}(y)$$

Or written equivalently as:

$$f_Y(y) = f_X(g^{-1}(y)) \cdot \left| \frac{d}{dy} g^{-1}(y) \right|$$

> **Exam Warning:** Always specify the **domain (range of validity)** of the new PDF $f_Y(y)$ by mapping the original boundaries of $X$ through the function $g(x)$. Leaving out the domain is a guaranteed way to lose marks.

---

## 3. Solved Exercises (9 Examples)

### Exercise 1: Discrete Transformation
**Problem:** Let $X$ have PMF:
*   $P(X = -1) = 0.2$
*   $P(X = 0) = 0.3$
*   $P(X = 1) = 0.4$
*   $P(X = 2) = 0.1$

Find the PMF of $Y = X^2$.

**Solution:**
- **Step 1: Map the values of $X$ to $Y$.**
  - If $x = -1 \implies y = (-1)^2 = 1$
  - If $x = 0 \implies y = 0^2 = 0$
  - If $x = 1 \implies y = 1^2 = 1$
  - If $x = 2 \implies y = 2^2 = 4$
  The possible values for $Y$ are $\{0, 1, 4\}$.
- **Step 2: WIP State.**
  Sum probabilities for each unique $y$:
  - $P(Y = 0) = P(X = 0) = 0.3$
  - $P(Y = 1) = P(X = -1) + P(X = 1) = 0.2 + 0.4 = 0.6$
  - $P(Y = 4) = P(X = ?) = ?$
- **Step 3: Final Calculation.**
  - $P(Y = 4) = P(X = 2) = 0.1$.
  - PMF Table:
    | $y$ | 0 | 1 | 4 |
    | :--- | :--- | :--- | :--- |
    | $P(Y = y)$ | 0.3 | 0.6 | 0.1 |
  Check sum: $0.3 + 0.6 + 0.1 = 1.0$.

---

### Exercise 2: Monotonic Linear Transformation (Continuous)
**Problem:** Let $X$ be a continuous random variable with PDF $f_X(x) = 2x$ for $0 < x < 1$. Find the PDF of $Y = 3X + 2$.

**Solution:**
- **Step 1: Find the inverse function and its derivative.**
  Let $y = 3x + 2 \implies x = \frac{y - 2}{3}$.
  $$\frac{dx}{dy} = \frac{1}{3}$$
- **Step 2: WIP State.**
  Find the new domain for $Y$:
  - When $x = 0 \implies y = 3(0) + 2 = 2$.
  - When $x = 1 \implies y = 3(1) + 2 = 5$.
  So the domain of $Y$ is $2 < y < 5$.
  Apply the Change of Variables formula:
  $$f_Y(y) = f_X(x) \cdot \left| \frac{dx}{dy} \right| = 2 \cdot \left(\frac{y-2}{3}\right) \cdot ?$$
- **Step 3: Final Calculation.**
  $$f_Y(y) = 2 \cdot \left(\frac{y - 2}{3}\right) \cdot \frac{1}{3} = \frac{2(y - 2)}{9}$$
  So, the final PDF is:
  $$f_Y(y) = \frac{2(y - 2)}{9}, \quad 2 < y < 5$$

---

### Exercise 3: Non-Monotonic Transformation ($Y = X^2$)
**Problem:** Let $X \sim U(-1, 2)$. Find the PDF of $Y = X^2$.

**Solution:**
- **Step 1: Write original PDF and find domain.**
  $$f_X(x) = \frac{1}{2 - (-1)} = \frac{1}{3}, \quad -1 < x < 2$$
  Since $Y = X^2$, the range of $Y$ is $[0, 4]$.
- **Step 2: WIP State (Apply CDF method).**
  For $0 < y < 1$, the values of $X$ that satisfy $X^2 \le y$ are $-\sqrt{y} \le X \le \sqrt{y}$.
  $$F_Y(y) = P(X^2 \le y) = P(-\sqrt{y} \le X \le \sqrt{y}) = F_X(\sqrt{y}) - F_X(-\sqrt{y})$$
  Differentiating:
  $$f_Y(y) = \frac{d}{dy}\left(F_X(\sqrt{y}) - F_X(-\sqrt{y})\right) = f_X(\sqrt{y}) \cdot \frac{1}{2\sqrt{y}} - f_X(-\sqrt{y}) \cdot \left(-\frac{1}{2\sqrt{y}}\right)$$
  $$f_Y(y) = \frac{1}{2\sqrt{y}} \left( f_X(\sqrt{y}) + f_X(-\sqrt{y}) \right)$$
  For $1 \le y < 4$, $X$ can only be positive because the lower boundary of $X$ is $-1$ (which squares to $1$). Thus, $X^2 \le y$ implies $-1 < X \le \sqrt{y}$.
  $$F_Y(y) = P(-1 < X \le \sqrt{y}) = F_X(\sqrt{y}) - F_X(-1)$$
  Differentiating:
  $$f_Y(y) = f_X(\sqrt{y}) \cdot \frac{1}{2\sqrt{y}} = \frac{1}{3} \cdot \frac{1}{2\sqrt{y}} = ?$$
- **Step 3: Final Calculation.**
  - For $0 < y < 1$: Both $\sqrt{y}$ and $-\sqrt{y}$ lie in the domain of $X$ ($-1 < x < 2$).
    $$f_Y(y) = \frac{1}{2\sqrt{y}} \left( \frac{1}{3} + \frac{1}{3} \right) = \frac{1}{3\sqrt{y}}$$
  - For $1 \le y < 4$: Only $\sqrt{y}$ lies in the domain of $X$.
    $$f_Y(y) = \frac{1}{6\sqrt{y}}$$
  Final piecewise PDF:
  $$f_Y(y) = \begin{cases} \frac{1}{3\sqrt{y}}, & 0 < y < 1 \\ \frac{1}{6\sqrt{y}}, & 1 \le y < 4 \\ 0, & \text{otherwise} \end{cases}$$

---

### Exercise 4: Exponential from Uniform
**Problem:** Let $X \sim U(0, 1)$. Find the PDF of $Y = -\ln(X)$.

**Solution:**
- **Step 1: Inverse function and derivative.**
  Let $y = -\ln(x) \implies -y = \ln(x) \implies x = e^{-y}$.
  $$\frac{dx}{dy} = -e^{-y} \implies \left| \frac{dx}{dy} \right| = e^{-y}$$
- **Step 2: WIP State.**
  Domain mapping:
  - As $x \to 0^+ \implies y \to \infty$.
  - As $x \to 1^- \implies y \to 0$.
  So the domain of $Y$ is $y > 0$.
  Apply formula:
  $$f_Y(y) = f_X(x) \cdot \left| \frac{dx}{dy} \right|$$
  Since $X \sim U(0, 1)$, $f_X(x) = 1$ on $(0, 1)$.
  $$f_Y(y) = 1 \cdot e^{-y} = ?$$
- **Step 3: Final Calculation.**
  $$f_Y(y) = e^{-y}, \quad y > 0$$
  *(Note: This is exactly the PDF of an Exponential distribution with parameter $\lambda = 1$. This is the basis of the Inverse Transform Method for generating random variables!)*

---

### Exercise 5: Transformation of a Normal Variable to Log-Normal
**Problem:** Let $X \sim N(\mu, \sigma^2)$. Find the PDF of $Y = e^X$.

**Solution:**
- **Step 1: Inverse and derivative.**
  Let $y = e^x \implies x = \ln(y)$ (for $y > 0$).
  $$\frac{dx}{dy} = \frac{1}{y}$$
- **Step 2: WIP State.**
  Domain: Since $x \in (-\infty, \infty)$, $y = e^x \in (0, \infty)$.
  Recall the Normal PDF:
  $$f_X(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x - \mu)^2}{2\sigma^2}}$$
  Apply Change of Variables formula:
  $$f_Y(y) = f_X(\ln(y)) \cdot \left| \frac{dx}{dy} \right| = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(\ln(y) - \mu)^2}{2\sigma^2}} \cdot ?$$
- **Step 3: Final Calculation.**
  $$f_Y(y) = \frac{1}{y \sigma \sqrt{2\pi}} e^{-\frac{(\ln(y) - \mu)^2}{2\sigma^2}}, \quad y > 0$$
  This is the PDF of the **Log-Normal distribution**.

---

### Exercise 6: CDF Method for a Square Root Function
**Problem:** Let $X \sim Exp(\lambda)$. Find the PDF of $Y = \sqrt{X}$.

**Solution:**
- **Step 1: Use the CDF method.**
  For $y > 0$:
  $$F_Y(y) = P(Y \le y) = P(\sqrt{X} \le y) = P(X \le y^2) = F_X(y^2)$$
- **Step 2: WIP State.**
  Since $X \sim Exp(\lambda)$, its CDF is $F_X(x) = 1 - e^{-\lambda x}$ for $x > 0$.
  $$F_Y(y) = 1 - e^{-\lambda y^2}$$
  Differentiate with respect to $y$ using the chain rule:
  $$f_Y(y) = \frac{d}{dy}\left(1 - e^{-\lambda y^2}\right) = -e^{-\lambda y^2} \cdot (-2\lambda y) = ?$$
- **Step 3: Final Calculation.**
  $$f_Y(y) = 2\lambda y e^{-\lambda y^2}, \quad y > 0$$
  *(Note: This is the Weibull distribution with shape parameter 2).*

---

### Exercise 7: Monotonic Decreasing Transformation
**Problem:** Let $X$ have PDF $f_X(x) = 3x^2$ for $0 < x < 1$. Find the PDF of $Y = \frac{1}{X}$.

**Solution:**
- **Step 1: Find inverse and derivative.**
  Let $y = 1/x \implies x = 1/y$.
  $$\frac{dx}{dy} = -\frac{1}{y^2} \implies \left| \frac{dx}{dy} \right| = \frac{1}{y^2}$$
- **Step 2: WIP State.**
  Domain mapping:
  - When $x = 0^+ \implies y \to \infty$.
  - When $x = 1 \implies y = 1$.
  So the domain of $Y$ is $y > 1$.
  Apply formula:
  $$f_Y(y) = f_X\left(\frac{1}{y}\right) \cdot \left| \frac{dx}{dy} \right| = 3\left(\frac{1}{y}\right)^2 \cdot ?$$
- **Step 3: Final Calculation.**
  $$f_Y(y) = \frac{3}{y^2} \cdot \frac{1}{y^2} = \frac{3}{y^4}, \quad y > 1$$

---

### Exercise 8: The Linear Scaling Gotcha
**Problem:** Let $X$ follow a distribution with PDF $f_X(x)$. If $Y = aX$, write the PDF $f_Y(y)$ using $f_X$.

**Solution:**
- **Step 1: Find inverse and derivative.**
  Let $y = ax \implies x = y/a$.
  $$\frac{dx}{dy} = \frac{1}{a} \implies \left| \frac{dx}{dy} \right| = \frac{1}{|a|}$$
- **Step 2: WIP State.**
  Apply formula:
  $$f_Y(y) = f_X\left(\frac{y}{a}\right) \cdot ?$$
- **Step 3: Final Calculation.**
  $$f_Y(y) = \frac{1}{|a|} f_X\left(\frac{y}{a}\right)$$
  *(Gotcha check: Students frequently write $f_Y(y) = f_X(y/a)$ and forget the division by $|a|$. This constant factor is mathematically required so that the PDF integrates to 1).*

---

### Exercise 9: Cauchy from Uniform (The tangent transformation)
**Problem:** Let $X \sim U\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$. Find the PDF of $Y = \tan(X)$.

**Solution:**
- **Step 1: Inverse function and derivative.**
  Let $y = \tan(x) \implies x = \arctan(y)$.
  $$\frac{dx}{dy} = \frac{1}{1 + y^2}$$
- **Step 2: WIP State.**
  Domain mapping:
  - When $x \to -\frac{\pi}{2}^+ \implies y \to -\infty$.
  - When $x \to \frac{\pi}{2}^- \implies y \to \infty$.
  So the domain of $Y$ is $-\infty < y < \infty$.
  The PDF of $X$ is $f_X(x) = \frac{1}{\frac{\pi}{2} - (-\frac{\pi}{2})} = \frac{1}{\pi}$ on its interval.
  Apply formula:
  $$f_Y(y) = f_X(\arctan(y)) \cdot \left| \frac{dx}{dy} \right| = \frac{1}{\pi} \cdot ?$$
- **Step 3: Final Calculation.**
  $$f_Y(y) = \frac{1}{\pi(1 + y^2)}, \quad -\infty < y < \infty$$
  This is the PDF of the standard **Cauchy distribution**.
