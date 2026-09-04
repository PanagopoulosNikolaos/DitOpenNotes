# Advanced Pointers and Memory Architecture in C

## Overview
Procedural systems development in C requires strict comprehension of pointer scaling rules, multi-level indirection, heap fragmentation, and virtual address spaces.

---

## 1. Multi-Level Indirection (Double Pointers)

Double pointers (`T**`) hold memory addresses of single pointer variables. They are essential in two canonical systems patterns:
1. **Modifying Caller Pointers**: Reallocating or mutating head pointers of dynamic lists:
   ```c
   void insertHead(Node **head_ref, int val) {
       Node *new_node = (Node *)malloc(sizeof(Node));
       new_node->val = val;
       new_node->next = *head_ref;
       *head_ref = new_node;
   }
   ```
2. **Two-Dimensional Dynamic Matrices**: Allocating contiguous row buffers indexed by an array of pointers:
   ```c
   int **matrix = (int **)malloc(rows * sizeof(int *));
   for (size_t i = 0; i < rows; i++) {
       matrix[i] = (int *)malloc(cols * sizeof(int));
   }
   ```

---

## 2. Pointer Arithmetic and Scaling

Pointer additions and subtractions scale automatically by the size of the referenced type (`sizeof(*p)`):
* Given `int *ptr = arr;` on an x86_64 system where `sizeof(int) == 4`:
  $$\text{Address of } (ptr + k) = \text{Address of } ptr + (k \times 4)$$
* Subtracting two pointers of the same type `p2 - p1` produces a signed offset of type `ptrdiff_t` (format specifier `%td`), denoting the number of elements separating them, not the raw byte difference.

---

## 3. Dynamic Heap Management Patterns

### 3.1 The Safe Realloc Pattern
Reallocating in-place with direct assignment leaks the original block if memory is exhausted:
```c
/* ANTI-PATTERN: Leaks original block if realloc returns NULL */
ptr = realloc(ptr, new_size);

/* CANONICAL SAFE PATTERN: Preserves old pointer on failure */
void *temp_ptr = realloc(ptr, new_size);
if (temp_ptr == NULL) {
    free(ptr); /* Frees original memory to prevent leakage */
    return NULL;
}
ptr = temp_ptr;
```

### 3.2 Allocation Tooling and Leak Detection
* **Valgrind Memcheck**:
  ```bash
  valgrind --leak-check=full --show-leak-kinds=all --track-origins=yes ./binary_name
  ```
* **GCC AddressSanitizer**:
  ```bash
  gcc -Wall -Wextra -fsanitize=address,undefined -g source.c -o binary_name
  ```

