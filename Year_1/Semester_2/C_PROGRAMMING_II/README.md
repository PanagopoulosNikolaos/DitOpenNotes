# C Programming II

## Course Overview
This course continues directly from C Programming I, delving deeper into systems programming, low-level memory layout, heap management, multi-level pointer indirection, binary stream serialization, abstract data types (ADTs), and algorithm complexity analysis in ANSI/ISO C.

## Course Code
204 (PROGRAMMING II)

## Prerequisites
* C Programming I (Code: 103)

---

## Topics Covered
* **Advanced Pointers and Memory Addressing**: Double pointers (`T**`), pointer arithmetic scaling rules, function pointers, and callback architectures.
* **Dynamic Storage Allocation**: Heap mechanics (`malloc`, `calloc`, `realloc`, `free`), memory leaks, dangling pointers, and heap fragmentation.
* **Binary File I/O and Persistence**: Stream management, binary record serialization, random-access positioning with `fseek`, `ftell`, and `rewind`.
* **Structured Types and Memory Alignment**: Struct packing, alignment padding, bit-fields, unions, and memory layout optimization.
* **Abstract Data Types (ADTs)**: Singly and doubly linked lists, stacks, queues, hash tables, and generic data containers using `void*`.
* **Algorithmic Complexity and Recursion**: Direct and mutual recursion, stack frame limits, divide-and-conquer algorithms, and asymptotic complexity ($O(n)$ notation).

---

## Learning Objectives
* Architect memory-safe, modular procedural codebases in C adhering to modern standards.
* Implement custom dynamic data structures with robust allocation error handling.
* Persist, index, and query structured records on disk using random-access binary streams.
* Detect and eliminate memory leaks, invalid frees, and out-of-bounds accesses using Valgrind and AddressSanitizer.
* Apply function pointers to implement higher-order operations, filters, and event dispatch tables.

---

## Directory Structure

| Directory | Description |
|:---|:---|
| [`Lectures/`](Lectures/) | Structured theory lectures, complete C reference guides, and DSA tutorials |
| [`Exercises/`](Exercises/) | Over 60 solved exercises across ctype, string manipulation, file handling, and structures |
| [`Examples/`](Examples/) | Executable C source implementations covering dynamic memory, binary I/O, linked lists, and callbacks |
| [`Assignments/`](Assignments/) | Practical laboratory assignments with formal grading rubrics |
| [`Tutorials/`](Tutorials/) | Hands-on walkthroughs for Valgrind memory debugging and binary serialization |
| [`Projects/`](Projects/) | Capstone term design project (High-Performance Student Record Database System) |
| [`Exams/`](Exams/) | Comprehensive model practice examinations with complete worked solutions |
| [`Resources/`](Resources/) | Deep-dive study notes, memory architecture guides, and curriculum mindmaps |

---

## How to Compile and Run

To compile any code sample with standard warnings and debugging symbols using the GNU C Compiler (`gcc`):

```bash
# Compile with strict warnings and debugging symbols
gcc -Wall -Wextra -std=c11 -g Examples/01_dynamic_memory_allocation.c -o dynamic_mem

# Execute the binary
./dynamic_mem

# Verify memory safety with Valgrind
valgrind --leak-check=full --show-leak-kinds=all ./dynamic_mem
```
