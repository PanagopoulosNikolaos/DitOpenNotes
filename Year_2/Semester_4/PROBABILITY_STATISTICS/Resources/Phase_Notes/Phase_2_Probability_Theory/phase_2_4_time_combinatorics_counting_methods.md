# Phase 2.4 (Time): Combinatorics and Counting Methods for Time-Based Data

Combinatorial analysis provides the mathematical techniques for counting the number of elements in a set without listing them individually. In probability theory, when outcomes in a sample space $\Omega$ are equally likely, the probability of an event $A$ is:

$$P(A) = \frac{|A|}{|\Omega|} = \frac{\text{Number of favorable outcomes}}{\text{Total number of possible outcomes}}$$

When dealing with **time-based scenarios** -- scheduling tasks into time slots, arranging events in a timeline, selecting time intervals -- the counting methods below are essential for determining $|A|$ and $|\Omega|$.

---

## 1. Fundamental Principles of Counting (Time Context)

### 1.1 The Multiplication Rule (Product Rule)
If a time-based operation can be performed in $n_1$ ways, and for each of these a second operation can be performed in $n_2$ ways, and so on, then the sequence of $k$ operations can be performed in:

$$N = n_1 \cdot n_2 \cdot \dots \cdot n_k \text{ ways}$$

> **Time example:** A schedule has 3 time slots for the morning and 4 for the afternoon. Total ways to assign one morning and one afternoon slot: $3 \cdot 4 = 12$.

### 1.2 The Addition Rule (Sum Rule)
If a time-based operation can be performed in $n_1$ ways, and a second disjoint operation in $n_2$ ways, then the total number of ways to perform either is:

$$N = n_1 + n_2 \text{ ways}$$

> **Time example:** A task can be scheduled in 3 morning slots OR 4 afternoon slots (but not both). Total choices: $3 + 4 = 7$.

---

## 2. Permutations (Time Context)

A permutation is an ordered arrangement. The order of selection matters.

### 2.1 Permutations of Distinct Time Slots
The number of ways to arrange $n$ distinct time slots taken all at a time:

$$P(n, n) = n!$$

The number of ways to arrange $n$ distinct time slots taken $r$ at a time:

$$P(n, r) = \frac{n!}{(n-r)!}$$

> **Time example:** 5 tasks must be scheduled into 3 time slots (order matters). $P(5, 3) = 5!/(5-3)! = 60$ ways.

### 2.2 Permutations with Repetition (Identical Time Slots)
The number of distinct permutations of $n$ time slots of which $n_1$ are of one type, $n_2$ of another, etc.:

$$P(n; n_1, n_2, \dots, n_k) = \frac{n!}{n_1! \cdot n_2! \dots n_k!}$$

> **Time example:** A timeline has 10 slots: 5 are "busy", 3 are "idle", 2 are "maintenance". The number of distinct timeline arrangements: $\frac{10!}{5! \cdot 3! \cdot 2!} = 2520$.

---

## 3. Combinations (Time Context)

A combination is a selection without regard to order.

### 3.1 Combinations of Distinct Time Slots (Without Replacement)
$$C(n, r) = \binom{n}{r} = \frac{n!}{r!(n-r)!}$$

> **Time example:** Choose 3 time slots from 8 available slots for processing (order does not matter). $\binom{8}{3} = 56$ ways.

### 3.2 Combinations with Replacement
$$C^{R}(n, r) = \binom{n + r - 1}{r} = \frac{(n + r - 1)!}{r!(n - 1)!}$$

> **Time example:** Select 6 time intervals from 4 types (repetition allowed, order does not matter). $\binom{4+6-1}{6} = \binom{9}{6} = 84$ ways.

---

## 4. Partitions & Multinomial Coefficients (Time Context)

The number of ways to partition $n$ distinct time slots into $k$ groups of sizes $r_1, r_2, \ldots, r_k$:

$$\binom{n}{r_1, r_2, \dots, r_k} = \frac{n!}{r_1! \cdot r_2! \dots r_k!}$$

> **Time example:** Distribute 10 time slots among 3 servers: 5 to server A, 3 to server B, 2 to server C. $\binom{10}{5, 3, 2} = \frac{10!}{5! \cdot 3! \cdot 2!} = 2520$ ways.

---

## 5. Time-Specific Gotchas

### Gotcha 1: Order Matters vs. Order Does Not Matter in Scheduling

When tasks are assigned to **distinct time slots** (e.g., slot 1, slot 2, slot 3), the order matters -- use **permutations**. When tasks are assigned to a **set of time slots** without caring which task goes where (e.g., "select 3 slots for maintenance"), order does not matter -- use **combinations**.

### Gotcha 2: Time Slots Are Labeled, Not Identical

Time slots are inherently **labeled** (e.g., 9:00, 10:00, 11:00). This means selecting slot 9:00 and 10:00 is different from selecting 10:00 and 11:00. The labeling makes them distinct objects for combinatorial purposes, even if the duration of each slot is the same.

### Gotcha 3: Circular Time and Arrangements

When arranging events on a **circular timeline** (e.g., a 24-hour clock with repeating shifts), the circular permutation formula $(n-1)!$ applies, not $n!$. This is because rotations of the same arrangement are considered identical on a circle.

### Gotcha 4: Probability with Time-Based Counting

When computing $P(A) = |A|/|\Omega|$ for time-based problems, ensure both $|A|$ and $|\Omega|$ are counted using the **same method** (both permutations or both combinations). Mixing methods is the most common source of error.

---

## 6. Solved Exercises (10 Examples)

### Exercise 1: Time Slot Codes (Multiplication Rule)

**Problem:** A log entry contains 3 time fields: hour (0--23), minute (0--59), and second (0--59). How many distinct timestamps can be formed?

**Solution:**
- **Step 1: Define operations.**
  We have 3 slots to fill. Let $n_i$ represent the number of choices for slot $i$.
- **Step 2: WIP State.**
  - Hour: 24 choices
  - Minute: 60 choices
  - Second: ? choices
- **Step 3: Final Calculation.**
  - Second has 60 choices.
  - Total timestamps $= 24 \cdot 60 \cdot 60 = 86\,400$.

> **Interpretation:** There are 86,400 distinct second-level timestamps in a 24-hour day.

---

### Exercise 2: Selecting Time Slots for Maintenance (Combinations)

**Problem:** From 8 available hourly time slots, a maintenance team must choose 3 slots for system maintenance. How many ways can the slots be chosen?

**Solution:**
- **Step 1: Identify the model.**
  We select 3 slots from 8, where order does not matter (maintenance is the same regardless of which slot is "first").
- **Step 2: WIP State.**
  $$\binom{8}{3} = \frac{8!}{3! \cdot 5!} = \frac{8 \cdot 7 \cdot 6}{3 \cdot 2 \cdot 1} = \frac{336}{?}$$
- **Step 3: Final Calculation.**
  $$\text{Denominator} = 6$$
  $$\text{Total ways} = \frac{336}{6} = 56 \text{ ways.}$$

---

### Exercise 3: Arranging Tasks in a Timeline (Permutations)

**Problem:** There are 4 monitoring tasks, 3 backup tasks, and 2 cleanup tasks. In how many ways can they be arranged in a 9-slot timeline if tasks of the same type must be consecutive?

**Solution:**
- **Step 1: Treat groups as units.**
  We arrange the 3 task types (monitoring, backup, cleanup) first: $3!$ ways.
- **Step 2: WIP State.**
  Within each group:
  - Monitoring tasks: $4!$ ways.
  - Backup tasks: $3!$ ways.
  - Cleanup tasks: ? ways.
- **Step 3: Final Calculation.**
  - Cleanup arrangements $= 2! = 2$ ways.
  - Total arrangements $= 3! \cdot (4! \cdot 3! \cdot 2!) = 6 \cdot (24 \cdot 6 \cdot 2) = 6 \cdot 288 = 1728$.

---

### Exercise 4: Distributing Time Slots Among Servers (Multinomial)

**Problem:** In how many ways can 10 distinct time slots be distributed among 3 servers if server A receives 5 slots, server B receives 3 slots, and server C receives 2 slots?

**Solution:**
- **Step 1: Set up the partition.**
  This is a partition of $n=10$ objects into cells of sizes $r_1=5, r_2=3, r_3=2$.
- **Step 2: WIP State.**
  $$\binom{10}{5, 3, 2} = \frac{10!}{5! \cdot 3! \cdot 2!} = \frac{10 \cdot 9 \cdot 8 \cdot 7 \cdot 6 \cdot 5!}{5! \cdot (3 \cdot 2 \cdot 1) \cdot (2 \cdot 1)} = \frac{10 \cdot 9 \cdot 8 \cdot 7 \cdot 6}{?}$$
- **Step 3: Final Calculation.**
  $$\text{Denominator} = 6 \cdot 2 = 12$$
  $$\text{Numerator} = 30240$$
  $$\text{Total ways} = \frac{30240}{12} = 2520 \text{ ways.}$$

---

### Exercise 5: Timeline Permutations with Repeated Durations

**Problem:** How many distinct timelines can be formed by arranging 10 time intervals where 4 intervals are 1-second durations, 3 are 2-second durations, 2 are 5-second durations, and 1 is a 10-second duration?

**Solution:**
- **Step 1: Count interval frequencies.**
  Total intervals $n = 10$.
  Frequencies: 1s (4), 2s (3), 5s (2), 10s (1).
- **Step 2: WIP State.**
  $$\text{Total timelines} = \frac{10!}{4! \cdot 3! \cdot 2! \cdot 1!} = \frac{3\,628\,800}{?}$$
- **Step 3: Final Calculation.**
  $$\text{Denominator} = 24 \cdot 6 \cdot 2 \cdot 1 = 288$$
  $$\text{Total timelines} = \frac{3\,628\,800}{288} = 12\,600 \text{ timelines.}$$

---

### Exercise 6: Circular Scheduling (Round-the-Clock Shifts)

**Problem:** In how many ways can 6 servers be arranged in a circular 24-hour shift rotation? (Two arrangements are identical if each server has the same left and right neighbors.)

**Solution:**
- **Step 1: Identify circular permutation.**
  For circular permutations of $n$ distinct objects, fix one position to eliminate rotational equivalence, leaving $(n-1)!$ arrangements.
- **Step 2: WIP State.**
  $$\text{Arrangements} = (6 - 1)! = ?!$$
- **Step 3: Final Calculation.**
  $$5! = 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1 = 120 \text{ ways.}$$

> **Gotcha reminder:** On a circular timeline (24-hour shift cycle), rotations are identical. This is why we use $(n-1)!$ instead of $n!$.

---

### Exercise 7: Selecting Time Intervals with Repetition (Combinations with Replacement)

**Problem:** A system has 4 types of maintenance intervals (short, medium, long, extended). In how many ways can a technician select 6 intervals for a workday?

**Solution:**
- **Step 1: Identify model parameters.**
  We are selecting $r = 6$ intervals from $n = 4$ types, where order does not matter and repetition is allowed.
- **Step 2: WIP State.**
  $$\binom{n + r - 1}{r} = \binom{4 + 6 - 1}{6} = \binom{9}{6} = \frac{9!}{6! \cdot 3!} = \frac{9 \cdot 8 \cdot 7}{?}$$
- **Step 3: Final Calculation.**
  $$\text{Denominator} = 3 \cdot 2 \cdot 1 = 6$$
  $$\text{Total ways} = \frac{504}{6} = 84 \text{ ways.}$$

---

### Exercise 8: Pathfinding on a Time-Duration Grid

**Problem:** A project plan has 5 "development" phases and 4 "testing" phases, each taking one time unit. A path from start to finish moves only right (development) or up (testing). How many distinct paths exist from $(0,0)$ to $(5,4)$?

**Solution:**
- **Step 1: Translate to symbols.**
  Any path requires exactly 5 Right (R) moves and 4 Up (U) moves, totaling $n = 9$ moves.
- **Step 2: WIP State.**
  Choose which 5 of the 9 moves are R:
  $$\text{Paths} = \binom{9}{5} = \frac{9!}{5! \cdot 4!} = \frac{9 \cdot 8 \cdot 7 \cdot 6}{?}$$
- **Step 3: Final Calculation.**
  $$\text{Denominator} = 4 \cdot 3 \cdot 2 \cdot 1 = 24$$
  $$\text{Total paths} = \frac{3024}{24} = 126 \text{ paths.}$$

---

### Exercise 9: Probability of Execution Time Sum (Combinatorics for Probability)

**Problem:** Three tasks are randomly assigned execution times of 1, 2, 3, 4, 5, or 6 seconds each (independently, with equal probability). What is the probability that the total execution time is exactly 5 seconds?

**Solution:**
- **Step 1: Calculate $|\Omega|$.**
  Each task has 6 possible durations. For 3 tasks: $|\Omega| = 6^3 = 216$.
- **Step 2: WIP State.**
  Count the combinations $(t_1, t_2, t_3)$ such that $t_1 + t_2 + t_3 = 5\text{ s}$, where $1 \le t_i \le 6$.
  Possible partitions of 5 into 3 positive integers:
  - $\{3, 1, 1\}$: can occur as $(3,1,1)$, $(1,3,1)$, $(1,1,3)$ $\Rightarrow$ 3 ways.
  - $\{2, 2, 1\}$: can occur as $(2,2,1)$, $(2,1,2)$, $(1,2,2)$ $\Rightarrow$ ? ways.
- **Step 3: Final Calculation.**
  - There are 3 ways for $\{2, 2, 1\}$.
  - Total favorable outcomes $|A| = 3 + 3 = 6$.
  - Probability $= \frac{|A|}{|\Omega|} = \frac{6}{216} = \frac{1}{36} \approx 0.0278$.

---

### Exercise 10: R Snippet -- Counting Time Slot Arrangements

**Problem:** Use R to compute the number of ways to choose 3 time slots from 8 for maintenance, and the number of ways to arrange 5 tasks into 3 time slots.

**Solution:**

```r
# Combination: choose 3 slots from 8 (order does not matter)
choose(8, 3)

# Permutation: arrange 5 tasks into 3 slots (order matters)
factorial(5) / factorial(5 - 3)

# Multinomial: distribute 10 slots among servers (5, 3, 2)
factorial(10) / (factorial(5) * factorial(3) * factorial(2))

# Circular permutation: 6 servers in a round-the-clock rotation
factorial(6 - 1)
```

**Expected output:**
```
[1] 56        # choose(8, 3)
[1] 60        # P(5, 3)
[1] 2520      # multinomial(10; 5, 3, 2)
[1] 120       # circular: (6-1)!
```

> **R note:** The `choose()` function computes binomial coefficients $\binom{n}{r}$ directly. The `factorial()` function computes $n!$. For large $n$, use `lfactorial()` (log-factorial) to avoid numeric overflow.

---

## Exam Tip: Identifying the Counting Method for Time Problems

| Question Pattern | Method | Formula |
| :--- | :--- | :--- |
| "How many timelines?" (order matters, all distinct) | Permutation | $n!$ |
| "How many ways to arrange $r$ of $n$ time slots?" (order matters) | Permutation | $P(n,r) = \frac{n!}{(n-r)!}$ |
| "How many ways to choose $r$ time slots?" (order does not matter) | Combination | $\binom{n}{r}$ |
| "How many ways to choose $r$ intervals from $n$ types?" (repetition allowed) | Combination with replacement | $\binom{n+r-1}{r}$ |
| "How many ways to distribute $n$ slots into groups?" | Multinomial | $\frac{n!}{r_1! \cdot r_2! \dots r_k!}$ |
| "How many circular shift arrangements?" | Circular permutation | $(n-1)!$ |
| "Probability of a time sum?" | Count favorable + total, then divide | $P = \frac{|A|}{|\Omega|}$ |

> **Critical:** Always ask yourself: "Does the order of time slots matter?" If yes, use permutations. If no, use combinations. This single question resolves 90% of combinatorics confusion in time-based problems.