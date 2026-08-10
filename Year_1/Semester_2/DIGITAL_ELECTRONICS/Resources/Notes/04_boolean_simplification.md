# 4. Boolean Algebra Simplification

Boolean expression simplification is the fundamental process for minimizing the number of gates in circuit implementation. The Karnaugh Map (K-Map) provides a graphical simplification method for up to 5 variables, while the Quine-McCluskey method is suitable for more variables.

---

## 1. Karnaugh Map (K-Map)

### 1.1 Arrangement of 2, 3, 4 Variables

The K-Map is a table of cells, where each cell corresponds to a minterm. Rows and columns are arranged in Gray code order so that consecutive cells differ by only one bit.

**2 variables ($A, B$):**

| $A \setminus B$ | 0 | 1 |
|:---|:---:|:---:|
| 0 | $m_0$ | $m_1$ |
| 1 | $m_2$ | $m_3$ |

**3 variables ($A, B, C$):**

| $AB \setminus C$ | 0 | 1 |
|:---|:---:|:---:|
| 00 | $m_0$ | $m_1$ |
| 01 | $m_3$ | $m_2$ |
| 11 | $m_7$ | $m_6$ |
| 10 | $m_4$ | $m_5$ |

**4 variables ($A, B, C, D$):**

| $AB \setminus CD$ | 00 | 01 | 11 | 10 |
|:---|:---:|:---:|:---:|:---:|
| 00 | $m_0$ | $m_1$ | $m_3$ | $m_2$ |
| 01 | $m_4$ | $m_5$ | $m_7$ | $m_6$ |
| 11 | $m_{12}$ | $m_{13}$ | $m_{15}$ | $m_{14}$ |
| 10 | $m_8$ | $m_9$ | $m_{11}$ | $m_{10}$ |

### 1.2 Grouping

1s are grouped in powers of 2: $1, 2, 4, 8, 16, \dots$

**Grouping rules:**
- Each group must contain $2^k$ cells
- Cells in a group must differ by only 1 bit (Gray code)
- Larger groups → simpler term
- Each 1 must be covered by at least one group
- Groups can wrap around

### 1.3 Prime Implicants

**Prime Implicant (PI):** A group of 1s that cannot be contained in a larger group. Every simplified function consists of prime implicants.

**Essential Prime Implicant (EPI):** A Prime Implicant that covers a 1 not covered by any other PI. EPIs must always be included.

### 1.4 Simplification Procedure

1. Place the 1s in the K-Map
2. Find all PIs (largest possible groups)
3. Select all EPIs
4. If there are uncovered 1s, select additional PIs (minimax or Petrick)
5. Write the simplified term

### 1.5 Handling Don't Care

Don't cares ($X$) can be treated as 0 or 1 as favorable for simplification. They are used when they allow the creation of larger groups.

> **[Key Insight]** Don't cares are not mandatory in grouping — they are only used if they help reduce the result.

### 1.6 5-Variable K-Map

Uses two 4-maps (one for $E=0$ and one for $E=1$). Groups can extend between the two maps.

---

## 2. Quine-McCluskey Method (QMC)

### 2.1 Algorithmic Simplification

The QMC method is algorithmic and suitable for more than 4 variables.

**Steps:**
1. Record the minterms corresponding to 1, with the number of 1s in each minterm
2. Combine minterms that differ in only 1 bit — replace the common bit with '-'
3. Repeat step 2 on the new data
4. Groups that could not be combined are PIs

**Example for $F = \sum m(1, 2, 3, 5, 6, 7, 8, 9, 10, 14)$:**

| Step | Group | Minterm | Binary |
|:---|:---:|:---|:---|
| 1 | 1 | $m_1$ | 0001 |
| 1 | 1 | $m_2$ | 0010 |
| 1 | 2 | $m_3, m_5, m_6$ | 0011, 0101, 0110 |
| 1 | 3 | $m_7$ | 0111 |
| 2 | 1-2 | $(1,3), (1,5), (2,3), (2,6), (2,10)$ | 00-1, 0-01, 001-, 0-1-, -010 |

### 2.2 Covering Table

A table is created where rows are minterms and columns are PIs. Each column indicates which minterms it covers.

### 2.3 Finding the Minimum Cover

1. Select all EPIs (columns with a single 1)
2. Remove covered minterms
3. Select the smallest number of remaining PIs

---

## 3. 2-Level Implementation

### 3.1 AND-OR (SOP)

First level: AND gates (each AND = one K-Map group)
Second level: OR gate (combining all AND outputs)

### 3.2 OR-AND (POS)

First level: OR gates (each OR = one group of 0s)
Second level: AND gate

### 3.3 NAND-NAND, NOR-NOR Equivalence

- **NAND-NAND equivalent to AND-OR SOP** (modified signs at the ends)
- **NOR-NOR equivalent to OR-AND POS**

---

## Solved Exercises

### Exercise 1: K-Map 3 Variables

**Problem:** Simplify $F = \sum m(1, 3, 4, 5, 7)$.

**Solution:**

K-Map:

| $AB \setminus C$ | 0 | 1 |
|:---|:---:|:---:|
| 00 | 0 | 1 |
| 01 | 0 | 1 |
| 11 | 1 | 1 |
| 10 | 1 | 0 |

Groups:
- $(1, 3, 5, 7)$: $\bar{B}C$ (rows 00, 01)
- $(4, 5)$: $A\bar{B}$ (rows 11, 10)

$$
F = A\bar{B} + \bar{B}C
$$

### Exercise 2: K-Map 4 Variables with Don't Care

**Problem:** $F = \sum m(0, 1, 2, 5, 6, 7, 8, 14, 15) + \sum d(3, 12, 13)$.

**Solution:**

| $AB \setminus CD$ | 00 | 01 | 11 | 10 |
|:---|:---:|:---:|:---:|:---:|
| 00 | 1 | 1 | $X$ | 1 |
| 01 | 0 | 1 | 1 | 1 |
| 11 | $X$ | $X$ | 1 | 1 |
| 10 | 1 | 0 | 0 | 1 |

Groups:
- $m_0, m_1, m_2, m_3, m_8, m_{12}, m_{13}, m_{14}, m_{15}$... treating X as 1: an 8-cell group is not possible.
- $(m_0, m_1, m_3, m_2)$: $\bar{A}\bar{B}$
- $(m_2, m_6, m_{14}, m_{10})$: $\bar{D}$
- $(m_5, m_7, m_{13}, m_{15})$: $BC$
- $(m_8)$: $A\bar{B}\bar{C}\bar{D}$

$$
F = \bar{A}\bar{B} + \bar{D} + BC
$$

### Exercise 3: Quine-McCluskey 4 Variables

**Problem:** $F = \sum m(0, 1, 2, 8, 9, 15)$.

**Solution:**

**Step 1 - Grouping by number of 1s:**
| Row | Minterm | 1s |
|:---|:---|:---:|
| A | $m_0$ | 0 |
| A | $m_1, m_2, m_8$ | 1 |
| B | $m_9$ | 2 |
| B | $m_{15}$ | 4 |

**Step 2 - Combinations:**
- $(m_0, m_1)$: $000-$
- $(m_0, m_2)$: $00-0$
- $(m_0, m_8)$: $-000$
- $(m_1, m_9)$: $-001$
- $(m_8, m_9)$: $100-$

**Step 3 - Next level:**
- $(m_0, m_1, m_8, m_9)$: $-00-$ → $\bar{B}\bar{C}$

**PI:** $\bar{B}\bar{C}$ (covers $m_0, m_1, m_8, m_9$), $m_2$ alone ($00-0 = \bar{A}\bar{B}\bar{D}$), $m_{15}$ alone ($1111 = ABCD$).

$$
F = \bar{B}\bar{C} + \bar{A}\bar{B}\bar{D} + ABCD
$$

### Exercise 4: From Truth Table to K-Map

**Problem:** $F(A,B,C,D) = \sum m(1,3,4,6,7,10,12,13,14,15)$.

**Solution:**

| $AB \setminus CD$ | 00 | 01 | 11 | 10 |
|:---|:---:|:---:|:---:|:---:|
| 00 | 0 | 1 | 1 | 0 |
| 01 | 1 | 1 | 0 | 1 |
| 11 | 1 | 1 | 1 | 1 |
| 10 | 0 | 0 | 0 | 1 |

Groups:
- $(m_4, m_6, m_{12}, m_{14})$: $B\bar{D}$
- $(m_{12}, m_{13}, m_{14}, m_{15})$: $AB$
- $(m_1, m_3)$: $\bar{A}\bar{B}D$

$$
F = AB + B\bar{D} + \bar{A}\bar{B}D
$$

### Exercise 5: Implementation with NAND

**Problem:** Implement $F = \bar{A}\bar{B} + AC + B\bar{C}$ using only NAND.

**Solution:**

$$
F = \overline{\overline{\bar{A}\bar{B}} \cdot \overline{AC} \cdot \overline{B\bar{C}}}
$$

Two-level NAND-NAND network.

### Exercise 6: K-Map with Minimal Expressions

**Problem:** Find all equivalent simplifications for $F = \sum m(0, 1, 2, 5, 6, 7)$.

**Solution:**

| $AB \setminus CD$ | 00 | 01 | 11 | 10 |
|:---|:---:|:---:|:---:|:---:|
| 00 | 1 | 1 | 0 | 1 |
| 01 | 0 | 1 | 1 | 1 |
| 11 | 0 | 0 | 0 | 0 |
| 10 | 0 | 0 | 0 | 0 |

Group selection:
1. $(0,1,2,5,6,7)$ as individual groups: $\bar{A}\bar{B} + \bar{A}C + \bar{A}B\bar{C} + ...$

More effectively:
- $(0,1,2,6)$: $\bar{B}\bar{C} + \bar{B}D$... depends on the layout.

### Exercise 7: Constructing K-Map with Wrap-around

**Problem:** $F = \sum m(0, 2, 8, 10)$.

**Solution:**

| $AB \setminus CD$ | 00 | 01 | 11 | 10 |
|:---|:---:|:---:|:---:|:---:|
| 00 | 1 | 0 | 0 | 1 |
| 01 | 0 | 0 | 0 | 0 |
| 11 | 0 | 0 | 0 | 0 |
| 10 | 1 | 0 | 0 | 1 |

Groups with wrap-around (left-right rows):
- $(0, 2, 8, 10)$: $-0-0$ → $\bar{B}\bar{D}$

$$
F = \bar{B}\bar{D}
$$

### Exercise 8: Comparing QMC and K-Map

**Problem:** Simplify $F = \sum m(0, 1, 3, 7, 8, 9, 11, 15)$ and compare K-Map with QMC.

**Solution:**

**K-Map:**
| $AB \setminus CD$ | 00 | 01 | 11 | 10 |
|:---|:---:|:---:|:---:|:---:|
| 00 | 1 | 1 | 1 | 0 |
| 01 | 0 | 0 | 1 | 0 |
| 11 | 0 | 0 | 1 | 0 |
| 10 | 1 | 1 | 1 | 0 |

Groups:
- $(0,1,8,9)$: $\bar{B}\bar{C}$
- $(1,3,9,11)$: $\bar{C}D$
- $(3,7,11,15)$: $CD$

$$
F = \bar{B}\bar{C} + \bar{C}D + CD
$$

Simplification: $\bar{B}\bar{C} + D$

---

## Exam Tip: Recognizing Groups

In K-Map, always look first for groups of powers of 2: 8 → 4 → 2. Horizontal and vertical groups totaling 8 cells give a constant. Groups of 4 cells in corners (wrap-around) are easily overlooked. Before starting grouping, check if there are corners and edges that connect.
