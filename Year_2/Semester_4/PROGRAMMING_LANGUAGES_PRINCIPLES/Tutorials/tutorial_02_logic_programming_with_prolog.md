# Εργαστηριακός Οδηγός 2: Λογικός Προγραμματισμός με SWI-Prolog

## 1. Σκοπός Εργαστηρίου
Εξοικείωση με το περιβάλλον SWI-Prolog, γραφή βάσεων γνώσης, χειρισμός αναδρομικών δομών λιστών και επίλυση προβλημάτων ικανοποίησης περιορισμών.

---

## 2. Εκκίνηση SWI-Prolog και Φόρτωση Προγράμματος
```bash
# Εγκατάσταση και εκκίνηση σε Linux
sudo apt-get install -y swi-prolog
swipl

# Φόρτωση αρχείου εντός του διερμηνέα
?- [lists_and_graphs].
```

---

## 3. Υλοποίηση Βασικών Κατηγορημάτων Λιστών

Δημιουργήστε το αρχείο `lists_and_graphs.pl`:
```prolog
% Μέλος λίστας
member_custom(X, [X | _]).
member_custom(X, [_ | Tail]) :-
    member_custom(X, Tail).

% Μήκος λίστας
length_custom([], 0).
length_custom([_ | Tail], N) :-
    length_custom(Tail, N1),
    N is N1 + 1.

% Αντιστροφή λίστας με συσσωρευτή (Tail Recursive Reverse)
reverse_acc([], Acc, Acc).
reverse_acc([H | T], Acc, Result) :-
    reverse_acc(T, [H | Acc], Result).

reverse_custom(List, Reversed) :-
    reverse_acc(List, [], Reversed).

% Εύρεση διαδρομής σε κατευθυνόμενο γράφο
edge(a, b).
edge(a, c).
edge(b, d).
edge(c, d).
edge(d, e).

path(X, Y, [X, Y]) :-
    edge(X, Y).
path(X, Y, [X | Path]) :-
    edge(X, Z),
    path(Z, Y, Path).
```

### Δοκιμαστικά Ερωτήματα:
```prolog
?- reverse_custom([1, 2, 3, 4], R).
R = [4, 3, 2, 1].

?- path(a, e, P).
P = [a, b, d, e] ;
P = [a, c, d, e].
```

