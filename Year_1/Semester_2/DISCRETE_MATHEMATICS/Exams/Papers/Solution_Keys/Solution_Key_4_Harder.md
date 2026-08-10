# Answer Key — Mock Exam 4 (Harder)

> Corresponds to the file: `Mock_Exam_4_Harder.md`

---

## Topic 1 (3 points) — Planar Graphs & Inequalities

**Given:** $G = (V, E)$ connected planar graph, $v$ vertices, $e$ edges, $f$ regions. Every vertex has degree $\ge 3$.

**Tools:**
1. **Euler's Formula for planar graphs:** $v - e + f = 2$
2. **Edges-regions inequality:** Every region is defined by at least 3 edges, and every edge belongs to at most 2 regions, therefore: $3f \le 2e \Rightarrow f \le \frac{2e}{3}$
3. **Handshaking Theorem:** $2e = \sum \deg(v) \ge 3v \Rightarrow e \ge \frac{3v}{2}$

---

### Group A — Proof of $e \ge \frac{3v}{2}$

From the Handshaking Theorem: since $\deg(v_i) \ge 3$ for every vertex:

$$2e = \sum_{i=1}^{v} \deg(v_i) \ge 3v \implies e \ge \frac{3v}{2} \qquad \blacksquare$$

---

### Group B — Proof of $e \ge \frac{3f}{2}$

From the edges-regions inequality: $3f \le 2e$, therefore:

$$e \ge \frac{3f}{2} \qquad \blacksquare$$

**Justification:** Every region has at least 3 edges on its boundary. Counting pairs (edge, region) we get $3f \le 2e$ (every edge is counted at most twice).

---

### Group C — Proof of $e \ge 3v - 6$

This is the classic inequality for planar graphs.

**Step 1:** From Euler's formula: $f = 2 - v + e$.

**Step 2:** From the edges-regions inequality: $3f \le 2e$, therefore:
$$3(2 - v + e) \le 2e \implies 6 - 3v + 3e \le 2e \implies e \ge 3v - 6 \qquad \blacksquare$$

**Note-Trap:** The converse does NOT hold: $e \le 3v - 6$ is a **necessary but NOT sufficient** condition for planarity.

---

### Group D — Proof of $e \ge 2v - 4$

Similar to Group C but we use that every region has at least **4** edges (if the graph has no triangles). However for the weaker inequality $e \ge 2v - 4$:

**Step 1:** From Euler's formula: $f = 2 - v + e$.

**Step 2:** From Handshaking $2e \ge 3v$, so $e \ge \frac{3v}{2}$, and from Euler $f = 2 - v + e \ge 2 - v + \frac{3v}{2} = 2 + \frac{v}{2}$.

**Step 3:** Using $f \ge 1$ and $3f \le 2e$:
$$3(2 - v + e) \le 2e \implies e \ge 3v - 6 \ge 2v - 4 \text{ for } v \ge 2$$

So $e \ge 2v - 4$ holds as a weak inequality. $\blacksquare$

---

## Topic 2 (4 points) — Regular Expressions (Complex)

**Alphabet:** $\Sigma = \{a, b\}$

---

### Group A — Language without $bb$

**Idea:** After every $b$ must follow $a$ or the end of the string. Also the $b$ can appear only once consecutively.

**Regular Expression:**
$$b^* (ab^*)^* = (a \mid ba)^* b^?$$

More precisely: Every $b$ must be followed by $a$ or be at the end. Therefore:

$$L_A = (a \mid ba)^* b^?$$

Verification:
- $\varepsilon$: accepted (zero repetitions $\times$ no $b$)
- $a$: accepted
- $ba$: accepted
- $bb$: not accepted
- $aba$: accepted

---

### Group B — Every $a$ is immediately followed by $\ge 1$ $b$

**Idea:** The $a$ cannot appear without at least one $b$ immediately after. Also $b$ can appear on its own.

$$L_B = b^* (ab^+)^* b^*$$

Verification:
- $abbb$: accepted
- $a$: not accepted (no $b$ follows)
- $bab$: accepted
- $aa$: not accepted

---

### Group C — Number of $a$'s a multiple of 3

**Idea:** We use the fact that between (and around) every group of three $a$'s any number of $b$'s can appear.

$$L_\Gamma = b^* (ab^*ab^*ab^*)^* b^*$$

Verification:
- $\varepsilon$: accepted (0 = 3·0)
- $bbb$: accepted (0 $a$)
- $aaa$: accepted (3 $a$)
- $aa$: not accepted (2 $a$)
- $babbab$: accepted (2 $a$ — a correction to an earlier note in the source)

---

### Group D — Without $aa$ and without $bb$

**Idea:** The $a$'s and $b$'s must alternate. Allowed strings: $\varepsilon, a, b, ab, ba, aba, bab, abab, baba, \ldots$

$$L_\Delta = (ab)^*(a \mid \varepsilon) \mid (ba)^*(b \mid \varepsilon)$$

Or equivalently:

$$L_\Delta = a?(ba)^*b? $$

Verification:
- $aba$: accepted
- $bab$: accepted
- $aa$: not accepted
- $abba$: not accepted

---

## Topic 3 (3 points) — Principle of Inclusion-Exclusion

**Given:**
- Set $|U| = 100$ students
- $|D| = 60$ (Discrete), $|P| = 50$ (Programming), $|G| = 40$ (Linear Algebra)
- $|D \cap P \cap G| = x$ (per Group)
- Unknown: $|D \cap P|, |D \cap G|, |P \cap G|$

**Inclusion-Exclusion Formula:**
$$|D \cup P \cup G| = |D| + |P| + |G| - |D \cap P| - |D \cap G| - |P \cap G| + |D \cap P \cap G|$$
$$= 60 + 50 + 40 - (|D \cap P| + |D \cap G| + |P \cap G|) + x = 150 - S_2 + x$$

where $S_2 = |D \cap P| + |D \cap G| + |P \cap G|$.

**Students who attend NONE:**
$$N_0 = 100 - |D \cup P \cup G| = 100 - 150 + S_2 - x = S_2 - 50 - x$$

**Bounds for $S_2$:**
- Lower bound: $S_2 \ge 3x$ (every student who belongs to all 3 courses is counted 3 times in $S_2$)
- Upper bound: $S_2 \le |D \cap P| + |D \cap G| + |P \cap G| \le \min(|D|,|P|) + \ldots$

We use: $|D \cap P| \le \min(60, 50) = 50$, $|D \cap G| \le \min(60, 40) = 40$, $|P \cap G| \le \min(50, 40) = 40$.
So $S_2 \le 130$.

Also, $|D \cup P \cup G| \le 100 \Rightarrow S_2 \ge 150 - 100 + x - 0 = 50 + x$ (minimum $S_2$).
Also, $N_0 \ge 0 \Rightarrow S_2 \ge 50 + x$.

**Results per Group:**

### Group A — $x = 10$

$N_0 = S_2 - 60$

- Minimum $N_0$: $S_2 = 50 + 10 = 60 \Rightarrow N_0 = 0$
- Maximum $N_0$: $S_2 \le 130$ (and also $|D \cup P \cup G| \ge 0$, so $S_2 \le 150 + 10 = 160$, but from the upper bounds $S_2 \le 130$) $\Rightarrow N_0 \le 130 - 60 = 70$.

**Minimum:** 0 students with none. **Maximum:** 70 students with none.

### Group B — $x = 15$

$N_0 = S_2 - 65$

- Minimum: $S_2 = 65 \Rightarrow N_0 = 0$
- Maximum: $S_2 \le 130 \Rightarrow N_0 \le 65$

**Minimum:** 0. **Maximum:** 65.

### Group C — $x = 20$

$N_0 = S_2 - 70$

- Minimum: $S_2 = 70 \Rightarrow N_0 = 0$
- Maximum: $S_2 \le 130 \Rightarrow N_0 \le 60$

**Minimum:** 0. **Maximum:** 60.

### Group D — $x = 5$

$N_0 = S_2 - 55$

- Minimum: $S_2 = 55 \Rightarrow N_0 = 0$
- Maximum: $S_2 \le 130 \Rightarrow N_0 \le 75$

**Minimum:** 0. **Maximum:** 75.