#include <iostream>
#include <vector>
#include <chrono>
#include <random>

// Include headers for all algorithms and data structures
#include "algorithms/searching.cpp"
#include "algorithms/sorting.cpp"
#include "algorithms/graph_algorithms.cpp"
#include "data_structures/arrays.cpp"
#include "data_structures/linked_lists.cpp"
#include "data_structures/stacks.cpp"
#include "data_structures/queues.cpp"
#include "data_structures/hash_tables.cpp"
#include "data_structures/trees.cpp"
#include "data_structures/graphs.cpp"

void demonstrateSearchingAlgorithms() {
    std::cout << "\n===========================================" << std::endl;
    std::cout << "DEMONSTRATING SEARCHING ALGORITHMS" << std::endl;
    std::cout << "===========================================" << std::endl;

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
}

void demonstrateSortingAlgorithms() {
    std::cout << "\n===========================================" << std::endl;
    std::cout << "DEMONSTRATING SORTING ALGORITHMS" << std::endl;
    std::cout << "===========================================" << std::endl;

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
}

void demonstrateArrays() {
    std::cout << "\n===========================================" << std::endl;
    std::cout << "DEMONSTRATING ARRAYS DATA STRUCTURE" << std::endl;
    std::cout << "===========================================" << std::endl;

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
}

void demonstrateLinkedLists() {
    std::cout << "\n===========================================" << std::endl;
    std::cout << "DEMONSTRATING LINKED LISTS DATA STRUCTURE" << std::endl;
    std::cout << "===========================================" << std::endl;

    std::cout << "=== Singly Linked List Demo ===" << std::endl;
    SinglyLinkedList sll;

    std::cout << "Empty list: ";
    sll.print();

    // Add elements
    sll.append(10);
    sll.append(20);
    sll.append(30);
    std::cout << "After appending 10, 20, 30: ";
    sll.print();

    sll.prepend(5);
    std::cout << "After prepending 5: ";
    sll.print();

    sll.insertAfter(20, 25);
    std::cout << "After inserting 25 after 20: ";
    sll.print();

    // Search
    int pos = sll.search(25);
    std::cout << "Position of 25: " << pos << std::endl;

    // Delete
    sll.remove(20);
    std::cout << "After deleting 20: ";
    sll.print();

    // Reverse
    sll.reverse();
    std::cout << "After reversing: ";
    sll.print();
    std::cout << "Size: " << sll.size() << std::endl;

    std::cout << "\n=== Doubly Linked List Demo ===" << std::endl;
    DoublyLinkedList dll;

    dll.append(100);
    dll.append(200);
    dll.append(300);
    std::cout << "After appending 100, 200, 300: ";
    dll.print();

    dll.prepend(50);
    std::cout << "After prepending 50: ";
    dll.print();

    dll.remove(200);
    std::cout << "After deleting 200: ";
    dll.print();

    dll.reverse();
    std::cout << "After reversing: ";
    dll.print();
    std::cout << "Size: " << dll.size() << std::endl;
}

void demonstrateStacks() {
    std::cout << "\n===========================================" << std::endl;
    std::cout << "DEMONSTRATING STACKS DATA STRUCTURE" << std::endl;
    std::cout << "===========================================" << std::endl;

    std::cout << "=== Array Stack Demo ===" << std::endl;
    ArrayStack<int> stack;

    // Push elements
    for (int i : {10, 20, 30, 40}) {
        stack.push(i);
        std::cout << "Pushed " << i << ": ";
        stack.print();
    }

    // Peek
    std::cout << "Top element: " << stack.peek() << std::endl;

    // Pop elements
    while (!stack.empty()) {
        int popped = stack.pop();
        std::cout << "Popped " << popped << ": ";
        stack.print();
    }

    std::cout << "\n=== Linked Stack Demo ===" << std::endl;
    LinkedStack<char> linkedStack;

    for (char c : {'A', 'B', 'C', 'D'}) {
        linkedStack.push(c);
        std::cout << "Pushed " << c << ": ";
        linkedStack.print();
    }

    std::cout << "Size: " << linkedStack.size() << std::endl;
}

void demonstrateQueues() {
    std::cout << "\n===========================================" << std::endl;
    std::cout << "DEMONSTRATING QUEUES DATA STRUCTURE" << std::endl;
    std::cout << "===========================================" << std::endl;

    std::cout << "=== Array Queue Demo ===" << std::endl;
    ArrayQueue<int> queue;

    for (int i : {10, 20, 30, 40}) {
        queue.enqueue(i);
        std::cout << "Enqueued " << i << ": ";
        queue.print();
    }

    std::cout << "Front element: " << queue.front() << std::endl;

    while (!queue.empty()) {
        int dequeued = queue.dequeue();
        std::cout << "Dequeued " << dequeued << ": ";
        queue.print();
    }

    std::cout << "\n=== Circular Queue Demo ===" << std::endl;
    CircularQueue<int> circQueue(5);

    for (int i = 1; i <= 5; ++i) {
        circQueue.enqueue(i * 10);
        std::cout << "Enqueued " << i * 10 << ": ";
        circQueue.print();
    }

    // Dequeue two elements
    circQueue.dequeue();
    circQueue.dequeue();
    std::cout << "After 2 dequeues: ";
    circQueue.print();

    // Add more (demonstrates circular nature)
    circQueue.enqueue(60);
    circQueue.enqueue(70);
    std::cout << "After adding 60, 70: ";
    circQueue.print();

    std::cout << "\n=== Linked Queue Demo ===" << std::endl;
    LinkedQueue<int> linkedQueue;

    for (char c : {'A', 'B', 'C', 'D'}) {
        int val = static_cast<int>(c);  // Convert char to int for storage
        linkedQueue.enqueue(val);
        std::cout << "Enqueued " << c << ": ";
        linkedQueue.print();
    }

    std::cout << "Size: " << linkedQueue.size() << std::endl;

    std::cout << "\n=== Deque Demo ===" << std::endl;
    Deque<int> dq;

    dq.addRear(10);
    dq.addRear(20);
    std::cout << "Added 10, 20 to rear: ";
    dq.print();

    dq.addFront(5);
    dq.addFront(1);
    std::cout << "Added 5, 1 to front: ";
    dq.print();

    std::cout << "Front: " << dq.front() << ", Rear: " << dq.rear() << std::endl;

    std::cout << "Remove front: " << dq.removeFront() << std::endl;
    std::cout << "Remove rear: " << dq.removeRear() << std::endl;
    std::cout << "After removals: ";
    dq.print();
}

void demonstrateHashTables() {
    std::cout << "\n===========================================" << std::endl;
    std::cout << "DEMONSTRATING HASH TABLES DATA STRUCTURE" << std::endl;
    std::cout << "===========================================" << std::endl;

    std::cout << "=== Hash Map with Chaining Demo ===" << std::endl;
    HashMapChaining<std::string, int> hashMap;

    // Insert key-value pairs
    hashMap.put("apple", 5);
    hashMap.put("banana", 7);
    hashMap.put("orange", 3);
    hashMap.put("grape", 12);
    std::cout << "Hash map: ";
    hashMap.print();
    std::cout << "Size: " << hashMap.size() << std::endl;

    // Access values
    std::cout << "apple: " << hashMap.get("apple") << std::endl;
    std::cout << "grape: " << hashMap.get("grape") << std::endl;

    // Update value
    hashMap.put("apple", 10);
    std::cout << "After update: ";
    hashMap.print();

    // Check existence
    std::cout << "'banana' in map: " << (hashMap.contains("banana") ? "true" : "false") << std::endl;
    std::cout << "'mango' in map: " << (hashMap.contains("mango") ? "true" : "false") << std::endl;

    // Delete entry
    hashMap.remove("orange");
    std::cout << "After deleting 'orange': ";
    hashMap.print();

    std::cout << "\n=== Hash Map with Linear Probing Demo ===" << std::endl;
    HashMapLinearProbing<std::string, int> lpMap;

    lpMap.put("one", 1);
    lpMap.put("two", 2);
    lpMap.put("three", 3);
    std::cout << "Linear probing map: ";
    lpMap.print();

    std::cout << "\n=== Hash Set Demo ===" << std::endl;
    HashSet<int> hashSet;

    // Add elements
    std::vector<int> nums = {1, 2, 3, 2, 4, 3, 5};
    for (int num : nums) {
        hashSet.add(num);
    }
    std::cout << "Set (duplicates removed): ";
    hashSet.print();

    // Check membership
    std::cout << "3 in set: " << (hashSet.contains(3) ? "true" : "false") << std::endl;
    std::cout << "10 in set: " << (hashSet.contains(10) ? "true" : "false") << std::endl;

    // Remove element
    hashSet.remove(2);
    std::cout << "After removing 2: ";
    hashSet.print();
}

void demonstrateTrees() {
    std::cout << "\n===========================================" << std::endl;
    std::cout << "DEMONSTRATING TREES DATA STRUCTURE" << std::endl;
    std::cout << "===========================================" << std::endl;

    std::cout << "=== Binary Tree Traversals Demo ===" << std::endl;
    BinaryTree bt;
    bt.setRoot(50);
    
    // Manually building the tree structure
    bt.setLeftChild(bt.getRoot(), 30);
    bt.setRightChild(bt.getRoot(), 70);
    
    // We need to get the child nodes to add their children
    auto leftChild = bt.getRoot()->left;
    auto rightChild = bt.getRoot()->right;
    
    bt.setLeftChild(leftChild, 20);
    bt.setRightChild(leftChild, 40);
    bt.setLeftChild(rightChild, 60);
    bt.setRightChild(rightChild, 80);

    std::cout << "Pre-order: ";
    auto preOrder = bt.preorderTraversal();
    for (size_t i = 0; i < preOrder.size(); ++i) {
        std::cout << preOrder[i];
        if (i < preOrder.size() - 1) std::cout << ", ";
    }
    std::cout << std::endl;

    std::cout << "In-order: ";
    auto inOrder = bt.inorderTraversal();
    for (size_t i = 0; i < inOrder.size(); ++i) {
        std::cout << inOrder[i];
        if (i < inOrder.size() - 1) std::cout << ", ";
    }
    std::cout << std::endl;

    std::cout << "Post-order: ";
    auto postOrder = bt.postorderTraversal();
    for (size_t i = 0; i < postOrder.size(); ++i) {
        std::cout << postOrder[i];
        if (i < postOrder.size() - 1) std::cout << ", ";
    }
    std::cout << std::endl;

    std::cout << "Level-order: ";
    auto levelOrder = bt.levelorderTraversal();
    for (size_t i = 0; i < levelOrder.size(); ++i) {
        std::cout << levelOrder[i];
        if (i < levelOrder.size() - 1) std::cout << ", ";
    }
    std::cout << std::endl;

    std::cout << "Height: " << bt.height() << std::endl;

    std::cout << "\n=== Binary Search Tree Demo ===" << std::endl;
    BinarySearchTree bst;

    std::vector<int> values = {50, 30, 70, 20, 40, 60, 80};
    for (int val : values) {
        bst.insert(val);
    }

    std::cout << "Inserted: ";
    for (size_t i = 0; i < values.size(); ++i) {
        std::cout << values[i];
        if (i < values.size() - 1) std::cout << ", ";
    }
    std::cout << std::endl;

    std::cout << "In-order (sorted): ";
    auto bstInOrder = bst.inorderTraversal();
    for (size_t i = 0; i < bstInOrder.size(); ++i) {
        std::cout << bstInOrder[i];
        if (i < bstInOrder.size() - 1) std::cout << ", ";
    }
    std::cout << std::endl;

    std::cout << "Size: " << bst.size() << std::endl;

    // Search
    std::cout << "Search 40: " << (bst.search(40) ? "found" : "not found") << std::endl;
    std::cout << "Search 100: " << (bst.search(100) ? "found" : "not found") << std::endl;

    // Min/Max
    std::cout << "Min: " << bst.findMin() << std::endl;
    std::cout << "Max: " << bst.findMax() << std::endl;

    // Delete
    bst.remove(30);
    std::cout << "After deleting 30: ";
    auto afterDelete = bst.inorderTraversal();
    for (size_t i = 0; i < afterDelete.size(); ++i) {
        std::cout << afterDelete[i];
        if (i < afterDelete.size() - 1) std::cout << ", ";
    }
    std::cout << std::endl;

    std::cout << "\n=== AVL Tree Demo ===" << std::endl;
    AVLTree avl;

    std::vector<int> avlValues = {10, 20, 30, 40, 50, 25};
    for (int val : avlValues) {
        avl.insert(val);
        std::cout << "Inserted " << val << ": ";
        auto avlOrder = avl.inorderTraversal();
        for (size_t i = 0; i < avlOrder.size(); ++i) {
            std::cout << avlOrder[i];
            if (i < avlOrder.size() - 1) std::cout << ", ";
        }
        std::cout << std::endl;
    }

    std::cout << "Final AVL tree (in-order): ";
    auto finalAvlOrder = avl.inorderTraversal();
    for (size_t i = 0; i < finalAvlOrder.size(); ++i) {
        std::cout << finalAvlOrder[i];
        if (i < finalAvlOrder.size() - 1) std::cout << ", ";
    }
    std::cout << std::endl;
}

void demonstrateGraphs() {
    std::cout << "\n===========================================" << std::endl;
    std::cout << "DEMONSTRATING GRAPHS DATA STRUCTURE" << std::endl;
    std::cout << "===========================================" << std::endl;

    std::cout << "=== Graph Adjacency List Demo ===" << std::endl;
    GraphAdjacencyList g(false); // undirected graph

    // Add edges (automatically adds vertices)
    g.addEdge(0, 1); // A, B represented as 0, 1
    g.addEdge(0, 2); // A, C represented as 0, 2
    g.addEdge(1, 3); // B, D represented as 1, 3
    g.addEdge(2, 3); // C, D represented as 2, 3
    g.addEdge(3, 4); // D, E represented as 3, 4

    std::cout << "Graph structure:" << std::endl;
    g.print();

    std::cout << "\nNeighbors of 0: ";
    auto neighbors = g.getNeighbors(0);
    for (size_t i = 0; i < neighbors.size(); ++i) {
        std::cout << neighbors[i].vertex;
        if (i < neighbors.size() - 1) std::cout << ", ";
    }
    std::cout << std::endl;

    std::cout << "Edge 0-1 exists: " << (g.hasEdge(0, 1) ? "true" : "false") << std::endl;
    std::cout << "Edge 0-4 exists: " << (g.hasEdge(0, 4) ? "true" : "false") << std::endl;

    std::cout << "\nBFS from 0: ";
    auto bfsResult = g.bfs(0);
    for (size_t i = 0; i < bfsResult.size(); ++i) {
        std::cout << bfsResult[i];
        if (i < bfsResult.size() - 1) std::cout << ", ";
    }
    std::cout << std::endl;

    std::cout << "DFS from 0: ";
    auto dfsResult = g.dfs(0);
    for (size_t i = 0; i < dfsResult.size(); ++i) {
        std::cout << dfsResult[i];
        if (i < dfsResult.size() - 1) std::cout << ", ";
    }
    std::cout << std::endl;

    std::cout << "DFS iterative from 0: ";
    auto dfsIterResult = g.dfsIterative(0);
    for (size_t i = 0; i < dfsIterResult.size(); ++i) {
        std::cout << dfsIterResult[i];
        if (i < dfsIterResult.size() - 1) std::cout << ", ";
    }
    std::cout << std::endl;

    std::cout << "\n=== Directed Graph Cycle Detection ===" << std::endl;
    GraphAdjacencyList dg(true); // directed graph
    dg.addEdge(0, 1); // A -> B
    dg.addEdge(1, 2); // B -> C
    dg.addEdge(2, 0); // C -> A (creates cycle)
    std::cout << "Has cycle: " << (dg.hasCycle() ? "true" : "false") << std::endl;

    std::cout << "\n=== Weighted Graph & Shortest Path Demo ===" << std::endl;
    WeightedGraph wg(false); // undirected weighted graph
    wg.addEdge(0, 1, 4); // A, B
    wg.addEdge(0, 2, 2); // A, C
    wg.addEdge(1, 2, 1); // B, C
    wg.addEdge(1, 3, 5); // B, D
    wg.addEdge(2, 3, 8); // C, D
    wg.addEdge(2, 4, 10); // C, E
    wg.addEdge(3, 4, 2); // D, E

    std::cout << "Weighted graph:" << std::endl;
    wg.print();

    std::cout << "\nDijkstra's shortest paths from 0:" << std::endl;
    auto distances = wg.dijkstra(0);
    for (const auto& pair : distances) {
        std::cout << "  " << pair.first << ": " << pair.second << std::endl;
    }

    std::cout << "\nBellman-Ford shortest paths from 0:" << std::endl;
    try {
        auto bfDistances = wg.bellmanFord(0);
        for (const auto& pair : bfDistances) {
            std::cout << "  " << pair.first << ": " << pair.second << std::endl;
        }
    } catch (const std::exception& e) {
        std::cout << "Error: " << e.what() << std::endl;
    }
}

int main() {
    std::cout << "DSA DATA STRUCTURES AND ALGORITHMS - C++ IMPLEMENTATION" << std::endl;
    std::cout << "========================================================" << std::endl;
    std::cout << "This program demonstrates all the data structures and algorithms" << std::endl;
    std::cout << "originally implemented in Python, now converted to C++." << std::endl;

    demonstrateSearchingAlgorithms();
    demonstrateSortingAlgorithms();
    demonstrateArrays();
    demonstrateLinkedLists();
    demonstrateStacks();
    demonstrateQueues();
    demonstrateHashTables();
    demonstrateTrees();
    demonstrateGraphs();

    std::cout << "\n===========================================" << std::endl;
    std::cout << "ALL DEMONSTRATIONS COMPLETED!" << std::endl;
    std::cout << "===========================================" << std::endl;

    return 0;
}