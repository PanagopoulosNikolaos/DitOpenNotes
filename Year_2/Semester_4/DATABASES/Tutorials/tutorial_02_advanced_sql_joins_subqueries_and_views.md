# Tutorial 02: Advanced SQL Joins, Subqueries, and Virtual Views

This practical tutorial expands database query capabilities through multi-table joins, nested correlated subqueries, Common Table Expressions (CTEs), and virtual view definitions using SQLite.

---

## 1. Schema Context and Data Population

Ensure the base tables from Tutorial 01 exist, then create and populate the `enrollments` junction table:

```sql
CREATE TABLE enrollments (
    student_id INTEGER NOT NULL,
    course_id VARCHAR(10) NOT NULL,
    semester VARCHAR(10) NOT NULL,
    grade NUMERIC(3, 1) CHECK (grade BETWEEN 0.0 AND 10.0),
    PRIMARY KEY (student_id, course_id, semester),
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE
);

INSERT INTO enrollments VALUES
    (101, 'CS101', 'Fall2025', 9.5),
    (102, 'CS101', 'Fall2025', 7.0),
    (101, 'CS202', 'Spring2026', 8.5),
    (103, 'CS101', 'Fall2025', 6.0),
    (104, 'CS305', 'Spring2026', 4.5);
```

---

## 2. Advanced Multi-Table Joins

### 2.1 Left Outer Join to Identify Unenrolled Courses
Find all courses including those with zero enrollments:

```sql
SELECT c.course_id, c.title, COUNT(e.student_id) AS enrolled_count
FROM courses c
LEFT JOIN enrollments e ON c.course_id = e.course_id
GROUP BY c.course_id, c.title;
```

---

## 3. Common Table Expressions (CTEs)

A Common Table Expression provides a named, temporary result set:

```sql
WITH course_statistics AS (
    SELECT course_id,
           COUNT(student_id) AS student_count,
           AVG(grade) AS average_grade
    FROM enrollments
    GROUP BY course_id
)
SELECT c.title, cs.student_count, ROUND(cs.average_grade, 2) AS avg_grade
FROM courses c
JOIN course_statistics cs ON c.course_id = cs.course_id
WHERE cs.average_grade >= 7.0;
```

---

## 4. Virtual Views

A virtual view encapsulates complex query logic behind a simplified relational interface without duplicating data on disk:

```sql
CREATE VIEW high_performing_students AS
SELECT student_id,
       COUNT(course_id) AS total_courses_passed,
       ROUND(AVG(grade), 2) AS gpa
FROM enrollments
WHERE grade >= 5.0
GROUP BY student_id
HAVING AVG(grade) >= 8.5;

-- Query the view directly
SELECT * FROM high_performing_students;
```

