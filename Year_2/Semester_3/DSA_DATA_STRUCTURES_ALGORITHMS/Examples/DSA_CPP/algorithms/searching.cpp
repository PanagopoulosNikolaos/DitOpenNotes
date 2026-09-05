#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <climits>

/**
 * @brief Collection of searching algorithm implementations in C++
 * 
 * Searching is the process of finding a specific element in a data structure.
 * Different algorithms are suitable for different data organizations.
 * 
 * Algorithm Comparison:
 * ┌─────────────────┬──────────┬──────────┬──────────┬──────────────────┐
 * │ Algorithm       │ Best     │ Average  │ Worst    │ Requirements     │
 * ├─────────────────┼──────────┼──────────┼──────────┼──────────────────┤
 * │ Linear Search   │ O(1)     │ O(n)     │ O(n)     │ None             │
 * │ Binary Search   │ O(1)     │ O(log n) │ O(log n) │ Sorted array     │
 * │ Jump Search     │ O(1)     │ O(√n)    │ O(√n)    │ Sorted array     │
 * │ Interpolation   │ O(1)     │ O(log log n)│O(n)   │ Sorted, uniform  │
 * │ Exponential     │ O(1)     │ O(log n) │ O(log n) │ Sorted, unbounded│
 * └─────────────────┴──────────┴──────────┴──────────┴──────────────────┘
 * 
 * Common Use Cases:
 * - Linear Search: Unsorted data, small datasets
 * - Binary Search: Sorted arrays, most common search
 * - Jump Search: Sorted arrays with costly comparisons
 * - Interpolation: Uniformly distributed sorted data
 * - Exponential: Unbounded/infinite sorted arrays
 */
class SearchingAlgorithms {
public:
    /**
     * @brief LINEAR SEARCH
     * 
     * Sequentially checks each element until target is found or end is reached.
     * Works on both sorted and unsorted arrays.
     * 
     * How it works:
     * - Start from first element
     * - Compare each element with target
     * - If match found, return index
     * - If end reached without match, return -1
     * 
     * Time: O(n) for all cases
     * Space: O(1)
     */
    static int linearSearch(const std::vector<int>& arr, int target) {
        for (int i = 0; i < arr.size(); ++i) {
            if (arr[i] == target) {
                return i;
            }
        }
        return -1;
    }

    /**
     * @brief BINARY SEARCH
     * 
     * Efficiently finds target in sorted array by repeatedly dividing search
     * interval in half. Compares target with middle element.
     * 
     * How it works:
     * - Start with entire array
     * - Compare target with middle element
     * - If match, return index
     * - If target < middle, search left half
     * - If target > middle, search right half
     * - Repeat until found or search space is empty
     * 
     * Time: O(log n)
     * Space: O(1) iterative, O(log n) recursive
     * Requires: Sorted array
     */
    static int binarySearch(const std::vector<int>& arr, int target) {
        int left = 0, right = arr.size() - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (arr[mid] == target) {
                return mid;
            } else if (arr[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return -1;
    }

    /**
     * @brief BINARY SEARCH (Recursive)
     * 
     * Recursive implementation of binary search.
     * Same logic but uses recursion instead of iteration.
     * 
     * Time: O(log n)
     * Space: O(log n) due to recursion stack
     */
    static int binarySearchRecursive(const std::vector<int>& arr, int target, int left = 0, int right = -1) {
        if (right == -1) {
            right = arr.size() - 1;
        }

        if (left > right) {
            return -1;
        }

        int mid = left + (right - left) / 2;

        if (arr[mid] == target) {
            return mid;
        } else if (arr[mid] < target) {
            return binarySearchRecursive(arr, target, mid + 1, right);
        } else {
            return binarySearchRecursive(arr, target, left, mid - 1);
        }
    }

    /**
     * @brief JUMP SEARCH
     * 
     * Works on sorted arrays. Jumps ahead by fixed steps, then performs
     * linear search in the block where element may exist.
     * 
     * How it works:
     * - Jump ahead by √n steps
     * - When arr[jump] > target, do linear search in previous block
     * - Optimal jump size is √n
     * 
     * Time: O(√n)
     * Space: O(1)
     * Requires: Sorted array
     */
    static int jumpSearch(const std::vector<int>& arr, int target) {
        int n = arr.size();
        int step = static_cast<int>(std::sqrt(n));
        int prev = 0;

        while (prev < n && arr[std::min(step, n) - 1] < target) {
            prev = step;
            step += static_cast<int>(std::sqrt(n));
            if (prev >= n) {
                return -1;
            }
        }

        while (prev < n && arr[prev] < target) {
            prev++;
            if (prev == std::min(step, n)) {
                return -1;
            }
        }

        if (prev < n && arr[prev] == target) {
            return prev;
        }

        return -1;
    }

    /**
     * @brief INTERPOLATION SEARCH
     * 
     * Improved binary search for uniformly distributed sorted arrays.
     * Estimates position based on value distribution.
     * 
     * How it works:
     * - Similar to binary search
     * - Instead of middle, calculates probable position:
     *   pos = low + [(target - arr[low]) * (high - low)] / (arr[high] - arr[low])
     * - Works best when data is uniformly distributed
     * 
     * Time: O(log log n) average for uniform distribution, O(n) worst
     * Space: O(1)
     * Requires: Sorted array with uniform distribution
     */
    static int interpolationSearch(const std::vector<int>& arr, int target) {
        int left = 0, right = arr.size() - 1;

        while (left <= right && arr[left] <= target && target <= arr[right]) {
            if (left == right) {
                if (arr[left] == target) {
                    return left;
                }
                return -1;
            }

            int pos = left + ((target - arr[left]) * (right - left)) / (arr[right] - arr[left]);

            if (arr[pos] == target) {
                return pos;
            } else if (arr[pos] < target) {
                left = pos + 1;
            } else {
                right = pos - 1;
            }
        }

        return -1;
    }

    /**
     * @brief EXPONENTIAL SEARCH
     * 
     * Useful for unbounded/infinite sorted arrays. Finds range where
     * element exists, then applies binary search.
     * 
     * How it works:
     * - Start with index 1
     * - Double index until arr[index] >= target
     * - Apply binary search in range [index/2, index]
     * 
     * Time: O(log n)
     * Space: O(1)
     * Requires: Sorted array
     */
    static int exponentialSearch(const std::vector<int>& arr, int target) {
        if (arr.empty()) {
            return -1;
        }

        if (arr[0] == target) {
            return 0;
        }

        int i = 1;
        while (i < arr.size() && arr[i] <= target) {
            i *= 2;
        }

        // Binary search in the range [i/2, min(i, n-1)]
        std::vector<int> subArr(arr.begin() + i/2, arr.begin() + std::min(i, static_cast<int>(arr.size())));
        int result = binarySearch(subArr, target);
        
        if (result != -1) {
            return result + i/2;
        }
        return -1;
    }

    /**
     * @brief TERNARY SEARCH
     * 
     * Divide-and-conquer algorithm that divides array into three parts.
     * Similar to binary search but with two mid points.
     * 
     * How it works:
     * - Divide array into three equal parts
     * - Determine which third contains target
     * - Recursively search that third
     * 
     * Time: O(log₃ n) ≈ O(log n)
     * Space: O(log n) due to recursion
     * Requires: Sorted array
     */
    static int ternarySearch(const std::vector<int>& arr, int target, int left = 0, int right = -1) {
        if (right == -1) {
            right = arr.size() - 1;
        }

        if (left > right) {
            return -1;
        }

        int mid1 = left + (right - left) / 3;
        int mid2 = right - (right - left) / 3;

        if (arr[mid1] == target) {
            return mid1;
        }
        if (arr[mid2] == target) {
            return mid2;
        }

        if (target < arr[mid1]) {
            return ternarySearch(arr, target, left, mid1 - 1);
        } else if (target > arr[mid2]) {
            return ternarySearch(arr, target, mid2 + 1, right);
        } else {
            return ternarySearch(arr, target, mid1 + 1, mid2 - 1);
        }
    }
};

/**
 * @brief Advanced searching techniques
 */
class AdvancedSearching {
public:
    /**
     * @brief Find first occurrence of target in sorted array with duplicates
     */
    static int findFirstOccurrence(const std::vector<int>& arr, int target) {
        int left = 0, right = arr.size() - 1;
        int result = -1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (arr[mid] == target) {
                result = mid;
                right = mid - 1;  // Continue searching in left half
            } else if (arr[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return result;
    }

    /**
     * @brief Find last occurrence of target in sorted array with duplicates
     */
    static int findLastOccurrence(const std::vector<int>& arr, int target) {
        int left = 0, right = arr.size() - 1;
        int result = -1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (arr[mid] == target) {
                result = mid;
                left = mid + 1;  // Continue searching in right half
            } else if (arr[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return result;
    }

    /**
     * @brief Count occurrences of target in sorted array
     */
    static int countOccurrences(const std::vector<int>& arr, int target) {
        int first = findFirstOccurrence(arr, target);
        if (first == -1) {
            return 0;
        }
        int last = findLastOccurrence(arr, target);
        return last - first + 1;
    }
};

// Example usage
#ifndef SKIP_STANDALONE_MAIN
int main() {
    // Test array (sorted for most algorithms)
    std::vector<int> sortedArr = {2, 5, 8, 12, 16, 23, 38, 45, 56, 67, 78};
    int target = 23;

    std::cout << "Array: ";
    for (int val : sortedArr) {
        std::cout << val << " ";
    }
    std::cout << std::endl;
    std::cout << "Target: " << target << std::endl << std::endl;

    std::cout << "Linear Search:        Index " << SearchingAlgorithms::linearSearch(sortedArr, target) << std::endl;
    std::cout << "Binary Search:        Index " << SearchingAlgorithms::binarySearch(sortedArr, target) << std::endl;
    std::cout << "Binary (Recursive):   Index " << SearchingAlgorithms::binarySearchRecursive(sortedArr, target) << std::endl;
    std::cout << "Jump Search:          Index " << SearchingAlgorithms::jumpSearch(sortedArr, target) << std::endl;
    std::cout << "Interpolation Search: Index " << SearchingAlgorithms::interpolationSearch(sortedArr, target) << std::endl;
    std::cout << "Exponential Search:   Index " << SearchingAlgorithms::exponentialSearch(sortedArr, target) << std::endl;
    std::cout << "Ternary Search:       Index " << SearchingAlgorithms::ternarySearch(sortedArr, target) << std::endl;

    // Test with duplicates
    std::cout << std::endl << "============================================================" << std::endl;
    std::cout << "Advanced Searching (with duplicates)" << std::endl;
    std::cout << "============================================================" << std::endl;
    
    std::vector<int> arrWithDups = {1, 2, 2, 2, 3, 4, 4, 5, 5, 5, 5, 6};
    int targetDup = 5;

    std::cout << "Array: ";
    for (int val : arrWithDups) {
        std::cout << val << " ";
    }
    std::cout << std::endl;
    std::cout << "Target: " << targetDup << std::endl;
    std::cout << "First occurrence: Index " << AdvancedSearching::findFirstOccurrence(arrWithDups, targetDup) << std::endl;
    std::cout << "Last occurrence:  Index " << AdvancedSearching::findLastOccurrence(arrWithDups, targetDup) << std::endl;
    std::cout << "Total occurrences: " << AdvancedSearching::countOccurrences(arrWithDups, targetDup) << std::endl;

    return 0;
}
#endif // SKIP_STANDALONE_MAIN
