# Deep-Dive Study Notes: Classes, Inheritance, and Runtime Polymorphism

This study guide provides an in-depth reference for C++ class semantics, object memory layout, virtual function tables, multiple inheritance resolution, and cast operators.

---

## 1. Class Memory Alignment and Padding

On modern 64-bit architectures, data members are aligned to multiples of their natural word size to maximize bus transfer efficiency.

```cpp
class Sample {
    char a;    // 1 byte
               // 3 bytes padding
    int b;     // 4 bytes
    double c;  // 8 bytes
};             // Total size = 16 bytes
```

Rearranging members from largest to smallest minimizes internal padding gaps:
```cpp
class OptimizedSample {
    double c;  // 8 bytes
    int b;     // 4 bytes
    char a;    // 1 byte
               // 3 bytes tail padding
};             // Total size = 16 bytes
```

---

## 2. The Diamond Problem in Multiple Inheritance

When a class derives from two classes that share a common base, the derived class inherits two independent copies of the top base class, creating ambiguity:

```
        Device
        /    \
    Scanner  Printer
        \    /
      Copier
```

### Resolution via Virtual Inheritance:
```cpp
class Device {
public:
    int device_id;
};

class Scanner : virtual public Device {};
class Printer : virtual public Device {};

class Copier : public Scanner, public Printer {
    // Only one shared instance of Device exists!
};
```
Virtual base classes introduce a virtual base pointer (`vptr_b`), ensuring that `Copier` contains exactly one shared subobject of `Device`.

---

## 3. C++ Explicit Cast Operators

Avoid C-style casts (`(Type)expr`). Use explicit, type-safe C++ casts:

| Cast Operator | Purpose | Runtime Check? |
|---|---|---|
| `static_cast<T>(expr)` | Compile-time conversion between related numeric or pointer types | No |
| `dynamic_cast<T>(expr)`| Safe downcasting across polymorphic hierarchies using RTTI | Yes (returns `nullptr` or throws `std::bad_cast`) |
| `const_cast<T>(expr)`  | Removes or adds `const` or `volatile` qualifiers | No |
| `reinterpret_cast<T>`  | Low-level bit reinterpretation (e.g., pointer to integer) | No |

