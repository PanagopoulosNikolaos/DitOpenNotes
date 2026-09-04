# Assignment 02: Generic Doubly Linked List and Priority Queue

## Objective
Implement a reusable, generic Abstract Data Type (ADT) library in standard C using `void*` data pointers, function pointers for custom comparisons and deallocations, and dynamic heap allocation.

---

## Technical Specifications

### 1. Generic Doubly Linked List Interface (`list.h`)
```c
typedef struct ListNode {
    void *data;
    struct ListNode *prev;
    struct ListNode *next;
} ListNode;

typedef struct List {
    ListNode *head;
    ListNode *tail;
    size_t size;
    void (*free_func)(void *data);
    int (*compare_func)(const void *a, const void *b);
} List;

List* listCreate(void (*free_func)(void *), int (*compare_func)(const void *, const void *));
void listPushFront(List *list, void *data);
void listPushBack(List *list, void *data);
void* listPopFront(List *list);
void* listPopBack(List *list);
int listRemove(List *list, const void *key);
void listDestroy(List *list);
```

### 2. Generic Priority Queue (`pqueue.h`)
Using the generic list or a dynamic binary heap array, implement a priority queue ADT supporting:
* `PQueue* pqueueCreate(int (*compare_func)(const void *, const void *));`
* `void pqueueEnqueue(PQueue *pq, void *item);`
* `void* pqueueDequeue(PQueue *pq);`
* `void* pqueuePeek(const PQueue *pq);`
* `void pqueueDestroy(PQueue *pq, void (*free_func)(void *));`

### 3. Application Driver: Task Scheduler
Write a test driver program `scheduler.c` that parses tasks containing an integer priority, task ID, and text description. Insert tasks in arbitrary order and execute them in strict priority order, printing execution statistics.

---

## Deliverables & Testing
* Files: `list.h`, `list.c`, `pqueue.h`, `pqueue.c`, `scheduler.c`, `Makefile`.
* Test cases must verify integer, floating-point, and dynamically allocated string payloads.
* All heap blocks must be freed during `listDestroy` and `pqueueDestroy`.

