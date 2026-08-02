# Phase 4.3 (Time): Poisson Distribution Across Time Windows

The Poisson Distribution models the count of rare, independent events occurring within a fixed **time window** $[0, t]$ at a constant average rate $\lambda$ per unit time.

---

## 1. When to Use the Poisson Model in Time Contexts

Apply the Poisson distribution when:
1. The random variable $X$ represents a **count of events** occurring during a continuous or discrete time interval $t$.
2. Events occur at a known **average rate $\lambda$** per unit time (e.g., requests/sec, failures/hour, calls/min).
3. **Independent Increments:** The number of events in non-overlapping time intervals are independent.
4. **Orderliness:** Events occur one at a time (the probability of two events occurring at the exact same millisecond is zero).

---

## 2. PMF Formula, Rate Scaling, Mean, and Variance

If events occur at rate $\lambda$ per unit time, then over a time window of length $t$, the scaled rate is:

$$\boxed{\lambda_t = \lambda \cdot t}$$

The probability of observing exactly $k$ events during time window $t$ is:

$$\boxed{P(X_t = k) = \frac{(\lambda \cdot t)^k \cdot e^{-\lambda \cdot t}}{k!}, \quad k = 0, 1, 2, 3, \ldots}$$

Where:
* $\lambda_t = \lambda \cdot t$ is the expected number of events in window $t$
* $e \approx 2.71828$ is Euler's constant
* $k!$ is the factorial of $k$

### Equal Mean and Variance Property
For a Poisson random variable, the mean and variance are **identically equal to the scaled rate**:

$$\boxed{E[X_t] = \lambda_t = \lambda \cdot t}$$

$$\boxed{V(X_t) = \lambda_t = \lambda \cdot t}$$

$$SD(X_t) = \sqrt{\lambda \cdot t}$$

---

## 3. Time-Specific Gotchas

### Gotcha 1: Scaling Rate $\lambda$ Incorrectly Across Time Windows
The single most frequent Poisson error is substituting a rate given in one time unit into a window of a different time unit without scaling. 
* *Wrong:* Given rate $\lambda = 120\text{ requests/hour}$, calculating $P(X = 2)$ in a 1-minute window using $\lambda = 120$.
* *Right:* First convert rate to minutes: $\lambda_{1\min} = 120 / 60 = 2\text{ requests/minute}$. Then use $\lambda = 2$.

### Gotcha 2: Confusing Discrete Time Ticks with Continuous Duration
Do not confuse discrete time ticks $n$ (used in Binomial or Geometric models) with continuous Poisson time duration $t$. In a Poisson process, $t$ can be any positive real number (e.g., $t = 0.35\text{ seconds}$).

### Gotcha 3: Memorylessness and Conditioning on Past Time Intervals
Due to **independent increments**, observing 10 events in the first 5 minutes provides **zero information** about the number of events in the next 5 minutes. The rate for the second window remains $\lambda \cdot t$. Never subtract past observed counts from future rates!

---

## 4. Solved Exercises (10 Examples)

### Exercise 1: Basic Arrival Count in 1 Hour Window
**Problem:** Server API calls arrive at a Poisson rate of $\lambda = 4$ requests per hour. Find the probability of receiving exactly 3 requests in a 1-hour window.

**Solution:**
- **Step 1: Identify $\lambda_t$.** Here $t = 1\text{ hour}$, so $\lambda_1 = 4$.
- **Step 2: WIP State.**
  $$P(X=3) = \frac{4^3 \cdot e^{-4}}{3!} = \frac{64 \cdot e^{-4}}{6}$$
  $$e^{-4} \approx 0.0183156$$
- **Step 3: Final Calculation.**
  $$P(X=3) = \frac{64 \cdot 0.0183156}{6} = \frac{1.1722}{6} \approx 0.1954 \text{ (19.54\%)}$$

---

### Exercise 2: Zero Outages in Time Window ($P(X=0)$)
**Problem:** Power grid fluctuations occur at a rate of $\lambda = 0.5$ per day. Find the probability of zero fluctuations over a 3-day window.

**Solution:**
- **Step 1: Scale rate to 3 days.**
  $$\lambda_{\text{3days}} = 0.5 \times 3 = 1.5$$
- **Step 2: WIP State.**
  $$P(X=0) = \frac{(1.5)^0 \cdot e^{-1.5}}{0!} = \frac{1 \cdot e^{-1.5}}{1} = e^{-1.5}$$
- **Step 3: Final Calculation.**
  $$P(X=0) = e^{-1.5} \approx 0.2231 \text{ (22.31\%)}$$

---

### Exercise 3: "At Least One" Event Using Complement
**Problem:** Network interrupts occur at a rate of $\lambda = 2$ per second. Find the probability of at least one interrupt in a 1-second window.

**Solution:**
- **Step 1: Set up complement formula.**
  $$P(X \ge 1) = 1 - P(X=0) = 1 - e^{-\lambda_t}$$
- **Step 2: WIP State.**
  $\lambda_1 = 2$, so $P(X=0) = e^{-2} \approx 0.135335$.
  $$P(X \ge 1) = 1 - 0.135335 = ?$$
- **Step 3: Final Calculation.**
  $$P(X \ge 1) = 0.8647 \text{ (86.47\%)}$$

---

### Exercise 4: Scaling Rate from Hours to Minutes
**Problem:** Database queries arrive at $\lambda = 6$ per hour. Find the probability of receiving exactly 2 queries in a 30-minute window.

**Solution:**
- **Step 1: Scale rate to 30 minutes ($t = 0.5\text{ hours}$).**
  $$\lambda_{30\min} = 6 \times 0.5 = 3$$
- **Step 2: WIP State.**
  $$P(X=2) = \frac{3^2 \cdot e^{-3}}{2!} = \frac{9 \cdot e^{-3}}{2}$$
  $$e^{-3} \approx 0.049787$$
- **Step 3: Final Calculation.**
  $$P(X=2) = \frac{9 \cdot 0.049787}{2} = \frac{0.44808}{2} = 0.2240 \text{ (22.40\%)}$$

---

### Exercise 5: Scaling Rate from Seconds to Milliseconds
**Problem:** High-frequency trading packet arrivals occur at $\lambda = 2000$ per second. Find the probability of receiving exactly 10 packets in a 5-millisecond window.

**Solution:**
- **Step 1: Convert rate to milliseconds.**
  $5\text{ ms} = 0.005\text{ seconds}$.
  $$\lambda_{5\text{ms}} = 2000 \times 0.005 = 10$$
- **Step 2: WIP State.**
  $$P(X=10) = \frac{10^{10} \cdot e^{-10}}{10!}$$
  $$10! = 3,628,800, \quad e^{-10} \approx 0.0000453999$$
- **Step 3: Final Calculation.**
  $$P(X=10) = \frac{10,000,000,000 \cdot 0.0000453999}{3,628,800} = \frac{453,999}{3,628,800} \approx 0.1251 \text{ (12.51\%)}$$

---

### Exercise 6: Cumulative Probability -- "Fewer Than 3 Arrivals"
**Problem:** For Poisson arrivals with $\lambda_t = 3$, find $P(X < 3)$.

**Solution:**
- **Step 1: $P(X < 3) = P(X=0) + P(X=1) + P(X=2)$.**
  $$P(X=0) = e^{-3} \approx 0.049787$$
  $$P(X=1) = 3e^{-3} \approx 0.149361$$
  $$P(X=2) = \frac{9}{2}e^{-3} \approx 0.224042$$
- **Step 2: WIP State.**
  $$P(X < 3) = 0.049787 + 0.149361 + ?$$
- **Step 3: Final Calculation.**
  $$P(X < 3) = 0.049787 + 0.149361 + 0.224042 = 0.4232 \text{ (42.32\%)}$$

---

### Exercise 7: Binomial to Poisson Approximation Over Time Slots
**Problem:** A log contains $n = 200$ time slots of 1 second each. In each slot, the error probability is $p = 0.02$. Approximate the probability of finding exactly 3 error slots using the Poisson distribution.

**Solution:**
- **Step 1: Validate conditions & scale rate.**
  $n = 200 \ge 20$ and $p = 0.02 \le 0.05$.
  $$\lambda = n \cdot p = 200 \times 0.02 = 4$$
- **Step 2: WIP State.**
  $$P(X=3) \approx \frac{4^3 \cdot e^{-4}}{3!} = \frac{64 \cdot e^{-4}}{6}$$
- **Step 3: Final Calculation.**
  $$P(X=3) \approx 0.1954$$

---

### Exercise 8: Finding Rate $\lambda$ from Duration Variance
**Problem:** Logged server crash counts over a 4-hour window have variance $V(X) = 6.25$. Find the hourly rate $\lambda$ and $P(X=0)$ in a 1-hour window.

**Solution:**
- **Step 1: Use Poisson variance property $V(X_{4\text{h}}) = \lambda_{4\text{h}}$.**
  $$\lambda_{4\text{h}} = 6.25 \implies \lambda_{\text{hourly}} = \frac{6.25}{4} = 1.5625\text{ crashes/hour}$$
- **Step 2: WIP State.**
  For a 1-hour window, $\lambda_1 = 1.5625$.
  $$P(X=0) = e^{-1.5625} = ?$$
- **Step 3: Final Calculation.**
  $$P(X=0) = e^{-1.5625} \approx 0.2096 \text{ (20.96\%)}$$

---

### Exercise 9: Gotcha Check -- Independent Time Increments
**Problem:** Errors in a system occur at $\lambda = 2$ per hour. During the first 2 hours, 5 errors were logged. What is the expected number of errors in the next 3 hours?

**Solution:**
- **The Error:** A student calculates $2 \times 3 - 5 = 1$. This is wrong! Past observed counts do not subtract from future rates.
- **Correct Logic:** By independent increments, the future 3-hour window is completely independent of past observations.
- **Final Calculation:**
  $$\lambda_{\text{next 3h}} = 2 \times 3 = 6\text{ expected errors}$$

---

### Exercise 10: R Code Snippet -- Poisson Time Window Rate Analysis
**Problem:** Write R code to scale a Poisson rate across different time windows and compute exact probabilities using `dpois` and `ppois`.

**Solution:**

```r
# Hourly arrival rate lambda
lambda_hourly <- 12

# Scale rates to 15-minute and 2-hour windows
lambda_15min <- lambda_hourly * (15 / 60) # 3 per 15 min
lambda_2hr   <- lambda_hourly * 2         # 24 per 2 hours

# P(Exactly 2 arrivals in 15 minutes)
p_2_in_15min <- dpois(2, lambda = lambda_15min)

# P(At most 20 arrivals in 2 hours)
p_atmost_20_in_2hr <- ppois(20, lambda = lambda_2hr)

cat("15-min scaled rate lambda:", lambda_15min, "\n")
cat("P(X = 2 in 15 min):", round(p_2_in_15min, 4), "\n")
cat("2-hr scaled rate lambda:", lambda_2hr, "\n")
cat("P(X <= 20 in 2 hr):", round(p_atmost_20_in_2hr, 4), "\n")
```

**Interpretation of Output:**
The functions `dpois` and `ppois` automatically take the scaled rate parameter `lambda`, making interval conversions seamless in R.
