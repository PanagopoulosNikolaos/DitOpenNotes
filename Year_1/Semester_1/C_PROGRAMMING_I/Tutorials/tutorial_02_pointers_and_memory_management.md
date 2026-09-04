# Tutorial 02: Pointers and Memory Safety

## Context and Grounding
This tutorial provides an in-depth practical investigation into memory addressing, pointer safety patterns, common memory defects, and automated dynamic verification using AddressSanitizer (ASan).

---

## 1. Virtual Address Space Anatomy

When a C executable executes on Linux, the operating system assigns it a virtual address space partitioned into distinct segments:

```text
High Memory (0x7FFF_FFFF_FFFF)
   ┌───────────────────────────┐
   │ Environment & CLI Args    │
   ├───────────────────────────┤
   │ Stack (grows downwards)   │ Local variables, stack frames
   │          │                │
   │          ▼                │
   │                           │
   │          ▲                │
   │          │                │
   │ Heap  (grows upwards)     │ Dynamic allocations (malloc, calloc)
   ├───────────────────────────┤
   │ BSS Segment               │ Uninitialized globals and statics
   ├───────────────────────────┤
   │ Data Segment              │ Initialized globals and statics
   ├───────────────────────────┤
   │ Text Segment              │ Executable machine instructions (read-only)
   └───────────────────────────┘
Low Memory  (0x0000_0000_0000)
```

---

## 2. Common Pointer Vulnerabilities

### 2.1 Null Pointer Dereference
Attempting to read or write through a pointer containing `NULL` (address 0) generates a `SIGSEGV` (Segmentation fault) because page 0 is unmapped by the operating system.

```c
int *ptr = NULL;
// Defect: Dereferencing without validation
// *ptr = 50; // Triggers immediate SIGSEGV

// Safe canonical defensive check:
if (ptr != NULL) {
    *ptr = 50;
}
```

### 2.2 Dangling Pointer
A dangling pointer retains a memory address after the storage at that address has been deallocated or invalidated.

```c
// Anti-pattern: Returning address of stack-local variable
int* getLocalCounter(void) {
    int counter = 10;
    return &counter; // Dangerous: frame destroyed upon function return!
}
```

### 2.3 Buffer Overrun via Pointer Arithmetic
Advancing a pointer beyond the bounds of an allocated array corrupts adjacent memory blocks:
```c
int buffer[4] = {1, 2, 3, 4};
int *p = buffer;

// Valid indices: p + 0 through p + 3
// Undefined behavior:
int out_of_bounds = *(p + 4); // Accesses unallocated stack data
```

---

## 3. Dynamic Analysis with AddressSanitizer (ASan)

Modern GCC versions provide built-in compiler instrumentation via AddressSanitizer to detect memory errors at runtime with zero manual instrumentation.

### 3.1 Enabling ASan
Compile with the `-fsanitize=address` flag:
```bash
gcc -Wall -Wextra -std=c11 -fsanitize=address -g3 program.c -o program
```

### 3.2 Interpreting ASan Output
When an invalid memory access occurs, the binary immediately halts and prints an informative diagnostic report:
```text
=================================================================
==12345==ERROR: AddressSanitizer: stack-buffer-overflow on address 0x7ffd1e8
READ of size 4 at 0x7ffd1e8 thread T0
    #0 0x1174 in main program.c:12
    #1 0x7f4c in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6)
Address 0x7ffd1e8 is located in stack of thread T0 at offset 48 in frame
    #0 0x10b9 in main program.c:6
=================================================================
```

---

## 4. Practical Exercise: Safe Pointer Manipulation

Write a function that reverses an array in-place using two pointer iterators (head and tail pointers):

```c
#include <stdio.h>

/**
 * Reverses an integer array in place using pointer arithmetic.
 *
 * Args:
 *   start_ptr (int *): Pointer to the beginning of the buffer.
 *   length (size_t): Number of elements in the buffer.
 *
 * Returns:
 *   void.
 */
void reverseArrayInPlace(int *start_ptr, size_t length) {
    if (start_ptr == NULL || length <= 1) {
        return;
    }

    int *left = start_ptr;
    int *right = start_ptr + length - 1;

    while (left < right) {
        int temp = *left;
        *left = *right;
        *right = temp;

        left++;
        right--;
    }
}

int main(void) {
    int dataset[5] = {1, 2, 3, 4, 5};
    reverseArrayInPlace(dataset, 5);

    for (size_t i = 0; i < 5; ++i) {
        printf("%d ", dataset[i]);
    }
    printf("\n");
    return 0;
}
```

