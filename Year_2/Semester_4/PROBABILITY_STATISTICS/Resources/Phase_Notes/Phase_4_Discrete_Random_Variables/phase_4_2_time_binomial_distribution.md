# Phase 4.2 (Time): Binomial Distribution in Discrete Time Slots

The Binomial Distribution models the number of successful events (e.g., successful packet transmissions, health check passes, queue completions) occurring across a fixed sequence of **$n$ discrete time slots** of equal duration $\Delta t$.

---

## 1. The Four Conditions in Time Slot Context (FINS)

A discrete time random variable $X$ (count of active or successful time slots) follows $X \sim B(n, p)$ if and only if:

1. **F**ixed number of time slots: $n$ discrete time intervals of length $\Delta t$ are monitored. Total monitoring window $T_{\text{total}} = n \cdot \Delta t$.
2. **I**ndependence: Events in one time slot do not affect subsequent time slots.
3. **N**o more than two outcomes: Each time slot is classified as either a "success" (event occurred) or "failure" (event did not occur).
4. **S**ame probability: Probability $p$ of success is constant in every time slot.

---

## 2. PMF Formula, Mean, and Variance

If $X \sim B(n, p)$, the probability of observing exactly $k$ successful time slots out of $n$ is:

$$\boxed{P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}, \quad k = 0, 1, 2, \ldots, n}$$

Where:
* $n$ = total number of discrete time slots
* $k$ = number of successful time slots
* $p$ = probability of success in a single time slot
* $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ = binomial coefficient

### Mean and Variance of Active Time Slots
$$\boxed{E[X] = n \cdot p}$$

$$\boxed{V(X) = n \cdot p \cdot (1-p)}$$

$$SD(X) = \sqrt{n \cdot p \cdot (1-p)}$$

---

## 3. Time-Specific Gotchas

### Gotcha 1: Conflating Time Slot Count $n$ with Total Duration $T_{\text{total}}$
In time-based problems, $n$ is the **count of discrete slots**, not the total elapsed time. If monitoring runs for 2 hours ($T_{\text{total}} = 120\text{ minutes}$) using 5-minute time slots, the number of trials is $n = 120 / 5 = 24$ slots, **not** 120 or 2.

### Gotcha 2: Time-Varying Probability $p$ (Non-Constant Rate)
If network congestion causes $p$ to drop during peak hours (e.g., $p = 0.9$ in slot 1, but $p = 0.5$ in slot 10), the **S** condition of FINS fails. The process can no longer be modeled using a standard Binomial distribution.

### Gotcha 3: Indexing Errors for Time Threshold Keywords

| English Phrase | Inequality | Complement Setup |
| :--- | :--- | :--- |
| "more than $k$ time slots" | $X > k \iff X \ge k+1$ | $1 - P(X \le k)$ |
| "at least $k$ time slots" | $X \ge k$ | $1 - P(X \le k-1)$ |
| "fewer than $k$ time slots" | $X < k \iff X \le k-1$ | $P(X \le k-1)$ |
| "at most $k$ time slots" | $X \le k$ | Direct sum or CDF |

---

## 4. Solved Exercises (10 Examples)

### Exercise 1: Identifying Parameters in Network Time Slots
**Problem:** A router transmits over $n = 8$ discrete time slots of 100 ms each. The probability of error-free transmission per slot is $p = 0.90$. Verify FINS conditions and compute $E[X]$ and $V(X)$.

**Solution:**
- **Fixed $n$:** $n = 8$ slots. Passed.
- **Independence:** Non-overlapping slots. Passed.
- **Two outcomes:** Error-free or Error. Passed.
- **Constant $p$:** $p = 0.90$. Passed.
- **Calculations:**
  $$E[X] = n \cdot p = 8 \cdot 0.90 = 7.2\text{ slots}$$
  $$V(X) = n \cdot p(1-p) = 8 \cdot 0.90 \cdot 0.10 = 0.72\text{ slots}^2$$

---

### Exercise 2: Computing PMF for Exact Number of Time Slots
**Problem:** A factory quality sensor inspects 5 time slots. The probability of detecting a bottleneck in any single slot is $p = 0.20$. Find the probability of a bottleneck in exactly 2 time slots.

**Solution:**
- **Step 1: Set up PMF formula ($X \sim B(5, 0.20)$).**
  $$P(X=2) = \binom{5}{2} (0.20)^2 (0.80)^3$$
- **Step 2: WIP State.**
  $$\binom{5}{2} = 10$$
  $$P(X=2) = 10 \cdot 0.04 \cdot ?$$
- **Step 3: Final Calculation.**
  $$(0.80)^3 = 0.512$$
  $$P(X=2) = 10 \cdot 0.04 \cdot 0.512 = 0.2048$$

---

### Exercise 3: Zero Outage Time Slots ($P(X=0)$)
**Problem:** A web server checks system health every minute for $n=6$ minutes. Probability of an outage per minute is $p=0.05$. Find the probability of zero outages in all 6 minutes.

**Solution:**
- **Step 1: Apply $P(X=0) = (1-p)^n$.**
  $$P(X=0) = \binom{6}{0} (0.05)^0 (0.95)^6 = 1 \cdot 1 \cdot (0.95)^6$$
- **Step 2: WIP State.**
  $$(0.95)^6 = ?$$
- **Step 3: Final Calculation.**
  $$P(X=0) = 0.7351 \text{ (73.51\%)}$$

---

### Exercise 4: Perfect Reliability ($P(X=n)$)
**Problem:** Find the probability that all $n=6$ time slots in Exercise 3 experience outages ($p=0.05$).

**Solution:**
- **Step 1: Apply $P(X=n) = p^n$.**
  $$P(X=6) = \binom{6}{6} (0.05)^6 (0.95)^0 = (0.05)^6$$
- **Step 2: WIP State.**
  $$(0.05)^6 = ?$$
- **Step 3: Final Calculation.**
  $$P(X=6) = 0.000000015625 \text{ (Extremely unlikely)}$$

---

### Exercise 5: "At Least One" Failed Time Slot
**Problem:** Using the health check scenario ($n=6, p=0.05$), find the probability of at least 1 outage time slot.

**Solution:**
- **Step 1: Apply complement rule.**
  $$P(X \ge 1) = 1 - P(X=0)$$
- **Step 2: WIP State.**
  From Ex 3, $P(X=0) = 0.7351$.
  $$P(X \ge 1) = 1 - 0.7351 = ?$$
- **Step 3: Final Calculation.**
  $$P(X \ge 1) = 0.2649 \text{ (26.49\%)}$$

---

### Exercise 6: Cumulative Time Slot Probability ("At Most 2")
**Problem:** For $X \sim B(4, 0.30)$ active processing time slots, find $P(X \le 2)$.

**Solution:**
- **Step 1: Sum $P(X=0) + P(X=1) + P(X=2)$.**
  $$P(X=0) = (0.70)^4 = 0.2401$$
  $$P(X=1) = \binom{4}{1}(0.30)^1(0.70)^3 = 4 \cdot 0.30 \cdot 0.343 = 0.4116$$
  $$P(X=2) = \binom{4}{2}(0.30)^2(0.70)^2 = 6 \cdot 0.09 \cdot 0.49 = 0.2646$$
- **Step 2: WIP State.**
  $$P(X \le 2) = 0.2401 + 0.4116 + ?$$
- **Step 3: Final Calculation.**
  $$P(X \le 2) = 0.2401 + 0.4116 + 0.2646 = 0.9163$$

---

### Exercise 7: Working Backwards to Find Number of Time Slots $n$
**Problem:** In a database ping setup, each slot has success probability $p = 0.25$. If the expected number of successful pings is $E[X] = 10$, how many time slots $n$ were monitored?

**Solution:**
- **Step 1: Set up mean equation.**
  $$E[X] = n \cdot p \implies 10 = n \cdot 0.25$$
- **Step 2: WIP State.**
  $$n = \frac{10}{0.25} = ?$$
- **Step 3: Final Calculation.**
  $$n = 40 \text{ time slots}$$
  Variance: $V(X) = 40 \cdot 0.25 \cdot 0.75 = 7.5\text{ slots}^2$.

---

### Exercise 8: Constructing Full PMF Table for 4 Time Slots
**Problem:** Construct the complete PMF table for $X \sim B(4, 0.50)$ active time slots.

**Solution:**

| $k$ | $\binom{4}{k}$ | $(0.5)^k$ | $(0.5)^{4-k}$ | $P(X=k)$ |
| :--- | :---: | :---: | :---: | :---: |
| 0 | 1 | 1 | 0.0625 | 0.0625 |
| 1 | 4 | 0.5 | 0.125 | 0.2500 |
| 2 | 6 | 0.25 | 0.25 | 0.3750 |
| 3 | 4 | 0.125 | 0.5 | 0.2500 |
| 4 | 1 | 0.0625 | 1 | 0.0625 |

Sum check: $0.0625 + 0.2500 + 0.3750 + 0.2500 + 0.0625 = 1.0000$. Verified.

---

### Exercise 9: Gotcha Check -- "More Than 8 Time Slots"
**Problem:** In $n=10$ time slots with success probability $p=0.30$, a developer sets up $P(X > 8) = 1 - P(X \le 8)$. Compute the exact value of $P(X > 8) = P(X=9) + P(X=10)$.

**Solution:**
- **Step 1: Evaluate $P(X=9)$ and $P(X=10)$.**
  $$P(X=9) = \binom{10}{9} (0.30)^9 (0.70)^1 = 10 \cdot (0.000019683) \cdot 0.70 = 0.0001378$$
  $$P(X=10) = \binom{10}{10} (0.30)^{10} (0.70)^0 = 1 \cdot (0.0000059049) \cdot 1 = 0.0000059$$
- **Step 2: WIP State.**
  $$P(X > 8) = 0.0001378 + ?$$
- **Step 3: Final Calculation.**
  $$P(X > 8) = 0.0001378 + 0.0000059 = 0.0001437$$

---

### Exercise 10: R Code Snippet -- Time Slot Reliability with `dbinom` and `pbinom`
**Problem:** Write R code to compute PMF values, cumulative probabilities, and plot the PMF for $X \sim B(20, 0.15)$ failed time slots.

**Solution:**

```r
# Binomial Parameters for time slots
n_slots <- 20
p_fail <- 0.15

# Probability of exactly 3 failed time slots
p_exact_3 <- dbinom(3, size = n_slots, prob = p_fail)

# Probability of at most 3 failed time slots P(X <= 3)
p_at_most_3 <- pbinom(3, size = n_slots, prob = p_fail)

# Probability of more than 5 failed time slots P(X > 5)
p_more_than_5 <- 1 - pbinom(5, size = n_slots, prob = p_fail)

cat("P(X = 3 failed slots):", round(p_exact_3, 4), "\n")
cat("P(X <= 3 failed slots):", round(p_at_most_3, 4), "\n")
cat("P(X > 5 failed slots):", round(p_more_than_5, 4), "\n")
```

**Interpretation of Output:**
Functions `dbinom` (density/PMF) and `pbinom` (CDF) evaluate exact time-slot probabilities without manual factorial computations.
