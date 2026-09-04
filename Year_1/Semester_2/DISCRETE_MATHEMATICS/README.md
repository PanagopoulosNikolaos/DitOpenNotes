# Discrete Mathematics

## Course Overview
This course provides a rigorous mathematical foundation for computer science, emphasizing formal proof techniques, discrete mathematical structures, counting principles, recurrence relations, relational algebra, graph algorithms, and elementary automata theory.

## Course Code
203 (DISCRETE MATHEMATICS)

## Prerequisites
* Mathematical Analysis (Code: 101)

---

## Topics Covered
* **Mathematical Induction and Formal Proofs**: Weak and strong mathematical induction, well-ordering principle, direct proofs, contraposition, and proof by contradiction.
* **Propositional and Predicate Logic**: Truth tables, logical equivalences, De Morgan's laws, predicates, existential ($\exists$) and universal ($\forall$) quantifiers, and inference rules.
* **Set Theory and Boolean Operations**: Set identities, power sets, Cartesian products, indexed family of sets, and Venn diagrams.
* **Relations and Functions**: Properties of binary relations (reflexivity, symmetry, antisymmetry, transitivity), equivalence relations, equivalence classes, partial orderings (posets), and Hasse diagrams.
* **Combinatorics and Counting Principles**: Sum and product rules, permutations $P(n, r)$, combinations $C(n, r)$, binomial theorem, pigeonhole principle, and inclusion-exclusion principle.
* **Recurrence Relations**: Solving linear homogeneous recurrence relations with constant coefficients via the characteristic equation, divide-and-conquer recurrences, and the Master Theorem.
* **Graph Theory and Trees**: Simple and directed graphs, degree handshaking lemma, Euler paths/circuits, Hamilton cycles, graph isomorphism, planarity (Euler's formula), trees, and minimum spanning trees.
* **Automata Theory and Formal Languages**: Alphabets, strings, formal languages, regular expressions, and deterministic finite automata (DFA).

---

## Learning Objectives
* Construct mathematically rigorous deductive proofs using induction, contradiction, and algebraic manipulation.
* Model computational relationships using sets, binary relations, directed graphs, and trees.
* Solve combinatorial counting problems and calculate sequence bounds from linear recurrence relations.
* Analyze graph connectivity, planarity, and traversals using algorithmic methods.
* Implement computational logic and graph models in Python.

---

## Directory Structure

| Directory | Description |
|:---|:---|
| [`Lectures/`](Lectures/) | Structured theory lectures and official slide decks covering the eight course modules |
| [`Exercises/`](Exercises/) | Solved exercise compilations across all chapters, counting drills, and problem sets |
| [`Examples/`](Examples/) | Python implementations for truth table solvers, Eulerian traversals, relation closures, combinatorics, and Dijkstra |
| [`Assignments/`](Assignments/) | Formal laboratory coursework assignments with evaluation rubrics |
| [`Tutorials/`](Tutorials/) | Hands-on walkthroughs for proof construction by induction and graph isomorphism algorithms |
| [`Projects/`](Projects/) | Capstone term design project (Graph Theory Network Analyzer) |
| [`Exams/`](Exams/) | Archival examination papers, midterm solutions, and graded practice exams |
| [`Resources/`](Resources/) | Granular chapter notes, curriculum mindmaps, and textbook bibliographies |

---

## Computational Examples in Python

The [`Examples/`](Examples/) directory contains standalone Python implementations demonstrating discrete algorithms:

```bash
# 1. Truth table generator and satisfiability solver
python3 Examples/01_truth_table_and_satisfiability.py

# 2. Graph representations and Eulerian path detection
python3 Examples/02_graph_representations_and_eulerian.py

# 3. Binary relations and Warshall transitive closure
python3 Examples/03_relations_and_transitive_closure.py

# 4. Combinatorics, permutations, and recurrence solver
python3 Examples/04_combinatorics_and_recurrences.py

# 5. Dijkstra shortest path algorithm on weighted graphs
python3 Examples/05_dijkstra_shortest_path.py
```
