# Phase 2.3: Probability Axioms & Rules

The **Probability Axioms** (Kolmogorov's Axioms) are the three foundational rules from which all of probability theory is derived. The **Addition Rule** and **De Morgan's Laws** are the most practically important tools built on top of these axioms for computing probabilities in exam problems.

---

## 1. Kolmogorov's Axioms

For any event $A$ in a sample space $\Omega$, probability $P$ is a function that satisfies three axioms:

**Axiom 1 (Non-negativity):**

$$P(A) \geq 0$$

The probability of any event is always a non-negative real number.

**Axiom 2 (Normalization):**

$$P(\Omega) = 1$$

The probability of the certain event (something must happen) is exactly 1.

**Axiom 3 (Countable Additivity):**

If $A$ and $B$ are mutually exclusive ($A \cap B = \emptyset$):

$$P(A \cup B) = P(A) + P(B)$$

More generally, for any finite collection of mutually exclusive events $A_1, A_2, \ldots, A_n$:

$$P\left(\bigcup_{i=1}^{n} A_i\right) = \sum_{i=1}^{n} P(A_i)$$

---

## 2. Derived Properties (Consequences of the Axioms)

These results follow directly from the three axioms:

| Property | Formula | Derivation |
| :--- | :--- | :--- |
| Complement Rule | $P(A') = 1 - P(A)$ | From $P(A) + P(A') = P(\Omega) = 1$ |
| Impossible event | $P(\emptyset) = 0$ | From $\emptyset = \Omega'$ |
| Probability bounds | $0 \leq P(A) \leq 1$ | From Axioms 1 and 2 |
| Monotonicity | If $A \subseteq B$, then $P(A) \leq P(B)$ | B covers A plus more outcomes |

---

## 3. The Addition Rule (General)

For any two events $A$ and $B$ (not necessarily mutually exclusive):

$$\boxed{P(A \cup B) = P(A) + P(B) - P(A \cap B)}$$

**Why subtract?** When computing $P(A) + P(B)$, the overlap region $A \cap B$ is counted twice (once in $P(A)$ and once in $P(B)$). Subtracting $P(A \cap B)$ corrects for this double-counting.

**Special case — Mutually Exclusive:** When $A \cap B = \emptyset$:

$$P(A \cup B) = P(A) + P(B) - 0 = P(A) + P(B)$$

**Extension to three events:**

$$P(A \cup B \cup C) = P(A) + P(B) + P(C) - P(A \cap B) - P(A \cap C) - P(B \cap C) + P(A \cap B \cap C)$$

This pattern is called the **Inclusion-Exclusion Principle**.

---

## 4. De Morgan's Laws

De Morgan's Laws describe the complement of a union or intersection. They are one of the most tested identities in probability exams.

**First Law:**

$$\boxed{(A \cup B)' = A' \cap B'}$$

In probability:

$$P((A \cup B)') = P(A' \cap B')$$

Reading: "NOT (A or B)" is the same as "(NOT A) AND (NOT B)". Neither event occurs.

**Second Law:**

$$\boxed{(A \cap B)' = A' \cup B'}$$

In probability:

$$P((A \cap B)') = P(A' \cup B')$$

Reading: "NOT (A and B)" is the same as "(NOT A) OR (NOT B)". At least one event fails to occur.

**Intuition:** De Morgan's Laws "push the complement inside" while swapping the operator between $\cup$ and $\cap$.

| Operation | After applying De Morgan | Operator swap |
| :--- | :--- | :--- |
| $(A \cup B)'$ | $A' \cap B'$ | $\cup \to \cap$ |
| $(A \cap B)'$ | $A' \cup B'$ | $\cap \to \cup$ |

---

## 5. Computing $P(A' \cap B')$ and $P(A' \cup B')$

These are the two most common forms asked in problems:

**Computing "neither" $P(A' \cap B')$:**

Apply De Morgan's First Law, then use the complement rule:

$$P(A' \cap B') = P((A \cup B)') = 1 - P(A \cup B)$$

**Computing "not both" $P(A' \cup B')$:**

Apply De Morgan's Second Law, then use the complement rule:

$$P(A' \cup B') = P((A \cap B)') = 1 - P(A \cap B)$$

---

## 6. Solved Exercises

### Exercise 1: Direct Application of Addition Rule

**Problem:** $P(A) = 0.6$, $P(B) = 0.4$, $P(A \cap B) = 0.2$. Find $P(A \cup B)$.

**Solution:**

$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

$$P(A \cup B) = 0.6 + 0.4 - 0.2 = 0.8$$

---

### Exercise 2: Finding $P(A \cap B)$ from the Addition Rule

**Problem:** $P(A) = 0.5$, $P(B) = 0.45$, $P(A \cup B) = 0.7$. Find $P(A \cap B)$.

**Solution:**

Rearrange the addition rule to solve for the intersection:

$$P(A \cap B) = P(A) + P(B) - P(A \cup B)$$

$$P(A \cap B) = 0.5 + 0.45 - 0.7 = 0.25$$

---

### Exercise 3: Applying De Morgan's First Law

**Problem:** $P(A) = 0.5$, $P(B) = 0.4$, $P(A \cap B) = 0.2$. Find $P(A' \cap B')$.

**Solution:**

**Step 1:** Apply De Morgan's First Law:

$$P(A' \cap B') = P((A \cup B)')$$

**Step 2:** Compute $P(A \cup B)$ using the addition rule:

$$P(A \cup B) = 0.5 + 0.4 - 0.2 = 0.7$$

**Step 3:** Apply the complement rule:

$$P((A \cup B)') = 1 - 0.7 = 0.3$$

Therefore $P(A' \cap B') = 0.3$.

---

### Exercise 4: Applying De Morgan's Second Law

**Problem:** Using the same values as Exercise 3, find $P(A' \cup B')$.

**Solution:**

**Step 1:** Apply De Morgan's Second Law:

$$P(A' \cup B') = P((A \cap B)')$$

**Step 2:** Apply the complement rule:

$$P((A \cap B)') = 1 - P(A \cap B) = 1 - 0.2 = 0.8$$

Therefore $P(A' \cup B') = 0.8$.

---

### Exercise 5: Mutually Exclusive Events

**Problem:** Two events $A$ and $B$ are mutually exclusive. $P(A) = 0.35$, $P(B) = 0.25$. Find: (a) $P(A \cup B)$, (b) $P(A' \cap B')$.

**Solution:**

Since $A \cap B = \emptyset$, we have $P(A \cap B) = 0$.

(a) $P(A \cup B) = P(A) + P(B) = 0.35 + 0.25 = 0.60$

(b) $P(A' \cap B') = 1 - P(A \cup B) = 1 - 0.60 = 0.40$

---

### Exercise 6: Checking Axiom Compliance

**Problem:** A student claims: $P(A) = 0.7$, $P(B) = 0.6$, $P(A \cup B) = 0.8$. Is this consistent with the probability axioms?

**Solution:**

Compute $P(A \cap B)$ from the addition rule:

$$P(A \cap B) = 0.7 + 0.6 - 0.8 = 0.5$$

**Check 1:** Is $P(A \cap B) \geq 0$? Yes, $0.5 \geq 0$.

**Check 2:** Is $P(A \cap B) \leq P(A)$ and $P(A \cap B) \leq P(B)$? Yes, $0.5 \leq 0.7$ and $0.5 \leq 0.6$.

**Check 3:** Is $P(A \cup B) \leq 1$? Yes, $0.8 \leq 1$.

All axiom requirements are satisfied. The assignment is **consistent**.

---

### Exercise 7: Three-Event Inclusion-Exclusion

**Problem:** $P(A) = 0.4$, $P(B) = 0.3$, $P(C) = 0.5$, $P(A \cap B) = 0.1$, $P(A \cap C) = 0.15$, $P(B \cap C) = 0.1$, $P(A \cap B \cap C) = 0.05$. Find $P(A \cup B \cup C)$.

**Solution:**

$$P(A \cup B \cup C) = P(A) + P(B) + P(C) - P(A \cap B) - P(A \cap C) - P(B \cap C) + P(A \cap B \cap C)$$

$$= 0.4 + 0.3 + 0.5 - 0.1 - 0.15 - 0.1 + 0.05$$

$$= 1.2 - 0.35 + 0.05 = 0.90$$

---

### Exercise 8: Full Multi-Step Problem

**Problem:** In a group of 100 people, 60 own a car ($C$), 45 own a motorbike ($M$), and 20 own neither. Find: (a) the number who own both, (b) $P(C' \cap M')$, (c) $P(C' \cup M')$.

**Solution:**

**Step 1:** Number owning at least one = $100 - 20 = 80$, so $P(C \cup M) = 0.80$.

**Step 2:** Apply the addition rule to find $P(C \cap M)$:

$$P(C \cap M) = P(C) + P(M) - P(C \cup M)$$

$$P(C \cap M) = 0.60 + 0.45 - 0.80 = 0.25$$

Number owning both = $0.25 \times 100 = \mathbf{25}$.

**Step 3:** (b) "Neither" using De Morgan's First Law:

$$P(C' \cap M') = 1 - P(C \cup M) = 1 - 0.80 = 0.20$$

**Step 4:** (c) "Not both" using De Morgan's Second Law:

$$P(C' \cup M') = 1 - P(C \cap M) = 1 - 0.25 = 0.75$$

---

## 7. Core Formulas Summary

| Formula | Name | When to Use |
| :--- | :--- | :--- |
| $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ | Addition Rule | Finding union of any two events |
| $P(A') = 1 - P(A)$ | Complement Rule | Finding probability of "not A" |
| $(A \cup B)' = A' \cap B'$ | De Morgan's First Law | "Neither" problems |
| $(A \cap B)' = A' \cup B'$ | De Morgan's Second Law | "Not both" problems |
| $P(A' \cap B') = 1 - P(A \cup B)$ | Neither (derived) | Quickest path to "neither" |
| $P(A' \cup B') = 1 - P(A \cap B)$ | Not both (derived) | Quickest path to "not both" |

---

## Exam Tip: The De Morgan Shortcut

Whenever you see $P(A' \cap B')$ or $P(A' \cup B')$ in an exam, do not attempt to compute complements directly. Instead, apply De Morgan's Law immediately:

*   $P(A' \cap B') \xrightarrow{\text{De Morgan}} 1 - P(A \cup B)$: compute the union first, then subtract from 1.
*   $P(A' \cup B') \xrightarrow{\text{De Morgan}} 1 - P(A \cap B)$: compute the intersection first, then subtract from 1.

This two-step method is the fastest and most reliable approach and reduces complex complement expressions to standard addition rule problems.
