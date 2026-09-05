# Lecture 03: Memory Hierarchy and Cache Organization

This lecture analyzes the physical and architectural design of memory hierarchies, the principles of locality, cache placement policies, 32-bit address decomposition, block replacement strategies, write policies, and Average Memory Access Time (AMAT) modeling.

---

## 1. Locality of Reference and the Memory Pyramid

High-performance microprocessors are constrained by the **Memory Wall** — the widening latency gap between fast CPU clock cycles ($\approx 0.3 - 0.5\text{ ns}$) and slower main memory DRAM access times ($\approx 50 - 80\text{ ns}$).

```mermaid
graph TD
    Reg[Registers: < 1 ns | < 1 KB] --> L1[L1 Cache: ~1 ns | 32-64 KB]
    L1 --> L2[L2 Cache: ~3-5 ns | 256 KB - 1 MB]
    L2 --> L3[L3 Cache: ~10-20 ns | 4 - 32 MB]
    L3 --> DRAM[Main Memory DRAM: ~50-80 ns | 8 - 64 GB]
    DRAM --> Storage[Solid State Storage SSD: ~10-100 us | 1 - 4 TB]
    style Reg fill:#ffebee
    style L1 fill:#ffcdd2
    style L2 fill:#ef9a9a
    style L3 fill:#e57373
    style DRAM fill:#ef5350
    style Storage fill:#d32f2f
```

### 1.1 Fundamental Principles of Locality
1. **Temporal Locality:** If a memory location is referenced, it is highly likely to be referenced again in the near future (e.g., loop counters, accumulator variables, subroutine instructions).
2. **Spatial Locality:** If a memory location is referenced, adjacent memory locations are likely to be referenced soon (e.g., sequential array iterations, contiguous instruction execution).

---

## 2. Cache Mapping Architectures

A cache consists of $N$ lines, each storing a data block of $B$ bytes along with metadata bits (Valid bit $V$, Tag, and optional Dirty bit $D$).

### 2.1 Direct-Mapped Cache
Every main memory block maps to exactly one predetermined cache line index:
$$
\text{Cache Line Index} = (\text{Block Address}) \pmod N
$$
- Advantage: Minimal lookup latency; single comparator required.
- Disadvantage: High conflict miss rate when multiple frequently accessed blocks map to the same line index.

### 2.2 $N$-Way Set-Associative Cache
The cache is partitioned into $S$ sets, where each set houses $W$ parallel ways (lines):
$$
S = \frac{\text{Total Cache Capacity } C}{W \times B}
$$
$$
\text{Set Index} = (\text{Block Address}) \pmod S
$$
A block mapping to set $S_i$ can reside in any of the $W$ lines within that set.
- Advantage: Significantly reduces conflict misses.
- Disadvantage: Requires $W$ parallel comparators and an associative multiplexer, increasing hit latency and silicon area.

### 2.3 Fully Associative Cache
Any block from memory can reside in any arbitrary cache line ($S = 1$, set index bits $= 0$).
- Advantage: Completely eliminates conflict misses.
- Disadvantage: Requires $N$ parallel comparators; impractical for large caches (used primarily for Translation Lookaside Buffers - TLBs).

---

## 3. 32-Bit Memory Address Bitfield Decomposition

A 32-bit physical byte address is partitioned into three orthogonal bitfields:

```
+---------------------------------+--------------------------+---------------------+
|            Tag (t bits)         |     Set Index (s bits)   | Byte Offset (b bits)|
+---------------------------------+--------------------------+---------------------+
<--------------------------------------- 32 bits ---------------------------------->
```

### 3.1 Bitfield Calculation Formulas
1. **Byte Offset ($b$):** Identifies the target byte within the fetched block of $B$ bytes:
   $$
   b = \log_2(B)
   $$
2. **Set Index ($s$):** Identifies which set to inspect among $S$ total sets:
   $$
   s = \log_2(S) = \log_2\left(\frac{C}{W \times B}\right)
   $$
3. **Tag ($t$):** Distinguishes the specific memory block stored in the selected set:
   $$
   t = 32 - (s + b)
   $$

### 3.2 Worked Example
Consider a $64\text{ KB}$, 4-way set-associative cache with 64-byte blocks over a 32-bit address space:
- Block size $B = 64\text{ bytes} \implies b = \log_2(64) = 6\text{ bits}$.
- Total blocks $N = \frac{64 \times 1024}{64} = 1024\text{ blocks}$.
- Number of sets $S = \frac{N}{W} = \frac{1024}{4} = 256\text{ sets} \implies s = \log_2(256) = 8\text{ bits}$.
- Tag bits $t = 32 - 8 - 6 = 18\text{ bits}$.

---

## 4. Cache Replacement Policies

When a set is fully occupied upon a cache miss, an existing block must be evicted:
1. **Least Recently Used (LRU):** Evicts the line that has not been accessed for the longest duration. Requires maintaining age state bits per set (optimal temporal locality exploitation).
2. **First-In, First-Out (FIFO):** Evicts the oldest allocated block regardless of recent access frequency.
3. **Pseudo-LRU (Tree-Based):** Uses a binary tree of flag bits to approximate LRU with $W - 1$ tracking bits instead of $\log_2(W!)$ bits.
4. **Random:** Selects a victim uniformly at random; simple hardware requiring no state tracking.

---

## 5. Write Policies and Coherency

Handling CPU write operations involves two design decisions:

### 5.1 Write Hits
- **Write-Through:** Data written to both cache line and main memory simultaneously.
  - Advantage: Memory always holds current data; simple crash recovery.
  - Disadvantage: High memory bus traffic; mitigated using a write buffer.
- **Write-Back:** Data written only to the cache line. A **Dirty Bit ($D$)** is set to 1. Memory is updated only when the dirty block is evicted.
  - Advantage: Low memory traffic for repeatedly modified data.
  - Disadvantage: Memory contains stale data until eviction.

### 5.2 Write Misses
- **Write-Allocate:** The missing block is loaded into the cache, followed by writing. Typically paired with Write-Back.
- **No-Write-Allocate (Write-Around):** Bypasses cache and writes directly to memory. Typically paired with Write-Through.

---

## 6. Performance Evaluation: Average Memory Access Time (AMAT)

The performance of a single-level cache is quantified by:
$$
\text{AMAT} = t_{\text{hit}} + (\text{Miss Rate} \times \text{Miss Penalty})
$$

For a multilevel hierarchy with L1 and L2 caches:
$$
\text{AMAT} = t_{\text{hit}, L1} + \text{MR}_{L1} \times \left( t_{\text{hit}, L2} + \text{MR}_{\text{local}, L2} \times t_{\text{DRAM}} \right)
$$
where:
- $\text{MR}_{L1} = \frac{\text{L1 Misses}}{\text{Total CPU References}}$
- $\text{MR}_{\text{local}, L2} = \frac{\text{L2 Misses}}{\text{L1 Misses}}$
- $\text{MR}_{\text{global}, L2} = \text{MR}_{L1} \times \text{MR}_{\text{local}, L2} = \frac{\text{L2 Misses}}{\text{Total CPU References}}$

