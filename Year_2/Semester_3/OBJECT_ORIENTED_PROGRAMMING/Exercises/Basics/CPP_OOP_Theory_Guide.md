# Comprehensive C++ Guide: From Basics to Advanced OOP

This guide covers C++ programming from fundamental concepts to advanced Object-Oriented Programming principles. Each section builds upon the previous one, providing a complete learning path for beginners to advance to professional-level C++ programming.

## Table of Contents
1. [Basic Printing (Output/Input)](#basic-printing-outputinput)
2. [Variables and Data Types](#variables-and-data-types)
3. [Control Flow (If/Else, Switch)](#control-flow-ifelse-switch)
4. [Loops (For, While)](#loops-for-while)
5. [Tables (Arrays)](#tables-arrays)
6. [Functions (Pass-by-value vs. Pass-by-reference)](#functions-pass-by-value-vs-pass-by-reference)
7. [Pointers and References](#pointers-and-references)
8. [Vectors (Dynamic Arrays)](#vectors-dynamic-arrays)
9. [Maps (Associative Containers)](#maps-associative-containers)
10. [Classes and Objects (The Basics)](#classes-and-objects-the-basics)
11. [Constructors and Destructors](#constructors-and-destructors)
12. [The `this` Pointer](#the-this-pointer)
13. [Object-Oriented Programming Principles (Encapsulation, Abstraction)](#object-oriented-programming-principles-encapsulation-abstraction)
14. [Inheritance and Polymorphism](#inheritance-and-polymorphism)
15. [Advanced Memory Management (Heap vs. Stack, Smart Pointers)](#advanced-memory-management-heap-vs-stack-smart-pointers)

---

## Basic Printing (Output/Input)

### Hello World Program
```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Hello, World!" << endl;
    return 0;
}
```

### Explanation:
- `#include <iostream>`: Includes input/output stream library
- `cout`: Console output stream object
- `<<`: Stream insertion operator
- `endl`: Inserts newline and flushes the buffer

### Multiple Print Statements
```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "First line" << endl;
    cout << "Second line" << endl;
    cout << "Number: " << 42 << endl;
    cout << "Decimal: " << 3.14 << endl;
    return 0;
}
```

### Input from User
```cpp
#include <iostream>
using namespace std;

int main() {
    int number;
    string name;
    
    cout << "Enter your name: ";
    cin >> name;
    cout << "Hello, " << name << "!" << endl;
    
    cout << "Enter a number: ";
    cin >> number;
    cout << "You entered: " << number << endl;
    
    return 0;
}
```

### Using printf (C-style)
```cpp
#include <cstdio>

int main() {
    printf("Hello, World!\n");
    printf("Number: %d\n", 42);
    printf("Float: %.2f\n", 3.14159);
    return 0;
}
```

---

## Variables and Data Types

### Fundamental Data Types
```cpp
#include <iostream>
using namespace std;

int main() {
    // Integer types
    int integer_var = 42;           // Regular integer
    short short_var = 100;          // Short integer
    long long_var = 100000L;        // Long integer
    long long very_long = 1000000LL; // Very long integer
    
    // Floating-point types
    float float_var = 3.14f;        // Single precision
    double double_var = 3.14159;    // Double precision
    long double long_double = 3.141592653589L; // Extended precision
    
    // Character types
    char char_var = 'A';            // Single character
    wchar_t wide_char = L'B';       // Wide character
    char16_t utf16_char = u'C';     // UTF-16 character
    char32_t utf32_char = U'D';     // UTF-32 character
    
    // Boolean type
    bool bool_var = true;           // Boolean (true/false)
    
    // Constants
    const int constant = 100;       // Constant value
    
    // Output all variables
    cout << "Integer: " << integer_var << endl;
    cout << "Short: " << short_var << endl;
    cout << "Long: " << long_var << endl;
    cout << "Very Long: " << very_long << endl;
    cout << "Float: " << float_var << endl;
    cout << "Double: " << double_var << endl;
    cout << "Long Double: " << long_double << endl;
    cout << "Char: " << char_var << endl;
    cout << "Bool: " << bool_var << endl;
    
    return 0;
}
```

### Variable Declaration and Initialization
```cpp
#include <iostream>
using namespace std;

int main() {
    // Different ways to initialize variables
    int a = 5;              // Copy initialization
    int b{10};              // Direct initialization (C++11)
    int c{};                // Value initialization (default value)
    
    // Type inference
    auto x = 42;            // x is deduced as int
    auto y = 3.14;          // y is deduced as double
    auto z = 'A';           // z is deduced as char
    
    // Multiple declarations
    int width = 10, height = 20, area = width * height;
    
    cout << "Width: " << width << ", Height: " << height << ", Area: " << area << endl;
    cout << "Auto x: " << x << ", y: " << y << ", z: " << z << endl;
    
    return 0;
}
```

---

## Control Flow (If/Else, Switch)

### If-Else Statements
```cpp
#include <iostream>
using namespace std;

int main() {
    int score = 85;
    
    // Simple if statement
    if (score >= 90) {
        cout << "Grade: A" << endl;
    }
    
    // If-else statement
    if (score >= 80) {
        cout << "Grade: B" << endl;
    } else {
        cout << "Grade: Below B" << endl;
    }
    
    // If-else if ladder
    if (score >= 90) {
        cout << "Excellent!" << endl;
    } else if (score >= 80) {
        cout << "Good job!" << endl;
    } else if (score >= 70) {
        cout << "Average" << endl;
    } else {
        cout << "Needs improvement" << endl;
    }
    
    // Nested if statements
    int age = 20;
    bool hasLicense = true;
    
    if (age >= 18) {
        if (hasLicense) {
            cout << "Eligible to drive" << endl;
        } else {
            cout << "Eligible for license" << endl;
        }
    } else {
        cout << "Not eligible to drive" << endl;
    }
    
    return 0;
}
```

### Switch Statement
```cpp
#include <iostream>
using namespace std;

int main() {
    int day = 3;
    
    switch (day) {
        case 1:
            cout << "Monday" << endl;
            break;
        case 2:
            cout << "Tuesday" << endl;
            break;
        case 3:
            cout << "Wednesday" << endl;
            break;
        case 4:
            cout << "Thursday" << endl;
            break;
        case 5:
            cout << "Friday" << endl;
            break;
        case 6:
            cout << "Saturday" << endl;
            break;
        case 7:
            cout << "Sunday" << endl;
            break;
        default:
            cout << "Invalid day" << endl;
    }
    
    // Switch with character
    char grade = 'B';
    
    switch (grade) {
        case 'A':
        case 'B':
            cout << "Good performance" << endl;
            break;
        case 'C':
            cout << "Average performance" << endl;
            break;
        case 'D':
        case 'F':
            cout << "Poor performance" << endl;
            break;
        default:
            cout << "Invalid grade" << endl;
    }
    
    return 0;
}
```

### Conditional Operator (Ternary)
```cpp
#include <iostream>
using namespace std;

int main() {
    int age = 20;
    string status;
    
    // Using conditional operator
    status = (age >= 18) ? "Adult" : "Minor";
    cout << "Status: " << status << endl;
    
    // Nested conditional operators
    int score = 85;
    string result = (score >= 90) ? "Excellent" :
                   (score >= 80) ? "Good" :
                   (score >= 70) ? "Average" : "Below Average";
    cout << "Result: " << result << endl;
    
    return 0;
}
```

---

## Loops (For, While)

### For Loop
```cpp
#include <iostream>
using namespace std;

int main() {
    // Basic for loop
    cout << "Counting from 1 to 5:" << endl;
    for (int i = 1; i <= 5; i++) {
        cout << i << " ";
    }
    cout << endl;
    
    // For loop with different increment
    cout << "Even numbers from 0 to 10:" << endl;
    for (int i = 0; i <= 10; i += 2) {
        cout << i << " ";
    }
    cout << endl;
    
    // For loop with decrement
    cout << "Counting down from 5 to 1:" << endl;
    for (int i = 5; i >= 1; i--) {
        cout << i << " ";
    }
    cout << endl;
    
    // Range-based for loop (C++11)
    int numbers[] = {1, 2, 3, 4, 5};
    cout << "Using range-based for loop:" << endl;
    for (int num : numbers) {
        cout << num << " ";
    }
    cout << endl;
    
    return 0;
}
```

### While Loop
```cpp
#include <iostream>
using namespace std;

int main() {
    int count = 1;
    
    cout << "Using while loop:" << endl;
    while (count <= 5) {
        cout << count << " ";
        count++;
    }
    cout << endl;
    
    // While loop with condition change
    int num = 10;
    cout << "Dividing by 2 until less than 1:" << endl;
    while (num > 1) {
        cout << num << " ";
        num /= 2;
    }
    cout << endl;
    
    return 0;
}
```

### Do-While Loop
```cpp
#include <iostream>
using namespace std;

int main() {
    int count = 1;
    
    cout << "Using do-while loop:" << endl;
    do {
        cout << count << " ";
        count++;
    } while (count <= 5);
    cout << endl;
    
    // Do-while guarantees at least one execution
    int condition = 0;
    cout << "Do-while executes at least once:" << endl;
    do {
        cout << "This will print once even if condition is false" << endl;
    } while (condition != 0);
    
    return 0;
}
```

### Nested Loops
```cpp
#include <iostream>
using namespace std;

int main() {
    // Multiplication table
    cout << "Multiplication Table (1-5):" << endl;
    for (int i = 1; i <= 5; i++) {
        for (int j = 1; j <= 5; j++) {
            cout << i * j << "\t";
        }
        cout << endl;
    }
    
    // Pattern printing
    cout << "\nRight triangle pattern:" << endl;
    for (int i = 1; i <= 5; i++) {
        for (int j = 1; j <= i; j++) {
            cout << "* ";
        }
        cout << endl;
    }
    
    return 0;
}
```

### Loop Control Statements
```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Using continue and break:" << endl;
    
    // Skip even numbers using continue
    cout << "Odd numbers from 1 to 10:" << endl;
    for (int i = 1; i <= 10; i++) {
        if (i % 2 == 0) {
            continue;  // Skip even numbers
        }
        cout << i << " ";
    }
    cout << endl;
    
    // Stop at 5 using break
    cout << "Numbers from 1 to 10, stopping at 5:" << endl;
    for (int i = 1; i <= 10; i++) {
        if (i > 5) {
            break;  // Exit loop when i > 5
        }
        cout << i << " ";
    }
    cout << endl;
    
    return 0;
}
```

---

## Tables (Arrays)

### Basic Arrays
```cpp
#include <iostream>
#include <array>
#include <iomanip>
using namespace std;

int main() {
    // Traditional C-style arrays
    int traditionalArray[5] = {10, 20, 30, 40, 50};
    
    // C++ std::array (preferred)
    array<int, 5> cppArray = {100, 200, 300, 400, 500};
    
    // Array of doubles
    double prices[] = {19.99, 29.99, 39.99, 49.99};
    
    // Array of strings
    string names[3] = {"Alice", "Bob", "Charlie"};
    
    cout << "Traditional array: ";
    for (int i = 0; i < 5; i++) {
        cout << traditionalArray[i] << " ";
    }
    cout << endl;
    
    cout << "C++ array: ";
    for (size_t i = 0; i < cppArray.size(); i++) {
        cout << cppArray[i] << " ";
    }
    cout << endl;
    
    cout << "Prices array: ";
    for (int i = 0; i < sizeof(prices)/sizeof(prices[0]); i++) {
        cout << fixed << setprecision(2) << prices[i] << " ";
    }
    cout << endl;
    
    cout << "Names array: ";
    for (const string& name : names) {
        cout << name << " ";
    }
    cout << endl;
    
    // Multidimensional arrays
    int matrix[3][3] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };
    
    cout << "\n2D Array (Matrix):" << endl;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }
    
    // 3D array example
    int cube[2][2][2] = {
        {{1, 2}, {3, 4}},
        {{5, 6}, {7, 8}}
    };
    
    cout << "\n3D Array (Cube):" << endl;
    for (int i = 0; i < 2; i++) {
        cout << "Layer " << i << ":" << endl;
        for (int j = 0; j < 2; j++) {
            for (int k = 0; k < 2; k++) {
                cout << cube[i][j][k] << " ";
            }
            cout << endl;
        }
        cout << endl;
    }
    
    return 0;
}
```

### Array Operations and Algorithms
```cpp
#include <iostream>
#include <array>
#include <algorithm>
#include <numeric>
#include <iterator>
using namespace std;

int main() {
    array<int, 10> numbers = {5, 2, 8, 1, 9, 3, 7, 4, 6, 0};
    
    cout << "Original array: ";
    for (int n : numbers) cout << n << " ";
    cout << endl;
    
    // Sort the array
    sort(numbers.begin(), numbers.end());
    cout << "Sorted: ";
    for (int n : numbers) cout << n << " ";
    cout << endl;
    
    // Reverse the array
    reverse(numbers.begin(), numbers.end());
    cout << "Reversed: ";
    for (int n : numbers) cout << n << " ";
    cout << endl;
    
    // Find maximum and minimum
    auto minMax = minmax_element(numbers.begin(), numbers.end());
    cout << "Min: " << *(minMax.first) << ", Max: " << *(minMax.second) << endl;
    
    // Calculate sum
    int sum = accumulate(numbers.begin(), numbers.end(), 0);
    cout << "Sum: " << sum << endl;
    
    // Count occurrences
    int count = count(numbers.begin(), numbers.end(), 5);
    cout << "Count of 5: " << count << endl;
    
    // Fill array with a value
    array<int, 5> filledArray;
    fill(filledArray.begin(), filledArray.end(), 42);
    cout << "Filled with 42: ";
    for (int n : filledArray) cout << n << " ";
    cout << endl;
    
    // Partial fill
    array<int, 10> partialFill = {};
    fill(partialFill.begin(), partialFill.begin() + 5, 7);
    cout << "Partially filled: ";
    for (int n : partialFill) cout << n << " ";
    cout << endl;
    
    // Array of objects
    struct Point {
        int x, y;
        Point(int x = 0, int y = 0) : x(x), y(y) {}
        void display() const { cout << "(" << x << "," << y << ") "; }
    };
    
    array<Point, 3> points = {Point(1, 2), Point(3, 4), Point(5, 6)};
    
    cout << "Array of Points: ";
    for (const Point& p : points) {
        p.display();
    }
    cout << endl;
    
    // Array iteration with indices
    cout << "Index-value pairs: ";
    for (size_t i = 0; i < numbers.size(); i++) {
        cout << "[" << i << "]=" << numbers[i] << " ";
    }
    cout << endl;
    
    // Using iterators
    cout << "Using iterators: ";
    for (auto it = numbers.begin(); it != numbers.end(); ++it) {
        cout << *it << " ";
    }
    cout << endl;
    
    return 0;
}
```

### Dynamic Arrays and Memory Management
```cpp
#include <iostream>
#include <vector>
#include <memory>
using namespace std;

int main() {
    // Dynamic array using new
    int size = 5;
    int* dynamicArray = new int[size];
    
    // Initialize the dynamic array
    for (int i = 0; i < size; i++) {
        dynamicArray[i] = (i + 1) * 10;
    }
    
    cout << "Dynamic array: ";
    for (int i = 0; i < size; i++) {
        cout << dynamicArray[i] << " ";
    }
    cout << endl;
    
    // Resize the array (manual implementation)
    int newSize = 8;
    int* resizedArray = new int[newSize];
    
    // Copy old values
    for (int i = 0; i < size; i++) {
        resizedArray[i] = dynamicArray[i];
    }
    
    // Initialize new elements
    for (int i = size; i < newSize; i++) {
        resizedArray[i] = (i + 1) * 100;
    }
    
    cout << "Resized array: ";
    for (int i = 0; i < newSize; i++) {
        cout << resizedArray[i] << " ";
    }
    cout << endl;
    
    // Clean up dynamically allocated memory
    delete[] dynamicArray;
    delete[] resizedArray;
    
    // Better approach: Using smart pointers
    unique_ptr<int[]> smartArray(new int[6]);
    for (int i = 0; i < 6; i++) {
        smartArray[i] = (i + 1) * 5;
    }
    
    cout << "Smart pointer array: ";
    for (int i = 0; i < 6; i++) {
        cout << smartArray[i] << " ";
    }
    cout << endl;
    // No need to manually delete - automatic cleanup
    
    // Using vector instead of manual dynamic arrays (recommended)
    cout << "\nUsing vector (recommended approach):" << endl;
    vector<int> recommendedArray = {10, 20, 30, 40, 50};
    
    cout << "Initial vector: ";
    for (int n : recommendedArray) cout << n << " ";
    cout << endl;
    
    // Add elements
    recommendedArray.push_back(60);
    recommendedArray.push_back(70);
    
    cout << "After adding elements: ";
    for (int n : recommendedArray) cout << n << " ";
    cout << endl;
    
    // Remove elements
    recommendedArray.pop_back();
    
    cout << "After removing last element: ";
    for (int n : recommendedArray) cout << n << ";
    cout << endl;
    
    // Multi-dimensional dynamic arrays
    int rows = 3, cols = 4;
    int** matrix = new int*[rows];
    for (int i = 0; i < rows; i++) {
        matrix[i] = new int[cols];
    }
    
    // Initialize the matrix
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            matrix[i][j] = i * cols + j;
        }
    }
    
    cout << "\nDynamic 2D array:" << endl;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            cout << matrix[i][j] << "\t";
        }
        cout << endl;
    }
    
    // Clean up 2D array
    for (int i = 0; i < rows; i++) {
        delete[] matrix[i];
    }
    delete[] matrix;
    
    return 0;
}
```

---

## Functions (Pass-by-value vs. Pass-by-reference)

### Basic Function Definition
```cpp
#include <iostream>
using namespace std;

// Function declaration
void greet();
int add(int a, int b);
double calculateArea(double radius);

int main() {
    // Function calls
    greet();
    
    int sum = add(10, 20);
    cout << "Sum: " << sum << endl;
    
    double area = calculateArea(5.0);
    cout << "Area of circle: " << area << endl;
    
    return 0;
}

// Function definitions
void greet() {
    cout << "Hello, welcome to C++ functions!" << endl;
}

int add(int a, int b) {
    return a + b;
}

double calculateArea(double radius) {
    const double PI = 3.14159;
    return PI * radius * radius;
}
```

### Function Parameters and Return Types
```cpp
#include <iostream>
#include <string>
using namespace std;

// Function with multiple parameters
int multiply(int x, int y, int z) {
    return x * y * z;
}

// Function with default parameters
int power(int base, int exp = 2) {
    int result = 1;
    for (int i = 0; i < exp; i++) {
        result *= base;
    }
    return result;
}

// Function returning multiple values via reference
void swapValues(int& a, int& b) {
    int temp = a;
    a = b;
    b = temp;
}

// Function with string parameter
string repeatString(const string& str, int times) {
    string result = "";
    for (int i = 0; i < times; i++) {
        result += str;
    }
    return result;
}

int main() {
    cout << "Product: " << multiply(2, 3, 4) << endl;
    cout << "Power (default): " << power(3) << endl;  // Uses default exponent 2
    cout << "Power (custom): " << power(3, 4) << endl;  // Uses custom exponent
    
    int x = 10, y = 20;
    cout << "Before swap: x = " << x << ", y = " << y << endl;
    swapValues(x, y);
    cout << "After swap: x = " << x << ", y = " << y << endl;
    
    cout << "Repeated string: " << repeatString("Hello ", 3) << endl;
    
    return 0;
}
```

### Pass-by-value vs Pass-by-reference
```cpp
#include <iostream>
using namespace std;

// Pass-by-value: function receives a copy
void modifyByValue(int x) {
    x = 100;  // Only modifies the local copy
    cout << "Inside modifyByValue: x = " << x << endl;
}

// Pass-by-reference: function receives a reference
void modifyByReference(int& x) {
    x = 200;  // Modifies the original variable
    cout << "Inside modifyByReference: x = " << x << endl;
}

// Pass-by-constant-reference: prevents modification
void printByConstReference(const int& x) {
    // x = 30;  // This would cause a compile error
    cout << "Inside printByConstReference: x = " << x << endl;
}

// Pass-by-pointer
void modifyByPointer(int* x) {
    if (x != nullptr) {
        *x = 300;  // Modifies the original variable
        cout << "Inside modifyByPointer: *x = " << *x << endl;
    }
}

int main() {
    int value = 42;
    
    cout << "Original value: " << value << endl;
    
    // Pass-by-value
    modifyByValue(value);
    cout << "After modifyByValue: " << value << endl;
    
    // Pass-by-reference
    modifyByReference(value);
    cout << "After modifyByReference: " << value << endl;
    
    // Pass-by-constant-reference
    printByConstReference(value);
    cout << "After printByConstReference: " << value << endl;
    
    // Pass-by-pointer
    modifyByPointer(&value);
    cout << "After modifyByPointer: " << value << endl;
    
    return 0;
}
```

### Function Overloading
```cpp
#include <iostream>
#include <string>
using namespace std;

// Function overloading - same name, different parameters
void print(int value) {
    cout << "Integer: " << value << endl;
}

void print(double value) {
    cout << "Double: " << value << endl;
}

void print(const string& value) {
    cout << "String: " << value << endl;
}

void print(int a, int b) {
    cout << "Two integers: " << a << ", " << b << endl;
}

void print(int arr[], int size) {
    cout << "Array: ";
    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main() {
    print(42);                    // Calls print(int)
    print(3.14);                  // Calls print(double)
    print("Hello");               // Calls print(string)
    print(10, 20);                // Calls print(int, int)
    
    int numbers[] = {1, 2, 3, 4, 5};
    print(numbers, 5);            // Calls print(array, size)
    
    return 0;
}
```

### Recursive Functions
```cpp
#include <iostream>
using namespace std;

// Factorial calculation using recursion
long long factorial(int n) {
    if (n <= 1) {
        return 1;  // Base case
    }
    return n * factorial(n - 1);  // Recursive case
}

// Fibonacci sequence using recursion
long long fibonacci(int n) {
    if (n <= 1) {
        return n;  // Base cases
    }
    return fibonacci(n - 1) + fibonacci(n - 2);  // Recursive case
}

// Power calculation using recursion
int powerRecursive(int base, int exp) {
    if (exp == 0) {
        return 1;  // Base case
    }
    if (exp == 1) {
        return base;  // Base case
    }
    return base * powerRecursive(base, exp - 1);  // Recursive case
}

int main() {
    cout << "Factorial of 5: " << factorial(5) << endl;
    cout << "Fibonacci of 10: " << fibonacci(10) << endl;
    cout << "2^8: " << powerRecursive(2, 8) << endl;
    
    return 0;
}
```

---

## Pointers and References

### Pointers
```cpp
#include <iostream>
using namespace std;

int main() {
    // Declaring and initializing a pointer
    int value = 42;
    int* ptr = &value; // ptr points to the address of value
    
    cout << "Value: " << value << endl;
    cout << "Address of value: " << &value << endl;
    cout << "Pointer value (address): " << ptr << endl;
    cout << "Value pointed to by ptr: " << *ptr << endl;
    
    // Changing value through pointer
    *ptr = 100;
    cout << "After changing through pointer, value: " << value << endl;
    
    // Pointer arithmetic
    int arr[] = {10, 20, 30, 40, 50};
    int* arrPtr = arr;  // Points to first element
    
    cout << "\nArray elements using pointer arithmetic:" << endl;
    for (int i = 0; i < 5; i++) {
        cout << "Element " << i << ": " << *(arrPtr + i) << endl;
    }
    
    // Pointer to pointer
    int** ptrToPtr = &ptr;
    cout << "\nValue through pointer to pointer: " << **ptrToPtr << endl;
    
    // Null pointer
    int* nullPtr = nullptr;
    if (nullPtr == nullptr) {
        cout << "Pointer is null" << endl;
    }
    
    return 0;
}
```

### References
```cpp
#include <iostream>
using namespace std;

int main() {
    int value = 42;
    
    // Reference declaration
    int& ref = value;  // ref is an alias for value
    
    cout << "Value: " << value << endl;
    cout << "Reference: " << ref << endl;
    
    // Modifying through reference
    ref = 100;
    cout << "After modifying through reference, value: " << value << endl;
    
    // References vs Pointers
    int x = 10;
    int y = 20;
    
    int& refX = x;  // Reference must be initialized
    cout << "refX = " << refX << endl;
    
    // refX = y;  // This assigns y's VALUE to x, not makes refX point to y
    cout << "After refX = y, x = " << x << ", y = " << y << ", refX = " << refX << endl;
    
    // Pointer example for comparison
    int* ptr = &x;
    ptr = &y;  // Now ptr points to y
    cout << "After ptr = &y, ptr points to value: " << *ptr << endl;
    
    return 0;
}
```

### Pointers and Functions
```cpp
#include <iostream>
using namespace std;

// Function that takes pointer as parameter
void modifyThroughPointer(int* ptr) {
    if (ptr != nullptr) {
        *ptr = 100;
    }
}

// Function that returns a pointer
int* createInt(int value) {
    int* ptr = new int(value);
    return ptr;
}

// Function that takes reference as parameter
void modifyThroughReference(int& ref) {
    ref = 200;
}

int main() {
    int value = 42;
    
    cout << "Original value: " << value << endl;
    
    // Modify through pointer
    modifyThroughPointer(&value);
    cout << "After modifyThroughPointer: " << value << endl;
    
    // Modify through reference
    modifyThroughReference(value);
    cout << "After modifyThroughReference: " << value << endl;
    
    // Function that returns pointer
    int* dynamicInt = createInt(300);
    cout << "Value from createInt: " << *dynamicInt << endl;
    
    // Don't forget to clean up dynamically allocated memory
    delete dynamicInt;
    
    return 0;
}
```

---

## Vectors (Dynamic Arrays)

### Basic Vector Operations
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

int main() {
    // Creating vectors
    vector<int> numbers;                    // Empty vector
    vector<int> numbers2(5, 10);           // Vector with 5 elements, all 10
    vector<int> numbers3 = {1, 2, 3, 4, 5}; // Initialize with values
    
    cout << "Empty vector size: " << numbers.size() << endl;
    cout << "Vector with 5 tens: ";
    for (int n : numbers2) cout << n << " ";
    cout << endl;
    
    cout << "Initialized vector: ";
    for (int n : numbers3) cout << n << " ";
    cout << endl;
    
    // Adding elements
    numbers.push_back(10);
    numbers.push_back(20);
    numbers.push_back(30);
    
    cout << "After adding elements: ";
    for (int n : numbers) cout << n << " ";
    cout << endl;
    
    // Accessing elements
    cout << "First element: " << numbers.front() << endl;
    cout << "Last element: " << numbers.back() << endl;
    cout << "Element at index 1: " << numbers[1] << endl;
    cout << "Element at index 1 (safe): " << numbers.at(1) << endl;
    
    // Iterating with iterators
    cout << "Using iterators: ";
    for (auto it = numbers.begin(); it != numbers.end(); ++it) {
        cout << *it << " ";
    }
    cout << endl;
    
    // Size and capacity
    cout << "Size: " << numbers.size() << ", Capacity: " << numbers.capacity() << endl;
    
    return 0;
}
```

### Vector Manipulation Methods
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<int> numbers = {10, 20, 30, 40, 50};
    
    cout << "Original vector: ";
    for (int n : numbers) cout << n << " ";
    cout << endl;
    
    // Insert elements
    numbers.insert(numbers.begin() + 2, 25);  // Insert at position 2
    cout << "After inserting 25 at pos 2: ";
    for (int n : numbers) cout << n << " ";
    cout << endl;
    
    // Insert multiple elements
    vector<int> moreNumbers = {15, 17};
    numbers.insert(numbers.begin() + 1, moreNumbers.begin(), moreNumbers.end());
    cout << "After inserting multiple: ";
    for (int n : numbers) cout << n << " ";
    cout << endl;
    
    // Erase elements
    numbers.erase(numbers.begin() + 3);  // Remove element at position 3
    cout << "After erasing position 3: ";
    for (int n : numbers) cout << n << " ";
    cout << endl;
    
    // Erase range
    numbers.erase(numbers.begin() + 1, numbers.begin() + 3);
    cout << "After erasing positions 1-2: ";
    for (int n : numbers) cout << n << ";
    cout << endl;
    
    // Clear vector
    vector<int> temp = {1, 2, 3, 4, 5};
    cout << "Before clear: " << temp.size() << " elements" << endl;
    temp.clear();
    cout << "After clear: " << temp.size() << " elements" << endl;
    
    // Resize vector
    temp.resize(3, 0);  // Resize to 3 elements, fill new with 0
    cout << "After resize to 3 with fill 0: ";
    for (int n : temp) cout << n << " ";
    cout << endl;
    
    temp.resize(6, 99);  // Resize to 6 elements, fill new with 99
    cout << "After resize to 6 with fill 99: ";
    for (int n : temp) cout << n << " ";
    cout << endl;
    
    return 0;
}
```

### Vector Algorithms and Sorting
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
using namespace std;

int main() {
    vector<int> numbers = {5, 2, 8, 1, 9, 3, 7, 4, 6};
    
    cout << "Original vector: ";
    for (int n : numbers) cout << n << " ";
    cout << endl;
    
    // Sort vector
    sort(numbers.begin(), numbers.end());
    cout << "Sorted ascending: ";
    for (int n : numbers) cout << n << " ";
    cout << endl;
    
    // Sort in descending order
    sort(numbers.rbegin(), numbers.rend());  // Reverse iterators
    cout << "Sorted descending: ";
    for (int n : numbers) cout << n << ";
    cout << endl;
    
    // Find element
    auto it = find(numbers.begin(), numbers.end(), 7);
    if (it != numbers.end()) {
        cout << "Found 7 at position: " << distance(numbers.begin(), it) << endl;
    } else {
        cout << "7 not found" << endl;
    }
    
    // Count occurrences
    int count = count(numbers.begin(), numbers.end(), 5);
    cout << "Count of 5: " << count << endl;
    
    // Calculate sum
    int sum = accumulate(numbers.begin(), numbers.end(), 0);
    cout << "Sum of all elements: " << sum << endl;
    
    // Minimum and maximum
    auto minMax = minmax_element(numbers.begin(), numbers.end());
    cout << "Min: " << *(minMax.first) << ", Max: " << *(minMax.second) << endl;
    
    // Reverse vector
    reverse(numbers.begin(), numbers.end());
    cout << "Reversed: ";
    for (int n : numbers) cout << n << " ";
    cout << endl;
    
    // Unique elements (requires sorted vector)
    vector<int> sortedNums = {1, 1, 2, 2, 3, 4, 4, 5};
    auto last = unique(sortedNums.begin(), sortedNums.end());
    sortedNums.erase(last, sortedNums.end());
    cout << "Unique elements: ";
    for (int n : sortedNums) cout << n << " ";
    cout << endl;
    
    return 0;
}
```

### Vector of Objects
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

class Person {
private:
    string name;
    int age;

public:
    Person(const string& n, int a) : name(n), age(a) {}
    
    const string& getName() const { return name; }
    int getAge() const { return age; }
    
    void display() const {
        cout << "Name: " << name << ", Age: " << age << endl;
    }
    
    // Comparison operator for sorting
    bool operator<(const Person& other) const {
        return age < other.age;
    }
};

int main() {
    // Vector of objects
    vector<Person> people = {
        Person("Alice", 25),
        Person("Bob", 30),
        Person("Charlie", 20),
        Person("Diana", 35)
    };
    
    cout << "People in vector:" << endl;
    for (const Person& person : people) {
        person.display();
    }
    
    // Sort by age using overloaded operator<
    sort(people.begin(), people.end());
    cout << "\nAfter sorting by age:" << endl;
    for (const Person& person : people) {
        person.display();
    }
    
    // Using lambda for custom sorting
    sort(people.begin(), people.end(), [](const Person& a, const Person& b) {
        return a.getName() < b.getName();  // Sort by name
    });
    
    cout << "\nAfter sorting by name:" << endl;
    for (const Person& person : people) {
        person.display();
    }
    
    // Find person by age
    auto it = find_if(people.begin(), people.end(), [](const Person& p) {
        return p.getAge() == 30;
    });
    
    if (it != people.end()) {
        cout << "\nFound person with age 30: ";
        it->display();
    }
    
    // Add new person
    people.emplace_back("Eve", 28);  // More efficient than push_back
    cout << "\nAfter adding Eve:" << endl;
    for (const Person& person : people) {
        person.display();
    }
    
    return 0;
}
```

---

## Maps (Associative Containers)

### Basic Map Operations
```cpp
#include <iostream>
#include <map>
#include <string>
#include <utility>
using namespace std;

int main() {
    // Creating maps
    map<string, int> ages;
    map<string, int> grades = {{"Alice", 85}, {"Bob", 92}, {"Charlie", 78}};
    
    // Inserting elements
    ages["John"] = 25;
    ages["Jane"] = 30;
    ages["Mike"] = 35;
    
    // Insert using insert method
    ages.insert(make_pair("Sarah", 28));
    ages.insert({"Tom", 32});
    
    cout << "Ages map:" << endl;
    for (const auto& pair : ages) {
        cout << pair.first << ": " << pair.second << endl;
    }
    
    cout << "\nGrades map:" << endl;
    for (const auto& pair : grades) {
        cout << pair.first << ": " << pair.second << endl;
    }
    
    // Accessing elements
    cout << "\nAccessing elements:" << endl;
    cout << "John's age: " << ages["John"] << endl;
    cout << "Jane's age (using at): " << ages.at("Jane") << endl;
    
    // Updating elements
    ages["John"] = 26;
    cout << "Updated John's age: " << ages["John"] << endl;
    
    // Check if key exists
    string key = "Bob";
    if (grades.find(key) != grades.end()) {
        cout << key << " exists in grades map with value: " << grades[key] << endl;
    } else {
        cout << key << " does not exist in grades map" << endl;
    }
    
    // Safe access using find
    auto it = ages.find("NonExistent");
    if (it != ages.end()) {
        cout << "Found: " << it->first << " -> " << it->second << endl;
    } else {
        cout << "Key not found in ages map" << endl;
    }
    
    return 0;
}
```

### Map Methods and Iteration
```cpp
#include <iostream>
#include <map>
#include <string>
using namespace std;

int main() {
    map<string, int> scores = {
        {"Math", 95},
        {"English", 87},
        {"Science", 92},
        {"History", 88}
    };
    
    cout << "Original map:" << endl;
    for (const auto& subject : scores) {
        cout << subject.first << ": " << subject.second << endl;
    }
    
    // Size and emptiness
    cout << "\nMap size: " << scores.size() << endl;
    cout << "Is empty: " << (scores.empty() ? "Yes" : "No") << endl;
    
    // Lower and upper bounds
    auto lower = scores.lower_bound("English");
    auto upper = scores.upper_bound("Science");
    
    cout << "\nElements from 'English' inclusive to 'Science' exclusive:" << endl;
    for (auto it = lower; it != upper; ++it) {
        cout << it->first << ": " << it->second << endl;
    }
    
    // Equal range (returns pair of iterators)
    auto range = scores.equal_range("History");
    cout << "\nEqual range for 'History':" << endl;
    for (auto it = range.first; it != range.second; ++it) {
        cout << it->first << ": " << it->second << endl;
    }
    
    // Erasing elements
    scores.erase("History");
    cout << "\nAfter erasing 'History':" << endl;
    for (const auto& subject : scores) {
        cout << subject.first << ": " << subject.second << endl;
    }
    
    // Erasing by iterator
    auto eraseIt = scores.find("English");
    if (eraseIt != scores.end()) {
        scores.erase(eraseIt);
        cout << "\nAfter erasing 'English' by iterator:" << endl;
        for (const auto& subject : scores) {
            cout << subject.first << ": " << subject.second << endl;
        }
    }
    
    // Clear the map
    map<string, int> temp = {{"A", 1}, {"B", 2}};
    cout << "\nBefore clear: " << temp.size() << " elements" << endl;
    temp.clear();
    cout << "After clear: " << temp.size() << " elements" << endl;
    
    return 0;
}
```

### Unordered Map vs Ordered Map
```cpp
#include <iostream>
#include <map>
#include <unordered_map>
#include <string>
#include <chrono>
using namespace std;

int main() {
    // Ordered map (std::map) - maintains sorted order
    map<string, int> orderedMap = {
        {"zebra", 1},
        {"apple", 2},
        {"banana", 3},
        {"cherry", 4},
        {"dog", 5}
    };
    
    cout << "Ordered map (maintains alphabetical order):" << endl;
    for (const auto& pair : orderedMap) {
        cout << pair.first << ": " << pair.second << endl;
    }
    
    // Unordered map (std::unordered_map) - faster access, no order guarantee
    unordered_map<string, int> unorderedMap = {
        {"zebra", 1},
        {"apple", 2},
        {"banana", 3},
        {"cherry", 4},
        {"dog", 5}
    };
    
    cout << "\nUnordered map (no guaranteed order):" << endl;
    for (const auto& pair : unorderedMap) {
        cout << pair.first << ": " << pair.second << endl;
    }
    
    // Performance comparison
    cout << "\nPerformance comparison:" << endl;
    
    // Timing ordered map insertion
    auto start = chrono::high_resolution_clock::now();
    map<int, string> orderedTest;
    for (int i = 0; i < 10000; i++) {
        orderedTest[i] = "value" + to_string(i);
    }
    auto end = chrono::high_resolution_clock::now();
    auto orderedTime = chrono::duration_cast<chrono::microseconds>(end - start);
    
    // Timing unordered map insertion
    start = chrono::high_resolution_clock::now();
    unordered_map<int, string> unorderedTest;
    for (int i = 0; i < 10000; i++) {
        unorderedTest[i] = "value" + to_string(i);
    }
    end = chrono::high_resolution_clock::now();
    auto unorderedTime = chrono::duration_cast<chrono::microseconds>(end - start);
    
    cout << "Ordered map insertion time: " << orderedTime.count() << " microseconds" << endl;
    cout << "Unordered map insertion time: " << unorderedTime.count() << " microseconds" << endl;
    
    // Count method
    cout << "\nUsing count method:" << endl;
    cout << "Does 'apple' exist in ordered map? " 
         << (orderedMap.count("apple") ? "Yes" : "No") << endl;
    cout << "Does 'grape' exist in ordered map? " 
         << (orderedMap.count("grape") ? "Yes" : "No") << endl;
    
    // Try-emplace (C++17) - only inserts if key doesn't exist
    auto [it, inserted] = orderedMap.try_emplace("elderberry", 6);
    cout << "Tried to insert 'elderberry': " << (inserted ? "Success" : "Already existed") << endl;
    
    // Emplace (always inserts)
    auto [it2, inserted2] = orderedMap.emplace("fig", 7);
    cout << "Emplaced 'fig': " << (inserted2 ? "New element" : "Already existed") << endl;
    
    return 0;
}
```

### Map with Custom Comparator
```cpp
#include <iostream>
#include <map>
#include <string>
#include <functional>
using namespace std;

// Custom comparator class
struct CaseInsensitiveCompare {
    bool operator()(const string& a, const string& b) const {
        string lowerA = a;
        string lowerB = b;
        
        // Convert to lowercase for comparison
        transform(lowerA.begin(), lowerA.end(), lowerA.begin(), ::tolower);
        transform(lowerB.begin(), lowerB.end(), lowerB.begin(), ::tolower);
        
        return lowerA < lowerB;
    }
};

int main() {
    // Map with custom comparator
    map<string, int, CaseInsensitiveCompare> caseInsensitiveMap;
    
    caseInsensitiveMap["Apple"] = 1;
    caseInsensitiveMap["banana"] = 2;
    caseInsensitiveMap["Cherry"] = 3;
    caseInsensitiveMap["apPLe"] = 4;  // This will overwrite the first "Apple"
    
    cout << "Case-insensitive map:" << endl;
    for (const auto& pair : caseInsensitiveMap) {
        cout << pair.first << ": " << pair.second << endl;
    }
    
    // Lambda-based custom comparator
    auto lengthComparator = [](const string& a, const string& b) {
        if (a.length() != b.length()) {
            return a.length() < b.length();  // Sort by length first
        }
        return a < b;  // Then alphabetically
    };
    
    map<string, int, decltype(lengthComparator)> lengthBasedMap(lengthComparator);
    
    lengthBasedMap["short"] = 1;
    lengthBasedMap["medium"] = 2;
    lengthBasedMap["a"] = 3;
    lengthBasedMap["verylongstring"] = 4;
    lengthBasedMap["hi"] = 5;
    
    cout << "\nLength-based sorted map:" << endl;
    for (const auto& pair : lengthBasedMap) {
        cout << pair.first << " (" << pair.first.length() << " chars): " << pair.second << endl;
    }
    
    // Map of pairs
    map<pair<string, int>, double> complexMap;
    complexMap[make_pair("Alice", 25)] = 3.8;
    complexMap[make_pair("Bob", 30)] = 3.9;
    complexMap[make_pair("Alice", 26)] = 3.7;  // Different age, same name
    
    cout << "\nMap with pair keys:" << endl;
    for (const auto& pair : complexMap) {
        cout << "(" << pair.first.first << ", " << pair.first.second 
             << "): " << pair.second << endl;
    }
    
    return 0;
}
```

---

## Classes and Objects (The Basics)

### Basic Class Definition
```cpp
#include <iostream>
#include <string>
using namespace std;

class Student {
private:
    string name;
    int age;
    double gpa;

public:
    // Default constructor
    Student() {
        name = "Unknown";
        age = 0;
        gpa = 0.0;
        cout << "Default constructor called for " << name << endl;
    }
    
    // Parameterized constructor
    Student(string n, int a, double g) : name(n), age(a), gpa(g) {
        cout << "Parameterized constructor called for " << name << endl;
    }
    
    // Copy constructor
    Student(const Student& other) {
        name = other.name;
        age = other.age;
        gpa = other.gpa;
        cout << "Copy constructor called for " << name << endl;
    }
    
    // Destructor
    ~Student() {
        cout << "Destructor called for " << name << endl;
    }
    
    // Getter methods
    string getName() const { return name; }
    int getAge() const { return age; }
    double getGPA() const { return gpa; }
    
    // Setter methods
    void setName(const string& n) { name = n; }
    void setAge(int a) { age = a; }
    void setGPA(double g) { gpa = g; }
    
    // Display method
    void display() const {
        cout << "Name: " << name << ", Age: " << age << ", GPA: " << gpa << endl;
    }
};

int main() {
    cout << "Creating student1 with default constructor:" << endl;
    Student student1;
    student1.display();
    
    cout << "\nCreating student2 with parameterized constructor:" << endl;
    Student student2("Alice", 20, 3.8);
    student2.display();
    
    cout << "\nCreating student3 as copy of student2:" << endl;
    Student student3(student2);
    student3.display();
    
    cout << "\nEnd of main function - destructors will be called:" << endl;
    return 0;
}
```

### Constructor Initialization Lists
```cpp
#include <iostream>
#include <string>
using namespace std;

class Rectangle {
private:
    double length;
    double width;
    string color;
    static int count;  // Static member

public:
    // Constructor using initialization list
    Rectangle(double l, double w, string c) : 
        length(l), width(w), color(c) {
        count++;
        cout << "Rectangle created. Total rectangles: " << count << endl;
    }
    
    // Constructor with default values
    Rectangle(double l = 1.0, double w = 1.0) : 
        length(l), width(w), color("white") {
        count++;
        cout << "Rectangle created with default color. Total: " << count << endl;
    }
    
    // Copy constructor
    Rectangle(const Rectangle& other) :
        length(other.length), width(other.width), color(other.color) {
        count++;
        cout << "Rectangle copied. Total: " << count << endl;
    }
    
    ~Rectangle() {
        count--;
        cout << "Rectangle destroyed. Remaining: " << count << endl;
    }
    
    // Getters
    double getLength() const { return length; }
    double getWidth() const { return width; }
    string getColor() const { return color; }
    
    // Calculate area
    double getArea() const {
        return length * width;
    }
    
    // Display rectangle info
    void display() const {
        cout << "Rectangle: " << length << "x" << width 
             << ", Color: " << color 
             << ", Area: " << getArea() << endl;
    }
    
    // Static method to get count
    static int getCount() { return count; }
};

// Initialize static member
int Rectangle::count = 0;

int main() {
    cout << "Creating rectangles:" << endl;
    
    Rectangle rect1(5.0, 3.0, "red");
    rect1.display();
    
    Rectangle rect2(4.0, 6.0);
    rect2.display();
    
    Rectangle rect3(rect1);  // Copy constructor
    rect3.display();
    
    cout << "\nTotal rectangles created: " << Rectangle::getCount() << endl;
    
    return 0;
}
```

### Methods and Access Specifiers
```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class BankAccount {
private:
    string accountNumber;
    double balance;
    string owner;
    vector<double> transactionHistory;
    
    // Private helper method
    bool isValidAmount(double amount) const {
        return amount >= 0;
    }
    
public:
    // Constructor
    BankAccount(const string& accNum, const string& own, double initialBalance = 0.0)
        : accountNumber(accNum), owner(own), balance(initialBalance) {
        if (initialBalance > 0) {
            transactionHistory.push_back(initialBalance);
        }
    }
    
    // Public interface methods
    void deposit(double amount) {
        if (isValidAmount(amount)) {
            balance += amount;
            transactionHistory.push_back(amount);
            cout << "Deposited $" << amount << ". New balance: $" << balance << endl;
        } else {
            cout << "Invalid deposit amount: $" << amount << endl;
        }
    }
    
    bool withdraw(double amount) {
        if (isValidAmount(amount) && amount <= balance) {
            balance -= amount;
            transactionHistory.push_back(-amount);  // Negative indicates withdrawal
            cout << "Withdrew $" << amount << ". New balance: $" << balance << endl;
            return true;
        } else {
            cout << "Invalid withdrawal amount: $" << amount 
                 << " (Balance: $" << balance << ")" << endl;
            return false;
        }
    }
    
    // Getter methods (controlled access)
    double getBalance() const {
        return balance;
    }
    
    string getAccountNumber() const {
        return accountNumber;
    }
    
    string getOwner() const {
        return owner;
    }
    
    // Method to view limited transaction history
    void showRecentTransactions(int count = 5) const {
        int start = max(0, (int)transactionHistory.size() - count);
        cout << "Recent " << count << " transactions:" << endl;
        for (int i = start; i < transactionHistory.size(); i++) {
            cout << "  " << (transactionHistory[i] >= 0 ? "Deposit: " : "Withdrawal: ")
                 << "$" << abs(transactionHistory[i]) << endl;
        }
    }
    
    // Display account info
    void displayInfo() const {
        cout << "Account: " << accountNumber << ", Owner: " << owner 
             << ", Balance: $" << balance << endl;
    }
};

int main() {
    BankAccount account("ACC001", "John Doe", 1000.0);
    account.displayInfo();
    
    account.deposit(500.0);
    account.withdraw(200.0);
    account.withdraw(2000.0);  // Invalid withdrawal
    
    account.showRecentTransactions();
    
    cout << "Final balance: $" << account.getBalance() << endl;
    
    return 0;
}
```

---

## Constructors and Destructors

### Basic Class with Constructor and Destructor
```cpp
#include <iostream>
#include <string>
using namespace std;

class Student {
private:
    string name;
    int age;
    double gpa;

public:
    // Default constructor
    Student() {
        name = "Unknown";
        age = 0;
        gpa = 0.0;
        cout << "Default constructor called for " << name << endl;
    }
    
    // Parameterized constructor
    Student(string n, int a, double g) : name(n), age(a), gpa(g) {
        cout << "Parameterized constructor called for " << name << endl;
    }
    
    // Copy constructor
    Student(const Student& other) {
        name = other.name;
        age = other.age;
        gpa = other.gpa;
        cout << "Copy constructor called for " << name << endl;
    }
    
    // Destructor
    ~Student() {
        cout << "Destructor called for " << name << endl;
    }
    
    // Getter methods
    string getName() const { return name; }
    int getAge() const { return age; }
    double getGPA() const { return gpa; }
    
    // Setter methods
    void setName(const string& n) { name = n; }
    void setAge(int a) { age = a; }
    void setGPA(double g) { gpa = g; }
    
    // Display method
    void display() const {
        cout << "Name: " << name << ", Age: " << age << ", GPA: " << gpa << endl;
    }
};

int main() {
    cout << "Creating student1 with default constructor:" << endl;
    Student student1;
    student1.display();
    
    cout << "\nCreating student2 with parameterized constructor:" << endl;
    Student student2("Alice", 20, 3.8);
    student2.display();
    
    cout << "\nCreating student3 as copy of student2:" << endl;
    Student student3(student2);
    student3.display();
    
    cout << "\nEnd of main function - destructors will be called:" << endl;
    return 0;
}
```

### Destructors and Resource Management
```cpp
#include <iostream>
#include <fstream>
#include <memory>
using namespace std;

class FileHandler {
private:
    string filename;
    ofstream file;
    int* dynamicMemory;

public:
    // Constructor allocates resources
    FileHandler(const string& fname) : filename(fname) {
        cout << "Opening file: " << filename << endl;
        file.open(filename);
        
        // Allocate dynamic memory
        dynamicMemory = new int[100];
        cout << "Allocated dynamic memory" << endl;
    }
    
    // Destructor releases resources
    ~FileHandler() {
        if (file.is_open()) {
            file.close();
            cout << "Closed file: " << filename << endl;
        }
        
        if (dynamicMemory != nullptr) {
            delete[] dynamicMemory;
            cout << "Freed dynamic memory" << endl;
        }
    }
    
    // Method to write to file
    void writeData(const string& data) {
        if (file.is_open()) {
            file << data << endl;
        }
    }
    
    // Method to simulate error handling
    void processWithError() {
        cout << "Processing with potential error..." << endl;
        throw runtime_error("Simulated error");
    }
};

int main() {
    try {
        cout << "Creating FileHandler object:" << endl;
        FileHandler handler("test.txt");
        handler.writeData("Hello, World!");
        
        // Uncomment the next line to test destructor with exception
        // handler.processWithError();
        
        cout << "Normal exit from try block" << endl;
    } catch (const exception& e) {
        cout << "Exception caught: " << e.what() << endl;
    }
    
    cout << "End of main function" << endl;
    return 0;
}
```

---

## The `this` Pointer

### Understanding the `this` Pointer
```cpp
#include <iostream>
#include <string>
using namespace std;

class BankAccount {
private:
    string accountNumber;
    double balance;
    string owner;

public:
    // Constructor
    BankAccount(const string& accNum, double bal, const string& own) 
        : accountNumber(accNum), balance(bal), owner(own) {}
    
    // Using 'this' to distinguish between member variables and parameters
    void setDetails(const string& accountNumber, double balance, const string& owner) {
        this->accountNumber = accountNumber;  // Member vs parameter
        this->balance = balance;              // Member vs parameter
        this->owner = owner;                  // Member vs parameter
        
        cout << "Account details updated using 'this' pointer" << endl;
    }
    
    // Method chaining using 'this'
    BankAccount& deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            cout << "Deposited $" << amount << ". New balance: $" << balance << endl;
        }
        return *this;  // Return reference to current object
    }
    
    BankAccount& withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            cout << "Withdrew $" << amount << ". New balance: $" << balance << endl;
        }
        return *this;  // Return reference to current object
    }
    
    // Method to compare with another object
    bool isEqual(const BankAccount& other) {
        return (this->accountNumber == other.accountNumber &&
                this->balance == other.balance &&
                this->owner == other.owner);
    }
    
    // Self-assignment protection
    BankAccount& operator=(const BankAccount& other) {
        if (this != &other) {  // Check for self-assignment
            accountNumber = other.accountNumber;
            balance = other.balance;
            owner = other.owner;
            cout << "Assignment performed" << endl;
        } else {
            cout << "Self-assignment detected and avoided" << endl;
        }
        return *this;
    }
    
    // Display account information
    void display() const {
        cout << "Account: " << accountNumber << ", Owner: " << owner 
             << ", Balance: $" << balance << endl;
    }
    
    // Accessor methods
    const string& getAccountNumber() const { return accountNumber; }
    double getBalance() const { return balance; }
    const string& getOwner() const { return owner; }
};

int main() {
    BankAccount account("ACC001", 1000.0, "John Doe");
    account.display();
    
    // Using 'this' in method chaining
    account.deposit(50).withdraw(200).deposit(100);
    
    // Using 'this' to distinguish parameters from members
    account.setDetails("ACC002", 2000.0, "Jane Smith");
    account.display();
    
    // Comparing with another object
    BankAccount account2("ACC002", 2000.0, "Jane Smith");
    cout << "Accounts are equal: " << (account.isEqual(account2) ? "Yes" : "No") << endl;
    
    // Self-assignment test
    account = account;  // Should detect self-assignment
    
    return 0;
}
```

### `this` in Complex Scenarios
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class NumberProcessor {
private:
    vector<int> numbers;

public:
    NumberProcessor(const vector<int>& nums) : numbers(nums) {}
    
    // Method that returns a reference to the current object
    NumberProcessor& addNumber(int num) {
        numbers.push_back(num);
        cout << "Added " << num << endl;
        return *this;
    }
    
    // Method that returns a reference to the current object
    NumberProcessor& removeNumber(int num) {
        auto it = find(numbers.begin(), numbers.end(), num);
        if (it != numbers.end()) {
            numbers.erase(it);
            cout << "Removed " << num << endl;
        }
        return *this;
    }
    
    // Method that uses 'this' to compare with another object
    bool containsSameNumbers(const NumberProcessor& other) const {
        // Compare sizes first
        if (this->numbers.size() != other.numbers.size()) {
            return false;
        }
        
        // Sort both vectors temporarily for comparison
        vector<int> thisSorted = this->numbers;
        vector<int> otherSorted = other.numbers;
        
        sort(thisSorted.begin(), thisSorted.end());
        sort(otherSorted.begin(), otherSorted.end());
        
        return thisSorted == otherSorted;
    }
    
    // Method that returns the object itself
    NumberProcessor& sortNumbers() {
        sort(numbers.begin(), numbers.end());
        cout << "Numbers sorted" << endl;
        return *this;
    }
    
    // Method that processes and returns a new object
    NumberProcessor getProcessedVersion() const {
        NumberProcessor processed = *this;  // Copy of current object
        processed.sortNumbers();  // Process the copy
        return processed;
    }
    
    // Display method
    void display() const {
        cout << "Numbers: ";
        for (int num : numbers) {
            cout << num << " ";
        }
        cout << endl;
    }
    
    // Get size
    size_t getSize() const {
        return numbers.size();
    }
    
    // Operator overload that uses 'this'
    bool operator<(const NumberProcessor& other) const {
        return this->getSize() < other.getSize();
    }
};

int main() {
    NumberProcessor processor({5, 2, 8, 1});
    processor.display();
    
    // Method chaining using 'this'
    processor.addNumber(10).removeNumber(2).sortNumbers();
    processor.display();
    
    // Create another processor for comparison
    NumberProcessor processor2({8, 5, 1, 10});
    cout << "Both processors have same numbers: " 
         << (processor.containsSameNumbers(processor2) ? "Yes" : "No") << endl;
    
    // Get processed version
    NumberProcessor sortedVersion = processor.getProcessedVersion();
    cout << "Original: ";
    processor.display();
    cout << "Sorted version: ";
    sortedVersion.display();
    
    return 0;
}
```

---

## Object-Oriented Programming Principles (Encapsulation, Abstraction)

### Encapsulation
```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class BankAccount {
private:
    string accountNumber;
    double balance;
    string owner;
    vector<double> transactionHistory;
    
    // Private helper method
    bool isValidAmount(double amount) const {
        return amount >= 0;
    }
    
public:
    // Constructor
    BankAccount(const string& accNum, const string& own, double initialBalance = 0.0)
        : accountNumber(accNum), owner(own), balance(initialBalance) {
        if (initialBalance > 0) {
            transactionHistory.push_back(initialBalance);
        }
    }
    
    // Public interface methods
    void deposit(double amount) {
        if (isValidAmount(amount)) {
            balance += amount;
            transactionHistory.push_back(amount);
            cout << "Deposited $" << amount << ". New balance: $" << balance << endl;
        } else {
            cout << "Invalid deposit amount: $" << amount << endl;
        }
    }
    
    bool withdraw(double amount) {
        if (isValidAmount(amount) && amount <= balance) {
            balance -= amount;
            transactionHistory.push_back(-amount);  // Negative indicates withdrawal
            cout << "Withdrew $" << amount << ". New balance: $" << balance << endl;
            return true;
        } else {
            cout << "Invalid withdrawal amount: $" << amount 
                 << " (Balance: $" << balance << ")" << endl;
            return false;
        }
    }
    
    // Getter methods (controlled access)
    double getBalance() const {
        return balance;
    }
    
    string getAccountNumber() const {
        return accountNumber;
    }
    
    string getOwner() const {
        return owner;
    }
    
    // Method to view limited transaction history
    void showRecentTransactions(int count = 5) const {
        int start = max(0, (int)transactionHistory.size() - count);
        cout << "Recent " << count << " transactions:" << endl;
        for (int i = start; i < transactionHistory.size(); i++) {
            cout << "  " << (transactionHistory[i] >= 0 ? "Deposit: " : "Withdrawal: ")
                 << "$" << abs(transactionHistory[i]) << endl;
        }
    }
    
    // Display account info
    void displayInfo() const {
        cout << "Account: " << accountNumber << ", Owner: " << owner 
             << ", Balance: $" << balance << endl;
    }
};

int main() {
    BankAccount account("ACC001", "John Doe", 1000.0);
    account.displayInfo();
    
    account.deposit(500.0);
    account.withdraw(200.0);
    account.withdraw(2000.0);  // Invalid withdrawal
    
    account.showRecentTransactions();
    
    cout << "Final balance: $" << account.getBalance() << endl;
    
    return 0;
}
```

### Abstraction
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
using namespace std;

// Abstract base class
class Shape {
protected:
    string color;
    
public:
    Shape(const string& c) : color(c) {}
    
    // Pure virtual function makes this class abstract
    virtual double calculateArea() const = 0;
    virtual double calculatePerimeter() const = 0;
    
    // Virtual function that can be overridden
    virtual void display() const {
        cout << "Shape color: " << color << endl;
    }
    
    // Virtual destructor for proper cleanup
    virtual ~Shape() = default;
};

// Concrete derived classes
class Circle : public Shape {
private:
    double radius;
    
public:
    Circle(const string& c, double r) : Shape(c), radius(r) {}
    
    double calculateArea() const override {
        const double PI = 3.14159265359;
        return PI * radius * radius;
    }
    
    double calculatePerimeter() const override {
        const double PI = 3.14159265359;
        return 2 * PI * radius;
    }
    
    void display() const override {
        cout << "Circle - Radius: " << radius << ", Color: " << color 
             << ", Area: " << calculateArea() 
             << ", Perimeter: " << calculatePerimeter() << endl;
    }
};

class Rectangle : public Shape {
private:
    double width, height;
    
public:
    Rectangle(const string& c, double w, double h) : Shape(c), width(w), height(h) {}
    
    double calculateArea() const override {
        return width * height;
    }
    
    double calculatePerimeter() const override {
        return 2 * (width + height);
    }
    
    void display() const override {
        cout << "Rectangle - Width: " << width << ", Height: " << height 
             << ", Color: " << color 
             << ", Area: " << calculateArea() 
             << ", Perimeter: " << calculatePerimeter() << endl;
    }
};

class Triangle : public Shape {
private:
    double side1, side2, side3;
    
public:
    Triangle(const string& c, double s1, double s2, double s3) 
        : Shape(c), side1(s1), side2(s2), side3(s3) {}
    
    double calculateArea() const override {
        // Using Heron's formula
        double s = (side1 + side2 + side3) / 2;
        return sqrt(s * (s - side1) * (s - side2) * (s - side3));
    }
    
    double calculatePerimeter() const override {
        return side1 + side2 + side3;
    }
    
    void display() const override {
        cout << "Triangle - Sides: " << side1 << ", " << side2 << ", " << side3 
             << ", Color: " << color 
             << ", Area: " << calculateArea() 
             << ", Perimeter: " << calculatePerimeter() << endl;
    }
};

int main() {
    // Using polymorphism with smart pointers
    vector<unique_ptr<Shape>> shapes;
    
    shapes.push_back(make_unique<Circle>("Red", 5.0));
    shapes.push_back(make_unique<Rectangle>("Blue", 4.0, 6.0));
    shapes.push_back(make_unique<Triangle>("Green", 3.0, 4.0, 5.0));
    
    cout << "Shape Information:" << endl;
    for (const auto& shape : shapes) {
        shape->display();
        cout << "Area: " << shape->calculateArea() << endl;
        cout << "Perimeter: " << shape->calculatePerimeter() << endl;
        cout << "---" << endl;
    }
    
    // Calculate total area
    double totalArea = 0;
    for (const auto& shape : shapes) {
        totalArea += shape->calculateArea();
    }
    cout << "Total area of all shapes: " << totalArea << endl;
    
    return 0;
}
```

---

## Inheritance and Polymorphism

### Single Inheritance
```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

// Base class
class Vehicle {
protected:
    string brand;
    string model;
    int year;
    double price;
    
public:
    Vehicle(const string& b, const string& m, int y, double p)
        : brand(b), model(m), year(y), price(p) {}
    
    virtual void displayInfo() const {
        cout << "Vehicle: " << brand << " " << model 
             << " (" << year << "), Price: $" << price << endl;
    }
    
    virtual void startEngine() const {
        cout << "Starting " << brand << " " << model << " engine..." << endl;
    }
    
    virtual void stopEngine() const {
        cout << "Stopping " << brand << " " << model << " engine..." << endl;
    }
    
    virtual ~Vehicle() = default;
    
    // Getters
    string getBrand() const { return brand; }
    string getModel() const { return model; }
    int getYear() const { return year; }
    double getPrice() const { return price; }
};

// Derived class
class Car : public Vehicle {
private:
    int doors;
    string fuelType;
    bool isElectric;
    
public:
    Car(const string& b, const string& m, int y, double p, int d, const string& fuel, bool electric = false)
        : Vehicle(b, m, y, p), doors(d), fuelType(fuel), isElectric(electric) {}
    
    void displayInfo() const override {
        cout << "Car: " << brand << " " << model << " (" << year << ")" << endl;
        cout << "  Doors: " << doors << ", Fuel: " << fuelType 
             << ", Electric: " << (isElectric ? "Yes" : "No") << endl;
        cout << "  Price: $" << price << endl;
    }
    
    void startEngine() const override {
        if (isElectric) {
            cout << "Starting electric motor for " << brand << " " << model << "..." << endl;
        } else {
            cout << "Starting internal combustion engine for " << brand << " " << model << "..." << endl;
        }
    }
    
    void openTrunk() const {
        cout << "Opening trunk of " << brand << " " << model << endl;
    }
    
    // Additional car-specific method
    void honk() const {
        cout << brand << " " << model << " goes beep beep!" << endl;
    }
};

// Another derived class
class Motorcycle : public Vehicle {
private:
    int engineCC;
    bool hasSidecar;
    
public:
    Motorcycle(const string& b, const string& m, int y, double p, int cc, bool sidecar = false)
        : Vehicle(b, m, y, p), engineCC(cc), hasSidecar(sidecar) {}
    
    void displayInfo() const override {
        cout << "Motorcycle: " << brand << " " << model << " (" << year << ")" << endl;
        cout << "  Engine: " << engineCC << "cc, Sidecar: " << (hasSidecar ? "Yes" : "No") << endl;
        cout << "  Price: $" << price << endl;
    }
    
    void wheelie() const {
        cout << brand << " " << model << " performs a wheelie!" << endl;
    }
    
    void startEngine() const override {
        cout << "Revving up the " << engineCC << "cc engine of " << brand << " " << model << "..." << endl;
    }
};

int main() {
    cout << "Single Inheritance Example:" << endl;
    
    Car car("Toyota", "Camry", 2023, 25000, 4, "Gasoline");
    Motorcycle motorcycle("Harley-Davidson", "Street 750", 2022, 8000, 750);
    
    // Base class method calls
    car.displayInfo();
    car.startEngine();
    cout << endl;
    
    motorcycle.displayInfo();
    motorcycle.startEngine();
    cout << endl;
    
    // Derived class specific methods
    car.openTrunk();
    car.honk();
    cout << endl;
    
    motorcycle.wheelie();
    cout << endl;
    
    // Polymorphism with base class pointers
    Vehicle* vehicles[] = {&car, &motorcycle};
    
    cout << "Using polymorphism:" << endl;
    for (int i = 0; i < 2; i++) {
        vehicles[i]->displayInfo();
        vehicles[i]->startEngine();
        cout << endl;
    }
    
    return 0;
}
```

### Polymorphism
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
#include <algorithm>
using namespace std;

// Base class demonstrating polymorphism
class Animal {
protected:
    string name;
    int age;
    
public:
    Animal(const string& n, int a) : name(n), age(a) {}
    
    // Virtual functions for runtime polymorphism
    virtual void makeSound() const {
        cout << name << " makes a sound." << endl;
    }
    
    virtual void move() const {
        cout << name << " moves." << endl;
    }
    
    virtual void eat() const {
        cout << name << " eats." << endl;
    }
    
    virtual void displayInfo() const {
        cout << "Animal: " << name << ", Age: " << age << endl;
    }
    
    virtual ~Animal() = default;
};

// Derived classes
class Dog : public Animal {
private:
    string breed;
    
public:
    Dog(const string& n, int a, const string& b) : Animal(n, a), breed(b) {}
    
    void makeSound() const override {
        cout << name << " the dog barks: Woof! Woof!" << endl;
    }
    
    void move() const override {
        cout << name << " the dog runs on four legs." << endl;
    }
    
    void eat() const override {
        cout << name << " the dog eats dog food." << endl;
    }
    
    void fetch() const {
        cout << name << " fetches the ball!" << endl;
    }
    
    void displayInfo() const override {
        cout << "Dog: " << name << ", Age: " << age << ", Breed: " << breed << endl;
    }
};

class Cat : public Animal {
private:
    bool isIndoor;
    
public:
    Cat(const string& n, int a, bool indoor) : Animal(n, a), isIndoor(indoor) {}
    
    void makeSound() const override {
        cout << name << " the cat meows: Meow!" << endl;
    }
    
    void move() const override {
        cout << name << " the cat prowls silently." << endl;
    }
    
    void eat() const override {
        cout << name << " the cat eats cat food." << endl;
    }
    
    void climb() const {
        cout << name << " climbs the tree!" << endl;
    }
    
    void displayInfo() const override {
        cout << "Cat: " << name << ", Age: " << age 
             << ", Indoor: " << (isIndoor ? "Yes" : "No") << endl;
    }
};

class Bird : public Animal {
private:
    string species;
    bool canFly;
    
public:
    Bird(const string& n, int a, const string& s, bool fly) 
        : Animal(n, a), species(s), canFly(fly) {}
    
    void makeSound() const override {
        cout << name << " the bird chirps: Chirp! Chirp!" << endl;
    }
    
    void move() const override {
        if (canFly) {
            cout << name << " the bird flies through the air." << endl;
        } else {
            cout << name << " the bird walks." << endl;
        }
    }
    
    void eat() const override {
        cout << name << " the bird eats seeds." << endl;
    }
    
    void fly() const {
        if (canFly) {
            cout << name << " soars in the sky!" << endl;
        } else {
            cout << name << " cannot fly." << endl;
        }
    }
    
    void displayInfo() const override {
        cout << "Bird: " << name << ", Age: " << age 
             << ", Species: " << species 
             << ", Can Fly: " << (canFly ? "Yes" : "No") << endl;
    }
};

// Function that demonstrates polymorphism
void animalActivity(const Animal& animal) {
    animal.displayInfo();
    animal.makeSound();
    animal.move();
    animal.eat();
    cout << "---" << endl;
}

int main() {
    // Create animals using smart pointers
    vector<unique_ptr<Animal>> animals;
    
    animals.push_back(make_unique<Dog>("Buddy", 3, "Golden Retriever"));
    animals.push_back(make_unique<Cat>("Whiskers", 2, true));
    animals.push_back(make_unique<Bird>("Tweety", 1, "Canary", true));
    animals.push_back(make_unique<Dog>("Rex", 5, "German Shepherd"));
    animals.push_back(make_unique<Cat>("Fluffy", 4, false));
    
    cout << "All animals performing activities:" << endl;
    for (const auto& animal : animals) {
        animalActivity(*animal);
    }
    
    // Demonstrating specific behaviors
    cout << "Specific behaviors:" << endl;
    for (const auto& animal : animals) {
        // Downcasting to access specific methods (with safety checks)
        if (Dog* dog = dynamic_cast<Dog*>(animal.get())) {
            dog->fetch();
        } else if (Cat* cat = dynamic_cast<Cat*>(animal.get())) {
            cat->climb();
        } else if (Bird* bird = dynamic_cast<Bird*>(animal.get())) {
            bird->fly();
        }
    }
    
    return 0;
}
```

### Multiple Inheritance
```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

// First base class
class Flyable {
protected:
    double maxAltitude;
    double maxSpeed;
    
public:
    Flyable(double altitude, double speed) : maxAltitude(altitude), maxSpeed(speed) {}
    
    virtual void takeOff() const {
        cout << "Taking off..." << endl;
    }
    
    virtual void land() const {
        cout << "Landing..." << endl;
    }
    
    virtual void fly() const {
        cout << "Flying at up to " << maxSpeed << " mph and " << maxAltitude << " feet" << endl;
    }
    
    virtual ~Flyable() = default;
};

// Second base class
class Swimmable {
protected:
    double maxDepth;
    double swimSpeed;
    
public:
    Swimmable(double depth, double speed) : maxDepth(depth), swimSpeed(speed) {}
    
    virtual void dive() const {
        cout << "Diving underwater..." << endl;
    }
    
    virtual void surface() const {
        cout << "Surfacing..." << endl;
    }
    
    virtual void swim() const {
        cout << "Swimming at " << swimSpeed << " mph up to " << maxDepth << " feet deep" << endl;
    }
    
    virtual ~Swimmable() = default;
};

// Third base class
class LandVehicle {
protected:
    double groundSpeed;
    int wheels;
    
public:
    LandVehicle(double speed, int w) : groundSpeed(speed), wheels(w) {}
    
    virtual void drive() const {
        cout << "Driving on " << wheels << " wheels at " << groundSpeed << " mph" << endl;
    }
    
    virtual void brake() const {
        cout << "Applying brakes..." << endl;
    }
    
    virtual ~LandVehicle() = default;
};

// Derived class using multiple inheritance
class AmphibiousVehicle : public Flyable, public Swimmable, public LandVehicle {
private:
    string name;
    
public:
    AmphibiousVehicle(const string& n, double alt, double fSpeed, 
                     double depth, double sSpeed, double gSpeed, int w)
        : Flyable(alt, fSpeed), Swimmable(depth, sSpeed), 
          LandVehicle(gSpeed, w), name(n) {}
    
    // Override methods to provide amphibious-specific behavior
    void takeOff() const override {
        cout << name << " taking off from water surface..." << endl;
    }
    
    void land() const override {
        cout << name << " landing on water surface..." << endl;
    }
    
    void fly() const override {
        cout << name << " flying: ";
        Flyable::fly();
    }
    
    void dive() const override {
        cout << name << " diving underwater..." << endl;
    }
    
    void surface() const override {
        cout << name << " surfacing from underwater..." << endl;
    }
    
    void swim() const override {
        cout << name << " swimming: ";
        Swimmable::swim();
    }
    
    void drive() const override {
        cout << name << " driving: ";
        LandVehicle::drive();
    }
    
    // New method combining all capabilities
    void performAmphibiousSequence() const {
        cout << "\n--- " << name << " Amphibious Sequence ---" << endl;
        
        // Drive on land
        drive();
        
        // Go to water
        brake();
        cout << name << " entering water..." << endl;
        
        // Swim
        swim();
        
        // Dive
        dive();
        cout << name << " exploring underwater..." << endl;
        surface();
        
        // Take off
        takeOff();
        fly();
        
        // Land
        land();
        cout << name << " returning to shore." << endl;
        cout << "--- End of sequence ---\n" << endl;
    }
    
    void displayCapabilities() const {
        cout << name << " Capabilities:" << endl;
        cout << "  Flight: Up to " << maxAltitude << " ft at " << maxSpeed << " mph" << endl;
        cout << "  Swimming: Up to " << maxDepth << " ft at " << swimSpeed << " mph" << endl;
        cout << "  Driving: " << groundSpeed << " mph on " << wheels << " wheels" << endl;
    }
};

int main() {
    cout << "Multiple Inheritance Example:" << endl;
    
    AmphibiousVehicle duckBoat("Duck Boat", 1000, 120, 30, 5, 30, 6);
    
    duckBoat.displayCapabilities();
    cout << endl;
    
    // Access methods from all inherited classes
    duckBoat.drive();
    duckBoat.swim();
    duckBoat.fly();
    cout << endl;
    
    // Perform the complete sequence
    duckBoat.performAmphibiousSequence();
    
    // Demonstrate accessing specific base class methods
    cout << "Accessing specific base class methods:" << endl;
    duckBoat.Flyable::takeOff();
    duckBoat.Swimmable::dive();
    duckBoat.LandVehicle::brake();
    
    return 0;
}
```

---

## Advanced Memory Management (Heap vs. Stack, Smart Pointers)

### Smart Pointers
```cpp
#include <iostream>
#include <memory>
#include <vector>
#include <string>
using namespace std;

class Resource {
private:
    string name;
    int* data;
    size_t size;
    
public:
    // Constructor
    Resource(const string& n, size_t s) : name(n), size(s) {
        data = new int[size];
        for (size_t i = 0; i < size; i++) {
            data[i] = i + 1;
        }
        cout << "Resource '" << name << "' allocated with " << size << " integers" << endl;
    }
    
    // Destructor
    ~Resource() {
        delete[] data;
        cout << "Resource '" << name << "' deallocated" << endl;
    }
    
    // Copy constructor
    Resource(const Resource& other) : name(other.name + "_copy"), size(other.size) {
        data = new int[size];
        for (size_t i = 0; i < size; i++) {
            data[i] = other.data[i];
        }
        cout << "Resource '" << name << "' copied from '" << other.name << "'" << endl;
    }
    
    // Assignment operator
    Resource& operator=(const Resource& other) {
        if (this != &other) {
            delete[] data;  // Clean up existing resource
            
            name = other.name + "_assigned";
            size = other.size;
            data = new int[size];
            for (size_t i = 0; i < size; i++) {
                data[i] = other.data[i];
            }
            
            cout << "Resource '" << name << "' assigned from '" << other.name << "'" << endl;
        }
        return *this;
    }
    
    // Move constructor
    Resource(Resource&& other) noexcept : name(move(other.name)), size(other.size), data(other.data) {
        other.data = nullptr;
        other.size = 0;
        cout << "Resource moved to '" << name << "'" << endl;
    }
    
    // Move assignment operator
    Resource& operator=(Resource&& other) noexcept {
        if (this != &other) {
            delete[] data;  // Clean up existing resource
            
            name = move(other.name);
            size = other.size;
            data = other.data;
            
            other.data = nullptr;
            other.size = 0;
            
            cout << "Resource moved to '" << name << "'" << endl;
        }
        return *this;
    }
    
    void display() const {
        cout << "Resource '" << name << "': ";
        for (size_t i = 0; i < min(size, (size_t)5); i++) {  // Show first 5 elements
            cout << data[i] << " ";
        }
        if (size > 5) cout << "...";
        cout << endl;
    }
    
    string getName() const { return name; }
};

void demonstrateUniquePtr() {
    cout << "\n=== Unique Pointer Demo ===" << endl;
    
    // Creating unique_ptr
    unique_ptr<Resource> ptr1 = make_unique<Resource>("Resource1", 10);
    ptr1->display();
    
    // Transfer ownership using move
    unique_ptr<Resource> ptr2 = move(ptr1);
    // ptr1 is now null
    cout << "ptr1 is " << (ptr1 ? "valid" : "null") << endl;
    cout << "ptr2 is " << (ptr2 ? "valid" : "null") << endl;
    
    ptr2->display();
    
    // Array with unique_ptr
    unique_ptr<int[]> arrayPtr = make_unique<int[]>(5);
    for (int i = 0; i < 5; i++) {
        arrayPtr[i] = (i + 1) * 10;
    }
    
    cout << "Array: ";
    for (int i = 0; i < 5; i++) {
        cout << arrayPtr[i] << " ";
    }
    cout << endl;
    
    // unique_ptr automatically cleans up when going out of scope
}

void demonstrateSharedPtr() {
    cout << "\n=== Shared Pointer Demo ===" << endl;
    
    // Creating shared_ptr
    shared_ptr<Resource> ptr1 = make_shared<Resource>("SharedResource", 5);
    cout << "Reference count: " << ptr1.use_count() << endl;
    
    {
        // Creating another shared_ptr pointing to the same object
        shared_ptr<Resource> ptr2 = ptr1;
        cout << "Reference count: " << ptr1.use_count() << endl;
        cout << "Reference count (ptr2): " << ptr2.use_count() << endl;
        
        ptr2->display();
        
        // Creating a third shared_ptr
        shared_ptr<Resource> ptr3 = ptr1;
        cout << "Reference count: " << ptr1.use_count() << endl;
    }
    
    // ptr2 and ptr3 went out of scope, reference count decreased
    cout << "Reference count after scope: " << ptr1.use_count() << endl;
    ptr1->display();
    
    // Weak pointer to break circular references
    weak_ptr<Resource> weakPtr = ptr1;
    cout << "Weak pointer created, shared count: " << weakPtr.use_count() << endl;
    
    if (auto lockedPtr = weakPtr.lock()) {  // Safely access the resource
        cout << "Successfully locked weak pointer" << endl;
        lockedPtr->display();
    }
    
    // Reset the shared pointer
    ptr1.reset();
    cout << "ptr1 reset, expired: " << weakPtr.expired() << endl;
}

void demonstrateCustomDeleter() {
    cout << "\n=== Custom Deleter Demo ===" << endl;
    
    // Custom deleter function
    auto customDeleter = [](Resource* res) {
        cout << "Custom deleter called for: " << res->getName() << endl;
        delete res;
    };
    
    unique_ptr<Resource, decltype(customDeleter)> ptr(
        new Resource("CustomDeleted", 3), 
        customDeleter
    );
    
    ptr->display();
    // Custom deleter will be called automatically
}

int main() {
    cout << "Advanced Memory Management with Smart Pointers" << endl;
    
    demonstrateUniquePtr();
    demonstrateSharedPtr();
    demonstrateCustomDeleter();
    
    cout << "\nAll smart pointers cleaned up automatically!" << endl;
    
    return 0;
}
```

### RAII (Resource Acquisition Is Initialization)
```cpp
#include <iostream>
#include <fstream>
#include <mutex>
#include <thread>
#include <chrono>
using namespace std;

// RAII class for file handling
class FileManager {
private:
    string filename;
    ofstream file;
    bool isOpen;
    
public:
    FileManager(const string& fname) : filename(fname), isOpen(false) {
        file.open(filename);
        if (file.is_open()) {
            isOpen = true;
            cout << "File '" << filename << "' opened successfully" << endl;
        } else {
            cout << "Failed to open file '" << filename << "'" << endl;
        }
    }
    
    // Destructor automatically closes file
    ~FileManager() {
        if (isOpen) {
            file.close();
            cout << "File '" << filename << "' closed automatically" << endl;
        }
    }
    
    // Non-copyable to prevent resource duplication
    FileManager(const FileManager&) = delete;
    FileManager& operator=(const FileManager&) = delete;
    
    // Move constructor
    FileManager(FileManager&& other) noexcept 
        : filename(move(other.filename)), file(move(other.file)), isOpen(other.isOpen) {
        other.isOpen = false;
        cout << "File manager moved" << endl;
    }
    
    // Write to file
    bool write(const string& data) {
        if (isOpen) {
            file << data << endl;
            return true;
        }
        return false;
    }
    
    bool isFileOpen() const { return isOpen; }
};

// RAII class for thread synchronization
class ThreadLock {
private:
    mutex& mtx;
    bool locked;
    
public:
    ThreadLock(mutex& m) : mtx(m), locked(true) {
        mtx.lock();
        cout << "Mutex locked" << endl;
    }
    
    ~ThreadLock() {
        if (locked) {
            mtx.unlock();
            cout << "Mutex unlocked" << endl;
        }
    }
    
    // Prevent copying
    ThreadLock(const ThreadLock&) = delete;
    ThreadLock& operator=(const ThreadLock&) = delete;
    
    // Move constructor
    ThreadLock(ThreadLock&& other) noexcept : mtx(other.mtx), locked(other.locked) {
        other.locked = false;
    }
    
    void unlock() {
        if (locked) {
            mtx.unlock();
            locked = false;
            cout << "Mutex unlocked early" << endl;
        }
    }
    
    void lockAgain() {
        if (!locked) {
            mtx.lock();
            locked = true;
            cout << "Mutex locked again" << endl;
        }
    }
};

// RAII class for database connection simulation
class DatabaseConnection {
private:
    string connectionString;
    bool isConnected;
    
public:
    DatabaseConnection(const string& connStr) : connectionString(connStr), isConnected(false) {
        // Simulate connection attempt
        cout << "Attempting to connect to: " << connectionString << endl;
        isConnected = true;  // Simulate successful connection
        cout << "Database connected successfully" << endl;
    }
    
    ~DatabaseConnection() {
        if (isConnected) {
            cout << "Database connection closed" << endl;
        }
    }
    
    // Prevent copying
    DatabaseConnection(const DatabaseConnection&) = delete;
    DatabaseConnection& operator=(const DatabaseConnection&) = delete;
    
    // Move constructor
    DatabaseConnection(DatabaseConnection&& other) noexcept 
        : connectionString(move(other.connectionString)), isConnected(other.isConnected) {
        other.isConnected = false;
    }
    
    void executeQuery(const string& query) {
        if (isConnected) {
            cout << "Executing query: " << query << endl;
        } else {
            cout << "Cannot execute query - not connected" << endl;
        }
    }
    
    bool connected() const { return isConnected; }
};

void demonstrateRAII() {
    cout << "=== RAII Demonstration ===" << endl;
    
    // File RAII
    {
        FileManager fm("example.txt");
        if (fm.isFileOpen()) {
            fm.write("Hello from RAII!");
            fm.write("Resource automatically managed");
        }
    }  // File automatically closed here
    
    // Mutex RAII
    mutex mtx;
    {
        ThreadLock lock(mtx);
        cout << "Critical section accessed safely" << endl;
        // Mutex automatically unlocked when lock goes out of scope
    }
    
    // Database RAII
    {
        DatabaseConnection db("localhost:5432/mydb");
        db.executeQuery("SELECT * FROM users;");
        // Connection automatically closed
    }
    
    cout << "All resources properly managed with RAII!" << endl;
}

void demonstrateExceptionSafety() {
    cout << "\n=== Exception Safety with RAII ===" << endl;
    
    try {
        FileManager fm("exception_test.txt");
        fm.write("Before exception");
        
        // Simulate an exception
        throw runtime_error("Simulated exception occurred");
        
        // This line won't be reached, but FileManager still gets cleaned up
        fm.write("After exception - this won't execute");
    } catch (const exception& e) {
        cout << "Caught exception: " << e.what() << endl;
        cout << "Notice that file was still properly closed due to RAII!" << endl;
    }
    
    // Demonstrate scoped resource management
    cout << "\nManual resource management vs RAII:" << endl;
    
    // Without RAII (bad practice):
    cout << "Without RAII - potential resource leak:" << endl;
    ofstream* badFile = new ofstream("bad_example.txt");
    *badFile << "This might not get cleaned up properly";
    // Forgot to close/delete - resource leak!
    
    // With RAII (good practice):
    cout << "With RAII - guaranteed cleanup:" << endl;
    {
        FileManager goodFile("good_example.txt");
        goodFile.write("This will definitely get cleaned up");
    }  // Automatic cleanup occurs here
}

int main() {
    demonstrateRAII();
    demonstrateExceptionSafety();
    
    return 0;
}
```

### Memory Pools and Custom Allocators
```cpp
#include <iostream>
#include <vector>
#include <memory>
#include <list>
#include <chrono>
using namespace std;

// Simple memory pool implementation
template<typename T, size_t PoolSize = 100>
class MemoryPool {
private:
    union Block {
        T object;
        Block* next;
        
        Block() : next(nullptr) {}
        ~Block() {}  // Must be trivial for placement new
    };
    
    Block* freeList;
    vector<Block> pool;
    size_t allocatedCount;
    
public:
    MemoryPool() : freeList(nullptr), pool(PoolSize), allocatedCount(0) {
        // Initialize free list
        for (size_t i = 0; i < PoolSize - 1; ++i) {
            pool[i].next = &pool[i + 1];
        }
        pool[PoolSize - 1].next = nullptr;
        freeList = &pool[0];
    }
    
    ~MemoryPool() {
        // Destroy all allocated objects
        reset();
    }
    
    // Allocate an object from the pool
    T* allocate() {
        if (!freeList) {
            throw bad_alloc();
        }
        
        Block* block = freeList;
        freeList = block->next;
        ++allocatedCount;
        
        // Use placement new to construct object in pre-allocated memory
        return new(&block->object) T();
    }
    
    // Deallocate an object back to the pool
    void deallocate(T* ptr) {
        if (!ptr) return;
        
        // Call destructor
        ptr->~T();
        
        // Find corresponding block
        Block* block = reinterpret_cast<Block*>(ptr);
        
        // Add back to free list
        block->next = freeList;
        freeList = block;
        --allocatedCount;
    }
    
    // Reset the entire pool
    void reset() {
        // Destroy all allocated objects
        // This is a simplified version - in practice, you'd need to track allocated objects
        pool.clear();
        pool.resize(PoolSize);
        
        // Rebuild free list
        for (size_t i = 0; i < PoolSize - 1; ++i) {
            pool[i].next = &pool[i + 1];
        }
        pool[PoolSize - 1].next = nullptr;
        freeList = &pool[0];
        allocatedCount = 0;
    }
    
    size_t getAllocatedCount() const { return allocatedCount; }
    size_t getFreeCount() const { return PoolSize - allocatedCount; }
};

// Class to demonstrate pool usage
class ExpensiveObject {
private:
    int id;
    vector<int> data;  // Simulate expensive initialization
    
public:
    ExpensiveObject(int objId = 0) : id(objId), data(1000, objId) {
        cout << "ExpensiveObject " << id << " created" << endl;
    }
    
    ~ExpensiveObject() {
        cout << "ExpensiveObject " << id << " destroyed" << endl;
    }
    
    int getId() const { return id; }
    size_t getDataSize() const { return data.size(); }
    
    void doWork() {
        // Simulate some work
        int sum = 0;
        for (int val : data) {
            sum += val;
        }
        cout << "Object " << id << " processed " << data.size() << " elements, sum: " << sum << endl;
    }
};

// Custom allocator example
template<typename T>
class TrackingAllocator {
public:
    using value_type = T;
    
    // Static counters for tracking allocations
    static size_t allocation_count;
    static size_t deallocation_count;
    static size_t bytes_allocated;
    static size_t bytes_deallocated;
    
    TrackingAllocator() = default;
    
    template<typename U>
    TrackingAllocator(const TrackingAllocator<U>&) {}
    
    T* allocate(size_t n) {
        T* ptr = static_cast<T*>(::operator new(n * sizeof(T)));
        allocation_count++;
        bytes_allocated += n * sizeof(T);
        cout << "Allocated " << n << " objects of size " << sizeof(T) 
             << ", total allocated: " << bytes_allocated << " bytes" << endl;
        return ptr;
    }
    
    void deallocate(T* ptr, size_t n) {
        deallocation_count++;
        bytes_deallocated += n * sizeof(T);
        cout << "Deallocated " << n << " objects of size " << sizeof(T) 
             << ", total deallocated: " << bytes_deallocated << " bytes" << endl;
        ::operator delete(ptr);
    }
    
    template<typename U>
    bool operator==(const TrackingAllocator<U>&) const { return true; }
    
    template<typename U>
    bool operator!=(const TrackingAllocator<U>&) const { return false; }
};

// Initialize static members
template<typename T>
size_t TrackingAllocator<T>::allocation_count = 0;

template<typename T>
size_t TrackingAllocator<T>::deallocation_count = 0;

template<typename T>
size_t TrackingAllocator<T>::bytes_allocated = 0;

template<typename T>
size_t TrackingAllocator<T>::bytes_deallocated = 0;

void demonstrateMemoryPool() {
    cout << "=== Memory Pool Demonstration ===" << endl;
    
    MemoryPool<ExpensiveObject, 10> pool;
    
    cout << "Initial pool state - Allocated: " << pool.getAllocatedCount() 
         << ", Free: " << pool.getFreeCount() << endl;
    
    // Allocate objects from pool
    vector<ExpensiveObject*> objects;
    for (int i = 0; i < 5; ++i) {
        ExpensiveObject* obj = pool.allocate();
        obj->doWork();
        objects.push_back(obj);
        
        cout << "After allocation " << (i + 1) << " - Allocated: " << pool.getAllocatedCount() 
             << ", Free: " << pool.getFreeCount() << endl;
    }
    
    // Deallocate some objects
    cout << "\nDeallocating objects..." << endl;
    for (int i = 0; i < 2; ++i) {
        pool.deallocate(objects[i]);
        objects[i] = nullptr;
        
        cout << "After deallocation " << (i + 1) << " - Allocated: " << pool.getAllocatedCount() 
             << ", Free: " << pool.getFreeCount() << endl;
    }
    
    // Clean up remaining objects
    for (size_t i = 2; i < objects.size(); ++i) {
        if (objects[i]) {
            pool.deallocate(objects[i]);
        }
    }
}

void demonstrateCustomAllocator() {
    cout << "\n=== Custom Allocator Demonstration ===" << endl;
    
    // Reset counters
    TrackingAllocator<int>::allocation_count = 0;
    TrackingAllocator<int>::deallocation_count = 0;
    TrackingAllocator<int>::bytes_allocated = 0;
    TrackingAllocator<int>::bytes_deallocated = 0;
    
    {
        // Use custom allocator with vector
        vector<int, TrackingAllocator<int>> trackedVec;
        
        // Add elements
        for (int i = 0; i < 100; ++i) {
            trackedVec.push_back(i);
        }
        
        cout << "Vector size: " << trackedVec.size() << endl;
    }
    
    cout << "Final stats - Allocations: " << TrackingAllocator<int>::allocation_count
         << ", Deallocations: " << TrackingAllocator<int>::deallocation_count << endl;
    cout << "Net allocated: " << (TrackingAllocator<int>::bytes_allocated - 
                                  TrackingAllocator<int>::bytes_deallocated) << " bytes" << endl;
}

void performanceComparison() {
    cout << "\n=== Performance Comparison ===" << endl;
    
    const int numObjects = 1000;
    
    // Time regular allocation
    auto start = chrono::high_resolution_clock::now();
    vector<unique_ptr<ExpensiveObject>> regularObjects;
    for (int i = 0; i < numObjects; ++i) {
        regularObjects.push_back(make_unique<ExpensiveObject>(i));
    }
    auto end = chrono::high_resolution_clock::now();
    auto regularTime = chrono::duration_cast<chrono::microseconds>(end - start);
    
    cout << "Regular allocation time: " << regularTime.count() << " microseconds" << endl;
    
    // Time pool allocation
    MemoryPool<ExpensiveObject, numObjects> pool;
    start = chrono::high_resolution_clock::now();
    vector<ExpensiveObject*> poolObjects;
    for (int i = 0; i < numObjects; ++i) {
        poolObjects.push_back(pool.allocate());
    }
    end = chrono::high_resolution_clock::now();
    auto poolTime = chrono::duration_cast<chrono::microseconds>(end - start);
    
    cout << "Pool allocation time: " << poolTime.count() << " microseconds" << endl;
    
    // Clean up pool objects
    for (auto obj : poolObjects) {
        pool.deallocate(obj);
    }
    
    cout << "Performance ratio (regular/pool): " << (double)regularTime.count() / poolTime.count() << endl;
}

int main() {
    demonstrateMemoryPool();
    demonstrateCustomAllocator();
    performanceComparison();
    
    return 0;
}
```

---

## Conclusion

This comprehensive guide covers C++ programming from basic concepts to advanced OOP principles and memory management. Each section builds upon the previous one, providing a solid foundation for understanding C++ programming.

Key concepts covered:
- Basic printing and variable operations
- Control flow (if/else, switch)
- Loops (for, while, do-while)
- Tables (arrays)
- Functions (pass-by-value vs. pass-by-reference)
- Pointers and references
- Vectors (dynamic arrays)
- Maps (associative containers)
- Classes and objects (the basics)
- Constructors and destructors
- The `this` pointer
- Object-oriented programming principles (encapsulation, abstraction)
- Inheritance and polymorphism
- Advanced memory management (heap vs. stack, smart pointers)

Each example includes practical code that demonstrates the concepts in action, allowing for hands-on learning and experimentation.
