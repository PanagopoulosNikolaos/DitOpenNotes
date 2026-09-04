# Tutorial 01: Constructing Mathematical Induction Proofs

## Context and Grounding
This tutorial provides a systematic methodology for formulating and writing rigorous proofs using weak mathematical induction, strong induction, and structural induction. It connects directly with `Lectures/0 Mathematical Induction.pdf` and `Resources/Notes/5_Induction & Recursion.md`.

---

## 1. The Structure of an Inductive Proof

Every formal proof by mathematical induction consists of four mandatory components:
1. **Predicate Definition**: State the property $P(n)$ to be proven for integers $n \ge n_0$.
2. **Basis Step (Base Case)**: Verify that $P(n_0)$ evaluates to True.
3. **Inductive Hypothesis**: Explicitly state: *"Assume $P(k)$ is true for an arbitrary integer $k \ge n_0$"*.
4. **Inductive Step**: Using the inductive hypothesis, demonstrate that $P(k+1)$ must be true.

---

## 2. Worked Examples

### Example 1: Summation Formula
**Theorem:** Prove that for all positive integers $n \ge 1$:
$$\sum_{i=1}^n i^2 = \frac{n(n + 1)(2n + 1)}{6}$$

#### Proof:
* **Step 1:** Let $P(n)$ be the proposition $\sum_{i=1}^n i^2 = \frac{n(n+1)(2n+1)}{6}$.
* **Step 2 (Basis Step):** For $n = 1$:
  $$\text{LHS} = 1^2 = 1$$
  $$\text{RHS} = \frac{1(1 + 1)(2(1) + 1)}{6} = \frac{1 \times 2 \times 3}{6} = 1$$
  Since $\text{LHS} = \text{RHS}$, $P(1)$ is true.
* **Step 3 (Inductive Hypothesis):** Assume $P(k)$ is true for some integer $k \ge 1$, so:
  $$\sum_{i=1}^k i^2 = \frac{k(k + 1)(2k + 1)}{6}$$
* **Step 4 (Inductive Step):** We must prove $P(k+1)$, namely:
  $$\sum_{i=1}^{k+1} i^2 = \frac{(k + 1)((k + 1) + 1)(2(k + 1) + 1)}{6} = \frac{(k + 1)(k + 2)(2k + 3)}{6}$$
  Starting with the LHS of $P(k+1)$:
  $$\sum_{i=1}^{k+1} i^2 = \left(\sum_{i=1}^k i^2\right) + (k + 1)^2$$
  Substitute the Inductive Hypothesis:
  $$= \frac{k(k + 1)(2k + 1)}{6} + (k + 1)^2 = (k + 1) \left[ \frac{k(2k + 1)}{6} + (k + 1) \right]$$
  $$= (k + 1) \left[ \frac{2k^2 + k + 6k + 6}{6} \right] = (k + 1) \left[ \frac{2k^2 + 7k + 6}{6} \right]$$
  Factor the numerator: $2k^2 + 7k + 6 = (k + 2)(2k + 3)$:
  $$= \frac{(k + 1)(k + 2)(2k + 3)}{6}$$
  This matches the RHS of $P(k+1)$.
* **Conclusion:** By the principle of mathematical induction, $P(n)$ holds for all integers $n \ge 1$. $\blacksquare$

---

### Example 2: Divisibility Proof
**Theorem:** Prove that $n^3 - n$ is divisible by 3 for all integers $n \ge 1$.

#### Proof:
* **Basis Step:** For $n = 1$: $1^3 - 1 = 0 = 3 \times 0$, which is divisible by 3. $P(1)$ holds.
* **Inductive Hypothesis:** Assume $k^3 - k = 3m$ for some integer $m$ where $k \ge 1$.
* **Inductive Step:** Consider $(k + 1)^3 - (k + 1)$:
  $$(k + 1)^3 - (k + 1) = (k^3 + 3k^2 + 3k + 1) - k - 1 = (k^3 - k) + 3(k^2 + k)$$
  Substitute the Inductive Hypothesis $(k^3 - k) = 3m$:
  $$= 3m + 3(k^2 + k) = 3(m + k^2 + k)$$
  Since $m + k^2 + k$ is an integer, $(k + 1)^3 - (k + 1)$ is divisible by 3.
* **Conclusion:** $P(n)$ is true for all $n \ge 1$. $\blacksquare$

---

## 3. Strong Induction Template
Use strong induction when $P(k+1)$ depends on several preceding values ($P(n_0), P(n_0+1), \dots, P(k)$), such as in recurrence relations and fundamental theorem of arithmetic proofs.
* **Hypothesis:** Assume $P(j)$ is true for all $n_0 \le j \le k$.
* **Step:** Prove $P(k+1)$ follows from this joint hypothesis.

