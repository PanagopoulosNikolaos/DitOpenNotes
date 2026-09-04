# Recurrence Relations and Asymptotic Analysis

## Overview
Recurrence relations express the $n$-th term of a sequence as a function of preceding terms, providing the primary mathematical formalization for analyzing recursive algorithms and dynamic programming state transitions.

---

## 1. Linear Homogeneous Recurrence Relations with Constant Coefficients

A linear homogeneous recurrence of degree $k$ has the standard form:
$$a_n = c_1 a_{n-1} + c_2 a_{n-2} + \dots + c_k a_{n-k}$$
where $c_1, c_2, \dots, c_k$ are real constants and $c_k \neq 0$.

### 1.1 The Characteristic Equation
Substituting the trial solution $a_n = r^n$ yields the characteristic polynomial:
$$r^k - c_1 r^{k-1} - c_2 r^{k-2} - \dots - c_k = 0$$

### 1.2 Second-Order Case ($k = 2$)
Given $a_n = c_1 a_{n-1} + c_2 a_{n-2}$ with roots $r_1, r_2$:
1. **Distinct Real Roots** ($r_1 \neq r_2$):
   $$a_n = \alpha_1 r_1^n + \alpha_2 r_2^n$$
2. **Repeated Root** ($r_1 = r_2 = r$):
   $$a_n = (\alpha_1 + \alpha_2 n) r^n$$
3. Constants $\alpha_1, \alpha_2$ are uniquely determined by initial conditions $a_0, a_1$.

---

## 2. Linear Non-Homogeneous Recurrence Relations

Standard form:
$$a_n = c_1 a_{n-1} + c_2 a_{n-2} + \dots + c_k a_{n-k} + F(n)$$
The general solution is the sum of the homogeneous solution $a_n^{(h)}$ and a particular solution $a_n^{(p)}$:
$$a_n = a_n^{(h)} + a_n^{(p)}$$

---

## 3. The Master Theorem for Divide-and-Conquer Recurrences

For recurrences dividing input size $n$ into $a$ subproblems of size $n/b$:
$$T(n) = a T\left(\frac{n}{b}\right) + O(n^d)$$
where $a \ge 1, b > 1, d \ge 0$:

1. If $d < \log_b a$:
   $$T(n) = \Theta(n^{\log_b a})$$
2. If $d = \log_b a$:
   $$T(n) = \Theta(n^d \log n)$$
3. If $d > \log_b a$:
   $$T(n) = \Theta(n^d)$$

