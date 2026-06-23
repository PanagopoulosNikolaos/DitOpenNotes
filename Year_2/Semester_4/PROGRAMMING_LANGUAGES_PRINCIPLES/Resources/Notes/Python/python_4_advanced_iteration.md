# Python — Advanced Iteration and Memory Efficiency

*Prerequisite: python_1_basics.md — Functions, the heap-bound object model, and bytecode evaluation costs.*
*Prerequisite: python_2_intermediate.md — List comprehensions and the iterator protocol.*

Python's iteration system is built on a two-protocol model — the **iterable** and **iterator** protocols — that enables lazy, memory-efficient data processing. This file covers generators and lazy evaluation as a mechanism for reducing heap allocation, the `itertools` module's infinite, combinatoric, and terminating iterators, and the performance rationale for delegating tight loops to native C-level implementations.

---

## 1. The Iterator Protocol

### 1.1 Iterable vs. Iterator

Two distinct concepts underlie Python's `for` loop:

| Concept | Required Method | Description |
| :--- | :--- | :--- |
| **Iterable** | `__iter__()` | An object that can produce an iterator; may be traversed multiple times |
| **Iterator** | `__iter__()` + `__next__()` | An object that tracks traversal state; raises `StopIteration` when exhausted |

An **iterator** is also an **iterable** (it returns `self` from `__iter__`), but an iterable is not necessarily an iterator.

**Protocol equivalences:**

| Syntax | Underlying Call |
| :--- | :--- |
| `iter(obj)` | `obj.__iter__()` |
| `next(it)` | `it.__next__()` |
| `for x in obj: ...` | `it = iter(obj)` then repeated `next(it)` until `StopIteration` |

```python
lst = [10, 20, 30]
it = iter(lst)            # Creates a list_iterator object.
print(next(it))           # 10 — advances the iterator.
print(next(it))           # 20
print(next(it))           # 30
# next(it)               # Would raise StopIteration here.
```

```text
10
20
30
```

### 1.2 Custom Iterator Class

```python
class Countdown:
    """An iterator that counts down from a starting value to zero."""

    def __init__(self, start):
        self.current = start

    def __iter__(self):
        """Returns self; the iterator is its own iterable."""
        return self

    def __next__(self):
        """Returns the next value in the countdown.

        Raises:
            StopIteration: When the countdown reaches below zero.
        """
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1   # Advances internal state.
        return value

for n in Countdown(5):
    print(n, end=" ")
```

```text
5 4 3 2 1 0
```

---

## 2. Generators and Lazy Evaluation

### 2.1 Generator Functions

A **generator function** is a function that contains at least one `yield` statement. When called, it does not execute its body immediately; instead, it returns a **generator object** (which is both an iterable and an iterator).

**Execution model:**

1. The generator body executes up to the first `yield` and **suspends** — the local variable state is preserved on a dedicated frame object on the heap.
2. Each call to `next()` on the generator resumes execution from the suspension point, runs until the next `yield`, and suspends again.
3. When the function body returns (or falls off the end), `StopIteration` is raised automatically.

```python
def count_up(limit):
    """Yields integers from 0 up to limit (inclusive), one at a time."""
    n = 0
    while n <= limit:
        yield n     # Suspends here; n and limit are preserved in the frame.
        n += 1

gen = count_up(4)
print(type(gen))    # <class 'generator'>
print(next(gen))    # 0
print(next(gen))    # 1
print(list(gen))    # Materializes the remaining values: [2, 3, 4]
```

```text
<class 'generator'>
0
1
[2, 3, 4]
```

### 2.2 Lazy Evaluation and Memory Efficiency

The critical property of generators is **lazy evaluation**: values are produced **one at a time, on demand**, rather than all at once. This means a generator that would logically produce a million integers does not allocate a list of a million integers — it allocates a single frame object regardless of the sequence length.

**Comparison — list vs. generator:**

```python
import sys

# Eager evaluation: all 1,000,000 integers are computed and stored immediately.
eager = [x**2 for x in range(1_000_000)]

# Lazy evaluation: no computation occurs until values are consumed.
lazy = (x**2 for x in range(1_000_000))   # Generator expression (parentheses).

print(f"List size:      {sys.getsizeof(eager):>12} bytes")
print(f"Generator size: {sys.getsizeof(lazy):>12} bytes")
```

```text
List size:       8448728 bytes
Generator size:       112 bytes
```

> **[Key Insight]** The generator object itself has a constant memory footprint (the frame object and a small amount of overhead) regardless of how many values it will produce. The list must hold a reference to every computed object simultaneously.

### 2.3 Generator Expressions

A **generator expression** has the same syntax as a list comprehension but uses parentheses instead of square brackets. It produces a generator object rather than a list.

```
(<output_expression> for <variable> in <iterable> [if <predicate>])
```

```python
total = sum(x**2 for x in range(1, 1001))   # No intermediate list is created.
print(total)
```

```text
333833500
```

### 2.4 `yield from`

`yield from <iterable>` delegates iteration to a sub-iterable, yielding all of its values in turn. It is equivalent to a `for` loop with `yield` inside, but is more efficient and properly forwards `send()`, `throw()`, and `close()` to the sub-generator.

```python
def chain_sequences(*iterables):
    """Yields all elements from each iterable in sequence."""
    for it in iterables:
        yield from it   # Delegates to each sub-iterable.

for value in chain_sequences([1, 2], [3, 4], [5]):
    print(value, end=" ")
```

```text
1 2 3 4 5
```

---

## 3. The `itertools` Module

The `itertools` module provides a collection of fast, memory-efficient iterators implemented in C. These iterators process elements lazily and compose with each other and with standard Python iterators.

> **[Supplementary]**
> All `itertools` iterators are **lazy**: they compute the next value only when `next()` is called. They are designed to be composed as building blocks — this is often called **iterator algebra**.

### 3.1 Infinite Iterators

Infinite iterators produce an unbounded sequence. They must always be paired with a termination mechanism (e.g., `islice`, `takewhile`, `break`).

#### `itertools.count(start=0, step=1)`

Produces an arithmetic sequence starting at `start`, incrementing by `step`, without end.

**Signature:**
```
count(start=0, step=1) → count object
```

```python
import itertools

counter = itertools.count(10, 5)   # Starts at 10, increments by 5.
print([next(counter) for _ in range(5)])
```

```text
[10, 15, 20, 25, 30]
```

#### `itertools.cycle(iterable)`

Cycles through the elements of `iterable` indefinitely.

```python
cycler = itertools.cycle(["A", "B", "C"])
print([next(cycler) for _ in range(7)])
```

```text
['A', 'B', 'C', 'A', 'B', 'C', 'A']
```

#### `itertools.repeat(object, times=None)`

Yields `object` either `times` times (if specified) or indefinitely.

```python
print(list(itertools.repeat(0, 5)))   # [0, 0, 0, 0, 0]
```

```text
[0, 0, 0, 0, 0]
```

**Infinite iterator summary:**

| Function | Output Pattern | Stops When |
| :--- | :--- | :--- |
| `count(n, s)` | $n,\ n+s,\ n+2s,\ \ldots$ | Never (must terminate externally) |
| `cycle(it)` | Repeats `it` cyclically | Never |
| `repeat(obj, n)` | $obj$ repeated $n$ times | After $n$ iterations (or never) |

---

### 3.2 Combinatoric Iterators

Combinatoric iterators produce tuples of elements drawn from a pool according to combinatoric rules (product, permutations, combinations).

#### `itertools.product(*iterables, repeat=1)`

Computes the Cartesian product of input iterables. Equivalent to nested `for` loops.

$$\text{product}(A, B) = \{ (a, b) \mid a \in A,\ b \in B \}$$

```python
result = list(itertools.product([1, 2], ["a", "b"]))
print(result)
```

```text
[(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]
```

The `repeat` keyword argument specifies the number of times the input is repeated for the product:

```python
# Equivalent to product([0,1], [0,1]) — all 2-bit binary patterns.
print(list(itertools.product([0, 1], repeat=2)))
```

```text
[(0, 0), (0, 1), (1, 0), (1, 1)]
```

#### `itertools.permutations(iterable, r=None)`

Produces all ordered arrangements of `r` elements from the iterable. If `r` is omitted, uses all elements.

$$P(n, r) = \frac{n!}{(n-r)!}$$

```python
result = list(itertools.permutations([1, 2, 3], 2))
print(result)
print(f"Count: {len(result)}")  # P(3,2) = 3! / 1! = 6
```

```text
[(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
Count: 6
```

#### `itertools.combinations(iterable, r)`

Produces all unordered selections of `r` elements from the iterable (no repetition). Order within a tuple is not significant; each subset appears exactly once.

$$C(n, r) = \binom{n}{r} = \frac{n!}{r!(n-r)!}$$

```python
result = list(itertools.combinations([1, 2, 3, 4], 2))
print(result)
print(f"Count: {len(result)}")  # C(4,2) = 6
```

```text
[(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
Count: 6
```

#### `itertools.combinations_with_replacement(iterable, r)`

Same as `combinations` but elements may be repeated.

$$C_R(n, r) = \binom{n+r-1}{r}$$

```python
result = list(itertools.combinations_with_replacement([1, 2, 3], 2))
print(result)
```

```text
[(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]
```

**Combinatoric iterator summary:**

| Function | Description | Count formula |
| :--- | :--- | :--- |
| `product(A, r=n)` | Cartesian product, with repetition | $\|A\|^n$ |
| `permutations(A, r)` | Ordered selections, no repetition | $P(\|A\|, r)$ |
| `combinations(A, r)` | Unordered selections, no repetition | $C(\|A\|, r)$ |
| `combinations_with_replacement(A, r)` | Unordered selections, with repetition | $C_R(\|A\|, r)$ |

---

### 3.3 Terminating Iterators

Terminating iterators process finite input sequences, applying transformations, filters, or aggregations.

#### `itertools.accumulate(iterable, func=operator.add, *, initial=None)`

Produces cumulative results of applying `func`. Default `func` is addition, producing running sums.

```python
import operator

data = [1, 2, 3, 4, 5]
print(list(itertools.accumulate(data)))                            # Running sum.
print(list(itertools.accumulate(data, operator.mul)))              # Running product.
print(list(itertools.accumulate(data, initial=0)))                 # With initial value.
```

```text
[1, 3, 6, 10, 15]
[1, 2, 6, 24, 120]
[0, 1, 3, 6, 10, 15]
```

#### `itertools.chain(*iterables)`

Chains multiple iterables together, yielding elements from each in sequence. Does not materialize a new list.

```python
result = list(itertools.chain([1, 2], [3, 4], [5, 6]))
print(result)
```

```text
[1, 2, 3, 4, 5, 6]
```

#### `itertools.islice(iterable, stop)` / `islice(iterable, start, stop[, step])`

Yields a slice of an iterator without materializing the preceding elements. This is the standard way to safely consume a prefix of an infinite iterator.

```python
# Takes the first 5 values from an infinite counter.
result = list(itertools.islice(itertools.count(0), 5))
print(result)

# Takes every other element from index 2 to 10.
result = list(itertools.islice(range(20), 2, 10, 2))
print(result)
```

```text
[0, 1, 2, 3, 4]
[2, 4, 6, 8]
```

#### `itertools.groupby(iterable, key=None)`

Groups consecutive elements with the same key value. The input must be **sorted** by the key for correct grouping.

```python
data = [("A", 1), ("A", 2), ("B", 3), ("B", 4), ("C", 5)]

for key, group in itertools.groupby(data, key=lambda x: x[0]):
    print(key, list(group))
```

```text
A [('A', 1), ('A', 2)]
B [('B', 3), ('B', 4)]
C [('C', 5)]
```

**Terminating iterator summary:**

| Function | Effect |
| :--- | :--- |
| `accumulate(it, f)` | Running application of `f`; default is cumulative sum |
| `chain(*its)` | Concatenates iterables without copying |
| `islice(it, start, stop, step)` | Slices an iterator (works on infinite iterators) |
| `groupby(it, key)` | Groups consecutive equal-key elements |
| `filterfalse(pred, it)` | Yields elements for which `pred` is `False` |
| `dropwhile(pred, it)` | Drops elements while `pred` is `True`, then yields all remaining |
| `takewhile(pred, it)` | Yields elements while `pred` is `True`, then stops |
| `starmap(func, it)` | Applies `func(*args)` for each tuple in `it` |
| `zip_longest(*its, fillvalue)` | Zips iterables, filling shorter ones with `fillvalue` |

---

## 4. Shifting Execution to Native C Loops

### 4.1 The Performance Gap

The bytecode evaluation overhead described in `python_1_basics.md` is most visible in tight loops. Each Python-level iteration involves:

- Fetching the iterator object.
- Calling `__next__` (a method dispatch through the object protocol).
- Performing the operation (type lookup, dispatch, allocation).
- Storing the result.

When these steps are repeated millions of times, the cumulative overhead dominates execution time.

**The resolution:** Replace Python-level iteration with operations that execute their inner loop entirely in native C code. `itertools` functions are the primary built-in mechanism for this; NumPy provides the same benefit for numerical computation.

### 4.2 Why `itertools` Functions Are Fast

Each `itertools` function is a C extension type. Its `tp_iternext` slot — the C-level equivalent of `__next__` — executes directly in the CPython interpreter without re-entering the Python evaluation loop for each element. The overhead per element is therefore comparable to a C `for` loop iteration, not a Python bytecode iteration sequence.

```python
import time
import itertools

N = 10_000_000

# Python-level loop: accumulates a running sum via Python bytecode.
start = time.perf_counter()
total = 0
for i in range(N):
    total += i
python_time = time.perf_counter() - start

# C-level loop via itertools.accumulate: the summation runs inside C.
start = time.perf_counter()
result = None
for result in itertools.accumulate(range(N)):
    pass   # The accumulation itself occurs in C.
c_time = time.perf_counter() - start

print(f"Python loop:  {python_time:.3f}s")
print(f"itertools:    {c_time:.3f}s")
```

```text
Python loop:  0.412s
itertools:    0.218s
```

> **[Key Insight]** The `sum()` built-in function is the canonical example of a C-level loop. `sum(range(N))` is significantly faster than a Python `for` loop accumulating into a variable, because `sum` iterates in C. Similarly, `max()`, `min()`, `sorted()`, `map()`, `filter()`, and all `itertools` functions push their hot path into C.

---

## Solved Exercises

### Exercise 1: Manual Iterator Implementation

**Problem:** Implement a class `FibonacciIterator` that yields the Fibonacci sequence indefinitely. Consume the first 10 values using `itertools.islice`.

**Solution:**

The Fibonacci sequence is defined by the recurrence:
$$F_0 = 0,\quad F_1 = 1,\quad F_n = F_{n-1} + F_{n-2} \quad \text{for } n \geq 2$$

```python
import itertools

class FibonacciIterator:
    """An infinite iterator yielding Fibonacci numbers in sequence."""

    def __init__(self):
        self._a = 0   # F_{n-1}
        self._b = 1   # F_n

    def __iter__(self):
        return self

    def __next__(self):
        """Yields the next Fibonacci number and advances internal state."""
        value = self._a
        self._a, self._b = self._b, self._a + self._b   # Simultaneous update.
        return value

fib = FibonacciIterator()
print(list(itertools.islice(fib, 10)))
```

```text
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

---

### Exercise 2: Generator Function for Fibonacci

**Problem:** Re-implement the Fibonacci sequence as a generator function. Show that the generator expression form is equivalent.

**Solution:**

```python
def fibonacci():
    """Generates the Fibonacci sequence lazily."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b   # Simultaneous update avoids a temporary variable.

import itertools
print(list(itertools.islice(fibonacci(), 10)))
```

```text
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

The generator function is more readable than the class-based iterator and produces identical results. The `while True` loop with `yield` is the standard pattern for infinite generators.

---

### Exercise 3: Memory Comparison — List vs. Generator

**Problem:** Measure the memory footprint of computing the sum of squares of the first $10^6$ integers using a list comprehension vs. a generator expression.

**Solution:**

```python
import sys
import time

N = 1_000_000

# Approach 1: List comprehension — materializes all values.
start = time.perf_counter()
squares_list = [x**2 for x in range(N)]
total_list = sum(squares_list)
t1 = time.perf_counter() - start
mem1 = sys.getsizeof(squares_list)

# Approach 2: Generator expression — computes values on demand.
start = time.perf_counter()
total_gen = sum(x**2 for x in range(N))
t2 = time.perf_counter() - start

print(f"List:      total={total_list}, time={t1:.3f}s, memory={mem1:,} bytes")
print(f"Generator: total={total_gen}, time={t2:.3f}s, memory=O(1)")
```

```text
List:      total=333332833333500000, time=0.184s, memory=8,448,728 bytes
Generator: total=333332833333500000, time=0.102s, memory=O(1)
```

The generator produces the same result with constant memory and lower time (no intermediate list allocation).

---

### Exercise 4: `itertools.product` for Brute Force Search

**Problem:** Use `itertools.product` to find all combinations of digits $(d_1, d_2, d_3)$ where $d_i \in \{0, \ldots, 9\}$ and $d_1 + d_2 + d_3 = 15$.

**Solution:**

The search space is $10^3 = 1000$ combinations.

```python
digits = range(10)
solutions = [
    (a, b, c)
    for a, b, c in itertools.product(digits, repeat=3)
    if a + b + c == 15
]
print(f"Count: {len(solutions)}")
print(f"First 5: {solutions[:5]}")
```

```text
Count: 73
First 5: [(0, 6, 9), (0, 7, 8), (0, 8, 7), (0, 9, 6), (1, 5, 9)]
```

---

### Exercise 5: `itertools.accumulate` for Running Statistics

**Problem:** Given a stream of measurements, compute the running maximum and the running cumulative sum.

**Solution:**

```python
import operator

measurements = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

running_sum = list(itertools.accumulate(measurements))
running_max = list(itertools.accumulate(measurements, max))

print("Measurements: ", measurements)
print("Running sum:  ", running_sum)
print("Running max:  ", running_max)
```

```text
Measurements:  [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
Running sum:   [3, 4, 8, 9, 14, 23, 25, 31, 36, 39]
Running max:   [3, 3, 4, 4, 5, 9, 9, 9, 9, 9]
```

---

### Exercise 6: `itertools.chain` for Flat Iteration

**Problem:** Given a list of lists (a 2D structure), iterate over all elements in row-major order without constructing a flat list. Compute the total count and sum.

**Solution:**

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flat = itertools.chain.from_iterable(matrix)   # chain.from_iterable accepts a single iterable of iterables.
# Equivalent to: itertools.chain(*matrix), but works when matrix is itself a generator.

# Since flat is a generator, it can only be consumed once.
flat_list = list(flat)
print(f"Elements: {flat_list}")
print(f"Count: {len(flat_list)}, Sum: {sum(flat_list)}")
```

```text
Elements: [1, 2, 3, 4, 5, 6, 7, 8, 9]
Count: 9, Sum: 45
```

---

### Exercise 7: `itertools.groupby` for Frequency Counting

**Problem:** Given a sorted list of strings, use `itertools.groupby` to count the frequency of each unique string.

**Solution:**

```python
words = sorted(["apple", "banana", "apple", "cherry", "banana", "apple"])

for word, group in itertools.groupby(words):
    count = sum(1 for _ in group)   # Exhausts the group iterator to count elements.
    print(f"{word}: {count}")
```

```text
apple: 3
banana: 2
cherry: 1
```

> **[Key Insight]** `groupby` groups only **consecutive** equal elements. If the input is not sorted, elements with the same key may appear in multiple separate groups. Always sort by the grouping key before calling `groupby`.

---

### Exercise 8: Combining `itertools` Primitives — Sliding Window

**Problem:** Implement a `sliding_window(iterable, n)` generator that yields all consecutive windows of size `n` from the input, using only `itertools` primitives.

**Solution:**

```python
from collections import deque

def sliding_window(iterable, n):
    """Yields consecutive overlapping tuples of length n from iterable.

    Args:
        iterable: Any iterable input sequence.
        n (int): The window size.

    Yields:
        tuple: Each consecutive window of n elements.
    """
    it = iter(iterable)
    window = deque(itertools.islice(it, n), maxlen=n)   # Fill the initial window.
    if len(window) == n:
        yield tuple(window)
    for element in it:
        window.append(element)   # deque with maxlen automatically drops the oldest element.
        yield tuple(window)

data = [1, 2, 3, 4, 5, 6, 7]
print(list(sliding_window(data, 3)))
```

```text
[(1, 2, 3), (2, 3, 4), (3, 4, 5), (4, 5, 6), (5, 6, 7)]
```

This pattern is a standard idiom for stream processing and is available as `itertools.pairwise` (for $n=2$) in Python 3.10+. The general form requires manual composition as shown above.

> **[Supplementary]**
> Python 3.10 introduced `itertools.pairwise(iterable)`, which is equivalent to `sliding_window(iterable, 2)` implemented in C. For window sizes greater than 2, the `collections.deque`-based pattern above remains the standard approach.

---

## Exam Tip: Generator Exhaustion and `itertools.groupby` Pre-Sort

**Generator exhaustion:** A generator object can be iterated only **once**. After raising `StopIteration`, subsequent calls to `next()` continue to raise `StopIteration` — the generator does not reset. Converting a generator to a `list` exhausts it. Any code that attempts to iterate a generator a second time will silently see an empty sequence.

```python
gen = (x for x in range(5))
print(list(gen))   # [0, 1, 2, 3, 4]
print(list(gen))   # [] — generator is exhausted.
```

**`groupby` pre-sort requirement:** The most common exam and practical mistake with `groupby` is omitting the sort step. `groupby` is a streaming operator; it sees only the current element and the previous element. If identical keys appear non-consecutively, they produce multiple groups:

```python
data = ["a", "b", "a"]   # Not sorted.
for k, g in itertools.groupby(data):
    print(k, list(g))
# Output: a ['a'], b ['b'], a ['a']  — "a" appears in two groups.
```

To obtain one group per unique key, always call `sorted(data, key=key_func)` before `groupby(data, key=key_func)`.

**`islice` for infinite iterators:** `islice` is the correct way to take a finite prefix from an infinite iterator. Never use `list()` directly on an infinite iterator — it will consume memory until the process terminates.
