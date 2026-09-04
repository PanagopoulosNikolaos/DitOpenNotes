# Lecture 01: Propositional Logic, Quantifiers, and Proof Techniques

## Context and Grounding
This lecture note establishes the formal foundations of mathematical logic, propositional equivalences, first-order predicate calculus, and deductive proof methodologies. It directly connects with `Resources/Notes/1_Discrete Mathematics.md` and `Lectures/1 Mathematical Logic.pdf`.

---

## 1. Propositional Logic and Semantic Truth

A proposition is a declarative statement that is either strictly True ($T$) or strictly False ($F$), but not both.

### 1.1 Logical Connectives
| Connective | Notation | Truth Condition |
|---|---|---|
| Negation | $\neg p$ or $p'$ | Inverts truth value |
| Conjunction | $p \land q$ | True iff both $p$ and $q$ are true |
| Disjunction | $p \lor q$ | True iff at least one of $p$ or $q$ is true |
| Implication | $p \to q$ | False only when $p$ is true and $q$ is false |
| Biconditional | $p \leftrightarrow q$ | True iff $p$ and $q$ share identical truth values |

### 1.2 Implication Variants
Given the conditional statement $p \to q$:
* **Converse**: $q \to p$
* **Inverse**: $\neg p \to \neg q$
* **Contrapositive**: $\neg q \to \neg p$ (Logically equivalent to $p \to q$)

---

## 2. Predicate Calculus and Quantifiers

A predicate $P(x)$ is a statement involving variable $x$ over a domain of discourse $D$.

* **Universal Quantifier ($\forall$)**: $\forall x \, P(x)$ is True iff $P(x)$ holds for every element in $D$.
* **Existential Quantifier ($\exists$)**: $\exists x \, P(x)$ is True iff $P(x)$ holds for at least one element in $D$.

### 2.1 Generalized De Morgan's Laws for Quantifiers
$$\neg (\forall x \, P(x)) \equiv \exists x \, \neg P(x)$$
$$\neg (\exists x \, P(x)) \equiv \forall x \, \neg P(x)$$

---

## 3. Fundamental Proof Techniques

### 3.1 Direct Proof
To prove $p \to q$: Assume $p$ is true. Use definitions, axioms, and established theorems to derive that $q$ must also be true.

### 3.2 Proof by Contraposition
To prove $p \to q$: Prove the logically equivalent contrapositive statement $\neg q \to \neg p$ directly.

*Example:* Prove that if $3n + 2$ is odd, then $n$ is odd ($n \in \mathbb{Z}$).
*Proof by Contraposition:* Assume $n$ is even. Then $n = 2k$ for some integer $k$.
$$3n + 2 = 3(2k) + 2 = 6k + 2 = 2(3k + 1)$$
Since $3k + 1$ is an integer, $3n + 2$ is of the form $2m$ (even). Having shown that $\neg q \implies \neg p$, the original statement $p \implies q$ is proven.

### 3.3 Proof by Contradiction (Reductio ad Absurdum)
To prove proposition $p$: Assume $\neg p$ is true. Derive a logical contradiction $R \land \neg R$. Conclude that $\neg p$ must be false, hence $p$ is true.

### 3.4 Mathematical Induction
To prove $\forall n \ge n_0, \, P(n)$:
1. **Base Case**: Verify that $P(n_0)$ is true.
2. **Inductive Hypothesis**: Assume $P(k)$ is true for an arbitrary integer $k \ge n_0$.
3. **Inductive Step**: Prove that $P(k+1)$ is true under the hypothesis.
4. **Conclusion**: By the principle of mathematical induction, $P(n)$ is true for all $n \ge n_0$.

