# Phase 4.1: Discrete Random Variables — Fundamentals

A **Random Variable** maps each outcome of a random experiment to a number. A **Discrete Random Variable** takes on a finite or countably infinite set of values. The three pillars of this topic — the PMF, the Expected Value, and the Variance — completely characterise the distribution's shape, centre, and spread.

---

## 1. Probability Mass Function (PMF)

The **PMF** of a discrete random variable $X$ is a function $p(x)$ that assigns a probability to each possible value $x$:

$$p(x) = P(X = x)$$

### Validity Conditions

Any function claiming to be a PMF must satisfy two conditions simultaneously:

**Condition 1 (Non-negativity):**

$$p(x) \geq 0 \quad \text{for all } x$$

**Condition 2 (Normalisation):**

$$\sum_{\text{all } x} p(x) = 1$$

If either condition fails, the function is not a valid PMF. These conditions are directly analogous to Kolmogorov's Axioms from Phase 2.

### Standard PMF Table Format

A PMF is most clearly presented as a table:

| $x$ | $x_1$ | $x_2$ | $\cdots$ | $x_k$ |
| :--- | :--- | :--- | :--- | :--- |
| $P(X=x)$ | $p_1$ | $p_2$ | $\cdots$ | $p_k$ |

The bottom row must sum to 1.

---

## 2. Expected Value $E[X]$

The **Expected Value** (also called the **mean** or **expectation**) is the probability-weighted average of all values $X$ can take. It represents the long-run average outcome over many repetitions of the experiment.

$$\boxed{E[X] = \mu = \sum_{\text{all } x} x \cdot p(x)}$$

### Key Properties of Expectation

These properties hold without any condition on the distribution:

| Property | Formula |
| :--- | :--- |
| Linearity | $E[aX + b] = a \cdot E[X] + b$ |
| Constant | $E[c] = c$ |
| Sum of variables | $E[X + Y] = E[X] + E[Y]$ |

---

## 3. Variance $V(X)$

The **Variance** measures the average squared deviation of $X$ from its mean. A higher variance means the distribution is more spread out.

**Definition formula:**

$$V(X) = E\left[(X - \mu)^2\right] = \sum_{\text{all } x} (x - \mu)^2 \cdot p(x)$$

**Computational shortcut formula** (always use this in practice — it avoids working with $\mu$ repeatedly):

$$\boxed{V(X) = E[X^2] - (E[X])^2}$$

where $E[X^2] = \sum_{\text{all } x} x^2 \cdot p(x)$.

**Standard Deviation:**

$$\sigma = SD(X) = \sqrt{V(X)}$$

### Key Properties of Variance

| Property | Formula | Note |
| :--- | :--- | :--- |
| Scaling | $V(aX) = a^2 \cdot V(X)$ | The square of $a$ appears |
| Shift | $V(X + b) = V(X)$ | Constants do not affect spread |
| Combined | $V(aX + b) = a^2 \cdot V(X)$ | $b$ disappears entirely |

> **Critical rule:** $V(aX + b) = a^2 \cdot V(X)$. The constant $b$ has **zero effect** on variance. This is the most common source of errors on exams.

---

## 4. Solved Exercises

### Exercise 1: Verifying a PMF

**Problem:** Determine whether the following is a valid PMF for $X \in \{1, 2, 3, 4\}$:

| $x$ | 1 | 2 | 3 | 4 |
| :--- | :--- | :--- | :--- | :--- |
| $P(X=x)$ | 0.1 | 0.3 | 0.4 | 0.2 |

**Solution:**

**Check 1 (Non-negativity):** All values are $\geq 0$. Passed.

**Check 2 (Normalisation):** $0.1 + 0.3 + 0.4 + 0.2 = 1.0$. Passed.

This is a valid PMF.

---

### Exercise 2: Finding a Missing Probability

**Problem:** The PMF of $X$ is given below. Find the value of $c$.

| $x$ | 0 | 1 | 2 | 3 |
| :--- | :--- | :--- | :--- | :--- |
| $P(X=x)$ | $c$ | $2c$ | $3c$ | $4c$ |

**Solution:**

Apply the normalisation condition:

$$c + 2c + 3c + 4c = 1$$

$$10c = 1 \implies c = 0.1$$

The completed PMF:

| $x$ | 0 | 1 | 2 | 3 |
| :--- | :--- | :--- | :--- | :--- |
| $P(X=x)$ | 0.1 | 0.2 | 0.3 | 0.4 |

---

### Exercise 3: Computing $E[X]$

**Problem:** Using the PMF from Exercise 2, compute $E[X]$.

**Solution:**

$$E[X] = \sum x \cdot p(x) = 0(0.1) + 1(0.2) + 2(0.3) + 3(0.4)$$

$$E[X] = 0 + 0.2 + 0.6 + 1.2 = 2.0$$

---

### Exercise 4: Computing $V(X)$ using the Shortcut

**Problem:** Using the PMF from Exercise 2 and $E[X] = 2.0$, compute $V(X)$ and $SD(X)$.

**Solution:**

**Step 1:** Compute $E[X^2]$:

$$E[X^2] = 0^2(0.1) + 1^2(0.2) + 2^2(0.3) + 3^2(0.4)$$

$$E[X^2] = 0 + 0.2 + 1.2 + 3.6 = 5.0$$

**Step 2:** Apply the shortcut formula:

$$V(X) = E[X^2] - (E[X])^2 = 5.0 - (2.0)^2 = 5.0 - 4.0 = 1.0$$

$$SD(X) = \sqrt{1.0} = 1.0$$

---

### Exercise 5: Applying Linearity of Expectation

**Problem:** A random variable $X$ has $E[X] = 3$ and $V(X) = 4$. Find $E[2X + 5]$ and $V(2X + 5)$.

**Solution:**

$$E[2X + 5] = 2 \cdot E[X] + 5 = 2(3) + 5 = 11$$

$$V(2X + 5) = 2^2 \cdot V(X) = 4 \cdot 4 = 16$$

Note that the constant $+5$ contributes nothing to the variance.

---

### Exercise 6: Computing a Probability from the PMF

**Problem:** Using the PMF from Exercise 2, find $P(X \geq 2)$ and $P(1 \leq X \leq 3)$.

**Solution:**

$$P(X \geq 2) = P(X=2) + P(X=3) = 0.3 + 0.4 = 0.7$$

$$P(1 \leq X \leq 3) = P(X=1) + P(X=2) + P(X=3) = 0.2 + 0.3 + 0.4 = 0.9$$

---

### Exercise 7: Building a PMF from a Word Problem

**Problem:** A fair die is rolled. Let $X$ = the number of dots showing. Build the PMF table and compute $E[X]$ and $V(X)$.

**Solution:**

Each face has probability $\frac{1}{6}$.

| $x$ | 1 | 2 | 3 | 4 | 5 | 6 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $P(X=x)$ | $\frac{1}{6}$ | $\frac{1}{6}$ | $\frac{1}{6}$ | $\frac{1}{6}$ | $\frac{1}{6}$ | $\frac{1}{6}$ |

$$E[X] = \frac{1+2+3+4+5+6}{6} = \frac{21}{6} = 3.5$$

$$E[X^2] = \frac{1+4+9+16+25+36}{6} = \frac{91}{6} \approx 15.167$$

$$V(X) = E[X^2] - (E[X])^2 = \frac{91}{6} - (3.5)^2 = \frac{91}{6} - \frac{49}{4} = \frac{182}{12} - \frac{147}{12} = \frac{35}{12} \approx 2.917$$

---

### Exercise 8: The Gotcha — Variance of a Difference

**Problem:** Two independent random variables $X$ and $Y$ have $E[X] = 4$, $V(X) = 3$, $E[Y] = 2$, $V(Y) = 5$. A student computes $V(X - Y)$ and writes:

$$V(X - Y) = V(X) - V(Y) = 3 - 5 = -2$$

Find the error and compute the correct answer.

**Solution:**

**The error:** The student subtracted the variances. Variance **cannot be subtracted** — it is always additive for independent variables, regardless of whether the operation on $X$ and $Y$ is addition or subtraction.

The correct rule for independent $X$ and $Y$:

$$V(X - Y) = V(X) + (-1)^2 \cdot V(Y) = V(X) + V(Y)$$

This follows from the scaling property $V(aY) = a^2 V(Y)$ with $a = -1$:

$$V(X - Y) = V(X) + V(-Y) = V(X) + (-1)^2 V(Y) = 3 + 5 = 8$$

**The general rule:**

$$V(aX + bY) = a^2 V(X) + b^2 V(Y) \quad \text{(for independent } X, Y\text{)}$$

A negative sign on a variable **always becomes a positive** in the variance calculation because it is squared.

---

## Exam Tip: The Shortcut Formula is Non-Negotiable

Always use $V(X) = E[X^2] - (E[X])^2$ rather than the definition formula $\sum (x-\mu)^2 p(x)$. The definition requires computing $\mu$, then subtracting it from each value, squaring, and multiplying — every step is a potential arithmetic error. The shortcut reduces this to two sums that can be computed in a single pass through the table.
