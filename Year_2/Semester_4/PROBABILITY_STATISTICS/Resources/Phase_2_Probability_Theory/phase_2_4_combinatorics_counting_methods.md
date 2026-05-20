# Phase 2.4: Combinatorics and Counting Methods

Combinatorial analysis provides the mathematical techniques for counting the number of elements in a set without listing them individually. In probability theory, when outcomes in a sample space $\Omega$ are equally likely, the probability of an event $A$ is:

$$P(A) = \frac{|A|}{|\Omega|} = \frac{\text{Number of favorable outcomes}}{\text{Total number of possible outcomes}}$$

Determining $|A|$ and $|\Omega|$ often requires the counting methods detailed below.

---

## 1. Fundamental Principles of Counting

### 1.1 The Multiplication Rule (Product Rule)
If an operation can be performed in $n_1$ ways, and for each of these a second operation can be performed in $n_2$ ways, and for each of these a third operation can be performed in $n_3$ ways, and so on, then the sequence of $k$ operations can be performed in:

$$N = n_1 \cdot n_2 \cdot \dots \cdot n_k \text{ ways}$$

### 1.2 The Addition Rule (Sum Rule)
If an operation can be performed in $n_1$ ways, and a second disjoint operation can be performed in $n_2$ ways, then the total number of ways to perform either the first or the second operation is:

$$N = n_1 + n_2 \text{ ways}$$

---

## 2. Permutations

A permutation is an ordered arrangement of all or part of a set of objects. The order of selection matters.

### 2.1 Permutations of Distinct Objects
The number of permutations of $n$ distinct objects taken all at a time is:

$$P(n, n) = n!$$

The number of permutations of $n$ distinct objects taken $r$ at a time (where $0 \le r \le n$) is:

$$P(n, r) = \frac{n!}{(n-r)!}$$

### 2.2 Permutations with Repetition (Identical Objects)
The number of distinct permutations of $n$ objects of which $n_1$ are of one type, $n_2$ are of a second type, $\dots$, and $n_k$ are of a $k$-th type (such that $n_1 + n_2 + \dots + n_k = n$) is:

$$P(n; n_1, n_2, \dots, n_k) = \frac{n!}{n_1! \cdot n_2! \dots n_k!}$$

---

## 3. Combinations

A combination is a selection of all or part of a set of objects without regard to order. The order of selection does not matter.

### 3.1 Combinations of Distinct Objects (Without Replacement)
The number of combinations of $n$ distinct objects taken $r$ at a time (where $0 \le r \le n$) is given by the binomial coefficient:

$$C(n, r) = \binom{n}{r} = \frac{n!}{r!(n-r)!}$$

### 3.2 Combinations with Replacement
The number of ways to choose $r$ objects from a set of $n$ distinct objects when repetition is allowed (and order does not matter) is:

$$C^{R}(n, r) = \binom{n + r - 1}{r} = \frac{(n + r - 1)!}{r!(n - 1)!}$$

---

## 4. Partitions & Multinomial Coefficients

The number of ways of partitioning a set of $n$ distinct objects into $k$ cells with $r_1$ objects in the first cell, $r_2$ objects in the second cell, and so on, where $r_1 + r_2 + \dots + r_k = n$, is:

$$\binom{n}{r_1, r_2, \dots, r_k} = \frac{n!}{r_1! \cdot r_2! \dots r_k!}$$

---

## 5. Solved Exercises (10 Examples)

### Exercise 1: License Plate Codes (Multiplication Rule)
**Problem:** A license plate contains 3 letters followed by 3 digits. Letters cannot be repeated, but digits can. How many distinct license plates can be formed if there are 26 letters in the alphabet?

**Solution:**
- **Step 1: Define operations.**
  We have 6 slots to fill. Let $n_i$ represent the number of choices for slot $i$.
- **Step 2: WIP State.**
  For letters (no repetition):
  - Slot 1: 26 choices
  - Slot 2: 25 choices
  - Slot 3: 24 choices
  For digits (repetition allowed):
  - Slot 4: 10 choices (0-9)
  - Slot 5: 10 choices
  - Slot 6: ? choices
- **Step 3: Final Calculation.**
  - Slot 6 has 10 choices.
  - Total plates $= 26 \cdot 25 \cdot 24 \cdot 10 \cdot 10 \cdot 10 = 15,600 \cdot 1,000 = 15,600,000$.

---

### Exercise 2: Selecting a Committee (Combinations)
**Problem:** From a group of 8 men and 6 women, a committee of 5 people must be formed. How many committees are possible if it must contain exactly 3 men and 2 women?

**Solution:**
- **Step 1: Split the selections.**
  We select men and women independently, then multiply the results.
- **Step 2: WIP State.**
  - Selection of men: $\binom{8}{3} = \frac{8!}{3! \cdot 5!} = \frac{8 \cdot 7 \cdot 6}{3 \cdot 2 \cdot 1} = 56$.
  - Selection of women: $\binom{6}{2} = \frac{6!}{2! \cdot 4!} = \frac{6 \cdot 5}{?} = 15$.
- **Step 3: Final Calculation.**
  Total committees $= 56 \cdot 15 = 840$.

---

### Exercise 3: Arranging Books on a Shelf (Permutations)
**Problem:** There are 4 Math books, 3 Physics books, and 2 Chemistry books. In how many ways can they be arranged on a shelf if books of the same subject must be kept together?

**Solution:**
- **Step 1: Treat groups as units.**
  We arrange the 3 subjects (Math, Physics, Chemistry) first: $3!$ ways.
- **Step 2: WIP State.**
  Within each subject group:
  - Math books can be arranged in $4!$ ways.
  - Physics books can be arranged in $3!$ ways.
  - Chemistry books can be arranged in ? ways.
- **Step 3: Final Calculation.**
  - Chemistry arrangements $= 2! = 2$ ways.
  - Total arrangements $= 3! \cdot (4! \cdot 3! \cdot 2!) = 6 \cdot (24 \cdot 6 \cdot 2) = 6 \cdot 288 = 1728$.

---

### Exercise 4: Distributing Toys (Multinomial Coefficient)
**Problem:** In how many ways can 10 distinct toys be distributed among 3 children if the eldest receives 5 toys, the middle child receives 3 toys, and the youngest receives 2 toys?

**Solution:**
- **Step 1: Set up the partition.**
  This is a partition of $n=10$ objects into cells of sizes $r_1=5, r_2=3, r_3=2$.
- **Step 2: WIP State.**
  $$\binom{10}{5, 3, 2} = \frac{10!}{5! \cdot 3! \cdot 2!} = \frac{10 \cdot 9 \cdot 8 \cdot 7 \cdot 6 \cdot 5!}{5! \cdot (3 \cdot 2 \cdot 1) \cdot (2 \cdot 1)} = \frac{10 \cdot 9 \cdot 8 \cdot 7 \cdot 6}{?}$$
- **Step 3: Final Calculation.**
  $$\text{Denominator} = 6 \cdot 2 = 12$$
  $$\text{Numerator} = 30240$$
  $$\text{Total ways} = \frac{30240}{12} = 2520 \text{ ways}.$$

---

### Exercise 5: Word Permutations with Repetition
**Problem:** How many distinct words (including nonsense words) can be formed by rearranging the letters of the word "PROBABILITY"?

**Solution:**
- **Step 1: Count letter frequencies.**
  Total letters $n = 11$.
  Frequencies: P (1), R (1), O (1), B (2), A (1), I (2), L (1), T (1), Y (1).
- **Step 2: WIP State.**
  We apply the permutation of identical objects formula:
  $$\text{Total permutations} = \frac{11!}{1! \cdot 1! \cdot 1! \cdot 2! \cdot 1! \cdot 2! \cdot 1! \cdot 1! \cdot 1!} = \frac{11!}{2! \cdot 2!} = \frac{39,916,800}{?}$$
- **Step 3: Final Calculation.**
  $$\text{Total permutations} = \frac{39,916,800}{4} = 9,979,200 \text{ words}.$$

---

### Exercise 6: Seating Arrangements at a Round Table
**Problem:** In how many ways can 6 people be seated at a round table? (Note: Two arrangements are considered identical if each person has the same left and right neighbors).

**Solution:**
- **Step 1: Identify circular permutation.**
  For circular permutations of $n$ distinct objects, we fix one person's position to eliminate rotational equivalence, leaving $(n-1)!$ arrangements.
- **Step 2: WIP State.**
  $$\text{Arrangements} = (6 - 1)! = ?!$$
- **Step 3: Final Calculation.**
  $$5! = 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1 = 120 \text{ ways}.$$

---

### Exercise 7: Choosing Donuts (Combinations with Replacement)
**Problem:** A bakery sells 4 varieties of donuts. In how many ways can a customer select 6 donuts?

**Solution:**
- **Step 1: Identify model parameters.**
  We are selecting $r = 6$ donuts from $n = 4$ types, where order does not matter and repetition is allowed.
- **Step 2: WIP State.**
  Use the combination with replacement formula:
  $$\binom{n + r - 1}{r} = \binom{4 + 6 - 1}{6} = \binom{9}{6} = \frac{9!}{6! \cdot 3!} = \frac{9 \cdot 8 \cdot 7}{?}$$
- **Step 3: Final Calculation.**
  $$\text{Denominator} = 3 \cdot 2 \cdot 1 = 6$$
  $$\text{Total ways} = \frac{504}{6} = 84 \text{ ways}.$$

---

### Exercise 8: Pathfinding on a Grid
**Problem:** A grid has coordinates from $(0,0)$ to $(5,4)$. A path moves only step-by-step to the right or up. How many paths exist from $(0,0)$ to $(5,4)$?

**Solution:**
- **Step 1: Translate to symbols.**
  Any path requires exactly 5 Right (R) moves and 4 Up (U) moves, totaling $n = 9$ moves.
- **Step 2: WIP State.**
  We need to choose which 5 of the 9 moves are R (the rest will be U):
  $$\text{Paths} = \binom{9}{5} = \frac{9!}{5! \cdot 4!} = \frac{9 \cdot 8 \cdot 7 \cdot 6}{?}$$
- **Step 3: Final Calculation.**
  $$\text{Denominator} = 4 \cdot 3 \cdot 2 \cdot 1 = 24$$
  $$\text{Total paths} = \frac{3024}{24} = 126 \text{ paths}.$$

---

### Exercise 9: Sum of Dice (Combinatorics for Probability)
**Problem:** Three fair six-sided dice are rolled. What is the probability that the sum of the numbers shown is exactly 5?

**Solution:**
- **Step 1: Calculate the size of the sample space $|\Omega|$.**
  Each die has 6 outcomes. For 3 dice: $|\Omega| = 6^3 = 216$.
- **Step 2: WIP State.**
  We count the combinations of $(x_1, x_2, x_3)$ such that $x_1 + x_2 + x_3 = 5$, where $1 \le x_i \le 6$.
  Possible partitions of 5 into 3 positive integers:
  - $\{3, 1, 1\}$ (order matters): can occur as $(3,1,1)$, $(1,3,1)$, or $(1,1,3)$ $\Rightarrow$ 3 ways.
  - $\{2, 2, 1\}$ (order matters): can occur as $(2,2,1)$, $(2,1,2)$, or $(1,2,2)$ $\Rightarrow$ ? ways.
- **Step 3: Final Calculation.**
  - There are 3 ways for $\{2, 2, 1\}$.
  - Total favorable outcomes $|A| = 3 + 3 = 6$.
  - Probability $= \frac{|A|}{|\Omega|} = \frac{6}{216} = \frac{1}{36} \approx 0.0278$.

---

### Exercise 10: Standard Poker Hands (Combination)
**Problem:** A standard poker deck has 52 cards. What is the probability of being dealt a "Four of a Kind" (4 cards of one rank, and 1 card of another rank) in a 5-card hand?

**Solution:**
- **Step 1: Compute total hands.**
  $$|\Omega| = \binom{52}{5} = 2,598,960$$
- **Step 2: WIP State.**
  To get a Four of a Kind:
  1. Choose the rank of the four cards: $\binom{13}{1} = 13$ ways.
  2. Select all 4 cards of that rank: $\binom{4}{4} = 1$ way.
  3. Choose the remaining card from the remaining cards: $\binom{48}{1} = ?$ ways.
- **Step 3: Final Calculation.**
  - $\binom{48}{1} = 48$ ways.
  - Total favorable hands $|A| = 13 \cdot 1 \cdot 48 = 624$.
  - Probability $= \frac{624}{2,598,960} \approx 0.00024$.
