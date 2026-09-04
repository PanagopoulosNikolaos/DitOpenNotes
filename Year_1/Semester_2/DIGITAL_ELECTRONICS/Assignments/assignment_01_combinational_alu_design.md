# Assignment 01: 4-Bit Arithmetic Logic Unit (ALU) Design

## Objective
Design, model, and simulate a 4-bit Arithmetic Logic Unit (ALU) using hierarchical combinational logic building blocks. This assignment assesses knowledge of full adders, multiplexers, two's complement arithmetic, and VHDL hardware modeling.

---

## Technical Specifications

### 1. Operations Table
The ALU accepts two 4-bit operands $A(3..0)$ and $B(3..0)$, a 3-bit operation select code $S(2..0)$, and a carry-in bit $C_{in}$.

| $S_2 S_1 S_0$ | Function | Description | Algebraic Implementation |
|---|---|---|---|
| `000` | ADD | Addition | $A + B + C_{in}$ |
| `001` | SUB | Subtraction | $A + B' + 1$ (Two's complement) |
| `010` | INC | Increment $A$ | $A + 1$ |
| `011` | DEC | Decrement $A$ | $A - 1$ |
| `100` | AND | Bitwise AND | $A \text{ and } B$ |
| `101` | OR  | Bitwise OR  | $A \text{ or } B$ |
| `110` | XOR | Bitwise XOR | $A \oplus B$ |
| `111` | NOT | Bitwise Invert | $\text{not } A$ |

### 2. Status Output Flags
In addition to the 4-bit result $Y(3..0)$, the ALU must compute four condition flags:
* **Zero Flag ($Z$)**: Asserted (1) when all bits of $Y$ are zero.
* **Carry Flag ($C$)**: Carry-out from arithmetic operations; 0 for logic operations.
* **Sign Flag ($N$)**: Most Significant Bit ($Y_3$) indicating negative two's complement value.
* **Overflow Flag ($V$)**: Asserted when signed two's complement overflow occurs during addition or subtraction:
  $$V = C_3 \oplus C_4$$

### 3. Deliverables
1. Gate-level schematic or block diagram showing the data path.
2. Synthesizable VHDL entity and architecture in `alu_4bit.vhd`.
3. Comprehensive testbench `alu_4bit_tb.vhd` exhaustively testing all 8 functions with boundary edge cases (zero, maximum positive `0111`, maximum negative `1000`).
4. Simulation report with annotated waveform captures validating operation flags.

---

## Grading Rubric
| Criteria | Description | Points |
|---|---|---|
| Arithmetic Data Path Design | Correct full-adder cascade and two's complement inversion | 30 |
| Logic Function Implementation | Multiplexer-based logic operations and selection routing | 20 |
| Flag Generation Logic | Correct $Z, C, N, V$ flag equations and behavior | 25 |
| VHDL Code Quality & Testbench | Synthesizable coding, comprehensive test cases, zero timing violations | 25 |
| **Total** | | **100** |

