## 1. Heaps - Definition and Differences

A heap is a complete binary tree where the key of each node satisfies a specific relationship with its children.

### Difference Between Max Heap and Min Heap

**Max Heap**: The value of each parent node is greater than or equal to the values of its children, with the maximum value at the root.

**Min Heap**: The value of each parent node is less than or equal to the values of its children, with the minimum value at the root.

### Maintaining Heap Property

**Insertion**: The new element is placed at the end of the heap. The heapify process then compares the element with its parent and swaps them if the heap property is violated, repeating until the property is restored.

**Deletion**: Typically the root (maximum/minimum) is deleted. The last element is moved to the root and the heapify process compares the element with its children, swapping it with the larger (max heap) or smaller (min heap) child, repeating until the property is restored.


## 2. Heaps and Priority Queues

### Why Are Heaps Suitable?

Heaps are considered suitable for implementing priority queues due to the heap order property, which ensures that the root always contains the maximum or minimum element, allowing quick extraction. Additionally, the basic insertion and deletion operations run in O(log N) time, while initial construction takes O(N), making them efficient for large data collections.

### Real-World Application Examples

1. Task Scheduling: In operating systems, processes/threads are maintained in a priority queue with their priorities as keys, allowing quick selection of the next process to execute.​

2. Dijkstra's Algorithm: For finding shortest paths in graphs, a priority queue is used to always select the node with the smallest distance for processing.


## 3. Hash Function
A **hash function** is a mathematical function that takes an arbitrary-sized number (key) and produces a fixed-size integer (hash value), which indicates a position in the hash table.

### Characteristics of an Efficient Hash Function

**1. Deterministic:**
- The same key always produces the same hash value
- If h(x) = 5 today, h(x) = 5 always

**2. Uniform Distribution:**
- Hash values are distributed uniformly across the space
- Avoids clustering that causes collisions

**3. Fast Computation:**
- Computation time should be O(1) or O(|key|)
- It should not be more time-consuming than the operation that triggers it

**4. Collision Minimization:**
- Different keys should produce different hash values
- Practically impossible for all keys, but they should be minimized

**5. Output Normalization:**
- h(key) mod table_size ensures the result is within bounds

```python
class HashFunction:
    def __init__(self, table_size):
        self.table_size = table_size
    
    def python_hash(self, key):
        return hash(key) % self.table_size
    
    # Polynomial rolling hash (custom implementation)
    def polynomial_hash(self, key, base=31):
        hash_value = 0
        for char in key:
            hash_value = (hash_value * base + ord(char)) % self.table_size
        return hash_value
    
    # Using hash() with absolute value for consistency
    def stable_hash(self, key):
        return abs(hash(key)) % self.table_size

# Example usage
hasher = HashFunction(table_size=10)
print(f"python_hash('apple'): {hasher.python_hash('apple')}")
print(f"stable_hash('apple'): {hasher.stable_hash('apple')}")
print(f"polynomial_hash('apple'): {hasher.polynomial_hash('apple')}")
print(f"python_hash(123): {hasher.python_hash(123)}")
```

## 4. Collision Resolution Strategies
## Chaining

Creates a linked list of elements with the same hash at the same table position.

**Advantages:**
- Simple implementation
- The table never fills up - there is no element limit
- Efficient for high load factor (lambda)
- Easy element deletion

**Disadvantages:**
- Requires extra memory for pointers
- Poor cache usage (non-contiguous memory)
- Worse performance if lists grow too large

## Open Addressing

Applies a secondary hash function continuously until an empty slot is found. Includes linear/quadratic probing and double hashing.

**Advantages:**
- Does not require extra memory for pointers
- Better cache performance (contiguous memory)
- For double hashing: avoids primary/secondary clustering, approaches optimal search cost

**Disadvantages:**
- The table fills up (limited size)
- Worse performance with high load factor (lambda)
- For double hashing: requires additional hash computation
- More complex deletion


## 5. Huffman Coding

The basic idea of Huffman coding is assigning variable-length binary codes to characters, where more frequent characters receive shorter codes to minimize the total data size.

### Huffman Tree Construction
The construction follows a greedy algorithm bottom-up:
1.  **Initialization**: A leaf node is created for each character with a weight equal to its frequency.
2.  **Sorting/Queue**: All nodes are inserted into a priority queue ordered by ascending frequency.
3.  **Merging**: The two nodes with the lowest frequencies are extracted. A new internal parent node is created with a frequency equal to the sum of its two children's frequencies.
4.  **Repetition**: The new node is reinserted into the queue. The process repeats until a single node remains (the root).
5.  **Encoding**: Edges to left children are typically assigned the value '0' and to right children the value '1', generating codes as paths from root to leaves.

### Optimality with Respect to Length
Huffman is optimal because it minimizes the weighted path length of the tree, which corresponds to the average code word length:
*   **Prefix Property**: It produces a prefix code, eliminating the need for separator symbols and ensuring unambiguous decoding.
*   **Frequency Mapping**: The algorithm guarantees that symbols with the highest frequency are closer to the root (smaller depth), thus having fewer bits. Conversely, rare symbols are pushed to deeper levels.
*   **Mathematical Proof**: It is proven that for a given probability distribution, there is no other prefix code that yields a smaller expected code word length $$\sum p_i l_i$$ than the Huffman code.
