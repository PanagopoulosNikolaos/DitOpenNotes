# Phase 2.1 (Time): Set Theory Fundamentals for Time-Based Events

Set Theory provides the mathematical language used to define and manipulate probability. Every probability problem is, at its core, a question about sets. When working with **time-based experiments** -- arrival times, timeout events, scheduling windows -- the sample space and events are defined in terms of **time intervals, timestamps, and temporal categories**.

---

## 1. Core Definitions (Time Context)

### Sample Space ($\Omega$)

The **Sample Space** $\Omega$ (also written $S$) is the set of **all possible outcomes** of a random experiment. For time-based experiments, outcomes are typically time values, time intervals, or temporal categories.

$$\Omega = \{ \text{all possible time-based outcomes} \}$$

**Key rule:** The sample space is always exhaustive (covers everything) and mutually exclusive (no outcome appears twice).

> **Time example:** If a server processes a request and the response time can be any value from 0 to 5 seconds, then $\Omega = [0, 5]\text{ s}$ (a continuous sample space).

### Event

An **Event** is any subset of the sample space. It is a collection of one or more time-based outcomes. We typically label events with capital letters $A$, $B$, $C$, etc.

$$A \subseteq \Omega$$

*   **Elementary event:** A single time outcome, e.g., $\{1.5\text{ s}\}$ -- a specific response time.
*   **Compound event:** A collection of time outcomes, e.g., $\{t : 1\text{ s} \le t < 2\text{ s}\}$ -- response times between 1 and 2 seconds.
*   **Impossible event ($\emptyset$):** The empty set. An event with no time outcomes that can never occur, e.g., "response time is negative."
*   **Certain event ($\Omega$):** The entire sample space. This event always occurs, e.g., "response time is between 0 and 5 seconds" when $\Omega = [0, 5]\text{ s}$.

---

## 2. Set Operations (Time Context)

These three operations are the building blocks of all probability expressions involving time events.

### Union ($\cup$)

The union $A \cup B$ is the event that **at least one** of $A$ or $B$ occurs. It contains every time outcome in $A$, every time outcome in $B$, or both.

$$A \cup B = \{ t \in \Omega : t \in A \text{ or } t \in B \}$$

> Think of $\cup$ as the logical **OR**.
>
> **Time example:** $A$ = "response time $< 100\text{ ms}$", $B$ = "response time $> 200\text{ ms}$". Then $A \cup B$ = "response time is either fast ($<100\text{ ms}$) or slow ($>200\text{ ms}$)".

### Intersection ($\cap$)

The intersection $A \cap B$ is the event that **both** $A$ and $B$ occur simultaneously. It contains only time outcomes that are in $A$ AND in $B$.

$$A \cap B = \{ t \in \Omega : t \in A \text{ and } t \in B \}$$

> Think of $\cap$ as the logical **AND**.
>
> **Time example:** $A$ = "response time $> 50\text{ ms}$", $B$ = "response time $< 150\text{ ms}$". Then $A \cap B$ = "response time is between 50 and 150 ms" = $(50, 150)\text{ ms}$.

### Complement ($A'$ or $A^c$)

The complement $A'$ is the event that $A$ does **not** occur. It contains all time outcomes in $\Omega$ that are not in $A$.

$$A' = \{ t \in \Omega : t \notin A \}$$

A fundamental identity:

$$A \cup A' = \Omega \quad \text{and} \quad A \cap A' = \emptyset$$

$$P(A') = 1 - P(A)$$

> **Time example:** If $A$ = "response time $< 100\text{ ms}$", then $A'$ = "response time $\ge 100\text{ ms}$" (the request was not fast).

---

## 3. Mutual Exclusivity (Disjoint Time Events)

Two time events $A$ and $B$ are **mutually exclusive** (or disjoint) if they cannot both occur at the same time:

$$A \cap B = \emptyset$$

> **Time example:** $A$ = "request arrives in the morning" and $B$ = "request arrives at night" are mutually exclusive -- a single request cannot arrive in both the morning and night categories simultaneously.

When $A$ and $B$ are mutually exclusive, the addition rule simplifies:

$$P(A \cup B) = P(A) + P(B) \quad \text{(only when } A \cap B = \emptyset \text{)}$$

---

## 4. Time-Specific Gotchas

### Gotcha 1: Continuous vs. Discrete Time Sample Spaces

Time data can be **continuous** (any real-valued duration, e.g., 1.234567 s) or **discrete** (time slots, e.g., hour 1, hour 2, hour 3). The set operations are the same, but the representation differs:

*   **Continuous:** $\Omega = [0, T]$, events are intervals like $[a, b)$.
*   **Discrete:** $\Omega = \{t_1, t_2, \ldots, t_k\}$, events are lists of specific time values.

### Gotcha 2: Overlapping Time Intervals

When defining events as time intervals, overlaps are easy to miss. For example, $A = [0, 100)\text{ ms}$ and $B = [50, 150)\text{ ms}$ overlap on $[50, 100)\text{ ms}$. The intersection $A \cap B = [50, 100)\text{ ms}$ is non-empty, so these events are **not** mutually exclusive.

### Gotcha 3: Cyclic Time and the Sample Space

For cyclic clock time (24-hour cycle), the sample space is $\Omega = [0, 24)\text{ h}$. Events like "between 22:00 and 02:00" **wrap around midnight**: $A = [22, 24) \cup [0, 2)$. This is a union of two intervals, not a single interval. Always check for wrap-around when defining time events on a clock.

---

## 5. Summary of Notation (Time Context)

| Notation | Read as | Time Meaning |
| :--- | :--- | :--- |
| $\Omega$ | Sample space | All possible time outcomes |
| $\emptyset$ | Empty set | Impossible time event |
| $A \cup B$ | A union B | Time outcome in A or B (at least one) |
| $A \cap B$ | A intersect B | Time outcome in both A and B |
| $A'$ | A complement | Time outcome not in A |
| $A \subseteq B$ | A is a subset of B | Every time outcome in A is also in B |
| $A \cap B = \emptyset$ | A and B are disjoint | A and B cannot both occur |

---

## 6. Solved Exercises (9 Examples)

### Exercise 1: Identifying the Sample Space (Response Time)

**Problem:** A server responds to a request in at most 5 seconds. The response time $T$ is measured. Define the sample space and the event $A$ = "response time greater than 3 seconds".

**Solution:**

$$\Omega = [0, 5]\text{ s}$$

$$A = (3, 5]\text{ s}$$

$$A' = [0, 3]\text{ s} \quad \text{(response time at most 3 seconds)}$$

---

### Exercise 2: Identifying the Sample Space (Two Time Slots)

**Problem:** A task is scheduled in one of two time slots: Morning (M) or Afternoon (A). Write out $\Omega$ using ordered pairs where the first element is the first task's slot and the second is the second task's slot. Define event $B$ = "at least one task is in the Morning".

**Solution:**

$$\Omega = \{(M,M), (M,A), (A,M), (A,A)\}$$

$$B = \{(M,M), (M,A), (A,M)\}$$

$$B' = \{(A,A)\} \quad \text{(both tasks in the Afternoon)}$$

---

### Exercise 3: Computing Union and Intersection of Time Events

**Problem:** From the response-time sample space $\Omega = [0, 10]\text{ s}$, let:
- $A$ = "response time less than 4 seconds" = $[0, 4)\text{ s}$
- $B$ = "response time greater than 3 seconds" = $(3, 10]\text{ s}$

Find $A \cup B$ and $A \cap B$.

**Solution:**

$$A \cup B = [0, 10]\text{ s} = \Omega \quad \text{(every response time is either < 4 or > 3)}$$

$$A \cap B = (3, 4)\text{ s} \quad \text{(response times between 3 and 4 seconds)}$$

> **Note:** $A$ and $B$ are **not** mutually exclusive because $A \cap B = (3, 4)\text{ s} \neq \emptyset$.

---

### Exercise 4: Computing the Complement of a Time Event

**Problem:** Using $A = [0, 4)\text{ s}$ from Exercise 3, find $A'$ and verify the fundamental identity.

**Solution:**

$$A' = [4, 10]\text{ s}$$

**Verification:**

$$A \cup A' = [0, 4) \cup [4, 10] = [0, 10] = \Omega \checkmark$$

$$A \cap A' = [0, 4) \cap [4, 10] = \emptyset \checkmark$$

---

### Exercise 5: Mutually Exclusive Time Events

**Problem:** A request can be classified by response time category: $A$ = "fast ($< 50\text{ ms}$)" and $B$ = "slow ($> 200\text{ ms}$)". Are $A$ and $B$ mutually exclusive?

**Solution:**

$$A = [0, 50)\text{ ms}, \quad B = (200, \infty)\text{ ms}$$

$$A \cap B = \emptyset$$

Yes, $A$ and $B$ are mutually exclusive. A single response cannot be both fast ($< 50\text{ ms}$) and slow ($> 200\text{ ms}$) simultaneously.

---

### Exercise 6: Three Time Events - Union and Intersection

**Problem:** A request is monitored across three time thresholds. Define:
- $A$ = "response time $< 100\text{ ms}$"
- $B$ = "response time $> 50\text{ ms}$"
- $C$ = "response time $< 200\text{ ms}$"

With $\Omega = [0, 500]\text{ ms}$, describe $A \cap B$, $A \cup C$, and $B \cap C'$.

**Solution:**

*   $A \cap B$ = "response time $< 100\text{ ms}$ AND $> 50\text{ ms}$" = $(50, 100)\text{ ms}$.
*   $A \cup C$ = "response time $< 100\text{ ms}$ OR $< 200\text{ ms}$" = $[0, 200)\text{ ms}$ (since $A \subseteq C$, the union is just $C$).
*   $C'$ = "response time $\ge 200\text{ ms}$" = $[200, 500]\text{ ms}$.
*   $B \cap C'$ = "response time $> 50\text{ ms}$ AND $\ge 200\text{ ms}$" = $[200, 500]\text{ ms}$.

---

### Exercise 7: Subset Relationship for Time Events

**Problem:** A response time $T$ is measured in $\Omega = [0, 10]\text{ s}$. Let:
- $A$ = "response time $< 1\text{ s}$" = $[0, 1)\text{ s}$
- $B$ = "response time $< 5\text{ s}$" = $[0, 5)\text{ s}$

Is $A$ a subset of $B$? What does this imply?

**Solution:**

Every time value in $A$ ($0 \le t < 1$) is also in $B$ ($0 \le t < 5$), so $A \subseteq B$.

This means: if event $A$ occurs (response time $< 1\text{ s}$), then event $B$ must also occur (response time $< 5\text{ s}$). A very fast response is automatically a fast response. Formally: $A \subseteq B \Rightarrow A \cap B = A$.

---

### Exercise 8: Complement of a Compound Time Event

**Problem:** Continuing from Exercise 7, find $(A \cup B)'$.

**Solution:**

First, compute the union:

$$A \cup B = [0, 5)\text{ s} = B \quad \text{(since } A \subseteq B \text{)}$$

The full sample space is $\Omega = [0, 10]\text{ s}$.

$$(A \cup B)' = B' = [5, 10]\text{ s} \quad \text{(response time at least 5 seconds)}$$

This is the set of outcomes where neither event $A$ nor event $B$ occurs -- the response was not fast. This connects to De Morgan's Law: $(A \cup B)' = A' \cap B'$, which will be covered in Phase 2.3.

---

### Exercise 9: Cyclic Time Event (Wrap-Around Midnight)

**Problem:** A maintenance window is defined as "between 22:00 and 02:00" on a 24-hour clock. Express this event as a set on $\Omega = [0, 24)\text{ h}$.

**Solution:**

The event wraps around midnight, so it is a **union of two intervals**:

$$A = [22, 24) \cup [0, 2) \text{ (hours)}$$

The complement (no maintenance) is:

$$A' = [2, 22) \text{ (hours)}$$

> **Gotcha reminder:** A naive single-interval representation like $[22, 2)$ is invalid because $22 > 2$ in linear order. Cyclic time events that cross midnight must be split into two intervals.

---

## Exam Tip: Listing vs. Describing Time Events

In exam problems, you may be asked to either **list** the time outcomes of an event (e.g., $A = [0, 100)\text{ ms}$) or **describe** it in words (e.g., "response time less than 100 ms"). Practise translating freely between both forms. The most common error is forgetting to account for overlapping time intervals when computing unions -- always check whether two time ranges share a common sub-interval before listing the union.