# Πλήρης Οδηγός Προγραμματισμού στη C

## Αρχεία στη C

### Δημιουργία Αρχείων

**Δείκτης FILE**: Χρησιμοποιήστε δείκτη `FILE*` και τη συνάρτηση `fopen()` για να εργαστείτε με αρχεία.

```c
FILE *fptr;
fptr = fopen("filename.txt", "w");  // Δημιουργεί το αρχείο αν δεν υπάρχει
fclose(fptr);  // Πάντα κλείνετε τα αρχεία
```

**Λειτουργίες**:
- `w` - Εγγραφή (δημιουργεί το αρχείο αν δεν υπάρχει)
- `a` - Προσθήκη (προσθέτει στο τέλος)
- `r` - Ανάγνωση

**Απόλυτη Διαδρομή** (Windows):
```c
fptr = fopen("C:\\directoryname\\filename.txt", "w");
```

### Εγγραφή σε Αρχεία

**Λειτουργία εγγραφής** (`w`) - Αντικαθιστά το υπάρχον περιεχόμενο:
```c
FILE *fptr = fopen("filename.txt", "w");
fprintf(fptr, "Some text");
fclose(fptr);
```

**Λειτουργία προσθήκης** (`a`) - Προσθέτει στο τέλος χωρίς διαγραφή:
```c
FILE *fptr = fopen("filename.txt", "a");
fprintf(fptr, "\nNew line");
fclose(fptr);
```

### Ανάγνωση Αρχείων

**Βασική ανάγνωση**:
```c
FILE *fptr = fopen("filename.txt", "r");
char myString[100];
fgets(myString, 100, fptr);  // Διαβάζει την πρώτη γραμμή
printf("%s", myString);
fclose(fptr);
```

**Ανάγνωση όλων των γραμμών**:
```c
FILE *fptr = fopen("filename.txt", "r");
char myString[100];
while(fgets(myString, 100, fptr)) {
    printf("%s", myString);
}
fclose(fptr);
```

**Έλεγχος NULL** (καλή πρακτική):
```c
FILE *fptr = fopen("filename.txt", "r");
if(fptr == NULL) {
    printf("Not able to open the file.\n");
    return 1;
}
// Επεξεργασία αρχείου
fclose(fptr);
```

---

## Δομές στη C

### Βασική Δομή

**Δήλωση και χρήση**:
```c
struct Car {
    char brand[30];
    char model[30];
    int year;
};

int main() {
    struct Car car1 = {"BMW", "X5", 1999};
    printf("%s %s %d\n", car1.brand, car1.model, car1.year);
    return 0;
}
```

**Ανάθεση συμβολοσειράς** - Χρησιμοποιήστε `strcpy()`:
```c
struct Car car1;
strcpy(car1.brand, "Toyota");
```

**Αντιγραφή δομών**:
```c
struct Car s1 = {13, 'B', "Some text"};
struct Car s2 = s1;  // Αντιγράφει όλες τις τιμές
```

### Ένθετες Δομές

**Δομή μέσα σε δομή**:
```c
struct Owner {
    char firstName[30];
    char lastName[30];
};

struct Car {
    char brand[30];
    int year;
    struct Owner owner;  // Ένθετη
};

int main() {
    struct Owner person = {"John", "Doe"};
    struct Car car1 = {"Toyota", 2010, person};
    printf("Owner: %s %s\n", car1.owner.firstName, car1.owner.lastName);
    return 0;
}
```

### Δομές με Δείκτες

**Δείκτης σε δομή** - Χρησιμοποιήστε τον τελεστή `->`:
```c
struct Car car = {"Toyota", 2020};
struct Car *ptr = &car;

// Πρόσβαση με ->
printf("Brand: %s\n", ptr->brand);
printf("Year: %d\n", ptr->year);
```

**Πέρασμα σε συνάρτηση**:
```c
void updateYear(struct Car *c) {
    c->year = 2025;  // Τροποποιεί το πρωτότυπο
}

int main() {
    struct Car myCar = {"Toyota", 2020};
    updateYear(&myCar);
    printf("Year: %d\n", myCar.year);  // 2025
    return 0;
}
```

**Γιατί να χρησιμοποιήσετε δείκτες;**
- Αποφυγή αντιγραφής μεγάλων δεδομένων (ταχύτερο, λιγότερη μνήμη)
- Τροποποίηση αρχικών τιμών σε συναρτήσεις
- Δυναμική κατανομή με `malloc()`

### Ενώσεις (Unions)

**Κοινόχρηστη μνήμη** - Όλα τα μέλη μοιράζονται τον ίδιο χώρο:
```c
union myUnion {
    int myNum;
    char myLetter;
    char myString[30];
};

int main() {
    union myUnion u1;
    u1.myLetter = 'A';  // Μόνο η τελευταία τιμή είναι έγκυρη
    printf("%c\n", u1.myLetter);  // Εκτυπώνει 'A'
    return 0;
}
```

**Μέγεθος** - Ισούται με το μεγαλύτερο μέλος:
```c
union myUnion {
    int myNum;        // 4 bytes
    char myString[36]; // 36 bytes
};
// Μέγεθος = 36 bytes (ενώ η δομή θα ήταν 40 bytes)
```

**Πότε να χρησιμοποιείται**: Αποθήκευση διαφορετικών τύπων στην ίδια θέση, μόνο μία τιμή τη φορά, εξοικονόμηση μνήμης.

### typedef

**Απλοποίηση δηλώσεων**:
```c
// Χωρίς typedef
struct Car car1 = {"BMW", 1999};

// Με typedef
typedef struct {
    char brand[30];
    int year;
} Car;

Car car2 = {"Ford", 1969};  // Πιο σύντομο!
```

**Πολλαπλές ένθετες δομές**:
```c
typedef struct {
    char firstName[20];
    char lastName[20];
} Owner;

typedef struct {
    char brand[20];
    int year;
    Owner owner;
} Car;

typedef struct {
    char name[30];
    Car featuredCar;
} Dealership;
```

### Ευθυγράμμιση Δομών (Struct Padding)

**Ευθυγράμμιση μνήμης** - Ο μεταγλωττιστής προσθέτει bytes συμπλήρωσης:
```c
struct Example {
    char a;  // 1 byte
    int b;   // 4 bytes
    char c;  // 1 byte
};
// Αναμενόμενο: 6 bytes, Πραγματικό: 12 bytes (με συμπλήρωση)
```

**Διάταξη μνήμης**:
| Μέλος | Bytes | Σημειώσεις |
|--------|-------|-------|
| a | 1 | Αποθηκεύεται πρώτο |
| συμπλήρωση | 3 | Ευθυγραμμίζει το `b` σε όριο 4 bytes |
| b | 4 | Ευθυγραμμισμένο |
| c | 1 | Αποθηκεύεται |
| συμπλήρωση | 3 | Το συνολικό μέγεθος είναι πολλαπλάσιο του 4 |

**Μείωση συμπλήρωσης** - Ταξινόμηση κατά μέγεθος:
```c
struct Example {
    int b;   // 4 bytes
    char a;  // 1 byte
    char c;  // 1 byte
};
// Μέγεθος = 8 bytes (λιγότερη συμπλήρωση)
```

**Συμπλήρωση Δομής έναντι Ένωσης**:
- **Δομή**: Συμπλήρωση μεταξύ μελών
- **Ένωση**: Καμία συμπλήρωση μεταξύ (μοιράζονται την ίδια μνήμη), μέγεθος = μεγαλύτερο μέλος

---

## Απαριθμήσεις στη C

### Βασική Απαρίθμηση

**Δήλωση**:
```c
enum Level {
    LOW,     // 0
    MEDIUM,  // 1
    HIGH     // 2
};

int main() {
    enum Level myVar = MEDIUM;
    printf("%d", myVar);  // Εκτυπώνει 1
    return 0;
}
```

### Προσαρμοσμένες Τιμές

**Ανάθεση συγκεκριμένων τιμών**:
```c
enum Level {
    LOW = 25,
    MEDIUM = 50,
    HIGH = 75
};
```

**Διαδοχικές τιμές**:
```c
enum Level {
    LOW = 5,
    MEDIUM,  // 6
    HIGH     // 7
};
```

### Απαρίθμηση σε Switch

```c
enum Level {
    LOW = 1,
    MEDIUM,
    HIGH
};

int main() {
    enum Level myVar = MEDIUM;
    switch (myVar) {
        case 1: printf("Low Level"); break;
        case 2: printf("Medium level"); break;
        case 3: printf("High level"); break;
    }
    return 0;
}
```

### typedef με Απαρίθμηση

**Συντομότερη σύνταξη**:
```c
// Χωρίς typedef
enum Day {MON, TUE, WED, THU, FRI, SAT, SUN};
enum Day today = WED;

// Με typedef
typedef enum {MON, TUE, WED, THU, FRI, SAT, SUN} Day;
Day today = WED;  // Πιο καθαρό!
```

**Πότε να χρησιμοποιείται**: Σταθερές τιμές (ημέρες, μήνες, χρώματα, καταστάσεις).

---

## Διαχείριση Μνήμης στη C

### Κατανόηση της Μνήμης

**Μεγέθη μνήμης**:
```c
int myInt;      // 4 bytes
float myFloat;  // 4 bytes
double myDouble; // 8 bytes
char myChar;    // 1 byte

printf("%zu\n", sizeof(myInt));  // Εκτυπώνει 4
```

**Γιατί είναι σημαντικό**: Διαχειριστείτε τη μνήμη για βελτιστοποίηση απόδοσης, αποφυγή διαρροών και αποφυγή καταρρεύσεων.

**Βασικά σημεία**:
- Χειροκίνητη διαχείριση μνήμης (κατανομή, επανακατανομή, απελευθέρωση)
- Χρήση δεικτών για άμεση εργασία με τη μνήμη
- Προσοχή με τους δείκτες (μπορούν να καταστρέψουν δεδομένα)

---

## Σφάλματα στη C

### Σφάλματα Μεταγλώττισης

**Λείπει ερωτηματικό**:
```c
int x = 5  // Σφάλμα: αναμενόταν ';'
printf("%d", x);
```

**Μη δηλωμένη μεταβλητή**:
```c
printf("%d", myVar);  // Σφάλμα: το 'myVar' δεν έχει δηλωθεί
```

**Αναντιστοιχία τύπου**:
```c
int x = "Hello";  // Σφάλμα: η αρχικοποίηση μετατρέπει ακέραιο από δείκτη
```

### Σφάλματα Χρόνου Εκτέλεσης

**Διαίρεση με το μηδέν**:
```c
int x = 10;
int y = 0;
int result = x / y;  // Σφάλμα χρόνου εκτέλεσης
```

**Πίνακας εκτός ορίων**:
```c
int numbers[3] = {1, 2, 3};
printf("%d\n", numbers[8]);  // Απροσδιόριστη συμπεριφορά
```

**Χρήση απελευθερωμένης μνήμης**:
```c
int* ptr = malloc(sizeof(int));
*ptr = 10;
free(ptr);
printf("%d\n", *ptr);  // Απροσδιόριστη συμπεριφορά
```

### Καλές Πρακτικές

- Πάντα αρχικοποιείτε τις μεταβλητές
- Χρησιμοποιείτε ουσιαστικά ονόματα
- Κρατήστε τον κώδικα καθαρό και με σωστή στοίχιση
- Κρατήστε τις συναρτήσεις σύντομες
- Ελέγχετε τους βρόχους/συνθήκες
- Διαβάστε προσεκτικά τα μηνύματα σφαλμάτων

---

## Αποσφαλμάτωση στη C

### Αποσφαλμάτωση με Εκτύπωση

**Παρακολούθηση εκτέλεσης**:
```c
int x = 10, y = 0;
printf("Before division\n");
int z = x / y;  // Καταρρέει εδώ
printf("After division\n");  // Ποτέ δεν εκτελείται
```

### Έλεγχος Τιμών

```c
int result = x - y;
printf("Result: %d\n", result);  // Έλεγχος αν είναι το αναμενόμενο
```

### Ασφαλείς Έλεγχοι

**Πρόληψη καταρρεύσεων**:
```c
int x = 10, y = 0;
if (y != 0) {
    int z = x / y;
    printf("Result: %d\n", z);
} else {
    printf("Error: Division by zero!\n");
}
```

**Όρια πίνακα**:
```c
int numbers[3] = {10, 20, 30};
int index = 5;
if (index >= 0 && index < 3) {
    printf("Value = %d\n", numbers[index]);
} else {
    printf("Error: Index out of bounds!\n");
}
```

### Εργαλεία Αποσφαλμάτωσης

Χρησιμοποιήστε αποσφαλματωτές IDE (Visual Studio, VS Code, Code::Blocks) για:
- Σημεία διακοπής (παύση εκτέλεσης)
- Βήμα-βήμα εκτέλεση κώδικα
- Παρακολούθηση αλλαγών μεταβλητών

---

## NULL στη C

### Δείκτης NULL

**Ειδική τιμή** - Δείχνει στο τίποτα:
```c
FILE *fptr = fopen("nothing.txt", "r");
if (fptr == NULL) {
    printf("Could not open file.\n");
    return 1;
}
fclose(fptr);
```

**Αποτυχία κατανομής μνήμης**:
```c
int *numbers = (int*) malloc(100000000000000 * sizeof(int));
if (numbers == NULL) {
    printf("Memory allocation failed.\n");
    return 1;
}
free(numbers);
numbers = NULL;  // Καλή πρακτική μετά το free
```

**Βασικά σημεία**:
- Πάντα ελέγχετε τους δείκτες πριν τη χρήση
- Προλαμβάνει καταρρεύσεις από μη έγκυρη πρόσβαση στη μνήμη
- Οι συναρτήσεις επιστρέφουν NULL σε αποτυχία

---

## Διαχείριση Σφαλμάτων στη C

### Τιμές Επιστροφής

**Έλεγχος NULL**:
```c
FILE *fptr = fopen("nothing.txt", "r");
if (fptr == NULL) {
    printf("Error opening file.\n");
    return 1;
}
fclose(fptr);
```

### perror()

**Λεπτομερές μήνυμα σφάλματος**:
```c
FILE *f = fopen("nothing.txt", "r");
if (f == NULL) {
    perror("Error opening file");
    return 1;
}
fclose(f);
// Έξοδος: Error opening file: No such file or directory
```

### errno και strerror()

**Κωδικοί σφαλμάτων**:
```c
#include <errno.h>
#include <string.h>

FILE *f = fopen("nothing.txt", "r");
if (f == NULL) {
    printf("Error: %s\n", strerror(errno));
    return 1;
}
```

**Συνηθισμένοι κωδικοί σφαλμάτων**:
| Κωδικός | Σημασία |
|------|---------|
| ENOENT | Δεν υπάρχει τέτοιο αρχείο ή κατάλογος |
| EACCES | Άρνηση πρόσβασης |
| ENOMEM | Δεν υπάρχει αρκετή μνήμη |
| EINVAL | Μη έγκυρο όρισμα |

**Έλεγχος συγκεκριμένου σφάλματος**:
```c
if (errno == ENOENT) {
    printf("The file was not found.\n");
}
```

### exit()

**Άμεση διακοπή προγράμματος**:
```c
#include <stdlib.h>

FILE *f = fopen("nothing.txt", "r");
if (f == NULL) {
    printf("Failed to open file.\n");
    exit(EXIT_FAILURE);  // ή exit(1)
}
```

**Κωδικοί εξόδου**:
- 0 ή `EXIT_SUCCESS` - Επιτυχία
- 1 ή `EXIT_FAILURE` - Σφάλμα

---

## Έλεγχος Εισόδου στη C

### Έλεγχος Εύρους Αριθμού

```c
int number;
do {
    printf("Choose a number between 1 and 5: ");
    scanf("%d", &number);
    while (getchar() != '\n');  // Καθαρισμός buffer
} while (number < 1 || number > 5);
printf("You chose: %d\n", number);
```

### Έλεγχος Εισόδου Κειμένου

```c
#include <string.h>

char name[100];
do {
    printf("Enter your name: ");
    fgets(name, sizeof(name), stdin);
    name[strcspn(name, "\n")] = 0;  // Αφαίρεση νέας γραμμής
} while (strlen(name) == 0);
printf("Hello, %s\n", name);
```

### Έλεγχος Ακέραιας Εισόδου

```c
int number;
char input[100];
printf("Enter a number: ");
while (fgets(input, sizeof(input), stdin)) {
    if (sscanf(input, "%d", &number) == 1) {
        break;  // Έγκυρος ακέραιος
    } else {
        printf("Invalid input. Try again: ");
    }
}
printf("You entered: %d\n", number);
```

---

## Ημερομηνία και Ώρα στη C

### Τρέχουσα Ώρα

```c
#include <time.h>

time_t currentTime;
time(&currentTime);
printf("Current time: %s", ctime(&currentTime));
```

### Ανάλυση Ώρας

**Πρόσβαση σε επιμέρους μέρη**:
```c
time_t now = time(NULL);
struct tm *t = localtime(&now);

printf("Year: %d\n", t->tm_year + 1900);  // Προσθήκη 1900
printf("Month: %d\n", t->tm_mon + 1);     // 0-11, προσθήκη 1
printf("Day: %d\n", t->tm_mday);
printf("Hour: %d\n", t->tm_hour);
printf("Minute: %d\n", t->tm_min);
printf("Second: %d\n", t->tm_sec);
```

### Μορφοποίηση Ημερομηνίας/Ώρας

```c
time_t now = time(NULL);
struct tm *t = localtime(&now);
char buffer[100];

strftime(buffer, sizeof(buffer), "%d-%m-%Y %H:%M:%S", t);
printf("Formatted time: %s\n", buffer);
```

**Πότε να χρησιμοποιείται**: Εμφάνιση ώρας, καταγραφή συμβάντων, χρονοσφραγίδες, μέτρηση διάρκειας, σπορά τυχαίων αριθμών.

---

## Τυχαίοι Αριθμοί στη C

### Βασικός Τυχαίος

```c
#include <stdlib.h>

int r = rand();
printf("%d\n", r);
// Σημείωση: Ίδια ακολουθία κάθε εκτέλεση χωρίς σπορά
```

### Σπορά

**Χρήση τρέχουσας ώρας**:
```c
#include <time.h>

srand(time(NULL));  // Σπορά μία φορά στην αρχή
printf("%d\n", rand());
printf("%d\n", rand());
```

### Τυχαίο Εύρος

**0 έως 9**:
```c
int x = rand() % 10;
```

**1 έως 6 (ζάρια)**:
```c
int dice = (rand() % 6) + 1;
```

**Παράδειγμα - Ρίψη δύο ζαριών**:
```c
srand(time(NULL));
int dice1 = (rand() % 6) + 1;
int dice2 = (rand() % 6) + 1;
printf("You rolled %d and %d (total = %d)\n", dice1, dice2, dice1 + dice2);
```

---

## Μακροεντολές στη C

### #include

**Συμπερίληψη αρχείων**:
```c
#include <stdio.h>     // Τυπική βιβλιοθήκη
#include "myfile.h"    // Δικά σας αρχεία
```

### #define

**Απλή μακροεντολή**:
```c
#define PI 3.14

int main() {
    printf("Value of PI: %.2f\n", PI);
    return 0;
}
```

**Μακροεντολή με παραμέτρους**:
```c
#define SQUARE(x) ((x) * (x))

int main() {
    printf("Square of 4: %d\n", SQUARE(4));
    return 0;
}
```

### Υπό συνθήκη Μεταγλώττιση

**#ifdef / #ifndef**:
```c
#define DEBUG

int main() {
    #ifdef DEBUG
        printf("Debug mode is ON\n");
    #endif
    return 0;
}
```

---

## Οργάνωση Κώδικα στη C

### Αρχεία Κεφαλίδας

**Γιατί να χρησιμοποιούνται**:
- Δήλωση συναρτήσεων από άλλα αρχεία
- Κοινή χρήση μεταβλητών, σταθερών, μακροεντολών
- Οργάνωση σε λογικές ενότητες

### Δημιουργία Αρχείου Κεφαλίδας

**calc.h**:
```c
#ifndef CALC_H
#define CALC_H

int add(int x, int y);
int subtract(int x, int y);

#endif
```

**Προστασία συμπερίληψης** (`#ifndef`, `#define`, `#endif`) αποτρέπει πολλαπλή συμπερίληψη.

### Ορισμοί Συναρτήσεων

**calc.c**:
```c
#include "calc.h"

int add(int x, int y) {
    return x + y;
}

int subtract(int x, int y) {
    return x - y;
}
```

### Χρήση στο Main

**main.c**:
```c
#include <stdio.h>
#include "calc.h"

int main() {
    printf("5 + 5 = %d\n", add(5, 5));
    printf("6 - 4 = %d\n", subtract(6, 4));
    return 0;
}
```

### Μεταγλώττιση Πολλαπλών Αρχείων

```bash
gcc main.c calc.c -o program
```

---

## Κατηγορίες Αποθήκευσης στη C

### auto

**Προεπιλογή για τοπικές μεταβλητές**:
```c
int main() {
    auto int x = 50;  // Ίδιο με: int x = 50;
    return 0;
}
```

### static

**Διατηρεί την τιμή μεταξύ κλήσεων**:
```c
void count() {
    static int myNum = 0;  // Διατηρεί την τιμή
    myNum++;
    printf("num = %d\n", myNum);
}

int main() {
    count();  // num = 1
    count();  // num = 2
    count();  // num = 3
    return 0;
}
```

**Εμβέλεια αρχείου** - Δεν είναι ορατό εκτός αρχείου (για καθολικές μεταβλητές/συναρτήσεις).

### register

**Πρόταση καταχωρητή CPU** (κυρίως παρωχημένο):
```c
register int counter = 0;
```

### extern

**Δήλωση από άλλο αρχείο**:

**main.c**:
```c
extern int shared;  // Δηλωμένο, ορισμένο αλλού

int main() {
    printf("shared = %d\n", shared);
    return 0;
}
```

**data.c**:
```c
int shared = 50;  // Ορισμός
```

Μεταγλώττιση: `gcc main.c data.c -o program`

---

## Τελεστές Bitwise στη C

### Τελεστές

| Τελεστής | Όνομα | Περιγραφή |
|----------|------|-------------|
| & | AND | Και τα δύο bits πρέπει να είναι 1 |
| \| | OR | Οποιοδήποτε bit μπορεί να είναι 1 |
| ^ | XOR | Μόνο ένα bit είναι 1 |
| ~ | NOT | Αντιστρέφει όλα τα bits |
| << | Αριστερή Ολίσθηση | Πολλαπλασιασμός με δυνάμεις του 2 |
| >> | Δεξιά Ολίσθηση | Διαίρεση με δυνάμεις του 2 |

### Παραδείγματα

**Ρύθμιση**:
```c
int a = 6;  // 0110
int b = 3;  // 0011
```

**AND (&)**:
```c
int result = a & b;  // 2 (0010)
```

**OR (|)**:
```c
int result = a | b;  // 7 (0111)
```

**XOR (^)**:
```c
int result = a ^ b;  // 5 (0101)
```

**NOT (~)**:
```c
int result = ~a;  // -7 (αντιστρέφει τα bits)
```

**Αριστερή Ολίσθηση (<<)**:
```c
int result = 3 << 2;  // 12 (3 * 2^2)
```

**Δεξιά Ολίσθηση (>>)**:
```c
int result = 12 >> 2;  // 3 (12 / 2^2)
```

### Παράδειγμα Σημαιών

**Σημαίες δικαιωμάτων**:
```c
#define READ  1  // 0001
#define WRITE 2  // 0010
#define EXEC  4  // 0100

int permissions = READ | WRITE;  // Μπορεί να διαβάσει και να γράψει

if (permissions & READ) {
    printf("Read allowed\n");
}
if (permissions & WRITE) {
    printf("Write allowed\n");
}
if (permissions & EXEC) {
    printf("Execute allowed\n");
}
```

---

## Ακέραιοι Σταθερού Πλάτους στη C

### Τύποι

**Συμπερίληψη** `<stdint.h>`:

| Τύπος | Μέγεθος | Εύρος | Printf |
|------|------|-------|--------|
| int8_t | 8 bits | -128 έως 127 | %d |
| uint8_t | 8 bits | 0 έως 255 | %u |
| int16_t | 16 bits | -32,768 έως 32,767 | %d |
| uint16_t | 16 bits | 0 έως 65,535 | %u |
| int32_t | 32 bits | -2,147,483,648 έως 2,147,483,647 | %d |
| uint32_t | 32 bits | 0 έως 4,294,967,295 | %u |
| int64_t | 64 bits | -9,223,372,036,854,775,808 έως 9,223,372,036,854,775,807 | %lld |
| uint64_t | 64 bits | 0 έως 18,446,744,073,709,551,615 | %llu |

**u** = unsigned (χωρίς πρόσημο, μόνο μη αρνητικές, διπλάσια μέγιστη θετική τιμή)

### Χρήση

```c
#include <stdint.h>

int8_t a = 100;
int16_t b = 30000;
int32_t c = 2000000;
int64_t d = 9000000000;

printf("%d\n", a);
printf("%d\n", b);
printf("%d\n", c);
printf("%lld\n", d);
```

### Πότε να Χρησιμοποιείται

**Απαραίτητο για**:
- Ενσωματωμένα συστήματα
- Μορφές αρχείων (τα ακριβή μεγέθη έχουν σημασία)
- Επικοινωνία δικτύου (συνέπεια μεταξύ μηχανημάτων)

**Παράδειγμα** - Επίπεδο μπαταρίας:
```c
uint8_t battery = 87;  // 0-100, εξοικονομεί μνήμη
printf("Battery level is %u out of 100\n", battery);
```

---

## Έργα στη C

### Γιατί να Δημιουργείτε Έργα

- Κατανόηση δομής προγράμματος
- Εξάσκηση συνδυασμού εννοιών
- Βελτίωση δεξιοτήτων αποσφαλμάτωσης
- Προετοιμασία για συνεντεύξεις

### Μικρά Έργα

**Γεια σου Όνομα**:
- Ρωτήστε όνομα και ηλικία
- Εκτυπώστε: "Γεια <όνομα>! Θα γίνεις <ηλικία+1> του χρόνου."

**Λίστα Αγορών**:
- Αποθήκευση 5 αντικειμένων σε πίνακα
- Εκτύπωση λίστας
- Αναζήτηση αντικειμένων

### Μεσαία Έργα

- Παιχνίδι Μάντεψε τον Αριθμό
- Υπολογισμός Μέσου Όρου Μαθητή
- Απλή Αριθμομηχανή

### Προχωρημένα Έργα

- Βιβλίο Διευθύνσεων (δομές + αρχεία)
- Λίστα Εργασιών (διαχείριση αρχείων)
- Παιχνίδι Κουίζ (συναρτήσεις + πίνακες)

### Παράδειγμα - Μέσος Όρος Μαθητή

```c
char gradeFunction(double avg) {
    if (avg >= 90) return 'A';
    else if (avg >= 80) return 'B';
    else if (avg >= 70) return 'C';
    else if (avg >= 60) return 'D';
    else return 'F';
}

int main(void) {
    int count;
    double sum = 0, grade;
    
    printf("How many grades (1 to 5)? ");
    scanf("%d", &count);
    
    if (count < 1 || count > 5) {
        printf("Invalid number.\n");
        return 1;
    }
    
    for (int i = 1; i <= count; i++) {
        printf("Enter grade %d: ", i);
        scanf("%lf", &grade);
        sum += grade;
    }
    
    double avg = sum / count;
    printf("Average: %.2f\n", avg);
    printf("Letter grade: %c\n", gradeFunction(avg));
    
    return 0;
}
```

---

## Λέξεις-Κλειδιά στη C

| Λέξη-Κλειδί | Περιγραφή |
|---------|-------------|
| break | Έξοδος από βρόχο/switch |
| case | Σήμανση μπλοκ σε switch |
| char | Τύπος μεμονωμένου χαρακτήρα |
| const | Αμετάβλητη μεταβλητή |
| continue | Επόμενη επανάληψη βρόχου |
| default | Προεπιλεγμένο μπλοκ switch |
| do | Βρόχος do-while |
| double | Κινητής υποδιαστολής 64-bit |
| else | Υπό συνθήκη else |
| enum | Απαριθμημένος τύπος |
| float | Κινητής υποδιαστολής 32-bit |
| for | Βρόχος for |
| goto | Μετάβαση σε ετικέτα |
| if | Υπό συνθήκη if |
| int | Ακέραιος τύπος |
| long | Τουλάχιστον 32-bit ακέραιος |
| return | Επιστροφή από συνάρτηση |
| short | 16-bit ακέραιος |
| signed | Θετικές/αρνητικές τιμές |
| sizeof | Τελεστής μεγέθους μνήμης |
| static | Μόνιμη μεταβλητή |
| struct | Ορισμός δομής |
| switch | Επιλογή πολλαπλών περιπτώσεων |
| typedef | Ψευδώνυμο προσαρμοσμένου τύπου |
| unsigned | Μόνο θετικές τιμές |
| void | Καμία επιστροφή/γενικός δείκτης |
| while | Βρόχος while |

---

## Γρήγορη Αναφορά - Τυπικές Βιβλιοθήκες

### <stdio.h>
Είσοδος/έξοδος αρχείων: `printf()`, `scanf()`, `fopen()`, `fclose()`, `fprintf()`, `fgets()`, `perror()`

### <stdlib.h>
Μνήμη, βοηθητικά: `malloc()`, `free()`, `rand()`, `srand()`, `exit()`, `EXIT_SUCCESS`, `EXIT_FAILURE`

### <string.h>
Λειτουργίες συμβολοσειρών: `strcpy()`, `strlen()`, `strcmp()`, `strcat()`, `strcspn()`, `strerror()`

### <math.h>
Μαθηματικές συναρτήσεις: `sqrt()`, `pow()`, `sin()`, `cos()`, `abs()`

### <ctype.h>
Χειρισμός χαρακτήρων: `isalpha()`, `isdigit()`, `tolower()`, `toupper()`

### <time.h>
Ημερομηνία/ώρα: `time()`, `localtime()`, `ctime()`, `strftime()`, `struct tm`

### <errno.h>
Κωδικοί σφαλμάτων: `errno`, `ENOENT`, `EACCES`, `ENOMEM`, `EINVAL`

### <stdint.h>
Ακέραιοι σταθερού πλάτους: `int8_t`, `uint8_t`, `int16_t`, `uint16_t`, `int32_t`, `uint32_t`, `int64_t`, `uint64_t`

---

## Περίληψη Βέλτιστων Πρακτικών

1. **Πάντα αρχικοποιείτε τις μεταβλητές**
2. **Ελέγχετε για NULL** μετά από λειτουργίες αρχείων και κατανομή μνήμης
3. **Κλείνετε τα αρχεία** με `fclose()`
4. **Απελευθερώνετε τη μνήμη** με `free()` μετά από `malloc()`
5. **Χρησιμοποιείτε ουσιαστικά ονόματα** για μεταβλητές και συναρτήσεις
6. **Επικυρώνετε την είσοδο χρήστη** πριν την επεξεργασία
7. **Διαχειρίζεστε τα σφάλματα** με σωστούς ελέγχους και μηνύματα
8. **Κρατήστε τις συναρτήσεις σύντομες** και εστιασμένες
9. **Χρησιμοποιείτε σχόλια** για να εξηγείτε σύνθετη λογική
10. **Δοκιμάζετε συχνά** κατά την ανάπτυξη
11. **Χρησιμοποιείτε `const`** για τιμές που δεν πρέπει να αλλάξουν
12. **Οργανώνετε τον κώδικα** σε πολλαπλά αρχεία για μεγάλα έργα
13. **Χρησιμοποιείτε typedef** για να απλοποιείτε σύνθετους τύπους
14. **Ελέγχετε τα όρια πινάκων** πριν την πρόσβαση
15. **Σπέρνετε τη γεννήτρια τυχαίων** μία φορά στην αρχή του προγράμματος

---

**Τέλος Οδηγού**