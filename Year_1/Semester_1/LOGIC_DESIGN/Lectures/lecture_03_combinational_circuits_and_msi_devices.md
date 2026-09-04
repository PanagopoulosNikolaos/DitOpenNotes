# Lecture 03: Combinational Circuits and Medium-Scale Integration (MSI) Devices

## Context and Grounding
This lecture addresses the synthesis of combinational logic networks and Medium-Scale Integration (MSI) building blocks. It covers binary arithmetic architectures (adders, subtractors, carry-lookahead networks), decoders, priority encoders, multiplexers, and magnitude comparators.

---

## 1. Binary Arithmetic Building Blocks

### 1.1 Half Adder (HA)
Adds two 1-bit operands $A$ and $B$:
* Sum: $S = A \oplus B$
* Carry: $C = A \cdot B$

### 1.2 Full Adder (FA)
Adds two 1-bit operands $A, B$ and input carry $C_{\text{in}}$:
* Sum: $S = A \oplus B \oplus C_{\text{in}}$
* Carry: $C_{\text{out}} = A B + (A \oplus B) C_{\text{in}} = A B + B C_{\text{in}} + A C_{\text{in}}$

### 1.3 Carry Lookahead Adder (CLA)
Ripple carry adders experience linear propagation delay $O(n)$ as carries ripple through $n$ bit stages. The Carry Lookahead Adder eliminates ripple delay by computing carries in parallel using **Generate** ($G_i$) and **Propagate** ($P_i$) functions:
* Carry Generate: $G_i = A_i \cdot B_i$ (produces a carry regardless of $C_i$)
* Carry Propagate: $P_i = A_i \oplus B_i$ (propagates $C_i$ to $C_{i+1}$)

Carry equations:
$$\begin{aligned}
C_1 &= G_0 + P_0 C_0 \\
C_2 &= G_1 + P_1 C_1 = G_1 + P_1 G_0 + P_1 P_0 C_0 \\
C_3 &= G_2 + P_2 C_2 = G_2 + P_2 G_1 + P_2 P_1 G_0 + P_2 P_1 P_0 C_0 \\
C_4 &= G_3 + P_3 C_3 = G_3 + P_3 G_2 + P_3 P_2 G_1 + P_3 P_2 P_1 G_0 + P_3 P_2 P_1 P_0 C_0
\end{aligned}$$
All carries are generated within **two gate delays**, achieving $O(1)$ constant delay for fixed-width adders.

---

## 2. Decoders and Encoders

### 2.1 Decoders
An $n$-to-$2^n$ line decoder activates exactly one of $2^n$ output lines corresponding to the $n$-bit binary input code.
* A decoder with an active-high enable input ($E$) outputs minterms:
  $$Y_i = E \cdot m_i$$
* **Universal Logic Synthesis**: Any Boolean function $F(A, B, C) = \sum m(1, 3, 5, 7)$ can be implemented using a 3-to-8 decoder connected to an OR gate summing the active minterm outputs.

### 2.2 Priority Encoders
An encoder performs the inverse operation of a decoder, converting $2^n$ lines to an $n$-bit binary output. A **priority encoder** resolves ambiguous simultaneous inputs by prioritizing the highest-index active input and asserting a valid flag $V$.

---

## 3. Multiplexers (Data Selectors)

A $2^n$-to-1 multiplexer selects one of $2^n$ data inputs ($I_0, \ldots, I_{2^n-1}$) and routes it to output $Y$ according to an $n$-bit selection address $(S_{n-1}, \ldots, S_0)$.

### 3.1 4-to-1 Multiplexer
Equation:
$$Y = S_1' S_0' I_0 + S_1' S_0 I_1 + S_1 S_0' I_2 + S_1 S_0 I_3$$

```text
       ┌──────────────┐
  I0 ──┤              │
  I1 ──┤   4-to-1     │
  I2 ──┤     MUX      ├──► Y
  I3 ──┤              │
       └───┬──────┬───┘
           │      │
          S1     S0
```

### 3.2 Function Implementation with Multiplexers
Any arbitrary $n$-variable Boolean function can be implemented using a $2^{n-1}$-to-1 multiplexer:
1. Connect $n-1$ variables to the multiplexer select lines ($S_{n-2}, \ldots, S_0$).
2. Express the remaining variable in the truth table for each minterm pair as $0, 1, X$, or $X'$, and connect to data inputs $I_k$.

