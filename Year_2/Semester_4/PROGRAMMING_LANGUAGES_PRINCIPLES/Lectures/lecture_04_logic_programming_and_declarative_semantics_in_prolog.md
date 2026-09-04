# Lecture 04: Logic Programming and Declarative Semantics in Prolog

This lecture explores the logic programming paradigm: declarative semantics, Horn clauses, Robinson's first-order unification algorithm, SLD-resolution proof trees, depth-first backtracking search, and the cut operator (`!`).

---

## 1. The Declarative Paradigm: Kowalski's Equation

Robert Kowalski summarized logic programming as:

$$
\text{Algorithm} = \text{Logic} + \text{Control}
$$

- **Logic:** The programmer declares **what** relationships and truths hold in the problem domain (knowledge base).
- **Control:** The runtime inference engine (Prolog interpreter) decides **how** to evaluate, search, and satisfy queries using mathematical deduction.

---

## 2. Syntax of First-Order Horn Clauses

A Prolog program consists of a database of **Horn clauses** (clauses with at most one positive literal):
- **Facts (Unit clauses):** Assert absolute unconditional truths:
  ```prolog
  parent(zeus, ares).
  parent(zeus, athena).
  ```
- **Rules (Conditional Horn clauses):** Form: `Head :- Body.` Meaning: "Head is true IF Body is true".
  ```prolog
  grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
  ```
- **Queries / Goals:** Inquiries posed to the interpreter:
  ```prolog
  ?- grandparent(zeus, Who).
  ```

### 2.1 Terms in Prolog
- **Atoms:** Constants beginning with lowercase letters (`zeus`, `apple`) or enclosed in single quotes.
- **Numbers:** Integers and floating-point literals (`42`, `3.14`).
- **Variables:** Identifiers beginning with an uppercase letter (`X`, `Person`) or underscore (`_` represents an anonymous wildcard variable).
- **Compound Terms (Structures):** Functor followed by arguments (`date(2026, 9, 4)`).

---

## 3. Robinson's Unification Algorithm

Unification is the algorithmic process of finding a most general variable substitution $\theta$ that makes two terms syntactically identical:

$$
T_1 \theta = T_2 \theta
$$

### 3.1 Unification Rules
1. Two identical constants unify: `apple = apple`.
2. A variable $X$ unifies with any term $T$, binding $X \leftarrow T$ (unless $T$ contains $X$, which triggers an **occurs check** failure in formal logic).
3. Two compound terms $f(s_1, \dots, s_n)$ and $g(t_1, \dots, t_m)$ unify if and only if $f == g$, $n == m$, and each respective pair of arguments $s_i$ and $t_i$ unifies.

Examples:
- `p(X, b) = p(a, Y) \implies \{ X \leftarrow a, Y \leftarrow b \}`.
- `p(X, X) = p(a, b) \implies` **Fails** (cannot bind $X$ to both $a$ and $b$).

---

## 4. SLD-Resolution and Backtracking Search

Prolog answers queries using **SLD-Resolution** (Selective Linear Definite clause resolution) coupled with Depth-First Search (DFS) with backtracking:
1. Matches the current leftmost goal against rules in the database top-to-bottom.
2. If unification succeeds, pushes a choice point onto the search stack and recursively pursues the subgoals in the rule body.
3. If a subgoal fails, the engine **backtracks** to the most recent choice point, undoes variable bindings, and attempts the next alternative clause.

---

## 5. Controlling Search: The Cut Operator (`!`)

The **Cut** (`!`) is a built-in nullary predicate that always succeeds, but dynamically commits the interpreter to all choices made since the parent clause was entered.

```prolog
max(X, Y, X) :- X >= Y, !.
max(X, Y, Y).
```

### 5.1 Cut Classifications
- **Green Cut:** Prunes search branches that are guaranteed not to contain any additional valid solutions, without altering the declarative meaning of the program (improves execution efficiency).
- **Red Cut:** Alters the declarative meaning of the program; removing a red cut changes the set of solutions produced (used for default fallbacks or negation-as-failure).

