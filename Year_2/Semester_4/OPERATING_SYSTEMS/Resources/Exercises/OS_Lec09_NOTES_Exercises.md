# Exercises — Process Scheduling (CPU Scheduling)

**Based on:** `OS_Lec09_NOTES.md`  
**Number of exercises:** 38

---

## Part A — Theory

### Exercise 1
Define: turnaround time, waiting time, response time, throughput, CPU utilization.

---

### Exercise 2
Distinguish long-term, medium-term, short-term scheduling.

---

### Exercise 3
Distinguish preemptive and non-preemptive scheduling. Which algorithms belong to each category?

---

### Exercise 4
What is the CPU-I/O burst cycle? Why does it affect scheduling?

---

### Exercise 5
Explain priority scheduling and the starvation problem. What is aging?

---

### Exercise 6
Compare FCFS, SJF, SRTF, Round Robin (preemption, starvation, use case).

---

### Exercise 7
What is the time quantum in RR? What are the trade-offs of a small vs large quantum?

---

### Exercise 8
Why does RR favor CPU-bound over I/O-bound? What is Virtual Round Robin?

---

### Exercise 9
Why is SJF optimal for average waiting time but difficult in practice?

---

### Exercise 10
Give the exponential average formula for estimating the CPU burst: $\tau_{n+1} = \alpha t_n + (1-\alpha)\tau_n$.

---

## Part B — Computational Exercises (Arrival t=0)

### Exercise 11
**FCFS**

Processes P1–P5, burst: P1=1, P2=3, P3=4, P4=3, P5=1 (arrival 0, order P1..P5).

(a) Complete the Gantt chart.  
(b) Calculate turnaround, waiting, response for each.  
(c) Average waiting time.

---

### Exercise 12
**SJF (non-preemptive)** — same set of processes as Exercise 11.

(a) Gantt chart.  
(b) Response times.  
(c) Average response time.

---

### Exercise 13
**Round Robin, q=2** — same set.

(a) Gantt chart (per ms).  
(b) Waiting queue at each time instant (as in the 2023 exam).  
(c) Waiting times and average waiting time.

---

### Exercise 14
**Round Robin, q=1** — same set. Compare context switches with q=2.

---

### Exercise 15
**SRTF** — bursts P1=8, P2=4, P3=9, P4=5, arrival t=0.

Gantt chart and waiting times.

---

## Part C — Different Arrival Times

### Exercise 16
P1 burst=8 (t=0), P2 burst=4 (t=1), P3 burst=9 (t=2), P4 burst=5 (t=3).

(a) SJF non-preemptive — Gantt.  
(b) SRTF — Gantt.  
(c) Compare the waiting times of P1.

---

### Exercise 17
With the data of Exercise 16, RR with q=3. Calculate the response time of P2.

---

### Exercise 18
4 processes: P1(24), P2(3), P3(3), arrival 0. FCFS vs SJF — table of waiting times.

---

### Exercise 19
P1(10,t=0), P2(1,t=1), P3(2,t=2). SRTF: how many preemptions? Final average waiting?

---

## Part D — Comparison and Analysis

### Exercise 20
Mark **T** or **F**:

1. FCFS is preemptive.
2. SJF gives the minimum average waiting time for a given set.
3. RR does not cause starvation.
4. When all processes arrive simultaneously, SRTF = SJF.
5. A large quantum in RR makes it similar to FCFS.

---

### Exercise 21
Circle the correct answer: Which algorithm is suitable for interactive time-sharing?

- a) FCFS  
- b) SJF  
- c) Round Robin  
- d) Batch priority

---

### Exercise 22
Why does context switch overhead increase with a small quantum in RR?

---

### Exercise 23
**Optimization:** RR with q=100ms, bursts of 5ms. What problem do you observe?

---

### Exercise 24
Calculate $\tau_3$ if $\alpha=0.5$, $t_1=10$, $t_2=6$, $\tau_1=\tau_2=8$.

---

### Exercise 25
Complete the table:

| Algorithm | Preemptive | Starvation | Min avg waiting |
| :--- | :--- | :--- | :--- |
| FCFS | | | |
| SJF | | | |
| SRTF | | | |
| RR | | | |

---

### Exercise 26
**2023 exam scenario:** P1=1, P2=3, P3=4, P4=3, P5=1, SJF. Verify: response times 0,2,8,5,1 and average 3.2 ms.

---

### Exercise 27
**2023 exam scenario:** same processes, RR q=2. Verify waiting times and average 5.8 ms.

---

### Exercise 28
Waiting time = Completion - Arrival - Burst. Show the calculation for P2 in RR q=2 (Exercise 13).

---

### Exercise 29
Response time = time of first execution - arrival. Difference from waiting time?

---

### Exercise 30
5 processes, bursts 10,1,2,1,1. SJF. Which process suffers starvation if new processes with burst 1 keep arriving?

---

### Exercise 31
Priority: P1(prio 3, burst 10), P2(prio 1, burst 1), P3(prio 2, burst 2), non-preemptive. Gantt;

---

### Exercise 32
How does aging address starvation in priority scheduling?

---

### Exercise 33
**Exam tip:** Common mistakes — (a) forgetting preemption in SRTF, (b) wrong queue in RR. Give an example for each.

---

### Exercise 34
8 processes, bursts 6,8,7,3, only these 4. FCFS vs SJF — which has the smaller $\sum$ waiting?

---

### Exercise 35
RR q=4, bursts 24,3,3. How many times does P2 enter the queue? Compare with FCFS for the response of P2.

---

### Exercise 36
Choose the appropriate algorithm: (a) batch overnight jobs, (b) web server, (c) real-time with hard deadlines, (d) batch with known burst times.

---

### Exercise 37
Draw a Gantt chart for 3 processes with RR q=2 by hand and check the waiting: P1(5), P2(3), P3(1).

---

### Exercise 38
Combined exam exercise: 5 processes, bursts 2,1,8,4,5, arrival 0.

Calculate the average waiting for FCFS, SJF, RR(q=2) and compare which algorithm is preferred for batch vs interactive.
