# DSA Python - Data Structures and Algorithms

A comprehensive collection of data structures and algorithms implemented in Python with detailed explanations and examples. All implementations follow clean, class-based design patterns with extensive documentation.

## 📁 Project Structure

```
DSA_Python/
├── data_structures/
│   ├── __init__.py
│   ├── arrays.py              # Dynamic and Static Arrays
│   ├── linked_lists.py        # Singly and Doubly Linked Lists
│   ├── stacks.py              # Array and Linked Stack implementations
│   ├── queues.py              # Array, Circular, Linked Queue, and Deque
│   ├── hash_tables.py         # Hash Maps and Hash Sets
│   ├── trees.py               # Binary Trees, BST, AVL Trees
│   └── graphs.py              # Graph representations and traversals
│
├── algorithms/
│   ├── __init__.py
│   ├── sorting.py             # 7 sorting algorithms
│   ├── searching.py           # 6 searching algorithms
│   └── graph_algorithms.py    # Shortest path, MST, Max flow
│
├── __init__.py
└── README.md
```

## 📚 Data Structures

### Arrays
- **DynamicArray**: Auto-resizing array with O(1) amortized append
- **StaticArray**: Fixed-size array implementation

**Time Complexities:**
- Access: O(1)
- Search: O(n)
- Insert at end: O(1) amortized (dynamic)
- Insert at position: O(n)

### Linked Lists
- **SinglyLinkedList**: Each node points to next
- **DoublyLinkedList**: Each node points to next and previous

**Time Complexities:**
- Access: O(n)
- Search: O(n)
- Insert at head: O(1)
- Insert at tail: O(n) for singly, O(1) for doubly
- Delete: O(n)

### Stacks
- **ArrayStack**: Stack using Python list
- **LinkedStack**: Stack using linked list
- **StackApplications**: Balanced parentheses, reverse string, postfix evaluation

**Time Complexities:**
- Push: O(1)
- Pop: O(1)
- Peek: O(1)

### Queues
- **ArrayQueue**: Basic queue using list
- **CircularQueue**: Fixed-size circular queue
- **LinkedQueue**: Queue using linked list
- **Deque**: Double-ended queue

**Time Complexities:**
- Enqueue: O(1)
- Dequeue: O(1) (except ArrayQueue which is O(n))
- Front: O(1)

### Hash Tables
- **HashMapChaining**: Collision resolution using chaining
- **HashMapLinearProbing**: Open addressing with linear probing
- **HashSet**: Set implementation using hash map

**Time Complexities:**
- Insert: O(1) average, O(n) worst
- Delete: O(1) average, O(n) worst
- Search: O(1) average, O(n) worst

### Trees
- **BinaryTree**: Basic binary tree with traversals
- **BinarySearchTree**: Binary search tree with insert/delete/search
- **AVLTree**: Self-balancing binary search tree

**Time Complexities (BST):**
- Search: O(log n) average, O(n) worst
- Insert: O(log n) average, O(n) worst
- Delete: O(log n) average, O(n) worst

**Time Complexities (AVL):**
- Search: O(log n)
- Insert: O(log n)
- Delete: O(log n)

### Graphs
- **GraphAdjacencyList**: Space-efficient for sparse graphs
- **GraphAdjacencyMatrix**: Fast edge lookup for dense graphs
- **WeightedGraph**: Supports weighted edges with shortest path algorithms

**Operations:**
- BFS Traversal: O(V + E)
- DFS Traversal: O(V + E)
- Cycle Detection: O(V + E)

## 🔄 Algorithms

### Sorting Algorithms

| Algorithm | Best | Average | Worst | Space | Stable |
|-----------|------|---------|-------|-------|--------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Counting Sort | O(n+k) | O(n+k) | O(n+k) | O(k) | Yes |
| Radix Sort | O(d·n) | O(d·n) | O(d·n) | O(n+k) | Yes |

### Searching Algorithms

| Algorithm | Best | Average | Worst | Requirements |
|-----------|------|---------|-------|--------------|
| Linear Search | O(1) | O(n) | O(n) | None |
| Binary Search | O(1) | O(log n) | O(log n) | Sorted array |
| Jump Search | O(1) | O(√n) | O(√n) | Sorted array |
| Interpolation | O(1) | O(log log n) | O(n) | Sorted, uniform |
| Exponential | O(1) | O(log n) | O(log n) | Sorted |
| Ternary | O(1) | O(log n) | O(log n) | Sorted |

### Graph Algorithms

**Shortest Path:**
- **Dijkstra's Algorithm**: O((V + E) log V) - non-negative weights
- **Bellman-Ford Algorithm**: O(V · E) - handles negative weights

**Minimum Spanning Tree:**
- **Prim's Algorithm**: O(E log V) - grows MST from vertex
- **Kruskal's Algorithm**: O(E log E) - sorts edges, uses Union-Find

**Maximum Flow:**
- **Ford-Fulkerson Algorithm**: O(E · max_flow) - uses DFS
- **Edmonds-Karp Algorithm**: O(V · E²) - uses BFS

## 🚀 Usage Examples

### Using Data Structures

```python
from DSA_Python.data_structures import DynamicArray, BinarySearchTree, HashMapChaining

# Dynamic Array
arr = DynamicArray()
arr.append(10)
arr.append(20)
print(arr[0])  # Output: 10

# Binary Search Tree
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
print(bst.search(30))  # Output: True
print(bst.inorder_traversal())  # Output: [30, 50, 70]

# Hash Map
hash_map = HashMapChaining()
hash_map["apple"] = 5
hash_map["banana"] = 7
print(hash_map["apple"])  # Output: 5
```

### Using Algorithms

```python
from DSA_Python.algorithms import SortingAlgorithms, SearchingAlgorithms
from DSA_Python.algorithms import ShortestPathAlgorithms

# Sorting
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = SortingAlgorithms.quick_sort(arr)
print(sorted_arr)  # Output: [11, 12, 22, 25, 34, 64, 90]

# Searching
sorted_arr = [2, 5, 8, 12, 16, 23, 38, 45]
index = SearchingAlgorithms.binary_search(sorted_arr, 23)
print(index)  # Output: 5

# Graph Algorithms
graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('C', 1), ('D', 5)],
    'C': [('D', 8), ('E', 10)],
    'D': [('E', 2)],
    'E': []
}
distances, _ = ShortestPathAlgorithms.dijkstra(graph, 'A')
print(distances)  # Shortest distances from A to all vertices
```

## 📖 Documentation

Each implementation includes:
- **Detailed docstrings** explaining how the algorithm/data structure works
- **Time and space complexity** analysis
- **Visual representations** and examples in comments
- **Common use cases** and applications
- **Working example code** at the bottom of each file

## 🎯 Features

✅ Clean, class-based implementations  
✅ Comprehensive documentation with large comment blocks  
✅ Time and space complexity analysis  
✅ Working examples for every data structure and algorithm  
✅ Educational focus with detailed explanations  
✅ Production-ready code with proper error handling  
✅ Minimal inline comments, focus on docstrings  

## 📝 Running Examples

Each file can be run independently to see examples:

```bash
# Run data structure examples
python -m DSA_Python.data_structures.arrays
python -m DSA_Python.data_structures.trees
python -m DSA_Python.data_structures.graphs

# Run algorithm examples
python -m DSA_Python.algorithms.sorting
python -m DSA_Python.algorithms.searching
python -m DSA_Python.algorithms.graph_algorithms
```

## 🎓 Learning Resources

This package is designed for:
- Computer Science students learning DSA
- Interview preparation
- Algorithm study and reference
- Teaching and educational purposes

## 📄 License

Educational use - Feel free to use and modify for learning purposes.

## 🤝 Contributing

This is an educational project. Feel free to extend it with:
- Additional data structures (Heaps, Tries, Segment Trees)
- More algorithms (Dynamic Programming, Backtracking)
- Performance optimizations
- Additional examples and test cases

---

**Happy Learning! 🚀**
