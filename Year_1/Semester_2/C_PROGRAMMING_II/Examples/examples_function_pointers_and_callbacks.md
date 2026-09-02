# Παραδείγματα: Δείκτες Συναρτήσεων και Συναρτήσεις Ανάκλησης (Callbacks)

## Παράδειγμα 1: Γενική Συνάρτηση Φιλτραρίσματος Πίνακα (Filter / Predicate)

### Περιγραφή
Υλοποίηση συνάρτησης γενικού φιλτραρίσματος ακεραίων, η οποία δέχεται έναν πίνακα, το μέγεθός του, και έναν δείκτη σε συνάρτηση κατηγορήματος (`Predicate`), επιστρέφοντας έναν νέο δυναμικά δεσμευμένο πίνακα με τα στοιχεία που ικανοποιούν τη συνθήκη.

```c
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef bool (*Predicate)(int);

/**
 * Predicate checking if an integer is even.
 */
bool isEven(int n) {
    return n % 2 == 0;
}

/**
 * Predicate checking if an integer is positive.
 */
bool isPositive(int n) {
    return n > 0;
}

/**
 * Filters an array based on predicate function pointer.
 */
int *filterArray(const int *source, size_t size, Predicate pred, size_t *out_count) {
    if (source == NULL || pred == NULL || out_count == NULL) return NULL;

    size_t matches = 0;
    for (size_t i = 0; i < size; ++i) {
        if (pred(source[i])) matches++;
    }

    *out_count = matches;
    if (matches == 0) return NULL;

    int *result = (int *)malloc(matches * sizeof(int));
    if (!result) return NULL;

    size_t k = 0;
    for (size_t i = 0; i < size; ++i) {
        if (pred(source[i])) {
            result[k++] = source[i];
        }
    }

    return result;
}

int main(void) {
    int data[] = {-5, 12, 3, -8, 0, 14, 7, 22};
    size_t count = sizeof(data) / sizeof(data[0]);

    size_t even_count = 0;
    int *evens = filterArray(data, count, isEven, &even_count);

    printf("Even numbers count: %zu\n", even_count);
    for (size_t i = 0; i < even_count; ++i) {
        printf("%d ", evens[i]);
    }
    printf("\n");

    free(evens);
    return 0;
}
```

