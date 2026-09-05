# Object Oriented Programming

## Course Overview
This course provides a comprehensive exploration of object-oriented analysis, software design, and modern C++ engineering (C++17). Topics include data abstraction, encapsulation, inheritance hierarchies, runtime polymorphism, virtual method tables (vtables), memory layout, resource acquisition is initialization (RAII), the Rule of Five, operator overloading, templates, generic programming, and classic Gang-of-Four (GoF) design patterns.

## Course Code
302 (OBJECT ORIENTED PROGRAMMING)

## Prerequisites
* C Programming II (Code: 204)

---

## Topics Covered
* **Core Object-Oriented Principles**: Encapsulation, information hiding, access specifiers (`public`, `protected`, `private`), constructors, destructors, and member initialization lists.
* **Inheritance & Runtime Polymorphism**: Single and multiple inheritance, virtual inheritance, the Diamond Problem, dynamic dispatch, abstract base classes, pure virtual functions, and virtual table (`vptr`/`vtable`) mechanics.
* **Resource Management and Modern C++**: RAII idiom, copy constructors, copy assignment, move semantics (rvalue references `T&&`), move constructors, move assignment, the Rule of Five, and smart pointers (`std::unique_ptr`, `std::shared_ptr`, `std::weak_ptr`).
* **Operator Overloading**: Arithmetic, stream extraction/insertion (`<<`, `>>`), relational, subscript (`[]`), and assignment operators.
* **Generic Programming and STL**: Function and class templates, template specialization, standard containers (`std::vector`, `std::list`, `std::map`), iterators, and `<algorithm>` functional utilities.
* **Software Design Patterns**: Creational (Factory, Singleton), Structural (Adapter, Decorator), and Behavioral patterns (Observer, Strategy).

---

## Learning Objectives
* Design modular, extensible, and type-safe class hierarchies modeling complex domains.
* Implement robust memory and resource management adhering strictly to RAII and the Rule of Five.
* Analyze object memory layout, object slicing, and runtime dynamic dispatch overhead.
* Apply classic object-oriented design patterns to decouple software components.

---

## Directory Structure

| Directory | Description |
|:---|:---|
| [`Lectures/`](Lectures/) | Structured theory lectures on classes, virtual dispatch, RAII, and modern C++ patterns |
| [`Exercises/`](Exercises/) | Extensive practice problem sets and 60 standalone C++ coding drills for self-study |
| [`Examples/`](Examples/) | Executable C++ implementations of abstract interfaces, polymorphic dispatch, and vtables |
| [`Assignments/`](Assignments/) | Laboratory programming projects including the Job Shop Scheduling Problem (JSSP) |
| [`Tutorials/`](Tutorials/) | Hands-on walkthroughs for GNU Make, GDB debugging, and Valgrind memory leak detection |
| [`Projects/`](Projects/) | Capstone design project: Object-Oriented Job Shop Scheduling Simulator |
| [`Exams/`](Exams/) | 100-point model practice examination with complete worked solutions and vtable memory diagrams |
| [`Resources/`](Resources/) | Curated bibliography, conceptual mindmap, and deep-dive notes on memory layout and design patterns |

---

## How to Compile and Run Examples

Compile C++ examples using strict warning flags and debugging symbols with `g++`:
```bash
g++ -std=c++17 -Wall -Wextra -Wpedantic Examples/examples_polymorphism_and_virtual_functions.cpp -o shape_runner
./shape_runner
```

To verify memory safety and ensure zero memory leaks with Valgrind:
```bash
valgrind --leak-check=full --show-leak-kinds=all ./shape_runner
```
