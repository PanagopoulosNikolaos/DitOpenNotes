# Lecture 03: SQL Data Definition and Manipulation

This lecture introduces Structured Query Language (SQL), the declarative standard for relational databases. It covers Data Definition Language (DDL) constraints, Data Manipulation Language (DML), and complex Data Query Language (DQL) constructs including multi-table joins, subqueries, grouping, and aggregations.

---

## 1. Data Definition Language (DDL)

DDL commands create, modify, and drop relational schema structures and enforce integrity constraints.

### 1.1 Integrity Constraints
- **Primary Key (`PRIMARY KEY`):** Enforces entity integrity; unique and non-null for every tuple.
- **Foreign Key (`FOREIGN KEY`):** Enforces referential integrity; references an existing primary or candidate key in another table.
- **Unique (`UNIQUE`):** Enforces candidate key uniqueness, but allows `NULL` values where permitted.
- **Check (`CHECK`):** Enforces arbitrary domain predicates.
- **Not Null (`NOT NULL`):** Forbids missing values.

### 1.2 Table Definition Example

```sql
CREATE TABLE department (
    dept_id INTEGER PRIMARY KEY,
    dept_name VARCHAR(50) NOT NULL UNIQUE,
    budget NUMERIC(12, 2) CHECK (budget >= 0)
);

CREATE TABLE employee (
    emp_id INTEGER PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    salary NUMERIC(10, 2) DEFAULT 30000.00 CHECK (salary > 0),
    dept_id INTEGER NOT NULL,
    FOREIGN KEY (dept_id) REFERENCES department(dept_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);
```

---

## 2. Data Manipulation Language (DML)

DML statements populate and modify relation instances:

```sql
-- Inserting records
INSERT INTO department (dept_id, dept_name, budget)
VALUES (1, 'Computer Science', 750000.00);

-- Updating records
UPDATE employee
SET salary = salary * 1.05
WHERE dept_id = 1;

-- Deleting records
DELETE FROM employee
WHERE emp_id = 105;
```

---

## 3. Data Query Language (DQL): The SELECT Statement

The canonical SQL query structure executes in a strict logical order:

```sql
SELECT [DISTINCT] select_list
FROM table_references
[WHERE where_condition]
[GROUP BY grouping_expressions]
[HAVING having_condition]
[ORDER BY sort_expressions [ASC | DESC]]
[LIMIT row_count];
```

### 3.1 Logical Query Processing Order
1. `FROM` (computes Cartesian products and joins)
2. `WHERE` (filters individual rows before grouping)
3. `GROUP BY` (partitions rows into groups based on key values)
4. `HAVING` (filters groups based on aggregate conditions)
5. `SELECT` (computes projection expressions and aggregates)
6. `DISTINCT` (eliminates duplicate result rows)
7. `ORDER BY` (sorts final output rows)
8. `LIMIT` / `OFFSET` (paginates output)

---

## 4. Multi-Table Joins and Aggregations

### 4.1 Join Variations

```sql
-- Inner Join
SELECT e.first_name, e.last_name, d.dept_name
FROM employee e
INNER JOIN department d ON e.dept_id = d.dept_id;

-- Left Outer Join (preserves unmatched rows from employee table)
SELECT e.first_name, e.last_name, d.dept_name
FROM employee e
LEFT OUTER JOIN department d ON e.dept_id = d.dept_id;
```

### 4.2 Grouping and Aggregate Functions
Standard aggregate functions (`COUNT`, `SUM`, `AVG`, `MIN`, `MAX`) compute summary statistics over partitions:

```sql
SELECT d.dept_name,
       COUNT(e.emp_id) AS total_employees,
       ROUND(AVG(e.salary), 2) AS average_salary
FROM department d
JOIN employee e ON d.dept_id = e.dept_id
GROUP BY d.dept_id, d.dept_name
HAVING COUNT(e.emp_id) >= 5
ORDER BY average_salary DESC;
```

### 4.3 Subqueries and Correlated Subqueries
A correlated subquery references columns from the outer query:

```sql
-- Find employees who earn strictly more than their department's average salary
SELECT e.emp_id, e.first_name, e.last_name, e.salary
FROM employee e
WHERE e.salary > (
    SELECT AVG(inner_e.salary)
    FROM employee inner_e
    WHERE inner_e.dept_id = e.dept_id
);
```

