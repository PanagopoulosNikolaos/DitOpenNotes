# Assignment 01: Boolean Algebra Minimization and Combinational Logic Design

## Objective
Design, minimize, and verify multi-output combinational logic networks. Students will synthesize a 4-bit BCD to 7-segment display decoder using Karnaugh map minimization and implement the design in Logisim-evolution.

---

## Technical Specifications

### 1. Problem Description: BCD to 7-Segment Display Decoder
Design a combinational circuit with 4 input lines representing a decimal digit in BCD format ($A, B, C, D$, where $A$ is the MSB and $D$ is the LSB) and 7 output lines ($a, b, c, d, e, f, g$) driving a standard common-cathode 7-segment LED display.

```text
       ── a ──
      │       │
      f       b
      │       │
       ── g ──
      │       │
      e       c
      │       │
       ── d ──
```

### 2. Design Requirements
1. **Truth Table**: Construct a complete 16-row truth table for inputs $0000_2$ to $1111_2$. For invalid BCD input patterns ($1010_2$ to $1111_2$), mark all segment outputs as **don't-cares** ($X$).
2. **Karnaugh Map Minimization**: For each segment $a, b, c, d, e, f, g$:
   - Construct a 4-variable K-map incorporating the don't-care conditions.
   - Circle Prime Implicants and extract minimal Sum of Products (SOP) algebraic expressions.
3. **Universal NAND Implementation**: Convert the minimal SOP equations for segments $a$ and $b$ into equivalent two-level NAND-NAND logic schematics.
4. **Multiplexer Alternative**: Implement the logic function for segment $c$ using an **8-to-1 multiplexer** and minimal external inverter logic.

### 3. Simulation & Schematic Capture
* Build the complete 7-segment decoder in **Logisim-evolution**.
* Create a hierarchical subcircuit `BCD_Decoder` and connect its 7 outputs to a 7-segment display component.
* Verify correct display rendering of digits $0$ through $9$.

---

## Deliverables & Evaluation Rubric

| Criterion | Target Metric | Points |
|:---|:---|:---:|
| Truth Table Formulation | Accurate segment activations and don't-care assignment for states 10-15 | 20 |
| K-Map Minimization | Proper prime implicant grouping and minimal algebraic equations | 35 |
| Universal Gate & MUX Synthesis | Correct two-level NAND conversion and 8-to-1 MUX implementation | 25 |
| Logisim Simulation File | Verified subcircuit rendering all 10 digits without glitching | 20 |
| **Total** | | **100** |

