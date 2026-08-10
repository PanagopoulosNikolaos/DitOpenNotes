# Boolean Algebra and Logic Gates

This chapter presents Boolean algebra, which forms the mathematical foundation for the design and analysis of digital circuits. It covers the Huntington axioms, properties of logical operations, the duality principle, Boolean functions, canonical forms (minterms and maxterms), standard forms, basic logic gates, digital logic families, and introductory elements for CAD/HDL.

---

## 1. Core Definitions

### 1.1 Axiomatic Definition of Boolean Algebra (Huntington, 1904)
Let $B = \{0, 1\}$ be a set of elements with two binary operators: addition $+$ (OR operation) and multiplication $\cdot$ (AND operation), and a unary complement operator $'$ (NOT operation). This structure defines a Boolean algebra if the following axioms are satisfied:
- **Closure:** For every $x, y \in B$, $x + y \in B$ and $x \cdot y \in B$.
- **Identity Element:**
  - $0$ is the identity element for the $+$ operation: $x + 0 = x$.
  - $1$ is the identity element for the $\cdot$ operation: $x \cdot 1 = x$.
- **Commutative Law:** $x + y = y + x$ and $x \cdot y = y \cdot x$.
- **Distributive Law:**
  - $\cdot$ distributes over $+$: $x \cdot (y + z) = (x \cdot y) + (x \cdot z)$.
  - $+$ distributes over $\cdot$: $x + (y \cdot z) = (x + y) \cdot (x + z)$.
- **Complement:** For every $x \in B$, there exists an element $x' \in B$ such that:
  - $x + x' = 1$
  - $x \cdot x' = 0$
- **Existence of two distinct elements:** There exist at least two elements $x, y \in B$ such that $x \neq y$.

### 1.2 Canonical Forms
- **Minterm:** A product (AND) term that contains all variables of the function in their normal or complemented form exactly once.
- **Maxterm:** A sum (OR) term that contains all variables of the function in their normal or complemented form exactly once.

---

## 2. Foundational Formulas & Theorems

### 2.1 Duality Principle
Every Boolean expression remains valid if we replace all $+$ operators with $\cdot$ (and vice versa), and all $1$s with $0$s (and vice versa).

### 2.2 Basic Theorems

| Theorem | Form (a) | Form (b) |
| :--- | :--- | :--- |
| **Theorem 1 (Idempotency)** | $x + x = x$ | $x \cdot x = x$ |
| **Theorem 2** | $x + 1 = 1$ | $x \cdot 0 = 0$ |
| **Theorem 3 (Double Negation)** | $(x')' = x$ | |
| **Theorem 4 (Associativity)** | $x + (y + z) = (x + y) + z$ | $x(yz) = (xy)z$ |
| **Theorem 5 (DeMorgan)** | $(x + y)' = x'y'$ | $(xy)' = x' + y'$ |
| **Theorem 6 (Absorption)** | $x + xy = x$ | $x(x + y) = x$ |
| **Consensus Theorem** | $xy + x'z + yz = xy + x'z$ | $(x+y)(x'+z)(y+z) = (x+y)(x'+z)$ |

---

## Solved Exercises

### Exercise 1: Proof of Idempotency $x+x=x$
**Problem:**
Prove algebraically Theorem 1(a): $x + x = x$ using only the Huntington axioms.

**Solution:**
1. Start from the left side:
   $$
   x + x = (x + x) \cdot 1 \quad (\text{Axiom 2b - identity element})
   $$
2. Substitute $1$ with $x + x'$:
   $$
   = (x + x) \cdot (x + x') \quad (\text{Axiom 5a - complement})
   $$
3. Apply the distributive law of $+$ over $\cdot$ (Axiom 4b):
   $$
   = x + (x \cdot x')
   $$
4. Substitute $x \cdot x'$ with $0$:
   $$
   = x + 0 \quad (\text{Axiom 5b - complement})
   $$
5. Simplify:
   $$
   = x \quad (\text{Axiom 2a - identity element})
   $$
   The equality has been proven.

---

### Exercise 2: Function Simplification
**Problem:**
Simplify the Boolean function $F = x'y'z + x'yz + xy'$.

**Solution:**
1. Group the first two terms and factor out $x'z$:
   $$
   F = x'z(y' + y) + xy'
   $$
2. Recognize that $y' + y = 1$:
   $$
   F = x'z(1) + xy'
   $$
3. Simplify:
   $$
   F = x'z + xy'
   $$

---

### Exercise 3: Finding Function Complement Using DeMorgan
**Problem:**
Find the complement of the function $F = x(y'z' + yz)$.

**Solution:**
1. Apply DeMorgan's theorem:
   $$
   F' = [x(y'z' + yz)]'
   $$
2. Use the rule $(AB)' = A' + B'$:
   $$
   F' = x' + (y'z' + yz)'
   $$
3. Apply DeMorgan's rule again for the sum $(A+B)' = A'B'$:
   $$
   F' = x' + (y'z')' \cdot (yz)'
   $$
4. Simplify the individual complements:
   $$
   (y'z')' = (y')' + (z')' = y + z
   $$
   $$
   (yz)' = y' + z'
   $$
5. Substitute:
   $$
   F' = x' + (y + z)(y' + z') = x' + yy' + yz' + y'z + zz'
   $$
   Since $yy' = 0$ and $zz' = 0$:
   $$
   F' = x' + y'z + yz'
   $$

---

### Exercise 4: Expressing Function as Sum of Minterms
**Problem:**
Express the function $F(A, B, C) = A + B'C$ in canonical sum-of-minterms form.

**Solution:**
1. The term $A$ lacks variables $B$ and $C$:
   $$
   A = A(B + B') = AB + AB'
   $$
   $$
   AB = AB(C + C') = ABC + ABC'
   $$
   $$
   AB' = AB'(C + C') = AB'C + AB'C'
   $$
2. The term $B'C$ lacks variable $A$:
   $$
   B'C = B'C(A + A') = AB'C + A'B'C
   $$
3. Combine all terms and remove duplicates:
   $$
   F = (ABC + ABC' + AB'C + AB'C') + (AB'C + A'B'C)
   $$
   $$
   F = ABC + ABC' + AB'C + AB'C' + A'B'C
   $$
4. Map to minterms:
   - $ABC = m_7$
   - $ABC' = m_6$
   - $AB'C = m_5$
   - $AB'C' = m_4$
   - $A'B'C = m_1$
   $$
   F(A, B, C) = \sum(1, 4, 5, 6, 7)
   $$

---

### Exercise 5: Expressing Function as Product of Maxterms
**Problem:**
Express the same function $F(A, B, C) = A + B'C$ in canonical product-of-maxterms form.

**Solution:**
1. Apply the distributive law of $+$ over $\cdot$:
   $$
   F = A + B'C = (A + B')(A + C)
   $$
2. Add missing variables to each term:
   - For term $(A + B')$, $C$ is missing:
     $$
     A + B' = A + B' + CC' = (A + B' + C)(A + B' + C')
     $$
   - For term $(A + C)$, $B$ is missing:
     $$
     A + C = A + C + BB' = (A + B + C)(A + B' + C)
     $$
3. Combine terms and remove duplicates:
   $$
   F = (A + B' + C)(A + B' + C')(A + B + C)
   $$
4. Map to maxterms:
   - $(A + B + C) = M_0$
   - $(A + B' + C) = M_2$
   - $(A + B' + C') = M_3$
   $$
   F(A, B, C) = \prod(0, 2, 3)
   $$

---

### Exercise 6: Conversion Between Canonical Forms
**Problem:**
If a 3-variable function is defined as $F(A, B, C) = \sum(1, 4, 5, 6, 7)$, find its expression as a product of maxterms.

**Solution:**
1. The maxterms that describe the function are those corresponding to the minterms missing from the sum.
2. The indices missing from the set $\{0, 1, 2, 3, 4, 5, 6, 7\}$ are $\{0, 2, 3\}$.
3. Therefore:
   $$
   F(A, B, C) = \prod(0, 2, 3)
   $$

---

### Exercise 7: Algebraic Proof of Consensus Theorem
**Problem:**
Prove algebraically the theorem: $xy + x'z + yz = xy + x'z$.

**Solution:**
1. Add the term $(x + x')$ to the term $yz$:
   $$
   xy + x'z + yz = xy + x'z + yz(x + x')
   $$
2. Expand the parentheses:
   $$
   = xy + x'z + xyz + x'yz
   $$
3. Group the terms:
   $$
   = xy(1 + z) + x'z(1 + y)
   $$
4. Since $1 + z = 1$ and $1 + y = 1$:
   $$
   = xy(1) + x'z(1) = xy + x'z
   $$
   The equality has been proven.

---

### Exercise 8: Truth Table
**Problem:**
Construct the truth table for the function $F = x'y + xy'$.

**Solution:**
Calculate the output for all possible combinations of $x, y$:

| $x$ | $y$ | $x'$ | $y'$ | $x'y$ | $xy'$ | $F$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | 0 | 1 | 1 | 0 | 0 | **0** |
| 0 | 1 | 1 | 0 | 1 | 0 | **1** |
| 1 | 0 | 0 | 1 | 0 | 1 | **1** |
| 1 | 1 | 0 | 0 | 0 | 0 | **0** |

---

## Exam Tip: Defining minterms / maxterms
A common mistake in exams is incorrectly mapping the digits $0$ and $1$ to minterms and maxterms.
- **Minterms (m):** The $0$ corresponds to the complemented variable ($x'$) and the $1$ to the normal ($x$).
  *Example:* $m_5$ ($101_2$) for variables $x, y, z$ is $xy'z$.
- **Maxterms (M):** The $0$ corresponds to the normal variable ($x$) and the $1$ to the complemented ($x'$).
  *Example:* $M_5$ ($101_2$) for variables $x, y, z$ is $x' + y + z'$.
