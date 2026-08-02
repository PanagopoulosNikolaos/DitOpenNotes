# Phase 3.3 (Time): Law of Total Probability & Bayes' Theorem for Time-Partitioned Data

The Law of Total Probability and Bayes' Theorem are essential for analyzing complex systems operating across different **time shifts, operational regimes, or execution phases**.

---

## 1. Theoretical Foundation (Time Context)

### Law of Total Probability for Time Partitions
Let the time domain or operational schedule be partitioned into $n$ mutually exclusive and exhaustive time windows or system states $B_1, B_2, \dots, B_n$ such that:

$$\bigcup_{i=1}^{n} B_i = S \quad \text{and} \quad B_i \cap B_j = \emptyset \text{ for } i \neq j, \quad \sum_{i=1}^n P(B_i) = 1$$

For any performance event $A$ (e.g., $A$: "Transaction execution time exceeds $500\text{ ms}$"), the total probability of $A$ occurring across the full operational cycle is:

$$\boxed{P(A) = \sum_{i=1}^{n} P(A \mid B_i) P(B_i) = P(A \mid B_1)P(B_1) + P(A \mid B_2)P(B_2) + \dots + P(A \mid B_n)P(B_n)}$$

### Bayes' Theorem for Temporal Inference
When a performance anomaly or execution time event $A$ is observed, Bayes' Theorem allows us to update the probability that the system was operating in a specific time regime or state $B_k$:

$$\boxed{P(B_k \mid A) = \frac{P(A \mid B_k) P(B_k)}{P(A)} = \frac{P(A \mid B_k) P(B_k)}{\sum_{j=1}^{n} P(A \mid B_j) P(B_j)}}$$

Where:
* **Prior Probability $P(B_k)$:** The fraction of total operating time spent in state/regime $B_k$.
* **Likelihood $P(A \mid B_k)$:** The probability of observing execution time event $A$ while in state $B_k$.
* **Posterior Probability $P(B_k \mid A)$:** The updated probability that state $B_k$ was active, given that execution time event $A$ occurred.

---

## 2. Time-Specific Gotchas

### Gotcha 1: Non-Exhaustive Time Partitions
When building a partition $B_1, B_2, \dots, B_n$, ensure the sum of time fractions equals 1. For example, partitioning a 24-hour day into Day Shift (8 hours = 8/24) and Night Shift (12 hours = 12/24) leaves 4 hours unaccounted for ($\sum = 20/24 \neq 1$). The Law of Total Probability will fail.

### Gotcha 2: Confusing Prior Duration Fractions with Posterior State Probabilities
A system might spend 90% of its operating time in Normal Mode ($P(N) = 0.90$) and 10% in High-Load Mode ($P(H) = 0.10$). If an extreme timeout occurs, students often mistakenly report $P(H) = 0.10$ instead of evaluating the posterior $P(H \mid \text{Timeout})$. The observed timeout significantly shifts the odds toward High-Load Mode!

### Gotcha 3: Uncalibrated Time-Window Rates
Likelihood rates $P(A \mid B_k)$ must be normalized to identical time-window lengths. Comparing a 1-minute defect rate in $B_1$ against an 8-hour defect rate in $B_2$ distorts Bayes' formula.

---

## 3. Solved Exercises (10 Examples)

### Exercise 1: Overall Latency Spike Probability (Total Probability)
**Problem:** A cloud database runs under three load regimes: Morning Peak ($B_1$, 40% of time), Afternoon Normal ($B_2$, 40% of time), and Night Low ($B_3$, 20% of time). The probabilities of a query taking over 100 ms are 0.15 in $B_1$, 0.05 in $B_2$, and 0.01 in $B_3$. Find the total probability that a randomly chosen query takes over 100 ms.

**Solution:**
- **Step 1: List given probabilities.**
  - $P(B_1) = 0.40, P(A \mid B_1) = 0.15$
  - $P(B_2) = 0.40, P(A \mid B_2) = 0.05$
  - $P(B_3) = 0.20, P(A \mid B_3) = 0.01$
- **Step 2: WIP State.**
  Apply Law of Total Probability:
  $$P(A) = (0.15 \cdot 0.40) + (0.05 \cdot 0.40) + (0.01 \cdot ?)$$
- **Step 3: Final Calculation.**
  $$P(A) = 0.060 + 0.020 + 0.002 = 0.082 \text{ (8.2\%)}$$

---

### Exercise 2: Diagnosing Load Regime from Latency Spike (Bayes)
**Problem:** Using the setup from Exercise 1 ($P(A) = 0.082$), if a query is observed to take over 100 ms ($A$), what is the posterior probability that it occurred during Morning Peak ($B_1$)?

**Solution:**
- **Step 1: Apply Bayes' Theorem.**
  $$P(B_1 \mid A) = \frac{P(A \mid B_1) P(B_1)}{P(A)}$$
- **Step 2: WIP State.**
  $$P(B_1 \mid A) = \frac{0.15 \cdot 0.40}{0.082} = \frac{0.060}{?}$$
- **Step 3: Final Calculation.**
  $$P(B_1 \mid A) = \frac{0.060}{0.082} \approx 0.7317 \text{ (73.17\%)}$$

---

### Exercise 3: Packet Loss across Peak vs. Off-Peak Hours
**Problem:** Network traffic operates under Peak hours (16 hours/day, $P(\text{Peak}) = 16/24 = 2/3$) and Off-Peak hours (8 hours/day, $P(\text{Off-Peak}) = 1/3$). Packet loss probability is $0.03$ during Peak and $0.006$ during Off-Peak. Find the overall packet loss probability $P(L)$.

**Solution:**
- **Step 1: Set up total probability.**
  $$P(L) = P(L \mid \text{Peak})P(\text{Peak}) + P(L \mid \text{Off-Peak})P(\text{Off-Peak})$$
- **Step 2: WIP State.**
  $$P(L) = \left(0.03 \cdot \frac{2}{3}\right) + \left(0.006 \cdot \frac{1}{3}\right) = 0.020 + ?$$
- **Step 3: Final Calculation.**
  $$P(L) = 0.020 + 0.002 = 0.022 \text{ (2.2\%)}$$

---

### Exercise 4: Identifying Equipment Supplier from Failure Time
**Problem:** A factory sources servers from Supplier X (70% of inventory) and Supplier Y (30% of inventory). The probability that a server fails before 1000 hours of runtime is 0.08 for Supplier X and 0.02 for Supplier Y. A server fails before 1000 hours. What is the probability it came from Supplier X?

**Solution:**
- **Step 1: Calculate total failure probability $P(F)$.**
  $$P(F) = (0.08 \cdot 0.70) + (0.02 \cdot 0.30) = 0.056 + 0.006 = 0.062$$
- **Step 2: WIP State.**
  Apply Bayes' Theorem:
  $$P(X \mid F) = \frac{P(F \mid X) P(X)}{P(F)} = \frac{0.056}{?}$$
- **Step 3: Final Calculation.**
  $$P(X \mid F) = \frac{0.056}{0.062} \approx 0.9032 \text{ (90.32\%)}$$

---

### Exercise 5: Software Bug Discovery Timing
**Problem:** Bugs in a software project are discovered during Unit Testing ($B_1$, 50% of bugs), Integration Testing ($B_2$, 30%), or Production ($B_3$, 20%). The probability that a bug takes $> 24\text{ hours}$ to resolve is 0.10 in $B_1$, 0.40 in $B_2$, and 0.90 in $B_3$. Find the total probability that a randomly logged bug takes $> 24\text{ hours}$ to resolve.

**Solution:**
- **Step 1: Apply total probability formula.**
  $$P(>24\text{h}) = P(>24\text{h} \mid B_1)P(B_1) + P(>24\text{h} \mid B_2)P(B_2) + P(>24\text{h} \mid B_3)P(B_3)$$
- **Step 2: WIP State.**
  $$P(>24\text{h}) = (0.10 \cdot 0.50) + (0.40 \cdot 0.30) + (0.90 \cdot ?)$$
- **Step 3: Final Calculation.**
  $$P(>24\text{h}) = 0.050 + 0.120 + 0.180 = 0.350 \text{ (35.0\%)}$$

---

### Exercise 6: Anomaly Detection in API Latency (Bayes)
**Problem:** Continuing Exercise 5 ($P(>24\text{h}) = 0.350$), if a bug log shows a resolution time $> 24\text{ hours}$, what is the probability it was reported in Production ($B_3$)?

**Solution:**
- **Step 1: Set up Bayes' ratio.**
  $$P(B_3 \mid >24\text{h}) = \frac{P(>24\text{h} \mid B_3) P(B_3)}{P(>24\text{h})}$$
- **Step 2: WIP State.**
  $$P(B_3 \mid >24\text{h}) = \frac{0.90 \cdot 0.20}{0.350} = \frac{0.180}{?}$$
- **Step 3: Final Calculation.**
  $$P(B_3 \mid >24\text{h}) = \frac{0.180}{0.350} \approx 0.5143 \text{ (51.43\%)}$$

---

### Exercise 7: Database Lock Delay Causes
**Problem:** Database locks stem from Query Type A (60%), Type B (30%), or Type C (10%). Lock durations exceed 2 seconds with probability 0.05 for Type A, 0.20 for Type B, and 0.80 for Type C. Find the total probability that a lock exceeds 2 seconds.

**Solution:**
- **Step 1: Sum partitioned probabilities.**
  $$P(L > 2\text{s}) = (0.05 \cdot 0.60) + (0.20 \cdot 0.30) + (0.80 \cdot 0.10)$$
- **Step 2: WIP State.**
  $$P(L > 2\text{s}) = 0.030 + 0.060 + ?$$
- **Step 3: Final Calculation.**
  $$P(L > 2\text{s}) = 0.030 + 0.060 + 0.080 = 0.170 \text{ (17.0\%)}$$

---

### Exercise 8: Cloud Server Crash Diagnosis
**Problem:** Cloud server reboots occur due to Memory Leaks ($M$, 50%), Power Spikes ($P$, 30%), or OS Updates ($U$, 20%). The reboot duration exceeds 5 minutes with probability 0.90 for $M$, 0.10 for $P$, and 0.30 for $U$. If a reboot took over 5 minutes, find the probability it was caused by a Memory Leak ($M$).

**Solution:**
- **Step 1: Compute total probability $P(T > 5\text{m})$.**
  $$P(T > 5\text{m}) = (0.90 \cdot 0.50) + (0.10 \cdot 0.30) + (0.30 \cdot 0.20) = 0.45 + 0.03 + 0.06 = 0.54$$
- **Step 2: WIP State.**
  $$P(M \mid T > 5\text{m}) = \frac{P(T > 5\text{m} \mid M) P(M)}{P(T > 5\text{m})} = \frac{0.45}{?}$$
- **Step 3: Final Calculation.**
  $$P(M \mid T > 5\text{m}) = \frac{0.45}{0.54} = \frac{5}{6} \approx 0.8333$$

---

### Exercise 9: Microservice Response SLA Verification
**Problem:** Requests are split across Region 1 (60% traffic) and Region 2 (40% traffic). Response time $T \le 100\text{ ms}$ is met 95% of the time in Region 1 and 80% of the time in Region 2. What is the overall percentage of requests satisfying the SLA ($T \le 100\text{ ms}$)?

**Solution:**
- **Step 1: Total probability calculation.**
  $$P(T \le 100) = (0.95 \cdot 0.60) + (0.80 \cdot 0.40)$$
- **Step 2: WIP State.**
  $$P(T \le 100) = 0.570 + ?$$
- **Step 3: Final Calculation.**
  $$P(T \le 100) = 0.570 + 0.320 = 0.890 \text{ (89.0\%)}$$

---

### Exercise 10: R Code Snippet -- Implementing Bayes' Updating for Log Diagnostics
**Problem:** Write an R function that computes the posterior probabilities of $n$ time-partitioned regimes given an observed execution delay threshold.

**Solution:**

```r
# Function for Bayes' updating across time regimes
bayes_time_update <- function(priors, likelihoods) {
  # Total probability of the event using Law of Total Probability
  p_total <- sum(priors * likelihoods)
  
  # Posterior probability for each regime
  posteriors <- (priors * likelihoods) / p_total
  
  return(list(total_prob = p_total, posteriors = posteriors))
}

# Example setup: 3 time regimes (Morning, Afternoon, Night)
priors <- c(Morning = 0.40, Afternoon = 0.40, Night = 0.20)
likelihoods <- c(Morning = 0.15, Afternoon = 0.05, Night = 0.01) # P(T > 100 ms | Regime)

res <- bayes_time_update(priors, likelihoods)

cat("Total Probability P(T > 100 ms):", round(res$total_prob, 4), "\n\n")
cat("Posterior Probabilities P(Regime | T > 100 ms):\n")
print(round(res$posteriors, 4))
```

**Interpretation of Output:**
The function computes both the total baseline rate using `sum(priors * likelihoods)` and the normalized vector of posterior probabilities, demonstrating the exact two-stage execution of Bayes' Theorem.
