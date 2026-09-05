# Principles of Programming Languages

## Course Overview
This course provides a rigorous, comparative study of programming language design, operational semantics, and implementation paradigms. Students explore formal syntax representation (BNF/EBNF grammars), lexical and syntactic analysis, static and dynamic type systems, scoping rules and activation records, memory management mechanisms, and contrasting programming paradigms: imperative, object-oriented, pure functional (Haskell), and declarative logic (Prolog).

## Course Code
401 (PRINCIPLES OF PROGRAMMING LANGUAGES)

## Prerequisites
* C Programming II (Code: 201)
* Object Oriented Programming (Code: 302)
* Data Structures and Algorithms (Code: 305)

---

## Topics Covered
* **Formal Syntax and Grammars**: Chomsky hierarchy, Context-Free Grammars (CFG), Backus-Naur Form (BNF/EBNF), left/right derivations, parse trees, syntactic ambiguity, and grammar disambiguation.
* **Names, Bindings, and Scoping**: Binding times (static vs. dynamic), variable lifetimes, lexical (static) scoping vs. dynamic scoping, referencing environments, and symbol table organization.
* **Functional Paradigm (Haskell)**: Pure functions, referential transparency, immutable state, lazy evaluation, pattern matching, structural recursion on lists, higher-order functions (`map`, `filter`, `foldr`), currying, and Algebraic Data Types (ADTs).
* **Logic Paradigm (Prolog)**: Horn clauses, first-order predicate logic, facts and rules, Robinson resolution principle, first-order unification, backtracking across choice points, and search pruning via the Cut (`!`) operator.
* **Type Systems & Parameter Passing**: Strong vs. weak typing, static vs. dynamic type checking, type inference (Hindley-Milner), parameter passing semantics (pass-by-value, pass-by-reference, pass-by-name, pass-by-need).
* **Runtime Memory Architecture**: Runtime stack layout, stack frames (activation records), static and dynamic chains, activation record pointer (`EBP`/`RBP`), heap management, and garbage collection algorithms (reference counting, mark-and-sweep, stop-and-copy).

---

## Learning Objectives
* Construct formal BNF/EBNF grammars and synthesize unambiguous parse trees for domain-specific language subsets.
* Trace variable bindings, identifier resolution, and scope visibility rules across nested static and dynamic block structures.
* Develop idiomatic, purely functional Haskell programs leveraging algebraic data types, pattern matching, and higher-order list combinators.
* Formulate declarative relational knowledge bases and execute query resolution in Prolog using recursion and backtracking controls.
* Analyze stack frame allocation, parameter passing mechanisms, and heap memory lifecycles during subroutine invocation.

---

## Directory Structure

| Directory | Description |
|:---|:---|
| [`Lectures/`](Lectures/) | Structured theory lecture modules and department slide notes |
| [`Exercises/`](Exercises/) | Solved theoretical drills on grammars, scoping, Haskell recursion, and laboratory solutions |
| [`Examples/`](Examples/) | Executable code implementations in Haskell, Prolog, and Python alongside walkthrough guides |
| [`Assignments/`](Assignments/) | Practical coursework deliverables, multi-paradigm routing projects, and laboratory rubrics |
| [`Tutorials/`](Tutorials/) | Hands-on tooling tutorials for the GHC compiler, SWI-Prolog REPL, and Python environments |
| [`Projects/`](Projects/) | Capstone design specification for a recursive descent syntax parser and AST evaluator |
| [`Exams/`](Exams/) | Model practice exams, interactive self-assessment quiz, and transcribed past examination papers |
| [`Resources/`](Resources/) | Language reference notes (C, C++, Haskell, Prolog, Python), conceptual mindmaps, and bibliography |

---

## Tooling and Execution Environment

### Haskell Interactive Environment (GHC)
To load and evaluate Haskell modules using GHCi:
```bash
ghci Examples/Haskell/examples_functional_paradigms.hs
```
Or execute directly using `runghc`:
```bash
runghc Examples/Haskell/examples_functional_paradigms.hs
```

### SWI-Prolog Querying Environment
To load and query the Prolog knowledge base:
```bash
swipl -s Examples/Prolog/examples_logic_programming.pl
```

### Python Multi-Paradigm Demonstrations
To execute the multi-paradigm stream processing scripts:
```bash
python3 Examples/Python/examples_multiparadigm_scripting.py
```