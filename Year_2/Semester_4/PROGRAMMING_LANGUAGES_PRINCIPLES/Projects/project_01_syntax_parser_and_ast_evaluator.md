# Project 01: Recursive-Descent Parser and Abstract Syntax Tree Evaluator

## Project Overview
Design, implement, and benchmark an interpreter for a domain-specific arithmetic and functional expressions language (`MiniLang`). The project requires building a lexical analyzer (lexer), a predictive recursive-descent syntax parser based on an unambiguous Context-Free Grammar, an Abstract Syntax Tree (AST) representation, and an evaluator supporting lexical scope environments.

---

## Architectural and Technical Specifications

### 1. The MiniLang Formal Grammar (EBNF)

```text
<Program>    ::= <Statement>*
<Statement>  ::= "let" <Ident> "=" <Expr> ";"
               | "print" <Expr> ";"
               | "if" "(" <Expr> ")" "{" <Statement>* "}" "else" "{" <Statement>* "}"
<Expr>       ::= <LogicOr>
<LogicOr>    ::= <LogicAnd> ( "||" <LogicAnd> )*
<LogicAnd>   ::= <Equality> ( "&&" <Equality> )*
<Equality>   ::= <Relational> ( ( "==" | "!=" ) <Relational> )*
<Relational> ::= <Additive> ( ( "<" | "<=" | ">" | ">=" ) <Additive> )*
<Additive>   ::= <Multiplicative> ( ( "+" | "-" ) <Multiplicative> )*
<Multiplicative> ::= <Unary> ( ( "*" | "/" | "%" ) <Unary> )*
<Unary>      ::= ( "-" | "!" ) <Unary> | <Primary>
<Primary>    ::= <Integer> | <Float> | <Boolean> | <Ident> | "(" <Expr> ")"
```

### 2. Core Subsystems

#### 2.1 Lexical Analyzer (Scanner / Tokenizer)
- Scans input source stream and yields tokens: `(TokenType, Lexeme, LineNumber, ColumnNumber)`.
- Skips whitespace and single-line/multi-line comments (`// ...` and `/* ... */`).
- Emits clean syntax error diagnostics upon encountering illegal characters.

#### 2.2 Recursive-Descent Syntax Parser
- Implements predictive LL(1) recursive-descent parsing with one-token lookahead.
- Verifies grammar rules and constructs an Abstract Syntax Tree (AST).
- Disallows left-recursion and enforces operator precedence and associativity structurally.

#### 2.3 AST Evaluator and Lexical Environment
- Traverses AST nodes via recursive tree-walk evaluation or the Visitor Pattern.
- Implements nested lexical environments (symbol tables) supporting block scoping (`let` bindings inside conditional branches do not leak to parent scope).
- Runtime type checking: enforces valid types for arithmetic (`+`, `-`, `*`, `/`) and boolean operations (`&&`, `||`).

---

## Project Milestones

| Milestone | Deliverable | Target Validation |
|---|---|---|
| **Phase 1** | Lexer Implementation | Token stream output tested against complex input programs |
| **Phase 2** | Recursive-Descent Parser & AST | AST node generation verified with visual tree-printer output |
| **Phase 3** | Lexical Environment & Evaluator | Arithmetic evaluation, let bindings, and nested scoping tested |
| **Phase 4** | Control Flow & Final Test Suite | Conditionals (`if-else`), short-circuit logic, error diagnostics |

---

## Grading Rubric

| Criterion | Evaluation Metric | Weight |
|---|---|---|
| **Grammar Adherence & Parsing Rigor** | Accurate LL(1) parsing without backtracking, correct operator precedence | 30% |
| **Lexical Environment & Scoping** | Proper hierarchical frame implementation, lexical scope isolation | 25% |
| **Error Handling & Diagnostics** | Informative syntax and runtime error reports with line numbers | 20% |
| **Test Suite Coverage** | Comprehensive automated test cases covering edge cases, nesting, and precedence | 15% |
| **Technical Architecture Report** | Formal grammar documentation, AST diagrams, design trade-off analysis | 10% |

