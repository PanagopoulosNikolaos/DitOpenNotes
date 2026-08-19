# Relational Model & Relational Algebra
*Relational Model & Relational Algebra*

---

## Table of Contents
*Table of Contents*

1. [Introduction](#introduction)
2. [Basic Elements of the Relational Model](#basic-elements-of-the-relational-model)
   - [Relations](#relations)
   - [Tuples](#tuples)
   - [Attributes](#attributes)
   - [Domains](#domains)
   - [Comparison Table of Basic Concepts](#comparison-table-of-basic-concepts)
3. [Constraints and Keys](#constraints-and-keys)
   - [Candidate Keys](#candidate-keys)
   - [Primary Key](#primary-key)
   - [Foreign Key](#foreign-key)
   - [Entity Integrity and Referential Integrity](#entity-integrity-and-referential-integrity)
   - [Referential Actions: ON DELETE / ON UPDATE](#referential-actions-on-delete--on-update)
   - [Comparative Table of Keys](#comparative-table-of-keys)
4. [Relational Algebra Operations](#relational-algebra-operations)
   - [Set-Theoretic Operations](#set-theoretic-operations)
   - [Specific Relational Operations](#specific-relational-operations)
   - [Join Operations](#join-operations)
   - [Division](#division)
5. [Summary Table of Key Concepts](#summary-table-of-key-concepts)
6. [Key Takeaways](#key-takeaways)

---

## Introduction

The **Relational Data Model** is the foundation of modern database technology. It was proposed by Edgar F. Codd in 1970 and is based on the mathematical theory of sets and relational algebra, providing a formal, precise framework for organizing and manipulating data. It is the result of **Logical Design** — the phase in which the Entity-Relationship Model (E-R) is converted into tables, keys and constraints. Understanding the relational model and **Relational Algebra** is necessary for writing correct SQL queries and for understanding how the Query Optimizer executes searches internally.

---

## Basic Elements of the Relational Model
*Basic Elements of the Relational Model*

The relational model organizes data into **relations**, which correspond to the familiar tables of SQL. Each relation is a mathematical set — without duplicate records and without a defined order of rows. The four basic concepts that define a relation are: relations, tuples, attributes and domains.

---

### Relations
*Relations*

A **Relation** is a **named set of tuples** that share the same type of structure (the same attributes). In practical application it corresponds to the **Table** of SQL.

**Characteristics**:
- Each relation has a unique **name** within the database.
- Tuples (rows) have no defined order — a set is independent of the order of its elements.
- **Duplicate tuples** (duplicate rows) are not allowed — every row must be unique.
- Each column (attribute) has a unique name within the relation.

**Analogy**: A relation is like a spreadsheet where each row corresponds to an object of the real world and each column to one of its properties. The critical difference: the spreadsheet accepts duplicate rows, while a relation does not.

```text
  Relation: EMPLOYEES
  +-------+----------+-----------+---------+
  | emp_id | last_name | first_name | dept_id |
  +-------+----------+-----------+---------+
  |   1   | Papas    | Giorgis   |   10    |
  |   2   | Nikos    | Alexis    |   20    |
  |   3   | Kostas   | Dimitris  |   10    |
  +-------+----------+-----------+---------+
  ^Tuples (Rows)^
  ^Attributes (Columns)^
```

```sql
-- Creating a relation in SQL
CREATE TABLE employees (
    emp_id     INT         PRIMARY KEY,
    last_name  VARCHAR(50) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    dept_id    INT         NOT NULL
);
```

---

### Tuples
*Tuples*

A **Tuple** is a **single record** in a relation — that is, a row of the table. Each tuple contains a value for each attribute of the relation, and every value must belong to the corresponding domain.

**Characteristics**:
- Every tuple is **unique** within the relation.
- The **order** of tuples is not significant in the relational model.
- Every value in a tuple is **atomic** — repeating groups are not allowed (1NF).

**Analogy**: A tuple is the card of a student in the registry office file — a unique record with all the information about them.

**Exam Note:** The set of tuples of a relation at a specific point in time is called the **Extension** (extension or instance), while the schema (structure) of the relation is called the **Intension** (intensive description or schema).

---

### Attributes
*Attributes*

An **Attribute** is the **column** of a relation — it corresponds to a property of the object described by the relation. Each attribute has:

- A unique **name** within the relation.
- A **domain** that defines the acceptable values.
- **One and only one value per tuple** (atomic value — 1NF property).

**Degree of a relation**: The number of attributes of a relation. A relation with 4 attributes has degree 4.

```text
  Relation EMPLOYEES — Degree: 4
  +--------+-----------+------------+---------+
  | emp_id | last_name | first_name | dept_id |   <-- 4 Attributes
  +--------+-----------+------------+---------+
  | ...    | ...       | ...        | ...     |
  +--------+-----------+------------+---------+
```

**Key Distinction:** In the E-R model, attributes are represented as ovals. In the relational model they constitute the **columns** of the table — the transition from ovals to columns is part of Logical Design.

---

### Domains
*Domains*

A **Domain** is the **set of permitted values** that an attribute can take. It acts as a semantic and formal integrity constraint.

**Examples**:
- The domain of the attribute `dept_id` is positive integers (`INT > 0`).
- The domain of `grade` can be defined as decimal numbers in the interval `[0.0, 10.0]`.
- The domain of `gender` can be defined as `{'M', 'F', 'Other'}`.

**Analogy**: The domain is like the acceptance criteria of a form — the data type defines "what", while the domain additionally defines "which values are logically acceptable".

```sql
-- Implementing a domain with a CHECK constraint
CREATE TABLE students (
    student_am  INT            PRIMARY KEY,
    grade       DECIMAL(4, 2)  CHECK (grade >= 0.0 AND grade <= 10.0),  -- Domain definition
    gender      CHAR(1)        CHECK (gender IN ('M', 'F', 'O'))        -- Domain definition
);
```

**Exam Note:** Two attributes from different relations can be compared **only if** they have **compatible domains** — e.g. two attributes of type `INT` representing identifiers are comparable even if they have different names.

---

### Comparison Table of Basic Concepts
*Comparison Table: Formal vs. SQL Terminology*

| Formal Terminology (Relational Model) | SQL Terminology | Description |
|---|---|---|
| **Relation** | Table | A set of tuples with a common structure |
| **Tuple** | Row / Record | A unique record in the relation |
| **Attribute** | Column / Field | A property/characteristic of the relation |
| **Domain** | Data Type + Constraint | Set of acceptable attribute values |
| **Degree** | Number of columns | Number of attributes of a relation |
| **Cardinality** | Number of rows | Number of tuples of a relation |
| **Relation Schema** | Table Definition | The name + the attributes of the relation |

---

## Constraints and Keys
*Constraints and Keys*

**Constraints** are rules that ensure the **integrity** and **correctness** of the data of a database. **Keys** are a special category of constraints that concern the identification and linking of tuples. Without properly defined keys, the database cannot guarantee uniqueness, referential integrity, or correct joins.

---

### Candidate Keys
*Candidate Keys*

A **Candidate Key** is a **minimal set of attributes** that uniquely identifies every tuple in a relation. It is called "minimal" because removing any attribute from this set destroys the uniqueness property.

**Candidate Key properties**:
- **Uniqueness**: There are no two tuples with the same values for the key.
- **Minimality**: No attribute of the key is redundant.

**Example**: In the relation `STUDENTS(student_am, afm, last_name, email)`:
- `student_am` is a Candidate Key (unique Registration Number).
- `afm` is a Candidate Key (unique tax ID).
- `email` is a Candidate Key (if defined as unique).
- `last_name` is **not** a Candidate Key (there may be students with the same name).

```text
  STUDENTS
  +------------+----------+-----------+--------------------+
  | student_am | afm      | last_name | email              |
  +------------+----------+-----------+--------------------+
  | 10001      | 123456789| Papas     | papas@uni.gr       |
  | 10002      | 987654321| Nikos     | nikos@uni.gr       |
  +------------+----------+-----------+--------------------+
  
  Candidate Keys: {student_am}, {afm}, {email}
  NOT a Candidate Key: {last_name}  -- Not unique
```

**Key Distinction:** Every relation can have **multiple Candidate Keys**. From these, **one** is selected as the Primary Key. The rest are called **Alternate Keys** and are implemented with the `UNIQUE` constraint.

---

### Primary Key
*Primary Key*

The **Primary Key (PK)** is the **selected Candidate Key** defined as the main identifier of every tuple in a relation. The selection is made by the database designer and is explicitly defined in the DDL.

**Primary Key rules**:
- PK values must be **unique** for every tuple.
- PK values **cannot be NULL** (Entity Integrity rule).
- The value must not change over time (stability).

**Analogy**: The tax ID (AFM) of a citizen is a Primary Key — unique, stable, and cannot be empty. The full name, on the other hand, is not a reliable PK because it can change (marriage) or there may be people with the same name.

```sql
-- Simple Primary Key
CREATE TABLE departments (
    dept_id   INT         PRIMARY KEY,          -- One attribute
    dept_name VARCHAR(50) NOT NULL UNIQUE
);

-- Composite Primary Key
CREATE TABLE enrollments (
    student_am  INT  NOT NULL,
    course_id   INT  NOT NULL,
    grade       DECIMAL(4, 2),
    PRIMARY KEY (student_am, course_id)         -- Composite: two attributes together
);
```

In relation schemas, the Primary Key is underlined:

`Employee(<u>emp_id</u>, last_name, first_name, #dept_id)`

---

### Foreign Key
*Foreign Key*

The **Foreign Key (FK)** is an attribute (or set of attributes) of a relation that **refers to the Primary Key of another (or the same) relation**, creating a connection bridge between tables.

**Foreign Key properties**:
- Every FK value must **exist in the referenced relation** as a PK value, or be `NULL` (if allowed).
- Determines the **Referential Integrity** of the database.
- Can refer to **any Candidate Key**, not only the PK (more rarely).

**Analogy**: The department code (`dept_id`) of an employee acts like an index in a book — it points to a specific department that exists in the `DEPARTMENTS` table. If the department does not exist, the pointer is broken.

```text
  DEPARTMENTS                          EMPLOYEES
  +-------+---------+                 +--------+-----------+--------+
  | dept_id| dept_name|                | emp_id | last_name | dept_id|
  +-------+---------+                 +--------+-----------+--------+
  |  10   | Accounting|       +------>|   1   | Papas     |  10    |
  |  20   | IT      |        |       |   2   | Nikos     |  20    |
  +-------+---------+        |       |   3   | Alexis    |  10    |
  ^Primary Key^              |       +--------+-----------+--------+
                             |                              ^
                             +------ Foreign Key ----------+
```

```sql
-- Defining a Foreign Key
CREATE TABLE employees (
    emp_id    INT         PRIMARY KEY,
    last_name VARCHAR(50) NOT NULL,
    dept_id   INT         NOT NULL,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
        ON DELETE RESTRICT       -- Prevents deletion if dependent records exist
        ON UPDATE CASCADE        -- Automatically updates the FK if the PK changes
);
```

In relation schemas, the Foreign Key is marked with `#`:

`Employee(<u>emp_id</u>, last_name, first_name, #dept_id)`

---

### Entity Integrity and Referential Integrity
*Entity Integrity and Referential Integrity*

Two fundamental integrity rules of the relational model ensure the reliability of the data:

#### Entity Integrity

**Rule**: No attribute that is part of the **Primary Key** can have a `NULL` value.

- **Rationale**: The PK is the unique identifier of a tuple. If it is `NULL`, the tuple cannot be identified, so its existence has no meaning.
- **Violation example**: `INSERT INTO employees VALUES (NULL, 'Papas', 10)` — prohibited by every DBMS.

```sql
-- The DBMS automatically rejects NULL values in a PK
INSERT INTO departments VALUES (NULL, 'New Department');  -- ERROR: Column 'dept_id' cannot be null
```

#### Referential Integrity

**Rule**: Every value of a **Foreign Key** must exist as a Primary Key value in the referenced relation, or be `NULL`.

- **Rationale**: An FK that points to a non-existent record creates an "orphan record" (dangling reference), which corrupts the results of Joins.
- **Violation example**: Adding an employee with `dept_id = 99` while department 99 does not exist.

```sql
-- Referential Integrity Violation
INSERT INTO employees VALUES (5, 'Kostas', 99);
-- ERROR: Foreign key constraint fails: dept_id=99 does not exist in DEPARTMENTS
```

**Exam Note:** **Entity Integrity** concerns exclusively the **PK** (no NULL). **Referential Integrity** concerns the **FK** (the reference must exist). The two rules are independent of each other.

---

### Referential Actions: ON DELETE / ON UPDATE
*Referential Actions: ON DELETE / ON UPDATE*

When a **referenced** primary key is **deleted** or **updated**, the DBMS must decide what happens to the foreign keys that point to it. This decision is specified by **referential actions** in the `FOREIGN KEY` clause.

| Action | Behavior on DELETE/UPDATE of the parent | Typical use |
|---|---|---|
| **`CASCADE`** | The change propagates to the dependent rows — they are **deleted or updated automatically** | Strong/weak (identifying) relationships; composition where the child cannot exist alone |
| **`SET NULL`** | The foreign key of dependent rows is set to `NULL` | Optional relationships where the child may survive without the parent (FK must allow `NULL`) |
| **`RESTRICT`** | The operation is **rejected** if dependent rows exist | Protecting master data from accidental deletion |
| **`NO ACTION`** | Like `RESTRICT`, but checked **after** the statement | Standard SQL default; allows deferred checks |
| **`SET DEFAULT`** | The foreign key is set to its **default value** | Rare; used when a valid fallback row exists |

```sql
-- Full referential-action examples
CREATE TABLE enrollments (
    student_am INT NOT NULL,
    course_id  INT NOT NULL,
    PRIMARY KEY (student_am, course_id),
    FOREIGN KEY (student_am) REFERENCES students(am)
        ON DELETE CASCADE     -- deleting a student removes their enrollments
        ON UPDATE CASCADE,    -- changing the AM propagates to enrollments
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
        ON DELETE RESTRICT    -- a course with enrollments cannot be deleted
        ON UPDATE CASCADE
);
```

**Selection guidance**:
- **Identifying/weak entity** (child cannot exist alone) → `ON DELETE CASCADE`.
- **Optional association** (child may become parentless) → `ON DELETE SET NULL`.
- **Master/aggregate data** that must never be orphaned or silently removed → `ON DELETE RESTRICT`.

**Key Distinction:** `CASCADE`, `SET NULL` and `SET DEFAULT` **modify** the dependent rows to preserve referential integrity, while `RESTRICT` and `NO ACTION` **block** the operation. `CASCADE` is the most dangerous to apply carelessly because a single parent deletion can erase many related rows.

---

### Comparative Table of Keys

| Key Type | Definition | NULL value? | Multiple? | SQL Implementation |
|---|---|---|---|---|
| **Candidate Key** | Minimal set of uniqueness attributes | Depends | Yes (many per relation) | `UNIQUE NOT NULL` |
| **Primary Key (PK)** | The selected Candidate Key | Never | No (one per relation) | `PRIMARY KEY` |
| **Alternate Key** | Candidate Key not selected as PK | Usually not | Yes | `UNIQUE` |
| **Foreign Key (FK)** | Attribute referring to the PK of another relation | Allowed | Yes (many per relation) | `FOREIGN KEY ... REFERENCES` |
| **Composite Key** | Key from a combination of multiple attributes | Partially not | Yes | `PRIMARY KEY (col1, col2)` |
| **Surrogate Key** | Artificial identifier (e.g. auto-increment) | Never | No | `INT AUTO_INCREMENT PRIMARY KEY` |

---

## Relational Algebra Operations
*Relational Algebra Operations*

**Relational Algebra** is a **formal system of operations** that takes one or two relations as input and produces a new relation as output. It constitutes the **theoretical basis** for Query Processing — the Query Optimizer of every DBMS internally translates SQL queries into relational algebra expressions.

The operations are divided into three categories:
1. **Set-Theoretic Operations**: Union, Intersection, Difference, Cartesian Product.
2. **Specific Relational Operations**: Selection, Projection.
3. **Joins**: Inner Join and its variants.

---

### Set-Theoretic Operations
*Set-Theoretic Operations*

These operations originate from set theory. **Union**, **Intersection** and **Difference** require **union-compatible relations** — the same number of attributes with compatible domains.

#### Union ($\cup$)

The **Union** of two relations $R$ and $S$ produces a new relation that contains **all the tuples** that belong to at least one of the two relations. Duplicates are removed automatically.

$$R \cup S = \{t \mid t \in R \lor t \in S\}$$

**Example**: Finding all employees who work in department 10 OR in department 20.

```text
  R (Dept 10)            S (Dept 20)            R ∪ S
  +------+------+       +------+------+       +------+------+
  | id   | name |       | id   | name |       | id   | name |
  +------+------+       +------+------+       +------+------+
  |  1   | A    |       |  3   | C    |  -->  |  1   | A    |
  |  2   | B    |       |  1   | A    |       |  2   | B    |  <- Duplicate removed
  +------+------+       +------+------+       |  3   | C    |
                                              +------+------+
```

```sql
-- SQL implementation of Union (removes duplicates)
SELECT emp_id, last_name FROM dept_10_employees
UNION
SELECT emp_id, last_name FROM dept_20_employees;

-- UNION ALL: keeps duplicates (faster if dedup is not needed)
SELECT emp_id, last_name FROM dept_10_employees
UNION ALL
SELECT emp_id, last_name FROM dept_20_employees;
```

#### Intersection ($\cap$)

The **Intersection** of two relations $R$ and $S$ produces a new relation that contains **only the tuples** that belong to **both** relations simultaneously.

$$R \cap S = \{t \mid t \in R \land t \in S\}$$

**Example**: Finding employees who work simultaneously in project A AND in project B.

```text
  R (Project A)         S (Project B)         R ∩ S
  +------+------+       +------+------+       +------+------+
  |  1   | A    |       |  2   | B    |  -->  |  2   | B    |  <- Common tuple
  |  2   | B    |       |  2   | B    |       +------+------+
  |  3   | C    |       |  4   | D    |
  +------+------+       +------+------+
```

```sql
-- SQL implementation of Intersection
SELECT emp_id, last_name FROM project_a_employees
INTERSECT
SELECT emp_id, last_name FROM project_b_employees;
```

#### Difference ($-$)

The **Difference** $R - S$ produces a new relation with the tuples that **belong to $R$ but NOT to $S$**. The operation is not commutative — $R - S \neq S - R$.

$$R - S = \{t \mid t \in R \land t \notin S\}$$

**Example**: Finding students who enrolled in course A but NOT in course B.

```text
  R (Course A)          S (Course B)          R - S
  +------+------+       +------+------+       +------+------+
  |  1   | A    |       |  2   | B    |  -->  |  1   | A    |
  |  2   | B    |       |  4   | D    |       |  3   | C    |
  |  3   | C    |       +------+------+       +------+------+
  +------+------+
```

```sql
-- SQL implementation of Difference
SELECT student_am, last_name FROM course_a_students
EXCEPT
SELECT student_am, last_name FROM course_b_students;

-- Alternative with NOT IN (broader support in MySQL)
SELECT student_am, last_name
FROM   course_a_students
WHERE  student_am NOT IN (SELECT student_am FROM course_b_students);
```

#### Cartesian Product ($\times$)

The **Cartesian Product** $R \times S$ produces a new relation that contains **every possible combination** of a tuple from $R$ with a tuple from $S$.

$$R \times S = \{(r, s) \mid r \in R \land s \in S\}$$

**Size of the result**: If $|R| = m$ and $|S| = n$, then $|R \times S| = m \times n$ tuples.

**Exam Note:** The Cartesian Product is **rarely used on its own** — it produces redundant, meaningless combinations. It becomes useful when combined with Selection ($\sigma$) to form a **Join**. In SQL, `FROM R, S` without `WHERE` produces a Cartesian Product.

```text
  R (2 tuples)           S (3 tuples)           R × S (2×3 = 6 tuples)
  +----+----+          +----+----+            +----+----+----+----+
  | A  | B  |          | C  | D  |            | A  | B  | C  | D  |
  +----+----+          +----+----+            +----+----+----+----+
  | 1  | x  |    X     | 10 | p  |   -->      | 1  | x  | 10 | p  |
  | 2  | y  |          | 20 | q  |            | 1  | x  | 20 | q  |
  +----+----+          | 30 | r  |            | 1  | x  | 30 | r  |
                       +----+----+            | 2  | y  | 10 | p  |
                                              | 2  | y  | 20 | q  |
                                              | 2  | y  | 30 | r  |
                                              +----+----+----+----+
```

```sql
-- SQL implementation of Cartesian Product (avoided in practice)
SELECT * FROM employees, departments;           -- Old syntax
SELECT * FROM employees CROSS JOIN departments; -- Modern syntax
```

---

### Specific Relational Operations
*Specific Relational Operations*

These operations are defined on the basis of the relational model and have no direct counterpart in set theory.

#### Selection ($\sigma$)

**Selection** is a **horizontal** operation that returns the tuples of a relation that **satisfy some condition** (predicate). It does not change the columns — it selects rows.

$$\sigma_{\text{predicate}}(R)$$

**Examples**:

$$\sigma_{\text{dept\_id} = 10}(\text{EMPLOYEES})$$

$$\sigma_{\text{grade} \geq 5.0 \land \text{grade} \leq 10.0}(\text{ENROLLMENTS})$$

```text
  EMPLOYEES (initial)          $\sigma$_{dept_id=10}(EMPLOYEES)
  +------+----------+--------+       +------+----------+--------+
  | id   | name     |dept_id |  -->  | id   | name     |dept_id |
  +------+----------+--------+       +------+----------+--------+
  |  1   | Papas    |  10    |       |  1   | Papas    |  10    |
  |  2   | Nikos    |  20    |       |  3   | Alexis   |  10    |
  |  3   | Alexis   |  10    |       +------+----------+--------+
  +------+----------+--------+
```

```sql
-- SQL implementation of Selection: the WHERE clause
SELECT * FROM employees WHERE dept_id = 10;

-- Composite selection condition
SELECT * FROM enrollments WHERE grade >= 5.0 AND grade <= 10.0;
```

**Relational Algebra — SQL correspondence**:

| Relational Algebra | SQL |
|---|---|
| $\sigma_{\text{condition}}(R)$ | `SELECT * FROM R WHERE condition` |

#### Projection ($\pi$)

**Projection** is a **vertical** operation that returns **specific columns** (attributes) of a relation, removing the rest. It also removes duplicate tuples that may arise.

$$\pi_{\text{attr\_list}}(R)$$

**Example**: Projecting only names and departments from `EMPLOYEES`:

$$\pi_{\text{last\_name, dept\_id}}(\text{EMPLOYEES})$$

```text
  EMPLOYEES (initial)          $\pi$_{last_name, dept_id}(EMPLOYEES)
  +------+----------+--------+       +----------+--------+
  | id   | name     |dept_id |  -->  | name     |dept_id |
  +------+----------+--------+       +----------+--------+
  |  1   | Papas    |  10    |       | Papas    |  10    |
  |  2   | Nikos    |  20    |       | Nikos    |  20    |
  |  3   | Alexis   |  10    |       | Alexis   |  10    |
  +------+----------+--------+       +----------+--------+
```

```sql
-- SQL implementation of Projection: specifying columns in SELECT
SELECT last_name, dept_id FROM employees;

-- With a different name (alias)
SELECT last_name AS surname, dept_id AS department FROM employees;
```

**Combination of Selection and Projection**:

$$\pi_{\text{last\_name}}(\sigma_{\text{dept\_id}=10}(\text{EMPLOYEES}))$$

```sql
-- Combination of Projection + Selection
SELECT last_name FROM employees WHERE dept_id = 10;
```

**Relational Algebra — SQL correspondence**:

| Relational Algebra | SQL |
|---|---|
| $\pi_{\text{col1, col2}}(R)$ | `SELECT col1, col2 FROM R` |
| $\pi_{\text{cols}}(\sigma_{\text{cond}}(R))$ | `SELECT cols FROM R WHERE cond` |

---

### Join Operations
*Join Operations*

The **Join** is the most important relational algebra operation for practical applications — it allows the **combination of data** from two or more relations based on a join condition.

#### Inner Join ($\bowtie$)

The **Inner Join** returns **only the tuples** that have **matching values** in both relations. Tuples without a match are excluded from the result.

**Formal definition** (as a special case of Cartesian Product + Selection):

$$R \bowtie_{\theta} S = \sigma_{\theta}(R \times S)$$

**Example**: Finding an employee's name and their department:

$$\text{EMPLOYEES} \bowtie_{\text{EMPLOYEES.dept\_id = DEPARTMENTS.dept\_id}} \text{DEPARTMENTS}$$

```text
  EMPLOYEES                          DEPARTMENTS
  +------+----------+--------+       +--------+-----------+
  | id   | name     |dept_id |       |dept_id | dept_name |
  +------+----------+--------+       +--------+-----------+
  |  1   | Papas    |  10    |       |   10   | Accounting|
  |  2   | Nikos    |  20    |       |   20   | IT        |
  |  3   | Alexis   |  10    |       |   30   | Legal     |
  +------+----------+--------+       +--------+-----------+
  
  EMPLOYEES INNER JOIN DEPARTMENTS ON EMPLOYEES.dept_id = DEPARTMENTS.dept_id:
  
  +------+----------+--------+--------+-----------+
  | id   | name     |dept_id |dept_id | dept_name |
  +------+----------+--------+--------+-----------+
  |  1   | Papas    |  10    |   10   | Accounting|   <- Matched
  |  2   | Nikos    |  20    |   20   | IT        |   <- Matched
  |  3   | Alexis   |  10    |   10   | Accounting|   <- Matched
  +------+----------+--------+--------+-----------+
  The department "Legal" (dept_id=30) does not appear — no employee belongs to it.
```

```sql
-- SQL implementation of Inner Join (modern syntax)
SELECT e.emp_id,
       e.last_name,
       d.dept_name
FROM   employees  AS e
INNER JOIN departments AS d ON e.dept_id = d.dept_id;

-- Alternative old syntax (discouraged)
SELECT e.emp_id, e.last_name, d.dept_name
FROM   employees e, departments d
WHERE  e.dept_id = d.dept_id;
```

**Relational Algebra — SQL correspondence**:

| Relational Algebra | SQL |
|---|---|
| $R \bowtie_{\theta} S$ | `SELECT ... FROM R INNER JOIN S ON $\theta$` |

**Key Distinction:** The Inner Join returns **only** tuples with a match on both sides. For tuples without a match (e.g. a department without employees, or an employee without a department), the **Outer Joins** (`LEFT JOIN`, `RIGHT JOIN`, `FULL OUTER JOIN`) are required — concepts that extend the basic relational model.

```sql
-- LEFT OUTER JOIN: Returns ALL employees,
-- even if they do not have a corresponding department
SELECT e.emp_id,
       e.last_name,
       d.dept_name
FROM   employees  AS e
LEFT JOIN departments AS d ON e.dept_id = d.dept_id;
```

**Combination of multiple operations** — Example of a complex query:

Finding the names of employees of the "IT" department with a salary above 2000:

$$\pi_{\text{last\_name, first\_name}}(\sigma_{\text{dept\_name='IT'} \land \text{salary}>2000}(\text{EMPLOYEES} \bowtie \text{DEPARTMENTS}))$$

```sql
SELECT   e.last_name,
         e.first_name
FROM     employees    AS e
INNER JOIN departments AS d ON e.dept_id = d.dept_id
WHERE    d.dept_name = 'IT'
  AND    e.salary    > 2000;
```

---

### Division
*Division*

The **Division** operator, denoted $R \div S$, answers **"for all"** queries — tuples of $R$ that are related to **every** tuple of $S$. It is the one standard relational algebra operation that cannot be expressed by a single SQL keyword and must be expressed through a **double negation** (`NOT EXISTS`/`NOT IN`).

**Formal definition**: Let $R(A, B)$ and $S(B)$. The division $R \div S$ returns the values of $A$ such that the corresponding set of $B$ values in $R$ **contains** the entire set $S$.

$$R \div S = \{t[A] \mid t \in R \land S \subseteq \{u[B] \mid u \in R \land u[A] = t[A]\}\}$$

**Requirements**: The attribute set of $S$ must be a **proper subset** of the attribute set of $R$. The result has only the attributes $A = R - S$.

**Worked Example**: Find the passengers who have booked **all** flights departing from `ATH`.

```text
   R = BOOKINGS(passenger, flight)       S = ATH_FLIGHTS(flight)
   +-----------+--------+                +--------+
   | passenger | flight |                | flight |
   +-----------+--------+                +--------+
   |  Maria    |  OA101 |                |  OA101 |
   |  Maria    |  OA202 |                |  OA202 |
   |  Kostas   |  OA101 |                +--------+
   |  Kostas   |  OA202 |
   |  Kostas   |  A3303 |
   +-----------+--------+

   BOOKINGS ÷ ATH_FLIGHTS:
   +-----------+
   | passenger |
   +-----------+
   |  Maria    |  <- has BOTH OA101 and OA202
   |  Kostas   |  <- has BOTH OA101 and OA202 (and more)
   +-----------+
```

**Equivalent SQL pattern** — via double negation:

```sql
SELECT passenger
FROM   bookings
WHERE  NOT EXISTS (
    SELECT 1
    FROM   ath_flights
    WHERE  NOT EXISTS (
        SELECT 1
        FROM   bookings AS b
        WHERE  b.passenger = bookings.passenger
          AND  b.flight    = ath_flights.flight
    )
);
```

**Relational Algebra — SQL correspondence**:

| Relational Algebra | SQL |
|---|---|
| $R \div S$ | Double `NOT EXISTS` (or `NOT IN`) with a correlated subquery |

**Exam Note:** Division is the tool for **"for all"** queries: *"entities that participate in **all** instances of a related set"* (e.g. members who borrowed all books of a publisher, passengers on all ATH flights). It can be derived from the set-theoretic identity $R \div S = \pi_A(R) - \pi_A\big((\pi_A(R) \times S) - R\big)$.

---

## Summary Table of Key Concepts
*Summary Table of Key Concepts*

| Concept | Definition | Key Characteristic / Rule |
|---|---|---|
| **Relation** | Named set of tuples with a common structure | Corresponds to the SQL Table — no duplicates |
| **Tuple** | A unique record in a relation | Corresponds to the SQL Row — order is not significant |
| **Attribute** | Property/characteristic of a relation | Corresponds to the SQL Column — atomic value |
| **Domain** | Set of permitted attribute values | Implemented with data type + CHECK constraint |
| **Candidate Key** | Minimal set for unique identification | Many per relation — one becomes PK |
| **Primary Key (PK)** | The selected Candidate Key | Never NULL — unique identifier of a tuple |
| **Foreign Key (FK)** | Attribute referring to the PK of another relation | Bridge linking tables — referential integrity |
| **Entity Integrity** | PK never NULL | Fundamental integrity rule of the relational model |
| **Referential Integrity** | FK must refer to an existing PK | Prevents "orphan records" |
| **Union ($\cup$)** | All tuples of R or S (union-compatible) | Removes duplicates — `UNION` in SQL |
| **Intersection ($\cap$)** | Only tuples common to R and S | `INTERSECT` in SQL |
| **Difference ($-$)** | Tuples of R not present in S | Not commutative — `EXCEPT` in SQL |
| **Cartesian Product ($\times$)** | Every combination of tuples of R and S | $\|R\| \times \|S\|$ tuples — `CROSS JOIN` |
| **Selection ($\sigma$)** | Horizontal filtering of tuples | Corresponds to the `WHERE` of SQL |
| **Projection ($\pi$)** | Vertical selection of attributes | Corresponds to `SELECT col1, col2` |
| **Inner Join ($\bowtie$)** | Joining tuples with common values | Excludes tuples without a match |
| **Division (÷)** | Tuples related to **all** tuples of another relation | Answers "for all" queries — double `NOT EXISTS` |
| **Referential Actions** | Behavior of FK on parent delete/update | `CASCADE`, `SET NULL`, `RESTRICT`, `NO ACTION`, `SET DEFAULT` |

---

## Key Takeaways
*Key Takeaways*

- The **Relational Model** organizes data into relations (tables) consisting of tuples (rows) and attributes (columns) — every value must belong to the Domain of its attribute.
- **Key Distinction:** Relation = mathematical set (no order, no duplicates). Table = SQL implementation (accepts duplicates if no PK/UNIQUE exists).
- Every relation can have **multiple Candidate Keys** — one is selected as the **Primary Key** (never NULL). The rest become **Alternate Keys** with `UNIQUE`.
- **Entity Integrity** prohibits NULL values in the PK. **Referential Integrity** ensures that every FK refers to an existing PK.
- **Relational Algebra** is the theoretical basis of SQL — every SQL query is internally translated into relational algebra expressions by the Query Optimizer.
- **Set-Theoretic Operations** (Union, Intersection, Difference) require **union-compatible relations** — the same number of attributes with compatible domains.
- The **Cartesian Product** $R \times S$ produces $|R| \times |S|$ tuples — rarely useful on its own, it is the basis for understanding the Join.
- **Selection ($\sigma$)** filters **rows** (horizontally), **Projection ($\pi$)** filters **columns** (vertically). Their combination corresponds to `SELECT col FROM table WHERE cond` in SQL.
- **Exam Note:** The **Inner Join** returns only tuples with a match in both relations. Tuples without a match (e.g. a department without employees) are excluded — the Outer Joins are required for them.
- The **correct use of keys** (PK, FK, Candidate Keys) and adherence to the integrity rules is the basis for a reliable, consistent database without orphaned or contradictory records.
- **Division ($\div$)** answers **"for all"** queries — tuples related to every tuple of a set — and is expressed in SQL through a double `NOT EXISTS` (or `NOT IN`) pattern.
- **Referential actions** decide what happens to foreign keys when the referenced row is deleted or updated: `CASCADE` propagates the change, `SET NULL` orphans the child, and `RESTRICT` blocks the operation.
- **Key Distinction:** `CASCADE`/`SET NULL`/`SET DEFAULT` modify dependent rows to preserve integrity; `RESTRICT`/`NO ACTION` reject the operation entirely.
