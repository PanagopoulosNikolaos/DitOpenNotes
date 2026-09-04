# Lecture 01: DC Circuit Analysis and Network Theorems

## Context and Grounding
This lecture note establishes the analytical framework for linear resistive direct-current (DC) circuits. It covers fundamental physical quantities, Ohm's Law, Kirchhoff's Laws, systematic nodal and mesh analysis, and core network theorems (Superposition, Thevenin, Norton, and Maximum Power Transfer).

---

## 1. Electrical Quantities and Physical Laws

### 1.1 Charge, Current, Voltage, and Resistance
* **Electric Current ($I$)**: The rate of transport of electric charge past a point:
  $$I = \frac{dQ}{dt} \quad \text{[Amperes, A]}$$
* **Electric Potential Difference / Voltage ($V$)**: The energy required to move a unit charge between two points:
  $$V = \frac{dW}{dQ} \quad \text{[Volts, V]}$$
* **Ohm's Law**: For an ideal linear resistor, voltage is directly proportional to current:
  $$V = I \cdot R, \quad I = \frac{V}{R}, \quad R = \frac{V}{I}$$
* **Electrical Power ($P$)**: Rate of energy conversion in an element:
  $$P = V \cdot I = I^2 R = \frac{V^2}{R} \quad \text{[Watts, W]}$$

---

## 2. Kirchhoff's Laws

### 2.1 Kirchhoff's Current Law (KCL)
Conservation of charge dictates that the algebraic sum of currents entering any circuit node is identically zero:
$$\sum_{k=1}^{n} I_k = 0 \iff \sum I_{\text{in}} = \sum I_{\text{out}}$$

### 2.2 Kirchhoff's Voltage Law (KVL)
Conservation of energy dictates that the algebraic sum of potential differences around any closed circuit loop is zero:
$$\sum_{k=1}^{m} V_k = 0 \iff \sum V_{\text{rises}} = \sum V_{\text{drops}}$$

---

## 3. Systematic Circuit Analysis Techniques

### 3.1 Nodal Analysis
1. Select one node as the reference ground ($V_{\text{ref}} = 0\text{ V}$).
2. Assign node voltage variables $V_1, V_2, \ldots, V_{n-1}$ to all remaining non-reference nodes.
3. Formulate KCL equations at each non-reference node expressing branch currents in terms of node voltages:
   $$I_{ij} = \frac{V_i - V_j}{R_{ij}}$$
4. Solve the resulting system of $n-1$ linear equations for unknown node voltages.

### 3.2 Mesh Current Analysis
1. Identify all independent planar loops (meshes).
2. Assign clockwise circulating mesh currents $I_1, I_2, \ldots, I_m$ to each mesh.
3. Formulate KVL equations around each mesh expressing branch voltages in terms of mesh currents.
4. Solve the resulting system of $m$ linear equations.

---

## 4. Fundamental Network Theorems

### 4.1 Superposition Principle
In any linear resistive network containing multiple independent sources, the voltage across or current through any element equals the algebraic sum of the voltages or currents produced by each independent source acting alone:
* Deactivate independent voltage sources by replacing them with **short circuits** ($V = 0$).
* Deactivate independent current sources by replacing them with **open circuits** ($I = 0$).
* Retain dependent sources active during all individual source evaluations.

### 4.2 Thevenin's Theorem
Any linear two-terminal DC network can be replaced with an electrically equivalent circuit consisting of a single independent voltage source $V_{\text{th}}$ in series with an equivalent resistance $R_{\text{th}}$:
1. **Open-Circuit Voltage ($V_{\text{th}}$)**: The voltage across terminals $A-B$ when open:
   $$V_{\text{th}} = V_{AB,\text{open}}$$
2. **Thevenin Resistance ($R_{\text{th}}$)**: The resistance seen looking into terminals $A-B$ with all independent sources deactivated:
   $$R_{\text{th}} = \left. \frac{V_{\text{test}}}{I_{\text{test}}} \right|_{\text{sources off}}$$

### 4.3 Norton's Theorem
Any linear two-terminal DC network can be equivalently modeled as an independent current source $I_N$ in parallel with an equivalent resistance $R_N$:
* **Norton Current ($I_N$)**: Short-circuit current between terminals $A-B$:
  $$I_N = I_{AB,\text{short}} = \frac{V_{\text{th}}}{R_{\text{th}}}$$
* **Norton Resistance ($R_N$)**: Identical to Thevenin resistance ($R_N = R_{\text{th}}$).

### 4.4 Maximum Power Transfer Theorem
A linear DC source network delivers maximum real power to a variable load resistor $R_L$ when the load resistance equals the Thevenin resistance of the network:
$$R_L = R_{\text{th}}$$

The maximum power delivered to the load is:
$$P_{\text{max}} = \frac{V_{\text{th}}^2}{4 R_{\text{th}}}$$

