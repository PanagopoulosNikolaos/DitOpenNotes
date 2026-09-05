# Data Structures and Algorithms

## Course Overview
This course provides a rigorous mathematical and practical treatment of fundamental data structures, computational complexity, algorithmic paradigms, and graph algorithms. Topics include asymptotic notation, recurrence relations, linear structures, balanced binary search trees (AVL), binary heaps, priority queues, hashing schemes, graph traversals, and shortest path optimization.

## Course Code
305 (DATA STRUCTURES AND ALGORITHMS)

## Prerequisites
* C Programming II (Code: 204)
* Discrete Mathematics (Code: 203)

---

## Topics Covered
* **Asymptotic Analysis & Recurrences**: Big-$O$, Big-$\Omega$, Big-$\Theta$ definitions, properties of growth rates, Master Theorem, recursion trees, substitution method, and amortized complexity analysis.
* **Linear Data Structures**: Static vs. dynamic arrays (amortized doubling), singly and doubly linked lists, LIFO stacks, FIFO queues, circular buffers, and deque implementations.
* **Tree Structures & Balanced BSTs**: Binary tree traversals (pre-order, in-order, post-order, level-order), Binary Search Tree invariants, search/insertion/deletion algorithms, AVL tree balancing, balance factors, single (LL, RR) and double (LR, RL) rotations.
* **Priority Queues & Heaps**: Min/Max binary heaps, array-based heap mapping, sift-up and sift-down operations, Floyd's linear-time $O(n)$ heap construction, and heapsort.
* **Hashing and Hash Tables**: Hash functions, load factors, collision resolution by separate chaining, open addressing (linear probing, quadratic probing, double hashing), and dynamic rehashing.
* **Graph Algorithms**: Adjacency matrix vs. adjacency list representations, Breadth-First Search (BFS), Depth-First Search (DFS), topological sorting (Kahn's algorithm), single-source shortest paths (Dijkstra, Bellman-Ford), and Minimum Spanning Trees (Kruskal, Prim).
* **Sorting and Searching**: Insertion sort, selection sort, merge sort, quicksort with randomized partitioning, linear search, binary search, jump search, and exponential search.

---

## Learning Objectives
* Analyze time and space complexity of iterative and recursive algorithms rigorously.
* Select, design, and implement optimal data structures tailored to specific algorithmic performance constraints.
* Implement self-balancing search trees (AVL) and priority queues with strict memory safety in C++ and Python.
* Formulate real-world routing, dependency, and network problems as graph models and solve them using standard graph traversals and optimization algorithms.

---

## Directory Structure

| Directory | Description |
|:---|:---|
| [`Lectures/`](Lectures/) | Structured theory lecture modules on complexity, trees, heaps, hashing, and graph theory |
| [`Exercises/`](Exercises/) | Solved step-by-step mathematical problem sets on asymptotic bounds, recurrences, and AVL rotations |
| [`Examples/`](Examples/) | High-performance C++ and Python 3 data structure and algorithm suites with automated test runners |
| [`Assignments/`](Assignments/) | Laboratory programming assignments with formal project briefs and model solutions |
| [`Tutorials/`](Tutorials/) | Hands-on tutorials on building generic C++ template containers and benchmarking sorting algorithms |
| [`Projects/`](Projects/) | Capstone design specification for an in-memory inverted text index and ranked retrieval engine |
| [`Exams/`](Exams/) | 100-point model practice examination with complete worked solutions and past exam assets |
| [`Resources/`](Resources/) | Comprehensive topic notes (AVL, BST, heaps, hashing), curriculum mindmap, and bibliography |

---

## How to Build and Run Examples

### C++ Suite
To compile and execute the complete C++ data structure and algorithm demonstration suite:
```bash
cd Examples/DSA_CPP
make all
./main_app
```

### Python Suite
To execute the automated Python verification suite:
```bash
python3 Examples/DSA_Python/run_all.py
```
