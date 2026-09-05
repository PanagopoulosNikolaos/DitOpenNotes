# Solutions to Synthetic Practice Exam 01: Computer Architecture

**Course:** Computer Architecture (Course Code: 301)  
**Exam Reference:** [`../../Papers/synthetic/synthetic_exam_paper_01.md`](../../Papers/synthetic/synthetic_exam_paper_01.md)  
**Total Points:** 100 points  

---

## Section A Solutions: ISA & MIPS Encoding (25 Points)

### Question A.1: Decoding `0x02538822` (13 Points)
1. **Binary Conversion (32 bits):**
   ```
   0x02538822 = 0000 0010 0101 0011 1000 1000 0010 0010
   ```
   - Bit 31..26 (`opcode`): `000000` $\implies$ **R-Type Format**. *(2 Points)*

2. **Bitfield Partitioning:**
   - `opcode` (bits 31..26): `000000` (Decimal: 0)
   - `rs` (bits 25..21): `10010` (Decimal: 18, register `$s2`)
   - `rt` (bits 20..16): `10011` (Decimal: 19, register `$s3`)
   - `rd` (bits 15..11): `10001` (Decimal: 17, register `$s1`)
   - `shamt` (bits 10..6): `00000` (Decimal: 0)
   - `funct` (bits 5..0): `100010` (Hex: `0x22`, Decimal: 34) *(6 Points)*

3. **Instruction Identification:**
   - Funct `0x22` specifies the `sub` (subtract signed) operation.
   - Assembly Syntax: `sub $rd, $rs, $rt`
   - Complete Symbolic Code:
     ```mips
     sub $s1, $s2, $s3
     ```
     *(5 Points)*

---

### Question A.2: Branch Distance Calculations (12 Points)
In MIPS, the target address for PC-relative branch instructions is computed as:
$$
\text{Target Address} = (PC + 4) + (\text{SignExt}(\text{immediate}) \ll 2)
$$
Rearranging to solve for the immediate field:
$$
\text{immediate} = \frac{\text{Target Address} - (PC + 4)}{4}
$$

1. **Forward Branch to `0x00400100`:**
   - Current $PC = \text{0x00400080} \implies PC + 4 = \text{0x00400084}$.
   - Offset in bytes:
     $$\Delta = \text{0x00400100} - \text{0x00400084} = 256 - 132 = 124\text{ bytes} = \text{0x0000007C}$$
   - Offset in words (immediate):
     $$\text{immediate} = \frac{124}{4} = 31 = \text{0x001F}$$
   - Encoded 16-bit field: `0000 0000 0001 1111` (`0x001F`). *(6 Points)*

2. **Backward Branch to `0x00400020`:**
   - Current $PC + 4 = \text{0x00400084}$.
   - Offset in bytes:
     $$\Delta = \text{0x00400020} - \text{0x00400084} = -100\text{ bytes} = -\text{0x64}$$
   - Offset in words:
     $$\text{immediate} = \frac{-100}{4} = -25$$
   - 16-bit Two's Complement of $-25$:
     $$+25 = 0000\ 0000\ 0001\ 1001_2$$
     $$\text{Invert: } 1111\ 1111\ 1110\ 0110_2$$
     $$\text{Add 1: } 1111\ 1111\ 1110\ 0111_2 = \text{0xFFE7}$$
   - Encoded 16-bit field: `1111 1111 1110 0111` (`0xFFE7`). *(6 Points)*

---

## Section B Solutions: Datapath & Timing (25 Points)

### Question B.1: Control Signal Generation (15 Points)
1. **Control Signal Truth Table:**

| Instruction | `RegDst` | `ALUSrc` | `MemtoReg` | `RegWrite` | `MemRead` | `MemWrite` | `Branch` | `ALUOp` |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `slt $t0, $s1, $s2` | 1 | 0 | 0 | 1 | 0 | 0 | 0 | `10` |
| `addi $t1, $s2, -15` | 0 | 1 | 0 | 1 | 0 | 0 | 0 | `00` |
*(10 Points: 5 points per instruction row)*

2. **`ALUSrc` Stuck-at-1 Fault Analysis:**
   - `ALUSrc = 1` forces the second ALU input to be the sign-extended 16-bit immediate constant rather than register `Reg[rt]`.
   - **Correct Execution:** Instructions that inherently require `ALUSrc = 1` continue functioning normally. These include `lw`, `sw`, and `addi`. *(2 Points)*
   - **Faulty Execution:** R-type instructions (`add`, `sub`, `slt`, `and`, `or`) and branches (`beq`, `bne`) fail catastrophically because the ALU operates on the bitfield containing bits 15..0 of the instruction word instead of `Reg[rt]`. *(3 Points)*

---

### Question B.2: Critical Path Timing Analysis (10 Points)
1. **Critical Path Identification:**
   The longest operational delay is imposed by the load word (`lw`) instruction:
   $$
   \text{Path: } PC \to \text{IM} \to \text{RF (read)} \to \text{ALU} \to \text{DM (read)} \to \text{Mux (MemtoReg)} \to \text{RF (write setup)}
   $$
   *(5 Points)*

2. **Timing & Frequency Calculations:**
   $$
   T_{\text{cycle}} = t_{\text{IM}} + t_{\text{RF-read}} + t_{\text{ALU}} + t_{\text{DM-read}} + t_{\text{Mux}} + t_{\text{RF-write}}
   $$
   $$
   T_{\text{cycle}} = 280\text{ ps} + 140\text{ ps} + 210\text{ ps} + 320\text{ ps} + 25\text{ ps} + 110\text{ ps} = 1085\text{ ps}
   $$
   $$
   f_{\max} = \frac{1}{T_{\text{cycle}}} = \frac{1}{1085 \times 10^{-12}\text{ s}} \approx 921.66\text{ MHz} \approx 0.922\text{ GHz}
   $$
   *(5 Points)*

---

## Section C Solutions: Pipelining & Hazards (25 Points)

### Question C.1: Forwarding Unit Timing Trace (15 Points)
1. **Execution Timing Chart (with Full Forwarding):**

| Instruction | C1 | C2 | C3 | C4 | C5 | C6 | C7 |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `I1: add $t1, $t2, $t3` | IF | ID | **EX** | **MEM** | WB | | |
| `I2: sub $t4, $t1, $t5` | | IF | ID | **EX** | **MEM** | WB | |
| `I3: and $t6, $t1, $t7` | | | IF | ID | **EX** | MEM | WB |
| `I4: or  $t8, $t4, $t1` | | | | IF | ID | **EX** | MEM |

*(8 Points)*

2. **Multiplexer Control Signals (`ForwardA`, `ForwardB`):**
   - **Cycle 4 (`I2` in EX):**
     - Operand `$t1` is generated by `I1` (currently in MEM).
     - `ForwardA = 10` (EX-to-EX forward from `EX/MEM` latch).
     - `ForwardB = 00` (Operand `$t5` read from Register File). *(2.5 Points)*
   - **Cycle 5 (`I3` in EX):**
     - Operand `$t1` is in WB stage of `I1`.
     - `ForwardA = 01` (MEM-to-EX forward from `MEM/WB` latch).
     - `ForwardB = 00` (`$t7` from Register File). *(2.5 Points)*
   - **Cycle 6 (`I4` in EX):**
     - Operand `$t4` is in WB stage of `I2` $\implies$ `ForwardA = 01`.
     - Operand `$t1` was committed to Register File in Cycle 5 $\implies$ `ForwardB = 00`. *(2 Points)*

---

### Question C.2: Load-Use Hazard & Scheduling (10 Points)
1. **Unscheduled Pipeline Timing with Stalls:**
   Because memory data from a load arrives at the end of the MEM stage, dependent ALU instructions require 1 stall bubble:

| Instruction | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | C9 |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `L1: lw  $s0, 0($t0)` | IF | ID | EX | MEM | WB | | | | |
| `[stall bubble 1]`   | | | IF | ID | **NOP** | | | | |
| `L2: add $t1, $s0, $t2` | | | | IF | ID | EX | MEM | WB | |
| `L3: lw  $s1, 4($t0)` | | | | | IF | ID | EX | MEM | WB |
| `[stall bubble 2]`   | | | | | | IF | ID | **NOP** | |
| `L4: sub $t3, $s1, $t4` | | | | | | | IF | ID | EX |

   - Total Execution Time: 9 clock cycles to complete. *(5 Points)*

2. **Rescheduled Code Sequence:**
   Interleave independent load `L3` between `L1` and `L2`:
   ```mips
   L1: lw  $s0, 0($t0)    # Loads $s0
   L3: lw  $s1, 4($t0)    # Independent load fills delay slot for $s0
   L2: add $t1, $s0, $t2  # Receives $s0 via MEM-to-EX forwarding
   L4: sub $t3, $s1, $t4  # Receives $s1 via MEM-to-EX forwarding
   ```
   - Total cycles reduced from 9 to 7 clock cycles (0 stalls).
   - Speedup: $\frac{9}{7} \approx 1.286\times$ ($28.6\%$ speedup). *(5 Points)*

---

## Section D Solutions: Cache & Memory Hierarchy (25 Points)

### Question D.1: Cache Bitfield Decomposition (15 Points)
1. **Bitfield Allocations:**
   - Block Size $B = 64\text{ bytes} \implies b = \log_2(64) = 6\text{ bits}$. (2 pts)
   - Total Lines $N = \frac{128 \times 1024\text{ bytes}}{64\text{ bytes}} = 2048\text{ lines}$.
   - Number of Sets:
     $$S = \frac{N}{W} = \frac{2048}{8\text{ ways}} = 256\text{ sets}$$
   - Set Index bits: $s = \log_2(256) = 8\text{ bits}$. (2 pts)
   - Tag bits: $t = 32 - s - b = 32 - 8 - 6 = 18\text{ bits}$. (2 pts)

2. **Total Hardware Storage Capacity:**
   - Per line: $1\text{ (Valid)} + 1\text{ (Dirty)} + 18\text{ (Tag)} + (64 \times 8)\text{ (Data)} = 20 + 512 = 532\text{ bits}$.
   - Across all 2048 lines:
     $$\text{Total Bits} = 2048 \times 532 = 1,089,536\text{ bits} = 136,192\text{ bytes} \approx 133.0\text{ KB}$$
     *(5 Points)*

3. **Mapping Address `0x004F3A8C`:**
   - Binary representation: `0000 0000 0100 1111 0011 1010 1000 1100`
   - Offset (Bits 5..0): `001100` (`0x0C` = 12)
   - Set Index (Bits 13..6): `1010 1000` (`0xA8` = Decimal 168)
   - Tag (Bits 31..14): `0000 0000 0100 1111 00` (`0x013C` = Decimal 316)
   - Address maps to **Set 168** (`0xA8`) with Tag **`0x013C`**. *(4 Points)*

---

### Question D.2: Multilevel AMAT Calculation (10 Points)
1. **Miss Rates:**
   - Overall L1 Miss Rate:
     $$\text{MR}_{L1,\text{overall}} = (0.70 \times 0.015) + (0.30 \times 0.050) = 0.0105 + 0.0150 = 0.0255 = 2.55\%$$
   - Global L2 Miss Rate:
     $$\text{MR}_{L2,\text{global}} = \text{MR}_{L1,\text{overall}} \times \text{MR}_{L2,\text{local}} = 0.0255 \times 0.120 = 0.00306 = 0.306\%$$
     *(5 Points)*

2. **Average Memory Access Time (AMAT):**
   - L1 Miss Penalty:
     $$\text{Penalty}_{L1} = t_{\text{hit}, L2} + (\text{MR}_{L2,\text{local}} \times t_{\text{mem}}) = 8 + (0.12 \times 100) = 8 + 12 = 20\text{ cycles}$$
   - Overall AMAT:
     $$\text{AMAT} = t_{\text{hit}, L1} + (\text{MR}_{L1,\text{overall}} \times \text{Penalty}_{L1}) = 1 + (0.0255 \times 20) = 1 + 0.51 = 1.51\text{ cycles}$$
   - In nanoseconds ($T_{\text{cycle}} = 0.4\text{ ns}$):
     $$\text{AMAT}_{[\text{ns}]} = 1.51 \times 0.4\text{ ns} = 0.604\text{ ns}$$
     *(5 Points)*

