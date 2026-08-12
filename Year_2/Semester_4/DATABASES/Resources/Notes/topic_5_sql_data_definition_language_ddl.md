# SQL Language: Data Definition (DDL — Data Definition Language)
*SQL Language: Data Definition Language*

---

## Table of Contents
*Table of Contents*

1. [Introduction](#introduction)
2. [Database Management](#database-management)
   - [CREATE DATABASE / SCHEMA](#create-database--schema)
   - [DROP DATABASE](#drop-database)
   - [USE](#use)
   - [SHOW DATABASES](#show-databases)
3. [Table Management (Structure/Schema)](#table-management-structureschema)
   - [CREATE TABLE](#create-table)
   - [DROP TABLE](#drop-table)
   - [DESCRIBE / EXPLAIN](#describe--explain)
4. [Modifying the Table Schema (ALTER TABLE)](#modifying-the-table-schema-alter-table)
   - [ADD](#add)
   - [MODIFY](#modify)
   - [CHANGE](#change)
   - [DROP COLUMN](#drop-column)
5. [Comparative Table: DDL Commands](#comparative-table-ddl-commands)
6. [Summary Table of Key Concepts](#summary-table-of-key-concepts)
7. [Key Takeaways](#key-takeaways)

---

## Introduction

**Data Definition Language (DDL)** is the subset of the SQL language used exclusively for the **definition, creation, alteration, and destruction** of a database's structures — namely the databases (databases/schemas) and the tables. In contrast to DML (Data Manipulation Language), which handles the **data** inside tables, DDL defines the **schema** — the skeleton on which the data will be stored. Executing any DDL statement entails an automatic commit (implicit `COMMIT`) in MySQL, which means that structural changes are **permanent and irreversible** without backups. Understanding DDL is fundamental, as it links logical design (Step 3 of the lifecycle) with the actual implementation in the DBMS.

---

## Database Management
*Database Management*

Before creating any table, a **database** (database or schema) that will contain it must exist. The database acts as a **namespace** — it isolates the tables and objects of one project from other projects running on the same MySQL Server.

**Analogy**: The database is like a **file folder** on a computer — the MySQL Server is the hard disk, each database is a separate folder, and the tables are the documents inside the folder.

```text
  MySQL Server
  |
  +-- university_db/          <-- Database (DATABASE)
  |   +-- Foititis             <-- Table (TABLE)
  |   +-- Mathima
  |   +-- Tmima
  |
  +-- shop_db/
      +-- Products
      +-- Orders
      +-- Customers
```

---

### CREATE DATABASE / SCHEMA
*Creating a New Database*

The `CREATE DATABASE` statement (or its synonym `CREATE SCHEMA`) creates a **new, empty database** on the MySQL Server. After creation, the database contains no tables.

**Basic syntax:**

```sql
CREATE DATABASE database_name;
-- Or equivalently:
CREATE SCHEMA schema_name;
```

**Example — Creating a university database:**

**Before:**

```text
  mysql> SHOW DATABASES;
  +--------------------+
  | Database           |
  +--------------------+
  | information_schema |
  | mysql              |
  | performance_schema |
  | sys                |
  +--------------------+
  4 rows in set (0.00 sec)
```

**Execution:**

```sql
CREATE DATABASE university_db;
```

**After:**

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

**Safe creation with `IF NOT EXISTS`:**

```sql
-- Prevents an error if the database already exists
CREATE DATABASE IF NOT EXISTS university_db;
```

**Exam Note:** In MySQL, `DATABASE` and `SCHEMA` are **completely synonymous** — the two statements produce exactly the same result. In other DBMSs (e.g., PostgreSQL), `DATABASE` and `SCHEMA` have different meanings.

---

### DROP DATABASE
*Total Deletion of a Database*

The `DROP DATABASE` statement **completely destroys** a database along with **all the tables, data, and objects** it contains. This action is **permanent and irrevocable** — there is no `UNDO`.

**Basic syntax:**

```sql
DROP DATABASE database_name;
-- Or equivalently:
DROP SCHEMA schema_name;
```

**Example — Deleting a database:**

```sql
DROP DATABASE university_db;
```

**Safe deletion with `IF EXISTS`:**

```sql
-- Prevents an error if the database does not exist
DROP DATABASE IF EXISTS university_db;
```

**Comparative Table: `CREATE DATABASE` vs `DROP DATABASE`:**

| Characteristic | `CREATE DATABASE` | `DROP DATABASE` |
|---|---|---|
| **Purpose** | Creates a new, empty database | Destroys an existing database |
| **Precondition** | The database must not already exist | The database must exist |
| **Effect on data** | No effect | Deletes all data and tables |
| **Reversibility** | Reversible with `DROP` | Irreversible |
| **Safe variant** | `CREATE DATABASE IF NOT EXISTS` | `DROP DATABASE IF EXISTS` |

**Key Distinction:** `DROP DATABASE` is the **most destructive** DDL statement — it deletes the entire database with all its contents. In production environments, a backup is always required before executing it.

---

### USE
*Selecting the Active Database for the Current Session*

The `USE` statement sets which database will be used as the **default working context** for the subsequent SQL statements of the current session. Without `USE`, every reference to a table must explicitly specify the database (e.g., `university_db.Foititis`).

**Basic syntax:**

```sql
USE database_name;
```

**Example — Selecting the active database and using it:**

```sql
-- Setting the active database
USE university_db;

-- From now on, all statements refer to university_db
-- without needing a fully qualified name
SELECT * FROM Foititis;  -- Equivalent to: SELECT * FROM university_db.Foititis
```

**Verifying the active database:**

```sql
SELECT DATABASE();
```

```text
  +---------------+
  | DATABASE()    |
  +---------------+
  | university_db |
  +---------------+
  1 row in set (0.00 sec)
```

**Exam Note:** `USE` affects **only the current session** (connection) — it does not change the settings of other users or connections. Every new session starts without an active database.

---

### SHOW DATABASES
*Viewing All Available Databases*

The `SHOW DATABASES` statement returns a list of **all the databases** that exist on the current MySQL Server and to which the current user has access rights.

**Basic syntax:**

```sql
SHOW DATABASES;
```

**Result:**

```text
  +--------------------+
  | Database           |
  +--------------------+
  | information_schema |
  | mysql              |
  | performance_schema |
  | sys                |
  | university_db      |
  | shop_db            |
  +--------------------+
  6 rows in set (0.00 sec)
```

**Brief workflow guide — Creating and using a new database:**

```sql
-- Step 1: Check existing databases
SHOW DATABASES;

-- Step 2: Create a new database
CREATE DATABASE university_db;

-- Step 3: Select as active
USE university_db;

-- Step 4: Verify
SELECT DATABASE();
```

---

## Table Management (Structure/Schema)
*Table Management (Structure/Schema)*

The **table** is the fundamental data storage structure in the relational model. Each table consists of **columns** (attributes) with specific data types and **rows** (tuples) that contain the actual data. DDL provides statements for the **creation**, **destruction**, and **inspection** of table structures.

---

### CREATE TABLE
*Creating a Table, Defining Fields, Types, and the Primary Key*

The `CREATE TABLE` statement is the **central DDL statement** — it defines the schema of a new table: the column names, their data types, the constraints, and the keys.

**Basic syntax:**

```sql
CREATE TABLE table_name (
    column1_name  datatype  [constraints],
    column2_name  datatype  [constraints],
    ...
    [table_constraints]
);
```

**Basic data types (Data Types) in MySQL:**

| Category | Type | Description | Usage Example |
|---|---|---|---|
| **Integers** | `INT` / `INTEGER` | 32-bit integer (-2.1B to 2.1B) | Student ID, age |
| **Integers** | `TINYINT` | 8-bit integer (0-255 or -128 to 127) | Active/inactive (0/1) |
| **Integers** | `BIGINT` | 64-bit integer | Transaction numbers |
| **Decimals** | `DECIMAL(p,s)` | Exact decimal, p digits, s decimal places | Grade (4,2), monetary amounts |
| **Decimals** | `FLOAT` / `DOUBLE` | Floating-point (approximate) | Scientific values |
| **Text** | `VARCHAR(n)` | Variable length up to n characters | Names, emails |
| **Text** | `CHAR(n)` | Fixed length of n characters | Codes (e.g., country code) |
| **Text** | `TEXT` | Large text (up to 65,535 chars) | Descriptions, comments |
| **Date** | `DATE` | Date (YYYY-MM-DD) | Date of birth |
| **Date** | `DATETIME` | Date and time | Record timestamp |
| **Date** | `YEAR` | 4-digit year | Academic year |

**Basic constraints:**

| Constraint | Purpose |
|---|---|
| `NOT NULL` | The column does not allow NULL values |
| `UNIQUE` | Every value in the column must be unique |
| `DEFAULT value` | Sets a default value if no value is given |
| `PRIMARY KEY` | Unique identification of each row — `NOT NULL` + `UNIQUE` |
| `FOREIGN KEY` | Reference to the Primary Key of another table |
| `AUTO_INCREMENT` | Automatic value increment (usually for PK) |
| `CHECK (condition)` | Verifies that the value satisfies some condition |

**Example — Creating the Department table:**

**Before:**

```text
  mysql> SHOW TABLES;
  Empty set (0.00 sec)
```

**Execution:**

```sql
USE university_db;

-- Creating the Department table (referenced table - created first)
CREATE TABLE Tmima (
    dept_id    INT           NOT NULL AUTO_INCREMENT,
    onoma      VARCHAR(100)  NOT NULL,
    tilefono   VARCHAR(15),
    CONSTRAINT pk_tmima PRIMARY KEY (dept_id)
);

-- Creating the Student table (with Foreign Key to Department)
CREATE TABLE Foititis (
    am         INT           NOT NULL,
    onoma      VARCHAR(50)   NOT NULL,
    eponymo    VARCHAR(50)   NOT NULL,
    email      VARCHAR(100)  UNIQUE,
    hmerominia DATE,
    dept_id    INT           NOT NULL,
    CONSTRAINT pk_foititis        PRIMARY KEY (am),
    CONSTRAINT fk_foititis_tmima  FOREIGN KEY (dept_id)
        REFERENCES Tmima(dept_id)
);
```

**After:**

```text
  mysql> SHOW TABLES;
  +-------------------------+
  | Tables_in_university_db |
  +-------------------------+
  | Foititis                |
  | Tmima                   |
  +-------------------------+
  2 rows in set (0.00 sec)
```

**Relational schema corresponding to the tables above:**

```text
  Tmima(<u>dept_id</u>, onoma, tilefono)
  Foititis(<u>am</u>, onoma, eponymo, email, hmerominia, dept_id#)
                                                         |
                                             Foreign Key -> Tmima(dept_id)
```

**Key Distinction:** The order of table creation is critical when Foreign Keys exist. The **referenced table** (the one being referenced) must be created **before** the referencing one (the one making the reference). In the example: `Tmima` must be created **before** `Foititis`.

---

### DROP TABLE
*Permanent Deletion of a Table*

The `DROP TABLE` statement **permanently destroys** a table along with **all the data** it contains. This action is **irreversible**.

**Basic syntax:**

```sql
DROP TABLE table_name;
```

**Safe deletion with `IF EXISTS`:**

```sql
-- Prevents an error if the table does not exist
DROP TABLE IF EXISTS Foititis;
```

**Example — Correct deletion order with Foreign Keys:**

```sql
-- Wrong order: will fail due to Foreign Key constraint
-- DROP TABLE Tmima;  -- ERROR: Foititis depends on Tmima

-- Correct order: delete the referencing tables first
DROP TABLE IF EXISTS Foititis;  -- First the table with the FK
DROP TABLE IF EXISTS Tmima;     -- Then the referenced table
```

**Comparative Table: `DROP TABLE` vs `DELETE FROM`:**

| Characteristic | `DROP TABLE` | `DELETE FROM table` |
|---|---|---|
| **SQL category** | DDL | DML |
| **What it destroys** | The table AND the data | Only the data (rows) |
| **Table structure** | Deleted | Remains intact |
| **Reversibility** | Irreversible | Reversible via `ROLLBACK` (within a transaction) |
| **Use** | Permanent removal | Data clearing |

---

### DESCRIBE / EXPLAIN
*Viewing the Table's Schema / Metadata*

The `DESCRIBE` (or `DESC`) and `EXPLAIN` statements return information about a **table's structure**: the column names, the data types, the constraints, and their default values.

**Basic syntax:**

```sql
DESCRIBE table_name;
-- Or equivalently:
DESC table_name;
EXPLAIN table_name;
```

**Example — Inspecting the structure of table `Foititis`:**

```sql
DESCRIBE Foititis;
```

**Result:**

```text
  +-----------+--------------+------+-----+---------+-------+
  | Field     | Type         | Null | Key | Default | Extra |
  +-----------+--------------+------+-----+---------+-------+
  | am        | int          | NO   | PRI | NULL    |       |
  | onoma     | varchar(50)  | NO   |     | NULL    |       |
  | eponymo   | varchar(50)  | NO   |     | NULL    |       |
  | email     | varchar(100) | YES  | UNI | NULL    |       |
  | hmerominia| date         | YES  |     | NULL    |       |
  | dept_id   | int          | NO   | MUL | NULL    |       |
  +-----------+--------------+------+-----+---------+-------+
  6 rows in set (0.00 sec)
```

**Interpretation of the result columns:**

| Result Column | Meaning |
|---|---|
| **Field** | Column name |
| **Type** | Data type |
| **Null** | `YES` = NULL allowed, `NO` = NOT NULL |
| **Key** | `PRI` = Primary Key, `UNI` = UNIQUE, `MUL` = Foreign Key / Non-unique Index |
| **Default** | Default value (NULL if not set) |
| **Extra** | Additional information (e.g., `auto_increment`) |

**Exam Note:** `DESCRIBE` is a **metadata inspection** statement — it does not return the table's data but its **structure**. To see the data, `SELECT` is required.

---

## Modifying the Table Schema (ALTER TABLE)
*Modifying the Table Schema*

The `ALTER TABLE` statement allows the **modification of an existing table's structure** without having to drop it and recreate it. It is especially useful in production environments where the table already contains data.

**Analogy**: `ALTER TABLE` is like renovating a building in use — we add or remove rooms while the building remains operational. `DROP TABLE` + `CREATE TABLE` would correspond to demolishing and rebuilding from scratch.

```text
  ALTER TABLE clauses:
  
  +------------------+-----------------------------------------+
  |     Keyword      |  Action                                 |
  +------------------+-----------------------------------------+
  | ADD              | Adds a new column (at the end)          |
  | MODIFY           | Changes type/constraints of a column    |
  | CHANGE           | Renames + changes the column type       |
  | DROP COLUMN      | Removes a column (and its data)         |
  +------------------+-----------------------------------------+
```

---

### ADD
*Adding a New Column at the End*

The `ADD` clause adds a **new column** at the end of the table. Existing rows automatically receive `NULL` in the new column (or the `DEFAULT` value if one was set).

**Basic syntax:**

```sql
ALTER TABLE table_name
    ADD column_name datatype [constraints];
```

**Example — Adding column `tilefono` to table `Foititis`:**

**Before:**

```text
  mysql> DESCRIBE Foititis;
  +-----------+--------------+------+-----+---------+-------+
  | Field     | Type         | Null | Key | Default | Extra |
  +-----------+--------------+------+-----+---------+-------+
  | am        | int          | NO   | PRI | NULL    |       |
  | onoma     | varchar(50)  | NO   |     | NULL    |       |
  | eponymo   | varchar(50)  | NO   |     | NULL    |       |
  | email     | varchar(100) | YES  | UNI | NULL    |       |
  | hmerominia| date         | YES  |     | NULL    |       |
  | dept_id   | int          | NO   | MUL | NULL    |       |
  +-----------+--------------+------+-----+---------+-------+
```

**Execution:**

```sql
ALTER TABLE Foititis
    ADD tilefono VARCHAR(15);
```

**After:**

```text
  mysql> DESCRIBE Foititis;
  +-----------+--------------+------+-----+---------+-------+
  | Field     | Type         | Null | Key | Default | Extra |
  +-----------+--------------+------+-----+---------+-------+
  | am        | int          | NO   | PRI | NULL    |       |
  | onoma     | varchar(50)  | NO   |     | NULL    |       |
  | eponymo   | varchar(50)  | NO   |     | NULL    |       |
  | email     | varchar(100) | YES  | UNI | NULL    |       |
  | hmerominia| date         | YES  |     | NULL    |       |
  | dept_id   | int          | NO   | MUL | NULL    |       |
  | tilefono  | varchar(15)  | YES  |     | NULL    |       |  <-- New column
  +-----------+--------------+------+-----+---------+-------+
```

**Adding a column with a DEFAULT value:**

```sql
-- The new column receives the value 1 (active) for the existing rows
ALTER TABLE Foititis
    ADD energos TINYINT DEFAULT 1;
```

**Exam Note:** `ADD` always places the new column **at the end** of the table. To place it at a specific position, the syntax `ADD column_name datatype AFTER other_column` or `ADD column_name datatype FIRST` is used.

---

### MODIFY
*Changing the Data Type of an Existing Column*

The `MODIFY` clause changes the **data type** and/or the **constraints** of an existing column, **without changing its name**.

**Basic syntax:**

```sql
ALTER TABLE table_name
    MODIFY column_name new_datatype [new_constraints];
```

**Example — Extending the `VARCHAR` column `onoma`:**

**Before:** `onoma VARCHAR(50) NOT NULL`

**Execution:**

```sql
-- Extending the character limit from 50 to 100
ALTER TABLE Foititis
    MODIFY onoma VARCHAR(100) NOT NULL;
```

**After:** `onoma VARCHAR(100) NOT NULL`

**Example — Adding a DEFAULT value to an existing column:**

```sql
-- Setting a default value in the tilefono column
ALTER TABLE Foititis
    MODIFY tilefono VARCHAR(15) DEFAULT 'N/A';
```

**Exam Note:** When using `MODIFY`, **the full definition** of the column (type + constraints) **must be restated**. If an existing constraint (e.g., `NOT NULL`) is omitted, **it will be removed** from the column.

---

### CHANGE
*Renaming a Column with a Simultaneous Declaration of a New Type*

The `CHANGE` clause allows the **simultaneous change of a column's name AND type**. It always requires declaring both the name and the type, even if only one of them changes.

**Basic syntax:**

```sql
ALTER TABLE table_name
    CHANGE old_column_name new_column_name new_datatype [constraints];
```

**Example — Renaming `onoma` to `prwto_onoma` with a new type:**

**Before:** `onoma VARCHAR(100) NOT NULL`

**Execution:**

```sql
-- Renaming and changing the type simultaneously
ALTER TABLE Foititis
    CHANGE onoma prwto_onoma VARCHAR(80) NOT NULL;
```

**After:** `prwto_onoma VARCHAR(80) NOT NULL`

**Example — Renaming only (the type does not change):**

```sql
-- Even if the type does not change, it must be declared again
ALTER TABLE Foititis
    CHANGE tilefono arithmos_tilefonou VARCHAR(15) DEFAULT 'N/A';
```

**Comparative Table: `MODIFY` vs `CHANGE`:**

| Characteristic | `MODIFY` | `CHANGE` |
|---|---|---|
| **Changing the column name** | Not supported | Supported |
| **Changing the data type** | Supported | Supported |
| **Changing constraints** | Supported | Supported |
| **Syntax** | `MODIFY col_name new_type` | `CHANGE old_name new_name new_type` |
| **Requirement of a new name** | No (uses the same one) | Yes (always required) |

**Key Distinction:** `CHANGE` requires declaring the **new definition** of the column (type + constraints) regardless of whether anything changes. If the type is not restated, the statement will fail syntactically.

---

### DROP COLUMN
*Removing a Column — Causes Data Loss*

The `DROP COLUMN` clause **permanently removes** a column from the table along with **all the data** that column contained in every row. The action is **irreversible**.

**Basic syntax:**

```sql
ALTER TABLE table_name
    DROP COLUMN column_name;
```

**Example — Removing column `tilefono`:**

**Before (for all rows):**

```text
  +----+---------+---------+---------------------+------------+---------+-----------+
  | am | onoma   | eponymo | email               | hmerominia | dept_id | tilefono  |
  +----+---------+---------+---------------------+------------+---------+-----------+
  |  1 | Alexis  | Nikolop | alex@example.com    | 2001-05-10 |       1 | 694123456 |
  |  2 | Eleni   | Papadi  | eleni@example.com   | 2002-09-15 |       2 | NULL      |
  +----+---------+---------+---------------------+------------+---------+-----------+
```

**Execution:**

```sql
ALTER TABLE Foititis
    DROP COLUMN tilefono;
```

**After:**

```text
  +----+---------+---------+---------------------+------------+---------+
  | am | onoma   | eponymo | email               | hmerominia | dept_id |
  +----+---------+---------+---------------------+------------+---------+
  |  1 | Alexis  | Nikolop | alex@example.com    | 2001-05-10 |       1 |
  |  2 | Eleni   | Papadi  | eleni@example.com   | 2002-09-15 |       2 |
  +----+---------+---------+---------------------+------------+---------+
```

The data of column `tilefono` (694123456, NULL) was **permanently lost**.

**Exam Note:** `DROP COLUMN` is the only `ALTER TABLE` clause that causes **data loss** — all the data of the removed column in every row of the table is permanently deleted. Verification and a backup are always required before executing it.

---

## Comparative Table: DDL Commands
*Comparative Table: DDL Commands*

| Command | Category | Affects | Reversible? | Risk of Data Loss |
|---|---|---|---|---|
| `CREATE DATABASE` | Database | Creates a new database | Yes (with `DROP DATABASE`) | No |
| `DROP DATABASE` | Database | Destroys database + contents | No | Yes (the entire database) |
| `USE` | Session | Active database of the current session | Yes (new `USE`) | No |
| `SHOW DATABASES` | Metadata | Displays list of databases | — (read-only) | No |
| `CREATE TABLE` | Table | Creates a new table | Yes (with `DROP TABLE`) | No |
| `DROP TABLE` | Table | Destroys table + data | No | Yes (the table) |
| `DESCRIBE` / `EXPLAIN` | Metadata | Displays table structure | — (read-only) | No |
| `ALTER TABLE ... ADD` | Table Schema | Adds a new column | Yes (with `DROP COLUMN`) | No |
| `ALTER TABLE ... MODIFY` | Table Schema | Changes column type/constraints | Partially | Potentially (if the type is incompatible) |
| `ALTER TABLE ... CHANGE` | Table Schema | Renames + changes column type | Partially | Potentially (if the type is incompatible) |
| `ALTER TABLE ... DROP COLUMN` | Table Schema | Removes column and its data | No | Yes (the column) |

---

## Summary Table of Key Concepts
*Summary Table of Key Concepts*

| Concept | Definition | Key Characteristic / Rule |
|---|---|---|
| **DDL** (Data Definition Language) | Subset of SQL for defining database structures | Implicit `COMMIT` — changes are permanent |
| **CREATE DATABASE** | Creates a new, empty database | Synonym for `CREATE SCHEMA` in MySQL |
| **DROP DATABASE** | Destroys the database + all its contents | Irreversible — deletes tables and data |
| **USE** | Sets the active database for the current session | Affects only that specific connection |
| **SHOW DATABASES** | Returns a list of available databases | Displays only the databases with access rights |
| **CREATE TABLE** | Creates a new table with a defined schema | Requires the referenced tables to already exist |
| **DROP TABLE** | Destroys the table and its data | Differs from `DELETE FROM` (preserves structure) |
| **DESCRIBE / DESC** | Displays table metadata/structure | Shows types, keys, NULL, DEFAULT |
| **ALTER TABLE ADD** | Adds a new column at the end of the table | Existing rows: NULL or DEFAULT value |
| **ALTER TABLE MODIFY** | Changes the type/constraints of an existing column | The full definition must be restated |
| **ALTER TABLE CHANGE** | Renames + changes the column type | Always requires declaring a new name AND type |
| **ALTER TABLE DROP COLUMN** | Permanently removes a column | Causes data loss — irreversible |
| **Constraint (NOT NULL)** | Prevents NULL values in a column | Violation causes an error during INSERT/UPDATE |
| **Constraint (UNIQUE)** | Ensures uniqueness of values | Allows ONE NULL (unlike `PRIMARY KEY`) |
| **Constraint (DEFAULT)** | Sets a value if none is given | Applied during INSERT without a value for the column |
| **AUTO_INCREMENT** | Automatic increment of an integer value | Usually for the Primary Key — MySQL-specific feature |
| **Implicit COMMIT** | Automatic permanent commit of DDL statements | `ROLLBACK` cannot be performed on DDL |

---

## Key Takeaways
*Key Takeaways*

- **DDL** (Data Definition Language) concerns the **definition of structures** — databases and tables — not the management of the data they contain. DML is used for data.
- Every DDL statement performs an **implicit `COMMIT`** in MySQL — structural changes are permanent and cannot be undone with `ROLLBACK`.
- `CREATE DATABASE` and `CREATE SCHEMA` are **exactly synonymous** in MySQL — they produce an identical result.
- The order of **creating and dropping tables** with Foreign Keys is critical: **the referenced table is created first, the referencing one is dropped first**.
- `DROP DATABASE` and `DROP TABLE` are **irreversible** — they permanently destroy data and structures. A backup is always required.
- `ALTER TABLE` allows modifying an **existing** table. The four basic clauses are: `ADD`, `MODIFY`, `CHANGE`, `DROP COLUMN`.
- **Key Distinction:** `MODIFY` changes type/constraints **without renaming**, while `CHANGE` allows **simultaneous renaming AND type change** — both require fully restating the column definition.
- `ALTER TABLE ... DROP COLUMN` is the only `ALTER TABLE` clause that **causes data loss** — the column's data is permanently deleted from every row.
- **Exam Note:** The `DESCRIBE` (or `DESC`) statement displays the **schema/metadata** of the table — it does not return data. For data, `SELECT * FROM table_name` is used.
- When using `MODIFY` or `CHANGE`, if an **existing constraint** (e.g., `NOT NULL`) is **omitted** from the new definition, it is **automatically removed** — this is a common mistake.
