# Exercises 01: Probability Theory, Set Operations, and Discrete Distributions

This practice problem set provides step-by-step solutions for event set algebra, Kolmogorov axioms, conditional probabilities, and the Binomial distribution.

---

## Problem 1: Event Probability Algebra

### Question
Let $A$ and $B$ be two events defined on the same sample space $\Omega$ with given probabilities:
$$P(A) = 0.60, \quad P(B) = 0.40, \quad P(A \cap B) = 0.24$$

1. Determine whether events $A$ and $B$ are **independent**.
2. Determine whether events $A$ and $B$ are **mutually exclusive (disjoint)**.
3. Calculate $P(A \cup B)$ (the probability that at least one of the two events occurs).
4. Calculate $P(A \cap B')$ (the probability that $A$ occurs but $B$ does not).
5. Calculate $P(A' \cap B')$ (the probability that neither event occurs).
6. Calculate $P(A \mid B)$ and $P(B \mid A)$.

---

### Solution

#### Part 1: Independence Test
Events $A$ and $B$ are independent if and only if $P(A \cap B) = P(A) \cdot P(B)$.
$$P(A) \cdot P(B) = 0.60 \times 0.40 = 0.24$$
Since $P(A \cap B) = 0.24$, the equality holds. **Events $A$ and $B$ are independent**.

#### Part 2: Disjoint Test
Two events are mutually exclusive if $A \cap B = \emptyset \implies P(A \cap B) = 0$.
Since $P(A \cap B) = 0.24 \neq 0$, **$A$ and $B$ are not mutually exclusive**.

#### Part 3: Probability of $A \cup B$
Using the general addition rule:
$$P(A \cup B) = P(A) + P(B) - P(A \cap B) = 0.60 + 0.40 - 0.24 = \mathbf{0.76}$$

#### Part 4: Probability of $A \cap B'$ (Difference Rule)
$$P(A \cap B') = P(A) - P(A \cap B) = 0.60 - 0.24 = \mathbf{0.36}$$

#### Part 5: Probability of $A' \cap B'$ (De Morgan's Law)
$$(A' \cap B') = (A \cup B)' \implies P(A' \cap B') = 1 - P(A \cup B) = 1 - 0.76 = \mathbf{0.24}$$

#### Part 6: Conditional Probabilities
$$P(A \mid B) = \frac{P(A \cap B)}{P(B)} = \frac{0.24}{0.40} = 0.60 = P(A)$$
$$P(B \mid A) = \frac{P(A \cap B)}{P(A)} = \frac{0.24}{0.60} = 0.40 = P(B)$$
This confirms independence.

---

## Problem 2: Binomial Distribution Calculations

### Question
An optical network transmission line has a bit error rate (BER) of $p = 0.05$. A frame of $n = 10$ bits is transmitted. Let $X$ denote the number of erroneous bits received.
1. State the probability mass function of $X$.
2. Calculate the probability that the frame is received without any errors ($P(X = 0)$).
3. Calculate the probability that the frame contains at least 2 bit errors ($P(X \ge 2)$).
4. Calculate the expected value $E[X]$ and variance $\text{Var}(X)$.

---

### Solution

#### Part 1: Distribution
$X \sim B(n = 10, p = 0.05)$.
$$P(X = k) = \binom{10}{k} (0.05)^k (0.95)^{10 - k} \quad \text{for } k = 0, 1, \dots, 10$$

#### Part 2: Zero Errors
$$P(X = 0) = \binom{10}{0} (0.05)^0 (0.95)^{10} = 1 \times 1 \times (0.95)^{10} \approx \mathbf{0.5987} \ (59.87\%)$$

#### Part 3: At Least 2 Errors
$$P(X \ge 2) = 1 - [P(X = 0) + P(X = 1)]$$
Compute $P(X = 1)$:
$$P(X = 1) = \binom{10}{1} (0.05)^1 (0.95)^9 = 10 \times 0.05 \times 0.63025 = 0.3151$$
$$P(X \ge 2) = 1 - [0.5987 + 0.3151] = 1 - 0.9138 = \mathbf{0.0862} \ (8.62\%)$$

#### Part 4: Moments
- $E[X] = n \cdot p = 10 \times 0.05 = \mathbf{0.50 \text{ bits}}$.
- $\text{Var}(X) = n \cdot p \cdot (1 - p) = 10 \times 0.05 \times 0.95 = \mathbf{0.475 \text{ bits}^2}$.

