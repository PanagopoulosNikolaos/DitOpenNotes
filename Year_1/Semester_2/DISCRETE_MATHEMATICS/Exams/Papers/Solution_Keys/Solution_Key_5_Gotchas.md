# Answer Key — Mock Exam 5 (Gotchas)

> Corresponds to the file: `Mock_Exam_5_Gotchas.md`

---

## Topic 1 (3 points) — Set Theory: Traps with $\in$ and $\subseteq$

### a. (1.5 points) — If $A \subseteq B \cup C$, then necessarily $(A \subseteq B)$ or $(A \subseteq C)$?

**Answer: FALSE.**

**Counterexample:**
- $A = \{1, 2\}$
- $B = \{1, 3\}$
- $C = \{2, 4\}$

Then $B \cup C = \{1, 2, 3, 4\}$ and $A = \{1, 2\} \subseteq \{1, 2, 3, 4\}$. So $A \subseteq B \cup C$.

However:
- $A \not\subseteq B$ because $2 \in A$ but $2 \notin B$.
- $A \not\subseteq C$ because $1 \in A$ but $1 \notin C$.

The statement is false: $A$ can "hang" between $B$ and $C$.

---

### b. (1.5 points) — The $\emptyset \in P((?))$ per Group

**Reminder:** The power set $P(X)$ contains as elements **all the subsets** of $X$. The $\emptyset$ is always a subset of any set, so $\emptyset \in P(X)$ for **every** set $X$.

**So for all Groups the answer is TRUE**, but the power sets differ:

---

**Group A — (?) = $\emptyset$:**

$$P(\emptyset) = \{\emptyset\}$$

Elements of $P(\emptyset)$: only the $\emptyset$. So $\emptyset \in P(\emptyset)$. **TRUE.**

**Trap:** $P(\emptyset) = \{\emptyset\}$ has **1 element**, i.e. $|P(\emptyset)| = 1 = 2^0$. $\emptyset$ is not equal to $\{\emptyset\}$!

---

**Group B — (?) = $\{\emptyset\}$:**

$$P(\{\emptyset\}) = \{\emptyset,\ \{\emptyset\}\}$$

So $\emptyset \in P(\{\emptyset\})$. **TRUE.**

**Trap:** Here $\{\emptyset\}$ is a set with **one element** (the empty set itself). The student must distinguish $\emptyset$ (empty set) from $\{\emptyset\}$ (set containing the empty set as an element).

---

**Group C — (?) = $\{1, 2\}$:**

$$P(\{1,2\}) = \{\emptyset,\ \{1\},\ \{2\},\ \{1,2\}\}$$

So $\emptyset \in P(\{1,2\})$. **TRUE.**

---

**Group D — (?) = $\{\{\emptyset\}\}$:**

$$P(\{\{\emptyset\}\}) = \{\emptyset,\ \{\{\emptyset\}\}\}$$

So $\emptyset \in P(\{\{\emptyset\}\})$. **TRUE.**

**Trap:** Do not confuse $\emptyset \in P(X)$ (always true) with $\emptyset \in X$ (not always true). Here $\emptyset \notin \{\{\emptyset\}\}$ (the set $\{\{\emptyset\}\}$ contains $\{\emptyset\}$ as an element, not $\emptyset$).

---

## Topic 2 (4 points) — NFA to DFA (Subset Construction)

**Language:** $L = (0 \cup 1)^*(??)(0 \cup 1)^*$, i.e. all strings that **contain** as a substring the (?) per Group.

**NFA idea:** A natural NFA for "contains $w$" has $|w|+1$ states: one initial, $|w|$ intermediate, one accepting (trap).

---

### Group A — (?) = $00$: Language of strings that contain $00$

**NFA:**
- $q_0$: initial (we have not yet seen a $0$)
- $q_1$: we saw one $0$
- $q_2$: we saw $00$ — accepting (trap)

| NFA State | with $0$ | with $1$ |
| :--- | :--- | :--- |
| $q_0$ | $\{q_0, q_1\}$ | $\{q_0\}$ |
| $q_1$ | $\{q_2\}$ | $\{q_0\}$ |
| $q_2$ | $\{q_2\}$ | $\{q_2\}$ |

**DFA Construction (Subsets):**

Initial DFA state: $\{q_0\}$

| DFA State | with $0$ | with $1$ | Accepting? |
| :--- | :--- | :--- | :---: |
| $\{q_0\}$ | $\{q_0, q_1\}$ | $\{q_0\}$ | No |
| $\{q_0, q_1\}$ | $\{q_0, q_1, q_2\}$ | $\{q_0\}$ | No |
| $\{q_0, q_1, q_2\}$ | $\{q_0, q_1, q_2\}$ | $\{q_0, q_2\}$ | Yes |
| $\{q_0, q_2\}$ | $\{q_0, q_1, q_2\}$ | $\{q_0, q_2\}$ | Yes |

**Minimal DFA: 4 states.**

**Trap:** The initial state $\{q_0\}$ and $\{q_0, q_1\}$ are not accepting, while every state containing $q_2$ is accepting.

---

### Group B — (?) = $11$: Language of strings that contain $11$

**NFA:**

| NFA State | with $0$ | with $1$ |
| :--- | :--- | :--- |
| $q_0$ | $\{q_0\}$ | $\{q_0, q_1\}$ |
| $q_1$ | $\emptyset$ | $\{q_2\}$ |
| $q_2$ | $\{q_2\}$ | $\{q_2\}$ |

**DFA Construction:**

| DFA State | with $0$ | with $1$ | Accepting? |
| :--- | :--- | :--- | :---: |
| $\{q_0\}$ | $\{q_0\}$ | $\{q_0, q_1\}$ | No |
| $\{q_0, q_1\}$ | $\{q_0\}$ | $\{q_0, q_1, q_2\}$ | No |
| $\{q_0, q_1, q_2\}$ | $\{q_0, q_2\}$ | $\{q_0, q_1, q_2\}$ | Yes |
| $\{q_0, q_2\}$ | $\{q_0, q_2\}$ | $\{q_0, q_1, q_2\}$ | Yes |

**Minimal DFA: 4 states.** (Symmetric to Group A due to the symmetry $0 \leftrightarrow 1$.)

---

### Group C — (?) = $01$: Language of strings that contain $01$

**NFA:**

| NFA State | with $0$ | with $1$ |
| :--- | :--- | :--- |
| $q_0$ | $\{q_0, q_1\}$ | $\{q_0\}$ |
| $q_1$ | $\emptyset$ | $\{q_2\}$ |
| $q_2$ | $\{q_2\}$ | $\{q_2\}$ |

**DFA Construction:**

| DFA State | with $0$ | with $1$ | Accepting? |
| :--- | :--- | :--- | :---: |
| $\{q_0\}$ | $\{q_0, q_1\}$ | $\{q_0\}$ | No |
| $\{q_0, q_1\}$ | $\{q_0, q_1\}$ | $\{q_0, q_2\}$ | No |
| $\{q_0, q_2\}$ | $\{q_0, q_1, q_2\}$ | $\{q_0, q_2\}$ | Yes |
| $\{q_0, q_1, q_2\}$ | $\{q_0, q_1, q_2\}$ | $\{q_0, q_2\}$ | Yes |

**Minimal DFA: 4 states.**

---

### Group D — (?) = $10$: Language of strings that contain $10$

**NFA:**

| NFA State | with $0$ | with $1$ |
| :--- | :--- | :--- |
| $q_0$ | $\{q_0\}$ | $\{q_0, q_1\}$ |
| $q_1$ | $\{q_2\}$ | $\emptyset$ |
| $q_2$ | $\{q_2\}$ | $\{q_2\}$ |

**DFA Construction:**

| DFA State | with $0$ | with $1$ | Accepting? |
| :--- | :--- | :--- | :---: |
| $\{q_0\}$ | $\{q_0\}$ | $\{q_0, q_1\}$ | No |
| $\{q_0, q_1\}$ | $\{q_0, q_2\}$ | $\{q_0, q_1\}$ | No |
| $\{q_0, q_2\}$ | $\{q_0, q_2\}$ | $\{q_0, q_1, q_2\}$ | Yes |
| $\{q_0, q_1, q_2\}$ | $\{q_0, q_2\}$ | $\{q_0, q_1, q_2\}$ | Yes |

**Minimal DFA: 4 states.**

---

## Topic 3 (3 points) — Function Composition & Properties

**Given:** $f: A \to B$, $g: B \to C$, $g \circ f: A \to C$.

---

### Group A — $g \circ f$ injective

**What is concluded with certainty:**

> **Theorem:** If $g \circ f$ is 1-1, then $f$ is 1-1.

**Proof:** Suppose $f(a_1) = f(a_2)$. Then $g(f(a_1)) = g(f(a_2))$, so $(g \circ f)(a_1) = (g \circ f)(a_2)$. Since $g \circ f$ is 1-1, it follows that $a_1 = a_2$. So $f$ is 1-1. $\blacksquare$

**What is NOT concluded:** $g$ is not necessarily 1-1.

**Counterexample for $g$:**
- $A = \{1\}$, $B = \{1, 2\}$, $C = \{1\}$
- $f(1) = 1$ (1-1)
- $g(1) = 1$, $g(2) = 1$ (not 1-1)
- $(g \circ f)(1) = 1$ — $g \circ f$ is 1-1, but $g$ is not.

---

### Group B — $g \circ f$ surjective

**What is concluded with certainty:**

> **Theorem:** If $g \circ f$ is onto, then $g$ is onto.

**Proof:** Suppose $c \in C$. Since $g \circ f$ is onto, there exists $a \in A$ with $(g \circ f)(a) = c$, i.e. $g(f(a)) = c$. We set $b = f(a) \in B$. Then $g(b) = c$. So $g$ is onto. $\blacksquare$

**What is NOT concluded:** $f$ is not necessarily onto.

**Counterexample for $f$:**
- $A = \{1\}$, $B = \{1, 2\}$, $C = \{1\}$
- $f(1) = 1$ (not onto, since $2 \notin \text{Im}(f)$)
- $g(1) = 1$, $g(2) = 1$ (onto, since $g$ covers $C$)
- $(g \circ f)(1) = 1$ — $g \circ f$ is onto, but $f$ is not.

---

### Group C — $g \circ f$ injective AND $f$ surjective

**What is concluded with certainty:**

From the injectivity of $g \circ f$ (Group A): $f$ is 1-1.
Given that additionally $f$ is **also** onto, $f$ is a **bijection**, hence invertible.

Then we can write: $g = (g \circ f) \circ f^{-1}$.
The composition of 1-1 functions is 1-1, so **$g$ is also 1-1**.

Therefore: **Both $f$ and $g$ are 1-1**, and additionally $f$ is also onto.

**Trap:** $g$ is not necessarily onto (it can be that $\text{Im}(g) \subsetneq C$).

---

### Group D — $g \circ f$ surjective AND $g$ injective

**What is concluded with certainty:**

From the surjectivity of $g \circ f$ (Group B): $g$ is onto.
Given that additionally $g$ is **also** 1-1, $g$ is a **bijection**, hence invertible.

Then: $f = g^{-1} \circ (g \circ f)$. The composition of onto functions is onto, so **$f$ is onto**.

Therefore: **Both $f$ and $g$ are onto**, and additionally $g$ is also 1-1.

**Trap:** $f$ is not necessarily 1-1.

**Counterexample for $f$ not-1-1:**
- $A = \{1, 2\}$, $B = \{1\}$, $C = \{1\}$
- $f(1) = 1$, $f(2) = 1$ (onto, but not 1-1)
- $g(1) = 1$ (bijection)
- $(g \circ f)(1) = 1$, $(g \circ f)(2) = 1$ — $g \circ f$ is onto.