#include <iostream>
#include <vector>
#include <memory>
#include <stdexcept>

/**
 * @brief Arrays - Data Structure Implementation in C++
 * 
 * An array is a fundamental data structure that stores elements of the same type in contiguous memory 
 * locations. Arrays provide O(1) access time to elements using their index, making them extremely 
 * efficient for random access operations.
 * 
 * Key Characteristics:
 * - Fixed or dynamic size (depending on implementation)
 * - Elements are stored in contiguous memory locations
 * - Direct access to elements using index: O(1)
 * - Insertion at end: O(1) amortized for dynamic arrays
 * - Insertion/deletion at arbitrary position: O(n) due to shifting elements
 * - Search in unsorted array: O(n)
 * - Search in sorted array: O(log n) using binary search
 * 
 * Memory Layout:
 * If an array starts at memory address 1000 and each element is 4 bytes:
 * Index:    0    1    2    3    4
 * Address: 1000 1004 1008 1012 1016
 * Value:   [10] [20] [30] [40] [50]
 * 
 * Common Use Cases:
 * - Storing collections of similar data
 * - Implementing other data structures (stacks, queues, heaps)
 * - Mathematical computations on vectors/matrices
 * - Buffering data streams
 */
template<typename T>
class DynamicArray {
private:
    std::unique_ptr<T[]> _array;
    size_t _capacity;
    size_t _size;

    void _resize(size_t newCapacity) {
        std::unique_ptr<T[]> newArray = std::make_unique<T[]>(newCapacity);
        for (size_t i = 0; i < _size; ++i) {
            newArray[i] = _array[i];
        }
        _array = std::move(newArray);
        _capacity = newCapacity;
    }

public:
    /**
     * @brief A dynamic array implementation that automatically resizes when capacity is reached.
     * Mimics Python's list behavior with manual memory management demonstration.
     */
    explicit DynamicArray(size_t capacity = 10) : _capacity(capacity), _size(0) {
        _array = std::make_unique<T[]>(capacity);
    }

    size_t size() const {
        return _size;
    }

    bool empty() const {
        return _size == 0;
    }

    T& operator[](size_t index) {
        if (index >= _size) {
            throw std::out_of_range("Index out of bounds");
        }
        return _array[index];
    }

    const T& operator[](size_t index) const {
        if (index >= _size) {
            throw std::out_of_range("Index out of bounds");
        }
        return _array[index];
    }

    /**
     * @brief Add element to end of array - O(1) amortized
     */
    void append(const T& value) {
        if (_size == _capacity) {
            _resize(2 * _capacity);
        }
        _array[_size] = value;
        ++_size;
    }

    /**
     * @brief Insert element at specific index - O(n)
     */
    void insert(size_t index, const T& value) {
        if (index > _size) {
            throw std::out_of_range("Index out of bounds");
        }
        if (_size == _capacity) {
            _resize(2 * _capacity);
        }
        // Shift elements to the right
        for (size_t i = _size; i > index; --i) {
            _array[i] = _array[i - 1];
        }
        _array[index] = value;
        ++_size;
    }

    /**
     * @brief Remove element at specific index - O(n)
     */
    T remove(size_t index) {
        if (index >= _size) {
            throw std::out_of_range("Index out of bounds");
        }
        T value = _array[index];
        // Shift elements to the left
        for (size_t i = index; i < _size - 1; ++i) {
            _array[i] = _array[i + 1];
        }
        --_size;
        _array[_size] = T{}; // Reset the last element
        return value;
    }

    void print() const {
        std::cout << "[";
        for (size_t i = 0; i < _size; ++i) {
            std::cout << _array[i];
            if (i < _size - 1) {
                std::cout << ", ";
            }
        }
        std::cout << "]" << std::endl;
    }
};

template<typename T>
class StaticArray {
private:
    std::unique_ptr<T[]> _array;
    size_t _size;

public:
    /**
     * @brief A fixed-size array implementation demonstrating array fundamentals.
     * Size is defined at creation and cannot be changed.
     */
    explicit StaticArray(size_t size) : _size(size) {
        _array = std::make_unique<T[]>(size);
    }

    size_t size() const {
        return _size;
    }

    T& operator[](size_t index) {
        if (index >= _size) {
            throw std::out_of_range("Index out of bounds");
        }
        return _array[index];
    }

    const T& operator[](size_t index) const {
        if (index >= _size) {
            throw std::out_of_range("Index out of bounds");
        }
        return _array[index];
    }

    void print() const {
        std::cout << "[";
        for (size_t i = 0; i < _size; ++i) {
            std::cout << _array[i];
            if (i < _size - 1) {
                std::cout << ", ";
            }
        }
        std::cout << "]" << std::endl;
    }
};

// Example usage
int main() {
    // Dynamic Array Demo
    std::cout << "=== Dynamic Array Demo ===" << std::endl;
    DynamicArray<int> dynArr(3);

    std::cout << "Initial array: ";
    dynArr.print();

    // Append elements
    for (int i = 0; i < 5; ++i) {
        dynArr.append(i * 10);
        std::cout << "After append(" << i * 10 << "): ";
        dynArr.print();
        std::cout << "Size: " << dynArr.size() << std::endl;
    }

    // Insert element
    dynArr.insert(2, 999);
    std::cout << "After insert(2, 999): ";
    dynArr.print();

    // Remove element
    int removed = dynArr.remove(3);
    std::cout << "After remove(3): ";
    dynArr.print();
    std::cout << "Removed: " << removed << std::endl;

    // Access elements
    std::cout << "Element at index 0: " << dynArr[0] << std::endl;
    std::cout << "Element at index 4: " << dynArr[4] << std::endl;

    // Static Array Demo
    std::cout << "\n=== Static Array Demo ===" << std::endl;
    StaticArray<int> staticArr(5);
    std::cout << "Initial static array: ";
    staticArr.print();

    // Fill array
    for (size_t i = 0; i < staticArr.size(); ++i) {
        staticArr[i] = static_cast<int>(i * 5);
    }
    std::cout << "Filled static array: ";
    staticArr.print();

    return 0;
}