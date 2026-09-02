# Διάλεξη 1: Δείκτες, Αριθμητική Δεικτών και Δυναμική Διαχείριση Μνήμης

## 1. Εισαγωγή στους Δείκτες και τη Διάταξη Μνήμης

Στη γλώσσα C, ένας δείκτης (pointer) είναι μια μεταβλητή που αποθηκεύει τη διεύθυνση μνήμης μιας άλλης μεταβλητής. Η κατανόηση της αρχιτεκτονικής μνήμης είναι θεμελιώδης:
- **Stack (Στοίβα):** Αυτόματη δέσμευση τοπικών μεταβλητών κατά την κλήση συναρτήσεων.
- **Heap (Σωρός):** Περιοχή δυναμικής παραχώρησης μνήμης κατά τον χρόνο εκτέλεσης (runtime).
- **Data/BSS Segment:** Καθολικές (global) και στατικές (static) μεταβλητές.
- **Code/Text Segment:** Οι εκτελέσιμες εντολές μηχανής του προγράμματος.

### Δήλωση και Τελεστές Δεικτών
- Ο τελεστής αναφοράς `&` (address-of) επιστρέφει τη διεύθυνση μνήμης.
- Ο τελεστής αποαναφοράς `*` (dereference) αποκτά πρόσβαση στην τιμή που βρίσκεται στη διεύθυνση.

```c
#include <stdio.h>

/**
 * Demonstrates basic pointer declarations and dereferencing.
 * Returns:
 *   int: Exit status code.
 */
int main(void) {
    int value = 42;
    int *ptr = &value; // Stores address of value

    printf("Value: %d\n", *ptr);
    printf("Address: %p\n", (void *)ptr);

    *ptr = 100; // Modifies the original variable via pointer
    printf("Modified Value: %d\n", value);

    return 0;
}
```

---

## 2. Αριθμητική Δεικτών (Pointer Arithmetic)

Η αριθμητική δεικτών βασίζεται στο μέγεθος του τύπου δεδομένων στον οποίο δείχνει ο δείκτης (`sizeof(T)`).
- `ptr + n`: Αυξάνει τη διεύθυνση κατά `n * sizeof(*ptr)` bytes.
- `ptr - n`: Μειώνει τη διεύθυνση αντίστοιχα.
- `ptr2 - ptr1`: Επιστρέφει τον αριθμό των στοιχείων ανάμεσα σε δύο δείκτες του ίδιου πίνακα (τύπος `ptrdiff_t`).

```c
#include <stdio.h>

/**
 * Demonstrates pointer arithmetic on an array.
 */
void traverseArray(const int *arr, size_t size) {
    const int *ptr = arr;
    for (size_t i = 0; i < size; ++i) {
        printf("Element %zu: %d (Address: %p)\n", i, *(ptr + i), (const void *)(ptr + i));
    }
}
```

---

## 3. Δυναμική Διαχείριση Μνήμης (stdlib.h)

Η δυναμική παραχώρηση μνήμης στο Heap πραγματοποιείται μέσω των συναρτήσεων της βιβλιοθήκης `<stdlib.h>`:

| Συνάρτηση | Περιγραφή |
|---|---|
| `malloc(size_t size)` | Δεσμεύει block μνήμης μεγέθους `size` bytes χωρίς αρχικοποίηση. |
| `calloc(size_t num, size_t size)` | Δεσμεύει μνήμη για `num` στοιχεία και αρχικοποιεί όλα τα bits σε 0. |
| `realloc(void *ptr, size_t new_size)` | Αλλάζει το μέγεθος ενός ήδη δεσμευμένου block μνήμης. |
| `free(void *ptr)` | Αποδεσμεύει τη μνήμη επιστρέφοντάς την στο σύστημα. |

### Παράδειγμα Δυναμικής Δέσμευσης και Ελέγχου

```c
#include <stdio.h>
#include <stdlib.h>

/**
 * Allocates and initializes a dynamic integer buffer.
 * Args:
 *   count (size_t): The number of integers to allocate.
 * Returns:
 *   int*: Pointer to the allocated memory, or NULL on failure.
 */
int *allocateBuffer(size_t count) {
    int *buffer = (int *)malloc(count * sizeof(int));
    if (buffer == NULL) {
        perror("Failed to allocate memory");
        return NULL;
    }

    for (size_t i = 0; i < count; ++i) {
        buffer[i] = (int)(i * 10);
    }

    return buffer;
}
```

---

## 4. Συνήθη Λάθη και Διαρροές Μνήμης (Memory Leaks)

1. **Memory Leak:** Μη αποδέσμευση μνήμης με `free()` πριν χαθεί ο δείκτης.
2. **Dangling Pointer:** Χρήση δείκτη μετά την κλήση της `free()`.
3. **Double Free:** Κλήση της `free()` δύο φορές στην ίδια διεύθυνση.
4. **Buffer Overflow:** Εγγραφή πέρα από τα όρια του δεσμευμένου block.

> Βέλτιστη πρακτική: Μετά από κάθε `free(ptr);`, ορίζουμε πάντα `ptr = NULL;`.

