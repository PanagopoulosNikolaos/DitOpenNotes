# Multi-Paradigm Computer Science Curriculum (Mindmap)

* **Python**
  * Basics
    * Variables, loops, functions
    * Dynamic typing & arithmetic expressions
    * Dynamically typed memory model (heap-bound objects)
    * Control flow: `for` / `while` loops
    * Bytecode evaluation costs
  * Intermediate
    * Lists, dictionaries, sets
    * `dict` → C-struct hash tables → avg O(1) insert/lookup
    * List comprehensions (set-builder notation)
    * Decorators
    * Examples: squares, evens, Cartesian products
  * Object-Oriented Programming
    * Classes, objects, instance attributes, `self`
    * Magic / dunder methods (`__init__`, `__repr__`)
    * Inheritance & `super()` / MRO
    * Encapsulation: `_protected`, `__name_mangling`
    * `@property` decorator (getter/setter abstraction)
    * Static vs. instance attributes, class methods
    * Composition & aggregation (Engine→Car, Book→Library)
    * Generator expressions in aggregation (`sum(book.price for book in self.books)`)
  * Advanced Iteration & Memory Efficiency
    * Generators & lazy evaluation
    * `itertools` module
      * Infinite Iterators: `count()`, `cycle()`, `repeat()`
      * Combinatoric Iterators: `product()`, `permutations()`, `combinations()`
      * Terminating Iterators: `accumulate()`, `chain()`, `islice()`, `groupby()`
    * Shifting execution to native C loops for performance

> [https://www.youtube.com/watch?v=ZDa-Z5JzLYM](https://www.youtube.com/watch?v=ZDa-Z5JzLYM)
> [https://www.youtube.com/watch?v=iLRZi0Gu8Go](https://www.youtube.com/watch?v=iLRZi0Gu8Go)
> [https://www.youtube.com/watch?v=q7gAio9OMLk](https://www.youtube.com/watch?v=q7gAio9OMLk)
> [https://www.youtube.com/watch?v=1p7xa_BHYDs](https://www.youtube.com/watch?v=1p7xa_BHYDs)
> [https://www.youtube.com/watch?v=p8FUoSIyIVY](https://www.youtube.com/watch?v=p8FUoSIyIVY)
> [https://www.youtube.com/watch?v=-duO0tuAfus](https://www.youtube.com/watch?v=-duO0tuAfus)

---

* **C++**
  * Basics & Hardware Semantics
    * Pass-by-value (copy → stack/heap cost)
    * Pass-by-reference (`&` → zero-copy alias)
    * Pass-by-pointer (`*` → explicit dereference)
    * `const` references for read-only large objects
    * Example: `void update(int &x, int y)`
  * Memory Layout & Optimization
    * Multi-dimensional arrays → 1D contiguous memory
    * Row-major order (C++, Java, Python): offset = `i × C + j`
    * Column-major order (Fortran, MATLAB, GLSL): offset = `j × R + i`
    * Spatial locality & CPU cache (L1/L2)
    * Cache miss penalty when iterating column-wise in C++
    * GEMM / computational kernel optimization
  * OOP & Resource Management
    * Constructors: default, parameterized, copy
    * Destructors (`~ClassName()`)
    * RAII: resource lifecycle bound to object scope
    * Rule of Three / Rule of Five
    * Dynamic memory: `new` / `delete`
    * Smart pointers (RAII wrappers)
    * Operator overloading
  * Standard Template Library (STL)
    * `std::vector` → dynamic arrays, `push_back()`, `pop_back()`
    * Iterators: `begin()` / `end()` (pointer arithmetic abstraction)
    * `std::unordered_map` → hash table, O(1) insert/lookup
    * `<algorithm>`: `count()`, `count_if()`, lambdas
    * Sort, transform, search primitives

> [https://archive.codewithharry.com/videos/cpp-tutorials-in-hindi-71](https://archive.codewithharry.com/videos/cpp-tutorials-in-hindi-71)
> [https://www.youtube.com/watch?v=qJHWeSAPHsw](https://www.youtube.com/watch?v=qJHWeSAPHsw)
> [https://www.youtube.com/watch?v=b5lYGvcBjy4](https://www.youtube.com/watch?v=b5lYGvcBjy4)
> [https://www.youtube.com/watch?v=J3T-8N9QK2A](https://www.youtube.com/watch?v=J3T-8N9QK2A)
> [https://www.youtube.com/watch?v=CHl6uxoiJPA](https://www.youtube.com/watch?v=CHl6uxoiJPA)

---
* **C**
* **Basics & Hardware Proximity**
  * Procedural paradigm: functions + data separation
  * Variables, scope, storage classes (`auto`, `static`, `extern`, `register`)
  * Primitive types and their sizes (implementation-defined but predictable on most platforms)
  * Control flow: `if/else`, `switch`, `for`, `while`, `do-while`, `goto` (use sparingly)
  * Functions: declaration, definition, parameter passing (by value vs. pointer simulation of reference)
  * Example: `void swap(int *a, int *b)` for in-place modification

* **Pointers, Memory & Arrays**
  * Pointers as first-class citizens: address arithmetic, dereferencing
  * Arrays decay to pointers: `int arr[10]` → `int *`
  * Multi-dimensional arrays as arrays of arrays (row-major layout)
  * Dynamic memory: `malloc()`, `calloc()`, `realloc()`, `free()`
  * Manual memory management pitfalls (leaks, double-free, use-after-free, dangling pointers)
  * Strings as null-terminated `char` arrays + `<string.h>` functions
  * `const` correctness and `volatile` for hardware registers

* **Structs, Unions & Bit Manipulation**
  * User-defined types: `struct` (data aggregation)
  * `typedef` for cleaner syntax
  * `union` for type punning / memory overlay
  * Bit-fields and bitwise operations (`&`, `|`, `^`, `~`, shifts)
  * Alignment and padding in structs (performance + ABI considerations)

* **Preprocessor & Build Process**
  * Macros (`#define`), conditional compilation (`#ifdef`, `#ifndef`)
  * Header files (`.h`) vs implementation (`.c`)
  * Separate compilation + linking model
  * `make` / build systems introduction
  * Inline functions and performance implications

* **Standard Library & Systems Programming**
  * `<stdio.h>`, `<stdlib.h>`, `<string.h>`, `<math.h>`
  * File I/O: `fopen`, `fread`, `fwrite`, buffering
  * Process control, signals, environment variables
  * Relationship to C++: C is a strict subset; C++ adds RAII, templates, exceptions, OOP, etc.
  * Portability vs. platform-specific code (POSIX, Win32)

* **Performance & Low-Level Optimization**
  * Direct hardware access (inline assembly when needed)
  * Cache-friendly data structures and access patterns
  * No runtime overhead (no GC, no hidden costs)
  * Common idioms: manual unrolling, restrict keyword (`__restrict`)
  * Connection to C++ performance model and Python’s C extensions (CPython internals)


> [Beej's Guide to C Programming](https://beej.us/guide/bgc/)
> [C Programming Language (K&R)](https://en.wikipedia.org/wiki/The_C_Programming_Language) — the classic

---

* **Haskell**
  * Basics of Pure Functions
    * Immutable state (no reassignment)
    * Referential transparency
    * Lazy evaluation → thunks (compute only when demanded)
    * No loops → pure recursion & higher-order functions
  * List Comprehensions & Pattern Matching
    * Format: `[ output | input_set, predicates ]`
    * Generators: `x <- [1..10]`
    * Predicates as filters: `x \`mod\` 2 == 0`
    * Multiple / dependent generators → Cartesian products
    * Infinite lists + `take` (lazy safe extraction)
    * Sieve of Eratosthenes, Fibonacci via golden ratio
    * Pattern matching & guard clauses (no if/else)
    * Comparison with Python:
      * Squares: `[x^2 | x <- [1..10]]`
      * Evens: `[x | x <- [1..20], x \`mod\` 2 == 0]`
      * Pairs: `[(x,y) | x <- [1..3], y <- [1..3]]`
  * Higher-Order Functions & Type System
    * First-class functions (pass, store, return)
    * Currying: every function takes exactly one argument
    * Partial application → new function from fewer args
    * Static type inference
    * Typeclasses: `Show`, `Read`, `Bounded`
    * Algebraic data types
    * `Maybe` type: `Just value` / `Nothing` (null-safe)
  * Advanced Abstractions
    * Functor → map over a type
    * Applicative Functor → apply wrapped functions to wrapped values
    * Monad → sequence context-dependent computations; isolates side-effects (I/O)
    * Monoid → associative operations with identity element
    * Zipper → functional navigation in immutable tree structures
    * Equational reasoning & mathematical induction for correctness proofs

> [https://www.youtube.com/watch?v=TklkNLihQ_A](https://www.youtube.com/watch?v=TklkNLihQ_A)
> [https://www.youtube.com/watch?v=Ex4FWMexQNo](https://www.youtube.com/watch?v=Ex4FWMexQNo)
> [https://www.classcentral.com/course/youtube-haskell-for-beginners-59640](https://www.classcentral.com/course/youtube-haskell-for-beginners-59640)
> [https://www.youtube.com/watch?v=bc3_yZEAC_0](https://www.youtube.com/watch?v=bc3_yZEAC_0)
> [https://www.youtube.com/c/grahamhuttonnotts](https://www.youtube.com/c/grahamhuttonnotts)

---

* **Prolog**
  * Basics of Logic Programming
    * Knowledge base: facts + rules
    * Fact: unconditional assertion → `parent(alice, bob)`
    * Rule (Horn clause): `dating(X,Y) :- likes(X,Y), likes(Y,X)`
    * Queries against knowledge base
    * Logical inference engine → boolean truths or variable instantiations
  * Execution Mechanisms
    * Resolution via backward chaining
    * Backtracking on contradiction → alternate path search
    * Recursive relationships: `ancestor(X,Y)`
      * Base case: `X` is direct parent of `Y`
      * Recursive case: `X` ancestor of `Z`, `Z` parent of `Y`
    * Variable unification across lineage trees
    * Academic DB example: `passed(Student, Course, PassGrade)`, `enrolled(Student, Course)`
  * List Processing & Parameter Modes
    * Bound parameters → act as input
    * Unbound parameters → act as output (populated by engine)
    * Multidirectional execution
    * `append(A, B, C)`: forward (A+B→C) or reverse (C→all A,B pairs)
    * Structural recursion on head/tail
    * List reversal & traversal without explicit return type
  * Advanced Applications
    * Constraint satisfaction problems (CSP)
    * Scheduling, resource optimization, Sudoku
    * Developer defines constraints → engine searches state space
    * Game AI: NPC decision trees, dialogue/knowledge systems
    * Linguistics & cognitive science models

> [https://www.youtube.com/watch?v=gJOZZvYijqk](https://www.youtube.com/watch?v=gJOZZvYijqk)
> [https://www.youtube.com/watch?v=zK7J7lyl9J0](https://www.youtube.com/watch?v=zK7J7lyl9J0)
> [https://www.youtube.com/watch?v=8caRh1lZfDs](https://www.youtube.com/watch?v=8caRh1lZfDs)
