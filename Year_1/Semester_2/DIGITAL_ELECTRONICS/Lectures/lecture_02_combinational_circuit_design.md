# Lecture 02: Combinational Circuit Design and Karnaugh Maps

## Context and Grounding
This lecture note formalizes the analysis and design procedure for combinational logic networks, algebraic minimization via Karnaugh Maps (K-maps), and standard arithmetic and routing building blocks. It connects directly with `Resources/Notes/04_boolean_simplification.md` through `06_decoders_encoders_multiplexers.md`.

---

## 1. Karnaugh Map (K-Map) Minimization

Karnaugh maps organize truth tables into multidimensional Gray-code indexed grids where adjacent cells differ by exactly one binary variable.

### 1.1 Adjacency and Grouping Rules
1. Groups must contain $2^k$ adjacent cells ($1, 2, 4, 8, 16, \dots$).
2. Groups must be rectangular and can wrap around edges and corners.
3. Groups should be as large as possible to eliminate redundant literals.
4. **Essential Prime Implicant**: A prime implicant containing at least one minterm not covered by any other prime implicant.
5. **Don't Care Conditions ($d$)**: Optional conditions included in groupings if they enlarge the group size, or ignored if they do not.

---

## 2. Arithmetic Combinational Circuits

### 2.1 Half Adder vs. Full Adder
* **Half Adder**: Computes the sum of two single-bit inputs:
  $$S = A \oplus B, \quad C_{out} = A \cdot B$$
* **Full Adder**: Computes the sum of two operand bits and an incoming carry bit:
  $$S = A \oplus B \oplus C_{in}$$
  $$C_{out} = AB + C_{in}(A \oplus B) = AB + BC_{in} + AC_{in}$$

### 2.2 Ripple Carry Adder (RCA)
An $n$-bit ripple carry adder cascades $n$ full adder stages. The total propagation delay is governed by the worst-case carry chain propagation:
$$t_{\text{delay}} = n \times t_{\text{carry\_delay}}$$

---

## 3. Multiplexers and Decoders

### 3.1 Multiplexers (Data Selectors)
An $2^n$-to-1 multiplexer routes one of $2^n$ data inputs ($D_0, \dots, D_{2^n-1}$) to a single output line $Y$ based on $n$ select lines ($S_{n-1}, \dots, S_0$):
$$Y = \sum_{i=0}^{2^n-1} m_i(S) \cdot D_i$$
Any Boolean function of $n$ variables can be implemented directly using a $2^{n-1}$-to-1 MUX by connecting $n-1$ variables to select lines and driving data inputs with $0, 1, X,$ or $X'$.

### 3.2 Decoders
An $n$-to-$2^n$ binary decoder generates all $2^n$ minterms of its $n$ input variables. An active-high decoder with enable input asserts exactly one output line corresponding to the binary value of the inputs:
$$Y_i = m_i \cdot E$$
Connecting selected decoder outputs to an OR gate directly synthesizes arbitrary SOP functions.

