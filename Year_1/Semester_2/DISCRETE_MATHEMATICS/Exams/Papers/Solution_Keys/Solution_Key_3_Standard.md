# Answer Key — Mock Exam 3 (Standard)

> Corresponds to the file: `Mock_Exam_3_Standard.md`

---

## Topic 1 (3 points) — Logic Gates & Boolean Algebra

**Given function:** $F(A, B, C) = (A\ \text{NAND}\ B)\ \text{XOR}\ (?)$

**Reminder:**
- $A\ \text{NAND}\ B \equiv \neg(A \land B)$
- $X\ \text{XOR}\ Y \equiv X \oplus Y$

---

### Group A — (?) = $C$

**a. Boolean expression:**
$$F(A, B, C) = \neg(A \land B) \oplus C$$

**b. Truth table:**

| $A$ | $B$ | $C$ | $A \land B$ | $\neg(A \land B)$ | $F = \neg(A \land B) \oplus C$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | 0 | 0 | 0 | 1 | 1 |
| 0 | 0 | 1 | 0 | 1 | 0 |
| 0 | 1 | 0 | 0 | 1 | 1 |
| 0 | 1 | 1 | 0 | 1 | 0 |
| 1 | 0 | 0 | 0 | 1 | 1 |
| 1 | 0 | 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 | 0 | 0 |
| 1 | 1 | 1 | 1 | 0 | 1 |

---

### Group B — (?) = $(B\ \text{OR}\ C)$

**a. Boolean expression:**
$$F(A, B, C) = \neg(A \land B) \oplus (B \lor C)$$

**b. Truth table:**

| $A$ | $B$ | $C$ | $\neg(A \land B)$ | $B \lor C$ | $F$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | 0 | 0 | 1 | 0 | 1 |
| 0 | 0 | 1 | 1 | 1 | 0 |
| 0 | 1 | 0 | 1 | 1 | 0 |
| 0 | 1 | 1 | 1 | 1 | 0 |
| 1 | 0 | 0 | 1 | 0 | 1 |
| 1 | 0 | 1 | 1 | 1 | 0 |
| 1 | 1 | 0 | 0 | 1 | 1 |
| 1 | 1 | 1 | 0 | 1 | 1 |

---

### Group C — (?) = $(A\ \text{AND}\ C)$

**a. Boolean expression:**
$$F(A, B, C) = \neg(A \land B) \oplus (A \land C)$$

**b. Truth table:**

| $A$ | $B$ | $C$ | $\neg(A \land B)$ | $A \land C$ | $F$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | 0 | 0 | 1 | 0 | 1 |
| 0 | 0 | 1 | 1 | 0 | 1 |
| 0 | 1 | 0 | 1 | 0 | 1 |
| 0 | 1 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 0 | 1 |
| 1 | 0 | 1 | 1 | 1 | 0 |
| 1 | 1 | 0 | 0 | 0 | 0 |
| 1 | 1 | 1 | 0 | 1 | 1 |

---

### Group D — (?) = $(\text{NOT}\ C)$

**a. Boolean expression:**
$$F(A, B, C) = \neg(A \land B) \oplus \neg C$$

**b. Truth table:**

| $A$ | $B$ | $C$ | $\neg(A \land B)$ | $\neg C$ | $F$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | 0 | 0 | 1 | 1 | 0 |
| 0 | 0 | 1 | 1 | 0 | 1 |
| 0 | 1 | 0 | 1 | 1 | 0 |
| 0 | 1 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 1 | 0 | 1 |
| 1 | 1 | 0 | 0 | 1 | 1 |
| 1 | 1 | 1 | 0 | 0 | 0 |

---

## Topic 2 (4 points) — Indexed Sets

**Given:** $A_i = [i,\, i+2]$ for $i \in \mathbb{Z}^+$ (closed intervals of real numbers).

**Question 1 — Union $\bigcup_{i=1}^{n} A_i$:**

$$A_1 = [1,3],\quad A_2 = [2,4],\quad A_3 = [3,5],\quad \ldots,\quad A_n = [n, n+2]$$

Each interval overlaps with the next (e.g. $A_1$ and $A_2$ share $[2,3]$). Therefore:

$$\bigcup_{i=1}^{n} A_i = [1,\, n+2]$$

---

**Question 2 — Intersection $\bigcap_{i=(?)}^{n+2} A_i$ per Group:**

The intersection of the closed intervals $[i, i+2]$ from index $k$ to $n+2$ is the interval that belongs to **all** $A_i$. The largest left endpoint is $n+2$ and the smallest right endpoint is $(k) + 2$.

For the intersection not to be empty we need: $n+2 \le k+2 \Rightarrow k \ge n$.

- **Group A** — (?) = $n$:
  $$\bigcap_{i=n}^{n+2} A_i = [n, n+2] \cap [n+1, n+3] \cap [n+2, n+4] = \{n+2\}$$
  The only common point is $n+2$.

- **Group B** — (?) = $n-1$:
  $$\bigcap_{i=n-1}^{n+2} A_i$$
  Left endpoint: $\max\{n-1, n, n+1, n+2\} = n+2$. Right endpoint: $\min\{n+1, n+2, n+3, n+4\} = n+1$.
  Since $n+2 > n+1$, the intersection is the **empty set** $\emptyset$.

- **Group C** — (?) = $1$:
  $$\bigcap_{i=1}^{n+2} A_i$$
  Left endpoint: $n+2$. Right endpoint: $1+2 = 3$.
  For $n \ge 2$: $n+2 > 3$, so the intersection = $\emptyset$.
  For $n = 1$: intersection = $\{3\}$.

- **Group D** — (?) = $n+1$:
  $$\bigcap_{i=n+1}^{n+2} A_i = [n+1, n+3] \cap [n+2, n+4] = [n+2, n+3]$$

---

## Topic 3 (3 points) — Mathematical Induction

### Group A — Sum of the first $n$ odd numbers $= n^2$

The $n$ first odd numbers are: $1, 3, 5, \ldots, (2n-1)$.

**Base:** $n=1$: $1 = 1^2$. True.

**Inductive Hypothesis:** We assume it is true for $n = k$:
$$1 + 3 + 5 + \cdots + (2k-1) = k^2$$

**Inductive Step:** We prove for $n = k+1$:
$$1 + 3 + \cdots + (2k-1) + (2k+1) = k^2 + (2k+1) = (k+1)^2$$

So it holds for every $n \ge 1$. $\blacksquare$

---

### Group B — Sum of the first $n$ even numbers $= n(n+1)$

The $n$ first even numbers: $2, 4, 6, \ldots, 2n$.

**Base:** $n=1$: $2 = 1 \cdot 2$. True.

**Inductive Hypothesis:** We assume for $n = k$:
$$2 + 4 + \cdots + 2k = k(k+1)$$

**Inductive Step:** For $n = k+1$:
$$2 + 4 + \cdots + 2k + 2(k+1) = k(k+1) + 2(k+1) = (k+1)(k+2)$$

So it holds for every $n \ge 1$. $\blacksquare$

---

### Group C — $3^n - 1$ is a multiple of 2 for $n \ge 1$

Equivalently: $2 \mid (3^n - 1)$.

**Base:** $n=1$: $3^1 - 1 = 2 = 2 \cdot 1$. True.

**Inductive Hypothesis:** We assume $2 \mid (3^k - 1)$, that is $3^k - 1 = 2m$ for some $m \in \mathbb{Z}$.

**Inductive Step:**
$$3^{k+1} - 1 = 3 \cdot 3^k - 1 = 3(3^k - 1) + 3 - 1 = 3 \cdot 2m + 2 = 2(3m + 1)$$

So $2 \mid (3^{k+1} - 1)$. $\blacksquare$

---

### Group D — $5^n - 1$ is a multiple of 4 for $n \ge 1$

**Base:** $n=1$: $5^1 - 1 = 4 = 4 \cdot 1$. True.

**Inductive Hypothesis:** We assume $4 \mid (5^k - 1)$, that is $5^k - 1 = 4m$.

**Inductive Step:**
$$5^{k+1} - 1 = 5 \cdot 5^k - 1 = 5(5^k - 1) + 5 - 1 = 5 \cdot 4m + 4 = 4(5m + 1)$$

So $4 \mid (5^{k+1} - 1)$. $\blacksquare$