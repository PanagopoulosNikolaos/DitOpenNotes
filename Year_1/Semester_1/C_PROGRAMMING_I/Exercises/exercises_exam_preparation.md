# Επαναληπτικές Ασκήσεις Προετοιμασίας Εξετάσεων C

## Θέμα 1: Συμβολοσειρές και Χειρισμός Χαρακτήρων
### Εκφώνηση
Να γραφεί συνάρτηση `int count_and_clean(char *str)` η οποία αφαιρεί όλους τους χαρακτήρες εκτός από αλφαριθμητικούς από τη συμβολοσειρά `str`, μετατρέπει όλα τα γράμματα σε πεζά και επιστρέφει το τελικό πλήθος των χαρακτήρων.

### Λύση
```c
#include <stdio.h>
#include <ctype.h>

int count_and_clean(char *str) {
    char *read_ptr = str;
    char *write_ptr = str;

    while (*read_ptr != '\0') {
        if (isalnum((unsigned char)*read_ptr)) {
            *write_ptr = tolower((unsigned char)*read_ptr);
            write_ptr++;
        }
        read_ptr++;
    }
    *write_ptr = '\0';
    return (int)(write_ptr - str);
}

int main(void) {
    char text[] = "Hello, World! 2026";
    int len = count_and_clean(text);
    printf("Καθαρισμένη συμβολοσειρά: %s (Μήκος: %d)\n", text, len);
    return 0;
}
```

---

## Θέμα 2: Δομές και Ταξινόμηση
### Εκφώνηση
Ορίστε δομή `Product` με πεδία `id`, `name`, και `price`. Υλοποιήστε συνάρτηση που ταξινομεί έναν πίνακα προϊόντων κατά αύξουσα σειρά τιμής χρησιμοποιώντας τον αλγόριθμο ταξινόμησης φυσαλίδας (Bubble Sort).

### Λύση
```c
#include <stdio.h>
#include <string.h>

typedef struct {
    int id;
    char name[30];
    float price;
} Product;

void sort_products_by_price(Product arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j].price > arr[j + 1].price) {
                Product temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}
```
