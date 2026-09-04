# Exercises: Sequential Logic, Flip-Flop Synthesis, and FSM Design

## Context and Grounding
This problem set exercises sequential design techniques, flip-flop conversions, synchronous counter synthesis, and state machine analysis. It directly builds on `Lectures/lecture_03_sequential_circuits_and_fsm.md` and `Resources/Notes/08_flipflops_registers_counters.md`.

---

## Problems

### Problem 1: Flip-Flop Conversion (JK to D)
Convert an available JK flip-flop into a D flip-flop using minimal external combinational logic. Show the truth table, excitation requirements, and gate schematic equation.

### Problem 2: Synchronous 3-Bit Up/Down Gray Code Counter
Design a synchronous counter using T flip-flops that sequences through the 3-bit Gray code sequence:
$$000 \to 001 \to 011 \to 010 \to 110 \to 111 \to 101 \to 100 \to 000$$
Derive the minimal excitation equations for $T_2, T_1, T_0$.

### Problem 3: FSM Sequence Detector
Design a Moore Finite State Machine that detects the overlapping sequence `1011` on a continuous serial binary stream $X$. When the sequence is detected, output $Z$ must be asserted to `1` for one clock cycle.
1. Draw the state transition table.
2. Determine state assignments using binary representation.
3. Formulate D flip-flop input equations.

---

## Detailed Step-by-Step Solutions

### Solution 1: JK to D Conversion
A D flip-flop requires next state $Q_{\text{next}} = D$.
The JK flip-flop characteristic equation is $Q_{\text{next}} = J Q' + K' Q$.

Compare excitation requirements:
* When $D = 0$, we need $Q_{\text{next}} = 0 \implies J = 0, K = 1$.
* When $D = 1$, we need $Q_{\text{next}} = 1 \implies J = 1, K = 0$.

In both cases:
$$J = D, \quad K = D'$$
Thus, connect input $D$ directly to terminal $J$, and connect $D$ through an inverter (NOT gate) to terminal $K$.

### Solution 2: 3-Bit Gray Code Counter with T Flip-Flops
Recall that for a T flip-flop, $T = Q \oplus Q_{\text{next}}$ (toggle when $T=1$, hold when $T=0$).

State Transition Table:
| Present State ($Q_2 Q_1 Q_0$) | Next State ($Q_2^+ Q_1^+ Q_0^+$) | $T_2$ | $T_1$ | $T_0$ |
|---|---|---|---|---|
| `000` | `001` | 0 | 0 | 1 |
| `001` | `011` | 0 | 1 | 0 |
| `011` | `010` | 0 | 0 | 1 |
| `010` | `110` | 1 | 0 | 0 |
| `110` | `111` | 0 | 0 | 1 |
| `111` | `101` | 0 | 1 | 0 |
| `101` | `100` | 0 | 0 | 1 |
| `100` | `000` | 1 | 0 | 0 |

K-Map Minimization for $T_2, T_1, T_0$:
* **$T_2$**: 1s at states `010` and `100`:
  $$T_2 = Q_2' Q_1 Q_0' + Q_2 Q_1' Q_0' = (Q_2 \oplus Q_1) Q_0'$$
* **$T_1$**: 1s at states `001` and `111`:
  $$T_1 = Q_2' Q_1' Q_0 + Q_2 Q_1 Q_0 = (Q_2 \odot Q_1) Q_0$$
* **$T_0$**: 1s at states `000`, `011`, `110`, `101`:
  $$T_0 = Q_2' Q_1' Q_0' + Q_2' Q_1 Q_0 + Q_2 Q_1 Q_0' + Q_2 Q_1' Q_0 = (Q_2 \oplus Q_1 \oplus Q_0)'$$

### Solution 3: Moore Sequence Detector (`1011`)
Define states:
* $S_0$: Reset state (no matching bits). Output $Z = 0$.
* $S_1$: Got '1'. Output $Z = 0$.
* $S_2$: Got '10'. Output $Z = 0$.
* $S_3$: Got '101'. Output $Z = 0$.
* $S_4$: Got '1011' (sequence detected). Output $Z = 1$.

Transitions:
* From $S_0$: If $X=1 \to S_1$; if $X=0 \to S_0$.
* From $S_1$: If $X=0 \to S_2$; if $X=1 \to S_1$.
* From $S_2$: If $X=1 \to S_3$; if $X=0 \to S_0$.
* From $S_3$: If $X=1 \to S_4$; if $X=0 \to S_2$.
* From $S_4$: If $X=1 \to S_1$; if $X=0 \to S_2$ (overlapping recognition).

State encoding: 5 states require 3 flip-flops ($Q_2 Q_1 Q_0$). Unused states ($101, 110, 111$) are treated as don't-cares ($d$) during K-map derivation.
Output equation: $Z = Q_2 Q_1' Q_0'$ (State $S_4 = 100_2$).

