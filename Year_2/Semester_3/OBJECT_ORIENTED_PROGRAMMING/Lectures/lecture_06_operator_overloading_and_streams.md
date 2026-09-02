# Διάλεξη 06: Υπερφόρτωση Τελεστών και Ροές Εισόδου/Εξόδου στη C++

## 1. Βασικές Αρχές Υπερφόρτωσης Τελεστών (Operator Overloading)
Η υπερφόρτωση τελεστών επιτρέπει στα αντικείμενα προσαρμοσμένων κλάσεων να χρησιμοποιούνται με τη φυσική σύνταξη των ενσωματωμένων τύπων δεδομένων.

- **Κανόνες Υπερφόρτωσης:**
  - Δεν μπορούν να δημιουργηθούν νέοι τελεστές (μόνο οι υπάρχοντες της C++).
  - Δεν μπορεί να αλλάξει η προτεραιότητα (precedence) και η προσεταιριστικότητα (associativity) των τελεστών.
  - Τελεστές που **δεν** υπερφορτώνονται: `.` (τελεία), `.*`, `::` (εμβέλεια), `?:` (τριαδικός), `sizeof`, `typeid`.

---

## 2. Μέθοδος-Μέλος vs. Ελεύθερη Συνάρτηση (Member vs Non-Member)
- **Ως Μέθοδος-Μέλος (Member Function):**
  Ο αριστερός τελεστέος είναι αυστηρά το αντικείμενο `*this`.
  ```cpp
  Complex Complex::operator+(const Complex& other) const;
  ```
- **Ως Ελεύθερη Συνάρτηση (Non-Member / Friend Function):**
  Απαραίτητο όταν ο αριστερός τελεστέος είναι διαφορετικού τύπου (π.χ. `2.5 + c` όπου `c` είναι `Complex`).
  ```cpp
  Complex operator+(double scalar, const Complex& c);
  ```

---

## 3. Υπερφόρτωση Τελεστών Ροής (`<<` και `>>`)
Οι τελεστές εισαγωγής (`<<`) και εξαγωγής (`>>`) ροών υλοποιούνται πάντα ως μη-μέλη (συνήθως `friend` functions), επειδή ο αριστερός τελεστέος είναι αναφορά σε ροή (`std::ostream&` ή `std::istream&`).

```cpp
#include <iostream>

class Complex {
private:
    double real;
    double imag;

public:
    Complex(double r = 0.0, double i = 0.0) : real(r), imag(i) {}

    friend std::ostream& operator<<(std::ostream& os, const Complex& c) {
        os << "(" << c.real << " + " << c.imag << "i)";
        return os; // Επιστροφή ροής για chaining (cout << a << b;)
    }

    friend std::istream& operator>>(std::istream& is, Complex& c) {
        is >> c.real >> c.imag;
        return is;
    }
};
```

---

## 4. Ειδικοί Τελεστές
- **Τελεστής Δεικτοδότησης (`operator[]`):**
  Υλοποιείται σε δύο εκδόσεις: μη-const για τροποποίηση και const για ανάγνωση:
  ```cpp
  T& operator[](size_t index);
  const T& operator[](size_t index) const;
  ```
- **Τελεστής Κλήσης Συνάρτησης (`operator()`):**
  Επιτρέπει σε ένα αντικείμενο να συμπεριφέρεται ως συνάρτηση (**Functor / Function Object**), χρήσιμο για παραμετροποίηση αλγορίθμων της STL (`std::sort`, `std::for_each`).

