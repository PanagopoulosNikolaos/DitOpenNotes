# Digital Systems and Binary Numbers

This chapter introduces the fundamental concepts of digital systems. It covers number systems (binary, octal, decimal, hexadecimal), conversions between them, basic arithmetic operations, negative number representation through complements, signed binary numbers, binary codes (BCD, Gray, ASCII), and basic logic operations.

---

## 1. Core Definitions

### 1.1 Analog and Digital Systems
- **Analog Signal:** A signal whose amplitude varies continuously over time, taking infinite values within a given interval.
- **Digital Signal:** A signal that takes only discrete values at specific time intervals (quantized signal).
- **Binary Digital Signal:** A digital signal with two discrete levels, corresponding to logic values $0$ (Low, False, Off) and $1$ (High, True, On).

### 1.2 Number Systems with Base $r$
A number $N$ in a system with base (radix) $r$ is represented as:
$$
(N)_r = d_{n-1} r^{n-1} + d_{n-2} r^{n-2} + \cdots + d_0 r^0 + d_{-1} r^{-1} + \cdots + d_{-m} r^{-m}
$$
where:
- $r$ is the base of the system ($r \geq 2$).
- $d_i$ are the digits, with $0 \leq d_i < r$.
- $r^i$ is the weight of position $i$.

### 1.3 Complements
Complements are used in digital systems to simplify subtraction and represent negative numbers.
- **Diminished Radix Complement (Complement with respect to $(r-1)$):**
  For an $n$-digit integer $N$ in base $r$:
  $$
  \text{Compl}_{r-1}(N) = (r^n - 1) - N
  $$
- **Radix Complement (Complement with respect to $r$):**
  $$
  \text{Compl}_r(N) = r^n - N \quad (\text{for } N \neq 0)
  $$
  It also holds:
  $$
  \text{Compl}_r(N) = \text{Compl}_{r-1}(N) + 1
  $$

---

## 2. Foundational Formulas

### 2.1 Decimal System ($r = 10$)
Digits: $\{0, 1, 2, 3, 4, 5, 6, 7, 8, 9\}$

### 2.2 Binary System ($r = 2$)
Digits: $\{0, 1\}$ (called binary digits or bits).
- $4 \; \text{bits} = 1 \; \text{Nibble}$
- $8 \; \text{bits} = 1 \; \text{Byte}$

### 2.3 Octal System ($r = 8$)
Digits: $\{0, 1, 2, 3, 4, 5, 6, 7\}$

### 2.4 Hexadecimal System ($r = 16$)
Digits: $\{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F\}$
Where: $A=10, B=11, C=12, D=13, E=14, F=15$.

### 2.5 Powers of 2
- $2^{10} = 1024 = 1\,\text{K} \; (\text{Kilo})$
- $2^{20} = 1\,\text{M} \; (\text{Mega})$
- $2^{30} = 1\,\text{G} \; (\text{Giga})$
- $2^{40} = 1\,\text{T} \; (\text{Tera})$

---

## Solved Exercises

### Exercise 1: Integer Decimal to Binary Conversion
**Problem:**
Convert the decimal number $(41)_{10}$ to the binary system.

**Solution:**
We divide successively by base $r=2$ and keep the remainders:
1. $41 \div 2 = 20$ with remainder $1$ (LSB - $a_0$)
2. $20 \div 2 = 10$ with remainder $0$ ($a_1$)
3. $10 \div 2 = 5$ with remainder $0$ ($a_2$)
4. $5 \div 2 = 2$ with remainder $1$ ($a_3$)
5. $2 \div 2 = 1$ with remainder $0$ ($a_4$)
6. $1 \div 2 = 0$ with remainder $1$ (MSB - $a_5$)

Collecting the remainders from end to beginning:
$$
(41)_{10} = (101001)_2
$$

---

### Exercise 2: Fractional Decimal to Binary Conversion
**Problem:**
Convert the decimal fraction $(0.6875)_{10}$ to the binary system.

**Solution:**
We multiply the fractional part successively by base $r=2$ and keep the integer part:
1. $0.6875 \times 2 = 1.375 \rightarrow$ integer part $1$ ($a_{-1}$)
2. $0.375 \times 2 = 0.75 \rightarrow$ integer part $0$ ($a_{-2}$)
3. $0.75 \times 2 = 1.5 \rightarrow$ integer part $1$ ($a_{-3}$)
4. $0.5 \times 2 = 1.0 \rightarrow$ integer part $1$ ($a_{-4}$)

The fractional part has been zeroed. Collecting the integer parts:
$$
(0.6875)_{10} = (0.1011)_2
$$

---

### Exercise 3: Conversion from Binary to Octal and Hexadecimal
**Problem:**
Given the binary number $(10110110.01101)_2$. Convert it to octal and hexadecimal systems.

**Solution:**
1. **To Octal ($r=8=2^3$):**
   Group bits by 3 starting from the radix point:
   - Integer part: $\underline{010} \; \underline{110} \; \underline{110} \rightarrow 2 \; 6 \; 6$
   - Fractional part: $\underline{011} \; \underline{010} \rightarrow 3 \; 2$
   $$
   (10110110.01101)_2 = (266.32)_8
   $$

2. **To Hexadecimal ($r=16=2^4$):**
   Group bits by 4 starting from the radix point:
   - Integer part: $\underline{1011} \; \underline{0110} \rightarrow B \; 6$
   - Fractional part: $\underline{0110} \; \underline{1000} \rightarrow 6 \; 8$
   $$
   (10110110.01101)_2 = (B6.68)_{16}
   $$

---

### Exercise 4: Calculation of Complements 1 and 2
**Problem:**
Find the complement with respect to 1 and with respect to 2 of the binary number $N = (1011000)_2$.

**Solution:**
1. **Complement with respect to 1:**
   Invert all bits (the $0$s become $1$s and the $1$s become $0$s):
   $$
   \text{Compl}_1(1011000) = 0100111
   $$
2. **Complement with respect to 2:**
   Add $1$ to the complement with respect to 1:
   $$
   0100111 + 1 = 0101000
   $$
   *Alternative rule:* Starting from the right, keep all bits up to and including the first $1$, and invert all remaining bits to the left:
   $$
   1011000 \rightarrow 0101000
   $$

---

### Exercise 5: Subtraction Using 2's Complement
**Problem:**
Perform the operation $X - Y$ using 2's complement for the binary numbers $X = (1010100)_2$ (minuend) and $Y = (1000011)_2$ (subtrahend).

**Solution:**
1. Calculate the 2's complement of $Y$:
   $$
   Y = 1000011 \rightarrow \text{Compl}_2(Y) = 0111101
   $$
2. Add the 2's complement of $Y$ to $X$:
   $$
   \begin{array}{r@{\quad}l}
   1010100 & (X) \\
   +\, 0111101 & (\text{Compl}_2(Y)) \\
   \hline
   10010001 & (\text{'1' is the final carry})
   \end{array}
   $$
3. Since there is a final carry (the leftmost $1$), we discard it. The result is positive:
   $$
   X - Y = 0010001
   $$

---

### Exercise 6: Subtraction Using 2's Complement (Negative Result)
**Problem:**
Perform the operation $Y - X$ using 2's complement for the same numbers $X = (1010100)_2$ and $Y = (1000011)_2$.

**Solution:**
1. Calculate the 2's complement of $X$:
   $$
   X = 1010100 \rightarrow \text{Compl}_2(X) = 0101100
   $$
2. Add the 2's complement of $X$ to $Y$:
   $$
   \begin{array}{r@{\quad}l}
   1000011 & (Y) \\
   +\, 0101100 & (\text{Compl}_2(X)) \\
   \hline
   1101111 & (\text{zero final carry})
   \end{array}
   $$
3. Since there is no final carry, the result is negative and equals the negative of the 2's complement of the sum:
   $$
   \text{Compl}_2(1101111) = 0010001
   $$
   Therefore:
   $$
   Y - X = -(0010001)_2
   $$

---

### Exercise 7: Addition of Signed Numbers Using 2's Complement
**Problem:**
Perform the addition $(+6) + (-13)$ using signed 2's complement representation with 8 bits.

**Solution:**
1. Representation of $+6$: $(+6)_{10} = (00000110)_2$
2. Representation of $-13$:
   - $+13 = (00001101)_2$
   - $-13 = \text{Compl}_2(00001101) = (11110011)_2$
3. Perform the addition:
   $$
   \begin{array}{r@{\quad}l}
   00000110 & (+6) \\
   +\, 11110011 & (-13) \\
   \hline
   11111001 & (\text{no final carry})
   \end{array}
   $$
4. The MSB is $1$, so the result is negative. Its magnitude is the 2's complement of $11111001$, which is $00000111$ ($7$).
   $$
   \text{Result} = -7
   $$

---

### Exercise 8: BCD Addition with Correction
**Problem:**
Perform the addition of BCD numbers $1000$ ($8$) and $0101$ ($5$).

**Solution:**
1. Add the two binary numbers:
   $$
   \begin{array}{r@{\quad}l}
   1000 & (8) \\
   +\, 0101 & (5) \\
   \hline
   1101 & (13)
   \end{array}
   $$
2. The binary sum is $1101_2 > 1001_2$ ($9$). This is not a valid BCD digit.
3. For correction, add the number $0110$ ($6$):
   $$
   \begin{array}{r@{\quad}l}
   1101 \\
   +\, 0110 \\
   \hline
   10011
   \end{array}
   $$
4. The final BCD result with 8 bits (2 BCD digits) is:
   $$
   0001 \; 0011 \rightarrow 1 \; 3 \rightarrow (13)_{10}
   $$

---

## Exam Tip: Subtraction with Complements
In exams, a common mistake is omitting the correction when the result is negative (i.e., when no final carry is generated).
- **If there is a final carry of 1:** Discard it; the result is positive.
- **If the final carry is 0:** The result is negative. Take the complement (with respect to 2 or 1 depending on the method) of the sum and apply a minus sign.
