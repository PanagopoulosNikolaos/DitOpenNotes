# Διάλεξη 05: Σημασιολογία Μετακίνησης (Move Semantics) και Έξυπνοι Δείκτες

## 1. lvalues, rvalues και Αναφορές Δεξιών Τιμών (rvalue References)
Στη σύγχρονη C++ (C++11 και νεότερη), οι εκφράσεις διακρίνονται σε:
- **lvalue (Locator Value):** Οντότητα με προσδιορίσιμη θέση στη μνήμη (διεύθυνση). Μπορεί να εμφανιστεί αριστερά από τελεστή ανάθεσης (π.χ. μεταβλητές, dereferenced δείκτες).
- **rvalue:** Προσωρινές τιμές χωρίς μόνιμη διεύθυνση στη μνήμη (π.χ. literals, αποτελέσματα αριθμητικών πράξεων ή προσωρινά αντικείμενα επιστροφής συναρτήσεων).
- **rvalue Reference (`T&&`):** Επιτρέπει τη δέσμευση προσωρινών αντικειμένων με σκοπό την «κλοπή» των πόρων τους αντί για δαπανηρή αντιγραφή.

---

## 2. Σημασιολογία Μετακίνησης (Move Semantics)
- **Κατασκευαστής Μετακίνησης (Move Constructor):**
  ```cpp
  MyString(MyString&& other) noexcept 
      : data(other.data), size(other.size) {
      other.data = nullptr;
      other.size = 0;
  }
  ```
- **Τελεστής Ανάθεσης Μετακίνησης (Move Assignment Operator):**
  ```cpp
  MyString& operator=(MyString&& other) noexcept {
      if (this != &other) {
          delete[] data;
          data = other.data;
          size = other.size;
          other.data = nullptr;
          other.size = 0;
      }
      return *this;
  }
  ```
- **`std::move`:** Μετατρέπει ρητά ένα lvalue σε rvalue reference (`static_cast<T&&>(val)`), δηλώνοντας ότι ο πόρος μπορεί να μεταφερθεί με ασφάλεια.

---

## 3. Ο Κανόνας των Πέντε (Rule of Five)
Εάν μια κλάση διαχειρίζεται απευθείας πόρους (π.χ. δυναμική μνήμη με `new`), πρέπει να ορίζει ρητά ή να διαγράφει (`= delete`) και τις 5 ειδικές συναρτήσεις μέλη:
1. Καταστροφέας (`~Class()`)
2. Κατασκευαστής Αντιγραφής (`Class(const Class&)`)
3. Τελεστής Ανάθεσης Αντιγραφής (`Class& operator=(const Class&)`)
4. Κατασκευαστής Μετακίνησης (`Class(Class&&) noexcept`)
5. Τελεστής Ανάθεσης Μετακίνησης (`Class& operator=(Class&&) noexcept`)

---

## 4. Έξυπνοι Δείκτες (Smart Pointers) και Ιδίωμα RAII
- **`std::unique_ptr<T>`:**
  - Αποκλειστική κυριότητα (non-copyable, movable).
  - Μηδενικό overhead σε σύγκριση με ωμό δείκτη.
  - Δημιουργία με `std::make_unique<T>()`.
- **`std::shared_ptr<T>`:**
  - Συνιδιοκτησία με μέτρηση αναφορών (Reference Counting).
  - Ο πόρος καταστρέφεται όταν το τελευταίο `shared_ptr` καταστραφεί.
  - Δημιουργία με `std::make_shared<T>()`.
- **`std::weak_ptr<T>`:**
  - Μη ιδιοκτησιακός παρατηρητής ενός `shared_ptr`.
  - Αποτρέπει κυκλικές εξαρτήσεις (cyclic references).
  - Έλεγχος εγκυρότητας και ασφαλής πρόσβαση μέσω της μεθόδου `lock()`.

