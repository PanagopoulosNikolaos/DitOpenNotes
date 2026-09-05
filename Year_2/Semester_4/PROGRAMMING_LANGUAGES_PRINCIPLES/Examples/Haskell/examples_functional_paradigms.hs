{- |
Module      : ExamplesFunctionalParadigms
Description : Foundational functional programming demonstrations in Haskell.
Copyright   : (c) Department of Informatics and Telecommunications, UOI
License     : MIT

Illustrates fundamental functional paradigm concepts:
- Pure functions and immutable data
- Pattern matching and structural recursion on lists
- Higher-order functions (map, filter, foldr, foldl)
- Custom algebraic data types (ADT) and recursive trees
-}

module Main where

-- =============================================================================
-- 1. Algebraic Data Types (Binary Search Tree)
-- =============================================================================

-- | Recursive tree definition modeling either an empty leaf or a node with subtrees.
data Tree a = Empty
            | Node a (Tree a) (Tree a)
            deriving (Show, Eq)

-- | Inserts an element into a binary search tree preserving BST invariants.
treeInsert :: (Ord a) => a -> Tree a -> Tree a
treeInsert x Empty = Node x Empty Empty
treeInsert x (Node val left right)
    | x == val  = Node val left right
    | x < val   = Node val (treeInsert x left) right
    | otherwise = Node val left (treeInsert x right)

-- | In-order tree traversal returning an ordered list of elements.
inOrderTraversal :: Tree a -> [a]
inOrderTraversal Empty = []
inOrderTraversal (Node val left right) = inOrderTraversal left ++ [val] ++ inOrderTraversal right

-- =============================================================================
-- 2. Pattern Matching & Structural Recursion
-- =============================================================================

-- | Computes the factorial of a non-negative integer using pattern matching.
factorial :: Integer -> Integer
factorial 0 = 1
factorial n
    | n > 0     = n * factorial (n - 1)
    | otherwise = error "Factorial undefined for negative integers"

-- | Computes the length of a list via recursive pattern matching.
listLength :: [a] -> Int
listLength []     = 0
listLength (_:xs) = 1 + listLength xs

-- =============================================================================
-- 3. Higher-Order Functions & Currying
-- =============================================================================

-- | Squares all even numbers in an integer list using filter and map.
squareEvens :: [Integer] -> [Integer]
squareEvens xs = map (^ (2 :: Integer)) (filter even xs)

-- | Reverses a list using foldl and lambda abstraction.
reverseList :: [a] -> [a]
reverseList = foldl (\acc x -> x : acc) []

-- | Evaluates whether a target element exists in a list using foldr.
containsElement :: (Eq a) => a -> [a] -> Bool
containsElement target = foldr (\x acc -> x == target || acc) False

-- =============================================================================
-- 4. Main Execution Driver
-- =============================================================================

main :: IO ()
main = do
    putStrLn "=== Functional Programming Paradigms in Haskell ==="

    -- 1. Factorial Demonstration
    let n = 6
    putStrLn $ "Factorial of " ++ show n ++ ": " ++ show (factorial n)

    -- 2. Higher-Order Processing
    let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    putStrLn $ "Original numbers: " ++ show numbers
    putStrLn $ "Squared evens:    " ++ show (squareEvens numbers)
    putStrLn $ "Reversed numbers: " ++ show (reverseList numbers)

    -- 3. Binary Search Tree
    let sampleKeys = [45, 12, 89, 3, 27, 64, 99]
    let bst = foldr treeInsert Empty (reverse sampleKeys)
    putStrLn $ "Constructed BST in-order: " ++ show (inOrderTraversal bst)
    putStrLn $ "Contains 27? " ++ show (containsElement 27 (inOrderTraversal bst))
    putStrLn $ "Contains 50? " ++ show (containsElement 50 (inOrderTraversal bst))

