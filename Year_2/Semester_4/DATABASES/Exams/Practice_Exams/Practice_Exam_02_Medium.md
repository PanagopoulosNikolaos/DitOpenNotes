# Εξέταση 2: Σχεσιακή Θεωρία & Βασικό SQL (Βαθμός: Μεσαίος)

Ερώτηση Πολλαπλής Επιλογής 1, Ποια μορφή κανονικοποίησης απαιτεί την εξάλειψη των μερικών εξαρτήσεων (partial dependencies);
[ ] 1. 1NF
[✅] 2. 2NF
[ ] 3. 3NF
[ ] 4. BCNF
---
*solution:*
Η Δεύτερη Κανονική Μορφή (2NF) ορίζει ότι ένας πίνακας πρέπει να είναι σε 1NF και όλα τα μη-κλειδιά γνωρίσματα να εξαρτώνται πλήρως από το πρωτεύον κλειδί, εξαλείφοντας τις μερικές εξαρτήσεις.
---

Ερώτηση Πολλαπλής Επιλογής 2, Ποιο είδος JOIN επιστρέφει μόνο τις εγγραφές που έχουν αντιστοιχία και στους δύο πίνακες;
[✅] 1. INNER JOIN
[ ] 2. LEFT JOIN
[ ] 3. RIGHT JOIN
[ ] 4. FULL OUTER JOIN
---
*solution:*
Το INNER JOIN συνενώνει τους πίνακες διατηρώντας μόνο τις γραμμές που ικανοποιούν τη συνθήκη ένωσης.
---

Άσκηση 3, Έστω οι πίνακες Course(course_id, title) και Student(student_id, name). Η σχέση μεταξύ φοιτητών και μαθημάτων είναι πολλά-προς-πολλά (M:N). Δείξτε τον σχεσιακό μετασχηματισμό σε SQL CREATE TABLE εντολές.
---
*solution:*
Σε σχέσεις πολλά-προς-πολλά δημιουργείται ένας ενδιάμεσος πίνακας.
```sql
CREATE TABLE Course (
    course_id INT PRIMARY KEY,
    title VARCHAR(100) NOT NULL
);

CREATE TABLE Student (
    student_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE Enrollment (
    student_id INT,
    course_id INT,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (course_id) REFERENCES Course(course_id)
);
```
---

Άσκηση 4, Βάσει του σχήματος της Άσκησης 3, γράψτε ερώτημα SQL που επιστρέφει το πλήθος των φοιτητών που έχουν εγγραφεί σε κάθε μάθημα (να εμφανίζεται το course_id και το πλήθος).
---
*solution:*
```sql
SELECT course_id, COUNT(student_id) AS student_count
FROM Enrollment
GROUP BY course_id;
```
---
