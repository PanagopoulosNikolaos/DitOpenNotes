# Tutorial 01: Functional Programming Patterns in Haskell

This laboratory tutorial introduces practical functional programming in Haskell using the Glasgow Haskell Compiler interactive environment (`GHCi`), focusing on recursive list functions, pattern matching, custom algebraic types, and higher-order combinators.

---

## 1. The GHCi Interactive Environment

Launch the Haskell interactive REPL:

```bash
ghci
```

### 1.1 Essential GHCi Commands
```text
-- Load or reload a Haskell source file (.hs)
Prelude> :load list_ops.hs
-- or shorthand:
Prelude> :l list_ops.hs

-- Inspect inferred type signature of an expression or function
Prelude> :type map
map :: (a -> b) -> [a] -> [b]

-- Inspect detailed typeclass info
Prelude> :info Eq

-- Exit GHCi
Prelude> :quit
```

---

## 2. Implementing Recursive List Functions

In a source file `list_ops.hs`:

```haskell
-- Computes the length of a list using structural pattern matching
customLength :: [a] -> Int
customLength []     = 0
customLength (_:xs) = 1 + customLength xs

-- Reverses a list using tail-recursive accumulator pattern
customReverse :: [a] -> [a]
customReverse list = helper list []
  where
    helper [] acc     = acc
    helper (x:xs) acc = helper xs (x : acc)

-- Quicksort algorithm expressed idiomatically in Haskell
quicksort :: (Ord a) => [a] -> [a]
quicksort []     = []
quicksort (p:xs) = quicksort smaller ++ [p] ++ quicksort larger
  where
    smaller = [x | x <- xs, x <= p]
    larger  = [x | x <- xs, x > p]
```

Test in `GHCi`:
```text
*Main> quicksort [34, 12, 89, 5, 23, 7]
[5, 7, 12, 23, 34, 89]
```

---

## 3. Custom Algebraic Data Types and Polymorphic Trees

```haskell
data BinarySearchTree a = Leaf
                        | Branch a (BinarySearchTree a) (BinarySearchTree a)
                        deriving (Show, Eq)

-- Inserting an element into an ordered BST
insertBST :: (Ord a) => a -> BinarySearchTree a -> BinarySearchTree a
insertBST item Leaf = Branch item Leaf Leaf
insertBST item (Branch val left right)
  | item < val  = Branch val (insertBST item left) right
  | item > val  = Branch val left (insertBST item right)
  | otherwise   = Branch val left right -- Element already exists

-- In-order traversal converting BST to sorted list
inOrder :: BinarySearchTree a -> [a]
inOrder Leaf                 = []
inOrder (Branch val left right) = inOrder left ++ [val] ++ inOrder right
```

---

## 4. Higher-Order Function Composition

The function composition operator `(.)` chains functions: `(f . g) x = f (g x)`.

```haskell
-- Sum the squares of all odd numbers in a list
sumOddSquares :: [Int] -> Int
sumOddSquares = sum . map (^2) . filter odd
```
Testing in `GHCi`:
```text
*Main> sumOddSquares [1, 2, 3, 4, 5]
35 -- Computes 1^2 + 3^2 + 5^2 = 1 + 9 + 25 = 35
```

