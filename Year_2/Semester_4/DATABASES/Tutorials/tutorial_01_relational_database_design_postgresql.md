# Εργαστηριακός Οδηγός 1: Σχεδίαση και Δημιουργία Σχεσιακής Βάσης σε PostgreSQL

## 1. Σκοπός Εργαστηρίου
Εγκατάσταση, σύνδεση και υλοποίηση σχεσιακού σχήματος σε περιβάλλον PostgreSQL / psql. Εφαρμογή περιορισμών ακεραιότητας (`PRIMARY KEY`, `FOREIGN KEY`, `CHECK`, `NOT NULL`, `UNIQUE`).

---

## 2. Σύνδεση στο Περιβάλλον psql
```bash
sudo -u postgres psql
CREATE DATABASE university_db;
\c university_db
```

---

## 3. Δημιουργία Πινάκων και Περιορισμών
```sql
CREATE TABLE Departments (
    dept_id SERIAL PRIMARY KEY,
    dept_name VARCHAR(100) NOT NULL UNIQUE,
    building VARCHAR(50)
);

CREATE TABLE Students (
    student_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    enrollment_year INT CHECK (enrollment_year >= 2000),
    dept_id INT REFERENCES Departments(dept_id) ON DELETE CASCADE
);

CREATE TABLE Courses (
    course_id VARCHAR(10) PRIMARY KEY,
    title VARCHAR(120) NOT NULL,
    credits INT CHECK (credits > 0),
    dept_id INT REFERENCES Departments(dept_id) ON DELETE RESTRICT
);

CREATE TABLE Enrollments (
    student_id INT REFERENCES Students(student_id) ON DELETE CASCADE,
    course_id VARCHAR(10) REFERENCES Courses(course_id) ON DELETE CASCADE,
    grade NUMERIC(4, 2) CHECK (grade >= 0.0 AND grade <= 10.0),
    PRIMARY KEY (student_id, course_id)
);
```

---

## 4. Εισαγωγή Δοκιμαστικών Δεδομένων
```sql
INSERT INTO Departments (dept_name, building) VALUES
('Informatics', 'Building A'),
('Telecommunications', 'Building B');

INSERT INTO Students (first_name, last_name, email, enrollment_year, dept_id) VALUES
('Kostas', 'Georgiou', 'kostas@uop.gr', 2022, 1),
('Eleni', 'Dimitriou', 'eleni@uop.gr', 2023, 1),
('Alexandros', 'Nikolaou', 'alex@uop.gr', 2021, 2);

INSERT INTO Courses (course_id, title, credits, dept_id) VALUES
('CS101', 'Introduction to CS', 5, 1),
('CS202', 'Data Structures', 6, 1),
('TC101', 'Signals and Systems', 5, 2);

INSERT INTO Enrollments (student_id, course_id, grade) VALUES
(1, 'CS101', 8.5),
(1, 'CS202', 9.0),
(2, 'CS101', 7.0),
(3, 'TC101', 6.5);
```

