# Lecture 02: Probability Spaces, Conditional Probability, and Bayes' Theorem

This lecture covers mathematical probability foundations: sample spaces, Kolmogorov's probability axioms, event algebra, conditional probability, independent vs. mutually exclusive events, the Law of Total Probability, and Bayes' Theorem.

---

## 1. Sample Spaces, Events, and Kolmogorov Axioms

An **experiment** produces outcomes that cannot be predicted with certainty.
- **Sample Space ($\Omega$):** The set of all possible fundamental outcomes $\omega$.
- **Event ($A$):** Any subset of the sample space ($A \subseteq \Omega$).

### 1.1 Kolmogorov's Three Probability Axioms
A probability function $P: \mathcal{F} \to \mathbb{R}$ assigns a real number to every event $A$ satisfying:
1. **Non-negativity:** For every event $A$,
   $$P(A) \ge 0$$
2. **Total Probability of Sample Space:**
   $$P(\Omega) = 1.0$$
3. **Countable Additivity:** For any sequence of pairwise mutually exclusive (disjoint) events $A_1, A_2, \dots$ ($A_i \cap A_j = \emptyset$ for $i \neq j$):
   $$P\left( \bigcup_{i=1}^{\infty} A_i \right) = \sum_{i=1}^{\infty} P(A_i)$$

### 1.2 Derived Event Relations
- Empty set: $P(\emptyset) = 0$.
- Complement rule: $P(A') = 1 - P(A)$.
- General Addition Rule:
  $$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$
- Difference rule:
  $$P(A \cap B') = P(A - B) = P(A) - P(A \cap B)$$
- De Morgan's Laws:
  $$(A \cup B)' = A' \cap B', \quad (A \cap B)' = A' \cup B'$$

---

## 2. Conditional Probability and Stochastic Independence

### 2.1 Conditional Probability
The probability of event $A$ given that event $B$ has already occurred ($P(B) > 0$):

$$
P(A \mid B) = \frac{P(A \cap B)}{P(B)}
$$

Multiplication Rule:

$$
P(A \cap B) = P(B) \cdot P(A \mid B) = P(A) \cdot P(B \mid A)
$$

### 2.2 Independent Events vs. Mutually Exclusive Events
Two events $A$ and $B$ are **statistically independent** if and only if:

$$
P(A \cap B) = P(A) \cdot P(B) \iff P(A \mid B) = P(A)
$$

**Critical Distinction:**
- **Mutually Exclusive (Disjoint):** $A \cap B = \emptyset \implies P(A \cap B) = 0$. Two disjoint events with non-zero probability can **never** be independent.
- **Independent:** Knowledge about $B$ imparts zero information about $A$.

---

## 3. Law of Total Probability

Let $B_1, B_2, \dots, B_k$ form a **partition** of sample space $\Omega$ (meaning they are pairwise disjoint: $B_i \cap B_j = \emptyset$, and exhaustive: $\bigcup_{i=1}^{k} B_i = \Omega$, with $P(B_i) > 0$).
For any arbitrary event $A$:

$$
P(A) = \sum_{i=1}^{k} P(A \cap B_i) = \sum_{i=1}^{k} P(B_i) \cdot P(A \mid B_i)
$$

---

## 4. Bayes' Theorem

Bayes' Theorem inverts conditional probabilities, updating prior probabilities $P(B_r)$ into posterior probabilities $P(B_r \mid A)$ following experimental evidence $A$:

$$
P(B_r \mid A) = \frac{P(B_r \cap A)}{P(A)} = \frac{P(B_r) \cdot P(A \mid B_r)}{\sum_{i=1}^{k} P(B_i) \cdot P(A \mid B_i)}
$$

### 4.1 Classical Medical / Network Diagnostic Example
A network IDS alerts with probability $0.98$ when an intrusion occurs ($P(\text{Alert} \mid \text{Intrusion}) = 0.98$), but has a false alarm rate of $0.03$ ($P(\text{Alert} \mid \text{Normal}) = 0.03$). Intrusions occur with prior rate $P(\text{Intrusion}) = 0.005$.
What is the probability an intrusion is actually taking place given an alert?

$$
P(\text{Intrusion} \mid \text{Alert}) = \frac{0.005 \times 0.98}{(0.005 \times 0.98) + (0.995 \times 0.03)} = \frac{0.0049}{0.0049 + 0.02985} = \frac{0.0049}{0.03475} \approx \mathbf{14.1\%}
$$
Despite a $98\%$ detection rate, the low prior makes false alarms dominate alerts.

