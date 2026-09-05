# Topic 1: C Programming Fundamentals

## 1. What Is C?

C is a general-purpose, compiled, procedural programming language created by Dennis Ritchie at Bell Labs in the early 1970s. It was originally designed to write the UNIX operating system, and it remains the foundation of operating systems, embedded systems, compilers, and countless libraries.

Key characteristics:

* **Compiled:** Source code is translated directly into machine instructions before execution, producing fast programs.
* **Low-level access:** C exposes memory through pointers and allows explicit memory management.
* **Small standard library:** The language core is minimal; functionality is provided by libraries such as `stdio.h` and `stdlib.h`.
* **Portable:** The same source can be compiled for many architectures with few changes.
* **Static typing:** Every variable has a fixed type known at compile time.

---

## 2. The Compilation Pipeline

Compiling a C program goes through four stages:

```
source.c → [Preprocessor] → [Compiler] → [Assembler] → [Linker] → executable
```

| Stage | Tool (GCC) | What Happens |
|-------|-----------|--------------|
| Preprocessing | `gcc -E` | Expands `#include` directives, replaces macros, strips comments |
| Compilation | `gcc -S` | Translates preprocessed C into assembly code |
| Assembly | `gcc -c` | Assembles code into an object file (`.o`) |
| Linking | `gcc` | Combines object files and libraries into a final executable |

Useful GCC commands:

```bash
gcc main.c -o main          # Compile and link in one step
gcc -Wall -Wextra main.c    # Enable most warnings (always do this)
gcc -g main.c -o main       # Include debug symbols for gdb
gcc -std=c99 main.c         # Enforce a specific C standard
```

---

## 3. Structure of a Minimal Program

```c
#include <stdio.h>   // Preprocessor directive: include standard I/O declarations

int main(void)       // Program entry point; execution starts here
{
    printf("Hello, world!\n");
    return 0;        // 0 signals successful execution to the operating system
}
```

Breaking this down:

* `#include <stdio.h>` — a *preprocessor directive* that pastes in declarations for input/output functions such as `printf`.
* `int main(void)` — every C program must have exactly one `main` function. It returns an `int` status code to the operating system.
* `{ ... }` — braces delimit the function body (a *block*).
* `printf("Hello, world!\n");` — a *statement*; every statement ends with a semicolon.
* `return 0;` — terminates `main` and reports success (`EXIT_SUCCESS`).

Every executable statement must live inside a function; there is no code "floating" at file scope.

---

## 4. Comments

C supports two comment styles:

```c
/* This is a multi-line
   block comment. */

// This is a single-line comment (C99 and later).
```

Comments are removed by the preprocessor and have no effect on the compiled program. Use them to explain *why* code exists, not to restate what it does.

---

## 5. Common First Mistakes

| Mistake | Symptom |
|---------|---------|
| Missing semicolon | Compiler error at the next line |
| Missing `#include <stdio.h>` | Warning/error: implicit declaration of `printf` |
| Forgetting `\n` in output | Output appears glued together or is not flushed |
| Wrong return type on `main` | Non-portable exit status |
| Not checking compiler warnings | Hidden bugs such as uninitialized variables |

---

## 6. Summary

* C source files are compiled through preprocessing, compilation, assembly, and linking.
* A program's entry point is `main`, which returns an integer status code.
* Statements end with semicolons; braces group statements into blocks.
* Always compile with warnings enabled (`-Wall -Wextra`).
