# Practice Exam 01: Object-Oriented Programming

**Course:** Object-Oriented Programming (Course Code 302)  
**Format:** Comprehensive Practice Examination with Full Solutions  
**Total Points:** 100 points  
**Time Allowed:** 120 minutes  

---

## Part I: Examination Questions

### Section A: Core OOP Theory & C++ Mechanics (25 Points)

1. *(5 Points)* Define Encapsulation and Data Hiding. How do access specifiers in C++ enforce these principles?
2. *(5 Points)* Explain the phenomenon of **Object Slicing** in C++. Provide a code example illustrating when slicing occurs, and state how to prevent it.
3. *(5 Points)* Why is declaring a `virtual` destructor mandatory in any base class intended for polymorphic use? What undefined behavior occurs if it is omitted?
4. *(5 Points)* State the **Rule of Five** in modern C++. Explain why the addition of move semantics in C++11 expanded the classic Rule of Three.
5. *(5 Points)* Explain the difference between compile-time (static) binding and runtime (dynamic) binding. Give a C++ code snippet demonstrating both on the same class hierarchy.

---

### Section B: Virtual Method Tables (Vtables) & Memory Layout (25 Points)

Consider the following class definitions:

```cpp
class Alpha {
public:
    int a;
    Alpha() : a(1) {}
    virtual ~Alpha() = default;
    virtual void func1() { std::cout << "Alpha::func1\n"; }
    virtual void func2() { std::cout << "Alpha::func2\n"; }
};

class Beta : public Alpha {
public:
    int b;
    Beta() : b(2) {}
    void func1() override { std::cout << "Beta::func1\n"; }
    virtual void func3() { std::cout << "Beta::func3\n"; }
};
```

1. *(15 Points)* Diagram the physical memory layout of an instance of class `Beta` on a 64-bit architecture (assuming 8-byte pointer alignment and standard struct padding). Include the position of the `vptr`, inherited members, and derived members.
2. *(10 Points)* Diagram the Virtual Method Tables (vtables) for both `Alpha` and `Beta`, showing which function pointer occupies each vtable index. Trace the execution steps when running:
   ```cpp
   Alpha* ptr = new Beta();
   ptr->func1();
   ```

---

### Section C: RAII and Operator Overloading (25 Points)

Design a class `DynamicBuffer` that encapsulates a dynamic character buffer of arbitrary length:

```cpp
class DynamicBuffer {
private:
    char* buffer_;
    size_t length_;
public:
    // Implementation required
};
```

1. *(15 Points)* Provide complete implementations for:
   - Parameterized constructor `DynamicBuffer(const char* str)`.
   - Destructor `~DynamicBuffer()`.
   - Copy constructor `DynamicBuffer(const DynamicBuffer& other)`.
   - Move constructor `DynamicBuffer(DynamicBuffer&& other) noexcept`.
   - Copy assignment operator using the **copy-and-swap** idiom.
2. *(10 Points)* Overload the stream insertion operator (`operator<<`) and equality comparison operator (`operator==`) as non-member friend functions.

---

### Section D: Smart Pointers and Generic Programming (25 Points)

1. *(15 Points)* Compare `std::unique_ptr`, `std::shared_ptr`, and `std::weak_ptr` with respect to ownership semantics, runtime memory overhead, and thread safety of reference counts.
2. *(10 Points)* Write a templated C++ function `filterElements` that accepts a `const std::vector<T>&` and a unary predicate function `Predicate pred`, returning a new `std::vector<T>` containing all elements satisfying the predicate.

---

## Part II: Complete Solutions and Grading Rubric

### Section A Solutions

1. **Encapsulation (5 Points):**
   - Encapsulation binds attributes and methods within a unified class structure. Data hiding restricts direct access to internal state using `private` or `protected` specifiers, allowing access only through validated public member functions (`getters`/`setters`). *(5 pts)*

2. **Object Slicing (5 Points):**
   - Occurs when a derived class instance is assigned to a base class instance by value:
     ```cpp
     Derived d;
     Base b = d; // Sliced!
     ```
   - The compiler copies only the base portion of `d` into `b`, discarding all derived member variables and resetting the vptr to `Base`'s vtable.
   - *Prevention:* Pass polymorphic objects by reference (`const Base&`) or smart pointer (`std::unique_ptr<Base>`). *(5 pts)*

3. **Virtual Destructors (5 Points):**
   - If a derived object deleted via a base pointer lacks a virtual destructor (`delete base_ptr;`), only the base destructor is invoked. The derived destructor never runs, leaking dynamic memory and resources held by the derived class. Declaring `virtual ~Base() = default;` ensures proper virtual destructor chaining. *(5 pts)*

4. **Rule of Five (5 Points):**
   - Destructor, Copy Constructor, Copy Assignment, Move Constructor, Move Assignment.
   - C++11 introduced rvalue references and move semantics, allowing resources to be efficiently moved from temporary objects rather than copied. If a class requires custom resource cleanup, it must implement both copy and move operations to avoid inefficient deep copies of temporary objects. *(5 pts)*

5. **Binding (5 Points):**
   - *Static Binding:* Resolved at compile time based on variable pointer type: `ptr->nonVirtualMethod()`.
   - *Dynamic Binding:* Resolved at runtime via vtable lookup based on actual heap object type: `ptr->virtualMethod()`. *(5 pts)*

---

### Section B Solutions

1. **Memory Layout of `Beta` (64-bit architecture) (15 Points):**
   - Offset `0x00 - 0x07` (8 bytes): `vptr` (points to `Beta`'s vtable)
   - Offset `0x08 - 0x0B` (4 bytes): `Alpha::a` (int = 4 bytes)
   - Offset `0x0C - 0x0F` (4 bytes): `Beta::b` (int = 4 bytes)
   - Total Object Size: 16 bytes (perfectly 8-byte aligned, 0 bytes padding). *(15 pts)*

2. **Vtable Structure & Trace (10 Points):**
   - `Alpha` vtable:
     - Slot 0: `&Alpha::~Alpha()`
     - Slot 1: `&Alpha::func1()`
     - Slot 2: `&Alpha::func2()`
   - `Beta` vtable:
     - Slot 0: `&Beta::~Beta()`
     - Slot 1: `&Beta::func1()` (Overridden!)
     - Slot 2: `&Alpha::func2()` (Inherited)
     - Slot 3: `&Beta::func3()` (New virtual method)
   - **Trace:**
     1. `ptr->func1()` initiates dynamic dispatch.
     2. Program dereferences `ptr` to read `Beta`'s `vptr`.
     3. It looks up Slot 1 in `Beta`'s vtable.
     4. Calls `&Beta::func1()`, printing `"Beta::func1\n"`. *(10 pts)*

---

### Section C Solutions

1. **`DynamicBuffer` Implementation (15 Points):**
```cpp
#include <cstring>
#include <utility>

class DynamicBuffer {
private:
    char* buffer_;
    size_t length_;

public:
    DynamicBuffer(const char* str = "") {
        length_ = std::strlen(str);
        buffer_ = new char[length_ + 1];
        std::memcpy(buffer_, str, length_ + 1);
    }

    ~DynamicBuffer() {
        delete[] buffer_;
    }

    DynamicBuffer(const DynamicBuffer& other) : length_(other.length_) {
        buffer_ = new char[length_ + 1];
        std::memcpy(buffer_, other.buffer_, length_ + 1);
    }

    DynamicBuffer(DynamicBuffer&& other) noexcept 
        : buffer_(other.buffer_), length_(other.length_) {
        other.buffer_ = nullptr;
        other.length_ = 0;
    }

    friend void swap(DynamicBuffer& first, DynamicBuffer& second) noexcept {
        using std::swap;
        swap(first.buffer_, second.buffer_);
        swap(first.length_, second.length_);
    }

    DynamicBuffer& operator=(DynamicBuffer other) noexcept {
        swap(*this, other);
        return *this;
    }
```
   *(15 pts)*

2. **Operators (10 Points):**
```cpp
    friend std::ostream& operator<<(std::ostream& os, const DynamicBuffer& buf) {
        if (buf.buffer_) os << buf.buffer_;
        return os;
    }

    friend bool operator==(const DynamicBuffer& lhs, const DynamicBuffer& rhs) {
        if (lhs.length_ != rhs.length_) return false;
        return std::strcmp(lhs.buffer_, rhs.buffer_) == 0;
    }
};
```
   *(10 pts)*

---

### Section D Solutions

1. **Smart Pointer Comparison (15 Points):**
   - `std::unique_ptr`: Exclusive ownership, single owner, zero memory overhead (same as raw pointer), non-copyable, movable.
   - `std::shared_ptr`: Shared ownership, reference-counted, overhead of control block (contains strong count, weak count, custom deleter), atomic ref-count increment/decrements are thread-safe.
   - `std::weak_ptr`: Non-owning reference to `std::shared_ptr` managed object. Does not prevent destruction. Used to break cyclic references. Must be locked (`wp.lock()`) to access resource. *(15 pts)*

2. **Templated Filter Function (10 Points):**
```cpp
#include <vector>

template <typename T, typename Predicate>
std::vector<T> filterElements(const std::vector<T>& input, Predicate pred) {
    std::vector<T> result;
    for (const auto& item : input) {
        if (pred(item)) {
            result.push_back(item);
        }
    }
    return result;
}
```
   *(10 pts)*

