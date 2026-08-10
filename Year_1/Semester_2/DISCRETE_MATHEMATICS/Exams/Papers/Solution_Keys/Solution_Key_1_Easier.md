# Answer Key — Mock Exam 1 (Easier)

> Corresponds to the file: `Mock_Exam_1_Easier.md`

---

## Topic 1 (3 points) — Set Operations

**Given:**
- $A = \{1, 2, 3, 4\}$
- $B = \{3, 4, 5, 6\}$
- $\Omega = \{1, 2, 3, 4, 5, 6, 7, 8\}$
- Required: $(A \cup B)^c \cup (?)$

**Step 1 — Calculation of $A \cup B$:**

$$A \cup B = \{1, 2, 3, 4, 5, 6\}$$

**Step 2 — Calculation of $(A \cup B)^c$:**

The complement with respect to $\Omega$:

$$(A \cup B)^c = \Omega \setminus (A \cup B) = \{7, 8\}$$

**Step 3 — Calculation of the individual expressions per Group:**

| Set | Value |
| :--- | :--- |
| $A \cap B$ | $\{3, 4\}$ |
| $A \setminus B$ | $\{1, 2\}$ |
| $B \setminus A$ | $\{5, 6\}$ |
| $A \oplus B$ (symmetric difference) | $\{1, 2, 5, 6\}$ |

**Step 4 — Final result $(A \cup B)^c \cup (?)$ per Group:**

- **Group A:** $\{7, 8\} \cup \{3, 4\} = \{3, 4, 7, 8\}$
- **Group B:** $\{7, 8\} \cup \{1, 2\} = \{1, 2, 7, 8\}$
- **Group C:** $\{7, 8\} \cup \{5, 6\} = \{5, 6, 7, 8\}$
- **Group D:** $\{7, 8\} \cup \{1, 2, 5, 6\} = \{1, 2, 5, 6, 7, 8\}$

---

## Topic 2 (3 points) — Truth Tables & Type Classification

**Formula:** $((p \lor q) \land \neg p) \to (?)$

**Key observation:** The hypothesis $((p \lor q) \land \neg p)$ simplifies. We analyze:

$(p \lor q) \land \neg p \equiv (\neg p \land p) \lor (\neg p \land q) \equiv \bot \lor (\neg p \land q) \equiv \neg p \land q$

So the formula becomes: $(\neg p \land q) \to (?)$

**Truth Table (common for all Groups — the ($?$) column changes):**

| $p$ | $q$ | $\neg p$ | $p \lor q$ | $(p \lor q) \land \neg p$ | $q$ | $\neg q$ | $p \land q$ | $p \lor q$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| F | F | T | F | F | F | T | F | F |
| F | T | T | T | T | T | F | F | T |
| T | F | F | T | F | F | T | F | T |
| T | T | F | T | F | T | F | T | T |

**Result per Group** (the condition is true only on the row $p=F, q=T$):

- **Group A** — $(?) = q$:
  On the row $p=F, q=T$: hypothesis = T, conclusion $q$ = T. Remaining rows: hypothesis = F, so the formula = T. **Result: Tautology.**

- **Group B** — $(?) = \neg q$:
  On the row $p=F, q=T$: hypothesis = T, conclusion $\neg q$ = F. The formula = F. **Result: Contingency.**

- **Group C** — $(?) = p \land q$:
  On the row $p=F, q=T$: hypothesis = T, conclusion $p \land q = F \land T$ = F. The formula = F. **Result: Contingency.**

- **Group D** — $(?) = p \lor q$:
  On the row $p=F, q=T$: hypothesis = T, conclusion $p \lor q = F \lor T$ = T. Remaining rows: hypothesis = F. **Result: Tautology.**

---

## Topic 3 (4 points) — Graphs & Vertex Degrees

**Given:** $G = (V, E)$, $V = \{v_1, v_2, v_3, v_4, v_5\}$, degrees $= \{2, 2, 2, 3, (?)\}$.

**Handshaking Lemma:**
$$\sum_{i=1}^{n} \deg(v_i) = 2|E|$$
So the sum of the degrees must be **even**.

**Also:** In a simple graph with $n = 5$ vertices, the maximum degree of any vertex is $n - 1 = 4$.

**Analysis per Group:**

- **Group A** — $(?) = 1$:
  Sum $= 2+2+2+3+1 = 10$ (even). Edges $= 10/2 = 5$.
  Does a graph exist? Does the degree sequence $(3, 2, 2, 2, 1)$ satisfy the Erdős–Gallai theorem? Yes. **The graph exists, edges = 5.**

- **Group B** — $(?) = 3$:
  Sum $= 2+2+2+3+3 = 12$ (even). Edges $= 12/2 = 6$.
  Sequence $(3, 3, 2, 2, 2)$: verified. **The graph exists, edges = 6.**

- **Group C** — $(?) = 5$:
  **Trap!** In a simple graph with 5 vertices, $\deg_{\max} \le 4$. A degree of 5 is impossible.
  **The graph does NOT exist.**

- **Group D** — $(?) = 7$:
  **Trap!** A degree of 7 in a graph with 5 vertices is impossible ($\deg_{\max} \le 4$).
  **The graph does NOT exist.**

**Example graph for Group A** (degrees 3, 2, 2, 2, 1):
- $v_1$: connected to $v_2, v_3, v_4$ (degree 3)
- $v_2$: connected to $v_1, v_5$ (degree 2)
- $v_3$: connected to $v_1, v_4$ (degree 2)
- $v_4$: connected to $v_1, v_3$ (degree 2)
- $v_5$: connected to $v_2$ (degree 1)