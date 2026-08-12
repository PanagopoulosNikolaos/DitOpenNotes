# Exam 2: Relational Theory & Basic SQL (Level: Medium)

Multiple Choice Question 1: Which normalization form requires the elimination of partial dependencies?
[ ] 1. 1NF
[✅] 2. 2NF
[ ] 3. 3NF
[ ] 4. BCNF
---
*solution:*
The Second Normal Form (2NF) states that a table must be in 1NF and all non-key attributes must depend fully on the primary key, eliminating partial dependencies.
---

Multiple Choice Question 2: Which type of JOIN returns only the records that have a match in both tables?
[✅] 1. INNER JOIN
[ ] 2. LEFT JOIN
[ ] 3. RIGHT JOIN
[ ] 4. FULL OUTER JOIN
---
*solution:*
The INNER JOIN combines the tables keeping only the rows that satisfy the join condition.
---

Exercise 3: Given the tables Course(course_id, title) and Student(student_id, name). The relationship between students and courses is many-to-many (M:N). Show the relational transformation into SQL CREATE TABLE commands.
---
*solution:*
In many-to-many relationships an intermediate table is created.
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

Exercise 4: Based on the schema of Exercise 3, write an SQL query that returns the number of students enrolled in each course (displaying the course_id and the count).
---
*solution:*
```sql
SELECT course_id, COUNT(student_id) AS student_count
FROM Enrollment
GROUP BY course_id;
```
---
