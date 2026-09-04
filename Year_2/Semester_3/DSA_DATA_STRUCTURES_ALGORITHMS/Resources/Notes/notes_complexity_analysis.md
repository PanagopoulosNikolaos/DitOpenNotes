# Algorithm Complexity Analysis in C++

## Introduction

The complexity of an algorithm is a measure that shows how much time or memory is required to execute the algorithm relative to the size of the input. Complexity analysis is critical for choosing the appropriate algorithm and optimizing the code.

## Big O Notation

Big O notation (O big) is used to describe the upper bound complexity of an algorithm. It represents the worst-case execution.

### Basic Complexity Categories

1. **O(1) - Constant Complexity**
   - The execution time does not depend on the size of the input
   - Example: Accessing an array element by index

2. **O(log n) - Logarithmic Complexity**
   - The execution time increases logarithmically with the size of the input
   - Example: Binary search

3. **O(n) - Linear Complexity**
   - The execution time increases linearly with the size of the input
   - Example: Linear search

4. **O(n log n) - Linearithmic Complexity**
   - Example: Merge Sort

5. **O(n²) - Quadratic Complexity**
   - The execution time increases proportionally to the square of the input size
   - Example: Bubble Sort

6. **O(2^n) - Exponential Complexity**
   - The execution time doubles with each addition of an element to the input
   - Example: Recursive Fibonacci number calculation

7. **O(n!) - Factorial Complexity**
   - The execution time increases factorially with the size of the input
   - Example: Traveling Salesman Problem

## Step-by-Step Complexity Analysis

### Step 1: Identifying Basic Operations

We need to determine which operations are considered "basic" and are counted:
- Value assignment to a variable
- Mathematical operations
- Comparisons
- Accessing array elements
- Function calls

### Step 2: Counting Iterations

We need to count how many times each basic operation is executed relative to the size of the input.

### Step 3: Simplification

We ignore constant factors and lower-order terms, keeping only the highest-order term.

## Complexity Analysis Examples

### Example 1: Constant Complexity O(1)

```cpp
#include <iostream>
using namespace std;

// Function with constant complexity
int getFirstElement(int arr[], int n) {
    // Accessing an array element by index
    // The execution time is always the same
    return arr[0];
}

int main() {
    int arr[] = {10, 20, 30, 40, 50};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    cout << "First element: " << getFirstElement(arr, n) << endl;
    return 0;
}
```

**Analysis:**
- The `getFirstElement` function performs only one operation (accessing an array element)
- The execution time does not depend on n
- **Complexity: O(1)**

### Example 2: Linear Complexity O(n)

```cpp
#include <iostream>
using namespace std;

// Function with linear complexity
int sumArray(int arr[], int n) {
    int sum = 0;                    // 1 operation
    
    for (int i = 0; i < n; i++) {   // Loop n times
        sum += arr[i];              // 1 operation per iteration
    }
    
    return sum;                     // 1 operation
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    cout << "Sum: " << sumArray(arr, n) << endl;
    return 0;
}
```

**Analysis:**
- Initialization `sum = 0`: 1 operation
- `for` loop: executes n times
  - Each iteration: 1 operation (`sum += arr[i]`)
  - Total: n operations
- Return result: 1 operation
- **Total operations: 1 + n + 1 = n + 2**
- **Complexity: O(n)** (ignoring constant terms)

### Example 3: Quadratic Complexity O(n²)

```cpp
#include <iostream>
using namespace std;

// Function with quadratic complexity
void printPairs(int arr[], int n) {
    for (int i = 0; i < n; i++) {           // Outer loop: n iterations
        for (int j = 0; j < n; j++) {       // Inner loop: n iterations
            cout << "(" << arr[i] << ", " << arr[j] << ") ";  // 1 operation per iteration
        }
        cout << endl;
    }
}

int main() {
    int arr[] = {1, 2, 3};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    cout << "All pairs:" << endl;
    printPairs(arr, n);
    return 0;
}
```

**Analysis:**
- Outer loop: executes n times
- For each iteration of the outer loop, the inner loop executes n times
- Total: n × n = n² iterations
- **Complexity: O(n²)**

### Example 4: Logarithmic Complexity O(log n)

```cpp
#include <iostream>
using namespace std;

// Binary search with logarithmic complexity
int binarySearch(int arr[], int n, int target) {
    int left = 0;                   // 1 operation
    int right = n - 1;              // 1 operation
    
    while (left <= right) {         // Loop until element is found
        int mid = left + (right - left) / 2;  // 1 operation
        
        if (arr[mid] == target) {   // 1 operation
            return mid;             // Found
        }
        
        if (arr[mid] < target) {    // 1 operation
            left = mid + 1;         // 1 operation
        } else {
            right = mid - 1;        // 1 operation
        }
    }
    
    return -1;  // Not found
}

int main() {
    int arr[] = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19};
    int n = sizeof(arr) / sizeof(arr[0]);
    int target = 7;
    
    int result = binarySearch(arr, n, target);
    
    if (result != -1) {
        cout << "Element " << target << " found at position " << result << endl;
    } else {
        cout << "Element " << target << " not found" << endl;
    }
    
    return 0;
}
```

**Analysis:**
- In each iteration, the search range is halved
- Initial range: n
- After 1 iteration: n/2
- After 2 iterations: n/4
- ...
- After k iterations: n/2^k
- The search terminates when n/2^k = 1, i.e., k = log₂(n)
- **Complexity: O(log n)**

### Example 5: Exponential Complexity O(2^n)

```cpp
#include <iostream>
using namespace std;

// Recursive Fibonacci number calculation
int fibonacci(int n) {
    if (n <= 1) {                   // 1 operation
        return n;                   // 1 operation
    }
    
    return fibonacci(n - 1) + fibonacci(n - 2);  // 2 recursive calls
}

int main() {
    int n = 6;
    
    cout << "Fibonacci(" << n << ") = " << fibonacci(n) << endl;
    return 0;
}
```

**Analysis:**
- Each call to `fibonacci` creates 2 new recursive calls
- The recursion tree has depth n
- The number of calls increases exponentially
- **Complexity: O(2^n)**

### Example 6: Linearithmic Complexity O(n log n)

```cpp
#include <iostream>
#include <vector>
using namespace std;

// Merge Sort
void merge(vector<int>& arr, int left, int mid, int right) {
    int n1 = mid - left + 1;        // 1 operation
    int n2 = right - mid;           // 1 operation
    
    vector<int> L(n1), R(n2);       // Create temporary arrays
    
    // Copy data to temporary arrays
    for (int i = 0; i < n1; i++)    // n1 iterations
        L[i] = arr[left + i];
    for (int j = 0; j < n2; j++)    // n2 iterations
        R[j] = arr[mid + 1 + j];
    
    // Merge the temporary arrays
    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2) {      // Until arrays are exhausted
        if (L[i] <= R[j]) {         // 1 operation
            arr[k] = L[i];          // 1 operation
            i++;                    // 1 operation
        } else {
            arr[k] = R[j];          // 1 operation
            j++;                    // 1 operation
        }
        k++;                        // 1 operation
    }
    
    // Copy remaining elements
    while (i < n1) {                // Until L is exhausted
        arr[k] = L[i];              // 1 operation
        i++;                        // 1 operation
        k++;                        // 1 operation
    }
    
    while (j < n2) {                // Until R is exhausted
        arr[k] = R[j];              // 1 operation
        j++;                        // 1 operation
        k++;                        // 1 operation
    }
}

void mergeSort(vector<int>& arr, int left, int right) {
    if (left < right) {             // 1 operation
        int mid = left + (right - left) / 2;  // 1 operation
        
        mergeSort(arr, left, mid);          // Recursive call
        mergeSort(arr, mid + 1, right);     // Recursive call
        merge(arr, left, mid, right);       // Merge
    }
}

int main() {
    vector<int> arr = {12, 11, 13, 5, 6, 7};
    int n = arr.size();
    
    cout << "Original array: ";
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    cout << endl;
    
    mergeSort(arr, 0, n - 1);
    
    cout << "Sorted array: ";
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    cout << endl;
    
    return 0;
}
```

**Analysis:**
- The array is split into two equal parts at each recursion level
- The recursion depth is log n
- At each level, the merge requires O(n) time
- **Total complexity: O(n log n)**

## Practical Tips for Complexity Analysis

### 1. Watch Out for Loops

```cpp
// Nested loops typically give O(n²)
for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
        // Some operation
    }
}

// Loop that halves the index gives O(log n)
for (int i = 1; i < n; i *= 2) {
    // Some operation
}
```

### 2. Recursive Functions

```cpp
// Recursive functions with one call: O(n)
// Recursive functions with two calls: O(2^n)
// Recursive functions with division: O(log n)
```

### 3. Space vs Time

```cpp
// Using additional memory can reduce time
// Example: Using a hash map for fast search
```

### 4. Avoid Nested Loops

```cpp
// Bad: O(n²)
for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
        if (arr[i] == arr[j]) {
            // Some operation
        }
    }
}

// Better: O(n) using a hash set
unordered_set<int> seen;
for (int i = 0; i < n; i++) {
    if (seen.find(arr[i]) != seen.end()) {
        // Some operation
    }
    seen.insert(arr[i]);
}
```

## Operations with Complexities

### Addition of Complexities

When we have two sequential executions, the complexities are added:

```cpp
// Example of complexity addition
void exampleAddition(int arr1[], int arr2[], int n) {
    // First loop: O(n)
    for (int i = 0; i < n; i++) {
        cout << arr1[i] << " ";
    }
    
    // Second loop: O(n)
    for (int i = 0; i < n; i++) {
        cout << arr2[i] << " ";
    }
}
// Total complexity: O(n) + O(n) = O(n)
```

**Rule:** We keep the term with the highest order:
- O(n) + O(n) = O(n)
- O(n²) + O(n) = O(n²)
- O(log n) + O(n) = O(n)

### Multiplication of Complexities

When we have nested executions, the complexities are multiplied:

```cpp
// Example of complexity multiplication
void exampleMultiplication(int arr1[], int arr2[], int n) {
    // Outer loop: O(n)
    for (int i = 0; i < n; i++) {
        // Inner loop: O(n)
        for (int j = 0; j < n; j++) {
            cout << "(" << arr1[i] << ", " << arr2[j] << ") ";
        }
    }
}
// Total complexity: O(n) × O(n) = O(n²)
```

**Multiplication rules:**
- O(n) × O(n) = O(n²)
- O(log n) × O(n) = O(n log n)
- O(n) × O(log n) = O(n log n)
- O(n²) × O(n) = O(n³)

### Complex Examples

```cpp
// Example 1: Addition and multiplication
void complexExample1(int arr[], int n) {
    // Part 1: O(n)
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    
    // Part 2: O(n²)
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << arr[i] + arr[j] << " ";
        }
    }
}
// Total complexity: O(n) + O(n²) = O(n²)
```

```cpp
// Example 2: Multiplication with different complexities
void complexExample2(int arr1[], int arr2[], int n) {
    // Outer loop: O(log n)
    for (int i = 1; i < n; i *= 2) {
        // Inner loop: O(n)
        for (int j = 0; j < n; j++) {
            cout << arr1[i] + arr2[j] << " ";
        }
    }
}
// Total complexity: O(log n) × O(n) = O(n log n)
```

```cpp
// Example 3: Multiplication with constants
void complexExample3(int arr[], int n) {
    // Outer loop: O(n)
    for (int i = 0; i < n; i++) {
        // Inner loop: O(1) - constant number of iterations
        for (int j = 0; j < 10; j++) {
            cout << arr[i] * j << " ";
        }
    }
}
// Total complexity: O(n) × O(1) = O(n)
```

### Simplification Rules

1. **Addition:** We keep the term with the highest order
   - O(n³) + O(n²) + O(n) = O(n³)
   - O(2^n) + O(n²) = O(2^n)

2. **Multiplication:** We multiply the terms
   - O(n) × O(log n) = O(n log n)
   - O(n²) × O(n) = O(n³)

3. **Constants:** Are ignored
   - O(5n) = O(n)
   - O(100) = O(1)

4. **Lower-order terms:** Are ignored
   - O(n² + n) = O(n²)
   - O(n + log n) = O(n)
