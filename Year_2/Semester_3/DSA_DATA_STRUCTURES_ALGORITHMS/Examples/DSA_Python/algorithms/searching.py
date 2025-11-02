"""
SEARCHING ALGORITHMS - Implementation

Searching is the process of finding a specific element in a data structure.
Different algorithms are suitable for different data organizations.

Algorithm Comparison:
┌─────────────────┬──────────┬──────────┬──────────┬──────────────────┐
│ Algorithm       │ Best     │ Average  │ Worst    │ Requirements     │
├─────────────────┼──────────┼──────────┼──────────┼──────────────────┤
│ Linear Search   │ O(1)     │ O(n)     │ O(n)     │ None             │
│ Binary Search   │ O(1)     │ O(log n) │ O(log n) │ Sorted array     │
│ Jump Search     │ O(1)     │ O(√n)    │ O(√n)    │ Sorted array     │
│ Interpolation   │ O(1)     │ O(log log n)│O(n)   │ Sorted, uniform  │
│ Exponential     │ O(1)     │ O(log n) │ O(log n) │ Sorted, unbounded│
└─────────────────┴──────────┴──────────┴──────────┴──────────────────┘

Common Use Cases:
- Linear Search: Unsorted data, small datasets
- Binary Search: Sorted arrays, most common search
- Jump Search: Sorted arrays with costly comparisons
- Interpolation: Uniformly distributed sorted data
- Exponential: Unbounded/infinite sorted arrays
"""

import math

class SearchingAlgorithms:
    """Collection of searching algorithm implementations"""
    
    @staticmethod
    def linear_search(arr, target):
        """
        LINEAR SEARCH
        
        Sequentially checks each element until target is found or end is reached.
        Works on both sorted and unsorted arrays.
        
        How it works:
        - Start from first element
        - Compare each element with target
        - If match found, return index
        - If end reached without match, return -1
        
        Time: O(n) for all cases
        Space: O(1)
        """
        for i in range(len(arr)):
            if arr[i] == target:
                return i
        return -1
    
    @staticmethod
    def binary_search(arr, target):
        """
        BINARY SEARCH
        
        Efficiently finds target in sorted array by repeatedly dividing search
        interval in half. Compares target with middle element.
        
        How it works:
        - Start with entire array
        - Compare target with middle element
        - If match, return index
        - If target < middle, search left half
        - If target > middle, search right half
        - Repeat until found or search space is empty
        
        Time: O(log n)
        Space: O(1) iterative, O(log n) recursive
        Requires: Sorted array
        """
        left, right = 0, len(arr) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
    
    @staticmethod
    def binary_search_recursive(arr, target, left=None, right=None):
        """
        BINARY SEARCH (Recursive)
        
        Recursive implementation of binary search.
        Same logic but uses recursion instead of iteration.
        
        Time: O(log n)
        Space: O(log n) due to recursion stack
        """
        if left is None:
            left = 0
        if right is None:
            right = len(arr) - 1
        
        if left > right:
            return -1
        
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return SearchingAlgorithms.binary_search_recursive(arr, target, mid + 1, right)
        else:
            return SearchingAlgorithms.binary_search_recursive(arr, target, left, mid - 1)
    
    @staticmethod
    def jump_search(arr, target):
        """
        JUMP SEARCH
        
        Works on sorted arrays. Jumps ahead by fixed steps, then performs
        linear search in the block where element may exist.
        
        How it works:
        - Jump ahead by √n steps
        - When arr[jump] > target, do linear search in previous block
        - Optimal jump size is √n
        
        Time: O(√n)
        Space: O(1)
        Requires: Sorted array
        """
        n = len(arr)
        step = int(math.sqrt(n))
        prev = 0
        
        while prev < n and arr[min(step, n) - 1] < target:
            prev = step
            step += int(math.sqrt(n))
            if prev >= n:
                return -1
        
        while prev < n and arr[prev] < target:
            prev += 1
            if prev == min(step, n):
                return -1
        
        if prev < n and arr[prev] == target:
            return prev
        
        return -1
    
    @staticmethod
    def interpolation_search(arr, target):
        """
        INTERPOLATION SEARCH
        
        Improved binary search for uniformly distributed sorted arrays.
        Estimates position based on value distribution.
        
        How it works:
        - Similar to binary search
        - Instead of middle, calculates probable position:
          pos = low + [(target - arr[low]) * (high - low)] / (arr[high] - arr[low])
        - Works best when data is uniformly distributed
        
        Time: O(log log n) average for uniform distribution, O(n) worst
        Space: O(1)
        Requires: Sorted array with uniform distribution
        """
        left, right = 0, len(arr) - 1
        
        while left <= right and arr[left] <= target <= arr[right]:
            if left == right:
                if arr[left] == target:
                    return left
                return -1
            
            pos = left + int((target - arr[left]) * (right - left) / 
                            (arr[right] - arr[left]))
            
            if arr[pos] == target:
                return pos
            elif arr[pos] < target:
                left = pos + 1
            else:
                right = pos - 1
        
        return -1
    
    @staticmethod
    def exponential_search(arr, target):
        """
        EXPONENTIAL SEARCH
        
        Useful for unbounded/infinite sorted arrays. Finds range where
        element exists, then applies binary search.
        
        How it works:
        - Start with index 1
        - Double index until arr[index] >= target
        - Apply binary search in range [index/2, index]
        
        Time: O(log n)
        Space: O(1)
        Requires: Sorted array
        """
        if not arr:
            return -1
        
        if arr[0] == target:
            return 0
        
        i = 1
        while i < len(arr) and arr[i] <= target:
            i *= 2
        
        return SearchingAlgorithms.binary_search(
            arr[i // 2:min(i, len(arr))], 
            target
        ) + i // 2 if SearchingAlgorithms.binary_search(
            arr[i // 2:min(i, len(arr))], 
            target
        ) != -1 else -1
    
    @staticmethod
    def ternary_search(arr, target, left=None, right=None):
        """
        TERNARY SEARCH
        
        Divide-and-conquer algorithm that divides array into three parts.
        Similar to binary search but with two mid points.
        
        How it works:
        - Divide array into three equal parts
        - Determine which third contains target
        - Recursively search that third
        
        Time: O(log₃ n) ≈ O(log n)
        Space: O(log n) due to recursion
        Requires: Sorted array
        """
        if left is None:
            left = 0
        if right is None:
            right = len(arr) - 1
        
        if left > right:
            return -1
        
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        
        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2
        
        if target < arr[mid1]:
            return SearchingAlgorithms.ternary_search(arr, target, left, mid1 - 1)
        elif target > arr[mid2]:
            return SearchingAlgorithms.ternary_search(arr, target, mid2 + 1, right)
        else:
            return SearchingAlgorithms.ternary_search(arr, target, mid1 + 1, mid2 - 1)

class AdvancedSearching:
    """Advanced searching techniques"""
    
    @staticmethod
    def find_first_occurrence(arr, target):
        """Find first occurrence of target in sorted array with duplicates"""
        left, right = 0, len(arr) - 1
        result = -1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if arr[mid] == target:
                result = mid
                right = mid - 1
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return result
    
    @staticmethod
    def find_last_occurrence(arr, target):
        """Find last occurrence of target in sorted array with duplicates"""
        left, right = 0, len(arr) - 1
        result = -1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if arr[mid] == target:
                result = mid
                left = mid + 1
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return result
    
    @staticmethod
    def count_occurrences(arr, target):
        """Count occurrences of target in sorted array"""
        first = AdvancedSearching.find_first_occurrence(arr, target)
        if first == -1:
            return 0
        last = AdvancedSearching.find_last_occurrence(arr, target)
        return last - first + 1

# Example usage
if __name__ == "__main__":
    # Test array (sorted for most algorithms)
    sorted_arr = [2, 5, 8, 12, 16, 23, 38, 45, 56, 67, 78]
    target = 23
    
    print(f"Array: {sorted_arr}")
    print(f"Target: {target}\n")
    
    print(f"Linear Search:        Index {SearchingAlgorithms.linear_search(sorted_arr, target)}")
    print(f"Binary Search:        Index {SearchingAlgorithms.binary_search(sorted_arr, target)}")
    print(f"Binary (Recursive):   Index {SearchingAlgorithms.binary_search_recursive(sorted_arr, target)}")
    print(f"Jump Search:          Index {SearchingAlgorithms.jump_search(sorted_arr, target)}")
    print(f"Interpolation Search: Index {SearchingAlgorithms.interpolation_search(sorted_arr, target)}")
    print(f"Exponential Search:   Index {SearchingAlgorithms.exponential_search(sorted_arr, target)}")
    print(f"Ternary Search:       Index {SearchingAlgorithms.ternary_search(sorted_arr, target)}")
    
    # Test with duplicates
    print("\n" + "="*60)
    print("Advanced Searching (with duplicates)")
    print("="*60)
    arr_with_dups = [1, 2, 2, 2, 3, 4, 4, 5, 5, 5, 5, 6]
    target_dup = 5
    
    print(f"Array: {arr_with_dups}")
    print(f"Target: {target_dup}")
    print(f"First occurrence: Index {AdvancedSearching.find_first_occurrence(arr_with_dups, target_dup)}")
    print(f"Last occurrence:  Index {AdvancedSearching.find_last_occurrence(arr_with_dups, target_dup)}")
    print(f"Total occurrences: {AdvancedSearching.count_occurrences(arr_with_dups, target_dup)}")
    
    # Performance comparison
    import random
    import time
    
    print("\n" + "="*60)
    print("Performance Comparison (10000 elements)")
    print("="*60)
    
    large_sorted = sorted([random.randint(0, 10000) for _ in range(10000)])
    search_target = large_sorted[len(large_sorted) // 2]
    
    algorithms = [
        ("Linear Search", SearchingAlgorithms.linear_search),
        ("Binary Search", SearchingAlgorithms.binary_search),
        ("Jump Search", SearchingAlgorithms.jump_search),
        ("Interpolation Search", SearchingAlgorithms.interpolation_search),
        ("Exponential Search", SearchingAlgorithms.exponential_search),
    ]
    
    for name, func in algorithms:
        start = time.time()
        for _ in range(1000):
            func(large_sorted, search_target)
        end = time.time()
        print(f"{name:25} {(end - start)*1000:.2f} ms (1000 searches)")
