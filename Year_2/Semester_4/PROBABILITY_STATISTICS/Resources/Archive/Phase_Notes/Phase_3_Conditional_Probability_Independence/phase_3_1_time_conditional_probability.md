# Phase 3.1 (Time): Conditional Probability in Time-Based Systems

Conditional probability measures the likelihood of an event occurring given that another event has already occurred. In time-based systems, the conditioning event is frequently defined by **elapsed durations, surviving times, timestamp thresholds, or historical uptime logs**. 

---

## 1. Theoretical Foundation (Time Context)

### Definition
Let $T$ be a non-negative random variable representing a duration, latency, or time-to-event (e.g., system lifetime, execution time, network packet delay). 

The conditional probability that an operation completes before time $t_2$, given that it has already surpassed time $t_1$ (where $t_2 > t_1$), is defined as:

$$P(T \le t_2 \mid T > t_1) = \frac{P(t_1 < T \le t_2)}{P(T > t_1)}$$

Similarly, the conditional survival probability (the probability a component survives an additional duration $s$ after surviving up to time $t$) is:

$$P(T > t + s \mid T > t) = \frac{P(T > t + s)}{P(T > t)}$$

### Fundamental Formula
For general time-dependent events $A$ and $B$ (such as $A$: "Server fails before $t=100\text{ ms}$" and $B$: "Server was under high load at $t=0$"), the conditional probability formula remains:

$$P(A \mid B) = \frac{P(A \cap B)}{P(B)} \quad \text{provided } P(B) > 0$$

### The Reduced Sample Space in Time Logs
When analyzing operational logs:
* The original sample space $S$ consists of all recorded events across all time frames.
* The conditioning statement "given $B$" filters the log to keep only records satisfying criterion $B$ (e.g., requests arriving during peak hour $t \in [12:00, 14:00]$).
* The probability $P(A \mid B)$ is computed strictly within this filtered subset.

### Multiplication Rule for Time Sequences
For multi-stage sequential processes occurring at successive times $t_1 < t_2 < \dots < t_n$:

$$P(A_1 \cap A_2 \cap \dots \cap A_n) = P(A_1) \cdot P(A_2 \mid A_1) \cdot P(A_3 \mid A_1 \cap A_2) \dots P(A_n \mid A_1 \cap \dots \cap A_{n-1})$$

---

## 2. Time-Specific Gotchas

### Gotcha 1: Conflating Elapsed Time with Remaining Time
A common mistake is assuming that $P(T > t + s \mid T > t) = P(T > s)$. This identity holds **only** for memoryless distributions (like the Exponential distribution). For systems subject to wear-and-tear or aging, $P(T > t + s \mid T > t) < P(T > s)$. Always evaluate the denominator $P(T > t)$ explicitly unless memorylessness is proven.

### Gotcha 2: Right-Censored Observation Windows
In real-world benchmarking, data collection stops at a maximum observation window $T_{\text{max}}$. If a process has not finished by $T_{\text{max}}$, its full duration is unknown. Computing conditional probabilities without accounting for right-censoring leads to severe bias by underestimating long latencies.

### Gotcha 3: Mixed Unit Prefixes in Conditional Ratios
When calculating $P(A \cap B) / P(B)$, ensure both numerator and denominator time bounds use identical units (e.g., milliseconds vs. seconds). Mixing $t_1 = 500\text{ ms}$ with $t_2 = 2\text{ s}$ without converting $t_2$ to $2000\text{ ms}$ will cause major calculation errors.

---

## 3. Solved Exercises (10 Examples)

### Exercise 1: System Uptime Survival Probability
**Problem:** The probability that a cloud instance functions past 10 hours without rebooting is 0.85, and the probability it functions past 24 hours is 0.60. Given that an instance has already run successfully for 10 hours, what is the probability it will reach 24 hours?

**Solution:**
- **Step 1: Define events.**
  - $A$: Instance survives past 24 hours ($T > 24$). $P(T > 24) = 0.60$.
  - $B$: Instance survives past 10 hours ($T > 10$). $P(T > 10) = 0.85$.
- **Step 2: WIP State.**
  We seek $P(T > 24 \mid T > 10) = \frac{P(T > 24 \cap T > 10)}{P(T > 10)}$.
  Since $T > 24$ is a subset of $T > 10$, $P(T > 24 \cap T > 10) = P(T > 24) = 0.60$.
  $$P(T > 24 \mid T > 10) = \frac{0.60}{?}$$
- **Step 3: Final Calculation.**
  $$P(T > 24 \mid T > 10) = \frac{0.60}{0.85} \approx 0.7059$$

---

### Exercise 2: Server Response Time SLA
**Problem:** A web service records response times $T$ (in ms). Historical data shows $P(T \le 100\text{ ms}) = 0.70$ and $P(T \le 300\text{ ms}) = 0.95$. If a request has not completed within 100 ms, what is the probability it completes within 300 ms?

**Solution:**
- **Step 1: Define events.**
  - $A$: $T \le 300$.
  - $B$: $T > 100$, so $P(B) = 1 - P(T \le 100) = 1 - 0.70 = 0.30$.
- **Step 2: WIP State.**
  $P(A \cap B) = P(100 < T \le 300) = P(T \le 300) - P(T \le 100) = 0.95 - 0.70 = 0.25$.
  $$P(T \le 300 \mid T > 100) = \frac{0.25}{?}$$
- **Step 3: Final Calculation.**
  $$P(T \le 300 \mid T > 100) = \frac{0.25}{0.30} = \frac{5}{6} \approx 0.8333$$

---

### Exercise 3: Two-Way Frequency Table of Incident Resolution Times
**Problem:** A company logs 200 IT incident resolution times across Day and Night shifts.

| Shift | $\le 1\text{ hr}$ | $> 1\text{ hr}$ | Total |
| :--- | :---: | :---: | :---: |
| Day Shift ($D$) | 90 | 30 | 120 |
| Night Shift ($N$) | 40 | 40 | 80 |
| **Total** | **130** | **70** | **200** |

Find the probability that an incident took more than 1 hour to resolve, given it occurred during the Night shift.

**Solution:**
- **Step 1: Identify conditioning event and intersection.**
  Conditioning event: Night shift ($N$), with $n(N) = 80$.
  Target event: $> 1\text{ hr}$ during Night shift, with $n(>1\text{ hr} \cap N) = 40$.
- **Step 2: WIP State.**
  $$P(>1\text{ hr} \mid N) = \frac{n(>1\text{ hr} \cap N)}{n(N)} = \frac{40}{?}$$
- **Step 3: Final Calculation.**
  $$P(>1\text{ hr} \mid N) = \frac{40}{80} = 0.50$$

---

### Exercise 4: Sequential Network Hops (Multiplication Rule)
**Problem:** A network packet must traverse 3 routers in sequence. The probability of successfully passing Router 1 is 0.98. Given Router 1 is passed, the probability of passing Router 2 is 0.95. Given Routers 1 and 2 are passed, the probability of passing Router 3 is 0.90. What is the probability the packet completes the entire path?

**Solution:**
- **Step 1: Map probabilities.**
  - $P(R_1) = 0.98$
  - $P(R_2 \mid R_1) = 0.95$
  - $P(R_3 \mid R_1 \cap R_2) = 0.90$
- **Step 2: WIP State.**
  $$P(R_1 \cap R_2 \cap R_3) = P(R_1) \cdot P(R_2 \mid R_1) \cdot P(R_3 \mid R_1 \cap R_2) = 0.98 \cdot 0.95 \cdot ?$$
- **Step 3: Final Calculation.**
  $$P(R_1 \cap R_2 \cap R_3) = 0.98 \cdot 0.95 \cdot 0.90 = 0.8379$$

---

### Exercise 5: Battery Discharge Time Bounds
**Problem:** A sensor battery lifetime $T$ (hours) has $P(T > 50) = 0.90$ and $P(T > 100) = 0.45$. If the sensor is verified working at 50 hours, what is the probability it dies before reaching 100 hours?

**Solution:**
- **Step 1: Identify target event.**
  We want $P(T \le 100 \mid T > 50) = 1 - P(T > 100 \mid T > 50)$.
- **Step 2: WIP State.**
  First compute survival conditional probability:
  $$P(T > 100 \mid T > 50) = \frac{P(T > 100)}{P(T > 50)} = \frac{0.45}{0.90} = 0.50$$
  Then compute complement:
  $$P(T \le 100 \mid T > 50) = 1 - ?$$
- **Step 3: Final Calculation.**
  $$P(T \le 100 \mid T > 50) = 1 - 0.50 = 0.50$$

---

### Exercise 6: Microservice Timeout Cascade
**Problem:** In a distributed pipeline, Service A takes $T_A$ ms and Service B takes $T_B$ ms. $P(T_A \le 50) = 0.80$. If $T_A \le 50$, Service B receives normal priority and $P(T_B \le 50 \mid T_A \le 50) = 0.90$. If $T_A > 50$, Service B is throttled and $P(T_B \le 50 \mid T_A > 50) = 0.40$. Find the probability that both services finish within 50 ms.

**Solution:**
- **Step 1: Identify required intersection.**
  Target: $P(T_A \le 50 \cap T_B \le 50)$.
- **Step 2: WIP State.**
  Using the multiplication rule:
  $$P(T_A \le 50 \cap T_B \le 50) = P(T_A \le 50) \cdot P(T_B \le 50 \mid T_A \le 50) = 0.80 \cdot ?$$
- **Step 3: Final Calculation.**
  $$P(T_A \le 50 \cap T_B \le 50) = 0.80 \cdot 0.90 = 0.72$$

---

### Exercise 7: Database Query Delay Under Peak Load
**Problem:** During peak hours ($B$), query response times $T$ exceed 500 ms with probability 0.35. During off-peak hours ($B^c$), query response times exceed 500 ms with probability 0.05. A benchmark is run during peak hours. What is the conditional probability that a query finishes in $\le 500\text{ ms}$?

**Solution:**
- **Step 1: Identify given conditional.**
  Given: $P(T > 500 \mid B) = 0.35$.
- **Step 2: WIP State.**
  The complement event is $(T \le 500 \mid B)$:
  $$P(T \le 500 \mid B) = 1 - P(T > 500 \mid B) = 1 - ?$$
- **Step 3: Final Calculation.**
  $$P(T \le 500 \mid B) = 1 - 0.35 = 0.65$$

---

### Exercise 8: Machine Maintenance Window Survival
**Problem:** Equipment maintenance is scheduled at $t=100\text{ days}$. Historical failure times $T$ satisfy $P(T > 80) = 0.88$ and $P(T > 100) = 0.77$. Given equipment reaches 80 days without failure, what is the probability it fails before the scheduled maintenance at 100 days?

**Solution:**
- **Step 1: Set up conditional expression.**
  $$P(T \le 100 \mid T > 80) = 1 - P(T > 100 \mid T > 80)$$
- **Step 2: WIP State.**
  $$P(T > 100 \mid T > 80) = \frac{P(T > 100)}{P(T > 80)} = \frac{0.77}{0.88} = 0.875$$
  $$P(T \le 100 \mid T > 80) = 1 - ?$$
- **Step 3: Final Calculation.**
  $$P(T \le 100 \mid T > 80) = 1 - 0.875 = 0.125 \text{ (12.5\%)}$$

---

### Exercise 9: Software Build Failure Stages
**Problem:** A CI/CD build has two timed phases: Compilation ($C$) and Testing ($T$). 90% of builds pass Compilation within 2 minutes ($P(C) = 0.90$). Of those that pass Compilation within 2 minutes, 85% pass Testing within 5 minutes ($P(T \mid C) = 0.85$). Find the probability a build fails at or before Testing.

**Solution:**
- **Step 1: Find probability of overall success.**
  $P(\text{Success}) = P(C \cap T) = P(C) \cdot P(T \mid C) = 0.90 \cdot 0.85 = 0.765$.
- **Step 2: WIP State.**
  $P(\text{Failure}) = 1 - P(\text{Success}) = 1 - ?$.
- **Step 3: Final Calculation.**
  $$P(\text{Failure}) = 1 - 0.765 = 0.235 \text{ (23.5\%)}$$

---

### Exercise 10: R Code Snippet -- Empirical Conditional Latency Calculation
**Problem:** Given a vector of latency observations in milliseconds, write R code to calculate the conditional probability $P(T \le 250 \mid T > 100)$.

**Solution:**

```r
# Simulated log of request response times (in ms)
set.seed(42)
latencies_ms <- rgamma(1000, shape = 2, scale = 80)

# Filter subset where T > 100 ms (Conditioning event B)
conditioned_subset <- latencies_ms[latencies_ms > 100]

# Count how many in conditioned subset satisfy T <= 250 ms (Event A)
favorable_count <- sum(conditioned_subset <= 250)
total_conditioned <- length(conditioned_subset)

# Empirical conditional probability
p_cond <- favorable_count / total_conditioned

cat("Number of requests exceeding 100 ms:", total_conditioned, "\n")
cat("Number of those completing within 250 ms:", favorable_count, "\n")
cat("Conditional Probability P(T <= 250 | T > 100):", round(p_cond, 4), "\n")
```

**Interpretation of Output:**
The subsetting operation `latencies_ms[latencies_ms > 100]` directly implements the reduced sample space logic, ensuring that the denominator is strictly the count of observations exceeding 100 ms.
