# Topic 12: Dynamic Memory Management

## 1. Stack vs. Heap

| | Stack | Heap |
|--|-------|------|
| Allocation | Automatic (function scope) | Manual (`malloc` family) |
| Lifetime | Dies when the function returns | Until explicitly `free`d |
| Size limit | Small (typically ~1–8 MB) | Large (available RAM) |
| Speed | Very fast | Slower, managed by allocator |
| Size known | Must be known at declaration | Decided at **runtime** |

Use dynamic memory when the required size is unknown at compile time or the data must outlive the creating function. The interface lives in `<stdlib.h>`.

---

## 2. malloc — Allocate a Block

```c
int *arr = malloc(n * sizeof(int));   // n ints, contents UNINITIALIZED
if (arr == NULL) {                    // malloc can fail!
    fprintf(stderr, "Out of memory.\n");
    return 1;
}
```

`malloc(size)` returns a `void *` pointing to at least `size` bytes, or `NULL` on failure. It returns `void *` so it can be assigned to any pointer type without a cast (casting it is legal but hides missing `#include <stdlib.h>`).

**Always multiply by `sizeof(type)`** — the most common allocation bug is allocating too little (e.g. `malloc(n)` for n ints).

---

## 3. calloc, realloc, free

```c
// calloc: allocate and zero-initialize
int *zeros = calloc(n, sizeof(int));      // n elements, all 0

// realloc: resize an existing block
int *bigger = realloc(arr, 2 * n * sizeof(int));
if (bigger == NULL) {
    // arr is STILL valid — only the new size failed
    free(arr);
    return 1;
}
arr = bigger;     // Contents are preserved up to the smaller of the sizes

// free: release the memory
free(arr);
arr = NULL;       // Prevents accidental reuse (dangling pointer)
```

Key rules:

* `free(NULL)` is legal and does nothing — a `NULL`-checked loop never needs a special case.
* After `free`, the pointer is **dangling**; assigning `NULL` makes misuse crash immediately instead of corrupting memory silently.
* Every allocation needs exactly one `free` — and the memory must be freed by the same "owner" that allocated it.

---

## 4. Common Dynamic Patterns

**Dynamic array sized at runtime:**

```c
size_t n;
scanf("%zu", &n);

double *data = malloc(n * sizeof *data);
if (!data) { /* handle failure */ }
for (size_t i = 0; i < n; i++) data[i] = i * 1.5;
free(data);
```

**Growing an array inside a loop:**

```c
size_t count = 0, capacity = 8;
int *items = malloc(capacity * sizeof *items);

while (more_input()) {
    if (count == capacity) {
        capacity *= 2;                                        // Geometric growth
        int *tmp = realloc(items, capacity * sizeof *items);
        if (!tmp) { free(items); return -1; }
        items = tmp;
    }
    items[count++] = next_value();
}
free(items);
```

**Dynamic strings:**

```c
char *dup = malloc(strlen(src) + 1);   // +1 for '\0'
if (dup) strcpy(dup, src);
```

**Dynamically allocated structs:**

```c
typedef struct { int id; char name[32]; } Person;

Person *p = malloc(sizeof *p);
if (!p) return -1;
p->id = 7;                       // Arrow operator on heap structs
snprintf(p->name, sizeof p->name, "Nikos");
free(p);
```

Note the `sizeof *pointer` idiom: the type is inferred and cannot drift out of sync with the declaration.

---

## 5. Memory Errors and How to Avoid Them

| Error | Cause | Symptom |
|-------|-------|---------|
| **Memory leak** | `free` never called, or pointer overwritten first | Program RAM grows forever |
| **Dangling pointer** | Using a pointer after `free` (use-after-free) | Crashes, corrupted data, security holes |
| **Double free** | `free` called twice on the same block | Allocator corruption / abort |
| **Buffer overrun** | Writing past the allocated size | Silent corruption elsewhere |
| **Uninitialized read** | Reading `malloc` memory before writing | Nondeterministic values |

Tools that detect these automatically:

```bash
valgrind ./program                # Reports leaks and invalid accesses
gcc -fsanitize=address -g main.c  # AddressSanitizer catches errors at runtime
```

---

## 6. Design Rules of Thumb

1. Every `malloc`/`calloc`/`realloc` result is checked for `NULL`.
2. Every allocation path has a matching, reachable `free`.
3. Free with the same "unit" that allocated; set pointers to `NULL` after freeing.
4. Prefer failing fast on allocation failure over pretending it succeeded.
5. For long-lived programs, track ownership: who creates a block and who destroys it.

---

## 7. Summary

* The heap provides runtime-sized, long-lived memory through `malloc`, `calloc`, `realloc`, and `free`.
* Check every allocation; size requests with `sizeof *ptr`.
* Leaks, dangling pointers, and double frees are the classic hazards — `valgrind` and ASan find them.
* Free memory exactly once and null out the pointer afterward.
