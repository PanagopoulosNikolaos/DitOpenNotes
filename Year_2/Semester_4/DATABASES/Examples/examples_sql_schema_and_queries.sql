-- ============================================================================
-- Course 404: Database Systems - Complete Schema Definition and Analytics Script
-- Dialect: SQLite 3 / ANSI SQL-92
-- ============================================================================

PRAGMA foreign_keys = ON;

-- Clean up any existing tables
DROP TABLE IF EXISTS enrollments;
DROP TABLE IF EXISTS courses;
DROP TABLE IF EXISTS instructors;
DROP TABLE IF EXISTS departments;

-- ----------------------------------------------------------------------------
-- 1. Schema Definitions (DDL)
-- ----------------------------------------------------------------------------

CREATE TABLE departments (
    dept_code VARCHAR(8) PRIMARY KEY,
    dept_name VARCHAR(60) NOT NULL UNIQUE,
    building VARCHAR(40) NOT NULL,
    annual_budget NUMERIC(12, 2) NOT NULL CHECK (annual_budget >= 10000.00)
);

CREATE TABLE instructors (
    instructor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(40) NOT NULL,
    last_name VARCHAR(40) NOT NULL,
    email VARCHAR(80) NOT NULL UNIQUE,
    salary NUMERIC(10, 2) NOT NULL CHECK (salary >= 20000.00),
    dept_code VARCHAR(8) NOT NULL,
    FOREIGN KEY (dept_code) REFERENCES departments(dept_code)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

CREATE TABLE courses (
    course_id VARCHAR(10) PRIMARY KEY,
    title VARCHAR(80) NOT NULL,
    credits INTEGER NOT NULL CHECK (credits BETWEEN 1 AND 6),
    dept_code VARCHAR(8) NOT NULL,
    instructor_id INTEGER,
    FOREIGN KEY (dept_code) REFERENCES departments(dept_code)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY (instructor_id) REFERENCES instructors(instructor_id)
        ON UPDATE CASCADE
        ON DELETE SET NULL
);

CREATE TABLE enrollments (
    student_id INTEGER NOT NULL,
    course_id VARCHAR(10) NOT NULL,
    semester VARCHAR(12) NOT NULL,
    grade NUMERIC(3, 1) CHECK (grade BETWEEN 0.0 AND 10.0),
    PRIMARY KEY (student_id, course_id, semester),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

-- ----------------------------------------------------------------------------
-- 2. Data Population (DML)
-- ----------------------------------------------------------------------------

INSERT INTO departments (dept_code, dept_name, building, annual_budget) VALUES
    ('CS', 'Computer Science', 'Turing Hall', 1500000.00),
    ('MATH', 'Mathematics', 'Euler Building', 950000.00),
    ('PHYS', 'Physics', 'Newton Lab', 800000.00);

INSERT INTO instructors (first_name, last_name, email, salary, dept_code) VALUES
    ('Grace', 'Hopper', 'g.hopper@dit.gr', 92000.00, 'CS'),
    ('Donald', 'Knuth', 'd.knuth@dit.gr', 98000.00, 'CS'),
    ('Carl', 'Gauss', 'c.gauss@dit.gr', 91000.00, 'MATH'),
    ('Richard', 'Feynman', 'r.feynman@dit.gr', 89000.00, 'PHYS');

INSERT INTO courses (course_id, title, credits, dept_code, instructor_id) VALUES
    ('CS101', 'Intro to Programming', 4, 'CS', 1),
    ('CS202', 'Data Structures', 5, 'CS', 2),
    ('CS404', 'Database Systems', 5, 'CS', 1),
    ('MATH101', 'Calculus I', 4, 'MATH', 3),
    ('PHYS101', 'Classical Mechanics', 4, 'PHYS', 4);

INSERT INTO enrollments (student_id, course_id, semester, grade) VALUES
    (1001, 'CS101', 'Fall2025', 9.5),
    (1001, 'CS202', 'Spring2026', 8.5),
    (1001, 'CS404', 'Fall2026', 9.0),
    (1002, 'CS101', 'Fall2025', 7.0),
    (1002, 'MATH101', 'Fall2025', 8.0),
    (1003, 'CS404', 'Fall2026', 6.5),
    (1003, 'PHYS101', 'Spring2026', 7.5);

-- ----------------------------------------------------------------------------
-- 3. Complex Analytic Queries (DQL)
-- ----------------------------------------------------------------------------

-- Query 1: Department budget and instructor compensation metrics
SELECT d.dept_name,
       COUNT(i.instructor_id) AS total_instructors,
       ROUND(AVG(i.salary), 2) AS average_salary,
       ROUND(SUM(i.salary), 2) AS total_payroll
FROM departments d
LEFT JOIN instructors i ON d.dept_code = i.dept_code
GROUP BY d.dept_code, d.dept_name
ORDER BY average_salary DESC;

-- Query 2: Course enrollment breakdown and grade metrics
SELECT c.course_id,
       c.title,
       i.last_name AS instructor_surname,
       COUNT(e.student_id) AS total_students,
       ROUND(AVG(e.grade), 2) AS average_course_grade
FROM courses c
LEFT JOIN instructors i ON c.instructor_id = i.instructor_id
LEFT JOIN enrollments e ON c.course_id = e.course_id
GROUP BY c.course_id, c.title, i.last_name;

-- Query 3: Window function ranking courses by enrollment
SELECT course_id,
       title,
       credits,
       dept_code,
       DENSE_RANK() OVER (PARTITION BY dept_code ORDER BY credits DESC) AS credit_rank
FROM courses;

