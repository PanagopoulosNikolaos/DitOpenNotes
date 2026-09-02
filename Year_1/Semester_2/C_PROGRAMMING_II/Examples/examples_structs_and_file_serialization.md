# Παραδείγματα: Σειριοποίηση Δομών Δεδομένων σε Δυαδικά Αρχεία

## Παράδειγμα 1: Σειριοποίηση και Αποσειριοποίηση Δυναμικής Δομής Δεδομένων

### Περιγραφή
Όταν μια δομή περιέχει δείκτες (π.χ. δυναμική συμβολοσειρά ή δυναμικό πίνακα), η απλή κλήση `fwrite(&struct_var, sizeof(struct_var), 1, fp)` αποθηκεύει μόνο τη διεύθυνση του δείκτη και όχι τα πραγματικά δεδομένα στο σωρό.

Το παρακάτω παράδειγμα επιδεικνύει τον σωστό τρόπο σειριοποίησης:
1. Αποθήκευση του μήκους των δεδομένων (`size_t`).
2. Αποθήκευση των πραγματικών bytes δεδομένων.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct DynamicDocument {
    int id;
    char *title;
    char *body;
} DynamicDocument;

/**
 * Serializes a DynamicDocument to a binary file.
 */
int serializeDocument(FILE *fp, const DynamicDocument *doc) {
    if (!fp || !doc) return -1;

    // Write ID
    if (fwrite(&doc->id, sizeof(int), 1, fp) != 1) return -1;

    // Write Title
    size_t title_len = doc->title ? strlen(doc->title) : 0;
    if (fwrite(&title_len, sizeof(size_t), 1, fp) != 1) return -1;
    if (title_len > 0) {
        if (fwrite(doc->title, sizeof(char), title_len, fp) != title_len) return -1;
    }

    // Write Body
    size_t body_len = doc->body ? strlen(doc->body) : 0;
    if (fwrite(&body_len, sizeof(size_t), 1, fp) != 1) return -1;
    if (body_len > 0) {
        if (fwrite(doc->body, sizeof(char), body_len, fp) != body_len) return -1;
    }

    return 0;
}

/**
 * Deserializes a DynamicDocument from a binary file.
 */
int deserializeDocument(FILE *fp, DynamicDocument *doc) {
    if (!fp || !doc) return -1;

    // Read ID
    if (fread(&doc->id, sizeof(int), 1, fp) != 1) return -1;

    // Read Title
    size_t title_len = 0;
    if (fread(&title_len, sizeof(size_t), 1, fp) != 1) return -1;
    if (title_len > 0) {
        doc->title = (char *)malloc(title_len + 1);
        if (!doc->title) return -1;
        fread(doc->title, sizeof(char), title_len, fp);
        doc->title[title_len] = '\0';
    } else {
        doc->title = NULL;
    }

    // Read Body
    size_t body_len = 0;
    if (fread(&body_len, sizeof(size_t), 1, fp) != 1) return -1;
    if (body_len > 0) {
        doc->body = (char *)malloc(body_len + 1);
        if (!doc->body) return -1;
        fread(doc->body, sizeof(char), body_len, fp);
        doc->body[body_len] = '\0';
    } else {
        doc->body = NULL;
    }

    return 0;
}

/**
 * Frees memory of document fields.
 */
void freeDocument(DynamicDocument *doc) {
    if (!doc) return;
    free(doc->title);
    free(doc->body);
    doc->title = NULL;
    doc->body = NULL;
}
```

