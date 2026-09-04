# Exercises: Boolean Algebra, Logic Optimization, and Combinational Logic

## Context and Grounding
This practice set provides worked problems with step-by-step solutions covering Boolean postulates, algebraic proof, K-map reduction, and decoder/multiplexer circuit synthesis. It reinforces topics from `Lectures/lecture_01_boolean_algebra_and_logic_gates.md` and `lecture_02_combinational_circuit_design.md`.

---

## Problems

### Problem 1: Algebraic Reduction
Using Boolean algebraic theorems and Huntington's postulates, simplify the following expression to a minimal sum of products:
$$F = A'B(D' + C'D) + B(A + A'CD)$$

### Problem 2: Universal NAND Gate Synthesis
Implement the exclusive-OR operation $Y = A \oplus B = A'B + AB'$ using:
1. Exactly five 2-input NAND gates.
2. Exactly four 2-input NAND gates. Draw the algebraic derivation for the 4-gate design.

### Problem 3: 4-to-1 Multiplexer Implementation
Implement the majority function $M(A, B, C) = \sum m(3, 5, 6, 7)$ using a single 4-to-1 multiplexer where $A$ and $B$ are connected to the select lines ($S_1 = A, S_0 = B$).

---

## Detailed Step-by-Step Solutions

### Solution 1
Expand and distribute terms:
$$F = A'BD' + A'BC'D + AB + A'BCD$$
Group terms containing $A'BD$:
$$A'BC'D + A'BCD = A'BD(C' + C) = A'BD(1) = A'BD$$
Substitute back:
$$F = A'BD' + A'BD + AB$$
Group the first two terms:
$$A'BD' + A'BD = A'B(D' + D) = A'B(1) = A'B$$
Combine remaining terms:
$$F = A'B + AB = (A' + A)B = (1)B = B$$
**Result:** $F = B$.

### Solution 2
Recall $A \oplus B = A'B + AB'$.
Observe:
$$(AB)' = A' + B'$$
Consider the intermediate term $T = (AB)'$:
$$Y = ((A \cdot T)' \cdot (B \cdot T)')'$$
Substitute $T = (AB)'$:
* $A \cdot T = A(A' + B') = AB'$
* $(A \cdot T)' = (AB')'$
* $B \cdot T = B(A' + B') = A'B$
* $(B \cdot T)' = (A'B)'$
Combine outer NAND:
$$Y = ((AB')' \cdot (A'B)')' = (AB')'' + (A'B)'' = AB' + A'B = A \oplus B$$
This achieves $A \oplus B$ using exactly four 2-input NAND gates:
1. $G_1 = (AB)'$
2. $G_2 = (A \cdot G_1)'$
3. $G_3 = (B \cdot G_1)'$
4. $G_4 = (G_2 \cdot G_3)' = A \oplus B$.

### Solution 3
A 4-to-1 MUX has truth table equation:
$$Y = S_1' S_0' D_0 + S_1' S_0 D_1 + S_1 S_0' D_2 + S_1 S_0 D_3$$
With $S_1 = A, S_0 = B$:
* For $AB = 00$ ($m_0, m_1$): $M(0, 0, C) = 0 \implies D_0 = 0$
* For $AB = 01$ ($m_2, m_3$): $M(0, 1, 0) = 0, M(0, 1, 1) = 1 \implies D_1 = C$
* For $AB = 10$ ($m_4, m_5$): $M(1, 0, 0) = 0, M(1, 0, 1) = 1 \implies D_2 = C$
* For $AB = 11$ ($m_6, m_7$): $M(1, 1, 0) = 1, M(1, 1, 1) = 1 \implies D_3 = 1$

**Configuration:** Connect $D_0 = 0$, $D_1 = C$, $D_2 = C$, $D_3 = 1$.

