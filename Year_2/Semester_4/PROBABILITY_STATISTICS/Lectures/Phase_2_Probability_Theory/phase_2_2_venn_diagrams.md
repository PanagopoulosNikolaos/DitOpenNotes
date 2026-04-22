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
