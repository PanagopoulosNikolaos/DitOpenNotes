# Assignment 01: Formal Logic, Predicates, and Set Operations

## Objective
Demonstrate mathematical rigor through formal deductive logic proofs, resolution refutation, quantified statements over discrete domains, and axiomatic set-theoretic identities.

---

## Assignment Problems

### Problem 1: Formal Deduction and Valid Arguments
Using propositional equivalence laws and rules of inference (Modus Ponens, Modus Tollens, Disjunctive Syllogism, Resolution), prove that the following argument is valid:
1. $p \to (q \lor r)$
2. $\neg q$
3. $p \land s$
4. $\therefore r$
Provide the specific inference rule or equivalence used at every step.

### Problem 2: Quantifier Negation and Predicate Logic
Translate each of the following natural language assertions into symbolic predicate logic, defining explicit predicate symbols and the domain of discourse:
1. "Every computer science student has submitted at least one programming assignment."
2. "There is a software module that no student was able to debug."
3. Negate both symbolic formulas using generalized De Morgan's laws such that no negation operator precedes a quantifier. Translate the resulting negated formulas back into clear English.

### Problem 3: Set Theoretic Proofs
Let $A, B,$ and $C$ be arbitrary sets within universal set $U$.
1. Prove rigorously that:
   $$(A \setminus B) \setminus C = A \setminus (B \cup C)$$
2. Determine whether the symmetric difference operator $\Delta$ distributes over intersection $\cap$:
   $$\text{Is } A \cap (B \Delta C) = (A \cap B) \Delta (A \cap C)?$$
   Provide a formal proof if true, or a concrete counterexample if false.

---

## Submission Guidelines & Evaluation
* Format: Clean Markdown or handwritten solutions rendered in LaTeX.
* Clarity: Every deduction step must cite the corresponding algebraic rule or inference principle.
* Total Points: 100 (Problem 1: 30 pts, Problem 2: 35 pts, Problem 3: 35 pts).

