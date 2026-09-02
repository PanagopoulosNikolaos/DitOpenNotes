# Εργαστηριακός Οδηγός 1: Υλοποίηση Αυτο-εξισορροπούμενου Δέντρου AVL σε C++

## 1. Σκοπός Εργαστηρίου
Σκοπός είναι η πρακτική κατανόηση της δομής του δέντρου AVL, ο υπολογισμός των υψών των υποδέντρων, ο έλεγχος του συντελεστή ισοζυγίου (Balance Factor) και η εκτέλεση μονών και διπλών περιστροφών (Right & Left Rotations) σε C++.

---

## 2. Πλήρης Υλοποίηση AVL Tree σε C++

```cpp
#include <iostream>
#include <algorithm>

struct AVLNode {
    int key;
    int height;
    AVLNode* left;
    AVLNode* right;

    AVLNode(int val) : key(val), height(1), left(nullptr), right(nullptr) {}
};

class AVLTree {
private:
    AVLNode* root;

    int getHeight(AVLNode* node) {
        return node ? node->height : 0;
    }

    int getBalanceFactor(AVLNode* node) {
        return node ? getHeight(node->left) - getHeight(node->right) : 0;
    }

    void updateHeight(AVLNode* node) {
        if (node) {
            node->height = 1 + std::max(getHeight(node->left), getHeight(node->right));
        }
    }

    // Δεξιά Περιστροφή (Right Rotation για περίπτωση Left-Left)
    AVLNode* rotateRight(AVLNode* y) {
        AVLNode* x = y->left;
        AVLNode* T2 = x->right;

        // Εκτέλεση περιστροφής
        x->right = y;
        y->left = T2;

        // Ενημέρωση υψών
        updateHeight(y);
        updateHeight(x);

        return x; // Νέα ρίζα
    }

    // Αριστερή Περιστροφή (Left Rotation για περίπτωση Right-Right)
    AVLNode* rotateLeft(AVLNode* x) {
        AVLNode* y = x->right;
        AVLNode* T2 = y->left;

        // Εκτέλεση περιστροφής
        y->left = x;
        x->right = T2;

        // Ενημέρωση υψών
        updateHeight(x);
        updateHeight(y);

        return y; // Νέα ρίζα
    }

    AVLNode* insert(AVLNode* node, int key) {
        if (!node) return new AVLNode(key);

        if (key < node->key) {
            node->left = insert(node->left, key);
        } else if (key > node->key) {
            node->right = insert(node->right, key);
        } else {
            return node; // Ίδια κλειδιά δεν επιτρέπονται
        }

        updateHeight(node);
        int balance = getBalanceFactor(node);

        // Case 1: Left Left
        if (balance > 1 && key < node->left->key) {
            return rotateRight(node);
        }

        // Case 2: Right Right
        if (balance < -1 && key > node->right->key) {
            return rotateLeft(node);
        }

        // Case 3: Left Right
        if (balance > 1 && key > node->left->key) {
            node->left = rotateLeft(node->left);
            return rotateRight(node);
        }

        // Case 4: Right Left
        if (balance < -1 && key < node->right->key) {
            node->right = rotateRight(node->right);
            return rotateLeft(node);
        }

        return node;
    }

    void inOrder(AVLNode* node) {
        if (!node) return;
        inOrder(node->left);
        std::cout << node->key << " (h=" << node->height << ") ";
        inOrder(node->right);
    }

public:
    AVLTree() : root(nullptr) {}

    void insert(int key) {
        root = insert(root, key);
    }

    void printInOrder() {
        inOrder(root);
        std::cout << "\n";
    }
};

int main() {
    AVLTree tree;
    int elements[] = {10, 20, 30, 40, 50, 25};
    
    for (int elem : elements) {
        std::cout << "Eisagogi: " << elem << "\n";
        tree.insert(elem);
    }

    std::cout << "Endodiataktiki Diasxisi (In-order): ";
    tree.printInOrder();

    return 0;
}
```

---

## 3. Οδηγίες Μεταγλώττισης και Εκτέλεσης
Εκτελέστε στο τερματικό:
```bash
g++ -std=c++17 -Wall -O2 avl_tree.cpp -o avl_tree
./avl_tree
```
Παρατηρήστε ότι τα στοιχεία εκτυπώνονται πλήρως ταξινομημένα με ισοζυγισμένα ύψη $O(\log n)$.

