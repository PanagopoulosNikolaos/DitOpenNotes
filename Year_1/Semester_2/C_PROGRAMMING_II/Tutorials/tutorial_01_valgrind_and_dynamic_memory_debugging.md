# Εργαστηριακός Οδηγός 1: Εντοπισμός Διαρροών Μνήμης με το Valgrind και τον AddressSanitizer

## 1. Σκοπός Εργαστηρίου
Σε αυτό το εργαστήριο θα εξοικειωθείτε με τα εργαλεία ανάλυσης μνήμης `Valgrind` (`Memcheck`) και τον ενσωματωμένο `AddressSanitizer` (`ASan`) του GCC/Clang για τον εντοπισμό:
- Διαρροών μνήμης (Memory Leaks).
- Μη αρχικοποιημένης ανάγνωσης (Uninitialized Reads).
- Μη έγκυρων προσπελάσεων (Out-of-bounds Read/Write, Use-after-free).

---

## 2. Μεταγλώττιση με Πληροφορίες Αποσφαλμάτωσης

Για να παρέχει το Valgrind ακριβείς αριθμούς γραμμών κώδικα, μεταγλωττίζουμε με τη σημαία `-g`:

```bash
gcc -Wall -Wextra -g -O0 memory_test.c -o memory_test
```

---

## 3. Παράδειγμα Προβληματικού Κώδικα

```c
#include <stdio.h>
#include <stdlib.h>

void faultyFunction(void) {
    int *array = (int *)malloc(5 * sizeof(int));
    
    // Bug 1: Out-of-bounds write
    for (int i = 0; i <= 5; ++i) {
        array[i] = i * 2;
    }

    // Bug 2: Missing free(array) -> Memory Leak
}

int main(void) {
    faultyFunction();
    return 0;
}
```

---

## 4. Εκτέλεση με Valgrind

Εκτελούμε την εντολή:

```bash
valgrind --leak-check=full --show-leak-kinds=all --track-origins=yes ./memory_test
```

### Ανάλυση Εξόδου Valgrind
- **Invalid write of size 4:** Αναφορά εγγραφής πέρα από το δεσμευμένο όριο του πίνακα.
- **HEAP SUMMARY:**
  - `definitely lost: 20 bytes in 1 blocks` — Το buffer που δεσμεύτηκε με `malloc` δεν αποδεσμεύτηκε ποτέ με `free()`.
- **ERROR SUMMARY:** Καταγραφή του συνολικού αριθμού λαθών μνήμης.

---

## 5. Χρήση του AddressSanitizer (ASan)

Μια εναλλακτική μέθοδος ταχείας ανίχνευσης είναι η μεταγλώττιση με τις σημαίες sanitizers:

```bash
gcc -fsanitize=address -g -O1 memory_test.c -o memory_test_asan
./memory_test_asan
```

Το πρόγραμμα διακόπτεται άμεσα μόλις ανιχνευθεί η παράνομη πρόσβαση, τυπώνοντας πλήρες stack trace.

