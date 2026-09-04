# Logic Design: Practice Examination 01

**Course**: Logic Design (Code: 104)  
**Duration**: 2 Hours  
**Evaluation**: Maximum 100 Points  
**Format**: Closed Book, No Electronic Devices Allowed  

---

## Part A: Multiple Choice and Theoretical Properties (25 Points)

### Question 1 (5 Points)
How many distinct Boolean functions can be formulated from $n$ binary input variables?
* A) $2^n$
* B) $2^{2^n}$
* C) $n^2$
* D) $2 \times 2^n$

### Question 2 (5 Points)
Which of the following Boolean expressions represents the dual of $x (y + z') = x y + x z'$?
* A) $x + (y \cdot z') = (x + y) \cdot (x + z')$
* B) $x + (y' \cdot z) = (x' + y') \cdot (x' + z)$
* C) $x' (y' + z) = x' y' + x' z$
* D) $(x + y)' \cdot z = (x \cdot y)' + z'$

### Question 3 (5 Points)
In a 4-variable Karnaugh map, a rectangular grouping of 8 adjacent cells containing $1$s eliminates how many literal variables from the resulting product term?
* A) 1
* B) 2
* C) 3
* D) 4

### Question 4 (5 Points)
Which of the following logic gate families is considered functionally complete (universal)?
* A) AND and OR
* B) XOR and XNOR
* C) NAND alone
* D) NOT alone

### Question 5 (5 Points)
A 3-to-8 line active-low decoder with an active-high enable input $E$ receives input $E = 1, A_2 A_1 A_0 = 101_2$. Which output line is asserted LOW ($0$)?
* A) $Y_1$
* B) $Y_3$
* C) $Y_5$
* D) None, all remain 1

---

## Part B: K-Map Minimization and Universal Gates (25 Points)

Given the Boolean function:
$$F(A, B, C, D) = \sum m(1, 3, 4, 5, 10, 11, 12, 13, 14, 15)$$
1. Plot the function on a 4-variable Karnaugh map.
2. Identify all Prime Implicants (PIs) and distinguish which ones are Essential Prime Implicants (EPIs).
3. Derive the minimal Sum of Products (SOP) expression.
4. Draw the logic circuit implementing $F$ using **only 2-input NAND gates**.

---

## Part C: MSI Decoder & Multiplexer Synthesis (25 Points)

1. Implement a Full Subtractor circuit generating Difference ($D$) and Borrow-out ($B_{\text{out}}$) for inputs $x, y, b_{\text{in}}$ using a single 3-to-8 line decoder and two external OR gates.
2. Implement the majority voting function $M(A, B, C) = \sum m(3, 5, 6, 7)$ using an **8-to-1 multiplexer**.
3. Implement the same majority voting function $M(A, B, C)$ using a **4-to-1 multiplexer** and minimal external logic.

---

## Part D: Fast Arithmetic Architecture Analysis (25 Points)

1. Explain why the propagation delay of an $n$-bit Ripple Carry Adder (RCA) scales as $O(n)$ while a Carry Lookahead Adder (CLA) operates in $O(1)$ gate delays.
2. For a 4-bit Carry Lookahead Adder, write down the explicit Boolean logic equations for Carry Generate $G_i$, Carry Propagate $P_i$, and carries $C_1, C_2, C_3, C_4$ in terms of inputs $A_i, B_i$, and $C_0$.
3. Compute the worst-case gate propagation delay (in $\Delta t$) from inputs $A, B$ to carry-out $C_4$ assuming 2-input AND, OR, and XOR gates each introduce delay $\Delta t$.

---

## Model Solutions & Marking Rubric

### Part A Solutions
1. **B**: There are $2^n$ rows in the truth table, and each row can output $0$ or $1$, resulting in $2^{2^n}$ possible functions.
2. **A**: The dual is formed by swapping $+$ with $\cdot$ and $0$ with $1$, leaving variables unchanged.
3. **C**: Merging $2^k$ cells eliminates $k$ literals. Here $2^3 = 8$ cells $\implies 3$ literals eliminated (only $4 - 3 = 1$ literal remains).
4. **C**: NAND is universal (NOT, AND, OR can all be built from NAND).
5. **C**: $101_2 = 5_{10}$. For an active-low decoder, line $Y_5$ asserts $0$.

### Part B Solution
1. **K-Map Table**:
   ```text
   CD \ 00   01   11   10
   AB
   00    0    1    1    0   <- m1, m3
   01    1    1    0    0   <- m4, m5
   11    1    1    1    1   <- m12, m13, m15, m14
   10    0    0    1    1   <- m11, m10
   ```
2. **Prime Implicants**:
   - Entire row $AB = 11$ ($m_{12}, m_{13}, m_{15}, m_{14}$): Term **$A B$** (Essential).
   - Group ($m_4, m_5, m_{12}, m_{13}$): Term **$B C'$** (Essential, covers $m_4$).
   - Group ($m_1, m_3, m_5, m_{13}$ wait: $m_5, m_{13}, m_1, m_3 \implies$ column $CD=01$ and $CD=11$ in rows $00$ and $01$ is $A' D$): Term **$A' D$** (Essential, covers $m_1, m_3$).
   - Group ($m_{10}, m_{11}, m_{14}, m_{15}$): Term **$A C$** (Essential, covers $m_{10}$).
3. **Minimal SOP Expression**:
   $$F(A, B, C, D) = A B + B C' + A' D + A C$$
4. **NAND Conversion**:
   $$F = [ (A B)' \cdot (B C')' \cdot (A' D)' \cdot (A C)' ]'$$
   Implemented as 4 first-level NAND gates feeding into a 4-input second-level NAND gate (or a tree of 2-input NAND gates).

### Part C Solution
1. **Full Subtractor via 3-to-8 Decoder**:
   - Difference $D(x, y, b_{\text{in}}) = \sum m(1, 2, 4, 7)$.
   - Borrow $B_{\text{out}}(x, y, b_{\text{in}}) = \sum m(1, 2, 3, 7)$.
   - Connect inputs $x, y, b_{\text{in}}$ to decoder address pins $A_2, A_1, A_0$. Connect active-high decoder outputs to OR gates:
     - $D = Y_1 + Y_2 + Y_4 + Y_7$
     - $B_{\text{out}} = Y_1 + Y_2 + Y_3 + Y_7$
2. **Majority via 8-to-1 MUX**:
   - Connect $A, B, C$ to select lines $S_2, S_1, S_0$.
   - Connect data inputs $I_3 = I_5 = I_6 = I_7 = 1$ (VCC), and $I_0 = I_1 = I_2 = I_4 = 0$ (GND).
3. **Majority via 4-to-1 MUX**:
   - Connect $A, B$ to $S_1, S_0$.
   - When $AB = 00$: $M = 0 \implies I_0 = 0$.
   - When $AB = 01$: $M = 1$ only if $C = 1 \implies I_1 = C$.
   - When $AB = 10$: $M = 1$ only if $C = 1 \implies I_2 = C$.
   - When $AB = 11$: $M = 1$ for both $C=0, 1 \implies I_3 = 1$.

### Part D Solution
1. **RCA vs. CLA Delay**:
   In an RCA, carry bit $C_i$ depends on $C_{i-1}$, requiring serial propagation through $n$ full adders ($t_{\text{delay}} = 2n \Delta t$). CLA computes carries directly from input operands using two-level AND-OR logic, generating all carries simultaneously in fixed time independent of word length $n$.
2. **CLA Equations**:
   $$G_i = A_i B_i, \quad P_i = A_i \oplus B_i$$
   $$C_1 = G_0 + P_0 C_0$$
   $$C_2 = G_1 + P_1 G_0 + P_1 P_0 C_0$$
   $$C_3 = G_2 + P_2 G_1 + P_2 P_1 G_0 + P_2 P_1 P_0 C_0$$
   $$C_4 = G_3 + P_3 G_2 + P_3 P_2 G_1 + P_3 P_2 P_1 G_0 + P_3 P_2 P_1 P_0 C_0$$
3. **Worst-Case Propagation Delay**:
   - $P_i, G_i$ generation: $1 \Delta t$ (XOR/AND).
   - Product terms in $C_4$ (e.g., $P_3 P_2 P_1 P_0 C_0$): $1 \Delta t$ (AND gate).
   - Summing OR gate for $C_4$: $1 \Delta t$ (OR gate).
   - Total delay to produce carry $C_4$: $1\Delta t + 1\Delta t + 1\Delta t = 3\Delta t$.

