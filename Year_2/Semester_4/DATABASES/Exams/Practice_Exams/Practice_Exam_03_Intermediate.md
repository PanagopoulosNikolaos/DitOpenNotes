# Exam 3: Intermediate Database Concepts (Level: Intermediate)

Multiple Choice Question 1: Which of the following transaction (ACID) properties guarantees that a transaction is executed completely or not at all?
[✅] 1. Atomicity
[ ] 2. Consistency
[ ] 3. Isolation
[ ] 4. Durability
---
*solution:*
Atomicity ensures that all the operations of a transaction complete successfully; otherwise the database returns to its initial state (Rollback).
---

Multiple Choice Question 2: The LEFT OUTER JOIN operation between table A (left) and B (right) will return:
[ ] 1. Only the common records.
[✅] 2. All the records of A and the matching ones from B (where there is no match, it inserts NULL).
[ ] 3. All the records of B and the matching ones from A.
[ ] 4. All the records of both tables regardless of matching.
---
*solution:*
The LEFT OUTER JOIN keeps all the tuples of the left relation. If there is no match in the right relation, its columns are filled with NULL.
---

Exercise 3: Given the relation R(A, B, C, D) and the functional dependencies: F = {A -> B, B -> C, C -> D}. Find the candidate key of the relation R.
---
*solution:*
We examine the closure of attribute A:
A+ = {A} (based on reflexivity)
A+ = {A, B} (due to A -> B)
A+ = {A, B, C} (due to B -> C)
A+ = {A, B, C, D} (due to C -> D)
Since A determines all the attributes of the relation, {A} is the candidate key.
---

Exercise 4: Write an SQL query that finds the names of the departments (Department table) that have no students (Student table), using a LEFT JOIN or a subquery.
---
*solution:*
```sql
SELECT d.dept_name
FROM Department d
LEFT JOIN Student s ON d.dept_id = s.dept_id
WHERE s.student_id IS NULL;
```
Alternatively, using a subquery:
```sql
SELECT dept_name
FROM Department
WHERE dept_id NOT IN (SELECT dept_id FROM Student);
```
---
