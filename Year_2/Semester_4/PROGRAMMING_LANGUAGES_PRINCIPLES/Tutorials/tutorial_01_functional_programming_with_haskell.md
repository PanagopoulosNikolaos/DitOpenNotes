# Εργαστηριακός Οδηγός 1: Συναρτησιακός Προγραμματισμός με το GHCi στη Haskell

## 1. Σκοπός Εργαστηρίου
Εγκατάσταση και χρήση του διαδραστικού διερμηνέα GHCi (Glasgow Haskell Compiler), ορισμός αναδρομικών συναρτήσεων, χειρισμός λιστών με list comprehensions και χρήση αλγεβρικών τύπων δεδομένων (Algebraic Data Types).

---

## 2. Εκκίνηση και Βασικές Εντολές GHCi
```bash
# Είσοδος στο περιβάλλον GHCi
ghci

# Φόρτωση αρχείου κώδικα
:load exercises.hs

# Έλεγχος τύπου μιας έκφρασης ή συνάρτησης
:type map

# Έξοδος από το περιβάλλον
:quit
```

---

## 3. Υλοποίηση Αλγεβρικών Τύπων και Αναδρομικών Συναρτήσεων

Δημιουργήστε το αρχείο `shapes_and_trees.hs`:
```haskell
module ShapesAndTrees where

-- Ορισμός αλγεβρικού τύπου δεδομένων για γεωμετρικά σχήματα
data Shape = Circle Double
           | Rectangle Double Double
           | Triangle Double Double Double
           deriving (Show, Eq)

-- Υπολογισμός εμβαδού με ταίριασμα προτύπων (Pattern Matching)
area :: Shape -> Double
area (Circle r)        = pi * r * r
area (Rectangle w h)   = w * h
area (Triangle a b c)  = 
    let s = (a + b + c) / 2
    in sqrt (s * (s - a) * (s - b) * (s - c))

-- Ορισμός πολυμορφικού δυαδικού δέντρου
data Tree a = Empty
            | Node a (Tree a) (Tree a)
            deriving (Show, Eq)

-- Εισαγωγή στοιχείου σε Δυαδικό Δέντρο Αναζήτησης (BST)
insertBST :: Ord a => a -> Tree a -> Tree a
insertBST x Empty = Node x Empty Empty
insertBST x (Node val left right)
    | x < val   = Node val (insertBST x left) right
    | x > val   = Node val left (insertBST x right)
    | otherwise = Node val left right

-- Ενδοδιατεταγμένη διάσχιση (In-order Traversal)
inorder :: Tree a -> [a]
inorder Empty = []
inorder (Node val left right) = inorder left ++ [val] ++ inorder right
```

