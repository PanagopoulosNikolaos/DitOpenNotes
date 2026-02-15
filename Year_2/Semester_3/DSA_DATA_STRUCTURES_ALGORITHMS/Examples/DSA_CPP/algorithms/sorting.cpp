#include <iostream>
#include <vector>
#include <algorithm>
#include <chrono>

/**
 * @brief Collection of sorting algorithm implementations in C++
 * 
 * Sorting is the process of arranging elements in a specific order (ascending or descending).
 * Different sorting algorithms have different time/space complexities and use cases.
 * 
 * Algorithm Comparison:
 * ┌─────────────────┬──────────┬──────────┬──────────┬────────┬─────────┐
 * │ Algorithm       │ Best     │ Average  │ Worst    │ Space  │ Stable  │
 * ├─────────────────┼──────────┼──────────┼──────────┼────────┼─────────┤
 * │ Bubble Sort     │ O(n)     │ O(n²)    │ O(n²)    │ O(1)   │ Yes     │
 * │ Selection Sort  │ O(n²)    │ O(n²)    │ O(n²)    │ O(1)   │ No      │
 * │ Insertion Sort  │ O(n)     │ O(n²)    │ O(n²)    │ O(1)   │ Yes     │
 * │ Quick Sort      │ O(n log n)│O(n log n)│ O(n²)    │ O(log n)│No      │
 * │ Merge Sort      │ O(n log n)│O(n log n)│O(n log n)│ O(n)   │ Yes     │
 * │ Counting Sort   │ O(n+k)   │ O(n+k)   │ O(n+k)   │ O(k)   │ Yes     │
 * │ Radix Sort      │ O(d·n)   │ O(d·n)   │ O(d·n)   │ O(n+k) │ Yes     │
 * └─────────────────┴──────────┴──────────┴──────────┴────────┴─────────┘
 * 
 * Stable: Maintains relative order of equal elements
 * In-place: Sorts within original array (low space complexity)
 * 
 * Common Use Cases:
 * - Bubble Sort: Educational purposes, nearly sorted data
 * - Selection Sort: Small datasets, memory-constrained systems
 * - Insertion Sort: Small datasets, nearly sorted data, online sorting
 * - Quick Sort: General purpose (most programming languages use variants)
 * - Merge Sort: Linked lists, stable sorting needed, external sorting
 * - Counting Sort: Integer sorting with limited range
 * - Radix Sort: Integer/string sorting, distributed systems
 */
class SortingAlgorithms {
public:
    /**
     * @brief BUBBLE SORT
     * 
     * Repeatedly steps through the list, compares adjacent elements and swaps them
     * if they are in wrong order. The pass through the list is repeated until sorted.
     * 
     * How it works:
     * - Compare adjacent elements
     * - Swap if they're in wrong order
     * - After each pass, largest element "bubbles" to end
     * - Repeat until no swaps needed
     * 
     * Time: O(n²) average/worst, O(n) best
     * Space: O(1)
     * Stable: Yes
     */
    static std::vector<int> bubbleSort(std::vector<int> arr) {
        int n = arr.size();

        for (int i = 0; i < n; ++i) {
            bool swapped = false;

            for (int j = 0; j < n - i - 1; ++j) {
                if (arr[j] > arr[j + 1]) {
                    std::swap(arr[j], arr[j + 1]);
                    swapped = true;
                }
            }

            if (!swapped) {
                break;  // Already sorted
            }
        }

        return arr;
    }

    /**
     * @brief SELECTION SORT
     * 
     * Divides array into sorted and unsorted portions. Repeatedly finds minimum
     * element from unsorted portion and places it at beginning of unsorted portion.
     * 
     * How it works:
     * - Find minimum element in unsorted array
     * - Swap it with first unsorted element
     * - Move boundary of sorted portion one position right
     * - Repeat until entire array is sorted
     * 
     * Time: O(n²) for all cases
     * Space: O(1)
     * Stable: No
     */
    static std::vector<int> selectionSort(std::vector<int> arr) {
        int n = arr.size();

        for (int i = 0; i < n; ++i) {
            int minIdx = i;

            for (int j = i + 1; j < n; ++j) {
                if (arr[j] < arr[minIdx]) {
                    minIdx = j;
                }
            }

            std::swap(arr[i], arr[minIdx]);
        }

        return arr;
    }

    /**
     * @brief INSERTION SORT
     * 
     * Builds final sorted array one element at a time. Takes each element and
     * inserts it into its correct position in the sorted portion.
     * 
     * How it works:
     * - Start with second element (first is considered sorted)
     * - Compare with elements in sorted portion
     * - Shift larger elements right
     * - Insert current element in correct position
     * - Repeat for all elements
     * 
     * Time: O(n²) average/worst, O(n) best (nearly sorted)
     * Space: O(1)
     * Stable: Yes
     */
    static std::vector<int> insertionSort(std::vector<int> arr) {
        int n = arr.size();

        for (int i = 1; i < n; ++i) {
            int key = arr[i];
            int j = i - 1;

            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                --j;
            }

            arr[j + 1] = key;
        }

        return arr;
    }

    /**
     * @brief QUICK SORT
     * 
     * Divide-and-conquer algorithm. Picks a pivot element and partitions array
     * around it, then recursively sorts subarrays.
     * 
     * How it works:
     * - Choose a pivot element
     * - Partition: rearrange so elements < pivot are left, > pivot are right
     * - Recursively apply to left and right partitions
     * - Base case: arrays of size 0 or 1 are already sorted
     * 
     * Time: O(n log n) average, O(n²) worst (rare with good pivot selection)
     * Space: O(log n) for recursion stack
     * Stable: No
     */
    static std::vector<int> quickSort(std::vector<int> arr) {
        quickSortRecursive(arr, 0, arr.size() - 1);
        return arr;
    }

private:
    static void quickSortRecursive(std::vector<int>& arr, int low, int high) {
        if (low < high) {
            int pi = partition(arr, low, high);
            quickSortRecursive(arr, low, pi - 1);
            quickSortRecursive(arr, pi + 1, high);
        }
    }

    static int partition(std::vector<int>& arr, int low, int high) {
        int pivot = arr[high];
        int i = low - 1;

        for (int j = low; j < high; ++j) {
            if (arr[j] <= pivot) {
                ++i;
                std::swap(arr[i], arr[j]);
            }
        }

        std::swap(arr[i + 1], arr[high]);
        return i + 1;
    }

public:
    /**
     * @brief MERGE SORT
     * 
     * Divide-and-conquer algorithm. Divides array into two halves, recursively
     * sorts them, then merges the sorted halves.
     * 
     * How it works:
     * - Divide array into two halves
     * - Recursively sort both halves
     * - Merge the sorted halves
     * - Base case: arrays of size 1 are already sorted
     * 
     * Time: O(n log n) for all cases
     * Space: O(n) for temporary arrays
     * Stable: Yes
     */
    static std::vector<int> mergeSort(std::vector<int> arr) {
        if (arr.size() <= 1) {
            return arr;
        }

        int mid = arr.size() / 2;
        std::vector<int> left(arr.begin(), arr.begin() + mid);
        std::vector<int> right(arr.begin() + mid, arr.end());

        left = mergeSort(left);
        right = mergeSort(right);

        return merge(left, right);
    }

private:
    static std::vector<int> merge(const std::vector<int>& left, const std::vector<int>& right) {
        std::vector<int> result;
        int i = 0, j = 0;

        while (i < left.size() && j < right.size()) {
            if (left[i] <= right[j]) {
                result.push_back(left[i]);
                ++i;
            } else {
                result.push_back(right[j]);
                ++j;
            }
        }

        // Add remaining elements
        while (i < left.size()) {
            result.push_back(left[i]);
            ++i;
        }
        while (j < right.size()) {
            result.push_back(right[j]);
            ++j;
        }

        return result;
    }

public:
    /**
     * @brief COUNTING SORT
     * 
     * Non-comparison based sorting for integers in limited range. Counts occurrences
     * of each value and uses counts to place elements in sorted order.
     * 
     * How it works:
     * - Count frequency of each element
     * - Calculate cumulative counts
     * - Place elements in output array using counts
     * - Works only for non-negative integers in limited range
     * 
     * Time: O(n + k) where k is range of input
     * Space: O(k)
     * Stable: Yes
     */
    static std::vector<int> countingSort(std::vector<int> arr) {
        if (arr.empty()) {
            return arr;
        }

        int maxVal = *std::max_element(arr.begin(), arr.end());
        int minVal = *std::min_element(arr.begin(), arr.end());
        int range = maxVal - minVal + 1;

        std::vector<int> count(range, 0);
        std::vector<int> output(arr.size());

        // Count occurrences
        for (int num : arr) {
            count[num - minVal]++;
        }

        // Calculate cumulative counts
        for (int i = 1; i < range; ++i) {
            count[i] += count[i - 1];
        }

        // Place elements in output array
        for (int i = arr.size() - 1; i >= 0; --i) {
            output[count[arr[i] - minVal] - 1] = arr[i];
            count[arr[i] - minVal]--;
        }

        return output;
    }

    /**
     * @brief RADIX SORT
     * 
     * Non-comparison based sorting that processes digits from least significant
     * to most significant using a stable sorting algorithm (counting sort).
     * 
     * How it works:
     * - Sort by least significant digit
     * - Sort by next digit (maintaining stability)
     * - Repeat for all digits
     * - Uses counting sort for each digit
     * 
     * Time: O(d·n) where d is number of digits
     * Space: O(n + k)
     * Stable: Yes
     */
    static std::vector<int> radixSort(std::vector<int> arr) {
        if (arr.empty()) {
            return arr;
        }

        int maxVal = *std::max_element(arr.begin(), arr.end());

        for (int exp = 1; maxVal / exp > 0; exp *= 10) {
            countingSortByDigit(arr, exp);
        }

        return arr;
    }

private:
    static void countingSortByDigit(std::vector<int>& arr, int exp) {
        int n = arr.size();
        std::vector<int> output(n);
        std::vector<int> count(10, 0);

        // Count occurrences of each digit
        for (int i = 0; i < n; ++i) {
            int index = arr[i] / exp;
            count[index % 10]++;
        }

        // Calculate cumulative counts
        for (int i = 1; i < 10; ++i) {
            count[i] += count[i - 1];
        }

        // Place elements in output array
        for (int i = n - 1; i >= 0; --i) {
            int index = arr[i] / exp;
            output[count[index % 10] - 1] = arr[i];
            count[index % 10]--;
        }

        // Copy output array back to original array
        for (int i = 0; i < n; ++i) {
            arr[i] = output[i];
        }
    }
};

// Example usage
int main() {
    std::vector<int> testArr = {64, 34, 25, 12, 22, 11, 90};

    std::cout << "Original array: ";
    for (int val : testArr) {
        std::cout << val << " ";
    }
    std::cout << std::endl << std::endl;

    std::cout << "Bubble Sort:    ";
    auto result = SortingAlgorithms::bubbleSort(testArr);
    for (int val : result) {
        std::cout << val << " ";
    }
    std::cout << std::endl;

    std::cout << "Selection Sort: ";
    result = SortingAlgorithms::selectionSort(testArr);
    for (int val : result) {
        std::cout << val << " ";
    }
    std::cout << std::endl;

    std::cout << "Insertion Sort: ";
    result = SortingAlgorithms::insertionSort(testArr);
    for (int val : result) {
        std::cout << val << " ";
    }
    std::cout << std::endl;

    std::cout << "Quick Sort:     ";
    result = SortingAlgorithms::quickSort(testArr);
    for (int val : result) {
        std::cout << val << " ";
    }
    std::cout << std::endl;

    std::cout << "Merge Sort:     ";
    result = SortingAlgorithms::mergeSort(testArr);
    for (int val : result) {
        std::cout << val << " ";
    }
    std::cout << std::endl;

    std::cout << "Counting Sort:  ";
    result = SortingAlgorithms::countingSort(testArr);
    for (int val : result) {
        std::cout << val << " ";
    }
    std::cout << std::endl;

    std::cout << "Radix Sort:     ";
    result = SortingAlgorithms::radixSort(testArr);
    for (int val : result) {
        std::cout << val << " ";
    }
    std::cout << std::endl;

    return 0;
}