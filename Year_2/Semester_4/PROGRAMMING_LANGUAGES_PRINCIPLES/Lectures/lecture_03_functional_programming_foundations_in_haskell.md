# Lecture 03: Functional Programming Foundations in Haskell

This lecture covers the functional programming paradigm using Haskell: pure functions, referential transparency, algebraic data types, pattern matching, higher-order functions (`map`, `filter`, `fold`), currying, and lazy evaluation.

---

## 1. Core Principles of the Functional Paradigm

Functional programming treats computation as the evaluation of mathematical functions, avoiding mutable state and side effects.

### 1.1 Pure Functions and Referential Transparency
- **Pure Function:** Given identical inputs, a pure function always returns identical outputs and causes zero observable side effects (no mutating global variables, modifying arguments, or performing unauthorized I/O).
- **Referential Transparency:** An expression can be replaced with its evaluated result without altering the program's behavior:
  $$f(x) + f(x) \equiv 2 \cdot f(x)$$

---

## 2. Haskell Type System and Type Inference

Haskell is statically typed and features the **Hindley-Milner** type inference algorithm, enabling compile-time type safety without requiring redundant type annotations.

### 2.1 Basic Types and Function Signatures
```haskell
-- Int (bounded) and Integer (arbitrary precision)
addTwo :: Int -> Int -> Int
addTwo x y = x + y

-- Boolean logic
isPositive :: Int -> Bool
isPositive x = x > 0
```

### 2.2 Currying and Partial Application
In Haskell, all functions technically take exactly one argument. A multi-parameter signature `a -> b -> c` is parsed as `a -> (b -> c)`:

```haskell
multiply :: Int -> Int -> Int
multiply x y = x * y

-- Partially applied function: (Int -> Int)
double :: Int -> Int
double = multiply 2
```

---

## 3. Algebraic Data Types and Pattern Matching

Algebraic Data Types (ADTs) combine sum types (tagged unions) and product types (tuples/records):

```haskell
-- Sum type: Shape is either a Circle or a Rectangle
data Shape = Circle Double
           | Rectangle Double Double
           deriving (Show, Eq)

-- Pattern matching function over Shape
area :: Shape -> Double
area (Circle r)        = pi * r * r
area (Rectangle w h)   = w * h
```

### 3.1 Recursive Data Structures: Binary Trees
```haskell
data Tree a = Empty
            | Node a (Tree a) (Tree a)
            deriving (Show, Eq)

-- Tree height calculation using pattern matching
treeHeight :: Tree a -> Int
treeHeight Empty        = 0
treeHeight (Node _ l r) = 1 + max (treeHeight l) (treeHeight r)
```

---

## 4. Higher-Order Functions

A higher-order function takes other functions as arguments or returns a function.

### 4.1 Fundamental List Combinators
- **`map`:** Transforms every element in a collection:
  ```haskell
  map :: (a -> b) -> [a] -> [b]
  -- map (*2) [1, 2, 3] yields [2, 4, 6]
  ```
- **`filter`:** Selects elements satisfying a boolean predicate:
  ```haskell
  filter :: (a -> Bool) -> [a] -> [a]
  -- filter even [1, 2, 3, 4] yields [2, 4]
  ```
- **`foldr` / `foldl`:** Reduces a list to a single accumulated value:
  ```haskell
  foldr :: (a -> b -> b) -> b -> [a] -> b
  -- foldr (+) 0 [1, 2, 3, 4] computes 1 + (2 + (3 + (4 + 0))) = 10
  ```

---

## 5. Lazy Evaluation (Call-by-Need)

Haskell uses **non-strict, lazy evaluation**: expressions are not evaluated until their results are genuinely demanded by a consumer (e.g., printing to screen or pattern matching).

### 5.1 Infinite Data Structures
Lazy evaluation allows defining theoretically infinite data structures:

```haskell
-- Infinite list of Fibonacci numbers
fibs :: [Integer]
fibs = 0 : 1 : zipWith (+) fibs (tail fibs)

-- Taking first 10 elements terminates normally
firstTenFibs :: [Integer]
firstTenFibs = take 10 fibs -- [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```
No infinite loop occurs because `take 10` forces only the first 10 elements.

