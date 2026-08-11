# Exam 2 — Operating Systems

**Department:** Computer Science & Telecommunications
**Duration:** 3 hours
**Maximum Score:** 100 units

---

> **Instructions:**
> The examination consists of two parts. **Part A** examines theory (50 units) and **Part B** examines the Unix laboratory through jsLinux (50 units). Answer **all** questions. The use of auxiliary materials is not permitted.

---

## PART A — THEORY (50 units)

*Topics: OS Purposes, Hardware Protection, Dual-Mode, Processes*

---

### A1. Multiple Choice Questions (12 units — 2 units each)

**Circle the letter of the correct answer.**

**1.** What is the **mode bit** in monitor mode?

- a) bit = 1
- b) bit = 0
- c) bit = -1
- d) There is no mode bit

---

**2.** Which commands are characterized as **privileged**?

- a) Only I/O commands
- b) Only the load timer command
- c) I/O commands, load base/limit, load timer, mode bit switching
- d) All Assembly commands

---

**3.** What is stored in the **limit register** for memory protection?

- a) The smallest acceptable physical memory address
- b) The size of the acceptable memory region
- c) The address of the last executed instruction
- d) The number of processes in waiting

---

**4.** What happens when the **Timer** reaches zero?

- a) The computer shuts down
- b) An interrupt is generated
- c) The current process terminates permanently
- d) The mode bit automatically changes to user mode

---

**5.** What is the **ultimate definition** of an Operating System?

- a) Only the Kernel
- b) The set of applications the user runs
- c) Combination of resource manager, control program, and kernel
- d) Only hardware drivers

---

**6.** What is defined as a **system call**?

- a) A call from the user to start the OS
- b) A trap mechanism to provide OS services to a user program
- c) A command that executes only in user mode
- d) A data copy command between processors

---

### A2. Round Robin Questions (10 units — 2 units each)

Each question has **only one correct** answer. Circle it.

**1.** What is the correct order of OS purposes?
a) Protection → Communication → Management → Evolution
b) Communication → Protection → Evolution → Management
c) Management → Communication → Protection → Evolution
d) Evolution → Management → Protection → Communication

**2.** In what mode do Compilers/Shell execute?
a) Monitor mode
b) Kernel mode
c) User mode
d) Privileged mode

**3.** What does the Kernel provide to users as a service?
a) Only program execution
b) Development, execution, I/O access, file traversal, error detection, accounting
c) Only file management
d) Only error detection

**4.** Which OS hierarchy level (Layers) is in user space?
a) Layer 0
b) Layer 2
c) Layer 4
d) Layer 13

**5.** What are the three categories of OS evolution?
a) Hardware, Software, Security
b) Hardware upgrades, New services, Fixes
c) Threads, Processes, Deadlocks
d) Parallel, Distributed, Real-Time

---

### A3. Short Answer Questions (12 units — 4 units each)

**1.** A user program is executing (mode bit = 1). A hardware interrupt appears. Describe **step by step** what happens in the system.

**2.** base register = 200000, limit register = 80000. Check if the following addresses are **acceptable**: (a) 250000, (b) 290000, (c) 180000. Justify.

**3.** Explain why **I/O commands are privileged** and how a user program can execute I/O operations.

---

### A4. Development Exercise (16 units)

**Exercise (16 units):**
An OS has the following resources for processes: CPU, Memory, I/O Devices. The OS must manage them efficiently.

a) **(5 units)** Describe and explain the **five purposes** of the OS for memory management.

b) **(5 units)** Describe the **System Call mechanism for I/O** step by step, explaining the role of the interrupt vector table.

c) **(6 units)** What is **Virtual Memory** and how does it contribute to process isolation? Describe the role of the MMU and what happens during a **page fault**.

---

## PART B — Unix Laboratory / jsLinux (50 units)

---

> **jsLinux Environment:** Write **exactly** the commands you would use.

---

### B1. File Management — Commands (10 units — 2 units each)

Write the command for each action:

1. Create an empty file named `notes.txt`.

2. Copy the file `notes.txt` to `notes_backup.txt`.

3. Rename (or move) `notes.txt` to `lecture_notes.txt`.

4. Delete the file `notes_backup.txt`.

5. Create a directory structure `projects/os/labs` with a single command.

---

### B2. File Information Commands (10 units)

**1. (5 units)** View the contents of the current directory in **long listing** format, also showing **hidden files**. Explain the important columns displayed (permissions, hard links, owner, size, date, name).

**2. (5 units)** In jsLinux, run `ls -la /` and list: (a) at least 5 directories you see, (b) who owns them, and (c) what characterizes directory permissions versus file permissions.

---

### B3. Input/Output Redirection (15 units)

**1. (5 units)** Write a command that:
   - Generates a file listing of `/etc`
   - Saves the result to a file `etc_list.txt` (overwriting existing content)
   - Then **appends** the phrase `"End of list"` to the end of this file

**2. (5 units)** Use **pipes** to count how many files are in the `/etc` directory. Write the command and explain each part of the pipeline.

**3. (5 units)** What is the difference between `>` and `>>` in redirection? Give one usage example. What happens if the file does not exist in both cases?

---

### B4. Practical Exercise Scenario (15 units)

In jsLinux, follow the scenario below and write the commands:

**Scenario:** You are the system administrator and need to organize the system log files.

1. **(3 units)** Create a directory `~/system_logs` in your home.

2. **(3 units)** Inside `system_logs`, create two subdirectories: `daily` and `weekly`.

3. **(3 units)** Create a file `~/system_logs/daily/log_today.txt` with content `"Daily log file"`.

4. **(3 units)** Copy `log_today.txt` to the `weekly` directory with a new name `log_week.txt`.

5. **(3 units)** Display the complete `system_logs` directory tree and verify the correctness of the structure.

---

*Good luck!*