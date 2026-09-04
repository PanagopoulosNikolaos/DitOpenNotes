# Practice Exercises: Boolean Algebra and Combinational Logic

This drill document provides comprehensive solved exercises covering number base conversions, 2's complement arithmetic, Boolean algebra simplification, K-map minimization, and multiplexer synthesis.

---

## Section 1: Number Systems and Complements

### Problem 1: Radix Conversions and 2's Complement Subtraction
**Problem:**
1. Convert $(218.625)_{10}$ to binary and hexadecimal.
2. Using 8-bit 2's complement arithmetic, compute $X = (+42) - (+65)$. Indicate if overflow occurs.

**Step-by-Step Solution:**
1. **Conversion of $(218)_{10}$**:
   - $218 / 2 = 109$ remainder $0$
   - $109 / 2 = 54$ remainder $1$
   - $54 / 2 = 27$ remainder $0$
   - $27 / 2 = 13$ remainder $1$
   - $13 / 2 = 6$ remainder $1$
   - $6 / 2 = 3$ remainder $0$
   - $3 / 2 = 1$ remainder $1$
   - $1 / 2 = 0$ remainder $1$
   - Integer binary: $11011010_2$.
   - **Fraction $(0.625)_{10}$**:
     - $0.625 \times 2 = 1.25$ (integer 1)
     - $0.25 \times 2 = 0.50$ (integer 0)
     - $0.50 \times 2 = 1.00$ (integer 1)
     - Fraction binary: $.101_2$.
   - Result in binary: $(11011010.101)_2$.
   - Hexadecimal grouping: $(1101 \quad 1010 . 1010)_2 = (\text{DA.A})_{16}$.

2. **8-Bit 2's Complement Subtraction $(42 - 65)$**:
   - $+42 = 00101010_2$.
   - $+65 = 01000001_2$.
   - Negate $+65$ to find $-65$:
     - 1's complement: $10111110_2$.
     - Add 1: $10111111_2$.
   - Perform binary addition $42 + (-65)$:
     ```text
       00101010  (+42)
     + 10111111  (-65)
     ──────────
       11101001
     ```
   - Result: $11101001_2$.
   - Magnitude verification: Invert and add 1 $\implies 00010110 + 1 = 00010111_2 = -(16 + 4 + 2 + 1) = -23$. Correct since $42 - 65 = -23$.
   - Overflow check: Adding a positive and a negative number cannot cause overflow. $V = 0$.

---

## Section 2: Boolean Algebra Simplification

### Problem 2: Algebraic Reduction
**Problem:** Simplify the Boolean function using algebraic theorems:
$$F = A B + A' C + B C$$

**Step-by-Step Solution:**
1. Observe that $B C$ is the **consensus term** between $A B$ and $A' C$:
   $$B C = B C \cdot 1 = B C (A + A') = A B C + A' B C$$
2. Substitute into original expression:
   $$F = A B + A' C + A B C + A' B C$$
3. Group terms:
   $$F = (A B + A B C) + (A' C + A' B C) = A B (1 + C) + A' C (1 + B)$$
4. Since $1 + X = 1$:
   $$F = A B (1) + A' C (1) = A B + A' C$$
This demonstrates the **Consensus Theorem**: $A B + A' C + B C = A B + A' C$.

---

## Section 3: Karnaugh Map Minimization

### Problem 3: 4-Variable K-Map with Don't-Cares
**Problem:** Minimize the function in Sum of Products (SOP) form:
$$F(A, B, C, D) = \sum m(0, 2, 5, 7, 8, 10, 15) + \sum d(13)$$

**Step-by-Step Solution:**
1. Place $1$s and don't-care $X$ into 4-variable K-map:
   ```text
   CD \ 00   01   11   10
   AB
   00    1    0    0    1   <- m0, m2
   01    0    1    1    0   <- m5, m7
   11    0    X    1    0   <- d13, m15
   10    1    0    0    1   <- m8, m10
   ```
2. Identify Prime Implicants:
   - **Four Corners**: $m_0, m_2, m_8, m_{10}$ form a 4-cell group.
     - $A$ changes ($0 \to 1$), $B = 0 \implies B'$.
     - $C$ changes ($0 \to 1$), $D = 0 \implies D'$.
     - Term: **$B' D'$**.
   - **Quad in Columns 01 and 11**: $m_5, m_7, d_{13}, m_{15}$ form a 4-cell group utilizing don't-care $d_{13}$.
     - $A$ changes ($0 \to 1$), $B = 1 \implies B$.
     - $C$ changes ($0 \to 1$), $D = 1 \implies D$.
     - Term: **$B D$**.
3. All minterms are covered by these two essential prime implicants.
4. Minimal SOP Expression:
   $$F(A, B, C, D) = B' D' + B D = (B \oplus D)' = B \odot D$$

---

## Section 4: Multiplexer Synthesis

### Problem 4: Function Implementation via 4-to-1 Multiplexer
**Problem:** Implement the function $F(A, B, C) = \sum m(1, 3, 4, 6)$ using a single 4-to-1 multiplexer. Let $A$ and $B$ be connected to select inputs $S_1$ and $S_0$ respectively.

**Step-by-Step Solution:**
1. Construct truth table mapping inputs $A, B$ to select lines $S_1, S_0$:

| $A (S_1)$ | $B (S_0)$ | $C$ | Minterm | $F$ | Data Input $I_k$ Expression |
|:---:|:---:|:---:|:---:|:---:|:---|
| 0 | 0 | 0 | $m_0$ | 0 | When $AB=00$: $F=0$ for $C=0$, $F=1$ for $C=1 \implies I_0 = C$ |
| 0 | 0 | 1 | $m_1$ | 1 | |
| 0 | 1 | 0 | $m_2$ | 0 | When $AB=01$: $F=0$ for $C=0$, $F=1$ for $C=1 \implies I_1 = C$ |
| 0 | 1 | 1 | $m_3$ | 1 | |
| 1 | 0 | 0 | $m_4$ | 1 | When $AB=10$: $F=1$ for $C=0$, $F=0$ for $C=1 \implies I_2 = C'$ |
| 1 | 0 | 1 | $m_5$ | 0 | |
| 1 | 1 | 0 | $m_6$ | 1 | When $AB=11$: $F=1$ for $C=0$, $F=0$ for $C=1 \implies I_3 = C'$ |
| 1 | 1 | 1 | $m_7$ | 0 | |

2. Multiplexer input assignments:
   - $I_0 = C$
   - $I_1 = C$
   - $I_2 = C'$
   - $I_3 = C'$
   - $S_1 = A, \quad S_0 = B$
3. Verification:
   $$F = S_1' S_0' (C) + S_1' S_0 (C) + S_1 S_0' (C') + S_1 S_0 (C')$$
   $$= A' B' C + A' B C + A B' C' + A B C' = m_1 + m_3 + m_4 + m_6$$
   The function is successfully realized with one 4-to-1 MUX and a single inverter for $C'$.

