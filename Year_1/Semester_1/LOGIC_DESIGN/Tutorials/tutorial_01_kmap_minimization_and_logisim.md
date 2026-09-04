# Tutorial 01: K-Map Minimization and Digital Circuit Simulation in Logisim

## Context and Grounding
This tutorial provides a hands-on guide to Karnaugh map logic reduction and schematic capture using Logisim-evolution (an educational digital circuit simulator).

---

## 1. Practical Karnaugh Map Reduction Rules

### 1.1 The Grouping Checklist
1. **Identify Isolated 1s**: Any $1$ that has no adjacent neighbors must be grouped as a 1-cell implicant.
2. **Identify Unique Neighbors**: Any $1$ that has only one adjacent $1$ must be paired immediately.
3. **Corner and Edge Wrap-Arounds**:
   - The four outer corners of a 4-variable map ($m_0, m_2, m_8, m_{10}$) form an essential 4-cell group:
     $$m_0 + m_2 + m_8 + m_{10} = B' D'$$
   - The top and bottom rows wrap around ($AB = 00$ and $AB = 10$).
   - The leftmost and rightmost columns wrap around ($CD = 00$ and $CD = 10$).
4. **Redundant Groups**: After all essential prime implicants are marked, remove any group whose $1$s are already entirely covered by other selected groups.

---

## 2. Getting Started with Logisim-evolution

Download and launch Logisim-evolution via Java:
```bash
java -jar logisim-evolution.jar
```

### 2.1 Workspace and Core Tooling
* **Selection Tool (Arrow)**: Move, select, and delete wires and components.
* **Poke Tool (Finger)**: Click on input pins to toggle binary states ($0 \leftrightarrow 1$) in real time.
* **Wiring Tool**: Click and drag from any component stub to route connection nets. Green wires indicate active logic $1$; dark green indicates logic $0$; blue indicates high impedance ($Z$); red indicates an electrical contention error.

---

## 3. Step-by-Step Circuit Build: 1-Bit Full Adder Subcircuit

### 3.1 Creating the Subcircuit
1. In the project explorer pane, right-click the project root and select **Add Circuit...**. Name it `FullAdder`.
2. Place three **Input Pins**:
   - Label: `A`, Bit Width: `1`
   - Label: `B`, Bit Width: `1`
   - Label: `Cin`, Bit Width: `1`
3. Place two **Output Pins**:
   - Label: `Sum`, Bit Width: `1`
   - Label: `Cout`, Bit Width: `1`
4. Place logic gates from the **Gates** library:
   - Two 2-input **XOR** gates for Sum logic:
     $$\text{Sum} = A \oplus B \oplus C_{\text{in}}$$
   - Two 2-input **AND** gates and one 2-input **OR** gate for Carry logic:
     $$C_{\text{out}} = (A \cdot B) + ((A \oplus B) \cdot C_{\text{in}})$$
5. Route wires connecting the inputs to gates and gate outputs to the output pins.

### 3.2 Testing and Verification
1. Switch to the **Poke Tool** (hand icon).
2. Toggle input pins and verify all 8 input combinations against the standard Full Adder truth table:

| $A$ | $B$ | $C_{\text{in}}$ | $\text{Sum}$ | $C_{\text{out}}$ |
|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 | 0 |
| 0 | 1 | 0 | 1 | 0 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 0 | 1 |
| 1 | 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 | 1 |

---

## 4. Combinational Analysis Tool in Logisim
Logisim features a built-in automated synthesis tool:
1. Navigate to **Window $\to$ Combinational Analysis**.
2. Under **Inputs**, define `A, B, C`.
3. Under **Outputs**, define `F`.
4. Under **Table**, enter the desired truth table outputs ($0, 1, X$).
5. View the **Expression** and **Minimized** tabs to inspect the automatically generated K-map and minimal SOP/POS equations.
6. Click **Build Circuit** to automatically generate the schematic on the canvas.

