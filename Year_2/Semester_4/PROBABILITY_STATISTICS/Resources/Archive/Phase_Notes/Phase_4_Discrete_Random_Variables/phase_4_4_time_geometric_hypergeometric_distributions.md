# Phase 4.4 (Time): Geometric & Hypergeometric Distributions in Time Contexts

This file covers two important discrete time models: the **Geometric Distribution** (modeling the number of discrete time slots until the first success occurs) and the **Hypergeometric Distribution** (modeling sampling without replacement from a fixed time batch of log entries).

---

## 1. Geometric Distribution in Time ($T \sim Geo(p)$)

The Geometric distribution models the elapsed discrete time slots $T$ until the first successful event occurs (e.g., time slots until a network connection succeeds, or retries until an API responds).

> **Critical Exam Gotcha:** There are two distinct definitions of the Geometric distribution in time contexts. Always check which definition is requested.

### Definition A: Counting Total Time Slots ($k = 1, 2, 3, \dots$)
Here, $T$ represents the **slot index of the first success**.
* **PMF:** $P(T = k) = (1-p)^{k-1} p$
* **Expected Time Slots:** $E[T] = \frac{1}{p}$
* **Variance:** $V(T) = \frac{1-p}{p^2}$
* **CDF:** $P(T \le k) = 1 - (1-p)^k$
* **Complement Shortcut ("More than $k$ time slots"):**
  $$\boxed{P(T > k) = (1-p)^k}$$

### Definition B: Counting Failed Time Slots Before First Success ($k = 0, 1, 2, \dots$)
Here, $Y = T - 1$ represents the **number of failed time slots** before the first success.
* **PMF:** $P(Y = k) = (1-p)^k p$
* **Expected Failed Slots:** $E[Y] = \frac{1-p}{p}$
* **Variance:** $V(Y) = \frac{1-p}{p^2}$

### Discrete Memoryless Property of Time Slots
The Geometric distribution is the **only** discrete distribution possessing the memoryless property:

$$\boxed{P(T > k + s \mid T > k) = P(T > s)}$$

*Interpretation:* If a process has already failed for $k$ time slots, the probability that it requires more than $s$ additional slots is identical to the initial probability of exceeding $s$ slots from scratch. Past failed time slots do not cause aging or wear in a Geometric process.

---

## 2. Hypergeometric Distribution in Time Windows ($X \sim HG(N, K, n)$)

The Hypergeometric distribution models the number of success events $X$ obtained when selecting a sample of $n$ time records **without replacement** from a finite batch of $N$ total time records containing exactly $K$ target events (e.g., error logs).

Because sampling is without replacement, time slot trials are **not independent** (the success probability changes after each drawn log record).

### Parameters & PMF Formula
* $N$: Total log records in the time batch
* $K$: Number of target event records (e.g., error logs) in the population
* $n$: Number of log records sampled without replacement
* $k$: Number of target event records in the sample

$$\boxed{P(X = k) = \frac{\binom{K}{k} \binom{N-K}{n-k}}{\binom{N}{n}}, \quad \max(0, n - (N - K)) \le k \le \min(n, K)}$$

### Mean and Variance
$$E[X] = n \cdot \frac{K}{N}$$

$$\boxed{V(X) = n \cdot \frac{K}{N} \cdot \left(1 - \frac{K}{N}\right) \cdot \left(\frac{N - n}{N - 1}\right)}$$

The factor $\frac{N-n}{N-1}$ is the **Finite Population Correction (FPC)** factor.

---

## 3. Time-Specific Gotchas

### Gotcha 1: Confusing Definition A ($k \ge 1$) and Definition B ($k \ge 0$) in Time Slots
* If a question asks for "the **time slot number** of the first success", use Definition A ($E[T] = 1/p$).
* If a question asks for "the **number of retries/failures** before the first success", use Definition B ($E[Y] = (1-p)/p$).

### Gotcha 2: Misapplying Memorylessness to Memoryful Time Distributions
Students often assume memorylessness applies to all duration models. It **only** applies to Geometric (discrete time) and Exponential (continuous time) distributions. Systems subject to physical wear or queue accumulation are memoryful ($P(T > k+s \mid T > k) \neq P(T > s)$).

### Gotcha 3: Omitting Finite Population Correction in Time Log Sampling
When auditing $n$ log entries from a daily batch of $N$ logs without replacement, trials are dependent. Forgetting the FPC factor $\frac{N-n}{N-1}$ overestimates variance unless $n/N \le 0.05$ (in which case Binomial approximation applies).

---

## 4. Solved Exercises (10 Examples)

### Exercise 1: First Connection Success on 4th Time Slot (Geometric)
**Problem:** A modem attempts connection in discrete 1-second time slots with success probability $p = 0.70$. Find the probability that the first successful connection occurs on the 4th time slot.

**Solution:**
- **Step 1: Use Definition A ($T \sim Geo(0.70)$).**
  $$P(T = 4) = (1 - 0.70)^{4-1} (0.70) = (0.30)^3 \cdot 0.70$$
- **Step 2: WIP State.**
  $$(0.30)^3 = 0.027$$
  $$P(T = 4) = 0.027 \cdot 0.70 = ?$$
- **Step 3: Final Calculation.**
  $$P(T = 4) = 0.0189 \text{ (1.89\%)}$$

---

### Exercise 2: Expected Time Slots to Link Establishment
**Problem:** Find the expected number of time slots needed to establish a link when $p = 0.20$.

**Solution:**
- **Step 1: Apply $E[T] = 1/p$.**
  $$E[T] = \frac{1}{0.20} = 5\text{ time slots}$$
- **Step 2: Variance.**
  $$V(T) = \frac{1 - 0.20}{(0.20)^2} = \frac{0.80}{0.04} = 20\text{ slots}^2$$

---

### Exercise 3: Cumulative Time Slots Probability ("Within First 3 Slots")
**Problem:** For $p = 0.05$ crash probability per boot time slot, find the probability that the first crash occurs within the first 3 boots ($P(T \le 3)$).

**Solution:**
- **Step 1: Use CDF formula $P(T \le k) = 1 - (1-p)^k$.**
  $$P(T \le 3) = 1 - (1 - 0.05)^3 = 1 - (0.95)^3$$
- **Step 2: WIP State.**
  $$(0.95)^3 = 0.857375$$
  $$P(T \le 3) = 1 - 0.857375 = ?$$
- **Step 3: Final Calculation.**
  $$P(T \le 3) = 0.1426 \text{ (14.26\%)}$$

---

### Exercise 4: "More Than 5 Time Slots" Shortcut
**Problem:** A server retry has success probability $p = 0.20$ per slot. What is the probability that more than 5 time slots are needed for the first success?

**Solution:**
- **Step 1: Apply complement shortcut $P(T > k) = (1-p)^k$.**
  $$P(T > 5) = (1 - 0.20)^5 = (0.80)^5$$
- **Step 2: WIP State.**
  $$(0.80)^5 = ?$$
- **Step 3: Final Calculation.**
  $$P(T > 5) = 0.3277 \text{ (32.77\%)}$$

---

### Exercise 5: Memoryless Property of Time Slots
**Problem:** A tester checks time slots for a defect ($p = 0.10$). Given that the first 5 slots were error-free ($T > 5$), find the conditional probability that the first defect occurs on the 8th slot ($P(T = 8 \mid T > 5)$).

**Solution:**
- **Step 1: Apply memoryless property.**
  $$P(T = 8 \mid T > 5) = P(T = 8 - 5) = P(T = 3)$$
- **Step 2: WIP State.**
  $$P(T = 3) = (0.90)^{3-1} (0.10) = (0.90)^2 \cdot 0.10 = 0.81 \cdot 0.10$$
- **Step 3: Final Calculation.**
  $$P(T = 3) = 0.081 \text{ (8.1\%)}$$

---

### Exercise 6: Time Log Audit (Hypergeometric)
**Problem:** A batch contains $N = 52$ hour-long log files, of which $K = 4$ contain security alerts. An auditor randomly inspects $n = 5$ log files without replacement. Find the probability of finding exactly 3 security alert logs ($P(X = 3)$).

**Solution:**
- **Step 1: Set up Hypergeometric PMF.**
  $$P(X = 3) = \frac{\binom{4}{3} \binom{48}{2}}{\binom{52}{5}}$$
- **Step 2: WIP State.**
  $\binom{4}{3} = 4$, $\binom{48}{2} = \frac{48 \cdot 47}{2} = 1128$, $\binom{52}{5} = 2,598,960$.
  $$P(X=3) = \frac{4 \cdot 1128}{2,598,960} = \frac{4512}{?}$$
- **Step 3: Final Calculation.**
  $$P(X=3) = \frac{4512}{2,598,960} \approx 0.001736$$

---

### Exercise 7: Quality Control Over Fixed Log Batch ($P(X=0)$)
**Problem:** A server log batch has $N = 20$ records, $K = 4$ of which are corrupt. An engineer samples $n = 5$ records without replacement. Find $P(X=0)$ corrupt records.

**Solution:**
- **Step 1: Set up PMF for $k=0$.**
  $$P(X=0) = \frac{\binom{4}{0} \binom{16}{5}}{\binom{20}{5}} = \frac{1 \cdot 4368}{15,504}$$
- **Step 2: WIP State.**
  $$P(X=0) = \frac{4368}{15,504} = ?$$
- **Step 3: Final Calculation.**
  $$P(X=0) \approx 0.2817 \text{ (28.17\%)}$$

---

### Exercise 8: Mean and Variance with Finite Population Correction
**Problem:** Using the setup from Exercise 7 ($N=20, K=4, n=5$), compute $E[X]$, $V(X)$, and FPC.

**Solution:**
- **Step 1: Compute $E[X]$.**
  $$E[X] = n \cdot \frac{K}{N} = 5 \cdot \frac{4}{20} = 1.0\text{ log record}$$
- **Step 2: Compute FPC and Variance.**
  $$\text{FPC} = \frac{N - n}{N - 1} = \frac{20 - 5}{20 - 1} = \frac{15}{19} \approx 0.7895$$
  $$V(X) = 5 \cdot \left(\frac{4}{20}\right) \cdot \left(1 - \frac{4}{20}\right) \cdot \left(\frac{15}{19}\right) = 1 \cdot 0.80 \cdot \frac{15}{19} = \frac{12}{19} \approx 0.6316$$

---

### Exercise 9: Hypergeometric vs. Binomial Approximation for Large Log Batches
**Problem:** A batch of $N = 1000$ log files contains $K = 100$ error logs. A sample of $n = 10$ logs is drawn without replacement. Compare exact $P(X=1)$ Hypergeometric with Binomial approximation.

**Solution:**
- **Exact Hypergeometric:**
  $$P(X=1) = \frac{\binom{100}{1} \binom{900}{9}}{\binom{1000}{10}} \approx 0.3899$$
- **Binomial Approximation ($p = 100/1000 = 0.10$):**
  $$P(Y=1) = \binom{10}{1} (0.10)^1 (0.90)^9 = 10 \cdot 0.10 \cdot 0.38742 = 0.3874$$
- **Conclusion:** Difference is only $0.3899 - 0.3874 = 0.0025$, confirming Binomial accuracy when $n/N = 0.01 \le 0.05$.

---

### Exercise 10: R Code Snippet -- Geometric & Hypergeometric Time Benchmarking
**Problem:** Write R code using `dgeom` (Def B), `dhyper`, and exact calculations for time slot evaluation.

**Solution:**

```r
# Geometric Distribution (Definition A: k trials)
p_success <- 0.20
k_trial <- 4
# R's dgeom uses Definition B (failures before success), so pass k_trial - 1
p_geom_defA <- dgeom(k_trial - 1, prob = p_success)

# Hypergeometric Distribution (Sampling without replacement)
N_pop <- 52   # Total log files
K_succ <- 4   # Security alert logs
n_sample <- 5 # Sample size
k_target <- 3 # Target alerts in sample

p_hyper <- dhyper(k_target, m = K_succ, n = N_pop - K_succ, k = n_sample)

cat("Geometric P(First success on slot 4):", round(p_geom_defA, 4), "\n")
cat("Hypergeometric P(3 alerts in sample of 5):", round(p_hyper, 6), "\n")
```

**Interpretation of Output:**
Note that R's `dgeom(x, prob)` implements Definition B ($x$ failures). Passing `k - 1` correctly adapts it to Definition A ($k$ total time slots).
