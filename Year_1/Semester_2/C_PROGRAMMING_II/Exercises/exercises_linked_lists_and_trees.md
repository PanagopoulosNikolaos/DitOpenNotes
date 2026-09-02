# Ασκήσεις Εμπέδωσης: Συνδεδεμένες Λίστες και Δυαδικά Δέντρα Αναζήτησης

## Άσκηση 1: Απλά Συνδεδεμένη Λίστα — Εισαγωγή και Διαγραφή

### Εκφώνηση
Υλοποιήστε συναρτήσεις για μια απλά συνδεδεμένη λίστα ακεραίων:
1. `void insertSorted(Node **head, int value)`: Εισαγωγή στοιχείου με διατήρηση αύξουσας ταξινόμησης.
2. `int deleteValue(Node **head, int value)`: Διαγραφή του πρώτου κόμβου με τη δοθείσα τιμή.
3. `void freeList(Node **head)`: Πλήρης αποδέσμευση της λίστας.

### Λύση

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node *next;
} Node;

/**
 * Inserts a value maintaining sorted ascending order.
 */
void insertSorted(Node **head, int value) {
    Node *newNode = (Node *)malloc(sizeof(Node));
    if (!newNode) return;
    newNode->data = value;
    newNode->next = NULL;

    if (*head == NULL || (*head)->data >= value) {
        newNode->next = *head;
        *head = newNode;
        return;
    }

    Node *current = *head;
    while (current->next != NULL && current->next->data < value) {
        current = current->next;
    }
    newNode->next = current->next;
    current->next = newNode;
}

/**
 * Deletes the first node containing the specified value.
 */
int deleteValue(Node **head, int value) {
    if (*head == NULL) return 0;

    Node *current = *head;
    Node *prev = NULL;

    if (current->data == value) {
        *head = current->next;
        free(current);
        return 1;
    }

    while (current != NULL && current->data != value) {
        prev = current;
        current = current->next;
    }

    if (current == NULL) return 0;

    prev->next = current->next;
    free(current);
    return 1;
}

/**
 * Frees all nodes in the linked list.
 */
void freeList(Node **head) {
    Node *current = *head;
    while (current != NULL) {
        Node *next = current->next;
        free(current);
        current = next;
    }
    *head = NULL;
}
```

---

## Άσκηση 2: Δυαδικό Δέντρο Αναζήτησης (BST) — Ενδοδιατεταγμένη Διάσχιση (In-order)

### Εκφώνηση
Υλοποιήστε αναδρομική εισαγωγή κόμβου και ενδοδιατεταγμένη διάσχιση (in-order traversal) που εκτυπώνει τα στοιχεία του BST σε ταξινομημένη σειρά.

### Λύση

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
} TreeNode;

/**
 * Inserts a node into BST.
 */
TreeNode *insertBST(TreeNode *root, int val) {
    if (root == NULL) {
        TreeNode *node = (TreeNode *)malloc(sizeof(TreeNode));
        if (!node) return NULL;
        node->val = val;
        node->left = node->right = NULL;
        return node;
    }
    if (val < root->val) {
        root->left = insertBST(root->left, val);
    } else if (val > root->val) {
        root->right = insertBST(root->right, val);
    }
    return root;
}

/**
 * Performs in-order traversal (Left, Root, Right).
 */
void inOrderTraversal(const TreeNode *root) {
    if (root == NULL) return;
    inOrderTraversal(root->left);
    printf("%d ", root->val);
    inOrderTraversal(root->right);
}
```

