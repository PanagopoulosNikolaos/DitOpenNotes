# Exam 5 — Operating Systems

**Department:** Computer Science & Telecommunications
**Duration:** 3 hours
**Maximum Score:** 100 units

---

> **Instructions:**
> The examination consists of two parts. **Part A** examines theory (50 units) and **Part B** examines the Unix laboratory through jsLinux (50 units). Answer **all** questions. The use of auxiliary materials is not permitted.

---

## PART A — THEORY (50 units)

*Topics: Memory Management — Partitioning, Placement, Swapping*

---

### A1. Multiple Choice Questions (10 units — 2 units each)

**Circle the letter of the correct answer.**

**1.** What is **internal fragmentation**?

- a) Free spaces between partitions that cannot be used
- b) Wasted space inside an allocated partition that the process does not use
- c) Space used by the kernel
- d) Memory located on disk

---

**2.** Which placement algorithm selects the **smallest free partition** that fits the process?

- a) First-Fit
- b) Next-Fit
- c) Best-Fit
- d) Worst-Fit

---

**3.** What is **Compaction**?

- a) The Best-Fit algorithm
- b) The technique of moving processes so that all free space is concentrated in one contiguous partition
- c) Dividing memory into fixed-size pages
- d) Transferring processes to disk

---

**4.** The formula CPU Utilization = $1 - p^v$ gives:

- a) Disk usage relative to number of processes
- b) The probability that at least one of the v processes uses CPU
- c) The number of pages loaded per second
- d) The context switch cost

---

**5.** Which technique allows executing programs **larger** than available memory in single-programming?

- a) Swapping
- b) Paging
- c) Overlays
- d) Segmentation

---

### A2. True/False Questions (6 units — 1 unit each)

**Mark T (True) or F (False).**

1. _____ **Dynamic Partitioning** does not produce internal fragmentation.

2. _____ The **Best-Fit** algorithm tends to leave very small unusable partitions.

3. _____ **Fixed Partitioning** with equal partitions produces external fragmentation.

4. _____ **Swapping** moves the **entire** process from RAM to disk.

5. _____ The **First-Fit** algorithm scans from the last allocation point.

6. _____ With $v = 4$ processes and $p = 0.8$, CPU utilization ≈ 59%.

---

### A3. Placement Algorithm Exercise (14 units)

Given free memory partitions (in KB) in order:
**[100, 500, 200, 300, 600]**

Process requests arrive in order: **212 KB, 417 KB, 112 KB, 426 KB**.
The last allocation point (for Next-Fit) is **before** the 200 KB partition.

**1. (4 units)** Apply **First-Fit**. Show the free partition list after each request.

**2. (4 units)** Apply **Best-Fit**. Show the free partition list after each request.

**3. (3 units)** Apply **Next-Fit**. Show the free partition list after each request.

**4. (3 units)** Compare the results of the three algorithms. Which one managed to serve all 4 requests and why?

---

### A4. Development Exercises (20 units)

**Exercise 1 (8 units):**
A system uses **fixed partitioning** with 5 partitions of equal size 8 MB each. The processes that want to load have sizes: 2 MB, 7 MB, 5 MB, 3 MB, 8 MB.

a) Calculate the **internal fragmentation** for each process and total.
b) If unequal partitions (2 MB, 4 MB, 6 MB, 8 MB, 12 MB) are used instead of equal ones, which process goes to which partition with a **single global queue**?
c) Which method (equal vs unequal) produces less internal fragmentation? Justify.

**Exercise 2 (12 units):**
A system has $p = 0.7$ (70% probability of I/O waiting).

a) **(4 units)** How many processes ($v$) are required for at least 95% CPU utilization? Show the calculation.

b) **(4 units)** Explain how **Dynamic Partitioning** creates **external fragmentation** with a diagram.

c) **(4 units)** What are **Overlays** and how do they differ from **Swapping**? What problems do they solve and what problems don't they solve?

---

## PART B — Unix Laboratory / jsLinux (50 units)

---

> **jsLinux Environment:** Write **exactly** the commands you would use.

---

### B1. File Viewing and Links (15 units)

**1. (5 units)** Explain the difference between **hard link** and **symbolic link (symlink)** in Unix:
   a) How is each type of link created?
   b) What happens if the original file is deleted?
   c) Can a hard link point to a directory?

**2. (5 units)** In jsLinux:
   a) Create a file `original.txt` with content `"Original file"`
   b) Create a **hard link** `hard_link.txt` pointing to `original.txt`
   c) Create a **symbolic link** `soft_link.txt`
   d) Display all three with `ls -li` and explain what you observe about the inode numbers

**3. (5 units)** What commands do you use to view file contents? Compare `cat`, `head`, `tail`, and `less`. Give an example of using `tail -n 5 /etc/passwd`.

---

### B2. Complex Pipelines (15 units)

Write and explain the following commands in jsLinux:

**1. (5 units)** A pipeline that:
   - Reads the file `/etc/passwd`
   - Extracts only the usernames (first field, separated by `:`)
   - Sorts alphabetically
   - Saves to `userlist.txt`
   *(Hint: use `cut -d: -f1`)*

**2. (5 units)** Explain what the command does:
   ```
   cat /etc/passwd | cut -d: -f3 | sort -n | tail -1
   ```
   What data type does `cut` process, and what does `sort -n` do?

**3. (5 units)** Write a pipeline that displays the **10 largest files** in a directory, sorted by size. Explain each command.

---

### B3. Redirection and Errors (5 units)

**1. (3 units)** Run in jsLinux:
   ```
   ls /nonexistent 2> errors.txt
   ls /etc >> output.txt 2>&1
   ```
   Explain what each command does. Which file contains which output?

**2. (2 units)** When do you use `2>&1`? What is its practical utility in production scripts?

---

### B4. Practical Exercise Scenario (15 units)

**Scenario:** System file analysis and data organization in jsLinux.

1. **(3 units)** Create a file `/tmp/sample_data.txt` with 5 lines of text of different lengths using `echo` and `>>` commands.

2. **(4 units)** Display:
   a) How many lines the file has (use `wc`)
   b) How many words it has
   c) How many characters it has

3. **(4 units)** Using `grep`, find and display lines containing a specific word from `/tmp/sample_data.txt`. Redirect the results to a new file `filtered.txt`.

4. **(4 units)** Create a **symbolic link** `data_link.txt` pointing to `/tmp/sample_data.txt`. Verify with `ls -l` and explain what you see.

---

*Good luck!*