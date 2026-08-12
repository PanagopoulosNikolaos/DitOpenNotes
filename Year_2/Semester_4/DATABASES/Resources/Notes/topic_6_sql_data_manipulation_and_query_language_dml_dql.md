# SQL Language: Data Manipulation & Queries (DML & DQL)
*SQL Language: Data Manipulation & Data Query Language*

---

## Table of Contents
*Table of Contents*

1. [Introduction](#introduction)
2. [Data Manipulation (DML — Data Manipulation Language)](#data-manipulation-dml--data-manipulation-language)
   - [INSERT INTO](#insert-into)
   - [UPDATE ... SET ... WHERE](#update--set--where)
   - [DELETE FROM ... WHERE](#delete-from--where)
   - [Comparative Table: DML Commands](#comparative-table-dml-commands)
3. [Queries & Retrieval (DQL — Data Query Language)](#queries--retrieval-dql--data-query-language)
   - [Basic SELECT Structure](#basic-select-structure)
   - [Column Projection or Full Row Selection (*)](#column-projection-or-full-row-selection-)
   - [Filtering: Comparison Operators and Logical Operators](#filtering-comparison-operators-and-logical-operators)
4. [Comparative Table: DDL vs DML vs DQL](#comparative-table-ddl-vs-dml-vs-dql)
5. [Summary Table of Key Concepts](#summary-table-of-key-concepts)
6. [Key Takeaways](#key-takeaways)

---

## Introduction

Once **DDL** (Data Definition Language) defines the schema — the structure of the tables, the columns, and the keys — the next critical step is the **populating and manipulation of the data** these will contain. This role belongs to two complementary subsets of SQL: **DML (Data Manipulation Language)** and **DQL (Data Query Language)**. DML concerns **writing** — inserting, updating, and deleting records — while DQL concerns **reading** — retrieving information from the database through queries. Understanding both is essential: a database without data has no value, and data without the ability to search and filter is not useful.

---

## Data Manipulation (DML — Data Manipulation Language)
*Data Manipulation Language*

**DML** includes the SQL statements that **modify the data** inside an already existing table. In contrast to DDL, which changes the **structure** (schema), DML changes the **contents** (records). DML statements **do not** perform an implicit `COMMIT` by default — they can be used within **transactions** and undone with `ROLLBACK`, as long as an explicit `COMMIT` has not been issued.

**Analogy**: If the table is a blank sheet of paper (structure from DDL), DML is the **pen that writes, corrects, or erases** the data on it.

```text
  SQL Subsets:

  +---------------------------------------+
  |                  SQL                  |
  +----------+----------+-----------------+
  |   DDL    |   DML    |      DQL        |
  +----------+----------+-----------------+
  | CREATE   | INSERT   | SELECT          |
  | DROP     | UPDATE   |                 |
  | ALTER    | DELETE   |                 |
  +----------+----------+-----------------+
  | Structure| Data     | Retrieval       |
  +----------+----------+-----------------+
```

---

### INSERT INTO
*Inserting New Records/Tuples into a Table*

The `INSERT INTO` statement adds **one or more new records (rows/tuples)** to an existing table. Every new record must respect the constraints defined when the table was created — `NOT NULL`, `UNIQUE`, `FOREIGN KEY`, etc.

**Basic syntax — Explicit column definition (Recommended way):**

```sql
INSERT INTO table_name (column1, column2, ...)
VALUES (value1, value2, ...);
```

**Basic syntax — Without column definition (Full value order):**

```sql
INSERT INTO table_name
VALUES (value1, value2, ...);
```

**Example — Inserting a record into table `Foititis`:**

**Before:**

```text
  mysql> SELECT * FROM Foititis;
  Empty set (0.00 sec)
```

**Execution:**

```sql
-- Inserting a student with explicit column definition (safe method)
INSERT INTO Foititis (am, onoma, eponymo, email, hmerominia, dept_id)
VALUES (10001, 'Alexis', 'Nikolopoulos', 'alex@uni.gr', '2001-05-10', 1);
```

**After:**

```text
  mysql> SELECT * FROM Foititis;
  +-------+--------+--------------+-----------+------------+---------+
  | am    | onoma  | eponymo      | email     | hmerominia | dept_id |
  +-------+--------+--------------+-----------+------------+---------+
  | 10001 | Alexis | Nikolopoulos | alex@uni.gr| 2001-05-10 |       1 |
  +-------+--------+--------------+-----------+------------+---------+
  1 row in set (0.00 sec)
```

**Inserting multiple records in one statement:**

**Execution:**

```sql
-- Inserting multiple tuples simultaneously (more efficient than many individual INSERTs)
INSERT INTO Foititis (am, onoma, eponymo, email, hmerominia, dept_id)
VALUES
    (10002, 'Eleni',   'Papadopoulou', 'eleni@uni.gr',  '2002-09-15', 2),
    (10003, 'Nikos',   'Kostopoulos',  'nikos@uni.gr',  '2000-03-22', 1),
    (10004, 'Maria',   'Stavridou',    'maria@uni.gr',  '2003-01-30', 3);
```

**After:**

```text
  mysql> SELECT * FROM Foititis;
  +-------+--------+--------------+--------------+------------+---------+
  | am    | onoma  | eponymo      | email        | hmerominia | dept_id |
  +-------+--------+--------------+--------------+------------+---------+
  | 10001 | Alexis | Nikolopoulos | alex@uni.gr  | 2001-05-10 |       1 |
  | 10002 | Eleni  | Papadopoulou | eleni@uni.gr | 2002-09-15 |       2 |
  | 10003 | Nikos  | Kostopoulos  | nikos@uni.gr | 2000-03-22 |       1 |
  | 10004 | Maria  | Stavridou    | maria@uni.gr | 2003-01-30 |       3 |
  +-------+--------+--------------+--------------+------------+---------+
  4 rows in set (0.00 sec)
```

**Insertion omitting optional columns:**

```sql
-- The hmerominia column is not provided - it receives NULL automatically
INSERT INTO Foititis (am, onoma, eponymo, dept_id)
VALUES (10005, 'Giorgos', 'Antoniou', 1);
```

**Exam Note:** The syntax **without** a column definition (`INSERT INTO table VALUES (...)`) requires values for **every column** of the table, **in the exact order** in which they were defined at creation. Omitting even one value causes an error. The syntax **with** a column definition is always safer and more readable.

**Key Distinction:** `INSERT INTO` violates constraints in real time:

```sql
-- PRIMARY KEY violation (am=10001 already exists)
INSERT INTO Foititis (am, onoma, eponymo, dept_id)
VALUES (10001, 'Other', 'Student', 2);
-- ERROR 1062 (23000): Duplicate entry '10001' for key 'PRIMARY'

-- FOREIGN KEY violation (dept_id=99 does not exist in table Tmima)
INSERT INTO Foititis (am, onoma, eponymo, dept_id)
VALUES (10006, 'Test', 'Student', 99);
-- ERROR 1452: Cannot add or update a child row: a foreign key constraint fails
```

---

### UPDATE ... SET ... WHERE
*Updating/Modifying Existing Data*

The `UPDATE` statement **modifies values in existing records** of a table. The `SET` clause defines which column changes and to which value, while the `WHERE` clause determines **which rows** will be affected. Without `WHERE`, the statement affects **all** the rows of the table.

**Basic syntax:**

```sql
UPDATE table_name
SET    column1 = value1,
       column2 = value2,
       ...
WHERE  condition;
```

**Example — Updating the email of a specific student:**

**Before:**

```text
  mysql> SELECT am, onoma, email FROM Foititis WHERE am = 10001;
  +-------+--------+-------------+
  | am    | onoma  | email       |
  +-------+--------+-------------+
  | 10001 | Alexis | alex@uni.gr |
  +-------+--------+-------------+
```

**Execution:**

```sql
-- Updating the email of only the student with am=10001
UPDATE Foititis
SET    email = 'alexniko@newmail.gr'
WHERE  am = 10001;
```

**After:**

```text
  mysql> SELECT am, onoma, email FROM Foititis WHERE am = 10001;
  +-------+--------+--------------------+
  | am    | onoma  | email              |
  +-------+--------+--------------------+
  | 10001 | Alexis | alexniko@newmail.gr|
  +-------+--------+--------------------+
```

**Updating multiple columns simultaneously:**

**Before:**

```text
  mysql> SELECT am, eponymo, dept_id FROM Foititis WHERE am = 10003;
  +-------+--------------+---------+
  | am    | eponymo      | dept_id |
  +-------+--------------+---------+
  | 10003 | Kostopoulos  |       1 |
  +-------+--------------+---------+
```

**Execution:**

```sql
-- Simultaneous change of surname and department
UPDATE Foititis
SET    eponymo = 'Kostopoulos-New',
       dept_id = 2
WHERE  am = 10003;
```

**After:**

```text
  mysql> SELECT am, eponymo, dept_id FROM Foititis WHERE am = 10003;
  +-------+------------------+---------+
  | am    | eponymo          | dept_id |
  +-------+------------------+---------+
  | 10003 | Kostopoulos-New |       2 |
  +-------+------------------+---------+
```

**Updating multiple rows with a common condition:**

**Before:**

```text
  mysql> SELECT am, dept_id FROM Foititis;
  +-------+---------+
  | am    | dept_id |
  +-------+---------+
  | 10001 |       1 |
  | 10002 |       2 |
  | 10003 |       2 |  (after the previous update)
  | 10004 |       3 |
  +-------+---------+
```

**Execution:**

```sql
-- Moving ALL students of department 2 to department 4
UPDATE Foititis
SET    dept_id = 4
WHERE  dept_id = 2;
```

**After:**

```text
  mysql> SELECT am, dept_id FROM Foititis;
  +-------+---------+
  | am    | dept_id |
  +-------+---------+
  | 10001 |       1 |
  | 10002 |       4 |  <-- Changed
  | 10003 |       4 |  <-- Changed
  | 10004 |       3 |
  +-------+---------+
```

**Dangerous example — UPDATE without WHERE:**

```sql
-- WARNING: Without WHERE, ALL rows of the table are affected
UPDATE Foititis
SET    dept_id = 1;
-- Result: ALL students are moved to department 1
```

**Exam Note:** Omitting `WHERE` in an `UPDATE` statement is one of the most **common and destructive mistakes** — it affects every row of the table. Before any `UPDATE`, it is recommended to run a corresponding `SELECT` with the same `WHERE` condition to verify that the correct rows are selected.

---

### DELETE FROM ... WHERE
*Deleting Specific Records Based on a Condition*

The `DELETE FROM` statement **deletes records (rows/tuples)** from a table. The `WHERE` clause determines which rows will be deleted. Without `WHERE`, **all** records are deleted (the table's schema remains). Unlike `DROP TABLE`, the table **continues to exist** after `DELETE`.

**Basic syntax:**

```sql
DELETE FROM table_name
WHERE  condition;
```

**Example — Deleting a specific student:**

**Before:**

```text
  mysql> SELECT am, onoma, eponymo FROM Foititis;
  +-------+--------+-----------------+
  | am    | onoma  | eponymo         |
  +-------+--------+-----------------+
  | 10001 | Alexis | Nikolopoulos    |
  | 10002 | Eleni  | Papadopoulou    |
  | 10003 | Nikos  | Kostopoulos-New|
  | 10004 | Maria  | Stavridou       |
  +-------+--------+-----------------+
```

**Execution:**

```sql
-- Deleting only the student with am=10003
DELETE FROM Foititis
WHERE  am = 10003;
```

**After:**

```text
  mysql> SELECT am, onoma, eponymo FROM Foititis;
  +-------+--------+--------------+
  | am    | onoma  | eponymo      |
  +-------+--------+--------------+
  | 10001 | Alexis | Nikolopoulos |
  | 10002 | Eleni  | Papadopoulou |
  | 10004 | Maria  | Stavridou    |
  +-------+--------+--------------+
  3 rows in set (0.00 sec)
```

**Deletion with a compound condition:**

**Execution:**

```sql
-- Deleting students who belong to department 4
DELETE FROM Foititis
WHERE  dept_id = 4;
```

**Deleting all records (without WHERE):**

```sql
-- Deletes ALL records - the table remains empty (structure intact)
DELETE FROM Foititis;
```

**The code above has the same result as:**

```sql
-- TRUNCATE: Faster for clearing an entire table
-- (cannot be recovered with ROLLBACK - behaves like DDL)
TRUNCATE TABLE Foititis;
```

**Referential Integrity Violation during DELETE:**

```sql
-- Attempting to delete a department that has students
DELETE FROM Tmima
WHERE  dept_id = 1;
-- ERROR 1451: Cannot delete or update a parent row:
-- a foreign key constraint fails (Foititis.dept_id REFERENCES Tmima.dept_id)
```

**Comparative Table: `DELETE FROM` vs `DROP TABLE` vs `TRUNCATE`:**

| Characteristic | `DELETE FROM` | `DROP TABLE` | `TRUNCATE TABLE` |
|---|---|---|---|
| **SQL category** | DML | DDL | DDL (behavior) |
| **Table structure** | Remains | Deleted | Remains |
| **Data** | Selective / Full deletion | Full deletion | Full deletion |
| **WHERE possible?** | Yes | No | No |
| **ROLLBACK possible?** | Yes (within a transaction) | No | No |
| **Speed** | Slow (row by row) | Fast | Very fast |
| **AUTO_INCREMENT reset** | No | — | Yes |

**Key Distinction:** `DELETE FROM table` (without `WHERE`) and `TRUNCATE TABLE table` both empty the table of data. However, `DELETE` is DML and supports `ROLLBACK`, while `TRUNCATE` behaves like DDL (implicit `COMMIT`) and is faster because it does not log each deletion separately.

---

### Comparative Table: DML Commands
*Comparative Table: DML Commands*

| Command | Action | Requires WHERE? | Affects Rows | Affects Structure |
|---|---|---|---|---|
| `INSERT INTO` | Adds new records | No | New rows | No |
| `UPDATE ... SET` | Modifies existing values | Recommended (without → full update) | Existing rows | No |
| `DELETE FROM` | Deletes existing records | Recommended (without → full deletion) | Existing rows | No |

---

## Queries & Retrieval (DQL — Data Query Language)
*Data Query Language*

**DQL** (or more commonly referred to as part of DML) essentially includes the `SELECT` statement — the **most frequently used statement** of the entire SQL language. `SELECT` **does not modify** the data — it retrieves and presents information from one or more tables based on criteria. The relationship between `SELECT` and Relational Algebra is direct: `WHERE` corresponds to **Selection** ($\sigma$) and the column list to **Projection** ($\pi$).

**Analogy**: `SELECT` is like a **question** one asks a librarian — it defines what one wants to see (columns), from where (tables), and under what conditions (filters). The librarian returns results without changing anything in the books.

---

### Basic SELECT Structure
*Basic SELECT Structure*

The basic structure of a `SELECT` query consists of three fundamental clauses that answer three questions:

| Clause | Question it answers | Relational Algebra Correspondence |
|---|---|---|
| `SELECT` | **What** do I retrieve? (which columns) | Projection $\pi$ |
| `FROM` | **From where** do I retrieve? (which table) | Relation $R$ |
| `WHERE` | **Under what conditions**? (which rows) | Selection $\sigma$ |

**Basic syntax:**

```sql
SELECT column1, column2, ...
FROM   table_name
WHERE  condition;
```

**General query form — Correspondence with Relational Algebra:**

$$\pi_{\text{column1, column2}}(\sigma_{\text{condition}}(\text{table\_name}))$$

```sql
-- SQL equivalent
SELECT column1, column2
FROM   table_name
WHERE  condition;
```

**Example — Retrieving the first and last name of ALL students:**

**Table state:**

```text
  Foititis:
  +-------+--------+--------------+--------------+------------+---------+
  | am    | onoma  | eponymo      | email        | hmerominia | dept_id |
  +-------+--------+--------------+--------------+------------+---------+
  | 10001 | Alexis | Nikolopoulos | alex@uni.gr  | 2001-05-10 |       1 |
  | 10002 | Eleni  | Papadopoulou | eleni@uni.gr | 2002-09-15 |       4 |
  | 10004 | Maria  | Stavridou    | maria@uni.gr | 2003-01-30 |       3 |
  +-------+--------+--------------+--------------+------------+---------+
```

**Execution:**

```sql
-- Selecting specific columns from ALL rows
SELECT onoma, eponymo
FROM   Foititis;
```

**Result:**

```text
  +--------+--------------+
  | onoma  | eponymo      |
  +--------+--------------+
  | Alexis | Nikolopoulos |
  | Eleni  | Papadopoulou |
  | Maria  | Stavridou    |
  +--------+--------------+
  3 rows in set (0.00 sec)
```

**Using an alias (AS) to rename columns in the result:**

```sql
-- The alias changes only the column name in the result - it does not change the database
SELECT onoma    AS "Student Name",
       eponymo  AS "Surname",
       dept_id  AS "Department"
FROM   Foititis;
```

**Result:**

```text
  +----------------+--------------+-------+
  | Student Name   | Surname       | Dept. |
  +----------------+--------------+-------+
  | Alexis         | Nikolopoulos |     1 |
  | Eleni          | Papadopoulou |     4 |
  | Maria          | Stavridou    |     3 |
  +----------------+--------------+-------+
```

---

### Column Projection or Full Row Selection (*)
*Column Projection or Full Row Selection*

`SELECT` offers two basic options for the columns that are returned: **explicit selection of specific columns** or the use of the **wildcard `*`**, which returns all columns.

**`SELECT *` syntax — Selecting all columns:**

```sql
SELECT *
FROM   table_name;
```

**Example — Full projection of table `Foititis`:**

**Execution:**

```sql
SELECT *
FROM   Foititis;
```

**Result:**

```text
  +-------+--------+--------------+--------------+------------+---------+
  | am    | onoma  | eponymo      | email        | hmerominia | dept_id |
  +-------+--------+--------------+--------------+------------+---------+
  | 10001 | Alexis | Nikolopoulos | alex@uni.gr  | 2001-05-10 |       1 |
  | 10002 | Eleni  | Papadopoulou | eleni@uni.gr | 2002-09-15 |       4 |
  | 10004 | Maria  | Stavridou    | maria@uni.gr | 2003-01-30 |       3 |
  +-------+--------+--------------+--------------+------------+---------+
```

**Comparison of `SELECT *` vs Specific Columns:**

| Criterion | `SELECT *` | `SELECT col1, col2` |
|---|---|---|
| **Code readability** | Low (it is not clear what is expected) | High (clear intent) |
| **Performance** | Lower (unnecessary columns are transferred) | Higher (only the necessary data) |
| **Resilience to schema changes** | Vulnerable (new columns appear automatically) | Resilient (stable result) |
| **Use** | Quick exploration / debugging | Production code |

**Using `DISTINCT` — Avoiding duplicates:**

**Execution:**

```sql
-- Displays only the unique departments that have students
SELECT DISTINCT dept_id
FROM   Foititis;
```

**Result:**

```text
  +---------+
  | dept_id |
  +---------+
  |       1 |
  |       4 |
  |       3 |
  +---------+
  3 rows in set (0.00 sec)
```

**Exam Note:** `SELECT *` is useful for quick data exploration and debugging, but it is **avoided in production code** — it returns unnecessary data, affects performance, and can produce unexpected results if the schema changes.

---

### Filtering: Comparison Operators and Logical Operators
*Filtering: Comparison Operators and Logical Operators*

The `WHERE` clause filters rows based on **conditions** built with **Comparison Operators** and **Logical Operators**. Only the rows for which the condition evaluates to `TRUE` are included in the result.

**Comparison Operators:**

| Operator | Meaning | Example |
|---|---|---|
| `=` | Equality | `dept_id = 1` |
| `!=` or `<>` | Inequality | `dept_id != 2` |
| `>` | Greater than | `am > 10002` |
| `<` | Less than | `am < 10003` |
| `>=` | Greater than or equal | `am >= 10002` |
| `<=` | Less than or equal | `am <= 10003` |
| `BETWEEN a AND b` | Between two values (inclusive) | `am BETWEEN 10001 AND 10003` |
| `IN (v1, v2, ...)` | Belongs to a set of values | `dept_id IN (1, 3)` |
| `IS NULL` | The value is NULL | `email IS NULL` |
| `IS NOT NULL` | The value is not NULL | `hmerominia IS NOT NULL` |
| `LIKE 'pattern'` | Pattern matching (% = many characters, _ = one) | `eponymo LIKE 'Papa%'` |

**Logical Operators:**

| Operator | Meaning | Result `TRUE` |
|---|---|---|
| `AND` | Logical AND | Both conditions are `TRUE` |
| `OR` | Logical OR | At least one condition is `TRUE` |
| `NOT` | Negation | The condition is `FALSE` |

**Example 1 — Equality filter `=`:**

**Table state:**

```text
  Foititis (full):
  +-------+--------+--------------+------------+---------+
  | am    | onoma  | eponymo      | hmerominia | dept_id |
  +-------+--------+--------------+------------+---------+
  | 10001 | Alexis | Nikolopoulos | 2001-05-10 |       1 |
  | 10002 | Eleni  | Papadopoulou | 2002-09-15 |       4 |
  | 10004 | Maria  | Stavridou    | 2003-01-30 |       3 |
  +-------+--------+--------------+------------+---------+
```

**Execution:**

```sql
-- Retrieving students who belong to department 1
SELECT am, onoma, eponymo
FROM   Foititis
WHERE  dept_id = 1;
```

**Result:**

```text
  +-------+--------+--------------+
  | am    | onoma  | eponymo      |
  +-------+--------+--------------+
  | 10001 | Alexis | Nikolopoulos |
  +-------+--------+--------------+
  1 row in set (0.00 sec)
```

**Example 2 — The `>` operator (greater than):**

**Execution:**

```sql
-- Retrieving students with am greater than 10001
SELECT am, onoma, eponymo
FROM   Foititis
WHERE  am > 10001;
```

**Result:**

```text
  +-------+--------+--------------+
  | am    | onoma  | eponymo      |
  +-------+--------+--------------+
  | 10002 | Eleni  | Papadopoulou |
  | 10004 | Maria  | Stavridou    |
  +-------+--------+--------------+
```

**Example 3 — The `AND` operator (both conditions):**

**Execution:**

```sql
-- Students of department 1 who were born before 2002
SELECT am, onoma, hmerominia, dept_id
FROM   Foititis
WHERE  dept_id = 1
  AND  hmerominia < '2002-01-01';
```

**Result:**

```text
  +-------+--------+------------+---------+
  | am    | onoma  | hmerominia | dept_id |
  +-------+--------+------------+---------+
  | 10001 | Alexis | 2001-05-10 |       1 |
  +-------+--------+------------+---------+
```

**Example 4 — The `OR` operator (at least one condition):**

**Execution:**

```sql
-- Students who belong to department 1 OR department 3
SELECT am, onoma, dept_id
FROM   Foititis
WHERE  dept_id = 1
    OR dept_id = 3;
```

**Result:**

```text
  +-------+--------+---------+
  | am    | onoma  | dept_id |
  +-------+--------+---------+
  | 10001 | Alexis |       1 |
  | 10004 | Maria  |       3 |
  +-------+--------+---------+
```

**Equivalent to `IN`:**

```sql
-- Shorter notation for multiple OR values
SELECT am, onoma, dept_id
FROM   Foititis
WHERE  dept_id IN (1, 3);
```

**Example 5 — The `NOT` operator (negation):**

**Execution:**

```sql
-- Students who do NOT belong to department 1
SELECT am, onoma, dept_id
FROM   Foititis
WHERE  NOT dept_id = 1;
-- Equivalent: WHERE dept_id != 1  or  WHERE dept_id <> 1
```

**Result:**

```text
  +-------+-------+---------+
  | am    | onoma | dept_id |
  +-------+-------+---------+
  | 10002 | Eleni |       4 |
  | 10004 | Maria |       3 |
  +-------+-------+---------+
```

**Example 6 — Combination of `AND`, `OR`, and parentheses:**

```sql
-- Students who (belong to department 1 AND were born after 2000)
-- Or belong to department 3
SELECT am, onoma, eponymo, hmerominia, dept_id
FROM   Foititis
WHERE  (dept_id = 1 AND hmerominia > '2000-01-01')
    OR dept_id = 3;
```

**Exam Note:** When using `AND` and `OR` in the same `WHERE`, the **precedence order** is critical: `AND` is evaluated **before** `OR`. Using **parentheses** to explicitly define the evaluation order is considered best practice and prevents logical errors.

**Example 7 — The `LIKE` operator for pattern search:**

**Execution:**

```sql
-- Students whose surname starts with 'Papa'
SELECT am, onoma, eponymo
FROM   Foititis
WHERE  eponymo LIKE 'Papa%';
```

**Result:**

```text
  +-------+-------+--------------+
  | am    | onoma | eponymo      |
  +-------+-------+--------------+
  | 10002 | Eleni | Papadopoulou |
  +-------+-------+--------------+
```

**Example 8 — The `IS NULL` operator:**

```sql
-- Students for whom an email has not been recorded
SELECT am, onoma
FROM   Foititis
WHERE  email IS NULL;
```

**Relational Algebra — SQL correspondence (summary):**

| Relational Algebra | SQL |
|---|---|
| $\sigma_{\text{dept\_id}=1}(\text{Foititis})$ | `SELECT * FROM Foititis WHERE dept_id = 1` |
| $\pi_{\text{onoma, eponymo}}(\text{Foititis})$ | `SELECT onoma, eponymo FROM Foititis` |
| $\pi_{\text{onoma}}(\sigma_{\text{dept\_id}=1}(\text{Foititis}))$ | `SELECT onoma FROM Foititis WHERE dept_id = 1` |
| $\sigma_{\text{dept\_id}=1 \land \text{am}>10001}(\text{Foititis})$ | `SELECT * FROM Foititis WHERE dept_id = 1 AND am > 10001` |

---

## Comparative Table: DDL vs DML vs DQL
*Comparative Table: DDL vs DML vs DQL*

| Characteristic | DDL | DML | DQL |
|---|---|---|---|
| **Name** | Data Definition Language | Data Manipulation Language | Data Query Language |
| **Purpose** | Defining/modifying structures | Manipulating data | Retrieving data |
| **Main statements** | `CREATE`, `DROP`, `ALTER` | `INSERT`, `UPDATE`, `DELETE` | `SELECT` |
| **What it modifies** | Database schema (structure) | Data (records) | Nothing (read-only) |
| **Implicit COMMIT** | Yes (MySQL) | No | Not applicable |
| **ROLLBACK possible?** | No | Yes (within a transaction) | Not applicable |
| **Risk of loss** | High (DROP) | Medium (DELETE without WHERE) | None |
| **Relational Algebra correspondence** | Relation definition | Tuple modification | $\sigma$, $\pi$, $\bowtie$ |

---

## Summary Table of Key Concepts
*Summary Table of Key Concepts*

| Concept | Definition | Key Characteristic / Rule |
|---|---|---|
| **DML** (Data Manipulation Language) | Subset of SQL for manipulating data | `INSERT`, `UPDATE`, `DELETE` — supports `ROLLBACK` |
| **DQL** (Data Query Language) | Subset of SQL for retrieving data | `SELECT` — does not modify data |
| **INSERT INTO** | Inserts new records into a table | Respects constraints (PK, FK, NOT NULL) |
| **UPDATE ... SET** | Modifies values of existing records | Without `WHERE` updates ALL rows |
| **DELETE FROM** | Deletes records from a table | Without `WHERE` deletes ALL rows — structure remains |
| **SELECT** | Retrieves data from table(s) | The most frequent SQL statement — corresponds to $\pi$ + $\sigma$ |
| **FROM** | Defines the source table(s) | Mandatory clause of every `SELECT` |
| **WHERE** | Filters rows based on a condition | Corresponds to the Selection $\sigma$ of Relational Algebra |
| **SELECT \*** | Selects all columns | Useful for debugging — avoided in production code |
| **SELECT DISTINCT** | Returns unique values | Removes duplicate rows from the result |
| **The `=` operator** | Equality in `WHERE` | Differs from `IS NULL` — `= NULL` does not work |
| **The `>`/`<` operators** | Size comparison | Applies to numbers, dates, text (alphanumeric) |
| **The `AND` operator** | Logical AND | Higher precedence than `OR` — parentheses recommended |
| **The `OR` operator** | Logical OR | Returns rows where at least one condition is `TRUE` |
| **The `NOT` operator** | Logical negation | Inverts the result of the condition |
| **The `IN` operator** | Belongs to a set of values | Shorthand for multiple `OR` equalities |
| **The `LIKE` operator** | Pattern-based search | `%` = many characters, `_` = one character |
| **The `IS NULL` operator** | Check for a NULL value | `= NULL` is wrong — `IS NULL` is always used |
| **Alias (`AS`)** | Renames a column in the result | Does not change the schema — only the presentation |
| **`TRUNCATE TABLE`** | Quickly deletes ALL records | Behaves like DDL — does not support `ROLLBACK` |

---

## Key Takeaways
*Key Takeaways*

- **DML** (INSERT, UPDATE, DELETE) handles the **data** inside the tables — it does not change their structure/schema. Unlike DDL, DML statements **support** `ROLLBACK` within transactions.
- The `INSERT INTO` statement with **explicit column definition** (`INSERT INTO table (col1, col2) VALUES (v1, v2)`) is always safer than the syntax without columns — it does not depend on the column order and allows omitting optional fields.
- **Exam Note:** Without a `WHERE` clause, `UPDATE` updates and `DELETE` deletes **every row** of the table — this is one of the most common and destructive mistakes. Running a corresponding `SELECT` before the `UPDATE`/`DELETE` is best practice.
- `SELECT` corresponds to the **combination of Projection ($\pi$) and Selection ($\sigma$)** of Relational Algebra: the column list implements the Projection, the `WHERE` implements the Selection.
- The `WHERE` clause is built with **Comparison Operators** (`=`, `>`, `<`, `>=`, `<=`, `!=`) and **Logical Operators** (`AND`, `OR`, `NOT`). The precedence order is: `NOT` > `AND` > `OR` — using parentheses eliminates ambiguity.
- **Key Distinction:** `DELETE FROM table` (without `WHERE`) empties the data but **preserves the table's structure**, while `DROP TABLE` destroys both the data and the structure. `TRUNCATE TABLE` empties quickly like `DELETE` without `WHERE`, but behaves like DDL (does not support `ROLLBACK`).
- `SELECT *` is useful for quick exploration, but it is **avoided in production code** — it burdens performance and hides which columns are actually used.
- **Key Distinction:** For checking a NULL value, `IS NULL` or `IS NOT NULL` is **always** used — the `= NULL` syntax does not work correctly in SQL, because `NULL` is not a value but a state of the absence of a value.
- The `IN (v1, v2, ...)` operator is equivalent to multiple `OR` equalities and is preferred for **shorter and more readable code** when checking many values.
- **Exam Note:** `SELECT` (DQL) is the **only statement that does not modify** data — it is purely read-only. Every `INSERT`, `UPDATE`, and `DELETE` modifies the table and leaves a permanent mark (except with `ROLLBACK`).
