# Exercises 02: Functional Dependencies and Normal Forms

This practice problem set provides step-by-step solutions for calculating attribute closures, determining candidate keys, identifying normal form violations (2NF, 3NF, BCNF), and synthesizing 3NF relational schemas.

---

## Problem 1: Attribute Closures and Candidate Key Discovery

### Given Schema and Dependencies
Let $R(A, B, C, D, E, F)$ be a relational schema with functional dependencies:

$$
F = \{ A \to BC, \ CD \to E, \ B \to D, \ E \to A \}
$$

### Tasks
1. Compute the attribute closure of $A$, denoted $A^+$.
2. Compute the attribute closure of $(B, C)$, denoted $(BC)^+$.
3. Find all candidate keys of $R$.

### Solution

#### Task 1: Closure of $A$ ($A^+$)
- Start with $A^{(0)} = \{ A \}$.
- Since $A \to BC$, add $B, C$: $A^{(1)} = \{ A, B, C \}$.
- Since $B \to D$ and $B \subseteq A^{(1)}$, add $D$: $A^{(2)} = \{ A, B, C, D \}$.
- Since $CD \to E$ and $\{ C, D \} \subseteq A^{(2)}$, add $E$: $A^{(3)} = \{ A, B, C, D, E \}$.
- No other FD can be applied. Notice attribute $F$ is never determined by $A$.
- Result:

$$
A^+ = \{ A, B, C, D, E \}
$$

#### Task 2: Closure of $(BC)$ ($(BC)^+$)
- Start with $(BC)^{(0)} = \{ B, C \}$.
- $B \to D \implies (BC)^{(1)} = \{ B, C, D \}$.
- $CD \to E \implies (BC)^{(2)} = \{ B, C, D, E \}$.
- $E \to A \implies (BC)^{(3)} = \{ A, B, C, D, E \}$.
- Result:

$$
(BC)^+ = \{ A, B, C, D, E \}
$$

#### Task 3: Candidate Keys of $R$
Observe that attribute $F$ does not appear on the right-hand side of any functional dependency in $F$. Therefore, $F$ must be present in every superkey of $R$.

Now test combinations containing $F$:
1. Check $(AF)$:
   $$(AF)^+ = A^+ \cup \{ F \} = \{ A, B, C, D, E, F \} = R$$
   Since $A^+ \neq R$ and $F^+ = \{ F \} \neq R$, $(AF)$ is minimal.
   Thus, **$AF$ is a candidate key**.

2. Check $(BCF)$:
   $$(BCF)^+ = (BC)^+ \cup \{ F \} = \{ A, B, C, D, E, F \} = R$$
   Check proper subsets:
   - $(BF)^+ = B^+ \cup \{ F \} = \{ B, D, F \} \neq R$
   - $(CF)^+ = \{ C, F \} \neq R$
   - $(BC)^+ \neq R$
   Thus, **$BCF$ is a candidate key**.

3. Check $(EF)$:
   $E \to A$, so $E^+ = A^+ = \{ A, B, C, D, E \}$.
   $$(EF)^+ = E^+ \cup \{ F \} = \{ A, B, C, D, E, F \} = R$$
   Neither $E$ nor $F$ alone determines $R$.
   Thus, **$EF$ is a candidate key**.

4. Check $(CDF)$:
   $CD \to E$, so $(CDF)^+ \supseteq (EF)^+ = R$.
   Check proper subsets: $(CF)^+ \neq R$, $(DF)^+ = \{ D, F \} \neq R$, $(CD)^+ = \{ C, D, E, A, B \} \neq R$.
   Thus, **$CDF$ is a candidate key**.

**All Candidate Keys:** $\{ AF, BCF, EF, CDF \}$.
**Prime Attributes:** $\{ A, B, C, D, E, F \}$ (All attributes are prime).

---

## Problem 2: Normal Form Testing and Decomposition

### Given Schema
$R(A, B, C, D)$ with $F = \{ A \to B, \ B \to C, \ C \to D, \ D \to A \}$.

### Tasks
1. Determine the highest normal form satisfied by $R$.
2. Explain whether BCNF decomposition is necessary.

### Solution
1. **Candidate Keys:**
   - $A \to B \to C \to D \to A$ forms a complete cycle.
   - $A^+ = \{ A, B, C, D \} = R \implies A$ is a candidate key.
   - Similarly, $B^+ = R$, $C^+ = R$, and $D^+ = R$.
   - The candidate keys are: $\{ A \}$, $\{ B \}$, $\{ C \}$, $\{ D \}$.
2. **Normal Form Analysis:**
   - For every FD in $F$ ($A \to B, B \to C, C \to D, D \to A$), the left-hand side determinant is a candidate key (hence a superkey).
   - Therefore, $R$ is already in **Boyce-Codd Normal Form (BCNF)**. No decomposition is needed.

