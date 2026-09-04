# Advanced Pointers, Memory Allocation, and Data Structures Exercises

## Context and Grounding
This exercise set reinforces core topics from `Lectures/lecture_01_pointers_and_dynamic_memory.md` and `Lectures/DSA-Guide-in-C.md`. It provides comprehensive practice problems with complete, step-by-step solutions.

---

## Problem Set

### Problem 1: Pointer Arithmetic and Array Traversal
Given an integer array `arr = {12, 24, 36, 48, 60}` and a pointer `p = arr + 1`:
1. What is the value of `*p`?
2. What is the value of `*(p + 2)`?
3. What is the value of `p[2]`?
4. Write a function using pure pointer arithmetic (no subscript operator `[]`) that sums the elements of an array.

### Problem 2: Safe String Duplication
Write a C function `safeStrdup(const char *src)` that duplicates a null-terminated string onto the heap. Your solution must:
1. Return `NULL` if `src` is `NULL` or if allocation fails.
2. Allocate exactly the required number of bytes.
3. Copy data securely without buffer overflow.

### Problem 3: Singly Linked List Node Reversal
Write a function `reverseList(Node **head_ref)` that reverses a singly linked list in-place in $O(n)$ time and $O(1)$ auxiliary space.

### Problem 4: File Record Extraction
Write a function `countOccurrences(const char *filename, const char *word)` that counts how many times `word` appears as a distinct token in the specified text file.

---

## Detailed Step-by-Step Solutions

### Solution 1
1. `arr + 1` points to index 1 of the array. Thus, `*p = arr[1] = 24`.
2. `*(p + 2)` points to index $1 + 2 = 3$. Thus, `*(p + 2) = arr[3] = 48`.
3. The subscript operator `p[2]` is defined by the standard as `*(p + 2) = 48`.
4. Pointer-based summation:
```c
long sumArray(const int *arr, size_t n) {
    long total = 0;
    const int *end = arr + n;
    for (const int *p = arr; p < end; p++) {
        total += *p;
    }
    return total;
}
```

### Solution 2
```c
#include <stdlib.h>
#include <string.h>

char* safeStrdup(const char *src) {
    if (src == NULL) {
        return NULL;
    }
    
    size_t len = strlen(src);
    char *dest = (char *)malloc(len + 1);
    if (dest == NULL) {
        return NULL;
    }
    
    memcpy(dest, src, len + 1);
    return dest;
}
```

### Solution 3
```c
typedef struct Node {
    int data;
    struct Node *next;
} Node;

void reverseList(Node **head_ref) {
    if (head_ref == NULL || *head_ref == NULL) {
        return;
    }
    
    Node *prev = NULL;
    Node *current = *head_ref;
    Node *next = NULL;
    
    while (current != NULL) {
        next = current->next;  /* Store pointer to next node */
        current->next = prev;  /* Reverse pointer direction */
        prev = current;        /* Advance prev pointer */
        current = next;        /* Advance current pointer */
    }
    
    *head_ref = prev;          /* Update head to point to previous tail */
}
```

### Solution 4
```c
#include <stdio.h>
#include <string.h>

int countOccurrences(const char *filename, const char *word) {
    if (filename == NULL || word == NULL) return -1;
    
    FILE *fp = fopen(filename, "r");
    if (fp == NULL) return -1;
    
    char buffer[256];
    int count = 0;
    
    while (fscanf(fp, "%255s", buffer) == 1) {
        if (strcmp(buffer, word) == 0) {
            count++;
        }
    }
    
    fclose(fp);
    return count;
}
```

