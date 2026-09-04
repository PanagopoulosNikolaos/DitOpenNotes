# Study Notes: Pointers, Addressing, and Memory Models in C

## 1. Physical Architecture and Virtual Addressing
Modern computer architectures abstract physical RAM via virtual address spaces managed by the Memory Management Unit (MMU). In a 64-bit user-space process on Linux:
* Addresses range from `0x000000000000` to `0x7FFFFFFFFFFF`.
* A pointer is an unsigned 64-bit integer holding one of these byte addresses.
* Dereferencing initiates a CPU memory read or write at that exact address location.

---

## 2. Pointer Decay and Array Equivalence
When an array expression appears in code, in almost all contexts it decays implicitly into a pointer to its first element:
```c
int arr[5] = {10, 20, 30, 40, 50};
int *p = arr; // Equivalent to int *p = &arr[0];
```

The bracket operator is formal syntactic sugar defined in the ISO C standard as:
$$\text{arr}[i] \equiv *(\text{arr} + i)$$

Because addition is commutative:
$$\text{arr}[i] \equiv *(i + \text{arr}) \equiv i[\text{arr}]$$

---

## 3. Pointer Arithmetic and Scaling
Pointer arithmetic always steps forward or backward by multiples of the size of the underlying type:
$$\text{Address}(p + k) = \text{Address}(p) + k \times \text{sizeof}(*p)$$

Example:
```c
double values[3];
double *ptr = values; // Suppose ptr is at address 0x1000

// ptr + 1 evaluates to address: 0x1000 + 1 * sizeof(double) = 0x1008
```

---

## 4. Constant Pointers vs. Pointers to Constants
Reading type qualifiers from right to left clarifies pointer mutability:
1. `const int *ptr`: Pointer to a constant integer. The integer value cannot be changed through `*ptr`, but `ptr` can be redirected to point to another address.
2. `int * const ptr`: Constant pointer to an integer. The pointer cannot be redirected to another address, but the value at `*ptr` can be mutated.
3. `const int * const ptr`: Constant pointer to a constant integer. Neither the address nor the target value can be modified.

---

## 5. Function Pointers and Dispatch Tables
C supports referencing executable machine instructions via function pointers:
```c
int (*operation)(int, int);

int add(int a, int b) { return a + b; }
int multiply(int a, int b) { return a * b; }

operation = add;
int sum = operation(3, 4); // 7

operation = multiply;
int prod = operation(3, 4); // 12
```
Function pointers enable callback architectures, event handlers, and comparator functions (such as the standard `qsort` library routine).

