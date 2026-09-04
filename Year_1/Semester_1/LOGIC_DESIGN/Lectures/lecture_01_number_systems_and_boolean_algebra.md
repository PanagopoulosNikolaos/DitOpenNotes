# Lecture 01: Number Systems and Boolean Algebra

## Context and Grounding
This lecture introduces the mathematical and algorithmic foundations of digital systems. It covers positional number systems, radix conversions, signed binary arithmetic via complements, alphanumeric and numeric codes, the axiomatic foundation of Boolean algebra, and canonical canonical Sum of Minterms and Product of Maxterms representations.

---

## 1. Positional Number Systems

A real number $N$ represented in base (radix) $r \ge 2$ is expanded as:
$$(N)_r = \sum_{i=-m}^{n-1} d_i r^i = d_{n-1} r^{n-1} + \cdots + d_0 r^0 + d_{-1} r^{-1} + \cdots + d_{-m} r^{-m}$$
where each digit satisfies $0 \le d_i < r$.

### 1.1 Common Digital Number Systems
| System | Radix ($r$) | Allowed Digits | Bit Equivalence |
|:---|:---:|:---|:---:|
| Binary | 2 | $\{0, 1\}$ | 1 bit |
| Octal | 8 | $\{0, 1, 2, 3, 4, 5, 6, 7\}$ | 3 bits ($2^3$) |
| Decimal | 10 | $\{0, 1, 2, 3, 4, 5, 6, 7, 8, 9\}$ | — |
| Hexadecimal | 16 | $\{0, 1, \ldots, 9, A, B, C, D, E, F\}$ | 4 bits ($2^4$) |

### 1.2 Base Conversions
* **Integer Conversion from Base 10 to Base $r$**: Repeated division by $r$; remainder sequence read from bottom to top (least to most significant).
* **Fractional Conversion from Base 10 to Base $r$**: Repeated multiplication by $r$; integer parts read from top to bottom.
* **Direct Binary-Octal-Hexadecimal Conversions**: Group binary bits into sets of 3 (for octal) or sets of 4 (for hex), partitioned from the binary point outwards.

---

## 2. Complements and Signed Arithmetic

### 2.1 Definitions of Complements
For an $n$-digit integer $N$ in base $r$:
1. **Radix Complement ($r$'s Complement)**:
   $$K_r(N) = r^n - N \quad (N \neq 0)$$
2. **Diminished Radix Complement ($(r-1)$'s Complement)**:
   $$K_{r-1}(N) = (r^n - 1) - N$$
   Relation: $K_r(N) = K_{r-1}(N) + 1$.

### 2.2 Signed 2's Complement Representation (Binary)
In an $n$-bit 2's complement system:
* The most significant bit (MSB) acts as the sign bit ($0 \implies$ positive, $1 \implies$ negative).
* Representable range:
  $$-2^{n-1} \le N \le 2^{n-1} - 1$$
* **Negation Rule**: Invert all bits ($1 \leftrightarrow 0$) and add $1$.
* **Arithmetic Subtraction**: $A - B = A + (-B) = A + K_2(B)$.
* **Arithmetic Overflow Condition**: Overflow occurs during the addition of two numbers with identical signs if the result exhibits the opposite sign:
  $$V = C_{\text{in}} \oplus C_{\text{out}}$$
  where $C_{\text{in}}$ and $C_{\text{out}}$ are carries into and out of the MSB.

---

## 3. Binary Codes

* **BCD (Binary Coded Decimal 8421)**: Encodes each decimal digit ($0-9$) using a 4-bit binary equivalent ($0000_2$ to $1001_2$). Combinations $1010_2$ through $1111_2$ are invalid.
* **Gray Code**: Reflected binary code where consecutive values differ in exactly **one bit position** ($\Delta = 1$), eliminating transient race conditions in rotary encoders.
  - Conversion Binary to Gray: $G_i = B_i \oplus B_{i+1}$.

---

## 4. Boolean Algebra and Canonical Forms

### 4.1 Huntington's Postulates & Algebraic Theorems
Let $B$ be a set equipped with binary operations $+$ (OR) and $\cdot$ (AND), unary operation $'$ (NOT), and identities $0$ and $1$:
1. **Closure**: $x + y \in B$, $x \cdot y \in B$.
2. **Commutativity**: $x + y = y + x$, $x \cdot y = y \cdot x$.
3. **Distributivity**:
   $$x \cdot (y + z) = (x \cdot y) + (x \cdot z)$$
   $$x + (y \cdot z) = (x + y) \cdot (x + z)$$
4. **Identity**: $x + 0 = x$, $x \cdot 1 = x$.
5. **Complement**: $x + x' = 1$, $x \cdot x' = 0$.
6. **Involution**: $(x')' = x$.
7. **De Morgan's Laws**:
   $$(x + y)' = x' \cdot y'$$
   $$(x \cdot y)' = x' + y'$$

### 4.2 Canonical Forms: Minterms and Maxterms
* **Minterm ($m_i$)**: A product (AND) of all literals where each variable appears complemented if $0$ or uncomplemented if $1$.
* **Maxterm ($M_i$)**: A sum (OR) of all literals where each variable appears uncomplemented if $0$ or complemented if $1$.
* Relation: $M_i = (m_i)'$.

Every Boolean function $F$ can be expressed uniquely as:
* **Sum of Minterms (SOP)**: $F = \sum m(\text{indices where } F = 1)$.
* **Product of Maxterms (POS)**: $F = \prod M(\text{indices where } F = 0)$.

