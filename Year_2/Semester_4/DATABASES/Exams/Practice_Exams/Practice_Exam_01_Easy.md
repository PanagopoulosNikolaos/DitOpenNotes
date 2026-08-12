# Exam 1: Basic Database Concepts (Level: Easy)

Multiple Choice Question 1: Which of the following commands belongs to the Data Definition Language (DDL)?
[ ] 1. SELECT
[ ] 2. INSERT
[✅] 3. CREATE TABLE
[ ] 4. UPDATE
---
*solution:*
The CREATE TABLE command is used to define the database schema and belongs to the DDL. The remaining commands belong to the Data Manipulation Language (DML).
---

Multiple Choice Question 2: Which of the following ensures the uniqueness of a record in a table?
[✅] 1. Primary Key
[ ] 2. Foreign Key
[ ] 3. Index
[ ] 4. All of the above
---
*solution:*
The Primary Key is used to uniquely identify each record in a table, while the Foreign Key is used for interconnecting tables.
---

Exercise 3: Given the relations "Student" and "Department". A student belongs to exactly one department, while a department has many students. Write the SQL commands (CREATE TABLE) to create the two tables, including the foreign key.
---
*solution:*
```sql
CREATE TABLE Department (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(100) NOT NULL
);

CREATE TABLE Student (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES Department(dept_id)
);
```
---

Exercise 4: Write an SQL query that returns the names of the students (from the Student table) who belong to the department with dept_id equal to 5.
---
*solution:*
```sql
SELECT student_name
FROM Student
WHERE dept_id = 5;
```
---
