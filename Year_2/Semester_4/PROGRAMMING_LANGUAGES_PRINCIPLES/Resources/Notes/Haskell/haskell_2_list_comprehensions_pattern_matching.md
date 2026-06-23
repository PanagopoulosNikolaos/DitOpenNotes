# Haskell — List Comprehensions and Pattern Matching

*Prerequisite: haskell_1_basics_pure_functions.md — Immutability, lazy evaluation, and recursion.*

Haskell provides declarative syntax for constructing lists from existing lists, closely analogous to mathematical set-builder notation. This file covers list comprehension syntax (generators, predicates, dependent generators), safe extraction from infinite lists, classic algorithms (Sieve of Eratosthenes, Fibonacci), and pattern matching with guard clauses as the primary control-flow mechanism replacing `if`/`else`.

---

## 1. List Comprehension Syntax

### 1.1 Concept Overview

A **list comprehension** builds a new list by iterating over one or more source lists, optionally filtering elements with predicates, and mapping each binding to an output expression. Because Haskell is lazy, comprehensions over infinite sources are well-defined when the result is consumed finitely.

### 1.2 Syntax Reference

```
[ <output_expr> | <qualifier_1>, <qualifier_2>, ... , <qualifier_n> ]
```

Where each **qualifier** is either:

- A **generator:** `<pattern> <- <list_expr>`
- A **predicate (guard):** `<bool_expr>`

### 1.3 Qualifier Reference Table

| Qualifier Type | Syntax | Role | Evaluated When |
| :--- | :--- | :--- | :--- |
| Generator | `x <- [1..10]` | Bind `x` to each element | Lazy, on demand |
| Predicate | `even x` | Filter: keep binding if `True` | After generator produces candidate |
| Dependent generator | `y <- [1..x]` | `y` range depends on prior `x` | Nested, inner per outer |
| Multiple generators | `x <- xs, y <- ys` | Cartesian product | All pairs enumerated |

### 1.4 Basic Examples

```haskell
-- Squares of 1 through 10.
squares = [x^2 | x <- [1..10]]

-- Evens from 1 through 20.
evens = [x | x <- [1..20], x `mod` 2 == 0]

-- Cartesian product (pairs).
pairs = [(x, y) | x <- [1..3], y <- [1..3]]
```

```text
[1,4,9,16,25,36,49,64,81,100]
[2,4,6,8,10,12,14,16,18,20]
[(1,1),(1,2),(1,3),(2,1),(2,2),(2,3),(3,1),(3,2),(3,3)]
```

---

## 2. Generators and Predicates

### 2.1 Generators

A generator `x <- list` introduces a pattern variable `x` drawn from each element of `list`. The pattern may destructure tuples or lists:

```haskell
-- Extract first component of each pair.
firsts = [a | (a, b) <- [(1, 'x'), (2, 'y'), (3, 'z')]]
```

```text
[1,2,3]
```

### 2.2 Predicates as Filters

Predicates appear after generators and act as filters. Multiple predicates are combined with logical **and** (all must hold):

```haskell
-- Pythagorean triples with sides <= 10.
triples = [(a, b, c)
          | a <- [1..10]
          , b <- [a..10]
          , c <- [b..10]
          , a^2 + b^2 == c^2]
```

```text
[(3,4,5),(6,8,10)]
```

### 2.3 Multiple and Dependent Generators

**Multiple generators** (comma-separated) produce a Cartesian product:

$$
\{(x, y) \mid x \in \{1,2,3\},\ y \in \{1,2,3\}\}
$$

**Dependent generators** constrain the inner range based on the outer binding:

```haskell
-- Pairs where y <= x.
dependent = [(x, y) | x <- [1..4], y <- [1..x]]
```

```text
[(1,1),(2,1),(2,2),(3,1),(3,2),(3,3),(4,1),(4,2),(4,3),(4,4)]
```

---

## 3. Infinite Lists and `take`

### 3.1 Concept Overview

The range syntax `[n..]` and `[n, n+step..]` produce **infinite lists**. Combined with lazy evaluation, these are first-class values. Extraction must be bounded with `take`, `drop`, `head`, or a terminating `fold`.

### 3.2 Syntax Reference

```
take <n> <list>
drop <n> <list>
[n..]           -- infinite naturals from n
[n, n+d..]      -- infinite arithmetic sequence with step d
```

### 3.3 Behavioral Description

| Expression | Finite? | Safe Usage |
| :--- | :--- | :--- |
| `[1..]` | No | `take n [1..]` |
| `[0,2..]` | No | `take 5 [0,2..]` → `[0,2,4,6,8]` |
| `iterate f x` | No | `take n (iterate f x)` |
| `repeat x` | No | `take n (repeat x)` |

```haskell
firstTenNats = take 10 [1..]
firstFiveEvens = take 5 [0, 2..]

main = do
  print firstTenNats
  print firstFiveEvens
```

```text
[1,2,3,4,5,6,7,8,9,10]
[0,2,4,6,8]
```

> **[Key Insight]** `take n` forces exactly $n$ elements from the front of a list. All remaining thunks are discarded. This is the standard idiom for making infinite structures usable.

---

## 4. Sieve of Eratosthenes

### 4.1 Algorithm

The **Sieve of Eratosthenes** generates primes by recursively filtering composites from an integer stream:

1. Start with `[2..]`.
2. The head $p$ is prime.
3. The tail removes all multiples of $p$: `filter (\n -> n `mod` p /= 0) rest`.
4. Repeat on the filtered tail.

### 4.2 Implementation

```haskell
sieve (p : xs) = p : sieve [x | x <- xs, x `mod` p /= 0]
primes = sieve [2..]

main = print (take 10 primes)
```

```text
[2,3,5,7,11,13,17,19,23,29]
```

### 4.3 Trace of First Three Primes

| Step | List Head | Filter Condition | New Prime |
| :--- | :--- | :--- | :--- |
| 1 | `2 : [3,4,5,...]` | — | `2` |
| 2 | `3 : [4,5,6,...]` | `x mod 2 /= 0` | `3` |
| 3 | `5 : [6,7,8,...]` | `x mod 3 /= 0` | `5` |

After filtering multiples of 2: `[3,5,7,9,...]`. After filtering multiples of 3: `[5,7,11,13,...]`.

---

## 5. Fibonacci Sequence

### 5.1 Recursive Definition

The Fibonacci sequence is defined by:

$$
F_0 = 0, \quad F_1 = 1, \quad F_n = F_{n-1} + F_{n-2} \quad \text{for } n \geq 2
$$

### 5.2 Infinite List Definition

```haskell
fibs = 0 : 1 : zipWith (+) fibs (tail fibs)

main = print (take 10 fibs)
```

```text
[0,1,1,2,3,5,8,13,21,34]
```

`zipWith (+) fibs (tail fibs)` aligns $F_n + F_{n+1}$ to produce $F_{n+2}$ at each step.

### 5.3 Golden Ratio Connection

The ratio of consecutive Fibonacci numbers converges to the **golden ratio** $\phi$:

$$
\phi = \frac{1 + \sqrt{5}}{2} \approx 1.618
$$

$$
\lim_{n \to \infty} \frac{F_{n+1}}{F_n} = \phi
$$

| $n$ | $F_n$ | $F_{n+1} / F_n$ |
| :--- | :--- | :--- |
| 5 | 5 | $8/5 = 1.600$ |
| 10 | 55 | $89/55 \approx 1.618$ |
| 20 | 6765 | $\approx 1.618034$ |

> **[Supplementary]**
>
> Binet's closed-form formula expresses the $n$-th Fibonacci number directly:
>
> $$
> F_n = \frac{\phi^n - \psi^n}{\sqrt{5}}, \quad \psi = \frac{1 - \sqrt{5}}{2}
> $$
>
> This formula is primarily of theoretical interest; the recursive or `zipWith` list definition is the standard Haskell idiom.

---

## 6. Pattern Matching

### 6.1 Concept Overview

**Pattern matching** deconstructs data by shape at the point of binding. It replaces conditional chains with equations over patterns. Patterns appear in function heads, `case` expressions, `let`, `where`, and list comprehensions.

### 6.2 Syntax Reference

```
<function> <pattern_1> = <expr_1>
<function> <pattern_2> = <expr_2>

case <expr> of
  <pattern_1> -> <expr_1>
  <pattern_2> -> <expr_2>
```

### 6.3 Common Patterns

| Pattern | Matches | Binds |
| :--- | :--- | :--- |
| `[]` | Empty list | Nothing |
| `(x:xs)` | Non-empty list | Head `x`, tail `xs` |
| `(a, b)` | 2-tuple | Both components |
| `0` | Exact value 0 | — |
| `_` | Anything (wildcard) | Discarded |
| `n` | Any value | `n` |

```haskell
-- Pattern matching on lists.
head' (x:_)   = x
tail' (_:xs)  = xs
sum' []       = 0
sum' (x:xs)   = x + sum' xs

main = print (head' [10,20,30], sum' [1,2,3])
```

```text
(10,6)
```

### 6.4 Non-Exhaustive Patterns

If no pattern matches, the program raises a runtime exception. The compiler warns about non-exhaustive patterns when possible.

```haskell
-- Only handles non-empty lists; [] causes runtime error.
badHead (x:_) = x
```

**Resolution:** Add a base case for `[]` or use `Maybe` to represent absence safely.

---

## 7. Guard Clauses

### 7.1 Concept Overview

**Guards** are Boolean conditions attached to function equations. They generalize `if-then-else` chains and are evaluated top-to-bottom; the first guard that evaluates to `True` selects its right-hand side.

### 7.2 Syntax Reference

```
<name> <pattern>
  | <guard_1> = <expr_1>
  | <guard_2> = <expr_2>
  | otherwise = <expr_default>
```

`otherwise` is defined as `True` and serves as the default case.

### 7.3 Example: Sign Classification

```haskell
sign x
  | x > 0     = 1
  | x < 0     = -1
  | otherwise = 0

main = print (map sign [-3, 0, 5])
```

```text
[-1,0,1]
```

### 7.4 Guards vs. `if-then-else`

| Feature | Guards | `if-then-else` |
| :--- | :--- | :--- |
| Multiple conditions | Natural (`\|`) | Nested expressions |
| Pattern + condition | Combined in one equation | Requires `case` or pattern in `if` |
| Readability for $\geq 3$ branches | Preferred | Degrades quickly |
| Lazy | Yes | Yes |

```haskell
-- Grade classification with guards.
grade n
  | n >= 90   = 'A'
  | n >= 80   = 'B'
  | n >= 70   = 'C'
  | otherwise = 'F'
```

---

## 8. Comparison with Python

### 8.1 Side-by-Side Syntax

| Task | Python | Haskell |
| :--- | :--- | :--- |
| Squares 1–10 | `[x**2 for x in range(1, 11)]` | `[x^2 \| x <- [1..10]]` |
| Evens 1–20 | `[x for x in range(1, 21) if x % 2 == 0]` | `[x \| x <- [1..20], x \`mod\` 2 == 0]` |
| Pairs (Cartesian) | `[(x,y) for x in range(1,4) for y in range(1,4)]` | `[(x,y) \| x <- [1..3], y <- [1..3]]` |
| Infinite stream | Generator: `(x for x in count())` | `[1..]` with `take` |

### 8.2 Semantic Differences

| Property | Python Comprehension | Haskell Comprehension |
| :--- | :--- | :--- |
| Evaluation | Eager (list) or lazy (generator) | Always lazy |
| Type | Homogeneous list (typed objects) | Homogeneous static type |
| Infinite source | Generator required | Native `[n..]` syntax |
| Output | `[...]` or `(...)` generator | Always list (or monad generalization) |

```python
# Python: eager list comprehension.
squares = [x**2 for x in range(1, 11)]
evens = [x for x in range(1, 21) if x % 2 == 0]
pairs = [(x, y) for x in range(1, 4) for y in range(1, 4)]
```

```haskell
-- Haskell equivalents.
squares = [x^2 | x <- [1..10]]
evens   = [x | x <- [1..20], x `mod` 2 == 0]
pairs   = [(x, y) | x <- [1..3], y <- [1..3]]
```

---

## Common Errors and Gotchas

### Error 1: Forgetting to Bound Infinite Lists

**Cause:** Passing an infinite list to a function that demands all elements (`sum`, `length`, `reverse`).

```haskell
-- sum [1..]   -- Diverges.
```

**Resolution:** Apply `take n` first: `sum (take 100 [1..])`.

### Error 2: Off-by-One in Range Syntax

**Cause:** `[1..10]` is inclusive on both ends (10 elements), unlike Python's `range(1, 10)` which excludes 10.

| Haskell | Python Equivalent | Elements |
| :--- | :--- | :--- |
| `[1..10]` | `range(1, 11)` | 1 through 10 |
| `[1..10)` | — | Invalid Haskell syntax |

**Resolution:** Remember Haskell ranges are **inclusive** at both endpoints.

### Error 3: Non-Exhaustive Pattern Match

**Cause:** Function defined only for non-empty lists but called with `[]`.

```haskell
second (x:y:_) = y
-- second []   -- Runtime error: Non-exhaustive patterns.
```

**Resolution:** Add a guard equation for `[]` or return `Maybe b`.

---

## Solved Exercises

### Exercise 1: Basic Squares Comprehension

**Problem:** Write a comprehension for squares of integers from 1 to 10 and list the result.

**Solution:**

```haskell
[x^2 | x <- [1..10]]
```

1. Generator binds `x` to each value 1 through 10.
2. Output: $1, 4, 9, \ldots, 100$.

```text
[1,4,9,16,25,36,49,64,81,100]
```

---

### Exercise 2: Filtered Evens

**Problem:** Produce all even numbers between 1 and 20 using a predicate.

**Solution:**

```haskell
[x | x <- [1..20], x `mod` 2 == 0]
```

1. Generator produces candidates 1–20.
2. Predicate `x mod 2 == 0` retains only even values.

```text
[2,4,6,8,10,12,14,16,18,20]
```

---

### Exercise 3: Cartesian Pairs

**Problem:** List all pairs $(x, y)$ where $x, y \in \{1, 2, 3\}$.

**Solution:**

```haskell
[(x, y) | x <- [1..3], y <- [1..3]]
```

1. Outer generator: 3 values for `x`.
2. Inner generator: 3 values for `y` per `x`.
3. Total: $3 \times 3 = 9$ pairs.

```text
[(1,1),(1,2),(1,3),(2,1),(2,2),(2,3),(3,1),(3,2),(3,3)]
```

---

### Exercise 4: Dependent Generator

**Problem:** Generate list `[(1,1), (2,1), (2,2), (3,1), (3,2), (3,3)]` using a comprehension.

**Solution:**

```haskell
[(x, y) | x <- [1..3], y <- [1..x]]
```

| `x` | `y` range | Pairs |
| :--- | :--- | :--- |
| 1 | `[1..1]` | `(1,1)` |
| 2 | `[1..2]` | `(2,1), (2,2)` |
| 3 | `[1..3]` | `(3,1), (3,2), (3,3)` |

---

### Exercise 5: First Eight Primes via Sieve

**Problem:** Trace `take 8 (sieve [2..])` through the first three filtering steps.

**Solution:**

1. `sieve [2..]` → `2 : sieve (filter mod 2) [3,4,5,...]` → `[3,5,7,9,...]`.
2. Next head: `3`; filter multiples of 3 → `[5,7,11,13,...]`.
3. Next head: `5`; filter multiples of 5 → `[7,11,13,17,...]`.
4. Continuing: primes 7, 11, 13, 17, ...

```text
[2,3,5,7,11,13,17,19]
```

---

### Exercise 6: Fibonacci via `zipWith`

**Problem:** Evaluate `take 7 (0 : 1 : zipWith (+) fibs (tail fibs))` where `fibs` is the infinite list being defined.

**Solution:**

1. `fibs = 0 : 1 : ...`
2. `tail fibs = 1 : ...`
3. `zipWith (+) [0,1,...] [1,...] = [1, 2, 3, 5, ...]`
4. `fibs = [0, 1, 1, 2, 3, 5, 8, ...]`

```text
[0,1,1,2,3,5,8]
```

---

### Exercise 7: Pattern Match — `length`

**Problem:** Trace `len [5, 10, 15]` for:

```haskell
len []     = 0
len (_:xs) = 1 + len xs
```

**Solution:**

1. `len [5,10,15]` = `1 + len [10,15]`.
2. `= 1 + 1 + len [15]`.
3. `= 1 + 1 + 1 + len []`.
4. `= 1 + 1 + 1 + 0 = 3`.

---

### Exercise 8: Guards — Absolute Value

**Problem:** Define `abs' n` using guards and evaluate `abs' (-7)` and `abs' 0`.

**Solution:**

```haskell
abs' n
  | n < 0     = -n
  | otherwise = n
```

1. `abs' (-7)`: guard `n < 0` is `True` → `-(-7) = 7`.
2. `abs' 0`: first guard `False`; `otherwise` → `0`.

```text
7
0
```

---

## Exam Tip: Comprehension and Pattern Desugaring

**List comprehensions desugar to `do` notation** (and ultimately to `map`/`concat`/`filter`):

```haskell
[e | x <- xs, p x]  --  concat (map (\x -> if p x then [e] else []) xs)
```

For exam questions:

1. **Count elements:** A comprehension with generators `x <- [1..m], y <- [1..n]` produces $m \times n$ elements (before predicates).
2. **Predicate effect:** Each predicate roughly halves or reduces proportionally — trace with a small example rather than guessing.
3. **Pattern match order:** Equations are tried top-to-bottom; guards within one equation are also top-to-bottom. First match wins.
4. **Range inclusivity:** `[a..b]` includes both endpoints. Step syntax `[a, a+d..b]` stops at the largest value $\leq b$ in the arithmetic sequence.