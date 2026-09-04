# Tutorial 01: SQLite Database Setup and DDL Schema Execution

This practical laboratory tutorial guides students through setting up an embedded relational database using the SQLite command-line shell, declaring relational tables, enforcing domain integrity constraints, and activating foreign key checks.

---

## 1. Initializing SQLite Command-Line Shell

SQLite stores an entire relational database in a single cross-platform disk file.

### 1.1 Creating or Opening a Database File
In the Linux terminal, launch `sqlite3` targeting a database file named `university.db`:

```bash
sqlite3 university.db
```

### 1.2 Essential Dot-Commands
Inside the SQLite interactive prompt:

```text
-- Enable foreign key constraint validation (disabled by default in SQLite)
sqlite> PRAGMA foreign_keys = ON;

-- Configure tabular output mode for readable queries
sqlite> .mode box
sqlite> .headers on

-- Display active tables
sqlite> .tables

-- Display table creation schema
sqlite> .schema
```

---

## 2. Defining Schema Tables with DDL

Execute the following DDL statements to build a university database schema:

```sql
-- Departments table
CREATE TABLE departments (
    dept_code VARCHAR(10) PRIMARY KEY,
    dept_name VARCHAR(100) NOT NULL UNIQUE,
    building VARCHAR(50) NOT NULL,
    annual_budget NUMERIC(12, 2) NOT NULL CHECK (annual_budget > 0)
);

-- Instructors table
CREATE TABLE instructors (
    instructor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    salary NUMERIC(10, 2) NOT NULL CHECK (salary >= 25000.00),
    dept_code VARCHAR(10) NOT NULL,
    FOREIGN KEY (dept_code) REFERENCES departments(dept_code)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

-- Courses table
CREATE TABLE courses (
    course_id VARCHAR(10) PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    credits INTEGER NOT NULL CHECK (credits BETWEEN 1 AND 6),
    dept_code VARCHAR(10) NOT NULL,
    FOREIGN KEY (dept_code) REFERENCES departments(dept_code)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);
```

---

## 3. Verifying Integrity Constraints

### 3.1 Valid Record Insertion

```sql
INSERT INTO departments (dept_code, dept_name, building, annual_budget)
VALUES ('CS', 'Computer Science', 'Turing Hall', 1200000.00);

INSERT INTO instructors (first_name, last_name, email, salary, dept_code)
VALUES ('Alan', 'Turing', 'a.turing@dit.gr', 85000.00, 'CS');
```

### 3.2 Testing Check Constraint Violation

```sql
-- Attempt inserting instructor with salary below the check constraint threshold (25000)
INSERT INTO instructors (first_name, last_name, email, salary, dept_code)
VALUES ('John', 'Doe', 'j.doe@dit.gr', 15000.00, 'CS');
```

**Expected SQLite Output:**
```text
Runtime error: CHECK constraint failed: salary >= 25000.00 (19)
```

### 3.3 Testing Foreign Key Referential Integrity

```sql
-- Attempt referencing a non-existent department code
INSERT INTO courses (course_id, title, credits, dept_code)
VALUES ('MATH101', 'Calculus I', 4, 'MATH');
```

**Expected SQLite Output:**
```text
Runtime error: FOREIGN KEY constraint failed (19)
```

