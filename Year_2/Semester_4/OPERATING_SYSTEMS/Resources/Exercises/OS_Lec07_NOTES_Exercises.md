# Exercises — Chapter 7: Memory Management

**Based on:** `OS_Lec07_NOTES.md`  
**Number of exercises:** 32

---

## Part A — Theory

### Exercise 1
What is the role of the memory manager and what five main responsibilities does it have?

---

### Exercise 2
Distinguish contiguous and non-contiguous memory allocation.

---

### Exercise 3
Explain uniprogramming: advantages, disadvantages, use of overlays.

---

### Exercise 4
Why was memory management for multiprogramming developed?

---

### Exercise 5
Give the CPU utilization formula and explain the $p_i$ (percentage of time of process i on the CPU).

---

### Exercise 6
What is internal and external fragmentation?

---

### Exercise 7
Distinguish fixed-size partitioning (equal vs unequal segments) and dynamic partitioning.

---

### Exercise 8
Explain swapping: what is transferred, when, which scheduler is involved.

---

## Part B — Placement Algorithms

### Exercise 9
Describe First-Fit, Best-Fit, Next-Fit. What are the advantages/disadvantages?

---

### Exercise 10
Why can Best-Fit leave many small unusable holes?

---

### Exercise 11
What are the limitations of swapping (e.g., multiprogramming, pinned pages)?

---

## Part C — Computational Exercises

### Exercise 12
**CPU Utilization:** 3 processes, each needs 20% CPU. $n=2$ processes in memory. Calculate the CPU utilization.

---

### Exercise 13
**CPU Utilization:** 4 processes with $p_1=0.1$, $p_2=0.2$, $p_3=0.3$, $p_4=0.4$. Degree of multiprogramming $n=3$. Calculate $1 - (1-p_1)(1-p_2)(1-p_3)$.

---

### Exercise 14
**Internal fragmentation:** 4KB partitions. A 2.5KB process. How many bytes are wasted per process? For 10 processes?

---

### Exercise 15
**Equal partitions:** 1MB memory, 4 equal partitions. Maximum number of processes? Maximum process size per partition?

---

### Exercise 16
**Dynamic partitioning — First-Fit**

Initial memory: one 640KB block. Requests (in order): 100, 170, 40, 190, 20, 500, 160, 104 (in KB). Draw the state after each request.

---

### Exercise 17
With the same data as Exercise 16, apply **Best-Fit**.

---

### Exercise 18
With the same data, apply **Next-Fit** (starting from the beginning).

---

### Exercise 19
After Exercise 16, the 160KB process is released. How many holes are there? Which algorithm is most affected by external fragmentation?

---

### Exercise 20
**Trade-offs:** The degree of multiprogramming increases. Describe the impact on throughput, response time, swapping overhead.

---

## Part D — True/False and Complex

### Exercise 21
Mark **T** or **F**:

1. In uniprogramming, memory is used efficiently for multiprogramming.
2. Overlays allow programs larger than physical memory.
3. Internal fragmentation occurs in fixed partitioning.
4. Swapping transfers the entire process to disk.
5. Next-Fit starts the search from the last successful placement.

---

### Exercise 22
Circle the correct answer: Which algorithm selects the **smallest** sufficient hole?

- a) First-Fit  
- b) Best-Fit  
- c) Worst-Fit  
- d) Next-Fit

---

### Exercise 23
Explain why unequal fixed partitions reduce internal fragmentation for mixed workloads.

---

### Exercise 24
Scenario: 256KB memory, processes of 50KB, 120KB, 30KB, 80KB. Equal partitioning of 64KB is used. How many fit? How much internal fragmentation?

---

### Exercise 25
How does the medium-term scheduler relate to swapping?

---

### Exercise 26
Complete:

| Strategy | Internal fragmentation | External fragmentation |
| :--- | :--- | :--- |
| Fixed equal | | |
| Dynamic | | |

---

### Exercise 27
Why does dynamic partitioning not fully solve the problem of programs larger than memory?

---

### Exercise 28
**Overlays:** A 200KB program, 100KB memory, modules 60KB+80KB+70KB (only one module at a time). Is it feasible? Describe.

---

### Exercise 29
Calculate CPU util for uniprogramming with I/O: CPU 0.0001s, I/O read 0.0015s, I/O write 0.0015s per record.

---

### Exercise 30
Compare the trade-off: degree of multiprogramming = 1 vs n = all processes in memory.

---

### Exercise 31
Describe how the choice of placement algorithm affects hole search time.

---

### Exercise 32
Exam scenario: 5 memory requests, 3 releases, give the final hole state for First-Fit and Best-Fit (create your own sizes and solve).
