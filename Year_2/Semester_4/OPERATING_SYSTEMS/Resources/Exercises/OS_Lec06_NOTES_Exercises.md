# Exercises — Chapter 6: Deadlock

**Based on:** `OS_Lec06_NOTES.md`  
**Number of exercises:** 35

---

## Part A — Basic Concepts

### Exercise 1
Define deadlock. Why does it occur in multiprogramming systems?

---

### Exercise 2
Distinguish preemptable and non-preemptable resources. Give two examples for each.

---

### Exercise 3
Distinguish reusable and consumable resources.

---

### Exercise 4
Describe the resource usage cycle: request, use, release.

---

### Exercise 5
Explain the classic deadlock pattern: P holds A requests B, Q holds B requests A.

---

## Part B — Graphs and Conditions

### Exercise 6
Explain the allocation graph notation: $P_i \rightarrow R_j$ and $R_j \rightarrow P_i$.

---

### Exercise 7
If the graph **does not** contain a cycle, is there a deadlock? If it contains a cycle and one instance per resource type?

---

### Exercise 8
State and explain the **4 necessary conditions** for deadlock.

---

### Exercise 9
For deadlock prevention, which condition must be violated? Give one technique for each.

---

### Exercise 10
Explain breaking circular wait by increasing resource order ($R_1 < R_2 < R_3$).

---

## Part C — Handling Strategies

### Exercise 11
Compare prevention, avoidance, detection & recovery, manual intervention.

---

### Exercise 12
What is a safe vs unsafe state in the context of avoidance?

---

### Exercise 13
Define: $Need[i,j] = Max[i,j] - Allocation[i,j]$. Why is the Max matrix needed?

---

### Exercise 14
Describe the steps of the safety algorithm.

---

### Exercise 15
What is the difference between detection and the safety algorithm?

---

### Exercise 16
State four recovery strategies when a deadlock is detected.

---

### Exercise 17
State five criteria for selecting a process to terminate.

---

## Part D — Dining Philosophers

### Exercise 18
Describe the dining philosophers problem. What does it model?

---

### Exercise 19
Why does the naive solution with wait(fork[i]) wait(fork[i+1]) lead to deadlock?

---

### Exercise 20
State three avoidance techniques (extra fork, max 4 philosophers, odd/even).

---

### Exercise 21
Explain the solution with the semaphore `room=4`. Why does it break circular wait?

---

## Part E — Numerical Exercises

### Exercise 22
Available memory of 200KB. $P_1$ requests 80KB then 60KB. $P_2$ requests 70KB then 80KB. If the initial requests are satisfied first, explain why they block.

---

### Exercise 23
**Banker's Algorithm — Safety**

Suppose 3 processes, 1 resource type (tape drives):

| | Max | Allocation |
| :--- | :--- | :--- |
| P0 | 7 | 0 |
| P1 | 3 | 2 |
| P2 | 9 | 2 |

Available = 3. Is there a safe sequence? Calculate Need and show the steps.

---

### Exercise 24
With the data of Exercise 23, can a request for 1 additional drive by P0 be granted? Apply the safety check.

---

### Exercise 25
Draw an allocation graph for: P1 → R1 (request), R2 → P1 (allocation), P2 → R2 (request), R1 → P2 (allocation). Is there a cycle?

---

### Exercise 26
Mark **T** or **F**:

1. A cycle in a graph always means deadlock.
2. Memory is usually a preemptable resource.
3. A printer is a non-preemptable resource.
4. Prevention with a printer daemon violates mutual exclusion.
5. An unsafe state means certain deadlock.

---

### Exercise 27
Circle the correct answer: Which approach allows allocations and periodically checks whether a deadlock exists?

- a) Prevention  
- b) Avoidance  
- c) Detection & recovery  
- d) Ignore

---

### Exercise 28
Explain why the requirement "all resources in advance" (hold and wait prevention) reduces resource utilization.

---

### Exercise 29
Scenario: 4 processes, 2 printers. Each process needs 1 printer for printing and 1 scanner (unique) for scanning. Can deadlock occur? Draw it.

---

### Exercise 30
Complete the table:

| Concept | Brief definition |
| :--- | :--- |
| Mutual exclusion | |
| Hold and wait | |
| No preemption | |
| Circular wait | |

---

### Exercise 31
How does deadlock relate to incorrect semaphore usage (from the mutual exclusion chapter)?

---

### Exercise 32
Avoidance vs Detection: which has greater runtime overhead and why?

---

### Exercise 33
**Exam scenario:** P holds a printer, waits for a file. Q holds a file, waits for a printer. Which conditions hold? Is it a deadlock?

---

### Exercise 34
Propose a prevention solution for a scenario of two processes and two non-preemptable resources A, B.

---

### Exercise 35
Compare starvation and deadlock in the philosophers problem. Can one exist without the other?
