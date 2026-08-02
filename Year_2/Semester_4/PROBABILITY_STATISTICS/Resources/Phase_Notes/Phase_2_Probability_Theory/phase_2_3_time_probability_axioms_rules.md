# Phase 2.3 (Time): Probability Axioms & Rules for Time-Based Events

The **Probability Axioms** (Kolmogorov's Axioms) are the three foundational rules from which all of probability theory is derived. The **Addition Rule** and **De Morgan's Laws** are the most practically important tools built on top of these axioms for computing probabilities in exam problems. When the events are **time-based** (timeouts, latency thresholds, scheduling conflicts), these rules apply identically -- but the interpretation of each probability is grounded in time.

---

## 1. Kolmogorov's Axioms (Time Context)

For any time-based event $A$ in a sample space $\Omega$, probability $P$ is a function that satisfies three axioms:

**Axiom 1 (Non-negativity):**

$$P(A) \geq 0$$

The probability of any time event is always a non-negative real number. (e.g., $P(\text{timeout}) \geq 0$.)

**Axiom 2 (Normalization):**

$$P(\Omega) = 1$$

The probability of the certain event (some time outcome must occur) is exactly 1. (e.g., the response time must be some value in $\Omega$.)

**Axiom 3 (Countable Additivity):**

If time events $A$ and $B$ are mutually exclusive ($A \cap B = \emptyset$):

$$P(A \cup B) = P(A) + P(B)$$

More generally, for any finite collection of mutually exclusive time events $A_1, A_2, \ldots, A_n$:

$$P\left(\bigcup_{i=1}^{n} A_i\right) = \sum_{i=1}^{n} P(A_i)$$

> **Time example:** If $A$ = "response time $< 50\text{ ms}$" and $B$ = "response time $\ge 200\text{ ms}$" are mutually exclusive, then $P(A \cup B) = P(A) + P(B)$ -- the probability of a very fast or very slow response.

---

## 2. Derived Properties (Consequences of the Axioms)

These results follow directly from the three axioms and apply equally to time events:

| Property | Formula | Time Interpretation |
| :--- | :--- | :--- |
| Complement Rule | $P(A') = 1 - P(A)$ | $P(\text{no timeout}) = 1 - P(\text{timeout})$ |
| Impossible event | $P(\emptyset) = 0$ | $P(\text{negative response time}) = 0$ |
| Probability bounds | $0 \leq P(A) \leq 1$ | Any time event probability is between 0 and 1 |
| Monotonicity | If $A \subseteq B$, then $P(A) \leq P(B)$ | If "response $< 50\text{ ms}$" $\subseteq$ "response $< 100\text{ ms}$", then $P(< 50) \le P(< 100)$ |

---

## 3. The Addition Rule (General) for Time Events

For any two time-based events $A$ and $B$ (not necessarily mutually exclusive):

$$\boxed{P(A \cup B) = P(A) + P(B) - P(A \cap B)}$$

**Why subtract?** When computing $P(A) + P(B)$, the overlap region $A \cap B$ is counted twice (once in $P(A)$ and once in $P(B)$). Subtracting $P(A \cap B)$ corrects for this double-counting.

> **Time example:** $A$ = "response $> 100\text{ ms}$", $B$ = "high CPU load". A request can be both slow and under high CPU load. The overlap $A \cap B$ = "slow AND high CPU" is counted in both $P(A)$ and $P(B)$, so it must be subtracted once.

**Special case -- Mutually Exclusive Time Events:** When $A \cap B = \emptyset$:

$$P(A \cup B) = P(A) + P(B) - 0 = P(A) + P(B)$$

**Extension to three time events:**

$$P(A \cup B \cup C) = P(A) + P(B) + P(C) - P(A \cap B) - P(A \cap C) - P(B \cap C) + P(A \cap B \cap C)$$

This pattern is called the **Inclusion-Exclusion Principle**.

---

## 4. De Morgan's Laws (Time Context)

De Morgan's Laws describe the complement of a union or intersection. They are one of the most tested identities in probability exams.

**First Law:**

$$\boxed{(A \cup B)' = A' \cap B'}$$

In probability:

$$P((A \cup B)') = P(A' \cap B')$$

Reading: "NOT (A or B)" is the same as "(NOT A) AND (NOT B)". Neither time event occurs.

> **Time example:** If $A$ = "timeout" and $B$ = "retry", then $(A \cup B)'$ = "no timeout AND no retry" = the request succeeded on the first attempt.

**Second Law:**

$$\boxed{(A \cap B)' = A' \cup B'}$$

In probability:

$$P((A \cap B)') = P(A' \cup B')$$

Reading: "NOT (A and B)" is the same as "(NOT A) OR (NOT B)". At least one time event fails to occur.

> **Time example:** If $A$ = "fast response" and $B$ = "low CPU", then $(A \cap B)'$ = "NOT (fast AND low CPU)" = "either slow OR high CPU (or both)".

**Intuition:** De Morgan's Laws "push the complement inside" while swapping the operator between $\cup$ and $\cap$.

| Operation     | After applying De Morgan | Operator swap   |
| :------------ | :----------------------- | :-------------- |
| $(A \cup B)'$ | $A' \cap B'$             | $\cup \to \cap$ |
| $(A \cap B)'$ | $A' \cup B'$             | $\cap \to \cup$ |

---

## 5. Computing $P(A' \cap B')$ and $P(A' \cup B')$ for Time Events

These are the two most common forms asked in problems:

**Computing "neither" $P(A' \cap B')$:**

Apply De Morgan's First Law, then use the complement rule:

$$P(A' \cap B') = P((A \cup B)') = 1 - P(A \cup B)$$

**Computing "not both" $P(A' \cup B')$:**

Apply De Morgan's Second Law, then use the complement rule:

$$P(A' \cup B') = P((A \cap B)') = 1 - P(A \cap B)$$

---

## 6. Time-Specific Gotchas

### Gotcha 1: Mutually Exclusive Time Events and the Addition Rule

When time events are defined as non-overlapping intervals (e.g., $A = [0, 50)\text{ ms}$, $B = [50, 100)\text{ ms}$), they are mutually exclusive and $P(A \cup B) = P(A) + P(B)$. But if the intervals share even a single boundary point (e.g., $A = [0, 50]$, $B = [50, 100]$), they are technically **not** mutually exclusive ($A \cap B = \{50\}$). In continuous probability, a single point has probability 0, so this is usually harmless -- but in discrete time slots, boundary overlap matters.

### Gotcha 2: Probability of a Single Point in Continuous Time

In continuous time sample spaces, $P(T = t_0) = 0$ for any exact time $t_0$. This means $P(T < 100\text{ ms}) = P(T \le 100\text{ ms})$. The boundary does not affect the probability. This is different from discrete time slots, where $P(T = \text{hour 3})$ can be nonzero.

### Gotcha 3: "Neither" vs. "Not Both" for Time Events

"Neither timeout nor retry" ($P(A' \cap B')$) means the request was clean -- no issues at all. "Not both timeout and retry" ($P(A' \cup B')$) is a much weaker condition -- it only excludes the case where both happened simultaneously. These are very different probabilities and must not be confused.

---

## 7. Solved Exercises (9 Examples)

### Exercise 1: Direct Application of Addition Rule (Time Events)

**Problem:** $P(A) = 0.6$ (slow response $> 200\text{ ms}$), $P(B) = 0.4$ (high CPU load), $P(A \cap B) = 0.2$ (slow and high CPU). Find $P(A \cup B)$ -- the probability of slow response or high CPU or both.

**Solution:**

$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

$$P(A \cup B) = 0.6 + 0.4 - 0.2 = 0.8$$

> **Interpretation:** 80% of requests are either slow, under high CPU, or both.

---

### Exercise 2: Finding $P(A \cap B)$ from the Addition Rule (Time Events)

**Problem:** $P(A) = 0.5$ (timeout), $P(B) = 0.45$ (retry), $P(A \cup B) = 0.7$ (at least one issue). Find $P(A \cap B)$ -- the probability of both timeout and retry.

**Solution:**

Rearrange the addition rule to solve for the intersection:

$$P(A \cap B) = P(A) + P(B) - P(A \cup B)$$

$$P(A \cap B) = 0.5 + 0.45 - 0.7 = 0.25$$

> **Interpretation:** 25% of requests both timed out and were retried.

---

### Exercise 3: Applying De Morgan's First Law (Time Events)

**Problem:** $P(A) = 0.5$ (timeout), $P(B) = 0.4$ (retry), $P(A \cap B) = 0.2$ (both). Find $P(A' \cap B')$ -- the probability of neither timeout nor retry.

**Solution:**

**Step 1:** Apply De Morgan's First Law:

$$P(A' \cap B') = P((A \cup B)')$$

**Step 2:** Compute $P(A \cup B)$ using the addition rule:

$$P(A \cup B) = 0.5 + 0.4 - 0.2 = 0.7$$

**Step 3:** Apply the complement rule:

$$P((A \cup B)') = 1 - 0.7 = 0.3$$

Therefore $P(A' \cap B') = 0.3$.

> **Interpretation:** 30% of requests had no timeout and no retry -- the clean path.

---

### Exercise 4: Applying De Morgan's Second Law (Time Events)

**Problem:** Using the same values as Exercise 3, find $P(A' \cup B')$ -- the probability that not both timeout and retry occur.

**Solution:**

**Step 1:** Apply De Morgan's Second Law:

$$P(A' \cup B') = P((A \cap B)')$$

**Step 2:** Apply the complement rule:

$$P((A \cap B)') = 1 - P(A \cap B) = 1 - 0.2 = 0.8$$

Therefore $P(A' \cup B') = 0.8$.

> **Interpretation:** 80% of requests did NOT have both timeout and retry simultaneously. This is a much weaker condition than "neither" (30%).

---

### Exercise 5: Mutually Exclusive Time Events

**Problem:** Two time events $A$ and $B$ are mutually exclusive. $A$ = "response $< 50\text{ ms}$", $B$ = "response $> 200\text{ ms}$". $P(A) = 0.35$, $P(B) = 0.25$. Find: (a) $P(A \cup B)$, (b) $P(A' \cap B')$.

**Solution:**

Since $A \cap B = \emptyset$, we have $P(A \cap B) = 0$.

(a) $P(A \cup B) = P(A) + P(B) = 0.35 + 0.25 = 0.60$

(b) $P(A' \cap B') = 1 - P(A \cup B) = 1 - 0.60 = 0.40$

> **Interpretation:** 60% of responses are either very fast or very slow. 40% are in the "normal" range ($50\text{--}200\text{ ms}$).

---

### Exercise 6: Checking Axiom Compliance (Time Events)

**Problem:** A student claims: $P(A) = 0.7$ (timeout), $P(B) = 0.6$ (retry), $P(A \cup B) = 0.8$ (at least one). Is this consistent with the probability axioms?

**Solution:**

Compute $P(A \cap B)$ from the addition rule:

$$P(A \cap B) = 0.7 + 0.6 - 0.8 = 0.5$$

**Check 1:** Is $P(A \cap B) \geq 0$? Yes, $0.5 \geq 0$.

**Check 2:** Is $P(A \cap B) \leq P(A)$ and $P(A \cap B) \leq P(B)$? Yes, $0.5 \leq 0.7$ and $0.5 \leq 0.6$.

**Check 3:** Is $P(A \cup B) \leq 1$? Yes, $0.8 \leq 1$.

All axiom requirements are satisfied. The assignment is **consistent**.

---

### Exercise 7: Three-Event Inclusion-Exclusion (Time Events)

**Problem:** $P(A) = 0.4$ (timeout), $P(B) = 0.3$ (retry), $P(C) = 0.5$ (cache miss), $P(A \cap B) = 0.1$, $P(A \cap C) = 0.15$, $P(B \cap C) = 0.1$, $P(A \cap B \cap C) = 0.05$. Find $P(A \cup B \cup C)$ -- the probability of at least one time event.

**Solution:**

$$P(A \cup B \cup C) = P(A) + P(B) + P(C) - P(A \cap B) - P(A \cap C) - P(B \cap C) + P(A \cap B \cap C)$$

$$= 0.4 + 0.3 + 0.5 - 0.1 - 0.15 - 0.1 + 0.05$$

$$= 1.2 - 0.35 + 0.05 = 0.90$$

> **Interpretation:** 90% of requests experienced at least one of: timeout, retry, or cache miss. Only 10% had a completely clean path.

---

### Exercise 8: Full Multi-Step Problem (Time Events)

**Problem:** In a group of 100 requests, 60 had response time $< 100\text{ ms}$ ($F$), 45 arrived during peak hours ($P$), and 20 were neither fast nor during peak. Find: (a) the number who were both fast and during peak, (b) $P(F' \cap P')$, (c) $P(F' \cup P')$.

**Solution:**

**Step 1:** Number with at least one condition = $100 - 20 = 80$, so $P(F \cup P) = 0.80$.

**Step 2:** Apply the addition rule to find $P(F \cap P)$:

$$P(F \cap P) = P(F) + P(P) - P(F \cup P)$$

$$P(F \cap P) = 0.60 + 0.45 - 0.80 = 0.25$$

Number both fast and during peak = $0.25 \times 100 = \mathbf{25}$.

**Step 3:** (b) "Neither" using De Morgan's First Law:

$$P(F' \cap P') = 1 - P(F \cup P) = 1 - 0.80 = 0.20$$

**Step 4:** (c) "Not both" using De Morgan's Second Law:

$$P(F' \cup P') = 1 - P(F \cap P) = 1 - 0.25 = 0.75$$

> **Interpretation:** 20% of requests were neither fast nor during peak. 75% did not have both conditions simultaneously (i.e., were not fast-during-peak).

---

### Exercise 9: R Snippet -- Addition Rule and De Morgan's for Time Events

**Problem:** Use R to verify the addition rule and De Morgan's Laws for $P(A) = 0.5$, $P(B) = 0.4$, $P(A \cap B) = 0.2$.

**Solution:**

```r
# Given probabilities for time events
P_A <- 0.5  # timeout
P_B <- 0.4  # retry
P_A_and_B <- 0.2  # both

# Addition rule
P_A_or_B <- P_A + P_B - P_A_and_B
cat("P(A union B) =", P_A_or_B, "\n")

# De Morgan's First Law: P(A' intersect B') = 1 - P(A union B)
P_neither <- 1 - P_A_or_B
cat("P(neither) = P(A' intersect B') =", P_neither, "\n")

# De Morgan's Second Law: P(A' union B') = 1 - P(A intersect B)
P_not_both <- 1 - P_A_and_B
cat("P(not both) = P(A' union B') =", P_not_both, "\n")

# Verification: four regions sum to 1
only_A <- P_A - P_A_and_B
only_B <- P_B - P_A_and_B
both <- P_A_and_B
neither <- P_neither
cat("\nFour regions:\n")
cat("  Only A:", only_A, "\n")
cat("  Both:", both, "\n")
cat("  Only B:", only_B, "\n")
cat("  Neither:", neither, "\n")
cat("  Sum:", only_A + only_B + both + neither, "\n")
```

**Expected output:**
```
P(A union B) = 0.7
P(neither) = P(A' intersect B') = 0.3
P(not both) = P(A' union B') = 0.8

Four regions:
  Only A: 0.3
  Both: 0.2
  Only B: 0.2
  Neither: 0.3
  Sum: 1
```

> **R note:** The four regions sum to 1, confirming axiom compliance. De Morgan's Laws provide the quickest path to "neither" (0.3) and "not both" (0.8) without computing complements of individual events.

---

## 8. Core Formulas Summary (Time Context)

| Formula | Name | When to Use (Time) |
| :--- | :--- | :--- |
| $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ | Addition Rule | Finding union of any two time events |
| $P(A') = 1 - P(A)$ | Complement Rule | Finding probability of "not A" (e.g., no timeout) |
| $(A \cup B)' = A' \cap B'$ | De Morgan's First Law | "Neither" problems (no timeout AND no retry) |
| $(A \cap B)' = A' \cup B'$ | De Morgan's Second Law | "Not both" problems |
| $P(A' \cap B') = 1 - P(A \cup B)$ | Neither (derived) | Quickest path to "neither" |
| $P(A' \cup B') = 1 - P(A \cap B)$ | Not both (derived) | Quickest path to "not both" |

---

## Exam Tip: The De Morgan Shortcut (Time Context)

Whenever you see $P(A' \cap B')$ or $P(A' \cup B')$ in an exam with time events, do not attempt to compute complements directly. Instead, apply De Morgan's Law immediately:

*   $P(A' \cap B') \xrightarrow{\text{De Morgan}} 1 - P(A \cup B)$: compute the union first, then subtract from 1.
*   $P(A' \cup B') \xrightarrow{\text{De Morgan}} 1 - P(A \cap B)$: compute the intersection first, then subtract from 1.

This two-step method is the fastest and most reliable approach and reduces complex complement expressions to standard addition rule problems.