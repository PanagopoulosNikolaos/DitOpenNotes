# Haskell — Higher-Order Functions and Type System

*Prerequisite: haskell_1_basics_pure_functions.md — Recursion, `map`, `filter`, `foldr`; haskell_2_list_comprehensions_pattern_matching.md — Pattern matching and guards.*

Haskell treats functions as first-class values: they can be passed as arguments, stored in data structures, and returned from other functions. Combined with automatic currying and Hindley-Milner type inference, this yields a concise higher-order programming style. This file covers currying, partial application, the static type system, typeclasses (`Show`, `Read`, `Bounded`), algebraic data types, and the `Maybe` type for null-safe computation.

---

## 1. First-Class Functions

### 1.1 Concept Overview

A **first-class function** is a function that enjoys the same privileges as any other value: it can be bound to a name, passed as an argument, returned from a function, and stored in a data structure.

### 1.2 Behavioral Description

| Capability | Example |
| :--- | :--- |
| Bind to name | `f = (+1)` |
| Pass as argument | `map (*2) [1,2,3]` |
| Return from function | `mkAdder n = \x -> n + x` |
| Store in list | `[(+1), (*2), (^2)]` |

```haskell
applyTwice :: (a -> a) -> a -> a
applyTwice f x = f (f x)

main = print (applyTwice (*2) 3)
```

```text
12
```

### 1.3 Function Type Notation

The type `a -> b -> c` is right-associative:

$$
(a \to b) \to c \quad \text{is written} \quad a \to b \to c
$$

meaning a function taking `a`, returning a function `b -> c` (curried form).

---

## 2. Currying

### 2.1 Concept Overview

In Haskell, **every function takes exactly one argument** and returns either a value or another function. A multi-argument function is syntactic sugar for a chain of single-argument functions.

### 2.2 Formal Model

A function of two arguments:

$$
f : A \times B \to C
$$

is represented as:

$$
f : A \to (B \to C)
$$

Application is left-associative: `f x y` means `(f x) y`.

### 2.3 Uncurrying Equivalence

```haskell
-- These are equivalent:
add :: Int -> Int -> Int
add x y = x + y

-- Desugared (explicit lambda):
add' :: Int -> Int -> Int
add' = \x -> \y -> x + y
```

| Expression | Type after step | Result |
| :--- | :--- | :--- |
| `add` | `Int -> Int -> Int` | Function awaiting first `Int` |
| `add 3` | `Int -> Int` | Function awaiting second `Int` |
| `add 3 5` | `Int` | `8` |

```haskell
main = do
  print (add 3 5)
  print ((add 3) 5)
```

```text
8
8
```

> **[Key Insight]** Currying enables **partial application** without any special syntax. `add 3` is a valid function of type `Int -> Int` that adds 3 to its argument.

---

## 3. Partial Application

### 3.1 Concept Overview

**Partial application** supplies fewer arguments than the function arity, producing a new function that awaits the remaining arguments.

### 3.2 Syntax Reference

```
<function> <arg_1> ... <arg_k>    -- where k < arity, yields a new function
```

### 3.3 Examples

```haskell
add :: Int -> Int -> Int
add x y = x + y

addFive :: Int -> Int
addFive = add 5          -- Partially applied: awaits one more Int.

mult :: Int -> Int -> Int -> Int
mult x y z = x * y * z

double :: Int -> Int
double = mult 2          -- Awaits y and z: mult 2 y z.

main = do
  print (addFive 10)     -- 15
  print (double 3 4)     -- 24
```

```text
15
24
```

### 3.4 Partial Application with Operators

Infix operators can be partially applied using **sections**:

| Section | Meaning | Example |
| :--- | :--- | :--- |
| `(+1)` | `\x -> x + 1` | `map (+1) [1,2,3]` |
| `(2*)` | `\x -> 2 * x` | `map (2*) [1,2,3]` |
| (`mod` 2) | `\x -> x mod 2` | `filter (`mod` 2 == 0) xs` |

```haskell
main = print (map (+1) [10, 20, 30])
```

```text
[11,21,31]
```

---

## 4. Static Type Inference

### 4.1 Concept Overview

Haskell uses **Hindley-Milner type inference**: the compiler deduces the most general type of every expression without requiring explicit annotations (though annotations are permitted and sometimes necessary). Type checking occurs at **compile time**; well-typed programs cannot fail with type errors at runtime.

### 4.2 Type Inference Rules (Simplified)

| Expression | Inferred Type | Reason |
| :--- | :--- | :--- |
| `5` | `Num a => a` | Polymorphic numeric literal |
| `[1,2,3]` | `[Integer]` | Default numeric type |
| `['a','b']` | `[Char]` | Homogeneous list |
| `\x -> x + 1` | `Num a => a -> a` | `+` requires `Num` |
| `\x -> not x` | `Bool -> Bool` | `not` is `Bool -> Bool` |

```haskell
-- Type annotation (optional but documents intent).
double :: Int -> Int
double x = x * 2

-- Polymorphic identity.
id' x = x          -- Type: a -> a

main = print (double 5)
```

```text
10
```

### 4.3 Polymorphism

A **polymorphic** type contains type variables (written in lowercase: `a`, `b`):

```haskell
-- length works on any list, regardless of element type.
-- length :: [a] -> Int
```

| Function | Type | Polymorphic? |
| :--- | :--- | :--- |
| `length` | `[a] -> Int` | Yes (over element type) |
| `id` | `a -> a` | Yes (fully polymorphic) |
| `(+)` | `Num a => a -> a -> a` | Constrained polymorphism |
| `tail` | `[a] -> [a]` | Yes |

### 4.4 Type Error Example

```haskell
-- broken = 'a' + 1   -- Compile error: Char is not Num.
```

The compiler rejects programs where no valid type assignment exists.

---

## 5. Typeclasses

### 5.1 Concept Overview

A **typeclass** is an interface specifying a set of operations that types may support. A **type instance** declares that a particular type implements the interface. Typeclasses enable ad-hoc polymorphism: one function name (`show`, `read`, etc.) with type-specific implementations.

**Syntax:**

```
class <ClassName> <vars> where
  <method> :: <type>

instance <ClassName> <ConcreteType> where
  <method> = <implementation>
```

### 5.2 `Show` — Convert to String

| Property | Value |
| :--- | :--- |
| Method | `show :: a -> String` |
| Purpose | Serialize a value to a `String` for display |
| Constraint | `Show a =>` in type signatures |

```haskell
main = do
  print (show 42)        -- Uses Show instance for Int.
  print (show [1,2,3])   -- Uses Show instance for [Int].
```

```text
"42"
"[1,2,3]"
```

`print` is defined as `putStrLn . show` and requires a `Show` constraint.

### 5.3 `Read` — Parse from String

| Property | Value |
| :--- | :--- |
| Method | `read :: Read a => String -> a` |
| Purpose | Parse a `String` into a typed value |
| Risk | Fails at runtime on malformed input |

```haskell
main = do
  print (read "42" :: Int)
  print (read "[1,2,3]" :: [Int])
```

```text
42
[1,2,3]
```

### 5.4 `Bounded` — Min/Max Values

| Property | Value |
| :--- | :--- |
| Methods | `minBound :: a`, `maxBound :: a` |
| Purpose | Provide minimum and maximum representable values |
| Applicable types | `Int`, `Char`, `Bool`, tuples of bounded types |

```haskell
main = do
  print (minBound :: Int)
  print (maxBound :: Char)
  print (minBound :: Bool)
```

```text
-9223372036854775808
'\1114111'
False
```

### 5.5 Typeclass Summary Table

| Typeclass | Key Method(s) | Constraint Meaning |
| :--- | :--- | :--- |
| `Eq` | `(==)`, `(/=)` | Values can be compared for equality |
| `Ord` | `(<)`, `(>)`, `compare` | Values can be totally ordered |
| `Show` | `show` | Values can be rendered as strings |
| `Read` | `read` | Values can be parsed from strings |
| `Bounded` | `minBound`, `maxBound` | Type has finite extrema |
| `Enum` | `toEnum`, `fromEnum` | Type can be enumerated |
| `Num` | `(+)`, `(*)`, `negate` | Numeric operations |

---

## 6. Algebraic Data Types

### 6.1 Concept Overview

An **algebraic data type (ADT)** is a composite type defined by listing its possible **constructors**. Each constructor carries zero or more typed fields. ADTs generalize enums, structs, and tagged unions from imperative languages.

### 6.2 Syntax Reference

```
data <TypeName> <type_params> = <Constructor1> <field_types>
                              | <Constructor2> <field_types>
                              | ...
```

### 6.3 Product and Sum Types

**Product type** (one constructor, multiple fields — like a struct):

```haskell
data Point = Point Int Int   -- Product: Point requires Int and Int.
```

**Sum type** (multiple constructors — like a tagged union):

```haskell
data Shape = Circle Double
           | Rectangle Double Double
```

| Constructor | Fields | Meaning |
| :--- | :--- | :--- |
| `Circle` | `Double` (radius) | A circle |
| `Rectangle` | `Double`, `Double` (w, h) | A rectangle |

```haskell
area :: Shape -> Double
area (Circle r)       = pi * r^2
area (Rectangle w h)  = w * h

main = print (area (Circle 2), area (Rectangle 3 4))
```

```text
(12.566370614359172,12.0)
```

### 6.4 Recursive ADTs

```haskell
data List a = Nil | Cons a (List a)
```

This mirrors the built-in list type: `[]` is `Nil`, `(:)` is `Cons`.

---

## 7. The `Maybe` Type

### 7.1 Concept Overview

`Maybe a` is a sum type representing an optional value of type `a`. It replaces null pointers with an explicit, type-safe construction:

$$
\text{Maybe } a = \text{Nothing} \mid \text{Just } a
$$

### 7.2 Definition and Type

```haskell
data Maybe a = Nothing | Just a
```

| Constructor | Meaning | Example |
| :--- | :--- | :--- |
| `Nothing` | Absence of value | Failed lookup |
| `Just x` | Presence of value `x` | Successful lookup |

### 7.3 Safe Division

```haskell
safeDiv :: Double -> Double -> Maybe Double
safeDiv _ 0 = Nothing
safeDiv x y = Just (x / y)

main = do
  print (safeDiv 10 2)
  print (safeDiv 10 0)
```

```text
Just 5.0
Nothing
```

### 7.4 Pattern Matching on `Maybe`

```haskell
fromMaybe :: a -> Maybe a -> a
fromMaybe defaultVal Nothing  = defaultVal
fromMaybe _         (Just x)  = x

main = print (fromMaybe 0 Nothing, fromMaybe 0 (Just 42))
```

```text
(0,42)
```

### 7.5 `Maybe` vs. Null in Imperative Languages

| Property | `Maybe a` (Haskell) | `null` (Java, C) |
| :--- | :--- | :--- |
| Type safety | `Nothing` is not `Just a` | Any reference can be null |
| Compiler enforcement | Must pattern-match or handle | NullPointerException at runtime |
| Composition | Functor/Monad instances | Manual null checks |

> **[Key Insight]** Functions that can fail should return `Maybe a` (or `Either e a` for error details) rather than using sentinel values like `-1` or `null`. The type system forces callers to handle both cases.

---

## Common Errors and Gotchas

### Error 1: Confusing `($)` with `($)` Application and Composition

**Cause:** Mixing up `f $ x` (apply with low precedence) and `f . g` (compose).

```haskell
-- ($)  :: (a -> b) -> a -> b       -- application
-- (.)  :: (b -> c) -> (a -> b) -> a -> c  -- composition

-- sum . map (*2) $ [1,2,3]  -- sum (map (*2) [1,2,3]) = 12
```

**Resolution:** `f . g` builds a new function; `f $ x` applies `f` to `x` with minimal precedence.

### Error 2: Monomorphism Restriction

**Cause:** A top-level binding without explicit type annotation may be monomorphized to a default type.

```haskell
-- defaultNum = 5       -- May default to Integer, not polymorphic Num a.
-- defaultNum :: Num a => a
-- defaultNum = 5
```

**Resolution:** Add explicit type signature when polymorphism is needed at the top level.

### Error 3: `Read` Without Type Annotation

**Cause:** `read "42"` has type `Read a => a`; the compiler cannot infer which `a`.

```haskell
-- n = read "42"   -- Ambiguous type.
n = read "42" :: Int
```

**Resolution:** Always annotate the expected type: `read "42" :: Int`.

---

## Solved Exercises

### Exercise 1: Currying Trace

**Problem:** Trace the types at each step of `mult 2 3 4` where `mult x y z = x * y * z`.

**Solution:**

1. `mult :: Int -> Int -> Int -> Int`.
2. `mult 2 :: Int -> Int -> Int`.
3. `mult 2 3 :: Int -> Int`.
4. `mult 2 3 4 :: Int` → $2 \times 3 \times 4 = 24$.

```text
24
```

---

### Exercise 2: Partial Application

**Problem:** Given `power x y = x ^ y`, evaluate `map (power 2) [1,2,3,4]`.

**Solution:**

1. `power 2 :: Int -> Int` — raises 2 to a given exponent.
2. `power 2 1 = 2`, `power 2 2 = 4`, `power 2 3 = 8`, `power 2 4 = 16`.

```text
[2,4,8,16]
```

---

### Exercise 3: Type Inference

**Problem:** Infer the type of `f g x = g (g x)`.

**Solution:**

1. `g` is applied to `x`, so `g :: a -> a` for some `a`.
2. `g (g x)` applies `g` again, so the output type matches: `g :: a -> a`.
3. `f` takes `g` and `x`: `f :: (a -> a) -> a -> a`.

---

### Exercise 4: `Show` and `Read` Round-Trip

**Problem:** Evaluate `read (show [True, False]) :: [Bool]`.

**Solution:**

1. `show [True, False]` → `"[True,False]"`.
2. `read "[True,False]" :: [Bool]` → `[True, False]`.

```text
[True,False]
```

---

### Exercise 5: `Bounded` Values

**Problem:** What are `minBound :: Word` and `maxBound :: Word`? (Word is unsigned.)

**Solution:**

1. `Word` is an unsigned machine word.
2. `minBound :: Word` = `0`.
3. `maxBound :: Word` = $2^{64} - 1$ on 64-bit systems (or platform-dependent).

---

### Exercise 6: ADT Pattern Match

**Problem:** Define `isCircle :: Shape -> Bool` and evaluate for `Circle 5` and `Rectangle 1 2`.

**Solution:**

```haskell
isCircle (Circle _) = True
isCircle _          = False
```

1. `isCircle (Circle 5)` → `True`.
2. `isCircle (Rectangle 1 2)` → `False`.

---

### Exercise 7: `Maybe` Chaining

**Problem:** Implement `safeHead :: [a] -> Maybe a` and evaluate `safeHead []` and `safeHead [7,8,9]`.

**Solution:**

```haskell
safeHead []    = Nothing
safeHead (x:_) = Just x
```

1. `safeHead []` → `Nothing`.
2. `safeHead [7,8,9]` → `Just 7`.

---

### Exercise 8: Higher-Order Composition

**Problem:** Evaluate `(map (*3) . filter even) [1..8]` step by step.

**Solution:**

1. `filter even [1..8]` → `[2,4,6,8]`.
2. `map (*3) [2,4,6,8]` → `[6,12,18,24]`.

```text
[6,12,18,24]
```

---

## Exam Tip: Reading Haskell Types

**The currying decode procedure** for any type signature:

1. **Count the arrows** right-to-left: `a -> b -> c -> d` is a 3-argument curried function.
2. **Identify constraints** before `=>`: `Eq a => a -> [a] -> Bool` requires `a` to support equality.
3. **Parenthesize mentally:** `a -> b -> c` means `a -> (b -> c)`, not `(a -> b) -> c`.
4. **Partial application arity:** For `f :: a -> b -> c -> d`, `f x` has type `b -> c -> d`; `f x y` has type `c -> d`.

**Most common exam trap:** Students read `Int -> Int -> Int` as "takes a tuple `(Int, Int)`". It does not — it takes one `Int` and returns `Int -> Int`. The uncurried form would be written with a tuple: `Int -> (Int -> Int)` vs. `(Int, Int) -> Int` (which requires `uncurry`).