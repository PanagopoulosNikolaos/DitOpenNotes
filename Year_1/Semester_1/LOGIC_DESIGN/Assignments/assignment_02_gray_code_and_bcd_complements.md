# Assignment 02: Gray Code and BCD Complements

## Codes and Conversions

### Exercise Materials

- 1 IC 7404 (Hex Inverters)
- 1 IC 7408 (Quad 2-input AND Gate)
- 1 IC 7432 (Quad 2-input OR Gate)
- 1 IC 7486 (Quad 2-input exclusive OR)

### Part 1: Gray Code to Binary Conversion

Implement a combinational circuit with 4 inputs and 4 outputs that converts a 4-bit Gray code number to its equivalent 4-bit binary number. Construct the Gray to binary conversion table. Design the logic diagram using only XOR gates. Implement and verify correct operation.

### Part 2: Complement with Respect to 9

Design a combinational circuit with 4 inputs representing a decimal digit in BCD code and 4 outputs that produce the complement with respect to 9 of the input digit. With one additional output, provide the ability to detect invalid inputs (non-coded).

---

  

### Part 1: Gray Code to Binary Conversion

To implement a combinational circuit that converts a 4-bit Gray code to its equivalent 4-bit binary number, we follow these steps:

**Gray to Binary Conversion Table:**

---

# Part 1: Gray Code to Binary Conversion

|   |   |   |   |   |
|---|---|---|---|---|
|Decimal|G3|G2|G1|G0|
|0|0|0|0|0|
|1|0|0|0|1|
|2|0|0|1|1|
|3|0|0|1|0|
|4|0|1|1|0|
|5|0|1|1|1|
|6|0|1|0|1|
|7|0|1|0|0|
|8|1|1|0|0|
|9|1|1|0|1|
|10|1|1|1|1|
|11|1|1|1|0|
|12|1|0|1|0|
|13|1|0|1|1|
|14|1|0|0|1|
|15|1|0|0|0|
|Hex|00FF|0F0F|3333|5555|

---

**Karnaugh Map for the Conversion:**

```undefined
G3G2\G1G0  00   01   11   10
    00     0000 0001 0011 0010
    01     0110 0111 0101 0100
    11     1100 1101 1111 1110
    10     1010 1011 1001 1000
```

---

# Binary - Gray Code Correspondence

|   |   |   |
|---|---|---|
|**Decimal**|**Binary**|**Gray Code**|
|0|0000|0000|
|1|0001|0001|
|2|0010|0011|
|3|0011|0010|
|4|0100|0110|
|5|0101|0111|
|6|0110|0101|
|7|0111|0100|
|8|1000|1100|
|9|1001|1101|
|10|1010|1111|
|11|1011|1110|
|12|1100|1010|
|13|1101|1011|
|14|1110|1001|
|15|1111|1000|

  

---

```Mermaid
graph TD
    subgraph "Part 1: Gray to Binary Conversion"
    
    
    
        G3 --> B3
        G3 --> XOR1
        G2 --> XOR1
        XOR1 --> B2
        B2 --> XOR2
        G1 --> XOR2
        XOR2 --> B1
        B1 --> XOR3
        G0 --> XOR3
        XOR3 --> B0
    end


    
    classDef default fill:\#f9f,stroke:#333,stroke-width:2px;
    classDef xor fill:\#ff9,stroke:#333,stroke-width:2px;

    class XOR1,XOR2,XOR3 xor;
```

---

  

**Design with XOR Gates:**

The conversion from Gray to binary is performed as follows:

- The most significant bit of the binary number (B3) is the same as the most significant bit of the Gray code (G3).
- Each subsequent binary bit is the result of the XOR operation between the previous binary bit and the corresponding Gray code bit.

**Equations:**

- **B3 = G3**
- **B2 = B3 XOR G2**
- **B1 = B2 XOR G1**
- **B0 = B1 XOR G0**

**Logic Diagram:**

- We use XOR gates for the operations.
- We have one XOR gate for each equation B2, B1, B0.
- B3 is connected directly to G3.

**Implementation:**

With the IC 7486 (Quad 2-input XOR Gate), we can implement the required XOR gates.

#### IC 7486 Pin Configuration
| Pin | Function | Connection |
|:---|:---|:---|
| 1, 2 | Gate 1 Inputs | G2, B3 |
| 3 | Gate 1 Output | B2 |
| 4, 5 | Gate 2 Inputs | G1, B2 |
| 6 | Gate 2 Output | B1 |
| 7 | Ground | GND (0V) |
| 9, 10 | Gate 3 Inputs | G0, B1 |
| 8 | Gate 3 Output | B0 |
| 14 | Supply Voltage | VCC (+5V) |


---

  

# Part 2: Complement with Respect to 9

**Circuit Design:**

- The circuit accepts a 4-bit BCD digit (D3 D2 D1 D0).
- It produces the complement with respect to 9 of the input digit.
- It detects invalid BCD inputs (values from 1010 to 1111).

---

### Complement with Respect to 9 Calculation

The complement with respect to 9 of a decimal digit $D$ is:

$C = 9 - D$

---

### Truth Table

|   |   |   |
|---|---|---|
|**D3 D2 D1 D0 (D)**|**C3 C2 C1 C0 (C)**|**Error**|
|0000 (0)|1001 (9)|0|
|0001 (1)|1000 (8)|0|
|0010 (2)|0111 (7)|0|
|0011 (3)|0110 (6)|0|
|0100 (4)|0101 (5)|0|
|0101 (5)|0100 (4)|0|
|0110 (6)|0011 (3)|0|
|0111 (7)|0010 (2)|0|
|1000 (8)|0001 (1)|0|
|1001 (9)|0000 (0)|0|
|**1010**|X|**1**|
|**1011**|X|**1**|
|**1100**|X|**1**|
|**1101**|X|**1**|
|**1110**|X|**1**|
|**1111**|X|**1**|

- For values from $D = [1010, ..., 1111]$, the Error is active ($Error = 1$).

---

### Karnaugh Maps

For C3:

```undefined
D3D2\D1D0 00  01  11  10
      00   1   1   1   1
      01   1   1   1   1
      11   0   0   0   0
      10   0   0   0   0
```

For C2:

```undefined
D3D2\D1D0 00  01  11  10
      00   1   1   1   1
      01   0   0   0   0
      11   0   0   0   0
      10   1   1   1   1
```

For C1:

```undefined
D3D2\D1D0 00  01  11  10
      00   1   1   0   0
      01   1   1   0   0
      11   1   1   0   0
      10   1   1   0   0
```

For C0:

```undefined
D3D2\D1D0 00  01  11  10
      00   1   0   0   1
      01   1   0   0   1
      11   1   0   0   1
      10   1   0   0   1
```

### Functions

### Complement with Respect to 9 Calculation:

The equations for $C3, C2, C1, C0$:

- $C3 = \overline{D3} + (\overline{D2} \cdot \overline{D1} \cdot \overline{D0})$
- $C2 = \overline{D2} + (\overline{D3} \cdot D2 \cdot \overline{D1})$
- $C1 = \overline{D1} + (\overline{D3} \cdot D2 \cdot D1 \cdot \overline{D0})$
- $C0 = \overline{D0}$

### Error Detection:

The equation for the error output:  
$Error = D3 \cdot (D2 + D1 + D0)$

---

### Hexadecimal Format for Each Signal

### Inputs:

- $D_0: \texttt{0000000000001111} = \texttt{0x000F}$
- $D_1: \texttt{0000000011110000} = \texttt{0x00F0}$
- $D_2: \texttt{0000111100001111} = \texttt{0x0F0F}$
- $D_3: \texttt{1111000011110000} = \texttt{0xF0F0}$

### Outputs:

- $C_0: \texttt{1111111111110000} = \texttt{FFF0}$
- $C_1: \texttt{1111000011110000} = \texttt{F0F0}$
- $C_2: \texttt{1100110011001100} = \texttt{CCCC}$
- $C_3: \texttt{1001100110011001} = \texttt{9999}$

### Error:

$\texttt{Error: } =\texttt{00FF}$

---

### Mermaid Diagram

```Mermaid
graph TD
    subgraph "Input Sequences"
        D0[D0 Sequence]
        D1[D1 Sequence]
        D2[D2 Sequence]
        D3[D3 Sequence]
    end

    subgraph "Logic Gates"
        direction LR
        D0 --> OR1[OR Gate 1]
        D1 --> OR1
        D2 --> OR2[OR Gate 2]
        OR1 --> OR2
        
        D3 --> AND1[AND Gate 1]
        OR2 --> AND1

        D0 --> COMP[Complement Logic]
        D1 --> COMP
        D2 --> COMP
        D3 --> COMP
    end

    subgraph "Output Lights"
        COMP --> C0[C0 Output]
        COMP --> C1[C1 Output]
        COMP --> C2[C2 Output]
        COMP --> C3[C3 Output]
        AND1 --> ERR[Error Light]
    end

    classDef sequence fill:\#e1f5fe,stroke:\#01579b,stroke-width:2px;
    classDef gate fill:\#fff3e0,stroke:\#e65100,stroke-width:2px;
    classDef output fill:\#f1f8e9,stroke:\#33691e,stroke-width:2px;
    
    class D0,D1,D2,D3 sequence;
    class OR1,OR2,AND1,COMP gate;
    class C0,C1,C2,C3,ERR output;
```

```Mermaid
graph TD
    subgraph "Complement with Respect to 9 and Error Detection"
        D3 --> NOT3[NOT]
        D2 --> NOT2[NOT]
        D1 --> NOT1[NOT]
        D0 --> NOT0[NOT]
        
        NOT3 --> C3
        NOT2 --> C2
        NOT1 --> C1
        NOT0 --> C0
        
        D2 --> OR1[OR]
        D1 --> OR1
        OR1 --> OR2[OR]
        D0 --> OR2
        
        D3 --> AND1[AND]
        OR2 --> AND1
        
        AND1 --> Error
    end
    
    classDef default fill:\#f9f,stroke:#333,stroke-width:2px;
    classDef not fill:\#ff9,stroke:#333,stroke-width:2px;
    classDef or fill:\#9ff,stroke:#333,stroke-width:2px;
    classDef and fill:\#f99,stroke:#333,stroke-width:2px;
    
    class NOT0,NOT1,NOT2,NOT3 not;
    class OR1,OR2 or;
    class AND1 and;
```

### Laboratory Implementation Summary

| IC Model | Function | Gates Used | Inputs Connected | Output Connected |
|:---|:---|:---|:---|:---|
| IC 7404 | Hex Inverters | 4 NOT gates | D0, D1, D2, D3 | C0, NOT(D1), NOT(D2), NOT(D3) |
| IC 7432 | Quad 2-input OR | 2 OR gates | (D0, D1), (OR1_out, D2) | OR1_out, OR2_out |
| IC 7408 | Quad 2-input AND | 1 AND gate | D3, OR2_out | Error LED |
| IC 7486 | Quad 2-input XOR | 3 XOR gates | (G2, B3), (G1, B2), (G0, B1) | B2, B1, B0 |

All power pins (Pin 14 = VCC +5V) and ground pins (Pin 7 = GND 0V) must be decoupled with 0.1 uF ceramic capacitors.

