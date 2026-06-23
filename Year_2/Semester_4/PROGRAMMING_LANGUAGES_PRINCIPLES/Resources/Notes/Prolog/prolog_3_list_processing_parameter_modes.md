# Prolog — List Processing and Parameter Modes

Prolog lists are homogeneous recursive structures built from the cons functor `[Head|Tail]` with base case `[]`. Unlike functions in imperative languages, Prolog predicates are **relation-oriented**: the same predicate can run in multiple **modes** depending on which arguments are bound (input) and which are free (output). This file covers `append/3`, structural recursion, list reversal, and multidirectional execution.

*Prerequisite: `prolog_2_execution_mechanisms.md` — unification, backtracking, recursion.*

---

## 1. Prolog Lists

### 1.1 Concept Overview

A Prolog **list** is either the empty list `[]` or a cons cell `[H|T]` where `H` is the head (element) and `T` is the tail (another list). The shorthand `[a, b, c]` expands to `[a|[b|[c|[]]]]`.

### 1.2 Syntax Reference

```
<list>       ::= [] | [ <term> | <list> ] | [ <term>, ..., <term> ]
<list_pattern> ::= [] | [ <var> | <var> ] | [ <term>, ..., <term> ]
```

### 1.3 Behavioral Description

| Notation | Internal Form | Elements |
| :--- | :--- | :--- |
| `[]` | Empty list | 0 |
| `[a]` | `[a|[]]` | 1 |
| `[a, b, c]` | `[a|[b|[c|[]]]]` | 3 |
| `[H|T]` | Cons decomposition | Head + tail |
| `[X, Y|Rest]` | Partial decomposition | First two + remainder |

```prolog
?- [1, 2, 3] = [H|T], T = [T1|T2].
```

```text
H = 1,
T = [2, 3],
T1 = 2,
T2 = [3].
```

---

## 2. Parameter Modes

### 2.1 Concept Overview

Each argument of a predicate has a **mode** at call time:

- **Bound (input):** Ground or partially instantiated term; acts as given data.
- **Unbound (output):** Free variable; the engine instantiates it upon success.

The same predicate definition supports multiple modes — this is **multidirectional execution**.

### 2.2 Mode Annotation Convention

| Annotation | Meaning |
| :--- | :--- |
| `+` | Bound on entry (input) |
| `-` | Unbound on entry (output) |
| `?` | Either bound or unbound |

### 2.3 Mode Behavior Table

| Call Pattern | Mode | Role |
| :--- | :--- | :--- |
| `append([1,2], [3], R)` | `++, -` | Forward: concatenate known lists |
| `append(A, B, [1,2,3])` | `-,-,+` | Reverse: split into all valid pairs |
| `append([1], B, [1,2,3])` | `+,?,+` | Mixed: find B given partial info |
| `append(L, [], L)` | `?,-,?` | Identity: any list appended with [] |

> **[Key Insight]** In Prolog, there is no separate "function return value." The last argument (or any argument) can serve as output purely by being unbound at call time and unified with a result term on success.

---

## 3. append/3 — The Canonical Multimode Predicate

### 3.1 Concept Overview

`append(A, B, C)` means "C is the concatenation of A and B." The same definition serves forward concatenation, list splitting, and constraint solving.

### 3.2 Syntax Reference

```
append(+, +, -)   % forward mode
append(-, -, +)   % reverse mode
```

### 3.3 Definition (Structural Recursion)

```prolog
% Base case: appending empty list to A yields A.
append([], A, A).

% Recursive case: append tail of first list, then cons head onto result.
append([H|T], B, [H|R]) :- append(T, B, R).
```

### 3.4 Behavioral Description — Forward Mode (`++, -`)

```prolog
?- append([1, 2], [3, 4], R).
```

**Trace:**

1. `append([1,2], [3,4], R)` → `H=1`, recurse `append([2], [3,4], R1)` → `R = [1|R1]`
2. `append([2], [3,4], R1)` → `H=2`, recurse `append([], [3,4], R2)` → `R1 = [2|R2]`
3. `append([], [3,4], R2)` → base case → `R2 = [3,4]`
4. Unwind: `R1 = [2,3,4]`, `R = [1,2,3,4]`

```text
R = [1, 2, 3, 4].
```

### 3.5 Behavioral Description — Reverse Mode (`-,-,+`)

```prolog
?- append(A, B, [1, 2, 3]).
```

**Solutions (all splits):**

```text
A = [], B = [1, 2, 3] ;
A = [1], B = [2, 3] ;
A = [1, 2], B = [3] ;
A = [1, 2, 3], B = [].
```

Each solution is a valid partition of the list into prefix `A` and suffix `B`.

### 3.6 Parameter Reference — append/3

| Argument | Forward Mode | Reverse Mode | Description |
| :--- | :--- | :--- | :--- |
| `A` | Input (bound list) | Output (variable) | Left operand list |
| `B` | Input (bound list) | Output (variable) | Right operand list |
| `C` | Output (variable) | Input (bound list) | Concatenation result |

---

## 4. Structural Recursion on Head/Tail

### 4.1 Concept Overview

List predicates follow a standard recursion template:

1. **Base case** — handle `[]`.
2. **Recursive case** — decompose `[H|T]`, process `T`, combine with `H`.

### 4.2 General Template

```prolog
predicate([], <base_value>).
predicate([H|T], <result>) :-
    predicate(T, <sub_result>),
    <combine H with sub_result>.
```

### 4.3 length/2

```prolog
length([], 0).
length([_|T], N) :- length(T, N1), N is N1 + 1.
```

```prolog
?- length([a, b, c], N).
```

```text
N = 3.
```

### 4.4 member/2

```prolog
member(X, [X|_]).
member(X, [_|T]) :- member(X, T).
```

```prolog
?- member(b, [a, b, c]).
```

```text
true.
```

```prolog
?- member(X, [a, b, c]).
```

```text
X = a ;
X = b ;
X = c.
```

`member/2` in output mode enumerates all list elements.

---

## 5. List Reversal

### 5.1 Concept Overview

List reversal can be defined recursively or via `append/3`. The recursive definition builds reversed order during unwinding; the accumulator-based definition is tail-recursive and efficient.

### 5.2 Naive Reverse (Structural Recursion)

```prolog
reverse([], []).
reverse([H|T], R) :-
    reverse(T, RT),
    append(RT, [H], R).
```

```prolog
?- reverse([1, 2, 3], R).
```

**Trace (intermediate state after reversing tail):**

1. `reverse([2,3], RT)` → in progress
2. `reverse([3], RT2)` → `RT2 = [3]`
3. `reverse([], [])` → base
4. Unwind: `reverse([3], [3])`, `append([3],[2], RT)` → `RT = [3,2]`
5. Unwind: `reverse([2,3], [3,2])`, `append([3,2],[1], R)` → `R = [3,2,1]`

```text
R = [3, 2, 1].
```

### 5.3 Accumulator-Based Reverse

```prolog
reverse(L, R) :- reverse_acc(L, [], R).

reverse_acc([], Acc, Acc).
reverse_acc([H|T], Acc, R) :- reverse_acc(T, [H|Acc], R).
```

| Step | Call | Accumulator |
| :--- | :--- | :--- |
| 1 | `reverse_acc([1,2,3], [], R)` | `[]` |
| 2 | `reverse_acc([2,3], [1], R)` | `[1]` |
| 3 | `reverse_acc([3], [2,1], R)` | `[2,1]` |
| 4 | `reverse_acc([], [3,2,1], R)` | `[3,2,1]` |
| Result | `R = [3,2,1]` | — |

### 5.4 Reverse in Output Mode

```prolog
?- reverse(X, [1, 2, 3]).
```

```text
X = [3, 2, 1].
```

A single solution — reversal is a bijection for lists.

---

## 6. List Traversal Without Explicit Return Type

### 6.1 Concept Overview

Prolog predicates need not declare return types. A traversal predicate can succeed with side-effect output (e.g., printing) or bind an output argument. The relation itself encodes the computation.

### 6.2 sumlist/2 — Accumulating Values

```prolog
sumlist([], 0).
sumlist([H|T], S) :- sumlist(T, S1), S is H + S1.
```

```prolog
?- sumlist([1, 2, 3, 4], S).
```

```text
S = 10.
```

### 6.3 all_prefixes/2 — Generate All Prefixes

```prolog
all_prefixes(L, P) :- append(P, _, L).
```

```prolog
?- all_prefixes([a, b, c], P).
```

```text
P = [] ;
P = [a] ;
P = [a, b] ;
P = [a, b, c].
```

Uses `append/3` in reverse mode: `P` is prefix, `_` is unconstrained suffix.

---

## Common Errors and Gotchas

### Error 1: Using `=` for List Construction with Arithmetic

**Cause:** `Result = [H|R]` is unification; arithmetic in list position needs `is`.

```prolog
% Wrong:
sumlist([H|T], S) :- sumlist(T, S1), S = H + S1.

% Correct:
sumlist([H|T], S) :- sumlist(T, S1), S is H + S1.
```

**Resolution:** Use `is` for evaluated expressions on the right; use `=` for structural unification.

### Error 2: Non-Termination in Reverse Mode with Unbalanced append

**Cause:** Query `append(A, B, L)` with partially bound `A` and infinite backtracking if constraints are inconsistent.

**Resolution:** Bind at least one of `A`, `B`, or `C` sufficiently to limit search space.

### Error 3: Assuming Single Direction

**Cause:** Defining predicates only tested in forward mode may accidentally work in reverse but produce unexpected multiple solutions or inefficiency.

```prolog
% Inefficient reverse mode due to append at each step.
reverse([H|T], R) :- reverse(T, RT), append(RT, [H], R).
```

**Resolution:** Use accumulator style for production code; understand which modes your predicates support.

---

## Solved Exercises

### Exercise 1: List Decomposition

**Problem:** Unify `[a, b, c, d]` with `[X, Y|Rest]` and state bindings.

**Solution:**

1. `X = a`
2. `Y = b`
3. `Rest = [c, d]`

---

### Exercise 2: append Forward

**Problem:** Evaluate `?- append([x, y], [z], R).`

**Solution:**

1. `H = x`, recurse on `[y]` and `[z]`
2. `H = y`, recurse on `[]` and `[z]`
3. Base: `append([], [z], [z])`
4. Unwind: `R = [y, z]`, then `R = [x, y, z]`
5. **Answer:** `R = [x, y, z].`

---

### Exercise 3: append Reverse — Count Splits

**Problem:** How many solutions does `?- append(A, B, [1, 2]).` produce?

**Solution:**

1. `A=[], B=[1,2]`
2. `A=[1], B=[2]`
3. `A=[1,2], B=[]`
4. **Answer:** 3 solutions.

---

### Exercise 4: length Trace

**Problem:** Trace `?- length([p, q], N).`

**Solution:**

1. `length([p,q], N)` → `length([q], N1)`, `N is N1 + 1`
2. `length([q], N1)` → `length([], N2)`, `N1 is N2 + 1`
3. `length([], N2)` → `N2 = 0`
4. Unwind: `N1 = 1`, `N = 2`
5. **Answer:** `N = 2.`

---

### Exercise 5: member Output Mode

**Problem:** List solutions to `?- member(X, [red, green, blue]), X \= green.`

**Solution:**

1. `X = red` — `red \= green` succeeds
2. Backtrack: `X = green` — fails inequality
3. Backtrack: `X = blue` — succeeds
4. **Answer:** `X = red ; X = blue.`

---

### Exercise 6: Reverse Accumulator Trace

**Problem:** Trace accumulator states for `reverse_acc([1, 2], [], R).`

**Solution:**

| Step | Remaining | Accumulator |
| :--- | :--- | :--- |
| 1 | `[1,2]` | `[]` |
| 2 | `[2]` | `[1]` |
| 3 | `[]` | `[2,1]` |
| Result | — | `R = [2,1]` |

---

### Exercise 7: Prefix Generation

**Problem:** Evaluate `?- append(P, [c], [a, b, c]).`

**Solution:**

1. `P = [a,b]` — `append([a,b], [c], [a,b,c])` succeeds
2. No other split yields suffix exactly `[c]`
3. **Answer:** `P = [a, b].`

---

### Exercise 8: sumlist and Mode Reversal

**Problem:** Can `?- sumlist(L, 6).` find a list summing to 6? Explain briefly.

**Solution:**

1. `sumlist/2` uses `is` with bound `S` and recursive structure on `L`.
2. With `S = 6` bound, Prolog can search for lists — e.g., `L = [1,2,3]` or `L = [6]`.
3. Multiple lists sum to 6; engine returns solutions via backtracking if additional constraints are added.
4. **Answer:** Yes, though infinitely many lists exist (e.g., `[6]`, `[1,5]`, `[1,1,4]`, ...). Practical use requires length bounds or additional constraints.

---

## Exam Tip: Identify the Mode Before Tracing

For any list predicate question:

1. **Label each argument** `+` or `-` at the call site.
2. **Forward (`++, -`)** — recurse down the first list, build output on unwind or via accumulator.
3. **Reverse (`-,-,+`)** — expect multiple solutions from `append/3`-style splitting; count solutions by enumerating prefix lengths $0 \ldots n$ for a list of length $n$.
4. **Accumulator predicates** — track the accumulator column separately; the final accumulator value is the answer.

**Most common exam trap:** Writing `append(A, B, C)` as if it were a function `append(A, B) → C`. In reverse mode, `C` is input and both `A` and `B` are outputs — the query generates all partitions, not a single "split point."