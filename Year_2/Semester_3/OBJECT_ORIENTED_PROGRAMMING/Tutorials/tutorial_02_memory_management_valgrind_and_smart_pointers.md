# Tutorial 02: Memory Profiling with Valgrind and Modern Smart Pointers

This tutorial demonstrates dynamic memory error detection using Valgrind Memcheck and guides the refactoring of raw manual memory management into modern RAII smart pointers.

---

## 1. Detecting Memory Defects with Valgrind

Valgrind's `memcheck` tool instruments compiled code to detect:
- Definite, indirect, and possible memory leaks.
- Out-of-bounds reads and writes on heap buffers.
- Use of uninitialized values.
- Double-free and mismatched `new[]`/`delete` operations.

### Running Memcheck:
```bash
valgrind --tool=memcheck --leak-check=full --show-leak-kinds=all --track-origins=yes ./bin/app
```

---

## 2. Refactoring Raw Pointers to `std::unique_ptr`

### Legacy Fragile Code:
```cpp
// ANTI-PATTERN: Prone to memory leaks if exception occurs before delete
void processDataset() {
    Widget* w = new Widget("SensorData");
    if (!w->validate()) {
        return; // LEAK: delete w is skipped!
    }
    w->execute();
    delete w;
}
```

### Modern Exception-Safe RAII Code:
```cpp
#include <memory>

void processDataset() {
    auto w = std::make_unique<Widget>("SensorData");
    if (!w->validate()) {
        return; // Safe: unique_ptr destructor cleans up automatically
    }
    w->execute();
}
```

---

## 3. Breaking Circular References with `std::weak_ptr`

A circular reference occurs when two objects retain owning `std::shared_ptr` instances pointing to each other, preventing their reference counts from ever reaching zero:

```cpp
#include <iostream>
#include <memory>

class NodeB; // Forward declaration

class NodeA {
public:
    std::shared_ptr<NodeB> neighbor;
    ~NodeA() { std::cout << "NodeA destroyed\n"; }
};

class NodeB {
public:
    // Using weak_ptr breaks the cycle!
    std::weak_ptr<NodeA> neighbor;
    ~NodeB() { std::cout << "NodeB destroyed\n"; }
};

int main() {
    auto a = std::make_shared<NodeA>();
    auto b = std::make_shared<NodeB>();

    a->neighbor = b;
    b->neighbor = a; // Weak reference does NOT increment owning use_count!

    return 0; // Both destructors run cleanly without memory leaks!
}
```

