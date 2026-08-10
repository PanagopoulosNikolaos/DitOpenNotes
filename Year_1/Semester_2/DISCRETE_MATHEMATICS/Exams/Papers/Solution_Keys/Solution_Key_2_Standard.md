# Answer Key — Mock Exam 2 (Standard)

> Corresponds to the file: `Mock_Exam_2_Standard.md`

---

## Topic 1 (3 points) — Equivalence Relations

**Given:** $A = \{a, b, c, d\}$, $R = \{(a,a),(b,b),(c,c),(d,d),(a,b),(b,a),(?)\}$

**Reminder of the definition:** A relation is an equivalence relation if and only if it is:
1. **Reflexive:** $(x, x) \in R$ for every $x \in A$
2. **Symmetric:** if $(x,y) \in R$ then $(y,x) \in R$
3. **Transitive:** if $(x,y) \in R$ and $(y,z) \in R$ then $(x,z) \in R$

**Common Basis (all Groups):**
The pairs $(a,a),(b,b),(c,c),(d,d)$ ensure reflexivity.
The pairs $(a,b),(b,a)$ ensure symmetry between $a,b$.

---

### Group A — (?) = $(b, c)$

$R$ contains $(a,b)$ and $(b,c)$, so by transitivity $(a,c)$ is required.
$R$ contains $(b,c)$, so by symmetry $(c,b)$ is required.
$R$ contains $(b,a)$ and $(a,b) \Rightarrow (b,b)$ exists. With $(c,b)$ and $(b,a) \Rightarrow$ $(c,a)$ is required.

**$R$ is NOT an equivalence relation.** Missing: $(c,b), (a,c), (c,a)$.

Minimum addition to make it one: **Add $\{(c,b),(a,c),(c,a)\}$** (3 pairs).

Then the equivalence class $[a] = \{a, b, c\}$ and $[d] = \{d\}$.

---

### Group B — (?) = $(a, c)$

$R$ contains $(a,c)$. By symmetry $(c,a)$ is required.
$R$ contains $(b,a)$ and $(a,c) \Rightarrow$ $(b,c)$ is required.
$R$ contains $(a,b)$ and $(b,a) \Rightarrow$ ok. With $(c,a)$ and $(a,b) \Rightarrow$ $(c,b)$ is required.

**$R$ is NOT an equivalence relation.** Missing: $(c,a),(b,c),(c,b)$.

Minimum addition: **$\{(c,a),(b,c),(c,b)\}$** (3 pairs). Classes: $[a]=\{a,b,c\}$, $[d]=\{d\}$.

---

### Group C — (?) = $(c, d),(d, c)$

$R$ contains $(a,b),(b,a)$ and $(c,d),(d,c)$.

**Transitivity check:**
- $(a,b)$ and $(b,a) \Rightarrow$ needs $(a,a)$ — exists. OK.
- There is no connection between $\{a,b\}$ and $\{c,d\}$, so no problem arises.

**Symmetry check:** $(c,d)$ and $(d,c)$ — OK.

**$R$ IS an equivalence relation.** Classes: $[a]=\{a,b\}$, $[c]=\{c,d\}$.

---

### Group D — (?) = $(a, d),(d, a)$

$R$ contains $(a,d),(d,a)$.

**Transitivity check:**
- $(b,a)$ and $(a,d) \Rightarrow$ $(b,d)$ is required — **it does not exist!**
- $(d,a)$ and $(a,b) \Rightarrow$ $(d,b)$ is required — **it does not exist!**

**$R$ is NOT an equivalence relation.** $(a,b),(b,a)$ already exist but $(b,d),(d,b)$ are also needed.

Minimum addition: **$\{(b,d),(d,b)\}$** (2 pairs). Classes: $[a]=\{a,b,d\}$, $[c]=\{c\}$.

---

## Topic 2 (4 points) — DFA Design

**Alphabet:** $\Sigma = \{0, 1\}$

### Group A — Strings that end in $10$

**Idea:** We need to remember the last 1-2 symbols.

**States:**
- $q_0$: initial state (no prefix to evaluate)
- $q_1$: the last symbol was $1$
- $q_2$: the last two symbols were $10$ — **accepting state**

**Transitions:**

| State | with $0$ | with $1$ |
| :--- | :--- | :--- |
| $q_0$ | $q_0$ | $q_1$ |
| $q_1$ | $q_2$ | $q_1$ |
| $q_2$ | $q_0$ | $q_1$ |

**Accepting:** $\{q_2\}$

---

### Group B — Strings that start with $01$

**Idea:** The beginning is strictly defined. After accepting $01$, any symbol becomes accepted.

**States:**
- $q_0$: initial (nothing read)
- $q_1$: read $0$
- $q_2$: read $01$ — accepting
- $q_3$: dead state (rejection)

**Transitions:**

| State | with $0$ | with $1$ |
| :--- | :--- | :--- |
| $q_0$ | $q_1$ | $q_3$ |
| $q_1$ | $q_3$ | $q_2$ |
| $q_2$ | $q_2$ | $q_2$ |
| $q_3$ | $q_3$ | $q_3$ |

**Accepting:** $\{q_2\}$

---

### Group C — Strings that contain $11$

**Idea:** Once the $11$ is detected, we remain in an accepting state.

**States:**
- $q_0$: no $1$ has been read
- $q_1$: exactly one $1$ was read (possible start of $11$)
- $q_2$: the $11$ has been detected — **accepting** (acceptance trap)

**Transitions:**

| State | with $0$ | with $1$ |
| :--- | :--- | :--- |
| $q_0$ | $q_0$ | $q_1$ |
| $q_1$ | $q_0$ | $q_2$ |
| $q_2$ | $q_2$ | $q_2$ |

**Accepting:** $\{q_2\}$

---

### Group D — Even number of $0$ AND odd number of $1$

**Idea:** We track **simultaneously** the number of $0$'s mod 2 and the number of $1$'s mod 2.

**States** $(i, j)$ where $i$ = number of $0$'s mod 2, $j$ = number of $1$'s mod 2:
- $(0,0)$: even $0$'s, even $1$'s — initial
- $(0,1)$: even $0$'s, odd $1$'s — **accepting**
- $(1,0)$: odd $0$'s, even $1$'s
- $(1,1)$: odd $0$'s, odd $1$'s

**Transitions:**

| State | with $0$ | with $1$ |
| :--- | :--- | :--- |
| $(0,0)$ | $(1,0)$ | $(0,1)$ |
| $(0,1)$ | $(1,1)$ | $(0,0)$ |
| $(1,0)$ | $(0,0)$ | $(1,1)$ |
| $(1,1)$ | $(0,1)$ | $(1,0)$ |

**Accepting:** $\{(0,1)\}$

---

## Topic 3 (3 points) — Probability (Lottery Bag)

**Given:** 10 balls (no. 1–10), we draw 3 without replacement.

**Step 1 — Set of possible outcomes:**

$$|\Omega| = \binom{10}{3} = \frac{10 \cdot 9 \cdot 8}{3!} = 120$$

---

### Group A — Probability that the sum is even

**Analysis:** The sum of three numbers is even when:
- All three are even, or
- Two are odd and one is even.

Even numbers in $\{1,...,10\}$: $\{2,4,6,8,10\}$ — **5 numbers**
Odd numbers: $\{1,3,5,7,9\}$ — **5 numbers**

$$|E_A| = \binom{5}{3} + \binom{5}{2}\binom{5}{1} = 10 + 10 \cdot 5 = 10 + 50 = 60$$

$$P(\text{even}) = \frac{60}{120} = \frac{1}{2}$$

---

### Group B — Probability that the sum is odd

Complement of Group A:

$$P(\text{odd}) = 1 - \frac{1}{2} = \frac{1}{2}$$

**Direct verification:** The sum is odd when: three odds or one odd and two evens.

$$|E_B| = \binom{5}{3} + \binom{5}{1}\binom{5}{2} = 10 + 50 = 60 \Rightarrow P = \frac{60}{120} = \frac{1}{2}$$

---

### Group C — Probability that the sum $> 24$

Maximum possible sum: $8+9+10 = 27$. We enumerate the triples with sum $\ge 25$:

| Triple | Sum |
| :--- | :---: |
| $\{8, 9, 10\}$ | 27 |
| $\{7, 9, 10\}$ | 26 |
| $\{6, 9, 10\}$ | 25 |
| $\{7, 8, 10\}$ | 25 |
| $\{8, 9, 10\}$ | already counted |

Triples with sum $= 25$: $\{6,9,10\}$ and $\{7,8,10\}$ → 2 triples
Triples with sum $= 26$: $\{7,9,10\}$ → 1 triple
Triples with sum $= 27$: $\{8,9,10\}$ → 1 triple

$$|E_\Gamma| = 4 \qquad P = \frac{4}{120} = \frac{1}{30}$$

---

### Group D — Probability that the sum $< 10$

Minimum possible sum: $1+2+3 = 6$. We enumerate the triples with sum $\le 9$:

| Triple | Sum |
| :--- | :---: |
| $\{1, 2, 3\}$ | 6 |
| $\{1, 2, 4\}$ | 7 |
| $\{1, 2, 5\}$ | 8 |
| $\{1, 3, 4\}$ | 8 |
| $\{1, 2, 6\}$ | 9 |
| $\{1, 3, 5\}$ | 9 |
| $\{2, 3, 4\}$ | 9 |

$$|E_\Delta| = 7 \qquad P = \frac{7}{120}$$