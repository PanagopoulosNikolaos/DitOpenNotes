# Exam 8 — Operating Systems (Comprehensive Review)

**Department:** Computer Science & Telecommunications
**Duration:** 3 hours
**Maximum Score:** 100 units

---

> **Instructions:**
> The examination consists of two parts. **Part A** examines theory (50 units) and **Part B** examines the Unix laboratory through jsLinux (50 units). This examination covers **the entire** semester material. Answer **all** questions. The use of auxiliary materials is not permitted.

---

## PART A — THEORY (50 units)

*Topics: Comprehensive Review — All Chapters*

---

### A1. Multiple Choice Questions (16 units — 2 units each)

**Circle the letter of the correct answer.**

**1.** Which OS uses **monolithic** architecture (modular)?

- a) MINIX
- b) QNX
- c) Linux
- d) Windows NT (microkernel)

---

**2.** Which of the following is **not** a condition for mutual exclusion?

- a) Two processes cannot be in the critical section simultaneously
- b) A process outside the critical section can suspend another
- c) Deadlock avoidance
- d) Starvation avoidance

---

**3.** Which OS architecture category is characterized by **guaranteed response times**?

- a) Distributed systems
- b) Parallel SMP systems
- c) Real-Time systems
- d) Microkernel

---

**4.** If $Max=(5,2,3)$ and $Allocation=(2,1,1)$, what is $Need$?

- a) $(7,3,4)$
- b) $(3,1,2)$
- c) $(2,1,1)$
- d) $(5,2,3)$

---

**5.** What is the correct relationship between $WT$ (Waiting Time) and $TAT$ (Turnaround Time)?

- a) $WT = TAT + \text{burst}$
- b) $TAT = WT - \text{burst}$
- c) $WT = TAT - \text{burst}$
- d) $WT = TAT \times \text{burst}$

---

**6.** Which page replacement algorithm is not affected by **Belady's Anomaly**?

- a) FIFO
- b) LRU
- c) NRU (Not Recently Used)
- d) Random

---

**7.** In **Symmetric Multiprocessing (SMP)**, all processors:

- a) Have separate local memory
- b) Execute different copies of the OS
- c) Run an identical copy of the OS in shared memory
- d) Are routed by a master CPU

---

**8.** What is the **main advantage** of Paging over Dynamic Partitioning?

- a) Zero internal fragmentation
- b) Visible structure to the programmer
- c) Elimination of external fragmentation
- d) Variable unit size

---

### A2. Round Robin Questions — Concept Connection (10 units — 2 units each)

Circle the **one** correct answer.

**1.** Which of the following Unix commands is **fork()**?
a) Replaces a process's memory image with a new program
b) Creates a process clone
c) Terminates a process
d) Waits for a child process to terminate

**2.** What is the operating principle of the **Dekker algorithm** (1st attempt)?
a) Uses TAS (Test and Set)
b) Implements mutual exclusion through strict alternation
c) Disables interrupts
d) Uses semaphores

**3.** What does the **presence bit** represent in the page table?
a) Access permissions to the page
b) Whether the page is in physical memory
c) Whether the page has been modified
d) The frame number of the page

**4.** Which scheduling criterion does the **SJF algorithm maximize**?
a) Throughput only
b) Average CPU utilization
c) Minimum average waiting time
d) Fairness

**5.** Which definition corresponds to **recovery** from deadlock?
a) Breaking one of the 4 conditions before deadlock occurs
b) Monitoring state to avoid unsafe states
c) Terminating or rolling back processes after deadlock detection
d) Allowing allocation without verification

---

### A3. Scheduling Exercises (14 units)

Given:

| Process | Arrival | Burst |
|:---|:---|:---|
| P1 | 0 | 6 |
| P2 | 2 | 4 |
| P3 | 4 | 7 |
| P4 | 6 | 2 |

**1. (7 units) Round Robin, q = 2:**
Show a detailed Gantt chart. Calculate:
- Completion time for each process
- Turnaround Time for each process
- Waiting Time for each process
- Average Turnaround Time
- Average Waiting Time

**2. (7 units) SRTF (Shortest Remaining Time First):**
Show a detailed Gantt chart and calculate average Waiting Time and Turnaround Time. Compare with Round Robin results.

---

### A4. Development Questions (10 units — 5 units each)

**1.** Explain fully the **execution flow** that the OS follows when a **page fault** occurs. Mention each step from the moment the CPU produces the virtual address until the process restarts.

**2.** A system has 3 resource types A (4 instances), B (2 instances) and C (3 instances). Processes P1, P2, P3 have:

| | Allocation (A,B,C) | Max (A,B,C) |
|:---|:---|:---|
| P1 | (1,0,1) | (3,2,2) |
| P2 | (2,1,0) | (4,1,3) |
| P3 | (0,1,1) | (1,1,2) |

Available = (1,0,1). Check if there is a safe sequence. If not, which resource release by the system would lead to a safe state?

---

## PART B — Unix Laboratory / jsLinux (50 units)

---

> **jsLinux Environment:** Write **exactly** the commands. This section is a **comprehensive review** of the Unix laboratory.

---

### B1. Basic Commands — Comprehensive Review (10 units)

For each of the following commands, write the **syntax**, explain what it does, and give a practical **example** of execution in jsLinux:

| Command | Syntax | What it does | Example |
|:---|:---|:---|:---|
| `pwd` | | | |
| `ls -la` | | | |
| `mkdir -p` | | | |
| `cp -r` | | | |
| `mv` | | | |
| `rm -rf` | | | |
| `cat` | | | |
| `chmod 755` | | | |
| `grep` | | | |
| `wc -l` | | | |

---

### B2. Permissions — Complex Scenario (10 units)

**Scenario:** In jsLinux, managing a secure directory with permissions.

1. **(2 units)** Create a directory `~/secure_data` and a file `private.key` inside it.

2. **(3 units)** Set permissions so that **only the owner** can read and write `private.key`, and **no one else** has any access. Write the command and verify.

3. **(3 units)** Set permissions on the `secure_data` directory so that: owner rwx, group r-x, others ---. Verify.

4. **(2 units)** Explain why it is important to set strict permissions on sensitive files. What danger exists if a private key is world-readable?

---

### B3. Complex Wildcards, Pipes, and Redirection Usage (15 units)

**1. (5 units)** In jsLinux, create 10 files with commands: `file_01.log`, `file_02.log`, ..., `file_10.log` in `/tmp`. Then:
   a) Display only those with numbers from 1 to 5 (using wildcard)
   b) Delete files `file_08.log`, `file_09.log`, `file_10.log` using wildcards
   c) Verify that only 7 files remain

**2. (5 units)** Write a pipeline that:
   a) Takes the `.log` filenames in `/tmp`
   b) Sorts alphabetically
   c) Numbers the lines (hint: `nl` or `cat -n`)
   d) Saves the result to `file_index.txt`

**3. (5 units)** Write a pipeline that analyzes the `/etc/passwd` file:
   a) Extracts UIDs (3rd field)
   b) Filters only UIDs >= 1000 (hint: `awk -F: '$3>=1000'`)
   c) Sorts numerically
   d) Displays the largest UID
   Explain each part of the pipeline.

---

### B4. Comprehensive Exercise Scenario (15 units)

**Scenario:** Complete application of Unix skills in jsLinux — managing projects, files, and data.

**Part I — Organization (5 units):**

1. Create the structure: `~/os_final/{config,data,output,archive}`
2. Create files: `config/settings.conf`, `config/users.txt`
3. Write the names of three fictional users in `users.txt` (one per line)
4. Give permissions `600` to `settings.conf`

**Part II — Processing (5 units):**

1. Display the users from `users.txt` in alphabetical order
2. Use `wc` to count how many users exist
3. Copy `users.txt` to `archive` with name `users_backup_$(date +%Y%m%d).txt`
   *(Hint: In jsLinux date substitution may not be supported — use a simple name if needed)*
4. Redirect the sorted user list to `output/sorted_users.txt`

**Part III — Verification and Cleanup (5 units):**

1. Display the **complete directory tree** `~/os_final` with `ls -lR`
2. Find all `.txt` files in `~/os_final` with `find`
3. Display permissions of each file in `config` with `ls -l`
4. Create a symbolic link `~/latest_output` pointing to `~/os_final/output`
5. Verify the symbolic link with `ls -la ~/`

---

*Good luck in the semester!*