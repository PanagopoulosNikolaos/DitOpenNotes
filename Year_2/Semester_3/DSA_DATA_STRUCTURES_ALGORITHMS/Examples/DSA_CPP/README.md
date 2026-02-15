# DSA Data Structures and Algorithms - C++ Implementation

This repository contains C++ implementations of various data structures and algorithms originally implemented in Python. All code has been carefully converted while maintaining the same functionality and educational purpose.

## Directory Structure

```
DSA_CPP/
├── algorithms/
│   ├── searching.cpp          # Searching algorithms (linear, binary, jump, etc.)
│   ├── sorting.cpp            # Sorting algorithms (bubble, quick, merge, etc.)
│   └── graph_algorithms.cpp   # Graph algorithms (Dijkstra, Prim's, Kruskal's, etc.)
├── data_structures/
│   ├── arrays.cpp             # Dynamic and static arrays
│   ├── linked_lists.cpp       # Singly and doubly linked lists
│   ├── stacks.cpp             # Stack implementations
│   ├── queues.cpp             # Queue implementations
│   ├── hash_tables.cpp        # Hash table implementations
│   ├── trees.cpp              # Tree implementations (BST, AVL)
│   └── graphs.cpp             # Graph implementations
└── main.cpp                   # Main file demonstrating all implementations
```

## Algorithms Included

### Searching Algorithms
- Linear Search
- Binary Search
- Jump Search
- Interpolation Search
- Exponential Search
- Ternary Search
- Advanced searching (first/last occurrence, count occurrences)

### Sorting Algorithms
- Bubble Sort
- Selection Sort
- Insertion Sort
- Quick Sort
- Merge Sort
- Counting Sort
- Radix Sort

### Graph Algorithms
- Dijkstra's Algorithm
- Bellman-Ford Algorithm
- Prim's Algorithm (MST)
- Kruskal's Algorithm (MST)
- Ford-Fulkerson Algorithm (Max Flow)
- Edmonds-Karp Algorithm (Max Flow)

## Data Structures Included

### Linear Data Structures
- Arrays (Dynamic and Static)
- Linked Lists (Singly and Doubly)
- Stacks (Array-based and Linked-list-based)
- Queues (Array, Circular, Linked, and Deque)

### Non-Linear Data Structures
- Hash Tables (Chaining and Linear Probing)
- Binary Trees (Basic traversals)
- Binary Search Trees (BST)
- AVL Trees (Self-balancing BST)
- Graphs (Adjacency List and Matrix representations)

## Compilation and Usage

To compile and run the main demonstration:

```bash
g++ -std=c++11 -o main main.cpp
./main
```

Each individual file can also be compiled separately if needed.

## Key Features

1. **Comprehensive Coverage**: All major data structures and algorithms covered
2. **Educational Focus**: Well-documented code with detailed comments explaining algorithms
3. **Performance Considerations**: Proper time and space complexity analysis
4. **Memory Management**: Proper use of smart pointers to avoid memory leaks
5. **Error Handling**: Appropriate exception handling for edge cases

## C++ Specific Notes

- Used smart pointers (`std::shared_ptr`, `std::unique_ptr`) for automatic memory management
- Utilized templates for generic data types where appropriate
- Leveraged STL containers like `std::vector`, `std::unordered_map`, and `std::queue`
- Implemented proper constructors, destructors, and RAII principles
- Used modern C++ features like `auto`, range-based loops, and initializer lists

## Learning Objectives

After studying this implementation, you should understand:

1. How to implement fundamental data structures in C++
2. The differences between Python and C++ implementations
3. Memory management in C++ using smart pointers
4. Time and space complexity of various algorithms
5. When to use specific data structures and algorithms
6. Best practices for C++ programming in the context of DSA