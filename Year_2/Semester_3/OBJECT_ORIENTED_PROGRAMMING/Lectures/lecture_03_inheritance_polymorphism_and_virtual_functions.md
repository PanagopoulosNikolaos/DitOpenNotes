# Διάλεξη 3: Κληρονομικότητα, Πολυμορφισμός και Εικονικές Συναρτήσεις (Virtual Functions)

## 1. Κληρονομικότητα (Inheritance)
Η κληρονομικότητα επιτρέπει τη δημιουργία ιεραρχιών κλάσεων εκφράζοντας τη σχέση "είναι-ένα" (IS-A relationship).

### 1.1 Μορφές Κληρονομικότητας σε C++
- `class Derived : public Base` — Τα `public` μέλη της Base παραμένουν `public`, τα `protected` παραμένουν `protected`.
- `class Derived : protected Base` — Τα `public` και `protected` γίνονται `protected`.
- `class Derived : private Base` — Όλα γίνονται `private` (εκφράζει σχέση υλοποίησης "has-a").

---

## 2. Στατικός vs. Δυναμικός Πολυμορφισμός
- **Στατικός Πολυμορφισμός (Compile-Time):**
  - Υπερφόρτωση συναρτήσεων (Function Overloading).
  - Υπερφόρτωση τελεστών (Operator Overloading).
  - Πρότυπα (Templates / Generic Programming).
- **Δυναμικός Πολυμορφισμός (Runtime):**
  - Εικονικές συναρτήσεις (`virtual functions`).
  - Υπέρβαση μεθόδων (Method Overriding) μέσω δεικτών ή αναφορών βασικής κλάσης (`Base*` ή `Base&`).

---

## 3. Εικονικές Συναρτήσεις και Virtual Table (vtable)
Όταν μια μέθοδος δηλώνεται ως `virtual`, η επιλογή της πραγματικής μεθόδου προς εκτέλεση αναβάλλεται για τον χρόνο εκτέλεσης (Dynamic Binding / Late Binding).

### 3.1 Μηχανισμός vtable και vptr
- Ο compiler δημιουργεί έναν πίνακα δεικτών συναρτήσεων (`vtable`) για κάθε κλάση με virtual συναρτήσεις.
- Κάθε αντικείμενο περιέχει έναν κρυφό δείκτη (`vptr`) που δείχνει στον αντίστοιχο `vtable`.
- Κατά την κλήση `base_ptr->draw()`, ο κώδικας ακολουθεί το `vptr` και ανακαλεί τη σωστή μέθοδο.

### 3.2 Αφηρημένες Κλάσεις και Pure Virtual Functions
Μια μέθοδος δηλώνεται ως αμιγώς εικονική (pure virtual) με τη σύνταξη `= 0`:
```cpp
class Shape {
public:
    virtual ~Shape() = default; // Πάντα Virtual Destructor στη βασική κλάση!
    virtual double area() const = 0; // Pure virtual function
    virtual void draw() const = 0;
};
```
Μια κλάση με τουλάχιστον μία pure virtual συνάρτηση είναι **Αφηρημένη Κλάση (Abstract Class)** και δεν μπορεί να δημιουργήσει αντικείμενα (instances).

---

## 4. Παράδειγμα Πολυμορφισμού
```cpp
#include <iostream>
#include <vector>
#include <memory>

class Shape {
public:
    virtual ~Shape() = default;
    virtual double area() const = 0;
};

class Circle : public Shape {
private:
    double radius;
public:
    Circle(double r) : radius(r) {}
    double area() const override {
        return 3.14159265359 * radius * radius;
    }
};

class Rectangle : public Shape {
private:
    double width, height;
public:
    Rectangle(double w, double h) : width(w), height(h) {}
    double area() const override {
        return width * height;
    }
};

int main() {
    std::vector<std::unique_ptr<Shape>> shapes;
    shapes.push_back(std::make_unique<Circle>(5.0));
    shapes.push_back(std::make_unique<Rectangle>(4.0, 6.0));

    for (const auto& shape : shapes) {
        std::cout << "Emvadon: " << shape->area() << "\n";
    }

    return 0;
}
```

