# Process Scheduling (CPU Scheduling)

This document covers single-processor CPU scheduling — the mechanisms, criteria, policies, and algorithms that determine which process runs next on the CPU. It maps directly to Chapter 9 of the Operating Systems course. The subject is a Type C (Engineering/Applied Systems) topic, meaning formal definitions and step-by-step mechanisms precede all worked examples.

---

## 1. Introduction

**Scheduling** is the OS function that decides the order and timing by which processes access the CPU in a single-processor system.

**Primary goals:**
- Maximize **CPU utilization** — keep the CPU as busy as possible.
- Maximize **throughput** — number of processes completed per unit time.
- Minimize **response time** — time from request submission to first response.

> **[Key Insight]** These goals are often in direct conflict. Maximizing throughput may require long, uninterrupted CPU bursts, while minimizing response time requires frequent context switching.

---

## 2. Performance Evaluation Criteria

| Criterion | Definition | Unit | Direction |
| :--- | :--- | :--- | :--- |
| **Fairness** | Every process gets regular CPU access; avoids starvation | — | Maximize |
| **Utilization** | Fraction of time a device (CPU) is in use: $\frac{t_{use}}{t_{total}}$ | % | Maximize |
| **Throughput** | Number of processes completed per unit time | processes/s | Maximize |
| **Turnaround Time (TAT)** | Total elapsed time from submission to completion; includes waiting | seconds | Minimize |
| **Waiting Time (WT)** | Time spent waiting in the ready queue | seconds | Minimize |
| **Response Time (RT)** | Time from submission until the process first occupies the CPU | seconds | Minimize |
| **Context Switch Overhead** | Time wasted switching execution context between processes | seconds | Minimize |
| **Scheduling Complexity** | Time required to select the next process from the ready list | seconds | Minimize |

**Key relation:**

$$
\text{Waiting Time} = \text{Turnaround Time} - \text{Burst Length}
$$

---

## 3. Optimization Criteria

**Maximize:**
- CPU utilization
- Throughput

**Minimize:**
- Turnaround time
- Waiting time
- Response time

> **[Key Insight]** These criteria frequently conflict. Improving one often degrades another. No single algorithm is optimal for all workloads.

---

## 4. Types of Scheduling

Three levels of scheduling exist in a multiprogramming OS:

### 4.1 Long-Term Scheduling

- Determines whether a **new process is admitted** to the system (enters the ready queue) or waits.
- Controls the **degree of multiprogramming**.
- Admitting more processes: fewer suspensions, better CPU utilization, but lower throughput per process and more context switches.
- Tries to maintain a **balance** between CPU-bound and I/O-bound processes.

### 4.2 Medium-Term Scheduling

- Decides which processes are **swapped in or out of main memory** (disk ↔ RAM).
- Related to the `ready-suspended` and `blocked-suspended` process states.
- Candidates for removal from memory: processes idle for long, low-priority, generating many page faults, or consuming large amounts of memory.
- Performed by **memory management software**.

### 4.3 Short-Term Scheduling (CPU Scheduling)

- The **primary focus** of this chapter.
- Selects which **ready process runs next** on the CPU.
- Also called **dispatching**; the component performing this is the **dispatcher**.
- Triggered by:
  - Clock interrupts
  - I/O interrupts
  - OS calls
  - Signals

**Dispatcher latency:** The time required for the dispatcher to stop one process and start another.

### 4.4 Short-Term Criteria

| Orientation | Criteria |
| :--- | :--- |
| User-oriented | Response time, Turnaround time |
| System-oriented | CPU utilization, Fairness, Throughput |

---

## 5. Scheduling Policies

### 5.1 Non-Preemptive Scheduling

- Once a process is in the **running** state, it continues until it **terminates voluntarily** or **blocks itself** waiting for I/O.
- Results in long waiting and response times.
- Simple to implement.
- **Not suitable for multi-user systems.**

### 5.2 Preemptive Scheduling

- The OS can **interrupt a running process** and move it back to the ready state.
- Possible causes of preemption:
  - Arrival of a higher-priority process
  - An interrupt occurs
  - A process changes state
  - A time limit (quantum) is exceeded
- Prevents CPU monopolization.
- Can lead to **race conditions** — resolved using process synchronization.

---

## 6. CPU-I/O Burst Cycle

Every process alternates between **CPU bursts** (computation) and **I/O bursts** (waiting for I/O).

- CPU bursts are generally **much shorter** than I/O bursts.
- A process **terminates during a CPU burst**.
- **CPU-bound** processes: long CPU bursts, few I/O bursts.
- **I/O-bound** processes: short CPU bursts, many I/O bursts.

> **[Key Insight]** The scheduler always operates per CPU burst, not per complete process execution. The decision of which process runs is re-evaluated at each burst boundary.

---

## 7. Priority Scheduling

- Implemented via **multiple ready queues**, each representing a priority level.
- The scheduler always picks a process from the **highest non-empty priority queue**.
- Low-priority processes may suffer **indefinite starvation**.
- Processes may be allowed to **dynamically change priority** based on time in the system or execution history (aging).

---

## 8. Scheduling Algorithms

### 8.1 First-Come, First-Served (FCFS)

**Type:** Non-preemptive

**Mechanism:**
- Processes are executed in the **order of arrival** (FIFO queue).
- If two processes arrive simultaneously, order is arbitrary (random tie-break).
- A process runs until it **voluntarily suspends** itself.

**Properties:**

| Property | Value |
| :--- | :--- |
| Queue type | FIFO |
| Preemption | No |
| Selection speed | O(1), independent of queue length |
| Starvation risk | Low |
| Suitable for | Batch systems |

**Disadvantages:**
- CPU-bound processes **monopolize** the CPU.
- I/O-bound processes wait even after their I/O completes (they lose their queue position when they block).
- **High variance** in average turnaround time.
- Unsuitable for interactive or time-sharing systems.

---

### 8.2 Shortest-Job-First (SJF)

**Type:** Non-preemptive (base form); preemptive variant = SRTF

**Mechanism:**
- From the ready queue, select the process with the **smallest CPU burst time**.
- If two processes have equal burst times, FCFS tie-breaking applies.
- Each process **declares** its CPU burst time to the scheduler.

**Properties:**

| Property | Value |
| :--- | :--- |
| Preemption | No (standard SJF) |
| Optimality | Gives **minimum average waiting time** for a given set of processes |
| Starvation risk | **High** — long processes may never run if short ones keep arriving |
| Burst time required | Yes — generally hard to know in advance |

> **[Key Insight]** SJF is provably optimal for minimizing average waiting time. However, its practical applicability is limited because CPU burst times are rarely known in advance and must be estimated.

> **[Supplementary]**
> In practice, the next CPU burst is estimated using an **exponential average** of past bursts:
> $$
> \tau_{n+1} = \alpha \cdot t_n + (1 - \alpha) \cdot \tau_n
> $$
> where $t_n$ is the actual $n$-th burst, $\tau_n$ is the $n$-th estimate, and $\alpha \in [0,1]$ controls the weight of recent history. A common value is $\alpha = 0.5$.

---

### 8.3 Shortest Remaining Time First (SRTF)

**Type:** Preemptive variant of SJF

**Mechanism:**
- At every new process arrival, compare the **remaining burst time** of the current process with the **burst time of the new arrival**.
- If the new process has a shorter remaining time, **preempt** the current process and run the new one.
- Remaining time = total burst time − time already spent on CPU.

**Properties:**

| Property | Value |
| :--- | :--- |
| Preemption | Yes (on every new arrival) |
| Decision point | Process completes burst OR new process arrives |
| Response time | Excellent for short processes |
| Context switch overhead | High |
| Starvation risk | High for long processes |
| Multi-user suitability | Good |

> **[Key Insight]** When all processes arrive simultaneously, SRTF degenerates into SJF. The distinction only matters when processes have different arrival times.

---

### 8.4 Round Robin (RR)

**Type:** Preemptive

**Mechanism:**
- Each process receives a fixed **time quantum** (time slice), typically 10–100 ms.
- Queue order is FIFO; after a quantum expires, a clock interrupt fires and the process is moved to the **end** of the ready queue.
- If a process completes before its quantum expires, it releases the CPU voluntarily.

**Properties:**

| Property | Value |
| :--- | :--- |
| Preemption | Yes (quantum expiry) |
| Starvation | None |
| Suitable for | Time-sharing, interactive systems |
| Fairness | High |
| Context switch overhead | Depends on quantum size |

**Quantum Size Trade-off:**

| Quantum | Effect |
| :--- | :--- |
| Very small | Many context switches → excessive overhead |
| Very large | Degenerates to FCFS |
| Optimal guideline | Choose $q$ such that **80–90% of processes** complete their burst within one quantum |

**Criticism — CPU-bound vs. I/O-bound fairness:**
- CPU-bound processes use the **full quantum** and re-enter at the back of the queue.
- I/O-bound processes use only a **fraction** of the quantum, then block for I/O; when they unblock, they re-enter behind processes that had full quanta.
- This implicitly **favors CPU-bound** processes.

**Virtual Round Robin (Solution):**
- When an I/O operation completes, the unblocked process moves into an **auxiliary queue** that has priority over the main ready queue.
- The process is dispatched for at most: $q - t_{used}$ (the remainder of the quantum it was interrupted during).
- This ensures I/O-bound processes are not penalized for blocking.

---

## 9. Algorithm Comparison

| Algorithm | Preemptive | Avg. Waiting Time | Starvation | Best Use Case |
| :--- | :--- | :--- | :--- | :--- |
| FCFS | No | High (variable) | Rare | Simple batch systems |
| SJF | No | **Minimum** (optimal) | Yes (long jobs) | Batch, known burst times |
| SRTF | Yes | Near-minimum | Yes (long jobs) | Multi-user, short jobs dominant |
| RR | Yes | Medium | **No** | Interactive / time-sharing |

> **[Key Insight]** The best algorithm depends on system load, hardware support for the dispatcher, the relative weight of performance criteria, and the evaluation method used. No universally optimal algorithm exists.

---

## Solved Exercises

### Exercise 1: FCFS — Turnaround and Waiting Times

**Problem:**
Five processes arrive at time 0 in order P1, P2, P3, P4, P5 with burst times:

| Process | Burst Time |
| :--- | :--- |
| P1 | 10 |
| P2 | 1 |
| P3 | 2 |
| P4 | 1 |
| P5 | 5 |

Calculate turnaround and waiting times for FCFS.

**Solution:**

FCFS execution order (arrival order): P1 → P2 → P3 → P4 → P5

Completion times:
- P1 finishes at $t = 10$
- P2 finishes at $t = 11$
- P3 finishes at $t = 13$
- P4 finishes at $t = 14$
- P5 finishes at $t = 19$

Turnaround Time ($TAT = \text{completion} - \text{arrival}$, all arrive at 0):

| Process | Burst | TAT | WT = TAT − Burst |
| :--- | :--- | :--- | :--- |
| P1 | 10 | 10 | 0 |
| P2 | 1 | 11 | 10 |
| P3 | 2 | 13 | 11 |
| P4 | 1 | 14 | 13 |
| P5 | 5 | 19 | 14 |
| **Avg** | | **13.4** | **9.6** |

---

### Exercise 2: SJF (Non-Preemptive) — Same Process Set

**Problem:** Same 5 processes from Exercise 1, apply SJF (all arrive at $t = 0$).

**Solution:**

Sort by burst time: P2(1), P4(1), P3(2), P5(5), P1(10)

Execution: P2 → P4 → P3 → P5 → P1

| Process | Burst | Completion | TAT | WT |
| :--- | :--- | :--- | :--- | :--- |
| P2 | 1 | 1 | 1 | 0 |
| P4 | 1 | 2 | 2 | 1 |
| P3 | 2 | 4 | 4 | 2 |  
| P5 | 5 | 9 | 9 | 4 |
| P1 | 10 | 19 | 19 | 9 |
| **Avg** | | | **7.0** | **3.2** |

SJF reduces average waiting time from 9.6 (FCFS) to **3.2** — a significant improvement.

---

### Exercise 3: Round Robin (q = 1) — Same Process Set

**Problem:** Same 5 processes, RR with time quantum = 1 unit.

**Solution:**

Execution sequence (all arrive at 0, FIFO initial order P1–P5):
```
t=0:P1, t=1:P2, t=2:P3, t=3:P4, t=4:P5, t=5:P1, t=6:P3, t=7:P5, t=8:P1, t=9:P5,
t=10:P1, t=11:P5, t=12:P1, t=13:P5, t=14:P1, t=15:P1, t=16:P1, t=17:P1, t=18:P1
```

P2 completes at $t=2$, P4 at $t=4$, P3 at $t=7$, P5 at $t=14$, P1 at $t=19$.

| Process | Burst | TAT | WT |
| :--- | :--- | :--- | :--- |
| P1 | 10 | 19 | 9 |
| P2 | 1 | 2 | 1 |
| P3 | 2 | 7 | 5 |
| P4 | 1 | 4 | 3 |
| P5 | 5 | 14 | 9 |
| **Avg** | | **9.2** | **5.4** |

---

### Exercise 4: SJF vs. SRTF Comparison (Different Arrival Times)

**Problem:**

| Process | Arrival | Burst |
| :--- | :--- | :--- |
| P1 | 0 | 7 |
| P2 | 2 | 4 |
| P3 | 4 | 1 |
| P4 | 5 | 4 |

Compute average waiting time for SJF (non-preemptive) and SRTF.

**Solution — SJF (Non-Preemptive):**

At $t=0$: only P1 is ready → P1 runs until $t=7$.
At $t=7$: P2(4), P3(1), P4(4) are ready → select P3 (burst=1) → runs $t=7$ to $t=8$.
At $t=8$: P2(4), P4(4) → tie → select P2 → runs $t=8$ to $t=12$.
At $t=12$: P4(4) → runs $t=12$ to $t=16$.

Gantt: `P1(0-7) | P3(7-8) | P2(8-12) | P4(12-16)`

| Process | Arrival | Finish | TAT | WT = TAT − Burst |
| :--- | :--- | :--- | :--- | :--- |
| P1 | 0 | 7 | 7 | 0 |
| P2 | 2 | 12 | 10 | 6 |
| P3 | 4 | 8 | 4 | 3 |
| P4 | 5 | 16 | 11 | 7 |
| **Avg** | | | | **4.0** |

**Solution — SRTF (Preemptive):**

At $t=0$: P1 starts (remaining=7).
At $t=2$: P2 arrives (burst=4) < P1 remaining (5) → preempt P1. P2 runs.
At $t=4$: P3 arrives (burst=1) < P2 remaining (2) → preempt P2. P3 runs.
At $t=5$: P3 finishes. P4 arrives (burst=4). Compare P2 remaining (2) vs P4 (4) → P2 runs.
At $t=7$: P2 finishes. P1 remaining=5, P4=4 → P4 runs.
At $t=11$: P4 finishes. P1 remaining=5 → P1 runs.
At $t=16$: P1 finishes.

Gantt: `P1(0-2) | P2(2-4) | P3(4-5) | P2(5-7) | P4(7-11) | P1(11-16)`

| Process | Arrival | Finish | TAT | WT = TAT − Burst |
| :--- | :--- | :--- | :--- | :--- |
| P1 | 0 | 16 | 16 | 9 |
| P2 | 2 | 7 | 5 | 1 |
| P3 | 4 | 5 | 1 | 0 |
| P4 | 5 | 11 | 6 | 2 |
| **Avg** | | | | **3.0** |

SRTF achieves average WT = 3.0 vs SJF's 4.0, confirming SRTF's theoretical advantage.

---

### Exercise 5: FCFS — Exercise 2 from Lecture (5 Processes, Sequential Arrival)

**Problem:**

| Process | Arrival | Burst |
| :--- | :--- | :--- |
| A | 0 | 3 |
| B | 0 | 6 |
| C | 0 | 4 |
| D | 0 | 5 |
| E | 0 | 2 |

Apply FCFS. Compute average TAT.

**Solution:**

All arrive at $t=0$, executed in order A, B, C, D, E.

Gantt: `A(0-3) | B(3-9) | C(9-13) | D(13-18) | E(18-20)`

| Process | Finish | TAT |
| :--- | :--- | :--- |
| A | 3 | 3 |
| B | 9 | 9 |
| C | 13 | 13 |
| D | 18 | 18 |
| E | 20 | 20 |

$$
\text{Average TAT} = \frac{3 + 9 + 13 + 18 + 20}{5} = \frac{63}{5} = 12.6 \text{ time units}
$$

---

### Exercise 6: SJF — Exercise 2 from Lecture (Same 5 Processes)

**Problem:** Same 5 processes as Exercise 5. Apply SJF.

**Solution:**

Sort by burst: E(2), A(3), C(4), D(5), B(6)

Gantt: `E(0-2) | A(2-5) | C(5-9) | D(9-14) | B(14-20)`

| Process | Finish | TAT |
| :--- | :--- | :--- |
| E | 2 | 2 |
| A | 5 | 5 |
| C | 9 | 9 |
| D | 14 | 14 |
| B | 20 | 20 |

$$
\text{Average TAT} = \frac{2 + 5 + 9 + 14 + 20}{5} = \frac{50}{5} = 10 \text{ time units}
$$

---

### Exercise 7: RR — Exercise 2 from Lecture (q = 2)

**Problem:** Same 5 processes, all arrive at $t=0$. Apply RR with quantum $q = 2$.

**Solution:**

Initial order: A(3), B(6), C(4), D(5), E(2)

Step-by-step:
```
t=0-2:  A runs, A remaining=1
t=2-4:  B runs, B remaining=4
t=4-6:  C runs, C remaining=2
t=6-8:  D runs, D remaining=3
t=8-10: E runs, E remaining=0 → E DONE at t=10
t=10-11: A runs (1 remaining), A DONE at t=11
t=11-13: B runs, B remaining=2
t=13-15: C runs, C remaining=0 → C DONE at t=15
t=15-17: D runs, D remaining=1
t=17-19: B runs, B remaining=0 → B DONE at t=19
t=19-20: D runs (1 remaining), D DONE at t=20
```

| Process | Burst | Finish | TAT |
| :--- | :--- | :--- | :--- |
| A | 3 | 11 | 11 |
| B | 6 | 19 | 19 |
| C | 4 | 15 | 15 |
| D | 5 | 20 | 20 |
| E | 2 | 10 | 10 |

$$
\text{Average TAT} = \frac{11 + 19 + 15 + 20 + 10}{5} = \frac{75}{5} = 15 \text{ time units}
$$

> **[Key Insight]** For this particular workload, RR (q=2) performs worst on average TAT (15.0) compared to FCFS (12.6) and SJF (10.0). This is expected: RR is optimized for fairness and response time, not for minimizing TAT.

---

### Exercise 8: SRTF with Different Arrival Times

**Problem:**

| Process | Arrival | Burst |
| :--- | :--- | :--- |
| A | 0 | 3 |
| B | 2 | 6 |
| C | 4 | 4 |
| D | 6 | 5 |
| E | 8 | 2 |

Apply SRTF. Compute average TAT.

**Solution:**

Step-by-step (tracking remaining times):
- $t=0$: A starts (remaining=3)
- $t=2$: B arrives (6). A remaining=1. $1 < 6$ → A continues
- $t=3$: A finishes. B runs (remaining=6)
- $t=4$: C arrives (4). B remaining=5. $4 < 5$ → preempt B, run C
- $t=6$: D arrives (5). C remaining=2. $2 < 5$ → C continues
- $t=8$: C finishes. E arrives (2). B remaining=5, D remaining=5. $2 < 5$ → run E
- $t=10$: E finishes. B remaining=5, D remaining=5 → run B (arrived first)
- $t=15$: B finishes. D remaining=5 → run D
- $t=20$: D finishes.

Gantt: `A(0-3) | B(3-4) | C(4-6) | [B preempted] | C(6-8) | E(8-10) | B(10-15) | D(15-20)`

| Process | Arrival | Finish | TAT |
| :--- | :--- | :--- | :--- |
| A | 0 | 3 | 3 |
| B | 2 | 15 | 13 |
| C | 4 | 8 | 4 |
| D | 6 | 20 | 14 |
| E | 8 | 10 | 2 |

$$
\text{Average TAT} = \frac{3 + 13 + 4 + 14 + 2}{5} = \frac{36}{5} = 7.2 \text{ time units}
$$

This matches the lecture result directly.

---

## Exam Tip: Common Mistakes and Pattern Recognition

**1. Confusing TAT and WT:**

$$
WT = TAT - \text{Burst Time}
$$

TAT measures from submission to completion. WT measures only idle time in the ready queue. Never subtract arrival time from WT directly.

**2. SRTF preemption condition:**
Preemption occurs when `new_burst < current_remaining`, not `<=`. Equal remaining times do not cause preemption.

**3. SJF with simultaneous arrivals = SRTF:**
When all processes arrive at $t=0$, SRTF never preempts (no new arrivals during execution), so it gives identical results to SJF.

**4. RR quantum selection:**
If a quantum is larger than all burst times, RR = FCFS. Always check whether the quantum causes preemption for each process.

**5. Starvation:**
- FCFS: rarely starves (eventually every process runs).
- SJF/SRTF: **can starve** long processes if short ones keep arriving.
- RR: **never starves** (every process gets regular CPU time).
- Priority: **can starve** low-priority processes — solved by **aging** (gradually raising priority of waiting processes).

**6. Exam pattern — comparative table questions:**
Given a process set, you will almost always be asked to compute TAT and WT for 2–3 algorithms and compare their averages. Always draw the Gantt chart first; computing directly from tables is error-prone.
