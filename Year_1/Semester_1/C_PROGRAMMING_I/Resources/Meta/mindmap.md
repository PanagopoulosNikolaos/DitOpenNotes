# C Programming I - Course Curriculum Mindmap

## 1. Environment & Program Structure
### 1.1 Compilation Architecture
- 1.1.1 Preprocessing (`#include`, `#define`, `#pragma`)
- 1.1.2 Compilation to Assembly
- 1.1.3 Assembler and Object Files (`.o`)
- 1.1.4 Linker and Standard C Runtime (`libc`)
### 1.2 Program Anatomy
- 1.2.1 `main()` entry signature and return semantics
- 1.2.2 Header inclusions (`<stdio.h>`, `<stdlib.h>`, `<stdbool.h>`)
- 1.2.3 Statement termination and block scoping `{ ... }`

## 2. Types, Variables & Arithmetic
### 2.1 Type System
- 2.1.1 Integer types (`char`, `short`, `int`, `long`, signed vs. unsigned)
- 2.1.2 Floating point types (`float`, `double`)
- 2.1.3 Type qualifiers (`const`, `volatile`)
- 2.1.4 Type casting (implicit promotion, explicit `(type)`)
### 2.2 Operator Mechanics
- 2.2.1 Arithmetic operators (`+`, `-`, `*`, `/`, `%`)
- 2.2.2 Relational and equality tests (`==`, `!=`, `<`, `<=`, `>`, `>=`)
- 2.2.3 Boolean logic and short-circuiting (`&&`, `||`, `!`)
- 2.2.4 Bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`)
- 2.2.5 Precedence and associativity rules

## 3. Control Flow Mechanics
### 3.1 Conditional Execution
- 3.1.1 Binary branching with `if` and `else`
- 3.1.2 Multi-branching ladders (`else if`)
- 3.1.3 Jump-table branching with `switch`, `case`, `default`, `break`
- 3.1.4 Ternary operator (`cond ? expr1 : expr2`)
### 3.2 Iteration Constructs
- 3.2.1 Counted iterations with `for`
- 3.2.2 Conditional entry loops with `while`
- 3.2.3 Guaranteed iteration with `do-while`
- 3.2.4 Loop interruption with `break` and `continue`

## 4. Functions & Stack Architecture
### 4.1 Modularity & Scoping
- 4.1.1 Prototypes vs. definitions
- 4.1.2 Stack frame anatomy and activation records
- 4.1.3 Pass-by-value argument semantics
- 4.1.4 Local vs. global variable scope and lifetime
### 4.2 Recursion
- 4.2.1 Base conditions and recursive decomposition
- 4.2.2 Stack depth and stack overflow vulnerabilities

## 5. Arrays, Strings & Pointers
### 5.1 Contiguous Storage
- 5.1.1 1D arrays, indexing, and memory offsets
- 5.1.2 2D and multi-dimensional row-major layouts
- 5.1.3 Null-terminated character arrays (`char[]`)
- 5.1.4 String library routines (`strlen`, `strcpy`, `strcmp`, `strcat`)
### 5.2 Pointer Mechanics
- 5.2.1 Address-of (`&`) and dereference (`*`) operators
- 5.2.2 Pointer arithmetic scaled by element size
- 5.2.3 Simulating pass-by-reference using pointers
- 5.2.4 Null pointer guards and boundary validation

## 6. Composite Data Types
### 6.1 Structures (`struct`)
- 6.1.1 Aggregate data member grouping
- 6.1.2 Member access (`.` vs. `->`)
- 6.1.3 Memory alignment, byte padding, and `sizeof`
- 6.1.4 Arrays of structures
### 6.2 Unions & Type Aliasing
- 6.2.1 Overlapping memory representations with `union`
- 6.2.2 Clean type abstraction using `typedef`

## 7. Stream Input/Output & File Persistence
### 7.1 Console I/O Streams
- 7.1.1 Standard streams (`stdin`, `stdout`, `stderr`)
- 7.1.2 Formatted operations (`printf`, `scanf`)
- 7.1.3 Character and line streaming (`getchar`, `putchar`, `fgets`, `puts`)
### 7.2 Secondary Storage Streams
- 7.2.1 File handle management (`FILE *`, `fopen`, `fclose`)
- 7.2.2 Formatted text files (`fprintf`, `fscanf`)
- 7.2.3 Raw binary streaming (`fread`, `fwrite`)
- 7.2.4 Stream status checking (`feof`, `ferror`)

