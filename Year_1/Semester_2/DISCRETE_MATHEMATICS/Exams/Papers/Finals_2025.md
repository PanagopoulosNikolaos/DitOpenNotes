Department of Informatics and Telecommunications
University of Ioannina
Spyridon Tzimas
Spring Semester 2025

# 203: Discrete Mathematics
## June 2025 Exam

Your seat in this exam is uniquely identified by a label of the form $X - I J$ where $X$ is the name of the room and $I$ and $J$ are the row and column respectively to which the particular seat belongs. Your group is:

| $I \setminus J$ | even | odd |
| :--- | :--- | :--- |
| even | Group A | Group B |
| odd | Group C | Group D |

The grading value of the exam is 10 points. The duration of the exam is three hours. Only blue and black pens are allowed. Pencil is allowed only for writing on scrap paper.

Good Luck!

---

**Topic 1. (2 points)** Construct the truth table of the following propositional formulas.
a. (1 point) $((p \to q) \land ((?) \to q)) \to q$
b. (1 point) $p \to ((p \to (?)) \lor (p \to q))$

- **Group A:** (?) = $\neg p$
- **Group B:** (?) = $\neg q$
- **Group C:** (?) = $\top$
- **Group D:** (?) = $\bot$

**Note:** $\top$ and $\bot$ are not variables, they are always true and false respectively.

---

**Topic 2. (1 point)** The 256 participants of a survey were asked which colors they like among the three primary colors red, green and blue. Of these, 169 answered that they like red, 100 green, 64 blue, 49 red and green, 36 green and blue, (?) red and blue, and only 1 that they like all three. Calculate how many of the survey participants like none of the three primary colors.

- **Group A:** (?) = 4
- **Group B:** (?) = 9
- **Group C:** (?) = 16
- **Group D:** (?) = 25

---

**Topic 3. (1 point)** Consider the experiment of rolling two distinct fair $d(?)$.

- **Group A:** (?) = 4
- **Group B:** (?) = 8
- **Group C:** (?) = 12
- **Group D:** (?) = 20

**Explanation:** For $n \in \{4, 6, 8, 12, 20\}$, with $dn$ we denote the die with $n$ identical faces.

a. (0.5 points) Enumerate the possible outcomes of the form (even, odd).  
b. (0.5 points) Enumerate the possible outcomes that sum to a prime number.

**Note:** The prime numbers from 1 to 20 are $2, 3, 5, 7, 11, 13, 17, 19$.

---

**Topic 4. (1 point)** It has been experimentally measured that a person who has contracted a respiratory virus has a probability of $1/2$ of having contracted the influenza $A$ virus, $1/3$ of the influenza $B$ virus and $1/6$ of the coronavirus, denoted $C$. A test $T$ for respiratory viruses has a $2\%$ probability of a false negative result for the influenza $A$ virus, $3\%$ for the influenza $B$ virus and $(?)\%$ for the coronavirus.

- **Group A:** (?) = 6
- **Group B:** (?) = 12
- **Group C:** (?) = 18
- **Group D:** (?) = 24

a. (0.5 points) Calculate the probability of an incorrectly negative diagnosis using test $T$ of a person who has contracted a respiratory virus.

b. (0.5 points) Given that a person has been incorrectly diagnosed as negative using test $T$, calculate the probability that they have contracted the influenza $A$ virus.

---

**Topic 5. (1 point)** For the following relation on $S = \{1, 2, 3\}$, check the validity of each of the properties: reflexive, symmetric, antisymmetric and transitive.

- **Group A:** $R = \{(1, 1), (1, 2), (2, 1), (2, 2), (3, 3)\}$
- **Group B:** $R = \{(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)\}$
- **Group C:** $R = \{(1, 1), (1, 2), (2, 3), (3, 1), (3, 3)\}$
- **Group D:** $R = \{(1, 1), (1, 2), (2, 1), (2, 2), (2, 3), (3, 2)\}$

---

**Topic 6. (2 points)** Consider the following graphs:

$G_1 = (V_1 = \{A, B, C, D, E, F\}, E_1 = \{\{A, B\}, \{A, D\}, \{B, C\}, \{C, D\}, \{D, E\}, \{E, F\}, \{A, F\}, (?)\})$  
$G_2 = (V_2 = \{1, 2, 3, 4, 5, 6\}, E_2 = \{\{1, 2\}, \{2, 3\}, \{2, 5\}, \{3, 4\}, \{3, 6\}, \{4, 5\}, \{5, 6\}, \{1, 6\}\})$

- **Group A:** (?) = $\{B, E\}$
- **Group B:** (?) = $\{B, F\}$
- **Group C:** (?) = $\{C, E\}$
- **Group D:** (?) = $\{C, F\}$

a. (1 point) Show whether the graphs $G_1$ and $G_2$ are isomorphic.

b. (1 point) Show that the graph $G_1$ is planar and verify Euler's formula.

---

**Topic 7. (0.5 points)** Write a regular expression that describes the set of strings over the alphabet $\{0, 1\}$ that contain:

- **Group A:** at least 2 occurrences of 0
- **Group B:** exactly 3 occurrences of 1
- **Group C:** an even number of occurrences of 0
- **Group D:** an odd number of occurrences of 1

---

**Topic 8. (0.5 points)** Write which of the strings $bat, bit, bot, but, bait, boat, bout$ belong to the regular set described by the following regular expression.

- **Group A:** $b(\epsilon | a)(\epsilon | i)t$
- **Group B:** $bo(\epsilon | a | u)t$
- **Group C:** $b(\epsilon | o)a(\epsilon | i)t$
- **Group D:** $b(\epsilon | i)(\epsilon | o | u)t$

**Note:** With $\epsilon$ we denote the empty string.

---

**Topic 9. (1 point)** Show that for every $n \ge 0$ the following equality holds.

- **Group A:** $1 + 3 + 3^2 + \cdots + 3^n = \frac{3^{n+1} - 1}{2}$
- **Group B:** $1 + 5 + 5^2 + \cdots + 5^n = \frac{5^{n+1} - 1}{4}$
- **Group C:** $1 + 7 + 7^2 + \cdots + 7^n = \frac{7^{n+1} - 1}{6}$
- **Group D:** $1 + 11 + 11^2 + \cdots + 11^n = \frac{11^{n+1} - 1}{10}$

**Note:** For every non-zero number $a$, we define $a^0 = 1$ and $a^1 = a$.