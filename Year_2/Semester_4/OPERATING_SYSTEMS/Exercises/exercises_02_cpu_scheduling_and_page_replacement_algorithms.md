# Exercises 02: CPU Scheduling and Page Replacement Algorithms

This practice problem set provides step-by-step solutions for calculating process scheduling Gantt charts (FCFS, SJF, Round Robin) and tracking virtual memory page faults across FIFO, Optimal, and LRU algorithms.

---

## Problem 1: Single-Processor CPU Scheduling Comparison

### Workload Specification
Consider five processes arriving at the times and requiring the CPU burst times listed below:

| Process | Arrival Time ($T_{\text{arr}}$) | Burst Time ($T_{\text{burst}}$) |
|---|---|---|
| $P_1$ | 0 | 8 |
| $P_2$ | 1 | 4 |
| $P_3$ | 2 | 9 |
| $P_4$ | 3 | 5 |
| $P_5$ | 4 | 2 |

Compute the Gantt chart, completion time, turnaround time, waiting time, and average waiting time under:
1. **First-Come, First-Served (FCFS)**
2. **Shortest Job First (SJF, Non-preemptive)**
3. **Round Robin (RR, Time Quantum $q = 3$)**

---

### Solution

#### Part 1: FCFS Scheduling
Processes execute strictly in order of arrival: $P_1 \to P_2 \to P_3 \to P_4 \to P_5$.
- Gantt Chart:
  - $[0 - 8]: P_1$
  - $[8 - 12]: P_2$
  - $[12 - 21]: P_3$
  - $[21 - 26]: P_4$
  - $[26 - 28]: P_5$
- Metrics Table:

| Process | Completion Time | Turnaround ($T_{\text{comp}} - T_{\text{arr}}$) | Waiting ($T_{\text{turn}} - T_{\text{burst}}$) |
|---|---|---|---|
| $P_1$ | 8 | $8 - 0 = 8$ | $8 - 8 = 0$ |
| $P_2$ | 12 | $12 - 1 = 11$ | $11 - 4 = 7$ |
| $P_3$ | 21 | $21 - 2 = 19$ | $19 - 9 = 10$ |
| $P_4$ | 26 | $26 - 3 = 23$ | $23 - 5 = 18$ |
| $P_5$ | 28 | $28 - 4 = 24$ | $24 - 2 = 22$ |

$$
\text{Average Waiting Time (FCFS)} = \frac{0 + 7 + 10 + 18 + 22}{5} = \frac{57}{5} = \mathbf{11.4}
$$

#### Part 2: Non-preemptive SJF Scheduling
- At $t=0$, only $P_1$ is available; runs to completion: $[0 - 8]: P_1$.
- At $t=8$, all processes $P_2, P_3, P_4, P_5$ have arrived.
  - Bursts: $P_5(2) < P_2(4) < P_4(5) < P_3(9)$.
  - Order: $P_5 \to P_2 \to P_4 \to P_3$.
- Gantt Chart:
  - $[0 - 8]: P_1$
  - $[8 - 10]: P_5$
  - $[10 - 14]: P_2$
  - $[14 - 19]: P_4$
  - $[19 - 28]: P_3$
- Metrics Table:

| Process | Completion Time | Turnaround Time | Waiting Time |
|---|---|---|---|
| $P_1$ | 8 | $8 - 0 = 8$ | 0 |
| $P_5$ | 10 | $10 - 4 = 6$ | $6 - 2 = 4$ |
| $P_2$ | 14 | $14 - 1 = 13$ | $13 - 4 = 9$ |
| $P_4$ | 19 | $19 - 3 = 16$ | $16 - 5 = 11$ |
| $P_3$ | 28 | $28 - 2 = 26$ | $26 - 9 = 17$ |

$$
\text{Average Waiting Time (SJF)} = \frac{0 + 4 + 9 + 11 + 17}{5} = \frac{41}{5} = \mathbf{8.2}
$$

---

## Problem 2: Virtual Memory Page Replacement

### Question
A process references the following page trace:
$$7, \ 0, \ 1, \ 2, \ 0, \ 3, \ 0, \ 4, \ 2, \ 3, \ 0, \ 3, \ 2$$
Assuming an allocated physical capacity of **3 frames**, initially empty:
Compute the total number of page faults under:
1. **FIFO**
2. **Optimal (OPT)**
3. **LRU**

### Solution

#### 1. FIFO (First-In, First-Out)
- 7: Fault [7, -, -]
- 0: Fault [7, 0, -]
- 1: Fault [7, 0, 1]
- 2: Fault (evicts oldest: 7) [2, 0, 1]
- 0: Hit [2, 0, 1]
- 3: Fault (evicts oldest: 0) [2, 3, 1]
- 0: Fault (evicts oldest: 1) [2, 3, 0]
- 4: Fault (evicts oldest: 2) [4, 3, 0]
- 2: Fault (evicts oldest: 3) [4, 2, 0]
- 3: Fault (evicts oldest: 0) [4, 2, 3]
- 0: Fault (evicts oldest: 4) [0, 2, 3]
- 3: Hit [0, 2, 3]
- 2: Hit [0, 2, 3]

**Total FIFO Page Faults:** $\mathbf{10}$ faults.

#### 2. Optimal (OPT)
- 7: Fault [7, -, -]
- 0: Fault [7, 0, -]
- 1: Fault [7, 0, 1]
- 2: Fault (evicts 7, never used again) [2, 0, 1]
- 0: Hit [2, 0, 1]
- 3: Fault (evicts 1, never used again) [2, 0, 3]
- 0: Hit [2, 0, 3]
- 4: Fault (evicts 0, used after 2 and 3) [2, 4, 3]
- 2: Hit [2, 4, 3]
- 3: Hit [2, 4, 3]
- 0: Fault (evicts 4) [2, 0, 3]
- 3: Hit [2, 0, 3]
- 2: Hit [2, 0, 3]

**Total OPT Page Faults:** $\mathbf{7}$ faults.

#### 3. LRU (Least Recently Used)
- 7: Fault [7, -, -]
- 0: Fault [7, 0, -]
- 1: Fault [7, 0, 1]
- 2: Fault (evicts least recently used: 7) [2, 0, 1]
- 0: Hit [2, 0, 1] (0 is now most recent)
- 3: Fault (evicts least recently used: 1) [2, 0, 3]
- 0: Hit [2, 0, 3]
- 4: Fault (evicts least recently used: 2) [4, 0, 3]
- 2: Fault (evicts least recently used: 3) [4, 0, 2]
- 3: Fault (evicts least recently used: 0) [4, 3, 2]
- 0: Fault (evicts least recently used: 4) [0, 3, 2]
- 3: Hit [0, 3, 2]
- 2: Hit [0, 3, 2]

**Total LRU Page Faults:** $\mathbf{9}$ faults.

