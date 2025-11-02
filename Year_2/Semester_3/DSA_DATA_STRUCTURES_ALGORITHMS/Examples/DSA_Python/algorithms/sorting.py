"""
SORTING ALGORITHMS - Implementation

Sorting is the process of arranging elements in a specific order (ascending or descending).
Different sorting algorithms have different time/space complexities and use cases.

Algorithm Comparison:
┌─────────────────┬──────────┬──────────┬──────────┬────────┬─────────┐
│ Algorithm       │ Best     │ Average  │ Worst    │ Space  │ Stable  │
├─────────────────┼──────────┼──────────┼──────────┼────────┼─────────┤
│ Bubble Sort     │ O(n)     │ O(n²)    │ O(n²)    │ O(1)   │ Yes     │
│ Selection Sort  │ O(n²)    │ O(n²)    │ O(n²)    │ O(1)   │ No      │
│ Insertion Sort  │ O(n)     │ O(n²)    │ O(n²)    │ O(1)   │ Yes     │
│ Quick Sort      │ O(n log n)│O(n log n)│ O(n²)    │ O(log n)│No      │
│ Merge Sort      │ O(n log n)│O(n log n)│O(n log n)│ O(n)   │ Yes     │
│ Counting Sort   │ O(n+k)   │ O(n+k)   │ O(n+k)   │ O(k)   │ Yes     │
│ Radix Sort      │ O(d·n)   │ O(d·n)   │ O(d·n)   │ O(n+k) │ Yes     │
└─────────────────┴──────────┴──────────┴──────────┴────────┴─────────┘

Stable: Maintains relative order of equal elements
In-place: Sorts within original array (low space complexity)

Common Use Cases:
- Bubble Sort: Educational purposes, nearly sorted data
- Selection Sort: Small datasets, memory-constrained systems
- Insertion Sort: Small datasets, nearly sorted data, online sorting
- Quick Sort: General purpose (most programming languages use variants)
- Merge Sort: Linked lists, stable sorting needed, external sorting
- Counting Sort: Integer sorting with limited range
- Radix Sort: Integer/string sorting, distributed systems
"""

class SortingAlgorithms:
    """Collection of sorting algorithm implementations"""
    
    @staticmethod
    def bubble_sort(arr):
        """
        BUBBLE SORT
        
        Repeatedly steps through the list, compares adjacent elements and swaps them
        if they are in wrong order. The pass through the list is repeated until sorted.
        
        How it works:
        - Compare adjacent elements
        - Swap if they're in wrong order
        - After each pass, largest element "bubbles" to end
        - Repeat until no swaps needed
        
        Time: O(n²) average/worst, O(n) best
        Space: O(1)
        Stable: Yes
        """
        n = len(arr)
        arr = arr.copy()
        
        for i in range(n):
            swapped = False
            
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            
            if not swapped:
                break
        
        return arr
    
    @staticmethod
    def selection_sort(arr):
        """
        SELECTION SORT
        
        Divides array into sorted and unsorted portions. Repeatedly finds minimum
        element from unsorted portion and places it at beginning of unsorted portion.
        
        How it works:
        - Find minimum element in unsorted array
        - Swap it with first unsorted element
        - Move boundary of sorted portion one position right
        - Repeat until entire array is sorted
        
        Time: O(n²) for all cases
        Space: O(1)
        Stable: No
        """
        n = len(arr)
        arr = arr.copy()
        
        for i in range(n):
            min_idx = i
            
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
        return arr
    
    @staticmethod
    def insertion_sort(arr):
        """
        INSERTION SORT
        
        Builds final sorted array one element at a time. Takes each element and
        inserts it into its correct position in the sorted portion.
        
        How it works:
        - Start with second element (first is considered sorted)
        - Compare with elements in sorted portion
        - Shift larger elements right
        - Insert current element in correct position
        - Repeat for all elements
        
        Time: O(n²) average/worst, O(n) best (nearly sorted)
        Space: O(1)
        Stable: Yes
        """
        n = len(arr)
        arr = arr.copy()
        
        for i in range(1, n):
            key = arr[i]
            j = i - 1
            
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            
            arr[j + 1] = key
        
        return arr
    
    @staticmethod
    def quick_sort(arr):
        """
        QUICK SORT
        
        Divide-and-conquer algorithm. Picks a pivot element and partitions array
        around it, then recursively sorts subarrays.
        
        How it works:
        - Choose a pivot element
        - Partition: rearrange so elements < pivot are left, > pivot are right
        - Recursively apply to left and right partitions
        - Base case: arrays of size 0 or 1 are already sorted
        
        Time: O(n log n) average, O(n²) worst (rare with good pivot selection)
        Space: O(log n) for recursion stack
        Stable: No
        """
        def partition(arr, low, high):
            pivot = arr[high]
            i = low - 1
            
            for j in range(low, high):
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            return i + 1
        
        def quick_sort_recursive(arr, low, high):
            if low < high:
                pi = partition(arr, low, high)
                quick_sort_recursive(arr, low, pi - 1)
                quick_sort_recursive(arr, pi + 1, high)
        
        arr = arr.copy()
        quick_sort_recursive(arr, 0, len(arr) - 1)
        return arr
    
    @staticmethod
    def merge_sort(arr):
        """
        MERGE SORT
        
        Divide-and-conquer algorithm. Divides array into two halves, recursively
        sorts them, then merges the sorted halves.
        
        How it works:
        - Divide array into two halves
        - Recursively sort both halves
        - Merge the sorted halves
        - Base case: arrays of size 1 are already sorted
        
        Time: O(n log n) for all cases
        Space: O(n) for temporary arrays
        Stable: Yes
        """
        def merge(left, right):
            result = []
            i = j = 0
            
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            
            result.extend(left[i:])
            result.extend(right[j:])
            return result
        
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left = SortingAlgorithms.merge_sort(arr[:mid])
        right = SortingAlgorithms.merge_sort(arr[mid:])
        
        return merge(left, right)
    
    @staticmethod
    def counting_sort(arr):
        """
        COUNTING SORT
        
        Non-comparison based sorting for integers in limited range. Counts occurrences
        of each value and uses counts to place elements in sorted order.
        
        How it works:
        - Count frequency of each element
        - Calculate cumulative counts
        - Place elements in output array using counts
        - Works only for non-negative integers in limited range
        
        Time: O(n + k) where k is range of input
        Space: O(k)
        Stable: Yes
        """
        if not arr:
            return arr
        
        max_val = max(arr)
        min_val = min(arr)
        range_size = max_val - min_val + 1
        
        count = [0] * range_size
        output = [0] * len(arr)
        
        for num in arr:
            count[num - min_val] += 1
        
        for i in range(1, range_size):
            count[i] += count[i - 1]
        
        for i in range(len(arr) - 1, -1, -1):
            output[count[arr[i] - min_val] - 1] = arr[i]
            count[arr[i] - min_val] -= 1
        
        return output
    
    @staticmethod
    def radix_sort(arr):
        """
        RADIX SORT
        
        Non-comparison based sorting that processes digits from least significant
        to most significant using a stable sorting algorithm (counting sort).
        
        How it works:
        - Sort by least significant digit
        - Sort by next digit (maintaining stability)
        - Repeat for all digits
        - Uses counting sort for each digit
        
        Time: O(d·n) where d is number of digits
        Space: O(n + k)
        Stable: Yes
        """
        if not arr:
            return arr
        
        max_val = max(arr)
        exp = 1
        arr = arr.copy()
        
        while max_val // exp > 0:
            counting_sort_by_digit(arr, exp)
            exp *= 10
        
        return arr

def counting_sort_by_digit(arr, exp):
    """Helper function for radix sort"""
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
    
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    for i in range(n - 1, -1, -1):
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
    
    for i in range(n):
        arr[i] = output[i]

# Example usage
if __name__ == "__main__":
    test_arr = [64, 34, 25, 12, 22, 11, 90]
    
    print(f"Original array: {test_arr}\n")
    
    print(f"Bubble Sort:    {SortingAlgorithms.bubble_sort(test_arr)}")
    print(f"Selection Sort: {SortingAlgorithms.selection_sort(test_arr)}")
    print(f"Insertion Sort: {SortingAlgorithms.insertion_sort(test_arr)}")
    print(f"Quick Sort:     {SortingAlgorithms.quick_sort(test_arr)}")
    print(f"Merge Sort:     {SortingAlgorithms.merge_sort(test_arr)}")
    print(f"Counting Sort:  {SortingAlgorithms.counting_sort(test_arr)}")
    print(f"Radix Sort:     {SortingAlgorithms.radix_sort(test_arr)}")
    
    # Performance comparison on larger array
    import random
    import time
    
    print("\n" + "="*60)
    print("Performance Comparison (1000 random elements)")
    print("="*60)
    
    large_arr = [random.randint(0, 1000) for _ in range(1000)]
    
    algorithms = [
        ("Bubble Sort", SortingAlgorithms.bubble_sort),
        ("Selection Sort", SortingAlgorithms.selection_sort),
        ("Insertion Sort", SortingAlgorithms.insertion_sort),
        ("Quick Sort", SortingAlgorithms.quick_sort),
        ("Merge Sort", SortingAlgorithms.merge_sort),
        ("Counting Sort", SortingAlgorithms.counting_sort),
        ("Radix Sort", SortingAlgorithms.radix_sort),
    ]
    
    for name, func in algorithms:
        start = time.time()
        func(large_arr)
        end = time.time()
        print(f"{name:20} {(end - start)*1000:.2f} ms")
