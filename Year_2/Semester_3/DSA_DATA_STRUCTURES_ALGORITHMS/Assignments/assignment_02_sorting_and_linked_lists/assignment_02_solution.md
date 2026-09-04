## 1. Binary Search

Binary search works by repeatedly dividing the search space in half. It compares the element in the middle position with the target value and decides whether to continue searching in the left or right half of the array. At each step, the size of the search space is reduced by half, ending either in finding the element or in an empty subarray.

**Prerequisite:** The array must be **sorted**. Without sorting, the logic of dividing the search space based on comparison with the middle element does not work.

## 2. Recursion vs Iteration

Recursion is considered an alternative to iteration because both techniques can express the same computational procedures. Recursion can be replaced by iteration with an explicit call stack, while iteration can be replaced by recursion using a queue.


**C++:**
```cpp
#include <iostream>

// Recursive approach
int factorialRecursive(int n) {
    if (n == 0) return 1;
    return n * factorialRecursive(n - 1);
}

// Iterative approach
int factorialIterative(int n) {
    int result = 1;
    for (int i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
}

int main() {
    std::cout << "Factorial of 5 (recursive): " << factorialRecursive(5) << std::endl;
    std::cout << "Factorial of 5 (iterative): " << factorialIterative(5) << std::endl;
    return 0;
}
```


## 3. Sorting Comparison

| Feature | Insertion Sort | Selection Sort | Bubble Sort |
|---|---|---|---|
| **Average Complexity** | O(n²)  | O(n²)  | O(n²)  |
| **Best Case** | O(n)  | O(n²)  | O(n)  |
| **Worst Case** | O(n²)  | O(n²)  | O(n²)  |
| **Adaptability** | Yes  | No  | No  |
| **Swaps** | Fewer  | Minimum  | Many  |
| **Speed** | Faster  | Moderate  | Slower  |

Insertion sort compares each element with the sorted portion to its left and places it in the correct position. Selection sort finds the minimum element and places it at the beginning. Bubble sort repeatedly compares and swaps adjacent elements.

**C++:**

```cpp
#include <iostream>
#include <vector>

void insertionSort(std::vector<int>& arr) {
    for (int i = 1; i < arr.size(); i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

void selectionSort(std::vector<int>& arr) {
    for (int i = 0; i < arr.size() - 1; i++) {
        int min_idx = i;
        for (int j = i + 1; j < arr.size(); j++) {
            if (arr[j] < arr[min_idx])
                min_idx = j;
        }
        std::swap(arr[min_idx], arr[i]);
    }
}

void bubbleSort(std::vector<int>& arr) {
    int n = arr.size();
    bool swapped;
    for (int i = 0; i < n - 1; i++) {
        swapped = false;
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                std::swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        }
        if (!swapped) break;
    }
}

void printArray(const std::vector<int>& arr) {
    for (int val : arr)
        std::cout << val << " ";
    std::cout << std::endl;
}

int main() {
    std::vector<int> arr1 = {64, 34, 25, 12, 22, 11, 90};
    std::vector<int> arr2 = arr1;
    std::vector<int> arr3 = arr1;
    
    insertionSort(arr1);
    std::cout << "Insertion Sort: ";
    printArray(arr1);
    
    selectionSort(arr2);
    std::cout << "Selection Sort: ";
    printArray(arr2);
    
    bubbleSort(arr3);
    std::cout << "Bubble Sort: ";
    printArray(arr3);
    
    return 0;
}
```


## 4. Divide and Conquer - Merge Sort

**Merge Sort** applies the Divide and Conquer strategy.

**Phases:**
1. **Divide:** Splitting the array in half into two subarrays
2. **Conquer:** Recursively sorting each subarray until single elements remain
3. **Combine:** Merging the sorted subarrays into a single sorted array

The process continues recursively until all elements are merged into a fully sorted array.



**C++:**

```cpp
#include <iostream>
#include <vector>

void merge(std::vector<int>& arr, int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;
    
    std::vector<int> L(n1), R(n2);
    
    for (int i = 0; i < n1; i++)
        L[i] = arr[left + i];
    for (int j = 0; j < n2; j++)
        R[j] = arr[mid + 1 + j];
    
    int i = 0, j = 0, k = left;
    
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k++] = L[i++];
        } else {
            arr[k++] = R[j++];
        }
    }
    
    while (i < n1) arr[k++] = L[i++];
    while (j < n2) arr[k++] = R[j++];
}

void mergeSort(std::vector<int>& arr, int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        
        mergeSort(arr, left, mid);      // Divide left
        mergeSort(arr, mid + 1, right); // Divide right
        merge(arr, left, mid, right);   // Combine
    }
}

int main() {
    std::vector<int> arr = {70, 50, 30, 10, 20, 40, 60};
    
    std::cout << "Original array: ";
    for (int val : arr) std::cout << val << " ";
    std::cout << std::endl;
    
    mergeSort(arr, 0, arr.size() - 1);
    
    std::cout << "Sorted array: ";
    for (int val : arr) std::cout << val << " ";
    std::cout << std::endl;
    
    return 0;
}
```


## 5. Complexity Table

| Algorithm | Complexity (Average) |
|---|---|
| Selection Sort | O(n²)  |
| Insertion Sort | O(n²)  |
| Merge Sort | O(n log n)  |
| Quick Sort | O(n log n)  |