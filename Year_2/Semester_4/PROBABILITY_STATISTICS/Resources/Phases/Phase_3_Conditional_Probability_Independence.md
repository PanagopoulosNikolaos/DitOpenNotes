# Phase 3: Conditional Probability & Independence

## Table of Contents
1. [Conditional Probability](#1-conditional-probability)
2. [Independence](#2-independence)
3. [Law of Total Probability & Bayes' Theorem](#3-law-of-total-probability--bayes-theorem)
4. [Time-Specific Gotchas](#4-time-specific-gotchas)
5. [Solved Exercises](#5-solved-exercises)
6. [Phase Summary](#phase-summary)

---

## 1. Conditional Probability

Conditional probability measures the likelihood of an event occurring, given that another event has already taken place. This "given" information effectively restricts the sample space to a specific subset.

### The Fundamental Formula
If $P(B) > 0$, the conditional probability of $A$ given $B$ is defined as:
$$P(A|B) = \frac{P(A \cap B)}{P(B)}$$

Where:
*   $P(A|B)$: Probability of $A$ occurring given $B$ has occurred.
*   $P(A \cap B)$: Probability that both $A$ and $B$ occur (Intersection).
*   $P(B)$: Probability of the conditioning event $B$.

**Intuitive Understanding (Reducing the Sample Space):**
Imagine a sample space $S$. When we say "given $B$", we are throwing away any part of $S$ that is not $B$. The new sample space becomes $B$. We then look for the portion of $A$ that survived this "filtering" process, which is exactly $A \cap B$.

### Conditional Probability in Time-Based Systems
In time-based systems, the conditioning event is frequently defined by elapsed durations, surviving times, or timestamp thresholds. Let $T$ be a non-negative random variable representing a duration.
The conditional probability that an operation completes before time $t_2$, given that it has already surpassed time $t_1$ (where $t_2 > t_1$), is:
$$P(T \le t_2 \mid T > t_1) = \frac{P(t_1 < T \le t_2)}{P(T > t_1)}$$

Similarly, the conditional survival probability (surviving an additional duration $s$ after surviving up to time $t$) is:
$$P(T > t + s \mid T > t) = \frac{P(T > t + s)}{P(T > t)}$$

### The Multiplication Rule
By rearranging the formula, we get the Multiplication Rule to find the probability of an intersection:
$$P(A \cap B) = P(B) \cdot P(A|B) = P(A) \cdot P(B|A)$$
For multi-stage sequential processes:
$$P(A_1 \cap A_2 \cap \dots \cap A_n) = P(A_1) \cdot P(A_2 \mid A_1) \dots P(A_n \mid A_1 \cap \dots \cap A_{n-1})$$

---

## 2. Independence

Independence is a statistical property where the occurrence of one event does not affect the probability of another event occurring.

### Mathematical Condition
Two events $A$ and $B$ are **independent** if the knowledge that $B$ has occurred does not change the probability of $A$. The **Product Rule** defines this:
$$P(A \cap B) = P(A) \cdot P(B)$$
Equivalently: $P(A|B) = P(A)$ and $P(B|A) = P(B)$.

### Independence vs. Mutually Exclusive
*   **Mutually Exclusive (Disjoint):** Events *cannot* happen at the same time ($P(A \cap B) = 0$). If $A$ happens, $B$ definitely cannot happen.
*   **Independent:** Events *can* happen at the same time, but they don't influence each other.
> **Shortcut:** If $A$ and $B$ have non-zero probabilities and are mutually exclusive, they **cannot** be independent.

### System Reliability over Execution Time
Consider $n$ components with independent lifetimes $T_1, T_2, \dots, T_n$:
1. **Series System (Requires all components to run):**
   $$P(T_{\text{sys}} > t) = \prod_{i=1}^{n} P(T_i > t)$$
2. **Parallel System (Requires at least one component to run):**
   $$P(T_{\text{sys}} \le t) = \prod_{i=1}^{n} P(T_i \le t)$$

---

## 3. Law of Total Probability & Bayes' Theorem

These two theorems are the most powerful tools in probability for handling multi-stage processes and updating beliefs based on new evidence.

### Law of Total Probability
If we have a set of events $B_1, B_2, \dots, B_n$ that **partition** the sample space (mutually exclusive and their union is the whole space), then for any event $A$:
$$P(A) = \sum_{i=1}^{n} P(A|B_i)P(B_i) = P(A|B_1)P(B_1) + \dots + P(A|B_n)P(B_n)$$

### Bayes' Theorem
Bayes' Theorem allows us to "reverse" conditional probabilities. If we know $P(A|B)$, we can find $P(B|A)$:
$$P(B_k|A) = \frac{P(A|B_k)P(B_k)}{P(A)} = \frac{P(A|B_k)P(B_k)}{\sum_{j=1}^{n} P(A|B_j)P(B_j)}$$
- **Prior Probability $P(B_k)$:** The baseline probability of state $B_k$.
- **Likelihood $P(A \mid B_k)$:** The probability of observing event $A$ given state $B_k$.
- **Posterior Probability $P(B_k \mid A)$:** The updated probability of state $B_k$ given event $A$ occurred.

---

## 4. Time-Specific Gotchas

1. **Conflating Elapsed Time with Remaining Time:** Assuming $P(T > t + s \mid T > t) = P(T > s)$ is only true for memoryless distributions (like the Exponential distribution). For aging systems, always evaluate the denominator $P(T > t)$ explicitly.
2. **Right-Censored Observation Windows:** If a process hasn't finished by a max window $T_{\text{max}}$, its duration is unknown. Not accounting for this under-estimates long latencies.
3. **Mixed Unit Prefixes:** When calculating $P(A \cap B) / P(B)$, ensure both use identical time units (e.g., ms vs seconds).
4. **Consecutive Time Windows (Autocorrelation):** Treating consecutive time intervals (e.g., minute $t$ and $t+1$) as independent often fails because they are correlated.
5. **Shared Infrastructure Contention:** Two timers on separate VMs may seem independent but could share a physical clock or hypervisor, violating independence during host overload.
6. **Non-Exhaustive Time Partitions:** When using Total Probability, the time fractions must sum to 1.
7. **Confusing Prior Duration with Posterior Probabilities:** If a system is in High-Load 10% of the time, the probability it was in High-Load *given* a timeout occurred is a posterior probability, which will be much higher than 10%.

---

## 5. Solved Exercises

#### Exercise 1: Medical Diagnostic Test (Classic Bayes)
**Problem:** A disease affects 1% of the population. A test is 95% accurate for those with the disease and 90% accurate for those without. If a person tests positive, what is the probability they have the disease?
**Solution:**
- $P(H) = 0.01, P(H^c) = 0.99$
- $P(Pos|H) = 0.95, P(Pos|H^c) = 1 - 0.90 = 0.10$
- Total probability $P(Pos) = (0.95 \cdot 0.01) + (0.10 \cdot 0.99) = 0.0095 + 0.0990 = 0.1085$.
- Bayes: $P(H|Pos) = \frac{0.0095}{0.1085} \approx 0.0876 \text{ (8.76\%)}$.

#### Exercise 2: System Uptime Survival Probability
**Problem:** The probability a cloud instance functions past 10 hours is 0.85, and past 24 hours is 0.60. Given it has run for 10 hours, what is the probability it reaches 24 hours?
**Solution:**
$$P(T > 24 \mid T > 10) = \frac{P(T > 24 \cap T > 10)}{P(T > 10)} = \frac{P(T > 24)}{P(T > 10)} = \frac{0.60}{0.85} \approx 0.7059$$

#### Exercise 3: Server Response Time SLA
**Problem:** A service records response times $T$ in ms. $P(T \le 100) = 0.70$ and $P(T \le 300) = 0.95$. If a request has not completed within 100 ms, what is the probability it completes within 300 ms?
**Solution:**
$P(T > 100) = 0.30$.
$P(100 < T \le 300) = 0.95 - 0.70 = 0.25$.
$$P(T \le 300 \mid T > 100) = \frac{0.25}{0.30} \approx 0.8333$$

#### Exercise 4: Two-Way Frequency Table of Incident Resolution Times
**Problem:** Out of 200 incidents, Day Shift had 90 $\le 1\text{ hr}$ and 30 $>1\text{ hr}$. Night Shift had 40 $\le 1\text{ hr}$ and 40 $>1\text{ hr}$. Find probability an incident took $>1\text{ hr}$ given Night shift.
**Solution:**
Night Shift Total = 80. Night Shift $>1\text{ hr}$ = 40.
$$P(>1\text{ hr} \mid N) = \frac{40}{80} = 0.50$$

#### Exercise 5: Sequential Network Hops
**Problem:** Packet passes Router 1 with 0.98. Given R1, it passes R2 with 0.95. Given R1 and R2, passes R3 with 0.90. What is the probability it completes the path?
**Solution:**
$$P(R_1 \cap R_2 \cap R_3) = 0.98 \cdot 0.95 \cdot 0.90 = 0.8379$$

#### Exercise 6: Microservice Timeout Cascade
**Problem:** Service A takes $T_A$ ms, B takes $T_B$ ms. $P(T_A \le 50) = 0.80$. $P(T_B \le 50 \mid T_A \le 50) = 0.90$. Find the probability both finish within 50 ms.
**Solution:**
$$P(T_A \le 50 \cap T_B \le 50) = 0.80 \cdot 0.90 = 0.72$$

#### Exercise 7: Independent Server Timeout Events
**Problem:** Two isolated servers have independent timeout probabilities: $P(T_1) = 0.04$ and $P(T_2) = 0.05$. Probability both timeout?
**Solution:**
$$P(T_1 \cap T_2) = 0.04 \cdot 0.05 = 0.0020 \text{ (0.2\%)}$$

#### Exercise 8: Parallel Redundant Watchdog Timers
**Problem:** Two independent hardware timers have failure probability $0.02$ each over 24 hours. Probability system works (at least one works)?
**Solution:**
$P(F_1 \cap F_2) = 0.02 \cdot 0.02 = 0.0004$.
$P(\text{System Works}) = 1 - 0.0004 = 0.9996 \text{ (99.96\%)}$.

#### Exercise 9: Series Pipeline Lifetime
**Problem:** 3 sequential stages operate independently. Survival probabilities $P(T_1 > 8) = 0.95, P(T_2 > 8) = 0.90, P(T_3 > 8) = 0.98$. Pipeline survival?
**Solution:**
$$P(T_{\text{sys}} > 8) = 0.95 \cdot 0.90 \cdot 0.98 = 0.8379$$

#### Exercise 10: Testing Independence of Latency Spikes
**Problem:** Service A spikes in 100/1000 mins ($0.10$). B spikes in 150/1000 mins ($0.15$). Both spike in 30/1000 mins ($0.03$). Are they independent?
**Solution:**
$P(A) \cdot P(B) = 0.10 \cdot 0.15 = 0.015$.
Since $P(A \cap B) = 0.03 \neq 0.015$, they are dependent.

#### Exercise 11: Probability of At Least One Outage
**Problem:** Probability of network glitch in 1 hour is 0.10. Across 4 independent hours, find probability of at least one glitch.
**Solution:**
$P(\text{No glitch in 1 hr}) = 0.90$.
$P(\text{No glitches in 4 hrs}) = (0.90)^4 = 0.6561$.
$P(\text{At least 1}) = 1 - 0.6561 = 0.3439 \text{ (34.39\%)}$.

#### Exercise 12: Probability of Exactly One Service Timeout
**Problem:** Independent microservices have timeouts $P(T_A) = 0.15, P(T_B) = 0.10$. Probability exactly one times out?
**Solution:**
$P(T_A \cap T_B^c) = 0.15 \cdot 0.90 = 0.135$.
$P(T_B \cap T_A^c) = 0.10 \cdot 0.85 = 0.085$.
$P(\text{Exactly one}) = 0.135 + 0.085 = 0.220$.

#### Exercise 13: Overall Latency Spike Probability (Total Probability)
**Problem:** Morning Peak (40%), Afternoon (40%), Night (20%). Probability query $>100\text{ ms}$ is 0.15, 0.05, 0.01 respectively. Find total probability.
**Solution:**
$$P(A) = (0.15 \cdot 0.40) + (0.05 \cdot 0.40) + (0.01 \cdot 0.20) = 0.060 + 0.020 + 0.002 = 0.082 \text{ (8.2\%)}$$

#### Exercise 14: Diagnosing Load Regime from Latency Spike (Bayes)
**Problem:** Using Exercise 13, if a query takes $>100\text{ ms}$, what is the posterior probability it was Morning Peak?
**Solution:**
$$P(B_1 \mid A) = \frac{0.15 \cdot 0.40}{0.082} = \frac{0.060}{0.082} \approx 0.7317 \text{ (73.17\%)}$$

#### Exercise 15: Software Bug Discovery Timing
**Problem:** Bugs found in Unit Test (50%), Integration (30%), Production (20%). Prob bug takes $>24\text{h}$ to resolve is 0.10, 0.40, 0.90 respectively. Total probability a bug takes $>24\text{h}$?
**Solution:**
$$P(>24\text{h}) = (0.10 \cdot 0.50) + (0.40 \cdot 0.30) + (0.90 \cdot 0.20) = 0.05 + 0.12 + 0.18 = 0.350$$

#### Exercise 16: Cloud Server Crash Diagnosis
**Problem:** Reboots due to Memory Leaks (50%), Power Spikes (30%), OS Updates (20%). Reboot $>5\text{m}$ probability is 0.90, 0.10, 0.30 respectively. Given reboot $>5\text{m}$, probability it was Memory Leak?
**Solution:**
$$P(>5\text{m}) = (0.90 \cdot 0.50) + (0.10 \cdot 0.30) + (0.30 \cdot 0.20) = 0.45 + 0.03 + 0.06 = 0.54$$
$$P(\text{Leak} \mid >5\text{m}) = \frac{0.45}{0.54} = \frac{5}{6} \approx 0.8333$$

#### Exercise 17: R Code Snippet -- Empirical Conditional Latency Calculation
**Problem:** R code to calculate conditional probability $P(T \le 250 \mid T > 100)$.
**Solution:**
```r
latencies_ms <- rgamma(1000, shape = 2, scale = 80)
conditioned_subset <- latencies_ms[latencies_ms > 100]
p_cond <- sum(conditioned_subset <= 250) / length(conditioned_subset)
```

#### Exercise 18: R Code Snippet -- Testing Independence
**Problem:** R code to test whether delays in two consecutive steps are statistically independent.
**Solution:**
```r
cor_val <- cor(t1, t2)
test_res <- cor.test(t1, t2)
```

#### Exercise 19: R Code Snippet -- Bayes Updating
**Problem:** R function for Bayes' updating.
**Solution:**
```r
bayes_time_update <- function(priors, likelihoods) {
  p_total <- sum(priors * likelihoods)
  posteriors <- (priors * likelihoods) / p_total
  return(list(total_prob = p_total, posteriors = posteriors))
}
```

---

## Phase Summary
- Conditional Probability $P(A|B) = \frac{P(A \cap B)}{P(B)}$ measures the probability of $A$ in the restricted sample space where $B$ has already occurred.
- The Multiplication Rule is derived from conditional probability and is essential for evaluating intersections of sequential events.
- Events are Independent if $P(A \cap B) = P(A)P(B)$. Independence implies that the occurrence of one event provides no information about the other.
- Mutually exclusive non-zero events are never independent (they are maximally dependent).
- For independent components, Series Systems survive if all components survive ($\prod P(T_i > t)$), and Parallel Systems fail if all components fail ($\prod P(T_i \le t)$).
- The Law of Total Probability computes the overall probability of an event by summing its occurrence across all mutually exclusive and exhaustive partitions of the sample space.
- Bayes' Theorem $P(B_k|A) = \frac{P(A|B_k)P(B_k)}{P(A)}$ provides the mechanism to reverse conditional probabilities, updating prior beliefs (e.g., time regime probabilities) based on new evidence (e.g., an observed anomaly).
- When applying these concepts to time series or system logs, right-censoring, correlated consecutive intervals, and unnormalized rates are the most common sources of error.
