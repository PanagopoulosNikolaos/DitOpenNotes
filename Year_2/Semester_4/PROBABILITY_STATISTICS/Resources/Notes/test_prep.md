# Test Prep: Practice Questions for the Probability & Statistics Exams (405)

Each unit corresponds to a section of `Complete_Exam_Theory_Guide.md`. Each question is of exam type (as in the real exam papers 2023–2026) and is accompanied by the necessary formula in note form.

---

## Unit 1: Probability Theory & Axioms (Classical Definition)

### Question 1.1
A box contains 10 red, 15 blue, and 5 green balls. We select one ball at random. Find the probability that the ball is blue.

> **Formula:**
> $$P(A) = \frac{N(A)}{N(\Omega)}$$

### Question 1.2
We roll two dice simultaneously. Find the probability that the sum of the outcomes is 7.

> **Formula:**
> $$P(A) = \frac{N(A)}{N(\Omega)}$$

### Question 1.3
For an event $A$ we have $P(A) = 0.3$. Compute the probability of the complementary event $A'$.

> **Formula:**
> $$P(A') = 1 - P(A)$$

### Question 1.4
In a class of 50 students, 30 are girls. We select a student at random. Find the probability that it is a boy.

> **Formula:**
> $$P(A) = \frac{N(A)}{N(\Omega)}, \quad P(A') = 1 - P(A)$$

### Question 1.5
We toss a coin three times. Find the probability of getting at least one heads.

> **Formula:**
> $$P(A') = 1 - P(A)$$

### Question 1.6
From a deck of 52 cards we draw one card at random. Find the probability that it is an ace.

> **Formula:**
> $$P(A) = \frac{N(A)}{N(\Omega)}$$

### Question 1.7
Two disjoint events $A$, $B$ are given with $P(A) = 0.5$ and $P(B) = 0.4$. Check whether it is possible that $P(A \cup B) = 0.7$. Justify your answer.

> **Formula:**
> If $A \cap B = \emptyset$: $P(A \cup B) = P(A) + P(B)$
> It must always hold: $P(A \cup B) \le 1$

### Question 1.8
We roll a die. Find the probability of getting an even number or a number greater than 4.

> **Formula:**
> $$P(A \cup B) = \frac{N(A \cup B)}{N(\Omega)}$$

### Question 1.9
A container holds 3 white and 7 black balls. We take 2 balls at the same time. Find the probability that both are white.

> **Formula:**
> $$P(A) = \frac{N(A)}{N(\Omega)}, \quad N(A) = \binom{3}{2}, \quad N(\Omega) = \binom{10}{2}$$

### Question 1.10
$P(A) = 0.6$ and $P(A \cap B) = 0.2$ are given. Find the probability that $A$ occurs but not $B$, i.e., $P(A \cap B')$.

> **Formula:**
> $$P(A \cap B') = P(A) - P(A \cap B)$$

---

## Unit 2: Event Operations & Identities (Union, Intersection, De Morgan)

### Question 2.1
In a survey, 30% of respondents read newspaper A, 25% read newspaper B, and 10% read both. We select a person at random. Find the probability that they read at least one of the two newspapers.

> **Formula:**
> $$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

### Question 2.2
Using the data of Question 2.1, find the probability that a random person reads only newspaper A.

> **Formula:**
> $$P(A \cap B') = P(A) - P(A \cap B)$$

### Question 2.3
Using the data of Question 2.1, find the probability that a random person reads neither of the two newspapers.

> **Formula:**
> $$P(A' \cap B') = 1 - P(A \cup B) \quad \text{(De Morgan's Law)}$$

### Question 2.4
Using the data of Question 2.1, find the probability that a random person reads both newspapers.

> **Formula:**
> $$P(A \cap B) = P(A) + P(B) - P(A \cup B)$$

### Question 2.5
Using the data of Question 2.1, find the probability that a random person reads exactly one of the two newspapers.

> **Formula:**
> $$P(\text{exactly one}) = P(A) + P(B) - 2P(A \cap B)$$

### Question 2.6
$P(A) = 0.5$, $P(B) = 0.4$ and $P(A \cup B) = 0.8$ are given. Compute $P(A \cap B)$.

> **Formula:**
> $$P(A \cap B) = P(A) + P(B) - P(A \cup B)$$

### Question 2.7
$P(A) = 0.6$ and $P(A \cap B) = 0.15$ are given. Compute $P(A \cap B')$.

> **Formula:**
> $$P(A \cap B') = P(A) - P(A \cap B)$$

### Question 2.8
$P(B) = 0.7$ and $P(A \cap B) = 0.2$ are given. Compute $P(B \cap A')$, i.e., the probability that $B$ occurs but not $A$.

> **Formula:**
> $$P(B \cap A') = P(B) - P(A \cap B)$$

### Question 2.9
$P(A \cup B) = 0.75$ is given. Compute the probability that neither of the two events occurs.

> **Formula:**
> $$P(A' \cap B') = 1 - P(A \cup B) \quad \text{(De Morgan's Law)}$$

### Question 2.10
If $A \subseteq B$, with $P(B) = 0.8$ and $P(A) = 0.3$, compute $P(B \setminus A) = P(B \cap A')$.

> **Formula:**
> If $A \subseteq B$: $P(B \setminus A) = P(B) - P(A)$ and $P(A) \le P(B)$

---

## Unit 3: Conditional Probability & Independence

### Question 3.1
$P(A \cap B) = 0.12$ and $P(B) = 0.4$ are given. Compute the conditional probability $P(A \mid B)$.

> **Formula:**
> $$P(A \mid B) = \frac{P(A \cap B)}{P(B)}, \quad P(B) > 0$$

### Question 3.2
In a department, 60% of students know the C language, 70% know Java, and 50% know both. We select a student at random. Given that they know C, find the probability that they also know Java.

> **Formula:**
> $$P(A \mid B) = \frac{P(A \cap B)}{P(B)}$$

### Question 3.3
Events $A$ and $B$ are independent with $P(A) = 0.5$ and $P(B) = 0.3$. Compute $P(A \cap B)$.

> **Formula:**
> If $A$, $B$ independent: $P(A \cap B) = P(A) \cdot P(B)$

### Question 3.4
Events $A$ and $B$ are independent with $P(A) = 0.4$ and $P(B) = 0.5$. Compute $P(A \cup B)$.

> **Formula:**
> If $A$, $B$ independent: $P(A \cup B) = P(A) + P(B) - P(A)P(B)$

### Question 3.5
$P(A) = 0.2$, $P(B) = 0.3$ and $P(A \cap B) = 0.06$ are given. Examine whether events $A$ and $B$ are independent.

> **Formula:**
> Independent if $P(A \cap B) = P(A) \cdot P(B)$. Disjoint if $P(A \cap B) = 0$.

### Question 3.6
$P(A \mid B) = 0.4$ and $P(B) = 0.3$ are given. Compute $P(A \cap B)$ using the multiplication rule.

> **Formula:**
> $$P(A \cap B) = P(A \mid B) \cdot P(B)$$

### Question 3.7
$P(A) = 0.6$, $P(B) = 0.4$ and $P(A \cap B) = 0.24$ are given. Compute $P(B \mid A)$ and examine whether $A$ and $B$ are independent.

> **Formula:**
> $$P(B \mid A) = \frac{P(A \cap B)}{P(A)}$$
> Independent if $P(B \mid A) = P(B)$ (or $P(A \cap B) = P(A)P(B)$).

### Question 3.8
$P(A) = 0.7$ and $P(A \cap B) = 0.21$ are given. Compute the conditional probability $P(B \mid A')$.

> **Formula:**
> $$P(B \mid A') = \frac{P(B \cap A')}{P(A')} = \frac{P(B) - P(A \cap B)}{1 - P(A)}$$

### Question 3.9
$P(A) = 0.3$ and $P(B) = 0.6$ are given with $A \cap B = \emptyset$. Examine whether $A$ and $B$ can be independent. Justify your answer.

> **Formula:**
> Disjoint: $P(A \cap B) = 0$. Independent: $P(A \cap B) = P(A)P(B)$.
> Disjoint events with $P(A), P(B) > 0$ are never independent.

### Question 3.10
$P(B \mid A') = 0.5$ and $P(A') = 0.4$ are given. Compute $P(B \cap A')$.

> **Formula:**
> $$P(B \cap A') = P(B \mid A') \cdot P(A')$$

---

## Unit 4: Total Probability & Bayes' Formula

### Question 4.1
A factory has three machines M1, M2, M3. M1 produces 50% of the products with 2% defective, M2 produces 30% with 3% defective, and M3 produces 20% with 4% defective. We select a product at random. Find the probability that it is defective.

> **Formula:**
> $$P(B) = \sum_{k=1}^{n} P(B \mid A_k) P(A_k)$$

### Question 4.2
Using the data of Question 4.1, given that the selected product is defective, find the probability that it came from machine M1.

> **Formula:**
> $$P(A_i \mid B) = \frac{P(B \mid A_i) P(A_i)}{\sum_{k=1}^{n} P(B \mid A_k) P(A_k)}$$

### Question 4.3
We have two urns. Urn A contains 3 white and 4 black balls, while urn B contains 5 white and 2 black. We toss a coin to choose an urn and then draw one ball. Find the probability that the ball is white.

> **Formula:**
> $$P(B) = \sum_{k=1}^{n} P(B \mid A_k) P(A_k)$$

### Question 4.4
Using the data of Question 4.3, given that the ball drawn is white, find the probability that urn A was chosen.

> **Formula:**
> $$P(A_i \mid B) = \frac{P(B \mid A_i) P(A_i)}{\sum_{k=1}^{n} P(B \mid A_k) P(A_k)}$$

### Question 4.5
1% of the population suffers from a disease. A test is positive with probability 95% if the person has the disease and positive with probability 2% if they do not. Find the probability that a random person has a positive result.

> **Formula:**
> $$P(B) = \sum_{k=1}^{n} P(B \mid A_k) P(A_k)$$

### Question 4.6
Using the data of Question 4.5, given that a person has a positive result, find the probability that they actually have the disease.

> **Formula:**
> $$P(A_i \mid B) = \frac{P(B \mid A_i) P(A_i)}{\sum_{k=1}^{n} P(B \mid A_k) P(A_k)}$$

### Question 4.7
Events $A_1$, $A_2$ form a partition of the sample space with $P(A_1) = 0.6$, $P(B \mid A_1) = 0.3$ and $P(B \mid A_2) = 0.4$. Compute $P(B)$.

> **Formula:**
> $$P(B) = P(B \mid A_1) P(A_1) + P(B \mid A_2) P(A_2)$$

### Question 4.8
Using the data of Question 4.7, compute the conditional probability $P(A_1 \mid B)$.

> **Formula:**
> $$P(A_1 \mid B) = \frac{P(B \mid A_1) P(A_1)}{P(B)}$$

### Question 4.9
40% of students read the course notes. Of those who read, 80% pass the course, while of the remaining only 50% pass. Find the probability that a random student passes the course.

> **Formula:**
> $$P(B) = P(B \mid A) P(A) + P(B \mid A') P(A')$$

### Question 4.10
Using the data of Question 4.9, given that a student passed the course, find the probability that they had read the notes.

> **Formula:**
> $$P(A \mid B) = \frac{P(B \mid A) P(A)}{P(B)}$$

---

## Unit 5: Parametric Probability Exercises

### Question 5.1
If $P(A) = a$, $P(B) = 0.4$ and $P(A \cup B) = 0.6$, find $a$ when $A$ and $B$ are disjoint events.

> **Formula:**
> Disjoint: $P(A \cup B) = P(A) + P(B) \implies a = P(A \cup B) - P(B)$

### Question 5.2
If $P(A) = a$, $P(B) = 0.4$ and $P(A \cup B) = 0.6$, find $a$ when $A$ and $B$ are independent events.

> **Formula:**
> Independent: $P(A \cup B) = a + b - ab \implies a = \frac{P(A \cup B) - b}{1 - b}$

### Question 5.3
If $P(A) = a$, $P(B) = 0.4$ and $P(A \cup B) = 0.6$, find $a$ when $B \subset A$.

> **Formula:**
> If $B \subset A$: $P(A \cup B) = P(A) = a$

### Question 5.4
If $P(A) = 0.2$, $P(B) = b$ and $A$, $B$ are disjoint with $P(A \cup B) = 0.5$, find $b$.

> **Formula:**
> Disjoint: $P(A \cup B) = P(A) + P(B) \implies b = P(A \cup B) - P(A)$

### Question 5.5
If $P(A) = a$, $P(B) = 0.3$, $A$ and $B$ are independent and $P(A \cup B) = 0.58$, find $a$.

> **Formula:**
> Independent: $P(A \cup B) = a + b - ab \implies a = \frac{P(A \cup B) - b}{1 - b}$

### Question 5.6
If $P(A) = 0.25$, $P(B) = b$ and $B \subset A$ with $P(A \cup B) = 0.25$, what do you conclude about $b$? Justify your answer.

> **Formula:**
> If $B \subset A$: $P(A \cup B) = P(A)$ and $P(B) \le P(A)$

### Question 5.7
$A$ and $B$ are independent with $P(A) = 0.3$ and $P(B) = 0.5$. Compute $P(A \cup B)$ and $P(A \cap B')$.

> **Formula:**
> $$P(A \cup B) = P(A) + P(B) - P(A)P(B)$$
> $$P(A \cap B') = P(A) - P(A \cap B)$$

### Question 5.8
$P(A \cup B) = 0.7$, $P(A \cap B) = 0.1$ and $P(B) = 0.5$ are given. Compute $P(A)$.

> **Formula:**
> $$P(A \cup B) = P(A) + P(B) - P(A \cap B) \implies P(A) = P(A \cup B) - P(B) + P(A \cap B)$$

### Question 5.9
$A$ and $B$ are disjoint with $P(A) = 0.4$ and $P(B) = 0.3$. Compute $P(A \cup B)$ and $P(A' \cap B')$.

> **Formula:**
> Disjoint: $P(A \cup B) = P(A) + P(B)$
> $$P(A' \cap B') = 1 - P(A \cup B)$$

### Question 5.10
$P(A) = a$, $P(B) = 0.6$ and $P(A \cup B) = 0.8$ are given. For which value of $a$ are the events disjoint?

> **Formula:**
> Disjoint: $P(A \cup B) = P(A) + P(B) \implies a = P(A \cup B) - P(B)$

---

## Unit 6: Data Organization & Frequency Tables

### Question 6.1
A grouping table is given with classes $[0, 10)$, $[10, 20)$, $[20, 30)$ and frequencies $f_i = 5, 12, 8$ respectively. Find the midpoints $x_i$ of each class.

> **Formula:**
> $$x_i = \frac{L_i + U_i}{2}$$

### Question 6.2
Using the data of Question 6.1, complete the column $f_i x_i$ and compute $\sum f_i x_i$.

> **Formula:**
> $$f_i x_i = f_i \cdot \frac{L_i + U_i}{2}, \quad \sum_{i=1}^{k} f_i x_i$$

### Question 6.3
Using the data of Question 6.1, compute the relative frequencies $h_i$ of each class.

> **Formula:**
> $$h_i = \frac{f_i}{N}, \quad N = \sum_{i=1}^{k} f_i, \quad \sum_{i=1}^{k} h_i = 1$$

### Question 6.4
Using the data of Question 6.1, compute the cumulative frequencies $F_i$.

> **Formula:**
> $$F_i = \sum_{j=1}^{i} f_j = F_{i-1} + f_i, \quad F_k = N$$

### Question 6.5
Using the data of Question 6.1, compute the cumulative relative frequencies $H_i$.

> **Formula:**
> $$H_i = \frac{F_i}{N} = \sum_{j=1}^{i} h_j, \quad H_k = 1$$

### Question 6.6
The completion time of a task for 20 workers was grouped into the classes $[0,5)$, $[5,10)$, $[10,15)$ with frequencies $4, 10, 6$. In which class is the median located?

> **Formula:**
> Find the class with $F_{i-1} < \frac{N}{2} \le F_i$

### Question 6.7
A table is given with classes $[20, 25)$, $[25, 30)$, $[30, 35)$ and frequencies $10, 22, 50$. Determine the class width $\delta$ and the midpoints $x_i$.

> **Formula:**
> $$\delta = U_i - L_i, \quad x_i = \frac{L_i + U_i}{2}$$

### Question 6.8
For grouped data of 100 observations, the cumulative frequencies $F_3 = 45$ and $F_4 = 70$ are given. Find the percentage of observations located in the first two classes.

> **Formula:**
> $$h = \frac{f}{N}, \quad f = F_k - F_{k-1}$$

### Question 6.9
In a table with 5 classes the frequencies are $f_1 = 8$, $f_2 = 12$, $f_3 = 20$, $f_4 = 15$, $f_5 = 5$. Compute the relative frequency of the third class.

> **Formula:**
> $$h_i = \frac{f_i}{N}, \quad N = \sum f_i$$

### Question 6.10
A partially completed table is given with classes $[0,4)$, $[4,8)$, $[8,12)$, $[12,16)$ and frequencies $30, 60, 70, 40$. Fully complete the columns $x_i$, $f_i x_i$, $F_i$.

> **Formula:**
> $$x_i = \frac{L_i + U_i}{2}, \quad f_i x_i, \quad F_i = F_{i-1} + f_i$$

---

## Unit 7: Measures of Central Tendency (Mean, Median, Quartiles, Mode)

### Question 7.1
The heights of 11 students are: 160, 162, 168, 168, 170, 173, 175, 178, 182, 185, 186 (in cm). Compute the average height $\bar{x}$.

> **Formula:**
> $$\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i$$

### Question 7.2
Using the data of Question 7.1, compute the median $M$.

> **Formula:**
> Ordered data. If $n$ is odd: $M = x_{\left(\frac{n+1}{2}\right)}$.

### Question 7.3
Using the data of Question 7.1, compute the third quartile $Q_3$ for discrete data.

> **Formula:**
> $Q_3$: the value at position $\frac{3(n+1)}{4}$ of the ordered series (or with the median-of-the-upper-half convention).

### Question 7.4
Using the data of Question 7.1, find the mode $T$.

> **Formula:**
> Mode: the value with the highest frequency of occurrence.

### Question 7.5
The monthly salary of 180 employees is given in the table:
| Salary | $f_i$ |
|---|---|
| 1250 | 22 |
| 1300 | 35 |
| 1550 | 65 |
| 1800 | 38 |
| 2000 | 20 |

Compute the average monthly salary.

> **Formula:**
> $$\bar{x} = \frac{1}{N} \sum_{i=1}^{k} f_i x_i$$

### Question 7.6
Using the data of Question 7.5, compute the median $M$. (The salary is given as a single value, not an interval.)

> **Formula:**
> Find the class with $F_{i-1} < \frac{N}{2} \le F_i$ and apply linear interpolation:
> $$M = L_i + \frac{\delta}{f_i}\left(\frac{N}{2} - F_{i-1}\right)$$

### Question 7.7
Using the data of Question 7.5, compute the first quartile $Q_1$ (boundary for the lowest 25%).

> **Formula:**
> Find the class with $F_{i-1} < \frac{1 \cdot N}{4} \le F_i$:
> $$Q_1 = L_i + \frac{\delta}{f_i}\left(\frac{N}{4} - F_{i-1}\right)$$

### Question 7.8
The completion time of an online purchase for 200 users is given in the table:
| Time | $f_i$ |
|---|---|
| [0,4) | 30 |
| [4,8) | 60 |
| [8,12) | 70 |
| [12,16) | 40 |

The company wants to improve the platform for the 25% of users with the longest time. Find the time boundary.

> **Formula:**
> The boundary is $Q_3$: class with $F_{i-1} < \frac{3N}{4} \le F_i$:
> $$Q_3 = L_i + \frac{\delta}{f_i}\left(\frac{3N}{4} - F_{i-1}\right)$$

### Question 7.9
A grouped data table is given with classes $[0,10)$, $[10,20)$, $[20,30)$, $[30,40)$ and frequencies $5, 15, 20, 10$. Compute the mode $T$.

> **Formula:**
> $$T = L_i + \delta \frac{\Delta_1}{\Delta_1 + \Delta_2}$$
> where $\Delta_1 = f_i - f_{i-1}$ and $\Delta_2 = f_i - f_{i+1}$ for the class with the largest $f_i$.

### Question 7.10
A frequency table is given:
| Class | $f_i$ |
|---|---|
| [10, 20) | 8 |
| [20, 30) | 12 |
| [30, 40) | 20 |
| [40, 50) | 10 |

Compute the mean $\bar{x}$, the median $M$, and $Q_1$.

> **Formula:**
> $$\bar{x} = \frac{\sum f_i x_i}{N}$$
> $$M = L_i + \frac{\delta}{f_i}\left(\frac{N}{2} - F_{i-1}\right), \quad Q_1 = L_i + \frac{\delta}{f_i}\left(\frac{N}{4} - F_{i-1}\right)$$

---

## Unit 8: Measures of Dispersion (Variance, Standard Deviation, CV)

### Question 8.1
The data 2, 4, 6, 8, 10 are given. Compute the sample variance $s^2$.

> **Formula:**
> $$s^2 = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2$$

### Question 8.2
Using the data of Question 8.1, compute the standard deviation $s$.

> **Formula:**
> $$s = \sqrt{s^2}$$

### Question 8.3
For grouped data of 120 workers, $\sum f_i (x_i - \bar{x})^2 = 3242.5$ is given. Compute the variance and the standard deviation.

> **Formula:**
> $$s^2 = \frac{1}{N-1} \sum_{i=1}^{k} f_i (x_i - \bar{x})^2, \quad s = \sqrt{s^2}$$

### Question 8.4
$\bar{x} = 50$ and $s = 5$ are given. Compute the coefficient of variation $CV$ as a percentage.

> **Formula:**
> $$CV = \frac{s}{\bar{x}}, \quad CV\% = \frac{s}{\bar{x}} \cdot 100\%$$

### Question 8.5
Group A: $\bar{x} = 100$, $s = 10$. Group B: $\bar{x} = 80$, $s = 12$. Which group exhibits greater relative variability?

> **Formula:**
> Compare using $CV = \frac{s}{\bar{x}}$ (a dimensionless measure).

### Question 8.6
$s^2 = 16$ is given. Compute the standard deviation $s$.

> **Formula:**
> $$s = \sqrt{s^2}$$

### Question 8.7
Department A: $\bar{x} = 70$, $s = 5$. Department B: $\bar{x} = 65$, $s = 4$. Which department has greater homogeneity of grades? Justify using the $CV$.

> **Formula:**
> $$CV = \frac{s}{\bar{x}}$$ — a smaller $CV$ means greater homogeneity.

### Question 8.8
A grouped data table is given with column $f_i (x_i - \bar{x})^2$ and total $\sum f_i (x_i - \bar{x})^2 = 137188$, with $N = 300$. Compute the standard deviation.

> **Formula:**
> $$s = \sqrt{\frac{\sum f_i (x_i - \bar{x})^2}{N-1}}$$

### Question 8.9
The data 3, 3, 5, 7, 9 are given. Compute the variance using the shortcut formula $\sum x_i^2 - n\bar{x}^2$.

> **Formula:**
> $$s^2 = \frac{1}{n-1}\left[\sum_{i=1}^{n} x_i^2 - n \bar{x}^2\right]$$

### Question 8.10
For 10 observations, $\sum x_i = 100$ and $\sum x_i^2 = 1200$ are given. Compute $\bar{x}$ and the sample standard deviation $s$.

> **Formula:**
> $$\bar{x} = \frac{\sum x_i}{n}, \quad s^2 = \frac{1}{n-1}\left[\sum x_i^2 - n \bar{x}^2\right]$$

---

## Unit 9: Empirical Rule (68-95-99.7)

### Question 9.1
A variable approximately follows a normal distribution with $\bar{x} = 100$ and $s = 10$. In which interval is 68% of the values expected to lie?

> **Formula:**
> $$[\bar{x} - s, \; \bar{x} + s]$$

### Question 9.2
Using the data of Question 9.1, in which interval is 95% of the values expected to lie?

> **Formula:**
> $$[\bar{x} - 2s, \; \bar{x} + 2s]$$

### Question 9.3
Using the data of Question 9.1, in which interval is 99.7% of the values expected to lie?

> **Formula:**
> $$[\bar{x} - 3s, \; \bar{x} + 3s]$$

### Question 9.4
For a symmetric bell-shaped distribution, what percentage of the values lies within the interval $[\bar{x} - 2s, \; \bar{x} + 2s]$?

> **Formula:**
> Empirical rule: approximately 95% lies within $\bar{x} \pm 2s$.

### Question 9.5
The lifetime of a battery has $\bar{x} = 48$ hours and $s = 4$ hours. What percentage of batteries has a lifetime between 40 and 56 hours?

> **Formula:**
> $40 = 48 - 2 \cdot 4$ and $56 = 48 + 2 \cdot 4$ → interval $\bar{x} \pm 2s$ → 95%.

### Question 9.6
Using the data of Question 9.5, what percentage of batteries has a lifetime between 44 and 52 hours?

> **Formula:**
> $44 = 48 - 4$ and $52 = 48 + 4$ → interval $\bar{x} \pm s$ → 68%.

### Question 9.7
The score in a competition has $\bar{x} = 60$ and $s = 8$. Find the interval that contains approximately 95% of the scores.

> **Formula:**
> $$[\bar{x} - 2s, \; \bar{x} + 2s]$$

### Question 9.8
For a bell-shaped distribution, 95% of the values lies in the interval $[50, 70]$. Find $\bar{x}$ and $s$.

> **Formula:**
> $\bar{x} = \frac{70 + 50}{2}$, $2s = \frac{70 - 50}{2}$ → $s = 5$.

### Question 9.9
Using the $\bar{x}$ and $s$ you found in Question 9.8, find the interval for 68% of the values.

> **Formula:**
> $$[\bar{x} - s, \; \bar{x} + s]$$

### Question 9.10
The completion time has $\bar{x} = 30$ minutes and $s = 5$ minutes. In which interval is almost the entire set (99.7%) of the times expected to lie?

> **Formula:**
> $$[\bar{x} - 3s, \; \bar{x} + 3s]$$

---

## Unit 10: Discrete Random Variables (PMF, CDF, Expected Value, Variance)

### Question 10.1
The probability distribution of the discrete r.v. $X$ is given:
| $x$ | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| $P(X=x)$ | 0.2 | 0.3 | 0.4 | 0.1 |

Examine whether it is a valid probability mass function.

> **Formula:**
> A valid PMF if $0 \le p(x_i) \le 1$ and $\sum_{i} p(x_i) = 1$.

### Question 10.2
Using the data of Question 10.1, compute the expected value $E[X]$.

> **Formula:**
> $$E[X] = \sum_{i} x_i \cdot P(X = x_i)$$

### Question 10.3
Using the data of Question 10.1, compute the variance $\text{Var}(X)$ and the standard deviation $\sigma$.

> **Formula:**
> $$\text{Var}(X) = E[X^2] - (E[X])^2, \quad \sigma = \sqrt{\text{Var}(X)}$$

### Question 10.4
We roll a die and let $X$ be the outcome. Compute $E[X]$.

> **Formula:**
> $$E[X] = \sum_{i=1}^{6} x_i \cdot \frac{1}{6}$$

### Question 10.5
For a discrete r.v. $X$, $E[X] = 5$ and $E[X^2] = 30$ are given. Compute $\text{Var}(X)$.

> **Formula:**
> $$\text{Var}(X) = E[X^2] - (E[X])^2$$

### Question 10.6
Using the data of Question 10.1, compute the cumulative function $F(2) = P(X \le 2)$.

> **Formula:**
> $$F(x) = P(X \le x) = \sum_{x_i \le x} p(x_i)$$

### Question 10.7
$E[X] = 4$ and $\text{Var}(X) = 9$ are given. Compute $E[2X + 3]$ and $\text{Var}(2X + 3)$.

> **Formula:**
> $$E[aX + b] = aE[X] + b, \quad \text{Var}(aX + b) = a^2 \text{Var}(X)$$

### Question 10.8
$P(X = k) = \frac{k}{10}$ is given for $k = 1, 2, 3, 4$. Examine whether it is a valid PMF and compute $E[X]$.

> **Formula:**
> $$\sum_{k=1}^{4} \frac{k}{10} = \frac{10}{10} = 1, \quad E[X] = \sum k \cdot p(k)$$

### Question 10.9
$P(X = 1) = c$, $P(X = 2) = 2c$, $P(X = 3) = 3c$ are given. Find the value of the constant $c$ so that it is a valid PMF.

> **Formula:**
> $$\sum_{i} p(x_i) = 1 \implies c + 2c + 3c = 1$$

### Question 10.10
Using the value of $c$ you found in Question 10.9, compute $E[X]$.

> **Formula:**
> $$E[X] = \sum_{i} x_i \cdot P(X = x_i)$$

---

## Unit 11: Binomial Distribution

### Question 11.1
In a factory, 2% of a product is out of specification. We select 6 units at random. Find the probability that exactly one unit is defective.

> **Formula:**
> $$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$$

### Question 11.2
Using the data of Question 11.1, find the probability that 2 or more units are defective.

> **Formula:**
> $$P(X \ge 2) = 1 - P(X = 0) - P(X = 1) = 1 - (1-p)^n - \binom{n}{1} p (1-p)^{n-1}$$

### Question 11.3
In a factory, 1% of a product is defective. We select 7 units. Find the probability that exactly one is defective.

> **Formula:**
> $$P(X = 1) = \binom{7}{1} p (1-p)^{6}$$

### Question 11.4
Using the data of Question 11.3, find the probability that at least two units are defective.

> **Formula:**
> $$P(X \ge 2) = 1 - P(X \le 1)$$

### Question 11.5
Let $X \sim \text{Bin}(10, 0.3)$. Compute $P(X \le 2)$.

> **Formula:**
> $$P(X \le k) = \sum_{j=0}^{k} \binom{n}{j} p^j (1-p)^{n-j}$$

### Question 11.6
Let $X \sim \text{Bin}(20, 0.08)$. Compute the expected value $E[X]$ and the standard deviation $\sigma$.

> **Formula:**
> $$E[X] = np, \quad \sigma = \sqrt{np(1-p)}$$

### Question 11.7
A drug causes side effects in 3 out of 100 patients. Five patients are selected at random. Find the probability that none of them experiences side effects.

> **Formula:**
> $$P(X = 0) = (1-p)^n$$

### Question 11.8
Using the percentage of Question 11.7, what is the expected number of patients with side effects if 100 patients are selected?

> **Formula:**
> $$E[X] = np = 100 \times 0.03$$

### Question 11.9
Let $X$ be the number of problematic connections in 20 random checks with probability of a problematic connection $p = 0.08$. State and justify the four conditions under which $X$ follows a binomial distribution.

> **Formula:**
> Conditions: (1) fixed number of trials $n$, (2) only two possible outcomes, (3) constant probability $p$, (4) independence of trials.

### Question 11.10
Let $X \sim \text{Bin}(12, 0.25)$. Compute the probability $P(X \ge 1)$.

> **Formula:**
> $$P(X \ge 1) = 1 - P(X = 0) = 1 - (1-p)^n$$

---

## Unit 12: Continuous Random Variables & Density Function

### Question 12.1
For a continuous random variable $X$, compute $P(X = 5)$.

> **Formula:**
> For a continuous $X$: $P(X = c) = 0$ for every specific value $c$.

### Question 12.2
The density function $f(x) = c x$ for $0 \le x \le 2$ and $f(x) = 0$ elsewhere is given. Find the constant $c$.

> **Formula:**
> $$\int_{-\infty}^{+\infty} f(x) \, dx = 1 \implies \int_{0}^{2} c x \, dx = 1$$

### Question 12.3
Using the constant $c$ of Question 12.2, compute $P(1 \le X \le 1.5)$.

> **Formula:**
> $$P(a \le X \le b) = \int_{a}^{b} f(x) \, dx$$

### Question 12.4
Explain why, for a continuous random variable, $P(a \le X \le b) = P(a < X \le b) = P(a \le X < b)$ holds.

> **Formula:**
> Because $P(X = a) = P(X = b) = 0$, the endpoints of the intervals do not affect the probability.

### Question 12.5
$f(x) = \frac{1}{4}$ for $0 \le x \le 4$ (uniform distribution) is given. Compute $P(1 \le X \le 3)$.

> **Formula:**
> $$P(1 \le X \le 3) = \int_{1}^{3} \frac{1}{4} \, dx$$

### Question 12.6
Using the data of Question 12.5, compute $P(X > 2)$.

> **Formula:**
> $$P(X > 2) = \int_{2}^{4} \frac{1}{4} \, dx$$

### Question 12.7
State the fundamental difference between the probability mass function (PMF) of a discrete variable and the probability density function (PDF) of a continuous variable.

> **Formula:**
> The PMF gives $P(X = x)$ directly. The PDF gives density: the probability is the area $\int f(x)dx$, and $P(X = c) = 0$.

### Question 12.8
$f(x) = 3x^2$ for $0 \le x \le 1$ and $0$ elsewhere is given. Examine whether it is a valid density function.

> **Formula:**
> A valid PDF if $f(x) \ge 0$ and $\int_{-\infty}^{+\infty} f(x) \, dx = 1$.

### Question 12.9
Using the data of Question 12.8, compute $P(X \le 0.5)$.

> **Formula:**
> $$P(X \le 0.5) = \int_{0}^{0.5} 3x^2 \, dx$$

### Question 12.10
Interpret geometrically the probability $P(a \le X \le b)$ for a continuous random variable.

> **Formula:**
> The area under the curve $y = f(x)$ between the vertical lines $x = a$ and $x = b$.

---

## Unit 13: The Normal Distribution (Properties)

### Question 13.1
Let $X \sim N(\mu, \sigma^2)$. What holds for the mean, the median, and the mode of the normal distribution?

> **Formula:**
> $$\bar{x} = M = T = \mu$$

### Question 13.2
For the normal distribution, around which value is the density curve symmetric?

> **Formula:**
> Symmetric around the mean $\mu$.

### Question 13.3
What is the total area under the curve of the normal distribution?

> **Formula:**
> $$\int_{-\infty}^{+\infty} f(x) \, dx = 1$$

### Question 13.4
For the normal distribution, what percentage of the values lies between $\mu - \sigma$ and $\mu + \sigma$?

> **Formula:**
> $P(\mu - \sigma \le X \le \mu + \sigma) \approx 0.6826$ (68%).

### Question 13.5
Let $X \sim N(10, 4)$. Determine the mean $\mu$, the variance $\sigma^2$, and the standard deviation $\sigma$.

> **Formula:**
> In the notation $N(\mu, \sigma^2)$: the second argument is the variance. $\sigma = \sqrt{\sigma^2}$.

### Question 13.6
Let $X \sim N(50, 25)$. Compute $E[X]$, $\text{Var}(X)$ and $\sigma$.

> **Formula:**
> $E[X] = \mu = 50$, $\text{Var}(X) = \sigma^2 = 25$, $\sigma = \sqrt{25} = 5$.

### Question 13.7
Why is the normal distribution called "bell-shaped"?

> **Formula:**
> Because the graph of the density function is bell-shaped, symmetric around $\mu$.

### Question 13.8
Let $X \sim N(\mu, \sigma^2)$. Compute $P(X < \mu)$.

> **Formula:**
> By symmetry: $P(X < \mu) = P(X > \mu) = 0.5$.

### Question 13.9
Let $X \sim N(100, 64)$. Compute $P(X > 100)$.

> **Formula:**
> $P(X > \mu) = 0.5$.

### Question 13.10
Let $Z \sim N(0, 1)$. Compute $\Phi(0) = P(Z \le 0)$.

> **Formula:**
> $$\Phi(0) = 0.5$$

---

## Unit 14: Z-Standardization & the Standard Normal Distribution

### Question 14.1
Let $X \sim N(48, 16)$. Convert the value $x = 39$ to a $z$ value.

> **Formula:**
> $$Z = \frac{X - \mu}{\sigma}$$

### Question 14.2
Let $X \sim N(48, 16)$. Compute $P(39 \le X \le 57)$. Given $\Phi(2.25) = 0.98778$ and $\Phi(1.5) = 0.93319$.

> **Formula:**
> $$P(a \le X \le b) = \Phi\left(\frac{b-\mu}{\sigma}\right) - \Phi\left(\frac{a-\mu}{\sigma}\right)$$

### Question 14.3
Let $X \sim N(15, 4)$. Compute $P(X > 9)$. Given $\Phi(1.5) = 0.93319$.

> **Formula:**
> $$P(X > a) = 1 - \Phi\left(\frac{a-\mu}{\sigma}\right) = \Phi\left(-\frac{a-\mu}{\sigma}\right)$$

### Question 14.4
Let $X \sim N(10, 4)$. Compute $P(9 \le X \le 13)$. Given $\Phi(0.5) = 0.69146$ and $\Phi(1.5) = 0.93319$.

> **Formula:**
> $$P(9 \le X \le 13) = \Phi(1.5) - \Phi(0.5)$$

### Question 14.5
Let $X \sim N(25, 25)$. Compute $P(X > 15)$. Given $\Phi(2) = 0.9772$.

> **Formula:**
> $$P(X > 15) = 1 - \Phi(2)$$

### Question 14.6
Let $X \sim N(25, 25)$. Compute $P(20 \le X \le 25)$. Given $\Phi(1) = 0.8413$.

> **Formula:**
> $$P(20 \le X \le 25) = \Phi(1) - \Phi(0) = \Phi(1) - 0.5$$

### Question 14.7
Given $\Phi(1.5) = 0.93319$. Compute $\Phi(-1.5) = P(Z \le -1.5)$.

> **Formula:**
> $$\Phi(-z) = 1 - \Phi(z)$$

### Question 14.8
Let $X \sim N(800, 1600)$. Compute $P(740 \le X \le 860)$. Given $\Phi(1.5) = 0.9332$ and $\Phi(2) = 0.9772$.

> **Formula:**
> $$P(740 \le X \le 860) = \Phi(1.5) - \Phi(-1.5) = \Phi(1.5) - (1 - \Phi(1.5))$$

### Question 14.9
Let $X \sim N(12, 4)$. Compute $P(X > 9)$ and $P(11 \le X \le 15)$. Given $\Phi(0.5) = 0.69146$ and $\Phi(1.5) = 0.93319$.

> **Formula:**
> $$P(X > 9) = 1 - \Phi(1.5), \quad P(11 \le X \le 15) = \Phi(1.5) - \Phi(0.5)$$

### Question 14.10
Given $\Phi(0.5) = 0.69146$ and $\Phi(1.5) = 0.93319$. Compute $P(-1.5 \le Z \le 0.5)$.

> **Formula:**
> $$P(z_1 \le Z \le z_2) = \Phi(z_2) - \Phi(z_1) = \Phi(0.5) - (1 - \Phi(1.5))$$

---

## Unit 15: Percentage Points & the Inverse Problem (Inverse Quantile)

### Question 15.1
Let $X \sim N(100, 100)$. Find the value $x_0$ such that $P(X \le x_0) = 0.75$. Given $z_{0.75} = 0.67$.

> **Formula:**
> $$x_0 = \mu + z \cdot \sigma$$

### Question 15.2
Let $X \sim N(50, 25)$. Find the value $x_0$ that exceeds the top 10% of the values. Given $z_{0.90} = 1.28$.

> **Formula:**
> Top 10%: $P(X > x_0) = 0.10$, hence $P(X \le x_0) = 0.90$:
> $$x_0 = \mu + z_{0.90} \cdot \sigma$$

### Question 15.3
Let $X \sim N(100, 64)$. Find the upper boundary of the lowest 25% of the values ($Q_1$). Given $z_{0.25} = -0.67$.

> **Formula:**
> $$Q_1 = \mu + z_{0.25} \cdot \sigma$$

### Question 15.4
Let $X \sim N(100, 64)$. Find the lower boundary of the top 25% of the values ($Q_3$). Given $z_{0.75} = 0.67$.

> **Formula:**
> $$Q_3 = \mu + z_{0.75} \cdot \sigma$$

### Question 15.5
The service time follows $N(12, 4)$. Management wants to give priority to the 25% of customers with the longest waiting time. Find the boundary. Given $z_{0.75} = 0.67$.

> **Formula:**
> The boundary is $Q_3 = \mu + z_{0.75} \cdot \sigma$.

### Question 15.6
Let $X \sim N(48, 16)$. Find the value $x_0$ such that $P(X > x_0) = 0.1587$. Given $\Phi(1) = 0.8413$.

> **Formula:**
> $P(X \le x_0) = 1 - 0.1587 = 0.8413 = \Phi(1)$:
> $$x_0 = \mu + 1 \cdot \sigma$$

### Question 15.7
Let $X \sim N(800, 1600)$. Find the value below which the lowest 2.5% of the values lies. Given $z_{0.025} = -1.96$.

> **Formula:**
> $$x_0 = \mu + z_{0.025} \cdot \sigma$$

### Question 15.8
For a normal distribution, 5% of the values exceeds 60 and the mean is $\mu = 50$. Find the standard deviation $\sigma$. Given $z_{0.95} = 1.645$.

> **Formula:**
> $P(X > 60) = 0.05 \implies z = \frac{60 - \mu}{\sigma} = 1.645 \implies \sigma = \frac{60 - \mu}{1.645}$

### Question 15.9
Let $X \sim N(15, 16)$. Find the value $x_0$ such that $P(X \le x_0) = 0.9772$. Given $\Phi(2) = 0.9772$.

> **Formula:**
> $$x_0 = \mu + 2 \cdot \sigma$$

### Question 15.10
Let $X \sim N(50, 100)$. Compute $Q_1$ and $Q_3$. Given $z_{0.25} = -0.67$, $z_{0.75} = 0.67$.

> **Formula:**
> $$Q_1 = \mu + z_{0.25} \cdot \sigma, \quad Q_3 = \mu + z_{0.75} \cdot \sigma$$

---

## Unit 16: Central Limit Theorem & Sampling Distributions

### Question 16.1
State the Central Limit Theorem (CLT).

> **Formula:**
> For independent, identically distributed r.v.s with mean $\mu$ and variance $\sigma^2$, for $n \ge 30$:
> $$\bar{X} \sim N\left(\mu, \frac{\sigma^2}{n}\right)$$

### Question 16.2
Let a r.v. $X$ have $\mu = 50$ and $\sigma = 10$. We take a random sample of size $n = 36$. Determine the distribution of the sample mean $\bar{X}$.

> **Formula:**
> $$\bar{X} \sim N\left(\mu, \frac{\sigma^2}{n}\right)$$

### Question 16.3
Using the data of Question 16.2, compute $P(\bar{X} < 52)$, expressing the result in terms of the standard normal.

> **Formula:**
> $$Z = \frac{\bar{X} - \mu}{\sigma / \sqrt{n}} \sim N(0, 1)$$

### Question 16.4
The loading time of a web page has $\mu = 30$ sec and $\sigma = 6$ sec. From a sample of $n = 100$, compute $P(\bar{X} < 29)$, expressing the result in terms of $\Phi$.

> **Formula:**
> $$Z = \frac{\bar{X} - \mu}{\sigma / \sqrt{n}}, \quad P(\bar{X} < 29) = \Phi\left(\frac{29 - 30}{6/10}\right)$$

### Question 16.5
Let $X$ have $\mu = 5$ and $\sigma = 2$. For a sample of $n = 50$, determine the distribution of the sum $S_n = \sum_{i=1}^{n} X_i$.

> **Formula:**
> $$S_n \sim N(n\mu, n\sigma^2)$$

### Question 16.6
Using the data of Question 16.5, compute $P(S_n < 260)$, expressing the result in terms of the standard normal.

> **Formula:**
> $$Z = \frac{S_n - n\mu}{\sigma\sqrt{n}} \sim N(0, 1)$$

### Question 16.7
Why does the CLT approximate the distribution of the sample mean by a normal distribution for large $n$? What is the usual threshold value?

> **Formula:**
> The sample mean tends toward a normal distribution as $n$ increases, regardless of the population distribution. Usually $n \ge 30$.

### Question 16.8
Let $X$ have $\mu = 100$ and $\sigma = 8$. For a sample of $n = 64$, compute the standard error of the mean $\sigma_{\bar{X}} = \sigma / \sqrt{n}$.

> **Formula:**
> $$\sigma_{\bar{X}} = \frac{\sigma}{\sqrt{n}}$$

### Question 16.9
Using the data of Question 16.8, compute $P(\bar{X} > 101)$. Given $\Phi(1) = 0.8413$.

> **Formula:**
> $$P(\bar{X} > 101) = 1 - \Phi(1)$$

### Question 16.10
What is the variance of the sample mean $\bar{X}$ for a sample of size $n$ from a population with variance $\sigma^2$?

> **Formula:**
> $$\text{Var}(\bar{X}) = \frac{\sigma^2}{n}$$

---

## Unit 17: Bivariate Distributions & Linear Combinations

### Question 17.1
Give the definition of the covariance $\text{Cov}(X, Y)$.

> **Formula:**
> $$\text{Cov}(X, Y) = E[(X - \mu_X)(Y - \mu_Y)] = E[XY] - E[X]E[Y]$$

### Question 17.2
If the random variables $X$ and $Y$ are independent, what is the value of $\text{Cov}(X, Y)$?

> **Formula:**
> If $X$, $Y$ independent: $\text{Cov}(X, Y) = 0$.

### Question 17.3
$E[X] = 3$, $E[Y] = 4$ and $E[XY] = 13$ are given. Compute $\text{Cov}(X, Y)$.

> **Formula:**
> $$\text{Cov}(X, Y) = E[XY] - E[X]E[Y]$$

### Question 17.4
$\text{Cov}(X, Y) = 6$, $\sigma_X = 2$ and $\sigma_Y = 3$ are given. Compute the correlation coefficient $\rho_{XY}$.

> **Formula:**
> $$\rho_{XY} = \frac{\text{Cov}(X, Y)}{\sigma_X \sigma_Y}, \quad -1 \le \rho \le 1$$

### Question 17.5
$X$ and $Y$ are independent with $\text{Var}(X) = 4$ and $\text{Var}(Y) = 9$. Compute $\text{Var}(2X + 3Y)$.

> **Formula:**
> If $X$, $Y$ independent:
> $$\text{Var}(aX + bY) = a^2 \text{Var}(X) + b^2 \text{Var}(Y)$$

### Question 17.6
$X$ and $Y$ have $\text{Var}(X) = 4$, $\text{Var}(Y) = 9$ and $\text{Cov}(X, Y) = 2$. Compute $\text{Var}(2X + 3Y)$.

> **Formula:**
> $$\text{Var}(aX + bY) = a^2 \text{Var}(X) + b^2 \text{Var}(Y) + 2ab \text{Cov}(X, Y)$$

### Question 17.7
Given $\rho_{XY} = -0.8$. What do you conclude about the relationship between $X$ and $Y$?

> **Formula:**
> Strong negative linear correlation: when $X$ increases, $Y$ tends to decrease.

### Question 17.8
$X$ and $Y$ are independent with $\text{Var}(X) = 5$ and $\text{Var}(Y) = 7$. Compute $\text{Var}(X + Y)$.

> **Formula:**
> $$\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y)$$

### Question 17.9
$E[X] = 10$ and $E[Y] = 20$ are given. Compute $E[3X - 2Y]$.

> **Formula:**
> $$E[aX + bY] = aE[X] + bE[Y]$$

### Question 17.10
If $\rho_{XY} = 0$, does it imply that $X$ and $Y$ are independent? Justify your answer.

> **Formula:**
> Not always. Zero correlation does not imply independence (except for the bivariate normal). Independence implies $\rho = 0$, but the converse does not hold in general.

---

## Unit 18: R Commands - Descriptive Statistics

### Question 18.1
The data are stored in an R vector named `x`. Which command computes the mean?

> **Formula:**
> ```r
> mean(x)
> ```

### Question 18.2
The data are stored in an R vector named `x`. Which command computes the median?

> **Formula:**
> ```r
> median(x)
> ```

### Question 18.3
The data are stored in an R vector named `x`. Which command computes the sample standard deviation?

> **Formula:**
> ```r
> sd(x)
> ```

### Question 18.4
The data are stored in an R vector named `x`. Which command computes the first quartile $Q_1$?

> **Formula:**
> ```r
> quantile(x, probs = 0.25)
> ```

### Question 18.5
The data are stored in an R vector named `x`. Which command computes the third quartile $Q_3$?

> **Formula:**
> ```r
> quantile(x, probs = 0.75)
> ```

### Question 18.6
The data are stored in an R vector named `x`. Which command computes the mode?

> **Formula:**
> ```r
> names(which.max(table(x)))
> ```

### Question 18.7
The data are stored in an R vector named `x`. Which command computes the sample variance?

> **Formula:**
> ```r
> var(x)
> ```

### Question 18.8
The original, ungrouped time data are stored in an R vector named `times`. Write the command to compute the standard deviation.

> **Formula:**
> ```r
> sd(times)
> ```

### Question 18.9
The data are stored in an R vector named `x`. Which command displays the summary statistics (Min, $Q_1$, Median, Mean, $Q_3$, Max)?

> **Formula:**
> ```r
> summary(x)
> ```

### Question 18.10
The data are stored in an R vector named `x`. Which command computes all three quartiles at the same time?

> **Formula:**
> ```r
> quantile(x, probs = c(0.25, 0.50, 0.75))
> ```

---

## Unit 19: R Commands - Binomial Distribution

### Question 19.1
Let $X \sim \text{Bin}(6, 0.02)$. Which R command computes $P(X = 1)$?

> **Formula:**
> ```r
> dbinom(1, size = 6, prob = 0.02)
> ```

### Question 19.2
Let $X \sim \text{Bin}(6, 0.02)$. Which R command computes $P(X \ge 2)$?

> **Formula:**
> ```r
> 1 - pbinom(1, size = 6, prob = 0.02)
> ```

### Question 19.3
Let $X \sim \text{Bin}(6, 0.02)$. Which alternative R command with the `lower.tail` argument computes $P(X \ge 2)$?

> **Formula:**
> ```r
> pbinom(1, size = 6, prob = 0.02, lower.tail = FALSE)
> ```

### Question 19.4
Let $X \sim \text{Bin}(10, 0.3)$. Which R command computes $P(X \le 2)$?

> **Formula:**
> ```r
> pbinom(2, size = 10, prob = 0.3)
> ```

### Question 19.5
Let $X \sim \text{Bin}(8, 0.2)$. Which R command computes $P(X < 3)$?

> **Formula:**
> $P(X < 3) = P(X \le 2)$:
> ```r
> pbinom(2, size = 8, prob = 0.2)
> ```

### Question 19.6
Let $X \sim \text{Bin}(10, 0.4)$. Which R command computes $P(X > 4)$?

> **Formula:**
> ```r
> 1 - pbinom(4, size = 10, prob = 0.4)
> ```
> or
> ```r
> pbinom(4, size = 10, prob = 0.4, lower.tail = FALSE)
> ```

### Question 19.7
Let $X \sim \text{Bin}(5, 0.03)$. Which R command computes $P(X = 0)$?

> **Formula:**
> ```r
> dbinom(0, size = 5, prob = 0.03)
> ```

### Question 19.8
Let $X \sim \text{Bin}(20, 0.5)$. Which R command finds the smallest value $k$ such that $P(X \le k) \ge 0.9$?

> **Formula:**
> ```r
> qbinom(0.9, size = 20, prob = 0.5)
> ```

### Question 19.9
Let $X \sim \text{Bin}(12, 0.25)$. Which R command computes $P(X \ge 1)$?

> **Formula:**
> ```r
> 1 - dbinom(0, size = 12, prob = 0.25)
> ```
> or
> ```r
> 1 - pbinom(0, size = 12, prob = 0.25)
> ```

### Question 19.10
Which R function is used to compute the point probability $P(X = k)$ of the binomial distribution and which one for the cumulative $P(X \le k)$?

> **Formula:**
> ```r
> dbinom(k, size = n, prob = p)   # P(X = k)
> pbinom(k, size = n, prob = p)   # P(X <= k)
> ```

---

## Unit 20: R Commands - Normal Distribution

### Question 20.1
Let $X \sim N(\mu, \sigma^2)$. Which R command computes $P(X \le x)$?

> **Formula:**
> ```r
> pnorm(x, mean = mu, sd = sigma)
> ```

### Question 20.2
Let $X \sim N(\mu, \sigma^2)$. Which R command computes $P(X > a)$?

> **Formula:**
> ```r
> 1 - pnorm(a, mean = mu, sd = sigma)
> ```

### Question 20.3
Let $X \sim N(\mu, \sigma^2)$. Which R command computes $P(a \le X \le b)$?

> **Formula:**
> ```r
> pnorm(b, mean = mu, sd = sigma) - pnorm(a, mean = mu, sd = sigma)
> ```

### Question 20.4
Let $X \sim N(\mu, \sigma^2)$. Which R command with the `lower.tail` argument computes $P(X > a)$?

> **Formula:**
> ```r
> pnorm(a, mean = mu, sd = sigma, lower.tail = FALSE)
> ```

### Question 20.5
Let $X \sim N(\mu, \sigma^2)$. Which R command finds the value $x_0$ such that $P(X \le x_0) = p$?

> **Formula:**
> ```r
> qnorm(p, mean = mu, sd = sigma)
> ```

### Question 20.6
Let $X \sim N(48, 4)$. Which R command computes $P(39 \le X \le 57)$?

> **Formula:**
> ```r
> pnorm(57, mean = 48, sd = 4) - pnorm(39, mean = 48, sd = 4)
> ```
> Caution: the value passed as `sd` is the standard deviation $\sigma = 4$, not the variance.

### Question 20.7
Let $X \sim N(15, 4)$. Which R command computes $P(X > 9)$?

> **Formula:**
> ```r
> 1 - pnorm(9, mean = 15, sd = 4)
> ```

### Question 20.8
Let $X \sim N(\mu, \sigma^2)$. Management wants the boundary for the top 25% of the values. Which R command gives this boundary?

> **Formula:**
> ```r
> qnorm(0.75, mean = mu, sd = sigma)
> ```

### Question 20.9
Let $X \sim N(12, 2)$. Which R command computes $P(11 \le X \le 15)$?

> **Formula:**
> ```r
> pnorm(15, mean = 12, sd = 2) - pnorm(11, mean = 12, sd = 2)
> ```

### Question 20.10
For computing normal distribution probabilities in R, why must the standard deviation be given in the `sd` argument and not the variance?

> **Formula:**
> `pnorm` (and `qnorm`) accept the parameter `sd = \sigma` (standard deviation). If the variance $\sigma^2$ is given, the result will be wrong. If $\sigma^2$ is known, use `sd = sqrt(sigma^2)`.

---

*End of test_prep.md — 200 practice questions (20 units x 10 questions).*
