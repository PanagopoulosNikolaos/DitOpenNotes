# 6. Decoders, Encoders & Multiplexers

Decoders, encoders, and multiplexers are important combinational units that are widely used in digital systems. They are used in data routing, source selection, and the implementation of logical functions.

---

## 1. Decoders

### 1.1 n-to-2ⁿ Decoder

Encodes n-bit input into $2^n$ outputs. Each input combination activates exactly one output.

**2-to-4 Decoder:**

| $A_1$ | $A_0$ | $Y_0$ | $Y_1$ | $Y_2$ | $Y_3$ |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| 0 | 0 | 1 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | 0 | 0 |
| 1 | 0 | 0 | 0 | 1 | 0 |
| 1 | 1 | 0 | 0 | 0 | 1 |

**Boolean expressions:**
$$
Y_0 = \bar{A_1}\bar{A_0},\; Y_1 = \bar{A_1}A_0,\; Y_2 = A_1\bar{A_0},\; Y_3 = A_1A_0
$$

### 1.2 Implementing Logical Functions with Decoder + OR

Every SOP can be implemented with n-to-2ⁿ decoder + OR gate:
1. The outputs corresponding to the minterms where $F = 1$ are activated
2. All these outputs are connected to one OR gate

### 1.3 Enable Input and Cascading

**Enable (EN):** Allows or disables the decoder:
$$
Y_i = \bar{A_1}\bar{A_0} \cdot EN \text{ (for } Y_0\text{)}
$$

**Cascading:** Connecting two 2-to-4 decoders with a NOT gate on the third input $A_2$:
- $A_2 = 0$: activates the first decoder
- $A_2 = 1$: activates the second decoder
- Result: 3-to-8 decoder

---

## 2. Encoders

### 2.1 2ⁿ-to-n Encoder

The reverse operation of a decoder: from $2^n$ inputs produces n-bit code. Only one output is active at a time.

**8-to-3 Encoder:**

| $Y_7$ | $Y_6$ | $Y_5$ | $Y_4$ | $Y_3$ | $Y_2$ | $Y_1$ | $Y_0$ | $A_2$ | $A_1$ | $A_0$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 |
| 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |
| 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 |

### 2.2 Priority Encoder

If multiple inputs are active simultaneously, the Priority encoder encodes only the highest priority (highest bit index).

**Priority:** Input $Y_i$ has higher priority than $Y_j$ if $i > j$.

### 2.3 Applications

- **Interrupt handling:** The priority encoder encodes which interrupt is active
- **DMA arbitration:** Selection among multiple requesters

---

## 3. Multiplexers (MUX)

### 3.1 2ⁿ-to-1 MUX

Selects one of $2^n$ inputs and routes it to the output, based on n-bit selector.

$$
Y = \sum_{i=0}^{2^n-1} S_i \cdot I_i
$$

where $S_i$ is the minterm of the selector.

**2-to-1 MUX:**
$$
Y = \bar{S} \cdot I_0 + S \cdot I_1
$$

**4-to-1 MUX:**
$$
Y = \bar{S_1}\bar{S_0} \cdot I_0 + \bar{S_1}S_0 \cdot I_1 + S_1\bar{S_0} \cdot I_2 + S_1S_0 \cdot I_3
$$

### 3.2 Implementing Any Function with MUX

Every n-variable Boolean function can be implemented with a $2^{n-1}$-to-1 MUX:
1. Set $n-1$ variables to the selectors
2. Each input of the MUX depends on the remaining variable (0, 1, or the same variable)

### 3.3 Cascading MUX for n Variables

**4-to-1 MUX for 3 variables:**
- 2 selectors: $S_1 = A$, $S_0 = B$
- Inputs: $I_0 = 0$, $I_1 = \bar{C}$, $I_2 = C$, $I_3 = 1$

**8-to-1 MUX for 4 variables:**
- 3 selectors: $S_2 = A$, $S_1 = B$, $S_0 = C$
- Inputs: $I_0 = 0$, $I_1 = D$, $I_2 = \bar{D}$, $I_3 = D$, $I_4 = 0$, $I_5 = 1$, $I_6 = 1$, $I_7 = 0$

### 3.4 Demultiplexer (DEMUX)

Reverse MUX: from one input, selects which output will be fed.

**1-to-4 DEMUX:**
$$
Y_0 = \bar{S_1}\bar{S_0} \cdot I,\; Y_1 = \bar{S_1}S_0 \cdot I,\; Y_2 = S_1\bar{S_0} \cdot I,\; Y_3 = S_1S_0 \cdot I
$$

---

## Solved Exercises

### Exercise 1: 3-to-8 Decoder

**Problem:** Construct a 3-to-8 decoder using AND gates.

**Solution:**

8 AND gates, each with 3 inputs (normal/inverted):
$$
Y_0 = \bar{A_2}\bar{A_1}\bar{A_0},\; Y_1 = \bar{A_2}\bar{A_1}A_0,\; \dots,\; Y_7 = A_2A_1A_0
$$

### Exercise 2: Implementation with Decoder + OR

**Problem:** Implement $F(A,B,C) = \sum m(0,3,5,6)$ using a 3-to-8 decoder.

**Solution:**
$$
F = Y_0 + Y_3 + Y_5 + Y_6
$$

### Exercise 3: 4-to-1 MUX

**Problem:** Derive the logic expression for a 4-to-1 MUX with $S_1S_0 = AB$ and $I_0=0, I_1=\bar{C}, I_2=C, I_3=1$.

**Solution:**
$$
Y = \bar{A}\bar{B}(0) + \bar{A}B(\bar{C}) + A\bar{B}(C) + AB(1)
$$
$$
Y = \bar{A}B\bar{C} + A\bar{B}C + AB = \bar{A}B\bar{C} + A(B + \bar{B}C) = \bar{A}B\bar{C} + A(B + C)
$$
$$
Y = \bar{A}B\bar{C} + AB + AC
$$

### Exercise 4: Priority Encoder

**Problem:** Given a 4-to-2 Priority encoder with inputs $D_3 D_2 D_1 D_0 = 0101$. Find the outputs.

**Solution:**

Input $D_3 = 0$, $D_2 = 1$. The highest active position is $D_2$.

Outputs: $Y_1 Y_0 = 10$ (binary of 2), $V = 1$ (valid).

### Exercise 5: 8-to-1 MUX for 4 Variables

**Problem:** Implement $F(A,B,C,D) = \sum m(1,2,5,9,10,12)$ using an 8-to-1 MUX.

**Solution:**

$S_2 = A$, $S_1 = B$, $S_0 = C$:

| $ABC$ | $I_i$ | Value |
|:---:|:---:|:---:|
| 000 | $I_0$ | $D$ (m0→0, m1→1) |
| 001 | $I_1$ | $\bar{D}$ (m2→1, m3→0) |
| 010 | $I_2$ | $D$ (m4→0, m5→1) |
| 011 | $I_3$ | 0 |
| 100 | $I_4$ | $\bar{D}$ (m8→0, m9→1) |
| 101 | $I_5$ | $\bar{D}$ (m10→1, m11→0) |
| 110 | $I_6$ | $\bar{D}$ (m12→1, m13→0) |
| 111 | $I_7$ | 0 |

### Exercise 6: DEMUX 1-to-4

**Problem:** Derive the expression for 1-to-4 DEMUX.

**Solution:**
$$
Y_0 = \bar{S_1}\bar{S_0} \cdot I,\quad Y_1 = \bar{S_1}S_0 \cdot I,\quad Y_2 = S_1\bar{S_0} \cdot I,\quad Y_3 = S_1S_0 \cdot I
$$

### Exercise 7: Cascading Decoders

**Problem:** Construct a 4-to-16 decoder from two 3-to-8 decoders.

**Solution:**

1. Use $A_3$ as selector
2. $A_3 = 0$: activates the first decoder ($Y_0$-$Y_7$)
3. $A_3 = 1$: activates the second ($Y_8$-$Y_{15}$)
4. Enable: the first decoder has EN, the second has EN + NOT($A_3$)

### Exercise 8: MUX as Universal Gate

**Problem:** Implement AND, OR, XOR, NAND using a 2-to-1 MUX.

**Solution:**

$Y = \bar{S} \cdot I_0 + S \cdot I_1$:

| Gate | $S$ | $I_0$ | $I_1$ | Explanation |
|:---|:---:|:---:|:---:|:---|
| AND | $B$ | 0 | $A$ | $Y = \bar{B}(0) + BA = AB$ |
| OR | $B$ | $A$ | 1 | $Y = \bar{B}A + B(1) = A + B$ |
| XOR | $B$ | $A$ | $\bar{A}$ | $Y = \bar{B}A + B\bar{A} = A \oplus B$ |
| NAND | $B$ | 1 | $\bar{A}$ | $Y = \bar{B}(1) + B\bar{A} = \overline{AB}$ |

---

## Exam Tip: Choosing the Right Tool

In exam problems, if asked to implement a Boolean function with:
- **Decoder:** Use n-to-2ⁿ decoder + OR (SOP). If there are many minterms, this is faster.
- **MUX:** Use $2^{n-1}$-to-1 MUX. Each input can be 0, 1, or a variable — very flexible.
- **Both:** If the function is in minterm form, the decoder is more natural. If there are don't cares, the MUX can exploit them more easily.
