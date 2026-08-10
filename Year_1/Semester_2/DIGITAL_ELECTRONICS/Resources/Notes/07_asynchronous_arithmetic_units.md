# 7. Adders & Arithmetic Units

Adders constitute the building block of arithmetic units (ALU). Understanding carry propagation is critical for analyzing speed and choosing between ripple carry and carry lookahead architectures.

---

## 1. Half Adder

### 1.1 Definition

Accepts two inputs ($A$, $B$) and produces two outputs: sum ($S$) and carry ($C$).

| $A$ | $B$ | $S$ | $C$ |
|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

$$
S = A \oplus B,\quad C = A \cdot B
$$

---

## 2. Full Adder

### 2.1 Definition

Accepts three inputs ($A$, $B$, $C_{in}$) and produces ($S$, $C_{out}$).

| $A$ | $B$ | $C_{in}$ | $S$ | $C_{out}$ |
|:---:|:---:|:--------:|:---:|:---------:|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 | 0 |
| 0 | 1 | 0 | 1 | 0 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 0 | 1 |
| 1 | 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 | 1 |

$$
S = A \oplus B \oplus C_{in}
$$
$$
C_{out} = AB + BC_{in} + AC_{in}
$$

### 2.2 Implementation with 2 Half Adders

**Structural implementation:**
1. HA1: $S_1 = A \oplus B$, $C_1 = AB$
2. HA2: $S = S_1 \oplus C_{in}$, $C_2 = S_1 \cdot C_{in}$
3. $C_{out} = C_1 + C_2$

### 2.3 VHDL Modeling

**Behavioral:**
```vhdl
S <= A XOR B XOR Cin;
Cout <= (A AND B) OR (A AND Cin) OR (B AND Cin);
```

**Dataflow:**
```vhdl
S <= A XOR B XOR Cin;
Cout <= (A AND B) OR ((A XOR B) AND Cin);
```

**Structural:**
```vhdl
HA1: half_adder port map (A => A, B => B, S => S1, C => C1);
HA2: half_adder port map (A => S1, B => Cin, S => S, C => C2);
Cout <= C1 OR C2;
```

---

## 3. Ripple Carry Adder

### 3.1 Architecture

n Full Adders connected in cascade: the $C_{out}$ of each FA is connected to the $C_{in}$ of the next.

### 3.2 Delay

The delay time arises from the cascade propagation of the carry:

$$
T_{total} = n \cdot T_{carry}
$$

where $T_{carry}$ is the delay time of one FA for the carry.

For a 32-bit ripple carry adder with $T_{carry} = 1\text{ns}$:
$$
T_{total} = 32 \text{ns}
$$

> **[Key Insight]** The accuracy of ripple carry is complete, but the speed is linearly proportional to the number of bits. This highlights the need for carry lookahead.

---

## 4. Carry Lookahead Adder (CLA)

### 4.1 Generate and Propagate

**Generate:** $G_i = A_i \cdot B_i$ — bit $i$ will generate a carry regardless of the input.

**Propagate:** $P_i = A_i \oplus B_i$ — bit $i$ will propagate a carry if one exists.

### 4.2 Carry Equations

$$
C_i = G_i + P_i \cdot C_{i-1}
$$

Expansion:
$$
C_0 = G_0 + P_0 \cdot C_{-1}
$$
$$
C_1 = G_1 + P_1 \cdot G_0 + P_1 \cdot P_0 \cdot C_{-1}
$$
$$
C_2 = G_2 + P_2 \cdot G_1 + P_2 \cdot P_1 \cdot G_0 + P_2 \cdot P_1 \cdot P_0 \cdot C_{-1}
$$

### 4.3 Speed vs Complexity

| Characteristic | Ripple Carry | CLA |
|:---|:---:|:---:|
| Delay | $O(n)$ | $O(\log n)$ |
| Number of gates | $O(n)$ | $O(n \log n)$ |
| Carry computation | Cascaded | Parallel |

> **[Exam Tip]** In an exam problem, if you are asked to compute the delay time, check if ripple carry (simple but slow) or CLA (complex but fast) is requested.

---

## 5. Subtractor

### 5.1 Using 2's Complement and Adder

The subtraction $A - B$ is implemented as $A + \bar{B} + 1$.

**Circuit:**
1. Invert all bits of $B$ (NOT gates)
2. Add with full adder, with $C_{in} = 1$

$$
D = A + (2's \text{ complement of } B)
$$

### 5.2 Integrated Adder-Subtractor

Using a control `M`:
- $M = 0$: addition
- $M = 1$: subtraction

$$
\text{Output} = A + (B \oplus M) + M
$$

---

## 6. ALU (Arithmetic Logic Unit)

### 6.1 Combining Operations

The ALU combines arithmetic (addition, subtraction) and logical (AND, OR, XOR, NOT) operations into one unit.

### 6.2 Operation Selection with MUX

**Control Signals (ALUOp):**

| ALUOp | Operation |
|:-----:|:---|
| 00 | AND |
| 01 | OR |
| 10 | XOR |
| 11 | ADD/SUB |

---

## Solved Exercises

### Exercise 1: Half Adder Truth Table

**Problem:** Prove that $S = A \oplus B$ and $C = AB$ for the half adder.

**Solution:**

From the truth table:
- $S = 1$ when $A \neq B$, i.e., $S = A \oplus B$
- $C = 1$ only when $A = B = 1$, i.e., $C = AB$

### Exercise 2: Full Adder from Half Adders

**Problem:** Prove that $C_{out} = AB + (A \oplus B)C_{in}$.

**Solution:**
$$
C_{out} = C_1 + C_2 = AB + S_1 \cdot C_{in} = AB + (A \oplus B)C_{in}
$$

### Exercise 3: 4-Bit Ripple Carry Adder

**Problem:** Calculate the sum $A = 1011$ and $B = 0110$ in a 4-bit ripple carry adder.

**Solution:**
```
  1 0 0 0    (carries C4, C3, C2, C1)
  1 0 1 1  (11)
+ 0 1 1 0  (6)
--------
1 0 0 0 1  (17)
```

$C_{-1} = 0$:
- $C_0 = 0$: $1+0+0=1$, $S_0=1$, $C_1=0$
- $C_1 = 0$: $1+1+0=0$, $S_1=0$, $C_2=1$
- $C_2 = 1$: $0+1+1=0$, $S_2=0$, $C_3=1$
- $C_3 = 1$: $1+0+1=0$, $S_3=0$, $C_4=1$
- $S = 0001$ (with $C_4=1$)

### Exercise 4: CLA Carry Calculations

**Problem:** For $A = 1011$, $B = 0110$ calculate the Generate/Propagate values and the carries with CLA.

**Solution:**

| $i$ | $A_i$ | $B_i$ | $G_i = A_iB_i$ | $P_i = A_i \oplus B_i$ |
|:---:|:---:|:---:|:---:|:---:|
| 0 | 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 | 0 |
| 2 | 0 | 1 | 0 | 1 |
| 3 | 1 | 0 | 0 | 1 |

$C_{-1} = 0$:
$$
C_0 = G_0 + P_0 \cdot C_{-1} = 0 + 1 \cdot 0 = 0
$$
$$
C_1 = G_1 + P_1 \cdot G_0 + P_1 \cdot P_0 \cdot C_{-1} = 1 + 0 + 0 = 1
$$
$$
C_2 = G_2 + P_2 \cdot G_1 + P_2 \cdot P_1 \cdot G_0 + P_2 \cdot P_1 \cdot P_0 \cdot C_{-1} = 0 + 1 \cdot 1 + 0 + 0 = 1
$$
$$
C_3 = G_3 + P_3 \cdot G_2 + P_3 \cdot P_2 \cdot G_1 + P_3 \cdot P_2 \cdot P_1 \cdot G_0 + \dots = 0 + 0 + 1 \cdot 0 + \dots = 0
$$

### Exercise 5: Subtractor

**Problem:** Calculate $13 - 7$ in 4-bit with 2's complement.

**Solution:**
1. $A = 13 = 1101$
2. $B = 7 = 0111$
3. $\bar{B} = 1000$, $2's\text{ complement} = 1001$
4. $A + (-B) = 1101 + 1001 = 10110 \to 0110$ (carry discarded)
5. $S = 0110 = 6$

### Exercise 6: 8-to-1 MUX ALU

**Problem:** Design an ALU that performs 4 operations using a 2-to-4 decoder and MUX.

**Solution:**
1. 2-to-4 decoder creates enable signals for 4 operations
2. Each operation (AND, OR, XOR, ADD) has its dedicated circuit
3. 4-to-1 MUX selects the result

### Exercise 7: Integrated Adder-Subtractor

**Problem:** Design a 4-bit adder/subtractor with M = control.

**Solution:**

4 XOR gates: $B_i \oplus M$ for each bit $B_i$
4 FA: $A_i + (B_i \oplus M) + C_{i-1}$

- $M = 0$: $A + B + 0$ (addition)
- $M = 1$: $A + \bar{B} + 1$ (subtraction)

### Exercise 8: Comparing Adders

**Problem:** Compare the execution time of a 16-bit ripple carry vs CLA adder with $t_{gate} = 1\text{ns}$.

**Solution:**

**Ripple Carry:**
- Carry delay per bit: 2 gate delays (AND + OR)
- Total delay: $16 \times 2 = 32$ gate delays

**CLA:**
- Carry compute: 2 gate delays (parallel)
- Sum compute: 2 gate delays
- Total delay: 4 gate delays

Difference: $32/4 = 8$ times faster with CLA.

---

## Exam Tip: Critical Path

In the ripple carry adder, the critical path is from $C_{-1}$ (LSB) to $C_{n-1}$ (MSB carry) and then to $S_{n-1}$ (MSB sum). If asked to improve speed, propose CLA or switching to smaller chunks (block CLA).
