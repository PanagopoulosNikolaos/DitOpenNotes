# Practice Exam 01: Computer Architecture and Organization

**Course:** Computer Architecture (Course Code 301)  
**Format:** Comprehensive Practice Examination with Full Worked Solutions  
**Total Points:** 100 points  
**Time Allowed:** 120 minutes  

---

## Part I: Examination Questions

### Section A: ISA, Instruction Encoding, and Calling Conventions (25 Points)

1. *(13 Points)* MIPS32 Instruction Encoding and Decoding:
   - **Instruction Decoding:** The 32-bit machine instruction `0x014B4820` resides in memory. Decode this word into its respective MIPS instruction format (R, I, or J). State the values of all bitfields in decimal, identify the assembly instruction mnemonic, and write the symbolic assembly code.
   - **Instruction Encoding:** Translate the MIPS assembly instruction `lw $t0, 32($s1)` into its 32-bit binary representation and hexadecimal machine code.

2. *(12 Points)* Calling Conventions and Activation Records:
   - State which registers are caller-saved versus callee-saved under standard MIPS calling conventions.
   - Explain why a leaf subroutine is not required to push `$ra` onto the stack, whereas any non-leaf subroutine must preserve `$ra`. What catastrophic failure occurs if a non-leaf procedure fails to preserve `$ra`?

---

### Section B: Single-Cycle Datapath Synthesis & Timing (25 Points)

1. *(15 Points)* Control Unit Synthesis:
   - Construct the control signal truth table (`RegDst`, `ALUSrc`, `MemtoReg`, `RegWrite`, `MemRead`, `MemWrite`, `Branch`, `ALUOp`) for the following instruction subset: `add`, `lw`, `sw`, `beq`.
   - Explain the hardware failure that occurs if the `MemtoReg` multiplexer control line becomes stuck-at-0 (permanently outputs 0). Which instructions continue executing correctly, and which fail?

2. *(10 Points)* Critical Path Timing Analysis:
   Given the following component propagation delays:
   - Instruction Memory read ($t_{\text{IM}}$): $300\text{ ps}$
   - Register File read or write ($t_{\text{RF}}$): $160\text{ ps}$
   - ALU operation ($t_{\text{ALU}}$): $220\text{ ps}$
   - Data Memory read or write ($t_{\text{DM}}$): $350\text{ ps}$
   - Multiplexer propagation ($t_{\text{Mux}}$): $30\text{ ps}$
   - Sign-extender and logic gates ($t_{\text{logic}}$): $20\text{ ps}$

   Calculate the minimum clock cycle duration $T_{\text{cycle}}$ and maximum clock frequency $f_{\max}$ for a single-cycle processor implementing `add`, `lw`, `sw`, and `beq`.

---

### Section C: Pipelining Hazards and Forwarding (25 Points)

1. *(15 Points)* Pipeline Data Hazard Analysis:
   Consider the following instruction sequence:
   ```mips
   I1: sub $s1, $t1, $t2
   I2: add $t3, $s1, $t4
   I3: and $t5, $s1, $t6
   ```
   - Draw the cycle-by-cycle execution timing diagram assuming a 5-stage pipeline **with hardware forwarding**.
   - State the forwarding multiplexer control equations that detect and resolve the RAW dependency for instruction `I2` and instruction `I3`.

2. *(10 Points)* Load-Use Interlock Stalling:
   - Explain why hardware forwarding cannot eliminate stalls when an instruction immediately consumes data loaded by a preceding `lw` instruction.
   - Write down the boolean logic equation implemented by the Hazard Detection Unit to detect a load-use hazard and describe the two actions taken by the processor during the stall cycle.

---

### Section D: Cache Memory Organization and AMAT (25 Points)

1. *(15 Points)* Cache Address Bitfield Decomposition:
   A CPU uses 32-bit byte addresses and integrates a $64\text{ KB}$ 4-way set-associative cache with 64-byte blocks.
   - Calculate the number of Byte Offset bits ($b$), Set Index bits ($s$), and Tag bits ($t$).
   - Determine the total physical storage capacity of the cache array in bits, including Valid bits ($V$) and Tag bits.

2. *(10 Points)* Multilevel AMAT Calculation:
   A microprocessor system features:
   - Clock frequency: $2.0\text{ GHz}$ ($T_{\text{cycle}} = 0.5\text{ ns}$).
   - Split L1 Caches: Hit time $= 1\text{ cycle}$. L1 I-Cache miss rate $= 2\%$. L1 D-Cache miss rate $= 8\%$.
   - Workload instruction mix: $80\%$ instructions, $20\%$ data accesses.
   - Unified L2 Cache: Hit time $= 12\text{ cycles}$, Local miss rate $= 25\%$.
   - Main Memory: Latency $= 150\text{ cycles}$.
   
   Calculate:
   - The overall L1 miss rate.
   - The global L2 miss rate.
   - The Average Memory Access Time (AMAT) in clock cycles and nanoseconds.

---

## Part II: Complete Worked Solutions & Grading Rubric

### Section A Solutions

#### 1.1 Instruction Decoding and Encoding (13 pts)
- **Decoding `0x014B4820`:**
  - Binary representation: `0000 0001 0100 1011 0100 1000 0010 0000`
  - Opcode (bits 31..26): `000000` $\implies$ **R-Type** instruction. (2 pts)
  - `rs` (bits 25..21): `01010` = 10 (`$t2`). (2 pts)
  - `rt` (bits 20..16): `01011` = 11 (`$t3`). (2 pts)
  - `rd` (bits 15..11): `01001` = 9 (`$t1`). (2 pts)
  - `shamt` (bits 10..6): `00000` = 0. (1 pt)
  - `funct` (bits 5..0): `100000` = `0x20` = 32 (`add`). (2 pts)
  - **Assembly Code:** `add $t1, $t2, $t3`. (2 pts)

- **Encoding `lw $t0, 32($s1)`:**
  - Opcode for `lw`: `100011` (`0x23` = 35).
  - Base register `rs`: `$s1` = register 17 (`10001`).
  - Target register `rt`: `$t0` = register 8 (`01000`).
  - Immediate offset: 32 = `0000 0000 0010 0000` (`0x0020`).
  - Assembled 32 bits: `1000 1110 0010 1000 0000 0000 0010 0000` = `0x8E280020`. (5 pts)

#### 1.2 Calling Conventions and Return Address Preservation (12 pts)
- **Register Preservation Conventions:**
  - Caller-saved (temporary, not preserved across calls): `$v0-$v1`, `$a0-$a3`, `$t0-$t9`. (3 pts)
  - Callee-saved (preserved across calls): `$s0-$s7`, `$sp`, `$fp`, `$ra`, `$gp`. (3 pts)
- **Return Address Mechanics:**
  - A leaf subroutine makes no `jal` calls; therefore, register `$ra` remains unaltered throughout its execution. It can return directly via `jr $ra` without accessing the stack. (3 pts)
  - In a non-leaf subroutine, executing `jal` overwrites `$ra` with the address of the instruction following the call. If the original `$ra` was not pushed onto the stack, the return address to the outer caller is destroyed. Executing `jr $ra` at the end creates an infinite loop jumping back to the middle of the function itself or causing an instruction bus error. (3 pts)

---

### Section B Solutions

#### 1. Control Unit Truth Table & Stuck-at Fault (15 pts)

| Instruction | `RegDst` | `ALUSrc` | `MemtoReg` | `RegWrite` | `MemRead` | `MemWrite` | `Branch` | `ALUOp` |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `add` (R-Type) | 1 | 0 | 0 | 1 | 0 | 0 | 0 | `10` |
| `lw` | 0 | 1 | 1 | 1 | 1 | 0 | 0 | `00` |
| `sw` | X | 1 | X | 0 | 0 | 1 | 0 | `00` |
| `beq` | X | 0 | X | 0 | 0 | 0 | 1 | `01` |
*(8 pts: 1 pt per row/signal group)*

- **`MemtoReg` Stuck-at-0 Analysis:**
  - When `MemtoReg = 0`, the multiplexer selects the ALU output rather than memory read data to write back to the register file.
  - Instructions `add`, `sw`, and `beq` operate correctly because `add` expects the ALU output, while `sw` and `beq` do not write to the register file (`RegWrite = 0`). (3 pts)
  - `lw` fails catastrophically: instead of loading data from memory into destination register `rt`, it writes the calculated effective address (`rs + offset`) into `rt`. (4 pts)

#### 2. Critical Path and Clock Frequency (10 pts)
Execution paths:
- `add`: $t_{\text{IM}} + t_{\text{RF}} + t_{\text{ALU}} + t_{\text{Mux}} = 300 + 160 + 220 + 30 = 710\text{ ps}$
- `sw`: $t_{\text{IM}} + t_{\text{RF}} + t_{\text{ALU}} + t_{\text{DM}} = 300 + 160 + 220 + 350 = 1030\text{ ps}$
- `beq`: $t_{\text{IM}} + t_{\text{RF}} + t_{\text{ALU}} + t_{\text{Mux}} = 300 + 160 + 220 + 30 = 710\text{ ps}$
- `lw` (Critical Path):
  $$T_{\text{cycle}} = t_{\text{IM}} + t_{\text{RF}} + t_{\text{ALU}} + t_{\text{DM}} + t_{\text{Mux}} = 300 + 160 + 220 + 350 + 30 = 1060\text{ ps}$$ (6 pts)
- **Maximum Frequency:**
  $$f_{\max} = \frac{1}{T_{\text{cycle}}} = \frac{1}{1060 \times 10^{-12}\text{ s}} \approx 943.4\text{ MHz}$$ (4 pts)

---

### Section C Solutions

#### 1. Timing Diagram & Forwarding Logic (15 pts)

| Instruction | C1 | C2 | C3 | C4 | C5 | C6 | C7 |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `I1: sub $s1, $t1, $t2` | IF | ID | **EX** | **MEM** | WB | | |
| `I2: add $t3, $s1, $t4` | | IF | ID | **EX** | MEM | WB | |
| `I3: and $t5, $s1, $t6` | | | IF | ID | **EX** | MEM | WB |

- **Cycle 4 (`I2` in EX):**
  - Dependency on `$s1` produced by `I1` (currently in MEM stage).
  - Condition: `EX/MEM.RegWrite && (EX/MEM.RegisterRd != 0) && (EX/MEM.RegisterRd == ID/EX.RegisterRs)`.
  - Signal: `ForwardA = 10` (EX-to-EX bypass from `EX/MEM` latch). (5 pts)
- **Cycle 5 (`I3` in EX):**
  - Dependency on `$s1` produced by `I1` (currently in WB stage).
  - Condition: `MEM/WB.RegWrite && (MEM/WB.RegisterRd != 0) && (MEM/WB.RegisterRd == ID/EX.RegisterRs)`.
  - Signal: `ForwardA = 01` (MEM-to-EX bypass from `MEM/WB` latch). (5 pts)

#### 2. Load-Use Hazard Detection & Interlock (10 pts)
- **Why Forwarding Fails:** Memory data arrives at the end of the MEM stage (Cycle 4). An immediately succeeding instruction requires the operand at the beginning of the EX stage (Cycle 4). Forwarding cannot transfer data backward in time; a 1-cycle stall bubble must be inserted. (4 pts)
- **Detection Equation:**
  ```cpp
  if (ID/EX.MemRead && 
     ((ID/EX.RegisterRt == IF/ID.RegisterRs) || (ID/EX.RegisterRt == IF/ID.RegisterRt)))
  ```
  (3 pts)
- **Stall Actions:**
  1. Freeze the Program Counter (`PC_Write = 0`) and pipeline register (`IF/ID_Write = 0`) so current instructions re-execute in their stages.
  2. Inject zeros into the `ID/EX` control register to generate a no-op bubble passing down the pipeline. (3 pts)

---

### Section D Solutions

#### 1. Cache Bitfield Decomposition (15 pts)
- **Offset bits ($b$):** Block size $= 64\text{ bytes} \implies b = \log_2(64) = 6\text{ bits}$. (3 pts)
- **Total Lines ($N$):** $\frac{64\text{ KB}}{64\text{ bytes}} = 1024\text{ lines}$. (2 pts)
- **Sets ($S$):** $\frac{1024}{4\text{ ways}} = 256\text{ sets}$.
- **Index bits ($s$):** $s = \log_2(256) = 8\text{ bits}$. (3 pts)
- **Tag bits ($t$):** $t = 32 - 8 - 6 = 18\text{ bits}$. (3 pts)
- **Total Hardware Storage:**
  - Bits per line: $1\text{ (Valid)} + 18\text{ (Tag)} + (64 \times 8)\text{ (Data)} = 1 + 18 + 512 = 531\text{ bits}$.
  - Total cache bits: $1024 \times 531 = 543,744\text{ bits} = 67,968\text{ bytes} \approx 66.38\text{ KB}$. (4 pts)

#### 2. Multilevel AMAT Calculation (10 pts)
1. **Overall L1 Miss Rate:**
   $$\text{MR}_{1} = (0.80 \times 0.02) + (0.20 \times 0.08) = 0.016 + 0.016 = 0.032 = 3.2\%$$ (3 pts)
2. **Global L2 Miss Rate:**
   $$\text{MR}_{2,\text{global}} = \text{MR}_{1} \times \text{MR}_{2,\text{local}} = 0.032 \times 0.25 = 0.008 = 0.8\%$$ (2 pts)
3. **AMAT:**
   - L1 Miss Penalty: $t_{2} + (\text{MR}_{2,\text{local}} \times t_{\text{mem}}) = 12 + (0.25 \times 150) = 12 + 37.5 = 49.5\text{ cycles}$.
   - $\text{AMAT} = t_{1} + (\text{MR}_{1} \times \text{Penalty}_{L1}) = 1 + (0.032 \times 49.5) = 1 + 1.584 = 2.584\text{ cycles}$. (3 pts)
   - In nanoseconds ($T_{\text{cycle}} = 0.5\text{ ns}$):
     $$\text{AMAT} = 2.584 \times 0.5\text{ ns} = 1.292\text{ ns}$$ (2 pts)

