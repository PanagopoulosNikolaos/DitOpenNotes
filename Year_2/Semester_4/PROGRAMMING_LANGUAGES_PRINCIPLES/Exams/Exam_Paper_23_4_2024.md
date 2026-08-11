# PRINCIPLES OF PROGRAMMING LANGUAGES
## MIDTERM EXAM 23/4/2024
**Department of Computer Science and Telecommunications**  
**University of Ioannina**

---

### Topic 1 - A [1]

**A.** Show that the following grammar is ambiguous:
```
<S> -> <A>
<A> -> <A> + <A> | <id>
<id> -> a | b | c
```

***

**Solution:**

A grammar is defined as ambiguous if there exists at least one string in its language that can be derived by more than one leftmost (or rightmost) derivation, or equivalently, if it has more than one parse tree.

Consider the string `a + b + c`.

**1st leftmost derivation (corresponds to left-associative grouping `(a + b) + c`):**
1. `<S>` => `<A>` (via `<S> -> <A>`)
2. `<A>` => `<A> + <A>` (via `<A> -> <A> + <A>`)
3. `<A>` => `<A> + <A> + <A>` (replacing the first `<A>` with `<A> + <A>`)
4. `<A>` => `<id> + <A> + <A>` => `a + <A> + <A>`
5. `<A>` => `a + <id> + <A>` => `a + b + <A>`
6. `<A>` => `a + b + <id>` => `a + b + c`

Parse tree 1:
```
      <S>
       |
      <A>
    /  |  \
  <A>  +  <A>
  /|\      |
<A>+<A>  <id>
 |   |     |
<id><id>   c
 |   |
 a   b
```

**2nd leftmost derivation (corresponds to right-associative grouping `a + (b + c)`):**
1. `<S>` => `<A>`
2. `<A>` => `<A> + <A>`
3. `<A>` => `<id> + <A>` => `a + <A>`
4. `<A>` => `a + <A> + <A>` (replacing the second `<A>` with `<A> + <A>`)
5. `<A>` => `a + <id> + <A>` => `a + b + <A>`
6. `<A>` => `a + b + <id>` => `a + b + c`

Parse tree 2:
```
      <S>
       |
      <A>
    /  |  \
  <A>  +  <A>
   |     /|\
 <id>  <A>+<A>
   |    |   |
   a  <id> <id>
        |   |
        b   c
```

Because the string `a + b + c` is generated from two different parse trees, the grammar is ambiguous.

***

### Topic 1 - B [1]

**B.** Consider the following code in a hypothetical programming language:
```javascript
function outer() {
    function inner1() {
        var x = 5;
        inner2();
    }
    function inner2() {
        var y = x;
        print(y);
    }
    var x = 16;
    inner1();
}
outer()
```
What will be displayed when executed if the programming language has a) static scoping, b) dynamic scoping?

***

**Solution:**

* **a) Static scoping (Static scoping / Lexical scoping):**
  In static scoping, name resolution (name binding) is determined at compile/parse time based on the spatial layout of the source code (nesting). The scope of a function is the environment in which it was defined.
  The function `inner2` is defined inside the function `outer`. Therefore, the lexical parent of `inner2` is `outer`.
  When the statement `var y = x;` is executed inside `inner2`, the variable `x` is searched for. Since it does not exist locally in `inner2`, the search goes to its lexical parent, which is `outer`. There, `x` has the value `16`. The local declaration `var x = 5` in `inner1` does not affect `inner2` because `inner2` is not nested inside `inner1`.
  Therefore, it will display: **`16`**.

* **b) Dynamic scoping:**
  In dynamic scoping, name resolution is determined at runtime based on the call stack of the subroutines.
  The execution flow is: `outer()` -> calls `inner1()` -> calls `inner2()`.
  When `inner2` searches for the variable `x`, since it does not exist locally, it searches in the function that called it, namely `inner1`. In `inner1`, the variable `x` has the value `5`.
  Therefore, it will display: **`5`**.

---

### Topic 2 - A [1]

Given the following C code that contains 6 points to be completed:
```c
#include <stdio.h>
#include <stdlib.h>

struct my_struct {
    int x;
    int y;
};

<[1] complete the return type of the function> fun1(int a) {
    <[2] complete the body of the function>
}

<[3] complete the return type of the function> fun2(int a) {
    <[4] complete the body of the function>
}

int main(void) {
    int a = 100;
    <[5] complete the call to function fun1>
    printf("%d %d \n", r.x, r.y);

    <[6] complete the call to function fun2>
    printf("%d %d \n", r2[0], r2[1]);
    free(r2);
}
```
When executed, the code should display:
```
101 101
101 101
```

**A.** Complete points [1] and [2] for the `fun1` function so that it returns a record of the `my_struct` structure where each field takes the value of the argument of the `fun1` function. Complete point [5] with the call to the `fun1` function.

***

**Solution:**

Completing points [1], [2] and [5]:
- At point **[1]**, the return type of the function is `struct my_struct`.
- At point **[2]**, we locally create a variable of type `struct my_struct`, assign the value `a` to its fields and return it.
- At point **[5]**, we call the function `fun1(a + 1)` and assign the result to the variable `struct my_struct r` (so that it prints `101 101`).

The code for the `fun1` function and its call:

```c
/**
 * Creates and returns a structure with fields initialized to a.
 * Args:
 *   a (int): The value to be assigned to both fields of the struct.
 * Returns:
 *   struct my_struct: The initialized struct object.
 */
struct my_struct fun1(int a) {
    struct my_struct temp_struct;
    temp_struct.x = a;
    temp_struct.y = a;
    return temp_struct;
}

// Point [5] in main:
struct my_struct r = fun1(a + 1);
```

---

### Topic 2 - B [1]

Given the following C code that contains 6 points to be completed:
```c
#include <stdio.h>
#include <stdlib.h>

struct my_struct {
    int x;
    int y;
};

<[1] complete the return type of the function> fun1(int a) {
    <[2] complete the body of the function>
}

<[3] complete the return type of the function> fun2(int a) {
    <[4] complete the body of the function>
}

int main(void) {
    int a = 100;
    <[5] complete the call to function fun1>
    printf("%d %d \n", r.x, r.y);

    <[6] complete the call to function fun2>
    printf("%d %d \n", r2[0], r2[1]);
    free(r2);
}
```
When executed, the code should display:
```
101 101
101 101
```

**B.** Complete points [3] and [4] for the `fun2` function so that it returns a two-position array with each position's value being the value of the argument of `fun2`. Complete point [6] with the call to the `fun2` function.

***

**Solution:**

Completing points [3], [4] and [6]:
- At point **[3]**, the return type of the function is `int*` (pointer to integer), because in C direct return of arrays by value is not allowed.
- At point **[4]**, we dynamically allocate memory for a 2-position integer array using `malloc()`, assign the value `a` to the array positions and return the pointer.
- At point **[6]**, we call the function `fun2(a + 1)` and assign the result to the variable `int *r2` (so that it prints `101 101`).

The code for the `fun2` function and its call:

```c
/**
 * Allocates an array of two integers initialized to the value a.
 * Args:
 *   a (int): The value to initialize the array elements with.
 * Returns:
 *   int*: A pointer to the dynamically allocated integer array.
 */
int* fun2(int a) {
    int *arr_ptr = (int *)malloc(2 * sizeof(int));
    if (arr_ptr != NULL) {
        arr_ptr[0] = a;
        arr_ptr[1] = a;
    }
    return arr_ptr;
}

// Point [6] in main:
int *r2 = fun2(a + 1);
```

---

### Topic 2 - C [1]

Given the following C code that contains 6 points to be completed:
```c
#include <stdio.h>
#include <stdlib.h>

struct my_struct {
    int x;
    int y;
};

<[1] complete the return type of the function> fun1(int a) {
    <[2] complete the body of the function>
}

<[3] complete the return type of the function> fun2(int a) {
    <[4] complete the body of the function>
}

int main(void) {
    int a = 100;
    <[5] complete the call to function fun1>
    printf("%d %d \n", r.x, r.y);

    <[6] complete the call to function fun2>
    printf("%d %d \n", r2[0], r2[1]);
    free(r2);
}
```

**C.** Comment on how the above code relates to the concept of orthogonality in programming languages and what holds regarding orthogonality in the C programming language.

***

**Solution:**

**Orthogonality:**
Orthogonality in a programming language means that a relatively small set of fundamental constructs can be combined in free and predictable ways, without context-dependent restrictions.

**Relation to the code and C:**
In the above code we observe a significant violation of orthogonality in the C language regarding data types and functions:
1. **Different treatment of structs and arrays:** C allows a function to return a struct directly by value (as in `fun1`), but does **not** allow the direct return of an array by value. To return an array, we are forced to use pointers and dynamic memory allocation (as in `fun2`).
2. **Argument passing:** Structs can be passed to functions either by value or by reference/pointer. In contrast, arrays are always passed as a pointer to their first element (array-to-pointer decay).

These inconsistencies (where structs and arrays, although composite data types, are treated completely differently) constitute a classic example of non-orthogonal design in the C language.

---

### Topic 3 - A [2]

**A.** Create a Python class `Box` with data members the width (`width`), length (`length`) and height (`height`) of a box. Implement the constructor method `__init__` and the `__str__` method that will display information about each `Box` object. Add a method named `volume` that returns the volume of the box. Create a `Box` object with width 10cm, length 15cm and height 8cm and display it.

***

**Solution:**

The code of the `Box` class in Python is given below, following the naming conventions (PascalCase for the class, camelCase for the methods, snake_case for the variables) and Google Style documentation:

```python
class Box:
    """Represents a box with width, length, and height dimensions.

    This class provides initialization, string representation, and a method
    to calculate the volume of the box.
    """

    def __init__(self, width: float, length: float, height: float):
        """Initializes the dimensions of the box.

        Args:
            width (float): The width of the box in centimeters.
            length (float): The length of the box in centimeters.
            height (float): The height of the box in centimeters.
        """
        self.width = width
        self.length = length
        self.height = height

    def __str__(self) -> str:
        """Returns a string representation of the box object.

        Returns:
            str: The box description with its dimensions.
        """
        return f"Box(width={self.width}cm, length={self.length}cm, height={self.height}cm)"

    def volume(self) -> float:
        """Calculates the volume of the box.

        Returns:
            float: The volume of the box.
        """
        return self.width * self.length * self.height


# Create a Box object with dimensions 10x15x8
box_object = Box(10.0, 15.0, 8.0)

# Display the object
print(box_object)

# Display the volume
print(f"Volume: {box_object.volume()} cm^3")
```

---

### Topic 3 - B [1]

**B.** Write in Python a function named `all_digits` that accepts a string as an argument and checks whether it contains all ten digits (0 through 9). For example, for the string `"7a102ab134563v789zi360"` it should return `True`. Suppose this function has been placed in a file `utils.py`. Write the contents of the file `erotima.py` that calls the `all_digits` function for one string and returns `True` and for another string returns `False`.

Note: the method `isdigit()` returns `True` if the calling object consists of characters that are all digits, so `"5".isdigit()` returns `True`, while `"a".isdigit()` returns `False`.

***

**Solution:**

The contents of the two files are given below. To comply with the naming conventions (Functions: `camelCase`), the function is defined as `allDigits` and an alias named `all_digits` is provided.

**Contents of file `utils.py`:**

```python
def allDigits(input_string: str) -> bool:
    """Checks if the input string contains all decimal digits from 0 to 9.

    Args:
        input_string (str): The string to check.

    Returns:
        bool: True if the string contains all ten digits, False otherwise.
    """
    found_digits = set(char for char in input_string if char.isdigit())
    return len(found_digits) == 10

# Alias for compatibility with the expected exam function name
all_digits = allDigits
```

**Contents of file `erotima.py`:**

```python
from utils import allDigits

def runTestCases():
    """Runs test cases on the allDigits function and prints the result.

    Returns:
        None
    """
    # String that contains all digits (0 to 9)
    test_str1 = "7a102ab134563v789zi360"
    
    # String that does not contain all digits
    test_str2 = "12345abcde"
    
    result1 = allDigits(test_str1) # Evaluates to True
    result2 = allDigits(test_str2) # Evaluates to False
    
    print(f"Test 1 result: {result1}")
    print(f"Test 2 result: {result2}")

if __name__ == "__main__":
    runTestCases()
```

---

### Topic 4 [2]

What will the following C++ code display when executed? What is the significance of defining the `fun` function of class `A` as `virtual`?
```cpp
#include <iostream>
using namespace std;
class A {
public:
    virtual void fun() { cout << "A" << endl; }
};
class B : public A {
public:
    void fun() { cout << "B" << endl; }
};
int main() {
    A *ref = new A();
    ref->fun();
    delete ref;
    ref = new B();
    ref->fun();
    delete ref;
    A obj = A();
    obj.fun();
    obj = B();
    obj.fun();
}
```

***

**Solution:**

**Program output:**
When the code is executed, it will display:
```
A
B
A
A
```

**Explanation:**
1. `A *ref = new A(); ref->fun();`
   The pointer `ref` is of type `A*` and points to an object of class `A`. `A::fun()` is called. **`A`** is printed.
2. `ref = new B(); ref->fun();`
   The pointer `ref` of type `A*` now points to an object of the derived class `B`. Because `fun()` is declared `virtual` in the base class `A`, **dynamic binding (late binding)** is used. At runtime the method of the derived class is called, namely `B::fun()`. **`B`** is printed.
3. `A obj = A(); obj.fun();`
   The object `obj` is of type `A`. `A::fun()` is called directly. **`A`** is printed.
4. `obj = B(); obj.fun();`
   Here we have an assignment of an object of type `B` to a variable of type `A`. In C++ this causes **object slicing**: the part of the `B` object belonging to the derived class is cut off/discarded and only the base part (of type `A`) is copied. The `obj` remains a normal object of type `A` (not a pointer or reference), therefore dynamic binding does not apply and `A::fun()` is called statically. **`A`** is printed.

**Significance of the `virtual` keyword:**
The `virtual` keyword enables **dynamic binding (late binding)** of methods. This means that the decision about which function will be executed is taken at runtime based on the actual type of the object the pointer or reference points to, and not based on the type of the pointer itself at compile-time. This constitutes the foundation for supporting **polymorphism** in C++.
