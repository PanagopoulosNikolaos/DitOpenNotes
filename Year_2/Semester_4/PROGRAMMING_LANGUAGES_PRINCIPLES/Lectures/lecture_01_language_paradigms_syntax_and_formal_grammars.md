# Lecture 01: Language Paradigms, Formal Syntax, and Context-Free Grammars

This lecture introduces the classification of programming language paradigms, the separation of syntax from semantics, Chomsky's hierarchy of formal languages, Context-Free Grammars (CFG) in Backus-Naur Form (BNF), derivation trees, and grammar ambiguity.

---

## 1. Programming Language Paradigms

A programming paradigm defines the computational model and conceptual abstractions used to structure and execute algorithms:

| Paradigm | Primary Abstraction | State & Control Flow | Canonical Languages |
|---|---|---|---|
| **Imperative / Procedural** | Sequential machine state mutations, statements | Mutable variables, explicit assignment, loops | C, Pascal, Fortran |
| **Object-Oriented (OOP)** | Interacting objects encapsulating state and behavior | Encapsulation, inheritance, polymorphism | Java, C++, Smalltalk |
| **Functional** | Mathematical functions as first-class citizens | Immutable values, pure functions, recursion, higher-order functions | Haskell, Scheme, OCaml, Erlang |
| **Logic / Declarative** | First-order logic predicates and relations | Facts, Horn clauses, Robinson unification, resolution search | Prolog, Datalog |
| **Multi-Paradigm** | Hybrid combinations of paradigms | Multi-modal: classes, closures, list comprehensions | Python, Rust, Scala |

---

## 2. Formal Language Syntax and Chomsky Hierarchy

Syntax specifies the structural validity of programs; semantics defines the execution meaning of syntactically valid programs.

### 2.1 Chomsky Hierarchy of Formal Languages
- **Type 3 (Regular Grammars):** Recognized by Finite State Automata (FSA). Used by lexical analyzers (tokenizers, `lex`/`flex`) to identify keywords, identifiers, and literals. Cannot handle arbitrarily nested structures (e.g., balanced parentheses).
- **Type 2 (Context-Free Grammars - CFG):** Recognized by Pushdown Automata (PDA). Used by syntax analyzers (parsers, `yacc`/`bison`) to represent nested hierarchical program structure.
- **Type 1 (Context-Sensitive):** Recognized by Linear Bounded Automata.
- **Type 0 (Unrestricted):** Recognized by Turing Machines.

---

## 3. Context-Free Grammars (CFG) and BNF

A Context-Free Grammar $G$ is a 4-tuple:

$$
G = (V_N, V_T, P, S)
$$

Where:
- $V_N$: Finite set of **Non-terminal symbols** (variables enclosed in `<...>` or capitalized).
- $V_T$: Finite set of **Terminal symbols** (tokens of the language, disjoint from $V_N$).
- $P$: Finite set of **Production rules** of the form $A \to \alpha$, where $A \in V_N$ and $\alpha \in (V_N \cup V_T)^*$.
- $S \in V_N$: Distinguished **Start symbol**.

### 3.1 Backus-Naur Form (BNF) Notation

```text
<expr>   ::= <expr> + <term> | <expr> - <term> | <term>
<term>   ::= <term> * <factor> | <term> / <factor> | <factor>
<factor> ::= ( <expr> ) | <number>
<number> ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
```

This grammar enforces standard arithmetic **operator precedence** ($*$ and $/$ bind tighter than $+$ and $-$) and **left-associativity** (left-recursive productions evaluate left-to-right).

---

## 4. Derivations and Parse Trees

A **derivation** is a sequence of production rule applications replacing non-terminals until only terminal tokens remain.
- **Leftmost Derivation:** The leftmost non-terminal is replaced at every step.
- **Rightmost Derivation:** The rightmost non-terminal is replaced at every step.
- **Parse Tree:** A hierarchical tree representation of a derivation whose root is $S$, internal nodes are non-terminals, and leaves are terminals.

---

## 5. Grammar Ambiguity

A Context-Free Grammar is **ambiguous** if there exists at least one valid string $w \in L(G)$ for which there exist:
- Two or more distinct parse trees, or equivalently,
- Two or more distinct leftmost derivations.

```
       Ambiguous Arithmetic: <E> ::= <E> + <E> | <E> * <E> | id
                     Target String: id + id * id

     Tree 1: (id + id) * id                     Tree 2: id + (id * id)
              <E>                                        <E>
             / | \                                      / | \
           <E> * <E>                                  <E> + <E>
          / | \    |                                   |   / | \
        <E> + <E>  id                                 id <E> * <E>
         |     |                                          |     |
        id    id                                         id    id
```

Ambiguity in programming languages is dangerous because distinct parse trees yield differing operational semantics (e.g., $(2+3)\times 4 = 20$ versus $2+(3\times 4) = 14$).
Grammars must be disambiguated by stratifying non-terminals into precedence levels or supplying parser precedence directives.

