# **Discrete Mathematics Exam - Difficulty: HARD**


## **Topic 1. (2.5 points) - Propositional Logic**

Construct the truth table and determine whether the following formulas are tautologies, contradictions, or satisfiable:

**a.** (1.25 points) $((p \to q) \land (q \to r) \land (r \to s)) \to ((p \land \neg s) \to \bot)$

**b.** (1.25 points) $(((p \lor q) \to r) \land ((r \lor s) \to t)) \to ((p \land q \land \neg t) \to \bot)$

***

## **Topic 2. (1.5 points) - Set Theory**

In a survey of 500 participants, they were asked about their preferences in four music genres: Classical (C), Jazz (J), Rock (R), and Pop (P). The results showed:
- 180 prefer Classical
- 150 prefer Jazz  
- 200 prefer Rock
- 220 prefer Pop
- 65 prefer Classical and Jazz
- 80 prefer Classical and Rock
- 70 prefer Jazz and Rock
- 90 prefer Rock and Pop
- 85 prefer Classical and Pop
- 75 prefer Jazz and Pop
- 25 prefer Classical, Jazz and Rock
- 30 prefer Classical, Rock and Pop
- 20 prefer Jazz, Rock and Pop
- 35 prefer Classical, Jazz and Pop
- 15 prefer all four genres

Calculate how many participants prefer none of the four music genres.

***

## **Topic 3. (1.5 points) - Probability**

Consider the experiment of rolling three distinct fair 12-sided dice (d12).

**a.** (0.75 points) Calculate the probability that the sum of the three dice is a prime number greater than 25.

**b.** (0.75 points) Calculate the probability that exactly two of the three dice show a number that is a perfect square (1, 4, 9).

***

## **Topic 4. (1.5 points) - Bayes' Theorem**

A software company uses three different malware detection systems: A, B, and C. System A is used in 40% of cases, B in 35%, and C in 25%. The probability of a false positive diagnosis is 2% for system A, 4% for B, and 6% for C.

**a.** (0.75 points) Calculate the probability that a file is incorrectly diagnosed as malicious.

**b.** (0.75 points) Given that a file was incorrectly diagnosed as malicious, calculate the probability that system C was used.

***

## **Topic 5. (1 point) - Relations**

For the following relation on $S = \{1, 2, 3, 4, 5\}$:

$R = \{(1,1), (1,3), (2,2), (2,4), (3,1), (3,3), (3,5), (4,2), (4,4), (5,3), (5,5)\}$

**a.** (0.5 points) Check the validity of each of the properties: reflexive, symmetric, antisymmetric and transitive.

**b.** (0.5 points) Find the transitive closure $R^+$ of the relation $R$.

***

## **Topic 6. (2 points) - Graph Theory**

Consider the following graphs:

$G_1 = (V_1 = \{A, B, C, D, E, F, G\}, E_1 = \{(A,B), (B,C), (C,D), (D,E), (E,F), (F,G), (G,A), (A,D), (B,E), (C,F)\})$

$G_2 = (V_2 = \{1, 2, 3, 4, 5, 6, 7\}, E_2 = \{(1,2), (2,3), (3,4), (4,5), (5,6), (6,7), (7,1), (1,4), (2,5), (3,6)\})$

**a.** (1 point) Prove that the graphs $G_1$ and $G_2$ are isomorphic by finding an isomorphism.

**b.** (1 point) Find the chromatic number of $G_1$ and justify your answer by providing an optimal coloring.

***

## **Topic 7. (0.5 points) - Regular Expressions**

Write a regular expression that describes the set of strings over the alphabet $\{0,1,2\}$ that:
- Start with the symbol 1
- Contain at least one occurrence of the sequence "02"  
- End with an even number of 2 symbols

***

## **Topic 8. (0.5 points) - String Recognition**

For the regular expression $(a|b)^*c(a|b|c)^*$, determine which of the following strings belong to the regular set it describes:

`abcca`, `ccab`, `abab`, `cabcba`, `bacacc`, `abcdefg`

***

## **Topic 9. (1.5 points) - Mathematical Induction**

Show by mathematical induction that for every natural number $n \geq 1$ it holds:

$$\sum_{k=1}^{n} k \cdot k! = (n+1)! - 1$$

**Note:** Recall that $k! = k \cdot (k-1) \cdot (k-2) \cdot \ldots \cdot 2 \cdot 1$ and $0! = 1$.

***

**End of Exam**

*Total time: 4 hours*  
*Total points: 10*