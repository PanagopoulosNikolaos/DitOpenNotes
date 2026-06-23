# C++ — OOP and Resource Management

*Prerequisite: cpp_1_basics_and_hardware.md — Stack/heap semantics and pass-by-reference.*
*Prerequisite: cpp_2_memory_layout.md — Contiguous memory and allocation cost.*

C++ couples object-oriented abstraction with deterministic resource management through constructors, destructors, and RAII (Resource Acquisition Is Initialization). This file covers the three standard constructor forms, destructor semantics, the Rule of Three and Rule of Five, manual `new`/`delete`, smart pointers as RAII wrappers, and operator overloading for user-defined types.

---

## 1. Constructors

### 1.1 Concept Overview

A **constructor** is a special member function invoked automatically when an object is created. Its role is to establish invariants and acquire resources. C++ provides three compiler-synthesized or user-defined forms relevant to this course: default, parameterized, and copy.

### 1.2 Syntax Reference

**Default constructor:**

```
<ClassName>()
```

**Parameterized constructor:**

```
<ClassName>(<param_list>)
```

**Copy constructor:**

```
<ClassName>(const <ClassName> &<other>)
```

**Member initializer list (preferred for initialization):**

```
<ClassName>(<params>) : <member1>(<init1>), <member2>(<init2>) { <body> }
```

### 1.3 Constructor Forms Reference

| Constructor | Signature | When Invoked |
| :--- | :--- | :--- |
| Default | `T()` or `T{}` | `T obj;` or `T obj{}` |
| Parameterized | `T(args...)` | `T obj(args...)` |
| Copy | `T(const T &other)` | `T obj2 = obj1;`, pass-by-value, return-by-value |
| Move (C++11) | `T(T &&other)` | `T obj2 = std::move(obj1);` |

```cpp
#include <iostream>
#include <string>

class Student {
public:
    std::string name;
    int grade;

    // Default constructor.
    Student() : name("unknown"), grade(0) {}

    // Parameterized constructor.
    Student(const std::string &n, int g) : name(n), grade(g) {}

    // Copy constructor.
    Student(const Student &other) : name(other.name), grade(other.grade) {
        std::cout << "Copy constructed: " << name << "\n";
    }
};

int main() {
    Student a;                        // Default.
    Student b("Alice", 95);           // Parameterized.
    Student c = b;                    // Copy.
    std::cout << c.name << " " << c.grade << "\n";
    return 0;
}
```

```text
Copy constructed: Alice
Alice 95
```

---

## 2. Destructors

### 2.1 Concept Overview

A **destructor** is invoked automatically when an object goes out of scope or is `delete`d. It releases resources acquired by the object. The destructor name is the class name prefixed with `~`.

### 2.2 Syntax Reference

```
~<ClassName>()
```

### 2.3 Behavioral Description

- Exactly one destructor per class.
- No parameters, no return type.
- Called in reverse order of construction for member subobjects.
- For stack objects, called when the enclosing scope ends.
- For heap objects, called when `delete` is invoked.

```cpp
#include <iostream>

class ScopeDemo {
public:
    ScopeDemo(const char *label) : label_(label) {
        std::cout << "Construct: " << label_ << "\n";
    }
    ~ScopeDemo() {
        std::cout << "Destruct:  " << label_ << "\n";
    }
private:
    const char *label_;
};

int main() {
    ScopeDemo a("outer");
    {
        ScopeDemo b("inner");
    }   // b destroyed here.
    return 0;
}       // a destroyed here.
```

```text
Construct: outer
Construct: inner
Destruct:  inner
Destruct:  outer
```

---

## 3. RAII — Resource Acquisition Is Initialization

### 3.1 Formal Definition

**RAII** binds the lifetime of a resource (heap memory, file handle, mutex lock, network socket) to the lifetime of a stack-allocated object. The resource is acquired in the constructor and released in the destructor. Scope exit — whether by normal return or exception — guarantees cleanup.

**RAII invariant:**

$$
\text{resource acquired in constructor} \implies \text{resource released in destructor at scope end}
$$

### 3.2 RAII vs. Manual Cleanup

| Approach | Cleanup Guarantee | Exception-Safe? |
| :--- | :--- | :--- |
| Manual `malloc`/`free` or `new`/`delete` | Programmer must call `free`/`delete` | No — early return or throw leaks |
| RAII wrapper (destructor calls `delete`) | Automatic at scope exit | Yes |

```cpp
#include <iostream>
#include <memory>

void raii_example() {
    // Resource (heap int) bound to unique_ptr's lifetime.
    std::unique_ptr<int> p = std::make_unique<int>(42);
    std::cout << *p << "\n";
    // No explicit delete — destructor of unique_ptr calls delete.
}

int main() {
    raii_example();
    return 0;
}
```

```text
42
```

> **[Key Insight]** RAII is the central design principle that distinguishes C++ resource management from C. The destructor is the cleanup hook; the compiler guarantees it runs. Smart pointers are RAII wrappers for heap memory.

---

## 4. Rule of Three and Rule of Five

### 4.1 Rule of Three (C++98)

If a class defines **any one** of the following, it should explicitly define **all three**:

1. **Destructor** (`~T()`)
2. **Copy constructor** (`T(const T &)`)
3. **Copy assignment operator** (`T &operator=(const T &)`)

**Reason:** If the default destructor is insufficient (the class manages a raw resource), the default copy operations perform member-wise shallow copy, producing double-free or dangling-pointer bugs.

### 4.2 Rule of Five (C++11)

Extend the Rule of Three with:

4. **Move constructor** (`T(T &&)`)
5. **Move assignment operator** (`T &operator=(T &&)`)

If move operations are not defined, the compiler falls back to copying — expensive for large resources.

### 4.3 Rule Summary Table

| Special Member | Purpose | Omit When |
| :--- | :--- | :--- |
| Destructor | Release owned resource | Class owns no raw resource |
| Copy constructor | Deep copy of owned resource | Type is non-copyable by design |
| Copy assignment | Deep copy; handle self-assignment | Same |
| Move constructor | Transfer ownership; leave source empty | Same |
| Move assignment | Transfer ownership; release old resource | Same |

### 4.4 Worked Example: Dynamic Buffer Class

```cpp
#include <iostream>
#include <cstring>
#include <utility>

class Buffer {
public:
    explicit Buffer(std::size_t size)
        : size_(size), data_(new char[size]) {}

    ~Buffer() { delete[] data_; }

    // Copy constructor — deep copy.
    Buffer(const Buffer &other)
        : size_(other.size_), data_(new char[other.size_]) {
        std::memcpy(data_, other.data_, size_);
    }

    // Copy assignment — deep copy with self-assignment check.
    Buffer &operator=(const Buffer &other) {
        if (this != &other) {
            delete[] data_;
            size_ = other.size_;
            data_ = new char[size_];
            std::memcpy(data_, other.data_, size_);
        }
        return *this;
    }

    // Move constructor — transfer ownership.
    Buffer(Buffer &&other) noexcept
        : size_(other.size_), data_(other.data_) {
        other.data_ = nullptr;
        other.size_ = 0;
    }

    // Move assignment.
    Buffer &operator=(Buffer &&other) noexcept {
        if (this != &other) {
            delete[] data_;
            size_ = other.size_;
            data_ = other.data_;
            other.data_ = nullptr;
            other.size_ = 0;
        }
        return *this;
    }

    std::size_t size() const { return size_; }

private:
    std::size_t size_;
    char *data_;
};

int main() {
    Buffer a(100);
    Buffer b = a;           // Copy.
    Buffer c = std::move(a); // Move; a.data_ is now nullptr.
    std::cout << b.size() << " " << c.size() << "\n";
    return 0;
}
```

```text
100 100
```

---

## 5. Dynamic Memory: `new` and `delete`

### 5.1 Syntax Reference

| Operation | Syntax | Deallocation |
| :--- | :--- | :--- |
| Single object | `T *p = new T(args);` | `delete p;` |
| Array | `T *p = new T[n];` | `delete[] p;` |
| Zero-initialized | `T *p = new T();` | `delete p;` |

### 5.2 Behavioral Description

- `new` allocates on the heap and invokes the constructor.
- `delete` invokes the destructor and deallocates.
- `new[]` / `delete[]` must be paired; mixing `new` with `delete[]` (or vice versa) is undefined behavior.
- Failed allocation throws `std::bad_alloc` (unless `nothrow` variant is used).

```cpp
#include <iostream>

int main() {
    int *single = new int(42);
    int *array  = new int[5]{1, 2, 3, 4, 5};

    std::cout << *single << " " << array[2] << "\n";

    delete single;
    delete[] array;
    return 0;
}
```

```text
42 3
```

### 5.3 Ownership Hazards

| Hazard | Cause | Consequence |
| :--- | :--- | :--- |
| Memory leak | `new` without matching `delete` | Heap grows unboundedly |
| Double free | Two `delete` on same pointer | Undefined behavior |
| Dangling pointer | Use after `delete` | Undefined behavior |
| Mismatched deallocator | `new` with `delete[]` | Undefined behavior |

---

## 6. Smart Pointers (RAII Wrappers)

### 6.1 Concept Overview

Smart pointers are class templates that wrap a raw pointer and enforce RAII. They invoke `delete` (or a custom deleter) in their destructor.

### 6.2 Smart Pointer Reference Table

| Type | Header | Ownership Model | Copyable? |
| :--- | :--- | :--- | :--- |
| `std::unique_ptr<T>` | `<memory>` | Exclusive | No (move only) |
| `std::shared_ptr<T>` | `<memory>` | Shared (reference counted) | Yes |
| `std::weak_ptr<T>` | `<memory>` | Non-owning observer of `shared_ptr` | Yes |

### 6.3 `std::unique_ptr`

**Syntax:**

```
std::unique_ptr<<type>> <name> = std::make_unique<<type>>(<args>);
```

```cpp
#include <iostream>
#include <memory>

int main() {
    auto p = std::make_unique<int>(99);
    std::cout << *p << "\n";

    // Transfer ownership.
    auto q = std::move(p);
    std::cout << *q << "\n";
    // p is now nullptr.
    std::cout << (p == nullptr) << "\n";
    return 0;
}
```

```text
99
99
1
```

### 6.4 `std::shared_ptr`

```cpp
#include <iostream>
#include <memory>

int main() {
    std::shared_ptr<int> a = std::make_shared<int>(10);
    std::shared_ptr<int> b = a;   // Refcount = 2.
    std::cout << *a << " use_count=" << a.use_count() << "\n";
    return 0;
}   // Refcount reaches 0; memory freed.
```

```text
10 use_count=2
```

> **[Key Insight]** Prefer `std::make_unique` and `std::make_shared` over raw `new`. They are exception-safe (allocation and wrapper construction are a single step) and eliminate manual `delete`.

---

## 7. Operator Overloading

### 7.1 Concept Overview

C++ allows redefining operators for user-defined types, enabling syntax such as `a + b` for custom classes. Overloaded operators are functions with the `operator` keyword.

### 7.2 Syntax Reference

**Member function form:**

```
<return_type> operator<op>(<params>) { ... }
```

**Non-member (free function) form:**

```
<return_type> operator<op>(const <Class> &a, const <Class> &b) { ... }
```

### 7.3 Overloadable Operators Table

| Category | Operators | Notes |
| :--- | :--- | :--- |
| Arithmetic | `+`, `-`, `*`, `/`, `%` | Typically non-member for symmetry |
| Comparison | `==`, `!=`, `<`, `>`, `<=`, `>=` | C++20: `<=>` (spaceship) |
| Assignment | `=` | Must be member; returns `*this` |
| Subscript | `[]` | Must be member |
| Dereference | `*`, `->` | Must be member |
| Stream | `<<`, `>>` | Must be non-member |
| Cannot overload | `::`, `.*`, `.`, `?:`, `sizeof` | Language restriction |

### 7.4 Worked Example: `Vector2D` Addition and Stream Output

```cpp
#include <iostream>

class Vector2D {
public:
    double x, y;
    Vector2D(double x, double y) : x(x), y(y) {}

    Vector2D operator+(const Vector2D &other) const {
        return Vector2D(x + other.x, y + other.y);
    }

    friend std::ostream &operator<<(std::ostream &os, const Vector2D &v) {
        return os << "(" << v.x << ", " << v.y << ")";
    }
};

int main() {
    Vector2D a(1.0, 2.0);
    Vector2D b(3.0, 4.0);
    Vector2D c = a + b;
    std::cout << c << "\n";
    return 0;
}
```

```text
(4, 6)
```

---

## Common Errors and Gotchas

### Error 1: Shallow Copy of Raw Pointer (Rule of Three Violation)

**Cause:** Class holds `int *data` but uses compiler-generated copy constructor. Two objects share the same buffer; both destructors call `delete[]` on it.

**Resolution:** Implement copy constructor and copy assignment with deep copy, or delete copy operations and use `unique_ptr`.

### Error 2: `delete` vs. `delete[]` Mismatch

**Cause:** `int *p = new int[10]; delete p;` — undefined behavior.

**Resolution:** Always pair `new[]` with `delete[]`.

### Error 3: Dangling Reference from `std::move`d Object

**Cause:** Using a moved-from `std::string` or `std::vector` as if it still holds valid data.

**Resolution:** After `std::move(x)`, treat `x` as empty; only assign a new value or destroy it.

---

## Solved Exercises

### Exercise 1: Constructor Invocation Order

**Problem:** Predict the output.

```cpp
struct A { A() { std::cout << "A "; } };
struct B { B() { std::cout << "B "; } };
struct C : A {
    B member;
    C() { std::cout << "C "; }
};
int main() { C obj; }
```

**Solution:**

1. Base class `A` constructed first.
2. Member `B` constructed.
3. `C` body executes.

```text
A B C
```

---

### Exercise 2: Destructor Call Count

**Problem:** How many times is `~Student()` called?

```cpp
Student arr[3];
Student *heap = new Student();
delete heap;
```

**Solution:**

1. `arr[3]` — 3 stack objects destroyed at scope end.
2. `heap` — 1 heap object destroyed by `delete`.
3. Total: **4** destructor calls.

---

### Exercise 3: Copy vs. Move After `std::move`

**Problem:** After `Buffer b = std::move(a);` in the `Buffer` class above, what are `a.data_` and `b.data_`?

**Solution:**

1. Move constructor transfers `a.data_` to `b.data_`.
2. `a.data_` is set to `nullptr`; `a.size_` is 0.
3. `b.data_` points to the original buffer; `b.size_` is unchanged.

---

### Exercise 4: Self-Assignment in Copy Assignment

**Problem:** Why is `if (this != &other)` necessary in `operator=`?

**Solution:**

1. Self-assignment (`a = a`) would `delete[] data_` before copying from `other` (same object).
2. After deletion, `other.data_` is also invalid — reading it is undefined behavior.
3. The guard skips deletion and reallocation when source and destination are the same object.

---

### Exercise 5: `unique_ptr` Ownership Transfer

**Problem:** Trace `use_count` and ownership after:

```cpp
auto a = std::make_shared<int>(5);
auto b = a;
auto c = std::move(b);
```

**Solution:**

1. After `auto b = a`: `a.use_count() == 2`.
2. After `auto c = std::move(b)`: `c` shares with `a`; `a.use_count() == 2`; `b` is empty (moved-from `shared_ptr` has count 0, does not hold resource).

---

### Exercise 6: Operator Overload Evaluation

**Problem:** Evaluate `a + b` for `Vector2D a(1, 2)` and `Vector2D b(-1, 5)`.

**Solution:**

1. `operator+` returns `Vector2D(1 + (-1), 2 + 5) = Vector2D(0, 7)`.
2. Stream output: `(0, 7)`.

```text
(0, 7)
```

---

### Exercise 7: RAII and Exception Safety

**Problem:** Explain why this leaks, and how RAII fixes it.

```cpp
void leaky() {
    int *p = new int[1000];
    process();   // May throw.
    delete[] p;
}
```

**Solution:**

1. If `process()` throws, `delete[] p` is never reached — leak of 1000 integers.
2. **RAII fix:** `std::vector<int> v(1000);` or `std::unique_ptr<int[]> p(new int[1000]);` — destructor runs during stack unwinding when the exception propagates.

---

### Exercise 8: Rule of Five Decision

**Problem:** Class `Logger` holds only `std::string message` and `std::ofstream file`. Must `Logger` define the Rule of Five explicitly?

**Solution:**

1. `std::string` and `std::ofstream` manage their own resources internally.
2. Compiler-generated copy/move/destructor delegate to members correctly.
3. **No** — the Rule of Five is not triggered. Define special members only when the class directly owns a raw pointer or OS handle that members do not manage.

---

## Exam Tip: Rule of Three Triggers and `delete[]` Pairing

**Rule of Three trigger question pattern:** "A class contains `int *arr;` allocated in the constructor. Which special members must be user-defined?"

Answer: **destructor** (to `delete[] arr`), **copy constructor** (deep copy), **copy assignment** (deep copy with self-assignment guard). In C++11+, add **move constructor** and **move assignment** (Rule of Five).

**`new`/`delete[]` pairing trap:**

| Allocation | Correct Deallocation |
| :--- | :--- |
| `new T` | `delete p` |
| `new T[n]` | `delete[] p` |

Using `delete` on an array allocated with `new[]` is undefined behavior — a favorite exam distinction question.

**Smart pointer selection:**

- Exclusive ownership → `unique_ptr`
- Shared ownership with unknown lifetime → `shared_ptr`
- Break `shared_ptr` cycles → `weak_ptr`