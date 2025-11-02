"""
ARRAYS - Data Structure Implementation

An array is a fundamental data structure that stores elements of the same type in contiguous memory 
locations. Arrays provide O(1) access time to elements using their index, making them extremely 
efficient for random access operations.

Key Characteristics:
- Fixed or dynamic size (depending on implementation)
- Elements are stored in contiguous memory locations
- Direct access to elements using index: O(1)
- Insertion at end: O(1) amortized for dynamic arrays
- Insertion/deletion at arbitrary position: O(n) due to shifting elements
- Search in unsorted array: O(n)
- Search in sorted array: O(log n) using binary search

Memory Layout:
If an array starts at memory address 1000 and each element is 4 bytes:
Index:    0    1    2    3    4
Address: 1000 1004 1008 1012 1016
Value:   [10] [20] [30] [40] [50]

Common Use Cases:
- Storing collections of similar data
- Implementing other data structures (stacks, queues, heaps)
- Mathematical computations on vectors/matrices
- Buffering data streams
"""


class DynamicArray:
    """
    A dynamic array implementation that automatically resizes when capacity is reached.
    Mimics Python's list behavior with manual memory management demonstration.
    """
    
    def __init__(self, capacity=10):
        self._capacity = capacity
        self._size = 0
        self._array = [None] * self._capacity
    
    def __len__(self):
        return self._size
    
    def __getitem__(self, index):
        if not 0 <= index < self._size:
            raise IndexError("Index out of bounds")
        return self._array[index]
    
    def __setitem__(self, index, value):
        if not 0 <= index < self._size:
            raise IndexError("Index out of bounds")
        self._array[index] = value
    
    def append(self, value):
        """Add element to end of array - O(1) amortized"""
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        self._array[self._size] = value
        self._size += 1
    
    def insert(self, index, value):
        """Insert element at specific index - O(n)"""
        if not 0 <= index <= self._size:
            raise IndexError("Index out of bounds")
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        # Shift elements to the right
        for i in range(self._size, index, -1):
            self._array[i] = self._array[i - 1]
        self._array[index] = value
        self._size += 1
    
    def remove(self, index):
        """Remove element at specific index - O(n)"""
        if not 0 <= index < self._size:
            raise IndexError("Index out of bounds")
        value = self._array[index]
        # Shift elements to the left
        for i in range(index, self._size - 1):
            self._array[i] = self._array[i + 1]
        self._array[self._size - 1] = None
        self._size -= 1
        return value
    
    def _resize(self, new_capacity):
        """Resize internal array - O(n)"""
        new_array = [None] * new_capacity
        for i in range(self._size):
            new_array[i] = self._array[i]
        self._array = new_array
        self._capacity = new_capacity
    
    def __str__(self):
        return '[' + ', '.join(str(self._array[i]) for i in range(self._size)) + ']'


class StaticArray:
    """
    A fixed-size array implementation demonstrating array fundamentals.
    Size is defined at creation and cannot be changed.
    """
    
    def __init__(self, size):
        self._size = size
        self._array = [None] * size
    
    def __len__(self):
        return self._size
    
    def __getitem__(self, index):
        if not 0 <= index < self._size:
            raise IndexError("Index out of bounds")
        return self._array[index]
    
    def __setitem__(self, index, value):
        if not 0 <= index < self._size:
            raise IndexError("Index out of bounds")
        self._array[index] = value
    
    def __str__(self):
        return '[' + ', '.join(str(item) for item in self._array) + ']'


# Example usage
if __name__ == "__main__":
    # Dynamic Array Demo
    print("=== Dynamic Array Demo ===")
    dyn_arr = DynamicArray(capacity=3)
    
    print(f"Initial array: {dyn_arr}")
    
    # Append elements
    for i in range(5):
        dyn_arr.append(i * 10)
        print(f"After append({i * 10}): {dyn_arr}, Size: {len(dyn_arr)}")
    
    # Insert element
    dyn_arr.insert(2, 999)
    print(f"After insert(2, 999): {dyn_arr}")
    
    # Remove element
    removed = dyn_arr.remove(3)
    print(f"After remove(3): {dyn_arr}, Removed: {removed}")
    
    # Access elements
    print(f"Element at index 0: {dyn_arr[0]}")
    print(f"Element at index 4: {dyn_arr[4]}")
    
    # Static Array Demo
    print("\n=== Static Array Demo ===")
    static_arr = StaticArray(5)
    print(f"Initial static array: {static_arr}")
    
    # Fill array
    for i in range(5):
        static_arr[i] = i * 5
    print(f"Filled static array: {static_arr}")
