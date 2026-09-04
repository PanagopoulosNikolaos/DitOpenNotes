## 1. Binary Tree - Characteristics

The **binary tree** is a data structure where each node has at most two children (left and right).

### Main Characteristics:

**Node degree**: The number of its children. In a binary tree: 0, 1 or 2.

**Root**: The topmost node without a parent.

**Leaves**: Nodes with degree 0 (without children).

**Internal nodes**: Nodes with at least one child.

**Height**: The length of the longest path from the root to a leaf. For a tree with a single node, the height is 0.

**Node depth**: The length of the path from the root to that node.

**Level**: All nodes at the same depth belong to the same level. The root is at level 0.



## 2. Binary Search Tree (BST)

The **Binary Search Tree (BST)** is a binary tree with a special property:

**Basic BST Property:**
- All values in the left subtree are **smaller** than the node's value
- All values in the right subtree are **larger** than the node's value
- Each subtree is also a BST

**How it helps efficient search:**
This property allows the application of binary search. At each step, we can eliminate half the tree, resulting in **O(log n)** complexity for a balanced BST (instead of O(n) in an unsorted structure).


### C++

```cpp
#include <iostream>

struct BSTNode {
    int value;
    BSTNode* left;
    BSTNode* right;
    
    BSTNode(int val) : value(val), left(nullptr), right(nullptr) {}
};

class BST {
private:
    BSTNode* root;
    
    BSTNode* insertRecursive(BSTNode* node, int value) {
        if (node == nullptr) {
            return new BSTNode(value);
        }
        if (value < node->value) {
            node->left = insertRecursive(node->left, value);
        } else {
            node->right = insertRecursive(node->right, value);
        }
        return node;
    }
    
    bool searchRecursive(BSTNode* node, int value) {
        if (node == nullptr) return false;
        if (node->value == value) return true;
        if (value < node->value) {
            return searchRecursive(node->left, value);
        } else {
            return searchRecursive(node->right, value);
        }
    }

    void destroy(BSTNode* node) {
        if (node == nullptr) return;
        destroy(node->left);
        destroy(node->right);
        delete node;
    }

public:
    BST() : root(nullptr) {}
    
    ~BST() {
        destroy(root);
        root = nullptr;
    }
    
    // Insert new value into BST
    void insert(int value) {
        root = insertRecursive(root, value);
    }
    
    // Search for value - O(log n) for balanced tree
    bool search(int value) {
        return searchRecursive(root, value);
    }
    
    // Finds the minimum value
    int findMin() {
        BSTNode* current = root;
        while (current->left != nullptr) {
            current = current->left;
        }
        return current->value;
    }
    
    // Finds the maximum value
    int findMax() {
        BSTNode* current = root;
        while (current->right != nullptr) {
            current = current->right;
        }
        return current->value;
    }
};

int main() {
    BST bst;
    int values[] = {50, 30, 70, 20, 40, 60, 80};
    
    for (int val : values) {
        bst.insert(val);
    }
    
    std::cout << "Search 40: " << (bst.search(40) ? "Found" : "Not found") << std::endl;
    std::cout << "Search 100: " << (bst.search(100) ? "Found" : "Not found") << std::endl;
    std::cout << "Minimum value: " << bst.findMin() << std::endl;
    std::cout << "Maximum value: " << bst.findMax() << std::endl;
    
    return 0;
}
```


## 3. Tree Traversals

### **Pre-order:** Root → Left → Right
- Visit the node first, then the left and right subtrees
- Usage: Tree copying, prefix expressions

### **In-order:** Left → Root → Right
- Visit the left subtree first, then the node, then the right
- **Produces sorted output for BST!** because the BST property (left < root < right) guarantees ascending order

### **Post-order:** Left → Right → Root
- Visit the subtrees first, then the node
- Usage: Tree deletion, postfix expressions


## 4. Balanced Trees

A tree is considered **balanced** when for each node, the height of the left and right subtrees differs by at most 1.

**Impact of balance on performance:**

| Operation | Unbalanced BST | Balanced BST |
|---|---|---|
| Search | O(n) (worst case) | O(log n) |
| Insertion | O(n) (worst case) | O(log n) |
| Deletion | O(n) (worst case) | O(log n) |


## 5. AVL Trees

An AVL tree is a binary search tree that automatically maintains balance. Each node has a balance factor calculated as:

$$BF = \text{height of left subtree} - \text{height of right subtree}$$

For a valid AVL tree: $BF \in \{-1, 0, 1\}$ for every node.

### Four Basic Rotations

**1. LL (Left-Left) - Right Rotation**
- Problem: BF = 2, left child has BF ≥ 0
- Solution: A single right rotation on the unbalanced node

**2. RR (Right-Right) - Left Rotation**
- Problem: BF = -2, right child has BF ≤ 0
- Solution: A single left rotation on the unbalanced node

**3. LR (Left-Right) - Double Rotation**
- Problem: BF = 2, left child has BF < 0
- Solution: Left rotation on the left child, then right on the root

**4. RL (Right-Left) - Double Rotation**
- Problem: BF = -2, right child has BF > 0
- Solution: Right rotation on the right child, then left on the root

Rotations are performed after each insertion/deletion to maintain the condition $|BF| \leq 1$.
