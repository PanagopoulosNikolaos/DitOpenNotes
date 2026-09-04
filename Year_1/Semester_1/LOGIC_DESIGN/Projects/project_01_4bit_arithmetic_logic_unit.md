# Term Project: 4-Bit Arithmetic Logic Unit (ALU) Design

## Project Overview
Design, model, and simulate a comprehensive 4-bit Arithmetic Logic Unit (ALU) using Logisim-evolution. The ALU serves as the computational heart of a simple microprocessor, performing 8 distinct arithmetic and logical operations on two 4-bit 2's complement operands and generating four processor status flags ($Z, C, V, N$).

---

## 1. ALU Operational Specifications

The unit accepts two 4-bit inputs $A = [A_3, A_2, A_1, A_0]$ and $B = [B_3, B_2, B_1, B_0]$, a 3-bit function select code $S = [S_2, S_1, S_0]$, and an input carry $C_{\text{in}}$. It outputs a 4-bit result $F = [F_3, F_2, F_1, F_0]$ and four status flags.

### 1.1 Operation Select Function Table
| $S_2$ | $S_1$ | $S_0$ | Operation Mode | Algebraic Expression | Functional Description |
|:---:|:---:|:---:|:---|:---|:---|
| 0 | 0 | 0 | Arithmetic | $F = A$ | Transfer $A$ through |
| 0 | 0 | 1 | Arithmetic | $F = A + 1$ | Increment $A$ |
| 0 | 1 | 0 | Arithmetic | $F = A + B$ | 2's complement addition |
| 0 | 1 | 1 | Arithmetic | $F = A - B$ | 2's complement subtraction ($A + B' + 1$) |
| 1 | 0 | 0 | Logic | $F = A \text{ AND } B$ | Bitwise conjunction |
| 1 | 0 | 1 | Logic | $F = A \text{ OR } B$ | Bitwise disjunction |
| 1 | 1 | 0 | Logic | $F = A \oplus B$ | Bitwise exclusive-OR |
| 1 | 1 | 1 | Logic | $F = A'$ | Bitwise complement of $A$ |

---

## 2. Processor Status Flags

The ALU must compute four standard condition flags upon every operation:
1. **Zero Flag ($Z$)**: Asserted ($Z = 1$) when all result bits are zero:
   $$Z = (F_3 + F_2 + F_1 + F_0)' = \text{NOR}(F_3, F_2, F_1, F_0)$$
2. **Negative Flag ($N$)**: Reflects the sign bit of the 4-bit 2's complement output:
   $$N = F_3$$
3. **Carry Flag ($C$)**: Active during arithmetic modes when an addition produces a carry-out ($C_{\text{out}} = 1$) or subtraction produces no borrow.
4. **Overflow Flag ($V$)**: Indicates signed 2's complement arithmetic overflow:
   $$V = C_3 \oplus C_4$$
   where $C_3$ is the carry into the MSB and $C_4$ is the carry out of the MSB.

---

## 3. Subcircuit Architecture and Hierarchy

Organize the design modularly in Logisim:
* **`FullAdder`**: 1-bit full adder subcircuit.
* **`AdderSubtractor4Bit`**: 4-bit ripple-carry or carry-lookahead adder/subtractor utilizing XOR gates on input $B$ controlled by subtraction signal $M$.
* **`LogicUnit4Bit`**: Parallel array of gates computing AND, OR, XOR, and NOT across all 4 bits.
* **`Mux8to1_4Bit`**: 4-bit wide 8-to-1 multiplexer selecting between arithmetic and logic outputs based on $S_2 S_1 S_0$.
* **`FlagsUnit`**: Combinational logic generating $Z, N, C, V$.
* **`Main`**: Top-level schematic connecting input switches, display hex digits, and probe indicators.

---

## 4. Verification and Test Vectors

Validate the ALU against boundary test vectors:
1. **Addition with Overflow**: $A = 0111_2 (+7)$, $B = 0001_2 (+1) \implies F = 1000_2 (-8)$, with $V = 1, N = 1, Z = 0$.
2. **Subtraction to Zero**: $A = 0101_2 (+5)$, $B = 0101_2 (+5) \implies F = 0000_2 (0)$, with $Z = 1, C = 1, V = 0$.
3. **Negative Subtraction**: $A = 0011_2 (+3)$, $B = 0100_2 (+4) \implies F = 1111_2 (-1)$, with $N = 1, Z = 0$.
4. **Logic Bitwise Ops**: $A = 1010_2$, $B = 1100_2 \implies \text{AND} = 1000_2, \text{OR} = 1110_2, \text{XOR} = 0110_2$.

---

## 5. Deliverables & Evaluation Rubric

| Criterion | Target Metric | Points |
|:---|:---|:---:|
| Hierarchical Modular Architecture | Clean decomposition into reusable subcircuits with minimal wiring clutter | 25 |
| Arithmetic Core Correctness | Flawless 4-bit addition, subtraction, increment, and decrement | 25 |
| Logic Core & Multiplexing | Accurate bitwise AND, OR, XOR, NOT operations and 8-to-1 bus routing | 20 |
| Status Flag Generation | Precise hardware implementation of Zero, Negative, Carry, and Overflow flags | 20 |
| Documentation & Testing | Complete test vector logs and schematic diagrams in the project report | 10 |
| **Total** | | **100** |

