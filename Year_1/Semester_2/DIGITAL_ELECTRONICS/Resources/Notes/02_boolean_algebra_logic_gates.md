# 2. Boolean Algebra and Logic Gates

Boolean Algebra constitutes the mathematical foundation for the design and analysis of digital circuits. It establishes a set of rules and properties that allow the description, simplification, and implementation of logical functions. Logic gates constitute the physical implementation of Boolean operators.

---

## 1. Basic Principles of Boolean Algebra

### 1.1 Boolean Axioms

Boolean Algebra is defined on a set $B = \{0, 1\}$ with two binary operations ($+$ for OR, $\cdot$ for AND) and one unary operation ($'$ for NOT):

| Axiom | OR ($+$) | AND ($\cdot$) |
|:-------|:--------:|:-------------:|
| Closure | $a + b \in B$ | $a \cdot b \in B$ |
| Identity | $a + 0 = a$ | $a \cdot 1 = a$ |
| Complement | $a + a' = 1$ | $a \cdot a' = 0$ |
| Commutative | $a + b = b + a$ | $a \cdot b = b \cdot a$ |
| Associative | $(a + b) + c = a + (b + c)$ | $(a \cdot b) \cdot c = a \cdot (b \cdot c)$ |
| Distributive | $a + (b \cdot c) = (a + b) \cdot (a + c)$ | $a \cdot (b + c) = a \cdot b + a \cdot c$ |

### 1.2 Properties and Theorems

**Basic Theorems:**
- $a + a = a$, $a \cdot a = a$ (idempotency)
- $a + 1 = 1$, $a \cdot 0 = 0$ (domination)
- $a + a \cdot b = a$, $a \cdot (a + b) = a$ (absorption)
- $a + a' \cdot b = a + b$ (simplification)

**De Morgan's Theorems:**
$$
\overline{A \cdot B} = \bar{A} + \bar{B}
$$
$$
\overline{A + B} = \bar{A} \cdot \bar{B}
$$

> **[Key Insight]** De Morgan's theorems are critical for conversion between SOP and POS forms and for implementing circuits exclusively with NAND or NOR gates.

**Duality Principle:** Every Boolean theorem remains valid if:
- $0 \leftrightarrow 1$
- $+ \leftrightarrow \cdot$

## 2. Logic Gates

### 2.1 Basic Gates

**AND ($Y = A \cdot B$):** Output is 1 only when all inputs are 1.
| $A$ | $B$ | $Y$ |
|:---:|:---:|:---:|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

**OR ($Y = A + B$):** Output is 1 when at least one input is 1.
| $A$ | $B$ | $Y$ |
|:---:|:---:|:---:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

**NOT ($Y = \bar{A}$):** Inversion of the input.
| $A$ | $Y$ |
|:---:|:---:|
| 0 | 1 |
| 1 | 0 |

### 2.2 Universal Gates (NAND, NOR)

**NAND ($Y = \overline{A \cdot B}$):** Equivalent to AND + NOT. It is a universal gate: any logical function can be implemented with only NAND.

| $A$ | $B$ | $Y$ |
|:---:|:---:|:---:|
| 0 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

**NOR ($Y = \overline{A + B}$):** Equivalent to OR + NOT. It is also a universal gate.

| $A$ | $B$ | $Y$ |
|:---:|:---:|:---:|
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 0 |

> **[Exam Tip]** Implementing any function with only NAND is done as follows: write the expression in SOP, replace each AND+OR with NAND. For NOR, use POS.

### 2.3 XOR and XNOR

**XOR ($Y = A \oplus B = \bar{A}B + A\bar{B}$):** Output is 1 when inputs are different.

| $A$ | $B$ | $Y$ |
|:---:|:---:|:---:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

**XNOR ($Y = \overline{A \oplus B} = A \odot B$):** Output is 1 when inputs are equal.

| $A$ | $B$ | $Y$ |
|:---:|:---:|:---:|
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

## 3. Truth Tables

### 3.1 Construction for n Variables

For $n$ variables, the truth table has $2^n$ rows. Inputs are arranged in ascending binary order.

**Example of 3 variables ($A, B, C$):**

| $A$ | $B$ | $C$ | $F$ |
|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 1 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 0 | 1 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 0 |
| 1 | 1 | 1 | 1 |

### 3.2 Minterm and Maxterm

**Minterm ($m_i$):** A product term that includes all variables of the function, either in normal or inverted form. For $n$ variables, there are $2^n$ minterms.

**Notation:** $m_i$, where $i$ is the decimal number corresponding to the binary value of the variables (0 for inverted, 1 for normal).

**Example for 3 variables ($A, B, C$):**
- $m_0 = \bar{A}\bar{B}\bar{C}$ (000)
- $m_1 = \bar{A}\bar{B}C$ (001)
- $m_3 = \bar{A}BC$ (011)
- $m_7 = ABC$ (111)

**Maxterm ($M_i$):** A sum term that includes all variables, either in normal or inverted form. For $n$ variables, there are $2^n$ maxterms.

**Notation:** $M_i$

**Example for 3 variables ($A, B, C$):**
- $M_0 = A + B + C$ (000)
- $M_1 = A + B + \bar{C}$ (001)
- $M_5 = \bar{A} + B + \bar{C}$ (101)
- $M_7 = \bar{A} + \bar{B} + \bar{C}$ (111)

### 3.3 Don't Care Conditions (X)

Don't care conditions ($X$) indicate that the output value is indifferent for specific input combinations. They are used in simplification to achieve smaller expressions.

---

## 4. Implementation Technologies

### 4.1 TTL (Transistor-Transistor Logic)

- Uses bipolar transistors
- Standard supply voltage: $5V$
- Speed: propagation delay $\approx 10ns$
- High fan-out (10-20)

### 4.2 CMOS (Complementary Metal-Oxide-Semiconductor)

- Uses MOSFET (NMOS + PMOS)
- Minimal power consumption in static state
- Standard voltage: $1.8V$ - $5V$
- High noise margin

### 4.3 Gate Characteristics

| Parameter | Description |
|:---|---:|
| Fan-in | Number of inputs to a gate |
| Fan-out | Maximum number of gates that can be driven |
| Propagation delay | Time from input change to output change |
| Noise margin | Resistance to unwanted voltage variations |

---

## Solved Exercises

### Exercise 1: Applying De Morgan

**Problem:** Simplify the expression $F = \overline{(A + B) \cdot (\bar{A} + C)}$.

**Solution:**

Apply De Morgan:
$$
F = \overline{A + B} + \overline{\bar{A} + C}
$$

Apply De Morgan again:
$$
F = \bar{A} \cdot \bar{B} + A \cdot \bar{C}
$$

### Exercise 2: Proving the Absorption Property

**Problem:** Prove $A + A \cdot B = A$.

**Solution:**
$$
A + A \cdot B = A \cdot (1 + B) = A \cdot 1 = A
$$

### Exercise 3: Single NAND Implementation

**Problem:** Implement the OR gate using only NAND.

**Solution:**
The OR can be implemented as NAND with inverted inputs:
$$
A + B = \overline{\bar{A} \cdot \bar{B}}
$$

Using NAND:
1. $X_1 = \text{NAND}(A, A) = \bar{A}$
2. $X_2 = \text{NAND}(B, B) = \bar{B}$
3. $Y = \text{NAND}(X_1, X_2) = \overline{\bar{A} \cdot \bar{B}} = A + B$

### Exercise 4: Simplification with De Morgan

**Problem:** Simplify $F = \overline{(\bar{A} + B) \cdot (A + \bar{B})}$.

**Solution:**

Apply De Morgan:
$$
F = \overline{\bar{A} + B} + \overline{A + \bar{B}} = A \cdot \bar{B} + \bar{A} \cdot B = A \oplus B
$$

### Exercise 5: Constructing a Truth Table

**Problem:** Construct the truth table for $F = \bar{A}B + A\bar{B}$.

**Solution:**

| $A$ | $B$ | $\bar{A}$ | $\bar{B}$ | $\bar{A}B$ | $A\bar{B}$ | $F$ |
|:---:|:---:|:---------:|:---------:|:----------:|:----------:|:---:|
| 0 | 0 | 1 | 1 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 0 | 0 | 0 | 0 |

This is XOR.

### Exercise 6: Expression Simplification

**Problem:** Simplify $F = A\bar{B} + \bar{A}B + \bar{A}\bar{B}$.

**Solution:**
$$
F = A\bar{B} + \bar{A}(B + \bar{B}) = A\bar{B} + \bar{A}(1) = A\bar{B} + \bar{A}
$$
$$
F = \bar{A} + A\bar{B} = \bar{A} + \bar{B}
$$

### Exercise 7: Single NAND Implementation

**Problem:** Implement $F = A \cdot B + C \cdot D$ using only NAND.

**Solution:**
$$
F = \overline{\overline{A \cdot B} \cdot \overline{C \cdot D}}
$$
Two NANDs for the products and one NAND for the sum.

### Exercise 8: Finding Expression from Truth Table

**Problem:** Given a truth table with $F = 1$ for $(A,B,C) = (0,0,1), (0,1,0), (1,0,1), (1,1,1)$. Find the SOP.

**Solution:**

The minterms are:
- $m_1 = \bar{A}\bar{B}C$
- $m_2 = \bar{A}B\bar{C}$
- $m_5 = A\bar{B}C$
- $m_7 = ABC$

$$
F = \bar{A}\bar{B}C + \bar{A}B\bar{C} + A\bar{B}C + ABC
$$

Simplification:
$$
F = C(\bar{A}\bar{B} + A\bar{B} + AB) + \bar{A}B\bar{C} = C(\bar{B} + AB) + \bar{A}B\bar{C}
$$
$$
F = C(\bar{B} + A) + \bar{A}B\bar{C}
$$

---

## Exam Tip: Recognizing Equivalent Gates

NAND and NOR gates are universal. In exam problems, if you are asked to implement a function with only NAND or only NOR:
1. For NAND: bring the expression to SOP, then apply double inversion.
2. For NOR: bring the expression to POS, then apply double inversion.

Also, remember that $\bar{A} = \text{NAND}(A, A)$ and $\bar{A} = \text{NOR}(A, A)$.
