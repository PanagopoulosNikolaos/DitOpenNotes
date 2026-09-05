# Topic 9: Pointers — Basics

## 1. Memory, Addresses, and Pointers

Every byte of memory has a numeric **address**. A variable lives at some address; a **pointer** is a variable that stores such an address.

```c
int x = 42;
int *p = &x;      // p holds the address of x
```

* `&` — the **address-of** operator: `&x` produces a pointer to `x`.
* `*` — the **dereference** (indirection) operator: `*p` accesses the value stored at the address `p` holds.

```c
printf("%d\n", x);     // 42
printf("%p\n", (void*)p);   // e.g. 0x7ffd... (address of x)
printf("%d\n", *p);    // 42 — "what p points to"
*p = 100;              // Changes x itself: x is now 100
```

Read `int *p` as "`p` is a pointer to `int`" — it is the pointed-to type, not the pointer, that fixes how many bytes are read/written on dereference.

---

## 2. NULL Pointers

A pointer that targets nothing is set to `NULL` (from `<stddef.h>`/`<stdio.h>`):

```c
int *p = NULL;
if (p != NULL) { use(*p); }    // Always check before dereferencing
```

Dereferencing `NULL` (or any invalid address) is undefined behavior — typically a segmentation fault. Initialize pointers on creation and never leave them dangling (Topic 12).

---

## 3. Pointers and Functions

Pointers are how a function modifies the caller's data:

```c
void swap(int *a, int *b) {
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

int x = 1, y = 2;
swap(&x, &y);          // x is now 2, y is 1
```

They also allow functions to "return" multiple results via output parameters:

```c
void divide(int a, int b, int *quotient, int *remainder) {
    *quotient  = a / b;
    *remainder = a % b;
}
```

---

## 4. Pointers and Arrays

An array name decays to a pointer to its first element in almost every expression:

```c
int arr[5] = {10, 20, 30, 40, 50};
int *p = arr;              // ≡ int *p = &arr[0];

printf("%d\n", *(p + 2));  // 30
printf("%d\n", arr[2]);    // 30 — the same element
```

The standard defines `arr[i]` as exactly `*(arr + i)`. Pointer arithmetic is **scaled** by the element size: `p + 1` advances by `sizeof(int)` bytes, not 1 byte. (Deep coverage of arithmetic, decay exceptions, and const-qualified pointers is in Topic 10.)

Because of this equivalence, array parameters are really pointers:

```c
void double_all(int *a, int n) {
    for (int i = 0; i < n; i++) a[i] *= 2;   // Modifies the caller's array
}
```

---

## 5. Pointers to Pointers

A pointer's own address can be stored too — `int **pp` holds the address of an `int *`:

```c
int x = 7;
int *p  = &x;
int **pp = &p;

printf("%d\n", **pp);   // 7 — two dereferences
```

Common uses: output parameters that must *replace* a pointer, and the `argv` string array in `main`:

```c
int main(int argc, char *argv[])   // argv is effectively char **
```

---

## 6. Pointers and const

`const` position determines what is protected (full treatment in Topic 10):

```c
const int *p1;      // Value pointed to is read-only
int * const p2 = &x;  // The pointer itself cannot move
```

---

## 7. Common Pitfalls

* **Dereferencing an uninitialized pointer:** `int *p; *p = 5;` writes to a random address — initialize to `NULL` or a valid address.
* **Returning a pointer to a local variable:** the local dies at return; the pointer dangles.
* **Confusing `*` in a declaration with `*` in an expression:** `int *p = &x;` declares; `*p = 5;` dereferences.
* **Wrong pointer type:** `int *p = &d;` (double) will not behave correctly; types must match.
* **Losing the original allocation:** reassigning a pointer without freeing (or storing) what it pointed to leaks memory (Topic 12).

---

## 8. Summary

* A pointer stores an address; `&` takes an address, `*` follows one.
* `NULL` means "points nowhere"; always test before dereferencing.
* Pass pointers to let functions modify caller data or emit multiple results.
* Array indexing is defined in terms of pointer arithmetic; array parameters are pointers in disguise.
