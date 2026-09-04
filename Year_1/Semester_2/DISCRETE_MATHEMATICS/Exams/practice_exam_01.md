# Practice Exam 01: Discrete Mathematics

## Context and Grounding
This practice exam provides an integrated assessment of the foundational mathematical structures taught in Discrete Mathematics, including formal logic, induction, relations, counting principles, and graph theory. It provides complete solutions and a step-by-step scoring breakdown.

---

## Part 1: Logic, Predicates, and Proofs (25 Points)

### Question 1.1 (10 Points)
Construct a truth table to determine whether the following proposition is a tautology, contradiction, or contingency:
$$((p \lor q) \land \neg(p \land q)) \leftrightarrow (p \oplus q)$$

### Question 1.2 (15 Points)
Prove by mathematical induction that for every positive integer $n \ge 1$:
$$1 \cdot 2 + 2 \cdot 3 + 3 \cdot 4 + \dots + n(n + 1) = \frac{n(n + 1)(n + 2)}{3}$$

---

## Part 2: Sets, Relations, and Combinatorics (35 Points)

### Question 2.1 (15 Points)
Let relation $R$ on $\mathbb{Z}$ be defined by $(a, b) \in R \iff a \equiv b \pmod 5$.
1. Prove that $R$ is an equivalence relation.
2. Determine the equivalence class $[3]$ and write its formal set representation.
3. How many distinct equivalence classes are formed by $R$?

### Question 2.2 (20 Points)
A committee of 6 members is to be formed from a department of 10 professors and 14 graduate students.
1. In how many ways can the committee be selected with no restrictions?
2. In how many ways can the committee be formed if it must contain at least 2 professors and at least 2 graduate students?

---

## Part 3: Graph Theory and Trees (40 Points)

### Question 3.1 (20 Points)
Let $G = (V, E)$ be a connected simple graph with 15 vertices and 21 edges.
1. Does $G$ necessarily contain a cycle? Justify using tree theorems.
2. If every vertex in $G$ has degree either 2 or 4, determine the exact number of vertices of degree 2 and degree 4.
3. Determine whether $G$ has an Eulerian circuit, an Eulerian path, or neither.

### Question 3.2 (20 Points)
A connected planar graph has 10 vertices, each of degree 3.
1. Calculate the total number of edges in $G$.
2. Use Euler's formula to determine how many regions (faces) are formed in any planar drawing of $G$.
3. Prove that it is impossible for all regions of $G$ to have boundaries of length 5 or greater.

---

## Complete Worked Solutions and Scoring Breakdown

### Solution 1.1
Observe that $(p \lor q) \land \neg(p \land q)$ is the semantic definition of the exclusive-OR operation ($p$ or $q$, but not both).
* For $(p, q) = (T, T)$: $(T \lor T) \land \neg(T) = T \land F = F$. $T \oplus T = F$. $F \leftrightarrow F \equiv T$.
* For $(p, q) = (T, F)$: $(T \lor F) \land \neg(F) = T \land T = T$. $T \oplus F = T$. $T \leftrightarrow T \equiv T$.
* For $(p, q) = (F, T)$: $(F \lor T) \land \neg(F) = T \land T = T$. $F \oplus T = T$. $T \leftrightarrow T \equiv T$.
* For $(p, q) = (F, F)$: $(F \lor F) \land \neg(F) = F \land T = F$. $F \oplus F = F$. $F \leftrightarrow F \equiv T$.
Since the evaluation yields True under all four truth assignments, the proposition is a **Tautology**.

### Solution 1.2
* **Basis Step ($n=1$):**
  $$\text{LHS} = 1 \cdot (1 + 1) = 2$$
  $$\text{RHS} = \frac{1(1 + 1)(1 + 2)}{3} = \frac{1 \times 2 \times 3}{3} = 2$$
  Since $\text{LHS} = \text{RHS} = 2$, the base case holds.
* **Inductive Hypothesis:** Assume the statement holds for an integer $k \ge 1$:
  $$\sum_{i=1}^k i(i + 1) = \frac{k(k + 1)(k + 2)}{3}$$
* **Inductive Step:** Show that the statement holds for $k + 1$:
  $$\sum_{i=1}^{k+1} i(i + 1) = \left(\sum_{i=1}^k i(i + 1)\right) + (k + 1)(k + 2)$$
  Substitute the induction hypothesis:
  $$= \frac{k(k + 1)(k + 2)}{3} + (k + 1)(k + 2) = (k + 1)(k + 2) \left[ \frac{k}{3} + 1 \right] = \frac{(k + 1)(k + 2)(k + 3)}{3}$$
  This matches the target expression for $k+1$.
* **Conclusion:** By mathematical induction, the identity holds for all integers $n \ge 1$. $\blacksquare$

### Solution 2.1
1. Equivalence proofs:
   * **Reflexive:** $a - a = 0 = 5 \times 0 \implies a \equiv a \pmod 5$.
   * **Symmetric:** If $a - b = 5k$, then $b - a = 5(-k) \implies b \equiv a \pmod 5$.
   * **Transitive:** If $a - b = 5k$ and $b - c = 5m$, then $a - c = (a - b) + (b - c) = 5(k + m) \implies a \equiv c \pmod 5$.
   Thus, $R$ is an equivalence relation.
2. $[3] = \{x \in \mathbb{Z} \mid x \equiv 3 \pmod 5\} = \{5k + 3 \mid k \in \mathbb{Z}\} = \{\dots, -7, -2, 3, 8, 13, \dots\}$.
3. There are exactly 5 distinct equivalence classes: $[0], [1], [2], [3], [4]$.

### Solution 2.2
Total people: $10 + 14 = 24$.
1. Total unrestricted selections:
   $$\binom{24}{6} = \frac{24!}{6! \, 18!} = 134,596$$
2. Breakdown by composition (Professors $P$, Students $S$):
   * Case 1 (2 P, 4 S): $\binom{10}{2} \times \binom{14}{4} = 45 \times 1,001 = 45,045$
   * Case 2 (3 P, 3 S): $\binom{10}{3} \times \binom{14}{3} = 120 \times 364 = 43,680$
   * Case 3 (4 P, 2 S): $\binom{10}{4} \times \binom{14}{2} = 210 \times 91 = 19,110$
   Summing disjoint cases:
   $$45,045 + 43,680 + 19,110 = 107,835 \text{ ways}$$

### Solution 3.1
1. Any tree on 15 vertices has exactly $15 - 1 = 14$ edges. Because $G$ is connected and has $21 > 14$ edges, adding any edge to a spanning tree creates a fundamental cycle. Therefore, $G$ must contain at least $21 - 14 = 7$ cycles.
2. Let $x$ be the number of degree 2 vertices and $y$ be the number of degree 4 vertices.
   * Total vertices: $x + y = 15 \implies x = 15 - y$
   * Handshaking lemma: $2x + 4y = 2|E| = 2(21) = 42$
   Substitute $x$:
   $$2(15 - y) + 4y = 42 \implies 30 + 2y = 42 \implies 2y = 12 \implies y = 6$$
   Then $x = 15 - 6 = 9$.
   There are 9 vertices of degree 2 and 6 vertices of degree 4.
3. Since all vertices have even degrees (either 2 or 4), every vertex degree is even. By Euler's Theorem, a connected graph where every vertex has an even degree contains an **Eulerian circuit**.

### Solution 3.2
1. By the Handshaking Lemma:
   $$2E = \sum \deg(v) = 10 \times 3 = 30 \implies E = 15$$
2. By Euler's Polyhedral Formula ($V - E + R = 2$):
   $$10 - 15 + R = 2 \implies -5 + R = 2 \implies R = 7 \text{ regions}$$
3. Suppose every region has a boundary of length at least 5 ($e \ge 5$). Each edge borders at most 2 regions, so:
   $$2E \ge 5R$$
   Substitute $E = 15$ and $R = 7$:
   $$2(15) \ge 5(7) \implies 30 \ge 35 \quad (\text{Contradiction!})$$
   Thus, it is impossible for all regions to have degree 5 or greater. At least one region must be bounded by fewer than 5 edges. $\blacksquare$

