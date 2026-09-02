# Εργαστηριακός Οδηγός 2: Υπερφόρτωση Τελεστών (Operator Overloading) και Copy Control

## 1. Σκοπός Εργαστηρίου
Σκοπός είναι η πλήρης υλοποίηση μιας μαθηματικής κλάσης Μιγαδικών Αριθμών (`ComplexNumber`) σε C++ με υπερφόρτωση αριθμητικών τελεστών (`+`, `-`, `*`), τελεστών ισότητας (`==`, `!=`) και τελεστών ροής εισόδου/εξόδου (`<<`, `>>`).

---

## 2. Πλήρης Υλοποίηση Κλάσης `ComplexNumber`

```cpp
#include <iostream>
#include <cmath>

class ComplexNumber {
private:
    double real;
    double imag;

public:
    // Constructors
    ComplexNumber(double r = 0.0, double i = 0.0) : real(r), imag(i) {}

    // Getters
    double getReal() const { return real; }
    double getImag() const { return imag; }

    // Μέτρο μιγαδικού (Magnitude)
    double magnitude() const {
        return std::sqrt(real * real + imag * imag);
    }

    // Υπερφόρτωση τελεστή πρόσθεσης (+)
    ComplexNumber operator+(const ComplexNumber& other) const {
        return ComplexNumber(real + other.real, imag + other.imag);
    }

    // Υπερφόρτωση τελεστή αφαίρεσης (-)
    ComplexNumber operator-(const ComplexNumber& other) const {
        return ComplexNumber(real - other.real, imag - other.imag);
    }

    // Υπερφόρτωση τελεστή πολλαπλασιασμού (*)
    ComplexNumber operator*(const ComplexNumber& other) const {
        return ComplexNumber(real * other.real - imag * other.imag,
                             real * other.imag + imag * other.real);
    }

    // Υπερφόρτωση τελεστή ισότητας (==)
    bool operator==(const ComplexNumber& other) const {
        return (real == other.real) && (imag == other.imag);
    }

    bool operator!=(const ComplexNumber& other) const {
        return !(*this == other);
    }

    // Υπερφόρτωση τελεστή εξόδου (<<) ως friend function
    friend std::ostream& operator<<(std::ostream& os, const ComplexNumber& c) {
        os << c.real;
        if (c.imag >= 0) {
            os << " + " << c.imag << "i";
        } else {
            os << " - " << -c.imag << "i";
        }
        return os;
    }

    // Υπερφόρτωση τελεστή εισόδου (>>) ως friend function
    friend std::istream& operator>>(std::istream& is, ComplexNumber& c) {
        std::cout << "Pragmatiko meros: ";
        is >> c.real;
        std::cout << "Fantastiko meros: ";
        is >> c.imag;
        return is;
    }
};

int main() {
    ComplexNumber c1(3.0, 4.0);
    ComplexNumber c2(1.5, -2.5);

    ComplexNumber sum = c1 + c2;
    ComplexNumber diff = c1 - c2;
    ComplexNumber prod = c1 * c2;

    std::cout << "c1 = " << c1 << " | Metro = " << c1.magnitude() << "\n";
    std::cout << "c2 = " << c2 << "\n";
    std::cout << "c1 + c2 = " << sum << "\n";
    std::cout << "c1 - c2 = " << diff << "\n";
    std::cout << "c1 * c2 = " << prod << "\n";

    return 0;
}
```

---

## 3. Εκτέλεση
```bash
g++ -std=c++17 complex_numbers.cpp -o complex_test
./complex_test
```

