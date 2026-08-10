# Gate-Level Minimization

This chapter focuses on methods for simplifying Boolean functions with the goal of minimizing the number of gates and inputs in digital circuits. It covers the Karnaugh Map method (K-Map) for 2, 3, 4, and 5 variables, finding prime and essential prime implicants, don't care conditions, implementation with NAND and NOR gates, XOR/XNOR functions, parity generation/checking, and modeling in VHDL and Verilog.

---

## 1. Core Definitions

### 1.1 Karnaugh Map (K-Map)
The K-Map is a graphical representation of the truth table of a Boolean function, consisting of squares where each square corresponds to a minterm. The arrangement of squares follows Gray code, so adjacent squares differ by only one variable (in normal or complemented form).

### 1.2 Prime and Essential Implicants
- **Prime Implicant (PI):** A product term obtained by combining the maximum possible number of adjacent squares (powers of 2: 1, 2, 4, 8, 16) on the K-Map. It cannot be simplified further.
- **Essential Prime Implicant:** A prime implicant that contains at least one minterm not covered by any other prime implicant. Essential PIs must be included in the minimum expression of the function.

### 1.3 Universal Gates
The **NAND** and **NOR** gates are characterized as universal because they can implement any Boolean function without using other gates.

---

## 2. Foundational Formulas & Properties

### 2.1 Properties of Exclusive-OR (XOR $\oplus$ and XNOR $\odot$)
- $x \oplus 0 = x$
- $x \oplus 1 = x'$
- $x \oplus x = 0$
- $x \oplus x' = 1$
- $x \oplus y' = (x \oplus y)'$
- $x' \oplus y = (x \oplus y)'$
- Commutative: $A \oplus B = B \oplus A$
- Associative: $(A \oplus B) \oplus C = A \oplus (B \oplus C) = A \oplus B \oplus C$

### 2.2 Odd and Even Functions
- **Odd Function (XOR):** The output is $1$ when an odd number of inputs equal $1$.
- **Even Function (XNOR):** The output is $1$ when an even number of inputs equal $1$.

### 2.3 Parity Generation and Checking
- **Parity Bit (P) for even parity:**
  $$
  P = x \oplus y \oplus z
  $$
- **Parity Checker (C):**
  $$
  C = x \oplus y \oplus z \oplus P
  $$
  If $C = 1$, an error is detected (odd number of errors). If $C = 0$, no error exists (or an even number of errors exists).

---

## Solved Exercises

### Exercise 1: 3-Variable K-Map Simplification
**Problem:**
Simplify the function $F(x, y, z) = \sum(0, 2, 4, 5, 6)$ using a K-Map.

**Solution:**
1. Draw the 3-variable K-Map ($2 \times 4$ squares) with variables $x$ (rows) and $y, z$ (columns with Gray code: $00, 01, 11, 10$):
   - Place $1$ in squares $0, 2, 4, 5, 6$.
2. **Grouping:**
   - Squares $0, 2, 4, 6$ form a quad at the four corners of the map. Variables $x$ and $y$ change, while $z$ remains constant at $0$. The resulting term is $z'$.
   - Squares $4, 5$ form a pair in the bottom row. $x$ remains $1$, $y$ remains $0$, while $z$ changes. The resulting term is $xy'$.
3. **Final result:**
   $$
   F = z' + xy'
   $$

---

### Exercise 2: 4-Variable K-Map Simplification
**Problem:**
Simplify the function $F(w, x, y, z) = \sum(0, 1, 2, 4, 5, 6, 8, 9, 12, 13, 14)$ using a K-Map.

**Solution:**
1. Draw the 4-variable K-Map ($4 \times 4$ squares).
2. **Grouping:**
   - An octet is formed by rows $00, 01, 11, 10$ and columns $00, 01$ (squares $0, 1, 4, 5, 12, 13, 8, 9$). The resulting term is $y'$.
   - A quad is formed by squares $0, 2, 8, 10$ (four corners). The term is $x'z'$.
   - Another quad is formed by squares $4, 6, 12, 14$ in columns $00, 10$ of rows $01, 11$. The term is $xz'$.
3. **Final result:**
   $$
   F = y' + w'z' + xz' \quad (\text{or alternatively} \; F = y' + x'z' + xz')
   $$

---

### Exercise 3: Product-of-Sums (POS) Simplification
**Problem:**
Simplify the function $F(A, B, C, D) = \sum(0, 1, 2, 5, 8, 9, 10)$ in product-of-sums (POS) form using a K-Map.

**Solution:**
1. Place $1$ in the function's squares, and $0$ in the remaining squares.
2. Group the $0$s to find the complement $F'$:
   - The $0$s are in squares $3, 4, 6, 7, 11, 12, 13, 14, 15$.
   - A quad is formed by squares $12, 13, 14, 15$ (bottom-middle/right). The term is $AB$.
   - Another quad is formed by squares $3, 7, 11, 15$. The term is $CD$.
   - A quad is formed by squares $4, 6, 12, 14$. The term is $BD'$.
3. The simplified complement expression is:
   $$
   F' = AB + CD + BD'
   $$
4. Apply DeMorgan's theorem to find $F$:
   $$
   F = (F')' = (A' + B')(C' + D')(B' + D)
   $$

---

### Exercise 4: Using Don't Care Conditions
**Problem:**
Simplify the function $F(w, x, y, z) = \sum(1, 3, 7, 11, 15)$ with don't care conditions $d(w, x, y, z) = \sum(0, 2, 5)$.

**Solution:**
1. Place $1$ in squares $1, 3, 7, 11, 15$ and $X$ in squares $0, 2, 5$ of the K-Map.
2. **Grouping:**
   - A quad is formed by squares $3, 7, 11, 15$ (column $11$). The term is $yz$.
   - Another quad is formed using the $X$s in squares $0, 2$ and the $1$s in $1, 3$ (top row). The term is $w'x'$.
3. **Final result:**
   $$
   F = yz + w'x'
   $$

---

### Exercise 5: Two-Level Implementation with NAND Gates
**Problem:**
Implement the function $F = xy' + x'y + z$ using only NAND gates.

**Solution:**
1. The function is already in sum-of-products (SOP) form.
2. Apply double complement to the function:
   $$
   F = (F'') = [(xy' + x'y + z)']'
   $$
3. Apply DeMorgan to the inner complement:
   $$
   F = [(xy')' \cdot (x'y)' \cdot z']'
   $$
4. This requires:
   - Two first-level NAND gates for the products $xy'$ and $x'y$ (with complemented inputs where needed).
   - An inverter (NAND gate with shorted inputs) for $z'$.
   - A second-level NAND gate that accepts the outputs of the previous gates.

---

### Exercise 6: Implementation with NOR Gates
**Problem:**
Implement the function $F = (A + B)(C + D)E$ using only NOR gates.

**Solution:**
1. The function is in product-of-sums (POS) form.
2. Apply double complement:
   $$
   F = [( (A+B)(C+D)E )']'
   $$
3. Apply DeMorgan to the inner complement:
   $$
   F = [(A+B)' + (C+D)' + E']''
   $$
4. This requires:
   - Two first-level NOR gates for $(A+B)'$ and $(C+D)'$.
   - An inverter (NOR gate) for $E'$.
   - A second-level NOR gate for the sum of the above.
   - A final NOR gate (inverter) for the outer complement.

---

### Exercise 7: Parity Generator Circuit Design
**Problem:**
Design an even parity generator circuit for a 3-bit message $x, y, z$.

**Solution:**
1. The truth table specifies that the parity bit $P$ must make the total number of ones even:
   - If $x,y,z = 001$, $P = 1$.
   - If $x,y,z = 011$, $P = 0$.
2. The logic function for $P$ is:
   $$
   P = x'y'z + x'yz' + xy'z' + xyz
   $$
3. This function simplifies using XOR gates:
   $$
   P = x \oplus y \oplus z
   $$

---

### Exercise 8: VHDL Code for Boolean Equations
**Problem:**
Write VHDL code describing the circuit for the function $E = C \cdot (A + B)$.

**Solution:**
```vhdl
entity or_and_vhdl is
    port(E: out bit; A, B, C: in bit);
end or_and_vhdl;

architecture Boolean_Equations of or_and_vhdl is
    signal D: bit;
begin
    D <= A or B;
    E <= C and D;
end Boolean_Equations;
```

---

## Exam Tip: prime implicants vs essential prime implicants
In exams, you are often asked to identify prime implicants (PIs) and essential prime implicants (Essential PIs).
- **Prime Implicant (PI):** Each group of $1$s on the map that cannot be included in a larger group.
- **Essential Prime Implicant:** A group containing at least one $1$ that is not covered by any other group.
First find the "isolated" $1$s that have only one grouping option. These define the Essential Prime Implicants!
