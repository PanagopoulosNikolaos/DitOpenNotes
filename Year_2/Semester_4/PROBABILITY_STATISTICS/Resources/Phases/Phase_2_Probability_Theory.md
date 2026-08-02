# Phase 2: Probability Theory

## Table of Contents
- [Section 2.1: Set Theory & Sample Spaces](#section-21-set-theory--sample-spaces)
- [Section 2.2: Venn Diagrams & Phrase Translations](#section-22-venn-diagrams--phrase-translations)
- [Section 2.3: Probability Axioms, Rules & De Morgan's Laws](#section-23-probability-axioms-rules--de-morgans-laws)
- [Section 2.4: Combinatorics & Counting Methods](#section-24-combinatorics--counting-methods)
- [Exam Preparation Guide](#exam-preparation-guide)
- [Phase Summary](#phase-summary)

---

## Section 2.1: Set Theory & Sample Spaces

### Core Theory & Definitions

Probability Theory provides the formal mathematical framework for modeling uncertainty. Every random experiment or non-deterministic physical process begins with a precise specification of its **Sample Space** and the associated **Events**.

1.  **Sample Space ($\Omega$ or $S$):** The set of all conceivable, mutually exclusive, and collectively exhaustive outcomes of a random experiment.
    *   **Discrete Sample Space:** Contains a finite or countably infinite number of distinct elements (e.g., tossing a coin $N$ times, counting network packet retransmissions).
    *   **Continuous Sample Space:** Contains an uncountably infinite continuum of outcomes (e.g., measuring server response latency $T \in [0, \infty)$ seconds).

2.  **Event ($A \subseteq \Omega$):** Any well-defined subset of the sample space. An event occurs if the actual outcome of the experiment belongs to $A$.
    *   **Elementary (Simple) Event:** A single individual outcome $\{\omega\}$.
    *   **Compound Event:** A set containing two or more outcomes (e.g., rolling an even number $\{2, 4, 6\}$).
    *   **Impossible Event ($\emptyset$):** The empty set containing zero outcomes. Its probability is always $P(\emptyset) = 0$.
    *   **Certain Event ($\Omega$):** The entire sample space. Its probability is always $P(\Omega) = 1$.

3.  **Fundamental Set Operations:**
    *   **Union ($A \cup B$):** The set of outcomes belonging to $A$, $B$, or both. Represents the logical **OR**.
        $$A \cup B = \{\omega \in \Omega : \omega \in A \text{ or } \omega \in B\}$$
    *   **Intersection ($A \cap B$):** The set of outcomes belonging to both $A$ and $B$ simultaneously. Represents the logical **AND**.
        $$A \cap B = \{\omega \in \Omega : \omega \in A \text{ and } \omega \in B\}$$
    *   **Complement ($A'$ or $A^c$):** The set of all outcomes in $\Omega$ that do not belong to $A$. Represents the logical **NOT**.
        $$A' = \{\omega \in \Omega : \omega \notin A\}$$

4.  **Mutual Exclusivity (Disjoint Events):** Two events $A$ and $B$ are **mutually exclusive** if they cannot occur at the same time:
    $$A \cap B = \emptyset$$

> **Practical / Time-Domain Note:**
> In performance engineering and real-time systems, sample spaces often mix continuous time bounds and discrete categorical states.
> **Gotcha 1 (Point Probability in Continuous Time):** For a continuous time variable $T \in [0, \infty)\text{ s}$, the probability of measuring any exact single point timestamp is zero: $P(T = t_0) = 0$. Probabilities are defined exclusively over non-zero duration time intervals $P(t_1 \le T \le t_2)$.
> **Gotcha 2 (Mutually Exclusive Time Windows vs Independent Time Events):** If Event $A$ represents "latency $< 10\text{ ms}$" and Event $B$ represents "latency $> 100\text{ ms}$", they are mutually exclusive ($A \cap B = \emptyset$). Being mutually exclusive means they are **maximally dependent**, because if $A$ occurs, $B$ cannot possibly occur ($P(B|A) = 0$).

### Mathematical Formulas & Derivations

1.  **Fundamental Complement Identity:**
    $$A \cup A' = \Omega \quad \text{and} \quad A \cap A' = \emptyset$$
    Taking probabilities yields:
    $$P(A \cup A') = P(\Omega) \implies P(A) + P(A') = 1 \implies \boxed{P(A') = 1 - P(A)}$$

2.  **Subset Probability Monotonicity:**
    If $A \subseteq B$, then every outcome in $A$ is contained in $B$. Thus:
    $$P(A) \le P(B) \quad \text{and} \quad A \cap B = A$$

3.  **Disjoint Addition Property:**
    If events $A_1, A_2, \dots, A_k$ are pairwise disjoint ($A_i \cap A_j = \emptyset$ for $i \neq j$):
    $$P\left(\bigcup_{i=1}^k A_i\right) = \sum_{i=1}^k P(A_i)$$

> **Practical / Time-Domain Adapted Formula:**
> When continuous execution latency $T$ is bounded within a continuous sample space $\Omega = [0, T_{\max}]\text{ s}$, continuous sub-interval probabilities carry explicit time units:
> $$A = [t_1, t_2]\text{ s} \implies P(A) = P(t_1 \le T \le t_2)$$
> For uniform continuous arrival times over total duration $T_{\max}\text{ s}$:
> $$P(t_1 \le T \le t_2) = \frac{t_{2, [s]} - t_{1, [s]}}{T_{\max, [s]}}$$

### Worked Exercises

#### Exercise 1: Sample Space and Event Specification (Die Roll & Coin)
**Problem:** A fair six-sided die is rolled and a fair coin is flipped.
**a) ** Write out the sample space $\Omega$.
**b) ** Define event $A$ = "rolling a prime number and landing Heads".
**c) ** Compute $P(A)$.

**Solution:**
**a) ** Outcomes are ordered pairs $(d, c)$ where $d \in \{1, 2, 3, 4, 5, 6\}$ and $c \in \{H, T\}$:
$$\Omega = \{(1,H), (1,T), (2,H), (2,T), (3,H), (3,T), (4,H), (4,T), (5,H), (5,T), (6,H), (6,T)\}$$
Total outcomes $|\Omega| = 6 \times 2 = 12$.

**b) ** Prime die rolls are $\{2, 3, 5\}$. Thus:
$$A = \{(2,H), (3,H), (5,H)\}$$

**c) ** $|A| = 3$. Since all outcomes are equally likely:
$$P(A) = \frac{|A|}{|\Omega|} = \frac{3}{12} = \frac{1}{4} = 0.25$$

**Final Answer:** $P(A) = \mathbf{0.25}$.

#### Exercise 2: Sample Space and Event Specification (Time-Domain)
**Problem:** An automated monitoring script tracks server boot duration $T$ in seconds up to a maximum timeout of $60\text{ s}$.
**a) ** Specify the continuous sample space $\Omega$.
**b) ** Define event $A$ = "boot takes strictly between $15\text{ s}$ and $35\text{ s}$" and event $B$ = "boot takes at least $30\text{ s}$".
**c) ** Find $A \cap B$ and $A \cup B$.

**Solution:**
**a) ** Continuous time sample space:
$$\Omega = [0, 60]\text{ s}$$

**b) ** Expressing intervals:
$$A = (15, 35)\text{ s}, \quad B = [30, 60]\text{ s}$$

**c) ** Intersection and Union:
$$A \cap B = (15, 35) \cap [30, 60] = [30, 35)\text{ s}$$
$$A \cup B = (15, 35) \cup [30, 60] = (15, 60]\text{ s}$$

**Final Answer:** $A \cap B = \mathbf{[30, 35)\ s}$, $A \cup B = \mathbf{(15, 60]\ s}$.

#### Exercise 3: Operations on Discrete Events
**Problem:** Let $\Omega = \{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\}$. Let $A = \{2, 4, 6, 8, 10\}$ (evens) and $B = \{3, 6, 9\}$ (multiples of 3).
**a) ** Find $A \cup B$, $A \cap B$, $A'$, and $B'$.
**b) ** Verify that $(A \cup B)' = A' \cap B'$.

**Solution:**
**a) ** Set operations:
*   $A \cup B = \{2, 3, 4, 6, 8, 9, 10\}$
*   $A \cap B = \{6\}$
*   $A' = \{1, 3, 5, 7, 9\}$
*   $B' = \{1, 2, 4, 5, 7, 8, 10\}$

**b) ** Left-hand side:
$A \cup B = \{2, 3, 4, 6, 8, 9, 10\} \implies (A \cup B)' = \{1, 5, 7\}$
Right-hand side:
$A' \cap B' = \{1, 3, 5, 7, 9\} \cap \{1, 2, 4, 5, 7, 8, 10\} = \{1, 5, 7\}$
Both sides match identically.

**Final Answer:** Verification complete: $(A \cup B)' = A' \cap B' = \mathbf{\{1, 5, 7\}}$.

#### Exercise 4: Operations on Continuous Latency Intervals (Time-Domain)
**Problem:** In a database query benchmark with max duration $1000\text{ ms}$, let $A = [0, 250)\text{ ms}$, $B = [200, 600)\text{ ms}$, and $C = [500, 1000]\text{ ms}$.
**a) ** Compute $A \cap B$ and $B \cap C$.
**b) ** Are $A$ and $C$ mutually exclusive?
**c) ** Compute $(A \cup B \cup C)'$.

**Solution:**
**a) ** Intersections:
$$A \cap B = [0, 250) \cap [200, 600) = [200, 250)\text{ ms}$$
$$B \cap C = [200, 600) \cap [500, 1000] = [500, 600)\text{ ms}$$

**b) ** Check $A \cap C$:
$$A \cap C = [0, 250) \cap [500, 1000] = \emptyset$$
Yes, $A$ and $C$ are mutually exclusive.

**c) ** Total union:
$$A \cup B \cup C = [0, 250) \cup [200, 600) \cup [500, 1000] = [0, 1000]\text{ ms} = \Omega$$
Complement of total union:
$$(A \cup B \cup C)' = \Omega' = \mathbf{\emptyset}$$

**Final Answer:** $A \cap B = \mathbf{[200, 250)\ ms}$, $A$ and $C$ are mutually exclusive, $(A \cup B \cup C)' = \mathbf{\emptyset}$.

#### Exercise 5: Disjoint vs Intersecting Events
**Problem:** A card is drawn from a standard 52-card deck. Let $A$ = "drawing a King", $B$ = "drawing a Heart", and $C$ = "drawing a Spade".
**a) ** Are $A$ and $B$ mutually exclusive?
**b) ** Are $B$ and $C$ mutually exclusive?
**c) ** Calculate $P(A \cap B)$ and $P(B \cap C)$.

**Solution:**
**a) ** $A \cap B$ contains the King of Hearts. Thus $A \cap B \neq \emptyset \implies$ NOT mutually exclusive.
**b) ** A single card cannot be both a Heart and a Spade simultaneously. Thus $B \cap C = \emptyset \implies$ Mutually exclusive.

**c) ** Probabilities:
$$P(A \cap B) = \frac{|\text{King of Hearts}|}{52} = \frac{1}{52} \approx 0.0192$$
$$P(B \cap C) = \frac{0}{52} = 0$$

**Final Answer:** $A, B$ not disjoint; $B, C$ disjoint; $P(A \cap B) = \mathbf{1/52}$, $P(B \cap C) = \mathbf{0}$.

#### Exercise 6: Overlapping Server Maintenance & SLA Windows (Time-Domain)
**Problem:** A cloud provider schedules routine disk maintenance during interval $M = [02:00, 05:00]$ and network upgrades during interval $N = [04:00, 08:00]$ on a 24-hour clock $\Omega = [00:00, 24:00]$.
**a) ** Express intervals $M$ and $N$ in hours from midnight.
**b) ** Determine the window during which BOTH maintenance tasks occur ($M \cap N$).
**c) ** Determine the total maintenance window during which AT LEAST ONE task occurs ($M \cup N$).
**d) ** Determine the fully operational window with NO maintenance ($(M \cup N)'$).

**Solution:**
**a) ** $M = [2, 5]\text{ h}, \quad N = [4, 8]\text{ h}$.

**b) ** Both tasks active:
$$M \cap N = [2, 5] \cap [4, 8] = [4, 5]\text{ h} \quad (04:00 \text{ to } 05:00)$$

**c) ** At least one task active:
$$M \cup N = [2, 5] \cup [4, 8] = [2, 8]\text{ h} \quad (02:00 \text{ to } 08:00)$$

**d) ** No maintenance active:
$$(M \cup N)' = [0, 2) \cup (8, 24]\text{ h} \quad (00:00 \text{ to } 02:00 \text{ and } 08:00 \text{ to } 24:00)$$

**Final Answer:** Both: $\mathbf{[04:00, 05:00]}$; Any: $\mathbf{[02:00, 08:00]}$; None: $\mathbf{[00:00, 02:00) \cup (08:00, 24:00]}$.

#### Exercise 7: Multi-Slot Task Scheduling Sample Space (Time-Domain)
**Problem:** Two batch jobs $J_1$ and $J_2$ are each assigned to one of three time slots: Morning (M), Afternoon (A), or Night (N).
**a) ** List all elements of the sample space $\Omega$ as ordered pairs $(J_1, J_2)$.
**b) ** Express event $E_1$ = "both jobs run in the same time slot".
**c) ** Express event $E_2$ = "$J_1$ runs strictly before $J_2$" (assuming chronological order $M < A < N$).
**d) ** Compute $P(E_1)$ and $P(E_2)$ assuming all schedule assignments are equally likely.

**Solution:**
**a) ** $\Omega = \{(M,M), (M,A), (M,N), (A,M), (A,A), (A,N), (N,M), (N,A), (N,N)\}$. Total $|\Omega| = 3^2 = 9$.

**b) ** $E_1 = \{(M,M), (A,A), (N,N)\}$.

**c) ** $J_1 < J_2 \implies E_2 = \{(M,A), (M,N), (A,N)\}$.

**d) ** Probabilities:
$$P(E_1) = \frac{|E_1|}{|\Omega|} = \frac{3}{9} = \frac{1}{3} \approx 0.3333$$
$$P(E_2) = \frac{|E_2|}{|\Omega|} = \frac{3}{9} = \frac{1}{3} \approx 0.3333$$

**Final Answer:** $|\Omega| = \mathbf{9}$, $P(E_1) = \mathbf{1/3}$, $P(E_2) = \mathbf{1/3}$.

### R Implementation

In R, discrete sets are represented as vectors. Standard R functions perform exact set operations:

```r
# Define sample space and subsets
omega <- 1:10
A <- c(2, 4, 6, 8, 10)
B <- c(3, 6, 9)

# Set Operations
union_AB <- union(A, B)        # A u B
intersect_AB <- intersect(A, B)# A n B
comp_A <- setdiff(omega, A)    # A' (Omega \ A)
comp_B <- setdiff(omega, B)    # B'

# De Morgan's First Law Verification: (A u B)' == A' n B'
lhs <- setdiff(omega, union_AB)
rhs <- intersect(comp_A, comp_B)

cat("LHS (A u B)':", lhs, "\n")
cat("RHS A' n B':", rhs, "\n")
cat("Equal?", setequal(lhs, rhs), "\n")
```

---

## Section 2.2: Venn Diagrams & Phrase Translations

### Core Theory & Definitions

Venn Diagrams represent sample spaces visually as bounded planar regions (typically rectangles for $\Omega$) containing overlapping shapes (circles) for events. They bridge natural language problem statements and formal set-theoretic logic.

#### The 4-Region Decomposition (2 Events)
For any two events $A$ and $B$, the sample space $\Omega$ is partitioned into exactly four non-overlapping, mutually exclusive regions:

| Region Index | Set Notation | English Meaning | Systems / Latency Context |
| :---: | :--- | :--- | :--- |
| **Region 1** | $A \cap B'$ | Only $A$ occurs ($A$ without $B$) | Latency exceeds SLA, but CPU load is normal |
| **Region 2** | $A \cap B$ | Both $A$ and $B$ occur simultaneously | Latency exceeds SLA AND CPU load is high |
| **Region 3** | $A' \cap B$ | Only $B$ occurs ($B$ without $A$) | CPU load is high, but latency remains normal |
| **Region 4** | $A' \cap B'$ | Neither $A$ nor $B$ occurs | Normal latency AND normal CPU load |

```
+-------------------------------------------------------+
| Sample Space (Omega)                                  |
|   +-------------------+   +-------------------+       |
|   | Event A           |   | Event B           |       |
|   |  [Region 1]       |   |  [Region 3]       |       |
|   |  (A n B')         |   |  (A' n B)         |       |
|   |           +-------+---+-------+            |       |
|   |           |    [Region 2]    |            |       |
|   |           |     (A n B)      |            |       |
|   +-----------+------------------+------------+       |
|                                                       |
|                     [Region 4]                        |
|                     (A' n B')                         |
+-------------------------------------------------------+
```

#### The Fundamental Venn Partition Axiom
Because the four regions form a complete partition of $\Omega$:
$$\boxed{P(A \cap B') + P(A \cap B) + P(A' \cap B) + P(A' \cap B') = 1.0}$$

#### English Phrase to Set Notation Translation Matrix

| Natural Language Phrase | Set Expression | Venn Region Formula |
| :--- | :--- | :--- |
| "Event A occurs" | $A$ | $(A \cap B') \cup (A \cap B)$ |
| "Event A does not occur" | $A'$ | $(A' \cap B) \cup (A' \cap B')$ |
| "Both A and B occur" | $A \cap B$ | Region 2 |
| "At least one of A or B occurs" | $A \cup B$ | Region 1 + Region 2 + Region 3 |
| "Neither A nor B occurs" | $A' \cap B' = (A \cup B)'$ | Region 4 = $1 - P(A \cup B)$ |
| "Only A occurs" / "A but not B" | $A \cap B'$ | Region 1 = $P(A) - P(A \cap B)$ |
| "Only B occurs" / "B but not A" | $A' \cap B$ | Region 3 = $P(B) - P(A \cap B)$ |
| "Exactly one of A or B occurs" | $(A \cap B') \cup (A' \cap B)$ | Region 1 + Region 3 = $P(A \cup B) - P(A \cap B)$ |
| "At most one of A or B occurs" | $(A \cap B)' = A' \cup B'$ | Region 1 + Region 3 + Region 4 = $1 - P(A \cap B)$ |

> **Practical / Time-Domain Note:**
> When translating system requirements into Venn diagrams:
> - "High latency OR packet drop" translates to $L \cup D$.
> - "High latency WITHOUT packet drop" translates to $L \cap D'$.
> - "SLA compliance" often means NEITHER error state occurs: $L' \cap D' = (L \cup D)'$.

### Mathematical Formulas & Derivations

1.  **Only Event A Probability:**
    Since $A = (A \cap B') \cup (A \cap B)$ and these two components are disjoint:
    $$P(A) = P(A \cap B') + P(A \cap B) \implies \boxed{P(A \cap B') = P(A) - P(A \cap B)}$$

2.  **Exactly One Event Probability:**
    $$\begin{aligned}
    P(\text{Exactly One}) &= P(A \cap B') + P(A' \cap B) \\
    &= [P(A) - P(A \cap B)] + [P(B) - P(A \cap B)] \\
    &= \boxed{P(A) + P(B) - 2P(A \cap B)} = P(A \cup B) - P(A \cap B)
    \end{aligned}$$

3.  **Three-Event Venn Partition (8 Regions):**
    For events $A, B, C$, $\Omega$ splits into 8 disjoint regions:
    $$P(\Omega) = P(A \cap B' \cap C') + P(A' \cap B \cap C') + P(A' \cap B' \cap C) + P(A \cap B \cap C') + P(A \cap B' \cap C) + P(A' \cap B \cap C) + P(A \cap B \cap C) + P(A' \cap B' \cap C') = 1$$

### Worked Exercises

#### Exercise 8: 4-Region Decomposition from Survey Data
**Problem:** In a survey of 100 computer science students, 65 take Java ($J$), 45 take Python ($P$), and 20 take both Java and Python.
**a) ** Find the number of students in each of the 4 Venn regions.
**b) ** Find the probability that a randomly chosen student takes Python but not Java.

**Solution:**
**a) ** Calculate regional counts:
*   Both Java and Python ($J \cap P$): $n_2 = 20$
*   Only Java ($J \cap P'$): $n_1 = n(J) - n_2 = 65 - 20 = 45$
*   Only Python ($J' \cap P$): $n_3 = n(P) - n_2 = 45 - 20 = 25$
*   Neither ($J' \cap P'$): $n_4 = 100 - (n_1 + n_2 + n_3) = 100 - (45 + 20 + 25) = 10$

**b) ** Probability of "Only Python":
$$P(J' \cap P) = \frac{n_3}{N} = \frac{25}{100} = 0.25$$

**Final Answer:** Regions: Only J=$\mathbf{45}$, Both=$\mathbf{20}$, Only P=$\mathbf{25}$, Neither=$\mathbf{10}$. $P(\text{Only P}) = \mathbf{0.25}$.

#### Exercise 9: 4-Region Latency & Peak Load Decomposition (Time-Domain)
**Problem:** A monitoring log of 500 web requests shows that 150 experienced high latency ($L$), 200 arrived during peak traffic hours ($H$), and 350 experienced neither high latency nor peak traffic hours.
**a) ** Compute the number of requests that experienced BOTH high latency and peak traffic ($L \cap H$).
**b) ** Compute $P(L \cap H')$.

**Solution:**
**a) ** Total $N = 500$. Neither region $n(L' \cap H') = 350$.
At least one region:
$$n(L \cup H) = N - n(L' \cap H') = 500 - 350 = 150$$
Using the frequency addition rule $n(L \cup H) = n(L) + n(H) - n(L \cap H)$:
$$150 = 150 + 200 - n(L \cap H)$$
$$n(L \cap H) = 350 - 150 = 200 \implies 200\text{ requests both}.$$

**b) ** Compute "Only High Latency":
$$n(L \cap H') = n(L) - n(L \cap H) = 150 - 200$$
Wait! Notice that $n(L \cap H) = 200 > n(L) = 150$. This calculation yields a negative count ($-50$), which violates Axiom 1!
Let's check the given numbers: if $n(L)=150$ and $n(L \cup H)=150$, then since $L \subseteq L \cup H$ and $n(L)=150$, we MUST have $L \cup H = L$. Thus $H \subseteq L$, meaning $n(H)$ cannot exceed 150. But $n(H)=200$, which is impossible!
Therefore, the log data is **inconsistent with probability axioms**.

**Final Answer:** The given parameters ($n(L)=150, n(H)=200, n(\text{Neither})=350$) are **mathematically inconsistent** because they imply $n(L \cap H) = \mathbf{200} > n(L)$, violating Kolmogorov's First Axiom.

#### Exercise 10: Multi-Part Phrase Translation & Region Mapping
**Problem:** Two independent automated tests $T_1$ and $T_2$ are run. $P(T_1) = 0.40$, $P(T_2) = 0.30$, and $P(T_1 \cap T_2) = 0.12$. Express the following phrases in set notation and calculate their probabilities:
**a) ** "At least one test passes"
**b) ** "Neither test passes"
**c) ** "Exactly one test passes"
**d) ** "At most one test passes"

**Solution:**
**a) ** "At least one": $T_1 \cup T_2$
$$P(T_1 \cup T_2) = P(T_1) + P(T_2) - P(T_1 \cap T_2) = 0.40 + 0.30 - 0.12 = 0.58$$

**b) ** "Neither": $T_1' \cap T_2' = (T_1 \cup T_2)'$
$$P(T_1' \cap T_2') = 1 - P(T_1 \cup T_2) = 1 - 0.58 = 0.42$$

**c) ** "Exactly one": $(T_1 \cap T_2') \cup (T_1' \cap T_2)$
$$P(\text{Exactly One}) = P(T_1 \cup T_2) - P(T_1 \cap T_2) = 0.58 - 0.12 = 0.46$$

**d) ** "At most one": $(T_1 \cap T_2)'$
$$P((T_1 \cap T_2)') = 1 - P(T_1 \cap T_2) = 1 - 0.12 = 0.88$$

**Final Answer:** **a) ** $\mathbf{0.58}$, **b) ** $\mathbf{0.42}$, **c) ** $\mathbf{0.46}$, **d) ** $\mathbf{0.88}$.

#### Exercise 11: Multi-Part System Outage & Database Lock Phrases (Time-Domain)
**Problem:** In a database server, event $A$ = "read queue delay $> 50\text{ ms}$" ($P(A) = 0.25$) and event $B$ = "write lock contention" ($P(B) = 0.15$). The joint probability of both is $P(A \cap B) = 0.05$.
**a) ** Calculate the probability of $A \cap B'$ and state its time-domain meaning.
**b) ** Calculate the probability of $A' \cap B$ and state its time-domain meaning.
**c) ** Calculate the probability that the server experiences either queue delay or write lock contention, but not both.
**d) ** Calculate the probability of complete normal operation ($(A \cup B)'$).

**Solution:**
**a) ** $P(A \cap B') = P(A) - P(A \cap B) = 0.25 - 0.05 = 0.20$.
*Meaning:* Read queue delay exceeds $50\text{ ms}$ while write locks remain uncontended.

**b) ** $P(A' \cap B) = P(B) - P(A \cap B) = 0.15 - 0.05 = 0.10$.
*Meaning:* Write lock contention occurs while read queue delay remains $\le 50\text{ ms}$.

**c) ** Either but not both (Exactly One):
$$P(\text{Exactly One}) = P(A \cap B') + P(A' \cap B) = 0.20 + 0.10 = 0.30$$

**d) ** Normal operation:
$$P(A \cup B) = 0.25 + 0.15 - 0.05 = 0.35$$
$$P((A \cup B)') = 1 - 0.35 = 0.65$$

**Final Answer:** **a) ** $\mathbf{0.20}$, **b) ** $\mathbf{0.10}$, **c) ** $\mathbf{0.30}$, **d) ** $\mathbf{0.65}$.

#### Exercise 12: 3-Event Venn Diagram Region Tallying
**Problem:** A survey of 120 developers tracks knowledge of C++ ($A$), Java ($B$), and Python ($C$).
- $n(A) = 60, n(B) = 50, n(C) = 45$
- $n(A \cap B) = 20, n(A \cap C) = 15, n(B \cap C) = 15$
- $n(A \cap B \cap C) = 8$
Compute the number of developers who know:
**a) ** All three languages
**b) ** Exactly two languages
**c) ** C++ only
**d) ** None of the three languages

**Solution:**
**a) ** Given directly: $n(A \cap B \cap C) = 8$.

**b) ** Two-language overlaps (excluding all three):
*   Only C++ and Java: $n(A \cap B \cap C') = 20 - 8 = 12$
*   Only C++ and Python: $n(A \cap C \cap B') = 15 - 8 = 7$
*   Only Java and Python: $n(B \cap C \cap A') = 15 - 8 = 7$
Total knowing exactly two: $12 + 7 + 7 = 26$.

**c) ** Only C++ ($A \cap B' \cap C'$):
$$n(A \cap B' \cap C') = n(A) - [12 + 7 + 8] = 60 - 27 = 33$$

**d) ** Total union $n(A \cup B \cup C)$:
$$n(A \cup B \cup C) = 60 + 50 + 45 - 20 - 15 - 15 + 8 = 113$$
None ($A' \cap B' \cap C'$):
$$n(\text{None}) = 120 - 113 = 7$$

**Final Answer:** **a) ** $\mathbf{8}$, **b) ** $\mathbf{26}$, **c) ** $\mathbf{33}$, **d) ** $\mathbf{7}$.

#### Exercise 13: 3-Component Microservice Jitter Breakdown (Time-Domain)
**Problem:** A distributed system consists of 3 microservices $M_1, M_2, M_3$. Jitter spikes occur with probabilities $P(M_1) = 0.10, P(M_2) = 0.12, P(M_3) = 0.08$. Pairwise joint jitter probabilities are $P(M_1 \cap M_2) = 0.03, P(M_1 \cap M_3) = 0.02, P(M_2 \cap M_3) = 0.02$, and all three experience simultaneous jitter with probability $P(M_1 \cap M_2 \cap M_3) = 0.01$.
**a) ** Compute the probability that at least one microservice experiences a jitter spike.
**b) ** Compute the probability that ONLY $M_1$ experiences a jitter spike.
**c) ** Compute the probability that NO microservice experiences a jitter spike.

**Solution:**
**a) ** Apply Inclusion-Exclusion for 3 events:
$$\begin{aligned}
P(M_1 \cup M_2 \cup M_3) &= (0.10 + 0.12 + 0.08) - (0.03 + 0.02 + 0.02) + 0.01 \\
&= 0.30 - 0.07 + 0.01 = 0.24
\end{aligned}$$

**b) ** Only $M_1$ ($M_1 \cap M_2' \cap M_3'$):
$$P(M_1 \cap M_2' \cap M_3') = P(M_1) - P(M_1 \cap M_2) - P(M_1 \cap M_3) + P(M_1 \cap M_2 \cap M_3)$$
$$P(M_1 \cap M_2' \cap M_3') = 0.10 - 0.03 - 0.02 + 0.01 = 0.06$$

**c) ** No jitter spike:
$$P(M_1' \cap M_2' \cap M_3') = 1 - P(M_1 \cup M_2 \cup M_3) = 1 - 0.24 = 0.76$$

**Final Answer:** **a) ** $\mathbf{0.24}$, **b) ** $\mathbf{0.06}$, **c) ** $\mathbf{0.76}$.

#### Exercise 14: R Code for 4-Region Venn Diagram Counts (Time-Domain)
**Problem:** Write an R function `venn_4regions(N, nA, nB, nAB)` that accepts total request count $N$, count of high-latency requests $nA$, count of peak-hour requests $nB$, and joint count $nAB$. The function must output a named vector with the 4 region counts and print a warning if the counts violate probability axioms.

**Solution:**
```r
venn_4regions <- function(N, nA, nB, nAB) {
  only_A <- nA - nAB
  only_B <- nB - nAB
  both   <- nAB
  neither <- N - (only_A + only_B + both)
  
  # Axiom verification
  if (only_A < 0 || only_B < 0 || both < 0 || neither < 0) {
    warning("Input parameters violate Kolmogorov Axioms (negative region count detected)!")
  }
  
  regions <- c(Only_A = only_A, Both = both, Only_B = only_B, Neither = neither)
  return(regions)
}

# Test execution with valid input
res <- venn_4regions(N = 500, nA = 150, nB = 200, nAB = 50)
print(res)
```

**Final Answer:** R command snippet provided and verified.

### R Implementation

Using the R script above, we can compute regional probabilities for any 2-event scenario:

```r
# Define parameters
N <- 1000
p_A <- 0.25; p_B <- 0.15; p_AB <- 0.05

# Region Probabilities
p_onlyA <- p_A - p_AB
p_onlyB <- p_B - p_AB
p_both  <- p_AB
p_neither <- 1 - (p_onlyA + p_onlyB + p_both)

cat("P(Only A):", p_onlyA, "\n")
cat("P(Only B):", p_onlyB, "\n")
cat("P(Both):", p_both, "\n")
cat("P(Neither):", p_neither, "\n")
cat("Sum of regions:", sum(p_onlyA, p_onlyB, p_both, p_neither), "\n")
```

---

## Section 2.3: Probability Axioms, Rules & De Morgan's Laws

### Core Theory & Definitions

Modern probability theory rests upon the three **Kolmogorov Axioms** established by Andrey Kolmogorov in 1933. All valid probability rules, bounds, and identity theorems are derived directly from these three axioms.

#### Kolmogorov's Axioms

1.  **Axiom 1 (Non-Negativity):** For any event $A \subseteq \Omega$, the assigned probability is non-negative:
    $$\boxed{P(A) \ge 0}$$

2.  **Axiom 2 (Normalization):** The probability of the entire sample space $\Omega$ equals unity:
    $$\boxed{P(\Omega) = 1.0}$$

3.  **Axiom 3 (Countable Additivity):** If $A_1, A_2, A_3, \dots$ is a sequence of pairwise disjoint events ($A_i \cap A_j = \emptyset$ for all $i \neq j$), then:
    $$\boxed{P\left(\bigcup_{i=1}^\infty A_i\right) = \sum_{i=1}^\infty P(A_i)}$$

#### The General Addition Rule
For any two arbitrary events $A$ and $B$ (whether disjoint or overlapping):
$$\boxed{P(A \cup B) = P(A) + P(B) - P(A \cap B)}$$
*Intuition:* Adding $P(A)$ and $P(B)$ counts the intersection $A \cap B$ twice. Subtracting $P(A \cap B)$ corrects the double-counting.

#### The Inclusion-Exclusion Principle (3 Events)
For any three arbitrary events $A, B, C$:
$$\boxed{P(A \cup B \cup C) = P(A) + P(B) + P(C) - P(A \cap B) - P(A \cap C) - P(B \cap C) + P(A \cap B \cap C)}$$

#### De Morgan's Laws
De Morgan's Laws describe how complement operators interact with unions and intersections:

1.  **First Law (Complement of Union):**
    $$(A \cup B)' = A' \cap B'$$
    In probability form:
    $$\boxed{P((A \cup B)') = P(A' \cap B') = 1 - P(A \cup B)}$$
    *Reading:* "NOT (A or B)" is logically equivalent to "(NOT A) AND (NOT B)". Neither event occurs.

2.  **Second Law (Complement of Intersection):**
    $$(A \cap B)' = A' \cup B'$$
    In probability form:
    $$\boxed{P((A \cap B)') = P(A' \cup B') = 1 - P(A \cap B)}$$
    *Reading:* "NOT (A and B)" is logically equivalent to "(NOT A) OR (NOT B)". At least one event fails to occur.

> **Practical / Time-Domain Note:**
> In distributed systems reliability, De Morgan's Laws evaluate overall system operational bounds.
> If $F_1, F_2, \dots, F_k$ represent component failure events:
> - System survival (all components working) is $F_1' \cap F_2' \cap \dots \cap F_k' = (F_1 \cup F_2 \cup \dots \cup F_k)'$.
> - System failure (at least one component down) is $F_1 \cup F_2 \cup \dots \cup F_k$.

### Mathematical Formulas & Derivations

1.  **Derivation of General Addition Rule:**
    Partition $A \cup B$ into three mutually exclusive regions:
    $$A \cup B = (A \cap B') \cup (A \cap B) \cup (A' \cap B)$$
    By Axiom 3:
    $$P(A \cup B) = P(A \cap B') + P(A \cap B) + P(A' \cap B)$$
    Substitute $P(A \cap B') = P(A) - P(A \cap B)$ and $P(A' \cap B) = P(B) - P(A \cap B)$:
    $$P(A \cup B) = [P(A) - P(A \cap B)] + P(A \cap B) + [P(B) - P(A \cap B)] = P(A) + P(B) - P(A \cap B) \quad \blacksquare$$

2.  **Probability Bounds (Boole's and Bonferroni's Inequalities):**
    *   **Boole's Inequality (Union Bound):** $P(A \cup B) \le P(A) + P(B)$
    *   **Bonferroni's Inequality:** $P(A \cap B) \ge P(A) + P(B) - 1$

### Worked Exercises

#### Exercise 15: Kolmogorov Axioms Consistency Check
**Problem:** A researcher proposes the following assignment for events $A$ and $B$: $P(A) = 0.70$, $P(B) = 0.50$, and $P(A \cup B) = 0.90$.
**a) ** Compute $P(A \cap B)$.
**b) ** Check if this probability assignment satisfies all Kolmogorov Axioms.

**Solution:**
**a) ** Apply the Addition Rule:
$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$
$$0.90 = 0.70 + 0.50 - P(A \cap B) \implies P(A \cap B) = 1.20 - 0.90 = 0.30$$

**b) ** Verify Kolmogorov Axioms:
1.  **Non-negativity:** $P(A)=0.70 \ge 0, P(B)=0.50 \ge 0, P(A \cap B)=0.30 \ge 0, P(A \cup B)=0.90 \ge 0$. Region probabilities: $P(A \cap B') = 0.40 \ge 0$, $P(A' \cap B) = 0.20 \ge 0$, $P(A' \cap B') = 0.10 \ge 0$. All $\ge 0 \checkmark$.
2.  **Normalization:** $P(\Omega) = P(A \cup B) + P((A \cup B)') = 0.90 + 0.10 = 1.00 \checkmark$.
3.  **Additivity:** All composite probabilities match disjoint region sums $\checkmark$.

**Final Answer:** $P(A \cap B) = \mathbf{0.30}$. The assignment is **fully consistent** with all axioms.

#### Exercise 16: Verification of Axioms on Buffer Overflow Bounds (Time-Domain)
**Problem:** A network router tracks buffer overflow ($O$) and packet corruption ($C$). An engineer claims: $P(O) = 0.15$, $P(C) = 0.10$, and $P(O \cap C) = 0.20$. Show why this violates probability theory.

**Solution:**
Recall that $O \cap C \subseteq O$. By subset monotonicity:
$$P(O \cap C) \le P(O)$$
Here, $P(O \cap C) = 0.20 > P(O) = 0.15$.
Furthermore, computing "Only Overflow":
$$P(O \cap C') = P(O) - P(O \cap C) = 0.15 - 0.20 = -0.05 < 0$$
This yields a negative probability, directly violating **Axiom 1 (Non-Negativity)**.

**Final Answer:** The claim is invalid because $P(O \cap C) > P(O)$, causing $P(O \cap C') = \mathbf{-0.05}$, which violates **Axiom 1**.

#### Exercise 17: Addition Rule & Complementary Probability
**Problem:** A student has a $0.60$ chance of passing Math ($M$) and a $0.50$ chance of passing Physics ($P$). The probability of passing both is $0.30$.
**a) ** Find the probability of passing at least one subject.
**b) ** Find the probability of failing both subjects.

**Solution:**
**a) ** At least one:
$$P(M \cup P) = P(M) + P(P) - P(M \cap P) = 0.60 + 0.50 - 0.30 = 0.80$$

**b) ** Failing both:
$$P(M' \cap P') = 1 - P(M \cup P) = 1 - 0.80 = 0.20$$

**Final Answer:** **a) ** $\mathbf{0.80}$, **b) ** $\mathbf{0.20}$.

#### Exercise 18: Addition Rule for Network Packet Dropping & Timeouts (Time-Domain)
**Problem:** During peak routing hours, packet drop probability is $P(D) = 0.08$, timeout probability is $P(T) = 0.05$, and the probability of experiencing both is $P(D \cap T) = 0.02$.
**a) ** Compute the probability of experiencing a packet drop, a timeout, or both.
**b) ** Compute the probability of successful transmission with neither issue.

**Solution:**
**a) ** Apply Addition Rule:
$$P(D \cup T) = P(D) + P(T) - P(D \cap T) = 0.08 + 0.05 - 0.02 = 0.11$$

**b) ** Successful transmission:
$$P(D' \cap T') = 1 - P(D \cup T) = 1 - 0.11 = 0.89$$

**Final Answer:** **a) ** $\mathbf{0.11}$, **b) ** $\mathbf{0.89}$.

#### Exercise 19: De Morgan's Laws Application
**Problem:** Given $P(A) = 0.55$, $P(B) = 0.40$, and $P(A \cup B) = 0.75$.
**a) ** Calculate $P(A \cap B)$.
**b) ** Apply De Morgan's First Law to calculate $P(A' \cap B')$.
**c) ** Apply De Morgan's Second Law to calculate $P(A' \cup B')$.

**Solution:**
**a) ** $P(A \cap B) = P(A) + P(B) - P(A \cup B) = 0.55 + 0.40 - 0.75 = 0.20$.

**b) ** First Law: $(A \cup B)' = A' \cap B'$
$$P(A' \cap B') = 1 - P(A \cup B) = 1 - 0.75 = 0.25$$

**c) ** Second Law: $(A \cap B)' = A' \cup B'$
$$P(A' \cup B') = 1 - P(A \cap B) = 1 - 0.20 = 0.80$$

**Final Answer:** **a) ** $\mathbf{0.20}$, **b) ** $\mathbf{0.25}$, **c) ** $\mathbf{0.80}$.

#### Exercise 20: De Morgan's Laws on System Heartbeat & Ping Failures (Time-Domain)
**Problem:** Two ping monitors check a remote server. Monitor 1 misses heartbeat ($M_1$) with probability $0.04$. Monitor 2 misses heartbeat ($M_2$) with probability $0.06$. Both miss simultaneously with probability $0.01$.
**a) ** What is the probability that AT LEAST ONE monitor misses the heartbeat?
**b) ** Use De Morgan's Law to find the probability that BOTH monitors receive the heartbeat.
**c) ** What is the probability that AT LEAST ONE monitor successfully receives the heartbeat?

**Solution:**
**a) ** At least one misses:
$$P(M_1 \cup M_2) = P(M_1) + P(M_2) - P(M_1 \cap M_2) = 0.04 + 0.06 - 0.01 = 0.09$$

**b) ** Both receive heartbeat:
By De Morgan's First Law, $M_1' \cap M_2' = (M_1 \cup M_2)'$:
$$P(M_1' \cap M_2') = 1 - P(M_1 \cup M_2) = 1 - 0.09 = 0.91$$

**c) ** At least one receives heartbeat:
By De Morgan's Second Law, $M_1' \cup M_2' = (M_1 \cap M_2)'$:
$$P(M_1' \cup M_2') = 1 - P(M_1 \cap M_2) = 1 - 0.01 = 0.99$$

**Final Answer:** **a) ** $\mathbf{0.09}$, **b) ** $\mathbf{0.91}$, **c) ** $\mathbf{0.99}$.

#### Exercise 21: 3-Event Inclusion-Exclusion Principle
**Problem:** In a factory, machines $A, B, C$ produce defective parts with probabilities $P(A)=0.10, P(B)=0.12, P(C)=0.15$. Pairwise joint defects are $P(A \cap B)=0.04, P(A \cap C)=0.03, P(B \cap C)=0.05$. All three defect simultaneously with probability $0.02$. Find the probability that a part has at least one defect.

**Solution:**
Apply 3-event Inclusion-Exclusion:
$$\begin{aligned}
P(A \cup B \cup C) &= (0.10 + 0.12 + 0.15) - (0.04 + 0.03 + 0.05) + 0.02 \\
&= 0.37 - 0.12 + 0.02 = 0.27
\end{aligned}$$

**Final Answer:** $P(A \cup B \cup C) = \mathbf{0.27}$.

#### Exercise 22: 3-Node Distributed Consensus Inclusion-Exclusion (Time-Domain)
**Problem:** A distributed database requires consensus among 3 nodes $N_1, N_2, N_3$. Node timeout probabilities are $P(N_1)=0.05, P(N_2)=0.05, P(N_3)=0.05$. Pairwise timeout probabilities are $P(N_i \cap N_j)=0.01$ for all pairs, and $P(N_1 \cap N_2 \cap N_3)=0.002$.
**a) ** Compute the probability that at least one node times out.
**b) ** Compute the probability that all three nodes respond without timeout.

**Solution:**
**a) ** At least one timeout:
$$P(N_1 \cup N_2 \cup N_3) = 3(0.05) - 3(0.01) + 0.002 = 0.15 - 0.03 + 0.002 = 0.122$$

**b) ** All respond:
$$P(N_1' \cap N_2' \cap N_3') = 1 - P(N_1 \cup N_2 \cup N_3) = 1 - 0.122 = 0.878$$

**Final Answer:** **a) ** $\mathbf{0.122}$, **b) ** $\mathbf{0.878}$.

#### Exercise 23: R Code for Inclusion-Exclusion & Axiom Verification (Time-Domain)
**Problem:** Write R code to verify the 3-event Inclusion-Exclusion principle and check Bonferroni's inequality for $P(A)=0.7, P(B)=0.8, P(A \cap B)=0.6$.

**Solution:**
```r
# Given probabilities
pA <- 0.7; pB <- 0.8; pAB <- 0.6

# 1. Addition Rule check
pA_union_B <- pA + pB - pAB
cat("P(A u B):", pA_union_B, "\n")

# 2. Bonferroni's Inequality check: P(A n B) >= P(A) + P(B) - 1
bonferroni_bound <- pA + pB - 1
cat("Bonferroni Lower Bound:", bonferroni_bound, "\n")
cat("P(A n B) >= Bound?", pAB >= bonferroni_bound, "\n")

# 3. Axiom Check
stopifnot(pA_union_B <= 1.0, pA_union_B >= 0.0)
cat("Axiom checks passed successfully!\n")
```

**Final Answer:** R code executed and Bonferroni bound verified ($0.6 \ge 0.5$).

### R Implementation

R script for verifying Bonferroni bounds and De Morgan's laws:

```r
# Verify De Morgan's Law via simulation
set.seed(42)
N <- 1e6
event_A <- runif(N) < 0.4
event_B <- runif(N) < 0.3

# Empirical probabilities
p_A_or_B <- mean(event_A | event_B)
p_notA_and_notB <- mean(!event_A & !event_B)

cat("Empirical P((A u B)'):", 1 - p_A_or_B, "\n")
cat("Empirical P(A' n B'):", p_notA_and_notB, "\n")
cat("Difference:", abs((1 - p_A_or_B) - p_notA_and_notB), "\n")
```

---

## Section 2.4: Combinatorics & Counting Methods

### Core Theory & Definitions

When all outcomes in a finite sample space $\Omega$ are **equally likely** (laplacian sample space), calculating the probability of an event $A$ reduces to a pure counting problem:
$$P(A) = \frac{|A|}{|\Omega|} = \frac{\text{Number of Favorable Outcomes}}{\text{Total Number of Possible Outcomes}}$$

Combinatorics provides the rigorous rules for counting large sample spaces without exhaustive enumeration.

#### 1. Fundamental Principles of Counting
*   **Product Rule (Multiplication Principle):** If a procedure can be broken into $k$ sequential stages, where stage 1 has $n_1$ outcomes, stage 2 has $n_2$ outcomes, ..., and stage $k$ has $n_k$ outcomes, the total number of composite outcomes is:
    $$N = n_1 \cdot n_2 \cdot \dots \cdot n_k$$
*   **Sum Rule (Addition Principle):** If an choice can be made either from set 1 with $n_1$ options OR from set 2 with $n_2$ options (where the sets are disjoint), the total number of choices is:
    $$N = n_1 + n_2$$

#### 2. Permutations (Order Matters)
An ordered arrangement of $r$ objects selected from a set of $n$ distinct objects.
*   **Without Repetition:**
    $$P(n, r) = \frac{n!}{(n-r)!}$$
    *Special case ($r=n$):* Arranging all $n$ distinct objects requires $P(n, n) = n!$ ways.
*   **Permutations with Repetition (Identical Objects):** Arranging $n$ total objects where $n_1$ are identical of type 1, $n_2$ identical of type 2, ..., $n_k$ identical of type $k$:
    $$P(n; n_1, n_2, \dots, n_k) = \frac{n!}{n_1! \cdot n_2! \dots n_k!}$$
*   **Circular Permutations:** Arranging $n$ distinct objects around a closed circle (where rotational shifts are considered identical):
    $$P_{\text{circular}} = (n - 1)!$$

#### 3. Combinations (Order Does NOT Matter)
An unordered selection of $r$ objects chosen from $n$ distinct objects.
*   **Without Replacement:**
    $$C(n, r) = \binom{n}{r} = \frac{n!}{r!(n-r)!}$$
*   **Combinations with Replacement (Stars and Bars):** Selecting $r$ items from $n$ distinct categories where items may be selected repeatedly:
    $$C^R(n, r) = \binom{n + r - 1}{r} = \frac{(n + r - 1)!}{r!(n - 1)!}$$

#### 4. Multinomial Coefficients
Partitioning $n$ distinct objects into $k$ distinct groups of specified sizes $r_1, r_2, \dots, r_k$ (where $\sum r_i = n$):
$$\binom{n}{r_1, r_2, \dots, r_k} = \frac{n!}{r_1! \cdot r_2! \dots r_k!}$$

> **Practical / Time-Domain Note:**
> In computer systems and networks:
> - **Permutations** model sequential execution order, pipeline stages, network packet routing paths, and priority queues.
> - **Combinations** model server pool selections, quorum voting nodes, parallel thread allocations, and memory buffer partitioning.
> - **Combinations with replacement** model assigning identical requests across server queues or allocating CPU cycles to processes.

### Mathematical Formulas & Derivations

1.  **Derivation of Circular Permutation Formula:**
    Linear arrangements of $n$ distinct objects equal $n!$. Around a circle, every valid arrangement can be rotated into $n$ equivalent configurations. Dividing linear permutations by $n$ rotational symmetries gives:
    $$P_{\text{circular}} = \frac{n!}{n} = (n - 1)! \quad \blacksquare$$

2.  **Stars and Bars Derivation (Combinations with Replacement):**
    To distribute $r$ identical items into $n$ distinct bins, place $r$ stars ($\star$) and $n-1$ dividers ($|$). Total symbols = $r + n - 1$. Selecting positions for the $r$ stars out of $r + n - 1$ total symbol positions yields $\binom{n+r-1}{r}$.

### Worked Exercises

#### Exercise 24: Permutations and Combinations in Quality Control
**Problem:** A batch of 20 manufactured circuit boards contains 4 defective boards. A sample of 5 boards is selected at random without replacement.
**a) ** How many total samples of 5 boards can be formed?
**b) ** How many samples contain exactly 2 defective boards?
**c) ** What is the probability that a sample contains at least 1 defective board?

**Solution:**
**a) ** Total possible samples $|\Omega|$:
$$|\Omega| = \binom{20}{5} = \frac{20 \cdot 19 \cdot 18 \cdot 17 \cdot 16}{5 \cdot 4 \cdot 3 \cdot 2 \cdot 1} = 15,504$$

**b) ** Choose 2 defective from 4, and 3 non-defective from 16:
$$|E_{\text{2 def}}| = \binom{4}{2} \cdot \binom{16}{3} = 6 \cdot \frac{16 \cdot 15 \cdot 14}{3 \cdot 2 \cdot 1} = 6 \cdot 560 = 3,360$$

**c) ** Complementary probability (0 defective):
$$|E_{\text{0 def}}| = \binom{4}{0} \cdot \binom{16}{5} = 1 \cdot 4,368 = 4,368$$
$$P(\text{0 def}) = \frac{4,368}{15,504} \approx 0.2817$$
$$P(\text{at least 1 def}) = 1 - P(\text{0 def}) = 1 - 0.2817 = 0.7183$$

**Final Answer:** **a) ** $\mathbf{15,504}$, **b) ** $\mathbf{3,360}$, **c) ** $\mathbf{0.7183}$.

#### Exercise 25: License Plate Permutations & Product Rule
**Problem:** A state formats vehicle license plates with 3 uppercase letters followed by 4 digits.
**a) ** How many total plates exist if repetition is allowed?
**b) ** How many total plates exist if NO repetition of letters or digits is allowed?
**c) ** What is the probability that a randomly assigned plate starts with the letter 'A' and ends with an even digit (repetition allowed)?

**Solution:**
**a) ** Repetition allowed:
$$N = 26^3 \cdot 10^4 = 17,576 \cdot 10,000 = 175,760,000$$

**b) ** No repetition:
$$N_{\text{no rep}} = (26 \cdot 25 \cdot 24) \cdot (10 \cdot 9 \cdot 8 \cdot 7) = 15,600 \cdot 5,040 = 78,624,000$$

**c) ** Starts with 'A' (1 option), next 2 letters (26 options each); ends with even digit $\{0,2,4,6,8\}$ (5 options), first 3 digits (10 options each):
$$|F| = (1 \cdot 26 \cdot 26) \cdot (10 \cdot 10 \cdot 10 \cdot 5) = 676 \cdot 5,000 = 3,380,000$$
$$P = \frac{3,380,000}{175,760,000} = \frac{1}{26} \cdot \frac{5}{10} = \frac{1}{26} \cdot \frac{1}{2} = \frac{1}{52} \approx 0.01923$$

**Final Answer:** **a) ** $\mathbf{175,760,000}$, **b) ** $\mathbf{78,624,000}$, **c) ** $\mathbf{1/52 \approx 0.01923}$.

#### Exercise 26: Server Task Scheduling Timeline & Permutations (Time-Domain)
**Problem:** An operating system scheduler must execute 8 processes: 3 real-time audio tasks, 3 database queries, and 2 background backups.
**a) ** How many total linear execution sequences exist?
**b) ** How many sequences execute all 3 audio tasks consecutively?
**c) ** How many sequences group tasks of the same type together?

**Solution:**
**a) ** Linear permutations of 8 distinct tasks:
$$P(8, 8) = 8! = 40,320$$

**b) ** Treat the 3 audio tasks as 1 super-task. Total objects to arrange = $1 + 3 + 2 = 6$.
Internal arrangements of audio tasks = $3! = 6$.
$$N = 6! \cdot 3! = 720 \cdot 6 = 4,320$$

**c) ** Arrange the 3 task categories: $3! = 6$ ways.
Arrange within categories: Audio ($3!$), Database ($3!$), Backup ($2!$).
$$N_{\text{grouped}} = 3! \cdot (3! \cdot 3! \cdot 2!) = 6 \cdot (6 \cdot 6 \cdot 2) = 6 \cdot 72 = 432$$

**Final Answer:** **a) ** $\mathbf{40,320}$, **b) ** $\mathbf{4,320}$, **c) ** $\mathbf{432}$.

#### Exercise 27: Multi-Tier Card Deck & Urn Selection (Combined, Moderate)
**Problem:** An urn contains 10 red balls, 8 blue balls, and 6 green balls (total 24 balls). A player draws 4 balls simultaneously at random.
**a) ** Calculate the total size of the sample space $|\Omega|$.
**b) ** Calculate the probability of drawing exactly 2 red and 2 blue balls.
**c) ** Calculate the probability of drawing all 4 balls of the same color.
**d) ** Calculate the probability of drawing at least 1 green ball.

**Solution:**
**a) ** Sample space:
$$|\Omega| = \binom{24}{4} = \frac{24 \cdot 23 \cdot 22 \cdot 21}{4 \cdot 3 \cdot 2 \cdot 1} = 10,626$$

**b) ** 2 Red ($\binom{10}{2}$), 2 Blue ($\binom{8}{2}$), 0 Green ($\binom{6}{0}$):
$$|E_b| = \binom{10}{2} \cdot \binom{8}{2} = 45 \cdot 28 = 1,260$$
$$P(E_b) = \frac{1,260}{10,626} = \frac{210}{1,771} \approx 0.1186$$

**c) ** Same color: All Red ($\binom{10}{4}$), All Blue ($\binom{8}{4}$), or All Green ($\binom{6}{4}$):
$$|E_c| = \binom{10}{4} + \binom{8}{4} + \binom{6}{4} = 210 + 70 + 15 = 295$$
$$P(E_c) = \frac{295}{10,626} \approx 0.02776$$

**d) ** At least 1 green = $1 - P(\text{0 green})$:
0 Green means drawing 4 balls from 18 non-green (10 Red + 8 Blue):
$$|E_{\text{no green}}| = \binom{18}{4} = 3,060$$
$$P(\text{at least 1 green}) = 1 - \frac{3,060}{10,626} = 1 - 0.28797 = 0.71203$$

**Final Answer:** **a) ** $\mathbf{10,626}$, **b) ** $\mathbf{0.1186}$, **c) ** $\mathbf{0.02776}$, **d) ** $\mathbf{0.71203}$.

#### Exercise 28: Multi-Channel Signal Routing & Permutations (Time-Domain) (Combined, Harder)
**Problem:** A network switch routes packets across 12 distinct physical channels. 5 channels carry high-priority video streams, 4 carry VoIP audio, and 3 carry data traffic.
**a) ** In how many distinct ways can the 12 channels be assigned to 3 processing cores if Core 1 receives 5 channels, Core 2 receives 4 channels, and Core 3 receives 3 channels?
**b) ** If 4 channels are selected at random without replacement, what is the probability that all 4 are video channels?
**c) ** If channels are routed sequentially one by one, what is the probability that the first 3 routed channels are all video streams?
**d) ** What R command computes the multinomial partitioning count from part a?

**Solution:**
**a) ** Apply Multinomial Coefficient:
$$\binom{12}{5, 4, 3} = \frac{12!}{5! \cdot 4! \cdot 3!} = \frac{479,001,600}{120 \cdot 24 \cdot 6} = \frac{479,001,600}{17,280} = 27,720$$

**b) ** Choose 4 video from 5 video; total channels 12:
$$P = \frac{\binom{5}{4}}{\binom{12}{4}} = \frac{5}{495} = \frac{1}{99} \approx 0.01010$$

**c) ** Sequential routing without replacement (first 3 video):
$$P = \frac{5}{12} \cdot \frac{4}{11} \cdot \frac{3}{10} = \frac{60}{1320} = \frac{1}{22} \approx 0.04545$$

**d) ** R command snippet:
```r
factorial(12) / (factorial(5) * factorial(4) * factorial(3))
```

**Final Answer:** **a) ** $\mathbf{27,720}$, **b) ** $\mathbf{1/99 \approx 0.01010}$, **c) ** $\mathbf{1/22 \approx 0.04545}$, **d) ** R command: `factorial(12) / (factorial(5)*factorial(4)*factorial(3))`.

#### Exercise 29: 3-Stage Microservice Queueing Delay & Venn Breakdown (Time-Domain) (Combined, Hard)
**Problem:** A complex transaction traverses 3 microservices $S_1, S_2, S_3$. Latency exceeding $100\text{ ms}$ occurs at $S_1$ with $P(S_1)=0.20$, at $S_2$ with $P(S_2)=0.25$, and at $S_3$ with $P(S_3)=0.15$.
Intersections: $P(S_1 \cap S_2) = 0.08$, $P(S_1 \cap S_3) = 0.05$, $P(S_2 \cap S_3) = 0.06$, and all three exceed delay simultaneously with $P(S_1 \cap S_2 \cap S_3) = 0.02$.
**a) ** Calculate the probability that the transaction experiences high latency at AT LEAST ONE microservice.
**b) ** Calculate the probability that the transaction completes within $100\text{ ms}$ across ALL 3 microservices.
**c) ** Calculate the probability that ONLY service $S_2$ experiences high latency.
**d) ** Calculate the probability that EXACTLY TWO microservices experience high latency.
**e) ** Write an R script using `choose()` or set logic to verify the total union probability.

**Solution:**
**a) ** Inclusion-Exclusion for 3 events:
$$\begin{aligned}
P(S_1 \cup S_2 \cup S_3) &= (0.20 + 0.25 + 0.15) - (0.08 + 0.05 + 0.06) + 0.02 \\
&= 0.60 - 0.19 + 0.02 = 0.43
\end{aligned}$$

**b) ** Complete SLA compliance across all 3:
$$P(S_1' \cap S_2' \cap S_3') = 1 - P(S_1 \cup S_2 \cup S_3) = 1 - 0.43 = 0.57$$

**c) ** Only $S_2$ ($S_2 \cap S_1' \cap S_3'$):
$$\begin{aligned}
P(\text{Only } S_2) &= P(S_2) - P(S_1 \cap S_2) - P(S_2 \cap S_3) + P(S_1 \cap S_2 \cap S_3) \\
&= 0.25 - 0.08 - 0.06 + 0.02 = 0.13
\end{aligned}$$

**d) ** Exactly two microservices:
*   Only $S_1$ and $S_2$: $0.08 - 0.02 = 0.06$
*   Only $S_1$ and $S_3$: $0.05 - 0.02 = 0.03$
*   Only $S_2$ and $S_3$: $0.06 - 0.02 = 0.04$
Total = $0.06 + 0.03 + 0.04 = 0.13$.

**e) ** R Verification snippet:
```r
p1 <- 0.20; p2 <- 0.25; p3 <- 0.15
p12 <- 0.08; p13 <- 0.05; p23 <- 0.06
p123 <- 0.02

union_3 <- p1 + p2 + p3 - (p12 + p13 + p23) + p123
cat("Total Union Probability:", union_3, "\n")
```

**Final Answer:** **a) ** $\mathbf{0.43}$, **b) ** $\mathbf{0.57}$, **c) ** $\mathbf{0.13}$, **d) ** $\mathbf{0.13}$, **e) ** Verified via R.

#### Exercise 30: Circular Clock Rotation & Combinations with Replacement (Time-Domain) (Combined, Hardest + Gotcha)
**Problem:** A system clock rotates through 6 scheduling time slots $\{T_1, T_2, T_3, T_4, T_5, T_6\}$ arranged in a continuous circular ring.
**a) ** In how many distinct circular arrangements can 6 distinct server workers be assigned to these 6 time slots?
**b) ** A system administrator selects 4 execution tasks to assign across the 6 time slots. Tasks are identical, and any time slot can accept multiple tasks. How many ways can the 4 tasks be distributed?
**c) ** Suppose 2 specific slots $T_1$ and $T_2$ are critical windows. If 4 tasks are distributed randomly with replacement across the 6 slots (each slot equally likely for each task), what is the probability that AT LEAST ONE task is assigned to $T_1$?
**d) ** An analyst computes the average slot index for events occurring at slot $T_6$ ($23:00\text{ h}$) and slot $T_1$ ($01:00\text{ h}$) using arithmetic mean: $\bar{t} = (23 + 1)/2 = 12:00\text{ h}$. Identify the flaw in this calculation, state the gotcha, and compute the true circular mean time.
**e) ** Write an R command to compute the combinations with replacement count from part b.

**Solution:**
**a) ** Circular permutations of 6 distinct workers:
$$P_{\text{circular}} = (6 - 1)! = 5! = 120\text{ ways}$$

**b) ** Combinations with replacement: $n = 6$ categories (slots), $r = 4$ identical tasks.
$$C^R(6, 4) = \binom{6 + 4 - 1}{4} = \binom{9}{4} = \frac{9 \cdot 8 \cdot 7 \cdot 6}{4 \cdot 3 \cdot 2 \cdot 1} = 126\text{ ways}$$

**c) ** Complement: 0 tasks in $T_1$. For each task, probability of NOT choosing $T_1$ is $5/6$.
$$P(\text{0 in } T_1) = \left(\frac{5}{6}\right)^4 = \frac{625}{1296} \approx 0.48225$$
$$P(\text{at least 1 in } T_1) = 1 - \frac{625}{1296} = \frac{671}{1296} \approx 0.51775$$

**d) ** **Gotcha Analysis:**
**Gotcha:** Applying the naive arithmetic mean to cyclic/circular time data produces completely erroneous mid-day results ($12:00\text{ h}$) for events wrapping around midnight!
*Correct Circular Mean:* Convert hours $t_i$ to angles $\theta_i = \frac{2\pi \cdot t_i}{24}$:
*   $t_1 = 23\text{ h} \implies \theta_1 = \frac{23 \cdot 2\pi}{24} = \frac{23\pi}{12} \text{ rad} \equiv -\frac{\pi}{12} \text{ rad}$
*   $t_2 = 1\text{ h} \implies \theta_2 = \frac{1 \cdot 2\pi}{24} = \frac{\pi}{12} \text{ rad}$
Compute vector sums:
$$\bar{S} = \sin(-\pi/12) + \sin(\pi/12) = 0, \quad \bar{C} = \cos(-\pi/12) + \cos(\pi/12) = 2 \cos(\pi/12) > 0$$
$$\bar{\theta} = \text{atan2}(0, 2\cos(\pi/12)) = 0\text{ rad} \implies \bar{t} = \frac{24 \cdot 0}{2\pi} = 00:00\text{ h (Midnight)!}$$

**e) ** R Command for combinations with replacement:
```r
choose(6 + 4 - 1, 4)  # returns 126
```

**Final Answer:** **a) ** $\mathbf{120}$, **b) ** $\mathbf{126}$, **c) ** $\mathbf{671/1296 \approx 0.51775}$, **d) ** **Gotcha:** Arithmetic mean fails on cyclic time. True circular mean = $\mathbf{00:00\ h}$, **e) ** `choose(9, 4)`.

### R Implementation

R script for combinatorics calculations:

```r
# Combinations & Permutations in R
n <- 6; r <- 4

# Combinations without replacement nCr
nCr <- choose(n, r)

# Combinations with replacement (Stars & Bars)
nCr_rep <- choose(n + r - 1, r)

# Permutations nPr
nPr <- factorial(n) / factorial(n - r)

cat("nCr (no rep):", nCr, "\n")
cat("nCr (with rep):", nCr_rep, "\n")
cat("nPr:", nPr, "\n")
```

---

## Exam Preparation Guide

### Formula Quick-Reference

| Topic | General Formula | Time-Domain Adapted Formula | Typologio / Exam Style |
| :--- | :--- | :--- | :--- |
| **Complement Rule** | $P(A') = 1 - P(A)$ | $P(T > t) = 1 - P(T \le t)$ | $P(A') = 1 - P(A)$ |
| **Disjoint Addition** | $P(A \cup B) = P(A) + P(B)$ | $P(T \in [t_1,t_2] \cup [t_3,t_4]) = P_1 + P_2$ | $P(A \cup B) = P(A) + P(B)$ |
| **General Addition** | $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ | $P(L \cup D) = P(L) + P(D) - P(L \cap D)$ | $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ |
| **3-Event Incl.-Excl.** | $P(A \cup B \cup C) = \sum P_i - \sum P_{ij} + P_{123}$ | $P(\bigcup M_i) = \sum P(M_i) - \sum P_{ij} + P_{123}$ | $P(A \cup B \cup C) = \sum P(A) - \sum P(A \cap B) + P(A \cap B \cap C)$ |
| **De Morgan's 1st Law** | $P((A \cup B)') = P(A' \cap B')$ | $P(\text{Neither latency nor drop}) = 1 - P(L \cup D)$ | $P(A' \cap B') = 1 - P(A \cup B)$ |
| **De Morgan's 2nd Law** | $P((A \cap B)') = P(A' \cup B')$ | $P(\text{Not both delayed}) = 1 - P(L_1 \cap L_2)$ | $P(A' \cup B') = 1 - P(A \cap B)$ |
| **Only A Probability** | $P(A \cap B') = P(A) - P(A \cap B)$ | $P(L \cap D') = P(L) - P(L \cap D)$ | $P(A \cap B') = P(A) - P(A \cap B)$ |
| **Exactly One Event** | $P(A \cup B) - P(A \cap B)$ | $P(L \cup D) - P(L \cap D)$ | $P(A) + P(B) - 2P(A \cap B)$ |
| **Permutations** | $P(n, r) = \frac{n!}{(n-r)!}$ | $P(N_{\text{tasks}}, K_{\text{slots}}) = \frac{N!}{(N-K)!}$ | $P(n, r) = \frac{n!}{(n-r)!}$ |
| **Circular Perms** | $P_{\text{circ}} = (n-1)!$ | $P_{\text{circ}} = (N_{\text{workers}}-1)!$ | $P_{\text{circ}} = (n-1)!$ |
| **Combinations** | $C(n, r) = \binom{n}{r} = \frac{n!}{r!(n-r)!}$ | $C(N_{\text{servers}}, K_{\text{nodes}}) = \binom{N}{K}$ | $\binom{n}{r} = \frac{n!}{r!(n-r)!}$ |
| **Comb. with Replacement** | $C^R(n, r) = \binom{n+r-1}{r}$ | $C^R(N_{\text{slots}}, K_{\text{tasks}}) = \binom{N+K-1}{K}$ | $\binom{n+r-1}{r}$ |
| **Multinomial** | $\binom{n}{r_1, \dots, r_k} = \frac{n!}{r_1! \dots r_k!}$ | $\binom{N}{K_1, K_2, K_3} = \frac{N!}{K_1! K_2! K_3!}$ | $\frac{n!}{r_1! r_2! \dots r_k!}$ |

---

### Exam Checklist

| Category | Items |
| :--- | :--- |
| **Must Memorize** | - Kolmogorov's Axioms ($P(A) \ge 0, P(\Omega)=1, P(\bigcup A_i) = \sum P(A_i)$)<br>- General Addition Rule: $P(A \cup B) = P(A) + P(B) - P(A \cap B)$<br>- De Morgan's Laws: $(A \cup B)' = A' \cap B'$ and $(A \cap B)' = A' \cup B'$<br>- Permutation formula $P(n,r) = \frac{n!}{(n-r)!}$ and Combination formula $\binom{n}{r} = \frac{n!}{r!(n-r)!}$<br>- Circular Permutations formula: $(n-1)!$ |
| **Must Understand** | - Distinction between Mutually Exclusive ($A \cap B = \emptyset$) and Independent ($P(A \cap B) = P(A)P(B)$) events<br>- Translation of English phrases ("at least one", "exactly one", "neither", "only A") into Venn region logic<br>- Classical probability rule $P(A) = |A| / |\Omega|$ for equiprobable outcomes<br>- The 4-region and 8-region Venn partition completeness rules |
| **Book-Only (Professor May Test)** | - **Combinations with Replacement (Stars and Bars):** Formula $\binom{n+r-1}{r}$ for selecting identical items into categories<br>- **Multinomial Coefficient Partitioning:** Distributing $n$ items into $k$ specific group sizes $\frac{n!}{r_1! r_2! \dots r_k!}$<br>- **Continuous Single-Point Zero Probability:** $P(T = t_0) = 0$ for continuous latency variables<br>- **Circular Mean on Cyclic Clock Times:** Why naive arithmetic mean fails on $23:00$ and $01:00$ |

---

### Common Exam Traps

1.  **Mutually Exclusive vs. Independent Confusion:**
    *   *Trap:* Assuming that mutually exclusive events ($A \cap B = \emptyset$) are independent.
    *   *Fix:* If $A$ and $B$ are mutually exclusive with $P(A) > 0$ and $P(B) > 0$, then $P(A \cap B) = 0 \neq P(A)P(B)$. Mutually exclusive events are **strongly dependent**!
2.  **At Least One vs. Exactly One Complement Trap:**
    *   *Trap:* Computing $1 - P(A \cap B)$ when asked for "neither $A$ nor $B$".
    *   *Fix:* "Neither $A$ nor $B$" is $P(A' \cap B') = 1 - P(A \cup B)$. "At most one" is $1 - P(A \cap B)$.
3.  **Circular Permutations Rotation Shift Trap:**
    *   *Trap:* Using $n!$ instead of $(n-1)!$ for items arranged in a circle.
    *   *Fix:* Always subtract 1 to fix the rotational reference point when arrangements are circular.
4.  **Combinations with Replacement Index Shift ($n$ vs $r$):**
    *   *Trap:* Swapping $n$ (categories) and $r$ (items) in $\binom{n+r-1}{r}$.
    *   *Fix:* $n$ is the number of distinct destination bins/categories, while $r$ is the number of items being selected/distributed.
5.  **Axiom Non-Negativity Violation in Region Subtraction:**
    *   *Trap:* Subtracting $P(A \cap B)$ without checking if $P(A \cap B) \le P(A)$.
    *   *Fix:* Verify that joint probabilities never exceed marginal probabilities ($P(A \cap B) \le \min(P(A), P(B))$).

---

### Exam Paper Cross-References

| Exam Paper | Relevant Questions | Difficulty |
| :--- | :--- | :---: |
| [Exam_paper_Easy.md](file:///home/ice/Documents/CodeHub/GitHub-Projects/Public/DitOpenNotes/Year_2/Semester_4/PROBABILITY_STATISTICS/Exams/Papers/Exam_paper_Easy.md) | Question 3 (Disjoint events, independent events, set operations, De Morgan's Law $P(A' \cap B')$) | **1/5** |
| [Exam_paper_2024_09_06_Team_A.md](file:///home/ice/Documents/CodeHub/GitHub-Projects/Public/DitOpenNotes/Year_2/Semester_4/PROBABILITY_STATISTICS/Exams/Papers/Exam_paper_2024_09_06_Team_A.md) | Question 2 (Set theory definitions, mutually exclusive vs independent events, $P(A \cup B)$ addition rule) | **1/5** |
| [Exam_paper_2023_06_12_Team_null.md](file:///home/ice/Documents/CodeHub/GitHub-Projects/Public/DitOpenNotes/Year_2/Semester_4/PROBABILITY_STATISTICS/Exams/Papers/Exam_paper_2023_06_12_Team_null.md) | Question 2 (Venn diagram translation, union and complement probability) | **2/5** |
| [Exam_paper_2024_06_14_Team_B.md](file:///home/ice/Documents/CodeHub/GitHub-Projects/Public/DitOpenNotes/Year_2/Semester_4/PROBABILITY_STATISTICS/Exams/Papers/Exam_paper_2024_06_14_Team_B.md) | Question 2 (Set probability calculation, disjoint events and complement) | **2/5** |
| [Exam_paper_2026_06_09_Team_B.md](file:///home/ice/Documents/CodeHub/GitHub-Projects/Public/DitOpenNotes/Year_2/Semester_4/PROBABILITY_STATISTICS/Exams/Papers/Exam_paper_2026_06_09_Team_B.md) | Question 2 (Set theory operations, phrase translation "at least one", "neither") | **2/5** |
| [Exam_paper_Intermediate_2.md](file:///home/ice/Documents/CodeHub/GitHub-Projects/Public/DitOpenNotes/Year_2/Semester_4/PROBABILITY_STATISTICS/Exams/Papers/Exam_paper_Intermediate_2.md) | Question 2 (Algebraic proofs of set relationships and De Morgan's laws) | **3/5** |

---

## Phase Summary

Phase 2 builds the formal set-theoretic foundation of Probability Theory:

*   **Set Theory & Sample Spaces:** Random experiments are defined on sample spaces ($\Omega$). Events are subsets $A \subseteq \Omega$. Fundamental operations include Union ($A \cup B$, logical OR), Intersection ($A \cap B$, logical AND), and Complement ($A'$, logical NOT). Mutually exclusive events satisfy $A \cap B = \emptyset$. Continuous time spaces $\Omega = [0, T]$ carry zero single-point probability ($P(T = t_0) = 0$).
*   **Venn Diagrams & Phrase Translation:** Venn diagrams partition sample spaces into 4 mutually exclusive regions for 2 events ($A \cap B', A \cap B, A' \cap B, A' \cap B'$) or 8 regions for 3 events. The partition probabilities sum to 1. Natural language expressions map directly to set operations: "at least one" $\rightarrow A \cup B$, "neither" $\rightarrow (A \cup B)' = A' \cap B'$, "only A" $\rightarrow A \cap B' = A - (A \cap B)$, and "exactly one" $\rightarrow P(A) + P(B) - 2P(A \cap B)$.
*   **Kolmogorov Axioms & Probability Rules:** Probability assignments must satisfy Kolmogorov's Axioms: Non-negativity ($P(A) \ge 0$), Normalization ($P(\Omega) = 1$), and Countable Additivity for disjoint events. The General Addition Rule handles overlapping events: $P(A \cup B) = P(A) + P(B) - P(A \cap B)$. De Morgan's Laws push complements inside set operations: $(A \cup B)' = A' \cap B'$ and $(A \cap B)' = A' \cup B'$.
*   **Combinatorics & Counting Methods:** For equiprobable outcomes, $P(A) = |A| / |\Omega|$. The Product Rule multiplies sequential stage choices, while the Sum Rule adds disjoint options. Permutations ($P(n, r) = \frac{n!}{(n-r)!}$) count ordered arrangements. Circular Permutations ($(n-1)!$) account for rotational symmetry. Combinations ($C(n, r) = \binom{n}{r} = \frac{n!}{r!(n-r)!}$) count unordered selections. Combinations with Replacement ($C^R(n, r) = \binom{n+r-1}{r}$) use Stars and Bars. Multinomial coefficients ($\frac{n!}{r_1! \dots r_k!}$) partition $n$ items into distinct group sizes.
