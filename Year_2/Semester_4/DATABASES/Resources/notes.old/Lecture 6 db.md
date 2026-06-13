# The Relational Model and ER-to-Relational Mapping

This lecture transitions from conceptual design to logical design. It defines the formal structure of the Relational Model, explains integrity constraints, and provides a systematic algorithm for transforming Entity-Relationship (ER) diagrams into relational tables.

---

## 1. Formal Definitions of the Relational Model

The Relational Model represents data as a collection of relations (tables).

### 1.1. Core Terminology
*   **Relation (Σχέση):** A table with rows and columns.
*   **Attribute (Γνώρισμα):** A named column in the relation.
*   **Domain (Πεδίο Ορισμού):** The set of allowable atomic values for an attribute (e.g., `dom(Age) = {0..120}`).
*   **Tuple (Πλειάδα):** A row in the table representing a single entity instance.
*   **Relation Schema:** The logical definition of the table, denoted as $R(A_1, A_2, \dots, A_n)$.
*   **Degree (Βαθμός):** The number of attributes in the schema.

### 1.2. Characteristics of Relations
1.  **Ordering:** The order of tuples and attributes is irrelevant.
2.  **Uniqueness:** No two tuples in a relation can be identical.
3.  **Atomicity:** Values must be atomic (simple). This is the basis of **First Normal Form (1-NF)**. Composite and multi-valued attributes are not allowed in a pure relational table.

---

## 2. Integrity Constraints (Περιορισμοί Ακεραιότητας)

Constraints ensure the correctness and consistency of data in the database.

### 2.1. Key Constraints
*   **Superkey (Υπερκλειδί):** A set of attributes that uniquely identifies a tuple.
*   **Candidate Key (Υποψήφιο Κλειδί):** A minimal superkey.
*   **Primary Key (Πρωτεύον Κλειδί):** The candidate key chosen to identify tuples. It cannot be null.

### 2.2. Entity Integrity (Ακεραιότητα Οντοτήτων)
The Primary Key of a relation cannot contain null values. This ensures every entity instance can be identified.

### 2.3. Referential Integrity (Αναφορική Ακεραιότητα)
A **Foreign Key (Ξένο Κλειδί)** in relation $R_1$ must either match a Primary Key value in the referenced relation $R_2$ or be null. This maintains valid links between tables.

### 2.4. Semantic Integrity (Σημασιολογική Ακεραιότητα)
Business rules that the data must follow (e.g., "Salary cannot exceed \$5,000").

---

## 3. ER-to-Relational Mapping Algorithm

A 7-step process to transform a conceptual ER diagram into a logical relational schema.

| Step | Scenario | Transformation Rule |
| :--- | :--- | :--- |
| **1** | **Strong Entities** | Create a table. Include all simple attributes. Choose a Primary Key. |
| **2** | **Weak Entities** | Create a table. Include owner's PK + weak entity's Partial Key as a **Composite PK**. |
| **3** | **1:1 Relationships** | Add the PK of one table as a FK in the other. (Prefer the side with Total Participation). |
| **4** | **1:N Relationships** | Add the PK of the "1" side as a FK in the "N" side table. |
| **5** | **M:N Relationships** | Create a **New Table**. PK is the combination of PKs from both participating entities. |
| **6** | **Multi-valued Attributes** | Create a **New Table**. Include the attribute and the PK of the parent entity. |
| **7** | **n-ary Relationships** | Create a **New Table**. Include PKs of all participating entities as FKs. |

---

## Solved Exercises

### Exercise 1: Identifying Degrees
**Problem:** Given $Student(ID, Name, Email, DeptCode)$, what is the degree of the relation?

**Solution:**
*   **Answer:** 4.
*   **Reason:** There are four attributes defined in the schema.

### Exercise 2: Mapping a 1:N Relationship
**Problem:** Entity `Department` (1) has a relationship `Works_For` with `Employee` (N). How is this mapped?

**Solution:**
*   **Action:** Add `DeptCode` (PK of Department) as a Foreign Key in the `Employee` table.

### Exercise 3: Mapping an M:N Relationship
**Problem:** `Students` and `Courses` have an M:N relationship `Enrollment`. How is this mapped?

**Solution:**
*   **Action:** Create a new table `Enrollment(StudentID, CourseCode)`. 
*   **Keys:** Both attributes together form the Primary Key. Each is individually a Foreign Key to its respective parent table.

### Exercise 4: Weak Entity Mapping
**Problem:** `Dependent` is a weak entity of `Employee(SSN)`. `Dependent` has a partial key `Name`. Define the schema for `Dependent`.

**Solution:**
*   **Schema:** `Dependent(EmpSSN, DepName, Gender, BirthDate)`.
*   **Primary Key:** `(EmpSSN, DepName)`.

### Exercise 5: Multi-valued Attribute Mapping
**Problem:** `Department` has a multi-valued attribute `Locations`. How is it stored?

**Solution:**
*   **Action:** Create a table `Dept_Locations(DeptNumber, Location)`.
*   **Primary Key:** `(DeptNumber, Location)`.

### Exercise 6: Referential Integrity Check
**Problem:** A record in `Employee` has `DeptID = 10`. If `Department` 10 is deleted, what happens to the employee record?

**Solution:**
*   **Answer:** Depends on the constraint policy:
    1. **Restrict:** Deletion of department is blocked.
    2. **Cascade:** Employee is also deleted.
    3. **Set Null:** Employee's `DeptID` becomes null.

### Exercise 7: Candidate Key vs. Primary Key
**Problem:** A table has `Email` (unique) and `EmployeeID` (unique). Which is the Primary Key?

**Solution:**
*   **Answer:** Both are **Candidate Keys**. The designer chooses one (usually `EmployeeID`) to be the **Primary Key**.

### Exercise 8: Recursive Mapping
**Problem:** `Employee(SSN)` has a recursive $1:N$ relationship `Supervises`. Define the table.

**Solution:**
*   **Schema:** `Employee(SSN, Name, ..., SupervisorSSN)`.
*   **Note:** `SupervisorSSN` is a Foreign Key referencing the *same* table's `SSN`.

---

## Exam Tip: The M:N Trap

> **[Key Insight]**
> A common exam mistake is trying to represent a Many-to-Many ($M:N$) relationship using a Foreign Key in one of the existing tables. 
> **Remember:** $M:N$ relationships *always* require a **New Table** (junction table). If you see $M:N$, your answer must include a separate table whose Primary Key is composite.
