# Phase 3: Conditional Probability & Independence

## Table of Contents
- [Section 3.1: Conditional Probability & Reduced Sample Space](#section-31-conditional-probability--reduced-sample-space)
- [Section 3.2: Multiplication Rule & Sequential Processes](#section-32-multiplication-rule--sequential-processes)
- [Section 3.3: Independence & System Reliability](#section-33-independence--system-reliability)
- [Section 3.4: Law of Total Probability & Bayes' Theorem](#section-34-law-of-total-probability--bayes-theorem)
- [Exam Preparation Guide](#exam-preparation-guide)
- [Phase Summary](#phase-summary)

---

## Section 3.1: Conditional Probability & Reduced Sample Space

### Core Theory & Definitions

Conditional probability evaluates the likelihood of an event $A$ occurring given that another event $B$ has already taken place ($P(B) > 0$). When we condition on $B$, the universal sample space $\Omega$ shrinks to $B$. Outcome elements outside $B$ become impossible and are discarded. The relevant subset of $A$ within this restricted universe is precisely the intersection $A \cap B$.

```
Universal Sample Space Ω:
+------------------------------------+
|  A only     | A ∩ B  |  B only     |
|             |        |             |
+-------------+--------+-------------+
                 ^^^^^^
         Conditioning on B shrinks
         the sample space from Ω to B.
```

Mathematically, conditional probability behaves as a true probability measure on the restricted sample space $B$. It satisfies all three Kolmogorov Axioms:

1. **Non-negativity:** For any event $A \subseteq \Omega$, $0 \le P(A \mid B) \le 1$.
2. **Normalization:** $P(\Omega \mid B) = \frac{P(\Omega \cap B)}{P(B)} = \frac{P(B)}{P(B)} = 1$, and similarly $P(B \mid B) = 1$.
3. **Countable Additivity:** For any sequence of mutually disjoint events $A_1, A_2, A_3, \dots$ (where $A_i \cap A_j = \emptyset$ for $i \neq j$):
   $$P\left( \bigcup_{i=1}^{\infty} A_i \;\middle|\; B \right) = \sum_{i=1}^{\infty} P(A_i \mid B)$$

#### Time-Domain Application: Survival Probability & Right-Censoring

In time-series analysis, performance engineering, and reliability testing, conditional probability frequently measures execution lifetimes and delay thresholds. Let $T \ge 0$ be a non-negative continuous random variable representing duration (e.g., latency, system uptime, job completion time in seconds or milliseconds).

The **conditional survival probability** measures the probability that a system continues running for an additional duration $s$, given that it has already survived up to time $t$:
$$P(T > t + s \mid T > t) = \frac{P(T > t + s \cap T > t)}{P(T > t)} = \frac{P(T > t + s)}{P(T > t)}$$

A critical practical challenge in time data analysis is **right-censored observation windows**. In continuous measurement systems, observation monitors stop recording at a maximum observation window $T_{\text{max}}$. If a request or job has not completed by $T_{\text{max}}$, its true duration is unknown—we only know $T > T_{\text{max}}$. If an analyst discards censored observations or treats $T_{\text{max}}$ as the actual completion time, conditional probabilities and tail latency estimates will be severely biased (underestimating long latencies).

---

### Mathematical Formulas & Derivations

#### Fundamental Conditional Probability Formula
For any two events $A$ and $B$ in a sample space $\Omega$ with $P(B) > 0$:
$$P(A \mid B) = \frac{P(A \cap B)}{P(B)}$$

Similarly, if $P(A) > 0$:
$$P(B \mid A) = \frac{P(A \cap B)}{P(A)}$$

#### Conditional Complement Rule
$$P(A^c \mid B) = 1 - P(A \mid B)$$

*Proof:*
$$P(A^c \mid B) = \frac{P(A^c \cap B)}{P(B)} = \frac{P(B) - P(A \cap B)}{P(B)} = 1 - \frac{P(A \cap B)}{P(B)} = 1 - P(A \mid B)$$

#### Conditional Inclusion-Exclusion Principle
$$P(A_1 \cup A_2 \mid B) = P(A_1 \mid B) + P(A_2 \mid B) - P(A_1 \cap A_2 \mid B)$$

#### Time-Domain Adapted Formulas (with Explicit Units)

When working with latency, duration, or time-series data, all duration parameters must explicitly state their time units (e.g., $[s]$, $[ms]$, $[\mu s]$).

1. **Conditional Latency Threshold Formula:**
   $$P(T \le t_{2,[ms]} \mid T > t_{1,[ms]}) = \frac{P(t_{1,[ms]} < T \le t_{2,[ms]})}{P(T > t_{1,[ms]})} = \frac{F_T(t_{2,[ms]}) - F_T(t_{1,[ms]})}{1 - F_T(t_{1,[ms]})}$$
   where $F_T(t) = P(T \le t)$ is the Cumulative Distribution Function (CDF).

2. **Conditional Survival Function Formula:**
   $$S_T(s_{[s]} \mid t_{[s]}) = P(T > t_{[s]} + s_{[s]} \mid T > t_{[s]}) = \frac{S_T((t+s)_{[s]})}{S_T(t_{[s]})}$$
   where $S_T(t) = P(T > t) = 1 - F_T(t)$ is the Survival Function.

> **Practical / Time-Domain Note:**
> Memoryless distributions (such as the Exponential distribution for continuous time or Geometric distribution for discrete steps) satisfy $P(T > t + s \mid T > t) = P(T > s)$. However, real-world hardware aging, memory leak accumulation, and queue buildup are **aging processes** where $P(T > t + s \mid T > t) < P(T > s)$. Never assume memorylessness without verifying distribution metrics.

---

### Worked Exercises

#### Exercise 1: Medical Diagnostic Contingency Table
**Problem:** A clinical study evaluates 500 patient records for a respiratory condition. 120 patients tested positive ($Pos$), of which 90 actually had the condition ($D$). Out of 380 patients who tested negative ($Neg$), 20 had the condition.
**a)** Calculate $P(D \mid Pos)$ (Positive Predictive Value).
**b)** Calculate $P(D^c \mid Neg)$ (Negative Predictive Value).

**Solution:**
**Step 1:** Construct the complete 2x2 contingency table:

| Condition | Positive Test ($Pos$) | Negative Test ($Neg$) | Total |
| :--- | :--- | :--- | :--- |
| **Disease ($D$)** | 90 | 20 | 110 |
| **No Disease ($D^c$)** | 30 | 360 | 390 |
| **Total** | 120 | 380 | 500 |

**Step 2:** Compute $P(D \mid Pos)$ using the reduced sample space of $Pos$ (120 patients):
$$P(D \mid Pos) = \frac{P(D \cap Pos)}{P(Pos)} = \frac{90 / 500}{120 / 500} = \frac{90}{120} = 0.75$$

**Step 3:** Compute $P(D^c \mid Neg)$ using the reduced sample space of $Neg$ (380 patients):
$$P(D^c \mid Neg) = \frac{P(D^c \cap Neg)}{P(Neg)} = \frac{360 / 500}{380 / 500} = \frac{360}{380} = \frac{18}{19} \approx 0.9474$$

Final Answer: **a) 0.7500 (75.00%)**, **b) 0.9474 (94.74%)**

---

#### Exercise 2: Urn Ball Selection Without Replacement
**Problem:** An urn contains 7 red balls and 5 blue balls. Two balls are drawn sequentially without replacement.
**a)** What is the probability that the second ball drawn is blue, given that the first ball drawn was red?
**b)** What is the joint probability that the first ball is red and the second ball is blue?

**Solution:**
**a)** Step 1: Initial state has $7 + 5 = 12$ total balls.
Step 2: Given the first ball drawn was red ($R_1$), the urn now contains 6 red balls and 5 blue balls ($6 + 5 = 11$ total remaining).
Step 3: The conditional probability of drawing a blue ball on the second draw ($B_2$) is:
$$P(B_2 \mid R_1) = \frac{5}{11} \approx 0.4545$$

**b)** Apply the multiplication rule:
$$P(R_1 \cap B_2) = P(R_1) \cdot P(B_2 \mid R_1) = \left( \frac{7}{12} \right) \cdot \left( \frac{5}{11} \right) = \frac{35}{132} \approx 0.2652$$

Final Answer: **a) 5/11 (0.4545)**, **b) 35/132 (0.2652)**

---

#### Exercise 3: Industrial Component Defect Probability
**Problem:** In a factory manufacturing batch, 15% of components have surface scratches ($S$), 10% have electrical defects ($E$), and 4% have both defects.
**a)** If a randomly chosen component has a surface scratch, what is the probability it also has an electrical defect?
**b)** If a component has no electrical defect, what is the probability it has no surface scratch?

**Solution:**
**Step 1:** Given probabilities: $P(S) = 0.15$, $P(E) = 0.10$, $P(S \cap E) = 0.04$.

**Step 2:** For part **a)**:
$$P(E \mid S) = \frac{P(S \cap E)}{P(S)} = \frac{0.04}{0.15} = \frac{4}{15} \approx 0.2667$$

**Step 3:** For part **b)**, we need $P(S^c \mid E^c) = \frac{P(S^c \cap E^c)}{P(E^c)}$.
Using De Morgan's Law: $P(S^c \cap E^c) = 1 - P(S \cup E)$.
$$P(S \cup E) = P(S) + P(E) - P(S \cap E) = 0.15 + 0.10 - 0.04 = 0.21$$
$$P(S^c \cap E^c) = 1 - 0.21 = 0.79$$
$$P(E^c) = 1 - P(E) = 1 - 0.10 = 0.90$$
$$P(S^c \mid E^c) = \frac{0.79}{0.90} = \frac{79}{90} \approx 0.8778$$

Final Answer: **a) 4/15 (0.2667)**, **b) 79/90 (0.8778)**

---

#### Exercise 4: Server SLA Response Time Threshold (Time-Domain)
**Problem:** Latency logs for a database cluster show that 75% of queries finish within $100\,[ms]$ ($P(T \le 100) = 0.75$) and 95% of queries finish within $300\,[ms]$ ($P(T \le 300) = 0.95$).
**a)** If a query has already exceeded $100\,[ms]$, what is the conditional probability that it finishes within $300\,[ms]$?
**b)** What R command computes this conditional probability from an empirical vector `latencies_ms`?

**Solution:**
**Step 1:** Define the events:
$A = \{T \le 300\,[ms]\}$, $B = \{T > 100\,[ms]\}$.
The intersection $A \cap B = \{100\,[ms] < T \le 300\,[ms]\}$.

**Step 2:** Compute individual probabilities:
$$P(B) = P(T > 100) = 1 - P(T \le 100) = 1 - 0.75 = 0.25$$
$$P(A \cap B) = P(100 < T \le 300) = P(T \le 300) - P(T \le 100) = 0.95 - 0.75 = 0.20$$

**Step 3:** Calculate conditional probability using the time-domain adapted formula:
$$P(T \le 300 \mid T > 100) = \frac{P(100 < T \le 300)}{P(T > 100)} = \frac{0.20}{0.25} = 0.8000$$

**Step 4:** R implementation:
```r
# R snippet for empirical conditional latency calculation
sub_vec <- latencies_ms[latencies_ms > 100]
p_cond <- sum(sub_vec <= 300) / length(sub_vec)
```

Final Answer: **a) 0.8000 (80.00%)**, **b) R command provided above**

---

#### Exercise 5: Microservice Latency Survival & Right-Censoring (Time-Domain)
**Problem:** Execution duration $T\,[s]$ of a distributed job has survival function $S_T(t) = \frac{1}{(1 + 0.1t)^2}$ for $t \ge 0$.
**a)** Calculate the probability that a job runs for more than $20\,[s]$, given it has survived past $10\,[s]$.
**b)** An analyst monitors jobs only up to $T_{\text{max}} = 10\,[s]$ and records all uncompleted jobs as exactly $10\,[s]$. Explain the effect of this right-censoring on conditional survival estimation.

**Solution:**
**a)** Step 1: Evaluate $S_T(10)$ and $S_T(20)$:
$$S_T(10) = P(T > 10) = \frac{1}{(1 + 0.1(10))^2} = \frac{1}{2^2} = \frac{1}{4} = 0.2500$$
$$S_T(20) = P(T > 20) = \frac{1}{(1 + 0.1(20))^2} = \frac{1}{3^2} = \frac{1}{9} \approx 0.1111$$

Step 2: Apply the conditional survival formula:
$$P(T > 20 \mid T > 10) = \frac{P(T > 20)}{P(T > 10)} = \frac{S_T(20)}{S_T(10)} = \frac{1/9}{1/4} = \frac{4}{9} \approx 0.4444$$

**b)** Right-censoring at $T_{\text{max}} = 10\,[s]$ truncates the tail. If jobs running $> 10\,[s]$ are assumed to terminate at $10\,[s]$, $P(T > 20 \mid T > 10)$ would be estimated as $0$, severely underestimating system delay risks.

Final Answer: **a) 4/9 (0.4444)**, **b) Right-censoring truncates the tail and underestimates tail risk**

---

#### Exercise 6: Incident Resolution Times Across Server Clusters (Time-Domain)
**Problem:** An IT ops team records incident resolution times across two shifts: Day Shift ($D$, 120 incidents) and Night Shift ($N$, 80 incidents). In Day Shift, 90 incidents resolved within $1\,[hr]$ ($\le 1$) and 30 took $> 1\,[hr]$. In Night Shift, 40 resolved within $1\,[hr]$ and 40 took $> 1\,[hr]$.
**a)** Find $P(> 1\,[hr] \mid N)$.
**b)** Find $P(N \mid > 1\,[hr])$.
**c)** Write an R snippet using `prop.table()` to compute both conditional distributions.

**Solution:**
**Step 1:** Construct table of counts:

| Shift | $\le 1\,[hr]$ | $> 1\,[hr]$ | Total |
| :--- | :--- | :--- | :--- |
| **Day ($D$)** | 90 | 30 | 120 |
| **Night ($N$)** | 40 | 40 | 80 |
| **Total** | 130 | 70 | 200 |

**Step 2:** Compute $P(> 1\,[hr] \mid N)$:
$$P(> 1\,[hr] \mid N) = \frac{40}{80} = 0.5000$$

**Step 3:** Compute $P(N \mid > 1\,[hr])$:
$$P(N \mid > 1\,[hr]) = \frac{40}{70} = \frac{4}{7} \approx 0.5714$$

**Step 4:** R implementation:
```r
# R snippet for table conditioning
counts <- matrix(c(90, 30, 40, 40), nrow = 2, byrow = TRUE,
                 dimnames = list(Shift = c("Day", "Night"), Time = c("<=1hr", ">1hr")))
p_time_given_shift  <- prop.table(counts, margin = 1) # Row conditional
p_shift_given_time  <- prop.table(counts, margin = 2) # Column conditional
```

Final Answer: **a) 0.5000 (50.00%)**, **b) 4/7 (0.5714)**, **c) R snippet provided above**

---

### R Implementation

```r
# R Implementation for Section 3.1: Conditional Probability & Filtering

# 1. Contingency Table Conditional Probabilities
tbl <- matrix(c(90, 30, 40, 40), nrow = 2, byrow = TRUE,
              dimnames = list(Shift = c("Day", "Night"), Duration = c("<=1hr", ">1hr")))

# Row-conditional probabilities P(Duration | Shift)
p_dur_given_shift <- prop.table(tbl, margin = 1)
print(p_dur_given_shift)

# Column-conditional probabilities P(Shift | Duration)
p_shift_given_dur <- prop.table(tbl, margin = 2)
print(p_shift_given_dur)

# 2. Empirical Vector Conditional Filtering (Time-Domain Latency)
set.seed(42)
latencies_ms <- rgamma(10000, shape = 2, scale = 80) # Sample latencies

# P(T <= 300 | T > 100)
denom_subset <- latencies_ms[latencies_ms > 100]
p_cond_empirical <- sum(denom_subset <= 300) / length(denom_subset)
cat("Empirical P(T <= 300 | T > 100):", round(p_cond_empirical, 4), "\n")
```

---

## Section 3.2: Multiplication Rule & Sequential Processes

### Core Theory & Definitions

The **Multiplication Rule** is derived directly by rearranging the conditional probability formula:
$$P(A \cap B) = P(B) \cdot P(A \mid B) = P(A) \cdot P(B \mid A)$$

This rule allows us to calculate the joint probability of multi-stage sequential processes by breaking them into a chain of conditional probabilities.

```
Stage 1: P(A_1)
   |
   +---> Stage 2: P(A_2 | A_1)
            |
            +---> Stage 3: P(A_3 | A_1 ∩ A_2)
```

#### Sampling With vs Without Replacement
- **Sampling With Replacement:** The sample space remains identical at each stage. Outcomes are independent: $P(A_2 \mid A_1) = P(A_2)$, so $P(A_1 \cap A_2) = P(A_1) \cdot P(A_2)$.
- **Sampling Without Replacement:** The sample space shrinks and composition changes after each draw. Outcomes are dependent: $P(A_2 \mid A_1) \neq P(A_2)$.

#### Time-Domain Application: Multi-Stage Pipelines & Cascades

In distributed computer systems, network routing, and software execution pipelines, request execution progresses through sequential dependent stages (e.g., DNS resolution -> TLS handshake -> Auth Check -> DB Query -> Serialization). The probability of a request successfully completing the entire pipeline without timing out or failing is computed via the Chain Rule of conditional probability.

---

### Mathematical Formulas & Derivations

#### General Chain Rule of Probability
For any sequence of $n$ events $A_1, A_2, \dots, A_n$ where $P(A_1 \cap A_2 \cap \dots \cap A_{n-1}) > 0$:
$$P(A_1 \cap A_2 \cap \dots \cap A_n) = P(A_1) \cdot P(A_2 \mid A_1) \cdot P(A_3 \mid A_1 \cap A_2) \cdots P(A_n \mid A_1 \cap A_2 \cap \dots \cap A_{n-1})$$

*Proof by Induction:*
For $n = 2$: $P(A_1 \cap A_2) = P(A_1) \cdot P(A_2 \mid A_1)$.
Assume true for $n = k$: $P(\bigcap_{i=1}^k A_i) = P(A_1) P(A_2 \mid A_1) \cdots P(A_k \mid \bigcap_{i=1}^{k-1} A_i)$.
For $n = k + 1$, let $E = \bigcap_{i=1}^k A_i$. Then:
$$P\left( \bigcap_{i=1}^{k+1} A_i \right) = P(E \cap A_{k+1}) = P(E) \cdot P(A_{k+1} \mid E) = \left[ \prod_{i=1}^k P\left(A_i \;\middle|\; \bigcap_{j=1}^{i-1} A_j\right) \right] \cdot P\left(A_{k+1} \;\middle|\; \bigcap_{j=1}^k A_j\right)$$

#### Time-Domain Sequential Pipeline Success Formula
For an $n$-stage processing pipeline where $S_i$ is the event that Stage $i$ completes within its allocation $t_{i,[ms]}$:
$$P(\text{Pipeline Success}) = P(S_1) \cdot P(S_2 \mid S_1) \cdot P(S_3 \mid S_1 \cap S_2) \cdots P(S_n \mid S_1 \cap \dots \cap S_{n-1})$$

> **Practical / Time-Domain Note:**
> In microservice architectures, stage completion times are often **positively correlated** (e.g., high database load causes both DB query latency and serialization latency to spike). Assuming independence across stages ($P(S_2 \mid S_1) = P(S_2)$) underestimates the probability of cumulative tail latency violations.

---

### Worked Exercises

#### Exercise 7: Consecutive Card Selection Without Replacement
**Problem:** A standard deck of 52 playing cards contains 4 Aces. Three cards are drawn sequentially without replacement.
**a)** Calculate the probability of drawing three consecutive Aces.
**b)** What R code evaluates this sequential cumulative probability?

**Solution:**
**Step 1:** Define events: $A_1$ (first card Ace), $A_2$ (second card Ace), $A_3$ (third card Ace).

**Step 2:** Apply the multiplication chain rule:
$$P(A_1) = \frac{4}{52}$$
$$P(A_2 \mid A_1) = \frac{3}{51}$$
$$P(A_3 \mid A_1 \cap A_2) = \frac{2}{50}$$

**Step 3:** Calculate the joint probability:
$$P(A_1 \cap A_2 \cap A_3) = \left( \frac{4}{52} \right) \cdot \left( \frac{3}{51} \right) \cdot \left( \frac{2}{50} \right) = \frac{24}{132600} = \frac{1}{5525} \approx 0.0001810$$

**Step 4:** R implementation:
```r
# R snippet for exact chain product
probs <- c(4/52, 3/51, 2/50)
p_three_aces <- prod(probs)
```

Final Answer: **a) 1/5525 (0.0001810)**, **b) R code provided above**

---

#### Exercise 8: Semiconductor Chip Defect Multi-Stage Inspection
**Problem:** A manufacturing lot contains 20 microchips, of which 4 are defective. An inspector randomly selects 3 chips without replacement for quality testing.
**a)** Find the probability that all 3 selected chips are non-defective.
**b)** Find the probability that at least 1 of the 3 selected chips is defective.

**Solution:**
**Step 1:** Non-defective chips count = $20 - 4 = 16$.

**Step 2:** For part **a)**, apply the chain rule for 3 non-defective draws ($G_1, G_2, G_3$):
$$P(G_1 \cap G_2 \cap G_3) = \left( \frac{16}{20} \right) \cdot \left( \frac{15}{19} \right) \cdot \left( \frac{14}{18} \right) = \frac{3360}{6840} = \frac{28}{57} \approx 0.4912$$

**Step 3:** For part **b)**, use the complement rule:
$$P(\text{At least 1 defective}) = 1 - P(G_1 \cap G_2 \cap G_3) = 1 - \frac{28}{57} = \frac{29}{57} \approx 0.5088$$

Final Answer: **a) 28/57 (0.4912)**, **b) 29/57 (0.5088)**

---

#### Exercise 9: Sequential Urn Ball Selection
**Problem:** Urn A contains 3 red and 2 white balls. Urn B contains 2 red and 4 white balls. A ball is drawn at random from Urn A and transferred into Urn B. Then a ball is drawn from Urn B.
**a)** Find the probability that the transferred ball was Red AND the ball drawn from Urn B is Red.
**b)** Find the probability that the transferred ball was White AND the ball drawn from Urn B is Red.

**Solution:**
**Step 1:** Transferred ball events from Urn A: $P(R_A) = 3/5$, $P(W_A) = 2/5$.

**Step 2:** For part **a)**: If $R_A$ is transferred, Urn B now has $2 + 1 = 3$ red and 4 white ($3 + 4 = 7$ total).
$$P(R_B \mid R_A) = \frac{3}{7}$$
$$P(R_A \cap R_B) = P(R_A) \cdot P(R_B \mid R_A) = \left( \frac{3}{5} \right) \cdot \left( \frac{3}{7} \right) = \frac{9}{35} \approx 0.2571$$

**Step 3:** For part **b)**: If $W_A$ is transferred, Urn B now has 2 red and $4 + 1 = 5$ white ($2 + 5 = 7$ total).
$$P(R_B \mid W_A) = \frac{2}{7}$$
$$P(W_A \cap R_B) = P(W_A) \cdot P(R_B \mid W_A) = \left( \frac{2}{5} \right) \cdot \left( \frac{2}{7} \right) = \frac{4}{35} \approx 0.1143$$

Final Answer: **a) 9/35 (0.2571)**, **b) 4/35 (0.1143)**

---

#### Exercise 10: Multi-Hop Network Routing Success (Time-Domain)
**Problem:** A network packet must traverse 3 sequential router hops ($H_1, H_2, H_3$). Hop survival probabilities under load are:
- $P(H_1 \text{ success}) = 0.98$
- $P(H_2 \text{ success} \mid H_1 \text{ success}) = 0.95$
- $P(H_3 \text{ success} \mid H_1 \cap H_2 \text{ success}) = 0.90$
**a)** Calculate the overall end-to-end packet delivery success probability.
**b)** What is the probability that the packet fails at Hop 3, given it successfully cleared Hop 1 and Hop 2?

**Solution:**
**a)** Apply the multiplication chain rule:
$$P(H_1 \cap H_2 \cap H_3) = P(H_1) \cdot P(H_2 \mid H_1) \cdot P(H_3 \mid H_1 \cap H_2) = 0.98 \cdot 0.95 \cdot 0.90 = 0.8379$$

**b)** Using the conditional complement rule:
$$P(H_3^c \mid H_1 \cap H_2) = 1 - P(H_3 \mid H_1 \cap H_2) = 1 - 0.90 = 0.1000$$

Final Answer: **a) 0.8379 (83.79%)**, **b) 0.1000 (10.00%)**

---

#### Exercise 11: Microservice Authentication and Data Fetch Pipeline (Time-Domain)
**Problem:** An API request passes through three sequential microservices: Auth Gateway ($A$), Data Fetch ($D$), and Output Formatter ($F$). Time budget allocations are $t_A = 20\,[ms], t_D = 100\,[ms], t_F = 30\,[ms]$.
From logs:
- $P(T_A \le 20) = 0.96$
- $P(T_D \le 100 \mid T_A \le 20) = 0.92$
- $P(T_F \le 30 \mid T_A \le 20 \cap T_D \le 100) = 0.95$
**a)** Calculate the overall pipeline success probability.
**b)** Write an R command that computes cumulative path probabilities using `cumprod()`.

**Solution:**
**Step 1:** Apply chain rule:
$$P(\text{Success}) = 0.96 \cdot 0.92 \cdot 0.95 = 0.83884 \approx 0.8388$$

**Step 2:** R code implementation:
```r
# R snippet for cumulative pipeline probability
stage_probs <- c(A = 0.96, D = 0.92, F = 0.95)
cum_success <- cumprod(stage_probs)
cat("Final Pipeline Probability:", cum_success["F"], "\n")
```

Final Answer: **a) 0.8388 (83.88%)**, **b) R command provided above**

---

#### Exercise 12: CI/CD Deployment Pipeline Execution (Time-Domain)
**Problem:** A DevOps deployment pipeline consists of 4 stages: Lint ($L$), Unit Test ($U$), Integration Test ($I$), and Deployment ($D$). The stage completion probabilities are:
- $P(L) = 0.99$
- $P(U \mid L) = 0.90$
- $P(I \mid L \cap U) = 0.85$
- $P(D \mid L \cap U \cap I) = 0.98$
**a)** Find the probability that the entire pipeline completes successfully.
**b)** If 500 independent build triggers occur, expected number of fully successful deployments?

**Solution:**
**a)** Apply the chain rule:
$$P(\text{Pipeline Success}) = 0.99 \cdot 0.90 \cdot 0.85 \cdot 0.98 = 0.7421547 \approx 0.7422$$

**b)** Expected successful deployments:
$$E[X] = N \cdot P(\text{Success}) = 500 \cdot 0.7421547 = 371.077 \approx 371 \text{ deployments}$$

Final Answer: **a) 0.7422 (74.22%)**, **b) 371 deployments**

---

### R Implementation

```r
# R Implementation for Section 3.2: Multiplication Rule & Sequential Chains

# 1. Chain Rule Cumulative Calculation (Pipeline Stages)
stage_conditional_probs <- c(
  Auth = 0.96,
  DataFetch = 0.92,
  Format = 0.95,
  Deploy = 0.98
)

# Compute cumulative success probability at each stage
cum_probs <- cumprod(stage_conditional_probs)
print(data.frame(Stage = names(cum_probs), CumProbability = cum_probs))

# 2. Simulating Sequential Sampling Without Replacement
simulate_draws <- function(red = 7, blue = 5, n_draws = 2) {
  urn <- c(rep("Red", red), rep("Blue", blue))
  draws <- sample(urn, size = n_draws, replace = FALSE)
  return(draws[1] == "Red" && draws[2] == "Blue")
}

set.seed(42)
sim_results <- replicate(100000, simulate_draws())
cat("Simulated P(Red1 & Blue2):", mean(sim_results), "\n")
```

---

## Section 3.3: Independence & System Reliability

### Core Theory & Definitions

Two events $A$ and $B$ are **statistically independent** if the occurrence of $B$ does not alter the probability of $A$ occurring. Knowledge of $B$ conveys zero information about $A$.

#### Pairwise vs Mutual (Joint) Independence
For three or more events $A_1, A_2, \dots, A_n$:
- **Pairwise Independence:** $P(A_i \cap A_j) = P(A_i) \cdot P(A_j)$ for all $i \neq j$.
- **Mutual (Joint) Independence:** $P(\bigcap_{i \in S} A_i) = \prod_{i \in S} P(A_i)$ for **every** subset $S \subseteq \{1, 2, \dots, n\}$.

> **Crucial Warning:** Pairwise independence does **NOT** imply mutual independence! (Bernstein's classic counterexample demonstrates 3 events that are pairwise independent but not mutually independent).

#### Mutually Exclusive vs Independent Events
- **Mutually Exclusive (Disjoint):** $A \cap B = \emptyset \implies P(A \cap B) = 0$. If $A$ happens, $B$ cannot happen.
- **Independent:** $P(A \cap B) = P(A) \cdot P(B)$.
- **Theorem:** If $P(A) > 0$ and $P(B) > 0$, mutually exclusive events can **NEVER** be independent. Since $P(A \cap B) = 0 \neq P(A)P(B) > 0$, mutual exclusivity implies maximum dependency.

```
Mutually Exclusive:            Independent:
+-------+ +-------+           +---------------+
|   A   | |   B   |           |  A  |A∩B|  B  |
+-------+ +-------+           +---------------+
 P(A ∩ B) = 0                  P(A ∩ B) = P(A)P(B)
```

#### System Reliability Architecture over Time
In engineering systems, reliability is modeled by treating individual component lifetimes $T_1, T_2, \dots, T_n$ as independent random variables:

1. **Series System (Logical AND - Weakest Link):**
   The system functions if and only if **all** $n$ components function.
   $$T_{\text{sys}} = \min(T_1, T_2, \dots, T_n)$$
   $$R_{\text{sys}}(t) = P(T_{\text{sys}} > t) = P(T_1 > t \cap T_2 > t \cap \dots \cap T_n > t) = \prod_{i=1}^{n} P(T_i > t)$$

2. **Parallel System (Logical OR - Redundant Architecture):**
   The system functions if **at least one** component functions. It fails only when all components fail.
   $$T_{\text{sys}} = \max(T_1, T_2, \dots, T_n)$$
   $$F_{\text{sys}}(t) = P(T_{\text{sys}} \le t) = \prod_{i=1}^{n} P(T_i \le t) \implies R_{\text{sys}}(t) = 1 - \prod_{i=1}^{n} \left(1 - P(T_i > t)\right)$$

---

### Mathematical Formulas & Derivations

#### Independence Conditions
Events $A$ and $B$ are independent if and only if any of the following equivalent statements hold:
1. $P(A \cap B) = P(A) \cdot P(B)$
2. $P(A \mid B) = P(A)$ (assuming $P(B) > 0$)
3. $P(B \mid A) = P(B)$ (assuming $P(A) > 0$)

#### Independence of Complemented Events
*Theorem:* If $A$ and $B$ are independent, then $A^c$ and $B^c$ are also independent.
*Proof:*
$$P(A^c \cap B^c) = P((A \cup B)^c) = 1 - P(A \cup B)$$
$$= 1 - [P(A) + P(B) - P(A \cap B)]$$
$$= 1 - P(A) - P(B) + P(A)P(B) = (1 - P(A))(1 - P(B)) = P(A^c) \cdot P(B^c)$$

#### Series and Parallel Reliability Formulas
- **Series Reliability:** $R_{\text{series}}(t) = \prod_{i=1}^{n} R_i(t)$
- **Parallel Reliability:** $R_{\text{parallel}}(t) = 1 - \prod_{i=1}^{n} (1 - R_i(t))$
- **$k$-out-of-$n$ System Reliability (Identical $R_i(t) = R(t)$):**
  $$R_{k:n}(t) = \sum_{j=k}^{n} \binom{n}{j} [R(t)]^j [1 - R(t)]^{n-j}$$

> **Practical / Time-Domain Note:**
> In distributed infrastructure, timers or worker processes running on separate virtual machines may appear independent, but if they share underlying physical CPU cores, hypervisors, or power units, a resource spike violates independence. Always audit for **shared infrastructure contention**.

---

### Worked Exercises

#### Exercise 13: Testing Independence from Survey Data
**Problem:** A survey of 1,000 users categorizes them by Device ($M = \text{Mobile}$, $D = \text{Desktop}$) and Subscription ($S = \text{Subscribed}$, $U = \text{Unsubscribed}$).
Data: 600 Mobile users, 400 Subscribed users, and 240 users who are both Mobile and Subscribed.
**a)** Are Device type ($M$) and Subscription status ($S$) independent?
**b)** Calculate $P(S \mid M)$ and compare it with $P(S)$.

**Solution:**
**Step 1:** Compute marginal probabilities:
$$P(M) = \frac{600}{1000} = 0.60, \quad P(S) = \frac{400}{1000} = 0.40$$
$$P(M \cap S) = \frac{240}{1000} = 0.24$$

**Step 2:** Test product rule for independence:
$$P(M) \cdot P(S) = 0.60 \cdot 0.40 = 0.24$$
Since $P(M \cap S) = P(M) \cdot P(S) = 0.24$, events $M$ and $S$ are **statistically independent**.

**Step 3:** Compute $P(S \mid M)$:
$$P(S \mid M) = \frac{P(M \cap S)}{P(M)} = \frac{0.24}{0.60} = 0.40 = P(S)$$

Final Answer: **a) Yes, independent ($P(M \cap S) = P(M)P(S) = 0.24$)**, **b) $P(S \mid M) = P(S) = 0.40$**

---

#### Exercise 14: Independence vs Disjointness in Dice Outcomes
**Problem:** A fair 6-sided die is rolled. Define events:
- $A = \{1, 2\}$ (Roll is 1 or 2)
- $B = \{2, 4, 6\}$ (Roll is even)
- $C = \{3, 5\}$ (Roll is 3 or 5)
**a)** Are $A$ and $B$ independent? Are they disjoint?
**b)** Are $A$ and $C$ independent? Are they disjoint?

**Solution:**
Sample space $\Omega = \{1, 2, 3, 4, 5, 6\}$, so $P(\text{each outcome}) = 1/6$.
$P(A) = 2/6 = 1/3$, $P(B) = 3/6 = 1/2$, $P(C) = 2/6 = 1/3$.

**a)** $A \cap B = \{2\} \implies P(A \cap B) = 1/6$.
Product test: $P(A) \cdot P(B) = (1/3) \cdot (1/2) = 1/6$.
Since $P(A \cap B) = P(A)P(B)$, $A$ and $B$ are **independent**.
Since $A \cap B \neq \emptyset$, they are **not disjoint**.

**b)** $A \cap C = \emptyset \implies P(A \cap C) = 0$.
Since $A \cap C = \emptyset$, $A$ and $C$ are **disjoint (mutually exclusive)**.
Product test: $P(A) \cdot P(C) = (1/3) \cdot (1/3) = 1/9 \neq 0$.
Since $P(A \cap C) \neq P(A)P(C)$, $A$ and $C$ are **not independent**.

Final Answer: **a) Independent, Not Disjoint**, **b) Disjoint, Not Independent**

---

#### Exercise 15: Probability of At Least One Success in Independent Trials
**Problem:** The probability of a network transmission error in any given $1\,[min]$ interval is $p = 0.05$. Assuming independent intervals:
**a)** What is the probability of experiencing at least one error across 10 consecutive minutes?
**b)** What R command computes this probability?

**Solution:**
**Step 1:** Probability of NO error in 1 minute = $1 - p = 0.95$.
**Step 2:** By independence, probability of NO errors in 10 minutes:
$$P(\text{No Errors in 10 min}) = (0.95)^{10} \approx 0.5987$$
**Step 3:** Use complement rule for "at least one":
$$P(\text{At Least 1 Error}) = 1 - (0.95)^{10} = 1 - 0.59874 = 0.40126 \approx 0.4013$$

**Step 4:** R command:
```r
p_at_least_1 <- 1 - pbinom(0, size = 10, prob = 0.05) # or 1 - (0.95)^10
```

Final Answer: **a) 0.4013 (40.13%)**, **b) `1 - (0.95)^10` or `1 - pbinom(0, 10, 0.05)`**

---

#### Exercise 16: Redundant Parallel Database Cluster Reliability (Time-Domain)
**Problem:** A critical cloud storage layer uses 3 independent redundant database nodes in parallel. Each node has a 24-hour survival probability of $R_i(24\,[hr]) = 0.90$.
**a)** Calculate the overall 24-hour reliability of the parallel database cluster.
**b)** If the nodes were configured in series (all 3 required), what would be the 24-hour system reliability?

**Solution:**
**a) Parallel Architecture:**
Failure probability of each node: $F_i = 1 - 0.90 = 0.10$.
Cluster fails iff all 3 nodes fail:
$$F_{\text{cluster}} = (0.10)^3 = 0.0010$$
$$R_{\text{parallel}}(24\,[hr]) = 1 - F_{\text{cluster}} = 1 - 0.0010 = 0.9990 \text{ (99.90\%)}$$

**b) Series Architecture:**
$$R_{\text{series}}(24\,[hr]) = (0.90)^3 = 0.7290 \text{ (72.90\%)}$$

Final Answer: **a) 0.9990 (99.90%)**, **b) 0.7290 (72.90%)**

---

#### Exercise 17: Series Pipeline Hardware Latency & Clock Skew (Time-Domain)
**Problem:** A digital clock distribution path has 4 sequential flip-flop stages in series. Stage survival within clock-to-Q timing window $T_{\text{clk}\to q} = 500\,[ps]$ are independent with $R_1 = 0.995, R_2 = 0.990, R_3 = 0.992, R_4 = 0.998$.
**a)** Compute the end-to-end timing reliability $R_{\text{path}}$.
**b)** If clock skew introduces coupling between stages 2 and 3 such that $P(\text{Stage 3 holds} \mid \text{Stage 2 holds}) = 0.980$ (instead of 0.992), calculate the revised path reliability.

**Solution:**
**a) Independent Series Path:**
$$R_{\text{path}} = R_1 \cdot R_2 \cdot R_3 \cdot R_4 = 0.995 \cdot 0.990 \cdot 0.992 \cdot 0.998 = 0.97517 \approx 0.9752$$

**b) Coupled Path (Dependent Stages 2 & 3):**
$$R_{\text{revised}} = R_1 \cdot R_2 \cdot P(\text{Stage 3} \mid \text{Stage 2}) \cdot R_4 = 0.995 \cdot 0.990 \cdot 0.980 \cdot 0.998 = 0.96336 \approx 0.9634$$

Final Answer: **a) 0.9752 (97.52%)**, **b) 0.9634 (96.34%)**

---

#### Exercise 18: Autocorrelation & Independence Test of Time Spikes (Time-Domain)
**Problem:** Latency logs record execution spike events ($E_t = 1$ if latency $> 200\,[ms]$, else $0$) across consecutive minutes. Out of 1,000 minutes:
- $E_t = 1$ occurred in 100 minutes ($P(E_t) = 0.10$).
- $E_{t+1} = 1$ given $E_t = 1$ occurred in 35 minutes.
**a)** Compute $P(E_t \cap E_{t+1})$ and test if consecutive latency spikes are independent.
**b)** Write an R snippet using `cor.test()` to test for serial correlation.

**Solution:**
**Step 1:** Compute joint probability:
$$P(E_t \cap E_{t+1}) = P(E_t) \cdot P(E_{t+1} \mid E_t) = 0.10 \cdot \frac{35}{100} = 0.0350$$

**Step 2:** Independence test:
If independent, $P(E_t) \cdot P(E_{t+1}) = 0.10 \cdot 0.10 = 0.0100$.
Since $P(E_t \cap E_{t+1}) = 0.0350 \neq 0.0100$, consecutive latency spikes are **strongly dependent (autocorrelated)**.

**Step 3:** R code:
```r
# R snippet testing autocorrelation between lag-1 spike vectors
spikes_t   <- spike_vec[-length(spike_vec)]
spikes_t1  <- spike_vec[-1]
test_res   <- cor.test(spikes_t, spikes_t1)
print(test_res$p.value)
```

Final Answer: **a) $P(E_t \cap E_{t+1}) = 0.0350 \neq 0.0100 \implies$ Dependent (Autocorrelated)**, **b) R code provided above**

---

### R Implementation

```r
# R Implementation for Section 3.3: Independence & System Reliability

# 1. Contingency Independence Test (Chi-Square Test)
observed <- matrix(c(240, 360, 160, 240), nrow = 2, byrow = TRUE,
                   dimnames = list(Device = c("Mobile", "Desktop"), Sub = c("Yes", "No")))
chi_test <- chisq.test(observed, correct = FALSE)
cat("Chi-Square Statistic:", chi_test$statistic, "P-Value:", chi_test$p.value, "\n")

# 2. System Reliability Simulation (Series vs Parallel)
n_sim <- 100000
t_comp1 <- rexp(n_sim, rate = 0.05) # Lifetime component 1
t_comp2 <- rexp(n_sim, rate = 0.05) # Lifetime component 2
t_comp3 <- rexp(n_sim, rate = 0.05) # Lifetime component 3

target_t <- 10 # 10 hours

# Series: min(T1, T2, T3) > 10
r_series_sim <- mean(pmin(t_comp1, t_comp2, t_comp3) > target_t)

# Parallel: max(T1, T2, T3) > 10
r_parallel_sim <- mean(pmax(t_comp1, t_comp2, t_comp3) > target_t)

cat("Simulated Series Reliability:", r_series_sim, "\n")
cat("Simulated Parallel Reliability:", r_parallel_sim, "\n")
```

---

## Section 3.4: Law of Total Probability & Bayes' Theorem

### Core Theory & Definitions

#### Partition of a Sample Space
A collection of events $\{B_1, B_2, \dots, B_n\}$ forms a **partition** of the sample space $\Omega$ if:
1. The events are mutually exclusive: $B_i \cap B_j = \emptyset$ for all $i \neq j$.
2. The events are collectively exhaustive: $\bigcup_{i=1}^{n} B_i = \Omega$.
3. $P(B_i) > 0$ for all $i = 1, \dots, n$.

```
Partition of Ω into B_1, B_2, B_3, B_4:
+------------------------------------+
|  B_1   |   B_2   |   B_3  |  B_4   |
|     +--+---------+--------+--+     |
|     |         Event A        |     |
|     +--+---------+--------+--+     |
+------------------------------------+
  Event A is composed of slices (A ∩ B_i) across each partition block.
```

#### Law of Total Probability
The Law of Total Probability calculates the unconditional probability $P(A)$ of an event $A$ by summing its conditional probabilities across all partition components $B_i$, weighted by the prior probability of each component:
$$P(A) = \sum_{i=1}^{n} P(A \cap B_i) = \sum_{i=1}^{n} P(A \mid B_i) P(B_i)$$

#### Bayes' Theorem
Bayes' Theorem provides the mathematical framework for **updating probabilities in light of new evidence**. It converts a **prior probability** $P(B_k)$ (our baseline belief before observing evidence) into a **posterior probability** $P(B_k \mid A)$ (our updated belief after observing evidence $A$).

The four key components of Bayes' Theorem are:
1. **Prior Probability $P(B_k)$:** Baseline probability of hypothesis $B_k$.
2. **Likelihood $P(A \mid B_k)$:** Probability of observing evidence $A$ given hypothesis $B_k$.
3. **Marginal Likelihood $P(A)$:** Overall probability of observing evidence $A$ across all hypotheses (computed via Law of Total Probability).
4. **Posterior Probability $P(B_k \mid A)$:** Updated probability of hypothesis $B_k$ given evidence $A$.

#### Time-Domain Application: Anomaly Isolation & Root-Cause Diagnosis
In system reliability and time-series monitoring, Bayes' Theorem isolates root causes of performance degradations. For example, if a high latency spike ($A$) is detected, Bayes' Theorem computes the posterior probability $P(B_k \mid A)$ that the root cause was a Database Lock ($B_1$), Network Congestion ($B_2$), or Garbage Collection Pause ($B_3$).

---

### Mathematical Formulas & Derivations

#### Law of Total Probability Formula
$$P(A) = P(A \mid B_1)P(B_1) + P(A \mid B_2)P(B_2) + \dots + P(A \mid B_n)P(B_n) = \sum_{i=1}^{n} P(A \mid B_i)P(B_i)$$

#### Bayes' Theorem Formula (General Partition Form)
For a partition $\{B_1, B_2, \dots, B_n\}$ and an observed event $A$ with $P(A) > 0$:
$$P(B_k \mid A) = \frac{P(A \cap B_k)}{P(A)} = \frac{P(A \mid B_k) P(B_k)}{\sum_{j=1}^{n} P(A \mid B_j) P(B_j)}$$

#### Binary Diagnostic / Screening Bayes Formula
In medical screening or binary signal detection:
- **Prevalence (Base Rate):** $p = P(D)$
- **Sensitivity (True Positive Rate):** $\text{Sens} = P(Pos \mid D)$
- **Specificity (True Negative Rate):** $\text{Spec} = P(Neg \mid D^c) \implies P(Pos \mid D^c) = 1 - \text{Spec}$

$$P(D \mid Pos) = \frac{\text{Sens} \cdot p}{\text{Sens} \cdot p + (1 - \text{Spec}) \cdot (1 - p)}$$

> **Practical / Time-Domain Note:**
> The **Base Rate Fallacy** occurs when an analyst ignores low prior probabilities $P(B_k)$. Even if a diagnostic test or anomaly alert has 99% accuracy ($P(A \mid B_k) = 0.99$), if the event $B_k$ is extremely rare ($P(B_k) = 0.001$), the majority of alerts will be false positives. Always evaluate the marginal denominator $P(A)$ explicitly.

---

### Worked Exercises

#### Exercise 19: Three-Factory Defect Analysis (Classic Partition Bayes)
**Problem:** A company buys components from 3 suppliers: Factory 1 ($B_1$, 50% of supply), Factory 2 ($B_2$, 30%), and Factory 3 ($B_3$, 20%). Defect rates are 1% for $B_1$, 2% for $B_2$, and 5% for $B_3$.
**a)** Calculate the overall defect rate $P(D)$ across all incoming inventory.
**b)** If a randomly inspected component is defective ($D$), what is the posterior probability that it originated from Factory 3 ($B_3$)?

**Solution:**
**Step 1:** Identify priors and likelihoods:
Priors: $P(B_1) = 0.50$, $P(B_2) = 0.30$, $P(B_3) = 0.20$.
Likelihoods: $P(D \mid B_1) = 0.01$, $P(D \mid B_2) = 0.02$, $P(D \mid B_3) = 0.05$.

**Step 2:** For part **a)**, apply the Law of Total Probability:
$$P(D) = P(D \mid B_1)P(B_1) + P(D \mid B_2)P(B_2) + P(D \mid B_3)P(B_3)$$
$$P(D) = (0.01 \cdot 0.50) + (0.02 \cdot 0.30) + (0.05 \cdot 0.20) = 0.005 + 0.006 + 0.010 = 0.0210 \text{ (2.10\%)}$$

**Step 3:** For part **b)**, apply Bayes' Theorem for $B_3$:
$$P(B_3 \mid D) = \frac{P(D \mid B_3)P(B_3)}{P(D)} = \frac{0.05 \cdot 0.20}{0.0210} = \frac{0.0100}{0.0210} = \frac{10}{21} \approx 0.4762$$

Final Answer: **a) 0.0210 (2.10%)**, **b) 10/21 (0.4762)**

---

#### Exercise 20: Medical Disease Screening Sensitivity/Specificity (Bayes Base-Rate)
**Problem:** A rare disease affects 0.2% of the population ($P(D) = 0.002$). A diagnostic test has 98% sensitivity ($P(Pos \mid D) = 0.98$) and 95% specificity ($P(Neg \mid D^c) = 0.95$).
**a)** Find the total probability that a randomly selected person tests positive ($P(Pos)$).
**b)** If a patient tests positive, what is the posterior probability that they actually have the disease ($P(D \mid Pos)$)?

**Solution:**
**Step 1:** Identify parameters:
$P(D) = 0.002 \implies P(D^c) = 0.998$.
$P(Pos \mid D) = 0.98$.
$P(Pos \mid D^c) = 1 - P(Neg \mid D^c) = 1 - 0.95 = 0.05$.

**Step 2:** For part **a)**, calculate $P(Pos)$ using Law of Total Probability:
$$P(Pos) = P(Pos \mid D)P(D) + P(Pos \mid D^c)P(D^c)$$
$$P(Pos) = (0.98 \cdot 0.002) + (0.05 \cdot 0.998) = 0.00196 + 0.04990 = 0.05186 \approx 0.0519$$

**Step 3:** For part **b)**, apply Bayes' Theorem:
$$P(D \mid Pos) = \frac{P(Pos \mid D)P(D)}{P(Pos)} = \frac{0.00196}{0.05186} \approx 0.03779 \approx 0.0378$$

> **Note:** Despite 98% test sensitivity, a positive result only carries a 3.78% probability of true disease due to the low base rate (0.2%).

Final Answer: **a) 0.0519 (5.19%)**, **b) 0.0378 (3.78%)**

---

#### Exercise 21: Binary Symmetric Channel Transmission Error
**Problem:** A binary communication channel transmits bits $X \in \{0, 1\}$ with prior probabilities $P(X=0) = 0.60$ and $P(X=1) = 0.40$. Due to noise, bit inversion error probability is $p_e = 0.05$ (i.e., $P(Y=1 \mid X=0) = 0.05$ and $P(Y=0 \mid X=1) = 0.05$).
**a)** Calculate the overall probability that bit $Y=1$ is received.
**b)** Given that $Y=1$ was received, what is the posterior probability that $X=1$ was transmitted?

**Solution:**
**Step 1:** Likelihoods:
$P(Y=1 \mid X=1) = 0.95$, $P(Y=1 \mid X=0) = 0.05$.

**Step 2:** For part **a)**, apply Law of Total Probability:
$$P(Y=1) = P(Y=1 \mid X=1)P(X=1) + P(Y=1 \mid X=0)P(X=0)$$
$$P(Y=1) = (0.95 \cdot 0.40) + (0.05 \cdot 0.60) = 0.380 + 0.030 = 0.4100$$

**Step 3:** For part **b)**, apply Bayes' Theorem:
$$P(X=1 \mid Y=1) = \frac{P(Y=1 \mid X=1)P(X=1)}{P(Y=1)} = \frac{0.380}{0.410} = \frac{38}{41} \approx 0.9268$$

Final Answer: **a) 0.4100 (41.00%)**, **b) 38/41 (0.9268)**

---

#### Exercise 22: Server Load Regime Isolation from Query Latency Spike (Time-Domain)
**Problem:** A web server operates under 3 load regimes: Off-Peak ($B_1$, 50% of time), Normal ($B_2$, 40%), and Peak ($B_3$, 10%). The probability of a query latency spike ($S$, latency $> 500\,[ms]$) under each regime is:
$P(S \mid B_1) = 0.01$, $P(S \mid B_2) = 0.05$, $P(S \mid B_3) = 0.40$.
**a)** Compute the total probability $P(S)$ of observing a query latency spike.
**b)** If a monitoring alert detects a latency spike ($S$), what is the posterior probability that the server is in Peak load regime ($B_3$)?

**Solution:**
**Step 1:** Priors: $P(B_1) = 0.50$, $P(B_2) = 0.40$, $P(B_3) = 0.10$.

**Step 2:** For part **a)**:
$$P(S) = (0.01 \cdot 0.50) + (0.05 \cdot 0.40) + (0.40 \cdot 0.10) = 0.005 + 0.020 + 0.040 = 0.0650 \text{ (6.50\%)}$$

**Step 3:** For part **b)**:
$$P(B_3 \mid S) = \frac{P(S \mid B_3)P(B_3)}{P(S)} = \frac{0.040}{0.0650} = \frac{40}{65} = \frac{8}{13} \approx 0.6154$$

Final Answer: **a) 0.0650 (6.50%)**, **b) 8/13 (0.6154)**

---

#### Exercise 23: Timestamp-Based Anomaly Filter Classification (Time-Domain)
**Problem:** An automated network filter classifies packet arrivals as Normal ($N$, 95%) or Malicious ($M$, 5%). The filter flags an anomaly alert ($A$) based on timestamp jitter metrics. Likelihoods are $P(A \mid M) = 0.90$ and $P(A \mid N) = 0.02$.
**a)** Compute $P(A)$ (total probability of an alert).
**b)** Compute $P(M \mid A)$ (probability a flagged packet is actually malicious).

**Solution:**
**a)** Apply Law of Total Probability:
$$P(A) = P(A \mid M)P(M) + P(A \mid N)P(N) = (0.90 \cdot 0.05) + (0.02 \cdot 0.95) = 0.045 + 0.019 = 0.0640$$

**b)** Apply Bayes' Theorem:
$$P(M \mid A) = \frac{P(A \mid M)P(M)}{P(A)} = \frac{0.045}{0.0640} = \frac{45}{64} \approx 0.7031$$

Final Answer: **a) 0.0640 (6.40%)**, **b) 45/64 (0.7031)**

---

#### Exercise 24: Software Failure Root-Cause Diagnosis (Time-Domain)
**Problem:** Software execution crashes ($C$) are caused by 3 bug categories: Memory Leak ($B_1$, prior 40%), Null Pointer ($B_2$, prior 35%), and Deadlock ($B_3$, prior 25%).
Probability of execution crash taking $> 10\,[s]$ before failure:
$P(> 10\,[s] \mid B_1) = 0.80$, $P(> 10\,[s] \mid B_2) = 0.10$, $P(> 10\,[s] \mid B_3) = 0.60$.
**a)** Compute total probability $P(> 10\,[s])$.
**b)** Given a crash took $> 10\,[s]$, find posterior probability $P(B_1 \mid > 10\,[s])$.

**Solution:**
**a)** $P(> 10\,[s]) = (0.80 \cdot 0.40) + (0.10 \cdot 0.35) + (0.60 \cdot 0.25) = 0.320 + 0.035 + 0.150 = 0.5050$.

**b)** $P(B_1 \mid > 10\,[s]) = \frac{0.320}{0.5050} = \frac{320}{505} = \frac{64}{101} \approx 0.6337$.

Final Answer: **a) 0.5050 (50.50%)**, **b) 64/101 (0.6337)**

---

#### Exercise 25: Cloud Instance Reboot Mode Posterior Update (Time-Domain)
**Problem:** Server reboots occur due to Hardware Fault ($H$, 10%), OS Kernel Panic ($K$, 30%), or Scheduled Maintenance ($M$, 60%). The reboot duration exceeds $5\,[min]$ ($D > 5$) with probabilities:
$P(D > 5 \mid H) = 0.90$, $P(D > 5 \mid K) = 0.50$, $P(D > 5 \mid M) = 0.05$.
**a)** Compute total probability $P(D > 5)$.
**b)** Given reboot took $> 5\,[min]$, calculate posteriors for all 3 causes.

**Solution:**
**a)** $P(D > 5) = (0.90 \cdot 0.10) + (0.50 \cdot 0.30) + (0.05 \cdot 0.60) = 0.090 + 0.150 + 0.030 = 0.2700$.

**b)** Posteriors:
$$P(H \mid D > 5) = \frac{0.090}{0.2700} = \frac{1}{3} \approx 0.3333$$
$$P(K \mid D > 5) = \frac{0.150}{0.2700} = \frac{5}{9} \approx 0.5556$$
$$P(M \mid D > 5) = \frac{0.030}{0.2700} = \frac{1}{9} \approx 0.1111$$

Final Answer: **a) 0.2700 (27.00%)**, **b) P(H|D>5) = 0.3333, P(K|D>5) = 0.5556, P(M|D>5) = 0.1111**

---

#### Exercise 26: R Function for Iterative Bayesian Log Updating (Time-Domain)
**Problem:** Write a generic R function `bayes_update(priors, likelihoods)` that accepts a vector of prior probabilities and a vector of likelihoods, computes the total evidence probability, and returns the posterior probability vector.

**Solution:**
```r
# Generic R Function for Bayes Updating
bayes_update <- function(priors, likelihoods) {
  stopifnot(length(priors) == length(likelihoods))
  stopifnot(abs(sum(priors) - 1) < 1e-6)
  
  joint_probs <- priors * likelihoods
  total_evidence <- sum(joint_probs)
  posteriors <- joint_probs / total_evidence
  
  return(list(
    total_evidence = total_evidence,
    posteriors = posteriors
  ))
}

# Example Test Case (Exercise 22 Verification)
priors <- c(B1 = 0.50, B2 = 0.40, B3 = 0.10)
like   <- c(B1 = 0.01, B2 = 0.05, B3 = 0.40)
res    <- bayes_update(priors, like)
cat("Total Evidence P(S):", res$total_evidence, "\n")
print(res$posteriors)
```

Final Answer: **R function provided above**

---

### R Implementation

```r
# R Implementation for Section 3.4: Law of Total Probability & Bayes' Theorem

# 1. Automated Bayes Update Function
bayes_update <- function(priors, likelihoods) {
  joint_probs <- priors * likelihoods
  p_evidence <- sum(joint_probs)
  posteriors <- joint_probs / p_evidence
  return(list(evidence_prob = p_evidence, posteriors = posteriors))
}

# 2. Applying Bayes Update to Medical Screening (Exercise 20)
priors_med <- c(Disease = 0.002, Healthy = 0.998)
like_med   <- c(Disease = 0.98, Healthy = 0.05) # Sens = 0.98, 1 - Spec = 0.05

med_result <- bayes_update(priors_med, like_med)
cat("Total P(Positive Test):", round(med_result$evidence_prob, 5), "\n")
cat("Posterior P(Disease | Positive):", round(med_result$posteriors["Disease"], 4), "\n")
```

---

## Combined Exercises (Exercises 27 - 30)

#### Exercise 27: Multi-Stage Manufacturing Defect & Warranty Claim Pipeline (Combined, Moderate)
**Problem:** An automated electronics assembly plant produces circuit boards using 3 production lines: Line A ($L_A$, 50% of output), Line B ($L_B$, 30%), and Line C ($L_C$, 20%).
During manufacturing, each board undergoes two sequential quality tests: Electrical Test ($T_1$) and Thermal Test ($T_2$).
From historical audit logs:
- Defect rate at $T_1$: $P(D_1 \mid L_A) = 0.02$, $P(D_1 \mid L_B) = 0.04$, $P(D_1 \mid L_C) = 0.05$.
- Defect rate at $T_2$ given it passed $T_1$: $P(D_2 \mid D_1^c \cap L_A) = 0.01$, $P(D_2 \mid D_1^c \cap L_B) = 0.02$, $P(D_2 \mid D_1^c \cap L_C) = 0.03$.

**a)** Compute the probability that a board from Line A passes both tests ($D_1^c \cap D_2^c$).
**b)** Compute the overall probability $P(\text{Pass Both})$ across all combined factory lines using the Law of Total Probability.
**c)** If a randomly selected board fails at least one test, what is the posterior probability that it was produced by Line C ($L_C$)?
**d)** Write an R snippet to verify these probabilities.

**Solution:**
**a)** For Line A:
$$P(D_1^c \mid L_A) = 1 - 0.02 = 0.98$$
$$P(D_2^c \mid D_1^c \cap L_A) = 1 - 0.01 = 0.99$$
By the multiplication rule:
$$P(\text{Pass Both} \mid L_A) = P(D_1^c \cap D_2^c \mid L_A) = 0.98 \cdot 0.99 = 0.9702 \text{ (97.02\%)}$$

**b)** Compute passing probabilities for Lines B and C:
- For Line B: $P(D_1^c \mid L_B) = 1 - 0.04 = 0.96$; $P(D_2^c \mid D_1^c \cap L_B) = 1 - 0.02 = 0.98$.
  $$P(\text{Pass Both} \mid L_B) = 0.96 \cdot 0.98 = 0.9408$$
- For Line C: $P(D_1^c \mid L_C) = 1 - 0.05 = 0.95$; $P(D_2^c \mid D_1^c \cap L_C) = 1 - 0.03 = 0.97$.
  $$P(\text{Pass Both} \mid L_C) = 0.95 \cdot 0.97 = 0.9215$$

Apply Law of Total Probability for overall passing rate:
$$P(\text{Pass Both}) = (0.9702 \cdot 0.50) + (0.9408 \cdot 0.30) + (0.9215 \cdot 0.20)$$
$$P(\text{Pass Both}) = 0.48510 + 0.28224 + 0.18430 = 0.95164 \approx 0.9516 \text{ (95.16\%)}$$

Overall failure probability $P(\text{Fail}) = 1 - 0.95164 = 0.04836 \approx 0.0484$.

**c)** Failure rate for Line C:
$$P(\text{Fail} \mid L_C) = 1 - P(\text{Pass Both} \mid L_C) = 1 - 0.9215 = 0.0785$$

Apply Bayes' Theorem for $P(L_C \mid \text{Fail})$:
$$P(L_C \mid \text{Fail}) = \frac{P(\text{Fail} \mid L_C) P(L_C)}{P(\text{Fail})} = \frac{0.0785 \cdot 0.20}{0.04836} = \frac{0.01570}{0.04836} \approx 0.3246 \text{ (32.46\%)}$$

**d)** R Code Verification:
```r
priors <- c(LA = 0.50, LB = 0.30, LC = 0.20)
pass_given_line <- c(LA = 0.98*0.99, LB = 0.96*0.98, LC = 0.95*0.97)
fail_given_line <- 1 - pass_given_line

p_pass_total <- sum(priors * pass_given_line)
p_fail_total <- sum(priors * fail_given_line)
post_LC_fail <- (fail_given_line["LC"] * priors["LC"]) / p_fail_total

cat("Total Pass Probability:", p_pass_total, "\n")
cat("Posterior P(LC | Fail):", post_LC_fail, "\n")
```

Final Answer: **a) 0.9702 (97.02%)**, **b) 0.9516 (95.16%)**, **c) 0.3246 (32.46%)**, **d) R code provided above**

---

#### Exercise 28: Microservice Architecture Reliability and Anomaly Bayes Root-Cause Analysis (Time-Domain) (Combined, Harder)
**Problem:** A cloud API backend processes user checkouts through a hybrid microservice topology:
- **Authentication:** Single Auth Gateway ($A$).
- **Processing Layer:** 2 independent parallel payment microservices ($P_1, P_2$).
- **Database Layer:** Single Primary Database ($DB$).

```
                +---> Payment P1 --->+
                |                    |
[Auth Gateway A]+                    +[Database DB]
                |                    |
                +---> Payment P2 --->+
```

The request succeeds if Auth ($A$) succeeds, AT LEAST ONE Payment service ($P_1$ or $P_2$) succeeds, AND Database ($DB$) succeeds.

From execution logs over a 30-day window ($t = 24\,[hr]$ period):
- $P(A \text{ succeeds}) = 0.99$.
- Individual payment service survival: $P(P_1 \text{ succeeds}) = 0.95$, $P(P_2 \text{ succeeds}) = 0.95$ (independent).
- $P(DB \text{ succeeds}) = 0.98$.
- Overall traffic load regimes: Low Load ($L_1$, 60% of time), High Load ($L_2$, 30%), Surge Load ($L_3$, 10%).
- Conditional probability of a checkout timeout ($T > 2\,[s]$) given load regime:
  $P(T > 2 \mid L_1) = 0.01$, $P(T > 2 \mid L_2) = 0.08$, $P(T > 2 \mid L_3) = 0.50$.

**a)** Calculate the reliability $R_{\text{pay}}$ of the parallel payment layer ($P_1 \parallel P_2$).
**b)** Calculate the end-to-end system reliability $R_{\text{sys}}$ of the entire checkout pipeline.
**c)** Compute the total probability $P(T > 2\,[s])$ of a checkout timeout across all load regimes.
**d)** If a monitoring agent fires a timeout alert ($T > 2\,[s]$), compute the posterior probability $P(L_3 \mid T > 2\,[s])$ that the system was in Surge Load regime.
**e)** Write an R script simulating this architecture and computing the posterior probabilities.

**Solution:**
**a)** Payment layer uses parallel redundancy.
Failure probability of single payment service: $F_P = 1 - 0.95 = 0.05$.
Both payment services fail iff $F_{\text{pay\_layer}} = (0.05)^2 = 0.0025$.
$$R_{\text{pay}} = 1 - 0.0025 = 0.9975 \text{ (99.75\%)}$$

**b)** End-to-end topology is in series across Auth ($A$), Payment Layer ($P_{\text{layer}}$), and Database ($DB$):
$$R_{\text{sys}} = P(A) \cdot R_{\text{pay}} \cdot P(DB) = 0.99 \cdot 0.9975 \cdot 0.98 = 0.9677745 \approx 0.9678 \text{ (96.78\%)}$$

**c)** Total probability of checkout timeout $P(T > 2\,[s])$ via Law of Total Probability:
$$P(T > 2) = P(T > 2 \mid L_1)P(L_1) + P(T > 2 \mid L_2)P(L_2) + P(T > 2 \mid L_3)P(L_3)$$
$$P(T > 2) = (0.01 \cdot 0.60) + (0.08 \cdot 0.30) + (0.50 \cdot 0.10) = 0.006 + 0.024 + 0.050 = 0.0800 \text{ (8.00\%)}$$

**d)** Apply Bayes' Theorem for Surge Load $L_3$:
$$P(L_3 \mid T > 2) = \frac{P(T > 2 \mid L_3)P(L_3)}{P(T > 2)} = \frac{0.050}{0.0800} = \frac{5}{8} = 0.6250 \text{ (62.50\%)}$$

**e)** R Verification Script:
```r
# Microservice Architecture Verification
p_A <- 0.99
p_P1 <- 0.95; p_P2 <- 0.95
p_DB <- 0.98

r_pay <- 1 - (1 - p_P1)*(1 - p_P2)
r_sys <- p_A * r_pay * p_DB

load_priors <- c(L1 = 0.60, L2 = 0.30, L3 = 0.10)
timeout_like <- c(L1 = 0.01, L2 = 0.08, L3 = 0.50)

p_timeout_total <- sum(load_priors * timeout_like)
post_L3 <- (timeout_like["L3"] * load_priors["L3"]) / p_timeout_total

cat("Payment Layer Reliability:", r_pay, "\n")
cat("End-to-End System Reliability:", r_sys, "\n")
cat("Total Timeout Probability:", p_timeout_total, "\n")
cat("Posterior P(L3 | Timeout):", post_L3, "\n")
```

Final Answer: **a) 0.9975 (99.75%)**, **b) 0.9678 (96.78%)**, **c) 0.0800 (8.00%)**, **d) 0.6250 (62.50%)**, **e) R script provided above**

---

#### Exercise 29: Telecommunications Channel Noise & Packet Delay Pipeline (Combined, Hard)
**Problem:** A digital communications link transmits data packets over a wireless channel.
The transmission involves two stochastic layers:
1. **Physical Transmission Noise (Binary Symmetric Channel):** Bit error rate $p_e = 0.02$. Prior probability of transmitting bit '1' is $P(X=1) = 0.70$, and bit '0' is $P(X=0) = 0.30$.
2. **Network Hop Latency Pipeline:** Packets pass through 3 sequential switches ($S_1, S_2, S_3$). Hop completion probabilities within frame time budget $t_{\text{frame}} = 10\,[ms]$ are:
   - $P(S_1 \le 10) = 0.95$
   - $P(S_2 \le 10 \mid S_1 \le 10) = 0.90$
   - $P(S_3 \le 10 \mid S_1 \le 10 \cap S_2 \le 10) = 0.85$

Furthermore, packet corruption ($C$) occurs independently of switch delays with probability $P(C) = 0.01$.

**a)** Calculate $P(Y=1)$, the total probability of receiving bit '1'.
**b)** Given that bit $Y=1$ was received, calculate the posterior probability $P(X=1 \mid Y=1)$.
**c)** Calculate the joint probability that a packet completes all 3 switch hops within time budget AND is NOT corrupted.
**d)** If 1,000 independent packets are sent, calculate the expected number of packets that arrive both on-time and uncorrupted.

**Solution:**
**a)** Physical channel likelihoods:
$P(Y=1 \mid X=1) = 1 - p_e = 0.98$.
$P(Y=1 \mid X=0) = p_e = 0.02$.

Apply Law of Total Probability for $P(Y=1)$:
$$P(Y=1) = P(Y=1 \mid X=1)P(X=1) + P(Y=1 \mid X=0)P(X=0)$$
$$P(Y=1) = (0.98 \cdot 0.70) + (0.02 \cdot 0.30) = 0.686 + 0.006 = 0.6920 \text{ (69.20\%)}$$

**b)** Apply Bayes' Theorem for $P(X=1 \mid Y=1)$:
$$P(X=1 \mid Y=1) = \frac{P(Y=1 \mid X=1)P(X=1)}{P(Y=1)} = \frac{0.686}{0.6920} = \frac{343}{346} \approx 0.99133 \approx 0.9913$$

**c)** Hop pipeline success probability via chain rule:
$$P(\text{On-Time}) = P(S_1 \le 10) \cdot P(S_2 \le 10 \mid S_1 \le 10) \cdot P(S_3 \le 10 \mid S_1 \cap S_2) = 0.95 \cdot 0.90 \cdot 0.85 = 0.72675$$

Since corruption $C$ is independent of delay:
$$P(\text{Uncorrupted}) = P(C^c) = 1 - 0.01 = 0.99$$
$$P(\text{On-Time} \cap \text{Uncorrupted}) = P(\text{On-Time}) \cdot P(C^c) = 0.72675 \cdot 0.99 = 0.7194825 \approx 0.7195$$

**d)** Expected successful packets out of $N = 1000$:
$$E[\text{Valid Packets}] = 1000 \cdot 0.7194825 = 719.48 \approx 719 \text{ packets}$$

Final Answer: **a) 0.6920 (69.20%)**, **b) 0.9913 (99.13%)**, **c) 0.7195 (71.95%)**, **d) 719 packets**

---

#### Exercise 30: High-Frequency Trading Latency, Redundant Watchdogs & Unit-Scaling Gotcha (Time-Domain) (Combined, Hardest + Gotcha)
**Problem:** A high-frequency trading (HFT) firm executes orders over an ultra-low-latency FPGA gateway.
1. **Engine Latency Distribution:** Order execution lifetime $T$ (in microseconds, $[\mu s]$) has survival function $S_T(t) = \frac{1}{1 + 0.02 t}$ for $t \ge 0$.
   - Evaluate $P(T > 100\,[\mu s] \mid T > 50\,[\mu s])$.
2. **Watchdog Timers:** Order execution is monitored by 2 independent redundant FPGA watchdog hardware timers ($W_1, W_2$). Each watchdog has a failure probability of $p_f = 0.02$ over a trading session.
   - Calculate the overall watchdog system reliability $R_{\text{watchdog}}$ (probability at least one watchdog functions).
3. **Market Regime Diagnosis:** Market volatility operates under 3 regimes: Calm ($M_1$, 70%), Volatile ($M_2$, 20%), Extreme ($M_3$, 10%).
   - Latency spike probabilities ($S = \{T > 100\,[\mu s]\}$):
     $P(S \mid M_1) = 0.01$, $P(S \mid M_2) = 0.15$, $P(S \mid M_3) = 0.80$.
   - Calculate $P(S)$ and posterior $P(M_3 \mid S)$.
4. **Unit-Conversion & Variance Scaling Gotcha:** The firm measures latency variance in seconds squared $[s^2]$ as $\text{Var}(T) = 4.0 \times 10^{-8}\,[s^2]$. An analyst converts latency measurements from seconds to microseconds ($1\,[s] = 10^6\,[\mu s]$) and claims the variance in microseconds squared is $\text{Var}_{\mu s}(T) = 4.0 \times 10^{-2}\,[\mu s^2]$.
   - Is the analyst's variance conversion correct? Calculate the exact variance in $[\mu s^2]$ and explain the gotcha.

**Solution:**
**Part 1: Conditional Survival Probability**
$$S_T(50) = P(T > 50) = \frac{1}{1 + 0.02(50)} = \frac{1}{1 + 1} = \frac{1}{2} = 0.5000$$
$$S_T(100) = P(T > 100) = \frac{1}{1 + 0.02(100)} = \frac{1}{1 + 2} = \frac{1}{3} \approx 0.3333$$
$$P(T > 100 \mid T > 50) = \frac{P(T > 100)}{P(T > 50)} = \frac{1/3}{1/2} = \frac{2}{3} \approx 0.6667 \text{ (66.67\%)}$$

**Part 2: Watchdog System Reliability**
Parallel redundancy:
$$F_{\text{system}} = p_f^2 = (0.02)^2 = 0.0004$$
$$R_{\text{watchdog}} = 1 - 0.0004 = 0.9996 \text{ (99.96\%)}$$

**Part 3: Market Regime Diagnosis**
Law of Total Probability for $P(S)$:
$$P(S) = (0.01 \cdot 0.70) + (0.15 \cdot 0.20) + (0.80 \cdot 0.10) = 0.007 + 0.030 + 0.080 = 0.1170 \text{ (11.70\%)}$$

Posterior for Extreme Regime $M_3$:
$$P(M_3 \mid S) = \frac{P(S \mid M_3)P(M_3)}{P(S)} = \frac{0.080}{0.1170} = \frac{80}{117} \approx 0.6838 \text{ (68.38\%)}$$

**Part 4: Unit-Conversion Variance Scaling Gotcha**
**Gotcha:** When converting time units by scaling factor $c$, the random variable transforms as $X_{\text{new}} = c \cdot X$.
By the properties of variance, $\text{Var}(c \cdot X) = c^2 \cdot \text{Var}(X)$ ($c^2$ rule).

Here, $c = 10^6\,[\mu s / s]$, so $c^2 = (10^6)^2 = 10^{12}$.
The analyst incorrectly scaled variance by $c = 10^6$ instead of $c^2 = 10^{12}$!

Correct calculation:
$$\text{Var}_{\mu s}(T) = c^2 \cdot \text{Var}_s(T) = 10^{12} \cdot (4.0 \times 10^{-8}) = 4.0 \times 10^4 = 40,000\,[\mu s^2]$$

Standard deviation scaling:
$$\sigma_s = \sqrt{4.0 \times 10^{-8}} = 2.0 \times 10^{-4}\,[s] = 0.2\,[ms] = 200\,[\mu s]$$
$$\sigma_{\mu s} = 200\,[\mu s] \implies \text{Var}_{\mu s}(T) = (200)^2 = 40,000\,[\mu s^2]$$

The analyst's figure of $4.0 \times 10^{-2}$ was off by a factor of one million ($10^6$) due to forgetting the $c^2$ rule!

Final Answer:
- **Part 1:** 2/3 (0.6667)
- **Part 2:** 0.9996 (99.96%)
- **Part 3:** P(S) = 0.1170 (11.70%), P(M3 | S) = 0.6838 (68.38%)
- **Part 4 (Gotcha):** **Incorrect analyst claim.** Correct variance is **$40,000\,[\mu s^2]$** (scaled by $c^2 = 10^{12}$, not $c = 10^6$).

---

## Exam Preparation Guide

### Formula Quick-Reference

| Topic | Formula | Notes / Exam Typologio Format |
| :--- | :--- | :--- |
| **Conditional Probability** | $P(A \mid B) = \frac{P(A \cap B)}{P(B)}$ | Requires $P(B) > 0$. Restricts sample space to $B$. |
| **Conditional Complement** | $P(A^c \mid B) = 1 - P(A \mid B)$ | Holds for any fixed conditioning event $B$. |
| **Two-Event Multiplication Rule** | $P(A \cap B) = P(A) \cdot P(B \mid A) = P(B) \cdot P(A \mid B)$ | Fundamental for multi-stage processes. |
| **Multi-Event Chain Rule** | $P(\bigcap_{i=1}^n A_i) = P(A_1) \prod_{i=2}^n P(A_i \mid \bigcap_{j=1}^{i-1} A_j)$ | Sequential sampling without replacement. |
| **Independence Test** | $P(A \cap B) = P(A) \cdot P(B) \iff P(A \mid B) = P(A)$ | Valid only when events do not affect each other. |
| **Series System Reliability** | $R_{\text{sys}}(t) = \prod_{i=1}^n P(T_i > t)$ | Weakest-link architecture (Logical AND). |
| **Parallel System Reliability** | $R_{\text{sys}}(t) = 1 - \prod_{i=1}^n (1 - P(T_i > t))$ | Redundant architecture (Logical OR). |
| **Law of Total Probability** | $P(A) = \sum_{i=1}^n P(A \mid B_i) P(B_i)$ | $\{B_1, \dots, B_n\}$ must form a valid partition. |
| **Bayes' Theorem** | $P(B_k \mid A) = \frac{P(A \mid B_k)P(B_k)}{\sum_{j=1}^n P(A \mid B_j)P(B_j)}$ | Updates prior $P(B_k)$ to posterior $P(B_k \mid A)$. |
| **Conditional Survival (Time-Domain)** | $P(T > t_{[s]} + s_{[s]} \mid T > t_{[s]}) = \frac{P(T > (t+s)_{[s]})}{P(T > t_{[s]})}$ | Uses time-domain units; memoryless only for Exp/Geom. |
| **Variance Unit Scaling ($c^2$ Rule)** | $\text{Var}(c \cdot X) = c^2 \cdot \text{Var}(X)$ | Scaling time units (e.g., $s \to ms$) scales Var by $c^2$. |

---

### Exam Checklist

| Category | Items |
| :--- | :--- |
| **Must Memorize** | - Conditional probability definition $P(A \mid B) = P(A \cap B)/P(B)$<br>- Multiplication chain rule<br>- Product rule for independence $P(A \cap B) = P(A)P(B)$<br>- Series ($R_{\text{series}} = \prod R_i$) and Parallel ($R_{\text{parallel}} = 1 - \prod (1-R_i)$) formulas<br>- Law of Total Probability formula<br>- Bayes' Theorem formula |
| **Must Understand** | - Difference between mutually exclusive ($P(A \cap B) = 0$) and independent ($P(A \cap B) = P(A)P(B)$) events<br>- Reduced sample space geometric intuition<br>- Reversing conditional probabilities using Bayes' Theorem<br>- Base Rate Fallacy in diagnostic/anomaly detection<br>- Conditional survival function calculation |
| **Book-Only (Professor May Test)** | - Pairwise vs Mutual Independence counterexamples ($n \ge 3$ events)<br>- Right-censored observation windows effect on conditional latency tail estimates<br>- Binary symmetric communication channel Bayes error rate derivations<br>- $k$-out-of-$n$ system reliability binomial expansion |

---

### Common Exam Traps

1. **Conflating Mutually Exclusive with Independent Events:**
   - *Trap:* Assuming that if two events are mutually exclusive ($A \cap B = \emptyset$), they must be independent.
   - *Correction:* If $P(A) > 0$ and $P(B) > 0$, mutually exclusive events are **always dependent** because $P(A \cap B) = 0 \neq P(A)P(B)$.

2. **Misapplying the Memoryless Property:**
   - *Trap:* Assuming $P(T > t + s \mid T > t) = P(T > s)$ for arbitrary time distributions.
   - *Correction:* Memorylessness is **only** true for the Exponential (continuous) and Geometric (discrete) distributions. For all other distributions, you must compute $\frac{P(T > t+s)}{P(T > t)}$ explicitly.

3. **Ignoring the Base Rate in Bayes' Theorem (Base Rate Fallacy):**
   - *Trap:* Conflating $P(A \mid B)$ with $P(B \mid A)$. For example, assuming a test with 99% accuracy means a positive result implies 99% chance of disease.
   - *Correction:* Always calculate the marginal denominator $P(A)$ using the Law of Total Probability. If the prior $P(B)$ is small, $P(B \mid A)$ will be much lower than $P(A \mid B)$.

4. **Forgetting the $c^2$ Variance Scaling Rule in Time Conversion:**
   - *Trap:* Converting time variance from seconds to milliseconds by multiplying by $1,000$.
   - *Correction:* Since $1\,[s] = 1000\,[ms]$, $c = 1000$. Standard deviation scales by $c = 1000$, but variance scales by $c^2 = 1,000,000 = 10^6$!

5. **Assuming Pairwise Independence Implies Mutual Independence:**
   - *Trap:* Proving $P(A \cap B) = P(A)P(B)$, $P(B \cap C) = P(B)P(C)$, and $P(A \cap C) = P(A)P(C)$ and concluding that $A, B, C$ are mutually independent.
   - *Correction:* You must also explicitly verify the 3-way product condition $P(A \cap B \cap C) = P(A)P(B)P(C)$.

---

### Exam Paper Cross-References

| Exam Paper | Relevant Questions | Difficulty | Core Topics Covered |
| :--- | :--- | :---: | :--- |
| [Exam_paper_Easy.md](file:///home/ice/Documents/CodeHub/GitHub-Projects/Public/DitOpenNotes/Year_2/Semester_4/PROBABILITY_STATISTICS/Exams/Papers/Exam_paper_Easy.md) | Question 2 | **1/5** | Basic set probability, independent vs disjoint events. |
| [Exam_paper_2024_09_06_Team_A.md](file:///home/ice/Documents/CodeHub/GitHub-Projects/Public/DitOpenNotes/Year_2/Semester_4/PROBABILITY_STATISTICS/Exams/Papers/Exam_paper_2024_09_06_Team_A.md) | Question 2 | **1/5** | Set relations, testing independence of basic events. |
| [Exam_paper_2023_06_12_Team_null.md](file:///home/ice/Documents/CodeHub/GitHub-Projects/Public/DitOpenNotes/Year_2/Semester_4/PROBABILITY_STATISTICS/Exams/Papers/Exam_paper_2023_06_12_Team_null.md) | Question 3 | **2/5** | Set-based probability, conditional probability basics. |
| [Exam_paper_Intermediate_1.md](file:///home/ice/Documents/CodeHub/GitHub-Projects/Public/DitOpenNotes/Year_2/Semester_4/PROBABILITY_STATISTICS/Exams/Papers/Exam_paper_Intermediate_1.md) | Question 3 | **2/5** | Law of Total Probability & Bayes' Theorem (3-factory problem). |
| [Exam_paper_Intermediate_2.md](file:///home/ice/Documents/CodeHub/GitHub-Projects/Public/DitOpenNotes/Year_2/Semester_4/PROBABILITY_STATISTICS/Exams/Papers/Exam_paper_Intermediate_2.md) | Question 3 | **3/5** | Conditional probability derivations, testing event independence. |
| [Exam_paper_Hard_1.md](file:///home/ice/Documents/CodeHub/GitHub-Projects/Public/DitOpenNotes/Year_2/Semester_4/PROBABILITY_STATISTICS/Exams/Papers/Exam_paper_Hard_1.md) | Question 3 | **4/5** | Bayes' Theorem with sensitivity, specificity, and low base rate. |
| [Exam_paper_Hard_2.md](file:///home/ice/Documents/CodeHub/GitHub-Projects/Public/DitOpenNotes/Year_2/Semester_4/PROBABILITY_STATISTICS/Exams/Papers/Exam_paper_Hard_2.md) | Question 3 | **5/5** | Binary symmetric communication channel Bayes modeling. |

---

## Phase Summary

- **Conditional Probability $P(A \mid B) = \frac{P(A \cap B)}{P(B)}$** quantifies the likelihood of event $A$ given that event $B$ has occurred. The conditioning event $B$ shrinks the universal sample space $\Omega$ to $B$.
- **The Multiplication Chain Rule** $P(A_1 \cap \dots \cap A_n) = P(A_1) P(A_2 \mid A_1) \cdots P(A_n \mid A_1 \cap \dots \cap A_{n-1})$ decomposes complex multi-stage sequential processes (such as microservice pipeline hops or sampling without replacement) into sequential conditional steps.
- **Statistical Independence** requires $P(A \cap B) = P(A) \cdot P(B)$. Independent events convey no information about each other. Mutually exclusive non-zero events ($P(A \cap B) = 0$) can **never** be independent.
- **System Reliability Models** use independence to evaluate infrastructure uptime:
  - **Series Systems (AND):** Require all components to function ($R_{\text{series}} = \prod R_i$).
  - **Parallel Systems (OR):** Require at least one component to function ($R_{\text{parallel}} = 1 - \prod (1 - R_i)$).
- **The Law of Total Probability** $P(A) = \sum P(A \mid B_i) P(B_i)$ reconstructs overall event probabilities across exhaustive sample space partitions.
- **Bayes' Theorem** $P(B_k \mid A) = \frac{P(A \mid B_k)P(B_k)}{\sum P(A \mid B_j)P(B_j)}$ updates prior beliefs $P(B_k)$ to posterior probabilities $P(B_k \mid A)$ upon observing empirical evidence $A$ (such as anomaly alerts or diagnostic test outcomes).
- **Time-Domain Applications** require explicit time units, careful evaluation of conditional survival functions $P(T > t+s \mid T > t)$, awareness of right-censoring bias, avoiding the base rate fallacy, and enforcing the $c^2$ variance scaling rule on unit conversions.
