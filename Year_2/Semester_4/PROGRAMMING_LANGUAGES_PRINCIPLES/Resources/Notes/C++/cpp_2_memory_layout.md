# C++ — Memory Layout and Optimization

*Prerequisite: cpp_1_basics_and_hardware.md — Stack/heap cost model and pass-by-reference semantics.*

Multi-dimensional arrays in C++ are stored as a single contiguous block of memory. The mapping from logical indices $(i, j)$ to a linear offset determines whether iteration patterns exploit or defeat CPU cache locality. This file covers row-major and column-major layout formulas, the role of L1/L2 cache and spatial locality, the performance penalty of column-wise traversal in row-major storage, and the application of these principles to GEMM and other computational kernels.

---

## 1. Multi-Dimensional Arrays as Contiguous Memory

### 1.1 Concept Overview

A 2D array of size $R \times C$ (rows $\times$ columns) is physically stored as a 1D array of $R \times C$ elements. The compiler maps the two logical indices to a single linear address using a **layout convention**. C++ uses **row-major order**: elements of the same row occupy consecutive memory addresses.

### 1.2 Declaration Syntax

**Static 2D array (stack-allocated):**

```
<type> <name>[<rows>][<cols>];
```

**Dynamic 1D buffer emulating 2D (heap-allocated):**

```
<type> *<name> = new <type>[<rows> * <cols>];
// Access element (i, j) via: name[i * cols + j]  (row-major)
```

**`std::vector` of `std::vector`:**

```cpp
std::vector<std::vector<int>> matrix(rows, std::vector<int>(cols));
```

Note: nested `std::vector` does **not** guarantee a single contiguous block across rows; each row is a separate heap allocation. For cache-critical kernels, a flat `std::vector<int>` of size $R \times C$ is preferred.

### 1.3 Memory Diagram (Row-Major, $3 \times 4$ Matrix)

Logical view:

$$
A = \begin{pmatrix}
a_{0,0} & a_{0,1} & a_{0,2} & a_{0,3} \\
a_{1,0} & a_{1,1} & a_{1,2} & a_{1,3} \\
a_{2,0} & a_{2,1} & a_{2,2} & a_{2,3}
\end{pmatrix}
$$

Physical memory (single contiguous block):

```
Index:  0    1    2    3  |  4    5    6    7  |  8    9   10   11
Value: a00  a01  a02  a03  | a10  a11  a12  a13  | a20  a21  a22  a23
        └──── row 0 ────┘     └──── row 1 ────┘     └──── row 2 ────┘
```

---

## 2. Row-Major and Column-Major Addressing

### 2.1 Row-Major Order (C++, Java, Python/NumPy default)

In row-major layout, the **last** index varies fastest in memory. For a matrix with $R$ rows and $C$ columns:

$$
\text{offset}(i, j) = i \times C + j
$$

where $i \in [0, R-1]$ is the row index and $j \in [0, C-1]$ is the column index.

| Language / System | Default Layout |
| :--- | :--- |
| C, C++ | Row-major |
| Java (2D arrays) | Row-major |
| Python (NumPy `ndarray`) | Row-major (C-contiguous) |
| Fortran | Column-major |
| MATLAB | Column-major |
| GLSL (OpenGL shaders) | Column-major |

### 2.2 Column-Major Order (Fortran, MATLAB, GLSL)

In column-major layout, the **first** index varies fastest. Elements of the same column are consecutive:

$$
\text{offset}(i, j) = j \times R + i
$$

### 2.3 Layout Comparison Table

| Layout | Offset Formula | Consecutive in Memory | Fastest-Varying Index |
| :--- | :--- | :--- | :--- |
| Row-major | $i \cdot C + j$ | Elements of row $i$ | Column $j$ |
| Column-major | $j \cdot R + i$ | Elements of column $j$ | Row $i$ |

### 2.4 Worked Address Calculation

For a $4 \times 3$ row-major `int` array ( $R = 4$, $C = 3$):

| $(i, j)$ | $\text{offset} = i \times 3 + j$ |
| :--- | :--- |
| $(0, 0)$ | $0$ |
| $(0, 2)$ | $2$ |
| $(1, 0)$ | $3$ |
| $(2, 1)$ | $7$ |
| $(3, 2)$ | $11$ |

```cpp
#include <iostream>

int main() {
    const int R = 4, C = 3;
    int A[R][C] = {
        { 0,  1,  2},
        { 3,  4,  5},
        { 6,  7,  8},
        { 9, 10, 11}
    };

    int i = 2, j = 1;
    int linear = i * C + j;
    std::cout << "A[" << i << "][" << j << "] = " << A[i][j]
              << ", linear index = " << linear << "\n";
    return 0;
}
```

```text
A[2][1] = 7, linear index = 7
```

---

## 3. Spatial Locality and CPU Cache

### 3.1 Conceptual Foundation

Main memory (RAM) is orders of magnitude slower than the CPU. To bridge this gap, modern processors employ a **cache hierarchy**:

| Level | Typical Size | Latency (approx.) |
| :--- | :--- | :--- |
| L1 cache | 32–64 KB per core | $\sim 1$ ns |
| L2 cache | 256 KB – 1 MB per core | $\sim 3$–$10$ ns |
| L3 cache | 8–64 MB shared | $\sim 10$–$40$ ns |
| Main memory | GB scale | $\sim 50$–$100$ ns |

When the CPU accesses a memory address, the cache fetches an entire **cache line** (typically 64 bytes) containing that address and its neighbors. Subsequent accesses to nearby addresses are served from cache — this is **spatial locality**.

### 3.2 Cache Line and Row-Major Traversal

A cache line of 64 bytes holds 16 consecutive `int` values (4 bytes each). Iterating row-wise in a row-major matrix accesses consecutive addresses, maximizing cache line utilization:

```cpp
// Row-wise: consecutive memory addresses → high cache hit rate.
for (int i = 0; i < R; ++i)
    for (int j = 0; j < C; ++j)
        sum += A[i][j];
```

### 3.3 Cache Miss Penalty: Column-Wise Iteration in C++

Iterating column-wise in a row-major matrix jumps by $C$ elements (stride $= C \times \text{sizeof}(T)$ bytes) on each inner-step:

```cpp
// Column-wise in row-major storage: stride = C * sizeof(int) → cache misses.
for (int j = 0; j < C; ++j)
    for (int i = 0; i < R; ++i)
        sum += A[i][j];
```

For large matrices, each inner iteration likely accesses a new cache line, causing an **L1/L2 cache miss**. A cache miss stalls the CPU for tens to hundreds of cycles while data is fetched from a deeper cache level or main memory.

**Performance ratio:** For a sufficiently large $R \times C$ matrix, column-wise traversal in row-major layout can be $5$–$20\times$ slower than row-wise traversal, depending on matrix size and hardware.

> **[Key Insight]** The iteration order must match the memory layout's fastest-varying dimension. In C++ (row-major), the inner loop should walk along columns (varying $j$) within a fixed row. In Fortran/MATLAB (column-major), the inner loop should walk along rows (varying $i$) within a fixed column.

---

## 4. GEMM and Computational Kernel Optimization

### 4.1 GEMM Definition

**GEMM** (General Matrix Multiply) computes:

$$
C = \alpha \, A \times B + \beta \, C
$$

where $A$ is $M \times K$, $B$ is $K \times N$, and $C$ is $M \times N$. The naive triple-loop implementation is the canonical example of how memory layout interacts with performance.

### 4.2 Naive Row-Major GEMM

```cpp
// C[i][j] = sum over k of A[i][k] * B[k][j]
// A: row-major (good for fixed i, varying k)
// B: row-major (BAD for fixed k, varying j then accessing B[k][j] column-wise)
// C: row-major (good for fixed i, varying j)

for (int i = 0; i < M; ++i)
    for (int j = 0; j < N; ++j)
        for (int k = 0; k < K; ++k)
            C[i][j] += A[i][k] * B[k][j];
```

The inner access to `B[k][j]` with fixed `j` and increasing `k` walks along rows of $B$ (good). But the middle loop over `j` with fixed `k` accesses `B[k][j]` with stride $N$ — partially cache-unfriendly for large $N$.

### 4.3 Loop Reordering (IKJ / I-K-J)

Reordering loops to place the $K$ dimension innermost for $A$ and using a transposed $B^T$ is a standard optimization strategy:

$$
C_{ij} = \sum_{k=0}^{K-1} A_{ik} \cdot B_{kj}
$$

**IKJ ordering** (fix $i$, sweep $k$, inner $j$):

```cpp
for (int i = 0; i < M; ++i)
    for (int k = 0; k < K; ++k) {
        float a_ik = A[i][k];
        for (int j = 0; j < N; ++j)
            C[i][j] += a_ik * B[k][j];   // B row access: consecutive.
    }
```

Here `B[k][j]` for fixed `k` and increasing `j` traverses a row of $B$ — consecutive in row-major layout.

### 4.4 Blocking (Tiling) for Cache

For matrices too large to fit in L1/L2 cache, **blocking** partitions the computation into submatrices (tiles) that fit in cache:

```
for (i_tile = 0; i_tile < M; i_tile += BLOCK)
    for (j_tile = 0; j_tile < N; j_tile += BLOCK)
        for (k_tile = 0; k_tile < K; k_tile += BLOCK)
            // Multiply BLOCK x BLOCK submatrices
```

> **[Supplementary]**
> Production BLAS libraries (OpenBLAS, Intel MKL) combine loop reordering, register blocking, SIMD vectorization, and multi-threading to achieve near-peak FLOPS on GEMM. The pedagogical takeaway is that algorithmic complexity $O(n^3)$ alone does not determine runtime; the constant factor from memory access patterns often dominates.

### 4.5 Optimization Summary Table

| Technique | Addresses | Typical Speedup |
| :--- | :--- | :--- |
| Row-wise vs. column-wise iteration | Spatial locality | $5$–$20\times$ |
| Loop interchange (IKJ) | Stride reduction on $B$ | $2$–$5\times$ |
| Cache blocking (tiling) | L1/L2 reuse | $2$–$10\times$ |
| SIMD vectorization | Instruction-level parallelism | $4$–$8\times$ |
| Parallelism (OpenMP) | Multi-core | $\approx P\times$ ( $P$ cores) |

---

## Common Errors and Gotchas

### Error 1: Assuming `vector<vector<T>>` Is Contiguous

**Cause:** Each row of a nested `std::vector` is independently heap-allocated; rows may be far apart in memory.

**Resolution:** Use a flat `std::vector<T>` of size $R \times C$ with manual index `i * C + j` for performance-critical code.

### Error 2: Column-Major Formula in C++

**Cause:** Applying $\text{offset} = j \times R + i$ (Fortran/MATLAB formula) to a C++ row-major array produces wrong elements.

**Resolution:** In C++, always use $\text{offset} = i \times C + j$.

### Error 3: Out-of-Bounds Linear Index

**Cause:** Using $i \times R + j$ instead of $i \times C + j$ when $R \neq C$.

**Resolution:** The stride multiplier is always the **number of columns** $C$ in row-major layout, not the number of rows.

---

## Solved Exercises

### Exercise 1: Linear Index from Row-Major Formula

**Problem:** A row-major `float` array has $R = 5$ rows and $C = 8$ columns. Compute the linear offset for element $(i, j) = (3, 5)$.

**Solution:**

$$
\text{offset} = i \times C + j = 3 \times 8 + 5 = 24 + 5 = 29
$$

The element is the 30th entry (0-indexed: 29) in the contiguous block.

---

### Exercise 2: Column-Major Offset

**Problem:** A Fortran-style column-major array has $R = 5$, $C = 8$. Compute the offset for $(i, j) = (3, 5)$.

**Solution:**

$$
\text{offset} = j \times R + i = 5 \times 5 + 3 = 25 + 3 = 28
$$

Note: offset 28 in column-major $\neq$ offset 28 in row-major — they refer to different logical elements.

---

### Exercise 3: Which Element at Linear Index 10?

**Problem:** A $3 \times 4$ row-major matrix ($R = 3$, $C = 4$). Which $(i, j)$ corresponds to linear index 10?

**Solution:**

1. Row index: $i = \lfloor 10 / 4 \rfloor = 2$.
2. Column index: $j = 10 \bmod 4 = 2$.
3. Answer: $(i, j) = (2, 2)$.

Verification: $2 \times 4 + 2 = 10$.

---

### Exercise 4: Row-Wise vs. Column-Wise Access Pattern

**Problem:** For a $1000 \times 1000$ row-major `double` matrix, classify each loop nest as cache-friendly (F) or cache-unfriendly (U).

```cpp
// A)
for (int i = 0; i < 1000; ++i)
    for (int j = 0; j < 1000; ++j)
        sum += M[i][j];

// B)
for (int j = 0; j < 1000; ++j)
    for (int i = 0; i < 1000; ++i)
        sum += M[i][j];
```

**Solution:**

1. **A) — F (friendly):** Inner loop increments $j$, accessing consecutive addresses along row $i$.
2. **B) — U (unfriendly):** Inner loop increments $i$ with fixed $j$, stride $= 1000 \times 8 = 8000$ bytes between accesses — far exceeds a 64-byte cache line.

---

### Exercise 5: Stride Calculation

**Problem:** A row-major `int` matrix has $C = 256$ columns. What is the memory stride (in bytes) between `A[i][j]` and `A[i+1][j]`?

**Solution:**

1. Logical stride in elements: $C = 256$ (one full row).
2. Byte stride: $256 \times \text{sizeof(int)} = 256 \times 4 = 1024$ bytes.

Each column-wise step crosses 16 cache lines ( $1024 / 64 = 16$ ).

---

### Exercise 6: Flat Buffer Emulation

**Problem:** Implement row-major access to a flat `std::vector<int>` representing a $3 \times 3$ matrix. Set `M[1][2] = 42` and read it back.

**Solution:**

```cpp
#include <iostream>
#include <vector>

int main() {
    const int R = 3, C = 3;
    std::vector<int> buf(R * C, 0);

    int i = 1, j = 2;
    buf[i * C + j] = 42;

    std::cout << buf[i * C + j] << "\n";
    return 0;
}
```

```text
42
```

---

### Exercise 7: GEMM Inner Loop Analysis

**Problem:** In naive GEMM, for fixed `i` and `k`, the inner loop `for (int j = 0; j < N; ++j) C[i][j] += A[i][k] * B[k][j];` accesses `B[k][j]` with increasing `j`. Is this access row-major-friendly? Explain.

**Solution:**

1. `B[k][j]` with fixed row $k$ and increasing column $j$ traverses row $k$ of matrix $B$.
2. In row-major layout, row elements are consecutive in memory.
3. **Yes, cache-friendly** — each step accesses the next `int`/`float` in the same cache line until the line is exhausted.

---

### Exercise 8: Tile Size Estimation

**Problem:** L1 data cache is 32 KB. Each `double` is 8 bytes. What is the maximum number of `double` elements that fit in L1? If using a square tile of matrix $A$ alone, what is the maximum tile dimension $T$ such that $T^2$ doubles fit in 32 KB?

**Solution:**

1. Total doubles in 32 KB: $32768 / 8 = 4096$ elements.
2. For a square tile: $T^2 \leq 4096$.
3. $T \leq \sqrt{4096} = 64$.

A $64 \times 64$ tile of `double` values exactly fills 32 KB. Practical blocking uses smaller tiles to leave room for $B$ and $C$ submatrices simultaneously.

---

## Exam Tip: Layout Formula and Iteration Direction

**Memorize two formulas:**

| Layout | Offset |
| :--- | :--- |
| Row-major (C++) | $\text{offset}(i,j) = i \cdot C + j$ |
| Column-major (Fortran) | $\text{offset}(i,j) = j \cdot R + i$ |

**Mnemonic:** In row-major, **C**olumns are the inner stride (multiply row index by **C**). In column-major, **R**ows are the inner stride (multiply column index by **R**).

**Iteration rule:** The **innermost loop** must vary the index that is consecutive in memory. For C++ row-major arrays, the inner loop should be over $j$ (columns) when $i$ is fixed. Reversing the loops is the single most tested cache-performance question pattern.

**Trap:** When $R = C = n$ (square matrix), $i \cdot C + j$ and $j \cdot R + i$ both simplify to $ni + j$ vs. $nj + i$ — different formulas that happen to share the same dimensions. Always identify layout first, then apply the correct formula.