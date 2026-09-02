# Ασκήσεις Εμπέδωσης: Δυναμική Μνήμη και Δείκτες

## Άσκηση 1: Δυναμικός Δισδιάστατος Πίνακας (2D Dynamic Array)

### Εκφώνηση
Γράψτε συνάρτηση σε C η οποία δεσμεύει δυναμικά έναν δισδιάστατο πίνακα ακεραίων διαστάσεων $R \times C$, τον αρχικοποιεί με τιμές $A[i][j] = i \cdot j$, και στη συνέχεια παρέχει συνάρτηση για την πλήρη αποδέσμευσή του χωρίς διαρροές μνήμης.

### Λύση

```c
#include <stdio.h>
#include <stdlib.h>

/**
 * Allocates a 2D integer matrix dynamically.
 */
int **allocateMatrix(int rows, int cols) {
    int **matrix = (int **)malloc((size_t)rows * sizeof(int *));
    if (matrix == NULL) return NULL;

    for (int i = 0; i < rows; ++i) {
        matrix[i] = (int *)malloc((size_t)cols * sizeof(int));
        if (matrix[i] == NULL) {
            // Rollback previously allocated rows
            for (int j = 0; j < i; ++j) {
                free(matrix[j]);
            }
            free(matrix);
            return NULL;
        }
    }
    return matrix;
}

/**
 * Frees a dynamically allocated 2D matrix.
 */
void freeMatrix(int **matrix, int rows) {
    if (matrix == NULL) return;
    for (int i = 0; i < rows; ++i) {
        free(matrix[i]);
    }
    free(matrix);
}
```

---

## Άσκηση 2: Αναστροφή Συμβολοσειράς In-Place με Δείκτες

### Εκφώνηση
Υλοποιήστε συνάρτηση `void reverseString(char *str)` η οποία αναστρέφει μια συμβολοσειρά επί τόπου (in-place) χρησιμοποιώντας αποκλειστικά αριθμητική δεικτών (χωρίς δείκτες θέσης `[]`).

### Λύση

```c
#include <stdio.h>
#include <string.h>

/**
 * Reverses a null-terminated string in-place using two pointers.
 */
void reverseString(char *str) {
    if (str == NULL || *str == '\0') return;

    char *start = str;
    char *end = str + strlen(str) - 1;

    while (start < end) {
        char temp = *start;
        *start = *end;
        *end = temp;
        start++;
        end--;
    }
}
```

