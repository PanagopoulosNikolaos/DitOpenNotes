# Combinational Logic

This chapter covers the design and analysis of Combinational Circuits, where outputs depend exclusively on the current inputs (no memory or feedback). Basic building blocks are presented such as half adders, full adders, BCD adders, subtractors, magnitude comparators, decoders, encoders, multiplexers, demultiplexers, and three-state gates.

---

## 1. Conceptual Foundation

Combinational circuits form the basis of arithmetic and logic units (ALU) in computers. Unlike sequential circuits, they have no memory elements. When inputs change, outputs change almost immediately, with the only delay being signal propagation through logic gates (propagation delay).

---

## 2. Formal Models of Combinational Units

### 2.1 Half-Adder (HA)
Adds two bits ($x, y$) and produces the Sum ($S$) and Carry ($C$):
- $S = x \oplus y$
- $C = x \cdot y$

### 2.2 Full-Adder (FA)
Adds three bits (two inputs $x, y$ and a carry input $z$) and produces the Sum ($S$) and carry output ($C$):
- $S = x \oplus y \oplus z$
- $C = xy + xz + yz = xy + z(x \oplus y)$

### 2.3 4-bit Binary Adder/Subtractor
Implemented with four full adders in series (Ripple Carry Adder) and XOR gates for subtraction control via the control signal $M$:
- When $M = 0$: $F = X + Y$ (addition)
- When $M = 1$: $F = X - Y$ (subtraction via 2's complement)

---

## 3. Key Parameters of Logic Blocks

| Parameter | Description | Typical Value / Range | Impact |
| :--- | :--- | :--- | :--- |
| **Fan-in** | Maximum number of inputs to a gate | $2 - 8$ | Limits input complexity |
| **Fan-out** | Number of gates an output can drive | $10 - 50$ | Determines load driving capability |
| **Propagation Delay ($t_{pd}$)** | Signal propagation delay | $1 - 10$ ns | Determines maximum operating frequency |
| **Noise Margin** | Voltage noise margin | $0.4 - 1.0$ V | Determines noise tolerance |

---

## 4. Step-by-Step Mechanisms

### 4.1 Combinational Circuit Design Procedure
1. **Specification:** Determine the number of input variables and required outputs.
2. **Truth Table Construction:** Record all input combinations and corresponding output values.
3. **Simplification:** Use K-Map or Boolean algebra to find the minimum expression for each output.
4. **Logic Diagram Design:** Design the circuit with logic gates.

---

## Solved Exercises

### Exercise 1: Half Adder Design
**Problem:**
Design a half adder circuit specifying the truth table and Boolean equations.

**Solution:**
1. **Truth Table:**

| $x$ | $y$ | $C$ (Carry) | $S$ (Sum) |
| :---: | :---: | :---: | :---: |
| 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 0 |

2. **Equations:**
   - For the Sum ($S$): The output is $1$ when the inputs are different $\rightarrow S = x'y + xy' = x \oplus y$.
   - For the Carry ($C$): The output is $1$ only when both inputs are $1 \rightarrow C = xy$.

---

### Exercise 2: Full Adder Design Using Two Half Adders
**Problem:**
Show how a Full Adder can be implemented using two Half Adders (HA) and one OR gate.

**Solution:**
1. Let the inputs be $x, y, z$.
2. The first half adder (HA1) accepts inputs $x, y$ and produces:
   - $S_1 = x \oplus y$
   - $C_1 = xy$
3. The second half adder (HA2) accepts inputs $S_1$ and $z$ (the carry input) and produces:
   - $S = S_1 \oplus z = (x \oplus y) \oplus z$
   - $C_2 = S_1 \cdot z = (x \oplus y) \cdot z$
4. The final carry output $C$ is obtained from the OR of the two individual carries:
   $$
   C = C_1 + C_2 = xy + z(x \oplus y)
   $$
   This expression is logically equivalent to $xy + xz + yz$, proving the correctness of the design.

---

### Exercise 3: BCD to Excess-3 Converter Design
**Problem:**
Design the circuit that converts a 4-digit BCD number ($A, B, C, D$) to the corresponding Excess-3 code ($w, x, y, z$).

**Solution:**
1. **Truth Table (combinations 1010 through 1111 are don't cares):**

| $A$ | $B$ | $C$ | $D$ | $w$ | $x$ | $y$ | $z$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 |
| 0 | 0 | 1 | 0 | 0 | 1 | 0 | 1 |
| 0 | 0 | 1 | 1 | 0 | 1 | 1 | 0 |
| 0 | 1 | 0 | 0 | 0 | 1 | 1 | 1 |
| 0 | 1 | 0 | 1 | 1 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 | 1 | 0 | 0 | 1 |
| 0 | 1 | 1 | 1 | 1 | 0 | 1 | 0 |
| 1 | 0 | 0 | 0 | 1 | 0 | 1 | 1 |
| 1 | 0 | 0 | 1 | 1 | 1 | 0 | 0 |

2. **K-Map Simplification:**
   - $w = A + BC + BD = A + B(C + D)$
   - $x = B'C + B'D + BC'D' = B'(C + D) + B(C + D)'$
   - $y = C'D' + CD = (C + D)' + CD$
   - $z = D'$

---

### Exercise 4: Function Implementation with a Decoder
**Problem:**
Implement the function $F(x, y, z) = \sum(1, 3, 6, 7)$ using a 3-to-8 decoder and one OR gate.

**Solution:**
1. The 3-to-8 decoder has 3 selection inputs ($x, y, z$) and 8 outputs ($Y_0$ through $Y_7$), each corresponding to a minterm: $Y_i = m_i$.
2. Connect the input variables $x, y, z$ to the decoder's selection inputs.
3. Route outputs $Y_1$, $Y_3$, $Y_6$, and $Y_7$ to a 4-input OR gate.
4. The OR gate output is the function $F = Y_1 + Y_3 + Y_6 + Y_7 = m_1 + m_3 + m_6 + m_7$.

---

### Exercise 5: 2-bit Magnitude Comparator Design
**Problem:**
Find the Boolean equations for a 2-bit magnitude comparator circuit that compares numbers $A = A_1A_0$ and $B = B_1B_0$.

**Solution:**
1. Define auxiliary equality variables for each bit:
   $$
   x_1 = A_1 B_1 + A_1' B_1' = (A_1 \oplus B_1)'
   $$
   $$
   x_0 = A_0 B_0 + A_0' B_0' = (A_0 \oplus B_0)'
   $$
2. **Equality Condition ($A = B$):**
   $$
   (A = B) = x_1 \cdot x_0
   $$
3. **Greater Than Condition ($A > B$):**
   $$
   (A > B) = A_1 B_1' + x_1 A_0 B_0'
   $$
4. **Less Than Condition ($A < B$):**
   $$
   (A < B) = A_1' B_1 + x_1 A_0' B_0
   $$

---

### Exercise 6: Function Implementation with a 4-to-1 Multiplexer
**Problem:**
Implement the function $F(x, y, z) = \sum(1, 2, 6, 7)$ using a 4-to-1 multiplexer (MUX).

**Solution:**
1. Select the two variables $x, y$ as the MUX selection signals ($S_1 = x, S_0 = y$). Variable $z$ will be used as data input.
2. Construct the mapping table:

| $x$ | $y$ | $z$ | $F$ | $F$ Relation to $z$ | MUX Input |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | 0 | 0 | 0 | $F = z$ | $I_0 = z$ |
| 0 | 0 | 1 | 1 | | |
| 0 | 1 | 0 | 1 | $F = z'$ | $I_1 = z'$ |
| 0 | 1 | 1 | 0 | | |
| 1 | 0 | 0 | 0 | $F = 0$ | $I_2 = 0$ |
| 1 | 0 | 1 | 0 | | |
| 1 | 1 | 0 | 1 | $F = 1$ | $I_3 = 1$ |
| 1 | 1 | 1 | 1 | | |

3. Connect the 4-to-1 MUX inputs as follows: $I_0 = z$, $I_1 = z'$, $I_2 = 0$, $I_3 = 1$.

---

### Exercise 7: 4-to-2 Priority Encoder Design
**Problem:**
Find the output equations $Y_1, Y_0$ and the validity variable $V$ for a 4-input priority encoder ($I_3, I_2, I_1, I_0$), where $I_3$ has the highest priority.

**Solution:**
1. **Truth Table:**

| $I_3$ | $I_2$ | $I_1$ | $I_0$ | $Y_1$ | $Y_0$ | $V$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | 0 | 0 | 0 | X | X | 0 |
| 0 | 0 | 0 | 1 | 0 | 0 | 1 |
| 0 | 0 | 1 | X | 0 | 1 | 1 |
| 0 | 1 | X | X | 1 | 0 | 1 |
| 1 | X | X | X | 1 | 1 | 1 |

2. **Output Equations:**
   - $Y_1 = I_3 + I_2$
   - $Y_0 = I_3 + I_2' I_1$
   - $V = I_3 + I_2 + I_1 + I_0$

---

### Exercise 8: MUX Implementation with Three-State Buffers
**Problem:**
Design a 2-to-1 multiplexer using two three-state buffers and one inverter.

**Solution:**
1. Let the data inputs be $A$ and $B$, the selection signal $S$, and the output $Y$.
2. Connect the outputs of both three-state buffers to the same common output point $Y$.
3. The first buffer accepts input $A$ and is controlled by signal $S$.
4. The second buffer accepts input $B$ and is controlled by signal $S'$ (through the inverter).
5. Operation:
   - If $S = 1$: The first buffer is enabled and $Y = A$. The second is in high-impedance state (Hi-Z).
   - If $S = 0$: The first is in Hi-Z. The second is enabled and $Y = B$.
   This implements exactly the 2-to-1 MUX functionality.

---

## 6. Connections and Cross-References

- The design of adders and encoders is based on K-Map simplification (Chapter 03).
- Decoders and multiplexers are extensively used in memory unit design (ROM/RAM) and data routing in processors.

---

## Exam Tip: Don't Cares in Design
In exams, when designing BCD circuits (e.g., BCD-to-Excess 3 or BCD-to-7-segment), do not forget to include the don't care conditions for combinations $1010$ through $1111$. This allows the creation of much larger groups on the K-Map and leads to significantly simpler circuits.
