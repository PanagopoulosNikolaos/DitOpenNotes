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
