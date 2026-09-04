# Exercises: Advanced Counting, Recurrences, and Graph Algorithms

## Context and Grounding
This practice set reinforces combinatorial problem-solving, generating functions, Pigeonhole principle applications, and graph degree constraints. It directly connects with `Lectures/3 Combinatorics.pdf`, `Lectures/6 Graph Theory.pdf`, and `Resources/Notes/6_Combinatorics & Pigeonhole.md`.

---

## Problems

### Problem 1: Stars and Bars (Integer Partitions)
How many distinct non-negative integer solutions $(x_1, x_2, x_3, x_4)$ satisfy:
$$x_1 + x_2 + x_3 + x_4 = 15$$
subject to the constraints $x_1 \ge 1$, $x_2 \ge 2$, $x_3 \ge 0$, and $x_4 \ge 3$?

### Problem 2: Pigeonhole Principle Application
Show that in any group of 8 people, there must exist at least two individuals whose difference in age (measured in complete years) is an exact multiple of 7.

### Problem 3: Handshaking Lemma on Regular Graphs
A $k$-regular graph is a simple graph in which every vertex has degree exactly $k$.
1. If a 3-regular (cubic) graph has 18 edges, how many vertices does it have?
2. Can a 3-regular graph have an odd number of vertices? Justify with a mathematical theorem.

---

## Detailed Step-by-Step Solutions

### Solution 1
Introduce change of variables to convert constraints into standard non-negative form ($y_i \ge 0$):
* Let $y_1 = x_1 - 1 \ge 0 \implies x_1 = y_1 + 1$
* Let $y_2 = x_2 - 2 \ge 0 \implies x_2 = y_2 + 2$
* Let $y_3 = x_3 \ge 0 \implies x_3 = y_3$
* Let $y_4 = x_4 - 3 \ge 0 \implies x_4 = y_4 + 3$

Substitute into the original equation:
$$(y_1 + 1) + (y_2 + 2) + y_3 + (y_4 + 3) = 15$$
$$y_1 + y_2 + y_3 + y_4 + 6 = 15$$
$$y_1 + y_2 + y_3 + y_4 = 9$$

By the stars-and-bars theorem, the number of non-negative integer solutions to distributing $n = 9$ indistinguishable items into $k = 4$ distinguishable bins is:
$$\binom{n + k - 1}{k - 1} = \binom{9 + 4 - 1}{4 - 1} = \binom{12}{3}$$
Calculate the binomial coefficient:
$$\binom{12}{3} = \frac{12 \times 11 \times 10}{3 \times 2 \times 1} = 2 \times 11 \times 10 = 220$$
**Result:** 220 distinct solutions.

### Solution 2
* Consider the age of each person $a_i \in \mathbb{Z}_{\ge 0}$ for $i = 1, \dots, 8$.
* When an integer is divided by 7, the possible remainders belong to the set $\{0, 1, 2, 3, 4, 5, 6\}$ (7 possible remainder values, which serve as our "pigeonholes").
* We have 8 people (8 "pigeons") whose ages produce remainders modulo 7.
* By the Pigeonhole Principle, since $8 > 7$, at least two people must have ages with the identical remainder modulo 7:
  $$a_i \equiv a_j \pmod 7 \quad \text{for some } i \neq j$$
* This implies:
  $$a_i - a_j = 7m \quad \text{for some integer } m$$
Thus, their age difference is an exact multiple of 7. $\blacksquare$

### Solution 3
1. By the Handshaking Lemma:
   $$\sum_{v \in V} \deg(v) = 2|E|$$
   For a $k$-regular graph with $|V| = n$ vertices, each vertex has degree $k$, so:
   $$n \times k = 2|E|$$
   Given $k = 3$ and $|E| = 18$:
   $$3n = 2(18) = 36 \implies n = 12$$
   The graph has 12 vertices.
2. By the Handshaking Lemma, $n \times 3 = 2|E|$.
   Since $2|E|$ is an even integer, $3n$ must be even.
   Since 3 is odd, $n$ must be even.
   Therefore, no 3-regular graph can have an odd number of vertices. $\blacksquare$

