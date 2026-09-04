# Assignment 01: DC Network Analysis and Thevenin Equivalents

## Objective
Apply nodal analysis, mesh analysis, and Thevenin's theorem to systematically solve a multi-source, multi-loop planar DC circuit. Validate analytical derivations against numerical calculations and SPICE simulation netlists.

---

## Technical Specifications

### 1. Circuit Topology
Analyze the two-mesh DC network with terminals $A$ and $B$:
* Independent voltage source $V_1 = 24\text{ V}$.
* Resistor $R_1 = 4\,\Omega$ in series with $V_1$.
* Resistor $R_2 = 12\,\Omega$ connected in parallel across the central branch.
* Independent voltage source $V_2 = 6\text{ V}$ in series with resistor $R_3 = 2\,\Omega$ in the second branch.
* Variable load resistor $R_L$ connected across output terminals $A-B$.

```text
       ┌─────[ R1: 4Ω ]────┬────[ R3: 2Ω ]────(+) V2: 6V ───┐
       │                   │                                 │
     (+)                   │                                 │
    V1: 24V              [ R2: 12Ω ]                       Terminal A
     (-)                   │                                 │
       │                   │                               [ R_L ]
       └───────────────────┴─────────────────────────────────┤
                                                           Terminal B
```

### 2. Analytical Problems
1. **Mesh-Current Formulation**: Set up matrix equation $[R][I] = [V]$ for mesh currents $I_1$ and $I_2$.
2. **Nodal Formulation**: Determine node voltage $V_1$ at the central node using KCL.
3. **Thevenin Equivalent ($V_{\text{th}}, R_{\text{th}}$)**:
   - Calculate open-circuit voltage $V_{AB,\text{oc}}$.
   - Deactivate sources and compute equivalent resistance $R_{\text{th}}$ across terminals $A-B$.
4. **Norton Equivalent ($I_N, R_N$)**: Determine short-circuit current $I_{AB,\text{sc}}$ and verify $I_N = \frac{V_{\text{th}}}{R_{\text{th}}}$.
5. **Maximum Power Transfer**: Determine value of $R_L$ that absorbs maximum power from terminals $A-B$, and calculate $P_{\text{max}}$.
6. **SPICE Netlist**: Write an NGSPICE netlist to compute operating point voltages and load currents for $R_L = \{1\,\Omega, R_{\text{th}}, 10\,\Omega\}$.

---

## Deliverables & Constraints
* Formally typeset PDF/Markdown report with complete step-by-step mathematical derivations.
* SPICE netlist file `dc_thevenin.cir` and raw simulation output logs.
* Discussion comparing analytical values with simulated results.

---

## Evaluation Rubric

| Criterion | Evaluation Target | Points |
|:---|:---|:---:|
| Systematic Analysis (Mesh/Nodal) | Accurate equation formulations and matrix inversions | 25 |
| Thevenin & Norton Equivalents | Exact analytical solutions for $V_{\text{th}}$, $R_{\text{th}}$, and $I_N$ | 25 |
| Maximum Power Analysis | Rigorous derivation of optimal load condition and power delivery | 20 |
| SPICE Simulation Validation | Functional netlist syntax and accurate `.op` simulation results | 20 |
| Report Quality & Presentation | Clear schematic representation and mathematical typesetting | 10 |
| **Total** | | **100** |

