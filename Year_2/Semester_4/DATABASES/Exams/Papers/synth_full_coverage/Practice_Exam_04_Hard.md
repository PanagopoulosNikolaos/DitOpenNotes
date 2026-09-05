# Exam 4: Normalization & Advanced SQL (Level: Hard)

Multiple Choice Question 1: What is the difference between the DELETE and TRUNCATE commands?
[ ] 1. No difference, they do exactly the same thing.
[ ] 2. DELETE is DDL while TRUNCATE is DML.
[✓] 3. DELETE is DML and allows ROLLBACK, while TRUNCATE is DDL and does not allow ROLLBACK.
[ ] 4. TRUNCATE also deletes the structure of the table (DROP).
---
*solution:*
TRUNCATE quickly empties the data, resets the auto-increments, and is not fully recorded in the transaction log, making it DDL, in contrast to DELETE (DML), which deletes records row by row and allows rollback.
---

Multiple Choice Question 2: A table is in BCNF if:
[✓] 1. It is in 3NF and for every dependency X -> Y, X is a superkey.
[ ] 2. It is in 2NF and has no transitive dependencies.
[ ] 3. Its data is organized in a tree structure (NoSQL).
[ ] 4. All attributes are atomic.
---
*solution:*
The Boyce-Codd form (BCNF) is stricter than 3NF. It requires every determinant (X) of a non-trivial functional dependency (X -> Y) to be a candidate key or a superkey.
---

Exercise 3: Given the relation R(K, L, M, N) and the dependencies F={KL -> M, M -> N}. The table is in 1NF. In which normal form is it, and how should it be decomposed to reach BCNF?
---
*solution:*
- The key is {K, L} (since (KL)+ = {K, L, M, N}).
- The dependency M -> N is a transitive dependency, since M is not a key. Therefore it is not in 3NF (nor in BCNF).
- It is in 2NF, because no subset of the key {K, L} by itself determines the non-key attributes.
- Decomposition into BCNF:
  Create a relation for the problematic dependency M -> N: R1(M, N) with primary key M.
  Remove N from the original relation: R2(K, L, M) with primary key (K, L).
---

Exercise 4: Given the tables Employee(emp_id, emp_name, salary, dept_id) and Department(dept_id, dept_name). Write an SQL query that finds the name and salary of the employees who earn the highest salary in their department (using a correlated subquery).
---
*solution:*
```sql
SELECT e1.emp_name, e1.salary
FROM Employee e1
WHERE e1.salary = (
    SELECT MAX(e2.salary)
    FROM Employee e2
    WHERE e2.dept_id = e1.dept_id
);
```
---
