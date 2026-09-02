# Πρότυπο Διαγώνισμα Εξάσκησης: Αντικειμενοστραφής Προγραμματισμός (C++)

## Θέμα 1: Ενθυλάκωση και Διαχείριση Πόρων (Rule of 5) (2.5 Μονάδες)
1. **(1.5 Μονάδες)** Γράψτε μια κλάση `StringWrapper` σε C++ που διαχειρίζεται δυναμικά δεσμευμένο πίνακα χαρακτήρων (`char* data`). Υλοποιήστε πλήρως: Constructor, Destructor, Deep Copy Constructor, Copy Assignment Operator, Move Constructor και Move Assignment Operator.
2. **(1.0 Μονάδα)** Εξηγήστε γιατί η ανάθεση `a = a;` (self-assignment) μπορεί να αποβεί καταστροφική χωρίς κατάλληλο έλεγχο στον Copy Assignment Operator.

---

## Θέμα 2: Κληρονομικότητα και Πολυμορφισμός (2.5 Μονάδες)
1. **(1.5 Μονάδες)** Δίνεται η βασική κλάση `MediaFile` και δύο παράγωγες `AudioFile` και `VideoFile`. Υλοποιήστε πολυμορφική αναπαραγωγή μέσω της μεθόδου `virtual void play() const = 0;`.
2. **(1.0 Μονάδα)** Εξηγήστε τον ρόλο του πίνακα εικονικών μεθόδων (`vtable`) και του δείκτη `vptr`. Τι επιβάρυνση σε χρόνο και μνήμη επιφέρει η χρήση τους;

---

## Θέμα 3: Πρότυπα (Templates) και STL (2.5 Μονάδες)
1. **(1.5 Μονάδες)** Υλοποιήστε μια template συνάρτηση `countOccurrences(const std::vector<T>& vec, const T& target)` που μετρά πόσες φορές εμφανίζεται το στοιχείο `target` στο διάνυσμα.
2. **(1.0 Μονάδα)** Ποιες είναι οι βασικές διαφορές μεταξύ `std::map` και `std::unordered_map` ως προς την πολυπλοκότητα αναζήτησης και την εσωτερική δομή δεδομένων;

---

## Θέμα 4: Σχεδιαστικά Πρότυπα και Εξαιρέσεις (2.5 Μονάδες)
1. **(1.5 Μονάδες)** Υλοποιήστε το σχεδιαστικό πρότυπο Observer (Παρατηρητής) σε C++ για ένα σύστημα ειδοποιήσεων μετεωρολογικού σταθμού (`WeatherStation` και `DisplayDevice`).
2. **(1.0 Μονάδα)** Γιατί δεν πρέπει ποτέ ένας destructor σε C++ να επιτρέπει σε μια εξαίρεση (exception) να διαφύγει εκτός του σώματός του (`noexcept by default`);

---

## Ενδεικτικές Απαντήσεις & Λύσεις

### Λύση Θέματος 1:
```cpp
#include <iostream>
#include <cstring>

class StringWrapper {
private:
    char* data;
    size_t length;
public:
    StringWrapper(const char* str = "") : length(strlen(str)), data(new char[length + 1]) {
        strcpy(data, str);
    }
    ~StringWrapper() {
        delete[] data;
    }
    StringWrapper(const StringWrapper& other) : length(other.length), data(new char[length + 1]) {
        strcpy(data, other.data);
    }
    StringWrapper& operator=(const StringWrapper& other) {
        if (this != &other) {
            delete[] data;
            length = other.length;
            data = new char[length + 1];
            strcpy(data, other.data);
        }
        return *this;
    }
    StringWrapper(StringWrapper&& other) noexcept : data(other.data), length(other.length) {
        other.data = nullptr;
        other.length = 0;
    }
    StringWrapper& operator=(StringWrapper&& other) noexcept {
        if (this != &other) {
            delete[] data;
            data = other.data;
            length = other.length;
            other.data = nullptr;
            other.size = 0;
        }
        return *this;
    }
};
```
Στην αυτο-ανάθεση `a = a`, χωρίς τον έλεγχο `if (this != &other)`, η εντολή `delete[] data` θα διέγραφε τα δεδομένα του ίδιου του αντικειμένου πριν προλάβει να τα αντιγράψει, οδηγώντας σε Dangling Pointer και ανάγνωση αποδεσμευμένης μνήμης.

### Λύση Θέματος 2:
1. Πολυμορφική ιεραρχία με pure virtual μέθοδο `virtual void play() const = 0` και virtual destructor.
2. Ο `vtable` είναι στατικός πίνακας δεικτών μεθόδων ανά κλάση. Κάθε αντικείμενο επιβαρύνεται με το μέγεθος ενός δείκτη (`vptr`, συνήθως 8 bytes σε 64-bit συστήματα). Κατά την κλήση virtual μεθόδου υπάρχει ελάχιστη καθυστέρηση μίας έμμεσης προσπέλασης δείκτη (pointer indirection).

### Λύση Θέματος 3:
1. Template συνάρτηση:
   ```cpp
   template <typename T>
   size_t countOccurrences(const std::vector<T>& vec, const T& target) {
       size_t count = 0;
       for (const auto& item : vec) {
           if (item == target) ++count;
       }
       return count;
   }
   ```
2. `std::map`: Υλοποιημένο με Red-Black Tree, διατηρεί ταξινόμηση κλειδιών, αναζήτηση $O(\log n)$. `std::unordered_map`: Υλοποιημένο με Hash Table, μη διατεταγμένο, αναζήτηση μέσης περίπτωσης $O(1)$ ($O(n)$ worst-case).

### Λύση Θέματος 4:
1. Υλοποίηση Observer Pattern με `IObserver` διεπαφή και λίστα παρατηρητών `std::vector<std::shared_ptr<IObserver>>`.
2. Εάν ένας destructor πετάξει εξαίρεση κατά τη διαδικασία εκτύλιξης στοίβας (stack unwinding) που προκλήθηκε από άλλη εξαίρεση, το runtime της C++ καλεί άμεσα τη συνάρτηση `std::terminate()`, τερματίζοντας βίαια την εφαρμογή.

