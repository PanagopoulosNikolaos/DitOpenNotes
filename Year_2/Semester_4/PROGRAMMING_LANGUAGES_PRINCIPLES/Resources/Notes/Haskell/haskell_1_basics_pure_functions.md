# Haskell — Basics of Pure Functions

Haskell is a statically typed, purely functional programming language whose evaluation model is built on immutable data, referential transparency, and lazy (non-strict) evaluation. This file covers the foundational semantic properties that distinguish Haskell from imperative languages: no variable reassignment, substitution-based reasoning, thunk-based deferred computation, and iteration expressed exclusively through recursion and higher-order functions rather than mutable loops.

---

## 1. Immutable State

### 1.1 Concept Overview

In Haskell, a **binding** associates a name with a value for the duration of a scope. Once a name is bound, it cannot be reassigned. There is no `x = x + 1` semantics. "Changing state" means creating a **new value** derived from the old one, leaving the original intact.

### 1.2 Syntax Reference

```
<name> = <expression>
```

Bindings appear at the top level or inside a `let` / `where` clause. Function parameters are also immutable bindings within the function body.

### 1.3 Behavioral Description

| Property | Haskell | Imperative (e.g., C, Python) |
| :--- | :--- | :--- |
| Reassignment | Not permitted | `x = x + 1` is valid |
| Mutation of data structure | New structure created; old preserved | In-place update possible |
| Reasoning model | Value substitution | Sequential state changes |
| Concurrency safety | No shared mutable state by default | Requires explicit synchronization |

```haskell
-- A binding is permanent within its scope.
x = 5
y = x + 3
-- x = 10   -- Compile error: cannot rebind x.

-- "Increment" returns a new value; x is unchanged.
increment n = n + 1

main = print (increment x, x)
```

```text
(8,5)
```

### 1.4 Data Structure Immutability

Lists, tuples, and user-defined algebraic data types are immutable. Appending to a list constructs a new list; the original list's memory is never modified.

```haskell
original = [1, 2, 3]
extended = original ++ [4]

main = do
  print original    -- [1,2,3]
  print extended    -- [1,2,3,4]
```

```text
[1,2,3]
[1,2,3,4]
```

> **[Key Insight]** Immutability eliminates an entire class of bugs involving aliasing and unexpected side effects. When function `f` receives a list, the caller's list cannot be silently modified by `f`.

---

## 2. Referential Transparency

### 2.1 Formal Definition

An expression is **referentially transparent** if it can be replaced by its value without changing the program's observable behavior. In a pure Haskell function, the return value depends **only** on its arguments — no hidden reads of mutable global state, no I/O, no random number generation (outside the `IO` monad).

**Substitution principle:**

If $f : A \to B$ is pure and $x : A$, then the expression $f(x)$ may be replaced by its computed result $y$ everywhere in the program, and behavior is unchanged.

### 2.2 Behavioral Description

| Expression Type | Referentially Transparent? | Reason |
| :--- | :--- | :--- |
| `2 + 3` | Yes | Always evaluates to `5` |
| `length [1,2,3]` | Yes | Always `3` |
| `readFile "data.txt"` | No | Result depends on external file state |
| `randomR (1,6)` in `IO` | No | Nondeterministic side effect |

```haskell
-- Pure: same inputs always yield same outputs.
double x = x * 2

main = print (double 7 + double 7)
-- Equivalent to: print (14 + 14) by referential transparency.
```

```text
28
```

### 2.3 Equational Reasoning Preview

Because of referential transparency, function definitions can be manipulated algebraically:

$$
\text{double}(x) = x \times 2
$$

Therefore:

$$
\text{double}(3) + \text{double}(3) = (3 \times 2) + (3 \times 2) = 12
$$

This property is the foundation for correctness proofs covered in `haskell_4_advanced_abstractions.md`.

---

## 3. Lazy Evaluation and Thunks

### 3.1 Concept Overview

Haskell uses **lazy evaluation** (also called **non-strict** evaluation): an expression is not computed until its value is **demanded** by a consumer (e.g., pattern matching, printing, arithmetic). Before demand, the runtime stores a **thunk** — a suspended computation recording the expression and its environment.

### 3.2 Evaluation Model

```
Expression written          Thunk created (unevaluated)       Forced (evaluated)
──────────────────          ─────────────────────────         ──────────────────
f (g x)          →    [suspended: apply f to (g x)]   →    concrete value
[1..]            →    [suspended: enumerate from 1]   →    1 : [suspended tail]
```

### 3.3 Behavioral Description

| Construct | Strict? | Behavior |
| :--- | :--- | :--- |
| `let x = expensive in x + x` | Lazy | `expensive` computed at most once (sharing) |
| `fst (a, expensive)` | Lazy | `expensive` never computed |
| `take 3 [1..]` | Lazy | Only first 3 elements of infinite list forced |
| Pattern match on `undefined` | — | Diverges (bottom $\bot$) when forced |

```haskell
-- Infinite list: the tail is a thunk until demanded.
naturals = [1..]

-- Only three elements are ever computed.
firstThree = take 3 naturals

main = print firstThree
```

```text
[1,2,3]
```

### 3.4 Thunk Sharing

When the same thunk is referenced multiple times, GHC evaluates it once and shares the result:

```haskell
slow = sum [1..1000000]

main = print (slow + slow)
-- `slow` is computed once, not twice.
```

> **[Key Insight]** Lazy evaluation enables working with infinite data structures (`[1..]`, Fibonacci streams) safely, provided extraction is bounded (`take`, `head`, `foldr` with finite input). The exam pattern is: identify which sub-expressions are never forced and therefore incur zero cost.

---

## 4. No Loops — Recursion and Higher-Order Functions

### 4.1 Concept Overview

Haskell has no `for`, `while`, or `do-while` loop constructs for pure computation. Iteration is expressed through:

1. **Structural recursion** on data (lists, naturals).
2. **Higher-order functions** (`map`, `filter`, `foldr`, `foldl`) that abstract common recursion patterns.

### 4.2 Recursion Syntax Reference

```
<function_name> <pattern> = <base_case>
<function_name> <pattern> = <recursive_case>
```

### 4.3 Factorial via Recursion

```haskell
factorial 0 = 1
factorial n = n * factorial (n - 1)
```

| Call | Expansion | Result |
| :--- | :--- | :--- |
| `factorial 3` | `3 * factorial 2` | — |
| `factorial 2` | `2 * factorial 1` | — |
| `factorial 1` | `1 * factorial 0` | — |
| `factorial 0` | `1` | `1` |
| Back-substitute | `3 * 2 * 1 * 1` | `6` |

```haskell
main = print (factorial 5)
```

```text
120
```

### 4.4 Higher-Order Function Reference

| Function | Type (simplified) | Purpose |
| :--- | :--- | :--- |
| `map` | `(a -> b) -> [a] -> [b]` | Apply function to each element |
| `filter` | `(a -> Bool) -> [a] -> [a]` | Keep elements satisfying predicate |
| `foldr` | `(a -> b -> b) -> b -> [a] -> b` | Right-associative accumulation |
| `foldl` | `(b -> a -> b) -> b -> [a] -> b` | Left-associative accumulation |
| `(.)` | `(b -> c) -> (a -> b) -> a -> c` | Function composition |
| `($)` | `(a -> b) -> a -> b` | Low-precedence application |

```haskell
-- Sum of squares of evens from 1 to 10, without explicit recursion.
result = sum (map (^2) (filter even [1..10]))
  where even x = x `mod` 2 == 0

main = print result
```

```text
220
```

### 4.5 `foldr` vs. `foldl`

For a list $[a_1, a_2, \ldots, a_n]$ and operator $\oplus$:

$$
\text{foldr } \oplus \ z \ [a_1, \ldots, a_n] = a_1 \oplus (a_2 \oplus (\cdots \oplus (a_n \oplus z) \cdots))
$$

$$
\text{foldl } \oplus \ z \ [a_1, \ldots, a_n] = (\cdots ((z \oplus a_1) \oplus a_2) \cdots \oplus a_n)
$$

```haskell
main = do
  print (foldr (+) 0 [1, 2, 3])   -- 1 + (2 + (3 + 0)) = 6
  print (foldl (+) 0 [1, 2, 3])   -- ((0 + 1) + 2) + 3 = 6
```

```text
6
6
```

For non-associative operations, `foldr` and `foldl` produce different results:

```haskell
main = do
  print (foldr (/) 1 [8, 4, 2])   -- 8 / (4 / (2 / 1)) = 4.0
  print (foldl (/) 1 [8, 4, 2])   -- ((1 / 8) / 4) / 2 = 0.015625
```

```text
4.0
0.015625
```

---

## Common Errors and Gotchas

### Error 1: Attempting Variable Reassignment

**Cause:** Treating `=` as assignment rather than binding.

```haskell
count = 0
-- count = count + 1   -- Compile error.
```

**Resolution:** Use recursion or `fold` to accumulate. For monadic state (I/O counters), use `IORef` or the `State` monad — but pure code never rebinds.

### Error 2: Non-Terminating Lazy Expression

**Cause:** Demanding an infinite structure without bounding extraction.

```haskell
-- print (sum [1..])   -- Never terminates: sum forces every element.
```

**Resolution:** Use `take n` before aggregation, or define a finite input list.

### Error 3: Space Leak from `foldl`

**Cause:** `foldl` accumulates unevaluated thunks when the combining function is lazy in its first argument.

```haskell
-- foldl (+) 0 [1..1000000] may use O(n) memory.
-- foldl' (+) 0 [1..1000000] forces strictly; O(1) memory.
```

**Resolution:** Use the strict variant `foldl'` from `Data.List` for large numeric accumulations.

---

## Solved Exercises

### Exercise 1: Trace Immutable Binding

**Problem:** Predict the output of the following program.

```haskell
x = 10
f y = y + x
main = print (f 5, x)
```

**Solution:**

1. `x` is bound to `10` permanently.
2. `f 5` computes `5 + 10 = 15`.
3. `x` remains `10`.

```text
(15,10)
```

---

### Exercise 2: Referential Transparency Substitution

**Problem:** Rewrite `g 3 + g 3` using referential transparency, given `g x = x * x`.

**Solution:**

1. `g 3 = 3 * 3 = 9`.
2. Substitute: `g 3 + g 3` becomes `9 + 9`.
3. Result: `18`.

---

### Exercise 3: Lazy — What Gets Evaluated?

**Problem:** How many elements of `[1..]` does `length (take 5 [1..])` force?

**Solution:**

1. `take 5` demands exactly 5 elements from the infinite list.
2. `length` on a finite list of 5 elements forces all 5 cons cells.
3. Elements beyond the 5th remain as unforced thunks.

**Answer:** 5 elements.

---

### Exercise 4: Recursive Length

**Problem:** Define `myLength` recursively and evaluate `myLength [10, 20, 30]`.

```haskell
myLength []     = 0
myLength (_:xs) = 1 + myLength xs
```

**Solution:**

| Step | Call | Result |
| :--- | :--- | :--- |
| 1 | `myLength [10,20,30]` | `1 + myLength [20,30]` |
| 2 | `myLength [20,30]` | `1 + myLength [30]` |
| 3 | `myLength [30]` | `1 + myLength []` |
| 4 | `myLength []` | `0` |
| Back-sub | `1 + 1 + 1 + 0` | `3` |

---

### Exercise 5: `map` and `filter` Composition

**Problem:** Evaluate `sum (map (*2) (filter (>3) [1,2,3,4,5,6]))`.

**Solution:**

1. `filter (>3) [1,2,3,4,5,6]` → `[4,5,6]`.
2. `map (*2) [4,5,6]` → `[8,10,12]`.
3. `sum [8,10,12]` → `30`.

```text
30
```

---

### Exercise 6: `foldr` Expansion

**Problem:** Expand `foldr (:) [] [1, 2, 3]` step by step.

**Solution:**

1. `foldr (:) [] [1,2,3]` = `1 : (foldr (:) [] [2,3])`.
2. `= 1 : (2 : (foldr (:) [] [3]))`.
3. `= 1 : (2 : (3 : (foldr (:) [] [])))`.
4. `= 1 : (2 : (3 : []))` = `[1,2,3]`.

---

### Exercise 7: Recursive vs. `foldr` — Sum

**Problem:** Show that `sumList xs = foldr (+) 0 xs` for `xs = [3, 1, 4]`.

**Solution:**

Recursive definition:

```haskell
sumList []     = 0
sumList (x:xs) = x + sumList xs
```

Trace:

1. `sumList [3,1,4]` = `3 + sumList [1,4]` = `3 + (1 + sumList [4])` = `3 + (1 + (4 + 0))` = `8`.

`foldr (+) 0 [3,1,4]` = `3 + (1 + (4 + 0))` = `8`.

---

### Exercise 8: Thunk Sharing Cost

**Problem:** A function `expensive = product [1..100]`. If `main = print (expensive + expensive)`, how many times is `product [1..100]` computed under lazy evaluation with sharing?

**Solution:**

1. First reference to `expensive` creates a thunk for `product [1..100]`.
2. Second reference reuses the same thunk.
3. When `+` demands the value, the thunk is forced once; the result is shared.
4. **Answer:** Computed once.

---

## Exam Tip: Pure Function Property Checklist

When analyzing a Haskell function on paper, apply this three-point checklist:

1. **Immutability:** Are all bindings constant? Any attempted reassignment is a compile error, not a runtime surprise.
2. **Referential transparency:** Does the function's result depend only on its arguments? If it uses `IO`, `unsafePerformIO`, or reads mutable state, it is not referentially transparent.
3. **Laziness:** Which sub-expressions are forced? Trace demand from the outermost consumer inward. `take n` bounds infinite lists; `fst` ignores the second component entirely.

**Most common exam trap:** Students assume `foldl` and `foldr` are interchangeable. For non-associative operators (e.g., `/`, `(:)`), they produce structurally different — and often different-valued — results. Always expand one level of the fold before computing.