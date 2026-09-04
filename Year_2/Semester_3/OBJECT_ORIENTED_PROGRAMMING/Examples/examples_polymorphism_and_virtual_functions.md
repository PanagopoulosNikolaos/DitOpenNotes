# Worked Examples: Polymorphism and Virtual Method Tables Walkthrough

This document analyzes the runtime polymorphism implementation in [`examples_polymorphism_and_virtual_functions.cpp`](file:///home/ice/Documents/CodeHub/GitHub-Projects/Public/DitOpenNotes/Year_2/Semester_3/OBJECT_ORIENTED_PROGRAMMING/Examples/examples_polymorphism_and_virtual_functions.cpp).

---

## 1. Technical Walkthrough

### 1.1 Pure Virtual Interfaces
`Shape` defines pure virtual methods `computeArea()` and `computePerimeter()`, making it an Abstract Base Class. It enforces an implementation contract across derived classes while prohibiting direct instantiation:
```cpp
// Compilation Error: cannot declare variable 's' to be of abstract type 'Shape'
// Shape s("Generic");
```

### 1.2 Polymorphic Container Management
By wrapping concrete derived instances inside `std::unique_ptr<Shape>`, the heterogeneous collection `std::vector<std::unique_ptr<Shape>>` manages diverse subclasses uniformly while guaranteeing automatic memory reclamation via `virtual ~Shape() = default;`.

---

## 2. Compilation and Execution

Compile with C++17 support:
```bash
g++ -std=c++17 -Wall -Wextra examples_polymorphism_and_virtual_functions.cpp -o shape_runner
./shape_runner
```

### Expected Output:
```text
--- Polymorphic Shape Evaluation ---
Shape: Rectangle | Area: 20 | Perimeter: 18
Shape: Circle | Area: 28.2743 | Perimeter: 18.8496
```

