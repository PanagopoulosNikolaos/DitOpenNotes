# Ασκήσεις Εμπέδωσης: Επίλυση Προβλημάτων σε Haskell και Prolog

## Άσκηση 1: Αναδίπλωση και Συναρτήσεις Ανώτερης Τάξης στη Haskell

### Εκφώνηση:
Υλοποιήστε στη Haskell αποκλειστικά με χρήση της `foldr` ή `foldl`:
1. Τη συνάρτηση `myMap :: (a -> b) -> [a] -> [b]`
2. Τη συνάρτηση `myFilter :: (a -> Bool) -> [a] -> [a]`
3. Τη συνάρτηση `myReverse :: [a] -> [a]`

### Λύση:
```haskell
-- 1. Υλοποίηση map με foldr
myMap :: (a -> b) -> [a] -> [b]
myMap f = foldr (\x acc -> f x : acc) []

-- 2. Υλοποίηση filter με foldr
myFilter :: (a -> Bool) -> [a] -> [a]
myFilter p = foldr (\x acc -> if p x then x : acc else acc) []

-- 3. Υλοποίηση reverse με foldl
myReverse :: [a] -> [a]
myReverse = foldl (\acc x -> x : acc) []
```

---

## Άσκηση 2: Επεξεργασία Λιστών και Αποκοπή στην Prolog

### Εκφώνηση:
Γράψτε ένα κατηγόρημα Prolog `remove_duplicates(List, Unique)` που αφαιρεί όλα τα διπλότυπα στοιχεία από μια λίστα διατηρώντας την πρώτη τους εμφάνιση. Χρησιμοποιήστε τον τελεστή αποκοπής (`!`).

### Λύση:
```prolog
% Βάση: κενή λίστα
remove_duplicates([], []).

% Περίπτωση 1: Η κεφαλή H υπάρχει στο υπόλοιπο της λίστας
remove_duplicates([H | T], Result) :-
    member(H, T),
    !, % Αποκοπή: μην δοκιμάσεις τον επόμενο κανόνα αν το H είναι μέλος
    remove_duplicates(T, Result).

% Περίπτωση 2: Η κεφαλή H δεν υπάρχει στο υπόλοιπο της λίστας
remove_duplicates([H | T], [H | Result]) :-
    remove_duplicates(T, Result).
```

