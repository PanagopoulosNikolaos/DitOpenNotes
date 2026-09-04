# Practice Exam 01: Digital Electronics and Switching Circuits

## Course Context and Information

* **Course**: Digital Electronics (Course Code: 205)
* **Academic Term**: Year 1, Semester 2
* **Duration**: 3 Hours
* **Total Value**: 100 Points
* **Format**: Closed Book. Scientific calculators allowed.

---

## Part 1: Combinational Logic Synthesis and Hazard Analysis (25 Points)

### Question 1.1: Quine-McCluskey Minimization (15 Points)
Given the incomplete Boolean function with don't-care conditions:
$$F(A, B, C, D) = \sum m(0, 2, 5, 7, 8, 10, 15) + \sum d(13, 14)$$

1. Construct the tabular grouping of minterms by number of ones.
2. Determine all Prime Implicants (PIs) through systematic pair matching.
3. Formulate the Prime Implicant Table and identify all Essential Prime Implicants (EPIs).
4. State the minimal Sum-of-Products (SOP) expression.

### Question 1.2: Static Hazards in Combinational Networks (10 Points)
Consider the function implemented as:
$$F = A B' + B C$$

1. Plot the K-map of $F$ and identify the transition between adjacent minterms that produces a potential static-1 hazard.
2. Explain the physical mechanism causing the hazard in terms of gate propagation delay ($t_{pd}$).
3. Modify the expression by adding a consensus term to eliminate the hazard without altering the Boolean transfer function.

---

## Part 2: Synchronous Sequential Systems and FSM Synthesis (35 Points)

### Question 2.1: Sequence Detector Design (20 Points)
Design a synchronous sequential circuit (Finite State Machine) that detects the overlapping bit pattern `1011` in a serial input stream $X$. When the pattern is detected, the output $Z$ must assert $1$ for exactly one clock period; otherwise, $Z = 0$.

1. Draw the complete Moore state diagram, labeling all states, transitions, and output values.
2. Perform state reduction using an implication table if redundant states exist.
3. Choose a state assignment using binary encoding with $D$ flip-flops ($Q_1, Q_0$ or higher as required).
4. Derive the minimal excitation equations for each $D$ input ($D_i$) and the output equation $Z$ using Karnaugh maps.
5. Draw the complete logic gate and flip-flop schematic.

### Question 2.2: Mealy vs. Moore Timing Mechanics (15 Points)
Compare the Mealy and Moore architectural models:
1. Formulate the mathematical dependency equations for the next-state vector $S_{n+1}$ and the output vector $Z_n$ in both models.
2. Explain why Mealy outputs may experience asynchronous glitching upon input transitions, whereas Moore outputs are strictly synchronous with clock edges.
3. Given identical state counts, contrast the number of states typically required by a Mealy machine versus a Moore machine for sequence detection.

---

## Part 3: Registers, Counters, and Timing Constraints (20 Points)

### Question 3.1: Synchronous Modulo-6 Up/Down Counter (12 Points)
Synthesize a synchronous modulo-6 counter using $JK$ flip-flops with an external direction control input $M$:
* When $M = 0$, the counter cycles up: $0 \to 1 \to 2 \to 3 \to 4 \to 5 \to 0$.
* When $M = 1$, the counter cycles down: $5 \to 4 \to 3 \to 2 \to 1 \to 0 \to 5$.
* Unused states ($6$ and $7$) must safely transition to state $0$ on the next clock edge.

1. Tabulate the state transition and $JK$ excitation table.
2. Derive the minimal SOP expressions for inputs $J_2, K_2, J_1, K_1, J_0, K_0$.

### Question 3.2: Setup and Hold Time Violations (8 Points)
An edge-triggered $D$ flip-flop has the following parameters:
* Clock-to-Q propagation delay: $t_{cq} = 1.2\text{ ns}$
* Setup time: $t_{su} = 0.8\text{ ns}$
* Hold time: $t_{hold} = 0.4\text{ ns}$
* Combinational logic path delay between flip-flops: $2.5\text{ ns} \le t_{comb} \le 6.0\text{ ns}$
* Clock skew between stages: $t_{skew} = 0.3\text{ ns}$

1. Calculate the maximum operating clock frequency ($f_{\max}$) that guarantees zero setup-time violations.
2. Determine whether a hold-time violation occurs under worst-case parameters.

---

## Part 4: Hardware Description Language (VHDL) Modeling (20 Points)

### Question 4.1: Structural and Behavioral Modeling (20 Points)
1. Write an IEEE 1076-compliant VHDL entity and behavioral architecture for an active-high synchronous 4-bit loadable up-counter with synchronous clear:
   * Clock: `clk` (rising edge)
   * Synchronous reset: `rst` (active-high, clears counter to `0000`)
   * Load enable: `load` (active-high, loads parallel input `d_in`)
   * Count enable: `en` (active-high, increments count)
   * Output: `q_out` (4-bit `std_logic_vector`)
2. Write a VHDL testbench process generating a 50 MHz clock signal and demonstrating reset, parallel load, and counting for 4 cycles.

---

## Complete Solutions and Grading Key

### Solution 1.1
1. **Grouping of minterms by number of 1s**:
   * Group 0 (0 ones): $m(0) = 0000$
   * Group 1 (1 one): $m(2) = 0010, m(8) = 1000$
   * Group 2 (2 ones): $m(5) = 0101, m(10) = 1010$
   * Group 3 (3 ones): $m(7) = 0111, d(13) = 1101, d(14) = 1110$
   * Group 4 (4 ones): $m(15) = 1111$

2. **First Reduction (Pair Matching)**:
   * $(0, 2) = 00-0$ ($A' B' D'$)
   * $(0, 8) = -000$ ($B' C' D'$)
   * $(2, 10) = -010$ ($B' C D'$)
   * $(8, 10) = 10-0$ ($A B' D'$)
   * $(5, 7) = 01-1$ ($A' B D$)
   * $(5, 13) = -101$ ($B C' D$)
   * $(7, 15) = -111$ ($B C D$)
   * $(13, 15) = 11-1$ ($A B D$)
   * $(10, 14) = 1-10$ ($A C D'$)
   * $(14, 15) = 111-$ ($A B C$)

3. **Second Reduction (Quads)**:
   * $(0, 2, 8, 10) = -0-0 \implies B' D'$
   * $(5, 7, 13, 15) = -1-1 \implies B D$
   * $(10, 14) \implies A C D'$
   * $(14, 15) \implies A B C$

4. **Prime Implicant Table Evaluation**:
   * $B' D'$ covers $m(0, 2, 8, 10)$ (Essential: only term covering $m(0), m(2), m(8)$)
   * $B D$ covers $m(5, 7)$ (Essential: only term covering $m(5), m(7)$)
   * Remaining minterm $m(15)$ is covered by $B D$
   * All active minterms are covered by $B' D'$ and $B D$

Minimal SOP Expression:
$$F = B' D' + B D$$

---

### Solution 1.2
1. In $F = A B' + B C$, adjacent minterms $A B C$ ($m_7$) and $A B' C$ ($m_5$) both produce $F = 1$. When input $B$ transitions from $1 \to 0$ while $A = C = 1$, term $B C$ switches OFF while term $A B'$ switches ON.
2. Because the inverter generating $B'$ introduces a propagation delay $\Delta t$, there is a transient window during which $B = 0$ and $B' = 0$ simultaneously. During this interval, both product terms evaluate to $0$, causing a brief glitch $1 \to 0 \to 1$.
3. By Consensus Theorem, adding the redundant product term $A C$ bridges the boundary:
$$F_{\text{hazard-free}} = A B' + B C + A C$$
When $A = C = 1$, $A C = 1$ constantly throughout the transition, holding the output HIGH and eliminating the static-1 hazard.

---

### Solution 2.1
1. **Moore State Allocation for `1011`**:
   * $S_0$: Reset / Idle (Output $Z = 0$)
   * $S_1$: Matched `1` (Output $Z = 0$)
   * $S_2$: Matched `10` (Output $Z = 0$)
   * $S_3$: Matched `101` (Output $Z = 0$)
   * $S_4$: Matched `1011` (Output $Z = 1$)

2. **State Transitions**:
   * From $S_0$: on $X=1 \to S_1$, on $X=0 \to S_0$
   * From $S_1$: on $X=1 \to S_1$, on $X=0 \to S_2$
   * From $S_2$: on $X=1 \to S_3$, on $X=0 \to S_0$
   * From $S_3$: on $X=1 \to S_4$, on $X=0 \to S_2$
   * From $S_4$: on $X=1 \to S_1$, on $X=0 \to S_2$ (overlapping detection)

3. **State Assignment**: 5 states require 3 flip-flops ($Q_2, Q_1, Q_0$):
   * $S_0 = 000, S_1 = 001, S_2 = 010, S_3 = 011, S_4 = 100$

4. **Excitation Equations for $D$ Flip-Flops**:
   * $D_2 = Q_1 Q_0 X$
   * $D_1 = Q_0' X' + Q_2 X'$
   * $D_0 = X$
   * Output $Z = Q_2$

---

### Solution 2.2
1. Mathematical formulations:
   * **Mealy Machine**: $S_{n+1} = \delta(S_n, X_n)$, $Z_n = \lambda(S_n, X_n)$ (Output depends on state AND current inputs).
   * **Moore Machine**: $S_{n+1} = \delta(S_n, X_n)$, $Z_n = \lambda(S_n)$ (Output depends SOLELY on present state).
2. Because a Mealy output logic block directly samples the asynchronous primary inputs $X$, any noise or skew on $X$ immediately propagates to output $Z$ within the current clock cycle. In a Moore machine, output transitions can only occur after clock edges update the state registers, buffering the outputs from combinational input jitter.
3. For sequence detection of an $N$-symbol pattern, a Mealy machine requires $N$ states, whereas a Moore machine requires $N+1$ states to decouple the final recognition state from input transitions.

---

### Solution 3.1
For Modulo-6 up/down counting, 3 flip-flops are needed ($Q_2, Q_1, Q_0$):
* Valid states: $000, 001, 010, 011, 100, 101$.
* Using the $JK$ excitation table ($0 \to 0: 0X$, $0 \to 1: 1X$, $1 \to 0: X1$, $1 \to 1: X0$):
  * $J_0 = 1, \quad K_0 = 1$
  * $J_1 = M' Q_0 + M Q_2' Q_0'$
  * $K_1 = M' Q_0 + M Q_0'$
  * $J_2 = M' Q_1 Q_0 + M Q_1' Q_0'$
  * $K_2 = M' Q_0 + M Q_1 Q_0'$

---

### Solution 3.2
1. **Maximum Clock Frequency ($f_{\max}$)**:
   The clock period must satisfy:
   $$T_{clk} \ge t_{cq} + t_{comb,\max} + t_{su} - t_{skew}$$
   $$T_{clk} \ge 1.2 + 6.0 + 0.8 - 0.3 = 7.7\text{ ns}$$
   $$f_{\max} = \frac{1}{7.7\text{ ns}} \approx 129.87\text{ MHz}$$

2. **Hold-Time Verification**:
   The hold constraint requires:
   $$t_{cq} + t_{comb,\min} \ge t_{hold} + t_{skew}$$
   $$1.2\text{ ns} + 2.5\text{ ns} = 3.7\text{ ns}$$
   $$t_{hold} + t_{skew} = 0.4\text{ ns} + 0.3\text{ ns} = 0.7\text{ ns}$$
   Since $3.7\text{ ns} \ge 0.7\text{ ns}$, the margin is $+3.0\text{ ns}$. No hold-time violation occurs.

---

### Solution 4.1

```vhdl
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity counter_4bit is
    port (
        clk   : in  std_logic;
        rst   : in  std_logic;
        load  : in  std_logic;
        en    : in  std_logic;
        d_in  : in  std_logic_vector(3 downto 0);
        q_out : out std_logic_vector(3 downto 0)
    );
end entity counter_4bit;

architecture behavioral of counter_4bit is
    signal count_reg : unsigned(3 downto 0);
begin
    process(clk)
    begin
        if rising_edge(clk) then
            if rst = '1' then
                count_reg <= (others => '0');
            elsif load = '1' then
                count_reg <= unsigned(d_in);
            elsif en = '1' then
                count_reg <= count_reg + 1;
            end if;
        end if;
    end process;

    q_out <= std_logic_vector(count_reg);
end architecture behavioral;
```

---

## Analytical Scoring Breakdown

| Section | Criterion | Points Allocated |
|:---|:---|:---:|
| **Part 1** | Tabular grouping and pairing accuracy | 8 |
| | PI table and EPI deduction | 7 |
| | Hazard identification and consensus term | 10 |
| **Part 2** | Correct Moore state diagram | 10 |
| | State assignment and excitation equations | 10 |
| | Mealy vs. Moore mathematical comparison | 15 |
| **Part 3** | JK excitation table and logic derivation | 12 |
| | Setup and hold timing calculations | 8 |
| **Part 4** | Complete syntax-valid VHDL entity/architecture | 12 |
| | Testbench design and process timing | 8 |
| **Total** | | **100** |

