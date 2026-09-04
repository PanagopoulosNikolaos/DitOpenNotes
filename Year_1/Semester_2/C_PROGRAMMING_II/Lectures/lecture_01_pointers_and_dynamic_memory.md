# Lecture 01: Pointers and Dynamic Memory Allocation

## Context and Grounding
This lecture note provides foundational theory and practical semantics for advanced pointer manipulation and heap memory management in C. It grounds the concepts implemented in `Exercises/Structures` and subsequent data structure implementations in C Programming II.

---

## 1. Pointer Mechanics and Memory Architecture

### 1.1 Memory Address Spaces and Pointer Types
In C, every variable resides at a contiguous sequence of byte addresses in virtual memory. A pointer is a variable whose r-value represents the memory address of an l-value.

```c
int val = 42;
int *ptr = &val; /* ptr stores the address of val */
```

* **Address-of Operator (`&`)**: Yields the address of an object.
* **Dereference Operator (`*`)**: Accesses the value stored at the address pointed to.

### 1.2 Pointer Arithmetic
Pointer arithmetic is scaled automatically by the byte size of the referenced type:
$$\text{Address}(ptr + k) = \text{Address}(ptr) + k \times \text{sizeof}(*ptr)$$

```c
int arr[5] = {10, 20, 30, 40, 50};
int *p = arr;

printf("First element: %d\n", *p);       /* 10 */
printf("Second element: %d\n", *(p + 1)); /* 20 */
```

### 1.3 Double Pointers and Indirection
A pointer to a pointer (`type **`) holds the memory address of another pointer variable. Double pointers are essential when a callee function must modify the address stored in a caller's pointer variable (e.g., dynamic reallocation, linked list head updates).

```c
void allocateBuffer(char **buffer, size_t size) {
    *buffer = (char *)malloc(size);
}
```

---

## 2. Dynamic Memory Management Functions

Standard dynamic memory functions are declared in `<stdlib.h>` and manage allocations on the process heap.

### 2.1 Heap Allocation Functions
| Function | Signature | Operational Semantics |
|---|---|---|
| `malloc` | `void* malloc(size_t size)` | Allocates `size` uninitialized bytes. Returns `NULL` on failure. |
| `calloc` | `void* calloc(size_t num, size_t size)` | Allocates `num * size` bytes and initializes all bits to zero. |
| `realloc` | `void* realloc(void *ptr, size_t new_size)` | Resizes previously allocated block. Copies data and frees old block if moved. |
| `free` | `void free(void *ptr)` | Deallocates heap block. No-op if `ptr` is `NULL`. |

### 2.2 Safe Reallocation Pattern
Direct assignment of `realloc` to the original pointer creates memory leaks if allocation fails:

```c
/* Unsafe pattern: ptr is overwritten with NULL on failure, losing reference */
ptr = realloc(ptr, new_size); 

/* Safe canonical pattern */
void *tmp = realloc(ptr, new_size);
if (tmp == NULL) {
    /* Handle allocation failure; original ptr remains valid */
    free(ptr);
    exit(EXIT_FAILURE);
}
ptr = tmp;
```

---

## 3. Common Memory Vulnerabilities

1. **Memory Leaks**: Allocating heap blocks without executing a corresponding `free()`.
2. **Dangling Pointers**: Retaining a pointer value after the referenced block has been deallocated.
3. **Double Free**: Calling `free()` twice on the same memory address, corrupting heap metadata.
4. **Buffer Overflows**: Writing past the boundary of allocated heap capacity.

---

## 4. Code Example: Dynamic 2D Array Allocation

```c
#include <stdio.h>
#include <stdlib.h>

int** createMatrix(int rows, int cols) {
    int **matrix = (int **)malloc(rows * sizeof(int *));
    if (matrix == NULL) {
        return NULL;
    }
    
    for (int i = 0; i < rows; i++) {
        matrix[i] = (int *)malloc(cols * sizeof(int));
        if (matrix[i] == NULL) {
            /* Cleanup previously allocated rows */
            for (int j = 0; j < i; j++) {
                free(matrix[j]);
            }
            free(matrix);
            return NULL;
        }
    }
    return matrix;
}

void freeMatrix(int **matrix, int rows) {
    if (matrix == NULL) return;
    for (int i = 0; i < rows; i++) {
        free(matrix[i]);
    }
    free(matrix);
}
```

