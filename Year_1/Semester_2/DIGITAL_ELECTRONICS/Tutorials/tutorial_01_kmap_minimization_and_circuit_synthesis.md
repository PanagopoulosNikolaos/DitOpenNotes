# Tutorial 01: Systematic K-Map Minimization and Hazard-Free Gate Synthesis

## Context and Grounding
This tutorial presents an algorithmic guide to simplifying multi-variable Boolean expressions using Karnaugh maps, identifying essential prime implicants, handling don't-care conditions, and eliminating static logic hazards. It directly connects with `Resources/Notes/04_boolean_simplification.md`.

---

## 1. 4-Variable K-Map Layout
A 4-variable map for variables $A, B, C, D$ uses Gray-code ordering for row headers ($AB$) and column headers ($CD$):

| $AB \setminus CD$ | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| **00** | $m_0$ | $m_1$ | $m_3$ | $m_2$ |
| **01** | $m_4$ | $m_5$ | $m_7$ | $m_6$ |
| **11** | $m_{12}$ | $m_{13}$ | $m_{15}$ | $m_{14}$ |
| **10** | $m_8$ | $m_9$ | $m_{11}$ | $m_{10}$ |

---

## 2. Worked Minimization Problem

### Problem Statement
Simplify the Boolean function:
$$F(A, B, C, D) = \sum m(0, 2, 5, 7, 8, 10, 14, 15) + \sum d(3, 11)$$

### Step 1: Populate the Grid
* Cells with 1: $(0, 2, 5, 7, 8, 10, 14, 15)$
* Cells with X (don't care): $(3, 11)$
* Remaining cells: 0

| $AB \setminus CD$ | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| **00** | 1 ($m_0$) | 0 | X ($m_3$) | 1 ($m_2$) |
| **01** | 0 | 1 ($m_5$) | 1 ($m_7$) | 0 |
| **11** | 0 | 0 | 1 ($m_{15}$) | 1 ($m_{14}$) |
| **10** | 1 ($m_8$) | 0 | X ($m_{11}$) | 1 ($m_{10}$) |

### Step 2: Form Prime Implicants
1. **Corner Group of 4**: Cells $(0, 2, 8, 10)$ combine because outer edges wrap around.
   * Eliminates $A$ and $C$.
   * Resulting term: $B'D'$.
2. **Column 3 Group of 4**: Cells $(3, 7, 15, 11)$ combine using the don't-care cells $m_3$ and $m_{11}$.
   * Eliminates $A$ and $B$.
   * Resulting term: $CD$.
3. **Horizontal Adjacent Pair**: Cells $(14, 15)$ in row 11.
   * Since $m_{15}$ is already covered by $CD$, check if $m_{14}$ can be grouped as a 2-group: $(14, 15)$ gives $ABC$.
4. **Group for $m_5$**: Cell $m_5$ pairs with $m_7$, giving $A'BD$. (Note: $m_7$ is also covered by $CD$).

### Step 3: Extract Essential Prime Implicants
* Cell $m_0$ and $m_{10}$ are uniquely covered by the 4-corner group $\implies B'D'$ is **essential**.
* Cell $m_5$ is uniquely covered by the pair $(5, 7) \implies A'BD$ is **essential**.
* Cell $m_{14}$ is uniquely covered by the pair $(14, 15) \implies ABC$ is **essential**.
* Cell $m_3$ is a don't care, so $CD$ covers remaining 1s ($m_7, m_{15}$).

**Minimal Sum of Products (SOP):**
$$F(A, B, C, D) = B'D' + A'BD + ABC$$

---

## 3. Detecting and Eliminating Static-1 Hazards

A **static-1 hazard** exists if an input transition between adjacent 1-cells covered by different product terms momentarily drops the output to 0 due to asymmetric gate delays.

### Detection
In $F = B'D' + A'BD + ABC$:
* Transition between $m_7 (0111)$ and $m_{15} (1111)$ causes $A$ to change while $B=1, C=1, D=1$.
* If $A'$ turns off before $A$ turns on, both $A'BD$ and $ABC$ briefly evaluate to 0!

### Elimination
Add a consensus redundant term that overlaps the two terms:
$$\text{Consensus}(A'BD, ABC) = BCD$$

**Hazard-Free Implementation:**
$$F_{\text{hazard\_free}} = B'D' + A'BD + ABC + BCD$$

