# C — Structs, Unions, and Bit Manipulation

Structures and unions allow C programmers to construct user-defined types, grouping data fields together or overlaying them in the same memory location. By exposing details such as struct member alignment, memory padding, and bitwise manipulation, C provides a direct interface to hardware registers, network packets, and binary formats. This file covers structures, unions, type definitions, compiler padding mechanics, and bitwise operations.

---

## 1. Structures and `typedef`

A **structure** (`struct`) is a user-defined aggregate type that groups variables of different types under a single name.

### 1.1 Declarations and Member Access

#### Syntax Reference

```text
/* Struct Declaration */
struct <tag_name> {
    <type1> <member1>;
    <type2> <member2>;
    ...
};

/* Instantiation and Initialization */
struct <tag_name> <variable_name> = { .member1 = <val1>, .member2 = <val2> };
```

Members are accessed using:
- The dot operator (`.`) for direct structure variables.
- The arrow operator (`->`) for pointers to structures.

---

### 1.2 The `typedef` Keyword

`typedef` creates an alias for an existing type, simplifying declarations.

#### Syntax Reference

```text
typedef struct <tag_name> {
    <type> <member>;
} <alias_name>;

/* Instantiation using alias */
<alias_name> <variable_name>;
```

---

## 2. Unions and Memory Overlay

A **union** is a user-defined type where all members share the same memory location. The size of a union is equal to the size of its largest member.

### 2.1 Declarations and Type Punning

#### Syntax Reference

```text
union <tag_name> {
    <type1> <member1>;
    <type2> <member2>;
};
```

Unions are commonly used for:
1. **Memory efficiency:** Storing mutually exclusive data fields.
2. **Type punning:** Accessing the underlying byte representation of a type.

```c
#include <stdio.h>

union float_bytes {
    float f;
    unsigned char bytes[4];
};

void print_bytes(float value) {
    union float_bytes pun;
    pun.f = value;
    printf("Byte representation: %02x %02x %02x %02x\n",
           pun.bytes[0], pun.bytes[1], pun.bytes[2], pun.bytes[3]);
}
```

---

## 3. Structural Alignment and Padding

Computers access memory in words (e.g. 4-byte or 8-byte boundaries). To optimize memory read/write cycles, compilers automatically align variables to memory addresses that are multiples of their size.

### 3.1 Alignment Rules

- An $n$-byte primitive type must reside at a memory address that is a multiple of $n$.
- Compilers insert unused **padding bytes** inside structs to satisfy these alignment restrictions.
- The overall size of a struct is padded to make it a multiple of its largest member's alignment requirement.

```
Example Struct:
struct data {
    char a;      // 1 byte
    // 3 bytes padding
    int b;       // 4 bytes
};
Total Size = 8 bytes
```

---

## 4. Bitwise Operators and Bit-fields

C provides bitwise operators to manipulate individual bits within integer variables.

### 4.1 Bitwise Operators Reference Table

| Operator | Name | Syntax | Behavior | Example (8-bit) |
| :--- | :--- | :--- | :--- | :--- |
| `&` | Bitwise AND | `a & b` | Sets bit to $1$ if both corresponding bits are $1$ | `0b1100 & 0b1010 = 0b1000` |
| `\|` | Bitwise OR | `a \| b` | Sets bit to $1$ if at least one bit is $1$ | `0b1100 \| 0b1010 = 0b1110` |
| `^` | Bitwise XOR | `a ^ b` | Sets bit to $1$ if corresponding bits differ | `0b1100 ^ 0b1010 = 0b0110` |
| `~` | Bitwise NOT | `~a` | Inverts all bits (one's complement) | `~0b1100 = 0b...0011` |
| `<<` | Left Shift | `a << n` | Shifts bits left by `n` places, filling with $0$ | `0b0011 << 2 = 0b1100` |
| `>>` | Right Shift | `a >> n` | Shifts bits right by `n` places | `0b1100 >> 2 = 0b0011` |

---

### 4.2 Bit-fields

Bit-fields allow specifying the exact number of bits allocated to struct members, which is useful for packing flags or matching hardware protocols.

#### Syntax Reference

```text
struct <tag_name> {
    <integer_type> <name> : <width_in_bits>;
};
```

---

## Solved Exercises

### Exercise 1: Struct Allocation and Member Access

**Problem:** Implement a struct representing a 2D Point. Write a function `double distance(const Point *p1, const Point *p2)` and demonstrate arrow operator syntax.

**Solution:**

```c
#include <stdio.h>
#include <math.h>

typedef struct {
    double x;
    double y;
} Point;

double distance(const Point *p1, const Point *p2) {
    // Access members via the arrow operator
    double dx = p1->x - p2->x;
    double dy = p1->y - p2->y;
    return sqrt(dx * dx + dy * dy);
}

int main(void) {
    Point p1 = {0.0, 0.0};
    Point p2 = {3.0, 4.0};
    printf("Distance = %.2f\n", distance(&p1, &p2));
    return 0;
}
```

```text
Distance = 5.00
```

---

### Exercise 2: Union Memory Footprint

**Problem:** Predict the size of the following union and explain the value printed.

```c
#include <stdio.h>

union Number {
    char c;
    short s;
    int i;
};

int main(void) {
    union Number n;
    n.i = 0x12345678;
    printf("c = 0x%x\n", n.c);
    printf("Size = %zu\n", sizeof(n));
    return 0;
}
```

**Solution:**
1. The union members are: `c` (1 byte), `s` (2 bytes), and `i` (4 bytes).
2. The size of the union is the size of its largest member: $4$ bytes.
3. Since all members share the same memory location, assigning `n.i = 0x12345678` overwrites the shared memory block.
4. On a little-endian platform (most modern targets), the bytes of `n.i` are laid out in memory starting with the least significant byte: `78 56 34 12`.
5. Accessing `n.c` reads the first byte of the memory block, which is `0x78`.

```text
c = 0x78
Size = 4
```

---

### Exercise 3: Struct Padding and Alignment Calculation

**Problem:** Calculate the total size of `struct A` and `struct B` assuming standard alignment rules.

```c
struct A {
    char x;
    int y;
    char z;
};

struct B {
    int y;
    char x;
    char z;
};
```

**Solution:**
1. **For `struct A`:**
   - `x` (type `char`, size 1) is placed at offset $0$.
   - `y` (type `int`, size 4) requires a 4-byte boundary. The next free address is offset $1$. The compiler adds $3$ bytes of padding, placing `y` at offset $4$.
   - `z` (type `char`, size 1) is placed at offset $8$.
   - The largest member alignment requirement is $4$ bytes. The current struct size is $9$ bytes. The compiler adds $3$ bytes of padding at the end to make the total size a multiple of $4$.
   - Total Size of `struct A` = $12$ bytes.
2. **For `struct B`:**
   - `y` (type `int`, size 4) is placed at offset $0$.
   - `x` (type `char`, size 1) is placed at offset $4$.
   - `z` (type `char`, size 1) is placed at offset $5$.
   - The largest member alignment requirement is $4$ bytes. The current size is $6$ bytes. The compiler adds $2$ bytes of padding at the end.
   - Total Size of `struct B` = $8$ bytes.

---

### Exercise 4: Struct Size Optimization Verification

**Problem:** Write a C program to print and verify the alignment calculations of `struct A` and `struct B` from Exercise 3.

**Solution:**

```c
#include <stdio.h>
#include <stddef.h>

struct A {
    char x;
    int y;
    char z;
};

struct B {
    int y;
    char x;
    char z;
};

int main(void) {
    printf("struct A size = %zu\n", sizeof(struct A));
    printf("A.x offset = %zu\n", offsetof(struct A, x));
    printf("A.y offset = %zu\n", offsetof(struct A, y));
    printf("A.z offset = %zu\n", offsetof(struct A, z));
    
    printf("struct B size = %zu\n", sizeof(struct B));
    return 0;
}
```

```text
struct A size = 12
A.x offset = 0
A.y offset = 4
A.z offset = 8
struct B size = 8
```

---

### Exercise 5: Bitwise Masking Operations

**Problem:** Given an 8-bit unsigned char `flags`, write code blocks to:
1. Set the 3rd bit (counting from 0, value 8).
2. Clear the 3rd bit.
3. Toggle the 3rd bit.
4. Check if the 3rd bit is set.

**Solution:**
1. **Set bit:** Use bitwise OR (`|`) with a mask: `flags |= (1 << 3);`
2. **Clear bit:** Use bitwise AND (`&`) with the one's complement of the mask: `flags &= ~(1 << 3);`
3. **Toggle bit:** Use bitwise XOR (`^`) with the mask: `flags ^= (1 << 3);`
4. **Check bit:** Use bitwise AND and test for non-zero: `if (flags & (1 << 3)) { ... }`

```c
#include <stdio.h>

int main(void) {
    unsigned char flags = 0; // 00000000
    flags |= (1 << 3);       // 00001000
    printf("After set: %d\n", flags);
    
    flags ^= (1 << 3);       // 00000000
    printf("After toggle: %d\n", flags);
    return 0;
}
```

```text
After set: 8
After toggle: 0
```

---

### Exercise 6: Struct Packing with Pragmas

**Problem:** How do you force the compiler to eliminate padding bytes inside a struct? Write an example code snippet.

**Solution:**
1. Standard packing behaves according to target platform ABIs.
2. Compilers (GCC/Clang) support `#pragma pack(push, 1)` or `__attribute__((packed))` to disable padding, forcing a 1-byte alignment.

```c
#include <stdio.h>

#pragma pack(push, 1)
struct PackedStruct {
    char x;
    int y;
    char z;
};
#pragma pack(pop)

int main(void) {
    printf("Packed size = %zu\n", sizeof(struct PackedStruct));
    return 0;
}
```

```text
Packed size = 6
```

---

### Exercise 7: Bit-fields Layout

**Problem:** Define a struct representing a network packet header with a 4-bit version field, a 4-bit header length field, and an 8-bit service type. What is its size?

**Solution:**

```c
#include <stdio.h>

struct PacketHeader {
    unsigned char version : 4;
    unsigned char ihl : 4;
    unsigned char tos : 8;
};

int main(void) {
    printf("Size = %zu\n", sizeof(struct PacketHeader));
    return 0;
}
```

```text
Size = 2
```

1. The first two members (`version` and `ihl`) occupy $4$ bits each, totaling $8$ bits ($1$ byte).
2. The third member (`tos`) occupies $8$ bits ($1$ byte).
3. The fields fit into two bytes. The total size is $2$ bytes.

---

### Exercise 8: Swap Variables with Bitwise XOR

**Problem:** Implement an in-place swap function using the bitwise XOR operator without using auxiliary temporary variables.

**Solution:**
1. The XOR operation has the mathematical properties:
   - $a \wedge a = 0$
   - $a \wedge 0 = a$
   - $a \wedge b = b \wedge a$
2. Applying XOR three times swaps the values:
   - $a_{\text{new}} = a \wedge b$
   - $b_{\text{new}} = b \wedge a_{\text{new}} = b \wedge (a \wedge b) = a$
   - $a_{\text{final}} = a_{\text{new}} \wedge b_{\text{new}} = (a \wedge b) \wedge a = b$

```c
#include <stdio.h>

void xor_swap(int *x, int *y) {
    if (x != y) { // Check to prevent self-erasure if pointing to the same address
        *x = *x ^ *y;
        *y = *x ^ *y;
        *x = *x ^ *y;
    }
}

int main(void) {
    int a = 10, b = 20;
    xor_swap(&a, &b);
    printf("a=%d b=%d\n", a, b);
    return 0;
}
```

```text
a=20 b=10
```

---

## Common Errors and Gotchas

### 1. Struct Member Offset Assumptions
* **Cause:** Hardcoding struct member offsets assuming no padding (e.g. assuming the second member is at address `base + 1` for a `char` first member). This causes crashes and data corruption on platforms that align variables differently.
* **Resolution:** Always use the `offsetof` macro from `<stddef.h>` to retrieve the compile-time calculated offsets of struct fields.

### 2. XOR Swap with Same Pointer (Self-Erasure)
* **Cause:** Invoking `xor_swap(&x, &x)` on the same memory address. The first operation computes `*x = *x ^ *x = 0`. The subsequent steps propagate this zero, erasing the variable.
* **Resolution:** Check if the memory addresses are identical before performing the bitwise swap operations: `if (x != y)`.

### 3. Bitwise Shift Overflow (Signed Right Shifts)
* **Cause:** Right-shifting a negative signed integer value (e.g., `val >> 2` where `val` is signed). The C standard allows the compiler to perform either an arithmetic shift (filling with the sign bit) or a logical shift (filling with zeroes), leading to non-portable behavior.
* **Resolution:** Always cast variables to `unsigned` types before performing shift operations if predictable logical shifts are expected.

---

## Exam Tip: Struct Padding Calculation Traps

**Struct Reordering for Size Optimization:**
Exams frequently ask students to calculate struct sizes or rearrange their fields to minimize memory usage.
- **Rule of thumb:** Place members in decreasing order of their alignment size (largest first, e.g. `double` or `long`, then `int`, then `short`, then `char`).
- **Example:**
  ```c
  // Bad Layout: Size = 24 bytes
  struct Bad { char c1; double d; char c2; int i; };
  
  // Optimized Layout: Size = 16 bytes
  struct Good { double d; int i; char c1; char c2; };
  ```

**Struct Returning Mechanics:**
- Remember that C functions can return structures directly. Under the hood, this is implemented by passing a pointer to a temporary space on the caller's stack frame, where the return value is copied.
- You **cannot** return a union or structure containing a pointer to a local stack variable, as the pointer becomes dangling immediately after the function return.
