# Κεφάλαιο 7 — Διαχείριση Μνήμης (Memory Management)

This file covers the core concepts of main memory management as presented in Chapter 7 of the Operating Systems course. Topics include memory manager design, management strategies, fixed and dynamic partitioning, fragmentation, placement algorithms, and swapping. The material falls under **Type C — Engineering and Applied Science Topics**.

---

## 1. Conceptual Foundation

Memory management is the OS function responsible for subdividing main memory dynamically so that as many processes as possible can be serviced efficiently. Without it:
- Programs larger than physical memory could not run.
- Multiple processes could not coexist in memory simultaneously (no multiprogramming).
- There would be no protection or isolation between processes.

**Key goals (from the programmer's and OS perspective):**

| Goal | Description |
| :--- | :--- |
| Minimize access time | Reduce latency to fetch instructions/data |
| Maximize addressable space | Allow programs to use as much memory as needed |
| Enable multiprogramming | Keep multiple processes resident simultaneously |
| Provide protection | Prevent one process from corrupting another |
| Ease of programming | Hide physical memory constraints from the programmer |

---

## 2. The Memory Manager

The **memory manager** is the OS component responsible for organizing and applying memory management strategies.

**Responsibilities:**
- Allocate primary (main) memory to processes.
- Map each process's address space onto physical memory.
- Minimize access time using cost-effective static or dynamic techniques.
- Interact with dedicated hardware — the **Memory Management Unit (MMU)** — to improve performance.

---

## 3. Memory Management Strategies

Three orthogonal strategy categories govern when, where, and which data occupies main memory:

| Strategy Class | Purpose |
| :--- | :--- |
| **Fetch strategy** (Προσκόμισης) | Decides *when* the next program/data segment is moved from secondary to primary memory |
| **Placement strategy** (Τοποθέτησης) | Decides *where* in main memory the incoming segment is placed |
| **Replacement strategy** (Επανατοποθέτησης) | Decides *which* segment to evict when main memory is full |

---

## 4. Memory Allocation Types

### 4.1 Contiguous Allocation (Συνεχόμενη Εκχώρηση)

The entire program is placed in adjacent memory locations.
- Used in early computing systems.
- If a program is larger than available memory, the system cannot execute it.

### 4.2 Non-Contiguous Allocation (Μη Συνεχόμενη Εκχώρηση)

The program is divided into pieces (pages or segments) placed in non-adjacent slots of main memory.
- Enables use of memory regions too small for an entire program.
- Increases system complexity but significantly raises the degree of multiprogramming.
- Realized through **virtual memory**.

---

## 5. Basic Memory Management

### 5.1 Monoprogramming (Μονοπρογραμματισμός)

One user monopolizes all system resources. Three simple physical memory layouts exist:

```
Layout A             Layout B             Layout C
+-----------------+  +-----------------+  +------------------+
| User Program    |  | OS (ROM)        |  | Device Drivers   |
| (RAM)           |  +-----------------+  | (ROM)            |
|                 |  | User Program    |  +------------------+
+-----------------+  | (RAM)           |  | User Program     |
| OS (RAM)        |  +-----------------+  | (RAM)            |
| 0               |                    |  +------------------+
+-----------------+                    |  | OS (RAM)         |
                                        |  | 0                |
                                        |  +------------------+
```

Memory protection is not a concern in monoprogramming — only one process runs at a time.

### 5.2 Overlays (Επικαλύψεις)

A technique enabling execution of programs larger than the available memory partition.

**Mechanism:**
1. The programmer divides the program into logical modules.
2. A portion of the program and data that must always remain in memory occupies the fixed area.
3. The remaining modules are loaded into an **overlay area** on demand, replacing the previous module.

```
Memory:
+-------------------------+
| OS                      |
+-------------------------+  <-- address a
| Permanent code/data     |
+-------------------------+  <-- address b
| Overlay area            |  <-- modules loaded here sequentially:
|  [1] Initialization     |      (1) Load init phase, run
|  [2] Processing         |      (2) Load processing phase, run
|  [3] Output             |      (3) Load output phase, run
+-------------------------+  <-- address c
```

> **[Key Insight]** Overlays solve the size-fit problem but require the programmer to manually decompose the program. The OS does not manage this automatically.

---

## 6. Memory and Multiprogramming

### 6.1 Motivation

A single process frequently blocks on I/O operations, which are orders of magnitude slower than CPU operations. The CPU sits idle during I/O waits. **Multiprogramming** keeps multiple processes resident in memory so that when one process waits on I/O, another can use the CPU.

### 6.2 CPU Utilization Formula

Let:
- $p$ = probability that a process is waiting on I/O at any given moment
- $v$ = number of processes (degree of multiprogramming)

$$
\text{CPU utilization} = 1 - p^v
$$

**Interpretation:** As $v$ increases, CPU utilization approaches 1 (100%). Higher I/O wait probability $p$ requires more concurrent processes to achieve the same utilization.

> **[Key Insight]** This formula assumes processes are independent and I/O waits are statistically independent. It is a probabilistic approximation, not an exact model.

**Example values:**

| $p$ (I/O wait) | $v = 1$ | $v = 2$ | $v = 4$ | $v = 8$ |
| :--- | :--- | :--- | :--- | :--- |
| 20% | 80% | 96% | 99.8% | ~100% |
| 50% | 50% | 75% | 93.8% | 99.6% |
| 80% | 20% | 36% | 59.0% | 83.2% |

### 6.3 Trade-offs in Degree of Multiprogramming

- More processes → better CPU utilization, but requires better memory management and protection.
- Fewer processes → less memory consumed, but CPU may be underutilized.
- Higher I/O wait → more processes required to maintain CPU utilization.

> **[Key Insight]** For the remainder of this chapter, **contiguous allocation** is assumed: each process is assigned one contiguous memory block.

---

## 7. Fixed Partitioning (Τμηματοποίηση Σταθερού Μεγέθους)

Memory is divided into a fixed number of partitions at system boot time. The number and sizes of partitions do not change during operation.

- Each process occupies exactly **one partition**.
- Maximum degree of multiprogramming = number of partitions.

### 7.1 Equal-Size Partitions (Ίσα Τμήματα)

All partitions have the same size.

**Operation:**
- Any process with size $\leq$ partition size can be loaded.
- If all partitions are occupied, the OS swaps out one process.
- A program larger than one partition requires **overlays**.

**Problem — Internal Fragmentation:**

$$
\text{Internal Fragmentation} = \text{Partition Size} - \text{Process Size}
$$

Even the smallest process occupies an entire partition, wasting the remainder.

```
Before loading:         After loading Process 1 (small):
+-----------+           +-----------+
| 8 MB      | (free)    | Process 1 | (used by process)
|           |           +-----------+
|           |           | Unused    | <-- internal fragmentation
+-----------+           +-----------+
```

**Advantages:**
- Very low OS overhead.

**Disadvantages:**
- Extremely inefficient memory use due to internal fragmentation.
- Small processes waste large partition space.

### 7.2 Unequal-Size Partitions (Άνισα Τμήματα)

Partitions have different sizes (e.g., 2 MB, 6 MB, 8 MB, 12 MB). This reduces internal fragmentation compared to equal-size partitions.

**Placement options:**

| Approach | Description | Drawback |
| :--- | :--- | :--- |
| **Queue per partition** | Each process is assigned to the queue of the smallest partition it fits in | A partition's queue may be empty while others are full; free memory exists but processes wait |
| **Single global queue** | When a process must be loaded, select the smallest available partition that fits | Better CPU utilization; reduces idle partitions |

**Advantages over equal-size:**
- Reduced internal fragmentation.
- More efficient use of main memory.

---

## 8. Fragmentation (Κατακερματισμός)

| Type | Definition | Cause | Visibility |
| :--- | :--- | :--- | :--- |
| **Internal** (εσωτερικός) | Allocated memory inside a partition that is not used by the process | Allocated block must be $\geq$ requested size | Visible only to the process holding the partition |
| **External** (εξωτερικός) | Free memory outside all partitions that cannot satisfy any pending request despite sufficient total free space | Memory requests vary in size; free blocks become scattered | Visible to the OS / system-wide |

---

## 9. Dynamic Partitioning (Δυναμική Τμηματοποίηση)

Partitions are created at runtime with exactly the size required by each process. The number and sizes of partitions vary throughout system operation.

**Key property:** A process is allocated exactly the memory it requests — no internal fragmentation.

**Problem — External Fragmentation:**
Over time, as processes enter and leave, gaps (holes) appear in memory. These gaps may individually be too small to satisfy new requests, even though their sum could.

```
Initial:                After P2 exits:        After P4 exits:
+----------+            +----------+           +----------+
| OS       |            | OS       |           | OS       |
+----------+            +----------+           +----------+
| P1       |            | P1       |           | P1       |
+----------+            +----------+           +----------+
| P2       |  P2 exits  | Hole     |           | Hole     |
+----------+  ------->  +----------+  ------>  +----------+
| P3       |            | P3       |           | P3       |
+----------+            +----------+           +----------+
| P4       |            | P4       |  P4 exits | Hole     |
+----------+            +----------+           +----------+
| P5       |            | P5       |           | P5       |
+----------+            +----------+           +----------+
| Hole     |            | Hole     |           | Hole     |
+----------+            +----------+           +----------+
```

**Solution — Compaction (Συμπίεση):**
Shift all processes toward one end of memory so all free space coalesces into one contiguous block.

**Compaction costs:**
- Consumes CPU time.
- Requires **dynamic relocation** capability: the ability to move a running program to a different memory area without invalidating its memory references (typically handled by the MMU via a relocation register).

---

## 10. Placement Algorithms (Αλγόριθμοι Τοποθέτησης)

When a process requests memory, the OS must select which free block to allocate. The three standard algorithms apply to dynamic partitioning.

### 10.1 First-Fit

Scan memory **from the beginning**; allocate the **first** free block large enough.

- Fastest algorithm.
- Tends to cluster allocations at the low end of memory, creating many small holes there.

### 10.2 Best-Fit

Scan **all** free blocks; allocate the **smallest** free block that is large enough.

- Minimizes wasted space within the chosen block.
- Worst overall performance: leaves very small residual fragments that are too small for future allocations, causing frequent compaction.
- Typically requires sorting or full scan of the free list.

### 10.3 Next-Fit

Scan memory **from the point of the last allocation**; allocate the **next** free block large enough.

- Distributes allocations more uniformly across memory.
- Tends to fragment the large free block at the high end of memory.
- Requires compaction to recover large free blocks at the end.
- Performance similar to first-fit.

**Algorithm comparison:**

| Algorithm | Scan Start | Selection Criterion | Speed | Fragmentation Behavior |
| :--- | :--- | :--- | :--- | :--- |
| First-Fit | Beginning | First sufficient block | Fastest | Small holes accumulate at low addresses |
| Best-Fit | Full scan | Smallest sufficient block | Slowest | Tiny residual fragments everywhere |
| Next-Fit | Last placement point | First sufficient block from that point | Moderate | Large end-block eroded |

---

## 11. Swapping (Εναλλαγή)

Swapping is the technique of temporarily moving an entire process from main memory to a **backing store** (secondary storage, typically a disk partition or swap file), freeing its memory for other processes.

**Swap-out:** Process is written from RAM to backing store.
**Swap-in:** Process is read back from backing store into RAM.

```
Main Memory         Backing Store
+----------+        +----------+
| OS       |        | P1 image |
+----------+  <-->  +----------+
| User     |  swap  | P2 image |
| space    |        +----------+
+----------+
```

**Memory allocation evolves as:**
- New processes arrive and are loaded.
- Processes complete and release memory.
- Blocked processes are swapped out to disk.

Swapping is typically used in conjunction with dynamic partitioning. Memory changes over time as processes move in and out:

```
State 1   State 2   State 3   State 4   State 5   State 6   State 7
+-----+   +-----+   +-----+   +-----+   +-----+   +-----+   +-----+
|     |   |     |   |  C  |   |  C  |   |  C  |   |  C  |   |  C  |
|     |   |  B  |   |  B  |   |  B  |   |  B  |   |     |   |  A  |
|  A  |   |  A  |   |  A  |   |     |   |  D  |   |  D  |   |  D  |
| OS  |   | OS  |   | OS  |   | OS  |   | OS  |   | OS  |   | OS  |
+-----+   +-----+   +-----+   +-----+   +-----+   +-----+   +-----+
```
(Grey/blank areas represent unused memory.)

### 11.1 Limitations of Swapping

| Problem | Description |
| :--- | :--- |
| Size constraint | A process must fit entirely within physical memory (no partial loading under contiguous allocation) |
| Fragmentation | Memory fragments over time; compaction required |
| Dual residence | A process can exist partially in memory and partially on disk simultaneously |

**Overlays** partially solve the size-constraint problem by subdividing a process over time (primarily data), but do **not** solve external fragmentation.

---

## Solved Exercises

### Exercise 1: CPU Utilization with Multiprogramming

**Problem:**
A system has $p = 0.80$ (80% I/O wait). How many concurrent processes ($v$) are needed to achieve at least 90% CPU utilization?

**Solution:**

$$
\text{CPU} = 1 - p^v \geq 0.90
$$

$$
p^v \leq 0.10
$$

$$
0.80^v \leq 0.10
$$

Taking logarithms:

$$
v \cdot \ln(0.80) \leq \ln(0.10)
$$

$$
v \geq \frac{\ln(0.10)}{\ln(0.80)} = \frac{-2.3026}{-0.2231} \approx 10.32
$$

Therefore, $v \geq 11$ processes are needed to achieve $\geq 90\%$ CPU utilization when $p = 0.80$.

---

### Exercise 2: Internal Fragmentation in Equal-Size Partitions

**Problem:**
A system uses fixed equal-size partitions of 8 MB each (5 partitions). Process sizes are: 2 MB, 7 MB, 5 MB, 3 MB, 8 MB. Calculate total internal fragmentation.

**Solution:**

| Process | Size | Partition Size | Internal Fragmentation |
| :--- | :--- | :--- | :--- |
| P1 | 2 MB | 8 MB | 6 MB |
| P2 | 7 MB | 8 MB | 1 MB |
| P3 | 5 MB | 8 MB | 3 MB |
| P4 | 3 MB | 8 MB | 5 MB |
| P5 | 8 MB | 8 MB | 0 MB |

$$
\text{Total internal fragmentation} = 6 + 1 + 3 + 5 + 0 = 15 \text{ MB}
$$

Out of $5 \times 8 = 40$ MB total memory (excluding OS), 15 MB (37.5%) is wasted.

---

### Exercise 3: Placement Algorithms — Worked Example (from slides)

**Problem:**
Free memory blocks (in order): 8K, 12K, 22K, 18K, 8K, 6K, 14K, 36K.
The **last allocation** was in the 18K block (14K was allocated there, leaving a small used portion).
Allocate a new block of **16K**. Show the result for First-Fit, Best-Fit, and Next-Fit.

**Solution:**

Free blocks that can satisfy 16K: 22K, 18K (partially — but the slide shows 18K as occupied after 14K allocation, so it is not free), 36K.

Examining only **free** blocks $\geq 16K$: 22K (position 3), 36K (last position).

**First-Fit:**
Scan from the beginning. First free block $\geq 16K$ is **22K**.
Allocate 16K there. Remaining fragment: $22 - 16 = 6K$.

**Best-Fit:**
Scan all free blocks. Smallest block $\geq 16K$: **18K** (if available) → from the slide the 18K block is shown as occupied; next candidate is **22K** (residual 6K). The slide confirms Best-Fit selects 18K and produces a **2K** residual.

> **[Key Insight]** The slide example shows the 18K block as still containing a free portion. Best-Fit selected 18K (16K allocated, 2K residual) — this is the smallest block that fits, confirming it leaves the smallest fragment of all three algorithms but contributes to fine-grained fragmentation over time.

**Next-Fit:**
Scan from the **last allocation point** (after the 18K block → the 8K, 6K, 14K, 36K region). First free block $\geq 16K$ from that point: **36K**.
Allocate 16K there. Remaining fragment: $36 - 16 = 20K$.

**Summary:**

| Algorithm | Block Used | Residual Fragment |
| :--- | :--- | :--- |
| First-Fit | 22K | 6K |
| Best-Fit | 18K | 2K |
| Next-Fit | 36K | 20K |

---

### Exercise 4: Dynamic Partitioning — First-Fit (Άσκηση 2 from slides)

**Problem:**
Free memory blocks (in order): 100KB, 500KB, 200KB, 300KB, 600KB.
Process requests arrive in order: 212KB, 417KB, 112KB, 426KB.
Apply **First-Fit**. Show the state of free blocks after each allocation.

**Solution:**

Initial free list: [100, 500, 200, 300, 600]

**Request 212KB:**
First-Fit scans: 100 (too small), 500 ($\geq$ 212). Allocate from 500KB block.
Residual: $500 - 212 = 288KB$.
Free list: [100, 288, 200, 300, 600]

**Request 417KB:**
First-Fit scans: 100 (no), 288 (no), 200 (no), 300 (no), 600 ($\geq$ 417). Allocate from 600KB.
Residual: $600 - 417 = 183KB$.
Free list: [100, 288, 200, 300, 183]

**Request 112KB:**
First-Fit scans: 100 (no), 288 ($\geq$ 112). Allocate from 288KB.
Residual: $288 - 112 = 176KB$.
Free list: [100, 176, 200, 300, 183]

**Request 426KB:**
First-Fit scans: 100, 176, 200, 300 — all $< 426$. 183 also $< 426$. **Cannot satisfy.** Request fails (or process waits).
Free list: [100, 176, 200, 300, 183] (unchanged)

---

### Exercise 5: Dynamic Partitioning — Best-Fit (Άσκηση 2 from slides)

**Problem:** Same initial free list and requests as Exercise 4. Apply **Best-Fit**.

**Solution:**

Initial free list: [100, 500, 200, 300, 600]

**Request 212KB:**
Blocks $\geq 212$: 500, 300, 600. Smallest is **300KB**.
Residual: $300 - 212 = 88KB$.
Free list: [100, 500, 200, 88, 600]

**Request 417KB:**
Blocks $\geq 417$: 500, 600. Smallest is **500KB**.
Residual: $500 - 417 = 83KB$.
Free list: [100, 83, 200, 88, 600]

**Request 112KB:**
Blocks $\geq 112$: 200, 600. Smallest is **200KB**.
Residual: $200 - 112 = 88KB$.
Free list: [100, 83, 88, 88, 600]

**Request 426KB:**
Blocks $\geq 426$: 600. Allocate from **600KB**.
Residual: $600 - 426 = 174KB$.
Free list: [100, 83, 88, 88, 174]

All requests satisfied.

---

### Exercise 6: Dynamic Partitioning — Next-Fit (Άσκηση 2 from slides)

**Problem:** Same initial free list [100, 500, 200, 300, 600]. Last allocation was before the **200KB block**. Apply **Next-Fit**.

**Solution:**

Scan starts **at** the 200KB block (the block after the last placement point).

**Request 212KB:**
Start at 200KB: 200 (no), 300 ($\geq 212$). Allocate from **300KB**.
Residual: $300 - 212 = 88KB$. Last pointer → after 300KB block.
Free list: [100, 500, 200, 88, 600]

**Request 417KB:**
Start after 300KB block: scan 88 (no), 600 ($\geq 417$). Allocate from **600KB**.
Residual: $600 - 417 = 183KB$. Last pointer → after 600KB block.
Free list: [100, 500, 200, 88, 183]

**Request 112KB:**
Wrap around from end: scan 100 (no), 500 ($\geq 112$). Allocate from **500KB**.
Residual: $500 - 112 = 388KB$. Last pointer → after 500KB block.
Free list: [100, 388, 200, 88, 183]

**Request 426KB:**
Start after 500KB block: scan 200 (no), 88 (no), 183 (no); wrap: 100 (no), 388 (no). **Cannot satisfy.**
Free list: [100, 388, 200, 88, 183] (unchanged)

---

### Exercise 7: Placement Algorithm 1 (Άσκηση 1 from slides)

**Problem:**
Memory image (left to right = low to high address). Shaded = occupied, white = free, black = last allocation point (12KB was last placed there).

| 20KB | [occ] | 30KB | [occ] | 12KB | [last] | 32KB | [occ] | 24KB | [occ] | 48KB |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

Free blocks: **20KB**, **30KB**, **32KB**, **48KB** (the 12KB block is the last-used region; 24KB is occupied).
Allocate **22KB**. Show result for First-Fit, Best-Fit, Next-Fit.

**Solution:**

Free blocks $\geq$ 22KB: 30KB, 32KB, 48KB.

**First-Fit:** Scan from start → first free block $\geq$ 22 is **30KB**.
Allocate 22KB; residual = **8KB**.

**Best-Fit:** Smallest free block $\geq$ 22 is **30KB** (residual 8K) — 30 is closer to 22 than 32 or 48.
Allocate 22KB; residual = **8KB**.

> **[Key Insight]** In this particular instance First-Fit and Best-Fit select the same block. Best-Fit is not always distinguishable from First-Fit in small examples.

**Next-Fit:** Last placement was in the 12KB region (between the two occupied blocks at position 5). Scan forward: next free block from that point = **32KB**.
Allocate 22KB; residual = **10KB**.

---

## Exam Tips

> **[Exam Tip — CPU Utilization Formula]**
> When asked to find the minimum number of processes $v$ for a target CPU utilization $u$, rearrange $1 - p^v \geq u$ to $p^v \leq 1 - u$ and apply logarithms: $v \geq \dfrac{\ln(1-u)}{\ln(p)}$. Always round **up** to the nearest integer. Do not forget to verify with the original formula.

> **[Exam Tip — Fragmentation Identification]**
> - **Internal** fragmentation: the wasted space is *inside* an allocated block — it belongs to a process that does not use it. Associated with **fixed partitioning**.
> - **External** fragmentation: the wasted space is *between* allocated blocks — it is free, but split into pieces too small to use. Associated with **dynamic partitioning**.
> These are mutually exclusive by definition.

> **[Exam Tip — Placement Algorithm Comparison]**
> The most common exam question asks you to apply all three algorithms to the same request and compare residual fragments. Remember:
> - **Best-Fit** always selects the *tightest* block but produces the most useless tiny fragments.
> - **Next-Fit** tends to destroy the largest block at the high end of memory.
> - **First-Fit** is empirically as good as or better than Best-Fit overall, and is faster.

> **[Exam Tip — Overlay vs. Swapping]**
> Overlays divide a **single process** over time (programmer-managed). Swapping moves **entire processes** in and out of memory (OS-managed). Overlays solve the size problem; neither technique eliminates external fragmentation.
