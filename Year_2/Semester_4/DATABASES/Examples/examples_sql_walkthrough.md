# Database Systems: SQL Schema & Query Walkthrough

This guide accompanies [`examples_sql_schema_and_queries.sql`](examples_sql_schema_and_queries.sql) to provide practical demonstrations of relational schema design, primary/foreign key constraints, and analytical query execution.

---

## 1. Schema Architecture

The demonstration models an academic department management system consisting of four normalized relational tables:

```text
DEPARTMENTS (dept_id PK)
     │
     ├────────────┐ 1:N
     │            ▼
     │       PROFESSORS (prof_id PK, dept_id FK)
     │            │
     │ 1:N        │ 1:N
     ▼            ▼
COURSES ──────── ENROLLMENTS (student_id, course_id PK, prof_id FK)
(course_id PK)
```

### Relational Constraints
- **Referential Integrity**: Foreign keys enforce cascade deletions (`ON DELETE CASCADE`) or nullification (`ON DELETE SET NULL`) to prevent orphan records.
- **Domain Constraints**: `CHECK` constraints enforce positive values for ECTS credits and valid email syntax.
- **Uniqueness**: `UNIQUE` constraints guarantee duplicate prevention across department names and course titles.

---

## 2. Executing the Script

Execute the SQL script directly against an in-memory or file-based SQLite database:

```bash
# Execute against SQLite3 CLI
sqlite3 university.db < Examples/examples_sql_schema_and_queries.sql

# Or execute with formatted table output
sqlite3 -header -column university.db < Examples/examples_sql_schema_and_queries.sql
```

---

## 3. Query Categories Demonstrated

1. **Multi-table `INNER JOIN` & `LEFT JOIN`**:
   - Retrieving full course profiles alongside instructor and department data.
   - Identifying courses with zero current student enrollments using outer joins and `IS NULL`.
2. **Aggregation and Grouping (`GROUP BY`, `HAVING`)**:
   - Computing average departmental GPA across enrolled cohorts.
   - Filtering departments offering more than a threshold number of credit units.
3. **Correlated Subqueries & Common Table Expressions (CTEs)**:
   - Finding professors earning above the departmental average.
   - Ranking student grades using SQL window functions (`RANK() OVER (...)`).

