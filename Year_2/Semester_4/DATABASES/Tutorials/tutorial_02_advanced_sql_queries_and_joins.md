# Εργαστηριακός Οδηγός 2: Προχωρημένα Ερωτήματα SQL, Συνενώσεις και Όψεις (Views)

## 1. Σκοπός Εργαστηρίου
Εξάσκηση σε σύνθετες συνενώσεις (`INNER JOIN`, `LEFT OUTER JOIN`, `FULL OUTER JOIN`), υποερωτήματα (`EXISTS`, `IN`, `ALL`, `ANY`) και δημιουργία όψεων (`VIEWS`).

---

## 2. Είδη Συνενώσεων (Joins)

### Εσωτερική Συνένωση (INNER JOIN)
Επιστρέφει μόνο τις εγγραφές που έχουν ταίριασμα και στους δύο πίνακες:
```sql
SELECT S.first_name, S.last_name, C.title, E.grade
FROM Students S
INNER JOIN Enrollments E ON S.student_id = E.student_id
INNER JOIN Courses C ON E.course_id = C.course_id;
```

### Αριστερή Εξωτερική Συνένωση (LEFT OUTER JOIN)
Επιστρέφει όλους τους φοιτητές, ακόμη και αν δεν έχουν εγγραφεί σε κανένα μάθημα:
```sql
SELECT S.student_id, S.last_name, COUNT(E.course_id) AS enrolled_courses
FROM Students S
LEFT JOIN Enrollments E ON S.student_id = E.student_id
GROUP BY S.student_id, S.last_name;
```

---

## 3. Συσχετισμένα Υποερωτήματα (Correlated Subqueries)
Εύρεση φοιτητών που έχουν βαθμό ανώτερο από τον μέσο όρο του εκάστοτε μαθήματος:
```sql
SELECT S.first_name, S.last_name, E.course_id, E.grade
FROM Students S
JOIN Enrollments E ON S.student_id = E.student_id
WHERE E.grade > (
    SELECT AVG(E2.grade)
    FROM Enrollments E2
    WHERE E2.course_id = E.course_id
);
```

---

## 4. Δημιουργία και Χρήση Όψεων (Views)
Δημιουργία ασφαλούς όψης για την εμφάνιση ακαδημαϊκής προόδου ανά φοιτητή:
```sql
CREATE VIEW Student_Performance_Summary AS
SELECT 
    S.student_id,
    S.first_name || ' ' || S.last_name AS full_name,
    D.dept_name,
    COUNT(E.course_id) AS total_courses,
    ROUND(AVG(E.grade), 2) AS gpa
FROM Students S
JOIN Departments D ON S.dept_id = D.dept_id
LEFT JOIN Enrollments E ON S.student_id = E.student_id
GROUP BY S.student_id, full_name, D.dept_name;

-- Χρήση της όψης
SELECT * FROM Student_Performance_Summary WHERE gpa >= 8.5;
```

