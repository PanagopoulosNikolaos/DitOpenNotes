# Lecture 03: Structures and Abstract Data Types

## Context and Grounding
This lecture note formalizes user-defined composite data types, memory layout rules (padding and alignment), and dynamic data structure construction in C. It grounds the linked list, stack, and queue implementations covered in `Lectures/DSA-Guide-in-C.md` and `Exercises/Structures/`.

---

## 1. Structures and Memory Layout

### 1.1 Declaration and Type Definition
A structure is a composite type grouping variables of diverse types under a single name:

```c
typedef struct Node {
    int data;
    struct Node *next; /* Self-referential pointer */
} Node;
```

### 1.2 Structure Padding and Alignment
Hardware architectures require multi-byte variables to align at memory addresses that are multiples of their size:
* `char`: 1-byte alignment
* `short`: 2-byte alignment
* `int`, `float`: 4-byte alignment
* `double`, pointers: 8-byte alignment (on 64-bit systems)

The compiler inserts padding bytes to satisfy alignment constraints:

```c
struct Unpadded {
    char a;    /* 1 byte */
    /* 3 padding bytes */
    int b;     /* 4 bytes */
    char c;    /* 1 byte */
    /* 3 padding bytes */
}; /* Total size: 12 bytes */

struct Optimized {
    int b;     /* 4 bytes */
    char a;    /* 1 byte */
    char c;    /* 1 byte */
    /* 2 padding bytes */
}; /* Total size: 8 bytes */
```

---

## 2. Dynamic Abstract Data Types

### 2.1 Singly Linked List Operations
A linked list consists of nodes allocated on the heap, connected sequentially via pointers.

* **Insertion at Head**: $O(1)$ time complexity.
* **Traversal / Search**: $O(n)$ time complexity.
* **Deletion**: $O(n)$ to locate, $O(1)$ to unbind pointer and deallocate node memory.

### 2.2 Stack Implementation (LIFO)
A stack restricts insertions and deletions to the top node:
* `push(Stack **top, int val)`: Prepends a node to the list.
* `pop(Stack **top)`: Removes and returns data from the top node.

### 2.3 Queue Implementation (FIFO)
A queue inserts at the rear and removes from the front. Maintaining both `head` and `tail` pointers enables $O(1)$ enqueue and dequeue operations:

```c
typedef struct Queue {
    Node *front;
    Node *rear;
} Queue;
```

---

## 3. Function Pointers and Generic Abstractions

Function pointers enable higher-order functions, callbacks, and polymorphic data structures:

```c
typedef int (*Comparator)(const void *, const void *);

void bubbleSort(void *base, size_t n, size_t size, Comparator cmp);
```

Using `void*` alongside function pointers allows building generic linked lists and container libraries in standard C.

