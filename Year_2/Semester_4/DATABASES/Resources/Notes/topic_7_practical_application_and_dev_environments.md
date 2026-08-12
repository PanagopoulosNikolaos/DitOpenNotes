# Practical Application & Development Environments
*Practical Application & Development Environments*

---

## Table of Contents
*Table of Contents*

1. [Introduction](#introduction)
2. [Tools, Systems & Architecture](#tools-systems--architecture)
   - [MySQL Server](#mysql-server)
   - [MySQL Workbench](#mysql-workbench)
   - [XAMPP & phpMyAdmin](#xampp--phpmyadmin)
   - [Comparative Table: Management Tools](#comparative-table-management-tools)
3. [Implementation in Real-World Conditions](#implementation-in-real-world-conditions)
   - [Determining Appropriate Data Types](#determining-appropriate-data-types)
   - [Implementing Constraints (NOT NULL, UNIQUE, DEFAULT)](#implementing-constraints-not-null-unique-default)
   - [Connecting Tables via Foreign Keys (FOREIGN KEY ... REFERENCES)](#connecting-tables-via-foreign-keys-foreign-key--references)
   - [Managing "Many-to-Many" Relationships (Junction Table)](#managing-many-to-many-relationships-junction-table)
4. [Summary Table of Key Concepts](#summary-table-of-key-concepts)
5. [Key Takeaways](#key-takeaways)

---

## Introduction

The theoretical knowledge of data models, Relational Algebra, and SQL gains full value only when applied to real software. In the context of this course, the dominant implementation system is **MySQL** — one of the most widely used open-source **Relational Database Management Systems (RDBMS)** worldwide. This practical section covers both the **tools** (MySQL Server, MySQL Workbench, XAMPP, phpMyAdmin) and the **design decisions** the database administrator makes during implementation: choosing data types, defining constraints, declaring Foreign Keys, and handling N:M relationships through junction tables. The ability to translate an ER diagram or a Relational Schema into a functional MySQL database is a fundamental skill for every software engineer.

---

## Tools, Systems & Architecture
*Tools, Systems & Architecture*

The architecture of a MySQL system is based on the **client-server** model: the **MySQL Server** runs in the background as a service (service/daemon) that manages the data, while various **client tools** connect to it to run queries and administrative tasks.

```text
  MySQL Client-Server Architecture:

  +---------------------+        TCP/IP or Socket      +---------------------+
  |     CLIENT TOOLS    |  <-------------------------->  |    MySQL Server     |
  +---------------------+                               +---------------------+
  |  mysql CLI          |                               |  - Query Engine     |
  |  MySQL Workbench    |                               |  - Storage Engine   |
  |  phpMyAdmin         |                               |    (InnoDB)         |
  |  Application (PHP/  |                               |  - Buffer Pool      |
  |  Python/Java)       |                               |  - Log Files        |
  +---------------------+                               +---------------------+
                                                               |
                                                        +------+------+
                                                        |  Data      |
                                                        |  (Disk     |
                                                        |  Files)    |
                                                        +------------+
```

---

### MySQL Server
*The Backend Database Management System*

The **MySQL Server** is the core (backend) of the system — the process that **stores, organizes, and serves** the data. It runs continuously as a **service** of the operating system and listens for incoming connections from clients (by default on port **3306**). It has no graphical interface — interaction takes place through SQL statements sent by a client.

**Main features:**
- Supports multiple concurrent users (**Concurrency**) through transaction management.
- Primarily uses the **InnoDB Storage Engine**, which supports Foreign Keys, Transactions, and ACID guarantees.
- Manages access rights (**privileges**) per user and per database.

**Connecting via the command line (mysql CLI):**

```sql
-- Connecting as root user to the local MySQL Server
mysql -u root -p

-- After connecting, display the available databases
SHOW DATABASES;
```

```text
  mysql> SHOW DATABASES;
  +--------------------+
  | Database           |
  +--------------------+
  | information_schema |
  | mysql              |
  | performance_schema |
  | sys                |
  | university_db      |
  +--------------------+
  5 rows in set (0.00 sec)
```

**Exam Note:** The databases `information_schema`, `mysql`, `performance_schema`, and `sys` are **system databases** created automatically by the MySQL Server. They must never be modified manually.

---

### MySQL Workbench
*Graphical Database Management Environment / GUI Client*

**MySQL Workbench** is the official **graphical environment (GUI)** provided by Oracle for managing MySQL Server. It combines in a single tool:
- **SQL Editor**: Writing and executing SQL queries with syntax highlighting and autocompletion.
- **Visual Schema Designer (EER Diagram)**: Visual design and modification of database schemas — creating tables, defining relationships with drag-and-drop.
- **Server Administration**: Managing users, privileges, server status, and log files.
- **Data Export / Import**: Importing and exporting data in SQL dump, CSV, and other formats.

```text
  MySQL Workbench — Work Areas:

  +-----------------------------------------------------------+
  |                    MySQL Workbench                        |
  +------------------+----------------------------------------+
  |  Navigator       |                                        |
  |  +------------+  |   +--------------------------------+  |
  |  | Schemas    |  |   |       SQL Editor               |  |
  |  | - uni_db   |  |   |  SELECT * FROM Foititis;       |  |
  |  |   Tables   |  |   |  > Execute (Ctrl+Enter)        |  |
  |  |   Views    |  |   +--------------------------------+  |
  |  |   Procs    |  |   |       Result Grid              |  |
  |  +------------+  |   |  am | onoma | eponymo | ...    |  |
  |                  |   +--------------------------------+  |
  +------------------+----------------------------------------+
```

**Analogy**: MySQL Workbench is like an **airplane cockpit** — it provides all the information and controls in a graphical environment, while the MySQL Server is the engines that actually do the work.

---

### XAMPP & phpMyAdmin
*Web-Based Management Package and Services*

**XAMPP** (X = Cross-platform, A = Apache, M = MariaDB/MySQL, P = PHP, P = Perl) is an **installation package** that bundles in one installer:
- **Apache HTTP Server**: Web server for serving PHP applications.
- **MySQL / MariaDB**: Relational database server.
- **PHP**: Server-side scripting language.
- **phpMyAdmin**: Web-based tool for managing MySQL through a browser.

**phpMyAdmin** is a PHP application that runs on Apache and provides **full MySQL management through a web browser**, without installing additional software. It is ideal for web hosting environments where there is no direct CLI access.

```text
  XAMPP Stack — Architecture:

  Browser (Client)
       |
       | HTTP Request (e.g., http://localhost/phpmyadmin)
       v
  +--------------------+
  |   Apache Server    |  <-- Runs PHP scripts
  +--------------------+
       |
       | MySQL Protocol (port 3306)
       v
  +--------------------+
  |  MySQL / MariaDB   |  <-- Stores the data
  +--------------------+

  phpMyAdmin is a set of PHP files on Apache
  that act as a web-based MySQL client.
```

**Key Distinction:** XAMPP is often used for **local development (localhost)** of web applications, while in a production environment the components (Apache, MySQL, PHP) are installed and configured separately for security and performance reasons.

---

### Comparative Table: Management Tools
*Comparative Table: Management Tools*

| Characteristic | MySQL Server (CLI) | MySQL Workbench | phpMyAdmin |
|---|---|---|---|
| **Type** | CLI / Backend Service | Desktop GUI Client | Web-based GUI Client |
| **Interface** | Command line | Graphical (Desktop App) | Browser |
| **Installation** | Only | Separately (requires Server) | Part of XAMPP or standalone |
| **ER design** | No | Yes (Visual EER Designer) | Limited |
| **Suitable for** | Scripting, automation | Development, design | Web hosting, quick access |
| **Requires PHP/Apache** | No | No | Yes |
| **Import/Export** | mysqldump CLI | Yes (GUI) | Yes (GUI) |

---

## Implementation in Real-World Conditions
*Implementation in Real-World Conditions*

Implementing a Relational Schema in MySQL requires, beyond knowledge of SQL syntax, a series of **design decisions** that affect the integrity, performance, and maintainability of the database. The critical decisions concern: which **data type** fits each field, which **constraints** ensure data quality, and how the **relationships** between tables are implemented.

---

### Determining Appropriate Data Types
*Determining Appropriate Data Types*

The **data type** of each column defines the **kind and range of values** it can store. Choosing the correct type is critical: a type that is too large wastes storage space, while one that is too small may not fit the data and can cause an error or loss of information.

**Main categories of MySQL data types:**

| Category | Type | Storage / Range | Typical Use |
|---|---|---|---|
| **Integers** | `TINYINT` | 1 byte, -128 to 127 (or 0-255 UNSIGNED) | Boolean flags, small categories |
| | `SMALLINT` | 2 bytes, -32,768 to 32,767 | Small numbers |
| | `INT` / `INTEGER` | 4 bytes, ~-2.1 billion to 2.1 billion | IDs, quantities, counts |
| | `BIGINT` | 8 bytes, ~-9.2 · 10¹⁸ to 9.2 · 10¹⁸ | Very large numbers, timestamps |
| **Decimals** | `FLOAT` | 4 bytes | Approximate decimals |
| | `DOUBLE` | 8 bytes | Scientific calculations |
| | `DECIMAL(M,D)` | Variable | Monetary amounts (exact representation) |
| **Text** | `CHAR(N)` | Fixed N bytes (1-255) | Fixed-length codes (e.g., country ISO) |
| | `VARCHAR(N)` | Variable, up to N bytes (1-65535) | Names, emails, titles |
| | `TEXT` | Up to 65,535 bytes | Large texts (descriptions, comments) |
| **Date/Time** | `DATE` | 3 bytes, `YYYY-MM-DD` | Birth date, start date |
| | `DATETIME` | 8 bytes, `YYYY-MM-DD HH:MM:SS` | Event timestamp |
| | `TIMESTAMP` | 4 bytes, automatic UTC update | Last record modification |
| | `TIME` | 3 bytes, `HH:MM:SS` | Duration, schedule |
| **Boolean** | `BOOLEAN` / `TINYINT(1)` | 1 byte (0 = FALSE, 1 = TRUE) | Status flags |

**Example — Creating table `Foititis` with selected types:**

```sql
CREATE TABLE Foititis (
    -- INT: integer Registration Number, up to ~2 billion
    am           INT            NOT NULL,
    -- VARCHAR(50): variable-length text, up to 50 characters
    onoma        VARCHAR(50)    NOT NULL,
    eponymo      VARCHAR(50)    NOT NULL,
    -- VARCHAR(100): email may be longer
    email        VARCHAR(100),
    -- DATE: stores only the date without time
    hmerominia   DATE,
    -- INT: Foreign Key to dept_id of the Tmima table
    dept_id      INT            NOT NULL,
    PRIMARY KEY (am)
);
```

**Comparison of `CHAR` vs `VARCHAR`:**

| Characteristic | `CHAR(N)` | `VARCHAR(N)` |
|---|---|---|
| **Storage length** | Always N bytes (padded with spaces) | Actual length + 1-2 bytes overhead |
| **Performance** | Faster for fixed length | More efficient for variable length |
| **Suitable for** | Country codes (`GR`, `US`), tax ID | Names, emails, addresses |

**Exam Note:** For monetary amounts, `FLOAT` or `DOUBLE` is **never** used because of floating-point rounding errors. `DECIMAL(10, 2)` (e.g., 10 digits in total, 2 decimal places) is used for exact representation.

---

### Implementing Constraints (NOT NULL, UNIQUE, DEFAULT)
*Implementing Constraints*

**Constraints** are rules that MySQL enforces automatically on every `INSERT` or `UPDATE`, ensuring **data integrity**. They are defined at creation time (`CREATE TABLE`) or added later (`ALTER TABLE`).

**Main constraints:**

| Constraint | Purpose | Violation |
|---|---|---|
| `NOT NULL` | Prohibits NULL values in a column | `ERROR 1048: Column cannot be null` |
| `UNIQUE` | Ensures uniqueness of values (NULL allowed) | `ERROR 1062: Duplicate entry` |
| `DEFAULT value` | Sets a default value if none is given | — (does not cause an error) |
| `PRIMARY KEY` | `NOT NULL` + `UNIQUE` + index | `ERROR 1062` or `ERROR 1048` |
| `CHECK (expr)` | Verifies a logical condition (MySQL 8.0.16+) | `ERROR 3819: Check constraint violated` |

**Example — Table `Mathima` with multiple constraints:**

```sql
CREATE TABLE Mathima (
    -- PRIMARY KEY: NOT NULL + UNIQUE automatically
    mathima_id   INT           NOT NULL AUTO_INCREMENT,
    -- NOT NULL: the title is mandatory
    titlos       VARCHAR(100)  NOT NULL,
    -- UNIQUE: the course code must be unique
    kodikos      VARCHAR(10)   NOT NULL UNIQUE,
    -- DEFAULT: if no ECTS credits are given, they are considered 5
    ects         TINYINT       NOT NULL DEFAULT 5,
    -- NULL allowed: the description is optional
    perigrafi    TEXT,
    -- CHECK: the ECTS credits must be between 1 and 30
    CONSTRAINT chk_ects CHECK (ects BETWEEN 1 AND 30),
    PRIMARY KEY (mathima_id)
);
```

**Demonstration of constraint behavior:**

**Before:**
```text
  mysql> SELECT * FROM Mathima;
  Empty set (0.00 sec)
```

**Successful insertion (with DEFAULT):**
```sql
-- No value is given for ects - it receives DEFAULT 5
INSERT INTO Mathima (titlos, kodikos)
VALUES ('Databases', 'CS301');
```

**After:**
```text
  mysql> SELECT * FROM Mathima;
  +------------+------------------+---------+------+-----------+
  | mathima_id | titlos           | kodikos | ects | perigrafi |
  +------------+------------------+---------+------+-----------+
  |          1 | Databases        | CS301   |    5 | NULL      |
  +------------+------------------+---------+------+-----------+
```

**NOT NULL violation:**
```sql
-- No value is given for titlos (NOT NULL) - error
INSERT INTO Mathima (kodikos) VALUES ('CS302');
-- ERROR 1364 (HY000): Field 'titlos' doesn't have a default value
```

**UNIQUE violation:**
```sql
-- The code 'CS301' already exists - UNIQUE violation
INSERT INTO Mathima (titlos, kodikos)
VALUES ('Another Course', 'CS301');
-- ERROR 1062 (23000): Duplicate entry 'CS301' for key 'mathima.kodikos'
```

**CHECK violation:**
```sql
-- ects = 50 exceeds the CHECK constraint (1-30)
INSERT INTO Mathima (titlos, kodikos, ects)
VALUES ('Test Course', 'CS399', 50);
-- ERROR 3819 (HY000): Check constraint 'chk_ects' is violated.
```

**Key Distinction:** The `UNIQUE` constraint allows **multiple NULL values** in the same column (NULL is not considered equal to any value, nor to another NULL). In contrast, `PRIMARY KEY` **does not allow** any NULL value.

---

### Connecting Tables via Foreign Keys (FOREIGN KEY ... REFERENCES)
*Connecting Tables via Foreign Keys*

The **Foreign Key** is the mechanism by which MySQL enforces **Referential Integrity** between two tables. It ensures that every value in the FK column of the **child table** corresponds to an existing value in the **parent table**.

**Referential Integrity rules:**
- No record can be inserted into the child with an FK value that does not exist in the parent.
- No record can be deleted from the parent if child records reference it.

**FOREIGN KEY declaration syntax:**

```sql
-- Inline definition (for simple FKs)
CREATE TABLE child_table (
    fk_column   INT,
    FOREIGN KEY (fk_column) REFERENCES parent_table (pk_column)
);

-- Definition with a constraint name (recommended - more readable)
CREATE TABLE child_table (
    fk_column   INT,
    CONSTRAINT fk_child_parent
        FOREIGN KEY (fk_column)
        REFERENCES parent_table (pk_column)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);
```

**Example — Relationship `Foititis` → `Tmima` (N:1):**

```text
  Relational Schema:
  Tmima(<u>dept_id</u>, onoma_tmimatos, sxoli)
  Foititis(<u>am</u>, onoma, eponymo, email, hmerominia, #dept_id)

  ER Representation:
  +-------------+            1:N           +------------+
  |    TMIMA    |  <>---( Belongs to )---<  |  FOITITIS  |
  +-------------+                          +------------+
  | dept_id(PK) |                          | am (PK)    |
  | onoma_tmim. |                          | onoma      |
  | sxoli       |                          | eponymo    |
  +-------------+                          | dept_id(FK)|
                                           +------------+
```

**Creating tables with a FOREIGN KEY:**

```sql
-- Step 1: First the parent table
CREATE TABLE Tmima (
    dept_id        INT          NOT NULL AUTO_INCREMENT,
    onoma_tmimatos VARCHAR(100) NOT NULL,
    sxoli          VARCHAR(100) NOT NULL,
    PRIMARY KEY (dept_id)
);

-- Step 2: Then the child table with FK
CREATE TABLE Foititis (
    am           INT          NOT NULL,
    onoma        VARCHAR(50)  NOT NULL,
    eponymo      VARCHAR(50)  NOT NULL,
    email        VARCHAR(100) UNIQUE,
    hmerominia   DATE,
    dept_id      INT          NOT NULL,
    PRIMARY KEY (am),
    -- Defining the Foreign Key with an explicit constraint name
    CONSTRAINT fk_foititis_tmima
        FOREIGN KEY (dept_id)
        REFERENCES Tmima (dept_id)
        ON DELETE RESTRICT   -- Prevents deleting a department with students
        ON UPDATE CASCADE    -- If dept_id changes in Tmima, it is updated automatically
);
```

**Demonstration of Referential Integrity:**

**Inserting data:**
```sql
-- Inserting departments into the parent
INSERT INTO Tmima (onoma_tmimatos, sxoli)
VALUES ('Informatics', 'Sciences'),
       ('Mathematics',  'Sciences');
```

```text
  Tmima:
  +---------+-------------------+-------------------+
  | dept_id | onoma_tmimatos    | sxoli             |
  +---------+-------------------+-------------------+
  |       1 | Informatics      | Sciences         |
  |       2 | Mathematics      | Sciences         |
  +---------+-------------------+-------------------+
```

```sql
-- Successful insertion: dept_id=1 exists in Tmima
INSERT INTO Foititis (am, onoma, eponymo, dept_id)
VALUES (10001, 'Alexis', 'Nikolopoulos', 1);
```

**FK violation — insertion with a non-existent dept_id:**
```sql
-- FAILURE: dept_id=99 does not exist in the Tmima table
INSERT INTO Foititis (am, onoma, eponymo, dept_id)
VALUES (10002, 'Eleni', 'Papadopoulou', 99);
-- ERROR 1452 (23000): Cannot add or update a child row:
-- a foreign key constraint fails (`university_db`.`Foititis`,
-- CONSTRAINT `fk_foititis_tmima` FOREIGN KEY (`dept_id`)
-- REFERENCES `Tmima` (`dept_id`))
```

**FK violation — deleting a parent with dependent children:**
```sql
-- FAILURE: department 1 has students - ON DELETE RESTRICT
DELETE FROM Tmima WHERE dept_id = 1;
-- ERROR 1451 (23000): Cannot delete or update a parent row:
-- a foreign key constraint fails
```

**ON DELETE / ON UPDATE options:**

| Option | Behavior upon deletion/update of a parent record |
|---|---|
| `RESTRICT` (default) | Prevents the action — returns an error |
| `CASCADE` | Propagates the change automatically to the children |
| `SET NULL` | Sets the FK column to NULL (the column must allow NULL) |
| `NO ACTION` | Similar to RESTRICT (checked at the end of the transaction) |
| `SET DEFAULT` | Sets a DEFAULT value (rarely supported by InnoDB) |

**Exam Note:** The order of table creation matters: **first the parent, then the child**. Conversely, when **deleting**: **first the child, then the parent**. Also, MySQL requires the **InnoDB** Storage Engine (not MyISAM) to support Foreign Keys.

---

### Managing "Many-to-Many" Relationships (Junction Table)
*Managing Many-to-Many Relationships via Junction Table*

**N:M (Many-to-Many)** relationships cannot be implemented directly in the Relational Model. The solution is to **break them down into two 1:N relationships** through a **junction table (associative table / bridge table)**, which contains the Foreign Keys of both tables.

**The problem of the N:M relationship:**

Suppose a student enrolls in many courses, and each course has many students.

```text
  ER Diagram (N:M):
  +------------+     N:M          +------------+
  |  FOITITIS  |<>--( Registers )--<>|  MATHIMA   |
  +------------+    in            +------------+
  | am (PK)    |                  | mathima_id |
  | onoma      |                  | titlos     |
  +------------+                  +------------+

  PROBLEM: It cannot be implemented with a single FK column —
  neither can Foititis have many dept_id values,
  nor can Mathima have many am values in one column.
```

**Solution — Decomposition into two 1:N relationships through a junction table:**

```text
  After decomposition:

  +------------+   1:N   +-------------------+   N:1   +------------+
  |  FOITITIS  |<--------| EGGRAFI (Junction) |-------->|  MATHIMA   |
  +------------+         +-------------------+         +------------+
  | am (PK)    |         | am (FK, PK)       |         | mathima_id |
  | onoma      |         | mathima_id (FK,PK)|         | titlos     |
  +------------+         | hmerominia_eggraf |         +------------+
                          | vathmos           |
                          +-------------------+

  Relational Schema:
  Foititis(<u>am</u>, onoma, eponymo, dept_id)
  Mathima(<u>mathima_id</u>, titlos, kodikos, ects)
  Eggrafi(<u>am</u>, <u>mathima_id</u>, hmerominia_eggrafis, vathmos)
           ^FK→Foititis  ^FK→Mathima
```

**Creating the junction table `Eggrafi`:**

```sql
-- Step 1: Parent tables (Foititis and Mathima already exist)

-- Step 2: The intermediate table with a Composite Primary Key
CREATE TABLE Eggrafi (
    -- FK to Foititis
    am                  INT  NOT NULL,
    -- FK to Mathima
    mathima_id          INT  NOT NULL,
    -- Additional attributes of the relationship (relationship attributes)
    hmerominia_eggrafis DATE,
    vathmos             DECIMAL(4, 2),
    -- Composite Primary Key: the am+mathima_id combination is unique
    PRIMARY KEY (am, mathima_id),
    -- FK to Foititis
    CONSTRAINT fk_eggrafi_foititis
        FOREIGN KEY (am)
        REFERENCES Foititis (am)
        ON DELETE CASCADE,   -- If a student is deleted, their records are deleted
    -- FK to Mathima
    CONSTRAINT fk_eggrafi_mathima
        FOREIGN KEY (mathima_id)
        REFERENCES Mathima (mathima_id)
        ON DELETE RESTRICT   -- A course with enrolled students cannot be deleted
);
```

**Inserting data into the junction table:**

```sql
-- Student am=10001 enrolls in course mathima_id=1
INSERT INTO Eggrafi (am, mathima_id, hmerominia_eggrafis)
VALUES (10001, 1, '2024-10-01');

-- The same student enrolls in a second course
INSERT INTO Eggrafi (am, mathima_id, hmerominia_eggrafis)
VALUES (10001, 2, '2024-10-01');

-- Another student in the same course
INSERT INTO Eggrafi (am, mathima_id, hmerominia_eggrafis)
VALUES (10002, 1, '2024-10-02');
```

```text
  Eggrafi:
  +-------+------------+--------------------+---------+
  | am    | mathima_id | hmerominia_eggraf. | vathmos |
  +-------+------------+--------------------+---------+
  | 10001 |          1 | 2024-10-01         |    NULL |
  | 10001 |          2 | 2024-10-01         |    NULL |
  | 10002 |          1 | 2024-10-02         |    NULL |
  +-------+------------+--------------------+---------+
```

**Retrieving data via JOIN:**

```sql
-- Which courses does student am=10001 attend?
SELECT f.onoma, f.eponymo, m.titlos, m.kodikos, e.hmerominia_eggrafis
FROM   Eggrafi e
JOIN   Foititis f  ON e.am         = f.am
JOIN   Mathima  m  ON e.mathima_id = m.mathima_id
WHERE  e.am = 10001;
```

```text
  +--------+--------------+------------------+---------+--------------------+
  | onoma  | eponymo      | titlos           | kodikos | hmerominia_eggraf. |
  +--------+--------------+------------------+---------+--------------------+
  | Alexis | Nikolopoulos | Databases        | CS301   | 2024-10-01         |
  | Alexis | Nikolopoulos | Algorithms       | CS201   | 2024-10-01         |
  +--------+--------------+------------------+---------+--------------------+
```

**Preventing duplicate enrollment (the same student in the same course):**

```sql
-- Attempting a duplicate enrollment: am=10001, mathima_id=1 already exists
INSERT INTO Eggrafi (am, mathima_id)
VALUES (10001, 1);
-- ERROR 1062 (23000): Duplicate entry '10001-1' for key 'Eggrafi.PRIMARY'
-- The Composite PK prevents the duplicate enrollment automatically.
```

**Key Distinction:** In the junction table, the **Composite Primary Key** `(am, mathima_id)` plays a dual role: (1) it guarantees that every student-course combination appears **at most once**, and (2) it automatically acts as an **index** for faster lookups based on both fields.

---

## Summary Table of Key Concepts
*Summary Table of Key Concepts*

| Concept | Definition | Key Characteristic / Rule |
|---|---|---|
| **MySQL Server** | The backend RDBMS that stores and serves data | Runs as a service, listens on port 3306 |
| **MySQL Workbench** | Official desktop GUI client for MySQL | Includes SQL editor, Visual EER designer, server admin |
| **XAMPP** | Cross-platform package (Apache + MySQL/MariaDB + PHP) | For local development of web applications (localhost) |
| **phpMyAdmin** | Web-based GUI for MySQL through a browser | Runs as a PHP application on Apache |
| **InnoDB** | MySQL's storage engine | Supports Foreign Keys, Transactions, ACID |
| **Data Type** | Defines the kind and range of values of a column | Wrong type → wasted space or data loss |
| **NOT NULL** | Constraint that prohibits NULL values | Violation → `ERROR 1048` |
| **UNIQUE** | Constraint of value uniqueness (NULL allowed) | Violation → `ERROR 1062` |
| **DEFAULT** | Sets an automatic value if none is provided | Does not cause an error — applied silently |
| **FOREIGN KEY** | Column that references the Primary Key of another table | Enforces Referential Integrity |
| **ON DELETE CASCADE** | Propagates the deletion to child records | Caution: mass automatic deletion |
| **ON DELETE RESTRICT** | Prevents deletion of the parent if children exist | Default — the safest option |
| **Junction Table** | Intermediate table for implementing an N:M relationship | Carries a Composite PK of the two FKs |
| **Composite Primary Key** | PK composed of two or more columns | Used in the N:M junction table |
| **AUTO_INCREMENT** | Automatic increment of an integer PK | MySQL assigns the next available value |

---

## Key Takeaways
*Key Takeaways*

- The **MySQL Server** is the backend system that runs as a service; the tools (Workbench, phpMyAdmin, CLI) are merely **clients** that connect to it.
- **MySQL Workbench** offers visual schema design (EER Diagrams) and is the main development tool; **XAMPP/phpMyAdmin** targets web environments and quick access through a browser.
- Choosing the correct **data type** is critical: `INT` for IDs, `VARCHAR` for variable-length text, `DATE` for dates, `DECIMAL` (not `FLOAT`) for monetary amounts.
- The combination of `NOT NULL`, `UNIQUE`, and `DEFAULT` defines the data quality rules at the column level and is enforced automatically by the engine on every write.
- The `FOREIGN KEY ... REFERENCES` declaration with an **explicit constraint name** is best practice — it facilitates debugging when an FK violation error appears.
- **Referential Integrity** requires a strict order of table creation: **first the parent, then the child**; and the reverse for deletion.
- `ON DELETE CASCADE` is powerful but dangerous — deleting a parent record can automatically delete **dozens or thousands** of child records. `ON DELETE RESTRICT` is the safest default rule.
- **N:M relationships are never implemented directly** — they are always decomposed into two 1:N relationships through a **junction table** with a **Composite Primary Key**.
- The junction table can carry **additional attributes** of the relationship itself (e.g., enrollment date, grade) that do not belong to the original tables.
- MySQL requires the **InnoDB** storage engine (not MyISAM) to support Foreign Keys; the check is done with `SHOW CREATE TABLE table_name;`.
