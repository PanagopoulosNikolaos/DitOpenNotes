# Exercises: Asymptotic Complexity and Recurrence Relations

Comprehensive solved problems covering formal asymptotic proofs, Master Theorem classifications, recursion tree expansions, and mathematical induction substitution proofs for **Data Structures and Algorithms (Course Code: 305)**.

---

## Problem 1: Formal $\epsilon$-$n_0$ Asymptotic Bounds

### Problem 1.1
Using the formal definition of $\Theta$-notation, find explicit positive constants $c_1, c_2,$ and $n_0$ to prove that:
$$
f(n) = 4n^2 + 7n - 5 = \Theta(n^2)
$$

### Problem 1.2
Prove or disprove the following asymptotic statements:
1. $2^{n+3} = O(2^n)$
2. $2^{2n} = O(2^n)$
3. $\log(n!) = \Theta(n \log n)$

---

## Solution to Problem 1

### Solution 1.1: Bounding $4n^2 + 7n - 5$
By definition, $f(n) = \Theta(n^2) \iff \exists c_1, c_2, n_0 > 0$ such that:
$$
0 \le c_1 n^2 \le 4n^2 + 7n - 5 \le c_2 n^2 \quad \forall n \ge n_0
$$

**Finding $c_2$ (Upper Bound):**
For all $n \ge 1$:
$$
4n^2 + 7n - 5 \le 4n^2 + 7n^2 = 11n^2
$$
Thus, choose $c_2 = 11$.

**Finding $c_1$ (Lower Bound):**
We require $4n^2 + 7n - 5 \ge c_1 n^2$.
Notice that for $n \ge 1$, $7n - 5 \ge 2 > 0$. Therefore:
$$
4n^2 + 7n - 5 \ge 4n^2
$$
Thus, choose $c_1 = 4$.

**Validity Region:**
Both inequalities hold simultaneously for all $n \ge n_0 = 1$.
$$
4 n^2 \le 4n^2 + 7n - 5 \le 11 n^2 \quad \forall n \ge 1
$$
Hence, $f(n) = \Theta(n^2)$ with $c_1 = 4, c_2 = 11, n_0 = 1$.

---

### Solution 1.2: Asymptotic Statements

#### 1. $2^{n+3} = O(2^n)$:
Using properties of exponents:
$$
2^{n+3} = 2^3 \cdot 2^n = 8 \cdot 2^n
$$
Choosing $c = 8$ and $n_0 = 1$:
$$
2^{n+3} \le 8 \cdot 2^n \quad \forall n \ge 1
$$
**Statement is TRUE.**

#### 2. $2^{2n} = O(2^n)$:
Suppose there exists a constant $c > 0$ and $n_0 > 0$ such that $2^{2n} \le c \cdot 2^n$ for all $n \ge n_0$.
Dividing both sides by $2^n$:
$$
\frac{2^{2n}}{2^n} \le c \implies 2^n \le c \quad \forall n \ge n_0
$$
Since $2^n \to \infty$ as $n \to \infty$, no finite constant $c$ can bound $2^n$ from above.
**Statement is FALSE.**

#### 3. $\log(n!) = \Theta(n \log n)$:
Recall $n! = 1 \times 2 \times \dots \times n \le n^n$.
- Upper Bound:
  $$
  \log(n!) = \sum_{i=1}^n \log i \le \sum_{i=1}^n \log n = n \log n \implies \log(n!) = O(n \log n)
  $$
- Lower Bound:
  Retain the upper half of the terms ($i \ge n/2$):
  $$
  \log(n!) = \sum_{i=1}^n \log i \ge \sum_{i=\lceil n/2 \rceil}^n \log i \ge \sum_{i=\lceil n/2 \rceil}^n \log(n/2) = \frac{n}{2} \log\left(\frac{n}{2}\right) = \frac{n}{2} (\log n - 1) = \Omega(n \log n)
  $$
Since $\log(n!) = O(n \log n)$ and $\log(n!) = \Omega(n \log n)$, it follows that $\log(n!) = \Theta(n \log n)$.
**Statement is TRUE.**

---

## Problem 2: Master Theorem Applications

Solve each recurrence or state why the standard Master Theorem does not apply:
1. $T(n) = 8 T(n/2) + 1000 n^2$
2. $T(n) = 2 T(n/2) + n \log_2 n$
3. $T(n) = 3 T(n/4) + n \log_2 n$
4. $T(n) = 2 T(n/2) + \frac{n}{\log_2 n}$

---

## Solution to Problem 2

The Master Theorem applies to recurrences of the form:
$$
T(n) = a T(n/b) + f(n), \quad a \ge 1, b > 1
$$
The critical benchmark value is $n^{\log_b a}$.

### 2.1 $T(n) = 8 T(n/2) + 1000 n^2$
- $a = 8, b = 2, f(n) = 1000 n^2$.
- $n^{\log_b a} = n^{\log_2 8} = n^3$.
- Compare $f(n)$ with $n^3$: $f(n) = O(n^{3 - \epsilon})$ for $\epsilon = 1$.
- **Case 1 Applies:** The tree root work is dominated by the subproblem leaves.
$$
T(n) = \Theta(n^{\log_b a}) = \Theta(n^3)
$$

### 2.2 $T(n) = 2 T(n/2) + n \log_2 n$
- $a = 2, b = 2, f(n) = n \log_2 n$.
- $n^{\log_2 2} = n^1 = n$.
- Here $f(n) = n \log n$ is asymptotically larger than $n$, but NOT polynomially larger (the difference is a logarithmic factor, not $n^\epsilon$). Thus standard Master Theorem does not strictly apply.
- **Extended Case 2:** When $f(n) = \Theta(n^{\log_b a} \log^k n)$ with $k \ge 0$:
  $$
  T(n) = \Theta(n^{\log_b a} \log^{k+1} n)
  $$
  Here $k = 1$:
  $$
  T(n) = \Theta(n \log^{1+1} n) = \Theta(n \log^2 n)
  $$

### 2.3 $T(n) = 3 T(n/4) + n \log_2 n$
- $a = 3, b = 4, f(n) = n \log_2 n$.
- $n^{\log_b a} = n^{\log_4 3} \approx n^{0.7925}$.
- $f(n) = \Omega(n^{\log_4 3 + \epsilon})$ for $\epsilon \approx 0.20$.
- **Check Regularity Condition (Case 3):**
  $$
  a f(n/b) \le c f(n) \implies 3 \cdot \left(\frac{n}{4} \log_2(n/4)\right) = \frac{3}{4} n (\log_2 n - 2) \le \frac{3}{4} n \log_2 n
  $$
  Choosing $c = 3/4 < 1$ satisfies regularity for large $n$.
  $$
  T(n) = \Theta(f(n)) = \Theta(n \log n)
  $$

### 2.4 $T(n) = 2 T(n/2) + \frac{n}{\log_2 n}$
- $a = 2, b = 2 \implies n^{\log_2 2} = n$.
- $f(n) = \frac{n}{\log n}$ is asymptotically smaller than $n$, but NOT polynomially smaller ($n / (n / \log n) = \log n \ne n^\epsilon$).
- Standard Master Theorem cannot be applied.
- Solving via Recursion Tree:
  - Height of tree: $k = \log_2 n$.
  - Work at level $j$: $2^j \cdot \frac{n/2^j}{\log_2(n/2^j)} = \frac{n}{\log_2 n - j}$.
  - Summing over levels $j = 0$ to $\log_2 n - 1$:
    $$
    T(n) = \sum_{j=0}^{\log_2 n - 1} \frac{n}{\log_2 n - j} + \Theta(n) = n \sum_{m=1}^{\log_2 n} \frac{1}{m} + \Theta(n)
    $$
    Recall harmonic series $H_k = \sum_{m=1}^k \frac{1}{m} = \ln k + O(1)$. With $k = \log_2 n$:
    $$
    T(n) = n \ln(\log_2 n) + \Theta(n) = \Theta(n \log(\log n))
    $$

---

## Problem 3: Recursion Tree Method for Unequal Splits

Solve the recurrence:
$$
T(n) = T(n/3) + T(2n/3) + c n
$$

---

## Solution to Problem 3

### Step 1: Analyze Tree Levels
```
Level 0:                         cn                         = cn
Level 1:              c(n/3)     +      c(2n/3)             = cn
Level 2:       c(n/9) + c(2n/9)  +  c(2n/9) + c(4n/9)       = cn
```
Each internal level of the tree sums to exactly $c n$.

### Step 2: Determine Tree Depth
- The shortest branch descends via the $n/3$ subproblem:
  $$
  n \cdot (1/3)^{h_{\min}} = 1 \implies h_{\min} = \log_3 n
  $$
- The longest branch descends via the $2n/3$ subproblem:
  $$
  n \cdot (2/3)^{h_{\max}} = 1 \implies h_{\max} = \log_{3/2} n
  $$

### Step 3: Compute Bounds
- Lower bound:
  $$
  T(n) \ge \sum_{j=0}^{\log_3 n} c n = c n \log_3 n = \Omega(n \log n)
  $$
- Upper bound:
  $$
  T(n) \le \sum_{j=0}^{\log_{3/2} n} c n = c n \log_{3/2} n = O(n \log n)
  $$
Thus, $T(n) = \Theta(n \log n)$.

---

## Problem 4: Substitution Method (Mathematical Induction)

Prove by the substitution method that $T(n) = 2 T(\lfloor n/2 \rfloor) + n$ satisfies $T(n) = O(n \log_2 n)$.

---

## Solution to Problem 4

**Hypothesis:** $T(n) \le c n \log_2 n$ for some constant $c > 0$ and all $n \ge n_0$.

**Inductive Step:**
Assume the hypothesis holds for all $k < n$, specifically for $k = \lfloor n/2 \rfloor$:
$$
T(\lfloor n/2 \rfloor) \le c \lfloor n/2 \rfloor \log_2(\lfloor n/2 \rfloor) \le c \frac{n}{2} \log_2(n/2)
$$

Substitute into the recurrence:
$$
T(n) = 2 T(\lfloor n/2 \rfloor) + n \le 2 \left( c \frac{n}{2} \log_2(n/2) \right) + n
$$
$$
T(n) \le c n (\log_2 n - \log_2 2) + n = c n \log_2 n - c n + n
$$
$$
T(n) \le c n \log_2 n - (c - 1) n
$$

To establish $T(n) \le c n \log_2 n$, we require:
$$
-(c - 1) n \le 0 \iff c - 1 \ge 0 \iff c \ge 1
$$

**Base Case:**
For $n = 2$:
$$
T(2) = 2 T(1) + 2
$$
If $T(1) = 1$, then $T(2) = 4$.
We require $T(2) \le c \cdot 2 \log_2 2 = 2c$.
$$
4 \le 2c \implies c \ge 2
$$
Choosing $c = 2$ satisfies both the base case ($n = 2$) and inductive step ($c \ge 1$).

Hence, by induction, $T(n) \le 2 n \log_2 n = O(n \log n)$ for all $n \ge 2$.

