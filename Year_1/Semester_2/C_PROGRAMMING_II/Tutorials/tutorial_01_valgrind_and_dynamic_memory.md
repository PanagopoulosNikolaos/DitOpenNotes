# Tutorial 01: Valgrind and Heap Memory Debugging

## Context and Grounding
This tutorial provides a hands-on guide to detecting, tracing, and resolving memory leaks, invalid pointer dereferences, and memory corruption using Valgrind (`memcheck`). It reinforces the memory allocation concepts introduced in `Lectures/lecture_01_pointers_and_dynamic_memory.md`.

---

## 1. Prerequisites and Setup
To compile code with full debugging symbols suitable for Valgrind inspection, invoke `gcc` with the `-g3` flag and disable compiler optimizations:

```bash
gcc -Wall -Wextra -g3 -O0 program.c -o program
```

Execute your binary through Valgrind's memory check tool:

```bash
valgrind --leak-check=full --show-leak-kinds=all --track-origins=yes ./program
```

---

## 2. Common Valgrind Error Diagnostics

### 2.1 Invalid Write / Invalid Read
Occurs when reading or writing past the allocated boundaries of a heap buffer.

```c
/* Buggy snippet */
int *arr = (int *)malloc(5 * sizeof(int));
arr[5] = 100; /* Buffer overflow: valid indices are 0 to 4 */
```

Valgrind Output:
```text
==12345== Invalid write of size 4
==12345==    at 0x10918B: main (program.c:6)
==12345==  Address 0x4a4a054 is 0 bytes after a block of size 20 alloc'd
```

*Solution:* Verify array bounds and loop termination predicates ($i < N$, not $i \le N$).

### 2.2 Definitely Lost (Direct Memory Leak)
Occurs when a heap-allocated pointer is overwritten or falls out of scope without invoking `free()`.

```c
void leakMemory(void) {
    char *buf = (char *)malloc(1024);
    /* Function exits without freeing buf */
}
```

Valgrind Output:
```text
==12345== 1,024 bytes in 1 blocks are definitely lost in loss record 1 of 1
==12345==    at 0x4848899: malloc (in /usr/libexec/valgrind/vgpreload_memcheck-amd64-linux.so)
==12345==    by 0x10915E: leakMemory (program.c:4)
```

*Solution:* Ensure every execution path (including error exits) executes `free(buf)`.

---

## 3. Practical Exercise: Leak-Free Dynamic String Concatenation

Implement a function `concatStrings` that dynamically allocates sufficient heap memory to merge two C-strings:

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* concatStrings(const char *s1, const char *s2) {
    if (s1 == NULL || s2 == NULL) return NULL;
    
    size_t len1 = strlen(s1);
    size_t len2 = strlen(s2);
    
    char *result = (char *)malloc(len1 + len2 + 1);
    if (result == NULL) return NULL;
    
    memcpy(result, s1, len1);
    memcpy(result + len1, s2, len2);
    result[len1 + len2] = '\0';
    
    return result;
}

int main(void) {
    char *msg = concatStrings("Data Structures ", "in C");
    if (msg != NULL) {
        printf("%s\n", msg);
        free(msg); /* Deallocate dynamically allocated memory */
    }
    return 0;
}
```

Expected Valgrind Summary:
```text
==12345== All heap blocks were freed -- no leaks are possible
==12345== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 0 from 0)
```

