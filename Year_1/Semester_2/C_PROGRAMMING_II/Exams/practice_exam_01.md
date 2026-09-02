# Επαναληπτικό Θέμα Εξετάσεων: Προγραμματισμός C II

## Οδηγίες
- Διάρκεια εξέτασης: 2.5 ώρες.
- Όλα τα θέματα είναι ισοδύναμα (από 2.5 μονάδες).
- Απαιτείται σωστή διαχείριση μνήμης χωρίς memory leaks.

---

## Θέμα 1: Δείκτες και Διαχείριση Μνήμης
Δίνεται ο ακόλουθος ορισμός δομής:
```c
typedef struct DynamicVector {
    double *data;
    size_t size;
    size_t capacity;
} DynamicVector;
```
1. Υλοποιήστε τη συνάρτηση `DynamicVector *vectorCreate(size_t initial_capacity)`.
2. Υλοποιήστε τη συνάρτηση `int vectorPushBack(DynamicVector *vec, double value)` η οποία, εάν `size == capacity`, διπλασιάζει τη χωρητικότητα με `realloc`.
3. Υλοποιήστε τη συνάρτηση `void vectorDestroy(DynamicVector *vec)`.

---

## Θέμα 2: Αλγόριθμοι σε Συνδεδεμένες Λίστες
Δίνεται απλά συνδεδεμένη λίστα:
```c
typedef struct ListNode {
    int val;
    struct ListNode *next;
} ListNode;
```
Υλοποιήστε συνάρτηση `ListNode *mergeSortedLists(ListNode *l1, ListNode *l2)` η οποία συνενώνει δύο ήδη ταξινομημένες λίστες σε μία νέα ταξινομημένη λίστα χωρίς να δεσμεύει νέους κόμβους (αναδιατάσσοντας μόνο τους δείκτες `next`).

---

## Θέμα 3: Δυαδικά Αρχεία και Σειριοποίηση
Δίνεται δυαδικό αρχείο `scores.dat` που περιέχει εγγραφές τύπου:
```c
typedef struct StudentScore {
    int id;
    float grade;
} StudentScore;
```
Γράψτε συνάρτηση `float calculateAverageGrade(const char *filename)` η οποία διαβάζει το αρχείο και επιστρέφει τον μέσο όρο όλων των βαθμολογιών. Εάν το αρχείο είναι κενό ή δεν υπάρχει, επιστρέφει `-1.0f`.

---

## Θέμα 4: Δείκτες σε Συναρτήσεις
Υλοποιήστε συνάρτηση `void applyMap(int *arr, size_t n, int (*transform)(int))` η οποία τροποποιεί κάθε στοιχείο του πίνακα `arr` εφαρμόζοντας τη συνάρτηση μετασχηματισμού `transform`.

---

## Ενδεικτικές Λύσεις

### Λύση Θέματος 1
```c
DynamicVector *vectorCreate(size_t initial_capacity) {
    DynamicVector *v = (DynamicVector *)malloc(sizeof(DynamicVector));
    if (!v) return NULL;
    v->data = (double *)malloc(initial_capacity * sizeof(double));
    if (!v->data) {
        free(v);
        return NULL;
    }
    v->size = 0;
    v->capacity = initial_capacity;
    return v;
}

int vectorPushBack(DynamicVector *vec, double value) {
    if (!vec) return -1;
    if (vec->size >= vec->capacity) {
        size_t new_cap = vec->capacity == 0 ? 2 : vec->capacity * 2;
        double *new_data = (double *)realloc(vec->data, new_cap * sizeof(double));
        if (!new_data) return -1;
        vec->data = new_data;
        vec->capacity = new_cap;
    }
    vec->data[vec->size++] = value;
    return 0;
}

void vectorDestroy(DynamicVector *vec) {
    if (!vec) return;
    free(vec->data);
    free(vec);
}
```

### Λύση Θέματος 2
```c
ListNode *mergeSortedLists(ListNode *l1, ListNode *l2) {
    ListNode dummy;
    ListNode *tail = &dummy;
    dummy.next = NULL;

    while (l1 != NULL && l2 != NULL) {
        if (l1->val <= l2->val) {
            tail->next = l1;
            l1 = l1->next;
        } else {
            tail->next = l2;
            l2 = l2->next;
        }
        tail = tail->next;
    }
    tail->next = (l1 != NULL) ? l1 : l2;
    return dummy.next;
}
```

### Λύση Θέματος 3
```c
float calculateAverageGrade(const char *filename) {
    FILE *fp = fopen(filename, "rb");
    if (!fp) return -1.0f;

    StudentScore temp;
    double sum = 0.0;
    size_t count = 0;

    while (fread(&temp, sizeof(StudentScore), 1, fp) == 1) {
        sum += temp.grade;
        count++;
    }
    fclose(fp);

    if (count == 0) return -1.0f;
    return (float)(sum / count);
}
```

### Λύση Θέματος 4
```c
void applyMap(int *arr, size_t n, int (*transform)(int)) {
    if (!arr || !transform) return;
    for (size_t i = 0; i < n; ++i) {
        arr[i] = transform(arr[i]);
    }
}
```

