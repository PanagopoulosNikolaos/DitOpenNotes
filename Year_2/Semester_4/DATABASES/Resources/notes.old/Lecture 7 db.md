# Introduction to SQL and Relational Algebra

This lecture introduces the standard language for database interaction, SQL (Structured Query Language), and its mathematical foundation, Relational Algebra. It covers table creation, data types, and fundamental query operations including selection, projection, aggregation, and grouping.

---

## 1. Relational Algebra Basics

Relational Algebra is a set of operations that take one or more relations as input and produce a new relation as output.

### 1.1. Unary Operations
*   **Selection ($\sigma$):** Filters tuples (rows) that satisfy a specific condition.
    *   *Notation:* $\sigma_{condition}(Relation)$
    *   *Example:* $\sigma_{Salary > 2000}(Employee)$
*   **Projection ($\Pi$):** Selects specific attributes (columns) from a relation.
    *   *Notation:* $\Pi_{attribute\_list}(Relation)$
    *   *Example:* $\Pi_{Name, Email}(Employee)$

### 1.2. Composition
Operations can be nested. The inner operation is evaluated first.
*   *Example:* $\Pi_{Name}(\sigma_{City='Athens'}(Customer))$ — "Find the names of customers living in Athens."

---

## 2. SQL Data Definition (DDL)

SQL's Data Definition Language is used to create and modify the database schema.

### 2.1. CREATE TABLE Syntax
```sql
CREATE TABLE table_name (
    column1 data_type [NOT NULL] [UNIQUE],
    column2 data_type,
    ...
    PRIMARY KEY (column_list),
    FOREIGN KEY (column_name) REFERENCES other_table(other_column)
);
```

### 2.2. Common Data Types
| Type | Description |
| :--- | :--- |
| `INT` | Integer numbers. |
| `VARCHAR(size)` | Variable-length character string. |
| `DECIMAL(p, s)` | Fixed-point number (p=precision, s=scale). |
| `DATE` | Calendar date (YYYY-MM-DD). |
| `CHAR(size)` | Fixed-length character string. |

---

## 3. SQL Data Manipulation (DML) - Basic Queries

The `SELECT` statement is the core of SQL retrieval.

### 3.1. Structure of a SELECT Query
```sql
SELECT [DISTINCT] attribute_list -- Equivalent to Projection (Π)
FROM table_list
WHERE condition                -- Equivalent to Selection (σ)
GROUP BY attribute_list        -- Grouping for aggregates
HAVING group_condition         -- Filtering after grouping
ORDER BY attribute_list [ASC|DESC]; -- Sorting
```

### 3.2. Logical Operators and Short-cuts
*   **Logical:** `AND`, `OR`, `NOT`.
*   **IN:** `WHERE City IN ('Athens', 'Patra')` (Checks against a list).
*   **BETWEEN:** `WHERE Salary BETWEEN 1000 AND 2000`.
*   **LIKE:** Pattern matching.
    *   `%` represents zero or more characters.
    *   `_` represents exactly one character.

---

## 4. Aggregate Functions and Grouping

Aggregate functions perform a calculation on a set of values and return a single value.

| Function | Description |
| :--- | :--- |
| `COUNT()` | Counts the number of rows. |
| `SUM()` | Calculates the total sum of a numeric column. |
| `AVG()` | Calculates the average value. |
| `MIN()` / `MAX()`| Finds the minimum or maximum value. |

### 4.1. The GROUP BY and HAVING Clause
*   **GROUP BY:** Collapses multiple rows into groups based on shared values in specific columns.
*   **HAVING:** Functions like a `WHERE` clause but for **groups**. It is used to filter results *after* aggregation.

---

## Solved Exercises

### Exercise 1: Relational Algebra to SQL
**Problem:** Write the SQL equivalent of $\Pi_{Title, Year}(\sigma_{Genre='Comedy'}(Movie))$.

**Solution:**
```sql
SELECT Title, Year
FROM Movie
WHERE Genre = 'Comedy';
```

### Exercise 2: Table Creation
**Problem:** Create a table `Course` with `Code` (integer PK), `Title` (string), and `Credits` (integer).

**Solution:**
```sql
CREATE TABLE Course (
    Code INT PRIMARY KEY,
    Title VARCHAR(100) NOT NULL,
    Credits INT
);
```

### Exercise 3: Pattern Matching
**Problem:** Find all customers whose names start with 'A'.

**Solution:**
```sql
SELECT *
FROM Customer
WHERE CustName LIKE 'A%';
```

### Exercise 4: Sorting Results
**Problem:** List all employees, ordered by Salary from highest to lowest.

**Solution:**
```sql
SELECT *
FROM Employee
ORDER BY Salary DESC;
```

### Exercise 5: Basic Aggregation
**Problem:** Find the total number of students in the database.

**Solution:**
```sql
SELECT COUNT(*)
FROM Student;
```

### Exercise 6: Grouping with SUM
**Problem:** For each department, find the total sum of salaries paid.

**Solution:**
```sql
SELECT DeptID, SUM(Salary)
FROM Employee
GROUP BY DeptID;
```

### Exercise 7: Filtering Groups (HAVING)
**Problem:** List departments where the average salary is greater than \$3,000.

**Solution:**
```sql
SELECT DeptID, AVG(Salary)
FROM Employee
GROUP BY DeptID
HAVING AVG(Salary) > 3000;
```

### Exercise 8: Column Aliasing and Calculation
**Problem:** Select the `LoanID` and the interest amount (8% of the `Amount`) for all loans.

**Solution:**
```sql
SELECT LoanID, Amount * 0.08 AS Interest
FROM Borrow;
```

---

## Exam Tip: WHERE vs. HAVING

> **[Key Insight]**
> This is a very common exam question.
> *   **WHERE** filters **individual rows** before any grouping happens. It cannot be used with aggregate functions (e.g., `WHERE SUM(Salary) > 1000` is **invalid**).
> *   **HAVING** filters **groups** after the `GROUP BY` clause has been processed. It is specifically designed to be used with aggregate functions.
