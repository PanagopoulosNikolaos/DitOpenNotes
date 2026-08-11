# Exam 1 — Operating Systems

**Department:** Computer Science & Telecommunications
**Duration:** 3 hours
**Maximum Score:** 100 units

---

> **Instructions:**
> The examination consists of two parts. **Part A** examines theory (50 units) and **Part B** examines the Unix laboratory through jsLinux (50 units). Answer **all** questions. The use of auxiliary materials is not permitted.

---

## PART A — THEORY (50 units)

---

### A1. Multiple Choice Questions (10 units — 2 units each)

**Circle the letter of the correct answer.**

**1.** Which of the following constitutes the definition of the **Kernel** of an Operating System?

- a) The set of applications executed by the user
- b) The single program that executes continuously throughout the system's operation
- c) The compiler that translates code to machine language
- d) The computer hardware

---

**2.** In which era did **multiprogramming** first appear?

- a) Early 1940s — Serial processing
- b) Early 1960s — Simple Batch systems
- c) 1965–1980 — Multiprogrammed Batch systems
- d) 1980–1990 — Fourth Generation (LSI)

---

**3.** What is the **main difference** between multiprogramming and time-sharing?

- a) Multiprogramming uses multiple processors while time-sharing uses one
- b) Multiprogramming aims to maximize CPU utilization while time-sharing aims to minimize response time
- c) Time-sharing processes only batch jobs
- d) There is no significant difference

---

**4.** What hardware feature is required by the Monitor in simple Batch systems to **prevent monopolization** of the CPU?

- a) Large disk capacity
- b) Timer
- c) High-resolution graphics card
- d) Multiple processors

---

**5.** What does it mean that an OS is treated as an **"extended/virtual machine"**?

- a) It has more physical memory than what appears
- b) It hides the complexity of the hardware from the user
- c) It executes programs faster than the hardware
- d) It provides virtualization capability

---

### A2. True/False Questions (6 units — 1 unit each)

**Mark T (True) or F (False) next to each statement.**

1. _____ The kernel always executes in **user mode** for security reasons.

2. _____ CPU Utilization in a single-programming system with I/O-bound tasks can reach as low as 3%.

3. _____ I/O commands are **privileged** and execute only in monitor mode.

4. _____ In a batch system with a Monitor, each job loads its own Job Control Language (JCL).

5. _____ POSIX (Portable Operating System Interface) is an OS standard that appeared after 2000.

6. _____ Distributed Operating Systems appear as traditional single-processor systems to the user.

---

### A3. Matching Questions (8 units — 2 units each)

**Match each item in Column A with the correct description in Column B.**

| Column A | | Column B |
|:---|:---:|:---|
| a) Batch Monitor | ___ | 1. Eliminates CPU waste during I/O waiting |
| b) Multiprogramming | ___ | 2. Grouping of jobs and execution control |
| c) Time-Sharing | ___ | 3. Minimizing response time through time quantum |
| d) Distributed OS | ___ | 4. Multiple nodes that appear as one system |

---

### A4. Short Answer Questions (10 units — 5 units each)

**1.** Describe the **four levels** of a computing system and the role of each in its operation.

---

**2.** Given the following execution example: Reading a record from file: 0.0015 sec, Executing 100 instructions: 0.0001 sec, Writing a record to file: 0.0015 sec. Calculate **CPU utilization** in a single-programming system and explain what causes the low value.

---

### A5. Development Exercises (16 units)

**Exercise 1 (8 units):**
A Batch system uses a Monitor for job execution. Describe and analyze the **four required hardware characteristics** for the Monitor's operation, explaining the purpose of each.

---

**Exercise 2 (8 units):**
**Detailed comparison** of the generations of Operating System evolution from Serial Processing (1940s) to Distributed Systems (1980–1990). For each generation mention: (a) the main problem it addresses, (b) the solution it proposes.

---

## PART B — Unix Laboratory / jsLinux (50 units)

---

> **Environment:** Use **jsLinux** (browser-based Linux terminal). All commands execute in this environment. Write **exactly** the commands you would use and briefly describe what each command does.

---

### B1. Basic System Commands (10 units — 2 units each)

Write the command that executes each of the following actions in jsLinux:

1. Display the **current date and time** of the system.

2. Display **which user** is currently logged in to the system.

3. Display the **calendar** of the current month.

4. **Change the password** of the current user.

5. **End the session** (logout) from the terminal.

---

### B2. File System Structure (10 units)

Examining the Unix filesystem structure, answer the following:

**1. (4 units)** In jsLinux, what command do you use to view the **absolute path of the current directory**? What is the expected result if you are in the root user's home directory?

**2. (3 units)** List three **basic directories** of the Unix filesystem (e.g., `/bin`, `/etc`) and briefly explain the purpose of each.

**3. (3 units)** What is the difference between **absolute path** and **relative path**? Give one example for each.

---

### B3. Practical Exercise — Navigation and Basic Commands (15 units)

In jsLinux, execute the following steps and write the command for each step:

1. **(2 units)** View the current working directory.

2. **(2 units)** Navigate to the `/tmp` directory.

3. **(3 units)** Create a new directory named `lab_exam` inside `/tmp`.

4. **(3 units)** Navigate to the `lab_exam` directory you just created.

5. **(2 units)** View the contents of `/etc` in long listing format.

6. **(3 units)** Return to the home directory using **two different methods**.

---

### B4. File Creation and Content (15 units)

**1. (5 units)** In jsLinux, create a text file named `info.txt` in the `/tmp/lab_exam` directory containing the phrase `"Operating Systems 2024"`. Write:
   - a) The command to create the file with the content.
   - b) The command to display the file content.

**2. (5 units)** Copy the file `info.txt` to a new file named `backup_info.txt` in the **same directory**. Then, display the file listing of the directory to verify the copy.

**3. (5 units)** Explain the difference between the commands `cat`, `more`, and `less` for viewing files. When would you prefer each one?

---

*Good luck!*