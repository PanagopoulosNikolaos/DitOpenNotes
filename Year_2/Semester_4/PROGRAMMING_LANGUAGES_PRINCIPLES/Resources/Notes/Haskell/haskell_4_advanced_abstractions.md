# Haskell — Advanced Abstractions

*Prerequisite: haskell_3_higher_order_functions_type_system.md — Typeclasses, ADTs, `Maybe`; haskell_1_basics_pure_functions.md — Referential transparency and equational reasoning.*

Beyond its core type system, Haskell provides a hierarchy of abstractions — Functor, Applicative, Monad, Monoid — that capture common patterns of computation over wrapped values and composable operations. This file defines each abstraction formally, relates them in the typeclass hierarchy, introduces the Zipper data structure for efficient navigation in immutable trees, and covers equational reasoning and structural induction as proof techniques for program correctness.

---

## 1. Functor

### 1.1 Definition and Scope

A **Functor** is a type constructor $F$ equipped with a mapping operation `fmap` that lifts a function $a \to b$ to a function $F a \to F b$ while preserving structure.

**Typeclass:**

```
class Functor f where
  fmap :: (a -> b) -> f a -> f b
```

### 1.2 Functor Laws

For all valid instances, `fmap` must satisfy:

1. **Identity:** $\text{fmap id} = \text{id}$
2. **Composition:** $\text{fmap (f . g)} = \text{fmap f . fmap g}$

### 1.3 Standard Instances

| Functor | Type | `fmap` Behavior |
| :--- | :--- | :--- |
| `[]` | `[a]` | `map` — apply to each element |
| `Maybe` | `Maybe a` | `Nothing` stays `Nothing`; `Just x` → `Just (f x)` |
| `(->) r` | `r -> a` | Pre-compose: `fmap f g = f . g` |
| `(a,)` | `(a, b)` | Map over second component |

```haskell
-- fmap over a list.
main = print (fmap (*2) [1, 2, 3])

-- fmap over Maybe.
main2 = print (fmap (*2) (Just 5), fmap (*2) Nothing)
```

```text
[2,4,6]
(Just 10,Nothing)
```

### 1.4 Infix Operator

`fmap` is also written as `<$>`:

```haskell
(*2) <$> [1, 2, 3]    -- [2, 4, 6]
(+1) <$> Just 10      -- Just 11
```

---

## 2. Applicative Functor

### 2.1 Definition and Scope

An **Applicative Functor** extends `Functor` with application of wrapped functions to wrapped values. It captures **independent** effectful computations (no dependency between successive results).

**Typeclass:**

```
class Functor f => Applicative f where
  pure  :: a -> f a
  (<*>) :: f (a -> b) -> f a -> f b
```

### 2.2 Applicative Laws

1. **Identity:** `pure id <*> v = v`
2. **Homomorphism:** `pure f <*> pure x = pure (f x)`
3. **Interchange:** `u <*> pure y = pure ($ y) <*> u`
4. **Composition:** `pure (.) <*> u <*> v <*> w = u <*> (v <*> w)`

### 2.3 Behavioral Description

| Expression | Meaning |
| :--- | :--- |
| `pure x` | Lift a pure value into the applicative context |
| `f <*> x` | Apply wrapped function `f` to wrapped value `x` |
| `(+)` `<$>`` `Just 3` `<*>`` `Just 5` | `Just 8` — both present |
| `(+)` `<$>`` `Just 3` `<*>`` `Nothing` | `Nothing` — either missing yields `Nothing` |

```haskell
-- Combining two Maybe values independently.
addMay :: Maybe Int -> Maybe Int -> Maybe Int
addMay mx my = (+) <$> mx <*> my

main = do
  print (addMay (Just 3) (Just 5))
  print (addMay (Just 3) Nothing)
```

```text
Just 8
Nothing
```

### 2.4 List Applicative — Cartesian Application

For lists, `<*>` distributes: every function in the left list is applied to every value in the right list:

```haskell
main = print ((+) <$> [1, 2] <*> [10, 20])
```

```text
[11,21,12,22]
```

This is equivalent to `[(+1), (+2)]` applied to `[10, 20]` producing $2 \times 2 = 4$ results.

---

## 3. Monad

### 3.1 Definition and Scope

A **Monad** extends `Applicative` with `>>=` (bind), enabling **sequential** computations where later steps depend on earlier results. Monads isolate side effects (notably I/O) within a typed context.

**Typeclass:**

```
class Applicative m => Monad m where
  return :: a -> m a          -- same as pure
  (>>=)  :: m a -> (a -> m b) -> m b
```

### 3.2 Monad Laws

1. **Left identity:** `return x >>= f = f x`
2. **Right identity:** `m >>= return = m`
3. **Associativity:** `(m >>= f) >>= g = m >>= (\x -> f x >>= g)`

### 3.3 `Maybe` Monad — Chained Dependent Steps

```haskell
safeComputation :: Int -> Int -> Maybe Int
safeComputation x y = do
  a <- safeDiv 10 x      -- Nothing if x == 0
  b <- safeDiv a y       -- Nothing if y == 0
  return (b + 1)

-- where safeDiv _ 0 = Nothing; safeDiv a b = Just (a / b)
```

| Input | Step 1 | Step 2 | Result |
| :--- | :--- | :--- | :--- |
| `x=2, y=5` | `Just 5.0` | `Just 1.0` | `Just 2.0` |
| `x=0, y=5` | `Nothing` | (skipped) | `Nothing` |
| `x=2, y=0` | `Just 5.0` | `Nothing` | `Nothing` |

```haskell
main = print (safeComputation 2 5)
```

```text
Just 2.0
```

### 3.4 `IO` Monad — Side Effect Isolation

I/O actions have type `IO a`. The `IO` monad sequences effectful operations while keeping pure code referentially transparent:

```haskell
main :: IO ()
main = do
  putStrLn "Enter a number:"
  line <- getLine
  putStrLn ("You entered: " ++ line)
```

Pure functions cannot call `getLine` directly. The type system enforces that side effects occur only within `IO`.

### 3.5 Functor / Applicative / Monad Hierarchy

```
Functor          fmap    :: (a -> b) -> f a -> f b
    |
Applicative    pure    :: a -> f a
               (<*>)  :: f (a -> b) -> f a -> f b
    |
Monad          (>>=)   :: m a -> (a -> m b) -> m b
```

| Abstraction | Dependency Between Steps | Typical Use |
| :--- | :--- | :--- |
| Functor | N/A (single `fmap`) | Transform wrapped value |
| Applicative | Independent | Combine parallel results |
| Monad | Dependent (later needs earlier) | Sequential pipelines, I/O |

> **[Key Insight]** Every monad is an applicative (when `(<*>)` is defined as `mf <*> mx = mf >>= \f -> mx >>= \x -> return (f x)`), but not every applicative arises from a monad. The exam focus is recognizing **when** `>>=` is needed: whenever the next action depends on the unwrapped value of the previous one.

---

## 4. Monoid

### 4.1 Definition and Scope

A **Monoid** is a set $M$ with an associative binary operation $\oplus$ and an identity element $e$:

$$
\forall a, b, c \in M: \quad (a \oplus b) \oplus c = a \oplus (b \oplus c)
$$

$$
\forall a \in M: \quad e \oplus a = a \oplus e = a
$$

**Typeclass:**

```
class Monoid a where
  mempty  :: a
  mappend :: a -> a -> a    -- written as `<>`
```

### 4.2 Standard Instances

| Monoid | `mempty` | `mappend` (`<>`) |
| :--- | :--- | :--- |
| `[a]` (lists) | `[]` | `++` (concatenation) |
| `Sum` (wrapper) | `Sum 0` | `Sum (a + b)` |
| `Product` (wrapper) | `Product 1` | `Product (a * b)` |
| `String` | `""` | `++` |

```haskell
import Data.Monoid

main = do
  print ([1,2] <> [3,4])                    -- [1,2,3,4]
  print (getSum (Sum 3 <> Sum 5))             -- 8
  print (getProduct (Product 3 <> Product 5)) -- 15
```

```text
[1,2,3,4]
8
15
```

### 4.3 `fold` and Monoid

`mconcat` folds a list of monoid values:

```haskell
mconcat ["ab", "cd", "ef"]   -- "abcdef"
mconcat [Sum 1, Sum 2, Sum 3] -- Sum 6 (with getSum)
```

---

## 5. Zipper

### 5.1 Definition and Scope

A **Zipper** is a data structure enabling efficient navigation and local modification in an immutable tree (or list) by maintaining a **focus** — the current position — together with a **context** (the path from the root, with "holes" marking where subtrees were removed).

### 5.2 List Zipper Model

For a list, a zipper consists of:

- **`focus`:** the element at the current position.
- **`left`:** elements to the left of focus (reversed).
- **`right`:** elements to the right of focus.

```
List: [1, 2, 3, 4, 5]
              ^
           focus = 3
left = [2, 1]  (reversed)
right = [4, 5]
```

### 5.3 Navigation Operations

| Operation | Effect |
| :--- | :--- |
| `goRight` | Move focus one position right; push old focus onto `left` |
| `goLeft` | Move focus one position left; pop from `left` |
| `update` | Replace focus value; original list unchanged elsewhere |
| `toList` | Reconstruct full list from zipper state |

```haskell
data ListZipper a = ListZipper [a] a [a]
  --                   reversed-left  focus  right

fromList :: [a] -> Maybe (ListZipper a)
fromList []    = Nothing
fromList (x:xs) = Just (ListZipper [] x xs)

goRight :: ListZipper a -> Maybe (ListZipper a)
goRight (ListZipper _ _ [])    = Nothing
goRight (ListZipper ls f (r:rs)) = Just (ListZipper (f:ls) r rs)

toList :: ListZipper a -> [a]
toList (ListZipper ls f rs) = reverse ls ++ [f] ++ rs
```

### 5.4 Trace: Navigate and Update

Starting from `[10, 20, 30, 40]`:

| Step | Operation | Focus | Full List |
| :--- | :--- | :--- | :--- |
| Init | `fromList` | `10` | `[10,20,30,40]` |
| 1 | `goRight` | `20` | `[10,20,30,40]` |
| 2 | `goRight` | `30` | `[10,20,30,40]` |
| 3 | update focus to `35` | `35` | `[10,20,35,40]` |

> **[Key Insight]** Zippers achieve $O(1)$ local navigation in immutable structures by storing the "one-hole context" explicitly. Without a zipper, updating element $i$ in an immutable list requires $O(n)$ copying.

---

## 6. Equational Reasoning

### 6.1 Concept Overview

**Equational reasoning** is a proof technique for Haskell programs based on referential transparency: any occurrence of an expression may be replaced by an equal expression without changing program behavior.

### 6.2 Proof by Reduction

Given:

```haskell
double x = x + x
```

Prove that `double (double 3) = 12`:

$$
\begin{aligned}
\text{double (double 3)}
  &= \text{double (3 + 3)}       & \text{(def. of double)} \\
  &= \text{double 6}             & \text{(arithmetic)} \\
  &= 6 + 6                       & \text{(def. of double)} \\
  &= 12                          & \text{(arithmetic)}
\end{aligned}
$$

### 6.3 Using Functor Laws

Prove `fmap id xs = xs` for lists by structural induction (see Section 7):

**Base case:** `fmap id [] = []` by definition of `fmap` on `[]`.

**Inductive case:** Assume `fmap id xs = xs`. Then:

$$
\text{fmap id (x : xs)} = \text{id x} : \text{fmap id xs} = x : xs
$$

---

## 7. Mathematical Induction on Data Structures

### 7.1 Structural Induction Principle

To prove property $P$ for all finite lists:

1. **Base case:** Prove $P([])$.
2. **Inductive step:** Assume $P(xs)$ (induction hypothesis); prove $P(x : xs)$.

If both hold, $P$ holds for all finite lists.

### 7.2 Example: Sum of `map f` Equals `f` Applied to Sum

**Claim:** For all finite lists `xs` of `Int`, `sum (map f xs) = f (sum xs)` when $f$ distributes over $+$ (e.g., `f x = x * 2`).

**Proof:**

**Base:** `sum (map f []) = sum [] = 0`. `f (sum []) = f 0`. For `f x = 2*x`, `f 0 = 0`. Holds.

**Step:** Assume `sum (map f xs) = f (sum xs)`.

$$
\begin{aligned}
\text{sum (map f (x : xs))}
  &= \text{sum (f x : map f xs)} \\
  &= f x + \text{sum (map f xs)} & \text{(def. sum)} \\
  &= f x + f(\text{sum xs})       & \text{(IH)} \\
  &= f(x + \text{sum xs})         & \text{(distributivity)} \\
  &= f(\text{sum (x : xs)})       & \text{(def. sum)}
\end{aligned}
$$

### 7.3 Induction on Natural Numbers

For recursive functions over `Nat` (defined as `Zero | Succ Nat`):

1. Prove $P(\text{Zero})$.
2. Prove $P(\text{Succ } n)$ assuming $P(n)$.

This mirrors induction on list length when the recursion is structural.

---

## 8. Abstraction Hierarchy Summary

| Abstraction | Core Operation | Laws | Example Instance |
| :--- | :--- | :--- | :--- |
| Functor | `fmap` | Identity, Composition | `[]`, `Maybe` |
| Applicative | `pure`, `<*>` | Identity, Homomorphism, Interchange, Composition | `Maybe`, `[]` |
| Monad | `>>=` | Left/right identity, Associativity | `Maybe`, `IO`, `[]` |
| Monoid | `mempty`, `<>` | Associativity, Identity | `[a]`, `Sum`, `String` |
| Zipper | `goLeft`, `goRight`, `update` | Reconstruction invariant | `ListZipper`, tree zippers |

---

## Common Errors and Gotchas

### Error 1: Using `<*>` When `>>=` Is Required

**Cause:** Trying to chain dependent `Maybe` computations with `<$>` and `<*>`.

```haskell
-- Cannot express: "divide 10 by x, then divide result by y" with pure Applicative
-- if y depends on the unwrapped result of the first division.
```

**Resolution:** Use `>>=` or `do` notation when later steps depend on earlier unwrapped values.

### Error 2: Confusing `return` with "return from function"

**Cause:** `return` in Haskell means `pure` — lift a value into a monad. It does not exit a function.

```haskell
f x = return (x + 1)   -- In Maybe: Just (x+1). In IO: produces an IO action.
```

**Resolution:** `return` = `pure`. Function exit is implicit (last expression) or via explicit pattern match.

### Error 3: Violating Monoid Laws

**Cause:** Defining a custom `Monoid` instance where `mappend` is not associative or `mempty` is not an identity.

```haskell
-- Invalid: "subtraction monoid" — not associative: (5-3)-2 /= 5-(3-2)
```

**Resolution:** Verify associativity and identity laws before declaring an instance.

---

## Solved Exercises

### Exercise 1: Functor — `fmap` on Lists

**Problem:** Evaluate `fmap (+1) (fmap (*2) [1, 2, 3])` using the composition law.

**Solution:**

1. By composition law: `fmap (+1) . fmap (*2) = fmap ((+1) . (*2))`.
2. `(+1) . (*2)` applied to `x` gives `2*x + 1`.
3. `fmap (\x -> 2*x + 1) [1,2,3]` = `[3, 5, 7]`.

```text
[3,5,7]
```

---

### Exercise 2: Applicative — Combining Maybes

**Problem:** Evaluate `(*) <$> Just 4 <*> Just 5` and `(*) <$> Just 4 <*> Nothing`.

**Solution:**

1. `Just 4` and `Just 5` both present: `Just (4 * 5) = Just 20`.
2. `Nothing` in second position: short-circuits to `Nothing`.

```text
Just 20
Nothing
```

---

### Exercise 3: List Applicative — Cartesian Product

**Problem:** Evaluate `[(*2), (+10)] <*> [1, 2]`.

**Solution:**

1. Apply `(*2)` to each: `[2, 4]`.
2. Apply `(+10)` to each: `[11, 12]`.
3. Result: `[2, 4, 11, 12]`.

```text
[2,4,11,12]
```

---

### Exercise 4: Monad Bind — Chained Division

**Problem:** Trace `Just 10 >>= (\x -> safeDiv x 2) >>= (\y -> safeDiv y 5)` where `safeDiv a 0 = Nothing`.

**Solution:**

1. `Just 10 >>= (\x -> safeDiv x 2)` → `safeDiv 10 2` → `Just 5.0`.
2. `Just 5.0 >>= (\y -> safeDiv y 5)` → `safeDiv 5.0 5` → `Just 1.0`.

```text
Just 1.0
```

---

### Exercise 5: Monoid — List Concatenation

**Problem:** Evaluate `mconcat [["a"], ["b", "c"], []]`.

**Solution:**

1. `["a"] <> ["b", "c"]` = `["a", "b", "c"]`.
2. `["a", "b", "c"] <> []` = `["a", "b", "c"]`.

```text
["a","b","c"]
```

---

### Exercise 6: Zipper Navigation

**Problem:** Starting from `[1, 2, 3]`, perform `goRight` twice and state the focus and `toList` result.

**Solution:**

1. `fromList [1,2,3]` → focus `1`, right `[2,3]`.
2. `goRight` → focus `2`, left `[1]`, right `[3]`.
3. `goRight` → focus `3`, left `[2,1]`, right `[]`.
4. `toList` = `reverse [2,1] ++ [3] ++ []` = `[1,2,3]`.

Focus after two `goRight` calls: `3`.

---

### Exercise 7: Equational Reasoning — `map`

**Problem:** Prove `map f (xs ++ ys) = map f xs ++ map f ys` for the base case `xs = []`.

**Solution:**

**Base case** (`xs = []`):

$$
\text{map f ([] ++ ys)} = \text{map f ys}
$$

$$
\text{map f [] ++ map f ys} = [] ++ \text{map f ys} = \text{map f ys}
$$

Both sides equal. Base case holds.

---

### Exercise 8: Structural Induction — Length of Reverse

**Problem:** State the base case and inductive step for proving `length (reverse xs) = length xs`.

**Solution:**

**Base case:** `xs = []`.

- LHS: `length (reverse []) = length [] = 0`.
- RHS: `length [] = 0`. Equal.

**Inductive step:** Assume `length (reverse xs) = length xs` for some `xs`. Prove for `x : xs`:

$$
\text{length (reverse (x : xs))} = \text{length (reverse xs ++ [x])} = \text{length (reverse xs)} + 1 = \text{length xs} + 1 = \text{length (x : xs)}
$$

The inductive step uses `length (as ++ bs) = length as + length bs`.

---

## Exam Tip: Choosing Functor vs. Applicative vs. Monad

**Decision flowchart for exam questions:**

1. **Single transformation inside a context?** → **Functor** (`fmap` / `<$>`).
2. **Multiple independent values in a context, combine with a function?** → **Applicative** (`pure` + `<*>`).
3. **Later step depends on unwrapped result of earlier step?** → **Monad** (`>>=` / `do`).
4. **Folding a collection with an associative operation and identity?** → **Monoid** (`mempty`, `<>`).
5. **Local edit in an immutable structure without full copy?** → **Zipper**.

**Proof questions:** Always state the **base case** and **inductive hypothesis** explicitly. Reference function definitions by name ("by def. of `map`"). One missing base case invalidates the entire inductive proof.