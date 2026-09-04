# Lecture 01: C Fundamentals and Control Flow

## Context and Grounding
This lecture note establishes the foundational principles of procedural programming in C. It introduces the compilation pipeline, standard execution environments, fundamental data types, operator precedence, and deterministic control flow structures (`if-else`, `switch`, `for`, `while`, `do-while`).

---

## 1. The C Compilation Pipeline

The translation of C source text into an executable binary is executed through four distinct phases by the GNU Compiler Collection (`gcc`):

```text
Source Code (.c)
      │
      ▼  1. Preprocessing (cpp)   --> Expands #include, #define, strips comments (.i)
      │
      ▼  2. Compilation (cc1)     --> Translates C to target assembly language (.s)
      │
      ▼  3. Assembly (as)         --> Translates assembly to relocatable machine code (.o)
      │
      ▼  4. Linking (ld)          --> Merges object files and standard libraries into executable binary
Executable Binary (a.out / binary)
```

### 1.1 Canonical Minimal Program
```c
#include <stdio.h>

/**
 * Serves as the standard entry point for the program.
 *
 * Args:
 *   None.
 *
 * Returns:
 *   int: Exit status code 0 indicating successful execution.
 */
int main(void) {
    // Outputs the canonical greeting string terminated by a newline.
    printf("Hello, World!\n");
    return 0;
}
```

---

## 2. Variables, Memory Representation, and Data Types

In C, variables are typed memory locations whose storage size and interpretation are determined at compile time.

### 2.1 Primitive Data Types on 64-bit Architecture
| Type Specifier | Size (Bytes) | Format Specifier | Typical Range |
|:---|:---:|:---:|:---|
| `char` | 1 | `%c` / `%d` | $-128$ to $127$ (or $0$ to $255$) |
| `short` | 2 | `%hd` | $-32,768$ to $32,767$ |
| `int` | 4 | `%d` or `%i` | $-2,147,483,648$ to $2,147,483,647$ |
| `unsigned int` | 4 | `%u` | $0$ to $4,294,967,295$ |
| `long` | 8 | `%ld` | $-2^{63}$ to $2^{63}-1$ |
| `float` | 4 | `%f` | $\pm 3.4 \times 10^{38}$ (7 decimal digits) |
| `double` | 8 | `%lf` | $\pm 1.7 \times 10^{308}$ (15-17 decimal digits) |

### 2.2 Constant Qualifiers and Identifiers
* `const`: Enforces read-only memory semantics; any mutation attempt triggers compiler diagnostic errors.
* Identifier naming: PascalCase for structs, camelCase for functions, and snake_case for variables.

---

## 3. Operators and Precedence

1. **Arithmetic Operators**: `+`, `-`, `*`, `/`, `%` (integer modulus; only defined for integral types).
2. **Relational and Equality Operators**: `<`, `<=`, `>`, `>=`, `==`, `!=`.
3. **Logical Operators**: `&&` (short-circuit AND), `||` (short-circuit OR), `!` (NOT).
4. **Bitwise Operators**: `&`, `|`, `^` (XOR), `~` (one's complement), `<<`, `>>`.
5. **Assignment Operators**: `=`, `+=`, `-=`, `*=`, `/=`, `%=`.

---

## 4. Control Flow Structures

### 4.1 Conditional Branching (`if`, `else if`, `else`)
Evaluates scalar expressions where $0$ corresponds to false and any non-zero value evaluates to true.

```c
int score = 85;

if (score >= 90) {
    printf("Grade: A\n");
} else if (score >= 75) {
    printf("Grade: B\n");
} else {
    printf("Grade: C\n");
}
```

### 4.2 Multi-Way Branching (`switch`)
Maps an integral expression directly to jump-table target labels:

```c
char grade = 'B';

switch (grade) {
    case 'A':
        printf("Distinction\n");
        break;
    case 'B':
        printf("Good standing\n");
        break;
    case 'C':
        printf("Passing\n");
        break;
    default:
        printf("Unrecognized grade\n");
        break;
}
```

### 4.3 Iterative Loops
1. **`for` loop**: Pre-tested iteration loop parameterized by initialization, termination condition, and increment expression.
2. **`while` loop**: Pre-tested entry loop; condition is verified before each iteration.
3. **`do-while` loop**: Post-tested exit loop; the body executes at least once regardless of the condition.

```c
// Pre-tested counter loop
for (int i = 0; i < 5; ++i) {
    printf("Iteration %d\n", i);
}

// Post-tested loop validating user input
int input_value = 0;
do {
    printf("Enter positive integer: ");
    if (scanf("%d", &input_value) != 1) {
        // Discard invalid input stream contents
        while (getchar() != '\n');
    }
} while (input_value <= 0);
```

---

## 5. Summary & Best Practices
* Always initialize variables prior to read access to prevent undefined behavior from indeterminate memory.
* Enable compiler warnings (`gcc -Wall -Wextra -std=c11 -pedantic`) to detect implicit conversions and unhandled switch branches.
* Verify return values of input functions like `scanf` to prevent format injection and state corruption.

