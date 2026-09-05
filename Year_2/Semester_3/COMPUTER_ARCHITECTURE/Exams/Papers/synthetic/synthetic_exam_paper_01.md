# Synthetic Practice Exam 01: Computer Architecture and Organization

**Course:** Computer Architecture (Course Code: 301)  
**Academic Level:** 2nd Year, 3rd Semester  
**Exam Type:** Synthetic Examination Paper  
**Total Points:** 100 points  
**Time Allowed:** 120 minutes  

---

## Examination Instructions
- This examination consists of four (4) mandatory sections totaling 100 points.
- Show all mathematical derivations, bitfield calculations, and truth tables clearly.
- State all assumptions regarding clock edges and pipeline latch timing where applicable.

---

## Section A: Instruction Set Architecture & MIPS Binary Encoding (25 Points)

### Question A.1: Binary Machine Code Decoding (13 Points)
A processor fetches the 32-bit instruction word `0x02538822` from memory address `0x00400040`.
1. Identify the MIPS instruction format (R-type, I-type, or J-type). *(2 Points)*
2. Decompose the instruction into its constituent bitfields. State the binary pattern and decimal integer value for each field (`opcode`, `rs`, `rt`, `rd`, `shamt`, `funct` or `immediate`/`address`). *(6 Points)*
3. Identify the assembly instruction mnemonic and write the complete symbolic MIPS assembly instruction. *(5 Points)*

### Question A.2: Memory Addressing & Branch Distance (12 Points)
A conditional branch instruction `bne $s0, $s1, target` is located at memory address `0x00400080`.
1. If the label `target` is located at memory address `0x00400100`, calculate the exact 16-bit two's complement immediate value encoded within the instruction. *(6 Points)*
2. If the label `target` was located at address `0x00400020` (a backward branch), what would be the encoded 16-bit immediate value? Express your answer in binary and hexadecimal. *(6 Points)*

---

## Section B: Single-Cycle Datapath & Critical Path Timing (25 Points)

### Question B.1: Datapath Control Signal Generation (15 Points)
Consider the classic single-cycle MIPS datapath supporting instructions `add`, `sub`, `lw`, `sw`, and `beq`.
1. Complete the control signals table for an R-type instruction `slt $t0, $s1, $s2` and an immediate instruction `addi $t1, $s2, -15`. State the logical values (`0`, `1`, or `X` for don't-care) for: `RegDst`, `ALUSrc`, `MemtoReg`, `RegWrite`, `MemRead`, `MemWrite`, `Branch`, and `ALUOp`. *(10 Points)*
2. Suppose a hardware defect permanently forces the `ALUSrc` control line to `1` (stuck-at-1 fault). Explain which instructions continue to operate properly and which instructions fail, specifying the exact nature of the failure. *(5 Points)*

### Question B.2: Critical Path & Frequency Calculation (10 Points)
The propagation delays of the datapath functional units are measured as follows:
- Instruction Memory Read ($t_{\text{IM}}$): $280\text{ ps}$
- Register File Read ($t_{\text{RF-read}}$): $140\text{ ps}$
- Register File Write Setup ($t_{\text{RF-write}}$): $110\text{ ps}$
- ALU Operation ($t_{\text{ALU}}$): $210\text{ ps}$
- Data Memory Read ($t_{\text{DM-read}}$): $320\text{ ps}$
- Data Memory Write ($t_{\text{DM-write}}$): $290\text{ ps}$
- Single Multiplexer ($t_{\text{Mux}}$): $25\text{ ps}$
- Sign Extension / Logic Gates ($t_{\text{logic}}$): $15\text{ ps}$

1. Identify the critical instruction that dictates the minimum clock cycle time and determine the exact path of functional units traversed. *(5 Points)*
2. Calculate the minimum clock cycle duration $T_{\text{cycle}}$ and the maximum operational clock frequency $f_{\max}$ in gigahertz (GHz). *(5 Points)*

---

## Section C: 5-Stage Pipelining, Hazards, and Forwarding (25 Points)

### Question C.1: Hazard Detection and Forwarding Unit Equations (15 Points)
Consider the following assembly code executing on a 5-stage RISC pipeline (IF, ID, EX, MEM, WB):

```mips
I1: add $t1, $t2, $t3
I2: sub $t4, $t1, $t5
I3: and $t6, $t1, $t7
I4: or  $t8, $t4, $t1
```

1. Construct the clock-cycle execution timing chart assuming the processor contains a **Full Forwarding Unit** (EX-to-EX and MEM-to-EX bypass). *(8 Points)*
2. State the values of the control multiplexer signals `ForwardA` and `ForwardB` at clock cycles 4, 5, and 6 for the active ALU inputs. *(7 Points)*

### Question C.2: Load-Use Data Hazard & Scheduling (10 Points)
Consider the sequence:
```mips
L1: lw  $s0, 0($t0)
L2: add $t1, $s0, $t2
L3: lw  $s1, 4($t0)
L4: sub $t3, $s1, $t4
```
1. Draw the pipeline execution table showing the stall bubbles inserted by the Hazard Detection Unit. How many total cycles are required to execute this sequence? *(5 Points)*
2. Reschedule the sequence without changing its programmatic output to execute in the minimum possible number of clock cycles. State the speedup achieved. *(5 Points)*

---

## Section D: Cache Memory Architectures and Performance (25 Points)

### Question D.1: Set-Associative Cache Decomposition (15 Points)
A computer system features a 32-bit physical byte-addressed memory space. The processor contains an on-chip $128\text{ KB}$ ($131,072\text{ bytes}$) 8-way set-associative data cache with 64-byte cache lines.
1. Calculate the number of bits allocated to the **Byte Offset ($b$)**, **Set Index ($s$)**, and **Tag ($t$)** fields. *(6 Points)*
2. Determine the total hardware storage capacity (in bits) required to construct the cache array, including 1 Valid bit, 1 Dirty bit, and Tag bits for each line. *(5 Points)*
3. Given memory address `0x004F3A8C`, determine which set index this address maps to, and find the corresponding hex value of its tag. *(4 Points)*

### Question D.2: Multilevel Memory Hierarchy AMAT (10 Points)
A processor operates at $2.5\text{ GHz}$ ($T_{\text{cycle}} = 0.4\text{ ns}$) with a two-level cache hierarchy:
- Instruction access mix: $70\%$; Data access mix: $30\%$.
- L1 Instruction Cache: Hit time $= 1\text{ cycle}$, Miss rate $= 1.5\%$.
- L1 Data Cache: Hit time $= 1\text{ cycle}$, Miss rate $= 5.0\%$.
- Unified L2 Cache: Hit time $= 8\text{ cycles}$, Local miss rate $= 12.0\%$.
- Main Memory (DRAM): Access latency $= 100\text{ cycles}$.

1. Calculate the overall L1 miss rate and global L2 miss rate. *(5 Points)*
2. Calculate the Average Memory Access Time (AMAT) in clock cycles and in nanoseconds. *(5 Points)*

