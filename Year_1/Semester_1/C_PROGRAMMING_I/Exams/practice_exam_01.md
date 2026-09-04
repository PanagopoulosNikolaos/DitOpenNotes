# C Programming I: Practice Examination 01

**Course**: C Programming I (Code: 103)  
**Duration**: 2 Hours  
**Evaluation**: Maximum 100 Points  
**Format**: Closed Book, Standard ANSI/ISO C11  

---

## Part A: Multiple Choice & Concept Evaluation (25 Points)

### Question 1 (5 Points)
Which of the following describes the behavior of passing an array identifier to a function in C?
* A) The entire array is copied element-by-element onto the stack frame.
* B) The array identifier decays into a pointer pointing to the zeroth element of the array.
* C) C forbids passing arrays to functions.
* D) The array is automatically dynamically allocated on the heap.

### Question 2 (5 Points)
What is the printed output of the following C code snippet?
```c
int a = 10, b = 20;
int *p1 = &a, *p2 = &b;
*p1 = *p2 + 5;
p2 = p1;
*p2 = *p2 * 2;
printf("%d %d\n", a, b);
```
* A) `25 20`
* B) `50 20`
* C) `50 40`
* D) `25 40`

### Question 3 (5 Points)
Which format mode string passed to `fopen` should be selected to append text data to an existing file without erasing previous contents?
* A) `"w"`
* B) `"r+"`
* C) `"a"`
* D) `"wb"`

### Question 4 (5 Points)
Given `int arr[5] = {1, 2, 3, 4, 5};`, which expression evaluates to the memory address of the third element (`3`)?
* A) `arr + 2`
* B) `&arr[2]`
* C) `arr + 3`
* D) Both A and B

### Question 5 (5 Points)
What occurs when an uninitialized local scalar variable declared inside a function is read?
* A) It defaults to 0.
* B) It defaults to NULL.
* C) It produces undefined behavior because it accesses indeterminate stack garbage.
* D) The compiler generates a runtime exception.

---

## Part B: Code Output Tracing (25 Points)

Trace the exact output produced by the following program:
```c
#include <stdio.h>

void modifyValues(int *x, int y) {
    *x += 10;
    y += 15;
}

int main(void) {
    int val_a = 5;
    int val_b = 8;
    modifyValues(&val_a, val_b);
    printf("Result: val_a = %d, val_b = %d\n", val_a, val_b);
    return 0;
}
```

---

## Part C: Defect Identification & Debugging (20 Points)

Identify the two critical defects in the following function and provide the corrected version:
```c
char* createGreeting(const char *name) {
    char buffer[128];
    sprintf(buffer, "Welcome, %s!", name);
    return buffer;
}
```

---

## Part D: Coding Implementation (30 Points)

Write a function `copyEvenNumbers` in C with the following signature:
```c
size_t copyEvenNumbers(const int *source, size_t src_len, int *dest, size_t dest_capacity);
```
* The function must iterate through `source`, identify all even numbers, and copy them sequentially into `dest`.
* It must not exceed `dest_capacity`.
* It must return the actual count of even elements copied.
* Validate all pointer parameters defensively.

---

## Comprehensive Solutions and Marking Scheme

### Part A Solutions
1. **B**: In C, array names decay to a pointer to their first element (`&arr[0]`).
2. **B**:
   - `*p1 = *p2 + 5` sets `a = 20 + 5 = 25`.
   - `p2 = p1` causes `p2` to point to `a`.
   - `*p2 = *p2 * 2` multiplies `a` by 2, resulting in `a = 50`.
   - `b` remains untouched at `20`. Output: `50 20`.
3. **C**: `"a"` opens a file for writing at the end of the file (append mode).
4. **D**: Both `arr + 2` and `&arr[2]` compute the memory address of the third element.
5. **C**: Reading uninitialized automatic variables yields indeterminate garbage values.

### Part B Solution
- `val_a` is passed by pointer (`&val_a`), so `*x += 10` alters `val_a` to $5 + 10 = 15$.
- `val_b` is passed by value, so `y += 15` mutates a local copy inside `modifyValues`. `val_b` remains `8`.
- Output:
  ```text
  Result: val_a = 15, val_b = 8
  ```

### Part C Solution
**Defects Identified:**
1. **Returning Stack-Local Pointer**: `buffer` is allocated on the function's stack frame. When `createGreeting` returns, its stack frame is discarded, creating a dangling pointer and undefined behavior.
2. **Potential Buffer Overflow**: `sprintf` performs unbounded writing into `buffer`.

**Corrected Version:**
The caller must provide the destination buffer and capacity:
```c
#include <stdio.h>
#include <stddef.h>

/**
 * Formats a greeting string into a caller-supplied buffer.
 *
 * Args:
 *   dest (char *): Destination character buffer.
 *   capacity (size_t): Size of destination buffer.
 *   name (const char *): Subject name string.
 *
 * Returns:
 *   int: Number of characters written, or -1 on error.
 */
int formatGreeting(char *dest, size_t capacity, const char *name) {
    if (dest == NULL || name == NULL || capacity == 0) {
        return -1;
    }
    return snprintf(dest, capacity, "Welcome, %s!", name);
}
```

### Part D Solution
```c
#include <stddef.h>

/**
 * Copies all even integers from source into destination buffer.
 *
 * Args:
 *   source (const int *): Source integer array.
 *   src_len (size_t): Number of elements in source array.
 *   dest (int *): Destination buffer for even elements.
 *   dest_capacity (size_t): Maximum capacity of destination buffer.
 *
 * Returns:
 *   size_t: Count of even numbers successfully copied.
 */
size_t copyEvenNumbers(const int *source, size_t src_len, int *dest, size_t dest_capacity) {
    if (source == NULL || dest == NULL || dest_capacity == 0) {
        return 0;
    }

    size_t copied_count = 0;
    for (size_t i = 0; i < src_len && copied_count < dest_capacity; ++i) {
        if (source[i] % 2 == 0) {
            dest[copied_count] = source[i];
            copied_count++;
        }
    }
    return copied_count;
}
```

