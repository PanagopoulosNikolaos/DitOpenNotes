# Topic 11: Structures, Unions, and Enums

## 1. Structures (struct)

A structure groups related values of different types into one named unit — C's fundamental record type:

```c
struct Student {
    char name[50];
    int  id;
    double gpa;
};
```

Declaration and member access:

```c
struct Student s1;                  // Declare (the keyword 'struct' is required)
struct Student s2 = {"Alice", 101, 3.9};   // Initialize

strcpy(s2.name, "Alice");           // Access members with the dot operator
s2.id = 101;
s2.gpa = 3.9;

struct Student s3 = s2;             // Whole-struct copy (all members copied)
```

---

## 2. typedef — Hiding the Keyword

`typedef` creates a type alias so `struct` does not have to be written every time:

```c
typedef struct {
    int x;
    int y;
} Point;

Point p = {3, 4};        // No 'struct' keyword needed
```

This is the dominant convention in real-world C code.

---

## 3. Structures and Functions

Structs are passed **by value** (copied) by default; for large structs or modification, pass pointers:

```c
void moveByValue(Point p) { p.x += 1; }        // Caller unaffected

void moveByPointer(Point *p) { p->x += 1; }    // Caller affected

void show(const Point *p) {                    // const = read-only intent
    printf("(%d, %d)\n", p->x, p->y);
}

Point q = {0, 0};
moveByPointer(&q);     // q is now (1, 0)
```

**The arrow operator:** when working through a pointer, `p->member` is shorthand for `(*p).member`. Both are identical; `->` is universally preferred.

---

## 4. Nested Structures and Arrays of Structures

```c
typedef struct {
    int day;
    int month;
    int year;
} Date;

typedef struct {
    char title[64];
    Date due;                 // A struct inside a struct
} Assignment;

Assignment hw[] = {           // Array of structures
    {"Essay",  {1, 12, 2025}},
    {"Lab 3",  {5, 12, 2025}}
};

hw[0].due.month;              // Chained access: element, member, member
```

---

## 5. Unions

A union stores **one member at a time** — all members share the same memory, and its size equals the largest member:

```c
typedef union {
    int   i;
    float f;
    char  bytes[4];
} Value;

Value v;
v.i = 65;                 // Valid now
printf("%c\n", v.bytes[0]);  // 'A' — same 4 bytes reinterpreted
v.f = 3.14f;              // Overwrites the int (v.i is now meaningless)
```

Reading a member other than the last one written is implementation-defined; in practice unions are used for type punning, memory views, and tagged variants:

```c
typedef struct {
    enum {INT, FLOAT} tag;   // Tag records which member is active
    union { int i; float f; } data;
} Number;
```

---

## 6. Enumerations (enum)

An enum defines named integer constants, making "magic numbers" self-documenting:

```c
enum Color { RED, GREEN, BLUE };          // RED=0, GREEN=1, BLUE=2
enum Level { LOW = 1, MEDIUM, HIGH };     // Explicit start: 1, 2, 3

enum Color c = GREEN;

switch (c) {
    case RED:   printf("stop\n");    break;
    case GREEN: printf("go\n");      break;
    case BLUE:  printf("cool\n");    break;
}
```

Enums are frequently used for state machines, menu codes, and error codes — they combine the readability of names with the switchability of integers.

---

## 7. Bit Fields (Brief)

Struct members can be sized in bits, useful for hardware/flag packing:

```c
typedef struct {
    unsigned int visible : 1;
    unsigned int mode    : 3;   // 0-7
    unsigned int id      : 12;
} Flags;
```

Layout details are implementation-defined; use only when memory packing matters.

---

## 8. Common Pitfalls

* Forgetting `struct`/`typedef` in the declaration of plain structs.
* Assigning with `=` to a **char array member** (`s.name = "Bob"` is illegal) — use `strcpy`/`snprintf`.
* Confusing `.` (on a struct) with `->` (on a pointer to struct).
* Assuming struct memory layout is exactly as written: the compiler may insert **padding** bytes between members for alignment.
* Treating all union members as simultaneously valid — only the last-written one is.

---

## 9. Summary

* `struct` aggregates heterogeneous data; `typedef` cleans up declarations.
* Structs pass by value; pass pointers and use `->` for efficiency or mutation.
* `union` overlays members on shared storage; an outer tag documents the active one.
* `enum` gives readable names to related integer constants.
