# C++ — Basics and Hardware Semantics

C++ is a statically typed, compiled language whose semantics are tightly coupled to the underlying machine model: stack frames, heap allocation, and direct memory addresses. This file covers the three principal parameter-passing mechanisms — pass-by-value, pass-by-reference, and pass-by-pointer — and the use of `const` references for efficient read-only access to large objects. Understanding these mechanisms is prerequisite to reasoning about copy cost, aliasing, and cache-friendly program design in subsequent C++ topics.

---

## 1. Pass-by-Value

### 1.1 Concept Overview

**Pass-by-value** copies the argument into the function's stack frame. The callee receives an independent copy; mutations inside the function do not affect the caller's original variable. For small primitive types (`int`, `double`, `bool`), the copy cost is negligible. For large objects (e.g., `std::vector`, custom classes), pass-by-value incurs a full copy onto the stack or heap, which can dominate runtime cost.

### 1.2 Syntax Reference

```
void <function_name>(<type> <param_name>)
```

The parameter type is specified without `&` or `*`. The caller passes an expression whose value is copied into the parameter.

### 1.3 Behavioral Description

When a function is invoked with pass-by-value:

1. The argument expression is evaluated.
2. A new object of the parameter type is created in the callee's activation record.
3. The argument's value is copied into this new object (via copy constructor for class types).
4. The function body operates on the copy.
5. On return, the copy is destroyed.

For class types, the copy may allocate heap memory (e.g., copying a `std::string` duplicates its internal character buffer).

### 1.4 Parameter Reference

| Mechanism | Syntax | Copy Cost | Caller Modified? | Typical Use |
| :--- | :--- | :--- | :--- | :--- |
| Pass-by-value | `void f(int x)` | Full copy | No | Small primitives, immutability guarantee |
| Pass-by-reference | `void f(int &x)` | None (alias) | Yes | In-out parameters, large objects to mutate |
| Pass-by-pointer | `void f(int *x)` | Pointer copy (8 bytes) | Yes (via dereference) | Optional parameters, C-style APIs |
| Const reference | `void f(const T &x)` | None (alias) | No | Read-only access to large objects |

```cpp
#include <iostream>

void increment_by_value(int x) {
    x += 10;   // Modifies the local copy only.
}

int main() {
    int a = 5;
    increment_by_value(a);
    std::cout << a << "\n";   // Caller unchanged.
    return 0;
}
```

```text
5
```

---

## 2. Pass-by-Reference

### 2.1 Concept Overview

**Pass-by-reference** binds the parameter name as an alias to the caller's object. No copy is made; the parameter and the argument refer to the same memory location. This achieves zero-copy semantics and allows the callee to modify the caller's state.

### 2.2 Syntax Reference

```
void <function_name>(<type> &<param_name>)
```

The `&` immediately follows the type (or the parameter name in trailing-return style). For `const` references:

```
void <function_name>(const <type> &<param_name>)
```

### 2.3 Behavioral Description

A reference is not a separate object; it is an alternative name for an existing object. At the machine level, references are typically implemented as pointers, but the language guarantees that a reference must be initialized to a valid object and cannot be rebound.

**Abstract model:**

```
caller variable (address A)  ←── alias ──→  reference parameter (same address A)
```

### 2.4 Worked Example: `update(int &x, int y)`

The mindmap example `void update(int &x, int y)` demonstrates mixed passing: `x` is modified in place; `y` is a local copy.

```cpp
#include <iostream>

void update(int &x, int y) {
    x = x + y;   // `x` aliases the caller's variable; mutation is visible outside.
    y = y * 2;   // `y` is a local copy; this has no effect on the caller.
}

int main() {
    int a = 10;
    int b = 3;
    update(a, b);
    std::cout << "a = " << a << ", b = " << b << "\n";
    return 0;
}
```

```text
a = 13, b = 3
```

| Variable | Before | After `update(a, b)` | Reason |
| :--- | :--- | :--- | :--- |
| `a` | 10 | 13 | Passed by reference; `x = x + y` writes to `a` |
| `b` | 3 | 3 | Passed by value; `y = y * 2` affects only the copy |

---

## 3. Pass-by-Pointer

### 3.1 Concept Overview

**Pass-by-pointer** passes the memory address of an object. The callee must explicitly dereference the pointer with `*` to access or modify the pointed-to value. Unlike references, pointers can be `nullptr`, can be reassigned to point elsewhere, and support pointer arithmetic.

### 3.2 Syntax Reference

```
void <function_name>(<type> *<param_name>)
```

Dereference operator: `*<pointer_name>`

Address-of operator: `&<variable_name>`

### 3.3 Behavioral Description

The pointer itself is passed by value — a copy of the address is made on the stack. However, dereferencing the pointer accesses the original object at that address. This is the mechanism used in C and in C++ APIs that require optional or nullable parameters.

```cpp
#include <iostream>

void swap(int *p, int *q) {
    int temp = *p;
    *p = *q;
    *q = temp;
}

int main() {
    int a = 1, b = 2;
    swap(&a, &b);   // Pass addresses of a and b.
    std::cout << "a = " << a << ", b = " << b << "\n";
    return 0;
}
```

```text
a = 2, b = 1
```

### 3.4 Reference vs. Pointer Comparison

| Property | Reference (`T &`) | Pointer (`T *`) |
| :--- | :--- | :--- |
| Must be initialized | Yes | No (can be `nullptr`) |
| Can be rebound | No | Yes |
| Syntax for access | Direct (`x`) | Requires `*x` |
| Arithmetic | Not allowed | Allowed |
| Null state | Not possible | `nullptr` represents absence |
| Typical era | Modern C++ style | C interoperability, optional args |

---

## 4. Const References for Read-Only Large Objects

### 4.1 Concept Overview

A **`const` reference** (`const T &`) provides zero-copy read-only access to an object. The callee cannot modify the object through the reference, but avoids the cost of copying large structures. This is the standard idiom for passing `std::string`, `std::vector`, and user-defined classes to functions that only read data.

### 4.2 Syntax Reference

```
void <function_name>(const <type> &<param_name>)
```

The `const` qualifier applies to the referenced object, not to the reference binding itself.

### 4.3 Behavioral Description

- No copy is performed.
- The function cannot call non-`const` member functions on the object.
- The function cannot assign to the object or its members.
- A `const T &` can bind to a temporary (rvalue), extending the temporary's lifetime for the duration of the call.

```cpp
#include <iostream>
#include <string>
#include <vector>

// Accepts a large string by const reference — no copy.
int count_vowels(const std::string &text) {
    int count = 0;
    for (char c : text) {
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u')
            ++count;
    }
    return count;
}

int main() {
    std::string sentence = "programming languages principles";
    std::cout << count_vowels(sentence) << "\n";
    // Temporary binding: const ref extends lifetime of the literal's temporary.
    std::cout << count_vowels("hello world") << "\n";
    return 0;
}
```

```text
9
3
```

### 4.4 When to Use Each Mechanism

| Scenario | Recommended Mechanism |
| :--- | :--- |
| Small primitive (`int`, `char`, `bool`) | Pass-by-value |
| Large object, read-only | `const T &` |
| Large object, must modify | `T &` |
| Optional / nullable parameter | `T *` (check for `nullptr`) |
| Output parameter (legacy style) | `T *` or `T &` |
| Transfer ownership | `T &&` (move semantics; see cpp_3_oop_resource_management.md) |

> **[Key Insight]** For function parameters of class type, the default rule in modern C++ is: pass by `const T &` for read-only, pass by `T &` for in-out, and pass by value (or `T &&`) only when ownership transfer or a local copy is genuinely needed. Blind pass-by-value on `std::vector` or `std::string` is a common performance bug.

---

## 5. Stack vs. Heap Cost Model

### 5.1 Activation Records

Function-local variables and pass-by-value copies of small types reside on the **stack**. Stack allocation is $O(1)$: the compiler adjusts the stack pointer by a fixed offset at function entry.

Objects created with `new` (or whose copies allocate internal buffers) reside on the **heap**. Heap allocation involves allocator bookkeeping and is orders of magnitude slower than stack allocation.

```
Stack frame of caller          Stack frame of callee (pass-by-value int)
┌──────────────┐               ┌──────────────┐
│  a = 5       │               │  x = 5       │  ← independent copy
└──────────────┘               └──────────────┘

Stack frame of caller          Stack frame of callee (pass-by-reference)
┌──────────────┐               ┌──────────────┐
│  a = 5  ◄────┼───────────────┼── x (alias)  │  ← same memory
└──────────────┘               └──────────────┘
```

### 5.2 Copy Cost for Class Types

When a `std::vector<int>` is passed by value, the entire dynamic array is duplicated:

1. Allocate a new heap buffer of equal capacity.
2. Copy all elements.
3. On function return, destroy the copy (deallocate buffer).

Passing the same vector by `const std::vector<int> &` avoids both allocation and element copy.

---

## Common Errors and Gotchas

### Error 1: Returning a Reference to a Local Variable

**Cause:** A function returns `T &` pointing to a stack-local object that is destroyed when the function returns.

```cpp
int &bad() {
    int x = 42;
    return x;   // Undefined behavior: x is destroyed at return.
}
```

**Resolution:** Return by value for locals, or return a reference/pointer only to objects that outlive the function (e.g., member variables, static storage, or heap objects whose ownership is documented).

### Error 2: Dereferencing a Null Pointer

**Cause:** A pointer parameter is not checked for `nullptr` before use.

```cpp
void print(int *p) {
    std::cout << *p;   // Crashes if p == nullptr.
}
```

**Resolution:** Guard with `if (p != nullptr)` or use references when null is not a valid state.

### Error 3: Confusing `const T &` with `T &` Overload Resolution

**Cause:** Calling a non-`const` member function on an object passed as `const T &` produces a compile error.

```cpp
void append_char(std::string &s) { s += '!'; }

int main() {
    const std::string msg = "hello";
    // append_char(msg);   // Error: cannot bind const object to non-const ref.
}
```

**Resolution:** Provide a `const`-correct overload, or remove `const` only when mutation is intended and safe.

---

## Solved Exercises

### Exercise 1: Trace Pass-by-Value

**Problem:** Predict the output without running the code.

```cpp
void add_five(int n) {
    n += 5;
}

int main() {
    int x = 10;
    add_five(x);
    std::cout << x;
}
```

**Solution:**

1. `x` is initialized to 10 in `main`.
2. `add_five(x)` copies `x` into local `n`; `n` becomes 15.
3. The copy is destroyed; `x` in `main` remains 10.

```text
10
```

---

### Exercise 2: Trace Pass-by-Reference

**Problem:** Predict the output.

```cpp
void add_five(int &n) {
    n += 5;
}

int main() {
    int x = 10;
    add_five(x);
    std::cout << x;
}
```

**Solution:**

1. `n` is an alias for `x`.
2. `n += 5` writes 15 directly to `x`.

```text
15
```

---

### Exercise 3: Mixed `update(int &x, int y)`

**Problem:** Trace the values of `a` and `b` after the call.

```cpp
void update(int &x, int y) {
    x = x * 2;
    y = y + 1;
}

int main() {
    int a = 4, b = 7;
    update(a, b);
    std::cout << a << " " << b;
}
```

**Solution:**

1. `x` aliases `a`: `a = 4 * 2 = 8`.
2. `y` is a copy of `b`: local `y = 8`, but `b` stays 7.

```text
8 7
```

---

### Exercise 4: Pointer Swap

**Problem:** Implement and trace `swap(int *a, int *b)` that exchanges the values at the two addresses. Initial state: `x = 100`, `y = 200`.

**Solution:**

```cpp
void swap(int *a, int *b) {
    int tmp = *a;
    *a = *b;
    *b = tmp;
}
// swap(&x, &y);
```

| Step | `*a` (x) | `*b` (y) | `tmp` |
| :--- | :--- | :--- | :--- |
| Initial | 100 | 200 | — |
| `tmp = *a` | 100 | 200 | 100 |
| `*a = *b` | 200 | 200 | 100 |
| `*b = tmp` | 200 | 100 | 100 |

```text
x = 200, y = 100
```

---

### Exercise 5: Const Reference Binding to Temporary

**Problem:** Explain why this compiles and what value is printed.

```cpp
int length(const std::string &s) {
    return static_cast<int>(s.size());
}

int main() {
    std::cout << length("abc");
}
```

**Solution:**

1. `"abc"` is a string literal of type `const char[4]`.
2. A temporary `std::string` is constructed for the call.
3. `const std::string &` binds to the temporary; its lifetime extends through the full expression.
4. `s.size()` returns 3.

```text
3
```

---

### Exercise 6: Choosing the Right Parameter Type

**Problem:** For each function signature below, state whether it should use value, `const &`, `&`, or `*`.

1. `void print_bool(bool flag)`
2. `void sort_vector(std::vector<int> &data)`
3. `void display(const std::vector<int> &data)`
4. `void find(int *result, bool *found)`

**Solution:**

1. **Pass-by-value** — `bool` is a single byte; copying is cheaper than indirection.
2. **Non-const reference** — `sort_vector` must reorder the caller's vector in place.
3. **Const reference** — `display` only reads; avoids copying the entire vector.
4. **Pointers** — two optional output slots; allows caller to pass `nullptr` if an output is not needed.

---

### Exercise 7: Reference Cannot Be Rebound

**Problem:** Explain why the following does not rebind reference `r` from `a` to `b`.

```cpp
int a = 1, b = 2;
int &r = a;
r = b;
std::cout << a << " " << r;
```

**Solution:**

1. `int &r = a` binds `r` to `a` permanently.
2. `r = b` is an **assignment** to the object `a`, not a rebinding of `r`.
3. Both `a` and `r` (same object) become 2.

```text
2 2
```

---

### Exercise 8: Copy Cost Analysis

**Problem:** A function `void process(std::vector<int> data)` receives a vector of $10^6$ integers. The caller's vector occupies 4 MB. Estimate the extra memory allocated inside the call due to pass-by-value, and state the fix.

**Solution:**

1. Pass-by-value invokes the copy constructor of `std::vector<int>`.
2. A second heap buffer of $\approx 4 \times 10^6$ bytes is allocated; all $10^6$ integers are copied.
3. Extra memory: approximately 4 MB for the duration of the call.
4. **Fix:** Change the signature to `void process(const std::vector<int> &data)` for read-only access, eliminating the copy entirely.

---

## Exam Tip: Parameter Passing on Paper Traces

**The three-question checklist** for any C++ parameter-passing trace question:

1. **Is the parameter a value, reference, or pointer?** Value → local copy; reference → alias; pointer → copy of address, shared object via `*`.
2. **Is `const` present?** `const T &` forbids modification through that parameter.
3. **Does the function body assign to the parameter name itself (rebinding) or to `*param` / through the reference?** Assignment to a pointer variable changes the address stored locally, not the caller's object. Assignment through `*p` or via `&` reference changes the caller's object.

**Most common exam trap:** Given `void f(int *p) { p = nullptr; }`, students claim the caller's pointer was set to null. In fact, only the local copy of the address was changed. To affect the caller's pointer, the signature must be `int **p` (pointer to pointer) or a reference `int *&p`.