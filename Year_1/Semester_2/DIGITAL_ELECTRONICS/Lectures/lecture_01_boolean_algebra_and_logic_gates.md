# Lecture 01: Boolean Algebra, Logic Gates, and Canonical Forms

## Context and Grounding
This lecture note introduces the formal algebraic foundations of switching theory, Huntington's postulates, logic gate primitives, and canonical representations of digital functions. It grounds the study material in `Resources/Notes/02_boolean_algebra_logic_gates.md` and `03_canonical_forms_sop_pos.md`.

---

## 1. Axiomatic Foundations of Boolean Algebra

Boolean algebra operates on the two-element set $B = \{0, 1\}$ equipped with binary operations $+$ (OR) and $\cdot$ (AND), and unary operation $'$ or $\overline{\phantom{A}}$ (NOT).

### 1.1 Huntington's Postulates
For all elements $x, y, z \in B$:
1. **Closure**: $x + y \in B$ and $x \cdot y \in B$.
2. **Identity Elements**:
   * $x + 0 = x$ (0 is additive identity)
   * $x \cdot 1 = x$ (1 is multiplicative identity)
3. **Commutativity**:
   * $x + y = y + x$
   * $x \cdot y = y \cdot x$
4. **Distributivity**:
   * $x \cdot (y + z) = (x \cdot y) + (x \cdot z)$
   * $x + (y \cdot z) = (x + y) \cdot (x + z)$ (Distributivity of $+$ over $\cdot$)
5. **Complementarity**:
   * $x + x' = 1$
   * $x \cdot x' = 0$

### 1.2 De Morgan's Laws and Involution
* **Involution**: $(x')' = x$
* **De Morgan's Theorem 1**: $(x + y)' = x' \cdot y'$
* **De Morgan's Theorem 2**: $(x \cdot y)' = x' + y'$

---

## 2. Fundamental Logic Gates

| Gate | Function | Truth Table | Algebraic Symbol |
|---|---|---|---|
| **AND** | Output 1 iff all inputs are 1 | $F = A \cdot B$ | $\cdot$ |
| **OR** | Output 1 iff at least one input is 1 | $F = A + B$ | $+$ |
| **NOT** | Inversion | $F = A'$ | $\overline{A}$ |
| **NAND** | Universal gate (inverted AND) | $F = (A \cdot B)'$ | $\uparrow$ |
| **NOR** | Universal gate (inverted OR) | $F = (A + B)'$ | $\downarrow$ |
| **XOR** | Output 1 iff odd number of 1s | $F = A \oplus B = A'B + AB'$ | $\oplus$ |
| **XNOR** | Equivalence | $F = (A \oplus B)' = AB + A'B'$ | $\odot$ |

---

## 3. Canonical Forms: SOP and POS

### 3.1 Sum of Minterms ($\Sigma m$)
A **minterm** is a product (AND) of all literals in which each variable appears exactly once in true or complemented form. A minterm evaluates to 1 for exactly one input combination.

$$F(A, B, C) = \sum m(1, 4, 7) = A'B'C + AB'C' + ABC$$

### 3.2 Product of Maxterms ($\Pi M$)
A **maxterm** is a sum (OR) of all literals in which each variable appears exactly once. A maxterm evaluates to 0 for exactly one input combination.

$$F(A, B, C) = \prod M(0, 2, 3, 5, 6) = (A+B+C)(A+B'+C)(A+B'+C')(A'+B+C')(A'+B'+C)$$

### 3.3 Complementary Duality
$$m_i' = M_i \quad \text{and} \quad \left(\sum m(\text{indices})\right)' = \sum m(\text{remaining indices}) = \prod M(\text{indices})$$

