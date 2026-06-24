# C — Pointers, Memory, and Arrays

Pointers and arrays are fundamental to C, offering direct control over memory layout and hardware access. By allowing developers to store and manipulate memory addresses, C enables efficient dynamic allocation, zero-copy data passing, and custom memory layout management. This file covers pointer mechanics, array decay, multi-dimensional array mapping, dynamic memory API functions, string handling, and qualifiers like `const` and `volatile`.

---

## 1. Pointers and Address Arithmetic

A **pointer** is a variable whose value is the memory address of another variable. Pointers are strongly typed; the type of the pointer specifies the layout of the memory block it references.

### 1.1 Core Operators

- `&` (Address-of operator): Retrieves the memory address of a variable.
- `*` (Dereference operator): Accesses the value stored at the memory address held by the pointer.

### 1.2 Address Arithmetic

Pointer arithmetic operates on memory blocks scaling by the size of the pointer's referenced type.

Let `p` be a pointer of type `T*` pointing to address $A$. The operation `p + n` calculates the target address as:

$$
\text{addr}(p + n) = A + n \times \text{sizeof}(T)
$$

Subtracting two pointers of the same type yields the distance between them measured in elements of type `T`, returned as a signed integer type `ptrdiff_t`.

---

## 2. Arrays and Decay Behavior

An array is a contiguous block of memory holding elements of the same type. In most contexts, the identifier of an array **decays** into a pointer to its first element:

```text
Type arr[N]; // arr decays to Type* pointing to &arr[0]
```

### 2.1 Exceptions to Decay

An array identifier does **not** decay to a pointer in the following three cases:

1. As the operand of the `sizeof` operator: `sizeof(arr)` returns the total size in bytes of the array ($N \times \text{sizeof(Type)}$), not the size of a pointer.
2. As the operand of the unary `&` (address-of) operator: `&arr` returns a pointer to the entire array of type `Type (*)[N]`, not a pointer to a pointer.
3. As a string literal initializer: `char str[] = "hello";`.

---

## 3. Multi-dimensional Arrays and Row-Major Memory Layout

Multi-dimensional arrays are represented as arrays of arrays. They are stored in contiguous memory using **row-major order**, where the rightmost index varies fastest.

```
For a 2D array: arr[Rows][Cols]
Memory Layout: [Row 0, Col 0] [Row 0, Col 1] ... [Row 1, Col 0] ...
```

### 3.1 2D Array Offset Calculation

For an array declared as `Type arr[R][C]`, the flat byte offset of element `arr[i][j]` from the base address is:

$$
\text{offset}(i, j) = (i \times C + j) \times \text{sizeof}(\text{Type})
$$

### 3.2 Parameter Declarations for Multi-dimensional Arrays

Because the compiler needs to know the sizes of the dimensions to compute offsets, passing a multi-dimensional array to a function requires specifying all dimensions except the first:

```c
void process_grid(int grid[][10], int rows); // Second dimension is mandatory
```

---

## 4. Dynamic Memory Allocation

Dynamic memory is allocated on the **heap** at runtime. The standard library provides allocation functions in `<stdlib.h>`.

### 4.1 Memory Management API Reference

| Function | Signature | Return Type | Purpose | Description of Parameters |
| :--- | :--- | :--- | :--- | :--- |
| `malloc` | `void* malloc(size_t size)` | `void*` | Allocates uninitialized memory block | `size`: Number of bytes to allocate |
| `calloc` | `void* calloc(size_t num, size_t size)` | `void*` | Allocates zero-initialized memory | `num`: Number of elements, `size`: Size of each element |
| `realloc` | `void* realloc(void* ptr, size_t new_size)` | `void*` | Resizes existing allocated block | `ptr`: Block pointer, `new_size`: New size in bytes |
| `free` | `void free(void* ptr)` | `void` | Deallocates heap memory | `ptr`: Memory address to release |

> **[Key Insight]** `realloc` may move the memory block to a new location if the current block cannot be expanded in-place. If `realloc` fails, it returns `NULL` and the original block remains allocated. Therefore, never write `ptr = realloc(ptr, size);` directly because a allocation failure will cause a memory leak.

---

## 5. Strings and String Processing

A string in C is a contiguous sequence of characters terminated by a null character (`'\0'`). C has no built-in string type; strings are manipulated using pointers to `char` arrays.

### 5.1 Common String Functions (`<string.h>`)

| Function | Parameters | Behavior |
| :--- | :--- | :--- |
| `strlen` | `const char *s` | Returns the number of characters in `s` excluding `'\0'`. |
| `strcpy` | `char *dest, const char *src` | Copies `src` to `dest` including `'\0'`. Dangerous if `dest` overflows. |
| `strncpy` | `char *dest, const char *src, size_t n` | Copies up to `n` bytes. Does not guarantee null-termination if `strlen(src) >= n`. |
| `strcmp` | `const char *s1, const char *s2` | Compares lexicographically. Returns `< 0`, `0`, or `> 0`. |

---

## 6. Const Correctness and Volatile Qualifier

Qualifiers modify how the compiler treats memory access.

### 6.1 `const` Pointer Declarations

The position of the `const` keyword relative to the asterisk (`*`) determines whether the pointer or the pointed-to data is immutable:

1. **Pointer to Constant:** `const int *p` (or `int const *p`)
   - The data at the address cannot be modified via `p`: `*p = 5; // Error`.
   - The pointer `p` can be changed to point elsewhere: `p = &x; // OK`.
2. **Constant Pointer:** `int * const p`
   - The pointer `p` is immutable: `p = &x; // Error`.
   - The data at the address can be modified: `*p = 5; // OK`.

### 6.2 The `volatile` Qualifier

The `volatile` qualifier informs the compiler that a memory location can be modified by hardware, interrupts, or concurrent threads outside of the program's control. It prevents the compiler from optimizing away reads or writes to that address.

```c
volatile int *status_reg = (volatile int *)0x40001000;
while (*status_reg == 0); // Compiler will not cache status_reg in a register
```

---

## Solved Exercises

### Exercise 1: Pointer Arithmetic

**Problem:** What is the output of the following program? Explain how pointers are modified.

```c
#include <stdio.h>

int main(void) {
    int arr[] = {10, 20, 30, 40, 50};
    int *p = arr;
    p++;
    printf("*p = %d\n", *p);
    p = p + 2;
    printf("*p = %d\n", *p);
    return 0;
}
```

**Solution:**
1. `p` starts pointing to `arr[0]` ($10$).
2. `p++` increments the pointer to point to the next element `arr[1]` ($20$).
3. `p = p + 2` adds $2 \times \text{sizeof}(int)$ to `p`, moving it to point to `arr[3]` ($40$).

```text
*p = 20
*p = 40
```

---

### Exercise 2: `sizeof` Array vs. Pointer Decay

**Problem:** What does this code print on a 64-bit platform where pointers are 8 bytes and `int` is 4 bytes?

```c
#include <stdio.h>

void printSize(int a[100]) {
    printf("func size = %zu\n", sizeof(a));
}

int main(void) {
    int arr[100];
    printf("main size = %zu\n", sizeof(arr));
    printSize(arr);
    return 0;
}
```

**Solution:**
1. In `main`, `arr` is a declared array of $100$ integers. `sizeof(arr)` returns $100 \times \text{sizeof}(int) = 100 \times 4 = 400$ bytes.
2. When passed as a function argument, the array parameter decays to a pointer of its base type (`int *`), regardless of the size declared in the parameter list.
3. Therefore, inside `printSize`, `sizeof(a)` returns the size of `int *`, which is $8$ bytes on a 64-bit target.

```text
main size = 400
func size = 8
```

---

### Exercise 3: 2D Array Flat Offset Calculation

**Problem:** Consider the declaration `short matrix[4][5]`. Assuming the base address of `matrix` is `0x1000`, calculate the memory address of `matrix[2][3]` if `sizeof(short)` is $2$ bytes.

**Solution:**
1. The array dimensions are: $R = 4$, $C = 5$.
2. To access element `matrix[2][3]`, the index is $i = 2$ and $j = 3$.
3. Using the row-major offset formula:
   $$
   \text{offset}(2, 3) = (i \times C + j) \times \text{sizeof}(\text{short})
   $$
   $$
   \text{offset}(2, 3) = (2 \times 5 + 3) \times 2 = (10 + 3) \times 2 = 13 \times 2 = 26 \text{ bytes}
   $$
4. Convert $26$ to hexadecimal: $26 = 16 \times 1 + 10 = 0x1A$.
5. The memory address is:
   $$
   \text{address} = 0x1000 + 0x1A = 0x101A
   $$

```text
Address of matrix[2][3] = 0x101a
```

---

### Exercise 4: Memory Leak Detection

**Problem:** Explain what is wrong with this function and rewrite it to fix the issue.

```c
#include <stdlib.h>

void leak_example(int n) {
    int *arr = (int *)malloc(n * sizeof(int));
    if (n > 100) {
        return;
    }
    free(arr);
}
```

**Solution:**
1. If the function argument `n` is greater than $100$, execution enters the conditional block and returns immediately.
2. The dynamic memory allocated via `malloc` and stored in local pointer variable `arr` is never freed, creating a memory leak on this execution path.
3. **Fix:** Free the memory block before returning, or defer allocation until checking the condition.

```c
void leak_example(int n) {
    if (n > 100) {
        return;
    }
    int *arr = (int *)malloc(n * sizeof(int));
    if (arr != NULL) {
        // use arr...
        free(arr);
    }
}
```

---

### Exercise 5: String Functions and Null-Termination Gotchas

**Problem:** Predict the output of this code. Explain the behavior of `strncpy`.

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char dest[6] = "xxxxx";
    char src[] = "hello";
    
    strncpy(dest, src, 3);
    printf("dest = %s\n", dest);
    return 0;
}
```

**Solution:**
1. `dest` is initialized with $5$ 'x' characters and a null terminator: `{'x', 'x', 'x', 'x', 'x', '\0'}`.
2. `strncpy(dest, src, 3)` copies exactly $3$ characters from `src` (`'h'`, `'e'`, `'l'`) to the beginning of `dest`.
3. `strncpy` does **not** append a null terminator if the length of `src` is greater than or equal to the limit $n$.
4. The contents of `dest` become: `{'h', 'e', 'l', 'x', 'x', '\0'}`.
5. The string printed is `"helxx"`.

```text
dest = helxx
```

---

### Exercise 6: Pointer-to-Pointer Dereferencing

**Problem:** Determine the output of the following code.

```c
#include <stdio.h>

int main(void) {
    int x = 42;
    int *p1 = &x;
    int **p2 = &p1;
    
    printf("**p2 = %d\n", **p2);
    **p2 = 100;
    printf("x = %d\n", x);
    return 0;
}
```

**Solution:**
1. `p1` contains the address of `x`.
2. `p2` contains the address of `p1`.
3. `*p2` dereferences once to obtain `p1` (address of `x`).
4. `**p2` dereferences again to access `x` ($42$).
5. Modifying `**p2` to $100$ modifies the value of `x` directly.

```text
**p2 = 42
x = 100
```

---

### Exercise 7: Realloc Safe Pointer Reassignment

**Problem:** Write a safe routine using `realloc` to resize a dynamically allocated array.

**Solution:**
1. Never assign the return value of `realloc` directly to the original pointer. If `realloc` returns `NULL`, the reference to the original block is overwritten and leaked.
2. Use a temporary pointer to store the result of `realloc` first, check if it is not `NULL`, and assign it to the target pointer.

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int *arr = malloc(5 * sizeof(int));
    if (arr == NULL) return 1;
    
    // Resize array safely
    int *temp = realloc(arr, 10 * sizeof(int));
    if (temp == NULL) {
        // Allocation failed; original arr remains valid.
        free(arr);
        return 1;
    }
    arr = temp; // Safe to reassign
    free(arr);
    return 0;
}
```

---

### Exercise 8: `const` Pointer Parsing

**Problem:** Identify which operations are valid and which generate compiler warnings/errors.

```c
int main(void) {
    int val1 = 10;
    int val2 = 20;
    
    const int *ptr1 = &val1;
    int * const ptr2 = &val1;
    
    ptr1 = &val2; // Op A
    *ptr1 = 30;   // Op B
    
    ptr2 = &val2; // Op C
    *ptr2 = 30;   // Op D
    
    return 0;
}
```

**Solution:**
1. `ptr1` is a pointer to constant data (`const int *`).
   - Op A (`ptr1 = &val2`) is **valid**. The pointer itself is mutable.
   - Op B (`*ptr1 = 30`) is **invalid** (compiler error). The referenced data is const.
2. `ptr2` is a constant pointer to dynamic integer data (`int * const`).
   - Op C (`ptr2 = &val2`) is **invalid** (compiler error). The pointer itself is constant.
   - Op D (`*ptr2 = 30`) is **valid**. The target integer data is mutable.

---

## Common Errors and Gotchas

### 1. Dangling Pointers
* **Cause:** Accessing a pointer after the memory block it references has been deallocated with `free()` or when a local variable goes out of scope.
* **Resolution:** Set pointers to `NULL` immediately after calling `free()` to prevent subsequent read/write attempts.

### 2. Double-Free Errors
* **Cause:** Calling `free()` twice on the same memory block address without an intervening allocation. This corrupts heap structures and triggers allocator crashes.
* **Resolution:** Ensure ownership of pointers is clear. Setting pointers to `NULL` after freeing them is safe, because `free(NULL)` is defined as a no-op by the C standard.

### 3. Out-of-Bounds Memory Corruption
* **Cause:** Accessing indices outside the allocated boundaries of an array (e.g. `arr[size]`). Because C does not perform bound checks, this accesses neighboring stack or heap memory.
* **Resolution:** Validate boundary indexes in loops. Use utility parameters to keep track of array sizes.

---

## Exam Tip: Array Decay and Parameter Size Equivalences

**Array Decay as Parameter Trap:**
When a function parameter is declared as an array, the compiler silently rewrites it as a pointer. For example, the following signatures are identical to the compiler:
```c
void process(int arr[]);
void process(int arr[100]);
void process(int *arr);
```
**Exam consequence:** Inside `process`, `sizeof(arr)` will **always** evaluate to the size of a pointer (usually 8 bytes on modern platforms), not the size of the array! Students often make the mistake of using `sizeof(arr) / sizeof(arr[0])` to find the length of a parameter array. This only works in the scope where the array was declared.

**Dynamic Array Returns:**
Functions cannot return array types directly. To return a list from a function:
1. Return a pointer to a dynamically allocated block (e.g. `malloc`), requiring the caller to explicitly release the resource:
   ```c
   int* create_array(int size) { return malloc(size * sizeof(int)); }
   ```
2. Pass a destination array pointer as a parameter and copy values into it.
