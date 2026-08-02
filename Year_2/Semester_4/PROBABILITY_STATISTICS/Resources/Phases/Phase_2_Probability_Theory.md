# Phase 2: Probability Theory

## Table of Contents
1. [Core Definitions & Set Operations](#1-core-definitions--set-operations)
2. [Venn Diagrams & Translating Worded Problems](#2-venn-diagrams--translating-worded-problems)
3. [Probability Axioms & Rules](#3-probability-axioms--rules)
4. [Combinatorics and Counting Methods](#4-combinatorics-and-counting-methods)
5. [Time-Specific Gotchas](#5-time-specific-gotchas)
6. [Solved Exercises](#6-solved-exercises)
7. [Phase Summary](#7-phase-summary)

---

## 1. Core Definitions & Set Operations

Set Theory provides the mathematical language used to define and manipulate probability. Every probability problem is, at its core, a question about sets.

### Sample Space ($\Omega$)
The **Sample Space** $\Omega$ (also written $S$) is the set of **all possible outcomes** of a random experiment. Every outcome that could conceivably occur must be listed exactly once.
- **Standard Example:** $\Omega = \{1, 2, 3, 4, 5, 6\}$ (rolling a die).
- **Time Context Example:** $\Omega = [0, 5]\text{ s}$ (response time of a server, a continuous sample space).

**Key rule:** The sample space is always exhaustive (covers everything) and mutually exclusive (no outcome appears twice).

### Event
An **Event** is any subset of the sample space. It is a collection of one or more outcomes. We typically label events with capital letters $A$, $B$, $C$, etc.
$$A \subseteq \Omega$$
- **Elementary event:** A single outcome, e.g., $\{3\}$ when rolling a die, or $\{1.5\text{ s}\}$ for a specific response time.
- **Compound event:** A collection of outcomes, e.g., $\{2, 4, 6\}$ (even number), or $\{t : 1\text{ s} \le t < 2\text{ s}\}$.
- **Impossible event ($\emptyset$):** The empty set. An event with no outcomes.
- **Certain event ($\Omega$):** The entire sample space.

### Set Operations

These operations are the building blocks of all probability expressions.

#### Union ($\cup$)
The union $A \cup B$ is the event that **at least one** of $A$ or $B$ occurs.
$$A \cup B = \{ \omega \in \Omega : \omega \in A \text{ or } \omega \in B \}$$
> Think of $\cup$ as the logical **OR**.

#### Intersection ($\cap$)
The intersection $A \cap B$ is the event that **both** $A$ and $B$ occur simultaneously.
$$A \cap B = \{ \omega \in \Omega : \omega \in A \text{ and } \omega \in B \}$$
> Think of $\cap$ as the logical **AND**.

#### Complement ($A'$ or $A^c$)
The complement $A'$ is the event that $A$ does **not** occur.
$$A' = \{ \omega \in \Omega : \omega \notin A \}$$

A fundamental identity:
$$A \cup A' = \Omega \quad \text{and} \quad A \cap A' = \emptyset$$
$$P(A') = 1 - P(A)$$

### Mutual Exclusivity (Disjoint Events)
Two events $A$ and $B$ are **mutually exclusive** (or disjoint) if they cannot both occur at the same time:
$$A \cap B = \emptyset$$
When $A$ and $B$ are mutually exclusive, the addition rule simplifies:
$$P(A \cup B) = P(A) + P(B) \quad \text{(only when } A \cap B = \emptyset \text{)}$$

---

## 2. Venn Diagrams & Translating Worded Problems

Venn Diagrams are a visual tool that maps relationships between events onto overlapping circles. They **translate English language problem descriptions into precise set notation**.

### Standard Venn Diagram Layout

For two events $A$ and $B$ within a sample space $\Omega$, the diagram divides the space into four mutually exclusive regions:

| Region | Set Notation | Meaning | Time Meaning |
| :--- | :--- | :--- | :--- |
| Left circle only | $A \cap B'$ | A occurs, B does not | A occurs, B does not |
| Overlapping center | $A \cap B$ | Both A and B occur | Both A and B occur |
| Right circle only | $A' \cap B$ | B occurs, A does not | B occurs, A does not |
| Outside both circles | $A' \cap B'$ | Neither A nor B occurs | Neither A nor B occurs |

The **fundamental partition rule**: the four regions are mutually exclusive and collectively exhaustive. Their probabilities sum to 1.
$$P(A \cap B') + P(A \cap B) + P(A' \cap B) + P(A' \cap B') = 1$$

### Translating Key Phrases into Set Notation

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
| "At most one of A, B" | $(A \cap B)'$ = $A' \cup B'$ | Not both simultaneously |

> **Critical insight:** "At least one" means $A \cup B$. "Exactly one" means $A \cup B$ minus the case where both occur, i.e., $(A \cup B) \setminus (A \cap B)$.

### Extending to Three Events

For three events $A$, $B$, $C$, the Venn Diagram has **8 mutually exclusive regions**.
- **All three occur:** $A \cap B \cap C$
- **At least one occurs:** $A \cup B \cup C$
- **None occur:** $A' \cap B' \cap C' = (A \cup B \cup C)'$

---

## 3. Probability Axioms & Rules

The **Probability Axioms** (Kolmogorov's Axioms) are the three foundational rules from which all of probability theory is derived.

### Kolmogorov's Axioms

**Axiom 1 (Non-negativity):**
$$P(A) \geq 0$$

**Axiom 2 (Normalization):**
$$P(\Omega) = 1$$

**Axiom 3 (Countable Additivity):**
If $A$ and $B$ are mutually exclusive ($A \cap B = \emptyset$):
$$P(A \cup B) = P(A) + P(B)$$

### The Addition Rule (General)

For any two events $A$ and $B$ (not necessarily mutually exclusive):
$$\boxed{P(A \cup B) = P(A) + P(B) - P(A \cap B)}$$

**Extension to three events (Inclusion-Exclusion Principle):**
$$P(A \cup B \cup C) = P(A) + P(B) + P(C) - P(A \cap B) - P(A \cap C) - P(B \cap C) + P(A \cap B \cap C)$$

### De Morgan's Laws

De Morgan's Laws describe the complement of a union or intersection. They "push the complement inside" while swapping the operator between $\cup$ and $\cap$.

**First Law:**
$$\boxed{(A \cup B)' = A' \cap B'}$$
$$P((A \cup B)') = P(A' \cap B')$$
(Reading: "NOT (A or B)" is the same as "(NOT A) AND (NOT B)". Neither event occurs.)

**Second Law:**
$$\boxed{(A \cap B)' = A' \cup B'}$$
$$P((A \cap B)') = P(A' \cup B')$$
(Reading: "NOT (A and B)" is the same as "(NOT A) OR (NOT B)". At least one event fails to occur.)

---

## 4. Combinatorics and Counting Methods

When outcomes in a sample space $\Omega$ are equally likely, the probability of an event $A$ is:
$$P(A) = \frac{|A|}{|\Omega|}$$

### Fundamental Principles of Counting
- **Multiplication Rule (Product Rule):** Sequence of operations. $N = n_1 \cdot n_2 \cdot \dots \cdot n_k$
- **Addition Rule (Sum Rule):** Disjoint operations. $N = n_1 + n_2$

### Permutations
An ordered arrangement. The order of selection matters.
- **Distinct Objects:** $P(n, r) = \frac{n!}{(n-r)!}$
- **With Repetition (Identical Objects):** $P(n; n_1, \dots, n_k) = \frac{n!}{n_1! \dots n_k!}$
- **Circular Permutations:** $(n - 1)!$

### Combinations
A selection without regard to order.
- **Distinct Objects (Without Replacement):** $C(n, r) = \binom{n}{r} = \frac{n!}{r!(n-r)!}$
- **With Replacement:** $C^{R}(n, r) = \binom{n + r - 1}{r} = \frac{(n + r - 1)!}{r!(n - 1)!}$

### Partitions & Multinomial Coefficients
Partition $n$ distinct objects into $k$ groups of sizes $r_1, r_2, \ldots, r_k$:
$$\binom{n}{r_1, r_2, \dots, r_k} = \frac{n!}{r_1! \cdot r_2! \dots r_k!}$$

---

## 5. Time-Specific Gotchas

When dealing with time-based sample spaces, several specific rules apply:

1. **Continuous vs. Discrete Time:** Time can be continuous ($\Omega = [0, T]$) or discrete ($\Omega = \{t_1, t_2\}$). Boundaries matter in discrete time, but the probability of an exact boundary point in continuous time is $0$ (i.e., $P(T = t_0) = 0$).
2. **Overlapping Time Intervals:** For $A = [0, 100)\text{ ms}$ and $B = [50, 150)\text{ ms}$, the overlap $A \cap B = [50, 100)\text{ ms}$ is non-empty. They are not mutually exclusive.
3. **Cyclic Time (Wrap-Around):** On a 24-hour clock, an event like "between 22:00 and 02:00" wraps around midnight and forms a union of two intervals: $A = [22, 24) \cup [0, 2)$.
4. **Mutually Exclusive Time Events Are Maximally Dependent:** If $A$ = "response $< 50\text{ ms}$" and $B$ = "response $> 200\text{ ms}$", they are mutually exclusive. Knowing $A$ occurred means $B$ definitely did not. They are not independent.
5. **Time Slots are Labeled:** 9:00 is not identical to 10:00. Combinatorially, they are distinct objects.

---

## 6. Solved Exercises

#### Exercise 1: Identifying the Sample Space (Die Roll)
**Problem:** A fair six-sided die is rolled once. Define the sample space and the event $A$ = "rolling a number greater than 4".
**Solution:**
$$\Omega = \{1, 2, 3, 4, 5, 6\}$$
$$A = \{5, 6\}$$
$$A' = \{1, 2, 3, 4\} \quad \text{(not rolling greater than 4)}$$

#### Exercise 2: Identifying the Sample Space (Response Time)
**Problem:** A server responds to a request in at most 5 seconds. The response time $T$ is measured. Define the sample space and the event $A$ = "response time greater than 3 seconds".
**Solution:**
$$\Omega = [0, 5]\text{ s}$$
$$A = (3, 5]\text{ s}$$
$$A' = [0, 3]\text{ s} \quad \text{(response time at most 3 seconds)}$$

#### Exercise 3: Identifying the Sample Space (Two Time Slots)
**Problem:** A task is scheduled in one of two time slots: Morning (M) or Afternoon (A). Write out $\Omega$ using ordered pairs where the first element is the first task's slot and the second is the second task's slot. Define event $B$ = "at least one task is in the Morning".
**Solution:**
$$\Omega = \{(M,M), (M,A), (A,M), (A,A)\}$$
$$B = \{(M,M), (M,A), (A,M)\}$$
$$B' = \{(A,A)\} \quad \text{(both tasks in the Afternoon)}$$

#### Exercise 4: Computing Union and Intersection of Time Events
**Problem:** From the response-time sample space $\Omega = [0, 10]\text{ s}$, let:
- $A$ = "response time less than 4 seconds" = $[0, 4)\text{ s}$
- $B$ = "response time greater than 3 seconds" = $(3, 10]\text{ s}$
Find $A \cup B$ and $A \cap B$.
**Solution:**
$$A \cup B = [0, 10]\text{ s} = \Omega \quad \text{(every response time is either < 4 or > 3)}$$
$$A \cap B = (3, 4)\text{ s} \quad \text{(response times between 3 and 4 seconds)}$$
> **Note:** $A$ and $B$ are **not** mutually exclusive because $A \cap B = (3, 4)\text{ s} \neq \emptyset$.

#### Exercise 5: Computing the Complement of a Time Event
**Problem:** Using $A = [0, 4)\text{ s}$ from Exercise 4, find $A'$ and verify the fundamental identity.
**Solution:**
$$A' = [4, 10]\text{ s}$$
**Verification:**
$$A \cup A' = [0, 4) \cup [4, 10] = [0, 10] = \Omega \checkmark$$
$$A \cap A' = [0, 4) \cap [4, 10] = \emptyset \checkmark$$

#### Exercise 6: Mutually Exclusive Time Events
**Problem:** A request can be classified by response time category: $A$ = "fast ($< 50\text{ ms}$)" and $B$ = "slow ($> 200\text{ ms}$)". Are $A$ and $B$ mutually exclusive?
**Solution:**
$$A = [0, 50)\text{ ms}, \quad B = (200, \infty)\text{ ms}$$
$$A \cap B = \emptyset$$
Yes, $A$ and $B$ are mutually exclusive. A single response cannot be both fast and slow simultaneously.

#### Exercise 7: Three Time Events - Union and Intersection
**Problem:** A request is monitored across three time thresholds. Define:
- $A$ = "response time $< 100\text{ ms}$"
- $B$ = "response time $> 50\text{ ms}$"
- $C$ = "response time $< 200\text{ ms}$"
With $\Omega = [0, 500]\text{ ms}$, describe $A \cap B$, $A \cup C$, and $B \cap C'$.
**Solution:**
*   $A \cap B$ = $(50, 100)\text{ ms}$.
*   $A \cup C$ = $[0, 200)\text{ ms}$ (since $A \subseteq C$, the union is just $C$).
*   $C'$ = $[200, 500]\text{ ms}$.
*   $B \cap C'$ = $[200, 500]\text{ ms}$.

#### Exercise 8: Subset Relationship for Time Events
**Problem:** A response time $T$ is measured in $\Omega = [0, 10]\text{ s}$. Let:
- $A$ = "response time $< 1\text{ s}$" = $[0, 1)\text{ s}$
- $B$ = "response time $< 5\text{ s}$" = $[0, 5)\text{ s}$
Is $A$ a subset of $B$? What does this imply?
**Solution:**
Every time value in $A$ ($0 \le t < 1$) is also in $B$ ($0 \le t < 5$), so $A \subseteq B$.
This means: if event $A$ occurs, then event $B$ must also occur. Formally: $A \subseteq B \Rightarrow A \cap B = A$.

#### Exercise 9: Cyclic Time Event (Wrap-Around Midnight)
**Problem:** A maintenance window is defined as "between 22:00 and 02:00" on a 24-hour clock. Express this event as a set on $\Omega = [0, 24)\text{ h}$.
**Solution:**
The event wraps around midnight, so it is a **union of two intervals**:
$$A = [22, 24) \cup [0, 2) \text{ (hours)}$$
The complement (no maintenance) is:
$$A' = [2, 22) \text{ (hours)}$$

#### Exercise 10: Building a Venn Diagram from Time-Based Counts
**Problem:** In a sample of 50 requests, 30 had response time $< 100\text{ ms}$ ($F$), 25 arrived during peak hours ($P$), and 15 were both fast and during peak. Find the number of requests that were only fast, only during peak, and neither.
**Solution:**
**Step 1:** Find the overlap region first: $|F \cap P| = 15$
**Step 2:** Find "only fast": $|F \cap P'| = |F| - |F \cap P| = 30 - 15 = 15$
**Step 3:** Find "only peak": $|F' \cap P| = |P| - |F \cap P| = 25 - 15 = 10$
**Step 4:** Find "neither": $|F' \cap P'| = 50 - 15 - 15 - 10 = 10$

#### Exercise 11: Translating "At Least One" (Time Events)
**Problem:** $P(A) = 0.5$ (request timed out), $P(B) = 0.4$ (request retried), $P(A \cap B) = 0.2$ (timed out and retried). Find the probability that at least one of $A$ or $B$ occurs.
**Solution:**
"At least one" translates to $A \cup B$.
$$P(A \cup B) = P(A) + P(B) - P(A \cap B) = 0.5 + 0.4 - 0.2 = 0.7$$

#### Exercise 12: Translating "Neither" (Time Events)
**Problem:** Using the values from Exercise 11, find the probability that neither $A$ nor $B$ occurs.
**Solution:**
"Neither" translates to $A' \cap B' = (A \cup B)'$.
$$P((A \cup B)') = 1 - P(A \cup B) = 1 - 0.7 = 0.3$$

#### Exercise 13: Translating "Exactly One" (Time Events)
**Problem:** Using the values from Exercise 11, find the probability that exactly one of $A$ or $B$ occurs.
**Solution:**
"Exactly one" = $(A \cap B') \cup (A' \cap B)$.
$$P(\text{exactly one}) = P(A \cup B) - P(A \cap B) = 0.7 - 0.2 = 0.5$$

#### Exercise 14: Translating "Only A" (Time Events)
**Problem:** $P(A) = 0.6$ (slow response), $P(B) = 0.5$ (high CPU load), $P(A \cup B) = 0.8$. Find $P(\text{only } A)$.
**Solution:**
**Step 1:** $P(A \cap B) = P(A) + P(B) - P(A \cup B) = 0.6 + 0.5 - 0.8 = 0.3$
**Step 2:** $P(A \cap B') = P(A) - P(A \cap B) = 0.6 - 0.3 = 0.3$

#### Exercise 15: Backward Problem - Finding an Unknown (Time Events)
**Problem:** Given $P(A) = 0.45$, $P(B) = 0.30$, and $P(\text{exactly one of } A, B) = 0.55$. Find $P(A \cap B)$.
**Solution:**
$$P(\text{exactly one}) = P(A) + P(B) - 2 \cdot P(A \cap B)$$
$$0.55 = 0.45 + 0.30 - 2 \cdot P(A \cap B)$$
$$2 \cdot P(A \cap B) = 0.75 - 0.55 = 0.20 \implies P(A \cap B) = 0.10$$

#### Exercise 16: Applying De Morgan's Laws (Time Events)
**Problem:** $P(A) = 0.5$ (timeout), $P(B) = 0.4$ (retry), $P(A \cap B) = 0.2$ (both). Find $P(A' \cap B')$ and $P(A' \cup B')$.
**Solution:**
**Step 1:** $P(A \cup B) = 0.5 + 0.4 - 0.2 = 0.7$
**Step 2 (De Morgan's First Law):** $P(A' \cap B') = P((A \cup B)') = 1 - 0.7 = 0.3$
**Step 3 (De Morgan's Second Law):** $P(A' \cup B') = P((A \cap B)') = 1 - 0.2 = 0.8$

#### Exercise 17: Mutually Exclusive Time Events
**Problem:** Two time events $A$ and $B$ are mutually exclusive. $P(A) = 0.35$, $P(B) = 0.25$. Find $P(A \cup B)$ and $P(A' \cap B')$.
**Solution:**
Since $A \cap B = \emptyset$, $P(A \cap B) = 0$.
$P(A \cup B) = 0.35 + 0.25 = 0.60$
$P(A' \cap B') = 1 - 0.60 = 0.40$

#### Exercise 18: Checking Axiom Compliance (Time Events)
**Problem:** A student claims: $P(A) = 0.7$, $P(B) = 0.6$, $P(A \cup B) = 0.8$. Is this consistent with the probability axioms?
**Solution:**
$P(A \cap B) = 0.7 + 0.6 - 0.8 = 0.5$.
Check 1: $0.5 \ge 0$.
Check 2: $0.5 \le 0.7$ and $0.5 \le 0.6$.
Check 3: $0.8 \le 1$.
All axioms satisfied. The assignment is consistent.

#### Exercise 19: Full Multi-Step Problem (Time Events)
**Problem:** In a group of 100 requests, 60 had response time $< 100\text{ ms}$ ($F$), 45 arrived during peak hours ($P$), and 20 were neither. Find: (a) number both fast and during peak, (b) $P(F' \cup P')$.
**Solution:**
**Step 1:** $P(F \cup P) = 0.80$ (since 20 were neither).
**Step 2:** $P(F \cap P) = 0.60 + 0.45 - 0.80 = 0.25 \implies 25\text{ requests}$.
**Step 3:** $P(F' \cup P') = 1 - P(F \cap P) = 1 - 0.25 = 0.75$.

#### Exercise 20: License Plate Codes (Multiplication Rule)
**Problem:** A license plate contains 3 letters followed by 3 digits. Letters cannot be repeated, but digits can. How many distinct plates?
**Solution:**
Letters: $26 \cdot 25 \cdot 24$ choices.
Digits: $10 \cdot 10 \cdot 10$ choices.
Total $= 26 \cdot 25 \cdot 24 \cdot 10 \cdot 10 \cdot 10 = 15,600,000$.

#### Exercise 21: Arranging Tasks in a Timeline (Permutations)
**Problem:** There are 4 monitoring tasks, 3 backup tasks, and 2 cleanup tasks. In how many ways can they be arranged in a 9-slot timeline if tasks of the same type must be consecutive?
**Solution:**
Arrange 3 task types: $3! = 6$ ways.
Arrange within types: $4! \cdot 3! \cdot 2! = 24 \cdot 6 \cdot 2 = 288$ ways.
Total $= 6 \cdot 288 = 1728$ ways.

#### Exercise 22: Selecting Time Slots for Maintenance (Combinations)
**Problem:** From 8 available hourly time slots, choose 3 slots for maintenance. How many ways?
**Solution:**
Order does not matter.
$$\binom{8}{3} = \frac{8!}{3! \cdot 5!} = \frac{8 \cdot 7 \cdot 6}{3 \cdot 2 \cdot 1} = 56 \text{ ways.}$$

#### Exercise 23: Distributing Time Slots Among Servers (Multinomial)
**Problem:** In how many ways can 10 distinct time slots be distributed among 3 servers if server A receives 5, B receives 3, and C receives 2?
**Solution:**
$$\binom{10}{5, 3, 2} = \frac{10!}{5! \cdot 3! \cdot 2!} = 2520 \text{ ways.}$$

#### Exercise 24: Circular Scheduling (Round-the-Clock Shifts)
**Problem:** In how many ways can 6 servers be arranged in a circular 24-hour shift rotation?
**Solution:**
For circular permutations: $(n-1)!$
$(6 - 1)! = 5! = 120 \text{ ways.}$

#### Exercise 25: Standard Poker Hands (Combination)
**Problem:** Probability of being dealt a "Four of a Kind" (4 cards of one rank, 1 card of another) in a 5-card hand from a 52-card deck?
**Solution:**
$$|\Omega| = \binom{52}{5} = 2,598,960$$
Favorable: $\binom{13}{1}$ for rank, $\binom{4}{4}$ for cards of rank, $\binom{48}{1}$ for last card.
$$|A| = 13 \cdot 1 \cdot 48 = 624$$
$$P = \frac{624}{2,598,960} \approx 0.00024$$

#### Exercise 26: Pathfinding on a Grid
**Problem:** A grid has coordinates from $(0,0)$ to $(5,4)$. A path moves only step-by-step to the right or up. How many paths exist?
**Solution:**
Total moves $n = 9$. We must choose which 5 are Right (R).
$$\binom{9}{5} = \frac{9!}{5! \cdot 4!} = 126 \text{ paths.}$$

#### Exercise 27: Selecting Time Intervals with Repetition
**Problem:** A system has 4 types of maintenance intervals. Select 6 intervals for a workday (repetition allowed).
**Solution:**
$$\binom{n + r - 1}{r} = \binom{4 + 6 - 1}{6} = \binom{9}{6} = 84 \text{ ways.}$$

#### Exercise 28: Probability of Execution Time Sum
**Problem:** Three tasks are randomly assigned execution times of 1, 2, 3, 4, 5, or 6 seconds each. What is the probability that the total time is exactly 5 seconds?
**Solution:**
$|\Omega| = 6^3 = 216$.
Partitions of 5 into 3 positive integers: $\{3,1,1\}$ (3 ways) and $\{2,2,1\}$ (3 ways).
$|A| = 6$.
$P = \frac{6}{216} = \frac{1}{36}$.

#### Exercise 29: R Snippet -- Venn Diagram Counts
**Problem:** R code for computing 4 Venn diagram regions for 50 requests (30 fast, 25 peak, 15 both).
**Solution:**
```r
n <- 50; n_F <- 30; n_P <- 25; both <- 15
only_F <- n_F - both
only_P <- n_P - both
neither <- n - only_F - only_P - both
cat("Only F:", only_F, "Only P:", only_P, "Both:", both, "Neither:", neither, "\n")
```

#### Exercise 30: R Snippet -- Combinatorics
**Problem:** R code to choose 3 slots from 8, and distribute 10 slots among servers (5, 3, 2).
**Solution:**
```r
choose(8, 3) # 56
factorial(10) / (factorial(5) * factorial(3) * factorial(2)) # 2520
```

---

## Phase Summary
- Set theory forms the foundation of probability. Events are subsets of the sample space $\Omega$.
- Union ($\cup$) represents logical OR, Intersection ($\cap$) represents logical AND, and Complement ($A'$) represents logical NOT.
- Mutually exclusive events cannot occur simultaneously ($A \cap B = \emptyset$).
- Venn diagrams provide a visual method to translate worded probability problems into precise regions, fundamentally relying on the rule: $P(A \cap B') + P(A \cap B) + P(A' \cap B) + P(A' \cap B') = 1$.
- Kolmogorov's axioms state probabilities are non-negative, the sample space probability is 1, and the probability of mutually exclusive unions is the sum of their individual probabilities.
- The General Addition Rule handles non-mutually exclusive events: $P(A \cup B) = P(A) + P(B) - P(A \cap B)$.
- De Morgan's Laws simplify complement expressions: $(A \cup B)' = A' \cap B'$ and $(A \cap B)' = A' \cup B'$.
- Combinatorics provides counting rules essential for equally likely outcomes: $P(A) = \frac{|A|}{|\Omega|}$.
- Permutations count ordered arrangements, whereas Combinations count unordered selections.
- Time-based problems introduce unique gotchas, such as continuous boundary overlap ($P(T = t) = 0$), cyclic wrap-around considerations, and properly differentiating between permutations and combinations when scheduling time slots.
