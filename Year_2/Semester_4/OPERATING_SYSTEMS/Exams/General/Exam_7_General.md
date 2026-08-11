# Exam 7 — Operating Systems

**Department:** Computer Science & Telecommunications
**Duration:** 3 hours
**Maximum Score:** 100 units

---

> **Instructions:**
> The examination consists of two parts. **Part A** examines theory (50 units) and **Part B** examines the Unix laboratory through jsLinux (50 units). Answer **all** questions. The use of auxiliary materials is not permitted.

---

## PART A — THEORY (50 units)

*Topics: Process Scheduling — FCFS, SJF, SRTF, Round Robin*

---

### A1. Multiple Choice Questions (10 units — 2 units each)

**Circle the letter of the correct answer.**

**1.** Which scheduling algorithm guarantees **zero starvation** probability?

- a) SJF
- b) SRTF
- c) Round Robin
- d) FCFS

---

**2.** What happens in the Round Robin algorithm if the **time quantum** becomes very large?

- a) The number of context switches increases
- b) It degenerates to FCFS
- c) It degenerates to SJF
- d) Starvation appears

---

**3.** Which definition corresponds to **Turnaround Time**?

- a) Time from request to first execution
- b) Time waiting in the ready queue
- c) Total time from submission to completion
- d) CPU burst execution time

---

**4.** Which algorithm **bypasses** the arrival order to select the process with the shortest execution time?

- a) FCFS
- b) Round Robin
- c) SJF
- d) POSIX scheduler

---

**5.** What does **Virtual Round Robin** (VRR) address?

- a) Starvation of low-priority processes
- b) Unfairness to I/O-bound processes that leave the CPU early
- c) High context switch cost
- d) Inability to execute in multiprocessor systems

---

### A2. Round Robin Questions (8 units — 2 units each)

**1.** The **long-term scheduler** decides:
a) Which process executes next
b) Whether a new process enters the system
c) Which processes are transferred to disk
d) How much time quantum each process receives

**2.** Which evaluation criterion does the **SJF algorithm minimize**?
a) Throughput
b) Average response time
c) Average waiting time
d) Context switch time

**3.** What is the main **weakness** of FCFS for interactive systems?
a) It does not support multiple queues
b) CPU-bound processes monopolize the CPU, leaving I/O-bound processes waiting
c) It cannot execute more than 10 processes
d) It requires knowledge of burst times in advance

**4.** The **medium-term scheduler** is mainly associated with:
a) CPU scheduling
b) Swapping — transferring processes between RAM and disk
c) Creating new processes
d) Deadlock detection

---

### A3. Scheduling Exercises (22 units)

Given the following processes:

| Process | Arrival Time | CPU Time (burst) |
|:---|:---|:---|
| P1 | 0 | 8 |
| P2 | 1 | 4 |
| P3 | 2 | 9 |
| P4 | 3 | 5 |

**1. (5 units) FCFS (Non-Preemptive):**
Show the **Gantt chart**, calculate for each process: completion time, turnaround time, waiting time. Calculate average turnaround time and average waiting time.

**2. (6 units) SJF (Non-Preemptive):**
Show the **Gantt chart** and calculate average turnaround time and waiting time. Compare with FCFS.

**3. (6 units) SRTF (Preemptive SJF):**
Show the **Gantt chart** — at each new arrival compare the remaining time. Calculate average turnaround time and waiting time.

**4. (5 units) Round Robin with quantum q = 3:**
Show the **Gantt chart** by quantum. Calculate average turnaround time and waiting time.

---

### A4. Development Question (10 units)

A university system manages three categories of jobs:
- **Batch jobs** (compilation, running large programs) — CPU-bound
- **Interactive jobs** (shell commands, editor) — I/O-bound, small bursts
- **Real-time jobs** (medical measurement request) — strict deadlines

a) **(4 units)** Which scheduling algorithm or combination of algorithms do you recommend for each category? Justify.

b) **(3 units)** How does **quantum selection** in Round Robin affect system performance? What is the practical guideline?

c) **(3 units)** What is **dispatcher latency** and where does it appear in the context switch cycle?

---

## PART B — Unix Laboratory / jsLinux (50 units)

---

> **jsLinux Environment:** Write **exactly** the commands you would use.

---

### B1. Process Management in Unix (15 units)

**1. (5 units)** In jsLinux, execute the following commands and explain what they display:
   a) `ps` — which columns do you see? What do PID, TTY, TIME, CMD mean?
   b) `ps aux` (if supported) — what additional information does it display?
   c) What is **PID** and which PID does the first process (init/systemd) always have?

**2. (5 units)** Explain the following regarding job execution in Unix terminal:
   a) What happens if you terminate a command with `Ctrl+C`?
   b) What does `Ctrl+Z` do?
   c) What is the difference between execution in **foreground** and **background** (`&`)?
   d) How do you bring a process from background to foreground?

**3. (5 units)** Write commands for:
   a) Executing `sleep 100` in the background
   b) Displaying background jobs
   c) Terminating the background `sleep` process by PID (assume PID=1234)

---

### B2. I/O Redirection — Complex Scenarios (15 units)

**1. (5 units)** In a script (command sequence), you want to record **both standard output and errors** in separate files. Write:
   a) A command that sends stdout to `out.log` and stderr to `err.log`
   b) A command that sends both stdout and stderr to one file `all.log`
   c) Explain the meaning of the expression `2>&1`

**2. (5 units)** jsLinux provides `/dev/null`. Explain:
   a) What `/dev/null` is
   b) Why `command > /dev/null 2>&1` is often used
   c) Give a practical example where this is useful

**3. (5 units)** Create a file `/tmp/test_data.txt` with 10 lines of numbers (using commands). Then:
   a) Sort the numbers and save to `sorted.txt`
   b) Display only the unique numbers (hint: `uniq`)
   c) Count how many unique numbers exist

---

### B3. Pipes and Filters (10 units)

**1. (5 units)** Write a pipeline for the following operations:
   a) Display lines of `/etc/passwd` containing `/bin/sh`
   b) Count the lines of result (a)
   c) Display only the 1st and 3rd columns (fields) of `/etc/passwd`

**2. (5 units)** Explain the command:
   ```
   who | awk '{print $1}' | sort | uniq -c | sort -rn
   ```
   What purpose does it serve? If `who` does not work in jsLinux, how would you replace it?

---

### B4. Practical Exercise Scenario (10 units)

**Scenario:** Creating an organized project directory structure and file management in jsLinux.

1. **(2 units)** Create the structure: `~/final_project/{bin,src,docs,tests,logs}`.

2. **(2 units)** Inside `src`, create 3 files: `main.c`, `utils.c`, `config.h`.

3. **(2 units)** Copy all `.c` files from `src` to `tests` using wildcards.

4. **(2 units)** Create a file `logs/run.log` and execute a command that writes the current date to this file.

5. **(2 units)** Display the directory tree `~/final_project` and redirect the output to `docs/project_structure.txt`.

---

*Good luck!*