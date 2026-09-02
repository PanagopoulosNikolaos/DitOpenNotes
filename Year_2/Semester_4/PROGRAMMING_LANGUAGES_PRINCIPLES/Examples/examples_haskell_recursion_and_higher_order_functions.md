# Παραδείγματα: Αναδρομή και Συναρτήσεις Ανώτερης Τάξης στη Haskell

## Παράδειγμα 1: Υλοποίηση Αριθμητικού Αξιολογητή με Μονάδες (Monadic Evaluator)

### Περιγραφή:
Ορισμός αφηρημένου συντακτικού δέντρου (AST) για απλές αριθμητικές εκφράσεις και ασφαλής αξιολόγηση με χρήση του `Maybe` monad για την αποφυγή διαίρεσης με το μηδέν.

### Πλήρης Κώδικας Haskell:
```haskell
module Evaluator where

-- Ορισμός εκφράσεων
data Expr = Val Double
          | Add Expr Expr
          | Sub Expr Expr
          | Mul Expr Expr
          | Div Expr Expr
          deriving (Show, Eq)

-- Ασφαλής αποτίμηση
eval :: Expr -> Maybe Double
eval (Val n) = Just n
eval (Add e1 e2) = do
    v1 <- eval e1
    v2 <- eval e2
    return (v1 + v2)
eval (Sub e1 e2) = do
    v1 <- eval e1
    v2 <- eval e2
    return (v1 - v2)
eval (Mul e1 e2) = do
    v1 <- eval e1
    v2 <- eval e2
    return (v1 * v2)
eval (Div e1 e2) = do
    v1 <- eval e1
    v2 <- eval e2
    if v2 == 0
        then Nothing -- Αποφυγή διαίρεσης με το μηδέν
        else return (v1 / v2)

-- Δοκιμές:
-- eval (Div (Val 10) (Val 2)) ==> Just 5.0
-- eval (Div (Val 10) (Val 0)) ==> Nothing
```

