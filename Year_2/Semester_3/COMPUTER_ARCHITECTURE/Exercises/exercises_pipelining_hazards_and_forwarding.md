# Exercises: Pipelining Hazards, Forwarding, and Branch Penalties

Quantitative drills, cycle-by-cycle pipeline execution timing diagrams, forwarding control multiplexer calculations, and code rescheduling optimizations for **Computer Architecture (Course Code: 301)**.

---

## Problem 1: RAW Hazard Detection and Execution Without Forwarding

Consider the following MIPS instruction sequence executing on a classic 5-stage RISC pipeline (IF, ID, EX, MEM, WB):

```mips
I1: add $s0, $t0, $t1
I2: sub $t2, $s0, $t3
I3: and $t4, $s0, $t5
I4: or  $t6, $s0, $t7
```

### Questions:
1. Identify all Read-After-Write (RAW) data dependencies involving register `$s0`.
2. Assume the hardware **lacks a forwarding unit**, but the Register File supports internal forwarding (a register write in the first half of a clock cycle is readable in the second half of the same cycle).
   - Construct the cycle-by-cycle pipeline timing chart showing all required stall bubbles.
   - Determine the total number of clock cycles required to complete the sequence and calculate the resulting Cycles Per Instruction (CPI).

---

## Solution to Problem 1

### 1. RAW Dependency Identification:
`I1` computes a new value for `$s0` during its EX stage (Cycle 3) and commits it to the register file in its WB stage (Cycle 5).
- **`I1` $\to$ `I2`:** `I2` reads `$s0` in its ID stage. If issued immediately at Cycle 2, `I2` attempts to read `$s0` during Cycle 2 before `I1` has written it $\implies$ **RAW Hazard**.
- **`I1` $\to$ `I3`:** `I3` reads `$s0` in ID. If issued at Cycle 3, `I3` attempts to read `$s0` during Cycle 3 $\implies$ **RAW Hazard**.
- **`I1` $\to$ `I4`:** `I4` reads `$s0` in ID during Cycle 5. Since register writes occur during the first half of Cycle 5 and reads during the second half, `I4` reads the correct updated value without stalling.

### 2. Cycle-by-Cycle Pipeline Timing Chart (No Forwarding):

To resolve dependencies without forwarding, two stall bubbles (`stall`) must be inserted before `I2` can perform its ID stage:

| Instruction | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | C9 |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `I1: add $s0, $t0, $t1` | IF | ID | EX | MEM | **WB** | | | | |
| *stall bubble 1* | | IF | ID | — | — | | | | |
| *stall bubble 2* | | | IF | — | — | — | | | |
| `I2: sub $t2, $s0, $t3` | | | | IF | **ID** | EX | MEM | WB | |
| `I3: and $t4, $s0, $t5` | | | | | IF | ID | EX | MEM | WB |
| `I4: or  $t6, $s0, $t7` | | | | | | IF | ID | EX | MEM |

- **Total Execution Time:** 9 clock cycles to complete 4 instructions (and 10 cycles for full write-back of `I4`).
- **CPI:** $\frac{10\text{ cycles}}{4\text{ instructions}} = 2.50\text{ cycles/instruction}$.

---

## Problem 2: Pipeline Execution with Full Hardware Forwarding

Using the identical instruction sequence from Problem 1:
```mips
I1: add $s0, $t0, $t1
I2: sub $t2, $s0, $t3
I3: and $t4, $s0, $t5
I4: or  $t6, $s0, $t7
```

### Questions:
1. Construct the pipeline timing chart assuming a **Full Forwarding Unit** (EX-to-EX and MEM-to-EX bypass paths).
2. For each clock cycle, state the values of the forwarding control signals `ForwardA` and `ForwardB` at the ALU inputs of executing instructions, where:
   - `00`: Input from Register File.
   - `10`: Forwarded from `EX/MEM` pipeline register.
   - `01`: Forwarded from `MEM/WB` pipeline register.

---

## Solution to Problem 2

### 1. Timing Chart with Full Forwarding:

With forwarding, instructions execute without inserting any stall bubbles:

| Instruction | C1 | C2 | C3 | C4 | C5 | C6 | C7 |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `I1: add $s0, $t0, $t1` | IF | ID | **EX** | **MEM** | WB | | |
| `I2: sub $t2, $s0, $t3` | | IF | ID | **EX** | MEM | WB | |
| `I3: and $t4, $s0, $t5` | | | IF | ID | **EX** | MEM | WB |
| `I4: or  $t6, $s0, $t7` | | | | IF | ID | EX | MEM |

### 2. Forwarding Unit Multiplexer Signal Trace:

- **Cycle 4 (`I2` in EX stage):**
  - `I2` needs `$s0` for ALU input A.
  - `I1` is in MEM stage (`EX/MEM.RegisterRd = $s0`, `EX/MEM.RegWrite = 1`).
  - Condition matches EX hazard: `ForwardA = 10` (EX-to-EX bypass).
  - Input B (`$t3`) is from register file: `ForwardB = 00`.
- **Cycle 5 (`I3` in EX stage):**
  - `I3` needs `$s0` for ALU input A.
  - `I1` is in WB stage (`MEM/WB.RegisterRd = $s0`, `MEM/WB.RegWrite = 1`).
  - `I2` (in MEM) writes `$t2 \ne $s0`.
  - Condition matches MEM hazard: `ForwardA = 01` (MEM-to-EX bypass).
  - Input B (`$t5`): `ForwardB = 00`.
- **Cycle 6 (`I4` in EX stage):**
  - `I4` reads `$s0` during ID in Cycle 5; by Cycle 6, `$s0` has been written back to the Register File.
  - `ForwardA = 00`, `ForwardB = 00`.
- **Total Cycles:** 7 cycles for 4 instructions (steady-state CPI = 1.0).

---

## Problem 3: Load-Use Hazard Detection and Instruction Rescheduling

Consider the following program fragment reading two words from memory:

```mips
I1: lw  $s1, 0($t0)
I2: add $t2, $s1, $t3
I3: lw  $s2, 4($t0)
I4: sub $t4, $s2, $t5
```

### Questions:
1. Explain why hardware forwarding cannot eliminate stalls in this sequence.
2. Draw the execution chart indicating the exact clock cycles and the stall bubble injected by the Hazard Detection Unit.
3. Reschedule (reorder) the instructions without altering program semantics to eliminate all stall cycles.

---

## Solution to Problem 3

### 1. The Load-Use Interlock Limitation:
Data read from memory in `I1` (`lw`) is only available at the **end of Cycle 4 (MEM stage)**. However, `I2` (`add`) requires `$s1` at the **beginning of Cycle 4 (EX stage)**. Because data cannot travel backward in time, forwarding alone cannot prevent a hazard. The Hazard Detection Unit must insert **1 stall cycle**.

### 2. Unoptimized Pipeline Timing Chart:

```
Cycle:       1    2    3    4    5    6    7    8    9
I1 (lw):    IF   ID   EX   MEM  WB
I2 (add):        IF   ID  [stall] EX   MEM  WB
I3 (lw):              IF  [stall] ID   EX   MEM  WB
I4 (sub):                     [stall] IF   ID  [stall] EX   MEM  WB
```
Two total stall bubbles are injected (one after each load).
Total cycles to complete: 9 cycles.

### 3. Optimized Code Rescheduling:
Separate each load instruction from its dependent consumer by interleaving the second independent load:

```mips
I1: lw  $s1, 0($t0)    # Load $s1
I3: lw  $s2, 4($t0)    # Load $s2 (Independent! Fills load-use slot for I1)
I2: add $t2, $s1, $t3  # Consumes $s1 (Data forwarded from MEM/WB without stalling)
I4: sub $t4, $s2, $t5  # Consumes $s2 (Data forwarded from MEM/WB without stalling)
```

#### Rescheduled Timing Chart:
| Instruction | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `I1: lw  $s1, 0($t0)` | IF | ID | EX | **MEM** | WB | | | |
| `I3: lw  $s2, 4($t0)` | | IF | ID | EX | **MEM** | WB | | |
| `I2: add $t2, $s1, $t3`| | | IF | ID | **EX** | MEM | WB | |
| `I4: sub $t4, $s2, $t5`| | | | IF | ID | **EX** | MEM | WB |

- In Cycle 5, `I1` is in WB and forwards `$s1` to `I2` in EX (`ForwardA = 01`).
- In Cycle 6, `I3` is in WB and forwards `$s2` to `I4` in EX (`ForwardA = 01`).
- **Result:** 0 stall bubbles, reducing total execution from 9 to 8 cycles.

