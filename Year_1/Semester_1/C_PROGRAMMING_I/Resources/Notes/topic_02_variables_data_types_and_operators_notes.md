# Topic 2: Variables, Data Types, and Operators

## 1. Variables and Declaration

A variable is a named storage location with a fixed type. In C, every variable must be **declared** before use:

```c
int age;              // Declaration
age = 25;             // Assignment

int count = 10;       // Declaration with initialization
double price = 9.99;
char grade = 'A';
```

Naming rules: identifiers may contain letters, digits, and underscores, must not start with a digit, and are case-sensitive (`Total` and `total` are different variables).

---

## 2. Basic Data Types

| Type | Typical Size | Purpose | Range (typical) |
|------|--------------|---------|-----------------|
| `char` | 1 byte | Single character / small integer | -128 to 127 (or 0 to 255) |
| `int` | 4 bytes | Whole numbers | about ±2.1 billion |
| `float` | 4 bytes | Single-precision real numbers | ~7 significant digits |
| `double` | 8 bytes | Double-precision real numbers | ~15 significant digits |

Type modifiers adjust size and signedness: `short`, `long`, `long long`, `unsigned`, `signed`.

```c
unsigned int nonNegative = 4000000000u;
long bigNumber = 9000000000L;
short smallValue = 100;
```

The `sizeof` operator reports the size of a type or variable in bytes:

```c
printf("int is %zu bytes\n", sizeof(int));
```

Exact-width types from `<stdint.h>` are preferred when the size matters: `int8_t`, `int32_t`, `uint64_t`, etc.

---

## 3. Constants and Literals

```c
const double PI = 3.14159;        // Read-only variable
#define MAX_USERS 100             // Preprocessor constant (no type)

int decimal   = 42;
int octal     = 052;              // Leading 0
int hex       = 0x2A;             // 0x prefix
char letter   = 'A';              // Single quotes = character
char *text    = "Hello";          // Double quotes = string literal
```

Escape sequences: `\n` (newline), `\t` (tab), `\\` (backslash), `\"` (quote), `\0` (null character).

---

## 4. Type Conversion and Casting

**Implicit conversion (promotion):** when mixing types, C converts the "smaller" type to the larger one automatically:

```c
int i = 5;
double d = i;              // int promoted to double: 5.0
double result = 7 / 2;     // CAUTION: integer division happens first → 3.0
double correct = 7.0 / 2;  // 3.5 — one operand must be a real number
```

**Explicit casting:**

```c
double x = 3.75;
int truncated = (int)x;    // 3 — the fractional part is discarded (truncation)
```

Always be aware of the division rule: **integer / integer = integer (truncated)**.

---

## 5. Operators

### Arithmetic

| Operator | Meaning |
|----------|---------|
| `+`, `-`, `*` | Add, subtract, multiply |
| `/` | Division (integer division for integer operands) |
| `%` | Modulus (remainder, integers only) |
| `++`, `--` | Increment / decrement by 1 |

`++i` (pre-increment) uses the new value; `i++` (post-increment) uses the old value before incrementing.

### Relational and Logical

| Operator | Meaning |
|----------|---------|
| `==`, `!=` | Equal, not equal |
| `<`, `<=`, `>`, `>=` | Comparisons |
| `&&` | Logical AND (both must be true) |
| `\|\|` | Logical OR (at least one true) |
| `!` | Logical NOT |

C has no dedicated boolean type by default (C99 provides `stdbool.h` with `bool`): any non-zero value is "true", and `0` is "false".

**Short-circuit evaluation:** `&&` stops if the left side is false; `||` stops if the left side is true. This is often used for safe checks:

```c
if (p != NULL && *p > 0) { /* safe: *p only read when p is not NULL */ }
```

### Bitwise Operators

| Operator | Meaning | Example (8-bit) |
|----------|---------|-----------------|
| `&` | AND | `0b1100 & 0b1010 = 0b1000` |
| `\|` | OR | `0b1100 \| 0b1010 = 0b1110` |
| `^` | XOR | `0b1100 ^ 0b1010 = 0b0110` |
| `~` | NOT (bitwise complement) | `~0b0000 = 0b1111` |
| `<<` | Left shift | `1 << 3 = 8` |
| `>>` | Right shift | `16 >> 2 = 4` |

Common use: masks and flags.

```c
int flags = 0;
flags |= 0x01;                 // Set bit 0
if (flags & 0x01) { /* bit 0 is set */ }
flags &= ~0x01;                // Clear bit 0
```

### Assignment Operators

Compound assignments combine an operation with assignment: `+=`, `-=`, `*=`, `/=`, `%=`, `&=`, `|=`, `^=`, `<<=`, `>>=`.

```c
total += amount;   // Equivalent to total = total + amount;
```

### The Conditional (Ternary) Operator

```c
int max = (a > b) ? a : b;
```

---

## 6. Operator Precedence (Practical Subset)

From highest to lowest binding:

1. `()` `[]` `.` `->`
2. `!` `~` `++` `--` unary `-` `*` `&` (unary) `sizeof` (all right to left)
3. `*` `/` `%`
4. `+` `-`
5. `<<` `>>`
6. `<` `<=` `>` `>=`
7. `==` `!=`
8. `&` `^` `|`
9. `&&`
10. `||`
11. `?:`
12. `=` `+=` `-=` ... (right to left)

When in doubt, add parentheses — they cost nothing and prevent subtle bugs.

---

## 7. Common Pitfalls

* Using `=` (assignment) instead of `==` (comparison) inside `if`: `if (x = 5)` assigns and is always true.
* Integer overflow: `int` wraps around silently on overflow (undefined behavior for signed types in practice).
* Comparing `float` values with `==`: floating-point rounding makes exact equality unreliable; compare against a small tolerance.
* Assuming `sizeof` results across platforms: sizes are implementation-defined; use `sizeof` or `<stdint.h>` types.

---

## 8. Summary

* Every variable has a fixed, statically known type declared before use.
* Integer division truncates; mixing types triggers implicit promotion.
* Logical operators short-circuit, enabling safe guard conditions.
* Bitwise operators manipulate individual bits for flags, masks, and shifts.
