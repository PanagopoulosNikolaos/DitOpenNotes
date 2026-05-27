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


# Phase 3.3: Law of Total Probability & Bayes' Theorem

These two theorems are the most powerful tools in probability for handling multi-stage processes and updating beliefs based on new evidence.

## 1. Theoretical Foundation

### Law of Total Probability
If we have a set of events $B_1, B_2, \dots, B_n$ that **partition** the sample space (meaning they are mutually exclusive and their union is the whole space), then for any event $A$:

$$P(A) = P(A|B_1)P(B_1) + P(A|B_2)P(B_2) + \dots + P(A|B_n)P(B_n)$$

**Intuition:** To find the total probability of $A$, you sum up the probability of $A$ occurring under each possible "branch" of the sample space.

### Bayes' Theorem
Bayes' Theorem allows us to "reverse" conditional probabilities. If we know $P(A|B)$, we can find $P(B|A)$.

$$P(B_i|A) = \frac{P(A|B_i)P(B_i)}{P(A)}$$

By substituting the Law of Total Probability for the denominator $P(A)$, we get the expanded form:

$$P(B_i|A) = \frac{P(A|B_i)P(B_i)}{\sum_{j=1}^{n} P(A|B_j)P(B_j)}$$

---

## 2. Solved Examples

### Example 1: Factory Production (Total Probability)
A factory uses three machines. $M_1$ produces 50%, $M_2$ produces 30%, and $M_3$ produces 20% of the total output. The defect rates are 1%, 2%, and 5% respectively. What is the probability a random product is defective?

**Step 1: Define events.**
*   $M_i$: Product from machine $i$.
*   $D$: Product is defective.

**Step 2: List given probabilities.**
*   $P(M_1)=0.5, P(D|M_1)=0.01$
*   $P(M_2)=0.3, P(D|M_2)=0.02$
*   $P(M_3)=0.2, P(D|M_3)=0.05$

**Step 3: WIP State.**
Apply Law of Total Probability:
$P(D) = (0.5 \cdot 0.01) + (0.3 \cdot 0.02) + (0.2 \cdot ?)$

**Step 4: Final Calculation.**
$P(D) = 0.005 + 0.006 + 0.010 = 0.021$.
The probability is **2.1%**.

---

### Example 2: Medical Diagnostic Test (Bayes)
A disease affects 1% of the population. A test is 95% accurate for those with the disease (sensitivity) and 90% accurate for those without (specificity). If a person tests positive, what is the probability they have the disease?

**Step 1: Define events.**
*   $H$: Has disease. $P(H) = 0.01$.
*   $H^c$: Healthy. $P(H^c) = 0.99$.
*   $Pos$: Tests positive.

**Step 2: List conditionals.**
*   $P(Pos|H) = 0.95$
*   $P(Pos|H^c) = 1 - 0.90 = 0.10$ (False Positive)

**Step 3: WIP State.**
Calculate total probability of testing positive $P(Pos)$:
$P(Pos) = (0.95 \cdot 0.01) + (0.10 \cdot 0.99) = 0.0095 + ?$

**Step 4: Final Calculation.**
$P(Pos) = 0.1085$.
$P(H|Pos) = \frac{P(Pos|H)P(H)}{P(Pos)} = \frac{0.0095}{0.1085} \approx 0.0876$.
The probability is only **8.76%**.

---

### Example 3: Two Urns (Multi-stage)
Urn A has 2 Red and 3 Blue balls. Urn B has 4 Red and 1 Blue ball. A fair coin is flipped; if Heads, a ball is drawn from Urn A. If Tails, from Urn B. What is the probability a Red ball is drawn?

**Step 1: Define events.**
*   $H$: Heads (Urn A). $P(H) = 0.5$.
*   $T$: Tails (Urn B). $P(T) = 0.5$.
*   $R$: Red ball.

**Step 2: Find conditionals.**
*   $P(R|H) = 2/5 = 0.4$
*   $P(R|T) = 4/5 = 0.8$

**Step 3: WIP State.**
$P(R) = P(R|H)P(H) + P(R|T)P(T) = (0.4 \cdot 0.5) + ?$

**Step 4: Final Calculation.**
$P(R) = 0.2 + 0.4 = 0.6$.

---

### Example 4: Identifying the Urn (Bayes)
Using the setup from Example 3: If a Red ball was drawn, what is the probability it came from Urn B?

**Step 1: Use previous results.**
*   $P(R) = 0.6$
*   $P(R|T)P(T) = 0.4$

**Step 2: Apply Bayes' Theorem.**
$P(T|R) = \frac{P(R|T)P(T)}{P(R)}$

**Step 3: WIP State.**
$P(T|R) = \frac{0.4}{?}$

**Step 4: Final Calculation.**
$P(T|R) = \frac{0.4}{0.6} = \frac{2}{3} \approx 0.6667$.

---

### Example 5: Spam Filter
A spam filter finds that 90% of spam emails contain the word "Offer", while only 5% of non-spam emails contain it. 20% of all emails are spam. If an email contains "Offer", what is the probability it is spam?

**Step 1: Define events.**
*   $S$: Spam. $P(S) = 0.2$.
*   $O$: Contains "Offer".
*   $P(O|S) = 0.9, P(O|S^c) = 0.05$.

**Step 2: Total probability of "Offer".**
$P(O) = (0.9 \cdot 0.2) + (0.05 \cdot 0.8) = 0.18 + 0.04 = 0.22$.

**Step 3: WIP State.**
$P(S|O) = \frac{0.18}{?}$

**Step 4: Final Calculation.**
$P(S|O) = \frac{0.18}{0.22} \approx 0.8182$.

---

### Example 6: Witness Reliability
A taxi was involved in a hit-and-run accident at night. Two companies, Green and Blue, operate in the city. 85% of taxis are Green and 15% are Blue. A witness identifies the taxi as Blue. The court tests the witness and finds they correctly identify the color 80% of the time. What is the probability the taxi was actually Blue?

**Step 1: Define events.**
*   $B$: Taxi was Blue. $P(B) = 0.15$.
*   $G$: Taxi was Green. $P(G) = 0.85$.
*   $W_B$: Witness says "Blue".

**Step 2: Conditionals.**
*   $P(W_B|B) = 0.80$ (Correct)
*   $P(W_B|G) = 0.20$ (Incorrect - says Blue when it's Green)

**Step 3: WIP State.**
Total probability witness says Blue:
$P(W_B) = (0.80 \cdot 0.15) + (0.20 \cdot 0.85) = 0.12 + ?$

**Step 4: Final Calculation.**
$P(W_B) = 0.12 + 0.17 = 0.29$.
$P(B|W_B) = \frac{0.12}{0.29} \approx 0.4138$.
Despite the witness, it's more likely the taxi was Green (58.62%)!

---

### Example 7: Flight Delays
The probability that it is a holiday is 0.1. During holidays, the probability of a flight delay is 0.6. On non-holidays, the probability of delay is 0.2. What is the probability a flight is delayed?

**Step 1: Define events.**
*   $H$: Holiday. $P(H) = 0.1$.
*   $D$: Delayed.
*   $P(D|H) = 0.6, P(D|H^c) = 0.2$.

**Step 2: WIP State.**
$P(D) = (0.6 \cdot 0.1) + (0.2 \cdot ?)$

**Step 3: Final Calculation.**
$P(D) = 0.06 + 0.18 = 0.24$.

---

### Example 8: Supplier Quality
A company buys chips from two suppliers, X (70%) and Y (30%). 2% of X's chips are defective, and 1% of Y's are defective. A chip is found to be defective. What is the probability it came from supplier X?

**Step 1: Total Defect Probability.**
$P(D) = (0.02 \cdot 0.7) + (0.01 \cdot 0.3) = 0.014 + 0.003 = 0.017$.

**Step 2: Apply Bayes.**
$P(X|D) = \frac{P(D|X)P(X)}{P(D)}$

**Step 3: WIP State.**
$P(X|D) = \frac{0.014}{?}$

**Step 4: Final Calculation.**
$P(X|D) = \frac{0.014}{0.017} \approx 0.8235$.
There is an 82.35% chance it came from Supplier X.
