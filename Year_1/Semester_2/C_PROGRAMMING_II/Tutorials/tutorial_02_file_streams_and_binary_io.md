# Εργαστηριακός Οδηγός 2: Ροές Αρχείων, Δυαδική Είσοδος/Έξοδος και Τυχαία Προσπέλαση

## 1. Σκοπός Εργαστηρίου
Στο παρόν εργαστήριο θα αναπτύξουμε μια ολοκληρωμένη εφαρμογή διαχείρισης αρχείου βάσης δεδομένων σε μορφή binary, κάνοντας χρήση των συναρτήσεων `fopen`, `fread`, `fwrite`, `fseek`, και `ftell`.

---

## 2. Θεωρητικό Υπόβαθρο

### Τυχαία Προσπέλαση με `fseek` και `ftell`
- `int fseek(FILE *stream, long offset, int origin)`: Μετακινεί τον δείκτη θέσης του αρχείου.
  - `SEEK_SET`: Σχετικά με την αρχή του αρχείου.
  - `SEEK_CUR`: Σχετικά με την τρέχουσα θέση.
  - `SEEK_END`: Σχετικά με το τέλος του αρχείου.
- `long ftell(FILE *stream)`: Επιστρέφει την τρέχουσα θέση του δείκτη σε bytes.
- `void rewind(FILE *stream)`: Επαναφέρει τον δείκτη στην αρχή (`fseek(stream, 0, SEEK_SET)`).

---

## 3. Πλήρης Υλοποίηση: Διαχείριση Προϊόντων Αποθήκης

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Product {
    int id;
    char name[32];
    double price;
    int stock;
} Product;

/**
 * Appends a product to the binary file.
 */
int addProduct(const char *filename, const Product *p) {
    FILE *fp = fopen(filename, "ab");
    if (!fp) return -1;
    fwrite(p, sizeof(Product), 1, fp);
    fclose(fp);
    return 0;
}

/**
 * Reads a product by its record index (0-indexed).
 */
int readProductByIndex(const char *filename, size_t index, Product *out_product) {
    FILE *fp = fopen(filename, "rb");
    if (!fp) return -1;

    fseek(fp, (long)(index * sizeof(Product)), SEEK_SET);
    size_t count = fread(out_product, sizeof(Product), 1, fp);
    fclose(fp);

    return (count == 1) ? 0 : -1;
}

/**
 * Counts total products in the file.
 */
long getTotalProducts(const char *filename) {
    FILE *fp = fopen(filename, "rb");
    if (!fp) return 0;

    fseek(fp, 0, SEEK_END);
    long bytes = ftell(fp);
    fclose(fp);

    return bytes / (long)sizeof(Product);
}
```

---

## 4. Ασκήσεις Εργαστηρίου
1. Υλοποιήστε συνάρτηση `updateProductStock(const char *filename, int id, int new_stock)` που βρίσκει το προϊόν με το συγκεκριμένο ID και τροποποιεί την τιμή stock in-place (`"r+b"`).
2. Υλοποιήστε συνάρτηση αναζήτησης με βάση το όνομα προϊόντος.

