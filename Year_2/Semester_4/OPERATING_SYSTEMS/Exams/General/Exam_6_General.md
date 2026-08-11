# Exam 6 — Operating Systems

**Department:** Computer Science & Telecommunications
**Duration:** 3 hours
**Maximum Score:** 100 units

---

> **Instructions:**
> The examination consists of two parts. **Part A** examines theory (50 units) and **Part B** examines the Unix laboratory through jsLinux (50 units). Answer **all** questions. The use of auxiliary materials is not permitted.

---

## PART A — THEORY (50 units)

*Topics: Virtual Memory — Paging, Segmentation, Page Replacement Algorithms*

---

### A1. Multiple Choice Questions (10 units — 2 units each)

**Circle the letter of the correct answer.**

**1.** What is a **page fault**?

- a) A programming error that crashes the system
- b) Accessing a page that is not in physical memory (RAM)
- c) Exceeding a process's memory limit
- d) An error in the page table

---

**2.** Which page replacement algorithm **is not implemented in practice** and is used only as a theoretical reference index?

- a) FIFO
- b) LRU
- c) OPT (Optimal)
- d) LFU

---

**3.** What is **Belady's Anomaly**?

- a) LRU is worse than FIFO
- b) Increasing the number of frames can increase the number of page faults with FIFO
- c) OPT does not always minimize page faults
- d) LRU cannot be implemented in multiprocessor systems

---

**4.** In **Segmentation**, the virtual address is expressed as:

- a) Only the page number (p)
- b) A pair (segment number s, offset d)
- c) An absolute physical address
- d) Frame number and offset

---

**5.** Which of the following properties characterizes **Paging**?

- a) Visible to the programmer
- b) Variable page size
- c) No external fragmentation
- d) Physical memory must be contiguous

---

### A2. Fill-in-the-Blank Questions (6 units — 1 unit each)

Fill in with the correct word/phrase:

1. The conversion from virtual to physical address is done by the ________________.

2. In Paging, the virtual address is divided into __________ (page number) and __________ (offset).

3. The LRU algorithm is based on the principle of ________________ locality.

4. Segmentation produces ________________ fragmentation but not ________________ fragmentation.

5. A page table contains for each page a __________ bit indicating whether the page is in memory.

---

### A3. Page Replacement Algorithm Exercise (18 units)

Given the page reference string: **3 2 1 0 3 2 4 3 2 1 0 4**
Number of frames: **3** (initially empty)

**1. (6 units)** Apply the **FIFO** algorithm. Show the frames at each step and count the page faults.

**2. (6 units)** Apply the **LRU** algorithm. Show the frames and the LRU order at each step. Count the page faults.

**3. (6 units)** Apply the **OPT** algorithm. Show which page is evicted each time. Count the page faults.

---

### A4. Address Translation Exercise (8 units)

**Exercise 1 (4 units):**
Page size: 4 KB = $2^{12}$ bytes. 16-bit virtual address.
The page table has: page 0 → frame 5, page 1 → frame 2, page 2 → frame 8.

Translate the virtual addresses: `0x1A20` and `0x0050`.

**Exercise 2 (4 units):**
Process segment table:

| Segment | Base | Limit |
|:---|:---|:---|
| 0 | 219 | 600 |
| 1 | 2300 | 14 |
| 2 | 90 | 100 |
| 3 | 1327 | 580 |

Translate: (a) $\langle 0, 430 \rangle$, (b) $\langle 1, 10 \rangle$, (c) $\langle 3, 600 \rangle$. Justify each result.

---

### A5. Paging vs Segmentation Comparison (8 units)

Complete the following comparison table:

| Characteristic | Paging | Segmentation |
|:---|:---|:---|
| Visibility to programmer | | |
| Internal fragmentation | | |
| External fragmentation | | |
| Partition/page size | | |
| Code/data separation | | |
| Sharing capability | | |
| Physical memory overflow | | |
| Growth capability (stack/heap) | | |

---

## PART B — Unix Laboratory / jsLinux (50 units)

---

> **jsLinux Environment:** Write **exactly** the commands you would use.

---

### B1. File System — Navigation Commands (10 units)

**1. (5 units)** Explain in detail what the following commands do and give an example output for each:
   a) `pwd`
   b) `cd ..`
   c) `cd -`
   d) `cd ~`
   e) `ls -la | head -20`

**2. (5 units)** Navigate in jsLinux:
   a) Find which directory you are in
   b) Go to `/var` if it exists, otherwise to `/etc`
   c) Display the directory with details
   d) Return to the previous directory using `cd -`
   e) Verify you returned with `pwd`

---

### B2. File Characteristics (15 units)

**1. (5 units)** Explain what each column of the `ls -l` output represents:

```
drwxr-xr-x  3  root  root  4096  Jun 15 12:30  home
-rw-r--r--  1  ice   ice    256  Jun 16 09:00  readme.txt
lrwxrwxrwx  1  root  root     7  Jun 10 08:00  lib -> usr/lib
```

**2. (5 units)** In jsLinux, use `stat` on a file (e.g., `/etc/hostname`). Explain what information it returns, particularly: inode number, hard links, size in bytes, permissions in octal.

**3. (5 units)** What is an **inode**? What information is **not** stored in the inode? What is the relationship between inodes and hard links?

---

### B3. Text Processing with Pipes (15 units)

**1. (5 units)** Using `cat /etc/passwd` and pipe commands, display:
   a) The number of users in the system
   b) Only the usernames (first field)
   c) The shells users use (last field), sorted without duplicates

**2. (5 units)** Create a file `/tmp/numbers.txt` with numbers 1–10 (one per line). Write a pipeline that displays the numbers in **reverse order** and saves them to `/tmp/reversed.txt`.

**3. (5 units)** Explain what the command does:
   ```
   find /etc -name "*.conf" 2>/dev/null | xargs wc -l | sort -n | tail -5
   ```
   What does it search for? Where does it redirect errors and why? What does it ultimately display?

---

### B4. Practical Exercise Scenario (10 units)

**Scenario:** Analyzing filesystem usage in jsLinux.

1. **(3 units)** Display the total disk usage for each directory in `/` with the command `du -sh /*` (or equivalent). What does the `-s` option do and what does `-h` do?

2. **(4 units)** Use `df -h` to view filesystem usage. Explain the columns displayed (Filesystem, Size, Used, Avail, Use%, Mounted on).

3. **(3 units)** Find the 5 largest files in the entire system (ignoring permission errors). Write the command and explain why you use `2>/dev/null`.

---

*Good luck!*