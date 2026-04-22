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
