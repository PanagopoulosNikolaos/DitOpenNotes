# Python — Intermediate Constructs

*Prerequisite: python_1_basics.md — Variables, dynamic typing, and heap-bound memory model.*

Python's intermediate constructs build on the fundamental object model to provide high-level, expressive data structures and syntax. This file covers the three principal built-in collection types (`list`, `dict`, `set`), their internal implementation and algorithmic complexity, list comprehensions derived from set-builder notation, and the decorator mechanism for higher-order function transformation.

---

## 1. Lists

### 1.1 Internal Representation

A Python `list` is a **dynamic array of object references**. Internally, CPython maintains a contiguous block of pointers to heap objects, plus a capacity field and a length field. When the capacity is exhausted, the array is reallocated at a larger size (the growth factor is approximately $1.125$, i.e., roughly $12.5\%$ amortized growth).

Because the list stores references (pointers) rather than values directly, a list can contain objects of heterogeneous types, and appending to a list does not require copying the objects themselves.

### 1.2 Core Operations and Complexity

| Operation | Syntax | Average Time Complexity | Notes |
| :--- | :--- | :--- | :--- |
| Index access | `lst[i]` | $O(1)$ | Direct pointer arithmetic |
| Append | `lst.append(x)` | $O(1)$ amortized | Occasional $O(n)$ resize |
| Insert at position | `lst.insert(i, x)` | $O(n)$ | Shifts elements right |
| Delete by index | `del lst[i]` | $O(n)$ | Shifts elements left |
| Delete by value | `lst.remove(x)` | $O(n)$ | Linear scan + shift |
| Membership test | `x in lst` | $O(n)$ | Linear scan |
| Length | `len(lst)` | $O(1)$ | Stored as a field |
| Slice | `lst[a:b]` | $O(b-a)$ | Allocates a new list |
| Sort (in-place) | `lst.sort()` | $O(n \log n)$ | Timsort; stable |
| Reverse (in-place) | `lst.reverse()` | $O(n)$ | Pointer swap |

```python
numbers = [5, 1, 4, 2, 8]
numbers.sort()
print(numbers)

numbers.append(10)
print(numbers)

print(numbers[2:5])  # Slice from index 2 (inclusive) to 5 (exclusive).
```

```text
[1, 2, 4, 5, 8]
[1, 2, 4, 5, 8, 10]
[4, 5, 8]
```

### 1.3 Negative Indexing

Python supports negative indices, which count from the end of the list. Index $-1$ refers to the last element, $-2$ to the second-to-last, and so on. For a list of length $n$, index $i$ is equivalent to index $n + i$ for negative $i$.

```python
lst = [10, 20, 30, 40, 50]
print(lst[-1])   # 50
print(lst[-3])   # 30
```

```text
50
30
```

---

## 2. Dictionaries

### 2.1 Internal Implementation: Hash Tables

A Python `dict` is implemented as a **hash table** with open addressing. The underlying data structure is essentially a C-struct array, where each slot stores a triple: `(hash, key, value)`.

**Insertion and lookup algorithm (simplified):**

1. Compute `hash(key)` — an integer hash value.
2. Compute the slot index: `slot = hash(key) % table_size`.
3. If the slot is empty, place the entry there.
4. If the slot is occupied by a different key (a **collision**), probe the next slot according to the probing sequence until an empty slot is found.

This yields **average-case** $O(1)$ insert and lookup, and **worst-case** $O(n)$ when all keys hash to the same slot (rare with good hash functions).

> **[Key Insight]** Only **hashable** objects may be used as dictionary keys. An object is hashable if it implements `__hash__` and `__eq__`. Immutable built-in types (`int`, `float`, `str`, `tuple` of hashables) are hashable. Mutable types (`list`, `dict`, `set`) are not and raise `TypeError` if used as keys.

### 2.2 Core Operations and Complexity

| Operation | Syntax | Average Time | Worst Case |
| :--- | :--- | :--- | :--- |
| Insert / update | `d[k] = v` | $O(1)$ | $O(n)$ |
| Lookup | `d[k]` | $O(1)$ | $O(n)$ |
| Delete | `del d[k]` | $O(1)$ | $O(n)$ |
| Membership test | `k in d` | $O(1)$ | $O(n)$ |
| Iteration | `for k in d` | $O(n)$ | $O(n)$ |
| Length | `len(d)` | $O(1)$ | — |

```python
# Dictionary creation and common operations.
student = {"name": "Alice", "grade": 90}
student["email"] = "alice@example.com"   # Insert new key.
student["grade"] = 95                    # Update existing key.

print(student.get("phone", "N/A"))       # Safe access with default.
print("name" in student)                 # Membership test on keys.

for key, value in student.items():
    print(f"{key}: {value}")
```

```text
N/A
True
name: Alice
grade: 95
email: alice@example.com
```

### 2.3 Dictionary Views

`dict.keys()`, `dict.values()`, and `dict.items()` return **view objects** — dynamic, read-only windows into the dictionary's current state. They reflect changes made to the dictionary after the view was created.

```python
d = {"a": 1, "b": 2}
keys_view = d.keys()
d["c"] = 3
print(keys_view)   # Includes "c" because views are dynamic.
```

```text
dict_keys(['a', 'b', 'c'])
```

---

## 3. Sets

### 3.1 Internal Implementation

A Python `set` is implemented as a **hash table of keys with no values** — effectively a dictionary that stores only the keys. This gives `set` the same $O(1)$ average-case membership test as `dict`, making it the appropriate data structure when the only concern is membership.

### 3.2 Core Operations and Complexity

| Operation | Syntax / Method | Average Time |
| :--- | :--- | :--- |
| Add element | `s.add(x)` | $O(1)$ |
| Remove element | `s.remove(x)` | $O(1)$; raises `KeyError` if absent |
| Remove if present | `s.discard(x)` | $O(1)$; no exception |
| Membership test | `x in s` | $O(1)$ |
| Union | `s1 \| s2` or `s1.union(s2)` | $O(\|s1\| + \|s2\|)$ |
| Intersection | `s1 & s2` | $O(\min(\|s1\|, \|s2\|))$ |
| Difference | `s1 - s2` | $O(\|s1\|)$ |
| Symmetric diff. | `s1 ^ s2` | $O(\|s1\| + \|s2\|)$ |

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)   # Union.
print(a & b)   # Intersection.
print(a - b)   # Elements in a but not in b.
print(a ^ b)   # Elements in exactly one of the two sets.
```

```text
{1, 2, 3, 4, 5, 6}
{3, 4}
{1, 2}
{1, 2, 5, 6}
```

### 3.3 Comparison: `list`, `dict`, `set`

| Property | `list` | `dict` | `set` |
| :--- | :--- | :--- | :--- |
| Ordered | Yes (insertion order) | Yes (since Python 3.7) | No |
| Duplicates allowed | Yes | Keys: No; Values: Yes | No |
| Membership test | $O(n)$ | $O(1)$ on keys | $O(1)$ |
| Mutable | Yes | Yes | Yes |
| Key/index access | By integer index | By arbitrary hashable key | No direct access |
| Hashable elements required | No | Keys only | Yes |

---

## 4. List Comprehensions

### 4.1 Set-Builder Notation

List comprehensions are Python's syntactic expression of **set-builder notation** from mathematics. In mathematics, a set is described as:

$$S = \{ f(x) \mid x \in D,\ P(x) \}$$

where $f(x)$ is the output expression, $D$ is the domain (input set), and $P(x)$ is a predicate (filter condition).

Python's list comprehension mirrors this directly:

```
[<output_expression> for <variable> in <iterable> if <predicate>]
```

The `if` clause is optional. Multiple `for` clauses may be combined to form Cartesian products.

### 4.2 Syntax Reference

**Single-variable with filter:**

```
[f(x) for x in iterable if predicate(x)]
```

**Multiple variables (Cartesian product):**

```
[f(x, y) for x in iterable_1 for y in iterable_2]
```

**Nested comprehension (matrix construction):**

```
[[f(i, j) for j in range(cols)] for i in range(rows)]
```

### 4.3 Common Patterns

**Squares of integers from 1 to 10:**

```python
squares = [x**2 for x in range(1, 11)]
print(squares)
```

```text
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

**Even numbers from 1 to 20:**

```python
evens = [x for x in range(1, 21) if x % 2 == 0]
print(evens)
```

```text
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

**Cartesian product of two ranges:**

```python
pairs = [(x, y) for x in range(1, 4) for y in range(1, 4)]
print(pairs)
```

```text
[(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
```

**String processing — extract uppercase letters:**

```python
text = "Hello, World!"
uppers = [ch for ch in text if ch.isupper()]
print(uppers)
```

```text
['H', 'W']
```

### 4.4 Dictionary and Set Comprehensions

The same pattern extends to `dict` and `set` comprehensions:

```python
# Square mapping: {x: x^2} for x in 1..5.
square_map = {x: x**2 for x in range(1, 6)}
print(square_map)

# Set of unique first characters from a list of words.
words = ["apple", "avocado", "banana", "blueberry", "cherry"]
first_chars = {word[0] for word in words}
print(first_chars)
```

```text
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
{'a', 'b', 'c'}
```

> **[Key Insight]** A list comprehension `[expr for x in iterable]` is semantically equivalent to a `for` loop that appends to a list, but is substantially faster in CPython because the entire iteration is handled internally as a single optimized bytecode sequence (`LIST_APPEND`), avoiding the overhead of repeatedly calling `list.append`.

---

## 5. Decorators

### 5.1 Functions as First-Class Objects

In Python, functions are objects. They can be assigned to variables, stored in data structures, passed as arguments, and returned from other functions.

```python
def greet():
    return "Hello"

alias = greet           # `alias` now references the same function object.
print(alias())          # Calls the function through the alias.
print(type(greet))      # Confirms functions are objects.
```

```text
Hello
<class 'function'>
```

### 5.2 Higher-Order Functions and Closures

A **higher-order function** accepts another function as an argument or returns a function. A **closure** is a function that captures variables from its enclosing scope even after the enclosing function has returned.

```python
def make_multiplier(factor):
    """Returns a closure that multiplies its argument by `factor`."""
    def multiplier(x):
        return x * factor   # `factor` is captured from the enclosing scope.
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)
print(double(5))   # 10
print(triple(5))   # 15
```

```text
10
15
```

### 5.3 Decorator Syntax and Semantics

A **decorator** is syntactic sugar for wrapping a function with a higher-order function. The syntax:

```python
@decorator
def target():
    ...
```

is exactly equivalent to:

```python
def target():
    ...
target = decorator(target)
```

The decorator receives the original function object, wraps it in a new function (the **wrapper**), and returns the wrapper. From that point on, the name `target` refers to the wrapper.

**Minimal decorator template:**

```python
import functools

def my_decorator(func):
    @functools.wraps(func)   # Preserves the original function's metadata.
    def wrapper(*args, **kwargs):
        # Pre-call logic.
        result = func(*args, **kwargs)
        # Post-call logic.
        return result
    return wrapper
```

`@functools.wraps(func)` copies the `__name__`, `__doc__`, and `__module__` attributes from `func` to `wrapper`, which is essential for correct introspection.

### 5.4 Parameterized Decorators

A decorator factory is a function that returns a decorator, enabling the decorator to accept configuration arguments.

**Abstract syntax:**

```
def decorator_factory(<params>):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            ...
        return wrapper
    return decorator

@decorator_factory(<args>)
def target():
    ...
```

This is equivalent to `target = decorator_factory(<args>)(target)`.

---

## Solved Exercises

### Exercise 1: List Slicing and Negative Indexing

**Problem:** Given `lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`, evaluate each expression.

```python
lst[2:7]
lst[:4]
lst[6:]
lst[::2]
lst[::-1]
lst[-3:]
lst[1:8:3]
```

**Solution:**

| Expression | Result | Explanation |
| :--- | :--- | :--- |
| `lst[2:7]` | `[2, 3, 4, 5, 6]` | Indices 2 through 6 |
| `lst[:4]` | `[0, 1, 2, 3]` | From start through index 3 |
| `lst[6:]` | `[6, 7, 8, 9]` | From index 6 through end |
| `lst[::2]` | `[0, 2, 4, 6, 8]` | Every second element |
| `lst[::-1]` | `[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]` | Reversed; step $-1$ |
| `lst[-3:]` | `[7, 8, 9]` | Last three elements |
| `lst[1:8:3]` | `[1, 4, 7]` | Indices 1, 4, 7 |

---

### Exercise 2: Dictionary Safe Access Patterns

**Problem:** Given the following dictionary, write code that prints the value for `"phone"` if it exists, and `"Not found"` otherwise — in three different ways.

```python
contact = {"name": "Bob", "email": "bob@example.com"}
```

**Solution:**

```python
# Method 1: dict.get() with a default.
print(contact.get("phone", "Not found"))

# Method 2: Conditional membership test.
if "phone" in contact:
    print(contact["phone"])
else:
    print("Not found")

# Method 3: try/except KeyError.
try:
    print(contact["phone"])
except KeyError:
    print("Not found")
```

```text
Not found
Not found
Not found
```

All three produce the same result. `dict.get()` is the most idiomatic for simple defaults.

---

### Exercise 3: Set Operations for Deduplication

**Problem:** Given two lists with overlapping elements, find:
1. All unique elements across both lists.
2. Elements that appear in both lists.
3. Elements that appear in the first list but not the second.

```python
a = [1, 2, 3, 4, 2, 3]
b = [3, 4, 5, 6, 4]
```

**Solution:**

```python
set_a = set(a)   # {1, 2, 3, 4}
set_b = set(b)   # {3, 4, 5, 6}

print("Union:", set_a | set_b)
print("Intersection:", set_a & set_b)
print("Difference (a - b):", set_a - set_b)
```

```text
Union: {1, 2, 3, 4, 5, 6}
Intersection: {3, 4}
Difference (a - b): {1, 2}
```

Converting lists to sets both deduplicates and enables $O(1)$ membership tests.

---

### Exercise 4: List Comprehension — Squares of Evens

**Problem:** Using a single list comprehension, produce a list of the squares of all even numbers from 1 to 20.

**Solution:**

The mathematical set-builder form is:
$$S = \{ x^2 \mid x \in \{1, \ldots, 20\},\ x \equiv 0 \pmod{2} \}$$

```python
result = [x**2 for x in range(1, 21) if x % 2 == 0]
print(result)
```

```text
[4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
```

---

### Exercise 5: Cartesian Product via Comprehension

**Problem:** Generate all pairs $(x, y)$ where $x \in \{1, 2, 3\}$ and $y \in \{a, b\}$ using a list comprehension.

**Solution:**

$$S = \{ (x, y) \mid x \in \{1, 2, 3\},\ y \in \{"a", "b"\} \}$$

```python
pairs = [(x, y) for x in [1, 2, 3] for y in ["a", "b"]]
print(pairs)
```

```text
[(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b'), (3, 'a'), (3, 'b')]
```

The first `for` clause is the outer loop; the second is the inner loop. The total number of pairs is $|A| \times |B| = 3 \times 2 = 6$.

---

### Exercise 6: Timing Decorator

**Problem:** Implement a decorator `@timer` that prints the execution time of any decorated function. Apply it to a function that computes the sum of squares of the first $n$ integers.

**Solution:**

```python
import functools
import time

def timer(func):
    """Wraps `func` to print its wall-clock execution time."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()          # High-resolution timer start.
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed:.6f} seconds")
        return result
    return wrapper

@timer
def sum_of_squares(n):
    """Computes the sum of squares from 1 to n."""
    return sum(x**2 for x in range(1, n + 1))

print(sum_of_squares(1_000_000))
```

```text
sum_of_squares took 0.083412 seconds
333333833333500000
```

`time.perf_counter()` is preferred over `time.time()` for measuring short durations because it has higher resolution and is not affected by system clock adjustments.

---

### Exercise 7: Memoization Decorator

**Problem:** Implement a `@memoize` decorator that caches the return value of a function for previously seen argument tuples, and apply it to a recursive Fibonacci function to demonstrate performance improvement.

**Solution:**

```python
import functools

def memoize(func):
    """Caches results of `func` keyed by its argument tuple."""
    cache = {}   # Maps argument tuple to return value.
    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)   # Computes and stores only on first call.
        return cache[args]
    return wrapper

@memoize
def fib(n):
    """Computes the n-th Fibonacci number recursively."""
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print([fib(i) for i in range(10)])
```

```text
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

Without memoization, the naive recursive Fibonacci has time complexity $O(2^n)$. With memoization, each unique argument is computed exactly once, reducing complexity to $O(n)$.

> **[Supplementary]**
> Python's standard library provides `functools.lru_cache` as a built-in memoization decorator with an optional bound on cache size. `@functools.lru_cache(maxsize=None)` is equivalent to the manual `@memoize` above but is implemented in C and is therefore faster.

---

### Exercise 8: Nested Comprehension — Transposing a Matrix

**Problem:** Given a $3 \times 4$ matrix represented as a list of lists, produce its $4 \times 3$ transpose using a nested list comprehension.

**Solution:**

Let $M$ be the matrix:

$$M = \begin{pmatrix} 1 & 2 & 3 & 4 \\ 5 & 6 & 7 & 8 \\ 9 & 10 & 11 & 12 \end{pmatrix}$$

The transpose $M^T$ swaps rows and columns: $M^T_{ij} = M_{ji}$.

```python
M = [
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12]
]

rows = len(M)       # 3
cols = len(M[0])    # 4

M_T = [[M[r][c] for r in range(rows)] for c in range(cols)]

for row in M_T:
    print(row)
```

```text
[1, 5, 9]
[2, 6, 10]
[3, 7, 11]
[4, 8, 12]
```

The outer comprehension iterates over column indices `c`; the inner comprehension iterates over row indices `r`, collecting `M[r][c]` — the element at row `r`, column `c` of the original matrix.

---

## Exam Tip: Comprehension Evaluation Order and Decorator Identity

**Comprehension clause order:** In a multi-`for` comprehension, the leftmost `for` clause corresponds to the **outermost** loop. The expression `[(x, y) for x in A for y in B]` is equivalent to:

```python
result = []
for x in A:
    for y in B:
        result.append((x, y))
```

Reversing the order of `for` clauses changes which variable changes most slowly (outermost) vs. most rapidly (innermost).

**Decorator identity test:** In an exam scenario, given `@dec` applied to `f`, if `dec` does not use `@functools.wraps`, then `f.__name__` after decoration will be `"wrapper"` (or whatever the wrapper function is named), not `"f"`. This is a common source of test questions on decorators.

**`set` vs. `dict` comprehension disambiguation:** `{}` alone creates an empty `dict`, not an empty `set`. An empty `set` must be created with `set()`. The comprehension `{x for x in iterable}` is a set comprehension; `{k: v for k, v in iterable}` is a dict comprehension.
