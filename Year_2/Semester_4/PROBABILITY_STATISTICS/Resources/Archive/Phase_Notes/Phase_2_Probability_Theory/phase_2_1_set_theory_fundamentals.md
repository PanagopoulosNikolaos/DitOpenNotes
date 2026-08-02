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
