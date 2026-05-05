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
