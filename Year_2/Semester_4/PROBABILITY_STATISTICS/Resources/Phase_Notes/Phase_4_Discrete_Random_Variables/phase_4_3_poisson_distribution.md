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
