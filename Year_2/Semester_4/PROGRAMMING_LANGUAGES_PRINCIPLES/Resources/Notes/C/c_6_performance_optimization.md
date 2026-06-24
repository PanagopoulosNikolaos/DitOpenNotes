# C — Performance and Low-Level Optimization

C's design matches compilation directly to physical CPU architectures, enabling execution with zero hidden costs, garbage collection delays, or dynamic dispatch penalties. Through hardware access and memory alignment optimization, developers can write cache-aware and pipeline-efficient algorithms. This file covers inline assembly, cache-locality optimization, manual loop unrolling, the `restrict` compiler keyword, and building native C extensions for Python.

---

## 1. Direct Hardware Access and Inline Assembly

For hardware-level interfaces, developers can write inline assembly to access specialized CPU registers or instructions that are not exposed by standard C keywords.

### 1.1 Assembly Syntax Reference

On GCC/Clang compilers, inline assembly uses the `__asm__` keyword.

#### Syntax Reference

```text
__asm__ [volatile] (
    "assembly code"
    : output_operands
    : input_operands
    : clobbered_registers
);
```

The `clobbered_registers` list tells the compiler which registers will be modified by the assembly code, preventing the compiler from caching variables in those registers.

---

## 2. Cache-Friendly Design and Cache Misses

Modern CPU architectures rely on cache hierarchies (L1, L2, L3) to bridge the speed gap between CPU cores and main RAM memory.

### 2.1 Cache Lines and Locality

Memory is transferred from RAM to CPU caches in chunks called **cache lines** (typically $64$ bytes).
- **Temporal Locality:** Accessing the same memory location repeatedly within a short window.
- **Spatial Locality:** Accessing memory locations that reside near each other (such as contiguous array elements).

### 2.2 Row-Major vs. Column-Major Traversal

Because C arrays are laid out in row-major order, iterating through a 2D array row-by-row utilizes spatial locality, loading multiple contiguous elements in a single cache line. In contrast, iterating column-by-column jumps across rows, triggering a **cache miss** for every single access and degrading memory bandwidth performance.

```
Row-major loop (Fast):  matrix[i][j] where outer loop is i, inner loop is j
Column-major loop (Slow): matrix[i][j] where outer loop is j, inner loop is i
```

---

## 3. Zero Runtime Overhead Model

C uses a zero-overhead performance model:
1. **No Garbage Collection:** Memory allocations (`malloc`, `free`) map directly to OS memory allocation APIs. The programmer has total control over when memory is released.
2. **No Dynamic Dispatch:** Function calls compile to static jumps (`CALL` instruction). There is no runtime class method lookup table (like C++ `vtable` or Python object type dict lookup), unless function pointers are used explicitly.
3. **Implicit Type Conversions:** Types are evaluated at compile time; runtime execution contains no type annotations or runtime checks.

---

## 4. Optimization Idioms and the `restrict` Keyword

The C99 standard introduced the `restrict` pointer qualifier to assist compilers in generating auto-vectorized code.

### 4.1 The `restrict` Keyword

By marking a pointer as `restrict`, the programmer promises the compiler that the pointer is the only reference to the underlying memory block for its scope. This guarantees that writes through this pointer will not alter memory referenced by other pointers, allowing the compiler to cache values in registers and generate parallel SIMD instructions.

#### Syntax Reference

```text
void process_data(int * restrict dest, const int * restrict src, int size);
```

---

### 4.2 Loop Unrolling

Loop unrolling decreases loop control overhead (incrementing indices, testing conditions, branching) by executing multiple iterations inside a single loop step.

```c
// Normal Loop
for (int i = 0; i < 4; i++) {
    sum += arr[i];
}

// Unrolled Loop
sum += arr[0];
sum += arr[1];
sum += arr[2];
sum += arr[3];
```

---

## 5. C Extensions and CPython Integration

To optimize bottlenecks, Python programs can import compiled C libraries using the CPython extension API (`<Python.h>`).

### 5.1 CPython Extension Types Reference Table

| CPython Type / Function | Purpose | Header |
| :--- | :--- | :--- |
| `PyObject*` | Unified wrapper pointer representing any Python object | `<Python.h>` |
| `PyArg_ParseTuple` | Parses Python positional arguments into C variable types | `<Python.h>` |
| `Py_BuildValue` | Converts C primitive types into Python objects | `<Python.h>` |
| `PyMethodDef` | Table of functions exported by the module | `<Python.h>` |

---

## Solved Exercises

### Exercise 1: Inline Assembly Addition

**Problem:** Implement a function that adds two integers using inline assembly.

**Solution:**

```c
#include <stdio.h>

int asm_add(int a, int b) {
    int result;
    // GCC basic input/output constraint syntax
    __asm__ (
        "add %2, %0"
        : "=r" (result) // %0 output
        : "0" (a), "r" (b) // %1 (same as %0), %2 input
    );
    return result;
}

int main(void) {
    printf("5 + 3 = %d\n", asm_add(5, 3));
    return 0;
}
```

```text
5 + 3 = 8
```

---

### Exercise 2: Cache-Miss Traversal Analysis

**Problem:** Explain the difference in execution performance between `traverse_rows` and `traverse_cols` for a matrix size of $10{,}000 \times 10{,}000$.

```c
#define SIZE 10000
int matrix[SIZE][SIZE];

void traverse_rows(void) {
    long long sum = 0;
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            sum += matrix[i][j];
        }
    }
}

void traverse_cols(void) {
    long long sum = 0;
    for (int j = 0; j < SIZE; j++) {
        for (int i = 0; i < SIZE; i++) {
            sum += matrix[i][j];
        }
    }
}
```

**Solution:**
1. In `traverse_rows`, the inner loop iterates over `j`. Elements `matrix[i][0]`, `matrix[i][1]`, etc., are contiguous in memory.
2. Loading `matrix[i][0]` pulls a $64$-byte cache line into the L1 cache, which contains $16$ contiguous integers (if `sizeof(int)` is $4$ bytes). The subsequent $15$ iterations are resolved directly from the L1 cache, causing only $1$ cache miss per $16$ accesses.
3. In `traverse_cols`, the inner loop iterates over `i`. Elements `matrix[0][j]`, `matrix[1][j]`, etc., are separated in memory by $10{,}000 \times 4$ bytes ($40$ KB).
4. Each access jumps past the active cache line size, forcing the CPU to fetch a new cache line from RAM.
5. `traverse_cols` generates a cache miss on almost every memory read, resulting in a performance slowdown of up to $10\times$ depending on architecture.

---

### Exercise 3: Pointer Aliasing and Restrict Optimization

**Problem:** Explain how the `restrict` keyword changes compile-time optimizations for the function below.

```c
void add_arrays(int *a, int *b, int *val) {
    *a += *val;
    *b += *val;
}
```

**Solution:**
1. Without `restrict`, the compiler must assume that pointers `a`, `b`, and `val` can point to overlapping memory (pointer aliasing).
2. For instance, if `b` and `val` point to the same location, modifying `*b` changes the value of `*val`.
3. Consequently, the compiler is forced to reload the value of `*val` from memory after modifying `*a`, generating multiple read instructions:
   - Load `*val` into register.
   - Load `*a`, add, write back to `*a`.
   - Reload `*val` from memory (in case `a` pointed to `val`).
   - Load `*b`, add, write back to `*b`.
4. Marking the pointers `int * restrict a`, `int * restrict b`, `const int * restrict val` informs the compiler that their memory blocks do not overlap.
5. The compiler can cache `*val` in a register and reuse it for both operations without reloading from RAM.

---

### Exercise 4: Manual Loop Unrolling by 4

**Problem:** Write a loop unrolled by a factor of $4$ to compute the sum of an array. Handle remainder elements safely.

**Solution:**

```c
#include <stdio.h>

int unrolled_sum(const int *arr, int size) {
    int sum = 0;
    int i = 0;
    int limit = size - (size % 4);
    
    // Unroll in blocks of 4
    for (; i < limit; i += 4) {
        sum += arr[i];
        sum += arr[i+1];
        sum += arr[i+2];
        sum += arr[i+3];
    }
    
    // Handle remaining elements
    for (; i < size; i++) {
        sum += arr[i];
    }
    return sum;
}

int main(void) {
    int data[] = {1, 2, 3, 4, 5, 6, 7};
    printf("Sum = %d\n", unrolled_sum(data, 7));
    return 0;
}
```

```text
Sum = 28
```

---

### Exercise 5: Compile Assembly Output Generation

**Problem:** Use `gcc` options to output assembly code and verify compilation optimizations.

**Solution:**
1. To generate assembly representation from `main.c`, use the `-S` flag:
   ```sh
   gcc -S -O2 main.c -o main.s
   ```
2. The compiler outputs a `main.s` file containing AT&T assembly instructions.
3. Using the `-O2` flag enables compiler optimizations (such as instruction scheduling, register allocation, and loop unrolling), which simplifies code compared to unoptimized compilation (`-O0`).

---

### Exercise 6: Basic Python C Extension Module

**Problem:** Sketch a minimal C source file utilizing `<Python.h>` that exports a function `add(a, b)` returning their sum to Python.

**Solution:**

```c
#include <Python.h>

// Function definition
static PyObject* method_add(PyObject* self, PyObject* args) {
    int a, b;
    if (!PyArg_ParseTuple(args, "ii", &a, &b)) {
        return NULL; // Raises TypeError in Python
    }
    return Py_BuildValue("i", a + b);
}

// Module method table
static PyMethodDef AddMethods[] = {
    {"add", method_add, METH_VARARGS, "Adds two integers."},
    {NULL, NULL, 0, NULL}
};

// Module definition structure
static struct PyModuleDef addmodule = {
    PyModuleDef_HEAD_INIT,
    "my_adder",
    "Minimal module for optimization.",
    -1,
    AddMethods
};

// Initialization function
PyMODINIT_FUNC PyInit_my_adder(void) {
    return PyModule_Create(&addmodule);
}
```

---

### Exercise 7: Cache Alignment Padding

**Problem:** Explain what cache line bouncing (false sharing) is and how structure padding prevents it.

**Solution:**
1. False sharing occurs in multi-threaded programs when two threads on different CPU cores modify independent variables that reside within the same $64$-byte cache line.
2. When Core 1 writes to variable `A`, it invalidates the entire cache line in Core 2's cache, forcing Core 2 to reload its variable `B` from RAM even though `B` was not modified.
3. **Fix:** Use compiler alignment specifications to ensure variables reside on separate cache boundaries:
   ```c
   struct ThreadData {
       int thread_a_var;
       char padding[60]; // Pad to 64 bytes
       int thread_b_var;
   };
   // Or align explicitly:
   alignas(64) int thread_a_var;
   alignas(64) int thread_b_var;
   ```

---

### Exercise 8: C vs. Python Execution Speed

**Problem:** Implement a loop calculating the sum of squares up to $1{,}000{,}000$ in C and explain why it runs faster than Python.

**Solution:**

```c
#include <stdio.h>

int main(void) {
    long long sum = 0;
    for (int i = 1; i <= 1000000; i++) {
        sum += (long long)i * i;
    }
    printf("Sum = %lld\n", sum);
    return 0;
}
```

1. **C Performance:** Compiles directly to register instructions. The loop body requires only a few CPU cycles (integer multiply and add).
2. **Python Performance:** Inside CPython, every loop iteration executes multiple bytecode instructions.
3. Every integer in Python is an object on the heap, requiring reference counting increments and dynamic type dispatch lookups for every multiplication and addition step.

---

## Common Errors and Gotchas

### 1. Column-Major Indexing Slowdown
* **Cause:** Accessing matrices in column-major patterns causes the processor to skip cache pages on every lookup, degrading memory performance.
* **Resolution:** Always nest loops so that the innermost loop index matches the rightmost dimension of the array: `matrix[row][col]`.

### 2. Violating `restrict` Promises (Undefined Behavior)
* **Cause:** Marking parameters with `restrict` and passing pointers that point to overlapping regions. The compiler optimizes assuming no aliasing occurs, which results in corrupted outputs.
* **Resolution:** Only use `restrict` when the caller is guaranteed to pass non-overlapping memory blocks. Use helper tools like `memmove` if overlap is possible.

### 3. Missing Python GIL release in C Extensions
* **Cause:** Running long-running computational loops inside C extensions without releasing the Python Global Interpreter Lock (GIL). This prevents other Python threads from executing.
* **Resolution:** Wrap performance-critical C blocks in GIL release macros:
   ```c
   Py_BEGIN_ALLOW_THREADS
   // long execution block
   Py_END_ALLOW_THREADS
   ```

---

## Exam Tip: Cache Locality and Array Traversal Loops

**Identifying Cache Optimization Patterns:**
Exams often test matrix traversal order or query why a specific loop ordering runs faster.
- **Rule of thumb:** Trace index ordering. Compare the index that changes fastest in the loop structure (the innermost loop index) with the array layout. If the innermost loop variable matches the rightmost array index, it has high spatial locality.
- **Example exam question:** Given:
  ```c
  for(int i=0; i<N; i++)
      for(int j=0; j<N; j++)
          arr[j][i] = 0;
  ```
  Is this loop cache-optimized? **No.** The innermost loop variable is `j`, but `j` is the leftmost index of `arr[j][i]`. The memory accesses jump by $N$ elements on every iteration. Swap the loop headers or the index access locations (`arr[i][j]`) to optimize.
