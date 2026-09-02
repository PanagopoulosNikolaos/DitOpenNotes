# Εργαστηριακή Εργασία 2: Χειρισμός Συμβολοσειρών και Αλγόριθμοι Κειμένου (<string.h>)

## 1. Σκοπός και Περιγραφή
Η εργασία αυτή καλύπτει τη βαθιά κατανόηση της αναπαράστασης συμβολοσειρών στη C (`char[]` τερματιζόμενο με `'\0'`), τις συναρτήσεις της βιβλιοθήκης `<string.h>` και την υλοποίηση κλασικών αλγορίθμων κειμένου.

## 2. Ευρετήριο Υλοποιήσεων (`String_LIB/src/`)
- `Lib_String_Exercise_0.c`: Υπολογισμός μήκους συμβολοσειράς (`strlen`).
- `Lib_String_Exercise_1.c`: Αντιγραφή περιεχομένου buffer (`strcpy`).
- `Lib_String_Exercise_2.c`: Συνένωση συμβολοσειρών (`strcat`).
- `Lib_String_Exercise_3.c`: Λεξικογραφική σύγκριση (`strcmp`).
- `Lib_String_Exercise_4.c`: Αντιστροφή συμβολοσειράς in-place.
- `Lib_String_Exercise_5.c`: Εντοπισμός πρώτης εμφάνισης χαρακτήρα (`strchr`).
- `Lib_String_Exercise_6.c`: Αναζήτηση υποσυμβολοσειράς (`strstr`).
- `Lib_String_Exercise_7.c`: Μετατροπή σε πεζά γράμματα (`toLowerString`).
- `Lib_String_Exercise_8.c`: Τεμαχισμός συμβολοσειράς σε tokens (`strtok`).
- `Lib_String_Exercise_9.c`: Αρχικοποίηση μνήμης (`memset`).
- `Lib_String_Exercise_10.c`: Καταμέτρηση συχνότητας μοναδικών λέξεων σε κείμενο.
- `Lib_String_Exercise_11.c`: Αφαίρεση χαρακτήρων νέας γραμμής με `strcspn`.
- `Lib_String_Exercise_12.c`: Έλεγχος παλινδρομικής συμβολοσειράς (Palindrome).
- `Lib_String_Exercise_13.c`: Δυναμικός κατακερματισμός και επιστροφή πίνακα δεικτών (`char**`).
- `Lib_String_Exercise_14.c`: Εύρεση Μεγαλύτερης Κοινής Υποσυμβολοσειράς (LCS) με δυναμικό προγραμματισμό.
- `Lib_String_Exercise_15.c`: Αλγόριθμος αναζήτησης προτύπου (Pattern Matching).
- `Lib_String_Exercise_16.c`: Μετατροπή αριθμών σε λεκτική περιγραφή (Number to Words).
- `Lib_String_Exercise_17.c`: Έλεγχος αναγραμματισμού (Anagrams).
- `Lib_String_Exercise_18.c`: Αλγόριθμος Boyer-Moore / Knuth-Morris-Pratt για αναζήτηση λέξεων.
- `Lib_String_Exercise_19.c`: Αποτίμηση απλών αριθμητικών εκφράσεων με `strtod`.

## 3. Οδηγίες Μεταγλώττισης και Εκτέλεσης
```bash
cd String_LIB/src
gcc -Wall -Wextra -std=c11 Lib_String_Exercise_4.c -o string_ex4
./string_ex4
```
