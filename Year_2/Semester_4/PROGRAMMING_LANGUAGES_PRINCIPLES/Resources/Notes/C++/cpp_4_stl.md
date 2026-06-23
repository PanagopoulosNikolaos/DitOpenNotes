# C++ — Standard Template Library (STL)

*Prerequisite: cpp_1_basics_and_hardware.md — Pass-by-reference and `const` correctness.*
*Prerequisite: cpp_3_oop_resource_management.md — RAII, iterators as abstraction over pointers.*

The C++ Standard Template Library provides generic containers, iterators, and algorithms that compose into efficient, type-safe data-processing pipelines. This file covers `std::vector` as a dynamic array, the iterator abstraction (`begin()`/`end()`), `std::unordered_map` as a hash table with $O(1)$ average-case operations, the `<algorithm>` header (`count`, `count_if`, lambdas), and the sort, transform, and search primitives.

---

## 1. `std::vector` — Dynamic Array

### 1.1 Concept Overview

`std::vector<T>` is a sequence container that stores elements in a contiguous heap-allocated buffer. It provides amortized $O(1)$ append via `push_back()`, $O(1)$ random access via `operator[]`, and automatic resizing when capacity is exceeded.

### 1.2 Syntax Reference

**Declaration:**

```
std::vector<<type>> <name>;
std::vector<<type>> <name>(<count>, <value>);
std::vector<<type>> <name>{<elem1>, <elem2>, ...};
```

**Core operations:**

```
<name>.push_back(<value>)
<name>.pop_back()
<name>.size()
<name>.capacity()
<name>[<index>]
<name>.at(<index>)    // bounds-checked
```

### 1.3 Core Operations Reference Table

| Operation | Syntax | Time Complexity | Notes |
| :--- | :--- | :--- | :--- |
| Append | `v.push_back(x)` | $O(1)$ amortized | Reallocates occasionally |
| Remove last | `v.pop_back()` | $O(1)$ | Does not reduce capacity |
| Random access | `v[i]`, `v.at(i)` | $O(1)$ | `at` throws on out-of-range |
| Size | `v.size()` | $O(1)$ | Number of elements |
| Capacity | `v.capacity()` | $O(1)$ | Allocated slots |
| Insert at position | `v.insert(it, x)` | $O(n)$ | Shifts elements |
| Erase | `v.erase(it)` | $O(n)$ | Shifts elements |

```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int> v;
    v.push_back(10);
    v.push_back(20);
    v.push_back(30);

    std::cout << "size=" << v.size() << " capacity=" << v.capacity() << "\n";
    std::cout << v[0] << " " << v.back() << "\n";

    v.pop_back();
    std::cout << "after pop_back: size=" << v.size() << "\n";
    return 0;
}
```

```text
size=3 capacity=3
10 30
after pop_back: size=2
```

### 1.4 Internal Growth Strategy

When `size() == capacity()` and `push_back` is called, the vector allocates a larger buffer (typically growth factor $\approx 2$), moves/copies all elements, and frees the old buffer. Amortized analysis yields $O(1)$ per `push_back` over a sequence of appends.

---

## 2. Iterators — `begin()` and `end()`

### 2.1 Concept Overview

An **iterator** is a generalized pointer abstraction that traverses container elements. `begin()` returns an iterator to the first element; `end()` returns a **past-the-end** sentinel (not dereferenceable). The half-open range $[\texttt{begin()}, \texttt{end()})$ contains all elements.

### 2.2 Syntax Reference

```
auto <it> = <container>.begin();
auto <it> = <container>.end();
auto <it> = <container>.cbegin();   // const iterator
*<it>                                  // dereference
++<it>                                 // advance
<it1> != <it2>                         // inequality (end sentinel)
```

### 2.3 Iterator Category for `vector`

| Iterator Type | Declaration | Can Write? |
| :--- | :--- | :--- |
| `iterator` | `vector<T>::iterator` | Yes |
| `const_iterator` | `vector<T>::const_iterator` | No |
| Reverse | `vector<T>::reverse_iterator` | Yes (via `rbegin`) |

### 2.4 Pointer Arithmetic Abstraction

For `std::vector`, iterators behave like pointers: incrementing an iterator moves to the next contiguous element.

```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int> v = {10, 20, 30, 40, 50};

    // Iterator traversal.
    for (auto it = v.begin(); it != v.end(); ++it) {
        std::cout << *it << " ";
    }
    std::cout << "\n";

    // Range-based for (desugars to begin/end).
    for (int x : v) {
        std::cout << x << " ";
    }
    std::cout << "\n";
    return 0;
}
```

```text
10 20 30 40 50
10 20 30 40 50
```

### 2.5 Half-Open Range Convention

```
Elements:  [ v[0], v[1], v[2], ..., v[n-1] ]
Iterators:   ^                        ^   ^
           begin()                  end()-1  end() (sentinel)
```

> **[Key Insight]** Algorithms in `<algorithm>` operate on half-open ranges `[first, last)`. The iterator `last` is never dereferenced. This convention unifies insertion, erasure, and search across all STL containers.

---

## 3. `std::unordered_map` — Hash Table

### 3.1 Concept Overview

`std::unordered_map<Key, Value>` implements an associative container as a **hash table** with average-case $O(1)$ insert, lookup, and delete. Keys must be hashable (have `std::hash` specialization and `operator==`). Iteration order is undefined.

### 3.2 Syntax Reference

```
std::unordered_map<<Key>, <Value>> <name>;
<name>[<key>]              // insert or update
<name>.at(<key>)           // access with exception on missing key
<name>.find(<key>)         // returns iterator
<name>.count(<key>)        // 0 or 1
<name>.erase(<key>)
```

### 3.3 Operations Reference Table

| Operation | Syntax | Average Time | Worst Case |
| :--- | :--- | :--- | :--- |
| Insert / update | `m[k] = v` | $O(1)$ | $O(n)$ |
| Lookup | `m.at(k)`, `m.find(k)` | $O(1)$ | $O(n)$ |
| Delete | `m.erase(k)` | $O(1)$ | $O(n)$ |
| Membership | `m.count(k)` | $O(1)$ | $O(n)$ |
| Iterate | `for (auto &p : m)` | $O(n)$ | $O(n)$ |

```cpp
#include <iostream>
#include <string>
#include <unordered_map>

int main() {
    std::unordered_map<std::string, int> grades;
    grades["Alice"] = 95;
    grades["Bob"]   = 87;
    grades["Carol"] = 92;

    std::cout << grades["Alice"] << "\n";
    std::cout << grades.count("Dave") << "\n";   // 0 — not found.

    for (const auto &pair : grades) {
        std::cout << pair.first << ": " << pair.second << "\n";
    }
    return 0;
}
```

```text
95
0
Carol: 92
Bob: 87
Alice: 95
```

### 3.4 Comparison: `unordered_map` vs. `map`

| Property | `unordered_map` | `map` |
| :--- | :--- | :--- |
| Underlying structure | Hash table | Red-black tree |
| Average insert/lookup | $O(1)$ | $O(\log n)$ |
| Key ordering | None | Sorted by key |
| Iterator stability | Rehash may invalidate | Stable except erased |

---

## 4. The `<algorithm>` Header

### 4.1 Concept Overview

`<algorithm>` provides function templates that operate on iterator ranges. They are generic: the same `std::sort` works on `vector`, raw arrays (via pointers), and other random-access containers.

### 4.2 `count` and `count_if`

**Syntax:**

```
std::count(<first>, <last>, <value>)
std::count_if(<first>, <last>, <predicate>)
```

| Function | Returns | Predicate |
| :--- | :--- | :--- |
| `count` | Number of elements equal to `value` | None (equality) |
| `count_if` | Number of elements satisfying predicate | Unary function / lambda returning `bool` |

```cpp
#include <algorithm>
#include <iostream>
#include <vector>

int main() {
    std::vector<int> v = {1, 2, 3, 4, 5, 4, 3, 2, 1};

    int n_even = std::count_if(v.begin(), v.end(),
        [](int x) { return x % 2 == 0; });

    int n_four = std::count(v.begin(), v.end(), 4);

    std::cout << "evens: " << n_even << ", fours: " << n_four << "\n";
    return 0;
}
```

```text
evens: 4, fours: 2
```

### 4.3 Lambda Expressions

**Syntax:**

```
[<capture>](<params>) -> <return_type> { <body> }
```

| Capture | Meaning |
| :--- | :--- |
| `[]` | No capture |
| `[=]` | Capture all by value |
| `[&]` | Capture all by reference |
| `[x]` | Capture `x` by value |
| `[&x]` | Capture `x` by reference |

Lambdas are the standard way to pass inline predicates to `count_if`, `sort` comparators, and `transform` functions.

---

## 5. Sort, Transform, and Search Primitives

### 5.1 `std::sort`

**Syntax:**

```
std::sort(<first>, <last>)
std::sort(<first>, <last>, <comparator>)
```

- Requires random-access iterators.
- Average complexity: $O(n \log n)$ (introsort).
- Not stable — equal elements may be reordered. Use `std::stable_sort` for stability.

```cpp
#include <algorithm>
#include <iostream>
#include <vector>

int main() {
    std::vector<int> v = {5, 1, 4, 2, 8};
    std::sort(v.begin(), v.end());
    for (int x : v) std::cout << x << " ";
    std::cout << "\n";

    // Descending with lambda comparator.
    std::sort(v.begin(), v.end(), [](int a, int b) { return a > b; });
    for (int x : v) std::cout << x << " ";
    std::cout << "\n";
    return 0;
}
```

```text
1 2 4 5 8
8 5 4 2 1
```

### 5.2 `std::transform`

**Syntax:**

```
std::transform(<first1>, <last1>, <result>, <unary_op>)
std::transform(<first1>, <last1>, <first2>, <result>, <binary_op>)
```

Applies a function to each element and writes the result to the output range starting at `result`. The output container must be large enough.

```cpp
#include <algorithm>
#include <iostream>
#include <vector>

int main() {
    std::vector<int> src = {1, 2, 3, 4, 5};
    std::vector<int> dst(5);

    std::transform(src.begin(), src.end(), dst.begin(),
        [](int x) { return x * x; });

    for (int x : dst) std::cout << x << " ";
    std::cout << "\n";
    return 0;
}
```

```text
1 4 9 16 25
```

### 5.3 Search Primitives

| Function | Syntax | Returns |
| :--- | :--- | :--- |
| `find` | `find(first, last, value)` | Iterator to first match, or `last` |
| `find_if` | `find_if(first, last, pred)` | Iterator to first satisfying predicate |
| `binary_search` | `binary_search(first, last, value)` | `bool` — requires sorted range |
| `lower_bound` | `lower_bound(first, last, value)` | Iterator to first element $\geq$ value |

```cpp
#include <algorithm>
#include <iostream>
#include <vector>

int main() {
    std::vector<int> v = {10, 20, 30, 40, 50};

    auto it = std::find(v.begin(), v.end(), 30);
    if (it != v.end())
        std::cout << "found at index "
                  << (it - v.begin()) << "\n";

    auto it2 = std::find_if(v.begin(), v.end(),
        [](int x) { return x > 35; });
    if (it2 != v.end())
        std::cout << "first > 35: " << *it2 << "\n";
    return 0;
}
```

```text
found at index 2
first > 35: 40
```

### 5.4 Algorithm Composition Pipeline

A typical STL pipeline chains containers, iterators, and algorithms:

```
vector (data) → sort (mutate) → count_if (query) → transform (map) → output
```

```cpp
#include <algorithm>
#include <iostream>
#include <vector>

int main() {
    std::vector<int> data = {3, 1, 4, 1, 5, 9, 2, 6};
    std::sort(data.begin(), data.end());

    int duplicates = data.size() - std::unique(data.begin(), data.end()) + data.begin() - data.begin();
    // After sort, count elements > 4:
    int gt4 = std::count_if(data.begin(), data.end(),
        [](int x) { return x > 4; });

    std::cout << "sorted, count > 4: " << gt4 << "\n";
    for (int x : data) std::cout << x << " ";
    std::cout << "\n";
    return 0;
}
```

```text
sorted, count > 4: 3
1 1 2 3 4 5 6 9
```

---

## Common Errors and Gotchas

### Error 1: Dereferencing `end()`

**Cause:** `*v.end()` is undefined behavior; `end()` is a past-the-end sentinel.

**Resolution:** Dereference only iterators known to be within `[begin(), end())`.

### Error 2: Iterator Invalidation on `vector` Reallocation

**Cause:** After `push_back` causes reallocation, all iterators, pointers, and references to elements are invalidated.

**Resolution:** Re-acquire `begin()` after modifications, or `reserve()` upfront to prevent reallocation.

### Error 3: `operator[]` Inserts into `unordered_map`

**Cause:** `m["missing_key"]` default-constructs and inserts the key if absent — unintended mutation.

**Resolution:** Use `m.find(k) != m.end()` or `m.at(k)` (throws `std::out_of_range`) for read-only lookup.

---

## Solved Exercises

### Exercise 1: Vector Growth

**Problem:** Start with an empty `vector<int>`. After pushing 5 elements, if capacity starts at 0 and doubles on each reallocation, what is the capacity after the 5th `push_back`?

**Solution:**

| Push # | Size | Capacity (doubling) |
| :--- | :--- | :--- |
| 1 | 1 | 1 |
| 2 | 2 | 2 |
| 3 | 3 | 4 |
| 4 | 4 | 4 |
| 5 | 5 | 8 |

Capacity after 5th push: **8**.

---

### Exercise 2: Iterator Distance

**Problem:** For `vector<int> v = {10, 20, 30}`, what is `v.end() - v.begin()`?

**Solution:**

1. The half-open range contains 3 elements.
2. Iterator difference (random-access): `end() - begin() = 3`.

---

### Exercise 3: `count_if` Predicate

**Problem:** Count elements divisible by 3 in `{9, 4, 6, 2, 3, 11}`.

**Solution:**

```cpp
std::count_if(v.begin(), v.end(), [](int x) { return x % 3 == 0; })
```

Elements divisible by 3: 9, 6, 3 → count = **3**.

---

### Exercise 4: `unordered_map` Lookup Safety

**Problem:** Distinguish the behavior of `grades["Dave"]` vs. `grades.at("Dave")` when Dave is absent.

**Solution:**

1. `grades["Dave"]` — inserts `{"Dave", 0}` (value-initialized `int`) and returns 0.
2. `grades.at("Dave")` — throws `std::out_of_range`.
3. For read-only test: use `grades.count("Dave")` (returns 0) or `find`.

---

### Exercise 5: Custom Sort Comparator

**Problem:** Sort strings `{"pear", "apple", "fig"}` by length ascending using `std::sort`.

**Solution:**

```cpp
std::sort(words.begin(), words.end(),
    [](const std::string &a, const std::string &b) {
        return a.size() < b.size();
    });
```

Result: `{"fig", "pear", "apple"}` (lengths 3, 4, 5).

---

### Exercise 6: `transform` Output Sizing

**Problem:** `src` has 4 elements. `dst` is default-constructed (size 0). What happens?

```cpp
std::vector<int> dst;
std::transform(src.begin(), src.end(), dst.begin(), [](int x){ return x * 2; });
```

**Solution:**

1. `dst.begin()` on an empty vector is not a valid output range.
2. **Undefined behavior** — writes past the end of zero capacity.
3. **Fix:** `dst.resize(src.size());` or construct `dst` with sufficient size before `transform`.

---

### Exercise 7: `find` Return Value

**Problem:** `find` does not locate the value in `{1, 3, 5, 7}`. What does it return?

**Solution:**

1. `find` returns the `last` argument (i.e., `v.end()`) when no match is found.
2. Check: `if (it != v.end())` before dereferencing.

---

### Exercise 8: Algorithm Complexity Pipeline

**Problem:** A `vector` of $n$ elements is sorted, then `count_if` scans the result. State the total time complexity.

**Solution:**

1. `std::sort`: $O(n \log n)$.
2. `std::count_if`: $O(n)$.
3. Total: $O(n \log n)$ — dominated by sort.

---

## Exam Tip: Half-Open Ranges and `operator[]` Side Effects

**Half-open range invariant:** Every STL algorithm taking `[first, last)` treats `last` as **one past the final element**. If a container has $n$ elements, `end() - begin() == n$. Off-by-one errors on paper usually come from treating `end()` as the last valid index.

**`unordered_map::operator[]` trap:** This operator **inserts** a default-constructed value for missing keys. On exams, `m["key"]` when `key` is absent both returns 0 (for `int` values) **and** increases `m.size()` by 1. Use `count` or `find` when the question asks for a lookup without modification.

**Iterator invalidation summary for `vector`:**

| Operation | Iterators Invalidated? |
| :--- | :--- |
| `push_back` (no reallocation) | No |
| `push_back` (reallocation) | All |
| `insert` / `erase` | At and after insertion/erasure point |
| `clear` | All |

**Lambda capture exam pattern:** `[=]` captures a copy; modifications inside the lambda to a captured `int x` do not affect the outer `x`. `[&]` captures by reference; modifications are visible outside.