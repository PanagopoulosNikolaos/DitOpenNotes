# Exercises 02: Functional and Logic Programming Drills

This practice problem set provides worked exercises and step-by-step traces for Haskell higher-order functions and Prolog first-order unification and backtracking.

---

## Problem 1: Haskell Higher-Order Combinators

### Question
Given the standard definitions of `foldr` and `foldl`:

```haskell
foldr :: (a -> b -> b) -> b -> [a] -> b
foldr f z []     = z
foldr f z (x:xs) = f x (foldr f z xs)

foldl :: (b -> a -> b) -> b -> [a] -> b
foldl f z []     = z
foldl f z (x:xs) = foldl f (f z x) xs
```

1. Trace the step-by-step reduction of:
   ```haskell
   foldr (-) 0 [1, 2, 3, 4]
   ```
2. Trace the step-by-step reduction of:
   ```haskell
   foldl (-) 0 [1, 2, 3, 4]
   ```
3. Implement `map` using `foldr`.

---

### Solution

#### Part 1: foldr Reduction Trace
`foldr` associates from right to left:
$$1 - (2 - (3 - (4 - 0)))$$
Step-by-step:
- $4 - 0 = 4$
- $3 - 4 = -1$
- $2 - (-1) = 3$
- $1 - 3 = \mathbf{-2}$

#### Part 2: foldl Reduction Trace
`foldl` associates from left to right with accumulator:
$$((((0 - 1) - 2) - 3) - 4)$$
Step-by-step:
- $0 - 1 = -1$
- $-1 - 2 = -3$
- $-3 - 3 = -6$
- $-6 - 4 = \mathbf{-10}$

#### Part 3: Defining map with foldr
```haskell
mapFoldr :: (a -> b) -> [a] -> [b]
mapFoldr f = foldr (\x acc -> f x : acc) []
```

---

## Problem 2: Prolog Unification and Backtracking Trace

### Question
Consider the Prolog knowledge base:

```prolog
p(1, a).
p(2, b).
p(3, c).

q(a, apple).
q(b, banana).

rel(X, Y) :- p(X, Z), q(Z, Y).
```

Trace the exact sequence of subgoals, unifications, and backtracking steps evaluated by the SWI-Prolog interpreter for the query:

```prolog
?- rel(Num, Fruit).
```

---

### Solution
1. **Goal:** `rel(Num, Fruit)`.
   - Matches rule `rel(X, Y) :- p(X, Z), q(Z, Y)`.
   - Variable substitution: `Num = X`, `Fruit = Y`.
2. **Subgoal 1:** `p(X, Z)`.
   - Matches first fact: `p(1, a)`.
   - Bindings: $X \leftarrow 1, Z \leftarrow a$. Choice point saved at `p(2, b)`.
3. **Subgoal 2:** `q(a, Y)`.
   - Matches first fact: `q(a, apple)`.
   - Binding: $Y \leftarrow apple$.
   - **First Solution Found:**
     ```prolog
     Num = 1, Fruit = apple
     ```
4. **User requests next solution (`;`):**
   - Backtracks to Subgoal 2: No more clauses for `q(a, Y)`. Fails.
   - Backtracks to Subgoal 1: Resumes choice point.
5. **Subgoal 1 (retry):** Matches `p(2, b)`.
   - Bindings: $X \leftarrow 2, Z \leftarrow b$. Choice point saved at `p(3, c)`.
6. **Subgoal 2:** `q(b, Y)`.
   - Matches fact: `q(b, banana)`.
   - Binding: $Y \leftarrow banana$.
   - **Second Solution Found:**
     ```prolog
     Num = 2, Fruit = banana
     ```
7. **User requests next solution (`;`):**
   - Backtracks to Subgoal 2: No more clauses for `q(b, Y)`. Fails.
   - Backtracks to Subgoal 1: Resumes choice point.
8. **Subgoal 1 (retry):** Matches `p(3, c)`.
   - Bindings: $X \leftarrow 3, Z \leftarrow c$.
9. **Subgoal 2:** `q(c, Y)`.
   - No facts match `q(c, _)`. Subgoal fails.
10. **Backtrack exhausted:** No remaining choice points. Interpreter emits `false.`.

