# Διάλεξη 2: Κατασκευαστές, Καταστροφείς και Διαχείριση Μνήμης (Rule of Three / Five)

## 1. Κύκλος Ζωής Αντικειμένου (Object Lifecycle)
- **Κατασκευαστής (Constructor):** Καλείται αυτόματα κατά τη δημιουργία του αντικειμένου για την αρχικοποίηση των μελών του.
- **Καταστροφέας (Destructor):** Καλείται αυτόματα κατά την καταστροφή του αντικειμένου (π.χ. όταν βγει εκτός εμβέλειας scope ή με κλήση `delete`) για την απελευθέρωση πόρων (μνήμης heap, αρχείων, locks).

---

## 2. Είδη Κατασκευαστών
1. **Προεπιλεγμένος Κατασκευαστής (Default Constructor):** Δεν δέχεται ορίσματα (π.χ. `Point()`).
2. **Κατασκευαστής με Παραμέτρους (Parameterized Constructor):** Αρχικοποιεί με συγκεκριμένες τιμές.
3. **Κατασκευαστής Αντιγραφής (Copy Constructor):** Δημιουργεί νέο αντικείμενο ως πιστό αντίγραφο υπάρχοντος (`Point(const Point& other)`).
4. **Κατασκευαστής Μετακίνησης (Move Constructor - C++11):** Μεταφέρει τους πόρους από ένα προσωρινό αντικείμενο (rvalue reference) χωρίς βαθιά αντιγραφή (`Point(Point&& other) noexcept`).

---

## 3. Ρηχό vs. Βαθύ Αντίγραφο (Shallow vs. Deep Copy)
- **Shallow Copy (Ρηχό):** Αντιγράφει μόνο τις τιμές των δεικτών. Και τα δύο αντικείμενα δείχνουν στην ίδια περιοχή μνήμης heap $\rightarrow$ Κίνδυνος Double Free σφάλματος κατά την καταστροφή!
- **Deep Copy (Βαθύ):** Δεσμεύει νέα αυτόνομη μνήμη heap και αντιγράφει τα περιεχόμενα.

---

## 4. Ο Κανόνας των Τριών / Πέντε (Rule of Three / Rule of Five)
Εάν μια κλάση διαχειρίζεται απευθείας δυναμικούς πόρους (RAW pointers), πρέπει να ορίζει ρητά:
1. **Destructor (`~ClassName()`)**
2. **Copy Constructor (`ClassName(const ClassName&)`**)
3. **Copy Assignment Operator (`ClassName& operator=(const ClassName&)`**)
4. **Move Constructor (`ClassName(ClassName&&) noexcept` - C++11)**
5. **Move Assignment Operator (`ClassName& operator=(ClassName&&) noexcept` - C++11)**

### Παράδειγμα Υλοποίησης:
```cpp
class DynamicArray {
private:
    int* data;
    size_t size;

public:
    // Constructor
    DynamicArray(size_t n) : size(n), data(new int[n]()) {}

    // Destructor
    ~DynamicArray() {
        delete[] data;
    }

    // Copy Constructor (Deep Copy)
    DynamicArray(const DynamicArray& other) : size(other.size), data(new int[other.size]) {
        for (size_t i = 0; i < size; ++i) {
            data[i] = other.data[i];
        }
    }

    // Copy Assignment Operator (Copy-and-Swap Idiom)
    DynamicArray& operator=(const DynamicArray& other) {
        if (this != &other) {
            delete[] data;
            size = other.size;
            data = new int[size];
            for (size_t i = 0; i < size; ++i) {
                data[i] = other.data[i];
            }
        }
        return *this;
    }

    // Move Constructor
    DynamicArray(DynamicArray&& other) noexcept : data(other.data), size(other.size) {
        other.data = nullptr;
        other.size = 0;
    }

    // Move Assignment Operator
    DynamicArray& operator=(DynamicArray&& other) noexcept {
        if (this != &other) {
            delete[] data;
            data = other.data;
            size = other.size;
            other.data = nullptr;
            other.size = 0;
        }
        return *this;
    }
};
```

