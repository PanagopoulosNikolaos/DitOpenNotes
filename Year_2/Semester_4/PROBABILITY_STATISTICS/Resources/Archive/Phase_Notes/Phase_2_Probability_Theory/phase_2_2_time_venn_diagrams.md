# Phase 2.2 (Time): Venn Diagrams & Translating Time-Based Worded Problems

Venn Diagrams are a visual tool that maps relationships between events onto overlapping circles. Their primary purpose in probability is to **translate English language problem descriptions into precise set notation**, which can then be evaluated using formulas. When the events are **time-based** (e.g., "request timed out", "response under 100 ms", "arrived during peak hours"), mastering this translation is one of the highest-leverage skills for exams.

---

## 1. Standard Venn Diagram Layout (Time Context)

For two time-based events $A$ and $B$ within a sample space $\Omega$, the diagram divides the space into four mutually exclusive regions:

```
 ___________________________________
|              Omega                |
|   ___________   ___________       |
|  |           | |           |      |
|  |  A only   |A|   B only  |      |
|  |  (A∩B')   |∩|   (A'∩B)  |      |
|  |___________|B|___________|      |
|                                   |
|         (A∪B)' = A'∩B'            |
|___________________________________|
```

| Region | Set Notation | Time Meaning |
| :--- | :--- | :--- |
| Left circle only | $A \cap B'$ | A occurs, B does not |
| Overlapping center | $A \cap B$ | Both A and B occur |
| Right circle only | $A' \cap B$ | B occurs, A does not |
| Outside both circles | $A' \cap B'$ | Neither A nor B occurs |

The **fundamental partition rule**: the four regions are mutually exclusive and collectively exhaustive. Their probabilities sum to 1.

$$P(A \cap B') + P(A \cap B) + P(A' \cap B) + P(A' \cap B') = 1$$

> **Time example:** $A$ = "response time $< 100\text{ ms}$", $B$ = "request arrived during peak hours". The overlap $A \cap B$ = "fast response AND arrived during peak". The region $A \cap B'$ = "fast response AND arrived off-peak".

---

## 2. Translating Key Time Phrases into Set Notation

This table is the most important reference in this file. Memorise these translations.

| English Phrase (Time) | Set Notation | Notes |
| :--- | :--- | :--- |
| "A occurs" | $A$ | Direct |
| "A does not occur" | $A'$ | Complement |
| "Both A and B occur" | $A \cap B$ | Intersection |
| "At least one of A, B occurs" | $A \cup B$ | Union (includes both) |
| "Exactly one of A, B occurs" | $(A \cap B') \cup (A' \cap B)$ | Union minus the overlap |
| "Only A occurs" | $A \cap B'$ | A but not B |
| "Only B occurs" | $A' \cap B$ | B but not A |
| "Neither A nor B occurs" | $A' \cap B'$ = $(A \cup B)'$ | Outside both circles |
| "A but not B" | $A \cap B'$ | Same as "only A" |
| "At most one of A, B" | $(A \cap B)'$ = $A' \cup B'$ | Not both simultaneously |

> **Critical insight:** "At least one" means $A \cup B$. "Exactly one" means $A \cup B$ minus the case where both occur, i.e., $(A \cup B) \setminus (A \cap B)$.

---

## 3. Extending to Three Time Events

For three time-based events $A$, $B$, $C$, the Venn Diagram has **8 mutually exclusive regions**. Key phrases extend naturally:

| Phrase (Time) | Set Notation |
| :--- | :--- |
| "All three occur" | $A \cap B \cap C$ |
| "At least one occurs" | $A \cup B \cup C$ |
| "None occur" | $A' \cap B' \cap C'$ = $(A \cup B \cup C)'$ |
| "Exactly one occurs" | $(A \cap B' \cap C') \cup (A' \cap B \cap C') \cup (A' \cap B' \cap C)$ |
| "At least two occur" | $(A \cap B \cap C') \cup (A \cap B' \cap C) \cup (A' \cap B \cap C) \cup (A \cap B \cap C)$ |

> **Time example with three events:** $A$ = "fast response ($< 100\text{ ms}$)", $B$ = "arrived during peak", $C$ = "from mobile client". "All three" = $A \cap B \cap C$ = fast, peak, mobile.

---

## 4. Time-Specific Gotchas

### Gotcha 1: Mutually Exclusive Time Events Are Not Independent

Two time events can be mutually exclusive (disjoint) without being independent. In fact, mutually exclusive events are **maximally dependent**: if $A$ occurs, $B$ cannot occur. For example, $A$ = "response time $< 50\text{ ms}$" and $B$ = "response time $> 200\text{ ms}$" are mutually exclusive. Knowing $A$ occurred tells you $B$ definitely did not.

### Gotcha 2: Overlapping Time Intervals in Venn Diagrams

When events are defined as time intervals (e.g., $A = [0, 100)\text{ ms}$, $B = [50, 200)\text{ ms}$), the overlap $A \cap B = [50, 100)\text{ ms}$ is a time interval, not a single point. The Venn diagram still applies -- the overlap region represents all outcomes in that sub-interval.

### Gotcha 3: "At Least One" vs. "Exactly One" for Time Events

In time monitoring, "at least one timeout occurred" ($A \cup B$) includes the case where both systems timed out. "Exactly one timeout" ($(A \cap B') \cup (A' \cap B)$) excludes the simultaneous timeout case. These are different probabilities and must not be confused.

---

## 5. Solved Exercises (9 Examples)

### Exercise 1: Building a Venn Diagram from Time-Based Counts

**Problem:** In a sample of 50 requests, 30 had response time $< 100\text{ ms}$ ($F$), 25 arrived during peak hours ($P$), and 15 were both fast and during peak. Find the number of requests that were only fast, only during peak, and neither.

**Solution:**

**Step 1:** Find the overlap region first.
$$|F \cap P| = 15$$

**Step 2:** Find "only fast":
$$|F \cap P'| = |F| - |F \cap P| = 30 - 15 = 15$$

**Step 3:** Find "only peak":
$$|F' \cap P| = |P| - |F \cap P| = 25 - 15 = 10$$

**Step 4:** Find "neither":
$$|F' \cap P'| = 50 - 15 - 15 - 10 = 10$$

**Filled Diagram regions:** Only Fast = 15, Both = 15, Only Peak = 10, Neither = 10. Total = 50. Verified.

---

### Exercise 2: Translating "At Least One" (Time Events)

**Problem:** $P(A) = 0.5$ (request timed out), $P(B) = 0.4$ (request retried), $P(A \cap B) = 0.2$ (timed out and retried). Find the probability that at least one of $A$ or $B$ occurs.

**Solution:**

"At least one" translates to $A \cup B$.

$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

$$P(A \cup B) = 0.5 + 0.4 - 0.2 = 0.7$$

> **Interpretation:** 70% of requests either timed out, were retried, or both.

---

### Exercise 3: Translating "Neither" (Time Events)

**Problem:** Using the values from Exercise 2, find the probability that neither $A$ nor $B$ occurs (no timeout and no retry).

**Solution:**

"Neither" translates to $A' \cap B' = (A \cup B)'$.

$$P((A \cup B)') = 1 - P(A \cup B) = 1 - 0.7 = 0.3$$

> **Interpretation:** 30% of requests had no timeout and no retry -- they succeeded on the first attempt within the time limit.

---

### Exercise 4: Translating "Exactly One" (Time Events)

**Problem:** Using the values from Exercise 2, find the probability that exactly one of $A$ or $B$ occurs (either a timeout or a retry, but not both).

**Solution:**

"Exactly one" = $(A \cap B') \cup (A' \cap B)$

**Method:** Total in at least one minus the overlap (where both occur):

$$P(\text{exactly one}) = P(A \cup B) - P(A \cap B)$$

$$P(\text{exactly one}) = 0.7 - 0.2 = 0.5$$

**Alternative breakdown:**
*   $P(A \cap B') = P(A) - P(A \cap B) = 0.5 - 0.2 = 0.3$ (timeout but no retry)
*   $P(A' \cap B) = P(B) - P(A \cap B) = 0.4 - 0.2 = 0.2$ (retry but no timeout)
*   $P(\text{exactly one}) = 0.3 + 0.2 = 0.5$ (same result)

---

### Exercise 5: Translating "Only A" (Time Events)

**Problem:** A monitoring system shows $P(A) = 0.6$ (slow response $> 200\text{ ms}$), $P(B) = 0.5$ (high CPU load), $P(A \cup B) = 0.8$. Find $P(\text{only } A)$ -- slow response without high CPU.

**Solution:**

**Step 1:** Find $P(A \cap B)$ using the addition rule:

$$P(A \cap B) = P(A) + P(B) - P(A \cup B) = 0.6 + 0.5 - 0.8 = 0.3$$

**Step 2:** "Only A" = $A \cap B'$:

$$P(A \cap B') = P(A) - P(A \cap B) = 0.6 - 0.3 = 0.3$$

> **Interpretation:** 30% of requests were slow without high CPU load -- the bottleneck is elsewhere (e.g., network or disk I/O).

---

### Exercise 6: Reading a Filled Venn Diagram (Time Events)

**Problem:** The regions of a Venn Diagram for time events $A$ (timeout) and $B$ (retry) are filled with the following probabilities:

| Region | Probability |
| :--- | :--- |
| Only $A$ ($A \cap B'$) | 0.25 |
| Both ($A \cap B$) | 0.15 |
| Only $B$ ($A' \cap B$) | 0.30 |
| Neither ($A' \cap B'$) | 0.30 |

Find: (a) $P(A)$, (b) $P(B)$, (c) $P(A \cup B)$, (d) $P(\text{exactly one})$.

**Solution:**

(a) $P(A) = P(A \cap B') + P(A \cap B) = 0.25 + 0.15 = 0.40$

(b) $P(B) = P(A' \cap B) + P(A \cap B) = 0.30 + 0.15 = 0.45$

(c) $P(A \cup B) = 0.25 + 0.15 + 0.30 = 0.70$

(d) $P(\text{exactly one}) = P(A \cap B') + P(A' \cap B) = 0.25 + 0.30 = 0.55$

**Verification:** $0.25 + 0.15 + 0.30 + 0.30 = 1.00$ (all regions sum to 1).

---

### Exercise 7: Three Time Events - "None"

**Problem:** $P(A \cup B \cup C) = 0.85$ where $A$ = "timeout", $B$ = "retry", $C$ = "cache miss". Find the probability that none of the three time events occur.

**Solution:**

"None occur" = $(A \cup B \cup C)'$

$$P(A' \cap B' \cap C') = 1 - P(A \cup B \cup C) = 1 - 0.85 = 0.15$$

> **Interpretation:** 15% of requests had no timeout, no retry, and no cache miss -- the ideal path.

---

### Exercise 8: Backward Problem - Finding an Unknown (Time Events)

**Problem:** Given $P(A) = 0.45$ (slow response), $P(B) = 0.30$ (high load), and $P(\text{exactly one of } A, B) = 0.55$. Find $P(A \cap B)$ -- the probability of both slow response and high load.

**Solution:**

"Exactly one" can be written as:

$$P(\text{exactly one}) = P(A) + P(B) - 2 \cdot P(A \cap B)$$

This is derived from:

$$P(\text{exactly one}) = [P(A) - P(A \cap B)] + [P(B) - P(A \cap B)]$$

Substituting known values:

$$0.55 = 0.45 + 0.30 - 2 \cdot P(A \cap B)$$

$$0.55 = 0.75 - 2 \cdot P(A \cap B)$$

$$P(A \cap B) = \frac{0.75 - 0.55}{2} = \frac{0.20}{2} = 0.10$$

> **Interpretation:** 10% of requests had both slow response and high CPU load -- these are the cases where CPU is the likely bottleneck.

---

### Exercise 9: R Snippet -- Venn Diagram Counts for Time Events

**Problem:** Use R to compute the four Venn diagram regions for 50 requests where 30 are fast ($F$), 25 arrive during peak ($P$), and 15 are both.

**Solution:**

```r
# Total counts
n <- 50
n_F <- 30       # fast response
n_P <- 25       # peak hours
n_F_and_P <- 15 # both fast and peak

# Four mutually exclusive regions
only_F <- n_F - n_F_and_P
only_P <- n_P - n_F_and_P
both <- n_F_and_P
neither <- n - only_F - only_P - both

cat("Only Fast:", only_F, "\n")
cat("Both:", both, "\n")
cat("Only Peak:", only_P, "\n")
cat("Neither:", neither, "\n")
cat("Total check:", only_F + only_P + both + neither, "\n")
```

**Expected output:**
```
Only Fast: 15
Both: 15
Only Peak: 10
Neither: 10
Total check: 50
```

> **R note:** The four-region decomposition is the foundation for all Venn diagram probability calculations. Once these four values are known, any probability expression involving $A$ and $B$ can be computed by summing the appropriate regions.

---

## Exam Tip: The Four-Region Decomposition (Time Context)

**Always decompose** a Venn Diagram into its four mutually exclusive regions at the start of a problem:

$$P(A \cap B'), \quad P(A \cap B), \quad P(A' \cap B), \quad P(A' \cap B')$$

Once these four values are known, **any probability expression** involving time events $A$ and $B$ can be computed by summing the appropriate regions. This method is infallible and prevents double-counting errors -- especially when time intervals overlap.