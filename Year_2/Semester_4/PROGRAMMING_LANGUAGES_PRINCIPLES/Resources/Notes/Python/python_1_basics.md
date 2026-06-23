# Python — Basics

Python is a dynamically typed, interpreted programming language that compiles source code to bytecode executed by the CPython virtual machine. This file covers the foundational constructs: variable binding, arithmetic expressions, the heap-bound object memory model, control flow via `for` and `while` loops, function definitions, and the performance costs introduced by bytecode evaluation.

---

## 1. Variables and Dynamic Typing

### 1.1 Variable Binding

In Python, a **variable** is not a memory location that holds a value directly; it is a **name** that is bound to an object residing on the heap. The statement `x = 5` creates an integer object with value `5` on the heap and binds the name `x` to it.

**Formal model:**

```
name → reference → object (type, value, reference count)
```

The built-in function `id()` returns the memory address of the object a name is currently bound to. The built-in function `type()` returns the type of the object.

```python
x = 42
print(id(x))    # Address of the integer object 42 on the heap.
print(type(x))  # <class 'int'>
```

```text
<some integer address>
<class 'int'>
```

### 1.2 Dynamic Typing

Python uses **dynamic typing**: type information is attached to the object itself, not to the variable name. The same name can be rebound to objects of different types at any point in execution.

```python
x = 10       # x references an int object.
x = "hello"  # x now references a str object; the int object may be garbage-collected.
x = [1, 2]   # x now references a list object.
```

The interpreter does **not** check types at parse or compile time. Type errors are discovered only at the moment the incompatible operation is attempted at runtime.

**Contrast with static typing (e.g., C):**

| Property | Python (dynamic) | C (static) |
| :--- | :--- | :--- |
| Type bound to | Object | Variable declaration |
| Type check time | Runtime | Compile time |
| Rebinding to different type | Allowed | Not allowed |
| Type annotation required | No (optional via PEP 484) | Yes |

### 1.3 Arithmetic Expressions

Python supports all standard arithmetic operators. Integer division behavior is a common source of errors.

| Operator | Symbol | Example | Result |
| :--- | :--- | :--- | :--- |
| Addition | `+` | `3 + 2` | `5` |
| Subtraction | `-` | `7 - 4` | `3` |
| Multiplication | `*` | `3 * 4` | `12` |
| True division | `/` | `7 / 2` | `3.5` (always `float`) |
| Floor division | `//` | `7 // 2` | `3` (rounds toward negative infinity) |
| Modulo | `%` | `7 % 3` | `1` |
| Exponentiation | `**` | `2 ** 10` | `1024` |

> **[Key Insight]** The `/` operator **always** returns a `float` in Python 3, even when both operands are integers. Use `//` explicitly when integer division is required.

---

## 2. Dynamically Typed Memory Model (Heap-Bound Objects)

### 2.1 The Object Model

Every value in Python — integers, strings, lists, functions, classes — is an object on the heap. Each object carries three pieces of internal metadata:

1. **Type pointer:** a reference to the class object that describes the object's type.
2. **Reference count:** the number of names or containers currently referencing the object.
3. **Value:** the actual data the object holds.

```
Stack frame (local names)        Heap
┌────────────┐               ┌──────────────────────┐
│  x  ───────┼──────────────►│ type: int            │
│  y  ───────┼──────┐        │ refcount: 1          │
└────────────┘      │        │ value: 42            │
                    │        └──────────────────────┘
                    │        ┌──────────────────────┐
                    └───────►│ type: str            │
                             │ refcount: 1          │
                             │ value: "hello"       │
                             └──────────────────────┘
```

### 2.2 Reference Counting and Garbage Collection

CPython manages memory primarily through **reference counting**. When the reference count of an object drops to zero, the memory is deallocated immediately. To handle **reference cycles** (objects that reference each other forming a cycle, preventing counts from reaching zero), CPython includes a cyclic garbage collector that runs periodically.

```python
import sys
a = [1, 2, 3]
b = a           # Both a and b reference the same list object.
print(sys.getrefcount(a))  # Reports refcount + 1 (the argument itself adds one ref).
```

```text
3
```

### 2.3 Identity vs. Equality

- `is` tests **identity**: whether two names refer to the **same object** (same `id()`).
- `==` tests **equality**: whether the objects have the **same value** (invokes `__eq__`).

```python
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)   # True  — same value.
print(x is y)   # False — different objects on the heap.
z = x
print(x is z)   # True  — z and x reference the same object.
```

```text
True
False
True
```

> **[Key Insight]** CPython caches small integers (typically $-5$ to $256$) and interned short strings, so `is` may return `True` for small integer literals. This is an implementation detail and must never be relied upon for equality testing.

---

## 3. Control Flow

### 3.1 The `for` Loop

The `for` loop in Python iterates over any **iterable** object. An iterable is any object that implements the `__iter__` protocol, returning an **iterator** that yields successive elements.

**Abstract syntax:**

```
for <target> in <iterable>:
    <body>
[else:
    <else_body>]
```

The optional `else` clause executes if the loop completes normally (i.e., it was not terminated by a `break` statement).

```python
# Iterates over a list, binding each element to the name `item`.
for item in [10, 20, 30]:
    print(item)
```

```text
10
20
30
```

**`range()` function:**

`range(start, stop, step)` generates an arithmetic sequence without materializing all values in memory.

| Form | Equivalent sequence |
| :--- | :--- |
| `range(n)` | $0, 1, 2, \ldots, n-1$ |
| `range(a, b)` | $a, a+1, \ldots, b-1$ |
| `range(a, b, s)` | $a, a+s, a+2s, \ldots$ while $< b$ |

```python
for i in range(0, 10, 2):
    print(i, end=" ")
```

```text
0 2 4 6 8
```

### 3.2 The `while` Loop

The `while` loop repeats its body as long as a Boolean condition evaluates to `True`.

**Abstract syntax:**

```
while <condition>:
    <body>
[else:
    <else_body>]
```

```python
n = 1
while n <= 5:
    print(n)
    n += 1
```

```text
1
2
3
4
5
```

### 3.3 `break` and `continue`

- `break`: immediately exits the innermost enclosing loop.
- `continue`: skips the remainder of the current iteration and proceeds to the next condition check.

```python
for i in range(10):
    if i == 3:
        continue   # Skips printing 3.
    if i == 6:
        break      # Exits the loop at 6.
    print(i, end=" ")
```

```text
0 1 2 4 5
```

---

## 4. Functions

### 4.1 Definition and Call

**Abstract syntax:**

```
def <function_name>(<parameters>):
    <body>
    [return <expression>]
```

A function without an explicit `return` statement returns `None` implicitly.

```python
def add(a, b):
    """Computes the sum of two values."""
    return a + b

result = add(3, 7)
print(result)
```

```text
10
```

### 4.2 Parameter Kinds

| Kind | Syntax | Behavior |
| :--- | :--- | :--- |
| Positional | `def f(a, b)` | Matched left-to-right by position |
| Keyword | `f(a=1, b=2)` | Matched by name; order-independent |
| Default value | `def f(a, b=10)` | `b` uses `10` if not supplied |
| Variadic positional | `def f(*args)` | Collects extra positional args into a tuple |
| Variadic keyword | `def f(**kwargs)` | Collects extra keyword args into a dict |

```python
def describe(name, age=0, *hobbies, **extra):
    print(f"Name: {name}, Age: {age}")
    print(f"Hobbies: {hobbies}")
    print(f"Extra: {extra}")

describe("Alice", 30, "chess", "hiking", city="Athens")
```

```text
Name: Alice, Age: 30
Hobbies: ('chess', 'hiking')
Extra: {'city': 'Athens'}
```

### 4.3 Scope: LEGB Rule

Python resolves names using the **LEGB** rule, searching four scopes in order:

1. **L**ocal — names defined inside the current function.
2. **E**nclosing — names in any enclosing function scopes (for nested functions).
3. **G**lobal — names defined at module level.
4. **B**uilt-in — names in Python's built-in namespace (`print`, `len`, etc.).

```python
x = "global"

def outer():
    x = "enclosing"
    def inner():
        print(x)   # Resolves to "enclosing" via the E scope.
    inner()

outer()
```

```text
enclosing
```

---

## 5. Bytecode Evaluation Costs

### 5.1 CPython Execution Pipeline

CPython processes Python source in four stages:

1. **Lexing:** Tokenizes source text into a stream of tokens.
2. **Parsing:** Constructs an Abstract Syntax Tree (AST) from tokens.
3. **Compilation:** Translates the AST into platform-independent **bytecode** (`.pyc` files).
4. **Interpretation:** The CPython virtual machine (PVM) executes bytecode instructions one by one via an evaluation loop.

This model distinguishes Python from fully compiled languages (C, C++) where stage 4 does not exist — machine code executes directly on the CPU.

### 5.2 The Overhead of Dynamic Dispatch

Because every object carries its type at runtime, **every operation in Python requires a type lookup**. A simple integer addition `a + b` does not map to a single CPU instruction. Instead, the interpreter must:

1. Fetch the object referenced by `a`.
2. Read its type pointer to find the `int` type object.
3. Look up the `__add__` method in the type's method table.
4. Call `__add__` with `b` as the argument.
5. Allocate a new integer object on the heap for the result.

This dispatch sequence costs orders of magnitude more than a native `ADD` instruction.

### 5.3 Bytecode Inspection

The `dis` module exposes the bytecode of any Python function.

```python
import dis

def square(n):
    return n * n

dis.dis(square)
```

```text
  2           0 RESUME                   0

  3           2 LOAD_FAST                0 (n)
              4 LOAD_FAST                0 (n)
              6 BINARY_OP               5 (*)
             10 RETURN_VALUE
```

Each line represents one **opcode**. The interpreter processes these opcodes sequentially. Even this trivial function requires multiple opcodes, each of which involves Python-level object protocol overhead.

> **[Key Insight]** The primary implication of bytecode evaluation cost is that tight loops over large datasets written in pure Python are significantly slower than equivalent operations delegated to libraries such as NumPy, which execute native C loops. Minimizing the number of Python-level operations inside hot loops is a key optimization strategy.

---

## Solved Exercises

### Exercise 1: Type Identification at Runtime

**Problem:** Given the assignments below, predict the output of each `type()` call without running the code.

```python
a = 7
b = 7.0
c = 7 + 0j
d = "7"
e = True
```

**Solution:**

1. `type(a)` → `<class 'int'>` — integer literal.
2. `type(b)` → `<class 'float'>` — decimal literal.
3. `type(c)` → `<class 'complex'>` — complex literal.
4. `type(d)` → `<class 'str'>` — string literal.
5. `type(e)` → `<class 'bool'>` — `bool` is a subclass of `int` in Python; `True` has integer value `1`.

---

### Exercise 2: Integer vs. Float Division

**Problem:** Evaluate the following expressions and explain each result.

```
7 / 2
7 // 2
-7 // 2
7 % 2
7.0 // 2
```

**Solution:**

1. `7 / 2` → `3.5` — true division always returns `float`.
2. `7 // 2` → `3` — floor division truncates toward negative infinity; $\lfloor 3.5 \rfloor = 3$.
3. `-7 // 2` → `-4` — floor of $-3.5$ is $-4$ (rounds toward negative infinity, not toward zero).
4. `7 % 2` → `1` — remainder; $7 = 3 \times 2 + 1$.
5. `7.0 // 2` → `3.0` — floor division with a `float` operand returns `float`.

---

### Exercise 3: Reference Counting

**Problem:** Trace the reference count of the list object `[1, 2, 3]` through the following sequence.

```python
a = [1, 2, 3]   # Step 1
b = a            # Step 2
c = [a, a]       # Step 3
del a            # Step 4
b = None         # Step 5
```

**Solution:**

| Step | Operation | Ref count of `[1,2,3]` | Reason |
| :--- | :--- | :--- | :--- |
| 1 | `a = [1,2,3]` | 1 | `a` references it |
| 2 | `b = a` | 2 | `b` also references it |
| 3 | `c = [a, a]` | 4 | `c[0]` and `c[1]` each add one reference |
| 4 | `del a` | 3 | `a` binding is removed |
| 5 | `b = None` | 2 | `b` no longer references the list; `c[0]` and `c[1]` remain |

The list is not garbage-collected at step 5 because `c` still holds two references to it.

---

### Exercise 4: Identity vs. Equality with Lists

**Problem:** Predict the output of the following code.

```python
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x == y)
print(x is y)
print(x is z)
print(id(x) == id(z))
```

**Solution:**

```text
True
False
True
True
```

- `x == y`: Both lists contain the same elements, so `__eq__` returns `True`.
- `x is y`: These are two distinct list objects on the heap, so `False`.
- `x is z`: `z = x` copies the reference, not the object; both names point to the same heap object, so `True`.
- `id(x) == id(z)`: Confirms the above; same object, same address.

---

### Exercise 5: LEGB Scope Resolution

**Problem:** Determine what is printed by this code without running it.

```python
value = 100

def outer():
    value = 200
    def inner():
        value = 300
        print(value)
    inner()
    print(value)

outer()
print(value)
```

**Solution:**

1. Inside `inner()`: the local scope defines `value = 300`. LEGB finds it in **L**. Prints `300`.
2. After `inner()` returns, back in `outer()`: the enclosing scope defines `value = 200`. Prints `200`.
3. After `outer()` returns, at module level: global `value = 100`. Prints `100`.

```text
300
200
100
```

---

### Exercise 6: `range()` Behavior

**Problem:** Without running the code, list all values printed by the following loop.

```python
for i in range(2, 20, 3):
    print(i)
```

**Solution:**

The sequence starts at $2$, increments by $3$, and stops before $20$:

$$2, \ 5, \ 8, \ 11, \ 14, \ 17$$

At the next step, $17 + 3 = 20$, which is not strictly less than $20$, so iteration stops.

```text
2
5
8
11
14
17
```

---

### Exercise 7: `for`-`else` Clause

**Problem:** Explain the behavior of the `else` clause and predict the output.

```python
def find_prime(numbers):
    for n in numbers:
        if n > 1:
            for i in range(2, n):
                if n % i == 0:
                    print(f"{n} is not prime")
                    break
            else:
                print(f"{n} is prime")

find_prime([2, 3, 4, 9, 11])
```

**Solution:**

The inner `else` executes only when the inner `for` loop completes **without** hitting a `break`. This happens exactly when no divisor is found — i.e., when `n` is prime.

```text
2 is prime
3 is prime
4 is not prime
9 is not prime
11 is prime
```

---

### Exercise 8: Variadic Arguments and Bytecode Overhead

**Problem:** Write a function `stats(label, *values)` that prints the label, the count of values, and their sum. Then use `dis` to inspect how many bytecode instructions the function body generates (conceptually — list the key operations).

**Solution:**

```python
import dis

def stats(label, *values):
    count = len(values)
    total = sum(values)
    print(f"{label}: count={count}, sum={total}")

stats("scores", 10, 20, 30, 40)
dis.dis(stats)
```

```text
scores: count=4, sum=100
```

Key bytecode operations (simplified):

- `LOAD_GLOBAL` to fetch `len` and `sum` from the global/built-in scope.
- `LOAD_FAST` to load the local names `values`, `count`, `total`, `label`.
- `CALL_FUNCTION` for each call to `len`, `sum`, and `print`.
- `LOAD_CONST` to load the f-string template components.

Each `LOAD_GLOBAL` incurs a dictionary lookup in the module's `__dict__`, which is more expensive than `LOAD_FAST` (which is a direct index into the local variable array). Assigning frequently-used global names to local variables inside performance-critical functions is a standard micro-optimization.

---

## Exam Tip: Dynamic Typing and Floor Division Edge Cases

**Floor division toward negative infinity** is the most commonly tested edge case. The floor function $\lfloor x \rfloor$ rounds toward $-\infty$, not toward zero. Therefore:

$$-7 // 2 = -4 \quad \text{not} \quad -3$$

because $\lfloor -3.5 \rfloor = -4$.

**Common exam pattern:** Given a fragment like `x = -9 // 4`, students often answer `-2` (truncation toward zero). The correct answer is `-3` because $-9 / 4 = -2.25$ and $\lfloor -2.25 \rfloor = -3$.

**Reference counting trap:** When tracing reference counts, remember that passing an object as a function argument temporarily increments its reference count for the duration of the call. `sys.getrefcount(x)` always reports one more than the "actual" count because the function call itself holds a reference.
