# 1. Number Systems and Binary Arithmetic

This chapter introduces the fundamental concepts of number systems used in digital systems, as well as the basic arithmetic operations in the binary system. Understanding number representation and arithmetic techniques is a prerequisite for designing arithmetic units (Chapter 7) and for analyzing computational errors.

---

## 1. Number Systems

### 1.1 Binary System (Base 2)

The binary system uses two digits: $0$ and $1$. Each binary number is represented as a polynomial of base 2:

$$
N_2 = \sum_{i=-m}^{n-1} b_i \cdot 2^i
$$

where $b_i \in \{0,1\}$ and $n$ is the number of integer bits, $m$ the number of fractional bits.

**Example:** $(1011.01)_2 = 1\cdot2^3 + 0\cdot2^2 + 1\cdot2^1 + 1\cdot2^0 + 0\cdot2^{-1} + 1\cdot2^{-2} = 8 + 0 + 2 + 1 + 0 + 0.25 = (11.25)_{10}$

### 1.2 Octal System (Base 8)

Uses digits $0$ through $7$. Each octal digit corresponds to three binary digits:

$$
N_8 = \sum_{i=-m}^{n-1} o_i \cdot 8^i,\quad o_i \in \{0,1,\dots,7\}
$$

**Conversion 2→8:** Group 3 bits from the radix point.
- $(110101.01)_2 \to 110\;101\;.010 \to (65.2)_8$

### 1.3 Hexadecimal System (Base 16)

Uses digits $0$-$9$ and $A$-$F$ ($A=10, B=11, C=12, D=13, E=14, F=15$). Each hexadecimal digit corresponds to four binary digits:

$$
N_{16} = \sum_{i=-m}^{n-1} h_i \cdot 16^i,\quad h_i \in \{0,1,\dots,9,A,\dots,F\}
$$

**Conversion 2→16:** Group 4 bits from the radix point.
- $(11010110.1)_2 \to 1101\;0110\;.1000 \to (D6.8)_{16}$

### 1.4 BCD (Binary Coded Decimal)

Each decimal digit is encoded in 4 bits:

| Decimal | BCD |
|:---|---:|
| 0 | 0000 |
| 1 | 0001 |
| 2 | 0010 |
| 3 | 0011 |
| 4 | 0100 |
| 5 | 0101 |
| 6 | 0110 |
| 7 | 0111 |
| 8 | 1000 |
| 9 | 1001 |

> **[Key Insight]** The code words $1010$ through $1111$ are invalid in BCD. The number $(127)_{10}$ in BCD is $0001\;0010\;0111$, not $01111111$ which would be the binary representation.

### 1.5 Gray Code

Binary encoding where consecutive values differ by only one bit. Used in K-Maps (Chapter 4) and position encoders.

**Conversion from binary to Gray:**
$$
G_n = B_n,\quad G_i = B_i \oplus B_{i+1}
$$

**Conversion from Gray to binary:**
$$
B_n = G_n,\quad B_i = B_{i+1} \oplus G_i
$$

**Example:** $(1011)_2 \to$ Gray:
- $G_3 = B_3 = 1$
- $G_2 = B_3 \oplus B_2 = 1 \oplus 0 = 1$
- $G_1 = B_2 \oplus B_1 = 0 \oplus 1 = 1$
- $G_0 = B_1 \oplus B_0 = 1 \oplus 1 = 0$
- Result: $(1110)_{\text{Gray}}$

---

## 2. Representation of Negative Numbers

### 2.1 Sign-Magnitude

The MSB (Most Significant Bit) defines the sign ($0=+$, $1=-$). The remaining $n-1$ bits represent the magnitude.

- Range n-bit: $[-(2^{n-1}-1),\;+(2^{n-1}-1)]$
- Two representations of zero: $0000$ $(+0)$ and $1000$ $(-0)$
- **Disadvantage:** Very complex implementation of arithmetic operations

### 2.2 1's Complement

The negative number is obtained by inverting all bits of the positive:

- $(+5)_{10} = 0101$ → $(-5)_{10} = 1010$
- Range n-bit: $[-(2^{n-1}-1),\;+(2^{n-1}-1)]$
- Two representations of zero: $0000$ $(+0)$ and $1111$ $(-0)$
- Subtraction is done by addition and end-around carry

### 2.3 2's Complement

The negative number is obtained as (1's complement) $+ 1$:

- $(+5)_{10} = 0101$ → $(-5)_{10} = 1010 + 1 = 1011$
- Range n-bit: $[-2^{n-1},\;2^{n-1}-1]$
- Unique representation of zero: $0000$
- **Preferred method** in digital systems

**Sign extension rule:** Copy the MSB to the new higher-order bits.

$$
(1011)_2 \text{ (4-bit, -5)} \to (11111011)_2 \text{ (8-bit, -5)}
$$

### 2.4 n-bit Value Range

| Representation | Minimum | Maximum |
|:---|---:|---:|
| Unsigned | $0$ | $2^n - 1$ |
| Sign-Magnitude | $-(2^{n-1} - 1)$ | $2^{n-1} - 1$ |
| 1's Complement | $-(2^{n-1} - 1)$ | $2^{n-1} - 1$ |
| 2's Complement | $-2^{n-1}$ | $2^{n-1} - 1$ |

---

## 3. Binary Arithmetic

### 3.1 Addition

The addition of two binary digits follows the rules:

| $A$ | $B$ | Sum | Carry |
|:---:|:---:|:---:|:-----:|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

**Carry propagation:** In multi-digit addition, the carry propagates from LSB to MSB. The delay of this propagation is critical for adder speed.

**Example of 4-bit addition:**
```
  1 1    (carries)
  0 1 1 0  (6)
+ 0 1 0 1  (5)
--------
  1 0 1 1  (11)
```

### 3.2 Subtraction with 2's Complement

The subtraction $A - B$ is implemented as $A + (-B)$, where $(-B)$ is the 2's complement of $B$:

**Steps:**
1. Compute the 2's complement of $B$ (invert + 1)
2. Add $A$ with the result
3. Discard the final carry (if present)

**Example:** $6 - 5 = 6 + (-5)$
```
  0110  (6)
+ 1011  (-5 in 2's complement)
--------
 10001 → 0001 (1) with carry discarded
```

### 3.3 Multiplication and Division

**Multiplication:** Follows the logic of decimal multiplication. Each bit of the multiplier determines whether the multiplicand is added with a shift (shift-and-add).

**Example:** $5 \times 3 = 15$
```
    0101  (5)
  × 0011  (3)
  -------
    0101   (5 × 1, shift 0)
   0101    (5 × 1, shift 1)
  0000     (5 × 0, shift 2)
+ 0000     (5 × 0, shift 3)
  --------
  0001111  (15)
```

**Division:** Uses the method of repeated subtraction with shift (restoring/non-restoring division). Implemented with alternating subtractions and shifts of the divisor.

> **[Key Insight]** In practice, multiplication and division by powers of 2 are implemented with left (multiplication) or right (division) shift. For example, $5 \ll 2 = 20$ (multiplication by 4).

### 3.4 Overflow Detection

Overflow occurs when the result of an operation exceeds the range of representation.

**Detection rule for 2's complement addition:**
$$
\text{Overflow} = C_{n-1} \oplus C_n
$$

where $C_{n-1}$ is the carry towards the MSB and $C_n$ is the output carry from the MSB.

**Example (overflow in 4-bit 2's complement):**
```
  0111  (7)
+ 0001  (1)
--------
  1000  (-8) → WRONG! C_3=0, C_4=1 → overflow=1
```

---

## 4. Character Encoding

### 4.1 ASCII

7-bit encoding (0-127) for Latin characters, numbers, and symbols. The 8th bit is used as parity bit.

- 'A' = $(65)_{10} = (1000001)_2$
- 'a' = $(97)_{10} = (1100001)_2$
- '0' = $(48)_{10} = (0110000)_2$

> **[Exam Tip]** The difference between uppercase and lowercase ASCII is 32. This means bit 5 (value 32) determines the case.

### 4.2 Error Detection Codes

**Parity Bit:**
- **Even parity:** The parity bit is chosen so that the count of 1s is even
- **Odd parity:** The parity bit is chosen so that the count of 1s is odd

**Example:** For the byte $1011001$:
- Even parity bit: $1$ (total 1s = 4, even)
- Odd parity bit: $0$ (total 1s = 4 + 0 = 4, even → needs 1 for odd)

**Hamming Code:** Allows detection and correction of single-bit errors. Parity bits are placed at positions that are powers of 2 (1, 2, 4, 8, ...). Each parity bit checks specific bit positions based on their binary representation.

---

## Solved Exercises

### Exercise 1: Base Conversion

**Problem:** Convert the number $(2F.4)_{16}$ to binary, octal, and decimal.

**Solution:**

1. **Hexadecimal → Binary:** Each digit in 4 bits:
   - $2 \to 0010$
   - $F \to 1111$
   - $4 \to 0100$
   - Result: $(0010\;1111\;.0100)_2 = (101111.01)_2$

2. **Binary → Octal:** Group 3 bits from radix point:
   - $101\;111\;.010 \to (57.2)_8$

3. **Hexadecimal → Decimal:**
   $$
   2F.4_{16} = 2\cdot16^1 + 15\cdot16^0 + 4\cdot16^{-1} = 32 + 15 + 0.25 = (47.25)_{10}
   $$

### Exercise 2: Addition in Different Bases

**Problem:** Calculate: (a) $(1101)_2 + (1011)_2$, (b) $(3A)_{16} + (2F)_{16}$.

**Solution (a):**
```
  1 1 1    (carries)
  1 1 0 1  (13)
+ 1 0 1 1  (11)
--------
1 1 0 0 0  (24)
```
Final carry: $1$ (not an overflow for unsigned).

**Solution (b):**
$$
3A_{16} = 3\cdot16 + 10 = 58_{10},\quad 2F_{16} = 2\cdot16 + 15 = 47_{10}
$$
$$
3A + 2F = 58 + 47 = 105_{10} = 69_{16}
$$

### Exercise 3: 2's Complement

**Problem:** Represent the number $(-23)_{10}$ in 8-bit 2's complement.

**Solution:**
1. Representation of $+23$: $(00010111)_2$
2. Invert all bits: $(11101000)_2$
3. Add 1: $(11101001)_2$

Verification: $11101001 + 00010111 = 00000000$ (carry discarded), so the representation is correct.

### Exercise 4: Subtraction with 2's Complement

**Problem:** Calculate $25 - 18$ with 8-bit 2's complement.

**Solution:**
1. $+25 = (00011001)_2$
2. $+18 = (00010010)_2$
3. 2's complement of $+18$: $11101101 + 1 = 11101110$
4. Addition:
```
  00011001  (25)
+ 11101110  (-18)
----------
1 00000111  (7) → carry discarded
```
Result: $(00000111)_2 = 7$, correct.

### Exercise 5: Overflow Detection

**Problem:** Check for overflow in the operations (4-bit 2's complement): (a) $7 + 1$, (b) $(-4) + (-5)$.

**Solution (a):**
```
  0111  (7)
+ 0001  (1)
--------
  1000  (-8)
```
$C_3 = 0$ (carry to MSB), $C_4 = 1$ (output carry)
$C_3 \oplus C_4 = 1$ → **Overflow exists** (sum of positives gives negative result).

**Solution (b):**
```
  1100  (-4)
+ 1011  (-5)
--------
1 0111  (7)
```
$C_3 = 1$, $C_4 = 1$
$C_3 \oplus C_4 = 0$ → **No overflow** (the result $-9$ is out of range $-8$ to $7$; but overflow is detected only when the signs of the addends are the same and the result sign is different. Here $(-4)+(-5)=-9$, and $-9$ in 4-bit 2's complement is $0111$ which is $+7$, so the signs differ: overflow.)

> **[Key Insight]** In practice, overflow is detected by checking if the signs of the two addends are the same and the sign of the result is different. The method $C_{n-1} \oplus C_n$ is equivalent.

### Exercise 6: Multiplication with Shift

**Problem:** Calculate $6 \times 10$ using shift-and-add.

**Solution:**
$$6_{10} = (0110)_2,\quad 10_{10} = (1010)_2$$

```
  0110  (6)
× 1010  (10)
-------
  0000   (6 × 0, shift 0)
 0110    (6 × 1, shift 1)
0000     (6 × 0, shift 2)
0110     (6 × 1, shift 3)
--------
0111100  (60)
```

### Exercise 7: Gray Code

**Problem:** Convert the binary number $(1101)_2$ to Gray and then verify by converting back to binary.

**Solution:**
**Binary → Gray:**
- $G_3 = B_3 = 1$
- $G_2 = B_3 \oplus B_2 = 1 \oplus 1 = 0$
- $G_1 = B_2 \oplus B_1 = 1 \oplus 0 = 1$
- $G_0 = B_1 \oplus B_0 = 0 \oplus 1 = 1$
- Gray: $(1011)_{\text{Gray}}$

**Gray → Binary:**
- $B_3 = G_3 = 1$
- $B_2 = B_3 \oplus G_2 = 1 \oplus 0 = 1$
- $B_1 = B_2 \oplus G_1 = 1 \oplus 1 = 0$
- $B_0 = B_1 \oplus G_0 = 0 \oplus 1 = 1$
- Verification: $(1101)_2$ (initial value)

### Exercise 8: BCD Encoding

**Problem:** Encode the number $(937)_{10}$ in BCD and add it to $(258)_{10}$ in BCD.

**Solution:**
1. $(937)_{10} \to 1001\;0011\;0111$ (BCD)
2. $(258)_{10} \to 0010\;0101\;1000$ (BCD)

BCD addition (per 4-bit group):
```
  1001 0011 0111  (937)
+ 0010 0101 1000  (258)
  --------------------
  1011 1000 1111
```
Each group > 9 requires correction (add 6):
- Units: $1111$ (15) → $1111 + 0110 = 1\;0101$ (carry 1)
- Tens: $1000 + 0001\;(\text{carry}) = 1001$ (9, valid)
- Hundreds: $1011$ (11) → $1011 + 0110 = 1\;0001$ (carry 1)
- Thousands: $0001$ (1)

Result: $0001\;0001\;1001\;0101$ → $(1195)_{10}$

---

## Exam Tip: Recognizing 2's Complement

In an n-bit number problem, if the MSB is 1 and you are asked to compute the value, remember:
1. If the representation is unsigned: simple conversion from binary
2. If the representation is 2's complement: subtract $2^n$ from the unsigned value

Example: $(1100)_2$ — unsigned: $12$, 2's complement: $12 - 16 = -4$

Also, in sign extension, the new MSB is a copy of the old MSB. For example, extending $1011$ (-5 in 4-bit) to 8-bit gives $11111011$ (-5 in 8-bit).
