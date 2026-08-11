# Exam 3 — Operating Systems

**Department:** Computer Science & Telecommunications
**Duration:** 3 hours
**Maximum Score:** 100 units

---

> **Instructions:**
> The examination consists of two parts. **Part A** examines theory (50 units) and **Part B** examines the Unix laboratory through jsLinux (50 units). Answer **all** questions. The use of auxiliary materials is not permitted.

---

## PART A — THEORY (50 units)

*Topics: Processes, PCB, Process States, OS Architectures*

---

### A1. Multiple Choice Questions (12 units — 2 units each)

**Circle the letter of the correct answer.**

**1.** What is a **Process Control Block (PCB)**?

- a) A table that stores data for all files
- b) The data structure that contains all information about a process
- c) A special CPU for system execution
- d) The algorithm for selecting the next process

---

**2.** Which state does **NOT** belong to the basic process state model?

- a) New
- b) Running
- c) Blocked
- d) Compiling

---

**3.** What is the **role of the Dispatcher**?

- a) Creates new processes
- b) Decides which process will execute next
- c) Checks which users can connect
- d) Manages files on disk

---

**4.** What is a **context switch**?

- a) The procedure of terminating a process
- b) Saving current process state and loading the next one
- c) Creating a new thread
- d) Transferring files between directories

---

**5.** In a **monolithic** OS architecture, all system processes:

- a) Execute in user mode
- b) Can directly call each other through parameters
- c) Communicate only through IPC
- d) Run in separate user space

---

**6.** Which of the following is an **advantage** of **microkernel** architecture?

- a) High performance due to direct communication
- b) Reliability — small kernel size allows precise control
- c) Simplicity without need for IPC
- d) All services execute in the kernel

---

### A2. Round Robin Questions (8 units — 2 units each)

**1.** Which of the following is **NOT** a cause for changing the executing process?

a) Clock interrupt
b) File size change
c) Memory fault
d) System call (e.g., file open)

**2.** In what state is a process waiting for I/O completion?

a) Ready
b) Running
c) Blocked
d) Exit

**3.** What is the cost of context switch for the system?

a) Uses disk
b) It is overhead — no useful work is produced
c) It has no cost
d) It increases memory usage vertically

**4.** Who performs **long-term scheduling** in an OS?

a) The user manually
b) The hardware
c) The OS — decides whether a new process enters the system
d) The compiler

---

### A3. Short Answer Questions (10 units)

**1. (4 units)** What data is stored in the **PCB** of a process? List **three** categories and give examples.

**2. (3 units)** What is the **difference** between a thread and a process in terms of: (a) address space, (b) creation cost, (c) context switch cost?

**3. (3 units)** Describe what the Unix functions: `fork()`, `exec()`, `wait()` do. What is their relationship?

---

### A4. Development Exercise (20 units)

**Exercise 1 (10 units):**
Explain **in detail** the difference between:
a) Monolithic Architecture and Microkernel Architecture (design, advantages, disadvantages).
b) Layered Architecture: list the 5 basic layers (Layer 0–4) and the function of each.

**Exercise 2 (10 units):**
Given the following scenario: A web server application receives 10 simultaneous user requests. The web server uses **threads** to serve each request.

a) Why are threads chosen instead of separate processes?
b) What do threads of a web server share among themselves?
c) What dangers arise from shared memory between threads?
d) How does **multithreading** help in utilizing multi-core processors?

---

## PART B — Unix Laboratory / jsLinux (50 units)

---

> **jsLinux Environment:** Write **exactly** the commands you would use.

---

### B1. File Permissions — Theory (10 units)

**1. (5 units)** Explain the meaning of the following `ls -l` output:

```
-rwxr-x--x  1  alice  staff  4096  Jun 10 10:00  script.sh
drwxr-xr-x  2  root   root   4096  Jun 10 09:00  configs/
```

For each line, explain: the file type, the permissions for each category (owner, group, others), and the owner.

**2. (5 units)** Complete the following table for the `chmod` command:

| Numeric Value | Symbolic | Meaning |
|:---|:---|:---|
| `chmod 755 file` | | |
| `chmod 644 file` | | |
| `chmod 700 file` | | |
| | `chmod u+x file` | |
| | `chmod g-w file` | |

---

### B2. Permission Commands (10 units — 2 units each)

Write the command for each action:

1. Give the **owner** read, write, and execute permissions on the file `myfile.sh`.

2. Remove execute permission from **all** users for the file `data.txt`.

3. Give the **owner** full permissions (rwx) and **others** only read (r).

4. Change the owner of the file `report.txt` to user `student`.

5. Change the group of the file `project.py` to group `devteam`.

---

### B3. Complex Commands with Pipes (15 units)

**1. (5 units)** Write a pipeline that:
   - Receives the file listing of `/etc`
   - Filters only those containing the word "conf"
   - Displays how many there are
   Explain each part.

**2. (5 units)** Run the `ps` or `ps aux` command (if supported) in jsLinux. Write a pipeline to:
   - Display only lines belonging to the current user
   - Sort alphabetically

**3. (5 units)** Explain what the following command does step by step:
```
ls -la | grep "^d" | wc -l
```
What does it ultimately calculate? Give an example of possible output.

---

### B4. Practical Exercise Scenario (15 units)

**Scenario:** Organizing a workspace in jsLinux for a laboratory project.

1. **(3 units)** Create the structure: `~/workspace/os_project/{src,docs,tests}` with a single command.

2. **(3 units)** Create an executable script `~/workspace/os_project/src/run.sh` and give it execute permissions.

3. **(3 units)** Recursively copy the `src` directory to the `tests` directory with the name `src_backup`.

4. **(3 units)** Use `ls -lR ~/workspace/os_project` to view the entire structure. Explain what the `-R` option shows.

5. **(3 units)** Recursively delete the `tests/src_backup` directory. What command do you use and why is the `-r` (or `-rf`) option needed?

---

*Good luck!*