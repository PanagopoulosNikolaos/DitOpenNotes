# Διάλεξη 2: Σύνθετες Δομές Δεδομένων, Δείκτες σε Συναρτήσεις και Δυαδική Είσοδος/Έξοδος Αρχείων

## 1. Δομές Δεδομένων (Structures) και Αυτοαναφορικές Δομές

Οι δομές στη C (`struct`) επιτρέπουν την ομαδοποίηση μεταβλητών διαφορετικών τύπων δεδομένων κάτω από ένα ενιαίο όνομα.

### Ορισμός και Χρήση
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct StudentRecord {
    int id;
    char name[64];
    double gpa;
} StudentRecord;

/**
 * Creates and initializes a new StudentRecord on heap.
 * Args:
 *   id (int): Student identification number.
 *   name (const char*): Full name.
 *   gpa (double): Grade point average.
 * Returns:
 *   StudentRecord*: Pointer to the allocated record.
 */
StudentRecord *createStudent(int id, const char *name, double gpa) {
    StudentRecord *student = (StudentRecord *)malloc(sizeof(StudentRecord));
    if (student == NULL) {
        return NULL;
    }
    student->id = id;
    strncpy(student->name, name, sizeof(student->name) - 1);
    student->name[sizeof(student->name) - 1] = '\0';
    student->gpa = gpa;
    return student;
}
```

### Αυτοαναφορικές Δομές (Self-referential Structures)
Μια δομή που περιέχει δείκτη στον ίδιο της τον τύπο αποτελεί τη βάση για δυναμικές δομές όπως συνδεδεμένες λίστες (linked lists) και δέντρα (trees):

```c
typedef struct Node {
    int data;
    struct Node *next;
} Node;
```

---

## 2. Δείκτες σε Συναρτήσεις (Function Pointers)

Οι δείκτες σε συναρτήσεις επιτρέπουν τη μεταβίβαση συναρτήσεων ως ορίσματα (callbacks), διευκολύνοντας τον πολυμορφισμό και την υλοποίηση γενικών αλγορίθμων (π.χ. `qsort`).

### Σύνταξη και Παράδειγμα
```c
#include <stdio.h>

typedef int (*CompareFunc)(int, int);

/**
 * Ascending comparison function.
 */
int compareAscending(int a, int b) {
    return a - b;
}

/**
 * Descending comparison function.
 */
int compareDescending(int a, int b) {
    return b - a;
}

/**
 * Performs bubble sort using a custom comparator callback.
 */
void bubbleSort(int *arr, size_t n, CompareFunc cmp) {
    for (size_t i = 0; i < n - 1; ++i) {
        for (size_t j = 0; j < n - i - 1; ++j) {
            if (cmp(arr[j], arr[j + 1]) > 0) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}
```

---

## 3. Διαχείριση Αρχείων και Δυαδική Είσοδος/Έξοδος (File I/O)

Η C παρέχει συναρτήσεις χειρισμού ροών αρχείων (`FILE*`) μέσω του `<stdio.h>`.

### Συναρτήσεις Κειμένου vs Δυαδικών Αρχείων
- Κείμενο: `fopen("file.txt", "r")`, `fprintf()`, `fscanf()`, `fgets()`, `fputs()`.
- Δυαδικά: `fopen("file.bin", "rb")`, `fread()`, `fwrite()`, `fseek()`, `ftell()`.

```c
#include <stdio.h>

/**
 * Writes an array of student records to a binary file.
 */
int saveStudentsBinary(const char *filename, const StudentRecord *students, size_t count) {
    FILE *file = fopen(filename, "wb");
    if (file == NULL) {
        perror("Error opening file for writing");
        return -1;
    }

    size_t written = fwrite(students, sizeof(StudentRecord), count, file);
    fclose(file);

    return (written == count) ? 0 : -1;
}

/**
 * Reads student records from a binary file into a buffer.
 */
int loadStudentsBinary(const char *filename, StudentRecord *students, size_t count) {
    FILE *file = fopen(filename, "rb");
    if (file == NULL) {
        perror("Error opening file for reading");
        return -1;
    }

    size_t read_count = fread(students, sizeof(StudentRecord), count, file);
    fclose(file);

    return (read_count == count) ? 0 : -1;
}
```

