# Prolog — Execution Mechanisms

Prolog execution is driven by **backward chaining** over Horn clauses: a query goal is matched against clause heads, and rule bodies become new subgoals to prove. When a subgoal fails, the engine **backtracks** to the most recent choice point and tries the next alternative clause or binding. This file covers resolution, backtracking, recursive rule definitions, variable unification, and the academic database pattern from the course mindmap.

*Prerequisite: `prolog_1_basics_logic_programming.md` — facts, rules, queries, Horn clauses.*

---

## 1. Resolution and Backward Chaining

### 1.1 Concept Overview

**Resolution** is the inference rule that Prolog uses to derive answers. Given a goal $G$ and a clause $H \leftarrow B_1 \land \cdots \land B_n$, if $G$ unifies with $H$, then proving $G$ reduces to proving $B_1, \ldots, B_n$.

**Backward chaining** starts from the query (the theorem to prove) and works backward toward known facts.

### 1.2 Syntax Reference

Resolution is implicit — no user syntax. The engine applies it when matching:

```
?- <goal> .
```

against clauses of the form:

```
<head> :- <body1>, <body2>, ...
```

or facts:

```
<head> .
```

### 1.3 Behavioral Description

| Step | Action | Outcome |
| :--- | :--- | :--- |
| 1 | Select leftmost unproven goal | Current subgoal to resolve |
| 2 | Search KB top-to-bottom for matching clause | First unifiable clause chosen |
| 3 | Unify goal with clause head | Variable bindings recorded |
| 4 | Replace goal with clause body goals | New subgoals pushed (left-to-right order) |
| 5 | All subgoals empty | Query succeeds; bindings reported |
| 6 | Subgoal fails | Backtrack to last choice point |

```prolog
parent(alice, bob).
parent(bob, carol).

grandparent(X, Z) :- parent(X, Y), parent(Y, Z).

?- grandparent(alice, carol).
```

**Resolution trace:**

1. Goal: `grandparent(alice, carol)`
2. Unify with rule head → subgoals: `parent(alice, Y)`, `parent(Y, carol)`
3. `parent(alice, Y)` → `Y = bob`
4. `parent(bob, carol)` → succeeds
5. All goals proven → `true.`

```text
true.
```

> **[Key Insight]** Prolog uses **depth-first** search with **left-to-right** goal ordering. The order of clauses in the KB and goals in a body affects both performance and whether all solutions are found.

---

## 2. Backtracking

### 2.1 Concept Overview

**Backtracking** occurs when the engine cannot prove a subgoal. It unwinds to the most recent **choice point** — a place where an alternative clause or binding could be tried — and continues search.

### 2.2 Behavioral Description

| Event | Engine Response |
| :--- | :--- |
| Goal unifies with multiple clauses | Choice point created; first tried |
| Goal unifies with fact/rule producing variable bindings | Choice point if more clauses exist |
| Subgoal fails | Undo bindings since choice point; try next alternative |
| No alternatives remain | Fail to previous choice point |
| User presses `;` at prompt | Force backtracking for next solution |

```prolog
likes(alice, pizza).
likes(alice, sushi).
likes(bob, pizza).

favorite_food(Person, Food) :- likes(Person, Food).

?- favorite_food(alice, Food).
```

```text
Food = pizza ;
Food = sushi.
```

**Trace for second solution:**

1. First solution: `Food = pizza` (first matching fact).
2. User types `;` → backtrack.
3. Engine tries next `likes(alice, _)` fact → `Food = sushi`.
4. No more facts → return to prompt.

### 2.3 Choice Point Diagram

```
Query: favorite_food(alice, Food)
         |
    [choice: likes(alice, ?)]
       /         \
  Food=pizza   Food=sushi
  (1st fact)  (2nd fact, after ;)
```

---

## 3. Unification

### 3.1 Formal Definition

**Unification** finds a substitution $\theta$ such that two terms become syntactically identical. If such $\theta$ exists, the terms are **unifiable**.

For terms $t_1$ and $t_2$, a substitution $\theta$ is a unifier iff $t_1\theta = t_2\theta$.

### 3.2 Unification Rules

| Pattern | Result |
| :--- | :--- |
| Variable $V$ vs. term $T$ (occur check passes) | Bind $V = T$ |
| Atom vs. same atom | Succeed |
| Atom vs. different atom | Fail |
| Compound $f(s_1,\ldots,s_n)$ vs. $f(t_1,\ldots,t_n)$ | Unify each argument pair |
| Number vs. same number | Succeed |
| Number vs. different number | Fail |
| List $[H|T]$ vs. list $[H'|T']$ | Unify heads, then tails |

**Occur check:** A variable cannot unify with a term containing that variable (prevents infinite structures).

### 3.3 Worked Unification Examples

| $t_1$ | $t_2$ | Result |
| :--- | :--- | :--- |
| `X` | `bob` | `X = bob` |
| `parent(X, bob)` | `parent(alice, Y)` | `X = alice, Y = bob` |
| `f(X, X)` | `f(a, b)` | Fail |
| `[H|T]` | `[1, 2, 3]` | `H = 1, T = [2, 3]` |
| `X` | `f(X)` | Fail (occur check) |

```prolog
?- parent(X, bob) = parent(alice, Y).
```

```text
X = alice,
Y = bob.
```

---

## 4. Recursive Relationships

### 4.1 Concept Overview

Recursion in Prolog is expressed through rules that refer to the same predicate in the body. Every recursive predicate requires at least one **base case** (direct fact or non-recursive rule) and one **recursive case**.

### 4.2 Syntax Reference

```
<base_predicate>(<base_args>) .
<base_predicate>(<base_args>) :- <non_recursive_goals> .

<recursive_predicate>(<args>) :- <direct_condition> .
<recursive_predicate>(<args>) :- <recursive_condition>, <recursive_predicate>(<smaller_args>) .
```

### 4.3 Ancestor Relation

The mindmap defines `ancestor/2` with:

- **Base case:** $X$ is a direct parent of $Y$.
- **Recursive case:** $X$ is an ancestor of $Z$, and $Z$ is a parent of $Y$.

```prolog
parent(alice, bob).
parent(bob, carol).
parent(carol, dave).

% Base case: direct parent is an ancestor.
ancestor(X, Y) :- parent(X, Y).

% Recursive case: parent's ancestor is also an ancestor.
ancestor(X, Y) :- ancestor(X, Z), parent(Z, Y).
```

```prolog
?- ancestor(alice, dave).
```

**Trace:**

1. `ancestor(alice, dave)` → recursive case → `ancestor(alice, Z)`, `parent(Z, dave)`
2. `parent(Z, dave)` → `Z = carol`
3. `ancestor(alice, carol)` → recursive case → `ancestor(alice, Z2)`, `parent(Z2, carol)`
4. `parent(Z2, carol)` → `Z2 = bob`
5. `ancestor(alice, bob)` → base case → `parent(alice, bob)` succeeds
6. All subgoals succeed

```text
true.
```

```prolog
?- ancestor(A, dave).
```

```text
A = carol ;
A = bob ;
A = alice.
```

### 4.4 Recursion Trace Table

| Step | Goal | Result |
| :--- | :--- | :--- |
| 1 | `ancestor(alice, dave)` | Expand recursive rule |
| 2 | `ancestor(alice, carol)` | Expand recursive rule |
| 3 | `ancestor(alice, bob)` | Base case succeeds |
| 4 | Unwind | `ancestor(alice, carol)` succeeds |
| 5 | Unwind | `ancestor(alice, dave)` succeeds |

---

## 5. Academic Database Example

### 5.1 Concept Overview

Prolog naturally models relational data. The mindmap uses predicates `passed/3` and `enrolled/2` to represent student records, enabling queries that join relations through shared variables.

### 5.2 Schema

| Predicate | Arity | Meaning |
| :--- | :--- | :--- |
| `enrolled(Student, Course)` | 2 | Student is enrolled in Course |
| `passed(Student, Course, Grade)` | 3 | Student passed Course with Grade |
| `pass_grade(Grade)` | 1 | Grade is a passing grade (helper) |

### 5.3 Knowledge Base

```prolog
enrolled(alice, cs101).
enrolled(alice, math201).
enrolled(bob, cs101).
enrolled(carol, phys101).

passed(alice, cs101, 85).
passed(alice, math201, 72).
passed(bob, cs101, 55).
passed(carol, phys101, 90).

pass_grade(G) :- G >= 60.
```

### 5.4 Derived Rules

```prolog
% Student passed a course with a passing grade.
passed_course(Student, Course) :-
    passed(Student, Course, Grade),
    pass_grade(Grade).

% Enrolled and passed.
completed(Student, Course) :-
    enrolled(Student, Course),
    passed_course(Student, Course).
```

```prolog
?- completed(Student, cs101).
```

```text
Student = alice.
```

```prolog
?- completed(bob, cs101).
```

```text
false.
```

(Bob's grade 55 fails `pass_grade`.)

```prolog
?- passed_course(S, C), enrolled(S, C).
```

```text
S = alice, C = cs101 ;
S = alice, C = math201 ;
S = carol, C = phys101.
```

### 5.5 Variable Unification Across Relations

Shared variables in conjunctive queries act as **join keys**:

```prolog
?- enrolled(Student, Course), passed(Student, Course, Grade), Grade >= 80.
```

```text
Student = alice, Course = cs101, Grade = 85 ;
Student = carol, Course = phys101, Grade = 90.
```

The variable `Student` and `Course` link the two relations — the same binding must satisfy both predicates.

---

## Common Errors and Gotchas

### Error 1: Non-Terminating Recursion

**Cause:** Missing or unreachable base case causes infinite expansion.

```prolog
% Wrong: no base case.
bad_ancestor(X, Y) :- bad_ancestor(X, Z), parent(Z, Y).
```

**Resolution:** Always include at least one clause that does not call itself (direct `parent/2` fact or non-recursive rule).

### Error 2: Wrong Clause Order (Incomplete Solutions)

**Cause:** With a single recursive rule and no base case placed first, some ground queries may loop.

```prolog
% Risky: recursive clause first.
ancestor(X, Y) :- ancestor(X, Z), parent(Z, Y).
ancestor(X, Y) :- parent(X, Y).
```

**Resolution:** Place base cases before recursive cases. Prolog tries clauses top-to-bottom.

### Error 3: Confusing `=` with `==` or `is`

**Cause:** `=` is unification; `==` is term equality without binding; `is` evaluates arithmetic.

```prolog
?- X = 2 + 3.      % X = 2+3 (compound term)
?- X is 2 + 3.     % X = 5 (arithmetic)
?- 2 + 3 == 5.     % false (structures differ)
```

**Resolution:** Use `is` for arithmetic evaluation; use `=` for unification; use `=:=` for arithmetic comparison.

---

## Solved Exercises

### Exercise 1: Resolution Step Expansion

**Problem:** Expand the first resolution step for `?- grandparent(alice, carol).` using:

```prolog
grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
```

**Solution:**

1. Goal: `grandparent(alice, carol)`
2. Unify with head: `X = alice, Z = carol`
3. New subgoals: `parent(alice, Y)`, `parent(Y, carol)`
4. **Answer:** Two subgoals remain; next step resolves `parent(alice, Y)`.

---

### Exercise 2: Backtracking Count

**Problem:** How many solutions does `?- parent(X, bob).` produce with four parent facts where two list `bob` as child?

```prolog
parent(alice, bob).
parent(tom, bob).
parent(bob, carol).
```

**Solution:**

1. `parent(alice, bob)` → `X = alice`
2. Backtrack → `parent(tom, bob)` → `X = tom`
3. `parent(bob, carol)` — second arg does not unify with `bob`
4. **Answer:** 2 solutions.

---

### Exercise 3: Unification Result

**Problem:** Determine if `f(X, a) = f(b, Y)` unifies and state the binding.

**Solution:**

1. Functors match: `f/2`
2. Unify `X` with `b` → `X = b`
3. Unify `a` with `Y` → `Y = a`
4. **Answer:** Succeeds with `X = b, Y = a`.

---

### Exercise 4: Ancestor Trace

**Problem:** Trace `?- ancestor(bob, dave).` with the Section 4.3 KB.

**Solution:**

1. `ancestor(bob, dave)` → recursive → `ancestor(bob, Z)`, `parent(Z, dave)` → `Z = carol`
2. `ancestor(bob, carol)` → base → `parent(bob, carol)` succeeds
3. Unwind: `ancestor(bob, dave)` succeeds
4. **Answer:** `true.`

---

### Exercise 5: Ancestor Query — All Ancestors

**Problem:** List all `A` such that `ancestor(A, dave)` using Section 4.3 KB.

**Solution:**

1. `A = carol` (direct parent)
2. Backtrack → `A = bob` (parent of carol)
3. Backtrack → `A = alice` (parent of bob)
4. **Answer:** `A = carol ; A = bob ; A = alice.`

---

### Exercise 6: Academic DB — Who Failed?

**Problem:** Which enrolled students did **not** complete `cs101`? Use Section 5 KB.

**Solution:**

1. Enrolled in cs101: alice, bob.
2. `completed(alice, cs101)` → true (grade 85).
3. `completed(bob, cs101)` → false (grade 55).
4. **Answer:** bob.

---

### Exercise 7: Join via Shared Variable

**Problem:** Write a query to find all courses where alice has grade above 70.

**Solution:**

```prolog
?- passed(alice, Course, Grade), Grade > 70.
```

1. `passed(alice, cs101, 85)` → 85 > 70 succeeds
2. `passed(alice, math201, 72)` → 72 > 70 succeeds
3. **Answer:** `Course = cs101, Grade = 85 ; Course = math201, Grade = 72.`

---

### Exercise 8: Recursive vs. Base Clause Selection

**Problem:** For `ancestor(alice, bob)`, which clause fires first in the correctly ordered KB (base before recursive)?

**Solution:**

1. Base case: `ancestor(X, Y) :- parent(X, Y).`
2. `parent(alice, bob)` is a fact → base case succeeds immediately
3. Recursive clause is never reached
4. **Answer:** Base clause; result `true.` without recursion.

---

## Exam Tip: Trace Backward Chaining on Paper

For execution-mechanism exam questions, use this template:

1. **Write the goal stack** — leftmost goal is current.
2. **Mark choice points** with a $\checkmark$ whenever multiple clauses or facts can match.
3. **Record bindings** in a column; strike through on backtrack.
4. **Base case first** — when tracing recursion, confirm the base clause terminates the descent before unwinding.

**Most common exam trap:** Assuming Prolog searches all solutions automatically. It returns the first solution and waits; further solutions require explicit backtracking (`;` interactively, or `findall/3` in programs). Order of facts and rules directly determines which solution appears first.