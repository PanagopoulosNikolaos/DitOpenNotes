# Topic 6: Functions

## 1. Why Functions?

Functions divide a program into named, reusable units. Benefits:

* **Reuse:** write once, call many times.
* **Abstraction:** callers need the *what*, not the *how*.
* **Testing:** each unit can be verified independently.
* **Readability:** `main` becomes a high-level outline of the program.

C is call-by-value: a function receives a **copy** of each argument (see §4 for the pointer workaround).

---

## 2. Declaration, Definition, and Prototypes

A **definition** provides the full body; a **prototype** (declaration) tells the compiler the name, return type, and parameter types without the body:

```c
// Prototype (usually at the top of the file or in a header)
double average(double a, double b);

int main(void) {
    printf("%.2f\n", average(4.0, 5.0));   // Safe: compiler already knows average
    return 0;
}

// Definition
double average(double a, double b) {
    return (a + b) / 2.0;
}
```

Prototype syntax: `return_type function_name(param_types);`

* A function with no parameters is declared `(void)` — writing `()` means "unspecified parameters".
* A function returning nothing uses `void`: `void printBanner(void) { ... }` (no `return` value needed).
* Prototypes let functions call each other in any order and are collected into header files (`.h`).

---

## 3. Parameters and Return Values

```c
int max(int a, int b) {           // Two input parameters
    return (a > b) ? a : b;       // One return value
}
```

Rules:

* The returned value's type must match (or be convertible to) the declared return type.
* A `void` function uses bare `return;` for early exit.
* Parameters are local variables initialized with copies of the arguments.

---

## 4. Call by Value and Pointers to Simulate References

Because arguments are copied, a function cannot modify the caller's variable through a plain parameter:

```c
void addTen(int x) {  x += 10;  }        // Does NOT change the caller's variable

void addTenByPointer(int *x) { *x += 10; } // DOES change it

int value = 5;
addTen(value);            // value is still 5
addTenByPointer(&value);  // value is now 15 — we passed its address
```

Passing an address lets the function reach the original storage. This is how `scanf("%d", &n)` works, and it is the standard idiom for "output parameters".

Arrays are different: an array argument automatically decays to a pointer to its first element, so array contents *can* be modified by the callee:

```c
void zeroAll(int arr[], int size) {   // arr is really int *
    for (int i = 0; i < size; i++) arr[i] = 0;
}
```

---

## 5. Variable Scope and Lifetime

| Category | Scope | Lifetime |
|----------|-------|----------|
| Local (automatic) | Inside the block where declared | Until the block ends |
| Global (file scope) | Rest of the file after declaration | Whole program |
| `static` local | Same as local | Whole program (keeps its value between calls) |
| Function parameter | Body of the function | Until the function returns |

```c
int counter(void) {
    static int calls = 0;    // Initialized once; persists across calls
    return ++calls;
}
```

Prefer locals and parameters over globals: global state makes programs hard to reason about and impossible to call safely from multiple places.

---

## 6. Recursion

A function may call itself, provided there is a **base case** that stops the recursion:

```c
unsigned long factorial(unsigned n) {
    if (n <= 1) return 1;              // Base case
    return n * factorial(n - 1);       // Recursive step (n shrinks each call)
}
```

Each call gets its own stack frame holding its parameters and locals. Deep recursion can exhaust the stack (stack overflow), so recursion suits problems whose depth is bounded (trees, divide-and-conquer) while simple counting is usually better done iteratively.

Classic recursive pair example:

```c
unsigned fib(unsigned n) {
    if (n < 2) return n;
    return fib(n - 1) + fib(n - 2);
}
```

---

## 7. Function Design Guidelines

* One function = one well-defined task; if the name contains "and", consider splitting it.
* Keep functions short enough to read on one screen.
* Pass small types by value; pass things to be modified (or large structs) via pointers.
* Validate assumptions at the start of the function (size > 0, pointer not NULL).
* Prefer returning values over writing through global variables.

---

## 8. Summary

* Prototypes make function use independent of definition order; headers share them across files.
* C is call-by-value; to modify caller data, pass pointers.
* Array parameters decay to pointers, letting callees modify array contents.
* `static` locals persist between calls; recursion requires a base case and consumes stack per call.
