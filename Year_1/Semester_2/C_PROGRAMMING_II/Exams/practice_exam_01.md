# Practice Exam 01: Advanced C Programming

## Context and Grounding
This practice exam provides a comprehensive evaluation of the core concepts taught in C Programming II, including pointer arithmetic, heap memory management, file stream I/O, dynamic data structures, and algorithm complexity. It includes complete solutions and an analytical grading rubric.

---

## Part 1: Theory and Pointer Tracing (25 Points)

### Question 1.1 (10 Points)
Consider the following 64-bit C program:

```c
#include <stdio.h>

int main(void) {
    int arr[] = {10, 20, 30, 40, 50, 60};
    int *p1 = arr;
    int *p2 = arr + 4;

    printf("%td\n", p2 - p1);
    printf("%d\n", *p1 + 2);
    printf("%d\n", *(p1 + 2));
    printf("%d\n", *p2--);
    printf("%d\n", *p2);

    return 0;
}
```
State the exact output printed by each `printf` statement. Explain the pointer arithmetic mechanics behind each output.

### Question 1.2 (15 Points)
Explain the difference between `malloc()` and `calloc()`. Why is writing `ptr = realloc(ptr, new_size);` considered an anti-pattern? Show the canonical safe pattern.

---

## Part 2: Code Debugging and Memory Analysis (25 Points)

### Question 2.1 (25 Points)
Identify three critical memory management errors in the following code. Provide the corrected version.

```c
char* duplicateUpper(const char *str) {
    int len = strlen(str);
    char *copy = (char *)malloc(len);
    for (int i = 0; i <= len; i++) {
        copy[i] = toupper(str[i]);
    }
    return copy;
}

void process(void) {
    char *result = duplicateUpper("hello");
    printf("%s\n", result);
}
```

---

## Part 3: Implementation - Linked Lists and File I/O (50 Points)

### Question 3.1 (25 Points)
Write a function `int deleteNodeByKey(Node **head_ref, int target_key)` that removes the first occurrence of a node with `value == target_key` from a singly linked list. Return 1 if found and deleted, 0 otherwise. Ensure that the memory of the removed node is freed.

### Question 3.2 (25 Points)
Write a function `double computeAverageGPA(const char *binary_filename)` that opens a binary file containing `StudentRecord` structures (fields: `int id`, `char name[32]`, `double gpa`), calculates the mean GPA of all records, closes the file, and returns the result. Return `-1.0` if the file cannot be opened or contains zero records.

---

## Complete Solutions and Grading Key

### Solution 1.1
Output:
```text
4
12
30
50
40
```
* `p2 - p1`: Difference between pointers to array elements yields the distance in elements ($4 - 0 = 4$).
* `*p1 + 2`: Dereferences `p1` (yielding `10`), then adds `2` ($10 + 2 = 12$).
* `*(p1 + 2)`: Evaluates pointer offset `p1 + 2` (address of `arr[2]`), then dereferences ($30$).
* `*p2--`: Postfix decrement has higher precedence than dereference, but returns old address before decrementing. Dereferences `arr[4]` ($50$), then decrements `p2` to point to `arr[3]`.
* `*p2`: Dereferences current position `arr[3]` ($40$).

### Solution 1.2
* `malloc(size)` allocates uninitialized heap memory.
* `calloc(num, size)` allocates contiguous memory and clears all bytes to zero (`0x00`).
* Unsafe reallocation overwrites `ptr` with `NULL` if `realloc` fails, causing an unrecoverable memory leak of the original block. Safe pattern:
```c
void *tmp = realloc(ptr, new_size);
if (tmp == NULL) {
    /* Handle error; original ptr remains valid and must be freed */
    free(ptr);
    return NULL;
}
ptr = tmp;
```

### Solution 2.1
1. **Off-by-one allocation**: `malloc(len)` does not allocate space for the terminating `'\0'`. It should be `malloc(len + 1)`.
2. **Buffer overflow / invalid write**: Loop runs to `i <= len` on an under-allocated buffer.
3. **Memory leak**: `process()` calls `duplicateUpper()`, prints `result`, but never calls `free(result)`.

Corrected Code:
```c
char* duplicateUpper(const char *str) {
    if (str == NULL) return NULL;
    size_t len = strlen(str);
    char *copy = (char *)malloc(len + 1);
    if (copy == NULL) return NULL;
    for (size_t i = 0; i < len; i++) {
        copy[i] = (char)toupper((unsigned char)str[i]);
    }
    copy[len] = '\0';
    return copy;
}

void process(void) {
    char *result = duplicateUpper("hello");
    if (result != NULL) {
        printf("%s\n", result);
        free(result);
    }
}
```

### Solution 3.1
```c
int deleteNodeByKey(Node **head_ref, int target_key) {
    if (head_ref == NULL || *head_ref == NULL) return 0;
    
    Node *curr = *head_ref;
    Node *prev = NULL;
    
    /* Check if head node holds the key */
    if (curr->value == target_key) {
        *head_ref = curr->next_node;
        free(curr);
        return 1;
    }
    
    while (curr != NULL && curr->value != target_key) {
        prev = curr;
        curr = curr->next_node;
    }
    
    if (curr == NULL) return 0; /* Key not found */
    
    prev->next_node = curr->next_node;
    free(curr);
    return 1;
}
```

### Solution 3.2
```c
double computeAverageGPA(const char *binary_filename) {
    if (binary_filename == NULL) return -1.0;
    
    FILE *fp = fopen(binary_filename, "rb");
    if (fp == NULL) return -1.0;
    
    StudentRecord rec;
    double total_gpa = 0.0;
    size_t count = 0;
    
    while (fread(&rec, sizeof(StudentRecord), 1, fp) == 1) {
        total_gpa += rec.gpa;
        count++;
    }
    
    fclose(fp);
    
    if (count == 0) return -1.0;
    return total_gpa / (double)count;
}
```

