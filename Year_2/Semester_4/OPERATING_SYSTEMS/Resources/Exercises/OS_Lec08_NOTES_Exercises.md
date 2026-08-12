# Exercises — Chapter 8: Virtual Memory

**Based on:** `OS_Lec08_NOTES.md`  
**Number of exercises:** 35

---

## Part A — Theory

### Exercise 1
Why is virtual memory needed? State three problems it solves.

---

### Exercise 2
Distinguish virtual (logical) and physical address. What is address translation?

---

### Exercise 3
Explain paging: page, frame, page table.

---

### Exercise 4
Logical addresses of 16 bits, page size of 1024 bytes. Calculate: (a) offset bits, (b) size of the page table.

---

### Exercise 5
Logical address 0x4B2A, page size 1KB (1024 bytes). Calculate the page number and offset (hexadecimal and decimal).

---

### Exercise 6
What is a page fault? Describe the handling steps performed by the OS.

---

### Exercise 7
State the properties of paging (internal fragmentation, external, etc.).

---

### Exercise 8
Explain segmentation: segment table, base, limit.

---

### Exercise 9
Compare paging and segmentation (unit size, fragmentation, etc.).

---

## Part B — Page Replacement Algorithms

### Exercise 10
Describe FIFO, OPT, LRU. Which is optimal and why is it not practical?

---

### Exercise 11
Explain the difference between a FIFO queue and an LRU stack in implementation.

---

### Exercise 12
What is Belady's anomaly and in which algorithm does it occur?

---

## Part C — Computational Exercises

### Exercise 13
**Address translation:** Page 5, offset 200, page size 512 bytes. Calculate the logical address.

---

### Exercise 14
**Page table:** Logical address 3500, page size 4KB. Page? Offset? If frame 7, what is the physical address?

---

### Exercise 15
**FIFO — 4 frames**

Reference string: `7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1`

Complete the page table and count the page faults.

---

### Exercise 16
With the same reference string as Exercise 15, apply **OPT** (4 frames).

---

### Exercise 17
With the same reference string, apply **LRU** (4 frames).

---

### Exercise 18
**Short sequence — 3 frames**

Reference: `1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5`

Compare the page faults for FIFO and LRU.

---

### Exercise 19
**Segmentation:** Segment table:

| Segment | Base | Limit |
| :--- | :--- | :--- |
| 0 | 1400 | 1000 |
| 1 | 6300 | 400 |
| 2 | 4300 | 400 |

Logical address (segment=1, offset=200). Calculate the physical address. Is it valid?

---

### Exercise 20
Logical address (segment=2, offset=500) with the table of Exercise 19. What happens?

---

### Exercise 21
**Page table lookup:** Page size 8KB. Logical address 0x00005000. Page number and offset?

---

### Exercise 22
System with 32-bit addresses, page size 4KB. How many pages maximum? How many bits for the page number?

---

## Part D — Comparison and True/False

### Exercise 23
Mark **T** or **F**:

1. Paging has internal fragmentation.
2. Segmentation has external fragmentation.
3. A page fault is always an error that terminates the process.
4. LRU requires hardware support or an approximation.
5. More frames always mean fewer page faults.

---

### Exercise 24
Circle the correct answer: Which algorithm replaces the page that **will not be used for the longest time in the future**?

- a) FIFO  
- b) OPT  
- c) LRU  
- d) Random

---

### Exercise 25
Why does paging allow non-contiguous physical memory?

---

### Exercise 26
Describe the steps of address translation in paging (5 steps from the notes).

---

### Exercise 27
**OPT tie-breaking:** Two pages are never used again. Which one is replaced?

---

### Exercise 28
Compare page faults for 3 vs 4 frames with LRU on the string `1,2,3,4,1,2,5,1,2,3,4,5`.

---

### Exercise 29
Explain demand paging vs prepaging.

---

### Exercise 30
How does a page fault relate to context switch and I/O?

---

### Exercise 31
**Scenario:** A process with 8GB virtual memory, 16GB RAM, page size 4KB. Explain how it executes without 8GB of physical memory.

---

### Exercise 32
Calculate the size of the page table (entries) for a 20-bit logical address, 1KB pages.

---

### Exercise 33
Complete the one-liners:

| Topic | Paging | Segmentation |
| :--- | :--- | :--- |
| Unit | | |
| Fragmentation | | |
| Table entry | | |

---

### Exercise 34
Reference string: `0,1,2,0,1,3,0,1,2,3`. 3 frames. Does Belady's anomaly appear with FIFO if we increase to 4 frames? Check.

---

### Exercise 35
Combined: 16-bit addresses, 2KB pages. (a) Offset bits, (b) page table size, (c) physical address for logical 0x3C00 if frame=10.
