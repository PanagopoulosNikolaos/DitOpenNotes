# Exercises 01: Context-Free Grammars and Scoping Invariants

This practice problem set provides step-by-step solutions for demonstrating grammar ambiguity, constructing leftmost derivations, and evaluating variables under static vs. dynamic scoping.

---

## Problem 1: Demonstrating Grammar Ambiguity

### Question
Consider the Context-Free Grammar $G$ over alphabet $\{ a, b, +, * \}$:

$$
S \to S + S \mid S * S \mid a \mid b
$$

1. Prove that grammar $G$ is ambiguous by exhibiting two distinct leftmost derivations for the string $a + a * b$.
2. Draw the two distinct parse trees corresponding to these derivations.
3. Rewrite the grammar into an equivalent unambiguous grammar $G'$ that enforces:
   - Multiplication $*$ has higher precedence than addition $+$.
   - Both operators are left-associative.

---

### Solution

#### Part 1: Two Distinct Leftmost Derivations

**Derivation 1 (evaluates $+$ first, then $*$):**
$$S \implies \mathbf{S * S} \implies (\mathbf{S + S}) * S \implies a + S * S \implies a + a * S \implies a + a * b$$

**Derivation 2 (evaluates $*$ first, then $+$):**
$$S \implies \mathbf{S + S} \implies a + \mathbf{S} \implies a + \mathbf{S * S} \implies a + a * S \implies a + a * b$$

Because two distinct leftmost derivations exist for the identical string $a + a * b$, **grammar $G$ is ambiguous**.

#### Part 2: Parse Tree Comparison
- **Tree 1:** Root $S \to S * S$. Left child is subtree $S \to S + S$ (yields $(a + a) * b$).
- **Tree 2:** Root $S \to S + S$. Right child is subtree $S \to S * S$ (yields $a + (a * b)$).

#### Part 3: Unambiguous Stratified Grammar
Stratify non-terminals into precedence layers ($E$ for addition, $T$ for multiplication, $F$ for factors):

$$
\begin{aligned}
E &\to E + T \mid T \\
T &\to T * F \mid F \\
F &\to a \mid b
\end{aligned}
$$

- Left recursion ($E \to E + T$) enforces left-associativity.
- Placement of $*$ inside $T$ ensures multiplication is evaluated lower in the parse tree (higher precedence).

---

## Problem 2: Lexical vs. Dynamic Scoping Evaluation

### Question
Consider the pseudocode program below:

```text
var x: integer = 5;
var y: integer = 10;

procedure p() {
    print(x + y);
}

procedure q() {
    var x: integer = 20;
    var y: integer = 30;
    p();
}

procedure main() {
    var y: integer = 50;
    q();
}
```

What values are printed by the invocation of `p()` under:
1. **Lexical (Static) Scoping**?
2. **Dynamic Scoping**?

---

### Solution

#### Part 1: Lexical (Static) Scoping
Under lexical scoping, identifier bindings are determined by spatial nesting in the program text at compile time:
- Procedure `p()` is declared at global scope.
- In `p()`, identifiers `x` and `y` resolve to the global variables:
  - Global `x = 5`
  - Global `y = 10`
- Output: $5 + 10 = \mathbf{15}$.

#### Part 2: Dynamic Scoping
Under dynamic scoping, identifier bindings are determined by the execution call stack at runtime:
- Execution trace: `main()` calls `q()`, which calls `p()`.
- Active call stack when `p()` prints:
  - `main()` frame: $[y = 50]$
  - `q()` frame: $[x = 20, \ y = 30]$
  - `p()` frame: []
- When resolving `x`: Searches backward $\to$ finds $x = 20$ in `q()`.
- When resolving `y`: Searches backward $\to$ finds $y = 30$ in `q()`.
- Output: $20 + 30 = \mathbf{50}$.

