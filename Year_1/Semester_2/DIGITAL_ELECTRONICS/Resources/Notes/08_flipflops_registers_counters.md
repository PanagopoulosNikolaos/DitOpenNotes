# 8. Flip-Flops, Registers & Counters

This section transitions from combinational to sequential circuits. Flip-flops constitute the basic building blocks from which registers, counters, and more complex sequential units are constructed. The difference between latch (level-triggered) and flip-flop (edge-triggered) is fundamental.

---

## 1. Latches

### 1.1 SR Latch (NOR)

Two NOR gates cross-coupled:

| $S$ | $R$ | $Q$ | $\bar{Q}$ | State |
|:---:|:---:|:---:|:---------:|:---|
| 0 | 0 | $Q_{prev}$ | $\bar{Q}_{prev}$ | Hold |
| 1 | 0 | 1 | 0 | Set |
| 0 | 1 | 0 | 1 | Reset |
| 1 | 1 | X | X | Forbidden |

### 1.2 SR Latch with NAND

Similarly, but with NAND: input 0 is active (active-low):
- $\bar{S}=0, \bar{R}=1$: Set
- $\bar{S}=1, \bar{R}=0$: Reset
- $\bar{S}=1, \bar{R}=1$: Hold
- $\bar{S}=0, \bar{R}=0$: Forbidden

### 1.3 D Latch (Level-Triggered)

Solves the forbidden state problem: $D = S$, $\bar{D} = R$:

| $EN$ | $D$ | $Q$ |
|:---:|:---:|:---:|
| 0 | X | $Q_{prev}$ |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

The output follows input $D$ as long as $EN = 1$. This leads to transparency problems.

> **[Key Insight]** The forbidden state in SR latch ($S=R=1$) can cause metastability — the circuit can "hang" between 0 and 1 for an indefinite time.

---

## 2. Flip-Flops (Edge-Triggered)

### 2.1 SR Flip-Flop

Same as SR latch, but triggered only on the clock edge (rising/falling).

### 2.2 D Flip-Flop

$$
Q(t+1) = D
$$

The value of $D$ at the clock edge is stored in $Q$. This FF is used in registers.

**Truth table:**

| $CLK$ | $D$ | $Q(t+1)$ |
|:---:|:---:|:--------:|
| Rising | 0 | 0 |
| Rising | 1 | 1 |
| Falling | X | $Q(t)$ |
| Steady | X | $Q(t)$ |

### 2.3 JK Flip-Flop

More general: $J=K=1$ corresponds to toggle.

$$
Q(t+1) = J\bar{Q}(t) + \bar{K}Q(t)
$$

| $J$ | $K$ | $Q(t+1)$ |
|:---:|:---:|:--------:|
| 0 | 0 | $Q(t)$ (Hold) |
| 0 | 1 | 0 (Reset) |
| 1 | 0 | 1 (Set) |
| 1 | 1 | $\bar{Q}(t)$ (Toggle) |

### 2.4 T Flip-Flop

$$
Q(t+1) = T \oplus Q(t)
$$

- $T = 0$: Hold
- $T = 1$: Toggle

### 2.5 Master-Slave JK FF

Combination of two JK FFs (master and slave) to avoid race-around condition:
- The master is read on the rising edge
- The slave is activated on the falling edge

### 2.6 Asynchronous vs Synchronous

**Asynchronous (Preset, Clear):** Act directly, outside the clock.
- `Preset (PR)`: Drives $Q \to 1$
- `Clear (CLR)`: Drives $Q \to 0$

**Synchronous:** Act only at the clock edge.

---

## 3. Flip-Flop Conversions

### 3.1 Excitation Tables

**D Flip-Flop:**

| $Q(t)$ | $Q(t+1)$ | $D$ |
|:---:|:--------:|:---:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

**JK Flip-Flop:**

| $Q(t)$ | $Q(t+1)$ | $J$ | $K$ |
|:---:|:--------:|:---:|:---:|
| 0 | 0 | 0 | X |
| 0 | 1 | 1 | X |
| 1 | 0 | X | 1 |
| 1 | 1 | X | 0 |

**T Flip-Flop:**

| $Q(t)$ | $Q(t+1)$ | $T$ |
|:---:|:--------:|:---:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

### 3.2 Conversions Between Types

**D → JK:** $D = J\bar{Q} + \bar{K}Q$
**JK → D:** $J = D$, $K = \bar{D}$ (simple connection)
**T → D:** $D = T \oplus Q$

---

## 4. Registers

### 4.1 4-Bit D FF Register (Parallel Load)

Four D flip-flops with a common clock. Each FF stores one bit:
- Parallel load: all $D_i$ are stored simultaneously
- Parallel read: all $Q_i$ are available simultaneously

### 4.2 Shift Registers

**SISO (Serial-In, Serial-Out):**
- Input of one bit each clock cycle
- Bits shift each cycle
- Output after n cycles

**SIPO (Serial-In, Parallel-Out):**
- Serial input, parallel read

**PISO (Parallel-In, Serial-Out):**
- Parallel load, serial output

**PIPO (Parallel-In, Parallel-Out):**
- Parallel load, parallel read (buffer)

### 4.3 Universal Shift Register

Can perform: hold, shift right, shift left, parallel load.

**Operation with 2-bit selector:**
- 00: Hold
- 01: Shift right
- 10: Shift left
- 11: Parallel load

### 4.4 Applications

- **Buffer:** PIPO register as a transitional buffer
- **Serial communication:** SISO/SIPO/PISO for sending/receiving data

---

## 5. Counters

### 5.1 Asynchronous (Ripple) Counter

Each flip-flop is driven by the output of the previous one. The counter "ripples" from LSB to MSB.

- 4-bit binary up counter: $0000 \to 0001 \to 0010 \to \dots \to 1111 \to 0000$
- Delay: cumulative (ripple)

### 5.2 Synchronous Counter

All flip-flops are triggered by the same clock. The control logic ensures the correct sequence.

### 5.3 Mod-N Counter

Counter that resets after N states (0 to N-1).

**mod-6 counter:** Counts $000 \to 001 \to 010 \to 011 \to 100 \to 101 \to 000$
- Requires 3 FFs
- Reset: when it counts 6 ($110$), resets to 0

### 5.4 Ring Counter and Johnson Counter

**Ring Counter:** n FFs in a chain, with the last FF feeding the first (circular shift). Active bit "passes" from position to position.

**Johnson Counter:** n FFs with the $\bar{Q}$ of the last feeding the $D$ of the first. Produces $2n$ unique states.

### 5.5 Up/Down Counter

Counter that can count either up or down, depending on a control signal `UP/DOWN`.

---

## Solved Exercises

### Exercise 1: SR Latch

**Problem:** Present the operation of an SR latch with NOR for alternating inputs.

**Solution:**

$S=1, R=0$: $Q=1$ (Set)
$S=0, R=0$: $Q=1$ (Hold)
$S=0, R=1$: $Q=0$ (Reset)
$S=1, R=1$: Forbidden (avoidable)

### Exercise 2: JK Flip-Flop Toggle

**Problem:** Prove that with $J=K=1$, the JK FF toggles on each edge.

**Solution:**
$Q(t+1) = J\bar{Q}(t) + \bar{K}Q(t) = 1 \cdot \bar{Q}(t) + 0 \cdot Q(t) = \bar{Q}(t)$

### Exercise 3: 4-Bit Shift Register

**Problem:** A 4-bit SIPO shift register receives the sequence $1011$ (LSB first). Present the state after 4 cycles.

**Solution:**

| Cycle | Input | Q3 | Q2 | Q1 | Q0 |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 1 | 0 | 0 | 0 | 1 |
| 2 | 1 | 0 | 0 | 1 | 1 |
| 3 | 0 | 0 | 1 | 1 | 1 |
| 4 | 1 | 1 | 1 | 1 | 0 |

### Exercise 4: mod-5 Counter

**Problem:** Design a mod-5 binary up counter with D flip-flops.

**Solution:**

Requires 3 FFs ($Q_2 Q_1 Q_0$). Counts: $000 \to 001 \to 010 \to 011 \to 100 \to 000$.

Reset state: $101$ (5) → $000$ (0).

### Exercise 5: D→JK Conversion

**Problem:** Implement a JK FF using a D FF.

**Solution:**
$$
D = J\bar{Q} + \bar{K}Q
$$

### Exercise 6: Ring Counter vs Johnson

**Problem:** Compare 4-bit ring and Johnson counters.

**Solution:**

| Counter | States | Count |
|:---|:---:|:---:|
| Ring | $1000 \to 0100 \to 0010 \to 0001 \to 1000$ | 4 |
| Johnson | $0000 \to 1000 \to 1100 \to 1110 \to 1111 \to 0111 \to 0011 \to 0001 \to 0000$ | 8 |

### Exercise 7: Parallel Load Register

**Problem:** Design a 4-bit register with parallel load and enable.

**Solution:**

4 D-FFs with MUX at each input:
- $EN = 1$: $D_i = \text{input}_i$ (parallel load)
- $EN = 0$: $D_i = Q_i$ (hold)

### Exercise 8: Up/Down mod-8 Counter

**Problem:** Design a mod-8 up/down counter with JK flip-flops.

**Solution:**

3 JK-FFs with common clock. Control signal $M$:
- $M = 1$: Up (normal binary)
- $M = 0$: Down (reverse binary)

$$
J_0 = K_0 = 1 \text{ (always toggle)}
$$
$$
J_1 = K_1 = Q_0 \oplus \bar{M}
$$
$$
J_2 = K_2 = Q_0 \cdot Q_1 \oplus \bar{M}
$$

---

## Exam Tip: Choosing a Flip-Flop

In FSM design problems:
- **D FF:** Simplest design (next state equations = output equations)
- **JK FF:** More controlled but more complex. Avoids invalid states
- **T FF:** Ideal for counters (toggle behavior)

Remember: excitation tables are the key. If you know $Q(t)$ and $Q(t+1)$, you can always find the required input value.
