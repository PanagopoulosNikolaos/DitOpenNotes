# Πλήρης Οδηγός Δομών Δεδομένων και Αλγορίθμων στη C

Ένας περιεκτικός οδηγός που καλύπτει Δομές Δεδομένων και Αλγορίθμους στη C με επεξηγήσεις εννοιών, σωστή διαχείριση μνήμης και πρακτικά παραδείγματα κώδικα.

---

## Πίνακας Περιεχομένων

1. [Βασικά της C](#1-βασικά-της-c)
2. [Ανάπτυξη Λογικής](#2-ανάπτυξη-λογικής)
3. [Ανάλυση Πολυπλοκότητας](#3-ανάλυση-πολυπλοκότητας)
4. [Πίνακες](#4-πίνακες)
5. [Πίνακες (Matrix)](#5-πίνακες-matrix)
6. [Δείκτες](#6-δείκτες)
7. [Αλγόριθμοι Αναζήτησης](#7-αλγόριθμοι-αναζήτησης)
8. [Αλγόριθμοι Ταξινόμησης](#8-αλγόριθμοι-ταξινόμησης)
9. [Κατακερματισμός](#9-κατακερματισμός)
10. [Τεχνική Δύο Δεικτών](#10-τεχνική-δύο-δεικτών)
11. [Τεχνική Συρόμενου Παραθύρου](#11-τεχνική-συρόμενου-παραθύρου)
12. [Τεχνική Αθροίσματος Προθεμάτων](#12-τεχνική-αθροίσματος-προθεμάτων)
13. [Συμβολοσειρές](#13-συμβολοσειρές)
14. [Αναδρομή](#14-αναδρομή)
15. [Δυναμική Κατανομή Μνήμης](#15-δυναμική-κατανομή-μνήμης)
16. [Στοίβα](#16-στοίβα)
17. [Ουρά](#17-ουρά)
18. [Συνδεδεμένη Λίστα](#18-συνδεδεμένη-λίστα)
19. [Δέντρο](#19-δέντρο)
20. [Σωρός](#20-σωρός)
21. [Γράφος](#21-γράφος)
22. [Άπληστος Αλγόριθμος](#22-άπληστος-αλγόριθμος)
23. [Δυναμικός Προγραμματισμός](#23-δυναμικός-προγραμματισμός)
24. [Άλλοι Αλγόριθμοι](#24-άλλοι-αλγόριθμοι)

---

## 1. Βασικά της C

### Μεταβλητές και Τύποι Δεδομένων

**Μεταβλητές** είναι ονομασμένες θέσεις αποθήκευσης που περιέχουν δεδομένα. Στη C, πρέπει να δηλώνετε τις μεταβλητές πριν τις χρησιμοποιήσετε.

```c
#include <stdio.h>

int main() {
    int age = 25;              // Integer
    float price = 99.99;       // Floating point
    char grade = 'A';          // Character
    double pi = 3.14159265;    // Double precision
    
    printf("Age: %d\n", age);
    printf("Price: %.2f\n", price);
    printf("Grade: %c\n", grade);
    printf("Pi: %.8lf\n", pi);
    
    return 0;
}
```

**Βασικοί Τύποι Δεδομένων:**
- `int`: 4 bytes (συνήθως), αποθηκεύει ακεραίους
- `float`: 4 bytes, αποθηκεύει δεκαδικούς (ακρίβεια 6-7 ψηφίων)
- `double`: 8 bytes, αποθηκεύει δεκαδικούς (ακρίβεια 15 ψηφίων)
- `char`: 1 byte, αποθηκεύει μεμονωμένο χαρακτήρα

### Τελεστές

```c
#include <stdio.h>

int main() {
    int a = 10, b = 3;
    
    // Arithmetic operators
    printf("Addition: %d\n", a + b);        // 13
    printf("Subtraction: %d\n", a - b);     // 7
    printf("Multiplication: %d\n", a * b);  // 30
    printf("Division: %d\n", a / b);        // 3
    printf("Modulo: %d\n", a % b);          // 1
    
    // Relational operators
    printf("Equal: %d\n", a == b);          // 0 (false)
    printf("Greater: %d\n", a > b);         // 1 (true)
    
    // Logical operators
    printf("AND: %d\n", (a > 5) && (b > 2)); // 1 (true)
    printf("OR: %d\n", (a > 15) || (b > 2)); // 1 (true)
    printf("NOT: %d\n", !(a > 5));           // 0 (false)
    
    return 0;
}
```

### Έλεγχος Ροής

**Δήλωση If-Else:**

```c
#include <stdio.h>

int main() {
    int num = 15;
    
    if (num > 0) {
        printf("Positive\n");
    } else if (num < 0) {
        printf("Negative\n");
    } else {
        printf("Zero\n");
    }
    
    return 0;
}
```

**Δήλωση Switch:**

```c
#include <stdio.h>

int main() {
    char grade = 'B';
    
    switch(grade) {
        case 'A':
            printf("Excellent\n");
            break;
        case 'B':
            printf("Good\n");
            break;
        case 'C':
            printf("Average\n");
            break;
        default:
            printf("Invalid grade\n");
    }
    
    return 0;
}
```

### Βρόχοι

**Βρόχος For:**

```c
#include <stdio.h>

int main() {
    for (int i = 0; i < 5; i++) {
        printf("%d ", i);  // 0 1 2 3 4
    }
    printf("\n");
    return 0;
}
```

**Βρόχος While:**

```c
#include <stdio.h>

int main() {
    int i = 0;
    while (i < 5) {
        printf("%d ", i);
        i++;
    }
    printf("\n");
    return 0;
}
```

**Βρόχος Do-While:**

```c
#include <stdio.h>

int main() {
    int i = 0;
    do {
        printf("%d ", i);
        i++;
    } while (i < 5);
    printf("\n");
    return 0;
}
```

### Συναρτήσεις

```c
#include <stdio.h>

// Function declaration
int add(int a, int b);
void printMessage();

int main() {
    int sum = add(5, 3);
    printf("Sum: %d\n", sum);
    printMessage();
    return 0;
}

// Function definition
int add(int a, int b) {
    return a + b;
}

void printMessage() {
    printf("Hello from function!\n");
}
```

---

## 2. Ανάπτυξη Λογικής

Logic building strengthens problem-solving skills. Start with basic patterns and mathematical problems.

### Παράδειγμα: Έλεγχος Πρώτου Αριθμού

```c
#include <stdio.h>
#include <stdbool.h>

bool isPrime(int n) {
    if (n <= 1) return false;
    if (n <= 3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;
    
    for (int i = 5; i * i <= n; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0)
            return false;
    }
    return true;
}

int main() {
    int num = 29;
    if (isPrime(num))
        printf("%d is prime\n", num);
    else
        printf("%d is not prime\n", num);
    return 0;
}
```

### Παράδειγμα: Εκτύπωση Μοτίβου

```c
#include <stdio.h>

int main() {
    int n = 5;
    
    // Right triangle pattern
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= i; j++) {
            printf("* ");
        }
        printf("\n");
    }
    
    return 0;
}
```

---

## 3. Ανάλυση Πολυπλοκότητας

**Χρονική Πολυπλοκότητα (Time Complexity)** μέτρα το πώς αυξάνεται ο χρόνος εκτέλεσης με το μέγεθος της εισόδου.  
**Χωρική Πολυπλοκότητα (Space Complexity)** μέτρα την αύξηση της χρήσης μνήμης με το μέγεθος της εισόδου.

### Συμβολισμός Big O

- **O(1)**: Σταθερός χρόνος - πρόσβαση σε στοιχείο πίνακα
- **O(log n)**: Λογαριθμικός - δυαδική αναζήτηση
- **O(n)**: Γραμμικός - διάσχιση πίνακα
- **O(n log n)**: Γραμμικο-λογαριθμικός - ταξινόμηση συγχώνευσης, ταχεία ταξινόμηση
- **O(n²)**: Τετραγωνικός - εμφωλευμένοι βρόχοι, ταξινόμηση φυσαλίδας
- **O(2ⁿ)**: Εκθετικός - αναδρομική ακολουθία Fibonacci

### Ανάλυση Παραδειγμάτων

```c
// O(1) - Constant Time
int getElement(int arr[], int index) {
    return arr[index];
}

// O(n) - Linear Time
int findMax(int arr[], int n) {
    int max = arr[0];
    for (int i = 1; i < n; i++) {
        if (arr[i] > max)
            max = arr[i];
    }
    return max;
}

// O(n²) - Quadratic Time
void printPairs(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            printf("(%d, %d) ", arr[i], arr[j]);
        }
    }
}

// O(log n) - Logarithmic Time
int binarySearch(int arr[], int n, int target) {
    int left = 0, right = n - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] == target) return mid;
        if (arr[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    return -1;
}
```

---

## 4. Πίνακες

**Πίνακας (Array)** είναι μια συλλογή στοιχείων του ίδιου τύπου που αποθηκεύονται σε συνεχόμενες θέσεις μνήμης. Η πρόσβαση στα στοιχεία γίνεται μέσω δείκτη (με βάση το 0).

### Δήλωση και Αρχικοποίηση Πίνακα

```c
#include <stdio.h>

int main() {
    // Declaration and initialization
    int arr1[5] = {1, 2, 3, 4, 5};
    
    // Partial initialization (rest filled with 0)
    int arr2[5] = {1, 2};  // {1, 2, 0, 0, 0}
    
    // Size inference
    int arr3[] = {10, 20, 30};  // Size is 3
    
    // Accessing elements
    printf("First element: %d\n", arr1[0]);
    printf("Third element: %d\n", arr1[2]);
    
    // Modifying elements
    arr1[0] = 100;
    printf("Modified first element: %d\n", arr1[0]);
    
    return 0;
}
```

### Διάσχιση Πίνακα

```c
#include <stdio.h>

int main() {
    int arr[5] = {2, 4, 8, 12, 16};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    // Forward traversal
    printf("Forward: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    
    // Backward traversal
    printf("Backward: ");
    for (int i = n - 1; i >= 0; i--) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    
    return 0;
}
```

### Κοινές Λειτουργίες Πινάκων

```c
#include <stdio.h>

// Find maximum element
int findMax(int arr[], int n) {
    int max = arr[0];
    for (int i = 1; i < n; i++) {
        if (arr[i] > max)
            max = arr[i];
    }
    return max;
}

// Calculate sum
int calculateSum(int arr[], int n) {
    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += arr[i];
    }
    return sum;
}

// Reverse array
void reverseArray(int arr[], int n) {
    int start = 0, end = n - 1;
    while (start < end) {
        int temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;
        start++;
        end--;
    }
}

int main() {
    int arr[] = {5, 2, 8, 1, 9};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    printf("Max: %d\n", findMax(arr, n));
    printf("Sum: %d\n", calculateSum(arr, n));
    
    reverseArray(arr, n);
    printf("Reversed: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    
    return 0;
}
```

---

## 5. Πίνακες (Matrix)

**Πίνακας (Matrix)** είναι ένας διδιάστατος (2D) πίνακας διατεταγμένος σε γραμμές και στήλες.

### Δήλωση και Αρχικοποίηση Πίνακα (Matrix)

```c
#include <stdio.h>

int main() {
    // Declaration and initialization
    int matrix[3][3] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };
    
    // Accessing elements
    printf("Element at (1, 2): %d\n", matrix[1][2]);  // 6
    
    // Traversing matrix
    printf("Matrix:\n");
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            printf("%d ", matrix[i][j]);
        }
        printf("\n");
    }
    
    return 0;
}
```

### Λειτουργίες Πινάκων (Matrix)

```c
#include <stdio.h>

#define MAX 10

// Matrix addition
void addMatrices(int a[][MAX], int b[][MAX], int result[][MAX], int rows, int cols) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            result[i][j] = a[i][j] + b[i][j];
        }
    }
}

// Matrix multiplication
void multiplyMatrices(int a[][MAX], int b[][MAX], int result[][MAX], 
                      int r1, int c1, int c2) {
    for (int i = 0; i < r1; i++) {
        for (int j = 0; j < c2; j++) {
            result[i][j] = 0;
            for (int k = 0; k < c1; k++) {
                result[i][j] += a[i][k] * b[k][j];
            }
        }
    }
}

// Transpose matrix
void transpose(int matrix[][MAX], int result[][MAX], int rows, int cols) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            result[j][i] = matrix[i][j];
        }
    }
}

// Print matrix
void printMatrix(int matrix[][MAX], int rows, int cols) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            printf("%d ", matrix[i][j]);
        }
        printf("\n");
    }
}

int main() {
    int a[MAX][MAX] = {{1, 2}, {3, 4}};
    int b[MAX][MAX] = {{5, 6}, {7, 8}};
    int result[MAX][MAX];
    
    addMatrices(a, b, result, 2, 2);
    printf("Addition:\n");
    printMatrix(result, 2, 2);
    
    return 0;
}
```

---

## 6. Δείκτες

**Δείκτης (Pointer)** είναι μια μεταβλητή που αποθηκεύει τη διεύθυνση μνήμης μιας άλλης μεταβλητής. Παρέχουν άμεση πρόσβαση στη μνήμη και είναι απαραίτητοι για τη δυναμική διαχείριση μνήμης.

### Pointer Basics

```c
#include <stdio.h>

int main() {
    int var = 10;
    int *ptr = &var;  // ptr stores address of var
    
    printf("Value of var: %d\n", var);
    printf("Address of var: %p\n", &var);
    printf("Value of ptr: %p\n", ptr);
    printf("Value at address stored in ptr: %d\n", *ptr);
    
    // Modify value using pointer
    *ptr = 20;
    printf("New value of var: %d\n", var);
    
    return 0;
}
```

### Αριθμητική Δεικτών

```c
#include <stdio.h>

int main() {
    int arr[] = {10, 20, 30, 40, 50};
    int *ptr = arr;  // Points to first element
    
    printf("First element: %d\n", *ptr);
    printf("Second element: %d\n", *(ptr + 1));
    printf("Third element: %d\n", *(ptr + 2));
    
    // Traversing array using pointer
    for (int i = 0; i < 5; i++) {
        printf("%d ", *(ptr + i));
    }
    printf("\n");
    
    return 0;
}
```

### Δείκτες και Πίνακες

```c
#include <stdio.h>

void modifyArray(int *arr, int n) {
    for (int i = 0; i < n; i++) {
        arr[i] *= 2;  // Double each element
    }
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    printf("Before: ");
    for (int i = 0; i < n; i++) printf("%d ", arr[i]);
    printf("\n");
    
    modifyArray(arr, n);
    
    printf("After: ");
    for (int i = 0; i < n; i++) printf("%d ", arr[i]);
    printf("\n");
    
    return 0;
}
```

### Διπλοί Δείκτες

```c
#include <stdio.h>

int main() {
    int var = 10;
    int *ptr1 = &var;      // Pointer to int
    int **ptr2 = &ptr1;    // Pointer to pointer
    
    printf("Value using var: %d\n", var);
    printf("Value using *ptr1: %d\n", *ptr1);
    printf("Value using **ptr2: %d\n", **ptr2);
    
    return 0;
}
```

### Δείκτες Συναρτήσεων

```c
#include <stdio.h>

int add(int a, int b) {
    return a + b;
}

int subtract(int a, int b) {
    return a - b;
}

int main() {
    // Function pointer declaration
    int (*operation)(int, int);
    
    // Point to add function
    operation = &add;
    printf("Addition: %d\n", operation(10, 5));
    
    // Point to subtract function
    operation = &subtract;
    printf("Subtraction: %d\n", operation(10, 5));
    
    return 0;
}
```

---

## 7. Αλγόριθμοι Αναζήτησης

### Γραμμική Αναζήτηση

**Χρονική Πολυπλοκότητα:** O(n)  
**Χωρική Πολυπλοκότητα:** O(1)

```c
#include <stdio.h>

int linearSearch(int arr[], int n, int target) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == target)
            return i;  // Return index if found
    }
    return -1;  // Return -1 if not found
}

int main() {
    int arr[] = {5, 2, 8, 12, 1, 6};
    int n = sizeof(arr) / sizeof(arr[0]);
    int target = 12;
    
    int result = linearSearch(arr, n, target);
    if (result != -1)
        printf("Element found at index %d\n", result);
    else
        printf("Element not found\n");
    
    return 0;
}
```

### Δυαδική Αναζήτηση

**Χρονική Πολυπλοκότητα:** O(log n)  
**Χωρική Πολυπλοκότητα:** O(1)  
**Προαπαιτούμενο:** Ο πίνακας πρέπει να είναι ταξινομημένος

```c
#include <stdio.h>

int binarySearch(int arr[], int n, int target) {
    int left = 0, right = n - 1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        if (arr[mid] == target)
            return mid;
        
        if (arr[mid] < target)
            left = mid + 1;
        else
            right = mid - 1;
    }
    
    return -1;
}

int main() {
    int arr[] = {1, 3, 5, 7, 9, 11, 13, 15};
    int n = sizeof(arr) / sizeof(arr[0]);
    int target = 7;
    
    int result = binarySearch(arr, n, target);
    if (result != -1)
        printf("Element found at index %d\n", result);
    else
        printf("Element not found\n");
    
    return 0;
}
```

### Αναδρομική Δυαδική Αναζήτηση

```c
#include <stdio.h>

int binarySearchRecursive(int arr[], int left, int right, int target) {
    if (left > right)
        return -1;
    
    int mid = left + (right - left) / 2;
    
    if (arr[mid] == target)
        return mid;
    
    if (arr[mid] < target)
        return binarySearchRecursive(arr, mid + 1, right, target);
    else
        return binarySearchRecursive(arr, left, mid - 1, target);
}

int main() {
    int arr[] = {1, 3, 5, 7, 9, 11, 13, 15};
    int n = sizeof(arr) / sizeof(arr[0]);
    int target = 9;
    
    int result = binarySearchRecursive(arr, 0, n - 1, target);
    if (result != -1)
        printf("Element found at index %d\n", result);
    else
        printf("Element not found\n");
    
    return 0;
}
```

---

## 8. Αλγόριθμοι Ταξινόμησης

### Ταξινόμηση Φυσαλίδας (Bubble Sort)

**Χρονική Πολυπλοκότητα:** O(n²) μέση και χειρότερη, O(n) καλύτερη  
**Χωρική Πολυπλοκότητα:** O(1)  
**Ευσταθής:** Ναι

```c
#include <stdio.h>

void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int swapped = 0;
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                // Swap
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                swapped = 1;
            }
        }
        // Optimization: break if no swaps occurred
        if (!swapped)
            break;
    }
}

int main() {
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    printf("Original array: ");
    for (int i = 0; i < n; i++) printf("%d ", arr[i]);
    printf("\n");
    
    bubbleSort(arr, n);
    
    printf("Sorted array: ");
    for (int i = 0; i < n; i++) printf("%d ", arr[i]);
    printf("\n");
    
    return 0;
}
```

### Ταξινόμηση Επιλογής (Selection Sort)

**Time Complexity:** O(n²)  
**Χωρική Πολυπλοκότητα:** O(1)  
**Ευσταθής:** Όχι

```c
#include <stdio.h>

void selectionSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int minIdx = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIdx])
                minIdx = j;
        }
        // Swap minimum element with first element
        if (minIdx != i) {
            int temp = arr[i];
            arr[i] = arr[minIdx];
            arr[minIdx] = temp;
        }
    }
}

int main() {
    int arr[] = {64, 25, 12, 22, 11};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    selectionSort(arr, n);
    
    printf("Sorted array: ");
    for (int i = 0; i < n; i++) printf("%d ", arr[i]);
    printf("\n");
    
    return 0;
}
```

### Ταξινόμηση Εισαγωγής (Insertion Sort)

**Χρονική Πολυπλοκότητα:** O(n²) μέση και χειρότερη, O(n) καλύτερη  
**Χωρική Πολυπλοκότητα:** O(1)  
**Ευσταθής:** Ναι

```c
#include <stdio.h>

void insertionSort(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        
        // Move elements greater than key one position ahead
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

int main() {
    int arr[] = {12, 11, 13, 5, 6};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    insertionSort(arr, n);
    
    printf("Sorted array: ");
    for (int i = 0; i < n; i++) printf("%d ", arr[i]);
    printf("\n");
    
    return 0;
}
```

### Ταχεία Ταξινόμηση (Quick Sort)

**Χρονική Πολυπλοκότητα:** O(n log n) μέση, O(n²) χειρότερη  
**Χωρική Πολυπλοκότητα:** O(log n) due to recursion  
**Ευσταθής:** Όχι

```c
#include <stdio.h>

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int partition(int arr[], int low, int high) {
    int pivot = arr[high];  // Choose last element as pivot
    int i = low - 1;
    
    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    return i + 1;
}

void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pivotIndex = partition(arr, low, high);
        quickSort(arr, low, pivotIndex - 1);
        quickSort(arr, pivotIndex + 1, high);
    }
}

int main() {
    int arr[] = {64, 34, 25, 12, 22, 11, 90, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    quickSort(arr, 0, n - 1);
    
    printf("Sorted array: ");
    for (int i = 0; i < n; i++) printf("%d ", arr[i]);
    printf("\n");
    
    return 0;
}
```

### Ταξινόμηση Συγχώνευσης (Merge Sort)

**Time Complexity:** O(n log n)  
**Χωρική Πολυπλοκότητα:** O(n)  
**Ευσταθής:** Ναι

```c
#include <stdio.h>
#include <stdlib.h>

void merge(int arr[], int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;
    
    // Create temporary arrays
    int *L = (int*)malloc(n1 * sizeof(int));
    int *R = (int*)malloc(n2 * sizeof(int));
    
    // Copy data to temp arrays
    for (int i = 0; i < n1; i++)
        L[i] = arr[left + i];
    for (int j = 0; j < n2; j++)
        R[j] = arr[mid + 1 + j];
    
    // Merge temp arrays back
    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }
    
    // Copy remaining elements
    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }
    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
    
    // Free temporary arrays
    free(L);
    free(R);
}

void mergeSort(int arr[], int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }
}

int main() {
    int arr[] = {12, 11, 13, 5, 6, 7};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    mergeSort(arr, 0, n - 1);
    
    printf("Sorted array: ");
    for (int i = 0; i < n; i++) printf("%d ", arr[i]);
    printf("\n");
    
    return 0;
}
```

---

## 9. Κατακερματισμός (Hashing)

**Hashing** maps data to fixed-size values using a hash function. It enables O(1) average-case insertion, deletion, and search.

### Hash Table with Separate Chaining

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TABLE_SIZE 100

// Node structure for linked list
typedef struct Node {
    char *key;
    char *value;
    struct Node *next;
} Node;

// Hash table structure
typedef struct HashTable {
    Node **buckets;
    int size;
} HashTable;

// Hash function
int hashFunction(char *key, int tableSize) {
    int sum = 0;
    int factor = 31;
    for (int i = 0; i < strlen(key); i++) {
        sum = ((sum % tableSize) + ((key[i]) * factor) % tableSize) % tableSize;
        factor = (factor * 31) % __INT16_MAX__;
    }
    return sum;
}

// Create hash table
HashTable* createHashTable(int size) {
    HashTable *table = (HashTable*)malloc(sizeof(HashTable));
    table->size = size;
    table->buckets = (Node**)calloc(size, sizeof(Node*));
    return table;
}

// Insert key-value pair
void insert(HashTable *table, char *key, char *value) {
    int index = hashFunction(key, table->size);
    
    Node *newNode = (Node*)malloc(sizeof(Node));
    newNode->key = key;
    newNode->value = value;
    newNode->next = table->buckets[index];
    table->buckets[index] = newNode;
}

// Search for a key
char* search(HashTable *table, char *key) {
    int index = hashFunction(key, table->size);
    Node *current = table->buckets[index];
    
    while (current != NULL) {
        if (strcmp(current->key, key) == 0)
            return current->value;
        current = current->next;
    }
    return NULL;
}

// Delete a key
void deleteKey(HashTable *table, char *key) {
    int index = hashFunction(key, table->size);
    Node *current = table->buckets[index];
    Node *prev = NULL;
    
    while (current != NULL) {
        if (strcmp(current->key, key) == 0) {
            if (prev == NULL)
                table->buckets[index] = current->next;
            else
                prev->next = current->next;
            free(current);
            return;
        }
        prev = current;
        current = current->next;
    }
}

// Free hash table
void freeHashTable(HashTable *table) {
    for (int i = 0; i < table->size; i++) {
        Node *current = table->buckets[i];
        while (current != NULL) {
            Node *temp = current;
            current = current->next;
            free(temp);
        }
    }
    free(table->buckets);
    free(table);
}

int main() {
    HashTable *table = createHashTable(TABLE_SIZE);
    
    insert(table, "name", "John");
    insert(table, "age", "25");
    insert(table, "city", "New York");
    
    printf("Name: %s\n", search(table, "name"));
    printf("Age: %s\n", search(table, "age"));
    
    deleteKey(table, "age");
    char *age = search(table, "age");
    if (age == NULL)
        printf("Age not found after deletion\n");
    
    freeHashTable(table);
    return 0;
}
```

---

## 10. Τεχνική Δύο Δεικτών (Two Pointer Technique)

**Two Pointer Technique** uses two pointers to iterate through data structure, often reducing time complexity from O(n²) to O(n).

### Example: Pair with Given Sum in Sorted Array

```c
#include <stdio.h>
#include <stdbool.h>

bool findPairWithSum(int arr[], int n, int target) {
    int left = 0;
    int right = n - 1;
    
    while (left < right) {
        int sum = arr[left] + arr[right];
        
        if (sum == target) {
            printf("Pair found: (%d, %d)\n", arr[left], arr[right]);
            return true;
        }
        else if (sum < target)
            left++;
        else
            right--;
    }
    
    return false;
}

int main() {
    int arr[] = {1, 2, 3, 4, 6, 8, 9};
    int n = sizeof(arr) / sizeof(arr[0]);
    int target = 10;
    
    if (!findPairWithSum(arr, n, target))
        printf("No pair found\n");
    
    return 0;
}
```

### Παράδειγμα: Αφαίρεση Διπλότυπων από Ταξινομημένο Πίνακα

```c
#include <stdio.h>

int removeDuplicates(int arr[], int n) {
    if (n == 0) return 0;
    
    int uniqueIdx = 0;
    for (int i = 1; i < n; i++) {
        if (arr[i] != arr[uniqueIdx]) {
            uniqueIdx++;
            arr[uniqueIdx] = arr[i];
        }
    }
    
    return uniqueIdx + 1;
}

int main() {
    int arr[] = {1, 1, 2, 2, 2, 3, 4, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    int newLength = removeDuplicates(arr, n);
    
    printf("Array after removing duplicates: ");
    for (int i = 0; i < newLength; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    
    return 0;
}
```

---

## 11. Τεχνική Συρόμενου Παραθύρου (Sliding Window Technique)

**Sliding Window** maintains a subset of elements (window) and slides it to process subarrays efficiently.

### Example: Maximum Sum Subarray of Size K

```c
#include <stdio.h>

int maxSumSubarray(int arr[], int n, int k) {
    if (n < k) return -1;
    
    // Compute sum of first window
    int windowSum = 0;
    for (int i = 0; i < k; i++)
        windowSum += arr[i];
    
    int maxSum = windowSum;
    
    // Slide the window
    for (int i = k; i < n; i++) {
        windowSum = windowSum - arr[i - k] + arr[i];
        if (windowSum > maxSum)
            maxSum = windowSum;
    }
    
    return maxSum;
}

int main() {
    int arr[] = {2, 1, 5, 1, 3, 2};
    int n = sizeof(arr) / sizeof(arr[0]);
    int k = 3;
    
    printf("Maximum sum of subarray of size %d: %d\n", 
           k, maxSumSubarray(arr, n, k));
    
    return 0;
}
```

### Παράδειγμα: Μεγαλύτερη Υποσυμβολοσειρά Χωρίς Επαναλαμβανόμενους Χαρακτήρες

```c
#include <stdio.h>
#include <string.h>

int lengthOfLongestSubstring(char *s) {
    int n = strlen(s);
    int maxLength = 0;
    int start = 0;
    int charIndex[256];  // ASCII characters
    
    // Initialize all character indices to -1
    for (int i = 0; i < 256; i++)
        charIndex[i] = -1;
    
    for (int end = 0; end < n; end++) {
        // If character already seen, move start
        if (charIndex[s[end]] >= start)
            start = charIndex[s[end]] + 1;
        
        charIndex[s[end]] = end;
        
        int currentLength = end - start + 1;
        if (currentLength > maxLength)
            maxLength = currentLength;
    }
    
    return maxLength;
}

int main() {
    char str[] = "abcabcbb";
    printf("Length of longest substring: %d\n", 
           lengthOfLongestSubstring(str));
    return 0;
}
```

---

## 12. Τεχνική Αθροίσματος Προθεμάτων (Prefix Sum Technique)

Το **Άθροισμα Προθεμάτων (Prefix Sum)** προϋπολογίζει αθροιστικά αθροίσματα για την απάντηση ερωτημάτων αθροίσματος περιοχής σε χρόνο O(1).

### Example: Range Sum Queries

```c
#include <stdio.h>

void computePrefixSum(int arr[], int prefixSum[], int n) {
    prefixSum[0] = arr[0];
    for (int i = 1; i < n; i++)
        prefixSum[i] = prefixSum[i - 1] + arr[i];
}

int rangeSum(int prefixSum[], int left, int right) {
    if (left == 0)
        return prefixSum[right];
    return prefixSum[right] - prefixSum[left - 1];
}

int main() {
    int arr[] = {3, 2, 5, 1, 6, 4};
    int n = sizeof(arr) / sizeof(arr[0]);
    int prefixSum[n];
    
    computePrefixSum(arr, prefixSum, n);
    
    printf("Sum from index 1 to 4: %d\n", rangeSum(prefixSum, 1, 4));
    printf("Sum from index 0 to 3: %d\n", rangeSum(prefixSum, 0, 3));
    
    return 0;
}
```

---

## 13. Συμβολοσειρές (Strings)

Μια **Συμβολοσειρά (String)** στη C είναι ένας πίνακας χαρακτήρων που τερματίζεται με τον μηδενικό χαρακτήρα (`\0`).

### String Declaration and Initialization

```c
#include <stdio.h>
#include <string.h>

int main() {
    // Different ways to declare strings
    char str1[] = "Hello";
    char str2[20] = "World";
    char str3[] = {'H', 'i', '\0'};
    
    printf("%s\n", str1);
    printf("%s\n", str2);
    printf("%s\n", str3);
    
    // String length
    printf("Length of str1: %lu\n", strlen(str1));
    
    return 0;
}
```

### Λειτουργίες Συμβολοσειρών

```c
#include <stdio.h>
#include <string.h>

int main() {
    char str1[50] = "Hello";
    char str2[] = " World";
    char str3[50];
    
    // String copy
    strcpy(str3, str1);
    printf("Copied: %s\n", str3);
    
    // String concatenation
    strcat(str1, str2);
    printf("Concatenated: %s\n", str1);
    
    // String comparison
    if (strcmp(str1, str3) == 0)
        printf("Strings are equal\n");
    else
        printf("Strings are different\n");
    
    return 0;
}
```

### Προσαρμοσμένες Συναρτήσεις Συμβολοσειρών

```c
#include <stdio.h>

// Calculate string length
int stringLength(char *str) {
    int len = 0;
    while (str[len] != '\0')
        len++;
    return len;
}

// Reverse string
void reverseString(char *str) {
    int n = stringLength(str);
    for (int i = 0; i < n / 2; i++) {
        char temp = str[i];
        str[i] = str[n - 1 - i];
        str[n - 1 - i] = temp;
    }
}

// Check palindrome
int isPalindrome(char *str) {
    int n = stringLength(str);
    for (int i = 0; i < n / 2; i++) {
        if (str[i] != str[n - 1 - i])
            return 0;
    }
    return 1;
}

int main() {
    char str[] = "radar";
    
    printf("Length: %d\n", stringLength(str));
    
    if (isPalindrome(str))
        printf("'%s' is a palindrome\n", str);
    
    reverseString(str);
    printf("Reversed: %s\n", str);
    
    return 0;
}
```

---

## 14. Αναδρομή (Recursion)

**Recursion** occurs when a function calls itself. It requires a base case to stop and a recursive case to continue.

### Factorial

```c
#include <stdio.h>

int factorial(int n) {
    // Base case
    if (n == 0 || n == 1)
        return 1;
    // Recursive case
    return n * factorial(n - 1);
}

int main() {
    int num = 5;
    printf("Factorial of %d is %d\n", num, factorial(num));
    return 0;
}
```

### Ακολουθία Fibonacci

```c
#include <stdio.h>

int fibonacci(int n) {
    // Base cases
    if (n == 0) return 0;
    if (n == 1) return 1;
    // Recursive case
    return fibonacci(n - 1) + fibonacci(n - 2);
}

int main() {
    int n = 10;
    printf("Fibonacci series: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", fibonacci(i));
    }
    printf("\n");
    return 0;
}
```

### Πύργοι του Ανόι (Tower of Hanoi)

```c
#include <stdio.h>

void towerOfHanoi(int n, char source, char auxiliary, char destination) {
    if (n == 1) {
        printf("Move disk 1 from %c to %c\n", source, destination);
        return;
    }
    
    towerOfHanoi(n - 1, source, destination, auxiliary);
    printf("Move disk %d from %c to %c\n", n, source, destination);
    towerOfHanoi(n - 1, auxiliary, source, destination);
}

int main() {
    int n = 3;
    towerOfHanoi(n, 'A', 'B', 'C');
    return 0;
}
```

---

## 15. Δυναμική Κατανομή Μνήμης

Dynamic memory allocation allows runtime memory management using heap memory.

### malloc() - Memory Allocation

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int n = 5;
    
    // Allocate memory for n integers
    int *arr = (int*)malloc(n * sizeof(int));
    
    // Check if allocation succeeded
    if (arr == NULL) {
        printf("Memory allocation failed\n");
        return 1;
    }
    
    // Use the allocated memory
    for (int i = 0; i < n; i++) {
        arr[i] = i * 10;
    }
    
    printf("Array: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    
    // Free the allocated memory
    free(arr);
    arr = NULL;  // Avoid dangling pointer
    
    return 0;
}
```

### calloc() - Συνεχόμενη Κατανομή

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int n = 5;
    
    // Allocate and initialize to 0
    int *arr = (int*)calloc(n, sizeof(int));
    
    if (arr == NULL) {
        printf("Memory allocation failed\n");
        return 1;
    }
    
    printf("Array (initialized to 0): ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    
    free(arr);
    return 0;
}
```

### realloc() - Επανακατανομή Μνήμης

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int *arr = (int*)malloc(5 * sizeof(int));
    
    if (arr == NULL) {
        printf("Initial allocation failed\n");
        return 1;
    }
    
    // Fill initial array
    for (int i = 0; i < 5; i++)
        arr[i] = i + 1;
    
    // Resize to 10 elements
    int *temp = (int*)realloc(arr, 10 * sizeof(int));
    
    if (temp == NULL) {
        printf("Reallocation failed\n");
        free(arr);
        return 1;
    }
    
    arr = temp;
    
    // Fill new elements
    for (int i = 5; i < 10; i++)
        arr[i] = i + 1;
    
    printf("Resized array: ");
    for (int i = 0; i < 10; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    
    free(arr);
    return 0;
}
```

### Δυναμικός Διδιάστατος (2D) Πίνακας

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int rows = 3, cols = 4;
    
    // Allocate array of pointers
    int **matrix = (int**)malloc(rows * sizeof(int*));
    
    // Allocate each row
    for (int i = 0; i < rows; i++) {
        matrix[i] = (int*)malloc(cols * sizeof(int));
    }
    
    // Fill matrix
    int value = 1;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            matrix[i][j] = value++;
        }
    }
    
    // Print matrix
    printf("Matrix:\n");
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            printf("%d ", matrix[i][j]);
        }
        printf("\n");
    }
    
    // Free memory
    for (int i = 0; i < rows; i++) {
        free(matrix[i]);
    }
    free(matrix);
    
    return 0;
}
```

---

## 16. Στοίβα (Stack)

**Stack** is a LIFO (Last In First Out) data structure. Elements are added and removed from the same end (top).

### Stack Implementation Using Array

```c
#include <stdio.h>
#include <stdbool.h>

#define MAX_SIZE 100

typedef struct {
    int arr[MAX_SIZE];
    int top;
} Stack;

// Initialize stack
void initialize(Stack *stack) {
    stack->top = -1;
}

// Check if stack is empty
bool isEmpty(Stack *stack) {
    return stack->top == -1;
}

// Check if stack is full
bool isFull(Stack *stack) {
    return stack->top == MAX_SIZE - 1;
}

// Push element onto stack
void push(Stack *stack, int value) {
    if (isFull(stack)) {
        printf("Stack Overflow\n");
        return;
    }
    stack->arr[++stack->top] = value;
}

// Pop element from stack
int pop(Stack *stack) {
    if (isEmpty(stack)) {
        printf("Stack Underflow\n");
        return -1;
    }
    return stack->arr[stack->top--];
}

// Peek top element
int peek(Stack *stack) {
    if (isEmpty(stack)) {
        printf("Stack is empty\n");
        return -1;
    }
    return stack->arr[stack->top];
}

int main() {
    Stack stack;
    initialize(&stack);
    
    push(&stack, 10);
    push(&stack, 20);
    push(&stack, 30);
    
    printf("Top element: %d\n", peek(&stack));
    printf("Popped: %d\n", pop(&stack));
    printf("Popped: %d\n", pop(&stack));
    printf("Top element: %d\n", peek(&stack));
    
    return 0;
}
```

### Εφαρμογές Στοίβας: Ισορροπημένες Παρενθέσεις

```c
#include <stdio.h>
#include <stdbool.h>
#include <string.h>

#define MAX_SIZE 100

typedef struct {
    char arr[MAX_SIZE];
    int top;
} Stack;

void initialize(Stack *stack) {
    stack->top = -1;
}

bool isEmpty(Stack *stack) {
    return stack->top == -1;
}

void push(Stack *stack, char value) {
    if (stack->top < MAX_SIZE - 1)
        stack->arr[++stack->top] = value;
}

char pop(Stack *stack) {
    if (!isEmpty(stack))
        return stack->arr[stack->top--];
    return '\0';
}

bool isMatchingPair(char opening, char closing) {
    return (opening == '(' && closing == ')') ||
           (opening == '{' && closing == '}') ||
           (opening == '[' && closing == ']');
}

bool isBalanced(char *expr) {
    Stack stack;
    initialize(&stack);
    
    for (int i = 0; i < strlen(expr); i++) {
        char ch = expr[i];
        
        if (ch == '(' || ch == '{' || ch == '[') {
            push(&stack, ch);
        }
        else if (ch == ')' || ch == '}' || ch == ']') {
            if (isEmpty(&stack))
                return false;
            
            char top = pop(&stack);
            if (!isMatchingPair(top, ch))
                return false;
        }
    }
    
    return isEmpty(&stack);
}

int main() {
    char expr1[] = "{[()]}";
    char expr2[] = "{[(])}";
    
    printf("'%s' is %s\n", expr1, 
           isBalanced(expr1) ? "balanced" : "not balanced");
    printf("'%s' is %s\n", expr2, 
           isBalanced(expr2) ? "balanced" : "not balanced");
    
    return 0;
}
```

---

## 17. Ουρά (Queue)

Η **Ουρά (Queue)** είναι μια δομή δεδομένων FIFO (First In First Out). Τα στοιχεία προστίθενται στο πίσω μέρος (rear) και αφαιρούνται από το μπροστινό μέρος (front).

### Queue Implementation Using Array

```c
#include <stdio.h>
#include <stdbool.h>

#define MAX_SIZE 100

typedef struct {
    int items[MAX_SIZE];
    int front;
    int rear;
} Queue;

// Initialize queue
void initialize(Queue *q) {
    q->front = -1;
    q->rear = 0;
}

// Check if queue is empty
bool isEmpty(Queue *q) {
    return q->front == q->rear - 1;
}

// Check if queue is full
bool isFull(Queue *q) {
    return q->rear == MAX_SIZE;
}

// Enqueue (add element)
void enqueue(Queue *q, int value) {
    if (isFull(q)) {
        printf("Queue is full\n");
        return;
    }
    q->items[q->rear++] = value;
}

// Dequeue (remove element)
int dequeue(Queue *q) {
    if (isEmpty(q)) {
        printf("Queue is empty\n");
        return -1;
    }
    return q->items[++q->front];
}

// Peek front element
int peek(Queue *q) {
    if (isEmpty(q)) {
        printf("Queue is empty\n");
        return -1;
    }
    return q->items[q->front + 1];
}

int main() {
    Queue q;
    initialize(&q);
    
    enqueue(&q, 10);
    enqueue(&q, 20);
    enqueue(&q, 30);
    
    printf("Front element: %d\n", peek(&q));
    printf("Dequeued: %d\n", dequeue(&q));
    printf("Dequeued: %d\n", dequeue(&q));
    printf("Front element: %d\n", peek(&q));
    
    return 0;
}
```

### Κυκλική Ουρά (Circular Queue)

```c
#include <stdio.h>
#include <stdbool.h>

#define MAX_SIZE 5

typedef struct {
    int items[MAX_SIZE];
    int front;
    int rear;
    int count;
} CircularQueue;

void initialize(CircularQueue *q) {
    q->front = 0;
    q->rear = -1;
    q->count = 0;
}

bool isEmpty(CircularQueue *q) {
    return q->count == 0;
}

bool isFull(CircularQueue *q) {
    return q->count == MAX_SIZE;
}

void enqueue(CircularQueue *q, int value) {
    if (isFull(q)) {
        printf("Queue is full\n");
        return;
    }
    q->rear = (q->rear + 1) % MAX_SIZE;
    q->items[q->rear] = value;
    q->count++;
}

int dequeue(CircularQueue *q) {
    if (isEmpty(q)) {
        printf("Queue is empty\n");
        return -1;
    }
    int value = q->items[q->front];
    q->front = (q->front + 1) % MAX_SIZE;
    q->count--;
    return value;
}

int main() {
    CircularQueue q;
    initialize(&q);
    
    enqueue(&q, 1);
    enqueue(&q, 2);
    enqueue(&q, 3);
    
    printf("Dequeued: %d\n", dequeue(&q));
    
    enqueue(&q, 4);
    enqueue(&q, 5);
    enqueue(&q, 6);
    
    while (!isEmpty(&q)) {
        printf("%d ", dequeue(&q));
    }
    printf("\n");
    
    return 0;
}
```

---

## 18. Συνδεδεμένη Λίστα (Linked List)

**Linked List** is a linear data structure where elements (nodes) are connected via pointers. Unlike arrays, elements are not stored contiguously.

### Singly Linked List

```c
#include <stdio.h>
#include <stdlib.h>

// Node structure
typedef struct Node {
    int data;
    struct Node *next;
} Node;

// Create new node
Node* createNode(int data) {
    Node *newNode = (Node*)malloc(sizeof(Node));
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

// Insert at beginning
void insertAtBeginning(Node **head, int data) {
    Node *newNode = createNode(data);
    newNode->next = *head;
    *head = newNode;
}

// Insert at end
void insertAtEnd(Node **head, int data) {
    Node *newNode = createNode(data);
    
    if (*head == NULL) {
        *head = newNode;
        return;
    }
    
    Node *temp = *head;
    while (temp->next != NULL) {
        temp = temp->next;
    }
    temp->next = newNode;
}

// Delete node with given value
void deleteNode(Node **head, int key) {
    Node *temp = *head;
    Node *prev = NULL;
    
    // If head needs to be deleted
    if (temp != NULL && temp->data == key) {
        *head = temp->next;
        free(temp);
        return;
    }
    
    // Search for node to delete
    while (temp != NULL && temp->data != key) {
        prev = temp;
        temp = temp->next;
    }
    
    // If key not found
    if (temp == NULL) return;
    
    // Unlink and free node
    prev->next = temp->next;
    free(temp);
}

// Search for a value
Node* search(Node *head, int key) {
    Node *current = head;
    while (current != NULL) {
        if (current->data == key)
            return current;
        current = current->next;
    }
    return NULL;
}

// Print list
void printList(Node *head) {
    Node *temp = head;
    while (temp != NULL) {
        printf("%d -> ", temp->data);
        temp = temp->next;
    }
    printf("NULL\n");
}

// Free entire list
void freeList(Node *head) {
    Node *temp;
    while (head != NULL) {
        temp = head;
        head = head->next;
        free(temp);
    }
}

int main() {
    Node *head = NULL;
    
    insertAtEnd(&head, 10);
    insertAtEnd(&head, 20);
    insertAtEnd(&head, 30);
    insertAtBeginning(&head, 5);
    
    printf("Linked List: ");
    printList(head);
    
    deleteNode(&head, 20);
    printf("After deleting 20: ");
    printList(head);
    
    Node *found = search(head, 10);
    if (found != NULL)
        printf("Found: %d\n", found->data);
    
    freeList(head);
    return 0;
}
```

### Διπλά Συνδεδεμένη Λίστα (Doubly Linked List)

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node *next;
    struct Node *prev;
} Node;

Node* createNode(int data) {
    Node *newNode = (Node*)malloc(sizeof(Node));
    newNode->data = data;
    newNode->next = NULL;
    newNode->prev = NULL;
    return newNode;
}

void insertAtEnd(Node **head, int data) {
    Node *newNode = createNode(data);
    
    if (*head == NULL) {
        *head = newNode;
        return;
    }
    
    Node *temp = *head;
    while (temp->next != NULL) {
        temp = temp->next;
    }
    
    temp->next = newNode;
    newNode->prev = temp;
}

void printList(Node *head) {
    while (head != NULL) {
        printf("%d <-> ", head->data);
        head = head->next;
    }
    printf("NULL\n");
}

void printReverse(Node *head) {
    if (head == NULL) return;
    
    // Go to last node
    while (head->next != NULL) {
        head = head->next;
    }
    
    // Print in reverse
    while (head != NULL) {
        printf("%d <-> ", head->data);
        head = head->prev;
    }
    printf("NULL\n");
}

int main() {
    Node *head = NULL;
    
    insertAtEnd(&head, 10);
    insertAtEnd(&head, 20);
    insertAtEnd(&head, 30);
    
    printf("Forward: ");
    printList(head);
    
    printf("Backward: ");
    printReverse(head);
    
    return 0;
}
```

---

## 19. Δέντρο (Tree)

Το **Δυαδικό Δέντρο (Binary Tree)** είναι μια ιεραρχική δομή δεδομένων όπου κάθε κόμβος έχει το πολύ δύο παιδιά (αριστερό και δεξί).

### Υλοποίηση Δυαδικού Δέντρου

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node *left;
    struct Node *right;
} Node;

// Create new node
Node* createNode(int data) {
    Node *newNode = (Node*)malloc(sizeof(Node));
    newNode->data = data;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

// Inorder traversal: Left -> Root -> Right
void inorderTraversal(Node *root) {
    if (root == NULL) return;
    inorderTraversal(root->left);
    printf("%d ", root->data);
    inorderTraversal(root->right);
}

// Preorder traversal: Root -> Left -> Right
void preorderTraversal(Node *root) {
    if (root == NULL) return;
    printf("%d ", root->data);
    preorderTraversal(root->left);
    preorderTraversal(root->right);
}

// Postorder traversal: Left -> Right -> Root
void postorderTraversal(Node *root) {
    if (root == NULL) return;
    postorderTraversal(root->left);
    postorderTraversal(root->right);
    printf("%d ", root->data);
}

// Calculate height of tree
int height(Node *root) {
    if (root == NULL) return 0;
    
    int leftHeight = height(root->left);
    int rightHeight = height(root->right);
    
    return (leftHeight > rightHeight ? leftHeight : rightHeight) + 1;
}

// Count nodes in tree
int countNodes(Node *root) {
    if (root == NULL) return 0;
    return 1 + countNodes(root->left) + countNodes(root->right);
}

int main() {
    // Create tree
    Node *root = createNode(1);
    root->left = createNode(2);
    root->right = createNode(3);
    root->left->left = createNode(4);
    root->left->right = createNode(5);
    
    printf("Inorder: ");
    inorderTraversal(root);
    printf("\n");
    
    printf("Preorder: ");
    preorderTraversal(root);
    printf("\n");
    
    printf("Postorder: ");
    postorderTraversal(root);
    printf("\n");
    
    printf("Height: %d\n", height(root));
    printf("Total nodes: %d\n", countNodes(root));
    
    return 0;
}
```

### Δυαδική Αναζήτηση Tree (BST)

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node *left;
    struct Node *right;
} Node;

Node* createNode(int data) {
    Node *newNode = (Node*)malloc(sizeof(Node));
    newNode->data = data;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

// Insert into BST
Node* insert(Node *root, int data) {
    if (root == NULL) {
        return createNode(data);
    }
    
    if (data < root->data)
        root->left = insert(root->left, data);
    else if (data > root->data)
        root->right = insert(root->right, data);
    
    return root;
}

// Search in BST
Node* search(Node *root, int key) {
    if (root == NULL || root->data == key)
        return root;
    
    if (key < root->data)
        return search(root->left, key);
    else
        return search(root->right, key);
}

// Find minimum value node
Node* findMin(Node *root) {
    while (root->left != NULL)
        root = root->left;
    return root;
}

// Delete from BST
Node* deleteNode(Node *root, int key) {
    if (root == NULL) return root;
    
    if (key < root->data)
        root->left = deleteNode(root->left, key);
    else if (key > root->data)
        root->right = deleteNode(root->right, key);
    else {
        // Node with one child or no child
        if (root->left == NULL) {
            Node *temp = root->right;
            free(root);
            return temp;
        }
        else if (root->right == NULL) {
            Node *temp = root->left;
            free(root);
            return temp;
        }
        
        // Node with two children
        Node *temp = findMin(root->right);
        root->data = temp->data;
        root->right = deleteNode(root->right, temp->data);
    }
    return root;
}

void inorder(Node *root) {
    if (root != NULL) {
        inorder(root->left);
        printf("%d ", root->data);
        inorder(root->right);
    }
}

int main() {
    Node *root = NULL;
    
    root = insert(root, 50);
    insert(root, 30);
    insert(root, 20);
    insert(root, 40);
    insert(root, 70);
    insert(root, 60);
    insert(root, 80);
    
    printf("Inorder: ");
    inorder(root);
    printf("\n");
    
    Node *found = search(root, 40);
    if (found != NULL)
        printf("Found: %d\n", found->data);
    
    root = deleteNode(root, 20);
    printf("After deleting 20: ");
    inorder(root);
    printf("\n");
    
    return 0;
}
```

---

## 20. Σωρός (Heap)

Ο **Σωρός (Heap)** είναι ένα πλήρες δυαδικό δέντρο που ικανοποιεί την ιδιότητα του σωρού. Σε ένα max heap, οι γονικοί κόμβοι είναι μεγαλύτεροι από τα παιδιά· σε ένα min heap, οι γονικοί κόμβοι είναι μικρότεροι.

### Υλοποίηση Min Heap

```c
#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 100

typedef struct {
    int arr[MAX_SIZE];
    int size;
} MinHeap;

void initialize(MinHeap *heap) {
    heap->size = 0;
}

int parent(int i) { return (i - 1) / 2; }
int leftChild(int i) { return 2 * i + 1; }
int rightChild(int i) { return 2 * i + 2; }

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// Heapify up (for insertion)
void heapifyUp(MinHeap *heap, int index) {
    while (index > 0 && heap->arr[parent(index)] > heap->arr[index]) {
        swap(&heap->arr[parent(index)], &heap->arr[index]);
        index = parent(index);
    }
}

// Insert element
void insert(MinHeap *heap, int value) {
    if (heap->size >= MAX_SIZE) {
        printf("Heap is full\n");
        return;
    }
    
    heap->arr[heap->size] = value;
    heap->size++;
    heapifyUp(heap, heap->size - 1);
}

// Heapify down (for deletion)
void heapifyDown(MinHeap *heap, int index) {
    int smallest = index;
    int left = leftChild(index);
    int right = rightChild(index);
    
    if (left < heap->size && heap->arr[left] < heap->arr[smallest])
        smallest = left;
    
    if (right < heap->size && heap->arr[right] < heap->arr[smallest])
        smallest = right;
    
    if (smallest != index) {
        swap(&heap->arr[index], &heap->arr[smallest]);
        heapifyDown(heap, smallest);
    }
}

// Extract minimum
int extractMin(MinHeap *heap) {
    if (heap->size <= 0) {
        printf("Heap is empty\n");
        return -1;
    }
    
    int min = heap->arr[0];
    heap->arr[0] = heap->arr[heap->size - 1];
    heap->size--;
    heapifyDown(heap, 0);
    
    return min;
}

// Get minimum without removing
int getMin(MinHeap *heap) {
    if (heap->size <= 0) {
        printf("Heap is empty\n");
        return -1;
    }
    return heap->arr[0];
}

void printHeap(MinHeap *heap) {
    for (int i = 0; i < heap->size; i++) {
        printf("%d ", heap->arr[i]);
    }
    printf("\n");
}

int main() {
    MinHeap heap;
    initialize(&heap);
    
    insert(&heap, 3);
    insert(&heap, 2);
    insert(&heap, 15);
    insert(&heap, 5);
    insert(&heap, 4);
    insert(&heap, 45);
    
    printf("Heap: ");
    printHeap(&heap);
    
    printf("Minimum: %d\n", getMin(&heap));
    
    printf("Extracted: %d\n", extractMin(&heap));
    printf("Heap after extraction: ");
    printHeap(&heap);
    
    return 0;
}
```

---

## 21. Γράφος (Graph)

Ο **Γράφος (Graph)** είναι μια μη γραμμική δομή δεδομένων που αποτελείται από κορυφές (κόμβους) που συνδέονται με ακμές. Οι γράφοι μπορεί να είναι κατευθυνόμενοι ή μη κατευθυνόμενοι, με βάρη ή χωρίς βάρη.

### Αναπαράσταση Γράφου: Πίνακας Γειτνίασης

```c
#include <stdio.h>

#define V 5

void addEdge(int graph[V][V], int src, int dest) {
    graph[src][dest] = 1;
    graph[dest][src] = 1;  // For undirected graph
}

void printGraph(int graph[V][V]) {
    printf("Adjacency Matrix:\n");
    for (int i = 0; i < V; i++) {
        for (int j = 0; j < V; j++) {
            printf("%d ", graph[i][j]);
        }
        printf("\n");
    }
}

int main() {
    int graph[V][V] = {0};
    
    addEdge(graph, 0, 1);
    addEdge(graph, 0, 4);
    addEdge(graph, 1, 2);
    addEdge(graph, 1, 3);
    addEdge(graph, 1, 4);
    addEdge(graph, 2, 3);
    addEdge(graph, 3, 4);
    
    printGraph(graph);
    
    return 0;
}
```

### Αναπαράσταση Γράφου: Λίστα Γειτνίασης

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int vertex;
    struct Node *next;
} Node;

typedef struct Graph {
    int numVertices;
    Node **adjLists;
} Graph;

Node* createNode(int v) {
    Node *newNode = (Node*)malloc(sizeof(Node));
    newNode->vertex = v;
    newNode->next = NULL;
    return newNode;
}

Graph* createGraph(int vertices) {
    Graph *graph = (Graph*)malloc(sizeof(Graph));
    graph->numVertices = vertices;
    graph->adjLists = (Node**)malloc(vertices * sizeof(Node*));
    
    for (int i = 0; i < vertices; i++)
        graph->adjLists[i] = NULL;
    
    return graph;
}

void addEdge(Graph *graph, int src, int dest) {
    // Add edge from src to dest
    Node *newNode = createNode(dest);
    newNode->next = graph->adjLists[src];
    graph->adjLists[src] = newNode;
    
    // Add edge from dest to src (undirected)
    newNode = createNode(src);
    newNode->next = graph->adjLists[dest];
    graph->adjLists[dest] = newNode;
}

void printGraph(Graph *graph) {
    for (int v = 0; v < graph->numVertices; v++) {
        Node *temp = graph->adjLists[v];
        printf("Vertex %d: ", v);
        while (temp) {
            printf("%d -> ", temp->vertex);
            temp = temp->next;
        }
        printf("NULL\n");
    }
}

int main() {
    Graph *graph = createGraph(5);
    
    addEdge(graph, 0, 1);
    addEdge(graph, 0, 4);
    addEdge(graph, 1, 2);
    addEdge(graph, 1, 3);
    addEdge(graph, 1, 4);
    addEdge(graph, 2, 3);
    addEdge(graph, 3, 4);
    
    printGraph(graph);
    
    return 0;
}
```

### Αναζήτηση Πρώτα κατά Πλάτος (BFS)

```c
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX 100

typedef struct {
    int items[MAX];
    int front;
    int rear;
} Queue;

void initQueue(Queue *q) {
    q->front = -1;
    q->rear = -1;
}

bool isEmpty(Queue *q) {
    return q->rear == -1;
}

void enqueue(Queue *q, int value) {
    if (q->rear == MAX - 1) return;
    if (q->front == -1) q->front = 0;
    q->items[++q->rear] = value;
}

int dequeue(Queue *q) {
    if (isEmpty(q)) return -1;
    int item = q->items[q->front];
    if (q->front >= q->rear) {
        q->front = -1;
        q->rear = -1;
    } else {
        q->front++;
    }
    return item;
}

void BFS(int graph[][MAX], int vertices, int startVertex) {
    bool visited[MAX] = {false};
    Queue q;
    initQueue(&q);
    
    visited[startVertex] = true;
    enqueue(&q, startVertex);
    
    printf("BFS Traversal: ");
    
    while (!isEmpty(&q)) {
        int currentVertex = dequeue(&q);
        printf("%d ", currentVertex);
        
        for (int i = 0; i < vertices; i++) {
            if (graph[currentVertex][i] == 1 && !visited[i]) {
                visited[i] = true;
                enqueue(&q, i);
            }
        }
    }
    printf("\n");
}

int main() {
    int vertices = 5;
    int graph[MAX][MAX] = {0};
    
    graph[0][1] = graph[1][0] = 1;
    graph[0][4] = graph[4][0] = 1;
    graph[1][2] = graph[2][1] = 1;
    graph[1][3] = graph[3][1] = 1;
    graph[1][4] = graph[4][1] = 1;
    graph[2][3] = graph[3][2] = 1;
    graph[3][4] = graph[4][3] = 1;
    
    BFS(graph, vertices, 0);
    
    return 0;
}
```

### Αναζήτηση Πρώτα κατά Βάθος (DFS)

```c
#include <stdio.h>
#include <stdbool.h>

#define MAX 100

void DFSUtil(int graph[][MAX], int vertices, int vertex, bool visited[]) {
    visited[vertex] = true;
    printf("%d ", vertex);
    
    for (int i = 0; i < vertices; i++) {
        if (graph[vertex][i] == 1 && !visited[i]) {
            DFSUtil(graph, vertices, i, visited);
        }
    }
}

void DFS(int graph[][MAX], int vertices, int startVertex) {
    bool visited[MAX] = {false};
    printf("DFS Traversal: ");
    DFSUtil(graph, vertices, startVertex, visited);
    printf("\n");
}

int main() {
    int vertices = 5;
    int graph[MAX][MAX] = {0};
    
    graph[0][1] = graph[1][0] = 1;
    graph[0][4] = graph[4][0] = 1;
    graph[1][2] = graph[2][1] = 1;
    graph[1][3] = graph[3][1] = 1;
    graph[1][4] = graph[4][1] = 1;
    graph[2][3] = graph[3][2] = 1;
    graph[3][4] = graph[4][3] = 1;
    
    DFS(graph, vertices, 0);
    
    return 0;
}
```

---

## 22. Άπληστος Αλγόριθμος (Greedy Algorithm)

Οι **Άπληστοι αλγόριθμοι (Greedy algorithms)** κατασκευάζουν λύσεις κάνοντας τοπικά βέλτιστες επιλογές σε κάθε βήμα, με την ελπίδα να βρουν ένα συνολικό (παγκόσμιο) βέλτιστο.

### Πρόβλημα Επιλογής Δραστηριοτήτων (Activity Selection)

```c
#include <stdio.h>

typedef struct {
    int start;
    int finish;
} Activity;

void swap(Activity *a, Activity *b) {
    Activity temp = *a;
    *a = *b;
    *b = temp;
}

void sortByFinishTime(Activity activities[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (activities[j].finish > activities[j + 1].finish) {
                swap(&activities[j], &activities[j + 1]);
            }
        }
    }
}

void activitySelection(Activity activities[], int n) {
    sortByFinishTime(activities, n);
    
    printf("Selected activities:\n");
    int lastSelected = 0;
    printf("Activity (%d, %d)\n", activities[0].start, activities[0].finish);
    
    for (int i = 1; i < n; i++) {
        if (activities[i].start >= activities[lastSelected].finish) {
            printf("Activity (%d, %d)\n", activities[i].start, activities[i].finish);
            lastSelected = i;
        }
    }
}

int main() {
    Activity activities[] = {
        {1, 3}, {2, 4}, {3, 5}, {0, 6}, {5, 7}, {8, 9}, {5, 9}
    };
    int n = sizeof(activities) / sizeof(activities[0]);
    
    activitySelection(activities, n);
    
    return 0;
}
```

### Κλασματικό Πρόβλημα Σακιδίου (Fractional Knapsack)

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int weight;
    int value;
    double ratio;
} Item;

int compare(const void *a, const void *b) {
    Item *item1 = (Item*)a;
    Item *item2 = (Item*)b;
    return (item2->ratio > item1->ratio) - (item2->ratio < item1->ratio);
}

double fractionalKnapsack(Item items[], int n, int capacity) {
    // Calculate value-to-weight ratio
    for (int i = 0; i < n; i++) {
        items[i].ratio = (double)items[i].value / items[i].weight;
    }
    
    // Sort by ratio
    qsort(items, n, sizeof(Item), compare);
    
    double totalValue = 0.0;
    int currentWeight = 0;
    
    for (int i = 0; i < n; i++) {
        if (currentWeight + items[i].weight <= capacity) {
            currentWeight += items[i].weight;
            totalValue += items[i].value;
        } else {
            int remaining = capacity - currentWeight;
            totalValue += items[i].ratio * remaining;
            break;
        }
    }
    
    return totalValue;
}

int main() {
    Item items[] = {{10, 60}, {20, 100}, {30, 120}};
    int n = sizeof(items) / sizeof(items[0]);
    int capacity = 50;
    
    double maxValue = fractionalKnapsack(items, n, capacity);
    printf("Maximum value: %.2f\n", maxValue);
    
    return 0;
}
```

---

## 23. Δυναμικός Προγραμματισμός (Dynamic Programming)

Ο **Δυναμικός Προγραμματισμός (Dynamic Programming)** επιλύει σύνθετα προβλήματα διασπώντας τα σε επικαλυπτόμενα υποπροβλήματα και αποθηκεύοντας αποτελέσματα για την αποφυγή περιττών υπολογισμών.

### Ακολουθία Fibonacci with Memoization

```c
#include <stdio.h>
#include <string.h>

#define MAX 100

int memo[MAX];

int fibonacciMemo(int n) {
    if (n <= 1) return n;
    
    if (memo[n] != -1)
        return memo[n];
    
    memo[n] = fibonacciMemo(n - 1) + fibonacciMemo(n - 2);
    return memo[n];
}

int main() {
    memset(memo, -1, sizeof(memo));
    
    int n = 10;
    printf("Fibonacci(%d) = %d\n", n, fibonacciMemo(n));
    
    return 0;
}
```

### Πρόβλημα Σακιδίου 0/1 (0/1 Knapsack)

```c
#include <stdio.h>

int max(int a, int b) {
    return (a > b) ? a : b;
}

int knapsack(int weights[], int values[], int n, int capacity) {
    int dp[n + 1][capacity + 1];
    
    for (int i = 0; i <= n; i++) {
        for (int w = 0; w <= capacity; w++) {
            if (i == 0 || w == 0)
                dp[i][w] = 0;
            else if (weights[i - 1] <= w)
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], 
                              dp[i - 1][w]);
            else
                dp[i][w] = dp[i - 1][w];
        }
    }
    
    return dp[n][capacity];
}

int main() {
    int values[] = {60, 100, 120};
    int weights[] = {10, 20, 30};
    int capacity = 50;
    int n = sizeof(values) / sizeof(values[0]);
    
    printf("Maximum value: %d\n", knapsack(weights, values, n, capacity));
    
    return 0;
}
```

### Μεγαλύτερη Κοινή Υποακολουθία (Longest Common Subsequence - LCS)

```c
#include <stdio.h>
#include <string.h>

int max(int a, int b) {
    return (a > b) ? a : b;
}

int LCS(char *X, char *Y, int m, int n) {
    int dp[m + 1][n + 1];
    
    for (int i = 0; i <= m; i++) {
        for (int j = 0; j <= n; j++) {
            if (i == 0 || j == 0)
                dp[i][j] = 0;
            else if (X[i - 1] == Y[j - 1])
                dp[i][j] = dp[i - 1][j - 1] + 1;
            else
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
        }
    }
    
    return dp[m][n];
}

int main() {
    char X[] = "AGGTAB";
    char Y[] = "GXTXAYB";
    
    int m = strlen(X);
    int n = strlen(Y);
    
    printf("Length of LCS: %d\n", LCS(X, Y, m, n));
    
    return 0;
}
```

---

## 24. Άλλοι Αλγόριθμοι

### Οπισθοδρόμηση (Backtracking): Πρόβλημα N-Βασιλισσών

```c
#include <stdio.h>
#include <stdbool.h>

#define N 8

void printSolution(int board[N][N]) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++)
            printf("%c ", board[i][j] ? 'Q' : '.');
        printf("\n");
    }
    printf("\n");
}

bool isSafe(int board[N][N], int row, int col) {
    // Check row on left side
    for (int i = 0; i < col; i++)
        if (board[row][i])
            return false;
    
    // Check upper diagonal on left side
    for (int i = row, j = col; i >= 0 && j >= 0; i--, j--)
        if (board[i][j])
            return false;
    
    // Check lower diagonal on left side
    for (int i = row, j = col; j >= 0 && i < N; i++, j--)
        if (board[i][j])
            return false;
    
    return true;
}

bool solveNQueensUtil(int board[N][N], int col) {
    if (col >= N) {
        printSolution(board);
        return true;
    }
    
    bool res = false;
    for (int i = 0; i < N; i++) {
        if (isSafe(board, i, col)) {
            board[i][col] = 1;
            res = solveNQueensUtil(board, col + 1) || res;
            board[i][col] = 0;  // Backtrack
        }
    }
    
    return res;
}

void solveNQueens() {
    int board[N][N] = {0};
    
    if (!solveNQueensUtil(board, 0))
        printf("Solution does not exist\n");
}

int main() {
    solveNQueens();
    return 0;
}
```

### Πράξεις σε Επίπεδο Bit (Bitwise Operations)

```c
#include <stdio.h>

void printBinary(int n) {
    for (int i = 31; i >= 0; i--) {
        printf("%d", (n >> i) & 1);
        if (i % 4 == 0) printf(" ");
    }
    printf("\n");
}

int main() {
    int a = 5;   // 0101
    int b = 3;   // 0011
    
    printf("a = ");
    printBinary(a);
    printf("b = ");
    printBinary(b);
    
    printf("a & b = ");
    printBinary(a & b);  // AND
    
    printf("a | b = ");
    printBinary(a | b);  // OR
    
    printf("a ^ b = ");
    printBinary(a ^ b);  // XOR
    
    printf("~a = ");
    printBinary(~a);     // NOT
    
    printf("a << 1 = ");
    printBinary(a << 1); // Left shift
    
    printf("a >> 1 = ");
    printBinary(a >> 1); // Right shift
    
    // Check if number is power of 2
    int n = 16;
    if ((n & (n - 1)) == 0 && n != 0)
        printf("%d is a power of 2\n", n);
    
    return 0;
}
```

---

## Βέλτιστες Πρακτικές Διαχείρισης Μνήμης

1. **Πάντα να απελευθερώνετε τη δυναμικά κατανεμημένη μνήμη**
   ```c
   int *ptr = (int*)malloc(sizeof(int) * 10);
   // Use ptr...
   free(ptr);
   ptr = NULL;  // Avoid dangling pointer
   ```

2. **Ελέγχετε για αποτυχίες κατανομής**
   ```c
   int *ptr = (int*)malloc(sizeof(int) * 10);
   if (ptr == NULL) {
       fprintf(stderr, "Memory allocation failed\n");
       exit(1);
   }
   ```

3. **Αποφεύγετε τις διαρροές μνήμης (memory leaks)**
   - Απελευθερώστε όλη τη κατανεμημένη μνήμη πριν την έξοδο του προγράμματος
   - Απελευθερώστε τη μνήμη με αντίστροφη σειρά κατανομής για εμφωλευμένες δομές

4. **Χρησιμοποιείτε το valgrind στο Linux για τον εντοπισμό προβλημάτων μνήμης**
   ```bash
   gcc -g program.c -o program
   valgrind --leak-check=full ./program
   ```

---

## Συγκεντρωτικός Πίνακας Πολυπλοκότητας

| Algorithm | Time (Best) | Time (Avg) | Time (Worst) | Space |
|-----------|-------------|------------|--------------|-------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) |
| Linear Search | O(1) | O(n) | O(n) | O(1) |
| Binary Search | O(1) | O(log n) | O(log n) | O(1) |
| BFS | O(V+E) | O(V+E) | O(V+E) | O(V) |
| DFS | O(V+E) | O(V+E) | O(V+E) | O(V) |

---

## Πρόσθετοι Πόροι

- Πρακτική εξάσκηση σε πλατφόρμες όπως LeetCode, HackerRank, Codeforces
- Μελέτη του βιβλίου "Introduction to Algorithms" των CLRS
- Χρήση διαδικτυακών εργαλείων οπτικοποίησης (visualizers) για δομές δεδομένων και αλγορίθμους
- Συμμετοχή σε κοινότητες ανταγωνιστικού προγραμματισμού

---

**Τέλος Οδηγού**