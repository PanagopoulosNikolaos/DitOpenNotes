# Lecture 02: Relations, Functions, and Principles of Combinatorics

## Context and Grounding
This lecture note formalizes relations (equivalence relations and partial orderings), functions (injective, surjective, bijective), and counting principles (permutations, combinations, pigeonhole principle, inclusion-exclusion). It directly grounds `Resources/Notes/5_Induction & Recursion.md`, `6_Combinatorics & Pigeonhole.md`, and `Lectures/3 Combinatorics.pdf`.

---

## 1. Binary Relations and Properties

A binary relation $R$ from set $A$ to set $B$ is a subset of the Cartesian product $A \times B$. If $A = B$, $R$ is a relation on $A$.

### 1.1 Fundamental Properties
For all $x, y, z \in A$:
* **Reflexive**: $\forall x, \, (x, x) \in R$.
* **Symmetric**: $\forall x, y, \, (x, y) \in R \implies (y, x) \in R$.
* **Antisymmetric**: $\forall x, y, \, ((x, y) \in R \land (y, x) \in R) \implies x = y$.
* **Transitive**: $\forall x, y, z, \, ((x, y) \in R \land (y, z) \in R) \implies (x, z) \in R$.

### 1.2 Equivalence Relations and Partitions
A relation $R$ is an **equivalence relation** iff it is reflexive, symmetric, and transitive.
* **Equivalence Class**: $[a] = \{x \in A \mid (a, x) \in R\}$.
* The set of all distinct equivalence classes forms a partition of $A$ into disjoint, non-empty subsets whose union equals $A$.

### 1.3 Partial Orders (Posets)
A relation $R$ is a **partial order** iff it is reflexive, antisymmetric, and transitive. A set $A$ with a partial order $R$ is a partially ordered set (poset), denoted $(A, \le)$. Posets are visually diagrammed using **Hasse diagrams**.

---

## 2. Functions and Cardinality

A function $f: A \to B$ assigns each element $a \in A$ exactly one element $b \in B$.
* **Injective (One-to-One)**: $f(x) = f(y) \implies x = y$.
* **Surjective (Onto)**: $\forall b \in B, \, \exists a \in A \text{ such that } f(a) = b$.
* **Bijective**: Both injective and surjective. A bijection admits a unique two-sided inverse $f^{-1}: B \to A$.

---

## 3. Combinatorics and Counting Principles

### 3.1 Sum and Product Rules
* **Sum Rule**: If task $A$ can be done in $m$ ways and independent task $B$ in $n$ ways, doing either takes $m + n$ ways.
* **Product Rule**: If a procedure breaks into stages 1 and 2, with $m$ ways for stage 1 and $n$ ways for stage 2, there are $m \times n$ total outcomes.

### 3.2 Permutations and Combinations
* **Permutations** (Order matters):
  $$P(n, r) = \frac{n!}{(n - r)!}$$
* **Combinations** (Order does not matter):
  $$C(n, r) = \binom{n}{r} = \frac{n!}{r!(n - r)!}$$
* **Binomial Theorem**:
  $$(x + y)^n = \sum_{k=0}^n \binom{n}{k} x^{n-k} y^k$$

### 3.3 The Pigeonhole Principle
* **Basic Form**: If $k+1$ or more objects are placed into $k$ boxes, at least one box contains two or more objects.
* **Generalized Form**: If $N$ objects are placed into $k$ boxes, at least one box contains at least $\lceil N/k \rceil$ objects.

### 3.4 Principle of Inclusion-Exclusion (PIE)
For finite sets $A_1, A_2, \dots, A_n$:
$$|A_1 \cup A_2| = |A_1| + |A_2| - |A_1 \cap A_2|$$
$$|A_1 \cup A_2 \cup A_3| = \sum |A_i| - \sum |A_i \cap A_j| + |A_1 \cap A_2 \cap A_3|$$

