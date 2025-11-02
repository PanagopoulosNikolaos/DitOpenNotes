# 20 Discrete Mathematics Exercises with Solutions

## Beginner Level (1-5)

### Exercise 1: Basic Set Operations
**Problem:** Given sets A = {1, 2, 3, 4} and B = {3, 4, 5, 6}, find:
- A ∪ B (union)
- A ∩ B (intersection)
- A - B (difference)

**Solution:**
- A ∪ B = {1, 2, 3, 4, 5, 6}
- A ∩ B = {3, 4}
- A - B = {1, 2}

---

### Exercise 2: Truth Tables
**Problem:** Create a truth table for the logical expression (P ∧ Q) ∨ ¬R

**Solution:**

| P | Q | R | P ∧ Q | ¬R | (P ∧ Q) ∨ ¬R |
|---|---|---|-------|----|----|
| T | T | T | T | F | T |
| T | T | F | T | T | T |
| T | F | T | F | F | F |
| T | F | F | F | T | T |
| F | T | T | F | F | F |
| F | T | F | F | T | T |
| F | F | T | F | F | F |
| F | F | F | F | T | T |

---

### Exercise 3: Combinations
**Problem:** In how many ways can we choose 3 items from 5 distinct items?

**Solution:**
Using the combination formula: $C(n,k) = \frac{n!}{k!(n-k)!}$

$$C(5,3) = \frac{5!}{3!2!} = \frac{5 \times 4}{2 \times 1} = 10$$

**Answer:** 10 ways

---

### Exercise 4: Permutations
**Problem:** How many 3-digit codes can be formed using digits 0-9 without repetition?

**Solution:**
Using permutations: $P(n,k) = \frac{n!}{(n-k)!}$

$$P(10,3) = \frac{10!}{7!} = 10 \times 9 \times 8 = 720$$

**Answer:** 720 codes

- If leading zeros are disallowed the count would be $9×9×8 = 648$.
---

### Exercise 5: Simple Graph Theory
**Problem:** A graph has vertices {A, B, C, D} with edges {(A,B), (B,C), (C,D), (D,A), (A,C)}. Find the degree of each vertex.

**Solution:**
- Degree of A: 3 (connected to B, D, C)
- Degree of B: 2 (connected to A, C)
- Degree of C: 3 (connected to B, D, A)
- Degree of D: 2 (connected to C, A)

---

## Intermediate Level (6-13)

### Exercise 6: Counting Principle with Constraints
**Problem:** How many 4-digit numbers can be formed using digits 1-9 where the first digit must be odd and the last digit must be even?

**Solution:**
- First digit (odd): 5 choices {1, 3, 5, 7, 9}
- Middle two digits: 9 choices each (can be any digit 1-9)
- Last digit (even): 4 choices {2, 4, 6, 8}

Total: $5 \times 9 \times 9 \times 4 = 1620$

**Answer:** 1620 numbers

---

### Exercise 7: Inclusion-Exclusion Principle
**Problem:** Among 100 students, 40 study Math, 35 study Physics, and 20 study both. How many study at least one subject?

**Solution:**
Using inclusion-exclusion: $|M ∪ P| = |M| + |P| - |M ∩ P|$

$|M ∪ P| = 40 + 35 - 20 = 55$

**Answer:** 55 students

---

### Exercise 8: Modular Arithmetic
**Problem:** Find the remainder when $2^{100}$ is divided by 7.

**Solution:**
We find the pattern of powers of 2 modulo 7:
- $2^1 \equiv 2 \pmod{7}$
- $2^2 \equiv 4 \pmod{7}$
- $2^3 \equiv 8 \equiv 1 \pmod{7}$

The pattern repeats every 3 powers. Since $100 = 3 \times 33 + 1$:
$$2^{100} \equiv 2^1 \equiv 2 \pmod{7}$$

**Answer:** Remainder is 2

---

### Exercise 9: Mathematical Induction
**Problem:** Prove that $1 + 2 + 3 + ... + n = \frac{n(n+1)}{2}$ for all positive integers n.

**Solution:**
**Base case** (n=1): $1 = \frac{1(2)}{2} = 1$ ✓

**Inductive step:** Assume true for n=k: $1 + 2 + ... + k = \frac{k(k+1)}{2}$

For n=k+1:
$$1 + 2 + ... + k + (k+1) = \frac{k(k+1)}{2} + (k+1)$$
$$= \frac{k(k+1) + 2(k+1)}{2} = \frac{(k+1)(k+2)}{2}$$

This matches the formula for n=k+1. ✓

---

### Exercise 10: Boolean Algebra
**Problem:** Simplify: $(A + B) \cdot (A + \overline{B}) \cdot (\overline{A} + B)$

**Solution:**
$$(A + B) \cdot (A + \overline{B}) = A + (B \cdot \overline{B}) = A + 0 = A$$

$$A \cdot (\overline{A} + B) = (A \cdot \overline{A}) + (A \cdot B) = 0 + (A \cdot B) = A \cdot B$$

**Answer:** $A \cdot B$

---

### Exercise 11: Pigeonhole Principle
**Problem:** In a group of 13 people, prove that at least two must share the same birth month.

**Solution:**
We have 13 people and only 12 months. By the pigeonhole principle, if we distribute 13 items into 12 boxes, at least one box must contain more than one item. Therefore, at least two people must share the same birth month.

---

### Exercise 12: Recurrence Relations
**Problem:** Solve the recurrence relation: $a_n = 2a_{n-1} + 1$ with $a_0 = 1$

**Solution:**
Let's compute first few terms:
- $a_0 = 1$
- $a_1 = 2(1) + 1 = 3$
- $a_2 = 2(3) + 1 = 7$
- $a_3 = 2(7) + 1 = 15$

Pattern: $a_n = 2^{n+1} - 1$

**Verification:** $a_n = 2(2^n - 1) + 1 = 2^{n+1} - 2 + 1 = 2^{n+1} - 1$ ✓

---

### Exercise 13: Graph Coloring
**Problem:** What is the chromatic number of a complete graph K₅?

**Solution:**
A complete graph Kₙ requires n colors because every vertex is connected to every other vertex. Therefore, every vertex must have a different color.

For K₅, we need 5 colors.

---

## Advanced Level (14-20)

### Exercise 14: Counting with Repetition
**Problem:** How many solutions does the equation $x_1 + x_2 + x_3 = 10$ have where each $x_i$ is a non-negative integer?

**Solution:**
Using stars and bars formula: $\binom{n+k-1}{k-1}$

where n=10 (sum) and k=3 (variables)

$$\binom{10+3-1}{3-1} = \binom{12}{2} = \frac{12 \times 11}{2} = 66$$

**Answer:** 66 solutions

---

### Exercise 15: Conditional Probability
**Problem:** A box contains 5 red and 3 blue balls. Two balls are drawn without replacement. What's the probability both are red?

**Solution:**
$$P(\text{both red}) = \frac{5}{8} \times \frac{4}{7} = \frac{20}{56} = \frac{5}{14}$$

**Answer:** $\frac{5}{14} ≈ 0.357$

---

### Exercise 16: Euclidean Algorithm
**Problem:** Find gcd(252, 105) using the Euclidean algorithm.

**Solution:**
$$252 = 105 \times 2 + 42$$
$$105 = 42 \times 2 + 21$$
$$42 = 21 \times 2 + 0$$

**Answer:** gcd(252, 105) = 21

---

### Exercise 17: Euler Characteristic
**Problem:** Find the Euler characteristic of a cube (polyhedron with 8 vertices, 12 edges, and 6 faces).

**Solution:**
Euler's formula: $V - E + F = χ$

$$8 - 12 + 6 = 2$$

**Answer:** χ = 2

---

### Exercise 18: De Morgan's Laws Application
**Problem:** Simplify: $\overline{(A ∩ B) ∪ (C ∩ D)}$

**Solution:**
Using De Morgan's law: $\overline{X ∪ Y} = \overline{X} ∩ \overline{Y}$

$\overline{(A ∩ B) ∪ (C ∩ D)} = \overline{(A ∩ B)} ∩ \overline{(C ∩ D)}$

Using De Morgan again: $\overline{X ∩ Y} = \overline{X} ∪ \overline{Y}$

$= (\overline{A} ∪ \overline{B}) ∩ (\overline{C} ∪ \overline{D})$

**Answer:** $(\overline{A} ∪ \overline{B}) ∩ (\overline{C} ∪ \overline{D})$

---

### Exercise 19: Hamiltonian Cycle
**Problem:** Does a complete graph K₄ have a Hamiltonian cycle? If yes, provide an example.

**Solution:**
Yes, K₄ has a Hamiltonian cycle. In K₄ with vertices {1, 2, 3, 4}, one example is:
1 → 2 → 3 → 4 → 1

Since K₄ is complete, every vertex is connected to every other vertex, guaranteeing the existence of Hamiltonian cycles. In fact, there are (4-1)!/2 = 3 distinct Hamiltonian cycles.

---

### Exercise 20: Chinese Remainder Theorem
**Problem:** Solve the system of congruences:
- x ≡ 2 (mod 3)
- x ≡ 3 (mod 5)
- x ≡ 2 (mod 7)

**Solution:**
From the first: x = 3k + 2

Substitute into second: 3k + 2 ≡ 3 (mod 5)
3k ≡ 1 (mod 5) → k ≡ 2 (mod 5) → k = 5j + 2
So x = 3(5j + 2) + 2 = 15j + 8

Substitute into third: 15j + 8 ≡ 2 (mod 7)
15j ≡ -6 ≡ 1 (mod 7)
j ≡ 1 (mod 7) → j = 7m + 1
So x = 15(7m + 1) + 8 = 105m + 23

**Answer:** x ≡ 23 (mod 105)

The general solution is x = 23, 128, 233, ... (adding multiples of 105)
