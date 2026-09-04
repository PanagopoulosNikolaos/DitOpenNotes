# Lecture 03: Operator Overloading and RAII Resource Management

This lecture explores operator overloading techniques, the Resource Acquisition Is Initialization (RAII) idiom, the Rule of Three/Five/Zero, and exception-safe resource management via the copy-and-swap idiom.

---

## 1. Operator Overloading Fundamentals

Operator overloading enables user-defined types to integrate with C++'s standard algebraic syntax.

### 1.1 Member vs. Non-Member (Friend) Operators
- **Member Operators:** The left-hand operand is implicitly `*this`. Mandatory for assignment (`=`), subscript (`[]`), function call (`()`), and member selection (`->`).
- **Non-Member (Friend) Operators:** Both operands are passed explicitly. Essential for symmetric binary operations (e.g., `a + b` allowing implicit type conversions on either operand) and stream operators (`std::ostream& operator<<(std::ostream&, const Complex&)`).

```cpp
#include <iostream>

class Complex {
private:
    double real_;
    double imag_;

public:
    Complex(double r = 0.0, double i = 0.0) : real_(r), imag_(i) {}

    // Compound assignment as member
    Complex& operator+=(const Complex& rhs) {
        real_ += rhs.real_;
        imag_ += rhs.imag_;
        return *this;
    }

    // Binary addition implemented in terms of +=
    friend Complex operator+(Complex lhs, const Complex& rhs) {
        lhs += rhs;
        return lhs;
    }

    // Stream output operator
    friend std::ostream& operator<<(std::ostream& os, const Complex& c) {
        os << c.real_ << (c.imag_ >= 0 ? " + " : " - ") << std::abs(c.imag_) << "i";
        return os;
    }
};
```

---

## 2. Resource Acquisition Is Initialization (RAII)

RAII binds the lifecycle of a resource (heap memory, file handles, mutex locks, network sockets) to the lifetime of an automatic object:
1. **Acquisition:** Resource is acquired in the object's constructor.
2. **Release:** Resource is released in the object's destructor.
When an object goes out of scope (via return, break, or stack unwinding due to an exception), the destructor runs deterministically, preventing leaks.

---

## 3. The Rules of Resource Management

### 3.1 The Rule of Three (C++98)
If a class requires an explicit destructor, it almost certainly requires a custom copy constructor and copy assignment operator to prevent double-free errors:
1. Destructor `~MyClass()`
2. Copy Constructor `MyClass(const MyClass&)`
3. Copy Assignment Operator `MyClass& operator=(const MyClass&)`

### 3.2 The Rule of Five (Modern C++11)
To support move semantics, five special member functions must be defined or defaulted:
1. Destructor
2. Copy Constructor
3. Copy Assignment Operator
4. Move Constructor `MyClass(MyClass&&) noexcept`
5. Move Assignment Operator `MyClass& operator=(MyClass&&) noexcept`

### 3.3 The Rule of Zero
Classes should avoid managing raw resources directly. By composing classes exclusively from RAII types (such as `std::string`, `std::vector`, `std::unique_ptr`), the compiler-generated member functions will be correct without writing any of the five custom methods.

---

## 4. The Copy-and-Swap Idiom

Provides strong exception safety for assignment operators by reusing the copy constructor and non-throwing `swap`:

```cpp
class DynamicArray {
private:
    size_t size_;
    int* data_;

public:
    DynamicArray(size_t size) : size_(size), data_(new int[size]()) {}
    ~DynamicArray() { delete[] data_; }

    // Copy Constructor (Deep copy)
    DynamicArray(const DynamicArray& other) 
        : size_(other.size_), data_(new int[other.size_]) {
        std::copy(other.data_, other.data_ + size_, data_);
    }

    // Move Constructor
    DynamicArray(DynamicArray&& other) noexcept 
        : size_(other.size_), data_(other.data_) {
        other.size_ = 0;
        other.data_ = nullptr;
    }

    friend void swap(DynamicArray& first, DynamicArray& second) noexcept {
        using std::swap;
        swap(first.size_, second.size_);
        swap(first.data_, second.data_);
    }

    // Unified assignment operator (Pass by value handles both copy and move!)
    DynamicArray& operator=(DynamicArray other) noexcept {
        swap(*this, other);
        return *this;
    }
};
```

---

## 5. Summary

- Operator overloading extends intuitive mathematical notation to custom abstractions.
- Stream operators (`<<`, `>>`) must be implemented as non-member functions.
- RAII eliminates manual cleanup and guarantees resource reclamation under exceptions.
- The copy-and-swap idiom implements strong exception-safe assignment in clean, minimal code.

