# Εξαμηνιαίο Project 1: Αντικειμενοστραφές Τραπεζικό Σύστημα σε Σύγχρονη C++

## 1. Στόχος του Project
Σχεδιασμός και ανάπτυξη μιας πλήρους κλίμακας αντικειμενοστραφούς εφαρμογής διαχείρισης τραπεζικών συναλλαγών (Banking Management System) σε C++17/C++20, με αυστηρή εφαρμογή των αρχών SOLID, πολυμορφισμού, έξυπνων δεικτών και σχεδιαστικών προτύπων.

---

## 2. Αρχιτεκτονική Κλάσεων & Διεπαφών

### 2.1 Ιεραρχία Λογαριασμών (`Account`)
- Αφηρημένη βασική κλάση `Account` με πεδία: `account_number`, `owner_info`, `balance`, `creation_date`.
- Καθαρά εικονικές μέθοδοι:
  - `virtual bool withdraw(double amount) = 0;`
  - `virtual void deposit(double amount) = 0;`
  - `virtual void applyMonthlyInterestOrFees() = 0;`
  - `virtual void printStatement() const = 0;`
- Παράγωγες κλάσεις:
  - `SavingsAccount`: Επιτόκιο ταμιευτηρίου και ελάχιστο υπόλοιπο.
  - `CheckingAccount`: Όριο υπερανάληψης (overdraft limit) και χρέωση ανά συναλλαγή.
  - `InvestmentAccount`: Χαρτοφυλάκιο επενδυτικών τίτλων με ημερήσια διακύμανση απόδοσης.

### 2.2 Διαχείριση Συναλλαγών & Σχεδιαστικά Πρότυπα
- **Command Pattern:** Κάθε συναλλαγή (`DepositCommand`, `WithdrawCommand`, `TransferCommand`) αποτελεί αντικείμενο με δυνατότητα `execute()` και `undo()`.
- **Factory Pattern:** `AccountFactory` για δυναμική δημιουργία λογαριασμών βάσει τύπου.
- **Observer Pattern:** Ειδοποίηση συνδρομητών (SMS/Email notification system) σε αναλήψεις μεγάλων ποσών ή αρνητικό υπόλοιπο.

---

## 3. Τεχνικές Απαιτήσεις
- **Smart Pointers:** Αποκλειστική χρήση `std::unique_ptr` και `std::shared_ptr` (μηδενική χρήση ωμών δεικτών `new`/`delete`).
- **Εξαιρέσεις (Exceptions):** Προσαρμοσμένες κλάσεις εξαιρέσεων (`InsufficientFundsException`, `AccountNotFoundException`, `InvalidAmountException`) που κληρονομούν από `std::exception`.
- **Μόνιμη Αποθήκευση (Persistence):** Εγγραφή και ανάγνωση καταστάσεων σε αρχεία JSON ή CSV με χρήση streams (`std::ifstream`, `std::ofstream`).

---

## 4. Παραδοτέα
- Πλήρως μεταγλωττίσιμο project με `CMakeLists.txt`.
- Unit tests με GoogleTest ή Catch2 που καλύπτουν όλες τις συναλλαγές και εξαιρέσεις.
- Διάγραμμα κλάσεων UML (Class Diagram) σε PlantUML ή Mermaid.
- Τελική τεχνική αναφορά 5-10 σελίδων.

