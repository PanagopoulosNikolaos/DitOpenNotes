# Combinatorics and Counting Principles

## Overview
Combinatorics investigates finite structures, arrangements, configurations, and enumeration techniques fundamental to computational complexity and discrete algorithm design.

---

## 1. Basic Rules of Counting

1. **Sum Rule (Disjoint Union)**:
   If tasks $A$ and $B$ cannot be performed simultaneously, and there are $m$ ways to do $A$ and $n$ ways to do $B$, then there are $m + n$ ways to perform either $A$ or $B$:
   $$|A \cup B| = |A| + |B| \quad (\text{if } A \cap B = \emptyset)$$

2. **Product Rule (Sequential Steps)**:
   If a procedure consists of two successive independent steps, where the first can be completed in $m$ ways and the second in $n$ ways, there are $m \times n$ total ways:
   $$|A \times B| = |A| \cdot |B|$$

---

## 2. Permutations and Combinations

### 2.1 Permutations ($P(n, r)$)
Ordered arrangements of $r$ distinct items selected from a collection of $n$ elements:
$$P(n, r) = \frac{n!}{(n - r)!} = n(n - 1)(n - 2)\cdots(n - r + 1)$$

### 2.2 Combinations ($C(n, r)$ or $\binom{n}{r}$)
Unordered selections of $r$ items from $n$ distinct elements:
$$\binom{n}{r} = \frac{P(n, r)}{r!} = \frac{n!}{r!(n - r)!}$$

Key algebraic identities:
* Symmetry: $\binom{n}{r} = \binom{n}{n - r}$
* Pascal's Identity: $\binom{n + 1}{r} = \binom{n}{r - 1} + \binom{n}{r}$
* Binomial Theorem:
  $$(x + y)^n = \sum_{k=0}^{n} \binom{n}{k} x^{n - k} y^k$$

---

## 3. The Pigeonhole Principle

### 3.1 Basic Principle
If $k + 1$ or more objects (pigeons) are placed into $k$ boxes (pigeonholes), then at least one box must contain two or more objects.

### 3.2 Generalized Pigeonhole Principle
If $N$ objects are placed into $k$ boxes, then there is at least one box containing at least:
$$\left\lceil \frac{N}{k} \right\rceil \text{ objects}$$

---

## 4. Principle of Inclusion-Exclusion (PIE)

For two finite sets:
$$|A \cup B| = |A| + |B| - |A \cap B|$$

For three finite sets:
$$|A \cup B \cup C| = |A| + |B| + |C| - (|A \cap B| + |A \cap C| + |B \cap C|) + |A \cap B \cap C|$$

For $n$ finite sets:
$$\left| \bigcup_{i=1}^n A_i \right| = \sum_{i=1}^n |A_i| - \sum_{1 \le i < j \le n} |A_i \cap A_j| + \dots + (-1)^{n - 1} \left| \bigcap_{i=1}^n A_i \right|$$

