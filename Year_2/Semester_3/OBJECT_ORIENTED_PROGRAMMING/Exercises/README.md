# Object-Oriented Programming: Practical Exercises & Drills

A comprehensive collection of 60 progressive C++ programming exercises and theoretical guides designed for **Object-Oriented Programming (Course Code: 302)**.

---

## Directory Overview

All code implementations are organized in the [`Basics/`](Basics/) directory, accompanied by the theoretical reference guide [`CPP_OOP_Theory_Guide.md`](Basics/CPP_OOP_Theory_Guide.md).

```
Exercises/
├── Basics/
│   ├── CPP_OOP_Theory_Guide.md   # Deep-dive theory on class layout, vtables, RAII, and templates
│   ├── 001_exercise.cpp          # Exercise 1: Console I/O and fundamental syntax
│   ├── ...
│   ├── 045_exercise.cpp          # Exercise 45: Advanced memory management and smart pointers
│   ├── 046_exercise_general.cpp  # General Practice 1: Multi-class system integration
│   └── 060_exercise_general.cpp  # General Practice 15: Capstone object-oriented architecture
└── README.md                     # This curriculum index and compilation guide
```

---

## Thematic Exercise Modules

### Module 1: C++ Language Fundamentals (Exercises 001 - 010)
- Input/output streams (`std::cin`, `std::cout`, stream manipulators).
- Primitive types, typecasting, and scope rules.
- Arithmetic, relational, and bitwise operators.
- Control flow: conditional branching (`if-else`, `switch-case`) and iterations (`for`, `while`, `do-while`).
- Procedural function definitions, pass-by-value vs. pass-by-reference.

### Module 2: Memory, Pointers, and Arrays (Exercises 011 - 020)
- Static arrays and multidimensional buffers.
- Pointer arithmetic, dereferencing, and address-of mechanics.
- Dynamic heap memory allocation (`new`, `new[]`, `delete`, `delete[]`).
- Pointer to pointer indirection and reference parameters (`&`).
- String manipulation using `std::string` and null-terminated character buffers.

### Module 3: Standard Template Library (STL) (Exercises 021 - 030)
- Sequence containers: `std::vector`, `std::deque`, `std::list`.
- Container adapters: `std::stack`, `std::queue`, `std::priority_queue`.
- Associative containers: `std::set`, `std::map`, `std::unordered_map`.
- Iterators and traversal algorithms (`std::sort`, `std::find`, `std::transform`).

### Module 4: Core Object-Oriented Mechanics (Exercises 031 - 045)
- Class declarations, data encapsulation, and access specifiers (`public`, `protected`, `private`).
- Constructors (default, parameterized, copy, move) and member initialization lists.
- Destructors, deterministic resource cleanup, and the RAII paradigm.
- Single, multiple, and hierarchical inheritance.
- Runtime polymorphism: `virtual` methods, pure virtual interfaces, `override`, and `final`.
- Operator overloading: arithmetic, relational, subscript `[]`, and streaming `<<` / `>>`.
- Modern C++ smart pointers: `std::unique_ptr`, `std::shared_ptr`, and `std::weak_ptr`.

### Module 5: Comprehensive System Architecture Drills (Exercises 046 - 060)
End-to-end multi-class engineering problems modeling real-world domain architectures:
- **046 - 050:** Banking account management, vehicle fleet dispatch, and shape geometry pipelines.
- **051 - 055:** University student enrollment, payroll processing, and company department hierarchy.
- **056 - 060:** E-commerce shopping cart, library catalog cataloging, and custom memory pool allocators.

---

## Compilation and Memory Safety Guidelines

Compile any individual exercise using modern C++ standards (`C++17` or `C++20`) with strict warning diagnostics:

```bash
# Compilation with warnings and debugging symbols
g++ -std=c++17 -Wall -Wextra -Wpedantic -g Basics/035_exercise.cpp -o exercise_runner

# Execute program
./exercise_runner

# Memory safety and leak validation with Valgrind
valgrind --leak-check=full --show-leak-kinds=all --track-origins=yes ./exercise_runner
```

