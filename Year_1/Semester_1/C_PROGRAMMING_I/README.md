# C Programming I

## Course Overview
This course provides a comprehensive introduction to procedural software development using the C programming language. It establishes foundational principles of algorithmic thinking, computer memory architecture, pointers, arrays, structures, and basic file input/output operations.

## Course Code
103 (PROGRAMMING I)

## Prerequisites
None (Entry-level introductory programming course)

---

## Topics Covered
* **Fundamental Syntax and Program Structure**: Compilation pipeline, preprocessor directives, data types, format specifiers.
* **Operators and Expressions**: Arithmetic, logical, relational, and bitwise operations.
* **Control Flow**: Conditional branching (`if-else`, `switch`) and iterative loops (`for`, `while`, `do-while`).
* **Modular Programming**: Function declarations, definitions, parameter passing (by value vs. reference), and scope.
* **Arrays and Strings**: One-dimensional and multi-dimensional arrays, null-terminated string manipulation, `<string.h>` and `<ctype.h>`.
* **Pointers and Memory Addressing**: Memory address spaces, the dereference (`*`) and address-of (`&`) operators, pointer arithmetic.
* **Structured Data**: User-defined structures (`struct`), unions (`union`), and type aliasing (`typedef`).
* **File I/O**: Stream management, text and binary file operations (`fopen`, `fclose`, `fprintf`, `fscanf`, `fread`, `fwrite`).

---

## Learning Objectives
* Formulate algorithmic solutions to computational problems and implement them in ANSI/ISO C.
* Understand memory organization, stack frames, and direct memory manipulation using pointers.
* Design modular codebases adhering to clean code standards and defensive programming principles.
* Debug procedural code using industry-standard tools including GCC and GDB.
* Implement structured record storage using file I/O operations.

---

## Directory Structure

| Directory | Description |
|:---|:---|
| [`Lectures/`](Lectures/) | Structured theory lectures and comprehensive C programming guide |
| [`Exercises/`](Exercises/) | Practice drills, algorithmic problem sets, and core C exercises |
| [`Examples/`](Examples/) | Twenty incremental C code implementations demonstrating syntax and semantics |
| [`Assignments/`](Assignments/) | Practical laboratory assignments with formal evaluation rubrics |
| [`Tutorials/`](Tutorials/) | Hands-on walkthroughs for GCC flags, GDB debugging, and pointer safety |
| [`Projects/`](Projects/) | Term capstone development project (Terminal Inventory System) |
| [`Exams/`](Exams/) | Practice mock examinations and archival exam paper scans |
| [`Resources/`](Resources/) | Deep-dive study notes, memory architecture guides, and curriculum mindmaps |

---

## How to Compile and Run

To compile any code sample from the course root using the GNU C Compiler (`gcc`):

```bash
# Compile with standard warnings and debugging symbols
gcc -Wall -Wextra -std=c11 -g Examples/01_hello_world.c -o hello_world

# Execute the binary
./hello_world
```

For advanced compilation and interactive debugging with GDB, refer to [`Tutorials/tutorial_01_gcc_compilation_and_gdb_debugging.md`](Tutorials/tutorial_01_gcc_compilation_and_gdb_debugging.md).
