# Lecture 03: Sequential Logic and Finite State Machines

## Context and Grounding
This lecture note introduces memory elements, synchronous sequential circuits, timing constraints, and Finite State Machine (FSM) synthesis models. It grounds `Resources/Notes/08_flipflops_registers_counters.md` and `09_sequential_circuits_fsm.md`.

---

## 1. Storage Elements: Latches and Flip-Flops

Unlike combinational circuits whose outputs depend solely on present inputs, sequential circuits maintain an internal state determined by past input histories.

### 1.1 Latch vs. Flip-Flop
* **Latch**: Level-sensitive storage element. Transparent while the clock/enable signal is active.
* **Flip-Flop**: Edge-triggered storage element. Changes state only at a specific transition (rising or falling edge) of the clock signal.

### 1.2 Flip-Flop Characteristic Equations and Excitation Tables
| Type | Characteristic Equation | Excitation ($Q \to Q_{\text{next}}$) |
|---|---|---|
| **D Flip-Flop** | $Q_{\text{next}} = D$ | $D = Q_{\text{next}}$ |
| **T Flip-Flop** | $Q_{\text{next}} = T \oplus Q = T'Q + TQ'$ | $T = Q \oplus Q_{\text{next}}$ |
| **JK Flip-Flop** | $Q_{\text{next}} = J Q' + K' Q$ | $0\to0: J=0, K=X$<br/>$0\to1: J=1, K=X$<br/>$1\to0: J=X, K=1$<br/>$1\to1: J=X, K=0$ |
| **SR Latch/FF** | $Q_{\text{next}} = S + R'Q$ (with $SR=0$) | $0\to0: S=0, R=X$<br/>$0\to1: S=1, R=0$<br/>$1\to0: S=0, R=1$<br/>$1\to1: S=X, R=0$ |

---

## 2. Timing Parameters and Metasynchrony

* **Setup Time ($t_{\text{su}}$)**: Minimum duration data inputs must remain stable *before* the active clock edge.
* **Hold Time ($t_{\text{h}}$)**: Minimum duration data inputs must remain stable *after* the active clock edge.
* **Clock-to-Q Delay ($t_{\text{cq}}$)**: Time required for output $Q$ to stabilize following the clock edge.
* **Maximum Clock Frequency**:
  $$T_{\text{clk}} \ge t_{\text{cq}} + t_{\text{comb\_max}} + t_{\text{su}}$$
  $$f_{\text{max}} = \frac{1}{T_{\text{clk}}}$$

---

## 3. Finite State Machine (FSM) Models

### 3.1 Mealy Machine
Outputs are a function of both the **current state** and the **current inputs**:
$$Z(t) = g(S(t), X(t))$$
* Responds to inputs within the same clock cycle.
* Often requires fewer states than an equivalent Moore model.

### 3.2 Moore Machine
Outputs are a function of the **current state only**:
$$Z(t) = h(S(t))$$
* Outputs change strictly synchronously with clock edges.
* Inherently glitch-free with respect to asynchronous input fluctuations.

### 3.3 Systematic Design Procedure
1. Construct state diagram from functional requirements.
2. Formulate state transition table and output table.
3. Perform state minimization (row matching / implication chart).
4. Select state encoding (binary, Gray, or one-hot).
5. Derive flip-flop excitation equations using K-maps.
6. Synthesize gate-level schematic or VHDL description.

