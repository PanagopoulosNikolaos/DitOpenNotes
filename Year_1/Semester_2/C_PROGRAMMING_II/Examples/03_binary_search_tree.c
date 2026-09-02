/**
 * Demonstrates a Binary Search Tree (BST) implementation in C.
 * Includes insertion, recursive search, in-order traversal,
 * and post-order deallocation.
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

/**
 * Node in a Binary Search Tree.
 */
typedef struct TreeNode {
    int key;
    struct TreeNode *left;
    struct TreeNode *right;
} TreeNode;

/**
 * Allocates and initializes a new BST node.
 * Args:
 * key (int): The integer key value.
 * Returns:
 * TreeNode*: Pointer to newly created node, or NULL upon failure.
 */
TreeNode *createTreeNode(int key) {
    TreeNode *node = (TreeNode *)malloc(sizeof(TreeNode));
    if (node == NULL) {
        perror("Memory allocation error for tree node");
        return NULL;
    }
    node->key = key;
    node->left = NULL;
    node->right = NULL;
    return node;
}

/**
 * Inserts a key into the BST recursively.
 * Args:
 * root (TreeNode*): Root of the tree/subtree.
 * key (int): Value to insert.
 * Returns:
 * TreeNode*: Updated root pointer.
 */
TreeNode *insertBST(TreeNode *root, int key) {
    if (root == NULL) {
        return createTreeNode(key);
    }
    if (key < root->key) {
        root->left = insertBST(root->left, key);
    } else if (key > root->key) {
        root->right = insertBST(root->right, key);
    }
    return root;
}

/**
 * Searches for a key in the BST.
 * Args:
 * root (const TreeNode*): Root of tree.
 * key (int): Value to locate.
 * Returns:
 * bool: true if key exists, false otherwise.
 */
bool searchBST(const TreeNode *root, int key) {
    if (root == NULL) {
        return false;
    }
    if (root->key == key) {
        return true;
    }
    if (key < root->key) {
        return searchBST(root->left, key);
    }
    return searchBST(root->right, key);
}

/**
 * Performs in-order traversal (prints keys in ascending sorted order).
 * Args:
 * root (const TreeNode*): Root of tree.
 * Returns:
 * void: No return value.
 */
void inOrderTraversal(const TreeNode *root) {
    if (root != NULL) {
        inOrderTraversal(root->left);
        printf("%d ", root->key);
        inOrderTraversal(root->right);
    }
}

/**
 * Recursively frees all tree nodes using post-order traversal.
 * Args:
 * root (TreeNode*): Root of tree.
 * Returns:
 * void: No return value.
 */
void freeTree(TreeNode *root) {
    if (root != NULL) {
        freeTree(root->left);
        freeTree(root->right);
        free(root);
    }
}

int main(void) {
    TreeNode *root = NULL;
    int values[] = {50, 30, 20, 40, 70, 60, 80};
    size_t count = sizeof(values) / sizeof(values[0]);

    for (size_t i = 0; i < count; i++) {
        root = insertBST(root, values[i]);
    }

    printf("In-order traversal of BST (sorted order):\n");
    inOrderTraversal(root);
    printf("\n");

    int search_target = 60;
    if (searchBST(root, search_target)) {
        printf("Key %d was successfully found in BST.\n", search_target);
    } else {
        printf("Key %d was not found.\n", search_target);
    }

    search_target = 99;
    if (searchBST(root, search_target)) {
        printf("Key %d was found.\n", search_target);
    } else {
        printf("Key %d was not found (as expected).\n", search_target);
    }

    freeTree(root);
    root = NULL;

    return EXIT_SUCCESS;
}
