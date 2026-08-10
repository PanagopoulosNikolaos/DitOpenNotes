# 5. Combinational Circuits

Combinational circuits constitute the foundation of digital systems. Their output depends exclusively on the current values of the inputs, without any memory of the past. They are the subject of design after Boolean simplification and before sequential circuits.

---

## 1. Design Principles

### 1.1 Properties of Combinational Circuits

The output $Y(t) = f(A(t), B(t), \dots)$ — depends only on current inputs.

**Design methodology:**
1. Specification (what we want the circuit to do)
2. Truth table or Boolean expression
3. Minimization (K-Map, QMC)
4. Implementation (AND-OR, NAND-NAND, etc.)

### 1.2 Static Hazards

**Static-1 Hazard:** The output should remain at 1, but momentarily becomes 0 during an input transition.

**Static-0 Hazard:** The output should remain at 0, but momentarily becomes 1.

**Dynamic Hazard:** The output changes three times (e.g., $0 \to 1 \to 0 \to 1$) instead of once.

> **[Key Insight]** Hazards arise from the different propagation delay times of different paths. Adding redundant terms to the expression removes static hazards.

---

## 2. Code Converters

### 2.1 BCD → 7-Segment Display

The BCD-to-7-segment converter takes a 4-bit BCD input and outputs 7 signals for each digit position (a-g) of an LED display.

| Segment | Position |
|:---|:---|
| a | top |
| b | top-right |
| c | bottom-right |
| d | bottom |
| e | bottom-left |
| f | top-left |
| g | middle |

For each digit $0$-$9$: which segments light up:
- $0$: a,b,c,d,e,f
- $1$: b,c
- $2$: a,b,d,e,g
- $3$: a,b,c,d,g
- $4$: b,c,f,g
- $5$: a,c,d,f,g
- $6$: a,c,d,e,f,g
- $7$: a,b,c
- $8$: a,b,c,d,e,f,g
- $9$: a,b,c,d,f,g

### 2.2 Binary ↔ Gray Code

*Prerequisite: Chapter 1 — Gray Code.*

$$
G_i = B_i \oplus B_{i+1},\quad B_i = B_{i+1} \oplus G_i
$$

Implementation: N XOR gates for N-bit.

### 2.3 BCD ↔ Excess-3

**BCD → Excess-3:** Add 3 to each BCD digit.

| BCD | Excess-3 |
|:---:|:--------:|
| 0000 | 0011 |
| 0001 | 0100 |
| 0010 | 0101 |
| 0011 | 0110 |
| 0100 | 0111 |
| 0101 | 1000 |
| 0110 | 1001 |
| 0111 | 1010 |
| 1000 | 1011 |
| 1001 | 1100 |

**Excess-3 → BCD:** Subtract 3 (or add 13 in 4-bit).

---

## 3. Magnitude Comparators

### 3.1 1-Bit Comparator

| $A$ | $B$ | $A>B$ | $A=B$ | $A<B$ |
|:---:|:---:|:-----:|:-----:|:-----:|
| 0 | 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 0 | 1 |
| 1 | 0 | 1 | 0 | 0 |
| 1 | 1 | 0 | 1 | 0 |

**Boolean expressions:**
$$
A > B: A\bar{B},\quad A = B: A \odot B,\quad A < B: \bar{A}B
$$

### 3.2 n-Bit Comparator

The n-bit comparator extends in cascade: starting from the MSB, each bit determines the relationship if the previous bits were equal.

**Algorithm:**
1. Compare MSB: if $A_{n-1} \neq B_{n-1}$, then the result is determined
2. If $A_{n-1} = B_{n-1}$, continue to the next bit
3. Repeat until LSB or until a different bit is found

---

## Solved Exercises

### Exercise 1: BCD-to-7-Segment Circuit

**Problem:** Find the Boolean expression for segment $a$ of the 7-segment display.

**Solution:**

Segment $a$ lights up for: $0, 2, 3, 5, 6, 7, 8, 9$.

$$
F_a(A,B,C,D) = \sum m(0, 2, 3, 5, 6, 7, 8, 9) + \sum d(10, 11, 12, 13, 14, 15)
$$

K-Map simplification:
$$
F_a = A + \bar{B}\bar{D} + \bar{B}C + B\bar{C}D + B C\bar{D}
$$

### Exercise 2: 2-Bit Comparator

**Problem:** Design a 2-bit comparator that outputs $A>B$.

**Solution:**

| $A_1$ | $A_0$ | $B_1$ | $B_0$ | $A>B$ |
|:---:|:---:|:---:|:---:|:-----:|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 0 | 1 |
| 1 | 0 | 0 | 0 | 1 |
| 1 | 1 | 0 | 1 | 1 |
| ... | ... | ... | ... | ... |

**Algorithm:**
$$
A > B = A_1\bar{B_1} + (A_1 \odot B_1)(A_0\bar{B_0})
$$

### Exercise 3: Binary → Gray 4-Bit

**Problem:** Design a Binary → Gray 4-bit converter.

**Solution:**
- $G_3 = B_3$
- $G_2 = B_3 \oplus B_2$
- $G_1 = B_2 \oplus B_1$
- $G_0 = B_1 \oplus B_0$

Four XOR gates.

### Exercise 4: BCD → Excess-3

**Problem:** Design a BCD → Excess-3 converter using K-Map.

**Solution:**

| BCD ($A B C D$) | Ex-3 ($W X Y Z$) |
|:---:|:---:|
| 0000 | 0011 |
| 0001 | 0100 |
| 0010 | 0101 |
| 0011 | 0110 |
| 0100 | 0111 |
| 0101 | 1000 |
| 0110 | 1001 |
| 0111 | 1010 |
| 1000 | 1011 |
| 1001 | 1100 |

$W = A + BC + BD$
$X = \bar{B}C + \bar{B}D + B\bar{C}\bar{D}$
$Y = C\bar{D} + \bar{C}D = C \oplus D$
$Z = \bar{D}$

### Exercise 5: 3-to-8 Decoder as Application

**Problem:** Implement $F(A,B,C) = \sum m(1,2,4,7)$ using a 3-to-8 decoder.

**Solution:**

The decoder produces $2^3=8$ outputs, one for each minterm. We need an OR gate:
$$
F = Y_1 + Y_2 + Y_4 + Y_7
$$

### Exercise 6: Hazard Detection

**Problem:** Check if there is a static-1 hazard in $F = \bar{A}B + A\bar{B}$.

**Solution:**

In the transition $A=0,B=1 \to A=1,B=1$: the term $\bar{A}B$ is disabled while $A\bar{B}$ is already 0. There is a possibility of a momentary 0.

**Solution:** Add a redundant term $B$: $F = \bar{A}B + A\bar{B} + B \cdot (B) = \bar{A}B + A\bar{B}$... in reality, we need the original term: $F = \bar{A}B + A\bar{B}$, defines more groups.

### Exercise 7: 4-Bit Comparator with Cascading

**Problem:** Connect two 4-bit comparators for 8-bit comparison.

**Solution:**

1. Connect the MSB 4-bit comparator ($A[7:4]$ vs $B[7:4]$)
2. The "equal" output of the first comparator enables the second ($A[3:0]$ vs $B[3:0]$)
3. The final outputs come primarily from the first, if there is equality from the second

### Exercise 8: Excess-3 → BCD

**Problem:** Design an Excess-3 → BCD converter using K-Map.

**Solution:**

| Ex-3 ($W X Y Z$) | BCD ($A B C D$) |
|:---:|:---:|
| 0011 | 0000 |
| 0100 | 0001 |
| 0101 | 0010 |
| 0110 | 0011 |
| 0111 | 0100 |
| 1000 | 0101 |
| 1001 | 0110 |
| 1010 | 0111 |
| 1011 | 1000 |
| 1100 | 1001 |

Inverse operation: $A = W + X\bar{Y}\bar{Z} + \bar{W}\bar{X}Y$, etc.

---

## Exam Tip: Attention to Don't Care Outputs

In code converters (BCD-to-7-segment, Excess-3), BCD values 1010-1111 are valid inputs that never occur. They are treated as don't care ($X$) in the K-Map. This allows simpler expressions than if you were forced to define a specific output value for invalid inputs.
