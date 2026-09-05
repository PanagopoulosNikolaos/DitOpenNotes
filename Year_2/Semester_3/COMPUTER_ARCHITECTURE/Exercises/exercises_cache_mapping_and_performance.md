# Exercises: Cache Memory Mapping, Address Decoding, and Performance Analysis

Comprehensive quantitative drills covering cache address bitfield decomposition, sequential memory access traces with LRU replacement, total hardware overhead calculations, and multilevel Average Memory Access Time (AMAT) modeling for **Computer Architecture (Course Code: 301)**.

---

## Problem 1: Cache Address Bitfield Decomposition

A processor employs a 32-bit byte-addressed physical memory architecture. The cache memory system has a total data capacity of $32\text{ KB}$ ($32,768\text{ bytes}$) with a block size of $32\text{ bytes}$.

### Questions:
1. Determine the number of **Byte Offset bits ($b$)**, **Set Index bits ($s$)**, and **Tag bits ($t$)** under each of the following configurations:
   - **Configuration A:** Direct-Mapped Cache.
   - **Configuration B:** 4-Way Set-Associative Cache.
   - **Configuration C:** Fully Associative Cache.
2. For Configuration B (4-way set-associative), calculate the **Total Hardware Overhead** in bits required to implement the cache (including Valid bits and Tag bits alongside data bits).

---

## Solution to Problem 1

### 1. Address Bitfield Calculations

For any 32-bit physical address:
$$
\text{Tag } (t) + \text{Set Index } (s) + \text{Byte Offset } (b) = 32\text{ bits}
$$

- **Byte Offset ($b$):**
  For a 32-byte block size:
  $$b = \log_2(32) = 5\text{ bits}$$
  This is identical across all three configurations.

- **Total Number of Cache Lines ($N$):**
  $$N = \frac{\text{Total Capacity } C}{\text{Block Size } B} = \frac{32,768\text{ bytes}}{32\text{ bytes}} = 1024\text{ lines}$$

#### Configuration A: Direct-Mapped Cache
- Number of sets $S = N = 1024$.
- Set Index bits: $s = \log_2(1024) = 10\text{ bits}$.
- Tag bits: $t = 32 - s - b = 32 - 10 - 5 = 17\text{ bits}$.
- **Layout:** `[Tag: 17 bits | Index: 10 bits | Offset: 5 bits]`

#### Configuration B: 4-Way Set-Associative Cache
- Ways per set $W = 4$.
- Number of sets:
  $$S = \frac{N}{W} = \frac{1024}{4} = 256\text{ sets}$$
- Set Index bits: $s = \log_2(256) = 8\text{ bits}$.
- Tag bits: $t = 32 - s - b = 32 - 8 - 5 = 19\text{ bits}$.
- **Layout:** `[Tag: 19 bits | Index: 8 bits | Offset: 5 bits]`

#### Configuration C: Fully Associative Cache
- Number of sets: $S = 1$.
- Set Index bits: $s = \log_2(1) = 0\text{ bits}$.
- Tag bits: $t = 32 - 0 - 5 = 27\text{ bits}$.
- **Layout:** `[Tag: 27 bits | Offset: 5 bits]`

---

### 2. Total Hardware Memory Calculation (Configuration B)

Each cache line stores:
- 1 Valid bit ($V$)
- 19 Tag bits ($t$)
- 32 bytes of payload data ($32 \times 8 = 256\text{ bits}$)

Total bits per line:
$$
\text{Bits per line} = 1 + 19 + 256 = 276\text{ bits}
$$
Since there are 1024 total lines in the cache:
$$
\text{Total Memory Storage} = 1024 \times 276 = 282,624\text{ bits} = 35,328\text{ bytes} \approx 34.5\text{ KB}
$$
The metadata overhead (Tag and Valid bits) contributes:
$$
\text{Overhead} = 1024 \times 20\text{ bits} = 20,480\text{ bits} = 2,560\text{ bytes} \quad (7.8\% \text{ storage overhead})
$$

---

## Problem 2: Sequential Memory Reference Trace

Consider a small 2-way set-associative cache with 4 sets (Set 0, Set 1, Set 2, Set 3) and a block size of 16 bytes. The cache utilizes a Least Recently Used (LRU) replacement policy and starts completely empty.

Given the following sequence of decimal byte address references:
$$
\text{Addresses: } [4, 12, 20, 36, 8, 68, 24, 40, 4]
$$

### Questions:
1. Determine the number of Tag, Index, and Offset bits for a 16-bit address space.
2. For each access, calculate the binary tag and set index, indicate Hit or Miss, classify the miss type (Compulsory / Cold, Conflict, or Capacity), and show the final state of each cache set.

---

## Solution to Problem 2

### 1. Bit Partitioning (16-bit Address)
- Block size $= 16\text{ bytes} \implies b = \log_2(16) = 4\text{ bits}$ (Bits 3..0).
- Sets $= 4 \implies s = \log_2(4) = 2\text{ bits}$ (Bits 5..4).
- Tag bits $= 16 - 2 - 4 = 10\text{ bits}$ (Bits 15..6).
- Block Address $= \lfloor \text{Address} / 16 \rfloor$.
- Set Index $= (\text{Block Address}) \pmod 4$.
- Tag $= \lfloor \text{Block Address} / 4 \rfloor$.

### 2. Step-by-Step Access Trace Table

| Step | Address | Block Addr | Set Index | Tag | Hit / Miss | Miss Classification | Evicted Block | Set Contents [Way 0, Way 1] |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | 4 | 0 | 0 | 0 | **Miss** | Compulsory | None | Set 0: [Blk 0 (MRU), —] |
| 2 | 12 | 0 | 0 | 0 | **Hit** | — | None | Set 0: [Blk 0 (MRU), —] |
| 3 | 20 | 1 | 1 | 0 | **Miss** | Compulsory | None | Set 1: [Blk 1 (MRU), —] |
| 4 | 36 | 2 | 2 | 0 | **Miss** | Compulsory | None | Set 2: [Blk 2 (MRU), —] |
| 5 | 8 | 0 | 0 | 0 | **Hit** | — | None | Set 0: [Blk 0 (MRU), —] |
| 6 | 68 | 4 | 0 | 1 | **Miss** | Compulsory | None | Set 0: [Blk 4 (MRU), Blk 0 (LRU)] |
| 7 | 24 | 1 | 1 | 0 | **Hit** | — | None | Set 1: [Blk 1 (MRU), —] |
| 8 | 40 | 2 | 2 | 0 | **Hit** | — | None | Set 2: [Blk 2 (MRU), —] |
| 9 | 4 | 0 | 0 | 0 | **Hit** | — | None | Set 0: [Blk 0 (MRU), Blk 4 (LRU)] |

### Performance Summary:
- Total References: 9
- Hits: 5 (Steps 2, 5, 7, 8, 9)
- Misses: 4 (Steps 1, 3, 4, 6)
- **Hit Rate:** $\frac{5}{9} \approx 55.56\%$
- **Miss Rate:** $\frac{4}{9} \approx 44.44\%$
- All 4 misses are **Compulsory (Cold)** misses because each missing block was referenced for the first time.

---

## Problem 3: Multilevel Average Memory Access Time (AMAT)

A high-performance CPU operates with split L1 caches and a unified L2 cache:
- **Instruction References:** $75\%$ of total memory accesses.
- **Data References:** $25\%$ of total memory accesses.
- **L1 Instruction Cache (I-Cache):** Hit time $t_{1,\text{inst}} = 1\text{ cycle}$, Miss rate $\text{MR}_{1,\text{inst}} = 2\%$.
- **L1 Data Cache (D-Cache):** Hit time $t_{1,\text{data}} = 1\text{ cycle}$, Miss rate $\text{MR}_{1,\text{data}} = 6\%$.
- **Unified L2 Cache:** Hit time $t_2 = 10\text{ cycles}$, Local miss rate $\text{MR}_{2,\text{local}} = 20\%$.
- **Main Memory (DRAM):** Access latency $t_{\text{mem}} = 120\text{ cycles}$.

### Questions:
1. Calculate the overall L1 miss rate.
2. Calculate the global L2 miss rate.
3. Calculate the Average Memory Access Time (AMAT) for instruction accesses, data accesses, and combined overall references.

---

## Solution to Problem 3

### 1. Overall L1 Miss Rate
$$
\text{MR}_{1,\text{overall}} = (0.75 \times \text{MR}_{1,\text{inst}}) + (0.25 \times \text{MR}_{1,\text{data}})
$$
$$
\text{MR}_{1,\text{overall}} = (0.75 \times 0.02) + (0.25 \times 0.06) = 0.015 + 0.015 = 0.030 = 3.0\%
$$

### 2. Global L2 Miss Rate
$$
\text{MR}_{2,\text{global}} = \text{MR}_{1,\text{overall}} \times \text{MR}_{2,\text{local}} = 0.030 \times 0.20 = 0.006 = 0.6\%
$$

### 3. AMAT Calculations

The L2 miss penalty is the DRAM latency:
$$
\text{Penalty}_{L2} = t_{\text{mem}} = 120\text{ cycles}
$$
The L1 miss penalty is the L2 access time plus any L2 miss penalty:
$$
\text{Penalty}_{L1} = t_2 + (\text{MR}_{2,\text{local}} \times t_{\text{mem}}) = 10 + (0.20 \times 120) = 10 + 24 = 34\text{ cycles}
$$

#### AMAT for Instructions:
$$
\text{AMAT}_{\text{inst}} = t_{1,\text{inst}} + (\text{MR}_{1,\text{inst}} \times \text{Penalty}_{L1}) = 1 + (0.02 \times 34) = 1 + 0.68 = 1.68\text{ cycles}
$$

#### AMAT for Data:
$$
\text{AMAT}_{\text{data}} = t_{1,\text{data}} + (\text{MR}_{1,\text{data}} \times \text{Penalty}_{L1}) = 1 + (0.06 \times 34) = 1 + 2.04 = 3.04\text{ cycles}
$$

#### Overall Combined AMAT:
$$
\text{AMAT}_{\text{overall}} = (0.75 \times \text{AMAT}_{\text{inst}}) + (0.25 \times \text{AMAT}_{\text{data}})
$$
$$
\text{AMAT}_{\text{overall}} = (0.75 \times 1.68) + (0.25 \times 3.04) = 1.26 + 0.76 = 2.02\text{ cycles}
$$
The multilevel cache hierarchy reduces memory stall overhead from 120 cycles down to an effective access time of only 2.02 clock cycles.

