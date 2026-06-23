# Prolog — Advanced Applications

Beyond relational querying, Prolog excels at **constraint satisfaction problems (CSPs)**: the developer declares variables, domains, and constraints; the engine searches the state space for assignments that satisfy all constraints simultaneously. This file covers CSP formulation, scheduling and resource allocation, Sudoku as a canonical grid CSP, game AI knowledge systems, and linguistics applications referenced in the course mindmap.

*Prerequisite: `prolog_3_list_processing_parameter_modes.md` — lists, modes, structural recursion.*

---

## 1. Constraint Satisfaction Problems (CSP)

### 1.1 Concept Overview

A **CSP** is a triple $(X, D, C)$ where:

- $X = \{X_1, \ldots, X_n\}$ — set of decision variables
- $D = \{D_1, \ldots, D_n\}$ — domains (allowed values per variable)
- $C = \{C_1, \ldots, C_m\}$ — constraints relating subsets of variables

The **solution** is an assignment $\theta : X_i \mapsto v_i$ with $v_i \in D_i$ such that every constraint in $C$ is satisfied.

In Prolog, variables are logical, constraints are relations, and the engine performs **generate-and-test** or **constraint propagation** search.

### 1.2 Syntax Reference — CSP Encoding Pattern

```
% Domain membership
domain(<var>, <min>, <max>).
domain(<var>, [<value>, ...]).

% Constraints as Prolog relations
constraint(<vars>) :- <goals that must hold> .

% Solve: instantiate variables satisfying all constraints
solve(<vars>) :- <domain declarations>, <constraint goals>.
```

### 1.3 Behavioral Description

| Phase | Prolog Mechanism | Role |
| :--- | :--- | :--- |
| Variable declaration | Unbound logical variables | Decision points |
| Domain specification | `between/3`, `member/2`, `ins/2` (CLP) | Limit candidate values |
| Constraint posting | Goal conjunction in rule body | Prune invalid assignments |
| Search | Backtracking over choices | Explore state space |
| Solution | Successful binding of all variables | Answer substitution |

```prolog
% Map coloring: adjacent regions must differ.
color(A) :- member(A, [red, green, blue]).

diff_neighbor(A, B, C) :-
    color(A), color(B), color(C),
    A \= B, B \= C, A \= C.
```

> **[Key Insight]** The developer defines **what** constitutes a valid solution; Prolog determines **how** to search. This inversion is the central advantage of logic programming for combinatorial problems.

---

## 2. Generate-and-Test Pattern

### 2.1 Concept Overview

The simplest CSP strategy in standard Prolog:

1. **Generate** — bind variables to candidate values (via `member/2`, `between/3`, or permutations).
2. **Test** — check constraints; on failure, backtrack to next candidate.

### 2.2 Syntax Reference

```
solve(Vars) :-
    generate(Vars),
    test_constraints(Vars).
```

### 2.3 N-Queens (Classic CSP)

Place $n$ queens on an $n \times n$ board so no two share a row, column, or diagonal.

```prolog
queens(N, Queens) :-
    length(Queens, N),
    queens(N, Queens, 0, 1, 2).

% queens(N, Qs, RowDiff, ColDiff, DiagDiff) — constraint parameters.
queens(_, [], _, _, _).
queens(N, [Q|Qs], Row, Col, Diag) :-
    between(1, N, Q),
    safe(Q, Qs, Row, Col, Diag),
    queens(N, Qs, Row, Col, Diag).

safe(_, [], _, _, _).
safe(Q, [Q1|Qs], Row, Col, Diag) :-
    Q =\= Q1,
    abs(Q - Q1) =\= Row,
    abs(Q - Q1) =\= Col,
    abs(Q - Q1) =\= Diag,
    safe(Q, Qs, Row + 1, Col + 1, Diag + 1).
```

```prolog
?- queens(4, Q).
```

```text
Q = [2, 4, 1, 3] ;
Q = [3, 1, 4, 2].
```

### 2.4 Generate-and-Test Parameter Table

| Component | Predicate | Purpose |
| :--- | :--- | :--- |
| Board representation | List of column positions | `Queens[i]` = row of queen in column $i$ |
| Domain | `between(1, N, Q)` | Row choices $1 \ldots n$ |
| Row constraint | Implicit (one queen per list position) | Each column has exactly one queen |
| Column constraint | `Q =\= Q1` | No two queens in same row |
| Diagonal constraint | `abs(Q - Q1) =\= Row` etc. | No diagonal attacks |

---

## 3. Scheduling and Resource Optimization

### 3.1 Concept Overview

Scheduling assigns tasks to time slots and resources subject to precedence, capacity, and exclusivity constraints. Prolog expresses these as relations over task variables.

### 3.2 Formal Model

For tasks $T = \{t_1, \ldots, t_n\}$:

- $start(t_i) \in \mathbb{Z}_{\geq 0}$ — start time
- $duration(t_i) \in \mathbb{Z}_{> 0}$ — fixed duration
- $resource(t_i) \in R$ — required resource

**Precedence constraint:** $start(t_j) \geq start(t_i) + duration(t_i)$ if $t_i$ must precede $t_j$.

**Resource constraint:** No two tasks sharing a resource may overlap in time.

### 3.3 Example KB

```prolog
task(a, 2, printer).   % task(Name, Duration, Resource)
task(b, 3, printer).
task(c, 1, cpu).
task(d, 2, cpu).

precedes(a, b).        % a must finish before b starts.
precedes(c, d).

% Start time domain
slot(T, S) :- task(T, _, _), between(0, 10, S).
```

### 3.4 Scheduling Rule

```prolog
schedule(Assignments) :-
    findall(T, task(T, _, _), Tasks),
    assign_starts(Tasks, Assignments),
    no_overlap(Assignments),
    respect_precedence(Assignments).

assign_starts([], []).
assign_starts([T|Ts], [T-Start|Rest]) :-
    task(T, _, _),
    between(0, 10, Start),
    assign_starts(Ts, Rest).

respect_precedence(Assignments) :-
    forall(precedes(A, B),
        (member(A-Sa, Assignments), task(A, Da, _),
         member(B-Sb, Assignments),
         Sb >= Sa + Da)).
```

```prolog
?- schedule(A), member(a-Sa, A), member(b-Sb, A).
```

The engine searches start times satisfying precedence and (with `no_overlap/1`) resource constraints.

### 3.5 Scheduling Constraint Summary

| Constraint Type | Prolog Encoding | Effect |
| :--- | :--- | :--- |
| Precedence | `Sb >= Sa + Duration` | Ordering of dependent tasks |
| Resource exclusivity | `no_overlap/1` on same resource | Mutual exclusion in time |
| Domain | `between(0, Max, Start)` | Bounded time window |
| Optimization | `findall` + `min_member/2` | Select minimum-cost schedule |

> **[Supplementary]**
>
> Industrial scheduling often uses **CLP(FD)** (Constraint Logic Programming over Finite Domains) via libraries such as SWI-Prolog's `library(clpfd)`. The `ins/2` and `#=/2` operators provide propagation that prunes search far more efficiently than pure generate-and-test. The declarative structure remains identical; only the constraint engine changes.

---

## 4. Sudoku as Grid CSP

### 4.1 Concept Overview

Sudoku is a $9 \times 9$ grid CSP: fill digits $1$–$9$ so each row, column, and $3 \times 3$ box contains all digits exactly once.

### 4.2 Variable and Domain Model

- **Variables:** 81 cells $C_{r,c}$ for $r, c \in \{1,\ldots,9\}$
- **Domain:** $\{1,2,3,4,5,6,7,8,9\}$ for empty cells; singleton for givens
- **Constraints:** `alldifferent` over each row, column, and box

### 4.3 Implementation Sketch

```prolog
sudoku(Rows) :-
    length(Rows, 9),
    maplist(same_length(Rows), Rows),   % 9x9 grid
    append(Rows, Cells),
    Cells ins 1..9,                      % CLP(FD) domain
    maplist(all_distinct, Rows),         % row constraints
    transpose(Rows, Cols),
    maplist(all_distinct, Cols),         % column constraints
    boxes(Rows, Boxes),
    maplist(all_distinct, Boxes).        % box constraints

boxes([], []).
boxes([A,B,C|T], [B1|Rest]) :-
    box(A, B, C, B1),
    boxes(T, Rest).

box([], [], [], []).
box([H1,H2,H3|T1], [H4,H5,H6|T2], [H7,H8,H9|T3], [H1,H2,H3,H4,H5,H6,H7,H8,H9|T]) :-
    box(T1, T2, T3, T).
```

### 4.4 Puzzle Query

```prolog
?- sudoku([
    [5,3,_,_,7,_,_,_,_],
    [6,_,_,1,9,5,_,_,_],
    [_,9,8,_,_,_,_,6,_],
    [8,_,_,_,6,_,_,_,3],
    [4,_,_,8,_,3,_,_,1],
    [7,_,_,_,2,_,_,_,6],
    [_,6,_,_,_,_,2,8,_],
    [_,_,_,4,1,9,_,_,5],
    [_,_,_,_,8,_,_,7,9]
]).
```

The engine binds `_` variables to digits satisfying all `all_distinct` constraints.

### 4.5 Sudoku Constraint Table

| Group | Size | Constraint |
| :--- | :--- | :--- |
| Rows | 9 | All 9 values distinct |
| Columns | 9 | All 9 values distinct |
| $3 \times 3$ boxes | 9 | All 9 values distinct |
| Givens | Variable | Pre-bound cells reduce search space |

---

## 5. Game AI — Decision Trees and Knowledge Systems

### 5.1 Concept Overview

Prolog models game NPC behavior as a **knowledge base** of facts (world state) and rules (decision policies). The engine evaluates which action rules fire given the current state — a form of backward-chaining decision tree.

### 5.2 World State Representation

```prolog
% Dynamic facts (assert/retract) or static scenario facts.
at(player, room_hall).
at(goblin, room_cave).
health(player, 80).
health(goblin, 30).
has_item(player, sword).
can_reach(room_hall, room_cave).
```

### 5.3 Decision Rules

```prolog
action(attack) :-
    at(player, Loc), at(Enemy, Loc), health(Enemy, H), H > 0.

action(flee) :-
    at(player, Loc), at(Enemy, Loc),
    health(player, PH), health(Enemy, EH),
    PH < 30, EH > PH.

action(explore) :-
    at(player, Loc), can_reach(Loc, Next), \+ at(_, Next).

action(heal) :-
    has_item(player, potion), health(player, H), H < 50.
```

```prolog
?- action(A).
```

```text
A = attack ;
A = explore.
```

### 5.4 Dialogue / Knowledge Systems

NPC dialogue is a rule set over player utterance patterns:

```prolog
intent(greeting, hello).
intent(greeting, hi).
intent(quest_request, help).
intent(quest_request, quest).

response(greeting, 'Greetings, traveler!').
response(quest_request, 'The goblin in the cave stole my amulet.').

reply(PlayerInput, NPCResponse) :-
    intent(Intent, PlayerInput),
    response(Intent, NPCResponse).
```

```prolog
?- reply(help, R).
```

```text
R = 'The goblin in the cave stole my amulet.'.
```

### 5.5 Game AI Architecture

| Layer | Prolog Representation | Function |
| :--- | :--- | :--- |
| World model | Facts (`at/2`, `health/2`) | Current game state |
| Perception | Queries over world facts | What the NPC "knows" |
| Policy | Rules (`action/1`) | Decision selection |
| Dialogue | Intent/response rules | Natural language interaction |
| Search | Path-finding via `can_reach/2` + recursion | Movement planning |

---

## 6. Linguistics and Cognitive Science

### 6.1 Concept Overview

Prolog originated from logic and was adopted for **computational linguistics**: parsing sentences, encoding grammars, and modeling cognitive rule systems. **Definite Clause Grammars (DCGs)** extend Prolog with grammar rules that compile to difference-list parsers.

### 6.2 Context-Free Grammar as Rules

```prolog
% sentence --> noun_phrase, verb_phrase.
sentence(S, V, O) :- noun_phrase(S), verb_phrase(V, O).

noun_phrase(the_cat).
verb_phrase(eats, fish).
```

```prolog
?- sentence(Subject, Verb, Object).
```

```text
Subject = the_cat, Verb = eats, Object = fish.
```

### 6.3 DCG Syntax Reference

```
<nonterminal> --> <terminal>, <nonterminal>.
<nonterminal> --> <nonterminal>, <nonterminal>.
<nonterminal> --> [ <terminal> ].
```

DCG rules translate to Prolog clauses with hidden difference-list arguments for efficient parsing.

### 6.4 Simple DCG Example

```prolog
sentence --> noun_phrase, verb_phrase.

noun_phrase --> [the], noun.
noun --> [cat].
noun --> [dog].

verb_phrase --> [eats], noun_phrase.
```

```prolog
?- phrase(sentence, [the, cat, eats, the, dog]).
```

```text
true.
```

```prolog
?- phrase(sentence, S).
```

```text
S = [the, cat, eats, the, cat] ;
S = [the, cat, eats, the, dog] ;
...
```

### 6.5 Linguistics Application Summary

| Application | Prolog Feature | Example |
| :--- | :--- | :--- |
| Parsing | DCGs | `phrase(sentence, Tokens)` |
| Morphology | Rule-based affixation | `plural(cat, cats)` |
| Semantic networks | Relation facts | `is_a(cat, mammal)` |
| Cognitive models | Production rules | `if perception(X) then action(Y)` |

---

## Common Errors and Gotchas

### Error 1: Unbounded Generate-and-Test

**Cause:** Generating permutations or integers without domain bounds causes infinite search.

```prolog
% Dangerous: infinite integers.
solve(X) :- X > 5, X < 100.
```

**Resolution:** Use `between/3` or CLP(FD) `ins` for finite domains.

### Error 2: Constraint Order Sensitivity

**Cause:** In pure Prolog, constraints tested after generation may explore many doomed branches.

```prolog
% Inefficient: generate first, check later.
coloring(A, B, C) :- color(A), color(B), color(C), A \= B, B \= C.
```

**Resolution:** Place tightest constraints earliest, or use CLP(FD) for propagation.

### Error 3: Confusing DCG Terminals with Predicates

**Cause:** `[the]` in a DCG is a terminal (word); `the` without brackets is a nonterminal or predicate call.

```prolog
% DCG terminal:
noun_phrase --> [the], noun.

% NOT the same as:
noun_phrase --> the, noun.  % Calls predicate the/2 — likely wrong.
```

**Resolution:** Terminals are always in square brackets in DCG notation.

---

## Solved Exercises

### Exercise 1: CSP Formalization

**Problem:** Formalize map coloring for 3 regions (A, B, C) where A borders B and B borders C (A and C do not border).

**Solution:**

1. Variables: $X = \{A, B, C\}$
2. Domains: $D_i = \{\text{red}, \text{green}, \text{blue}\}$
3. Constraints: $A \neq B$, $B \neq C$
4. Prolog: `color(A), color(B), color(C), A \= B, B \= C.`

---

### Exercise 2: N-Queens — Why [2,4,1,3]?

**Problem:** Verify that `Q = [2,4,1,3]` is a valid 4-queens solution (column $i$ has queen in row `Q[i]`).

**Solution:**

| Column | Row | Column check | Diagonal check |
| :--- | :--- | :--- | :--- |
| 1 | 2 | Unique | — |
| 2 | 4 | Unique | $|2-4| = 2 \neq 1$ (row diff) |
| 3 | 1 | Unique | $|2-1| = 1 = 3-2$ row diff... check: $|4-1| = 3$, $|2-1| = 1$ |
| 4 | 3 | Unique | All pairwise diagonal checks pass |

No two queens share row, column, or diagonal. **Valid.**

---

### Exercise 3: Scheduling Precedence

**Problem:** Tasks `a` (duration 2) precedes `b` (duration 3). If `a` starts at 4, what is the earliest start for `b`?

**Solution:**

1. $end(a) = start(a) + duration(a) = 4 + 2 = 6$
2. Precedence: $start(b) \geq end(a) = 6$
3. **Answer:** Earliest $start(b) = 6$.

---

### Exercise 4: Sudoku Row Constraint

**Problem:** Can row `[1, 2, 3, 4, 5, 6, 7, 8, 1]` be part of a valid Sudoku?

**Solution:**

1. Value `1` appears twice in the row.
2. `all_distinct` constraint violated.
3. **Answer:** No.

---

### Exercise 5: Game AI Action Selection

**Problem:** Given `health(player, 20)`, `health(goblin, 50)`, both `at/2` same location, which actions fire from Section 5.3 rules?

**Solution:**

1. `action(attack)` — enemy present with health > 0 → succeeds.
2. `action(flee)` — `PH=20 < 30` and `EH=50 > PH` → succeeds.
3. `action(heal)` — no potion → fails.
4. **Answer:** `attack` and `flee`.

---

### Exercise 6: Dialogue Intent Matching

**Problem:** Evaluate `?- reply(hello, R).`

**Solution:**

1. `intent(greeting, hello)` succeeds.
2. `response(greeting, 'Greetings, traveler!')` succeeds.
3. **Answer:** `R = 'Greetings, traveler!'.`

---

### Exercise 7: DCG Parse Success

**Problem:** Does `phrase(sentence, [the, dog, eats, the, cat])` succeed with Section 6.4 DCG?

**Solution:**

1. `noun_phrase` → `[the, dog]`
2. `verb_phrase` → `[eats, the, cat]`
3. Full sentence consumed; no tokens remain.
4. **Answer:** `true.`

---

### Exercise 8: CSP Search Space Size

**Problem:** For map coloring with 3 regions and 3 colors (no adjacency constraints), how large is the raw search space before constraints?

**Solution:**

1. Each of 3 regions independently chooses 3 colors.
2. $|\text{search space}| = 3^3 = 27$
3. With `A \= B, B \= C`, some assignments are pruned.
4. **Answer:** 27 unconstrained assignments; fewer after constraints.

---

## Exam Tip: CSP Problem Decomposition

When facing a Prolog application exam question, decompose in four steps:

1. **Identify variables** — what must be decided?
2. **Define domains** — what values can each variable take?
3. **List constraints** — what relations must hold among variables?
4. **Choose search strategy** — generate-and-test (standard Prolog) or CLP(FD) (if available)?

Write constraints as **relations**, not assignments. The engine assigns values by unification during search.

**Most common exam trap:** Forgetting that Prolog CSP solutions are returned one at a time via backtracking. "Find all solutions" requires pressing `;` interactively or wrapping with `findall/3`. For counting solutions, `findall(X, solve(X), L), length(L, N)` is the standard idiom.