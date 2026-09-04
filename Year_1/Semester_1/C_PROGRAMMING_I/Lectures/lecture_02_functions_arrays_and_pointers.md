# Lecture 02: Functions, Arrays, and Pointer Mechanics

## Context and Grounding
This lecture note explores procedural modularity and contiguous memory architecture. It analyzes function call conventions, call stack activation frames, linear and multi-dimensional array layouts, null-terminated string buffers, pointer arithmetic, and pass-by-reference semantics via memory addresses.

---

## 1. Modular Functions and Execution Frames

Functions in C enforce code reuse, abstraction, and scope isolation.

### 1.1 Prototypes and Definitions
A function prototype alerts the compiler to the return type and parameter types prior to invocation:

```c
/**
 * Calculates the square of a numeric floating point value.
 *
 * Args:
 *   val (double): The base numeric operand.
 *
 * Returns:
 *   double: The computed squared value.
 */
double computeSquare(double val);
```

### 1.2 Call Stack and Parameter Passing
* C strictly employs **pass-by-value** semantics. Arguments evaluated at the call site are copied into the callee function's activation frame on the stack.
* Modifying a parameter within a callee does not alter the caller's variable unless the parameter is a pointer containing the address of that variable.

---

## 2. Arrays and Memory Layout

An array in C represents a contiguous, fixed-size allocation of homogeneous elements in virtual memory.

### 2.1 One-Dimensional Arrays
```c
int numbers[5] = {10, 20, 30, 40, 50};
```
* The array identifier `numbers` decays into a pointer to its zeroth element (`&numbers[0]`) when passed to expressions or functions.
* Array indexing satisfies:
  $$\text{Address}(\text{arr}[i]) = \text{BaseAddress}(\text{arr}) + i \times \text{sizeof}(\text{type})$$

### 2.2 Multi-Dimensional Arrays
C lays out multi-dimensional arrays in **row-major order**:
```c
int matrix[2][3] = {
    {1, 2, 3},
    {4, 5, 6}
};
// Element matrix[i][j] is located at: BaseAddress + (i * 3 + j) * sizeof(int)
```

---

## 3. Strings and Character Manipulation

In C, a string is a sequence of characters terminated by a null byte (`'\0'`, ASCII 0).

```c
char message[] = "Informatics"; // Allocates 12 bytes (11 characters + '\0')
```

### 3.1 Standard Library Utilities (`<string.h>`)
| Function | Signature | Operational Behavior |
|:---|:---|:---|
| `strlen` | `size_t strlen(const char *s)` | Computes count of characters preceding the null terminator. |
| `strcpy` | `char* strcpy(char *dest, const char *src)` | Copies string from source into destination buffer. |
| `strncpy` | `char* strncpy(char *dest, const char *src, size_t n)` | Safe copy bounded by maximum byte count $n$. |
| `strcmp` | `int strcmp(const char *s1, const char *s2)` | Lexicographical byte comparison ($<0, 0, >0$). |
| `strcat` | `char* strcat(char *dest, const char *src)` | Appends source string onto the end of destination buffer. |

---

## 4. Pointer Mechanics

A pointer is a typed variable whose value represents an address in memory.

### 4.1 Address and Dereference Operators
```c
int count = 100;
int *p_count = &count; // p_count stores the memory address of count

printf("Direct value: %d\n", count);        // 100
printf("Indirect value: %d\n", *p_count);    // Dereferencing yields 100
printf("Memory address: %p\n", (void *)p_count);
```

### 4.2 Pointer Arithmetic
Adding integer $k$ to a pointer increments the stored address by $k \times \text{sizeof}(*ptr)$:
```c
int values[3] = {10, 20, 30};
int *ptr = values;

printf("First: %d\n", *ptr);         // 10
printf("Second: %d\n", *(ptr + 1));  // 20
```

### 4.3 Passing Pointers for In-Place Mutation
```c
/**
 * Exchanges the contents of two integer variables in place.
 *
 * Args:
 *   first_ptr (int *): Pointer to first integer operand.
 *   second_ptr (int *): Pointer to second integer operand.
 *
 * Returns:
 *   void.
 */
void swapValues(int *first_ptr, int *second_ptr) {
    if (first_ptr == NULL || second_ptr == NULL) {
        return;
    }
    int temp = *first_ptr;
    *first_ptr = *second_ptr;
    *second_ptr = temp;
}
```

---

## 5. Summary & Safety Directives
* Always verify that pointers are non-null before performing dereferencing operations.
* Never return a pointer to a local stack-allocated variable from a function; stack frames are invalidated upon function return.
* Bound string copying operations using `strncpy` or explicit capacity counters to avoid buffer overflow vulnerabilities.

