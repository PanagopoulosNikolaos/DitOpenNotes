# 3. Canonical Forms - SOP / POS

The canonical forms Sum of Products (SOP) and Product of Sums (POS) constitute standardized representations of logical functions. Every Boolean function can be expressed uniquely either as a sum of minterms or as a product of maxterms. The choice between SOP and POS depends on the complexity of the implementation and the available gate type.

---

## 1. Canonical SOP (Sum of Minterms)

### 1.1 Definition of Minterm

A minterm is a product term that includes all variables of the function, either in normal or inverted form. For $n$ variables, there are $2^n$ minterms.

**Notation:** $m_i$, where $i$ is the decimal number corresponding to the binary value of the variables (0 for inverted, 1 for normal).

**Example for 3 variables ($A, B, C$):**
- $m_0 = \bar{A}\bar{B}\bar{C}$ (000)
- $m_1 = \bar{A}\bar{B}C$ (001)
- $m_3 = \bar{A}BC$ (011)
- $m_7 = ABC$ (111)

### 1.2 Construction from Truth Table

The canonical SOP is obtained by summing the minterms for the rows where the output $F = 1$:

$$
F = \sum m(i, j, k, \dots)
$$

**Example:**

| $A$ | $B$ | $C$ | $F$ |
|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 1 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 0 |
| 1 | 1 | 1 | 1 |

$$
F = \sum m(1, 3, 4, 7) = \bar{A}\bar{B}C + \bar{A}BC + A\bar{B}\bar{C} + ABC
$$

---

## 2. Canonical POS (Product of Maxterms)

### 2.1 Definition of Maxterm

A maxterm is a sum term that includes all variables, either in normal or inverted form. For $n$ variables, there are $2^n$ maxterms.

**Notation:** $M_i$

**Example for 3 variables ($A, B, C$):**
- $M_0 = A + B + C$ (000)
- $M_1 = A + B + \bar{C}$ (001)
- $M_5 = \bar{A} + B + \bar{C}$ (101)
- $M_7 = \bar{A} + \bar{B} + \bar{C}$ (111)

### 2.2 Construction from Truth Table

The canonical POS is obtained by multiplying the maxterms for the rows where the output $F = 0$:

$$
F = \prod M(i, j, k, \dots)
$$

For the same truth table:
$$
F = \prod M(0, 2, 5, 6) = (A+B+C)(A+\bar{B}+C)(\bar{A}+B+\bar{C})(\bar{A}+\bar{B}+C)
$$

---

## 3. Relationship Between SOP and POS

### 3.1 Complementarity of Indices

The indices of minterms (SOP) and maxterms (POS) are complementary:
- If $F = \sum m(i_1, i_2, \dots, i_k)$, then $\bar{F} = \sum m(\text{remaining indices})$
- $F = \prod M(\text{remaining indices})$

**Example:** For $F = \sum m(1, 3, 4, 7)$:
- $\bar{F} = \sum m(0, 2, 5, 6)$
- $F = \prod M(0, 2, 5, 6)$

### 3.2 Conversion SOP ↔ POS

**SOP → POS:**
1. Find the complement of the SOP
2. Apply De Morgan
3. The result is the POS of the complement

**POS → SOP:**
1. Find the complement of the POS
2. Apply De Morgan
3. The result is the SOP of the complement

### 3.3 Standard vs Canonical Form

**Canonical form:** Each term includes all variables.
**Standard form:** Terms may include a subset of variables (simplified expression).

**Example:**
- Canonical SOP: $F = \bar{A}BC + A\bar{B}C + ABC$
- Standard SOP (after simplification): $F = BC + AC$

> **[Key Insight]** The canonical form is unique for each function. The standard form is not unique — there are many equivalent simplified expressions.

---

## Solved Exercises

### Exercise 1: Finding SOP from Truth Table

**Problem:** Given a truth table with $F = 1$ for $(A,B,C,D) = (0,0,0,1), (0,1,0,0), (1,0,1,1), (1,1,0,0)$. Write the canonical SOP.

**Solution:**

The corresponding minterms are:
- $(0001)_2 = 1$: $m_1 = \bar{A}\bar{B}\bar{C}D$
- $(0100)_2 = 4$: $m_4 = \bar{A}B\bar{C}\bar{D}$
- $(1011)_2 = 11$: $m_{11} = A\bar{B}CD$
- $(1100)_2 = 12$: $m_{12} = AB\bar{C}\bar{D}$

$$
F = \sum m(1, 4, 11, 12) = \bar{A}\bar{B}\bar{C}D + \bar{A}B\bar{C}\bar{D} + A\bar{B}CD + AB\bar{C}\bar{D}
$$

### Exercise 2: Finding POS from Truth Table

**Problem:** For the same table, write the canonical POS.

**Solution:**

The maxterms for $F = 0$ are the remaining ones: $0, 2, 3, 5, 6, 7, 8, 9, 10, 13, 14, 15$.

$$
F = \prod M(0, 2, 3, 5, 6, 7, 8, 9, 10, 13, 14, 15)
$$

### Exercise 3: Converting SOP to POS

**Problem:** Convert $F = \bar{A}B + A\bar{B}$ from SOP to POS.

**Solution:**
1. The function is already simplified (XOR).
2. The canonical SOP: $F = \bar{A}B + A\bar{B} = \sum m(1, 2)$
3. The canonical POS: $F = \prod M(0, 3) = (A+B)(\bar{A}+\bar{B})$

Verification:
$$
(A+B)(\bar{A}+\bar{B}) = A\bar{A} + A\bar{B} + B\bar{A} + B\bar{B} = 0 + A\bar{B} + \bar{A}B + 0 = A\bar{B} + \bar{A}B
$$

### Exercise 4: From SOP to Truth Table

**Problem:** Construct the truth table for $F(A,B,C) = \sum m(1, 2, 5, 6)$.

**Solution:**

| $A$ | $B$ | $C$ | $F$ |
|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 1 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 0 |

### Exercise 5: Simplification and Canonical Form

**Problem:** Given $F = \bar{A}\bar{B}C + \bar{A}B\bar{C} + A\bar{B}C + AB\bar{C}$. Express in canonical SOP and then simplify.

**Solution:**

The canonical SOP is already given:
$$
F = \sum m(1, 2, 5, 6)
$$

Grouping:
$$
F = \bar{A}(\bar{B}C + B\bar{C}) + A(\bar{B}C + B\bar{C}) = (\bar{A} + A)(\bar{B}C + B\bar{C}) = 1 \cdot (\bar{B}C + B\bar{C})
$$
$$
F = \bar{B}C + B\bar{C} = B \oplus C
$$

### Exercise 6: From POS to SOP

**Problem:** Convert $F = (A + \bar{B})(\bar{A} + B)$ to SOP.

**Solution:**
$$
F = (A + \bar{B})(\bar{A} + B) = A\bar{A} + AB + \bar{B}\bar{A} + \bar{B}B = 0 + AB + \bar{A}\bar{B} + 0
$$
$$
F = AB + \bar{A}\bar{B} = A \odot B
$$

### Exercise 7: Canonical SOP with Don't Care

**Problem:** Given $F(A,B,C,D)$ with $F = 1$ for $(0,3,5,7,10)$ and don't care for $(1,9,15)$. Write the canonical SOP using don't care.

**Solution:**

The canonical SOP can include or not include the don't cares. Using them, a simpler expression may result:

$$F = \sum m(0, 3, 5, 7, 10) + \sum d(1, 9, 15)$$

### Exercise 8: Complementary Function

**Problem:** If $F = \sum m(0, 2, 4, 6)$, find $\bar{F}$ in SOP and POS.

**Solution:**

$$
\bar{F} = \sum m(1, 3, 5, 7)
$$
$$
\bar{F} = \prod M(0, 2, 4, 6) = \bar{F}_{\text{POS}}
$$

Verification: $F + \bar{F} = \sum m(0,1,2,3,4,5,6,7) = 1$ (tautology).

---

## Exam Tip: Choosing SOP vs POS

In exam problems:
- If the function has few rows with $F=1$, prefer SOP (fewer terms).
- If it has few rows with $F=0$, prefer POS.
- For implementation with only NAND: use SOP and replace the gates.
- For implementation with only NOR: use POS and replace the gates.

Remember: $m_i = \overline{M_i}$ (the minterm is the complement of the corresponding maxterm with the same index).
