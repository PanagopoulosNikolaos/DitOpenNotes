# Παραδείγματα: Έξυπνοι Δείκτες (Smart Pointers) στη Σύγχρονη C++

## Επισκόπηση

Στη σύγχρονη C++ (C++11 και μεταγενέστερες), η χειροκίνητη διαχείριση δυναμικής μνήμης με `new` και `delete` αντικαθίσταται από τους **έξυπνους δείκτες (smart pointers)** της βιβλιοθήκης `<memory>`. Οι έξυπνοι δείκτες υλοποιούν το ιδίωμα **RAII (Resource Acquisition Is Initialization)**, εξασφαλίζοντας αυτόματη απελευθέρωση πόρων και αποτροπή διαρροών μνήμης (memory leaks).

---

## Παράδειγμα 1: `std::unique_ptr` και Μεταβίβαση Ιδιοκτησίας (Move Semantics)

### Περιγραφή
Ο `std::unique_ptr` διαχειρίζεται πόρους με αποκλειστική ιδιοκτησία (exclusive ownership). Δεν επιτρέπει αντιγραφή (`copy`), παρά μόνο μετακίνηση (`std::move`).

### Πλήρης Κώδικας C++

```cpp
#include <iostream>
#include <memory>
#include <string>

class DatabaseConnection {
private:
    std::string connection_string;

public:
    /**
     * Initializes database connection with connection string.
     * Args:
     * conn_str (const std::string&): Database target URI.
     */
    explicit DatabaseConnection(const std::string& conn_str)
        : connection_string(conn_str) {
        std::cout << "[DatabaseConnection] Συνδέθηκε: " << connection_string << "\n";
    }

    /**
     * Destructor closing database connection automatically.
     */
    ~DatabaseConnection() {
        std::cout << "[DatabaseConnection] Αποσυνδέθηκε: " << connection_string << "\n";
    }

    /**
     * Executes SQL query.
     * Args:
     * query (const std::string&): SQL command to execute.
     */
    void executeQuery(const std::string& query) const {
        std::cout << "[DatabaseConnection] Εκτέλεση ερωτήματος: " << query << "\n";
    }
};

void processConnection(std::unique_ptr<DatabaseConnection> conn) {
    if (conn) {
        conn->executeQuery("SELECT * FROM students WHERE semester = 3;");
    }
    // conn goes out of scope here and deletes the connection
}

int main() {
    // Δημιουργία με std::make_unique (προτεινόμενη μέθοδος)
    auto db = std::make_unique<DatabaseConnection>("tcp://localhost:5432/dit_db");

    db->executeQuery("SELECT NOW();");

    // Μεταβίβαση ιδιοκτησίας με std::move
    processConnection(std::move(db));

    if (db == nullptr) {
        std::cout << "[main] Το db είναι πλέον nullptr μετά το std::move.\n";
    }

    return 0;
}
```

---

## Παράδειγμα 2: `std::shared_ptr` και `std::weak_ptr` (Επίλυση Κυκλικών Αναφορών)

### Περιγραφή
Ο `std::shared_ptr` χρησιμοποιεί μέτρηση αναφορών (reference counting). Όταν δύο αντικείμενα έχουν αμοιβαίους `std::shared_ptr`, προκαλείται κυκλική εξάρτηση (circular dependency) και διαρροή μνήμης. Η λύση είναι η χρήση `std::weak_ptr` για τη μη-ιδιοκτησιακή παρατήρηση.

### Πλήρης Κώδικας C++

```cpp
#include <iostream>
#include <memory>
#include <string>
#include <vector>

class Node {
public:
    int value;
    std::shared_ptr<Node> next;
    std::weak_ptr<Node> prev; // weak_ptr αποτρέπει την κυκλική εξάρτηση

    /**
     * Initializes node with integer value.
     * Args:
     * val (int): Node value.
     */
    explicit Node(int val) : value(val) {
        std::cout << "[Node] Δημιουργία κόμβου: " << value << "\n";
    }

    ~Node() {
        std::cout << "[Node] Καταστροφή κόμβου: " << value << "\n";
    }
};

int main() {
    auto first = std::make_shared<Node>(10);
    auto second = std::make_shared<Node>(20);

    // Διασύνδεση κόμβων
    first->next = second;
    second->prev = first; // Δεν αυξάνει το reference count του first

    std::cout << "first use_count: " << first.use_count() << "\n";
    std::cout << "second use_count: " << second.use_count() << "\n";

    // Πρόσβαση στο prev μέσω του lock() του weak_ptr
    if (auto locked_prev = second->prev.lock()) {
        std::cout << "Προηγούμενος κόμβος: " << locked_prev->value << "\n";
    }

    return 0;
}
```

---

## Παράδειγμα 3: Προσαρμοσμένος Καταστροφέας (Custom Deleter)

### Περιγραφή
Ο `std::unique_ptr` μπορεί να διαχειριστεί πόρους που απαιτούν ειδικές συναρτήσεις απελευθέρωσης, όπως δείκτες αρχείων C (`FILE*`).

### Πλήρης Κώδικας C++

```cpp
#include <iostream>
#include <memory>
#include <cstdio>

struct FileCloser {
    /**
     * Custom deleter function object for C file pointers.
     * Args:
     * fp (FILE*): File pointer to close.
     */
    void operator()(FILE* fp) const {
        if (fp != nullptr) {
            std::fclose(fp);
            std::cout << "[FileCloser] Το αρχείο έκλεισε με ασφάλεια.\n";
        }
    }
};

int main() {
    using UniqueFile = std::unique_ptr<FILE, FileCloser>;

    UniqueFile file(std::fopen("temp_log.txt", "w"), FileCloser{});

    if (file) {
        std::fputs("DIT Open Notes Modern C++\n", file.get());
        std::cout << "[main] Εγγεγραμμένα δεδομένα στο αρχείο.\n";
    }

    // Το αρχείο κλείνει αυτόματα με την FileCloser όταν το file βγει από το scope
    return 0;
}
```

