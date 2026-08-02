# Phase 3.2 (Time): Independence in Time-Based Systems

Independence is a fundamental property in temporal probability modeling: two events occurring in time are independent if the occurrence or timing of one provides zero information about the timing or occurrence of the other.

---

## 1. Theoretical Foundation (Time Context)

### Mathematical Definition
Two temporal events $A$ and $B$ (e.g., $A$: "Server 1 experiences a latency spike during time window $W_1$" and $B$: "Server 2 experiences a latency spike during time window $W_2$") are **independent** if and only if:

$$P(A \cap B) = P(A) \cdot P(B)$$

Equivalently, in terms of conditional probabilities:

$$P(A \mid B) = P(A) \quad \text{and} \quad P(B \mid A) = P(B)$$

### Independent Time Intervals
For continuous processes, events taking place in non-overlapping time intervals $[t_1, t_2]$ and $[t_3, t_4]$ (where $t_2 \le t_3$) are frequently assumed to be independent. This is known as the **independent increments property** (found in Poisson processes and Brownian motion).

### System Reliability over Execution Time
Consider $n$ components with independent lifetimes $T_1, T_2, \dots, T_n$:

1. **Series System (Requires all components to run):**
   The overall system lifetime is $T_{\text{sys}} = \min(T_1, T_2, \dots, T_n)$. The system survives past time $t$ only if *every* component survives past $t$:
   $$P(T_{\text{sys}} > t) = P(T_1 > t \cap T_2 > t \cap \dots \cap T_n > t) = \prod_{i=1}^{n} P(T_i > t)$$

2. **Parallel System (Requires at least one component to run):**
   The overall system lifetime is $T_{\text{sys}} = \max(T_1, T_2, \dots, T_n)$. The system fails at or before time $t$ only if *every* component fails at or before $t$:
   $$P(T_{\text{sys}} \le t) = P(T_1 \le t \cap T_2 \le t \cap \dots \cap T_n \le t) = \prod_{i=1}^{n} P(T_i \le t)$$

### Independence vs. Mutually Exclusive Time Slots
* **Mutually Exclusive Time Slots:** Two events $A$ and $B$ occupy the exact same non-sharable resource at time $t$ ($P(A \cap B) = 0$). If $A$ happens at $t$, $B$ cannot. Mutually exclusive non-zero events are **always dependent**.
* **Independent Time Events:** $A$ and $B$ can occur at the same time $t$ without affecting each other ($P(A \cap B) = P(A)P(B)$).

---

## 2. Time-Specific Gotchas

### Gotcha 1: Assuming Independence in Consecutive Time Windows (Autocorrelation)
In time-series logs (e.g., CPU load sampled every minute), latency in minute $t+1$ is strongly correlated with latency in minute $t$. Treating consecutive time intervals as independent events leads to underestimating the probability of prolonged outages.

### Gotcha 2: Confusing Disjoint Time Intervals with Independent Events
If Task A can only execute in $[0, 5\text{ s}]$ and Task B can only execute in $[5, 10\text{ s}]$ on a single core, they cannot occur simultaneously. Their intersection is empty ($P(A \cap B) = 0$). They are **mutually exclusive**, not independent.

### Gotcha 3: Shared Infrastructure Contention (Hidden Coupling)
Two timers or network calls running on separate virtual machines may appear independent. However, if they share a common physical clock source, network switch, or hypervisor host, an overload on the host impacts both simultaneously, invalidating independence assumptions.

---

## 3. Solved Exercises (10 Examples)

### Exercise 1: Independent Server Timeout Events
**Problem:** Two isolated edge servers, $S_1$ and $S_2$, have independent timeout probabilities during a 1-hour monitoring window: $P(\text{Timeout}_1) = 0.04$ and $P(\text{Timeout}_2) = 0.05$. What is the probability that both experience timeouts in that hour?

**Solution:**
- **Step 1: Apply product rule.**
  Since $S_1$ and $S_2$ are independent:
  $$P(T_1 \cap T_2) = P(T_1) \cdot P(T_2)$$
- **Step 2: WIP State.**
  $$P(T_1 \cap T_2) = 0.04 \cdot ?$$
- **Step 3: Final Calculation.**
  $$P(T_1 \cap T_2) = 0.04 \cdot 0.05 = 0.0020 \text{ (0.2\%)}$$

---

### Exercise 2: Parallel Redundant Watchdog Timers
**Problem:** A critical embedded safety module utilizes two independent hardware timers running in parallel. Each timer has a failure probability of $0.02$ over a 24-hour operation window. What is the probability that the safety module remains operational (at least one timer works)?

**Solution:**
- **Step 1: Identify failure conditions.**
  System fails only if both timers fail at or before 24 hours:
  $$P(\text{System Fails}) = P(F_1 \cap F_2) = P(F_1) \cdot P(F_2) = 0.02 \cdot 0.02 = 0.0004$$
- **Step 2: WIP State.**
  $P(\text{System Works}) = 1 - P(\text{System Fails}) = 1 - ?$.
- **Step 3: Final Calculation.**
  $$P(\text{System Works}) = 1 - 0.0004 = 0.9996 \text{ (99.96\%)}$$

---

### Exercise 3: Series Pipeline Lifetime
**Problem:** A data streaming pipeline consists of 3 sequential processing stages. Each stage operates independently, and their 8-hour survival probabilities are $P(T_1 > 8) = 0.95$, $P(T_2 > 8) = 0.90$, and $P(T_3 > 8) = 0.98$. What is the probability the entire pipeline runs uninterrupted for 8 hours?

**Solution:**
- **Step 1: Apply series survival product.**
  $$P(T_{\text{sys}} > 8) = P(T_1 > 8) \cdot P(T_2 > 8) \cdot P(T_3 > 8)$$
- **Step 2: WIP State.**
  $$P(T_{\text{sys}} > 8) = 0.95 \cdot 0.90 \cdot ?$$
- **Step 3: Final Calculation.**
  $$P(T_{\text{sys}} > 8) = 0.95 \cdot 0.90 \cdot 0.98 = 0.8379$$

---

### Exercise 4: Testing Independence of Microservice Latency Spikes
**Problem:** A log analysis checks two microservices, A and B. Over 1000 observation minutes:
- Service A spikes ($A$) in 100 minutes ($P(A) = 0.10$).
- Service B spikes ($B$) in 150 minutes ($P(B) = 0.15$).
- Both spike in the same minute ($A \cap B$) in 30 minutes ($P(A \cap B) = 0.03$).
Are latency spikes in Service A and Service B independent?

**Solution:**
- **Step 1: Compute product of marginal probabilities.**
  $$P(A) \cdot P(B) = 0.10 \cdot 0.15 = 0.015$$
- **Step 2: WIP State.**
  Compare $P(A \cap B)$ with $P(A) \cdot P(B)$:
  $$0.030 \neq ?$$
- **Step 3: Final Calculation.**
  $$0.030 \neq 0.015$$
  Since $P(A \cap B) > P(A)P(B)$, the events are **dependent** (positively coupled, likely due to shared load).

---

### Exercise 5: Probability of At Least One Outage Across Non-Overlapping Hours
**Problem:** The probability of a network glitch in any single 1-hour window is $P(G) = 0.10$. Assuming glitches across 4 non-overlapping hours are independent, find the probability of at least one glitch during a 4-hour block.

**Solution:**
- **Step 1: Use complement rule.**
  $P(\text{At least 1 glitch}) = 1 - P(\text{No glitches in all 4 hours})$.
- **Step 2: WIP State.**
  For 1 hour, $P(\text{No glitch}) = 1 - 0.10 = 0.90$.
  For 4 independent hours, $P(\text{No glitches}) = (0.90)^4 = ?$.
- **Step 3: Final Calculation.**
  $$(0.90)^4 = 0.6561$$
  $$P(\text{At least 1 glitch}) = 1 - 0.6561 = 0.3439 \text{ (34.39\%)}$$

---

### Exercise 6: Independent Disk Backup Durations
**Problem:** Two independent backup tasks, $B_1$ and $B_2$, complete within 30 minutes with probabilities $0.80$ and $0.70$ respectively. What is the probability that $B_1$ completes within 30 minutes BUT $B_2$ takes longer than 30 minutes?

**Solution:**
- **Step 1: Formulate independent target event.**
  We want $P(B_1 \le 30 \cap B_2 > 30)$.
  Since $B_1$ and $B_2$ are independent, $B_1 \le 30$ and $B_2 > 30$ are also independent.
- **Step 2: WIP State.**
  $P(B_2 > 30) = 1 - 0.70 = 0.30$.
  $$P(B_1 \le 30 \cap B_2 > 30) = 0.80 \cdot ?$$
- **Step 3: Final Calculation.**
  $$P(B_1 \le 30 \cap B_2 > 30) = 0.80 \cdot 0.30 = 0.24$$

---

### Exercise 7: Cron Job Execution Alignment
**Problem:** Job 1 runs every 5 minutes and succeeds with probability 0.99. Job 2 runs every 10 minutes and succeeds with probability 0.95. Assuming execution outcomes are independent, what is the probability that at $t=10\text{ min}$ (when both run simultaneously), both jobs succeed?

**Solution:**
- **Step 1: Identify probabilities.**
  $P(J_1) = 0.99$, $P(J_2) = 0.95$.
- **Step 2: WIP State.**
  $$P(J_1 \cap J_2) = 0.99 \cdot ?$$
- **Step 3: Final Calculation.**
  $$P(J_1 \cap J_2) = 0.99 \cdot 0.95 = 0.9405 \text{ (94.05\%)}$$

---

### Exercise 8: Probability of Exactly One Service Timeout
**Problem:** Two independent microservices have timeout probabilities $P(T_A) = 0.15$ and $P(T_B) = 0.10$ during a benchmark run. What is the probability that **exactly one** service times out?

**Solution:**
- **Step 1: Identify mutually exclusive paths.**
  Path 1: A times out and B does not ($T_A \cap T_B^c$).
  Path 2: B times out and A does not ($T_B \cap T_A^c$).
- **Step 2: WIP State.**
  $P(T_A \cap T_B^c) = 0.15 \cdot (1 - 0.10) = 0.15 \cdot 0.90 = 0.135$.
  $P(T_B \cap T_A^c) = 0.10 \cdot (1 - 0.15) = 0.10 \cdot 0.85 = 0.085$.
  $$P(\text{Exactly one}) = 0.135 + ?$$
- **Step 3: Final Calculation.**
  $$P(\text{Exactly one}) = 0.135 + 0.085 = 0.220 \text{ (22.0\%)}$$

---

### Exercise 9: Triple-Redundant Real-Time Sensor Clock
**Problem:** Three independent atomic clock signals $C_1, C_2, C_3$ maintain sync accuracy over 1000 hours with probabilities $0.99, 0.98, 0.96$. A majority vote system requires at least 2 clocks to remain in sync. Find the probability the system stays synced.

**Solution:**
- **Step 1: List favorable outcomes.**
  1. All 3 synced: $0.99 \cdot 0.98 \cdot 0.96 = 0.931392$
  2. $C_1, C_2$ synced, $C_3$ failed: $0.99 \cdot 0.98 \cdot 0.04 = 0.038808$
  3. $C_1, C_3$ synced, $C_2$ failed: $0.99 \cdot 0.02 \cdot 0.96 = 0.019008$
  4. $C_2, C_3$ synced, $C_1$ failed: $0.01 \cdot 0.98 \cdot 0.96 = 0.009408$
- **Step 2: WIP State.**
  Sum the four mutually exclusive probabilities:
  $$P(\ge 2 \text{ synced}) = 0.931392 + 0.038808 + 0.019008 + ?$$
- **Step 3: Final Calculation.**
  $$P(\ge 2 \text{ synced}) = 0.931392 + 0.038808 + 0.019008 + 0.009408 = 0.998616 \approx 0.9986$$

---

### Exercise 10: R Code Snippet -- Testing Independence of Temporal Delays
**Problem:** Write an R script to compute the sample covariance and test whether delays in two consecutive queueing steps ($T_1$ and $T_2$) are statistically independent.

**Solution:**

```r
# Simulate 500 log entries of multi-stage queueing times (in seconds)
set.seed(123)
t1 <- rexp(500, rate = 0.5) # Stage 1 delay
t2 <- rexp(500, rate = 0.4) + 0.2 * t1 # Stage 2 delay with partial coupling

# Compute correlation coefficient
cor_val <- cor(t1, t2)

# Perform Pearson correlation test for independence (H0: cor = 0)
test_res <- cor.test(t1, t2)

cat("Sample Correlation coefficient:", round(cor_val, 4), "\n")
cat("P-value for independence test:", format.pval(test_res$p.value), "\n")

if (test_res$p.value < 0.05) {
  cat("Result: Reject independence (Delays are dependent over time).\n")
} else {
  cat("Result: Fail to reject independence.\n")
}
```

**Interpretation of Output:**
A p-value below 0.05 provides empirical evidence against temporal independence, indicating that Stage 1 queue delays actively propagate into Stage 2 delays.
