# Εργαστηριακός Οδηγός 1: Διαχείριση Πόρων με RAII και Smart Pointers στη Σύγχρονη C++

## 1. Σκοπός Εργαστηρίου
Σκοπός είναι η εφαρμογή του ιδιώματος RAII (Resource Acquisition Is Initialization), η αντικατάσταση των ωμών δεικτών (`raw pointers`) από έξυπνους δείκτες (`std::unique_ptr`, `std::shared_ptr`) και η αποφυγή διαρροών μνήμης (memory leaks).

---

## 2. Εργαστηριακό Παράδειγμα: Διαχείριση Αρχείου και Μνήμης με RAII

```cpp
#include <iostream>
#include <memory>
#include <string>
#include <vector>

class DatabaseConnection {
private:
    std::string connection_id;

public:
    DatabaseConnection(const std::string& id) : connection_id(id) {
        std::cout << "[DB] Syndesh " << connection_id << " anoikse.\n";
    }

    ~DatabaseConnection() {
        std::cout << "[DB] Syndesh " << connection_id << " ekleise automata (Destructor).\n";
    }

    void executeQuery(const std::string& sql) const {
        std::cout << "[DB " << connection_id << "] Ektelesi query: " << sql << "\n";
    }
};

void demonstrateUniquePtr() {
    std::cout << "--- Dokimi std::unique_ptr ---\n";
    // Δημιουργία με std::make_unique (C++14)
    auto db = std::make_unique<DatabaseConnection>("MySQL_Main");
    db->executeQuery("SELECT * FROM users;");
    
    // Μεταβίβαση ιδιοκτησίας με std::move
    std::unique_ptr<DatabaseConnection> db_moved = std::move(db);
    if (!db) {
        std::cout << "O arxikos deiktis einai pleon nullptr meta to std::move.\n";
    }
    db_moved->executeQuery("SELECT * FROM orders;");
} // Αυτόματη απελευθέρωση πόρου εδώ

void demonstrateSharedPtr() {
    std::cout << "\n--- Dokimi std::shared_ptr ---\n";
    std::shared_ptr<DatabaseConnection> p1 = std::make_shared<DatabaseConnection>("PostgreSQL_Analytics");
    std::cout << "Reference count (p1): " << p1.use_count() << "\n";

    {
        std::shared_ptr<DatabaseConnection> p2 = p1; // Συνιδιοκτησία
        std::cout << "Reference count (p1 & p2 mesa sto block): " << p1.use_count() << "\n";
        p2->executeQuery("COUNT(*) logs;");
    } // Το p2 καταστρέφεται, αλλά ο πόρος παραμένει

    std::cout << "Reference count meta to esoteriko block: " << p1.use_count() << "\n";
} // Το p1 καταστρέφεται, ref_count = 0, ο πόρος αποδεσμεύεται

int main() {
    demonstrateUniquePtr();
    demonstrateSharedPtr();
    return 0;
}
```

---

## 3. Μεταγλώττιση και Εκτέλεση
```bash
g++ -std=c++17 -Wall -Wextra raii_smart_pointers.cpp -o raii_test
./raii_test
```

