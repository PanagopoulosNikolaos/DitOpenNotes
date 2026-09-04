# Assignment 02: Combinatorics, Recurrence Relations, and Graph Theory

## Objective
Apply combinatorial counting techniques, solve non-homogeneous linear recurrence relations, and analyze structural graph properties including connectivity, planarity, and tree metrics.

---

## Assignment Problems

### Problem 1: Combinatorial Counting and Inclusion-Exclusion
Find the number of integers between 1 and 1,000 (inclusive) that:
1. Are divisible by 3, 5, or 7.
2. Are divisible by 3 or 5, but NOT by 7.
3. Are relatively prime to 1,000.

### Problem 2: Solving Second-Order Recurrence Relations
Solve the following second-order linear recurrence relation with initial conditions:
$$a_n = 5a_{n-1} - 6a_{n-2} + 2^n \quad \text{for } n \ge 2$$
with $a_0 = 1$ and $a_1 = 4$.
1. Find the characteristic equation and homogeneous solution $a_n^{(h)}$.
2. Formulate the particular solution $a_n^{(p)}$ (noting root multiplicity).
3. Determine constants using the initial conditions.

### Problem 3: Graph Planarity and Colorability
Let $G = (V, E)$ be a connected simple planar graph with 12 vertices and 8 faces/regions.
1. Use Euler's formula to determine the exact number of edges in $G$.
2. Prove that $G$ must contain at least one vertex of degree 3 or less.
3. Show that any connected simple planar graph with fewer than 12 vertices must have a vertex of degree at most 4.

---

## Evaluation Rubric
| Question | Focus | Points |
|---|---|---|
| Problem 1 | Inclusion-Exclusion, sets arithmetic, totient calculations | 30 |
| Problem 2 | Characteristic roots, particular ansatz, exact solution verification | 35 |
| Problem 3 | Euler's formula, Handshaking lemma, degree bound proofs | 35 |
| **Total** | | **100** |

