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


# Phase 4.2: Binomial Distribution

The Binomial Distribution models the number of **successes** in a fixed sequence of independent trials where each trial has exactly two possible outcomes (success or failure) and the probability of success is constant. It is the most frequently examined discrete distribution at the university level.

---

## 1. The Four Conditions (FINS)

A random variable $X$ follows a Binomial Distribution **only if all four conditions hold**:

1. **F**ixed number of trials: $n$ is known and constant.
2. **I**ndependence: each trial's outcome does not affect any other.
3. **N**o more than two outcomes: each trial is either "success" or "failure".
4. **S**ame probability: $p$ (probability of success) is constant across all trials.

If any single condition fails, the Binomial model is invalid and a different distribution must be used.

---

## 2. The PMF Formula

If $X \sim B(n, p)$, then the probability of exactly $k$ successes in $n$ trials is:

$$\boxed{P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}, \quad k = 0, 1, 2, \ldots, n}$$

Where:
- $n$ = total number of trials
- $k$ = number of successes (the value you are computing for)
- $p$ = probability of success on a single trial
- $1-p = q$ = probability of failure on a single trial
- $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ = the binomial coefficient (number of ways to choose $k$ from $n$)

---

## 3. Mean and Variance

For $X \sim B(n, p)$, the mean and variance have elegant closed-form expressions derived from the general definitions:

$$\boxed{E[X] = n \cdot p}$$

$$\boxed{V(X) = n \cdot p \cdot (1-p)}$$

$$SD(X) = \sqrt{n \cdot p \cdot (1-p)}$$

These formulas must be memorised. Deriving them from the PMF during an exam wastes significant time.

---

## 4. Cumulative Probability

For "at most $k$" or "at least $k$" questions, sum the individual PMF values:

$$P(X \leq k) = \sum_{i=0}^{k} \binom{n}{i} p^i (1-p)^{n-i}$$

$$P(X \geq k) = 1 - P(X \leq k-1)$$

The complement rule $P(X \geq k) = 1 - P(X \leq k-1)$ is almost always faster than summing many terms directly.

---

## 5. Solved Exercises

### Exercise 1: Identifying Parameters

**Problem:** A fair coin is tossed 8 times. Let $X$ be the number of Heads. Identify the distribution, state all parameters, and verify the four conditions.

**Solution:**

- **Fixed $n$:** 8 tosses — fixed. Passed.
- **Independence:** Each toss is independent. Passed.
- **Two outcomes:** Head (success) or Tail (failure). Passed.
- **Constant $p$:** $p = 0.5$ for every toss. Passed.

$$X \sim B(8, 0.5)$$

$$E[X] = 8 \times 0.5 = 4, \quad V(X) = 8 \times 0.5 \times 0.5 = 2$$

---

### Exercise 2: Computing a Single PMF Value

**Problem:** A factory produces items where 20% are defective. A quality inspector picks 5 items at random. Find the probability that exactly 2 are defective.

**Solution:**

$$X \sim B(5, 0.2), \quad P(X = 2) = \binom{5}{2}(0.2)^2(0.8)^3$$

$$\binom{5}{2} = \frac{5!}{2! \cdot 3!} = 10$$

$$P(X=2) = 10 \times 0.04 \times 0.512 = 10 \times 0.02048 = 0.2048$$

---

### Exercise 3: Computing $P(X = 0)$ — The "None" Case

**Problem:** Using the same factory setting ($n=5$, $p=0.2$), find the probability that no items are defective.

**Solution:**

$$P(X=0) = \binom{5}{0}(0.2)^0(0.8)^5 = 1 \times 1 \times 0.32768 = 0.3277$$

> **Note:** $(0.2)^0 = 1$ and $\binom{5}{0} = 1$. Students often hesitate here — both are always exactly 1.

---

### Exercise 4: Computing $P(X = n)$ — The "All" Case

**Problem:** Find the probability that all 5 items are defective ($n=5$, $p=0.2$).

**Solution:**

$$P(X=5) = \binom{5}{5}(0.2)^5(0.8)^0 = 1 \times 0.00032 \times 1 = 0.00032$$

This confirms that all 5 being defective at a 20% rate is extremely unlikely.

---

### Exercise 5: "At Least One" Using the Complement

**Problem:** From the factory example ($n=5$, $p=0.2$), find the probability of **at least one** defective item.

**Solution:**

Direct computation would require summing $P(X=1)$ through $P(X=5)$. The complement is far faster:

$$P(X \geq 1) = 1 - P(X = 0) = 1 - 0.3277 = 0.6723$$

> **Exam shortcut:** "At least one" always equals $1 - P(X=0)$. Compute $P(X=0)$ and subtract from 1. Never sum the remaining terms.

---

### Exercise 6: "At Most" Cumulative Probability

**Problem:** For $X \sim B(6, 0.3)$, find $P(X \leq 2)$.

**Solution:**

$$P(X=0) = \binom{6}{0}(0.3)^0(0.7)^6 = 0.117649$$

$$P(X=1) = \binom{6}{1}(0.3)^1(0.7)^5 = 6 \times 0.3 \times 0.16807 = 0.302526$$

$$P(X=2) = \binom{6}{2}(0.3)^2(0.7)^4 = 15 \times 0.09 \times 0.2401 = 0.324135$$

$$P(X \leq 2) = 0.117649 + 0.302526 + 0.324135 = 0.7443$$

---

### Exercise 7: Working Backwards — Finding $n$

**Problem:** A multiple-choice test has 4 options per question, only one of which is correct. A student guesses randomly. If $E[X] = 5$, how many questions are on the test?

**Solution:**

$$p = \frac{1}{4} = 0.25, \quad E[X] = n \cdot p = 5$$

$$n = \frac{5}{0.25} = 20 \text{ questions}$$

$$V(X) = 20 \times 0.25 \times 0.75 = 3.75$$

---

### Exercise 8: Full Distribution Table Construction

**Problem:** For $X \sim B(4, 0.5)$, construct the full PMF table and verify that it sums to 1.

**Solution:**

| $k$ | $\binom{4}{k}$ | $(0.5)^k$ | $(0.5)^{4-k}$ | $P(X=k)$ |
| :--- | :--- | :--- | :--- | :--- |
| 0 | 1 | 1 | 0.0625 | 0.0625 |
| 1 | 4 | 0.5 | 0.125 | 0.2500 |
| 2 | 6 | 0.25 | 0.25 | 0.3750 |
| 3 | 4 | 0.125 | 0.5 | 0.2500 |
| 4 | 1 | 0.0625 | 1 | 0.0625 |

**Sum:** $0.0625 + 0.2500 + 0.3750 + 0.2500 + 0.0625 = 1.0000$. Verified.

---

### Exercise 9: The Gotcha — "At Least" Requires Careful Indexing

**Problem:** A call centre receives calls independently. The probability that any given call results in a sale is 0.3. In a batch of 10 calls, find the probability that **more than 8 calls** result in a sale.

A student sets up the calculation as:

$$P(X \geq 8) = 1 - P(X \leq 8)$$

Identify the error and compute the correct answer.

**Solution:**

**The error:** The phrase "more than 8" translates to $X > 8$, which is equivalent to $X \geq 9$.

The student wrote $P(X \geq 8) = 1 - P(X \leq 8)$. There are **two simultaneous errors** here:
- **Label error:** The event should be labelled $P(X \geq 9)$, not $P(X \geq 8)$.
- **Formula error for the label used:** If the student truly wanted $P(X \geq 8)$, the correct complement would be $1 - P(X \leq 7)$, not $1 - P(X \leq 8)$.

By coincidence, the formula $1 - P(X \leq 8)$ happens to give the numerically correct answer for the original question ($P(X > 8)$), but the reasoning is wrong because the student is conflating "more than 8" with "at least 8." The correct, unambiguous setup is:

$$P(X > 8) = P(X \geq 9) = 1 - P(X \leq 8)$$

**Correct computation** for $P(X > 8)$ with $X \sim B(10, 0.3)$:

$$P(X = 9) = \binom{10}{9}(0.3)^9(0.7)^1 = 10 \times 0.000019683 \times 0.7 = 0.0001378$$

$$P(X = 10) = \binom{10}{10}(0.3)^{10}(0.7)^0 = 1 \times 0.0000059049 \times 1 = 0.0000059$$

$$P(X > 8) = P(X=9) + P(X=10) \approx 0.0001378 + 0.0000059 = 0.0001437$$

This is an extremely small probability, which makes intuitive sense: achieving 9 or 10 sales when the success probability is only 0.3 is very unlikely over 10 calls.

**Key lesson:** Always translate the English phrase to a mathematical inequality **before** writing a complement expression:

| Phrase | Inequality | Complement Setup |
| :--- | :--- | :--- |
| "more than $k$" | $X > k$ | $1 - P(X \leq k)$ |
| "at least $k$" | $X \geq k$ | $1 - P(X \leq k-1)$ |
| "fewer than $k$" | $X < k$ | $P(X \leq k-1)$ |
| "at most $k$" | $X \leq k$ | Direct sum or table |

---

## Exam Tip: Recognising the Binomial Setup

The words "independent", "fixed number of trials", "probability of success", and "how many" in a problem are strong signals for the Binomial model. The moment you confirm all four FINS conditions, write $X \sim B(n, p)$ explicitly and use $E[X] = np$ and $V(X) = np(1-p)$ without re-deriving them.


# Phase 4.3: Poisson Distribution

The Poisson Distribution models the number of times a **rare event** occurs within a fixed interval of time, space, or volume, given a known average rate. It fills the gap in the discrete distribution toolkit: where the Binomial requires a fixed, finite $n$, the Poisson handles situations where the number of "trials" is very large (or effectively infinite) and the individual probability of each event is very small.

---

## 1. When to Use the Poisson Distribution

Apply the Poisson model when the problem describes:

- A **count** of events (not a proportion or ratio) over a continuous interval.
- A known **average rate** $\lambda$ (lambda) per unit interval.
- Events occur **independently** of each other.
- Events occur **one at a time** (two events cannot happen at the exact same instant).

**Common real-world contexts:**
- Number of phone calls arriving at a switchboard per hour.
- Number of defects per metre of fabric.
- Number of accidents at an intersection per month.
- Number of radioactive particle emissions per second.

---

## 2. The PMF Formula

If $X \sim Po(\lambda)$, the probability of exactly $k$ events is:

$$\boxed{P(X = k) = \frac{\lambda^k \cdot e^{-\lambda}}{k!}, \quad k = 0, 1, 2, 3, \ldots}$$

Where:
- $\lambda > 0$ is the average rate (mean number of events per interval)
- $e \approx 2.71828$ is Euler's number
- $k!$ is the factorial of $k$

The Poisson distribution has **no upper bound** on $k$ — theoretically, any non-negative integer is possible.

---

## 3. Mean and Variance

A defining and elegant property of the Poisson distribution is that **the mean and variance are equal**:

$$\boxed{E[X] = \lambda}$$

$$\boxed{V(X) = \lambda}$$

$$SD(X) = \sqrt{\lambda}$$

If a problem gives you only one value and calls it the "average rate" or "expected number of events", that single value is $\lambda$, and it serves as both the mean and the variance.

---

## 4. Scaling the Rate to a Different Interval

This is one of the most important practical skills for the Poisson distribution. If the rate is given for one interval length but the question asks about a different interval length, scale $\lambda$ proportionally.

**Rule:** If $\lambda$ is the rate per unit time and you want the rate over $t$ units of time:

$$\lambda_t = \lambda \cdot t$$

Then $X_t \sim Po(\lambda \cdot t)$.

**Example:** If calls arrive at 3 per hour ($\lambda = 3$), then over 2 hours the rate is $\lambda_{2h} = 3 \times 2 = 6$.

---

## 5. Poisson as an Approximation to Binomial

When $n$ is large and $p$ is small (rule of thumb: $n \geq 20$ and $p \leq 0.05$), the Binomial distribution $B(n,p)$ is well approximated by $Po(\lambda)$ where:

$$\lambda = n \cdot p$$

This approximation avoids computing large binomial coefficients.

---

## 6. Solved Exercises

### Exercise 1: Basic PMF Calculation

**Problem:** Customers arrive at a bank at an average rate of 4 per hour. Find the probability that exactly 3 customers arrive in a given hour.

**Solution:**

$$X \sim Po(4), \quad P(X=3) = \frac{4^3 \cdot e^{-4}}{3!}$$

$$= \frac{64 \times 0.018316}{6} = \frac{1.17222}{6} \approx 0.1954$$

---

### Exercise 2: Computing $P(X = 0)$

**Problem:** Using the same bank setting ($\lambda = 4$), find the probability that no customers arrive in a given hour.

**Solution:**

$$P(X=0) = \frac{4^0 \cdot e^{-4}}{0!} = \frac{1 \times 0.018316}{1} = 0.0183$$

There is approximately a 1.83% chance of a completely quiet hour.

> **Recall:** $4^0 = 1$ and $0! = 1$. So $P(X=0) = e^{-\lambda}$ always.

---

### Exercise 3: "At Least One" Using the Complement

**Problem:** A Geiger counter detects on average 2 radioactive particles per second. Find the probability of detecting at least one particle in a given second.

**Solution:**

$$X \sim Po(2), \quad P(X \geq 1) = 1 - P(X=0) = 1 - e^{-2}$$

$$P(X \geq 1) = 1 - 0.1353 = 0.8647$$

---

### Exercise 4: Scaling the Interval

**Problem:** A call centre receives calls at an average rate of 5 per hour. Find the probability of receiving exactly 2 calls in a 30-minute window.

**Solution:**

**Step 1:** Convert the rate to the interval of interest.

30 minutes = 0.5 hours, so:

$$\lambda_{30\min} = 5 \times 0.5 = 2.5$$

**Step 2:** Apply the Poisson PMF with $\lambda = 2.5$:

$$P(X=2) = \frac{2.5^2 \cdot e^{-2.5}}{2!} = \frac{6.25 \times 0.082085}{2} = \frac{0.513}{2} \approx 0.2565$$

---

### Exercise 5: Cumulative Probability — "Fewer Than"

**Problem:** For $X \sim Po(3)$, find $P(X < 3)$.

**Solution:**

"Fewer than 3" means $X \leq 2$:

$$P(X=0) = \frac{3^0 e^{-3}}{0!} = e^{-3} \approx 0.049787$$

$$P(X=1) = \frac{3^1 e^{-3}}{1!} = 3e^{-3} \approx 0.149361$$

$$P(X=2) = \frac{3^2 e^{-3}}{2!} = \frac{9e^{-3}}{2} \approx 0.224042$$

$$P(X < 3) = 0.049787 + 0.149361 + 0.224042 = 0.4232$$

---

### Exercise 6: Using Poisson to Approximate Binomial

**Problem:** A manufacturing process produces bolts where the probability of a defect is $p = 0.02$. A batch of 200 bolts is inspected. Approximate the probability of exactly 3 defective bolts using the Poisson distribution.

**Solution:**

**Check conditions:** $n = 200 \geq 20$ and $p = 0.02 \leq 0.05$. Approximation is valid.

$$\lambda = n \cdot p = 200 \times 0.02 = 4$$

$$P(X=3) \approx \frac{4^3 e^{-4}}{3!} = \frac{64 \times 0.018316}{6} \approx 0.1954$$

---

### Exercise 7: Finding $\lambda$ from Given Information

**Problem:** A Poisson random variable $X$ has $V(X) = 6.25$. Find $E[X]$, $P(X=0)$, and $P(X \geq 2)$.

**Solution:**

Since $V(X) = \lambda$ for a Poisson distribution:

$$\lambda = 6.25, \quad E[X] = 6.25$$

$$P(X=0) = e^{-6.25} \approx 0.001930$$

$$P(X=1) = \frac{6.25^1 e^{-6.25}}{1!} = 6.25 \times 0.001930 \approx 0.012063$$

$$P(X \geq 2) = 1 - P(X=0) - P(X=1) = 1 - 0.001930 - 0.012063 = 0.986007$$

---

### Exercise 8: Full Distribution — Comparing Two Intervals

**Problem:** Accidents at a busy intersection follow a Poisson distribution with an average of 6 per month. Management claims that in any given week, the probability of zero accidents is over 20%. Verify this claim.

**Solution:**

**Step 1:** Convert the rate from monthly to weekly.

Assuming a month has approximately 4 weeks:

$$\lambda_{\text{week}} = \frac{6}{4} = 1.5$$

**Step 2:** Compute $P(X=0)$ for a weekly window:

$$P(X=0) = e^{-1.5} \approx 0.2231$$

**Conclusion:** $P(X=0) \approx 22.31\% > 20\%$. The management's claim is **verified**.

---

### Exercise 9: The Gotcha — Rate Change Disguised as a Different Problem

**Problem:** Typos in a manuscript follow a Poisson distribution at a rate of 2 per page. An editor reviews a **half-page excerpt** and then a **full 3-page section** on the same day.

(a) Find the probability of exactly 1 typo in the half-page excerpt.

(b) Find the probability of **at most 2** typos in the 3-page section.

(c) A student argues: "Since we already know there was 1 typo in the half-page, the expected number of typos in the remaining 2.5 pages of the 3-page section is $2 \times 2.5 - 1 = 4$." Identify the error in this reasoning.

**Solution:**

**Part (a): Half-page**

$$\lambda_{0.5} = 2 \times 0.5 = 1$$

$$P(X=1) = \frac{1^1 e^{-1}}{1!} = e^{-1} \approx 0.3679$$

**Part (b): 3-page section**

$$\lambda_3 = 2 \times 3 = 6$$

$$P(X=0) = e^{-6} \approx 0.002479$$

$$P(X=1) = 6e^{-6} \approx 0.014873$$

$$P(X=2) = \frac{36 e^{-6}}{2} \approx 0.044618$$

$$P(X \leq 2) = 0.002479 + 0.014873 + 0.044618 = 0.0620$$

**Part (c): The error**

The student committed two mistakes in one step:

**Mistake 1 — Conditioning on a past outcome:** The Poisson distribution assumes events are **independent**. The outcome in the half-page excerpt has absolutely no effect on the expected count in the remaining pages. You cannot "subtract" a count from one sub-interval when computing the rate for another. Each interval is modelled independently with its own $\lambda$.

**Mistake 2 — Subtracting observed counts from expected rates:** Even if conditioning were valid, subtracting a realised count (1 typo) from an expected rate ($2 \times 2.5 = 5$) confuses two different quantities. The expected number of typos in the remaining 2.5 pages is simply $\lambda_{2.5} = 2 \times 2.5 = 5$, regardless of what was observed anywhere else.

The correct approach treats each interval as an independent Poisson random variable with its own scaled rate. The half-page result is irrelevant to the 3-page section calculation.

---

## 7. Core Formulas Summary

| Formula | Description |
| :--- | :--- |
| $P(X=k) = \frac{\lambda^k e^{-\lambda}}{k!}$ | Poisson PMF |
| $E[X] = \lambda$ | Mean equals rate |
| $V(X) = \lambda$ | Variance equals rate |
| $P(X=0) = e^{-\lambda}$ | Probability of zero events (simplification) |
| $P(X \geq 1) = 1 - e^{-\lambda}$ | At least one event (complement shortcut) |
| $\lambda_t = \lambda \cdot t$ | Rate scaling to a different interval of length $t$ |
| $\lambda \approx n \cdot p$ | Binomial-to-Poisson approximation |

---

## Exam Tip: Always Scale $\lambda$ Before Substituting

The most common Poisson exam error is substituting the wrong rate into the formula. Before writing down the PMF, always ask: "Is the rate given for the same interval length as the question asks about?" If not, scale first. Label your scaled rate explicitly (e.g., $\lambda_{2h} = 6$) to avoid confusion during multi-part problems.


# Phase 4.4: Geometric and Hypergeometric Distributions

This file covers two important discrete distributions: the **Geometric Distribution** (which models the number of trials until the first success) and the **Hypergeometric Distribution** (which models sampling without replacement).

---

## 1. Geometric Distribution ($X \sim Geo(p)$)

The Geometric distribution models the number of independent Bernoulli trials required to obtain the first success. 

> **Critical Exam Gotcha:** There are two common definitions of the Geometric distribution used in university syllabi. Confusing them will lead to wrong formulas for the PMF and expected value. Always check which definition your professor uses.

### Definition A: Counting the Number of Trials ($k = 1, 2, 3, \dots$)
Here, $X$ is the trial number of the first success.
*   **PMF:** $P(X = k) = (1-p)^{k-1} p$
*   **Mean (Expected Value):** $E[X] = \frac{1}{p}$
*   **Variance:** $Var(X) = \frac{1-p}{p^2}$
*   **CDF:** $P(X \le k) = 1 - (1-p)^k$

### Definition B: Counting the Number of Failures Before the First Success ($k = 0, 1, 2, \dots$)
Here, $Y$ is the number of failures before the first success occurs. Note that $Y = X - 1$.
*   **PMF:** $P(Y = k) = (1-p)^k p$
*   **Mean (Expected Value):** $E[Y] = \frac{1-p}{p}$
*   **Variance:** $Var(Y) = \frac{1-p}{p^2}$
*   **CDF:** $P(Y \le k) = 1 - (1-p)^{k+1}$

---

## 2. Hypergeometric Distribution ($X \sim HG(N, K, n)$)

The Hypergeometric distribution models the number of successes in a sample of size $n$ drawn from a finite population of size $N$ containing exactly $K$ successes, **without replacement**.

Unlike the Binomial distribution, the trials are **not independent** because the probability of success changes with each draw.

*   **Parameters:**
    *   $N$: Total population size
    *   $K$: Number of success items in the population
    *   $n$: Number of items drawn (sample size)
    *   $k$: Number of success items in the sample
*   **PMF:**
    $$P(X = k) = \frac{\binom{K}{k} \binom{N-K}{n-k}}{\binom{N}{n}}, \quad \max(0, n - (N - K)) \le k \le \min(n, K)$$
*   **Expected Value:** $E[X] = n \cdot \frac{K}{N}$
*   **Variance:**
    $$Var(X) = n \cdot \frac{K}{N} \cdot \left(1 - \frac{K}{N}\right) \cdot \left(\frac{N - n}{N - 1}\right)$$
    The term $\frac{N-n}{N-1}$ is known as the **finite population correction factor**.

---

## 3. Solved Exercises (10 Examples)

### Exercise 1: Finding first success on a specific trial (Geometric)
**Problem:** A basketball player makes a free throw with probability $p = 0.7$. Find the probability that they make their first successful free throw on their 4th attempt.

**Solution:**
- **Step 1: Identify distribution and parameters.**
  We count the trials, so we use Definition A ($X \sim Geo(0.7)$). We want to find $P(X = 4)$.
- **Step 2: WIP State.**
  Formula: $P(X=4) = (1-p)^{4-1} p = (0.3)^3 \cdot ?$
- **Step 3: Final Calculation.**
  $$P(X=4) = (0.3)^3 \cdot 0.7 = 0.027 \cdot 0.7 = 0.0189.$$

---

### Exercise 2: Rolling a Die (Geometric)
**Problem:** A fair six-sided die is rolled repeatedly. What is the expected number of rolls needed to get the first 6?

**Solution:**
- **Step 1: Identify parameter.**
  Success is rolling a 6, so $p = 1/6$. We are counting the number of rolls (trials), so we use Definition A.
- **Step 2: WIP State.**
  Expected value $E[X] = \frac{1}{?}$
- **Step 3: Final Calculation.**
  $$E[X] = \frac{1}{1/6} = 6 \text{ rolls}.$$

---

### Exercise 3: Cumulative Geometric Probability ("At Most")
**Problem:** A computer system has a 5% chance of crash during a boot sequence. What is the probability that the first crash occurs within the first 3 boots?

**Solution:**
- **Step 1: Define variables.**
  Let $X$ be the boot sequence number of the first crash. $X \sim Geo(0.05)$. We want $P(X \le 3)$.
- **Step 2: WIP State.**
  Use the CDF formula: $P(X \le 3) = 1 - (1-p)^3 = 1 - (0.95)^3 = 1 - ?$
- **Step 3: Final Calculation.**
  $$(0.95)^3 = 0.857375$$
  $$P(X \le 3) = 1 - 0.857375 = 0.142625 \approx 0.1426.$$

---

### Exercise 4: Geometric Complement Rule ("More Than")
**Problem:** A salesman makes a sale with a probability of 0.2 on any call. What is the probability that he needs more than 5 calls to make his first sale?

**Solution:**
- **Step 1: Define target probability.**
  We want $P(X > 5)$, where $X \sim Geo(0.2)$.
- **Step 2: WIP State.**
  The complement rule for "more than $k$ trials" is:
  $$P(X > k) = (1-p)^k$$
  So, $P(X > 5) = (1 - 0.2)^5 = (0.8)^5 = ?$
- **Step 3: Final Calculation.**
  $$P(X > 5) = 0.32768 \approx 0.3277.$$
  *(Exam shortcut: "More than $k$" simply means the first $k$ trials were all failures. So the probability is just $(1-p)^k$. Never sum terms or use the CDF if you can avoid it!)*

---

### Exercise 5: Memoryless Property of Geometric Distribution
**Problem:** A tester is testing chips until a defective one is found. The probability of finding a defect on any chip is $p = 0.1$. If the first 5 chips tested were good, what is the probability that the first defective chip is found on the 8th test?

**Solution:**
- **Step 1: Understand the setup.**
  We want the conditional probability $P(X = 8 | X > 5)$.
- **Step 2: WIP State.**
  By the memoryless property of the Geometric distribution, the fact that 5 trials failed does not affect future trials. Thus, finding the first defect on the 8th trial (which is 3 additional trials) is equivalent to finding the first defect on the 3rd trial starting from scratch:
  $$P(X = 8 | X > 5) = P(X = 3) = (0.9)^2 \cdot ?$$
- **Step 3: Final Calculation.**
  $$P(X=3) = 0.81 \cdot 0.1 = 0.081.$$

---

### Exercise 6: Card Selection (Hypergeometric)
**Problem:** A hand of 5 cards is dealt from a standard deck of 52 cards. What is the probability that the hand contains exactly 3 Aces?

**Solution:**
- **Step 1: Identify population and sample parameters.**
  - Total population $N = 52$
  - Successes in population $K = 4$ (Aces)
  - Sample size $n = 5$
  - Successes in sample $k = 3$
- **Step 2: WIP State.**
  We apply the Hypergeometric PMF:
  $$P(X = 3) = \frac{\binom{K}{k} \binom{N-K}{n-k}}{\binom{N}{n}} = \frac{\binom{4}{3} \binom{48}{2}}{\binom{52}{5}}$$
  - $\binom{4}{3} = 4$
  - $\binom{48}{2} = \frac{48 \cdot 47}{2} = 1128$
  - $\binom{52}{5} = ?$
- **Step 3: Final Calculation.**
  - $\binom{52}{5} = 2,598,960$
  - $P(X=3) = \frac{4 \cdot 1128}{2,598,960} = \frac{4512}{2,598,960} \approx 0.001736$.

---

### Exercise 7: Quality Control (Hypergeometric)
**Problem:** A box contains 20 components, of which 4 are defective. An engineer randomly selects 5 components without replacement. Find the probability that no defective components are in the sample.

**Solution:**
- **Step 1: Map parameters.**
  - Population $N = 20$, Defectives (successes) $K = 4$, Sample size $n = 5$.
  - We want $P(X = 0)$ successes in the sample.
- **Step 2: WIP State.**
  $$P(X = 0) = \frac{\binom{4}{0} \binom{16}{5}}{\binom{20}{5}} = \frac{1 \cdot \frac{16!}{5! \cdot 11!}}{\frac{20!}{5! \cdot 15!}} = \frac{4368}{?}$$
- **Step 3: Final Calculation.**
  - $\binom{20}{5} = 15,504$
  - $P(X = 0) = \frac{4368}{15,504} \approx 0.2817$.

---

### Exercise 8: Expected Value & Variance of Hypergeometric
**Problem:** Using the same quality control setup from Exercise 7 ($N=20, K=4, n=5$), calculate the expected number of defective components in the sample and the variance.

**Solution:**
- **Step 1: Calculate Mean.**
  $$E[X] = n \cdot \frac{K}{N} = 5 \cdot \frac{4}{20} = 1$$
- **Step 2: WIP State for Variance.**
  $$Var(X) = n \cdot \frac{K}{N} \cdot \left(1 - \frac{K}{N}\right) \cdot \left(\frac{N - n}{N - 1}\right)$$
  $$Var(X) = 5 \cdot \frac{4}{20} \cdot \left(1 - \frac{4}{20}\right) \cdot \left(\frac{20 - 5}{20 - 1}\right) = 1 \cdot 0.8 \cdot \frac{15}{?}$$
- **Step 3: Final Calculation.**
  $$Var(X) = 0.8 \cdot \frac{15}{19} = \frac{12}{19} \approx 0.6316.$$

---

### Exercise 9: Hypergeometric vs. Binomial Approximation
**Problem:** A batch of 1000 items contains 100 defective items. If a sample of 10 items is selected without replacement, find the exact probability of getting exactly 1 defective item using the Hypergeometric distribution, and compare it to the Binomial approximation.

**Solution:**
- **Step 1: Exact Hypergeometric calculation.**
  $N = 1000, K = 100, n = 10, k = 1$.
  $$P(X = 1) = \frac{\binom{100}{1} \binom{900}{9}}{\binom{1000}{10}} \approx 0.3899$$
- **Step 2: WIP State for Binomial approximation.**
  Since the population $N$ is very large compared to the sample size $n$ ($n/N = 10/1000 = 0.01 \le 0.05$), we can approximate this using a Binomial model with $p = K/N = 0.1$.
  $$Y \sim B(10, 0.1)$$
  $$P(Y = 1) = \binom{10}{1} (0.1)^1 (0.9)^9 = 10 \cdot 0.1 \cdot ?$$
- **Step 3: Final Calculation.**
  $$(0.9)^9 = 0.38742$$
  $$P(Y=1) = 1 \cdot 0.38742 = 0.3874$$
  **Comparison:** The difference is very small ($0.3899 - 0.3874 = 0.0025$). This illustrates why the Binomial approximation is highly accurate when the sample is less than 5% of the population.

---

### Exercise 10: Cumulative Hypergeometric ("At Least")
**Problem:** A bag contains 6 red marbles and 4 blue marbles. A child draws 3 marbles at random without replacement. Find the probability of getting at least 2 red marbles.

**Solution:**
- **Step 1: Map variables.**
  - Population $N = 10$, Red Marbles $K = 6$, Sample size $n = 3$.
  - We want $P(X \ge 2) = P(X = 2) + P(X = 3)$.
- **Step 2: WIP State.**
  - $P(X=2) = \frac{\binom{6}{2} \binom{4}{1}}{\binom{10}{3}} = \frac{15 \cdot 4}{120} = \frac{60}{120} = 0.5$
  - $P(X=3) = \frac{\binom{6}{3} \binom{4}{0}}{\binom{10}{3}} = \frac{20 \cdot 1}{?}$
- **Step 3: Final Calculation.**
  - $P(X=3) = \frac{20}{120} \approx 0.1667$.
  - $P(X \ge 2) = 0.5 + 0.1667 = 0.6667$.


# Phase 4.5: Moment Generating Functions and Characteristic Functions

This file introduces **Moment Generating Functions (MGFs)** and **Characteristic Functions**, which are powerful tools for finding moments (mean, variance, etc.) and identifying the distributions of sums of independent random variables.

---

## 1. Moment Generating Function (MGF)

### 1.1 Definition
The Moment Generating Function $M_X(t)$ of a random variable $X$ is defined for all real values of $t$ for which the expected value exists in an open interval around $t = 0$:

$$M_X(t) = E\left[e^{tX}\right]$$

*   **Discrete RV:** $M_X(t) = \sum_{x} e^{tx} \cdot P(X = x)$
*   **Continuous RV:** $M_X(t) = \int_{-\infty}^{\infty} e^{tx} \cdot f(x) \, dx$

### 1.2 Finding Moments via Differentiation
The term "moment generating" comes from the fact that we can generate any $n$-th raw moment $E[X^n]$ by taking the $n$-th derivative of $M_X(t)$ with respect to $t$ and evaluating it at $t = 0$:

$$E[X^n] = \left. \frac{d^n}{dt^n} M_X(t) \right|_{t=0} = M_X^{(n)}(0)$$

Specifically:
*   **Mean:** $E[X] = M'_X(0)$
*   **Variance:** $Var(X) = E[X^2] - (E[X])^2 = M''_X(0) - (M'_X(0))^2$

### 1.3 Key Properties
1.  **Linear Transformation:** If $Y = aX + b$, then:
    $$M_Y(t) = M_{aX+b}(t) = e^{bt} \cdot M_X(at)$$
2.  **Sum of Independent RVs:** If $X$ and $Y$ are independent random variables, the MGF of their sum is the product of their individual MGFs:
    $$M_{X+Y}(t) = M_X(t) \cdot M_Y(t)$$
3.  **Uniqueness Theorem:** If two random variables have the same MGF in an interval containing 0, they have the exact same probability distribution.

---

## 2. Common MGFs

| Distribution | parameters | MGF $M_X(t)$ |
| :--- | :--- | :--- |
| **Bernoulli** | $p$ | $q + p e^t \quad (\text{where } q = 1-p)$ |
| **Binomial** | $n, p$ | $(q + p e^t)^n$ |
| **Poisson** | $\lambda$ | $e^{\lambda (e^t - 1)}$ |
| **Geometric** (Definition A) | $p$ | $\frac{p e^t}{1 - q e^t} \quad (\text{for } t < -\ln q)$ |
| **Exponential** | $\lambda$ | $\frac{\lambda}{\lambda - t} \quad (\text{for } t < \lambda)$ |
| **Normal** | $\mu, \sigma^2$ | $e^{\mu t + \frac{1}{2}\sigma^2 t^2}$ |

---

## 3. Characteristic Function ($\phi_X(t)$)

The MGF of a random variable might not exist if the integral or sum does not converge for $t \neq 0$ (e.g., Cauchy distribution). To guarantee existence, we define the **Characteristic Function** using complex numbers:

$$\phi_X(t) = E\left[e^{itX}\right] = E[\cos(tX)] + i \cdot E[\sin(tX)]$$

Since $|e^{itX}| = 1$ for all real $t$ and $X$, the expectation $\phi_X(t)$ is **guaranteed to exist** for all random variables. The properties of characteristic functions are identical to MGFs, replacing $t$ with $it$.

---

## 4. Solved Exercises (9 Examples)

### Exercise 1: Finding moments from an MGF
**Problem:** The MGF of a random variable $X$ is $M_X(t) = \frac{1}{1 - 2t}$ for $t < 0.5$. Find the mean and variance of $X$.

**Solution:**
- **Step 1: Compute the first derivative.**
  $$M_X(t) = (1 - 2t)^{-1}$$
  $$M'_X(t) = -1 \cdot (1 - 2t)^{-2} \cdot (-2) = 2 \cdot (1 - 2t)^{-2}$$
- **Step 2: WIP State for mean.**
  Evaluate at $t=0$:
  $$E[X] = M'_X(0) = 2 \cdot (1 - 0)^{-2} = ?$$
- **Step 3: Compute the second derivative and variance.**
  - Mean $E[X] = 2$.
  - Second derivative:
    $$M''_X(t) = 2 \cdot (-2) \cdot (1 - 2t)^{-3} \cdot (-2) = 8 \cdot (1 - 2t)^{-3}$$
  - Evaluate at $t=0$: $E[X^2] = M''_X(0) = 8 \cdot (1)^{-3} = 8$.
  - Variance:
    $$Var(X) = E[X^2] - (E[X])^2 = 8 - 2^2 = 8 - 4 = 4.$$

---

### Exercise 2: Deriving the MGF of a Bernoulli Distribution
**Problem:** Derive the MGF of a Bernoulli random variable $X$ with success probability $p$.

**Solution:**
- **Step 1: Set up the sum.**
  A Bernoulli variable takes value 1 with probability $p$ and 0 with probability $q = 1-p$.
- **Step 2: WIP State.**
  $$M_X(t) = E\left[e^{tX}\right] = e^{t(0)} \cdot P(X=0) + e^{t(1)} \cdot P(X=1) = 1 \cdot q + ?$$
- **Step 3: Final Calculation.**
  $$M_X(t) = q + p e^t.$$

---

### Exercise 3: Sum of Independent Poissons
**Problem:** Let $X \sim Po(\lambda_1)$ and $Y \sim Po(\lambda_2)$ be independent random variables. Find the distribution of $W = X + Y$.

**Solution:**
- **Step 1: Set up the MGF multiplication.**
  Since $X$ and $Y$ are independent, $M_W(t) = M_X(t) \cdot M_Y(t)$.
- **Step 2: WIP State.**
  $$M_X(t) = e^{\lambda_1 (e^t - 1)}, \quad M_Y(t) = e^{\lambda_2 (e^t - 1)}$$
  $$M_W(t) = e^{\lambda_1 (e^t - 1)} \cdot e^{\lambda_2 (e^t - 1)} = e^{?}$$
- **Step 3: Final Calculation.**
  $$M_W(t) = e^{(\lambda_1 + \lambda_2)(e^t - 1)}$$
  By the uniqueness theorem, this is the MGF of a Poisson distribution with parameter $\lambda_1 + \lambda_2$.
  Thus, $W \sim Po(\lambda_1 + \lambda_2)$.

---

### Exercise 4: MGF Linear Transformation
**Problem:** If $X$ has MGF $M_X(t) = e^{2t + 8t^2}$, find the MGF of $Y = 3X - 5$.

**Solution:**
- **Step 1: Use the linear transformation formula.**
  $$M_Y(t) = e^{-5t} \cdot M_X(3t)$$
- **Step 2: WIP State.**
  Substitute $3t$ for $t$ in $M_X(t)$:
  $$M_X(3t) = e^{2(3t) + 8(3t)^2} = e^{6t + 8(9t^2)} = e^{6t + ?}$$
- **Step 3: Final Calculation.**
  $$M_X(3t) = e^{6t + 72t^2}$$
  $$M_Y(t) = e^{-5t} \cdot e^{6t + 72t^2} = e^{(-5t + 6t + 72t^2)} = e^{t + 72t^2}$$
  *(Exam note: Since the MGF of a normal variable is $e^{\mu t + \frac{1}{2}\sigma^2 t^2}$, this proves $Y \sim N(1, 144)$ because $\mu = 1$ and $\frac{1}{2}\sigma^2 = 72 \Rightarrow \sigma^2 = 144$.)*

---

### Exercise 5: Expected value from discrete probability generating MGF
**Problem:** A discrete random variable $X$ has PMF $P(X=1) = 0.2$, $P(X=2) = 0.5$, $P(X=3) = 0.3$. Write its MGF and compute the mean.

**Solution:**
- **Step 1: Write the MGF expression.**
  $$M_X(t) = \sum e^{tx} P(X=x) = 0.2 e^t + 0.5 e^{2t} + 0.3 e^{3t}$$
- **Step 2: WIP State for derivative.**
  $$M'_X(t) = \frac{d}{dt}\left(0.2 e^t + 0.5 e^{2t} + 0.3 e^{3t}\right) = 0.2 e^t + 1.0 e^{2t} + ?$$
- **Step 3: Final Calculation.**
  $$M'_X(t) = 0.2 e^t + 1.0 e^{2t} + 0.9 e^{3t}$$
  Evaluate at $t=0$:
  $$E[X] = M'_X(0) = 0.2 + 1.0 + 0.9 = 2.1.$$

---

### Exercise 6: Sum of Independent Binomials
**Problem:** Let $X \sim B(n, p)$ and $Y \sim B(m, p)$ be independent random variables. Find the distribution of $W = X + Y$.

**Solution:**
- **Step 1: Recall MGF formulas.**
  $$M_X(t) = (q + p e^t)^n, \quad M_Y(t) = (q + p e^t)^m$$
- **Step 2: WIP State.**
  $$M_W(t) = M_X(t) \cdot M_Y(t) = (q + p e^t)^n \cdot (q + p e^t)^m = (q + p e^t)^{?}$$
- **Step 3: Final Calculation.**
  $$M_W(t) = (q + p e^t)^{n+m}$$
  By the uniqueness theorem, this matches the MGF of a Binomial distribution with parameters $n+m$ and $p$.
  Thus, $W \sim B(n + m, p)$.
  *(Warning: This property ONLY holds if the success probability $p$ is identical for both variables!)*

---

### Exercise 7: Deriving Exponential MGF
**Problem:** Derive the MGF of $X \sim Exp(\lambda)$.

**Solution:**
- **Step 1: Set up the integral.**
  The PDF is $f(x) = \lambda e^{-\lambda x}$ for $x \ge 0$.
  $$M_X(t) = \int_{0}^{\infty} e^{tx} \cdot \lambda e^{-\lambda x} \, dx = \lambda \int_{0}^{\infty} e^{(t - \lambda)x} \, dx$$
- **Step 2: WIP State.**
  Evaluate the integral (assuming $t < \lambda$ for convergence):
  $$\int_{0}^{\infty} e^{(t - \lambda)x} \, dx = \left[ \frac{e^{(t - \lambda)x}}{t - \lambda} \right]_{0}^{\infty} = 0 - \frac{1}{?}$$
- **Step 3: Final Calculation.**
  $$\text{Denominator} = t - \lambda$$
  $$M_X(t) = \lambda \cdot \left( \frac{-1}{t - \lambda} \right) = \frac{\lambda}{\lambda - t} \quad (\text{for } t < \lambda).$$

---

### Exercise 8: Expansion of MGF to find moments
**Problem:** If the MGF of $X$ is $M_X(t) = e^{t^2/2}$, find $E[X^4]$ using Taylor expansion.

**Solution:**
- **Step 1: Recall the Taylor series for $e^u$.**
  $$e^u = 1 + u + \frac{u^2}{2!} + \frac{u^3}{3!} + \dots$$
- **Step 2: WIP State.**
  Substitute $u = t^2/2$:
  $$M_X(t) = 1 + \left(\frac{t^2}{2}\right) + \frac{\left(\frac{t^2}{2}\right)^2}{2!} + \frac{\left(\frac{t^2}{2}\right)^3}{3!} + \dots$$
  $$M_X(t) = 1 + \frac{t^2}{2} + \frac{t^4}{8} + \dots$$
  Recall the general definition of MGF as a power series of moments:
  $$M_X(t) = \sum_{k=0}^{\infty} \frac{E[X^k]}{k!} t^k = 1 + E[X]t + \frac{E[X^2]}{2!} t^2 + \frac{E[X^3]}{3!} t^3 + \frac{E[X^4]}{4!} t^4 + \dots$$
- **Step 3: Final Calculation.**
  Compare coefficients of $t^4$:
  $$\frac{E[X^4]}{4!} = \frac{1}{8} \implies E[X^4] = \frac{4!}{8} = \frac{24}{8} = 3.$$

---

### Exercise 9: Characteristic function of a symmetric distribution
**Problem:** Show that if a random variable $X$ is symmetric about 0 (i.e. $X$ and $-X$ have the same distribution), then its characteristic function $\phi_X(t)$ is purely real.

**Solution:**
- **Step 1: Relate $\phi_X(t)$ to $\phi_{-X}(t)$.**
  $$\phi_{-X}(t) = E\left[e^{it(-X)}\right] = \phi_X(-t)$$
- **Step 2: WIP State.**
  Since $X$ is symmetric, $X \sim -X$, meaning their characteristic functions must be identical:
  $$\phi_X(t) = \phi_{-X}(t) \implies \phi_X(t) = \phi_X(-t)$$
  Also, recall that the complex conjugate is:
  $$\overline{\phi_X(t)} = \overline{E[\cos(tX) + i\sin(tX)]} = E[\cos(tX)] - i E[\sin(tX)] = \phi_X(-t)$$
- **Step 3: Final Calculation.**
  Combining these yields:
  $$\overline{\phi_X(t)} = \phi_X(t)$$
  Any complex number equal to its own conjugate must be purely real. Thus, $\phi_X(t)$ is purely real (and specifically, $E[\sin(tX)] = 0$).
