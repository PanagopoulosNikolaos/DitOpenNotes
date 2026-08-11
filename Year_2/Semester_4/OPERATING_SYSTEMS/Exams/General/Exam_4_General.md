# Exam 4 — Operating Systems

**Department:** Computer Science & Telecommunications
**Duration:** 3 hours
**Maximum Score:** 100 units

---

> **Instructions:**
> The examination consists of two parts. **Part A** examines theory (50 units) and **Part B** examines the Unix laboratory through jsLinux (50 units). Answer **all** questions. The use of auxiliary materials is not permitted.

---

## PART A — THEORY (50 units)

*Topics: Mutual Exclusion, Semaphores, Deadlock*

---

### A1. Multiple Choice Questions (10 units — 2 units each)

**Circle the letter of the correct answer.**

**1.** Which of the following is **not** a condition for deadlock?

- a) Mutual Exclusion
- b) Hold and Wait
- c) Preemption
- d) Circular Wait

---

**2.** What does the **P (wait)** operation of a semaphore do?

- a) Increases the semaphore value by 1 and releases a process
- b) Waits until the semaphore becomes > 0 and decreases it by 1
- c) Sets the semaphore to zero
- d) Creates a new semaphore

---

**3.** What value is a **binary semaphore** initialized to for mutual exclusion?

- a) 0
- b) 1
- c) -1
- d) Infinity

---

**4.** What does a **Resource Allocation Graph** describe?

- a) The relationship between users and files
- b) The requests and allocations of resources between processes
- c) The filesystem structure
- d) The scheduling algorithm

---

**5.** To which deadlock handling strategy does the **Banker's Algorithm** belong?

- a) Prevention
- b) Detection
- c) Avoidance
- d) Recovery

---

### A2. Round Robin Questions (10 units — 2 units each)

Circle the correct answer.

**1.** What is a **critical section**?
a) A code section that never executes
b) A sequence of instructions requiring access to shared resources
c) The memory region of the kernel
d) The waiting queue of the scheduler

**2.** Which of the following is a **disadvantage** of disabling interrupts for mutual exclusion?
a) It does not guarantee mutual exclusion in single-processor systems
b) It does not guarantee mutual exclusion in multiprocessor systems
c) It is very slow
d) It requires more memory

**3.** What is **Priority Inversion** in TAS (Test and Set)?
a) A low-priority process blocks a high-priority one
b) The high-priority always proceeds first
c) All processes have equal priority
d) The system does not support priorities

**4.** What does a **safe state** mean in the Banker's Algorithm?
a) All processes are blocked
b) There exists an execution sequence that allows all processes to complete
c) Resources have been allocated equally
d) No resource is in use

**5.** How many of the 4 deadlock conditions must hold **simultaneously** for deadlock to occur?
a) At least 1
b) At least 2
c) At least 3
d) All 4

---

### A3. Short Answer Questions (10 units)

**1. (4 units)** Process A holds resource R1 and waits for R2. Process B holds R2 and waits for R1. Check if **all 4 deadlock conditions** apply. What do you conclude?

**2. (3 units)** If $Max = (7, 3, 4)$ and $Allocation = (3, 1, 2)$, calculate $Need$ and explain what it represents.

**3. (3 units)** List three **avoidance techniques** for deadlock in the Dining Philosophers problem.

---

### A4. Development Exercise (20 units)

**Exercise 1 (10 units):**
Given the following semaphore scenario:

```c
Semaphore S1 = 1;
Semaphore S2 = 0;
```

**Process P1:**
```c
A;
signal(S2);
wait(S1);
B;
```

**Process P2:**
```c
wait(S2);
C;
signal(S1);
D;
```

a) **(3 units)** In what order do sections A, B, C, D execute? Explain why.
b) **(3 units)** If `wait(S1)` and `signal(S2)` are reversed in P1, what happens?
c) **(4 units)** If both processes execute `wait(S1)` before anything else and we have `S1 = 1`, what happens with the second one?

**Exercise 2 (10 units):**
System with 3 resource types A, B, C and 4 processes P0–P3:

| Process | Allocation (A,B,C) | Max (A,B,C) |
|:---|:---|:---|
| P0 | (0, 1, 0) | (7, 5, 3) |
| P1 | (2, 0, 0) | (3, 2, 2) |
| P2 | (3, 0, 2) | (9, 0, 2) |
| P3 | (2, 1, 1) | (2, 2, 2) |

Available resources = (3, 3, 2). Total resources = (10, 5, 7).

a) Calculate $Need$ for each process.
b) Check if the system is in a **safe state** by finding a safe sequence.
c) If P1 requests additional resources (1, 0, 2), can the request be satisfied?

---

## PART B — Unix Laboratory / jsLinux (50 units)

---

> **jsLinux Environment:** Write **exactly** the commands you would use.

---

### B1. Wildcards and Glob Patterns (15 units)

**1. (5 units)** Explain the meaning of the following wildcards in Unix shell. Give one usage example for each:

| Wildcard | Meaning | Example |
|:---|:---|:---|
| `*` | | |
| `?` | | |
| `[abc]` | | |
| `[a-z]` | | |
| `[!0-9]` | | |

**2. (5 units)** In jsLinux, write commands using wildcards to:
   a) List files starting with letter `a` in `/etc`
   b) List files with extension `.conf` in `/etc`
   c) List files with exactly 5 characters in their name

**3. (5 units)** What does the command `rm -f /tmp/test[1-5].txt` execute? Which files will be deleted? Is it safe to use? Justify.

---

### B2. Search Commands (10 units)

**1. (5 units)** Use the `find` command in jsLinux to:
   a) Find all `.txt` files in `/tmp`
   b) Find files modified in the last 1 day
   c) Find files larger than 100 bytes

**2. (5 units)** Explain the difference between `find` and `grep`. Give an example where you use both in a pipeline to find files containing a specific word.

---

### B3. Permissions and Security (10 units)

**1. (5 units)** In jsLinux, create a script file `secure_script.sh`. Set permissions so that:
   - The owner has full permissions (rwx)
   - The group has only read and execute (r-x)
   - Others have no permissions (---)
   
   Write the commands and verify with `ls -l`.

**2. (5 units)** Explain the meaning of **umask** in Unix. If umask is `022`, what will be the permissions of a new file and a new directory created? Show the calculation.

---

### B4. Practical Exercise Scenario (15 units)

**Scenario:** Project file management with wildcards and permissions in jsLinux.

1. **(3 units)** Create 5 files: `report_1.txt`, `report_2.txt`, `report_3.txt`, `draft_1.txt`, `draft_2.txt` in the `/tmp` directory.

2. **(4 units)** Use **wildcards** to copy only the `report_*.txt` files to a new directory `/tmp/final_reports`.

3. **(4 units)** Give the `report_*.txt` files in `/tmp/final_reports` permissions `644`. Verify.

4. **(4 units)** Display the contents of all `report_*.txt` files **simultaneously** using wildcards. Then, redirect this output to a new file `combined_reports.txt`.

---

*Good luck!*