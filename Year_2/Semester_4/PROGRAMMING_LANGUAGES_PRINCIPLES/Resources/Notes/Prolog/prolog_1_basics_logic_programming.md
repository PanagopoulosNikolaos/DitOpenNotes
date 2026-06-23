# Prolog — Basics of Logic Programming

Prolog is a declarative logic programming language whose programs are **knowledge bases** composed of facts and rules. Execution is query-driven: the programmer states *what* is true (relations and constraints) and asks questions; a built-in **logical inference engine** attempts to prove the query by deriving consequences from the knowledge base. Unlike imperative languages, control flow is not explicitly coded — it emerges from resolution, unification, and backtracking (covered in `prolog_2_execution_mechanisms.md`).

---

## 1. Knowledge Base Structure

### 1.1 Concept Overview

A Prolog program is a collection of **clauses** stored in a knowledge base (KB). Clauses fall into two categories:

1. **Facts** — unconditional assertions about ground or partially ground relations.
2. **Rules** — conditional assertions (Horn clauses) that hold when their body goals succeed.

The KB is passive data until a **query** activates the inference engine.

### 1.2 Syntax Reference

```
<fact>       ::= <atom>(<term>, ..., <term>) .
<rule>       ::= <head> :- <body> .
<head>       ::= <atom>(<term>, ..., <term>)
<body>       ::= <goal> { , <goal> }
<goal>       ::= <atom>(<term>, ..., <term>)
<query>      ::= ?- <goal> { , <goal> } .
<term>       ::= <atom> | <variable> | <number> | <list> | <compound>
<variable>   ::= <UppercaseLetter><alphanumeric>*   % e.g., X, Parent, _Result
<atom>       ::= <lowercase_identifier> | 'quoted atom'
```

- `.` terminates every fact and rule.
- `:-` (if) separates rule head from body; read as "is true if".
- `,` (and) conjoins goals in a body or query.
- `;` (or) disjoins alternative goals (introduced in later sections).

### 1.3 Behavioral Description

| Construct | Role | Evaluation |
| :--- | :--- | :--- |
| Fact | Asserts a relation unconditionally | Succeeds when unified with matching query |
| Rule | Defines derived relations | Succeeds when all body goals succeed |
| Query | Question posed to the KB | Engine searches for proofs; may bind variables |
| Variable | Placeholder for unknown term | Bound by unification during proof search |
| Atom | Constant symbol (predicate or functor name) | Must match exactly (case-sensitive) |

### 1.4 Parameter Reference — Clause Components

| Name | Type/Values | Required | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| Predicate name | atom | Yes | — | Identifies the relation (e.g., `parent`, `likes`) |
| Arity | non-negative integer | Yes | — | Number of arguments; `parent/2` has arity 2 |
| Arguments (terms) | atom, variable, number, compound | Per clause | — | Positional relation components |
| Rule body goals | comma-separated goals | For rules | — | Conditions that must all succeed |
| Query variables | uppercase identifiers | Optional | unbound | Receive bindings when proof succeeds |

---

## 2. Facts

### 2.1 Concept Overview

A **fact** is a clause with no body — a direct assertion that a relation holds between specific terms. Facts form the ground truth of the KB.

### 2.2 Syntax Reference

```
<predicate>(<arg1>, <arg2>, ..., <argN>) .
```

### 2.3 Behavioral Description

Facts are always true within the KB. When a query unifies with a fact, the engine reports success. If the query contains variables, the engine reports the bindings that make the unification succeed.

```prolog
% Family relations knowledge base.
parent(alice, bob).
parent(alice, carol).
parent(bob, dave).
parent(bob, eve).

male(bob).
male(dave).
female(alice).
female(carol).
female(eve).
```

```prolog
?- parent(alice, bob).
```

```text
true.
```

```prolog
?- parent(alice, X).
```

```text
X = bob ;
X = carol.
```

> **[Key Insight]** A single fact can answer multiple query shapes depending on which arguments are variables. `parent(alice, X)` asks "who are Alice's children?"; `parent(X, bob)` asks "who is Bob's parent?"

---

## 3. Rules (Horn Clauses)

### 3.1 Concept Overview

A **rule** defines a relation in terms of other relations. Structurally, it is a **Horn clause**: exactly one positive literal (the head) and zero or more positive literals in the body (no negated disjunction in standard Prolog).

**Logical reading:**

$$
\text{head}(X_1, \ldots, X_n) \leftarrow \text{goal}_1 \land \text{goal}_2 \land \cdots \land \text{goal}_m
$$

In Prolog syntax: `head(...) :- goal1, goal2, ..., goalm.`

### 3.2 Syntax Reference

```
<head>(<terms>) :- <goal1>, <goal2>, ..., <goalN> .
```

### 3.3 Behavioral Description

A rule succeeds when **every** goal in its body succeeds in sequence (conjunction). The head is considered proven with the variable bindings accumulated from the body.

```prolog
likes(alice, pizza).
likes(bob, sushi).
likes(carol, pizza).
likes(dave, sushi).

% Mutual liking: both must like each other.
dating(X, Y) :- likes(X, Y), likes(Y, X).
```

```prolog
?- dating(alice, carol).
```

```text
true.
```

```prolog
?- dating(alice, X).
```

```text
false.
```

```prolog
?- dating(X, Y).
```

```text
X = bob, Y = dave ;
X = dave, Y = bob.
```

### 3.4 Horn Clause Structure Table

| Component | Prolog Syntax | Logical Meaning |
| :--- | :--- | :--- |
| Head | `dating(X, Y)` | Conclusion to prove |
| Body goal 1 | `likes(X, Y)` | Premise: X likes Y |
| Body goal 2 | `likes(Y, X)` | Premise: Y likes X |
| Conjunction | `,` | All premises required |

---

## 4. Queries and the Inference Engine

### 4.1 Concept Overview

A **query** asks the inference engine whether a goal can be derived from the KB. Outcomes fall into three categories:

1. **Ground success** — query with no variables; answer is `true.` or `false.`
2. **Variable instantiation** — query with variables; answer is bindings for variables, possibly multiple solutions separated by `;`
3. **Failure** — no proof exists; answer is `false.`

### 4.2 Syntax Reference

```
?- <goal> .
?- <goal1>, <goal2> .
```

### 4.3 Behavioral Description

| Query Type | Example | Typical Response |
| :--- | :--- | :--- |
| Existence (ground) | `?- parent(alice, bob).` | `true.` |
| Single-variable | `?- parent(alice, Child).` | `Child = bob ; Child = carol.` |
| Multi-variable | `?- parent(Parent, Child).` | All `(Parent, Child)` pairs from facts |
| Conjunctive | `?- parent(P, C), female(C).` | Parents of female children |
| No solution | `?- parent(alice, dave).` | `false.` |

```prolog
?- parent(P, C), female(C).
```

```text
P = alice, C = carol.
```

```prolog
?- parent(alice, dave).
```

```text
false.
```

### 4.4 Inference Engine Responsibilities

The engine performs three core operations (detailed in `prolog_2_execution_mechanisms.md`):

1. **Unification** — match query terms with fact/rule heads, binding variables.
2. **Resolution** — apply rules via backward chaining to reduce goals to provable subgoals.
3. **Backtracking** — on failure, undo bindings and try alternative clauses.

---

## 5. Declarative vs. Imperative Reading

### 5.1 Concept Overview

Prolog programs are read **declaratively** (what is true) and executed **procedurally** (how the engine searches). Both readings must be understood for exam questions.

### 5.2 Comparative Analysis

| Aspect | Imperative (Python, C++) | Prolog |
| :--- | :--- | :--- |
| Program structure | Sequence of commands | Collection of facts and rules |
| Control flow | Explicit (`if`, `for`, `while`) | Implicit (engine search order) |
| State | Mutable variables | Logical bindings during search |
| Output | Return values, side effects | Success/failure + variable bindings |
| Problem style | How to compute | What relations hold |

### 5.3 Dual Reading Example

```prolog
sibling(X, Y) :- parent(P, X), parent(P, Y), X \= Y.
```

| Reading | Interpretation |
| :--- | :--- |
| Declarative | "X and Y are siblings if some parent P has both X and Y as children, and X is not Y." |
| Procedural | "To prove `sibling(X,Y)`, find P such that `parent(P,X)` succeeds, then `parent(P,Y)`, then verify X and Y differ." |

---

## Common Errors and Gotchas

### Error 1: Missing Period Terminator

**Cause:** Facts and rules must end with `.` A missing period causes a syntax error or causes the next clause to be parsed as part of the current one.

```prolog
% Wrong:
parent(alice, bob)

% Correct:
parent(alice, bob).
```

**Resolution:** Every fact and rule ends with `.` on its own logical line.

### Error 2: Variable vs. Atom Casing

**Cause:** `Parent` (variable) and `parent` (atom/predicate) are distinct. Lowercase identifiers are atoms; uppercase starts a variable.

```prolog
?- Parent(alice, bob).   % Calls predicate named Parent/2 — likely undefined.
?- parent(alice, bob).   % Correct: queries fact parent/2.
```

**Resolution:** Predicate names and constant atoms are lowercase; use uppercase only for variables.

### Error 3: Treating Rules as Sequential Assignment

**Cause:** Reading `dating(X,Y) :- likes(X,Y), likes(Y,X).` as "first assign X, then assign Y" misses that the engine searches for bindings satisfying **both** goals simultaneously.

**Resolution:** Think in terms of constraint satisfaction: find values of `X` and `Y` such that all body goals succeed.

---

## Solved Exercises

### Exercise 1: Identify Clause Type

**Problem:** Classify each clause as fact or rule.

```prolog
color(red).
color(blue).
warm(X) :- color(X), X = red.
```

**Solution:**

1. `color(red).` — **fact** (no `:-` body).
2. `color(blue).` — **fact**.
3. `warm(X) :- color(X), X = red.` — **rule** (has `:-` with two body goals).

---

### Exercise 2: Ground Query Evaluation

**Problem:** Given the KB below, evaluate `?- teaches(prof_smith, cs101).`

```prolog
teaches(prof_smith, cs101).
teaches(prof_jones, cs102).
enrolled(alice, cs101).
```

**Solution:**

1. Query goal `teaches(prof_smith, cs101)` unifies with fact `teaches(prof_smith, cs101).`
2. Unification succeeds with no variables to bind.
3. **Answer:** `true.`

---

### Exercise 3: Variable Instantiation

**Problem:** List all answers to `?- teaches(Prof, cs101).` using the KB from Exercise 2.

**Solution:**

1. Scan KB for `teaches/2` facts where second argument unifies with `cs101`.
2. `teaches(prof_smith, cs101)` matches with `Prof = prof_smith`.
3. `teaches(prof_jones, cs102)` does not match `cs101`.
4. **Answer:** `Prof = prof_smith.`

---

### Exercise 4: Rule Body Conjunction

**Problem:** Define `enrolled_in_cs(Student) :- enrolled(Student, Course), teaches(_, Course), sub_string(Course, 0, 2, _, 'cs').` and evaluate `?- enrolled_in_cs(alice).` with the KB from Exercise 2 plus `sub_string/5` built-in behavior for prefix `cs`.

**Solution:**

1. `enrolled(alice, cs101)` succeeds → `Course = cs101`.
2. `teaches(_, cs101)` succeeds (prof_smith teaches it).
3. `sub_string(cs101, 0, 2, _, 'cs')` succeeds (`cs` is prefix).
4. All body goals succeed → head proven.
5. **Answer:** `true.`

---

### Exercise 5: Horn Clause Logical Form

**Problem:** Write the logical formula for `dating(X, Y) :- likes(X, Y), likes(Y, X).`

**Solution:**

$$
\forall X, Y \; \big( \text{likes}(X, Y) \land \text{likes}(Y, X) \rightarrow \text{dating}(X, Y) \big)
$$

Equivalently as a Horn clause:

$$
\text{dating}(X, Y) \leftarrow \text{likes}(X, Y) \land \text{likes}(Y, X)
$$

---

### Exercise 6: Failed Query Analysis

**Problem:** Why does `?- dating(alice, bob).` fail given only:

```prolog
likes(alice, pizza).
likes(bob, sushi).
dating(X, Y) :- likes(X, Y), likes(Y, X).
```

**Solution:**

1. To prove `dating(alice, bob)`, body requires `likes(alice, bob)` and `likes(bob, alice)`.
2. `likes(alice, bob)` — no matching fact; fails.
3. Even if the first goal could succeed, `likes(bob, alice)` also has no matching fact.
4. **Answer:** `false.` — mutual liking is not established.

---

### Exercise 7: Multi-Solution Query

**Problem:** How many solutions does `?- parent(P, C).` produce with the family KB from Section 2?

**Solution:**

1. `parent(alice, bob).` → `P=alice, C=bob`
2. `parent(alice, carol).` → `P=alice, C=carol`
3. `parent(bob, dave).` → `P=bob, C=dave`
4. `parent(bob, eve).` → `P=bob, C=eve`
5. **Answer:** 4 solutions.

---

### Exercise 8: Conjunctive Query Filtering

**Problem:** Evaluate `?- parent(P, C), male(C).` with the Section 2 KB.

**Solution:**

1. Try `P=alice, C=bob`: `male(bob)` succeeds.
2. Try `P=alice, C=carol`: `male(carol)` fails — backtrack.
3. Try `P=bob, C=dave`: `male(dave)` succeeds.
4. Try `P=bob, C=eve`: `male(eve)` fails.
5. **Answer:** `P = alice, C = bob ; P = bob, C = dave.`

---

## Exam Tip: Fact vs. Rule vs. Query Recognition

On exam questions, apply this three-step identification:

1. **Contains `:-`?** Yes → rule. No → fact (if it ends with `.` in the program) or query (if prefixed with `?-`).
2. **Has variables?** Facts can contain variables (unusual but valid); queries with variables expect bindings as answers.
3. **Read declaratively first:** State the logical meaning in plain English before tracing procedural execution. The declarative reading is almost always sufficient for "what does this program mean?" questions; procedural tracing is required for "what is the output order?" questions.

**Most common exam trap:** Confusing the direction of a relation. `parent(alice, bob)` means "alice is parent of bob", not the reverse. Relation arity and argument order are part of the predicate's meaning and are not commutative.