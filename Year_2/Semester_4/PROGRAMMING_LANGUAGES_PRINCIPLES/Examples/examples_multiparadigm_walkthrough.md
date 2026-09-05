# Multi-Paradigm Code Walkthrough: Haskell, Prolog, and Python

This guide provides a comparative walkthrough of solving core computer science problems across functional, declarative logic, and multi-paradigm languages.

---

## 1. Running the Examples

### Functional Programming in Haskell (`Haskell/examples_functional_paradigms.hs`)
Execute directly using the GHC Haskell compiler or interpreter:
```bash
# Run interactively using runghc
runghc Haskell/examples_functional_paradigms.hs

# Or compile with optimizations
ghc -O2 Haskell/examples_functional_paradigms.hs -o run_haskell
./run_haskell
```

### Declarative Logic Programming in Prolog (`Prolog/examples_logic_programming.pl`)
Load and query using SWI-Prolog:
```bash
swipl -s Prolog/examples_logic_programming.pl
```
Sample interactive queries in the SWI-Prolog REPL:
```prolog
% Find all prerequisites of Operating Systems (402)
?- hasPrerequisite(402, Prereq), course(Prereq, Title, ECTS).

% Compute length and sum of a list
?- listLength([10, 20, 30, 40], L).
?- sumList([10, 20, 30, 40], S).

% Find first prerequisite with cut operator
?- firstPrerequisite(401, P).
```

### Multi-Paradigm Scripting in Python (`Python/examples_multiparadigm_scripting.py`)
Run using standard Python 3:
```bash
python3 Python/examples_multiparadigm_scripting.py
```

---

## 2. Key Paradigm Comparisons

| Feature | Haskell (Functional) | Prolog (Logic) | Python (Multi-Paradigm) |
|:---|:---|:---|:---|
| **Computation Model** | Lambda calculus & expression reduction | First-order predicate calculus & resolution | Imperative Von Neumann + Object-Oriented + Functional extensions |
| **State & Variables** | Strictly immutable bindings | Logical variables bound through unification | Mutable references bound dynamically |
| **Control Flow** | Pure recursion & higher-order combinators | Automatic backtracking across choice points | Sequential loops, generators, and exception handling |
| **Type Checking** | Static, strong, Hindley-Milner inference | Dynamic / untyped symbolic terms | Dynamic typing with optional static type hints |
| **Primary Data Unit** | Algebraic Data Types (ADT) & lists | Horn clauses, compound terms, and lists | Objects, dicts, lists, and dataclasses |

