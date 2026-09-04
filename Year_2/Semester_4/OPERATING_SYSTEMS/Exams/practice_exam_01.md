# Practice Exam 01: Operating Systems (Course 402)

This practice examination tests both theoretical OS concepts (CPU scheduling, synchronization, deadlocks, virtual memory) and practical UNIX terminal commands, pipelines, and permission calculations.

**Duration:** 2 Hours  
**Total Points:** 100 Points  

---

## Part A: UNIX Systems and Terminal Pipelines (25 Points)

### Question 1 (15 Points)
A directory contains a web server log file `access.log` where the first field of each line is the client IP address.
1. Write a single-line shell pipeline to output the **top 3 most active IP addresses** along with their request counts, sorted in descending order of frequency.
2. Explain the purpose of each filter in your pipeline.
3. If an error occurred and the command generated error messages, how would you redirect those error messages to `errors.log` while keeping the standard output displayed on screen?

### Question 2 (10 Points)
A file `backup.sh` currently has permissions `-rwxr-x---`.
1. What is the octal permission value of this file?
2. What operations can the file owner, group members, and others perform on this file?
3. Write a single `chmod` command in octal notation to grant read and execute permissions to everyone, while maintaining write permission for the owner only.

---

## Part B: Process Management and CPU Scheduling (25 Points)

### Question 3 (25 Points)
Consider four processes arriving at the following times:

| Process | Arrival Time ($T_{\text{arr}}$) | Burst Time ($T_{\text{burst}}$) |
|---|---|---|
| $P_1$ | 0 | 7 |
| $P_2$ | 2 | 4 |
| $P_3$ | 4 | 1 |
| $P_4$ | 5 | 4 |

1. Draw the Gantt chart and compute the average waiting time for **First-Come, First-Served (FCFS)**.
2. Draw the Gantt chart and compute the average waiting time for **Shortest Remaining Time First (SRTF, preemptive)**.
3. Which algorithm achieves a lower average waiting time? Explain why.

---

## Part C: Concurrency and Deadlocks (25 Points)

### Question 4 (15 Points)
State the **Four Coffman Conditions** required for a deadlock to occur. For each condition, explain how an operating system designer can prevent deadlock by denying or preventing that condition from holding.

### Question 5 (10 Points)
Define the **Critical Section Problem**. What are the three mandatory requirements that any valid solution must satisfy? Explain the difference between **Deadlock** and **Starvation**.

---

## Part D: Virtual Memory and Paging (25 Points)

### Question 6 (15 Points)
Consider a memory system with $4 \text{ KB}$ page size and a 32-bit virtual address space.
1. How many bits are used for the page offset?
2. How many bits are used for the virtual page number?
3. If the Translation Lookaside Buffer (TLB) has a hit ratio of $95\%$, TLB lookup time is $2 \text{ ns}$, and main memory access time is $80 \text{ ns}$, calculate the Effective Memory Access Time (EMAT).

### Question 7 (10 Points)
Given the reference string:
$$1, \ 2, \ 3, \ 4, \ 1, \ 2, \ 5, \ 1, \ 2, \ 3, \ 4, \ 5$$
With an allocation of **3 physical frames** initially empty:
Compute the total number of page faults under the **FIFO** page replacement algorithm.

---

## Complete Solution and Grading Guide

### Solution to Part A

#### Question 1
1. **Pipeline:**
   ```bash
   awk '{print $1}' access.log | sort | uniq -c | sort -rn | head -n 3
   ```
2. **Filter Explanation:**
   - `awk '{print $1}'`: Extracts field 1 (client IP address).
   - `sort`: Sorts IPs alphabetically so duplicates are contiguous.
   - `uniq -c`: Counts occurrences of each unique consecutive IP.
   - `sort -rn`: Sorts counts numerically in reverse (descending) order.
   - `head -n 3`: Emits the top 3 highest count records.
3. **Error Redirection:**
   Append `2> errors.log` to the command.
*(15 Points: 6+6+3)*

#### Question 2
1. Octal: `rwx` = $7$, `r-x` = $5$, `---` = $0 \implies \mathbf{750}$.
2. Owner: read, write, execute. Group members: read, execute. Others: no access.
3. Desired permissions: `-rwxr-xr-x` ($7, 5, 5$). Command: `chmod 755 backup.sh`.
*(10 Points: 3+3+4)*

---

### Solution to Part B

#### Question 3
1. **FCFS Scheduling:**
   - Gantt: $[0 - 7]: P_1, \ [7 - 11]: P_2, \ [11 - 12]: P_3, \ [12 - 16]: P_4$.
   - Waiting Times:
     - $P_1: 0 - 0 = 0$
     - $P_2: 7 - 2 = 5$
     - $P_3: 11 - 4 = 7$
     - $P_4: 12 - 5 = 7$
   - Average Waiting Time: $\frac{0 + 5 + 7 + 7}{4} = \frac{19}{4} = \mathbf{4.75}$.
2. **SRTF Scheduling:**
   - $t=0$: $P_1$ runs (remaining: 7).
   - $t=2$: $P_2$ arrives (burst 4). $P_1$ remaining is 5. Since $4 < 5$, $P_2$ preempts $P_1$.
   - $t=4$: $P_3$ arrives (burst 1). $P_2$ remaining is 2. Since $1 < 2$, $P_3$ preempts $P_2$.
   - $t=5$: $P_3$ completes. $P_4$ arrives (burst 4). Ready: $P_2(2), P_4(4), P_1(5)$. $P_2$ resumes.
   - $t=7$: $P_2$ completes. Ready: $P_4(4), P_1(5)$. $P_4$ runs.
   - $t=11$: $P_4$ completes. $P_1$ resumes.
   - $t=16$: $P_1$ completes.
   - Gantt: $[0-2]: P_1, \ [2-4]: P_2, \ [4-5]: P_3, \ [5-7]: P_2, \ [7-11]: P_4, \ [11-16]: P_1$.
   - Waiting Times:
     - $P_1: (2 - 0) + (11 - 2) = 0 + 9 = 9$
     - $P_2: (2 - 2) + (5 - 4) = 0 + 1 = 1$
     - $P_3: 4 - 4 = 0$
     - $P_4: 7 - 5 = 2$
   - Average Waiting Time: $\frac{9 + 1 + 0 + 2}{4} = \frac{12}{4} = \mathbf{3.00}$.
3. **Comparison:** SRTF achieves a lower average waiting time ($3.00 < 4.75$). SRTF is provably optimal for minimizing average waiting time because running shorter remaining bursts first minimizes the accumulation of delay across all waiting processes.
*(25 Points)*

---

### Solution to Part C

#### Question 4
1. **Mutual Exclusion:** Make resources shareable where possible (e.g., read-only files).
2. **Hold and Wait:** Require processes to request all resources at once before execution, or release all held resources before requesting new ones.
3. **No Preemption:** If a process holding resources requests a resource that cannot be immediately allocated, preempt all resources currently held.
4. **Circular Wait:** Impose a strict global linear ordering on all resource types ($F: R \to \mathbb{N}$); require that processes request resources strictly in increasing order.
*(15 Points)*

#### Question 5
- **Three Requirements:** Mutual Exclusion, Progress, Bounded Waiting.
- **Deadlock vs. Starvation:** In deadlock, two or more processes are permanently blocked because each holds a resource the other needs; no process can ever proceed. In starvation (indefinite postponement), a process is runnable but continuously passed over in favor of other processes due to scheduling bias (e.g., low priority).
*(10 Points)*

---

### Solution to Part D

#### Question 6
1. Page size $= 4 \text{ KB} = 2^{12} \text{ bytes} \implies \mathbf{12 \text{ bits}}$ for offset.
2. Virtual page number: $32 - 12 = \mathbf{20 \text{ bits}}$.
3. EMAT calculation:
   $$\text{EMAT} = h \cdot (t_{\text{TLB}} + t_{\text{RAM}}) + (1 - h) \cdot (t_{\text{TLB}} + 2 \cdot t_{\text{RAM}})$$
   $$\text{EMAT} = 0.95 \cdot (2 + 80) + 0.05 \cdot (2 + 160) = 0.95 \cdot 82 + 0.05 \cdot 162 = 77.9 + 8.1 = \mathbf{86.0 \text{ ns}}$$
*(15 Points: 4+4+7)*

#### Question 7
FIFO trace with 3 frames:
1. `1`: Fault `[1, -, -]`
2. `2`: Fault `[1, 2, -]`
3. `3`: Fault `[1, 2, 3]`
4. `4`: Fault (evicts 1) `[4, 2, 3]`
5. `1`: Fault (evicts 2) `[4, 1, 3]`
6. `2`: Fault (evicts 3) `[4, 1, 2]`
7. `5`: Fault (evicts 4) `[5, 1, 2]`
8. `1`: Hit `[5, 1, 2]`
9. `2`: Hit `[5, 1, 2]`
10. `3`: Fault (evicts 1) `[5, 3, 2]`
11. `4`: Fault (evicts 2) `[5, 3, 4]`
12. `5`: Hit `[5, 3, 4]`

**Total Page Faults:** $\mathbf{9}$ faults.
*(10 Points)*

