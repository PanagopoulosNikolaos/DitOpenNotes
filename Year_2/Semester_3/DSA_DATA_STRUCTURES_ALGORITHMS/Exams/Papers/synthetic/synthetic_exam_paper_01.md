# University of Ioannina - Department of Informatics and Telecommunications
## Course: Data Structures and Algorithms (Course Code: 305)
### Academic Year: 2025-2026
### Synthetic Final Examination - Paper 01

**Time Allowed:** 3 Hours  
**Total Marks:** 100 Points  
**Instructions:**
- Answer all questions clearly and show all intermediate steps and derivations.
- Code submissions must conform to C++ standards with strict naming conventions (`PascalCase` for classes, `camelCase` for functions, `snake_case` for variables).
- Clearly sketch and label tree structures, balance factors, array indices, and hash table states.

---

### Question 1: Asymptotic Complexity & Recurrence Relations (15 Marks)

#### Part A (8 Marks)
Analyze the exact number of basic operations and find the tight asymptotic bound $\Theta(f(n))$ for the following algorithmic snippet:

```cpp
int sum_value = 0;
for (int i = 1; i <= n; i *= 2) {
    for (int j = 0; j < i; ++j) {
        for (int k = 1; k <= n; k += 2) {
            sum_value += (i * j) + k;
        }
    }
}
```

1. Express the total number of additions executed inside the innermost loop as a formal mathematical summation.
2. Evaluate the summation in closed form.
3. Conclude the tight Big-$\Theta$ bound.

#### Part B (7 Marks)
Solve the following recurrence relations using either the Master Theorem or the recursion tree method. Explicitly identify the case applied and state any regularity conditions where applicable.

1. $T(n) = 3T\left(\frac{n}{4}\right) + n \log_2 n$, with $T(1) = \Theta(1)$.
2. $T(n) = 4T\left(\frac{n}{2}\right) + n^2 \sqrt{n}$, with $T(1) = \Theta(1)$.

---

### Question 2: Binary Search Trees & Structural Integrity (12 Marks)

#### Part A (6 Marks)
Consider an initially empty Binary Search Tree (BST). Keys are inserted in the following sequential order:
$$\{45, 23, 68, 12, 34, 56, 89, 7, 28, 50\}$$

1. Draw the resulting BST after all insertions are completed.
2. State the pre-order, in-order, and post-order traversals of the resulting tree.
3. Calculate the height of the tree (height of a single-node tree defined as 0) and the balance factor for each node.

#### Part B (6 Marks)
Using the BST obtained from Part A:
1. Trace the deletion of key `23` using its **in-order successor**. Show the node replacement and the intermediate pointers updated.
2. Draw the final BST after the deletion of `23` is complete.
3. Is the resulting tree a valid AVL tree? Justify your answer by calculating the balance factors of all nodes along the path from the deleted node up to the root.

---

### Question 3: AVL Tree Sequential Construction & Rotations (16 Marks)

Construct an AVL tree by inserting the following sequence of keys one by one into an initially empty tree:
$$\{30, 20, 10, 40, 50, 25, 28\}$$

The balance factor for every node $u$ is defined as:
$$BF(u) = \text{height}(\text{left}(u)) - \text{height}(\text{right}(u))$$
where an empty child has height $-1$.

For each inserted key:
1. Insert the node as in a standard BST.
2. State the balance factors of all affected ancestors up to the root.
3. If an imbalance ($|BF| \ge 2$) occurs, identify the critical node and the type of rotation required:
   - Left-Left (LL / single right rotation)
   - Right-Right (RR / single left rotation)
   - Left-Right (LR / double left-right rotation)
   - Right-Left (RL / double right-left rotation)
4. Sketch the tree state immediately after each rotation until all 7 keys are successfully inserted.

---

### Question 4: AVL Node Deletion & Cascading Rebalancing (12 Marks)

Consider the balanced AVL tree containing the keys:
```
              44
            /    \
          17      62
         /  \    /  \
        10  28  50  78
            /         \
           22         88
```

1. Verify that all nodes satisfy the AVL balance condition $|BF| \le 1$.
2. Delete key `50` from the tree.
3. Trace the bottom-up rebalancing process. Identify any nodes that become unbalanced, the exact rotation applied, and sketch the final AVL tree.
4. Next, from the tree obtained in step 3, delete key `62` (a node with one child or two children depending on the previous rotation). Trace the rebalancing step and draw the final AVL tree.

---

### Question 5: Binary Heaps & Floyd's Linear-Time Construction (15 Marks)

#### Part A (9 Marks)
You are given the following 10-element array representing the level-order traversal of a complete binary tree:
$$A = [14, 33, 27, 45, 62, 19, 81, 92, 55, 38]$$

1. Draw the initial complete binary tree prior to heapification.
2. Apply **Floyd's bottom-up `buildHeap` algorithm** to transform array $A$ into a **Max-Heap**.
3. Detail every `percolateDown` (or `maxHeapify`) operation performed:
   - Identify each non-leaf index evaluated (from $\lfloor n/2 \rfloor - 1$ down to index $0$).
   - Show all key comparisons and element swaps step by step.
4. Provide the final array layout and draw the corresponding binary max-heap tree.

#### Part B (6 Marks)
Starting from the max-heap constructed in Part A:
1. Perform one `extractMax()` operation. Trace the replacement of the root by the last leaf element and the subsequent `percolateDown` cascade.
2. Show the array state immediately after the extraction.
3. Insert key `95` into this max-heap and trace the `percolateUp` cascade until the heap invariant is restored.

---

### Question 6: Hash Tables & Collision Resolution Strategies (15 Marks)

A hash table has capacity $M = 11$ (indices $0$ through $10$).
Keys are inserted into the table in the following order:
$$\{35, 12, 46, 23, 79, 57, 68\}$$

The primary hash function is:
$$h_1(k) = k \pmod{11}$$

The secondary hash function is:
$$h_2(k) = 7 - (k \pmod 7)$$

#### Part A: Separate Chaining (4 Marks)
Draw the hash table using separate chaining (linked list buckets). Insert new collisions at the tail of each linked list.

#### Part B: Linear Probing (5 Marks)
The probe sequence function is:
$$h(k, i) = (h_1(k) + i) \pmod{11}, \quad i = 0, 1, 2, \dots$$
1. Show the probe sequence and collision resolution for each key.
2. Provide the final contents of table array $T[0 \dots 10]$.
3. Calculate the average number of probes required for a **successful search** across the 7 inserted keys.

#### Part C: Double Hashing (6 Marks)
The double hashing probe sequence is:
$$h(k, i) = (h_1(k) + i \cdot h_2(k)) \pmod{11}, \quad i = 0, 1, 2, \dots$$
1. For each key, calculate $h_1(k)$ and $h_2(k)$.
2. Show the detailed probe sequence for keys that encounter collisions.
3. Write the final array state $T[0 \dots 10]$.
4. Calculate the number of probes needed to determine that key `90` is **not present** in the table (unsuccessful search).

---

### Question 7: Huffman Coding & Algorithmic Implementation (15 Marks)

#### Part A: Theoretical Huffman Tree (8 Marks)
A text file contains messages using an alphabet of six symbols $\Sigma = \{A, B, C, D, E, F\}$ with the following character frequencies:

| Symbol | Frequency ($f_i$) |
|:------:|:-----------------:|
| A      | 28                |
| B      | 15                |
| C      | 12                |
| D      | 22                |
| E      | 5                 |
| F      | 18                |

1. Show the step-by-step construction of the optimal Huffman prefix tree using a min-priority queue. At each step, record the two trees extracted and the newly merged tree with its combined weight.
2. Label left branches with `0` and right branches with `1`.
3. Provide the resulting variable-length binary code for each symbol.
4. Calculate:
   - The total bit length of the compressed message.
   - The average code length $L_{\text{avg}} = \sum p_i l_i$.
   - The compression ratio compared to standard uncompressed 8-bit ASCII encoding.

#### Part B: C++ Implementation (7 Marks)
Write a C++ function `hoarePartition` that implements the Hoare partition scheme for the QuickSort algorithm.

**Specifications:**
- Function signature: `int hoarePartition(std::vector<int>& arr_data, int low_idx, int high_idx)`
- The pivot must be chosen as `arr_data[low_idx]`.
- Two pointers `left_ptr` and `right_ptr` start beyond the boundaries and move inwards.
- All code must conform strictly to the project coding standard:
  - Function name: `camelCase`
  - Variables: `snake_case`
  - Google Style docstring with Args and Returns.
  - Explanatory single-line comments explaining why the swap or pointer movement occurs.

