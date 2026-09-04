# Practice Exam 01: Principles of Programming Languages (Course 401)

This comprehensive practice examination tests proficiency across formal grammars, runtime memory models and scoping, pure functional programming in Haskell, and declarative logic programming in Prolog.

**Duration:** 2 Hours  
**Total Points:** 100 Points  

---

## Part A: Formal Syntax and Grammar Analysis (25 Points)

### Question 1 (15 Points)
Consider the Context-Free Grammar $G$:
$$E \to E - E \mid E / E \mid \text{id}$$

1. Prove that grammar $G$ is ambiguous by demonstrating two distinct parse trees for the expression:
   $$\text{id} - \text{id} / \text{id}$$
2. What are the two distinct arithmetic values produced if $\text{id}$ evaluates to numbers $12, 6, 2$?
3. Construct an unambiguous grammar that forces $/$ to have higher precedence than $-$, with both operators left-associative.

### Question 2 (10 Points)
Explain the difference between a **Context-Free Grammar (CFG)** and a **Regular Grammar**. Why can regular expressions not be used to verify arbitrary nested parenthesized expressions in programming languages?

---

## Part B: Names, Scopes, and Runtime Stack Management (25 Points)

### Question 3 (15 Points)
Consider the following pseudo-code program:

```text
var a: integer = 10;
var b: integer = 20;

procedure alpha() {
    print(a, b);
}

procedure beta() {
    var a: integer = 100;
    alpha();
}

procedure gamma() {
    var b: integer = 200;
    beta();
}

procedure main() {
    gamma();
}
```

1. What is printed under **Static (Lexical) Scoping**? Justify with reference to the lexical nesting structure.
2. What is printed under **Dynamic Scoping**? Show the active stack frames when `alpha()` is invoked.

### Question 4 (10 Points)
Draw the layout of an **Activation Record (Stack Frame)** on the call stack for a function in C. Explain the role of the **Frame Pointer (FP)** and the **Return Address**.

---

## Part C: Functional Programming in Haskell (25 Points)

### Question 5 (15 Points)
Write a pure Haskell function:
```haskell
runLengthEncode :: (Eq a) => [a] -> [(Int, a)]
```
That compresses consecutive duplicate elements of a list into pairs of `(count, element)`.
Example:
```haskell
runLengthEncode "aaabbcca" -- yields [(3, 'a'), (2, 'b'), (2, 'c'), (1, 'a')]
```
Implement this using recursion and pattern matching without using external libraries.

### Question 6 (10 Points)
Explain the concept of **Lazy Evaluation (Call-by-Need)** in Haskell. Give an example showing how lazy evaluation enables working with infinite data structures.

---

## Part D: Logic Programming in Prolog (25 Points)

### Question 7 (15 Points)
Given the Prolog predicate:
```prolog
duplicate_elements([], []).
duplicate_elements([H | T], [H, H | Res]) :- duplicate_elements(T, Res).
```
1. Trace the query `?- duplicate_elements([a, b], Output).` showing all unifications.
2. Can this predicate run in reverse (i.e., `?- duplicate_elements(Input, [a, a, b, b]).`)? Explain why or why not.

### Question 8 (10 Points)
Explain the purpose of the **Cut (`!`)** operator in Prolog. What is the difference between a **Green Cut** and a **Red Cut**? Give an example of each.

---

## Complete Solution and Grading Guide

### Solution to Part A

#### Question 1
1. **Ambiguity Proof:**
   - Tree 1: Root $E \to E - E$. Right child is $E \to E / E$. Expression evaluates as $\text{id} - (\text{id} / \text{id})$.
   - Tree 2: Root $E \to E / E$. Left child is $E \to E - E$. Expression evaluates as $(\text{id} - \text{id}) / \text{id}$.
   Two distinct parse trees exist $\implies$ Grammar is ambiguous.
2. **Values:**
   - Tree 1: $12 - (6 / 2) = 12 - 3 = \mathbf{9}$.
   - Tree 2: $(12 - 6) / 2 = 6 / 2 = \mathbf{3}$.
3. **Unambiguous Grammar:**
   $$E \to E - T \mid T$$
   $$T \to T / F \mid F$$
   $$F \to \text{id}$$
*(15 Points: 6+4+5)*

#### Question 2
- **Difference:** Regular grammars have production rules restricted to $A \to aB$ or $A \to a$. They are recognized by finite state automata (FSA) with finite memory. Context-Free Grammars allow arbitrary right-hand sides and are recognized by pushdown automata (PDA) equipped with an unbounded stack.
- **Parentheses:** Matching nested parentheses of arbitrary depth requires counting/stack memory, which exceeds the finite state capacity of regular grammars (proven via the Pumping Lemma for Regular Languages).
*(10 Points)*

---

### Solution to Part B

#### Question 3
1. **Lexical Scoping:**
   `alpha()` is defined at the global scope. It resolves `a` and `b` in the global environment where $a = 10, b = 20$.
   Output: $\mathbf{10, \ 20}$.
2. **Dynamic Scoping:**
   Call chain: `main` $\to$ `gamma` ($b=200$) $\to$ `beta` ($a=100$) $\to$ `alpha`.
   When `alpha()` references `a`, it finds $a = 100$ in caller `beta()`.
   When `alpha()` references `b`, it skips `beta()` (no local $b$) and finds $b = 200$ in caller `gamma()`.
   Output: $\mathbf{100, \ 200}$.
*(15 Points: 7+8)*

#### Question 4
- **Stack Frame Layout:** Function parameters, return address, saved frame pointer, local variables, temporary registers.
- **Return Address:** Holds the memory address of the instruction in the caller function to resume after the callee executes `ret`.
- **Frame Pointer:** Fixed base pointer (`EBP`/`RBP`) providing a stable reference address for accessing function parameters (positive offsets) and local variables (negative offsets), independent of variable stack pointer (`ESP`/`RSP`) movements.
*(10 Points)*

---

### Solution to Part C

#### Question 5
```haskell
runLengthEncode :: (Eq a) => [a] -> [(Int, a)]
runLengthEncode [] = []
runLengthEncode (x:xs) = encodeCount 1 x xs
  where
    encodeCount count current [] = [(count, current)]
    encodeCount count current (y:ys)
      | current == y = encodeCount (count + 1) current ys
      | otherwise    = (count, current) : encodeCount 1 y ys
```
*(15 Points)*

#### Question 6
- **Lazy Evaluation:** Expressions are not evaluated when bound to variables, but deferred as uncomputed closures ("thunks"). Evaluation occurs only when the value is strictly needed by an output operation or pattern match.
- **Infinite Data Structures:**
  ```haskell
  naturals = [1..]          -- Infinite list of positive integers
  firstFive = take 5 naturals -- Evaluates only [1, 2, 3, 4, 5] and terminates
  ```
*(10 Points)*

---

### Solution to Part D

#### Question 7
1. **Trace:**
   - Step 1: Matches rule with $H = a, T = [b]$. Goal becomes: `duplicate_elements([b], Res1)`.
   - Step 2: Matches rule with $H = b, T = []$. Goal becomes: `duplicate_elements([], Res2)`.
   - Step 3: Matches base fact: `Res2 = []`.
   - Unwinding: $\text{Res1} = [b, b]$, $\text{Output} = [a, a, b, b]$.
2. **Reverse Execution:**
   Yes. Because Prolog uses unification across relations, passing `[a, a, b, b]` as the second argument unifies $H = a$, and recursively recovers `Input = [a, b]`.
*(15 Points: 8+7)*

#### Question 8
- **The Cut (`!`):** Commits the engine to choices made in the current predicate, preventing backtracking into earlier alternatives.
- **Green Cut:** Prunes search branches without altering declarative semantics (pure performance optimization).
  *Example:* `max(X, Y, X) :- X >= Y, !. max(X, Y, Y).`
- **Red Cut:** Alters the logical declarative meaning; removing it changes program results.
  *Example:* `not(P) :- P, !, fail. not(_).`
*(10 Points)*

