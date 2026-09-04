# Lecture 02: Karnaugh Maps and Gate-Level Minimization

## Context and Grounding
This lecture addresses algebraic and graphical methods for gate-level minimization of combinational logic. It formalizes Karnaugh map (K-map) geometry, Gray code adjacency, prime implicant determination, don't-care condition utilization, two-level NAND/NOR logic realization, and static hazard prevention.

---

## 1. Karnaugh Map (K-Map) Architecture

A Karnaugh map is a modified truth table array where adjacent cells differ in only a **single binary bit** (Gray code ordering). Grouping adjacent cells containing $1$s mechanically applies the Boolean absorption theorem:
$$x y + x y' = x (y + y') = x \cdot 1 = x$$

### 1.1 2-, 3-, and 4-Variable K-Map Geometries
* **2-Variable Map (4 cells)**: Rows ($A \in \{0, 1\}$), Columns ($B \in \{0, 1\}$).
* **3-Variable Map (8 cells)**: Rows ($A \in \{0, 1\}$), Columns ($BC \in \{00, 01, 11, 10\}$).
* **4-Variable Map (16 cells)**: Rows ($AB \in \{00, 01, 11, 10\}$), Columns ($CD \in \{00, 01, 11, 10\}$).

```text
4-Variable K-Map Cell Numbering:
   CD \ 00   01   11   10
AB   ┌────┬────┬────┬────┐
00   │  0 │  1 │  3 │  2 │
     ├────┼────┼────┼────┤
01   │  4 │  5 │  7 │  6 │
     ├────┼────┼────┼────┤
11   │ 12 │ 13 │ 15 │ 14 │
     ├────┼────┼────┼────┤
10   │  8 │  9 │ 11 │ 10 │
     └────┴────┴────┴────┘
```

---

## 2. Grouping Rules and Prime Implicant Analysis

### 2.1 Grouping Axioms
1. Groups must contain $2^k$ cells ($1, 2, 4, 8, 16$).
2. Groups must be rectangular and may wrap around top/bottom and left/right map edges.
3. Groups should be chosen as large as possible to eliminate the maximum number of literal variables ($k$ merged cells eliminate $k$ literals).
4. Every cell containing a $1$ must belong to at least one group; groups may overlap.

### 2.2 Definitions
* **Implicant**: Any product term corresponding to a valid group of $1$s.
* **Prime Implicant (PI)**: An implicant group that cannot be combined with another group to form a larger group of size $2^{k+1}$.
* **Essential Prime Implicant (EPI)**: A prime implicant that covers at least one minterm $1$ that is not covered by any other prime implicant.

### 2.3 Minimization Algorithm:
1. Identify all Essential Prime Implicants (EPIs) and include them in the minimal SOP expression.
2. Cover all remaining uncovered minterms using the minimum possible number of non-essential Prime Implicants.

---

## 3. Don't-Care Conditions ($d$)

In many practical digital designs, certain input combinations never occur physically (e.g., states $10-15$ in BCD arithmetic):
$$F(A, B, C, D) = \sum m(\dots) + \sum d(\dots)$$
* **Rule**: Treat don't-care $X$ cells as $1$ if they help enlarge an existing group of $1$s; otherwise, treat them as $0$ and leave them uncovered.

---

## 4. Universal Gate Implementations (NAND and NOR)

Modern CMOS fabrication exclusively favors NAND and NOR gates due to superior silicon area and switching speed compared to AND/OR gates.

### 4.1 Two-Level NAND Implementation
By involution and De Morgan's laws, any minimal Sum of Products (SOP) directly translates to a **two-level NAND-NAND** circuit:
$$F = (A B) + (C D) \iff F = [ (A B)' \cdot (C D)' ]'$$

```text
A ──┐
    ├──[NAND 1]──┐
B ──┘            │
                 ├──[NAND 3]── F
C ──┐            │
    ├──[NAND 2]──┘
D ──┘
```

### 4.2 Two-Level NOR Implementation
Similarly, any minimal Product of Sums (POS) directly translates to a **two-level NOR-NOR** circuit.

---

## 5. Combinational Hazards and Glitches

A **static-1 hazard** is a temporary spurious $1 \to 0 \to 1$ transition glitch that occurs when an input variable switches between two adjacent K-map groups:
* **Remedy**: Identify adjacent prime implicant groups that share boundary cells and add a **redundant consensus implicant** to bridge the boundary.

