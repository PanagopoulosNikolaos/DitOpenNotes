# C — Basics and Hardware Proximity

C is a statically typed, procedural programming language designed for systems programming and hardware-proximate development. It features a low-level memory mapping model, minimal runtime abstraction, and a direct mapping to machine instructions, which provides developers with precise control over system resources. This file covers program structure, primitive data types, storage classes, control flow constructs, and function execution.

---

## 1. The Procedural Paradigm

The procedural programming paradigm centers on the separation of data structures from the functions that manipulate them. Unlike object-oriented paradigms where state and behavior are encapsulated within classes, C represents data using primitive variables or aggregate structures (`struct`) and modifies that data using standalone procedures (functions).

```
[Data Structures] ────► [State Passed to Functions] ────► [Functions / Procedures]
```

C source code is compiled directly to machine code. There is no virtual machine, runtime interpreter, or garbage collector. Consequently, execution speed and memory footprints are minimized, making C the foundational language for operating system kernels and embedded firmware.

---

## 2. Primitive Types, Representation, and Sizes

C defines several basic types for representing integer and floating-point values. The exact size and memory representation of these types are implementation-defined (governed by the platform's Application Binary Interface, or ABI), but the C standard guarantees minimum width requirements.

### 2.1 Integer and Floating-Point Types

| Type | Minimum Size (Bits) | Typical Size (LP64 ABI) | Range (LP64 ABI) | Format Specifier |
| :--- | :--- | :--- | :--- | :--- |
| `char` | $8$ | $8$ bits ($1$ byte) | $-128$ to $127$ (or $0$ to $255$) | `%c` or `%d` |
| `short` | $16$ | $16$ bits ($2$ bytes) | $-32{,}768$ to $32{,}767$ | `%hd` |
| `int` | $16$ | $32$ bits ($4$ bytes) | $-2^{31}$ to $2^{31} - 1$ | `%d` or `%i` |
| `long` | $32$ | $64$ bits ($8$ bytes) | $-2^{63}$ to $2^{63} - 1$ | `%ld` |
| `long long` | $64$ | $64$ bits ($8$ bytes) | $-2^{63}$ to $2^{63} - 1$ | `%lld` |
| `float` | $32$ | $32$ bits ($4$ bytes) | IEEE-754 Single Precision | `%f` |
| `double` | $64$ | $64$ bits ($8$ bytes) | IEEE-754 Double Precision | `%lf` |

The `unsigned` modifier shifts the representation range by utilizing the sign bit as part of the value magnitude. For example, an `unsigned int` on a 32-bit width maps to a range of $0$ to $2^{32} - 1$.

### 2.2 Integer Overflow and Signedness

Signed integers use two's complement representation. Integer overflow on signed types is classified as **undefined behavior** by the C standard, permitting compilers to optimize away overflow checks. In contrast, unsigned integer overflow is defined to wrap around using modulo arithmetic:

$$
\text{val}_{\text{new}} = \text{val}_{\text{old}} \pmod{2^W}
$$

where $W$ represents the width of the unsigned type in bits.

---

## 3. Variables, Scope, and Storage Classes

A variable in C represents a named memory location. Variable behavior is determined by its scope (where the variable is visible) and its storage duration (how long the variable exists in memory).

### 3.1 Scope

- **Block Scope:** Variables declared inside a block (bounded by `{ }`) are visible only within that block.
- **File Scope:** Variables declared outside of any function are visible from their point of declaration to the end of the source file.

### 3.2 Storage Classes

C storage classes specify the storage duration and linkage of variables.

#### Syntax Reference

```text
<storage_class> <type> <variable_name> [= <initializer>];
```

#### Behavioral Description

1. `auto`: The default storage class for local variables. Memory is allocated on the stack frame when the block is entered and deallocated when the block is exited.
2. `register`: Advises the compiler to store the variable in a CPU register instead of RAM to accelerate access. You cannot take the address of a `register` variable using the `&` operator, even if the compiler decides to store it in memory.
3. `static`:
   - **Local static variables:** Retain their value between function calls. Memory is allocated in the data segment (initialized) or BSS segment (uninitialized) at program startup and persists for the duration of the program.
   - **Global static variables:** Restrict visibility to the file in which they are declared (internal linkage), preventing symbol collision during linking.
4. `extern`: Declares a variable that is defined in another translation unit. It tells the compiler that the actual storage allocation is handled elsewhere.

```c
#include <stdio.h>

static int file_var = 10; // Visible only to this file

void counter(void) {
    static int count = 0; // Initialized once; persists across calls
    count++;
    printf("Count: %d\n", count);
}
```

---

## 4. Control Flow Mechanisms

C provides structural control flow statements. Execution transfers are implemented using conditional branches and jumps at the machine level.

### 4.1 Conditionals: `if`/`else` and `switch`

#### Syntax Reference

```text
if (<expression>) {
    <statements>
} else if (<expression>) {
    <statements>
} else {
    <statements>
}
```

```text
switch (<integer_expression>) {
    case <constant_expression>:
        <statements>
        [break;]
    default:
        <statements>
}
```

#### Behavioral Description

- **`if`/`else`:** The conditional expression is evaluated. Any non-zero value represents truth; zero represents falsehood.
- **`switch`:** Computes the value of `<integer_expression>` and jumps to the matching `case` label. If no `break` is present, execution "falls through" to subsequent cases. This is a common source of bugs but can be used intentionally for duff's devices or shared logic blocks.

---

### 4.2 Loops: `while`, `do-while`, and `for`

#### Syntax Reference

```text
while (<condition>) {
    <body>
}
```

```text
do {
    <body>
} while (<condition>);
```

```text
for ([<initialization>]; [<condition>]; [<loop_expression>]) {
    <body>
}
```

#### Behavioral Description

- **`while`:** Checks the condition before executing the body.
- **`do-while`:** Executes the body once before checking the condition, ensuring at least one iteration.
- **`for`:** Executes `<initialization>` once. Then, while `<condition>` is true, executes `<body>`, and evaluates `<loop_expression>` after each iteration.

---

### 4.3 Jump Statements: `goto`

The `goto` statement jumps execution to a labeled statement within the same function.

#### Syntax Reference

```text
goto <label_name>;
...
<label_name>:
    <statement>
```

> **[Key Insight]** `goto` should be used sparingly. Its primary legitimate use in systems programming is for cleanup blocks at the end of functions to release resources in reverse order of allocation, preventing deeply nested structures.

---

## 5. Functions and Parameter Passing

A function in C is a self-contained block of code that performs a specific task. C functions must be declared before they are called.

### 5.1 Declarations vs. Definitions

- **Declaration (Prototype):** Specifies the function name, return type, and parameters. This informs the compiler of the function signature.
- **Definition:** Contains the actual implementation block.

#### Syntax Reference

```text
/* Function Prototype / Declaration */
<return_type> <function_name>(<parameter_list>);

/* Function Definition */
<return_type> <function_name>(<parameter_list>) {
    <body>
    [return <value>];
}
```

---

### 5.2 Parameter Passing Mechanisms

C supports only **pass-by-value**. When a variable is passed to a function, the compiler creates a copy of the argument value and places it on the function's stack frame. Modifications to the parameter inside the function do not affect the original variable.

To simulate **pass-by-reference**, a pointer referencing the original variable's memory address is passed by value. The function dereferences the pointer to read or modify the value stored at that address.

```c
#include <stdio.h>

/* Pass-by-value: modifies only the copy on the stack frame */
void modifyVal(int x) {
    x = 42;
}

/* Simulating pass-by-reference: modifies memory location directly */
void modifyRef(int *x) {
    *x = 42;
}
```

---

## Solved Exercises

### Exercise 1: Storage Class Lifetime and State

**Problem:** Determine the exact terminal output of the following program.

```c
#include <stdio.h>

void increment(void) {
    auto int local_var = 10;
    static int static_var = 10;
    
    local_var++;
    static_var++;
    printf("local=%d static=%d\n", local_var, static_var);
}

int main(void) {
    increment();
    increment();
    increment();
    return 0;
}
```

**Solution:**
1. **First invocation of `increment()`:**
   - `local_var` is initialized to $10$ on the stack frame. It increments to $11$.
   - `static_var` is initialized to $10$ in the data segment. It increments to $11$.
   - Prints: `local=11 static=11`
2. **Second invocation of `increment()`:**
   - `local_var` is re-initialized to $10$ on the stack frame. It increments to $11$.
   - `static_var` retains its state ($11$) from the previous execution. It increments to $12$.
   - Prints: `local=11 static=12`
3. **Third invocation of `increment()`:**
   - `local_var` is re-initialized to $10$ on the stack frame. It increments to $11$.
   - `static_var` retains its state ($12$). It increments to $13$.
   - Prints: `local=11 static=13`

```text
local=11 static=11
local=11 static=12
local=11 static=13
```

---

### Exercise 2: Simulating Pass-by-Reference

**Problem:** Implement a swap function `void swap(int *a, int *b)` that exchanges the integer values of two variables in-place. Provide a `main` function showing before and after states.

**Solution:**
1. The swap function must receive the memory addresses of the two variables.
2. It uses a temporary local variable to hold the value of the first pointer location, copies the value of the second pointer location to the first, and writes the temporary value to the second.

```c
#include <stdio.h>

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main(void) {
    int x = 5;
    int y = 10;
    
    printf("Before: x=%d y=%d\n", x, y);
    swap(&x, &y);
    printf("After: x=%d y=%d\n", x, y);
    
    return 0;
}
```

```text
Before: x=5 y=10
After: x=10 y=5
```

---

### Exercise 3: Signed vs. Unsigned Conversions

**Problem:** Explain what the following code prints and explain why using signed/unsigned comparisons.

```c
#include <stdio.h>

int main(void) {
    int a = -5;
    unsigned int b = 3;
    
    if (a < b) {
        printf("a is less than b\n");
    } else {
        printf("a is greater than or equal to b\n");
    }
    return 0;
}
```

**Solution:**
1. C performs **usual arithmetic conversions** when evaluating binary operators on differing types.
2. When comparing a signed `int` and an `unsigned int` of the same width, the signed value (`a = -5`) is implicitly converted to an `unsigned int`.
3. In two's complement representation, $-5$ is represented as `0xFFFFFFFB` on 32-bit platforms. Converted to unsigned, this value is $4{,}294{,}967{,}291$.
4. Since $4{,}294{,}967{,}291 > 3$, the expression `a < b` evaluates to false ($0$).

```text
a is greater than or equal to b
```

---

### Exercise 4: Switch-Case Fall-Through

**Problem:** Predict the output of the following code snippet.

```c
#include <stdio.h>

int main(void) {
    int val = 2;
    switch (val) {
        case 1:
            printf("One ");
        case 2:
            printf("Two ");
        case 3:
            printf("Three ");
            break;
        default:
            printf("Default ");
    }
    printf("\n");
    return 0;
}
```

**Solution:**
1. `val` evaluates to $2$. The execution jump goes to the label `case 2:`.
2. Prints `"Two "`.
3. Because there is no `break` at the end of the `case 2` statements, execution falls through to `case 3:`.
4. Prints `"Three "`.
5. The `break` statement at the end of `case 3` halts execution and exits the switch block.

```text
Two Three 
```

---

### Exercise 5: Modulo and Integer Division with Negatives

**Problem:** Calculate the mathematical result of $(-17) / 5$ and $(-17) \% 5$ in C99.

**Solution:**
1. In C99 and later, integer division truncates toward zero (algebraic truncation).
2. For $-17 / 5$:
   $$
   -17 / 5 = -3.4 \xrightarrow{\text{truncate}} -3
   $$
3. The modulo operator must satisfy the identity:
   $$
   (a / b) \times b + a \% b = a
   $$
4. Substituting the values:
   $$
   (-3) \times 5 + (-17) \% 5 = -17 \implies -15 + (-17) \% 5 = -17 \implies (-17) \% 5 = -2
   $$

```c
#include <stdio.h>

int main(void) {
    printf("div=%d mod=%d\n", -17 / 5, -17 % 5);
    return 0;
}
```

```text
div=-3 mod=-2
```

---

### Exercise 6: Duff's Device Concept for Loop Unrolling

**Problem:** Write a loop structure that uses a `switch` and `do-while` block to unroll a loop copying elements in groups of $4$. This is a simplified concept of Duff's device.

**Solution:**
1. Loop unrolling reduces overhead by executing multiple operations per loop index test.
2. Duff's device combines a `switch` fall-through and a `do-while` loop to handle arbitrary count sizes that are not multiples of the unrolling factor.

```c
#include <stdio.h>

void copy(int *to, int *from, int count) {
    int n = (count + 3) / 4;
    switch (count % 4) {
        case 0: do { *to++ = *from++;
        case 3:      *to++ = *from++;
        case 2:      *to++ = *from++;
        case 1:      *to++ = *from++;
                } while (--n > 0);
    }
}

int main(void) {
    int src[6] = {10, 20, 30, 40, 50, 60};
    int dest[6] = {0};
    copy(dest, src, 6);
    for (int i = 0; i < 6; i++) {
        printf("%d ", dest[i]);
    }
    printf("\n");
    return 0;
}
```

```text
10 20 30 40 50 60 
```

---

### Exercise 7: Global Static Linkage

**Problem:** Explain what happens when a variable is declared `static` at file scope and another file attempts to access it using `extern`.

**Solution:**
1. A global variable marked `static` has internal linkage. Its symbol is not exported to the global symbol table by the assembler.
2. File A: `static int secret = 42;`
3. File B: `extern int secret;`
4. During the linking phase, the linker tries to resolve `secret` in File B. Because File A's `secret` is not in the global symbol table, a linker error occurs: `undefined reference to 'secret'`.

```text
linker error: undefined reference to 'secret'
```

---

### Exercise 8: Recursive Stack Behavior

**Problem:** Write a recursive implementation of the Fibonacci sequence and explain how local variables behave on the call stack for an input $n = 3$.

**Solution:**

```c
#include <stdio.h>

int fib(int n) {
    if (n <= 1) return n;
    return fib(n - 1) + fib(n - 2);
}

int main(void) {
    printf("fib(3)=%d\n", fib(3));
    return 0;
}
```

```text
fib(3)=2
```

1. **Call Stack tracing:**
   - `fib(3)` is pushed onto the stack. Space is allocated for parameter `n = 3`.
   - `fib(3)` evaluates `n <= 1` (false), then invokes `fib(2)`.
   - `fib(2)` is pushed onto the stack. Space is allocated for `n = 2`.
   - `fib(2)` invokes `fib(1)`.
   - `fib(1)` is pushed. `n = 1` is true; returns $1$ and is popped from stack.
   - `fib(2)` resumes and calls `fib(0)`.
   - `fib(0)` is pushed. `n = 0` is true; returns $0$ and is popped from stack.
   - `fib(2)` sums $1 + 0 = 1$, returns $1$ and is popped from stack.
   - `fib(3)` resumes, holds $1$ from `fib(2)` branch, and calls `fib(1)`.
   - `fib(1)` is pushed, returns $1$ and is popped.
   - `fib(3)` sums $1 + 1 = 2$, returns $2$ to `main`.

---

## Common Errors and Gotchas

### 1. Missing Switch Break (Fall-Through Bug)
* **Cause:** Omitting `break` at the end of a `case` block causes the compiler to continue executing subsequent statements in the next `case` block.
* **Resolution:** Ensure every case ends with a `break;` statement unless fall-through behavior is explicitly desired and documented.

### 2. Confusing Assignment (`=`) with Equality (`==`)
* **Cause:** Using `if (x = 5)` instead of `if (x == 5)`. The single `=` assigns $5$ to `x`. The overall expression evaluates to the assigned value ($5$, which is non-zero, making the condition evaluate to true).
* **Resolution:** Enable compiler warnings (`-Wparentheses` or `-Wall`). Alternatively, write comparisons with literals on the left-hand side (e.g., `if (5 == x)`), which triggers a compilation error if an assignment is written accidentally.

### 3. Accessing Uninitialized Stack Variables
* **Cause:** Automatic storage class variables (`auto`) have indeterminate contents upon allocation. Reading them before writing a value yields garbage data, which represents undefined behavior.
* **Resolution:** Always initialize variables upon declaration: `int value = 0;`.

---

## Exam Tip: Simulating Reference Semantics and Orthogonality

**Simulating Reference Semantics:**
Because C only supports pass-by-value, you cannot pass a variable directly to modify its state. You must pass its address.
- **Common exam mistake:** Writing a swap function without pointers or passing arguments without the address-of (`&`) operator.
  ```c
  void bad_swap(int a, int b) { int temp = a; a = b; b = temp; }
  // Calling bad_swap(x, y) has no effect on x and y.
  ```

**Language Orthogonality Trap:**
Orthogonality refers to the ability to combine a small set of primitive constructs in any combination. C exhibits poor orthogonality in several areas:
1. **Returning Structures vs. Arrays:**
   - A function can return a `struct` by value (it copies the entire struct).
   - A function **cannot** return an array by value (it decays to a pointer, or you must wrap it in a struct).
2. **Operations on Structures vs. Arrays:**
   - You can assign one `struct` to another of the same type: `structA = structB;`.
   - You **cannot** assign one array directly to another: `arrayA = arrayB;` is a compilation error.
