# Phase 3.2: Independence

Independence is a statistical property where the occurrence of one event does not affect the probability of another event occurring. Understanding independence is crucial for simplifying complex probability calculations.

## 1. Theoretical Foundation

### Definition
Two events $A$ and $B$ are **independent** if the knowledge that $B$ has occurred does not change the probability of $A$ occurring.

### Mathematical Condition
The most common way to test for independence is the **Product Rule**:
Two events $A$ and $B$ are independent if and only if:
$$P(A \cap B) = P(A) \cdot P(B)$$

Alternatively, using conditional probability, $A$ and $B$ are independent if:
1. $P(A|B) = P(A)$
2. $P(B|A) = P(B)$

### Independence vs. Mutually Exclusive
It is a common mistake to confuse these two concepts:
*   **Mutually Exclusive (Disjoint):** Events *cannot* happen at the same time ($P(A \cap B) = 0$). If $A$ happens, $B$ definitely cannot happen.
*   **Independent:** Events *can* happen at the same time, but they don't influence each other.

> **Shortcut:** If $A$ and $B$ have non-zero probabilities and are mutually exclusive, they **cannot** be independent.

---

## 2. Solved Examples

### Example 1: Flipping Two Coins
If you flip a fair coin twice, what is the probability of getting two Heads?

**Step 1: Define events.**
*   $H_1$: Head on the first flip. $P(H_1) = 0.5$.
*   $H_2$: Head on the second flip. $P(H_2) = 0.5$.

**Step 2: Determine if they are independent.**
The outcome of the first flip does not affect the second. They are independent.

**Step 3: WIP State.**
Apply the product rule:
$$P(H_1 \cap H_2) = P(H_1) \cdot P(H_2) = 0.5 \cdot ?$$

**Step 4: Final Calculation.**
$$P(H_1 \cap H_2) = 0.5 \cdot 0.5 = 0.25$$

---

### Example 2: Drawing Cards with Replacement
You draw a card from a 52-card deck, look at it, put it back, shuffle, and draw again. What is the probability that both cards are Hearts?

**Step 1: Define events.**
*   $H_1$: First card is Heart. $P(H_1) = 13/52 = 0.25$.
*   $H_2$: Second card is Heart. $P(H_2) = 13/52 = 0.25$.

**Step 2: Analyze independence.**
Because of "replacement", the state of the deck is the same for both draws. The events are independent.

**Step 3: WIP State.**
$$P(H_1 \cap H_2) = 0.25 \cdot ?$$

**Step 4: Final Calculation.**
$$P(H_1 \cap H_2) = 0.0625$$

---

### Example 3: Shooting at a Target
Two archers, Alice and Bob, shoot at a target. Alice hits the target with probability 0.7, and Bob hits it with probability 0.4. If they both shoot, what is the probability they both hit?

**Step 1: Define events.**
*   $A$: Alice hits. $P(A) = 0.7$.
*   $B$: Bob hits. $P(B) = 0.4$.

**Step 2: Assume independence.**
Usually, in such problems, the performance of one person is independent of the other.

**Step 3: WIP State.**
$$P(A \cap B) = P(A) \cdot P(B) = 0.7 \cdot 0.4 = ?$$

**Step 4: Final Calculation.**
$$P(A \cap B) = 0.28$$

---

### Example 4: Testing for Independence (Dice)
A fair six-sided die is rolled. Let $A = \{1, 2, 3\}$ and $B = \{2, 4, 6\}$. Are $A$ and $B$ independent?

**Step 1: Calculate individual probabilities.**
*   $P(A) = 3/6 = 0.5$
*   $P(B) = 3/6 = 0.5$

**Step 2: Identify the intersection.**
$A \cap B = \{2\}$.
$P(A \cap B) = 1/6 \approx 0.1667$.

**Step 3: WIP State.**
Check the product: $P(A) \cdot P(B) = 0.5 \cdot 0.5 = 0.25$.
Does $P(A \cap B) = P(A) \cdot P(B)$?
$? = ?$

**Step 4: Final Calculation.**
$0.1667 \neq 0.25$.
Therefore, events $A$ and $B$ are **not independent** (they are dependent).

---

### Example 5: Weather in Two Cities
The probability of rain in London is 0.4. The probability of rain in Tokyo is 0.3. Assuming these are independent, what is the probability it rains in at least one city?

**Step 1: Define events.**
*   $L$: Rain in London. $P(L) = 0.4$.
*   $T$: Rain in Tokyo. $P(T) = 0.3$.

**Step 2: Identify the method.**
"At least one" is best solved using the complement: $1 - P(\text{None})$.
$P(L^c) = 0.6$, $P(T^c) = 0.7$.

**Step 3: WIP State.**
$P(\text{Neither rains}) = P(L^c \cap T^c) = 0.6 \cdot ?$

**Step 4: Final Calculation.**
$P(L^c \cap T^c) = 0.6 \cdot 0.7 = 0.42$.
$P(\text{At least one}) = 1 - 0.42 = 0.58$.

---

### Example 6: Three Independent Events
Three different light bulbs have probabilities 0.1, 0.2, and 0.05 of failing in the first year. What is the probability all three fail?

**Step 1: Define events.**
$F_1, F_2, F_3$ with $P(F_1)=0.1, P(F_2)=0.2, P(F_3)=0.05$.

**Step 2: Extend the product rule.**
For independent events, $P(A \cap B \cap C) = P(A) \cdot P(B) \cdot P(C)$.

**Step 3: WIP State.**
$P(F_1 \cap F_2 \cap F_3) = 0.1 \cdot 0.2 \cdot ?$

**Step 4: Final Calculation.**
$P(F_1 \cap F_2 \cap F_3) = 0.001$.

---

### Example 7: System Reliability (Parallel)
A system consists of two independent components in parallel. The system works if at least one component works. $P(C_1 \text{ works}) = 0.95$ and $P(C_2 \text{ works}) = 0.90$. Find the probability the system works.

**Step 1: Find failure probabilities.**
$P(C_1^c) = 0.05$.
$P(C_2^c) = 0.10$.

**Step 2: Calculate probability both fail.**
$P(\text{Both fail}) = 0.05 \cdot 0.10 = 0.005$.

**Step 3: WIP State.**
$P(\text{System works}) = 1 - P(\text{Both fail}) = 1 - ?$

**Step 4: Final Calculation.**
$P(\text{System works}) = 0.995$.

---

### Example 8: Probability of Exactly One
Given two independent events $A$ and $B$ with $P(A)=0.6$ and $P(B)=0.4$. What is the probability that **exactly one** of them occurs?

**Step 1: Identify the two scenarios.**
1. $A$ occurs and $B$ does not: $P(A \cap B^c)$.
2. $B$ occurs and $A$ does not: $P(B \cap A^c)$.

**Step 2: Calculate each using independence.**
$P(A \cap B^c) = 0.6 \cdot (1 - 0.4) = 0.6 \cdot 0.6 = 0.36$.
$P(B \cap A^c) = 0.4 \cdot (1 - 0.6) = 0.4 \cdot 0.4 = 0.16$.

**Step 3: WIP State.**
Add the two probabilities (since they are mutually exclusive):
$P(\text{Exactly one}) = 0.36 + ?$

**Step 4: Final Calculation.**
$P(\text{Exactly one}) = 0.52$.
