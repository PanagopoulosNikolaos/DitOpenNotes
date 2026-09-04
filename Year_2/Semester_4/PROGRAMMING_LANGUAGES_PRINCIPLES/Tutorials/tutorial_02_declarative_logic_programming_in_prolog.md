# Tutorial 02: Declarative Logic Programming in Prolog

This practical tutorial introduces logic programming using SWI-Prolog: constructing knowledge bases of facts and rules, running queries, tracing Robinson unification and backtracking with `trace`, and manipulating recursive lists.

---

## 1. SWI-Prolog Environment Setup

Launch the SWI-Prolog interactive shell:

```bash
swipl
```

### 1.1 Essential Interpreter Commands
```text
-- Consult (load) a knowledge base file (.pl)
?- [family].
-- or:
?- consult('family.pl').

-- Trace goal evaluation step-by-step
?- trace.

-- Turn off tracing
?- notrace.

-- Terminate SWI-Prolog
?- halt.
```

---

## 2. Knowledge Base Definition: Family Relationships

Create a file `family.pl`:

```prolog
% Facts
parent(cronus, zeus).
parent(rhea, zeus).
parent(zeus, ares).
parent(zeus, athena).
parent(hera, ares).

male(cronus).
male(zeus).
male(ares).
female(rhea).
female(hera).
female(athena).

% Rules
father(X, Y) :- parent(X, Y), male(X).
mother(X, Y) :- parent(X, Y), female(X).

sibling(X, Y) :-
    parent(Z, X),
    parent(Z, Y),
    X \= Y.

ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).
```

### 2.1 Interactive Querying and Backtracking
```text
?- father(Father, ares).
Father = zeus.

?- sibling(ares, Sibling).
Sibling = athena ;
false.
```
Pressing `;` prompts the engine to backtrack and search for alternative solutions.

---

## 3. Recursive List Processing in Prolog

Prolog represents lists using the `[Head | Tail]` syntactic pattern.

```prolog
% Membership predicate: element X is in list
element_of(X, [X | _]).
element_of(X, [_ | Tail]) :- element_of(X, Tail).

% List concatenation (append)
custom_append([], L, L).
custom_append([H | T], L2, [H | Result]) :-
    custom_append(T, L2, Result).

% Reversing a list using accumulator
custom_rev(List, Reversed) :- rev_acc(List, [], Reversed).
rev_acc([], Acc, Acc).
rev_acc([H | T], Acc, Result) :- rev_acc(T, [H | Acc], Result).
```

### 3.2 Bidirectional Execution of `custom_append`
Because Prolog rules are relations rather than one-way functions, `custom_append` can be run in reverse to decompose lists:

```text
?- custom_append(Left, Right, [1, 2, 3]).
Left = [], Right = [1, 2, 3] ;
Left = [1], Right = [2, 3] ;
Left = [1, 2], Right = [3] ;
Left = [1, 2, 3], Right = [] ;
false.
```

