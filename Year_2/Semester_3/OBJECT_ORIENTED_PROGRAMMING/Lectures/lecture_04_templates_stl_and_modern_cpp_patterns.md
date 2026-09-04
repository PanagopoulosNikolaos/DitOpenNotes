# Lecture 04: Templates, the STL, and Modern C++ Patterns

This lecture examines generic programming in C++ via templates, the architecture of the Standard Template Library (STL), memory ownership through smart pointers, and classic design patterns.

---

## 1. Generic Programming and Templates

Templates instruct the compiler to generate specialized functions or classes across varying data types at compile time.

### 1.1 Function Templates
```cpp
template <typename T>
const T& getMax(const T& a, const T& b) {
    return (a > b) ? a : b;
}
```

### 1.2 Class Templates with Template Specialization
```cpp
template <typename T, size_t N>
class StaticBuffer {
private:
    T buffer_[N];
public:
    size_t size() const noexcept { return N; }
    T& operator[](size_t index) { return buffer_[index]; }
};
```

---

## 2. Standard Template Library (STL) Architecture

The STL decouples data structures from algorithmic operations via iterators:

```
[ Container: std::vector<int> ] <---> [ RandomAccessIterator ] <---> [ Algorithm: std::sort() ]
```

### Container Classifications:
1. **Sequence Containers:** `std::vector`, `std::deque`, `std::list`.
2. **Associative Containers (Red-Black Trees):** `std::set`, `std::map`, `std::multiset`.
3. **Unordered Associative Containers (Hash Tables):** `std::unordered_set`, `std::unordered_map`.
4. **Container Adapters:** `std::stack`, `std::queue`, `std::priority_queue`.

---

## 3. Smart Pointers and Modern Ownership Semantics

Raw pointers do not express ownership. Modern C++ standardizes three smart pointer types in `<memory>`:

| Smart Pointer | Ownership Model | Reference Overhead | Copyable? | Movable? | Use Case |
|---|---|---|---|---|---|
| `std::unique_ptr<T>` | Exclusive (single owner) | Zero overhead | No | Yes | Default choice for heap allocation |
| `std::shared_ptr<T>` | Shared (reference-counted) | Control block + count | Yes | Yes | Resource shared across multiple consumers |
| `std::weak_ptr<T>` | Non-owning observer | Weak count in control block | Yes | Yes | Breaks circular reference cycles |

### 3.1 Recommended Creation Idioms:
Always prefer `std::make_unique` and `std::make_shared`:
```cpp
auto ptr1 = std::make_unique<Widget>("Config");
auto ptr2 = std::make_shared<Widget>("Config");
```
*Benefits:* Avoids explicit `new`, guarantees exception safety, and `std::make_shared` allocates the control block and object in a single contiguous memory block.

---

## 4. Classic Object-Oriented Design Patterns

### 4.1 Strategy Pattern
Enables swapping algorithmic behaviors at runtime by encapsulating strategies behind an abstract interface:

```cpp
#include <memory>
#include <vector>

class SortStrategy {
public:
    virtual ~SortStrategy() = default;
    virtual void sort(std::vector<int>& dataset) = 0;
};

class SorterContext {
private:
    std::unique_ptr<SortStrategy> strategy_;

public:
    void setStrategy(std::unique_ptr<SortStrategy> new_strat) {
        strategy_ = std::move(new_strat);
    }

    void executeSort(std::vector<int>& data) {
        if (strategy_) strategy_->sort(data);
    }
};
```

### 4.2 Factory Method Pattern
Defines an interface for creating objects, letting subclasses decide which concrete class to instantiate.

### 4.3 Thread-Safe Meyers Singleton
```cpp
class ConfigurationManager {
public:
    static ConfigurationManager& getInstance() {
        static ConfigurationManager instance; // Guaranteed thread-safe in C++11
        return instance;
    }

    ConfigurationManager(const ConfigurationManager&) = delete;
    ConfigurationManager& operator=(const ConfigurationManager&) = delete;

private:
    ConfigurationManager() = default;
};
```

---

## 5. Summary

- Templates provide compile-time polymorphism with zero runtime overhead.
- The STL architecture separates containers and algorithms using standardized iterators.
- Smart pointers (`std::unique_ptr`, `std::shared_ptr`) eliminate raw pointer leaks and dangling references.
- Design patterns establish proven architectural structures for maintainable software.

