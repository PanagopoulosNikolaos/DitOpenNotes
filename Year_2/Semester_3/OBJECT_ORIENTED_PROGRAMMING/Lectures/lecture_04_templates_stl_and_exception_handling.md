# Διάλεξη 4: Πρότυπα (Templates), STL και Διαχείριση Εξαιρέσεων

## 1. Γενικός Προγραμματισμός και Πρότυπα (Templates)
Τα πρότυπα (Templates) επιτρέπουν τη συγγραφή γενικού κώδικα ανεξάρτητου από συγκεκριμένους τύπους δεδομένων (Compile-time Type Genericity).

### 1.1 Πρότυπα Συναρτήσεων (Function Templates)
```cpp
template <typename T>
T findMax(const T& a, const T& b) {
    return (a > b) ? a : b;
}
```

### 1.2 Πρότυπα Κλάσεων (Class Templates)
```cpp
template <typename T, size_t Capacity>
class FixedStack {
private:
    T data[Capacity];
    size_t top_index = 0;

public:
    void push(const T& elem) {
        if (top_index < Capacity) {
            data[top_index++] = elem;
        }
    }

    T pop() {
        if (top_index > 0) {
            return data[--top_index];
        }
        throw std::underflow_error("Stack is empty");
    }
};
```

---

## 2. Βασική Βιβλιοθήκη Προτύπων (Standard Template Library - STL)
Η STL χωρίζεται σε 3 βασικά μέρη:
1. **Περιέκτες (Containers):**
   - *Ακολουθιακοί (Sequence):* `std::vector`, `std::deque`, `std::list`, `std::array`.
   - *Συσχετιστικοί (Associative):* `std::set`, `std::map`, `std::multiset`, `std::multimap` (υλοποιημένοι με Red-Black Trees).
   - *Μη διατεταγμένοι (Unordered):* `std::unordered_map`, `std::unordered_set` (Hash Tables).
   - *Προσαρμογείς (Adapters):* `std::stack`, `std::queue`, `std::priority_queue`.
2. **Επαναλήπτες (Iterators):** Γέφυρα επικοινωνίας μεταξύ containers και αλγορίθμων (`begin()`, `end()`, `rbegin()`).
3. **Αλγόριθμοι (Algorithms):** `std::sort`, `std::find`, `std::binary_search`, `std::for_each`, `std::accumulate`.

---

## 3. Διαχείριση Εξαιρέσεων (Exception Handling)
Χρήση των λέξεων-κλειδιών `try`, `throw`, `catch` για ασφαλή χειρισμό σφαλμάτων εκτέλεσης.

```cpp
#include <iostream>
#include <stdexcept>

double safeDivide(double a, double b) {
    if (b == 0.0) {
        throw std::invalid_argument("Diairesh me to miden den epitrepetai");
    }
    return a / b;
}

int main() {
    try {
        double result = safeDivide(10.0, 0.0);
        std::cout << "Apotelesma: " << result << "\n";
    } catch (const std::invalid_argument& e) {
        std::cerr << "Sfalma: " << e.what() << "\n";
    } catch (const std::exception& e) {
        std::cerr << "Geniko Sfalma: " << e.what() << "\n";
    }
    return 0;
}
```

---

## 4. Έξυπνοι Δείκτες (Smart Pointers - RAII)
- `std::unique_ptr<T>`: Μοναδική ιδιοκτησία (Exclusive ownership), μηδενικό overhead.
- `std::shared_ptr<T>`: Συνιδιοκτησία με καταμέτρηση αναφορών (Reference counting).
- `std::weak_ptr<T>`: Μη-ιδιοκτησιακή παρατήρηση (αποτρέπει κυκλικές αναφορές - Circular references).

