# 9. Sequential Circuits & FSM (Finite State Machines)

FSMs constitute the fundamental model for the design and analysis of sequential circuits. Each state corresponds to a group of outputs, and transitions occur at the clock edge. FSM design includes state reduction, encoding, and construction of next-state equations.

---

## 1. Theory of Sequential Circuits

### 1.1 Basic Properties

- The output depends on inputs **and** current state (memory)
- State = information stored in flip-flops
- Transition: $Q(t+1) = f(Q(t), \text{inputs}(t))$

### 1.2 Synchronous vs Asynchronous

| Characteristic | Synchronous | Asynchronous |
|:---|:---:|:---:|
| States | Flip-flops (edge-triggered) | Latches (level-triggered) |
| Clock | Common clock | None |
| Transition | At clock edge | Immediately after input change |
| Design | Safer | More complex analysis |

> **[Key Insight]** Almost all synchronous FSMs are designed with D flip-flops, and transitions occur at the rising edge of the clock.

### 1.3 Moore vs Mealy

**Moore:** The output depends only on the current state:
$$
\text{Output} = f(Q(t))
$$

**Mealy:** The output depends on current state and current inputs:
$$
\text{Output} = f(Q(t), \text{inputs}(t))
$$

| Characteristic | Moore | Mealy |
|:---|:---:|:---:|
| Output delay | +1 clock cycle | Immediate |
| Number of states | More | Fewer |
| Input dependence | No | Yes |

---

## 2. FSM Representation

### 2.1 State Diagram

- **Nodes:** States
- **Edges:** Transitions (with label `input/output`)
- **Initial state:** Double circle

### 2.2 State Table

| Current State | Input | Next State | Output |
|:---|:---:|:---:|:---:|
| $S_0$ | 0 | $S_1$ | 0 |
| $S_0$ | 1 | $S_2$ | 0 |
| $S_1$ | 0 | $S_0$ | 1 |
| $S_1$ | 1 | $S_3$ | 1 |

### 2.3 State Encoding

| Method | Number of FFs | Advantages |
|:---|:---:|:---|
| Binary | $\lceil \log_2 n \rceil$ | Minimum number of FFs |
| One-hot | $n$ (number of states) | Simple logic, speed |
| Gray | $\lceil \log_2 n \rceil$ | Only one bit changes each time |

---

## 3. FSM Design

### 3.1 FSM Analysis

1. Display diagram or table
2. Identify initial state
3. Extract transition table
4. Synthesize with logic

### 3.2 FSM Synthesis

1. Specification (state table)
2. State minimization (if applicable)
3. State encoding
4. Extract equations with K-Map
5. Implementation with FF + combinational logic

### 3.3 State Minimization

**Equivalent pairs method:** Two states are equivalent if:
1. They have the same output
2. For every input combination, they lead to equivalent states

**Implication Table:**
1. Draw triangular table
2. Mark pairs with different output (X)
3. Repeat check until stability
4. Merge equivalent states

---

## 4. Excitation & Output Tables

### 4.1 Excitation Table by FF Type

*Prerequisite: Chapter 8 — Excitation tables.*

### 4.2 K-Map for Next-State Equations

1. Create K-Map for each FF ($D_i$ or $J_i$, $K_i$)
2. Enter values from transition table
3. Simplify

### 4.3 K-Map for Outputs

If the FSM is Moore, the output depends only on the state.
If Mealy, the output depends on state + input.

---

## 5. FSM Examples

### 5.1 Sequence Detector "101"

**Detecting the sequence "101" in a bit stream.**

| State | Description | $x=0$ | $x=1$ | Output |
|:---:|:---|:---:|:---:|:---:|
| $S_0$ | Clear | $S_0$ | $S_1$ | 0 |
| $S_1$ | See "1" | $S_2$ | $S_1$ | 0 |
| $S_2$ | See "10" | $S_0$ | $S_1$ | 1 |

### 5.2 Traffic Controller

Counts 4 and resets: $S_0 \to S_1 \to S_2 \to S_3 \to S_0$.

### 5.3 Synchronous Mod-N Counter

*Prerequisite: Chapter 8 — Counters.*

---

## Solved Exercises

### Exercise 1: Detector "01"

**Problem:** Design a Mealy FSM detector for the sequence "01".

**Solution:**

| State | $x=0$ | $x=1$ | Output |
|:---:|:---:|:---:|:---:|
| $S_0$ | $S_1$ | $S_0$ | 0 |
| $S_1$ | $S_1$ | $S_0$ | 1 (if $x=1$) |

### Exercise 2: Moore vs Mealy

**Problem:** Compare Moore and Mealy for the same FSM.

**Solution:**

The Moore FSM would need more states to achieve the same functionality, but the outputs would be more reliable (they do not depend on glitches in the inputs).

### Exercise 3: State Minimization

**Problem:** Minimize an FSM with 4 states:

| State | $x=0$ | $x=1$ | Output |
|:---:|:---:|:---:|:---:|
| $A$ | $C$ | $B$ | 0 |
| $B$ | $D$ | $A$ | 1 |
| $C$ | $C$ | $D$ | 0 |
| $D$ | $D$ | $B$ | 0 |

**Solution:**

$B$ and $D$ have different outputs (1 vs 0), so they are not equivalent.
$A$ and $C$ have the same output (0):
- $A$: $x=0 \to C$, $x=1 \to B$
- $C$: $x=0 \to C$, $x=1 \to D$
They are not equivalent because they lead to different states.

### Exercise 4: Design with D FF

**Problem:** Design an FSM with D-FF for the "101" detector.

**Solution:**

3 states: $\lceil \log_2 3 \rceil = 2$ FFs. Encoding: $S_0=00$, $S_1=01$, $S_2=10$.

| State | $x=0$ | $x=1$ |
|:---:|:---:|:---:|
| $00$ | $00$ | $01$ |
| $01$ | $10$ | $01$ |
| $10$ | $00$ | $01$ |

$Q_1 Q_0$ next state equations (K-Map):
$$
Q_1(t+1) = Q_0\bar{x},\quad Q_0(t+1) = \bar{Q_1}x
$$

### Exercise 5: One-Hot Encoding

**Problem:** Apply one-hot encoding to the "101" detector.

**Solution:**

3 FFs: $Q_0, Q_1, Q_2$ (one for each state).
- $S_0$: $100$
- $S_1$: $010$
- $S_2$: $001$

Binary: $D_0 = \bar{Q_1}\bar{x} + \bar{Q_2}x$, etc.

### Exercise 6: Implication Table

**Problem:** Use implication table for 4 states.

**Solution:**

Draw triangular table with pairs $(A,B)$, $(A,C)$, $(A,D)$, $(B,C)$, $(B,D)$, $(C,D)$. Check equivalence through extraction.

### Exercise 7: Sequence Detector "1101"

**Problem:** Design an FSM detector for "1101" (Moore).

**Solution:**

5 states:
- $S_0$: clear
- $S_1$: see "1"
- $S_2$: see "11"
- $S_3$: see "110"
- $S_4$: see "1101" (output=1)

### Exercise 8: Transition Table to Diagram

**Problem:** Convert a transition table to a state diagram.

**Solution:**

Read the table, convert to nodes (states) and edges (transitions). Add initial state and outputs.

---

## Exam Tip: Sequence Detector

For FSM sequence detectors:
1. Record how many bits you have correctly detected so far (state = progress)
2. Each wrong bit returns to the beginning or a smaller subsequence
3. For "101": if you see "1010", recognize the "1" of the last bit as the start of a new sequence
