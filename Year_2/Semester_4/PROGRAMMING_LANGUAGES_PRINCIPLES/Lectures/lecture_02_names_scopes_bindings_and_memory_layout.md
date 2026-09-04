# Lecture 02: Names, Scopes, Binding Times, and Memory Layout

This lecture examines semantic foundations across programming languages: binding times, static vs. dynamic typing, lexical (static) vs. dynamic scoping, activation records on the runtime call stack, and process memory architecture (stack vs. heap).

---

## 1. Names and Binding Times

A **binding** is an association between an entity and an attribute (e.g., variable name to memory address, variable to type, operator symbol to operation).

### 1.1 Binding Time Categories
- **Language Design Time:** Operator symbols bound to semantic meanings (e.g., `+` bound to addition).
- **Language Implementation Time:** Primitive types bound to representation sizes (e.g., 32-bit vs. 64-bit integer word sizes).
- **Compile Time (Static Binding):** Variable names bound to static data types in statically typed languages (C, Java, Haskell).
- **Link Time:** External function symbols bound to code module entry addresses.
- **Load Time:** Global and static variables bound to virtual memory addresses.
- **Runtime (Dynamic Binding):** Variable names bound to values, dynamic types, or polymorphic method dispatch addresses (Python, Smalltalk, virtual methods in C++).

---

## 2. Type Systems

- **Statically Typed:** Type checking occurs at compile time (C, C++, Java, Haskell). Eliminates type error crashes at runtime; enhances optimization.
- **Dynamically Typed:** Type checking occurs at runtime (Python, JavaScript, Ruby). Variables hold references to tagged objects; offers greater prototyping flexibility.
- **Strongly Typed:** The type system strictly forbids operations on incompatible types without explicit conversion (Python, Haskell, Java).
- **Weakly Typed:** The type system permits implicit conversions or unchecked pointer reinterpretations (C, C++).

---

## 3. Scoping: Lexical (Static) vs. Dynamic Scoping

The **scope** of a variable binding is the spatial region of program text within which the binding is visible and valid.

### 3.1 Lexical (Static) Scoping
Bindings are determined strictly by the spatial nesting of code blocks at compile time.
- Standard in modern languages (C, C++, Java, Python, Haskell).
- The compiler traverses enclosing lexical blocks outward to resolve an identifier.

### 3.2 Dynamic Scoping
Bindings are determined by the temporal execution call chain at runtime.
- Used in early Lisp dialects, Emacs Lisp, and Bash shell scripts.
- An identifier lookup searches backward through the active call stack until a binding is encountered.

### 3.3 Scoping Comparison Example

```python
x = 10

def f():
    return x

def g():
    x = 20
    return f()

print(g())
```

- **Under Lexical Scoping:** `f()` is bound to global `x = 10`. Output: `10`.
- **Under Dynamic Scoping:** When `f()` executes, its caller `g()` has an active local binding `x = 20`. Output: `20`.

---

## 4. Runtime Process Memory Organization

A compiled procedural or object-oriented program occupies four distinct virtual memory segments:

```
Higher Memory Addresses (0xFFFFFFFF)
+-------------------------------------------------------------+
| Stack (Grows Downward)                                      |
|   [ Activation Records / Stack Frames:                      |
|     Parameters, Return Address, Saved FP, Local Variables ] |
|                             |                               |
|                             v                               |
|                                                             |
|                             ^                               |
|                             |                               |
| Heap (Grows Upward)                                         |
|   [ Dynamically Allocated Memory: malloc(), new ]           |
+-------------------------------------------------------------+
| BSS Segment (Uninitialized Global / Static Data)            |
+-------------------------------------------------------------+
| Data Segment (Initialized Global / Static Variables)        |
+-------------------------------------------------------------+
| Text Segment (Machine Code Instructions - Read Only)        |
+-------------------------------------------------------------+
Lower Memory Addresses (0x00000000)
```

### 4.1 Stack Frames (Activation Records)
Whenever a function is called, an activation record is pushed onto the stack containing:
1. Actual parameters passed to the function.
2. Return address pointing to next instruction in caller.
3. Dynamic link (saved frame pointer `EBP`/`RBP` restoring caller's stack frame).
4. Static link (in lexically nested languages, points to immediate enclosing lexical parent frame).
5. Local variables allocated within the function block.

