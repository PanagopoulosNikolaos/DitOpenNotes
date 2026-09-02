# Διάλεξη 1: Κλάσεις, Αντικείμενα και Ενθυλάκωση (Encapsulation)

## 1. Θεμελιώδεις Αρχές Αντικειμενοστραφούς Προγραμματισμού (OOP)
Ο Αντικειμενοστραφής Προγραμματισμός βασίζεται σε τέσσερις βασικούς πυλώνες:
1. **Ενθυλάκωση (Encapsulation):** Συνδυασμός δεδομένων (πεδίων) και μεθόδων (συναρτήσεων) σε μία ενιαία οντότητα (κλάση) και απόκρυψη της εσωτερικής κατάστασης.
2. **Αφαίρεση (Abstraction):** Προβολή μόνο των απαραίτητων λειτουργιών προς τα έξω (interface), αποκρύπτοντας τις λεπτομέρειες υλοποίησης.
3. **Κληρονομικότητα (Inheritance):** Δυνατότητα μιας κλάσης (παράγωγη/παιδί) να κληρονομεί γνωρίσματα και συμπεριφορές από άλλη κλάση (βασική/γονέας).
4. **Πολυμορφισμός (Polymorphism):** Δυνατότητα διαφορετικών αντικειμένων να αποκρίνονται στο ίδιο μήνυμα/κλήση μεθόδου με διαφορετικό τρόπο.

---

## 2. Προσδιοριστές Πρόσβασης (Access Specifiers) σε C++
- **`private`:** Προσβάσιμα μόνο από μέλη της ίδιας της κλάσης και από συναρτήσεις-φίλους (`friend`). (Προεπιλογή σε C++ classes).
- **`public`:** Προσβάσιμα από οποιοδήποτε σημείο του προγράμματος.
- **`protected`:** Προσβάσιμα από μέλη της ίδιας της κλάσης και από παράγωγες κλάσεις (υποκλάσεις).

---

## 3. Δομή Κλάσης και Μέλη
```cpp
#include <iostream>
#include <string>

class BankAccount {
private:
    std::string account_holder;
    double balance;

public:
    // Κατασκευαστής (Constructor)
    BankAccount(const std::string& name, double initial_balance)
        : account_holder(name), balance(initial_balance) {
        if (balance < 0) {
            balance = 0;
        }
    }

    // Getters (const member functions)
    std::string getAccountHolder() const {
        return account_holder;
    }

    double getBalance() const {
        return balance;
    }

    // Μέθοδοι τροποποίησης (Setters / Mutators)
    void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
        }
    }

    bool withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            return true;
        }
        return false;
    }
};
```

---

## 4. `const` Member Functions και `this` Pointer
- **`const` μέθοδος:** Υπόσχεται στον compiler ότι δεν θα τροποποιήσει κανένα πεδίο του αντικειμένου (π.χ. `double getBalance() const`).
- **Δείκτης `this`:** Ένας σιωπηρός (implicit) δείκτης προς το αντικείμενο που κάλεσε τη μέθοδο (`this->balance`).

