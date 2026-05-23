# Phase 2.1: Set Theory Fundamentals

Set Theory provides the mathematical language used to define and manipulate probability. Every probability problem is, at its core, a question about sets. Understanding the formal notation and operations is the foundation upon which all probability rules are built.

---

## 1. Core Definitions

### Sample Space ($\Omega$)

The **Sample Space** $\Omega$ (also written $S$) is the set of **all possible outcomes** of a random experiment. Every outcome that could conceivably occur must be listed exactly once.

$$\Omega = \{ \text{all possible outcomes} \}$$

**Key rule:** The sample space is always exhaustive (covers everything) and mutually exclusive (no outcome appears twice).

### Event

An **Event** is any subset of the sample space. It is a collection of one or more outcomes. We typically label events with capital letters $A$, $B$, $C$, etc.

$$A \subseteq \Omega$$

*   **Elementary event:** A single outcome, e.g., $\{3\}$ when rolling a die.
*   **Compound event:** A collection of outcomes, e.g., $\{2, 4, 6\}$ (rolling an even number).
*   **Impossible event ($\emptyset$):** The empty set. An event with no outcomes that can never occur.
*   **Certain event ($\Omega$):** The entire sample space. This event always occurs.

---

## 2. Set Operations

These three operations are the building blocks of all probability expressions.

### Union ($\cup$)

The union $A \cup B$ is the event that **at least one** of $A$ or $B$ occurs. It contains every outcome in $A$, every outcome in $B$, or both.

$$A \cup B = \{ \omega \in \Omega : \omega \in A \text{ or } \omega \in B \}$$

> Think of $\cup$ as the logical **OR**.

### Intersection ($\cap$)

The intersection $A \cap B$ is the event that **both** $A$ and $B$ occur simultaneously. It contains only outcomes that are in $A$ AND in $B$.

$$A \cap B = \{ \omega \in \Omega : \omega \in A \text{ and } \omega \in B \}$$

> Think of $\cap$ as the logical **AND**.

### Complement ($A'$ or $A^c$)

The complement $A'$ is the event that $A$ does **not** occur. It contains all outcomes in $\Omega$ that are not in $A$.

$$A' = \{ \omega \in \Omega : \omega \notin A \}$$

A fundamental identity:

$$A \cup A' = \Omega \quad \text{and} \quad A \cap A' = \emptyset$$

$$P(A') = 1 - P(A)$$

---

## 3. Mutual Exclusivity (Disjoint Events)

Two events $A$ and $B$ are **mutually exclusive** (or disjoint) if they cannot both occur at the same time:

$$A \cap B = \emptyset$$

This is a crucial property. When $A$ and $B$ are mutually exclusive, the addition rule simplifies significantly:

$$P(A \cup B) = P(A) + P(B) \quad \text{(only when } A \cap B = \emptyset \text{)}$$

---

## 4. Summary of Notation

| Notation | Read as | Meaning |
| :--- | :--- | :--- |
| $\Omega$ | Sample space | All possible outcomes |
| $\emptyset$ | Empty set | Impossible event |
| $A \cup B$ | A union B | A or B (at least one) |
| $A \cap B$ | A intersect B | A and B (both) |
| $A'$ | A complement | Not A |
| $A \subseteq B$ | A is a subset of B | Every outcome in A is also in B |
| $A \cap B = \emptyset$ | A and B are disjoint | A and B cannot both occur |

---

## 5. Solved Exercises

### Exercise 1: Identifying the Sample Space (Die Roll)

**Problem:** A fair six-sided die is rolled once. Define the sample space and the event $A$ = "rolling a number greater than 4".

**Solution:**

$$\Omega = \{1, 2, 3, 4, 5, 6\}$$

$$A = \{5, 6\}$$

$$A' = \{1, 2, 3, 4\} \quad \text{(not rolling greater than 4)}$$

---

### Exercise 2: Identifying the Sample Space (Two Coin Tosses)

**Problem:** Two coins are tossed. Write out $\Omega$ using ordered pairs where H = Heads, T = Tails. Define event $B$ = "at least one Head".

**Solution:**

$$\Omega = \{(H,H), (H,T), (T,H), (T,T)\}$$

$$B = \{(H,H), (H,T), (T,H)\}$$

$$B' = \{(T,T)\} \quad \text{(no heads, i.e., both tails)}$$

---

### Exercise 3: Computing Union and Intersection

**Problem:** From the die-roll sample space $\Omega = \{1,2,3,4,5,6\}$, let:
- $A$ = "even number" = $\{2, 4, 6\}$
- $B$ = "number greater than 3" = $\{4, 5, 6\}$

Find $A \cup B$ and $A \cap B$.

**Solution:**

$$A \cup B = \{2, 4, 5, 6\} \quad \text{(all outcomes in either A or B)}$$

$$A \cap B = \{4, 6\} \quad \text{(outcomes in both: even AND greater than 3)}$$

---

### Exercise 4: Computing the Complement

**Problem:** Using $A = \{2, 4, 6\}$ from Exercise 3, find $A'$ and verify the fundamental identity.

**Solution:**

$$A' = \{1, 3, 5\}$$

**Verification:**

$$A \cup A' = \{2,4,6\} \cup \{1,3,5\} = \{1,2,3,4,5,6\} = \Omega \checkmark$$

$$A \cap A' = \{2,4,6\} \cap \{1,3,5\} = \emptyset \checkmark$$

---

### Exercise 5: Mutually Exclusive Check

**Problem:** From the die-roll experiment, are $A$ = "rolling 1 or 2" and $B$ = "rolling 5 or 6" mutually exclusive?

**Solution:**

$$A = \{1, 2\}, \quad B = \{5, 6\}$$

$$A \cap B = \emptyset$$

Yes, $A$ and $B$ are mutually exclusive. Rolling a 1 or 2 and simultaneously rolling a 5 or 6 is impossible in a single roll.

---

### Exercise 6: Three Events - Union and Intersection

**Problem:** A card is drawn from a standard 52-card deck. Define:
- $A$ = "card is a Heart"
- $B$ = "card is a King"
- $C$ = "card is red"

Describe $A \cap B$, $A \cup B$, and $B \cap C'$.

**Solution:**

*   $A \cap B$ = "Heart AND King" = $\{K\heartsuit\}$ — exactly 1 card.
*   $A \cup B$ = "Heart OR King" = all 13 Hearts plus the 3 remaining Kings (of Clubs, Diamonds, Spades) = 16 cards.
*   $B \cap C'$ = "King AND NOT red" = King of black suits = $\{K\clubsuit, K\spadesuit\}$ — 2 cards.

---

### Exercise 7: Subset Relationship

**Problem:** A number is picked from $\{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\}$. Let:
- $A$ = "multiple of 4" = $\{4, 8\}$
- $B$ = "even number" = $\{2, 4, 6, 8, 10\}$

Is $A$ a subset of $B$? What does this imply?

**Solution:**

Every element of $A$ ($4$ and $8$) is also in $B$, so $A \subseteq B$.

This means: if event $A$ occurs, then event $B$ must also occur. Knowing a number is a multiple of 4 guarantees it is also even. Formally: $A \subseteq B \Rightarrow A \cap B = A$.

---

### Exercise 8: Complement of a Compound Event

**Problem:** Continuing from Exercise 7, find $(A \cup B)'$.

**Solution:**

First, compute the union:

$$A \cup B = \{2, 4, 6, 8, 10\} = B \quad \text{(since } A \subseteq B \text{)}$$

The full sample space is $\Omega = \{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\}$.

$$(A \cup B)' = B' = \{1, 3, 5, 7, 9\} \quad \text{(all odd numbers)}$$

This is the set of outcomes where neither event A nor event B occurs. This outcome connects directly to De Morgan's Law: $(A \cup B)' = A' \cap B'$, which will be covered in Phase 2.3.

---

## Exam Tip: Listing vs. Describing Events

In exam problems, you may be asked to either **list** the outcomes of an event (e.g., $A = \{2, 4, 6\}$) or **describe** it in words. Practise translating freely between both forms. The most common error is forgetting to account for overlapping outcomes when computing unions — always check whether an element appears in both sets before listing it.


# Phase 2.2: Venn Diagrams & Translating Worded Problems

Venn Diagrams are a visual tool that maps relationships between events onto overlapping circles. Their primary purpose in probability is to **translate English language problem descriptions into precise set notation**, which can then be evaluated using formulas. Mastering this translation is one of the highest-leverage skills for exams.

---

## 1. Standard Venn Diagram Layout

For two events $A$ and $B$ within a sample space $\Omega$, the diagram divides the space into four mutually exclusive regions:

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

| Region | Set Notation | Meaning |
| :--- | :--- | :--- |
| Left circle only | $A \cap B'$ | A occurs, B does not |
| Overlapping center | $A \cap B$ | Both A and B occur |
| Right circle only | $A' \cap B$ | B occurs, A does not |
| Outside both circles | $A' \cap B'$ | Neither A nor B occurs |

The **fundamental partition rule**: the four regions are mutually exclusive and collectively exhaustive. Their probabilities sum to 1.

$$P(A \cap B') + P(A \cap B) + P(A' \cap B) + P(A' \cap B') = 1$$

---

## 2. Translating Key Phrases into Set Notation

This table is the most important reference in this file. Memorise these translations.

| English Phrase | Set Notation | Notes |
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

## 3. Extending to Three Events

For three events $A$, $B$, $C$, the Venn Diagram has **8 mutually exclusive regions**. Key phrases extend naturally:

| Phrase | Set Notation |
| :--- | :--- |
| "All three occur" | $A \cap B \cap C$ |
| "At least one occurs" | $A \cup B \cup C$ |
| "None occur" | $A' \cap B' \cap C'$ = $(A \cup B \cup C)'$ |
| "Exactly one occurs" | $(A \cap B' \cap C') \cup (A' \cap B \cap C') \cup (A' \cap B' \cap C)$ |
| "At least two occur" | $(A \cap B \cap C') \cup (A \cap B' \cap C) \cup (A' \cap B \cap C) \cup (A \cap B \cap C)$ |

---

## 4. Reading Probabilities from a Filled Venn Diagram

When a Venn Diagram is given with numerical values already filled in, the values represent the probabilities (or counts) of each region. The key skill is to identify which regions belong to the event you are asked about, then sum them.

**Reading strategy:**
1. Identify all regions that satisfy the event description.
2. Sum the values in those regions.

---

## 5. Solved Exercises

### Exercise 1: Building a Venn Diagram from Counts

**Problem:** In a class of 50 students, 30 study Mathematics ($M$), 25 study Physics ($P$), and 15 study both. Find the number of students who study only Mathematics, only Physics, and neither subject.

**Solution:**

**Step 1:** Find the overlap region first.
$$|M \cap P| = 15$$

**Step 2:** Find "only Mathematics":
$$|M \cap P'| = |M| - |M \cap P| = 30 - 15 = 15$$

**Step 3:** Find "only Physics":
$$|M' \cap P| = |P| - |M \cap P| = 25 - 15 = 10$$

**Step 4:** Find "neither":
$$|M' \cap P'| = 50 - 15 - 15 - 10 = 10$$

**Filled Diagram regions:** Only M = 15, Both = 15, Only P = 10, Neither = 10. Total = 50. Verified.

---

### Exercise 2: Translating "At Least One"

**Problem:** $P(A) = 0.5$, $P(B) = 0.4$, $P(A \cap B) = 0.2$. Find the probability that at least one of $A$ or $B$ occurs.

**Solution:**

"At least one" translates to $A \cup B$.

$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

$$P(A \cup B) = 0.5 + 0.4 - 0.2 = 0.7$$

---

### Exercise 3: Translating "Neither"

**Problem:** Using the values from Exercise 2, find the probability that neither $A$ nor $B$ occurs.

**Solution:**

"Neither" translates to $A' \cap B' = (A \cup B)'$.

$$P((A \cup B)') = 1 - P(A \cup B) = 1 - 0.7 = 0.3$$

---

### Exercise 4: Translating "Exactly One"

**Problem:** Using the values from Exercise 2, find the probability that exactly one of $A$ or $B$ occurs.

**Solution:**

"Exactly one" = $(A \cap B') \cup (A' \cap B)$

**Method:** Total in at least one minus the overlap (where both occur):

$$P(\text{exactly one}) = P(A \cup B) - P(A \cap B)$$

$$P(\text{exactly one}) = 0.7 - 0.2 = 0.5$$

**Alternative breakdown:**
*   $P(A \cap B') = P(A) - P(A \cap B) = 0.5 - 0.2 = 0.3$
*   $P(A' \cap B) = P(B) - P(A \cap B) = 0.4 - 0.2 = 0.2$
*   $P(\text{exactly one}) = 0.3 + 0.2 = 0.5$ (same result)

---

### Exercise 5: Translating "Only A"

**Problem:** A survey shows $P(A) = 0.6$, $P(B) = 0.5$, $P(A \cup B) = 0.8$. Find $P(\text{only } A)$.

**Solution:**

**Step 1:** Find $P(A \cap B)$ using the addition rule:

$$P(A \cap B) = P(A) + P(B) - P(A \cup B) = 0.6 + 0.5 - 0.8 = 0.3$$

**Step 2:** "Only A" = $A \cap B'$:

$$P(A \cap B') = P(A) - P(A \cap B) = 0.6 - 0.3 = 0.3$$

---

### Exercise 6: Reading a Filled Venn Diagram

**Problem:** The regions of a Venn Diagram for events $A$ and $B$ are filled with the following probabilities:

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

### Exercise 7: Three Events - "None"

**Problem:** $P(A \cup B \cup C) = 0.85$. Find the probability that none of the three events occur.

**Solution:**

"None occur" = $(A \cup B \cup C)'$

$$P(A' \cap B' \cap C') = 1 - P(A \cup B \cup C) = 1 - 0.85 = 0.15$$

---

### Exercise 8: Backward Problem - Finding an Unknown

**Problem:** Given $P(A) = 0.45$, $P(B) = 0.30$, and $P(\text{exactly one of } A, B) = 0.55$. Find $P(A \cap B)$.

**Solution:**

"Exactly one" can be written as:

$$P(\text{exactly one}) = P(A) + P(B) - 2 \cdot P(A \cap B)$$

This is derived from:

$$P(\text{exactly one}) = [P(A) - P(A \cap B)] + [P(B) - P(A \cap B)]$$

Substituting known values:

$$0.55 = 0.45 + 0.30 - 2 \cdot P(A \cap B)$$

$$0.55 = 0.75 - 2 \cdot P(A \cap B)$$

$$P(A \cap B) = \frac{0.75 - 0.55}{2} = \frac{0.20}{2} = 0.10$$

---

## Exam Tip: The Four-Region Decomposition

**Always decompose** a Venn Diagram into its four mutually exclusive regions at the start of a problem:

$$P(A \cap B'), \quad P(A \cap B), \quad P(A' \cap B), \quad P(A' \cap B')$$

Once these four values are known, **any probability expression** involving $A$ and $B$ can be computed by summing the appropriate regions. This method is infallible and prevents double-counting errors.


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


# Phase 2.4: Combinatorics and Counting Methods

Combinatorial analysis provides the mathematical techniques for counting the number of elements in a set without listing them individually. In probability theory, when outcomes in a sample space $\Omega$ are equally likely, the probability of an event $A$ is:

$$P(A) = \frac{|A|}{|\Omega|} = \frac{\text{Number of favorable outcomes}}{\text{Total number of possible outcomes}}$$

Determining $|A|$ and $|\Omega|$ often requires the counting methods detailed below.

---

## 1. Fundamental Principles of Counting

### 1.1 The Multiplication Rule (Product Rule)
If an operation can be performed in $n_1$ ways, and for each of these a second operation can be performed in $n_2$ ways, and for each of these a third operation can be performed in $n_3$ ways, and so on, then the sequence of $k$ operations can be performed in:

$$N = n_1 \cdot n_2 \cdot \dots \cdot n_k \text{ ways}$$

### 1.2 The Addition Rule (Sum Rule)
If an operation can be performed in $n_1$ ways, and a second disjoint operation can be performed in $n_2$ ways, then the total number of ways to perform either the first or the second operation is:

$$N = n_1 + n_2 \text{ ways}$$

---

## 2. Permutations

A permutation is an ordered arrangement of all or part of a set of objects. The order of selection matters.

### 2.1 Permutations of Distinct Objects
The number of permutations of $n$ distinct objects taken all at a time is:

$$P(n, n) = n!$$

The number of permutations of $n$ distinct objects taken $r$ at a time (where $0 \le r \le n$) is:

$$P(n, r) = \frac{n!}{(n-r)!}$$

### 2.2 Permutations with Repetition (Identical Objects)
The number of distinct permutations of $n$ objects of which $n_1$ are of one type, $n_2$ are of a second type, $\dots$, and $n_k$ are of a $k$-th type (such that $n_1 + n_2 + \dots + n_k = n$) is:

$$P(n; n_1, n_2, \dots, n_k) = \frac{n!}{n_1! \cdot n_2! \dots n_k!}$$

---

## 3. Combinations

A combination is a selection of all or part of a set of objects without regard to order. The order of selection does not matter.

### 3.1 Combinations of Distinct Objects (Without Replacement)
The number of combinations of $n$ distinct objects taken $r$ at a time (where $0 \le r \le n$) is given by the binomial coefficient:

$$C(n, r) = \binom{n}{r} = \frac{n!}{r!(n-r)!}$$

### 3.2 Combinations with Replacement
The number of ways to choose $r$ objects from a set of $n$ distinct objects when repetition is allowed (and order does not matter) is:

$$C^{R}(n, r) = \binom{n + r - 1}{r} = \frac{(n + r - 1)!}{r!(n - 1)!}$$

---

## 4. Partitions & Multinomial Coefficients

The number of ways of partitioning a set of $n$ distinct objects into $k$ cells with $r_1$ objects in the first cell, $r_2$ objects in the second cell, and so on, where $r_1 + r_2 + \dots + r_k = n$, is:

$$\binom{n}{r_1, r_2, \dots, r_k} = \frac{n!}{r_1! \cdot r_2! \dots r_k!}$$

---

## 5. Solved Exercises (10 Examples)

### Exercise 1: License Plate Codes (Multiplication Rule)
**Problem:** A license plate contains 3 letters followed by 3 digits. Letters cannot be repeated, but digits can. How many distinct license plates can be formed if there are 26 letters in the alphabet?

**Solution:**
- **Step 1: Define operations.**
  We have 6 slots to fill. Let $n_i$ represent the number of choices for slot $i$.
- **Step 2: WIP State.**
  For letters (no repetition):
  - Slot 1: 26 choices
  - Slot 2: 25 choices
  - Slot 3: 24 choices
  For digits (repetition allowed):
  - Slot 4: 10 choices (0-9)
  - Slot 5: 10 choices
  - Slot 6: ? choices
- **Step 3: Final Calculation.**
  - Slot 6 has 10 choices.
  - Total plates $= 26 \cdot 25 \cdot 24 \cdot 10 \cdot 10 \cdot 10 = 15,600 \cdot 1,000 = 15,600,000$.

---

### Exercise 2: Selecting a Committee (Combinations)
**Problem:** From a group of 8 men and 6 women, a committee of 5 people must be formed. How many committees are possible if it must contain exactly 3 men and 2 women?

**Solution:**
- **Step 1: Split the selections.**
  We select men and women independently, then multiply the results.
- **Step 2: WIP State.**
  - Selection of men: $\binom{8}{3} = \frac{8!}{3! \cdot 5!} = \frac{8 \cdot 7 \cdot 6}{3 \cdot 2 \cdot 1} = 56$.
  - Selection of women: $\binom{6}{2} = \frac{6!}{2! \cdot 4!} = \frac{6 \cdot 5}{?} = 15$.
- **Step 3: Final Calculation.**
  Total committees $= 56 \cdot 15 = 840$.

---

### Exercise 3: Arranging Books on a Shelf (Permutations)
**Problem:** There are 4 Math books, 3 Physics books, and 2 Chemistry books. In how many ways can they be arranged on a shelf if books of the same subject must be kept together?

**Solution:**
- **Step 1: Treat groups as units.**
  We arrange the 3 subjects (Math, Physics, Chemistry) first: $3!$ ways.
- **Step 2: WIP State.**
  Within each subject group:
  - Math books can be arranged in $4!$ ways.
  - Physics books can be arranged in $3!$ ways.
  - Chemistry books can be arranged in ? ways.
- **Step 3: Final Calculation.**
  - Chemistry arrangements $= 2! = 2$ ways.
  - Total arrangements $= 3! \cdot (4! \cdot 3! \cdot 2!) = 6 \cdot (24 \cdot 6 \cdot 2) = 6 \cdot 288 = 1728$.

---

### Exercise 4: Distributing Toys (Multinomial Coefficient)
**Problem:** In how many ways can 10 distinct toys be distributed among 3 children if the eldest receives 5 toys, the middle child receives 3 toys, and the youngest receives 2 toys?

**Solution:**
- **Step 1: Set up the partition.**
  This is a partition of $n=10$ objects into cells of sizes $r_1=5, r_2=3, r_3=2$.
- **Step 2: WIP State.**
  $$\binom{10}{5, 3, 2} = \frac{10!}{5! \cdot 3! \cdot 2!} = \frac{10 \cdot 9 \cdot 8 \cdot 7 \cdot 6 \cdot 5!}{5! \cdot (3 \cdot 2 \cdot 1) \cdot (2 \cdot 1)} = \frac{10 \cdot 9 \cdot 8 \cdot 7 \cdot 6}{?}$$
- **Step 3: Final Calculation.**
  $$\text{Denominator} = 6 \cdot 2 = 12$$
  $$\text{Numerator} = 30240$$
  $$\text{Total ways} = \frac{30240}{12} = 2520 \text{ ways}.$$

---

### Exercise 5: Word Permutations with Repetition
**Problem:** How many distinct words (including nonsense words) can be formed by rearranging the letters of the word "PROBABILITY"?

**Solution:**
- **Step 1: Count letter frequencies.**
  Total letters $n = 11$.
  Frequencies: P (1), R (1), O (1), B (2), A (1), I (2), L (1), T (1), Y (1).
- **Step 2: WIP State.**
  We apply the permutation of identical objects formula:
  $$\text{Total permutations} = \frac{11!}{1! \cdot 1! \cdot 1! \cdot 2! \cdot 1! \cdot 2! \cdot 1! \cdot 1! \cdot 1!} = \frac{11!}{2! \cdot 2!} = \frac{39,916,800}{?}$$
- **Step 3: Final Calculation.**
  $$\text{Total permutations} = \frac{39,916,800}{4} = 9,979,200 \text{ words}.$$

---

### Exercise 6: Seating Arrangements at a Round Table
**Problem:** In how many ways can 6 people be seated at a round table? (Note: Two arrangements are considered identical if each person has the same left and right neighbors).

**Solution:**
- **Step 1: Identify circular permutation.**
  For circular permutations of $n$ distinct objects, we fix one person's position to eliminate rotational equivalence, leaving $(n-1)!$ arrangements.
- **Step 2: WIP State.**
  $$\text{Arrangements} = (6 - 1)! = ?!$$
- **Step 3: Final Calculation.**
  $$5! = 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1 = 120 \text{ ways}.$$

---

### Exercise 7: Choosing Donuts (Combinations with Replacement)
**Problem:** A bakery sells 4 varieties of donuts. In how many ways can a customer select 6 donuts?

**Solution:**
- **Step 1: Identify model parameters.**
  We are selecting $r = 6$ donuts from $n = 4$ types, where order does not matter and repetition is allowed.
- **Step 2: WIP State.**
  Use the combination with replacement formula:
  $$\binom{n + r - 1}{r} = \binom{4 + 6 - 1}{6} = \binom{9}{6} = \frac{9!}{6! \cdot 3!} = \frac{9 \cdot 8 \cdot 7}{?}$$
- **Step 3: Final Calculation.**
  $$\text{Denominator} = 3 \cdot 2 \cdot 1 = 6$$
  $$\text{Total ways} = \frac{504}{6} = 84 \text{ ways}.$$

---

### Exercise 8: Pathfinding on a Grid
**Problem:** A grid has coordinates from $(0,0)$ to $(5,4)$. A path moves only step-by-step to the right or up. How many paths exist from $(0,0)$ to $(5,4)$?

**Solution:**
- **Step 1: Translate to symbols.**
  Any path requires exactly 5 Right (R) moves and 4 Up (U) moves, totaling $n = 9$ moves.
- **Step 2: WIP State.**
  We need to choose which 5 of the 9 moves are R (the rest will be U):
  $$\text{Paths} = \binom{9}{5} = \frac{9!}{5! \cdot 4!} = \frac{9 \cdot 8 \cdot 7 \cdot 6}{?}$$
- **Step 3: Final Calculation.**
  $$\text{Denominator} = 4 \cdot 3 \cdot 2 \cdot 1 = 24$$
  $$\text{Total paths} = \frac{3024}{24} = 126 \text{ paths}.$$

---

### Exercise 9: Sum of Dice (Combinatorics for Probability)
**Problem:** Three fair six-sided dice are rolled. What is the probability that the sum of the numbers shown is exactly 5?

**Solution:**
- **Step 1: Calculate the size of the sample space $|\Omega|$.**
  Each die has 6 outcomes. For 3 dice: $|\Omega| = 6^3 = 216$.
- **Step 2: WIP State.**
  We count the combinations of $(x_1, x_2, x_3)$ such that $x_1 + x_2 + x_3 = 5$, where $1 \le x_i \le 6$.
  Possible partitions of 5 into 3 positive integers:
  - $\{3, 1, 1\}$ (order matters): can occur as $(3,1,1)$, $(1,3,1)$, or $(1,1,3)$ $\Rightarrow$ 3 ways.
  - $\{2, 2, 1\}$ (order matters): can occur as $(2,2,1)$, $(2,1,2)$, or $(1,2,2)$ $\Rightarrow$ ? ways.
- **Step 3: Final Calculation.**
  - There are 3 ways for $\{2, 2, 1\}$.
  - Total favorable outcomes $|A| = 3 + 3 = 6$.
  - Probability $= \frac{|A|}{|\Omega|} = \frac{6}{216} = \frac{1}{36} \approx 0.0278$.

---

### Exercise 10: Standard Poker Hands (Combination)
**Problem:** A standard poker deck has 52 cards. What is the probability of being dealt a "Four of a Kind" (4 cards of one rank, and 1 card of another rank) in a 5-card hand?

**Solution:**
- **Step 1: Compute total hands.**
  $$|\Omega| = \binom{52}{5} = 2,598,960$$
- **Step 2: WIP State.**
  To get a Four of a Kind:
  1. Choose the rank of the four cards: $\binom{13}{1} = 13$ ways.
  2. Select all 4 cards of that rank: $\binom{4}{4} = 1$ way.
  3. Choose the remaining card from the remaining cards: $\binom{48}{1} = ?$ ways.
- **Step 3: Final Calculation.**
  - $\binom{48}{1} = 48$ ways.
  - Total favorable hands $|A| = 13 \cdot 1 \cdot 48 = 624$.
  - Probability $= \frac{624}{2,598,960} \approx 0.00024$.
