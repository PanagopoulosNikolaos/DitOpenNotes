#include <iostream>
#include <vector>
#include <queue>
#include <memory>

/**
 * @brief TREES - Data Structure Implementation in C++
 * 
 * A tree is a hierarchical data structure consisting of nodes connected by edges. It has a root node
 * and subtrees of children nodes. Trees are used to represent hierarchical relationships.
 * 
 * Key Characteristics:
 * - Root: Top node with no parent
 * - Parent/Child: Nodes connected by edges
 * - Leaf: Node with no children
 * - Height: Longest path from root to leaf
 * - Depth: Distance from root to a node
 * - Binary Tree: Each node has at most 2 children
 * - Binary Search Tree (BST): Left child < parent < right child
 * 
 * Binary Tree Traversals:
 * 1. Pre-order: Root → Left → Right (used for copying tree)
 * 2. In-order: Left → Root → Right (gives sorted order in BST)
 * 3. Post-order: Left → Right → Root (used for deleting tree)
 * 4. Level-order: Visit nodes level by level (BFS)
 * 
 * Visual Example (Binary Search Tree):
 *         50
 *        /  \
 *       30   70
 *      / \ / \
 *     20 40 60 80
 * 
 * In-order: 20, 30, 40, 50, 60, 70, 80 (sorted)
 * Pre-order: 50, 30, 20, 40, 70, 60, 80
 * Post-order: 20, 40, 30, 60, 80, 70, 50
 * Level-order: 50, 30, 70, 20, 40, 60, 80
 * 
 * Common Use Cases:
 * - File systems (directory structure)
 * - DOM tree in browsers
 * - Database indexing (B-trees, B+ trees)
 * - Expression trees in compilers
 * - Decision trees in machine learning
 * - Autocomplete (Trie)
 */

struct TreeNode {
    int data;
    std::shared_ptr<TreeNode> left;
    std::shared_ptr<TreeNode> right;

    explicit TreeNode(int data) : data(data), left(nullptr), right(nullptr) {}
};

class BinaryTree {
protected:
    std::shared_ptr<TreeNode> root;

    void _preorderTraversal(std::shared_ptr<TreeNode> node, std::vector<int>& result) {
        if (node) {
            result.push_back(node->data);
            _preorderTraversal(node->left, result);
            _preorderTraversal(node->right, result);
        }
    }

    void _inorderTraversal(std::shared_ptr<TreeNode> node, std::vector<int>& result) {
        if (node) {
            _inorderTraversal(node->left, result);
            result.push_back(node->data);
            _inorderTraversal(node->right, result);
        }
    }

    void _postorderTraversal(std::shared_ptr<TreeNode> node, std::vector<int>& result) {
        if (node) {
            _postorderTraversal(node->left, result);
            _postorderTraversal(node->right, result);
            result.push_back(node->data);
        }
    }

    int _heightRecursive(std::shared_ptr<TreeNode> node) {
        if (node == nullptr) {
            return -1;
        }

        int leftHeight = _heightRecursive(node->left);
        int rightHeight = _heightRecursive(node->right);

        return 1 + std::max(leftHeight, rightHeight);
    }

public:
    /**
     * @brief Basic binary tree implementation with traversal methods.
     */
    BinaryTree() : root(nullptr) {}

    /**
     * @brief Pre-order: Root → Left → Right - O(n)
     */
    std::vector<int> preorderTraversal() {
        std::vector<int> result;
        _preorderTraversal(root, result);
        return result;
    }

    /**
     * @brief In-order: Left → Root → Right - O(n)
     */
    std::vector<int> inorderTraversal() {
        std::vector<int> result;
        _inorderTraversal(root, result);
        return result;
    }

    /**
     * @brief Post-order: Left → Right → Root - O(n)
     */
    std::vector<int> postorderTraversal() {
        std::vector<int> result;
        _postorderTraversal(root, result);
        return result;
    }

    /**
     * @brief Level-order (BFS): Visit level by level - O(n)
     */
    std::vector<int> levelorderTraversal() {
        if (!root) {
            return {};
        }

        std::vector<int> result;
        std::queue<std::shared_ptr<TreeNode>> q;
        q.push(root);

        while (!q.empty()) {
            auto node = q.front();
            q.pop();
            result.push_back(node->data);

            if (node->left) {
                q.push(node->left);
            }
            if (node->right) {
                q.push(node->right);
            }
        }

        return result;
    }

    /**
     * @brief Calculate height of tree - O(n)
     */
    int height() {
        return _heightRecursive(root);
    }

    void setRoot(int data) {
        root = std::make_shared<TreeNode>(data);
    }

    std::shared_ptr<TreeNode> getRoot() const {
        return root;
    }

    void setLeftChild(std::shared_ptr<TreeNode> parent, int data) {
        if (parent) {
            parent->left = std::make_shared<TreeNode>(data);
        }
    }

    void setRightChild(std::shared_ptr<TreeNode> parent, int data) {
        if (parent) {
            parent->right = std::make_shared<TreeNode>(data);
        }
    }
};

class BinarySearchTree : public BinaryTree {
private:
    size_t _size;

    std::shared_ptr<TreeNode> _insertRecursive(std::shared_ptr<TreeNode> node, int data) {
        if (node == nullptr) {
            ++_size;
            return std::make_shared<TreeNode>(data);
        }

        if (data < node->data) {
            node->left = _insertRecursive(node->left, data);
        } else {
            node->right = _insertRecursive(node->right, data);
        }

        return node;
    }

    std::shared_ptr<TreeNode> _searchRecursive(std::shared_ptr<TreeNode> node, int data) {
        if (node == nullptr || node->data == data) {
            return node;
        }

        if (data < node->data) {
            return _searchRecursive(node->left, data);
        } else {
            return _searchRecursive(node->right, data);
        }
    }

    std::shared_ptr<TreeNode> _deleteRecursive(std::shared_ptr<TreeNode> node, int data) {
        if (node == nullptr) {
            return nullptr;
        }

        if (data < node->data) {
            node->left = _deleteRecursive(node->left, data);
        } else if (data > node->data) {
            node->right = _deleteRecursive(node->right, data);
        } else {
            // Node to be deleted found
            --_size;

            // Node with only one child or no child
            if (node->left == nullptr) {
                return node->right;
            } else if (node->right == nullptr) {
                return node->left;
            }

            // Node with two children: get inorder successor
            auto minLargerNode = _findMin(node->right);
            node->data = minLargerNode->data;
            node->right = _deleteRecursive(node->right, minLargerNode->data);
        }

        return node;
    }

    std::shared_ptr<TreeNode> _findMin(std::shared_ptr<TreeNode> node) {
        while (node->left) {
            node = node->left;
        }
        return node;
    }

public:
    /**
     * @brief Binary Search Tree where left child < parent < right child.
     * Provides efficient search, insert, and delete operations.
     */
    BinarySearchTree() : _size(0) {}

    size_t size() const {
        return _size;
    }

    bool empty() const {
        return root == nullptr;
    }

    /**
     * @brief Insert value into BST - O(log n) average, O(n) worst
     */
    void insert(int data) {
        root = _insertRecursive(root, data);
    }

    /**
     * @brief Search for value in BST - O(log n) average, O(n) worst
     */
    bool search(int data) {
        return _searchRecursive(root, data) != nullptr;
    }

    /**
     * @brief Delete value from BST - O(log n) average, O(n) worst
     */
    void remove(int data) {
        root = _deleteRecursive(root, data);
    }

    /**
     * @brief Find minimum value in tree - O(log n) average
     */
    int findMin() {
        if (empty()) {
            throw std::runtime_error("Tree is empty");
        }
        auto minNode = _findMin(root);
        return minNode->data;
    }

    /**
     * @brief Find maximum value in tree - O(log n) average
     */
    int findMax() {
        if (empty()) {
            throw std::runtime_error("Tree is empty");
        }
        auto current = root;
        while (current->right) {
            current = current->right;
        }
        return current->data;
    }

    /**
     * @brief In-order traversal (returns sorted order) - O(n)
     */
    std::vector<int> inorderTraversal() {
        std::vector<int> result;
        _inorderTraversal(root, result);
        return result;
    }

    void _inorderTraversal(std::shared_ptr<TreeNode> node, std::vector<int>& result) {
        if (node) {
            _inorderTraversal(node->left, result);
            result.push_back(node->data);
            _inorderTraversal(node->right, result);
        }
    }
};

struct AVLNode {
    int data;
    std::shared_ptr<AVLNode> left;
    std::shared_ptr<AVLNode> right;
    int height;

    explicit AVLNode(int data) : data(data), left(nullptr), right(nullptr), height(1) {}
};

class AVLTree {
private:
    std::shared_ptr<AVLNode> root;

    int _getHeight(std::shared_ptr<AVLNode> node) {
        if (!node) {
            return 0;
        }
        return node->height;
    }

    int _getBalance(std::shared_ptr<AVLNode> node) {
        if (!node) {
            return 0;
        }
        return _getHeight(node->left) - _getHeight(node->right);
    }

    std::shared_ptr<AVLNode> _rotateLeft(std::shared_ptr<AVLNode> z) {
        auto y = z->right;
        auto T2 = y->left;

        y->left = z;
        z->right = T2;

        z->height = 1 + std::max(_getHeight(z->left), _getHeight(z->right));
        y->height = 1 + std::max(_getHeight(y->left), _getHeight(y->right));

        return y;
    }

    std::shared_ptr<AVLNode> _rotateRight(std::shared_ptr<AVLNode> z) {
        auto y = z->left;
        auto T3 = y->right;

        y->right = z;
        z->left = T3;

        z->height = 1 + std::max(_getHeight(z->left), _getHeight(z->right));
        y->height = 1 + std::max(_getHeight(y->left), _getHeight(y->right));

        return y;
    }

    std::shared_ptr<AVLNode> _insertRecursive(std::shared_ptr<AVLNode> node, int data) {
        if (!node) {
            return std::make_shared<AVLNode>(data);
        }

        if (data < node->data) {
            node->left = _insertRecursive(node->left, data);
        } else {
            node->right = _insertRecursive(node->right, data);
        }

        node->height = 1 + std::max(_getHeight(node->left), _getHeight(node->right));

        int balance = _getBalance(node);

        // Left-Left case
        if (balance > 1 && data < node->left->data) {
            return _rotateRight(node);
        }

        // Right-Right case
        if (balance < -1 && data > node->right->data) {
            return _rotateLeft(node);
        }

        // Left-Right case
        if (balance > 1 && data > node->left->data) {
            node->left = _rotateLeft(node->left);
            return _rotateRight(node);
        }

        // Right-Left case
        if (balance < -1 && data < node->right->data) {
            node->right = _rotateRight(node->right);
            return _rotateLeft(node);
        }

        return node;
    }

    void _inorderTraversal(std::shared_ptr<AVLNode> node, std::vector<int>& result) {
        if (node) {
            _inorderTraversal(node->left, result);
            result.push_back(node->data);
            _inorderTraversal(node->right, result);
        }
    }

public:
    /**
     * @brief Self-balancing Binary Search Tree (AVL Tree).
     * Maintains balance by ensuring height difference between left and right subtrees ≤ 1.
     */
    AVLTree() : root(nullptr) {}

    /**
     * @brief Insert value and rebalance - O(log n)
     */
    void insert(int data) {
        root = _insertRecursive(root, data);
    }

    /**
     * @brief In-order traversal - O(n)
     */
    std::vector<int> inorderTraversal() {
        std::vector<int> result;
        _inorderTraversal(root, result);
        return result;
    }
};

// Example usage
int main() {
    std::cout << "=== Binary Tree Traversals Demo ===" << std::endl;
    BinaryTree bt;
    auto rootNode = std::make_shared<TreeNode>(50);
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

    return 0;
}