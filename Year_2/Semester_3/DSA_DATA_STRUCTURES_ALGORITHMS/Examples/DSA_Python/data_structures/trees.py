"""
TREES - Data Structure Implementation


A tree is a hierarchical data structure consisting of nodes connected by edges. It has a root node
and subtrees of children nodes. Trees are used to represent hierarchical relationships.


Key Characteristics:
- Root: Top node with no parent
- Parent/Child: Nodes connected by edges
- Leaf: Node with no children
- Height: Longest path from root to leaf
- Depth: Distance from root to a node
- Binary Tree: Each node has at most 2 children
- Binary Search Tree (BST): Left child < parent < right child


Binary Tree Traversals:
1. Pre-order: Root → Left → Right (used for copying tree)
2. In-order: Left → Root → Right (gives sorted order in BST)
3. Post-order: Left → Right → Root (used for deleting tree)
4. Level-order: Visit nodes level by level (BFS)


Visual Example (Binary Search Tree):
        50
       /  \\
      30   70
     / \\ / \\
    20 40 60 80


In-order: 20, 30, 40, 50, 60, 70, 80 (sorted)
Pre-order: 50, 30, 20, 40, 70, 60, 80
Post-order: 20, 40, 30, 60, 80, 70, 50
Level-order: 50, 30, 70, 20, 40, 60, 80


Common Use Cases:
- File systems (directory structure)
- DOM tree in browsers
- Database indexing (B-trees, B+ trees)
- Expression trees in compilers
- Decision trees in machine learning
- Autocomplete (Trie)
"""


class TreeNode:
    """Node for binary tree"""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    """
    Basic binary tree implementation with traversal methods.
    """
    
    def __init__(self):
        self.root = None
    
    def preorder_traversal(self, node=None, result=None):
        """Pre-order: Root → Left → Right - O(n)"""
        if result is None:
            result = []
            node = self.root
        
        if node:
            result.append(node.data)
            self.preorder_traversal(node.left, result)
            self.preorder_traversal(node.right, result)
        
        return result
    
    def inorder_traversal(self, node=None, result=None):
        """In-order: Left → Root → Right - O(n)"""
        if result is None:
            result = []
            node = self.root
        
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.data)
            self.inorder_traversal(node.right, result)
        
        return result
    
    def postorder_traversal(self, node=None, result=None):
        """Post-order: Left → Right → Root - O(n)"""
        if result is None:
            result = []
            node = self.root
        
        if node:
            self.postorder_traversal(node.left, result)
            self.postorder_traversal(node.right, result)
            result.append(node.data)
        
        return result
    
    def levelorder_traversal(self):
        """Level-order (BFS): Visit level by level - O(n)"""
        if not self.root:
            return []
        
        result = []
        queue = [self.root]
        
        while queue:
            node = queue.pop(0)
            result.append(node.data)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return result
    
    def height(self, node=None):
        """Calculate height of tree - O(n)"""
        if node is None:
            node = self.root
        
        return self._height_recursive(node)
    
    def _height_recursive(self, node):
        """Helper for height calculation"""
        if node is None:
            return -1
        
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        
        return 1 + max(left_height, right_height)


class BinarySearchTree:
    """
    Binary Search Tree where left child < parent < right child.
    Provides efficient search, insert, and delete operations.
    """
    
    def __init__(self):
        self.root = None
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self.root is None
    
    def insert(self, data):
        """Insert value into BST - O(log n) average, O(n) worst"""
        self.root = self._insert_recursive(self.root, data)
        self._size += 1
    
    def _insert_recursive(self, node, data):
        """Helper method for insertion"""
        if node is None:
            return TreeNode(data)
        
        if data < node.data:
            node.left = self._insert_recursive(node.left, data)
        else:
            node.right = self._insert_recursive(node.right, data)
        
        return node
    
    def search(self, data):
        """Search for value in BST - O(log n) average, O(n) worst"""
        return self._search_recursive(self.root, data)
    
    def _search_recursive(self, node, data):
        """Helper method for search"""
        if node is None:
            return False
        
        if data == node.data:
            return True
        elif data < node.data:
            return self._search_recursive(node.left, data)
        else:
            return self._search_recursive(node.right, data)
    
    def delete(self, data):
        """Delete value from BST - O(log n) average, O(n) worst"""
        self.root = self._delete_recursive(self.root, data)
        self._size -= 1
    
    def _delete_recursive(self, node, data):
        """Helper method for deletion"""
        if node is None:
            return None
        
        if data < node.data:
            node.left = self._delete_recursive(node.left, data)
        elif data > node.data:
            node.right = self._delete_recursive(node.right, data)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            # Node with two children: get inorder successor
            min_larger_node = self._find_min(node.right)
            node.data = min_larger_node.data
            node.right = self._delete_recursive(node.right, min_larger_node.data)
        
        return node
    
    def _find_min(self, node):
        """Find minimum value node in subtree"""
        current = node
        while current.left:
            current = current.left
        return current
    
    def find_min(self):
        """Find minimum value in tree - O(log n) average"""
        if self.is_empty():
            return None
        return self._find_min(self.root).data
    
    def find_max(self):
        """Find maximum value in tree - O(log n) average"""
        if self.is_empty():
            return None
        current = self.root
        while current.right:
            current = current.right
        return current.data
    
    def inorder_traversal(self):
        """In-order traversal (returns sorted order) - O(n)"""
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        """Helper for in-order traversal"""
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.data)
            self._inorder_recursive(node.right, result)


class AVLNode:
    """Node for AVL tree with height tracking"""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    """
    Self-balancing Binary Search Tree (AVL Tree).
    Maintains balance by ensuring height difference between left and right subtrees ≤ 1.
    """
    
    def __init__(self):
        self.root = None
    
    def _get_height(self, node):
        """Get height of node"""
        if not node:
            return 0
        return node.height
    
    def _get_balance(self, node):
        """Get balance factor of node"""
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)
    
    def _rotate_left(self, z):
        """Left rotation"""
        y = z.right
        T2 = y.left
        
        y.left = z
        z.right = T2
        
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        
        return y
    
    def _rotate_right(self, z):
        """Right rotation"""
        y = z.left
        T3 = y.right
        
        y.right = z
        z.left = T3
        
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        
        return y
    
    def insert(self, data):
        """Insert value and rebalance - O(log n)"""
        self.root = self._insert_recursive(self.root, data)
    
    def _insert_recursive(self, node, data):
        """Helper for insertion with rebalancing"""
        if not node:
            return AVLNode(data)
        
        if data < node.data:
            node.left = self._insert_recursive(node.left, data)
        else:
            node.right = self._insert_recursive(node.right, data)
        
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        
        balance = self._get_balance(node)
        
        # Left-Left case
        if balance > 1 and data < node.left.data:
            return self._rotate_right(node)
        
        # Right-Right case
        if balance < -1 and data > node.right.data:
            return self._rotate_left(node)
        
        # Left-Right case
        if balance > 1 and data > node.left.data:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        
        # Right-Left case
        if balance < -1 and data < node.right.data:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        
        return node
    
    def inorder_traversal(self):
        """In-order traversal - O(n)"""
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        """Helper for in-order traversal"""
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.data)
            self._inorder_recursive(node.right, result)


# Example usage
if __name__ == "__main__":
    print("=== Binary Tree Traversals Demo ===")
    bt = BinaryTree()
    bt.root = TreeNode(50)
    bt.root.left = TreeNode(30)
    bt.root.right = TreeNode(70)
    bt.root.left.left = TreeNode(20)
    bt.root.left.right = TreeNode(40)
    bt.root.right.left = TreeNode(60)
    bt.root.right.right = TreeNode(80)
    
    print(f"Pre-order: {bt.preorder_traversal()}")
    print(f"In-order: {bt.inorder_traversal()}")
    print(f"Post-order: {bt.postorder_traversal()}")
    print(f"Level-order: {bt.levelorder_traversal()}")
    print(f"Height: {bt.height()}")
    
    print("\n=== Binary Search Tree Demo ===")
    bst = BinarySearchTree()
    
    values = [50, 30, 70, 20, 40, 60, 80]
    for val in values:
        bst.insert(val)
    
    print(f"Inserted: {values}")
    print(f"In-order (sorted): {bst.inorder_traversal()}")
    print(f"Size: {len(bst)}")
    
    # Search
    print(f"Search 40: {bst.search(40)}")
    print(f"Search 100: {bst.search(100)}")
    
    # Min/Max
    print(f"Min: {bst.find_min()}")
    print(f"Max: {bst.find_max()}")
    
    # Delete
    bst.delete(30)
    print(f"After deleting 30: {bst.inorder_traversal()}")
    
    print("\n=== AVL Tree Demo ===")
    avl = AVLTree()
    
    values = [10, 20, 30, 40, 50, 25]
    for val in values:
        avl.insert(val)
        print(f"Inserted {val}: {avl.inorder_traversal()}")
    
    print(f"Final AVL tree (in-order): {avl.inorder_traversal()}")
