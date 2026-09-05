# Topic 7: Arrays

## 1. What Is an Array?

An array stores a fixed number of elements of the **same type** in one contiguous block of memory:

```c
int scores[5];                       // 5 ints, uninitialized
int primes[5] = {2, 3, 5, 7, 11};    // Fully initialized
int partial[5] = {1, 2};             // {1, 2, 0, 0, 0} — rest are zero
int zeros[100] = {0};                // All zeros idiom
int autoSize[] = {1, 2, 3};          // Compiler infers size 3
```

**Indexing starts at 0** and runs to `size - 1`. Access uses the subscript operator:

```c
primes[0] = 2;      // First element
primes[4] = 11;     // Last element of a 5-element array
```

There is **no bounds checking** in C: `primes[5]` compiles silently and corrupts adjacent memory — the single most dangerous beginner mistake.

---

## 2. Arrays and Memory Layout

For `int primes[5]`, the elements occupy 5 × `sizeof(int)` = 20 consecutive bytes. `primes` itself, when used in an expression, decays to a pointer to its first element (`&primes[0]`):

```c
printf("%p == %p\n", (void*)primes, (void*)&primes[0]);   // Same address
```

---

## 3. Traversing Arrays

```c
#define SIZE 5
int data[SIZE] = {10, 20, 30, 40, 50};

for (int i = 0; i < SIZE; i++) {     // Condition is i < SIZE, never i <= SIZE
    printf("%d ", data[i]);
}
```

Use a named constant (`SIZE`) or `sizeof(data) / sizeof(data[0])` instead of hard-coded numbers.

---

## 4. Common Operations

```c
// Sum / average
int total = 0;
for (int i = 0; i < SIZE; i++) total += data[i];
double average = (double)total / SIZE;    // Cast to avoid integer division

// Maximum
int max = data[0];                        // Start with the first element
for (int i = 1; i < SIZE; i++)
    if (data[i] > max) max = data[i];

// Reverse in place
for (int i = 0; i < SIZE / 2; i++) {
    int tmp = data[i];
    data[i] = data[SIZE - 1 - i];
    data[SIZE - 1 - i] = tmp;
}
```

---

## 5. Passing Arrays to Functions

An array parameter decays to a pointer, so the function receives the address (not a copy) and can modify the original. The size is **not** transmitted — pass it as a separate parameter:

```c
void fill(int arr[], int size) {          // int arr[] ≡ int *arr here
    for (int i = 0; i < size; i++) arr[i] = i * 10;
}

void print(const int arr[], int size) {   // const documents "read-only"
    for (int i = 0; i < size; i++) printf("%d ", arr[i]);
    printf("\n");
}

int nums[4];
fill(nums, 4);
print(nums, 4);
```

Inside the function, `sizeof(arr)` yields the size of a **pointer** (8 bytes on 64-bit), not of the array — another reason the length must travel separately.

---

## 6. Multidimensional Arrays

A 2D array is an "array of arrays" stored row by row (row-major order):

```c
int grid[2][3] = {
    {1, 2, 3},
    {4, 5, 6}
};

grid[1][2];              // Row 1, column 2 → 6
```

Traversal and passing to functions:

```c
void show(int g[][3], int rows) {     // Column count REQUIRED; rows may vary
    for (int r = 0; r < rows; r++) {
        for (int c = 0; c < 3; c++) printf("%d ", g[r][c]);
        printf("\n");
    }
}
```

The first dimension may be omitted; all later dimensions must be specified so the compiler can compute `g[r][c]` as `base + (r * cols + c) * sizeof(int)`.

---

## 7. Arrays of Characters vs. Other Arrays

A `char` array holding text must reserve one extra byte for the terminating `'\0'` (see Topic 8). Numeric arrays have no sentinel — the length must always be tracked explicitly.

---

## 8. Arrays vs. Pointers — First Look

| Expression | Meaning |
|------------|---------|
| `int a[5]` | Allocates 20 bytes; `a` is not assignable |
| `int *p` | Holds an address; `p` can be reassigned |
| `a[i]` | Identical to `*(a + i)` |
| `sizeof a` (in scope) | Total array size (20) |
| `sizeof p` | Pointer size (8) |

Full pointer mechanics are covered in Topics 9–10.

---

## 9. Common Pitfalls

* **Out-of-bounds access:** reading/writing `a[size]` is undefined behavior; loop with `i < size`.
* **Returning a local array** from a function: the storage dies when the function returns.
* **Assuming initialization:** `int a[10];` contains garbage, not zeros — use `{0}`.
* **VLA misuse:** variable-length arrays (`int a[n];`) exist in C99 but fail ungracefully when `n` is huge; dynamic allocation (Topic 12) is safer for large sizes.

---

## 10. Summary

* Arrays are contiguous, fixed-size, same-type collections indexed from 0.
* Passing an array passes a pointer; pass the length separately and mark read-only parameters `const`.
* 2D arrays are laid out row-major; later dimensions must be declared in parameters.
* C performs no bounds checking — every access is the programmer's responsibility.
