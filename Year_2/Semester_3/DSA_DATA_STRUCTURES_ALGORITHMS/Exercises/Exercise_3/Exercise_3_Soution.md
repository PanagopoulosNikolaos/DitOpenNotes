## 1. Δυαδικό Δέντρο - Χαρακτηριστικά

Το **δυαδικό δέντρο** είναι μια δομή δεδομένων όπου κάθε κόμβος έχει το πολύ δύο παιδιά (αριστερό και δεξί).

### Κύρια Χαρακτηριστικά:

**Βαθμός κόμβου**: Ο αριθμός των παιδιών του. Σε δυαδικό δέντρο: 0, 1 ή 2.

**Ρίζα**: Ο κορυφαίος κόμβος χωρίς γονέα.

**Φύλλα**: Κόμβοι με βαθμό 0 (χωρίς παιδιά).

**Εσωτερικοί κόμβοι**: Κόμβοι με τουλάχιστον ένα παιδί.

**Ύψος**: Το μήκος του μεγαλύτερου μονοπατιού από τη ρίζα σε φύλλο. Για δέντρο με έναν κόμβο το ύψος είναι 0.

**Βάθος κόμβου**: Το μήκος του μονοπατιού από τη ρίζα σε αυτόν τον κόμβο.

**Επίπεδο**: Όλοι οι κόμβοι στο ίδιο βάθος ανήκουν στο ίδιο επίπεδο. Η ρίζα είναι στο επίπεδο 0.



## 2. Δυαδικό Δέντρο Αναζήτησης (BST)

Το **Binary Search Tree (BST)** είναι ένα δυαδικό δέντρο με μια ειδική ιδιότητα:

**Βασική Ιδιότητα BST:**
- Όλες οι τιμές στο αριστερό υποδέντρο είναι **μικρότερες** από την τιμή του κόμβου
- Όλες οι τιμές στο δεξί υποδέντρο είναι **μεγαλύτερες** από την τιμή του κόμβου
- Κάθε υποδέντρο είναι επίσης BST

**Πώς βοηθά στην αποδοτική αναζήτηση:**
Η ιδιότητα αυτή επιτρέπει την εφαρμογή δυαδικής αναζήτησης. Σε κάθε βήμα, μπορούμε να αποκλείσουμε το μισό δέντρο, καταλήγοντας σε **O(log n)** πολυπλοκότητα για ισορροπημένο BST (αντί για O(n) σε μη ταξινομημένη δομή).


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


## 3. Διασχίσεις Δέντρων

### **Pre-order:** Ρίζα → Αριστερά → Δεξιά
- Επισκεπτόμαστε πρώτα τον κόμβο, μετά το αριστερό και δεξί υποδέντρο
- Χρήση: Αντιγραφή δέντρου, prefix expressions

### **In-order:** Αριστερά → Ρίζα → Δεξιά
- Επισκεπτόμαστε πρώτα το αριστερό υποδέντρο, μετά τον κόμβο, μετά το δεξί
- **Παράγει ταξινομημένη έξοδο για BST!** γιατί η ιδιότητα του BST (αριστερά < ρίζα < δεξιά) εγγυάται αύξουσα σειρά

### **Post-order:** Αριστερά → Δεξιά → Ρίζα
- Επισκεπτόμαστε τα υποδέντρα πρώτα, μετά τον κόμβο
- Χρήση: Διαγραφή δέντρου, postfix expressions


## 4. Ισοζυγισμένα Δέντρα

Ένα δέντρο θεωρείται **ισοζυγισμένο** όταν για κάθε κόμβο, το ύψος του αριστερού και δεξιού υποδέντρου διαφέρει το πολύ κατά 1.

**Επίδραση της ισορροπίας στην απόδοση:**

| Πράξη | Μη Ισορροπημένο BST | Ισορροπημένο BST |
|---|---|---|
| Αναζήτηση | O(n) (χειρότερη) | O(log n) |
| Εισαγωγή | O(n) (χειρότερη) | O(log n) |
| Διαγραφή | O(n) (χειρότερη) | O(log n) |


## 5. AVL Δέντρα

Είναι δυαδικό δέντρο αναζήτησης που διατηρεί αυτόματα ισορροπία. Κάθε κόμβος έχει συντελεστή ισορροπίας που υπολογίζεται ως:

$$BF = \text{ύψος αριστερού υποδέντρου} - \text{ύψος δεξιού υποδέντρου}$$

Για να είναι έγκυρο AVL δέντρο: $BF \in \{-1, 0, 1\}$ για κάθε κόμβο.

### Τέσσερις Βασικές Περιστροφές

**1. LL (Left-Left) - Δεξιά Περιστροφή**
- Πρόβλημα: BF = 2, αριστερό παιδί έχει BF ≥ 0
- Λύση: Μία δεξιά περιστροφή στον ανισορροπημένο κόμβο

**2. RR (Right-Right) - Αριστερή Περιστροφή**
- Πρόβλημα: BF = -2, δεξί παιδί έχει BF ≤ 0
- Λύση: Μία αριστερή περιστροφή στον ανισορροπημένο κόμβο

**3. LR (Left-Right) - Διπλή Περιστροφή**
- Πρόβλημα: BF = 2, αριστερό παιδί έχει BF < 0
- Λύση: Αριστερή περιστροφή στο αριστερό παιδί, μετά δεξιά στη ρίζα

**4. RL (Right-Left) - Διπλή Περιστροφή**
- Πρόβλημα: BF = -2, δεξί παιδί έχει BF > 0
- Λύση: Δεξιά περιστροφή στο δεξί παιδί, έπειτα αριστερή στη ρίζα

Οι περιστροφές εκτελούνται μετά από κάθε εισαγωγή/διαγραφή για να διατηρηθεί η συνθήκη $|BF| \leq 1$.