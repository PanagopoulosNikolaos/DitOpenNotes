# C — Preprocessor and Build Process

The C compilation pipeline separates preprocessing, translation, assembly, and linking into distinct stages. Using preprocessor directives, developers can define macros, manage conditional compilation, and include header files. This file covers macro expansion mechanisms, header guards, separate compilation models, build systems like `make`, and the performance implications of inline functions.

---

## 1. The Preprocessor and Macro Expansion

The preprocessor is a text-substitution tool that runs before compilation. Directives begin with `#` and are processed top-down.

### 1.1 Object-like and Function-like Macros

- **Object-like macros:** Substitute a symbolic token with a replacement text block.
- **Function-like macros:** Accept arguments and substitute them within the replacement text.

#### Syntax Reference

```text
#define <MACRO_NAME> <replacement_text>
#define <MACRO_NAME>(<param1>, <param2>) (<replacement_text_using_params>)
```

#### Preprocessor Directive Reference Table

| Directive | Parameters | Purpose | Example |
| :--- | :--- | :--- | :--- |
| `#define` | `NAME value` | Defines macro substitution | `#define PI 3.14159` |
| `#undef` | `NAME` | Cancels macro definition | `#undef PI` |
| `#include` | `<header.h>` or `"header.h"` | Copies contents of header file | `#include <stdio.h>` |
| `#ifdef` | `NAME` | Compiles block if macro is defined | `#ifdef DEBUG` |
| `#ifndef` | `NAME` | Compiles block if macro is not defined | `#ifndef HEADER_H` |

---

## 2. Conditional Compilation and Header Guards

To prevent double inclusion errors when headers import other headers, **header guards** or `#pragma once` are used to restrict parsing to a single occurrence.

### 2.1 Header Guard Syntax Reference

```c
#ifndef UNIQUE_HEADER_NAME_H
#define UNIQUE_HEADER_NAME_H

// Declarations, types, prototypes

#endif /* UNIQUE_HEADER_NAME_H */
```

### 2.2 Compilation Flags Reference Table

| Flag | Purpose | Stage | Example |
| :--- | :--- | :--- | :--- |
| `-E` | Stop after preprocessing | Preprocessing | `gcc -E main.c` |
| `-c` | Compile to object file without linking | Compilation/Assembly | `gcc -c main.c` (generates `main.o`) |
| `-o` | Specify output filename | Linking | `gcc main.o utils.o -o program` |
| `-I` | Add directory to include search path | Preprocessing | `gcc -I./include main.c` |
| `-D` | Define a macro from the command line | Preprocessing | `gcc -DDEBUG=1 main.c` |

---

## 3. Separate Compilation and Linking Model

A C program can be split across multiple source files (`.c`), which are compiled independently into object files (`.o`) and combined by the linker.

```
Source Files (.c) ──► Compiler ──► Object Files (.o) ──┐
Header Files (.h) ──┘                                   ├──► Linker ──► Executable
Libraries (.a/.so) ─────────────────────────────────────┘
```

- **Compilation stage:** Compiles `.c` files individually. The compiler only needs declarations (from `.h` files) to verify signatures and layout sizes.
- **Linking stage:** Combines object files and resolves external references (functions or variables defined in other files).

---

## 4. Build Automation with Make

`make` uses a file named `Makefile` containing dependency rules to recompile only the files that have changed, saving build time.

### 4.1 Makefile Rule Syntax Reference

```text
target: dependencies
<tab>command
```

> **[Key Insight]** The command line in a Makefile rule **must** be indented with a literal tab character, not spaces. Using spaces triggers a syntax error from `make`.

---

## 5. Inline Functions

Inline functions advise the compiler to expand the function body at the call site, eliminating call overhead (such as stack frame setup and register saving).

### 5.1 Inline Declarations

#### Syntax Reference

```text
inline <return_type> <function_name>(<parameters>) {
    <body>
}
```

Unlike macros, inline functions are type-safe, evaluate arguments exactly once, and respect block scope.

---

## Solved Exercises

### Exercise 1: Macro Operator Precedence Bug

**Problem:** Find the issue with this macro definition and fix it. Show what `SQUARE(x + 1)` expands to under the bad definition.

```c
#define SQUARE(x) x * x
```

**Solution:**
1. The preprocessor performs literal text substitution without respecting algebraic operator precedence.
2. The expression `SQUARE(x + 1)` expands to:
   ```text
   x + 1 * x + 1
   ```
3. Due to multiplication taking precedence over addition, this is evaluated as:
   $$
   x + (1 \times x) + 1 = 2x + 1
   $$
   instead of the expected $(x + 1)^2 = x^2 + 2x + 1$.
4. **Fix:** Wrap parameters and the entire macro expression in parentheses.

```c
#define SQUARE(x) ((x) * (x))
```

---

### Exercise 2: Macro Argument Side Effects

**Problem:** Explain what happens when this code is executed.

```c
#include <stdio.h>
#define MAX(a, b) ((a) > (b) ? (a) : (b))

int main(void) {
    int x = 5;
    int y = 10;
    int result = MAX(x++, y++);
    printf("result=%d x=%d y=%d\n", result, x, y);
    return 0;
}
```

**Solution:**
1. The macro call expands to:
   ```c
   int result = ((x++) > (y++) ? (x++) : (y++));
   ```
2. The condition evaluates `x++ > y++` ($5 > 10$, which is false). Both variables are incremented once during evaluation: `x` becomes $6$, and `y` becomes $11$.
3. Because the condition was false, the ternary operator evaluates the second branch: `(y++)`.
4. The value of `y++` (which is current value $11$) is assigned to `result`. `y` is then incremented a second time, becoming $12$.
5. The printed state is: `result=11 x=6 y=12`.
6. **Gotcha:** Never pass expressions with side effects (like `++` or `--` or function calls) to macros.

```text
result=11 x=6 y=12
```

---

### Exercise 3: Header Guards Prevention of Re-declaration

**Problem:** Show what compiler error occurs when a struct is defined in a header without guards and included twice in a translation unit.

**Solution:**
1. Let `data.h` contain:
   ```c
   struct Point { int x; int y; };
   ```
2. Let `main.c` contain:
   ```c
   #include "data.h"
   #include "data.h"
   ```
3. Preprocessing replaces the directives, yielding:
   ```c
   struct Point { int x; int y; };
   struct Point { int x; int y; };
   ```
4. The compiler parses the duplicate definitions and fails with a re-declaration error.
5. **Fix:** Wrap the header contents in guards.

```text
compiler error: redefinition of 'struct Point'
```

---

### Exercise 4: Macro Stringification and Token Pasting

**Problem:** Write a macro using `#` (stringification) and `##` (token pasting) to print variable names and values, and to declare dynamic variable names.

**Solution:**
1. `#` converts a macro parameter into a string literal.
2. `##` concatenates two tokens into a single token.

```c
#include <stdio.h>

#define PRINT_INT(var) printf(#var " = %d\n", var)
#define DECLARE_VAR(name, suffix) int name##_##suffix = 42

int main(void) {
    int value = 99;
    PRINT_INT(value); // Expands to: printf("value" " = %d\n", value);
    
    DECLARE_VAR(count, num); // Expands to: int count_num = 42;
    printf("count_num = %d\n", count_num);
    return 0;
}
```

```text
value = 99
count_num = 42
```

---

### Exercise 5: Separate Compilation Steps

**Problem:** Write the exact sequence of `gcc` commands to compile `main.c` and `helper.c` (which references `helper.h`) separately and link them together.

**Solution:**
1. Compile `main.c` to object file `main.o`:
   ```sh
   gcc -c main.c -o main.o
   ```
2. Compile `helper.c` to object file `helper.o`:
   ```sh
   gcc -c helper.c -o helper.o
   ```
3. Link both object files to produce the executable `program`:
   ```sh
   gcc main.o helper.o -o program
   ```

---

### Exercise 6: Basic Makefile Construction

**Problem:** Write a Makefile that compiles `main.c` and `helper.c` using the separate compilation model. Ensure clean targets are included.

**Solution:**

```make
CC = gcc
CFLAGS = -Wall -Wextra -O2

program: main.o helper.o
	$(CC) main.o helper.o -o program

main.o: main.c helper.h
	$(CC) $(CFLAGS) -c main.c

helper.o: helper.c helper.h
	$(CC) $(CFLAGS) -c helper.c

clean:
	rm -f *.o program
```

---

### Exercise 7: Macro Conditional Compile Guards

**Problem:** Write a code block that compiles debug logging statements only when the macro `DEBUG` is defined.

**Solution:**

```c
#include <stdio.h>

#ifdef DEBUG
    #define LOG(msg) printf("[LOG] %s\n", msg)
#else
    #define LOG(msg) ((void)0) /* Evaluates to no-op */
#endif

int main(void) {
    LOG("Program started");
    return 0;
}
```

If compiled with `gcc -DDEBUG main.c`, the program prints:
```text
[LOG] Program started
```
If compiled without the flag, it generates no terminal output.

---

### Exercise 8: Inline Function vs. Macro Compilation

**Problem:** State two distinct advantages of inline functions over function-like macros.

**Solution:**
1. **Type Checking:** Inline functions are checked by the compiler for argument type compatibility, preventing hard-to-detect runtime bugs caused by passing invalid types to macros.
2. **Evaluation of Arguments:** Inline functions evaluate parameters exactly once when called, avoiding multiple-evaluation bugs (such as those seen with `MAX(x++, y++)`).

---

## Common Errors and Gotchas

### 1. Makefile Space Indentation Error
* **Cause:** Indenting make commands with spaces instead of a tab character.
* **Resolution:** Configure the text editor to preserve tabs in files named `Makefile`.

### 2. Missing Macro Parentheses
* **Cause:** Defining macros like `#define ADD(a, b) a + b`. An expression like `ADD(2, 3) * 5` expands to `2 + 3 * 5` (which evaluates to $17$, not the expected $25$).
* **Resolution:** Always wrap parameters and the final expression in parentheses: `#define ADD(a, b) ((a) + (b))`.

### 3. Multiple Definition Errors at Link Time
* **Cause:** Defining variables or function bodies inside header files (e.g. `int global_val = 10;` in `helper.h`). When `helper.h` is included in multiple `.c` files, the linker complains about duplicate symbol definitions.
* **Resolution:** Place declarations in headers (`extern int global_val;`) and the actual storage definitions in corresponding `.c` implementation files.

---

## Exam Tip: Preprocessor Tracing and Parentheses

**Tracing Macro Transformations:**
Exams often test preprocessor macro substitutions by including operations with mixed precedence or operators with side effects.
- **Strategy:** Perform the textual substitution exactly as written. Do not simplify expressions during substitution. Write out the expanded string first, apply normal C operator precedence rules, and calculate the final result.

**Header Guard Importance:**
- Remember that header guards do **not** prevent a header from being processed; they prevent the *contents* from being compiled more than once in a single compilation unit. The preprocessor still opens the file, but the conditional compilation skip ensures the compiler sees only the first copy of the declarations.
