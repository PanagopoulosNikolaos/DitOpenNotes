# Εργαστηριακή Εργασία 4: Δομές Δεδομένων, Δυαδικά Αρχεία και Σειριοποίηση Εγγραφών

## 1. Σκοπός και Περιγραφή
Η εργασία πραγματεύεται τη δήλωση και χρήση δομών (`struct`), πινάκων δομών, περασμάτων σε συναρτήσεις με δείκτες (`->`), καθώς και τη σειριοποίηση/αποσειριοποίηση δομών σε δυαδικά αρχεία (`.dat`) με τυχαία προσπέλαση (`fseek`, `ftell`).

## 2. Ευρετήριο Υλοποιήσεων (`Structures/src/`)

### Μέρος Α: Θεμελιώδεις Έννοιες Δομών (Fundamental Structs)
- `exercise_01_fundamental.c`: Βασική δήλωση δομής `Student` και αρχικοποίηση πεδίων.
- `exercise_02_fundamental.c`: Πέρασμα δομής σε συνάρτηση κατ' αξία και κατ' αναφορά.
- `exercise_03_fundamental.c`: Πίνακας δομών για καταγραφή πολλαπλών φοιτητών.
- `exercise_04_fundamental.c`: Φώλιασμα δομών (Nested structures).
- `exercise_05_fundamental.c`: Δυναμική δέσμευση μνήμης για δομές με `malloc`.
- `exercise_06_fundamental.c`: Ταξινόμηση πίνακα δομών με βάση πεδίο βαθμολογίας.
- `exercise_07_fundamental.c`: Χρήση `typedef` και ορισμός γεωμετρικών σημείων (`Point`).
- `exercise_08_fundamental.c`: Υπολογισμός αποστάσεων μεταξύ σημείων.
- `exercise_09_fundamental.c`: Δομή `Date` και υπολογισμός ημερολογιακών διαφορών.
- `exercise_10_fundamental.c`: Διαχείριση αποθήκης προϊόντων με δομή `Inventory`.

### Μέρος Β: Δυαδικά Αρχεία και Εγγραφές (Binary File Handling)
- `init_items_dat.c`, `init_movies_dat.c`, `init_tasks_dat.c`: Βοηθητικά προγράμματα αρχικοποίησης δυαδικών βάσεων δεδομένων.
- `exercise_11_file_handling.c`: Εγγραφή δομής `Product` σε δυαδικό αρχείο `product.dat`.
- `exercise_12_file_handling.c`: Ανάγνωση δυαδικής εγγραφής από το `product.dat`.
- `exercise_13_file_handling.c`: Εγγραφή πολλαπλών δομών με `fwrite`.
- `exercise_14_file_handling.c`: Ανάγνωση όλων των εγγραφών με βρόχο `fread`.
- `exercise_15_file_handling.c`: Τυχαία προσπέλαση με `fseek` για ανάγνωση της n-οστής εγγραφής.
- `exercise_16_file_handling.c`: Προσάρτηση νέων εγγραφών σε υπάρχον δυαδικό αρχείο (`"ab"`).
- `exercise_17_file_handling.c`: Αναζήτηση εγγραφής με βάση πρωτεύον κλειδί (ID).
- `exercise_18_file_handling.c`: Ενημέρωση (Update in-place) συγκεκριμένου πεδίου εγγραφής σε δυαδικό αρχείο.
- `exercise_19_file_handling.c`: Λογική διαγραφή εγγραφής με flag.
- `exercise_20_file_handling.c`: Φυσική διαγραφή εγγραφής μέσω αντιγραφής σε προσωρινό αρχείο.

## 3. Οδηγίες Εκτέλεσης
```bash
cd Structures/src
# Αρχικοποίηση δυαδικών αρχείων
gcc -Wall -Wextra -std=c11 init_items_dat.c -o init_items
./init_items

# Εκτέλεση άσκησης ενημέρωσης
gcc -Wall -Wextra -std=c11 exercise_18_file_handling.c -o ex18
./ex18
```
