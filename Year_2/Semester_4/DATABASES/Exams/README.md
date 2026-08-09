# Εξετάσεις Βάσεων Δεδομένων & Συγκεντρωτικά Τελικά

Καλώς ορίσατε στο **Κέντρο Ετοιμάσεως για Εξετάσεις**. Αυτός ο φάκελος περιέχει θεματικές εξάσκησης, συγκεντρωτικές ψεύτικες τελικές εξετάσεις, και αυτοματοποιημένους σενάριους συγκέντρωσης.

---

## Δομή Φακέλου

```
Exams/
├── README.md                           # Κύριος κατάλογος και οδηγός χρήσης (αυτό το αρχείο)
├── general_exam_subjects.md            # Λεπτομερής περιγραφή θεμάτων και μορφής εξέτασης
├── combine_notes.py                    # Σενάριο κατασκευής για all_exams.md
├── all_exams.md                        # Συγκεντρωτικό ελεγδοτικό έγγραφο
├── Practice_Exams/                     # Θεματικές εξάσκησης
│   ├── Practice_Exam_01_Easy.md        # Βαθμός: Εύκολο (Βασικά DDL & SQL)
│   ├── Practice_Exam_02_Medium.md      # Βαθμός: Μεσαίος (2NF, INNER JOINs)
│   ├── Practice_Exam_03_Intermediate.md# Βαθμός: Μεσητικός (ACID, Outer JOINs, FDs)
│   ├── Practice_Exam_04_Hard.md        # Βαθμός: Δυσκολος (3NF/BCNF, Correlated Subqueries)
│   ├── Practice_Exam_05_Advanced.md    # Βαθμός: Προχωρημένος (Indexes, Weak Entities, CASCADE)
│   ├── Practice_Exam_06_Image_Translation.md # Μετατροπή εικόνας σε διάγραμμα ER & σχέμα
│   ├── Practice_Exam_07_Topic_8_9.md    # Natural JOINs, Rainbow Tables, Social Engineering, Ασφάλεια
│   └── Practice_Exam_08_Topic_all_in_one_exam.md # Πλήρης ενότητα All-In-One Εξέταση
├── Synthetic_Finals/                   # Συγκεντρωτικές ψεύτικες τελικές εξετάσεις (15–20 Παραδείγματα)
│   └── (Synthetic_Exam_01.md ... Synthetic_Exam_20.md)
└── images/                             # Σχήματα ER και αποδείξεις υπερκεφαλίδας
    ├── Exam_paper_null_null_null.png   # Πρότυπο σελίδας τελικής εξέτασης
    └── hospital-er-diagram-1.png         # Λύση σχεδίου ER νοσοκομείου
```

---

## Κατάλογος Εξάσκησης

| Αρχείο Εξέτασης | Βαθμός Δύσκολης | Κύρια Θέματα |
| :--- | :--- | :--- |
| [Practice_Exam_01_Easy.md](file:///home/ice/Documents/CodeHub/GitHub-Projects/Public/DitOpenNotes/Year_2/Semester_4/DATABASES/Exams/Practice_Exams/Practice_Exam_01_Easy.md) | Εύκολο | DDL, Πρωτεύοντα Κλειδιά, Ξένα Κλειδιά, Απλός SELECT |
| [Practice_Exam_02_Medium.md](file:///home/ice/Documents/CodeHub/GitHub-Projects/Public/DitOpenNotes/Year_2/Semester_4/DATABASES/Exams/Practice_Exams/Practice_Exam_02_Medium.md) | Μεσαίος | 2NF Κανονικοποίηση, INNER JOINs, M:N Σχεδιασμός |
| [Practice_Exam_03_Intermediate.md](file:///home/ice/Documents/CodeHub/GitHub-Projects/Public/DitOpenNotes/Year_2/Semester_4/DATABASES/Exams/Practice_Exams/Practice_Exam_03_Intermediate.md) | Μεσητικός | ACID Ακμιοποίηση, LEFT JOINs, Κλειδιοποίηση Λειτουργικών Εξαρτήσεων |
| [Practice_Exam_04_Hard.md](file:///home/ice/Documents/CodeHub/GitHub-Projects/Public/DitOpenNotes/Year_2/Semester_4/DATABASES/Exams/Practice_Exams/Practice_Exam_04_Hard.md) | Δυσκολος | TRUNCATE vs DELETE, BCNF Αποσύνθεση, Correlated Subqueries |
| [Practice_Exam_05_Advanced.md](file:///home/ice/Documents/CodeHub/GitHub-Projects/Public/DitOpenNotes/Year_2/Semester_4/DATABASES/Exams/Practice_Exams/Practice_Exam_05_Advanced.md) | Προχωρημένος | Indexes, Weak Entities, M:N Junction Tables, CASCADE |
| [Practice_Exam_06_Image_Translation.md](file:///home/ice/Documents/CodeHub/GitHub-Projects/Public/DitOpenNotes/Year_2/Semester_4/DATABASES/Exams/Practice_Exams/Practice_Exam_06_Image_Translation.md) | Εξάχθηκε | Μετάφραση εξάσκησης, Mermaid διάγραμμα ER, σχέμα σχεσιακής δομής |
| [Practice_Exam_07_Topic_8_9.md](file:///home/ice/Documents/CodeHub/GitHub-Projects/Public/DitOpenNotes/Year_2/Semester_4/DATABASES/Exams/Practice_Exams/Practice_Exam_07_Topic_8_9.md) | Ειδικευμένος | Natural JOIN, Rainbow Tables, Social Engineering, Ασφάλεια |
| [Practice_Exam_08_Topic_all_in_one_exam.md](file:///home/ice/Documents/CodeHub/GitHub-Projects/Public/DitOpenNotes/Year_2/Semester_4/DATABASES/Exams/Practice_Exams/Practice_Exam_08_Topic_all_in_one_exam.md) | Πλήρης | Πλήρης ενότητα All-In-One (Μέρος Α: ER & Σχέμα, Μέρος Β: SQL & BCNF) |

---

## Συγκεντρωτικές Τελικές Εξετάσεις (15–20 Ψεύτικες Εξετάσεις)

Οι συγκεντρωτικές ψεύτικες εξετάσεις πρέπει να τοποθεταίονται στον φάκελο `Synthetic_Finals/` ακολουθώντας την ονομαστική συνθετεία `Synthetic_Exam_XX.md`. Κάθε συγκεντρωτική εξέταση ακολουθεί τη μορφή της τυπικής τελικής εξέτασης.

---

## Συγκέντρωση Όλων των Εξετάσεων

Για την ενοποίηση όλων των εξασκήσεων και των συγκεντρωτικών ψεύτικων εξετάσεων σε ένα ενιαίο ενιαίο αρχείο (`all_exams.md`), εκτελέστε το `combine_notes.py`:

```bash
python combine_notes.py
```