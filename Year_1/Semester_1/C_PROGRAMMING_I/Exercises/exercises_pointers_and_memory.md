# Ασκήσεις Εξάσκησης: Δείκτες και Διαχείριση Μνήμης

## Άσκηση 1: Αριθμητική Δεικτών και Αντιστροφή Πίνακα
### Εκφώνηση
Υλοποιήστε συνάρτηση με πρωτότυπο `void reverse_array(int *start, int *end)` η οποία δέχεται δείκτη στην αρχή και στο τέλος ενός πίνακα ακεραίων και αντιστρέφει τα στοιχεία του επί τόπου (in-place) χρησιμοποιώντας αποκλειστικά αριθμητική δεικτών.

### Λύση
```c
#include <stdio.h>

void reverse_array(int *start, int *end) {
    while (start < end) {
        int temp = *start;
        *start = *end;
        *end = temp;
        start++;
        end--;
    }
}

int main(void) {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);

    reverse_array(arr, arr + n - 1);

    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    return 0;
}
```

---

## Άσκηση 2: Δυναμική Δέσμευση Δισδιάστατου Πίνακα
### Εκφώνηση
Γράψτε συνάρτηση που δεσμεύει δυναμικά πίνακα $N \times M$ ακεραίων, αρχικοποιεί τα στοιχεία του με μηδέν, και αντίστοιχη συνάρτηση αποδέσμευσης της μνήμης.

### Λύση
```c
#include <stdio.h>
#include <stdlib.h>

int** allocate_matrix(int rows, int cols) {
    int **matrix = (int**)malloc(rows * sizeof(int*));
    if (matrix == NULL) return NULL;

    for (int i = 0; i < rows; i++) {
        matrix[i] = (int*)calloc(cols, sizeof(int));
        if (matrix[i] == NULL) {
            for (int j = 0; j < i; j++) free(matrix[j]);
            free(matrix);
            return NULL;
        }
    }
    return matrix;
}

void free_matrix(int **matrix, int rows) {
    if (matrix == NULL) return;
    for (int i = 0; i < rows; i++) {
        free(matrix[i]);
    }
    free(matrix);
}
```
