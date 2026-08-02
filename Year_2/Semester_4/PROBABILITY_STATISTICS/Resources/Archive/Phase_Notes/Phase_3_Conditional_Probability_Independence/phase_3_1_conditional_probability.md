# Phase 3.1: Conditional Probability

Conditional probability is a fundamental concept in statistics that measures the likelihood of an event occurring, given that another event has already taken place. This "given" information effectively restricts the sample space to a specific subset.

## 1. Theoretical Foundation

### Definition
The conditional probability of an event $A$ given that event $B$ has occurred is the probability that $A$ happens within the restricted sample space defined by $B$.

### The Fundamental Formula
If $P(B) > 0$, the conditional probability of $A$ given $B$ is defined as:

$$P(A|B) = \frac{P(A \cap B)}{P(B)}$$

Where:
*   $P(A|B)$: Probability of $A$ occurring given $B$ has occurred.
*   $P(A \cap B)$: Probability that both $A$ and $B$ occur (Intersection).
*   $P(B)$: Probability of the conditioning event $B$.

### Intuitive Understanding: Reducing the Sample Space
Imagine a sample space $S$. When we say "given $B$", we are throwing away any part of $S$ that is not $B$. The new sample space becomes $B$. We then look for the portion of $A$ that survived this "filtering" process, which is exactly $A \cap B$.

### The Multiplication Rule
By rearranging the formula, we get the Multiplication Rule, which is used to find the probability of an intersection:

$$P(A \cap B) = P(B) \cdot P(A|B)$$
$$P(A \cap B) = P(A) \cdot P(B|A)$$

---

## 2. Solved Examples

### Example 1: Drawing Balls from an Urn
An urn contains 6 Red balls and 4 Blue balls. Two balls are drawn sequentially without replacement. What is the probability that the second ball is Red, given that the first ball was Blue?

**Step 1: Define the events.**
*   $B_1$: First ball is Blue.
*   $R_2$: Second ball is Red.

**Step 2: Analyze the initial state.**
Total balls = 10 (6R, 4B).
$P(B_1) = \frac{4}{10}$.

**Step 3: Work-in-Progress (WIP) State.**
If the first ball drawn is Blue ($B_1$ occurs), we must update the contents of the urn:
*   Total balls remaining: $10 - 1 = 9$
*   Red balls remaining: ?
*   Blue balls remaining: $4 - 1 = 3$

**Step 4: Final Calculation.**
Since we drew a Blue ball, the number of Red balls remains 6.
$$P(R_2|B_1) = \frac{\text{Red balls remaining}}{\text{Total balls remaining}} = \frac{6}{9} = \frac{2}{3}$$
$P(R_2|B_1) \approx 0.6667$.

---

### Example 2: Two-Way Frequency Table
A survey of 100 students asked about their preferred study environment.

| Gender | Library | Coffee Shop | Total |
| :--- | :---: | :---: | :---: |
| Male | 30 | 20 | 50 |
| Female | 25 | 25 | 50 |
| **Total** | **55** | **45** | **100** |

Find the probability that a student prefers the Library, given they are Female.

**Step 1: Define events.**
*   $L$: Prefers Library.
*   $F$: Is Female.

**Step 2: Identify values from the table.**
*   $n(F) = 50$
*   $n(L \cap F) = 25$

**Step 3: WIP State.**
We are calculating $P(L|F)$.
$$P(L|F) = \frac{n(L \cap F)}{n(F)} = \frac{25}{?}$$

**Step 4: Final Calculation.**
$$P(L|F) = \frac{25}{50} = 0.5$$

---

### Example 3: Rolling Two Dice
Two fair dice are rolled. What is the probability that the sum is 8, given that the first die shows a 5?

**Step 1: Define events.**
*   $S_8$: Sum is 8.
*   $D_5$: First die is 5.

**Step 2: Identify the reduced sample space (Event $D_5$).**
If the first die is 5, the possible outcomes are:
$(5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6)$.
Total outcomes in $D_5 = 6$.

**Step 3: WIP State.**
Which of these outcomes result in a sum of 8?
*   $5 + ? = 8 \implies ? = 3$
Outcome: $(5, 3)$.

**Step 4: Final Calculation.**
There is only 1 favorable outcome in the reduced sample space of 6.
$$P(S_8|D_5) = \frac{1}{6} \approx 0.1667$$

---

### Example 4: Card Drawing
A card is drawn from a standard deck of 52 cards. What is the probability it is an Ace, given that it is a Spade?

**Step 1: Define events.**
*   $A$: Card is an Ace.
*   $S$: Card is a Spade.

**Step 2: Identify counts.**
*   $n(S) = 13$ (Spades in a deck)
*   $n(A \cap S) = 1$ (The Ace of Spades)

**Step 3: WIP State.**
$$P(A|S) = \frac{P(A \cap S)}{P(S)} = \frac{1/52}{?/52}$$

**Step 4: Final Calculation.**
$$P(A|S) = \frac{1}{13} \approx 0.0769$$

---

### Example 5: Family with Two Children
A family has two children. Given that at least one is a girl, what is the probability that both are girls? (Assume $P(G) = P(B) = 0.5$).

**Step 1: Define the sample space $S$.**
$S = \{BB, BG, GB, GG\}$ where $B$ is Boy and $G$ is Girl.

**Step 2: Define the conditioning event $E$.**
$E$: At least one girl.
$E = \{BG, GB, GG\}$.
$n(E) = 3$.

**Step 3: WIP State.**
We want the probability of $GG$ given $E$.
The favorable outcome is $\{GG\}$.
$n(GG \cap E) = 1$.

**Step 4: Final Calculation.**
$$P(GG|E) = \frac{1}{3} \approx 0.3333$$

---

### Example 6: Weather and Traffic
The probability that it rains is 0.3. The probability of heavy traffic is 0.4. The probability that it rains and there is heavy traffic is 0.2. What is the probability of heavy traffic given that it is raining?

**Step 1: Define events.**
*   $R$: It rains. $P(R) = 0.3$.
*   $T$: Heavy traffic. $P(T) = 0.4$.
*   $P(R \cap T) = 0.2$.

**Step 2: Apply the formula.**
$$P(T|R) = \frac{P(T \cap R)}{P(R)}$$

**Step 3: WIP State.**
$$P(T|R) = \frac{0.2}{?}$$

**Step 4: Final Calculation.**
$$P(T|R) = \frac{0.2}{0.3} = \frac{2}{3} \approx 0.6667$$

---

### Example 7: Students Passing Exams
In a class, 70% of students passed Math, and 60% passed Physics. 50% passed both. If a student is chosen at random and we know they passed Math, what is the probability they also passed Physics?

**Step 1: Define events.**
*   $M$: Passed Math. $P(M) = 0.70$.
*   $Ph$: Passed Physics. $P(Ph) = 0.60$.
*   $P(M \cap Ph) = 0.50$.

**Step 2: Apply formula.**
$$P(Ph|M) = \frac{P(Ph \cap M)}{P(M)}$$

**Step 3: WIP State.**
$$P(Ph|M) = \frac{0.50}{0.70} = ?$$

**Step 4: Final Calculation.**
$$P(Ph|M) = \frac{5}{7} \approx 0.7143$$

---

### Example 8: Assembly Line Defects
A factory has two assembly lines, A and B. Line A produces 60% of the products and Line B produces 40%. Line A has a 5% defect rate. A product is chosen from Line A. What is the probability it is defective?

**Step 1: Identify the given information.**
*   $P(A) = 0.60$
*   $P(B) = 0.40$
*   $P(D|A) = 0.05$ (This is already a conditional probability!)

**Step 2: Rephrase the question.**
The question asks for the probability that a product is defective *given* it came from Line A.

**Step 3: WIP State.**
The value is directly provided in the problem description as the "defect rate of Line A".

**Step 4: Final Calculation.**
$$P(D|A) = 0.05$$

*Note: This example illustrates that in many word problems, the conditional probability is the "starting point" or "rate" provided for a specific subgroup.*
