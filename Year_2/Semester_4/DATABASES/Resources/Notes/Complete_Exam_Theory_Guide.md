# Complete Theoretical & Methodological Exam Guide: Database Systems (Course 404)

---

## Table of Contents
1. [Course Overview & Exam Structure](#1-course-overview--exam-structure)
2. [Unit 1: Conceptual Data Modeling & ER / EER Foundations](#2-unit-1-conceptual-data-modeling--er--eer-foundations)
3. [Unit 2: The Relational Model & ER-to-Relational Mapping Algorithms](#3-unit-2-the-relational-model--er-to-relational-mapping-algorithms)
4. [Unit 3: Relational Table Schema Representation (Exam Standards)](#4-unit-3-relational-table-schema-representation-exam-standards)
5. [Unit 4: Relational Algebra & Formal Query Languages](#5-unit-4-relational-algebra--formal-query-languages)
6. [Unit 5: SQL Complete Reference Guide (DDL, DML, DQL)](#6-unit-5-sql-complete-reference-guide-ddl-dml-dql)
7. [Unit 6: Normalization Theory & Functional Dependencies](#7-unit-6-normalization-theory--functional-dependencies)
8. [Unit 7: Transactions, Concurrency Control & Database Security](#8-unit-7-transactions-concurrency-control--database-security)
9. [Unit 8: Step-by-Step Methodological Algorithms & Solution Recipes](#9-unit-8-step-by-step-methodological-algorithms--solution-recipes)
10. [Unit 9: Official Schema & ER Notation Reference Sheet](#10-unit-9-official-schema--er-notation-reference-sheet)
11. [Unit 10: Critical Exam Traps & Checklist of Common Mistakes](#11-unit-10-critical-exam-traps--checklist-of-common-mistakes)

---

## 1. Course Overview & Exam Structure

The examination for **Database Systems (Course 404)** in the Department of Informatics & Telecommunications typically tests students across both conceptual database design and formal/practical relational operations. Across historical progress tests, midterm exams, and final exams, exam questions fall into five core pillars:

| Exam Section | Topic Focus | Core Deliverables & Question Types | Typical Point Weight |
|---|---|---|---|
| **Question A** | Conceptual Analysis & Semantic Modeling | Identification of Entities (Strong vs. Weak), Attributes (Simple, Composite, Single/Multi-valued, Derived), Keys (Candidate, Primary, Partial), Relationships, Cardinality Ratios (1:1, 1:N, N:M), and Participation Constraints with mandatory written justification | 4.0 - 5.0 / 10 |
| **Question B** | Entity-Relationship (ER / EER) Diagramming | Complete graphical schema diagram using Chen or Crow's Foot / Mermaid notation, depicting weak entities, identifying relationships, multi-valued attributes, derived attributes, recursive relationships, and participation lines | 3.0 - 5.0 / 10 |
| **Question C** | Relational Schema Transformation | Converting the conceptual ER diagram into physical relational tables in standard tabular format, with explicit underlining of Primary Keys (PKs), identification of Foreign Keys (FKs), and referential integrity actions | 3.0 / 10 |
| **Question D** | Relational Algebra & SQL Queries | Formal relational algebra expressions ($\sigma, \pi, \bowtie, \cup, -, \div$) and ANSI SQL queries (DDL constraints, JOINs, aggregations, GROUP BY / HAVING, correlated subqueries) | 2.5 - 3.0 / 10 |
| **Question E** | Normalization, Transactions & Security | Functional dependencies, Attribute closure $X^+$, Candidate key derivation, Normal form verification (1NF, 2NF, 3NF, BCNF), Lossless decomposition, ACID properties, Conflict serializability, SQL Injection, DAC security | 2.0 - 2.5 / 10 |

---

## 2. Unit 1: Conceptual Data Modeling & ER / EER Foundations

### 2.1 Entity Types & Existence Dependency

An **Entity** represents a distinct real-world object or concept with independent or dependent existence.

```
+-----------------------------------------------------------------------------------+
| ENTITY CLASSIFICATION                                                             |
+------------------------------------+----------------------------------------------+
| Strong (Regular) Entity            | Weak Entity                                  |
+------------------------------------+----------------------------------------------+
| - Possesses an independent key     | - Cannot exist without an Owner Entity       |
| - Primary key formed internally    | - Does not possess a complete primary key    |
| - Represented by a single rectangle| - Has a Partial Key (Discriminator)          |
| - Example: `PROFESSOR(ProfID)`     | - Represented by a double rectangle          |
|   `PATIENT(AMKA)`, `HOTEL(HotelID)`| - Connected via an Identifying Relationship  |
|                                    |   (double diamond)                           |
|                                    | - Example: `DEPENDENT` of `PROFESSOR`        |
|                                    |   `ROOM` of `HOTEL`, `EPISODE` of `TV_SERIES`|
+------------------------------------+----------------------------------------------+
```

#### Criteria for Identifying Weak Entities in Exam Problems
1. **Ownership Constraint:** An entity instance cannot exist without a corresponding instance of another entity (the owner/identifying entity).
2. **Key Insufficiency:** The entity's attributes do not uniquely distinguish instances across the entire universe—only within the owner's context.
3. **Identifying Relationship:** The relationship linking the weak entity to its owner must be a 1:N relationship with total participation (double line) on the weak entity side.
4. **Primary Key Formulation:** $\text{PK}(\text{Weak Entity}) = \text{PK}(\text{Owner Entity}) \cup \text{Partial Key}$.

---

### 2.2 Attribute Classifications

Attributes are characteristics or properties describing an entity or relationship.

| Attribute Classification | Formal Definition | Exam Notation / Representation | Real-World Example |
|---|---|---|---|
| **Simple / Atomic** | Cannot be divided into smaller sub-components | Single oval (or plain text) | `Salary`, `ECTS`, `BloodType` |
| **Composite** | Can be subdivided into independent sub-attributes with individual meaning | Tree of connected ovals | `Address` $\to$ (`Street`, `Number`, `PostalCode`, `City`) |
| **Single-Valued** | Takes exactly one atomic value per entity instance | Single solid oval | `DateOfBirth`, `Gender`, `HireDate` |
| **Multi-Valued** | Can hold a set of multiple values for a single entity instance | Double solid oval | `PhoneNumbers`, `Amenities`, `Colors` |
| **Derived** | Computed dynamically from stored attributes or relationships; not stored statically | Dashed / dotted oval | `Age` (from `DateOfBirth`), `Duration` (from `Start` & `End`), `TotalCost` |
| **Key Attribute (PK)** | Uniquely identifies every entity instance in the entity set | Solid oval with underlined attribute name | `AMKA`, `TaxID (AFM)`, `CourseCode` |
| **Partial Key (Discriminator)** | Uniquely distinguishes weak entity instances belonging to the same owner | Dashed underlined attribute name | `DependentName`, `RoomNumber`, `EpisodeNumber` |

---

### 2.3 Relationships, Degrees, and Structural Constraints

A **Relationship** is an association among two or more entities.

#### Degree of a Relationship
*   **Unary (Recursive) Relationship (Degree 1):** The same entity type participates more than once in distinct roles.
    *   *Example 1:* `DOCTOR` supervises junior `DOCTOR` (Roles: `Supervisor` [1], `Supervisee` [N]).
    *   *Example 2:* `COURSE` has prerequisite `COURSE` (Roles: `PrerequisiteCourse` [N], `MainCourse` [M]).
*   **Binary Relationship (Degree 2):** Involves two distinct entity types (e.g., `PROFESSOR` directs `FACULTY`).
*   **Ternary Relationship (Degree 3):** Involves three entity types simultaneously (e.g., `PHYSICIAN` prescribes `MEDICATION` to `PATIENT` during `HOSPITALIZATION`).

---

### 2.4 Cardinality Ratios & Participation Constraints

Every binary relationship has two fundamental structural dimensions:

```
                  +----------------------------------------------+
                  |            STRUCTURAL CONSTRAINTS            |
                  +----------------------+-----------------------+
                                         |
               +-------------------------+-------------------------+
               |                                                   |
               v                                                   v
   [ CARDINALITY RATIO ]                               [ PARTICIPATION CONSTRAINT ]
   Maximum number of relationship                      Minimum number of relationship
   instances an entity can enter.                      instances an entity must enter.
   - 1:1  (One-to-One)                                 - Total / Mandatory (min = 1)
   - 1:N  (One-to-Many)                                  (Represented by Double Line)
   - N:M  (Many-to-Many)                               - Partial / Optional (min = 0)
                                                         (Represented by Single Line)
```

#### Detailed Cardinality Ratios

1. **One-to-One (1:1):**
   *   *Rule:* One instance of entity $A$ is associated with at most one instance of entity $B$, and vice versa.
   *   *Example:* `FACULTY` $\xleftrightarrow{\text{1:1}}$ `PROFESSOR` (via `DIRECTS` / `HEADS`).
   *   *Participation Analysis:* Every faculty must have a director (Total participation for `FACULTY`), but not every professor is a director (Partial participation for `PROFESSOR`).

2. **One-to-Many (1:N):**
   *   *Rule:* One instance of entity $A$ is associated with zero, one, or many instances of entity $B$, but each instance of $B$ is associated with at most one instance of $A$.
   *   *Example:* `FACULTY` $\xrightarrow{\text{1:N}}$ `EDUCATIONAL_PROGRAM` (via `OFFERS`).
   *   *Participation Analysis:* A faculty offers many programs; every program belongs to exactly one faculty (Total for `EDUCATIONAL_PROGRAM`).

3. **Many-to-Many (N:M):**
   *   *Rule:* One instance of entity $A$ is associated with many instances of $B$, and one instance of $B$ is associated with many instances of $A$.
   *   *Example:* `PROFESSOR` $\xleftrightarrow{\text{N:M}}$ `EDUCATIONAL_PROGRAM` (via `PARTICIPATES_IN`).
   *   *Descriptive Attributes:* Relationships with N:M cardinality frequently contain descriptive attributes that belong to the association itself (e.g., `WeeklyHours` worked by a professor in a specific program).

---

### 2.5 Enhanced ER (EER): Specialization & Generalization

Specialization is the process of defining a set of subclasses of an entity type (the superclass).

```
                     +---------------------------+
                     |    SUPERCLASS: PERSON     |
                     | Attributes: ID, Name, DoB |
                     +-------------+-------------+
                                   |
                                   v  ( d, t )
                        +----------+----------+
                        |                     |
                        v                     v
            +-----------------------+  +-----------------------+
            | SUBCLASS 1: PROFESSOR |  |   SUBCLASS 2: STUDENT |
            | Attributes: Salary    |  | Attributes: Semester  |
            +-----------------------+  +-----------------------+
```

#### Disjointness Constraint
*   **Disjoint (`d`):** An entity instance can be a member of at most one subclass (e.g., a media title is either a `MOVIE` or a `TV_SERIES`).
*   **Overlapping (`o`):** An entity instance can simultaneously belong to multiple subclasses (e.g., a university person can be both an `EMPLOYEE` and a `STUDENT`).

#### Completeness Constraint
*   **Total Specialization (`t` / Double Line):** Every superclass instance must belong to at least one subclass.
*   **Partial Specialization (`p` / Single Line):** An entity instance may belong to the superclass without belonging to any subclass.

---

## 3. Unit 2: The Relational Model & ER-to-Relational Mapping Algorithms

The standard 7-step algorithm transforms any conceptual ER diagram into a normalized relational schema:

```
+---------------------------------------------------------------------------------------------------+
| SEVEN-STEP ER-TO-RELATIONAL MAPPING ALGORITHM                                                     |
+------+--------------------------+-----------------------------------------------------------------+
| Step | Target ER Construct      | Relational Mapping Action                                       |
+------+--------------------------+-----------------------------------------------------------------+
| 1    | Regular Strong Entities  | Create a table. PK = Key attribute(s). Include atomic attributes.|
| 2    | Weak Entity Types        | Create a table. PK = (Owner PK + Partial Key). FK = Owner PK.   |
| 3    | 1:1 Binary Relationships | Add Foreign Key to the side with Total Participation.           |
| 4    | 1:N Binary Relationships | Add Foreign Key to the N-side table referencing the 1-side.     |
| 5    | N:M Binary Relationships | Create a new Junction Table. PK = (FK_A + FK_B).                |
| 6    | Multi-Valued Attributes  | Create a new Table. PK = (Parent PK + Attribute Value).         |
| 7    | N-ary Relationships      | Create a new Table. PK = Composite of all participating FKs.    |
+------+--------------------------+-----------------------------------------------------------------+
```

---

### 3.1 Detailed Step-by-Step Mapping Procedures

#### Step 1: Mapping Regular Strong Entity Types
*   For each strong entity type $E$, create a relation $R$ containing all simple attributes of $E$.
*   For composite attributes, include only their simple sub-components.
*   Choose one candidate key as the Primary Key ($\underline{\text{PK}}$).

#### Step 2: Mapping Weak Entity Types
*   For each weak entity type $W$ with owner entity type $E$, create a relation $R$.
*   Include all simple attributes of $W$.
*   Include the Primary Key of $E$ as a Foreign Key ($FK$) in $R$.
*   The Primary Key of $R$ is the composite key: $\underline{\text{PK}(R) = \{\text{FK from } E, \text{Partial Key of } W\}}$.
*   Set `ON DELETE CASCADE` on the Foreign Key to maintain existence dependency.

#### Step 3: Mapping 1:1 Binary Relationships
Let $R$ and $S$ be the relations corresponding to entity types participating in relationship $T$. Choose one of three strategies based on participation:
1. **Foreign Key Approach (Standard / Preferred):**
   *   Identify the entity with **total participation** in $T$ (e.g., $S$).
   *   Include $\text{PK}(R)$ as a Foreign Key in $S$.
   *   Add any descriptive attributes of $T$ to $S$.
   *   Declare the Foreign Key column as `UNIQUE NOT NULL` in $S$.
2. **Merged Relation Approach:** If both entities participate totally and are tightly coupled, merge $R$ and $S$ into a single relation.
3. **Cross-Reference Table Approach:** Create a separate relation $T(\underline{\text{PK}_R}, \text{PK}_S, \dots)$ with $\text{PK}_R$ as primary key and $\text{PK}_S$ declared `UNIQUE`.

#### Step 4: Mapping 1:N Binary Relationships
*   Identify the relation $S$ representing the entity type on the **N-side** (many-side).
*   Include the Primary Key of the relation $R$ (on the 1-side) as a Foreign Key in $S$.
*   Include any descriptive attributes of the relationship in $S$.
*   If participation of $S$ is total, declare the Foreign Key column as `NOT NULL`.

#### Step 5: Mapping N:M Binary Relationships
*   Create a new **Junction (Associative) Relation** $J$.
*   Include the Primary Keys of both participating relations $R$ and $S$ as Foreign Keys in $J$: $\text{FK}_1$ and $\text{FK}_2$.
*   The Primary Key of $J$ is the composite set: $\underline{\text{PK}(J) = \{\text{FK}_1, \text{FK}_2\}}$.
*   Include any descriptive attributes of the N:M relationship in $J$.

#### Step 6: Mapping Multi-Valued Attributes
*   For each multi-valued attribute $A$ of entity $E$, create a distinct relation $R_A$.
*   Include the attribute $A$ along with the Primary Key $\text{PK}(E)$ of $E$ as a Foreign Key.
*   The Primary Key of $R_A$ is the combination: $\underline{\text{PK}(R_A) = \{\text{FK from } E, A\}}$.

#### Step 7: Mapping Specialization / Generalization Hierarchies
*   **Option 8A (Multiple relations for Superclass and Subclasses):** Create a relation for the superclass $C$ with $\text{PK}(C)$, and a relation for each subclass $S_i$ with $\text{PK}(S_i) = \text{PK}(C)$ (acting as both PK and FK).
*   **Option 8B (Subclass relations only):** Valid only if specialization is **total and disjoint** ($t, d$). Create relations $S_i$ containing all superclass attributes plus subclass attributes.
*   **Option 8C (Single relation with type discriminator):** Valid for disjoint specialization. Create a single relation with all attributes plus a `Type` attribute.
*   **Option 8D (Single relation with boolean flags):** Valid for overlapping specialization. Create a single relation with boolean flags for each subclass.

---

## 4. Unit 3: Relational Table Schema Representation (Exam Standards)

The official examination evaluation rubric for University Database exams requires strict adherence to schema presentation standards.

### 4.1 Required Visual Format

Each table must be presented with its entity/relation name at the top, a header row containing all attributes, **underlining of the Primary Key** attributes, and explicit documentation of all Foreign Keys.

```
Student
| Registration_Number | First_Name | Last_Name | Semester | Department_Code |
|---------------------|------------|-----------|----------|-----------------|

Primary Key: Registration_Number
Foreign Keys:
- Department_Code REFERENCES Department(Department_Code) ON DELETE RESTRICT ON UPDATE CASCADE
```

### 4.2 Handling Composite and Weak Primary Keys

When primary keys consist of multiple columns (composite keys, weak entities, or junction tables), **all participating columns must be underlined**.

```
Course_Enrollment
| Student_AM | Course_Code | Academic_Year | Semester | Final_Grade | Exam_Date |
|------------|-------------|---------------|----------|-------------|-----------|

Primary Key: (Student_AM, Course_Code, Academic_Year, Semester)
Foreign Keys:
- Student_AM REFERENCES Student(AM) ON DELETE CASCADE
- Course_Code REFERENCES Course(Course_Code) ON DELETE RESTRICT
```

```
Dependent
| Doctor_AMI | Dependent_Name | Gender | Date_Of_Birth | Relationship |
|------------|----------------|--------|---------------|--------------|

Primary Key: (Doctor_AMI, Dependent_Name)
Foreign Keys:
- Doctor_AMI REFERENCES Doctor(AMI) ON DELETE CASCADE ON UPDATE CASCADE
```

---

## 5. Unit 4: Relational Algebra & Formal Query Languages

Relational Algebra is a formal, procedural query language working on relation instances and producing relation instances.

```
+---------------------------------------------------------------------------------------------------+
| FUNDAMENTAL RELATIONAL ALGEBRA OPERATORS                                                          |
+----------------------+--------------------+-------------------------------------------------------+
| Operator Name        | Notation           | Formal Semantics                                      |
+----------------------+--------------------+-------------------------------------------------------+
| Selection            | $\sigma_C(R)$      | Selects tuples from $R$ that satisfy condition $C$    |
| Projection           | $\pi_L(R)$         | Projects columns specified in attribute list $L$      |
| Rename               | $\rho_{S}(R)$      | Renames relation $R$ to $S$ or attributes             |
| Union                | $R \cup S$         | Tuples in $R$, $S$, or both ($R, S$ union compatible) |
| Set Difference       | $R - S$            | Tuples in $R$ that are not in $S$                     |
| Cartesian Product    | $R \times S$       | All pairwise concatenations of tuples from $R$ and $S$|
+----------------------+--------------------+-------------------------------------------------------+
| DERIVED & EXTENDED OPERATORS                                                                      |
+----------------------+--------------------+-------------------------------------------------------+
| Set Intersection     | $R \cap S$         | $R - (R - S)$ (Tuples in both $R$ and $S$)            |
| Theta Join           | $R \bowtie_\theta S$| $\sigma_\theta(R \times S)$                           |
| Natural Join         | $R \bowtie S$      | Equi-join on all shared common attribute names        |
| Left Outer Join      | $R ⟕ S$            | Keeps all tuples from $R$, pads unmatched $S$ with NULL|
| Right Outer Join     | $R ⟖ S$            | Keeps all tuples from $S$, pads unmatched $R$ with NULL|
| Full Outer Join      | $R ⟗ S$            | Keeps all tuples from both $R$ and $S$                |
| Semi-Join            | $R \ltimes S$      | $\pi_{\text{attrs}(R)}(R \bowtie S)$                  |
| Division             | $R \div S$         | Tuples in $\pi_{R-S}(R)$ associated with ALL tuples $S$|
| Aggregate Grouping   | $_{G}\mathcal{G}_{F}(R)$| Groups by $G$ and applies aggregate functions $F$ |
+----------------------+--------------------+-------------------------------------------------------+
```

---

### 5.1 Step-by-Step Relational Algebra Formulations

#### Query 1: Selection and Projection
*Find the first name and salary of all professors in Department 'CS' with salary > 3000.*
$$\pi_{\text{First\_Name}, \text{Salary}}(\sigma_{\text{Dept\_Code} = '\text{CS}' \land \text{Salary} > 3000}(\text{Professor}))$$

#### Query 2: Natural Join
*Find the names of students enrolled in the course 'Database Systems'.*
$$\pi_{\text{First\_Name}, \text{Last\_Name}}(\sigma_{\text{Course\_Title} = '\text{Database Systems}'}(\text{Student} \bowtie \text{Enrollment} \bowtie \text{Course}))$$

#### Query 3: Set Difference ("NOT IN" Logic)
*Find the ID numbers of professors who have NEVER chaired any department.*
$$\pi_{\text{Prof\_ID}}(\text{Professor}) - \pi_{\text{Director\_Prof\_ID}}(\text{Department})$$

#### Query 4: Relational Division ("FOR ALL" Logic)
*Find the student IDs of students who have enrolled in ALL compulsory courses offered by the 'CS' department.*
1. Target Course Set ($S$): $S = \pi_{\text{Course\_Code}}(\sigma_{\text{Dept} = '\text{CS}' \land \text{Category} = '\text{Compulsory}'}(\text{Course}))$
2. Student Enrollment Pairs ($R$): $R = \pi_{\text{Student\_AM}, \text{Course\_Code}}(\text{Enrollment})$
3. Division Expression: $\text{Result} = R \div S$

---

## 6. Unit 5: SQL Complete Reference Guide (DDL, DML, DQL)

### 6.1 Data Definition Language (DDL) Syntax Reference

```sql
-- Comprehensive DDL Table Creation Template
CREATE TABLE Professor (
    prof_id INT NOT NULL,
    tax_id CHAR(9) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    academic_rank VARCHAR(30) DEFAULT 'Assistant Professor',
    monthly_salary DECIMAL(10, 2) NOT NULL,
    hire_date DATE NOT NULL,
    dept_code VARCHAR(10) NOT NULL,
    supervisor_prof_id INT NULL,
    CONSTRAINT pk_professor PRIMARY KEY (prof_id),
    CONSTRAINT uq_prof_tax_id UNIQUE (tax_id),
    CONSTRAINT chk_prof_salary CHECK (monthly_salary >= 800.00),
    CONSTRAINT fk_prof_department FOREIGN KEY (dept_code)
        REFERENCES Department(dept_code)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,
    CONSTRAINT fk_prof_supervisor FOREIGN KEY (supervisor_prof_id)
        REFERENCES Professor(prof_id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

-- Junction Table for N:M Relationship
CREATE TABLE Professor_Project (
    prof_id INT NOT NULL,
    project_id INT NOT NULL,
    weekly_hours DECIMAL(4, 1) NOT NULL DEFAULT 0.0,
    CONSTRAINT pk_prof_project PRIMARY KEY (prof_id, project_id),
    CONSTRAINT fk_pp_prof FOREIGN KEY (prof_id)
        REFERENCES Professor(prof_id) ON DELETE CASCADE,
    CONSTRAINT fk_pp_project FOREIGN KEY (project_id)
        REFERENCES Project(project_id) ON DELETE CASCADE,
    CONSTRAINT chk_weekly_hours CHECK (weekly_hours >= 0.0 AND weekly_hours <= 40.0)
);
```

---

### 6.2 Data Query Language (DQL) Clauses and Execution Order

```
SQL LOGICAL QUERY PROCESSING ORDER
1. FROM / JOIN     -> Identify source tables and construct cartesian/join product
2. WHERE           -> Filter individual rows based on predicate conditions
3. GROUP BY        -> Partition filtered rows into distinct groups
4. HAVING          -> Filter aggregated groups based on group conditions
5. SELECT          -> Project requested columns and compute scalar expressions
6. DISTINCT        -> Eliminate duplicate output tuples
7. UNION / EXCEPT  -> Apply set-level operations
8. ORDER BY        -> Sort final result set by specified criteria
9. LIMIT / OFFSET  -> Restrict number of output rows
```

#### Essential DQL Query Patterns

```sql
-- Pattern 1: Grouping with HAVING filter and Multi-Table INNER JOIN
SELECT 
    d.dept_name,
    COUNT(p.prof_id) AS total_professors,
    AVG(p.monthly_salary) AS avg_salary
FROM Department d
INNER JOIN Professor p ON d.dept_code = p.dept_code
GROUP BY d.dept_code, d.dept_name
HAVING COUNT(p.prof_id) >= 5
ORDER BY avg_salary DESC;

-- Pattern 2: Correlated Subquery with NOT EXISTS (Anti-Join)
SELECT p.prof_id, p.first_name, p.last_name
FROM Professor p
WHERE NOT EXISTS (
    SELECT 1 
    FROM Professor_Project pp
    WHERE pp.prof_id = p.prof_id
);

-- Pattern 3: Finding Entities Associated With All Items (Relational Division in SQL)
-- Find students who have taken ALL courses offered by 'CS'
SELECT e.student_am
FROM Enrollment e
INNER JOIN Course c ON e.course_code = c.course_code
WHERE c.dept_code = 'CS'
GROUP BY e.student_am
HAVING COUNT(DISTINCT e.course_code) = (
    SELECT COUNT(*) 
    FROM Course 
    WHERE dept_code = 'CS'
);
```

---

## 7. Unit 6: Normalization Theory & Functional Dependencies

Normalization is the systematic design procedure to eliminate data redundancy and prevent update, insertion, and deletion anomalies.

### 7.1 Functional Dependencies (FDs) & Armstrong's Axioms

Given relation schema $R(A_1, \dots, A_n)$ and $X, Y \subseteq R$, $X \to Y$ denotes that $X$ functionally determines $Y$.

#### Primary Axioms (Sound and Complete)
1. **Reflexivity Rule:** If $Y \subseteq X$, then $X \to Y$. (Trivial FD)
2. **Augmentation Rule:** If $X \to Y$, then $XZ \to YZ$ for any $Z$.
3. **Transitivity Rule:** If $X \to Y$ and $Y \to Z$, then $X \to Z$.

#### Secondary Derived Rules
4. **Decomposition (Projectivity) Rule:** If $X \to YZ$, then $X \to Y$ and $X \to Z$.
5. **Union (Additivity) Rule:** If $X \to Y$ and $X \to Z$, then $X \to YZ$.
6. **Pseudotransitivity Rule:** If $X \to Y$ and $WY \to Z$, then $WX \to Z$.

---

### 7.2 Attribute Closure Algorithm ($X^+$)

To find all attributes functionally determined by attribute set $X$ under a set of functional dependencies $F$:

```
Algorithm AttributeClosure(X, F):
1. Set X+ := X
2. Repeat until X+ does not change:
     For each FD (Y -> Z) in F:
       If Y is a subset of X+:
         Set X+ := X+ union Z
3. Return X+
```

#### Determining Candidate Keys Using $X^+$
*   An attribute set $K$ is a **Superkey** of $R$ if $K^+ = R$.
*   $K$ is a **Candidate Key** if $K^+ = R$ and no proper subset $K' \subset K$ satisfies $(K')^+ = R$.
*   **Rule of Thumb:** Attributes that never appear on the right-hand side of any FD in $F$ **must** be part of every candidate key.

---

### 7.3 The Hierarchy of Normal Forms

```
+---------------------------------------------------------------------------------------------------+
| NORMAL FORM HIERARCHY & DEFINITIONS                                                               |
+-------------+---------------------------------------+---------------------------------------------+
| Normal Form | Formal Condition                      | Violation Remedy                            |
+-------------+---------------------------------------+---------------------------------------------+
| **1NF**     | All attribute values are atomic;      | Flatten composite attributes; decompose     |
|             | no repeating groups or nested tables. | multi-valued attributes into new relations.|
+-------------+---------------------------------------+---------------------------------------------+
| **2NF**     | 1NF AND no non-prime attribute is     | Decompose into separate tables so that      |
|             | partially dependent on any candidate  | non-prime attributes depend on the full key.|
|             | key ($X \to Y$ where $X \subset K$).  |                                             |
+-------------+---------------------------------------+---------------------------------------------+
| **3NF**     | 2NF AND for every non-trivial         | Decompose to eliminate transitive           |
|             | $X \to Y$, either:                    | dependencies $K \to X \to Y$.               |
|             | 1. $X$ is a superkey, OR              |                                             |
|             | 2. $Y$ is a prime attribute.          |                                             |
+-------------+---------------------------------------+---------------------------------------------+
| **BCNF**    | For every non-trivial $X \to Y$,      | Decompose into $R_1(X \cup Y)$ and          |
|             | $X$ MUST be a superkey of $R$.        | $R_2(R - (Y - X))$.                         |
+-------------+---------------------------------------+---------------------------------------------+
```

---

### 7.4 Decomposition Properties

When decomposing relation schema $R$ into $D = \{R_1, R_2\}$:

1. **Lossless-Join Decomposition (MANDATORY):**
   *   A binary decomposition $D = \{R_1, R_2\}$ is lossless with respect to $F$ if and only if:
       $$(R_1 \cap R_2) \to R_1 \quad \text{OR} \quad (R_1 \cap R_2) \to R_2$$
   *   That is, the common attributes must form a superkey of at least one of the decomposed relations.

2. **Dependency Preservation:**
   *   A decomposition preserves dependencies if $(F_1 \cup F_2 \dots \cup F_k)^+ = F^+$.
   *   3NF synthesis guarantees both lossless join and dependency preservation.
   *   BCNF decomposition guarantees lossless join, but may not always preserve all dependencies.

---

## 8. Unit 7: Transactions, Concurrency Control & Database Security

### 8.1 ACID Properties of Transactions

A **Transaction** is an atomic unit of database program execution.

```
+---------------------------------------------------------------------------------------------------+
| ACID PRINCIPLES                                                                                   |
+-------------------+---------------------------------------+---------------------------------------+
| Property          | Guarantee                             | DBMS Implementation Mechanism         |
+-------------------+---------------------------------------+---------------------------------------+
| **Atomicity**     | "All or nothing": Either all actions  | Write-Ahead Logging (WAL), Undo Logs, |
|                   | complete or none take effect.         | Transaction Rollback                  |
+-------------------+---------------------------------------+---------------------------------------+
| **Consistency**   | Transaction transforms database from  | Schema constraints (PK, FK, CHECK),  |
|                   | one valid state to another valid state| Application business logic assertions |
+-------------------+---------------------------------------+---------------------------------------+
| **Isolation**     | Concurrent execution behaves as if    | Two-Phase Locking (2PL), MVCC,        |
|                   | transactions executed sequentially.   | Transaction Isolation Levels          |
+-------------------+---------------------------------------+---------------------------------------+
| **Durability**    | Once committed, updates persist even  | Redo Logs, Non-volatile disk flush,   |
|                   | through system crashes.               | Checkpointing                         |
+-------------------+---------------------------------------+---------------------------------------+
```

---

### 8.2 Concurrency Anomalies & SQL Isolation Levels

| Concurrency Anomaly | Description | SQL Scenario |
|---|---|---|
| **Dirty Read** | Transaction $T_2$ reads uncommitted modifications made by $T_1$, which subsequently aborts ($ROLLBACK$). | $W_1(A) \to R_2(A) \to \text{Abort}_1$ |
| **Non-Repeatable Read** | Transaction $T_1$ reads a row, $T_2$ updates or deletes that row and commits, $T_1$ re-reads and observes different values. | $R_1(A) \to W_2(A) \to C_2 \to R_1(A)$ |
| **Phantom Read** | Transaction $T_1$ reads a set of rows satisfying a condition; $T_2$ inserts a new row satisfying the predicate; $T_1$ re-queries and sees a new "phantom" row. | $R_1(\text{predicate}) \to \text{Insert}_2 \to C_2 \to R_1(\text{predicate})$ |
| **Lost Update** | Two transactions read the same data and simultaneously update it; one overwrite overwrites the other without awareness. | $R_1(A) \to R_2(A) \to W_1(A) \to W_2(A)$ |

---

### 8.3 Conflict Serializability & Precedence Graphs

A schedule $S$ is **Conflict Serializable** if it is conflict equivalent to some serial schedule.

#### Conflicting Operations
Two operations $O_i, O_j \in S$ conflict if:
1. They belong to different transactions ($i \neq j$).
2. They access the exact same data item $Q$.
3. At least one of the operations is a write ($W(Q)$).
   *   Conflict Pairs: $(R_i(Q), W_j(Q))$, $(W_i(Q), R_j(Q))$, $(W_i(Q), W_j(Q))$.

#### Building the Precedence Graph (Serialization Graph)
1. Create a node for each active transaction $T_i$.
2. Draw a directed edge $T_i \to T_j$ if an operation of $T_i$ precedes and conflicts with an operation of $T_j$.
3. **Serializability Theorem:** A schedule $S$ is conflict serializable if and only if its precedence graph contains **no directed cycles**.

---

### 8.4 Database Security: SQL Injection, DAC & Password Hashing

#### SQL Injection Mitigation
*   **Vulnerability Cause:** Directly concatenating raw user input strings into dynamic SQL statements.
*   **Defense Mechanism:** Prepared statements with parameterized query placeholders (`?` or `:param`), ORMs, and strict input validation.

#### Discretionary Access Control (DAC)
```sql
-- Grant read/write access to specific table
GRANT SELECT, INSERT, UPDATE ON Professor TO 'department_admin'@'localhost';

-- Revoke permissions
REVOKE INSERT, UPDATE ON Professor FROM 'department_admin'@'localhost';
```

#### Cryptographic Password Security
*   **Requirement:** Never store cleartext passwords.
*   **Technique:** Use slow, memory-hard cryptographic hash functions (e.g., bcrypt, Argon2, PBKDF2) combined with a cryptographically secure random **Salt** per user to prevent Rainbow Table attacks.

---

## 9. Unit 8: Step-by-Step Methodological Algorithms & Solution Recipes

### 9.1 Recipe 1: Solving Exam Question A (Conceptual Analysis & Cardinalities)

Follow this 4-step template to secure maximum points on Question A:

```
STEP-BY-STEP RECIPE FOR QUESTION A
1. Entity Identification:
   - Strong Entities: List entity name, brief description, and independent existence justification.
   - Weak Entities: List entity name, identifying/owner entity, and reason for key insufficiency.
2. Attribute Categorization:
   - For every entity, list all attributes and explicitly classify them:
     (Simple/Composite, Single-valued/Multi-valued, Stored/Derived, Key/Partial Key).
3. Key Specifications:
   - Enumerate all Candidate Keys for each entity.
   - Declare the chosen Primary Key.
   - For weak entities, state the Partial Key (Discriminator) and the resulting composite PK.
4. Relationships & Cardinality Justifications (CRITICAL):
   - For every relationship, write a 2-directional verbal justification:
     "Direction A -> B: One [A] can be associated with [0..1 / 1..N] [B] because..."
     "Direction B -> A: One [B] can be associated with [0..1 / 1..N] [A] because..."
   - State the final Cardinality Ratio (1:1, 1:N, N:M).
   - State the Participation Constraints (Total vs. Partial) on each side.
```

---

### 9.2 Recipe 2: Drawing ER Diagrams (Question B)

1. Draw **Strong Entities** as single rectangular boxes.
2. Draw **Weak Entities** as double rectangular boxes.
3. Draw **Relationships** as diamonds (single diamond for regular relationships, double diamond for identifying relationships).
4. Connect entities to relationships with:
   *   **Double Line:** Total / mandatory participation.
   *   **Single Line:** Partial / optional participation.
   *   Label the cardinality ($1, N, M$) next to each entity line.
5. Draw **Attributes** as ovals:
   *   Solid underlined oval: Primary Key.
   *   Dashed underlined oval: Partial Key.
   *   Double oval: Multi-valued attribute.
   *   Dashed oval: Derived attribute.
   *   Subdivided branching ovals: Composite attribute.

---

### 9.3 Recipe 3: Converting ER to Relational Tables (Question C)

1. Map each **Strong Entity** to a table. Underline its primary key: `| PK | Attr1 | Attr2 |`.
2. Map each **Weak Entity** to a table. Underline the composite key: `| Owner_PK | Partial_Key | Attr1 |`.
3. For **1:N Relationships**, insert the 1-side's PK into the N-side table as a Foreign Key column.
4. For **1:1 Relationships**, insert one table's PK into the table with Total Participation as a Foreign Key (declare `UNIQUE`).
5. For **N:M Relationships**, create a brand new Junction Table whose PK is the combination of both FKs: `| FK1 | FK2 | Rel_Attr |`.
6. For **Multi-Valued Attributes**, create a new table: `| Owner_PK | Multi_Valued_Value |`.
7. List all **Foreign Keys** explicitly beneath each table with their referenced tables and cascade options.

---

### 9.4 Recipe 4: Candidate Key & Normal Form Derivation

1. **Find $X^+$ for attribute combinations:**
   *   Identify all attributes appearing only on LHS (must be in all keys).
   *   Identify attributes appearing on RHS only (cannot be part of any minimal candidate key).
2. **Test 2NF:** Check if any FD $X \to Y$ has $X$ as a *proper subset* of a candidate key and $Y$ is non-prime.
3. **Test 3NF:** For all non-trivial FDs $X \to Y$, check if $X$ is a superkey or $Y$ is prime.
4. **Test BCNF:** For all non-trivial FDs $X \to Y$, check if $X$ is a superkey.

---

## 10. Unit 9: Official Schema & ER Notation Reference Sheet

```
+---------------------------------------------------------------------------------------------------+
| NOTATION COMPARISON & CONVERSION CHEAT SHEET                                                      |
+--------------------------+-----------------------+-----------------------+------------------------+
| Semantic Element         | Chen ER Notation      | Crow's Foot Notation  | Relational Schema      |
+--------------------------+-----------------------+-----------------------+------------------------+
| Strong Entity            | Single Rectangle      | Box with Header       | Table Name             |
| Weak Entity              | Double Rectangle      | Box with FK in PK     | Table with Composite PK|
| Primary Key              | Underlined in Oval    | PK symbol in header   | Underlined Column Name |
| Partial Key              | Dashed Underline      | Discriminator in PK   | Underlined in Table PK |
| Multi-Valued Attribute   | Double Oval           | Not permitted         | Separate Child Table   |
| Derived Attribute        | Dashed Oval           | Not stored (Virtual)  | Computed column/View   |
| 1:1 Relationship         | Diamond (1 : 1)       | 1 -- 1 Line           | FK in total side (UQ)  |
| 1:N Relationship         | Diamond (1 : N)       | 1 -- {< Line          | FK in N-side Table     |
| N:M Relationship         | Diamond (N : M)       | }< -- >{ Line         | Junction / Bridge Table|
| Identifying Relationship | Double Diamond        | Identifying Parent FK | Child Table with FK    |
+--------------------------+-----------------------+-----------------------+------------------------+
```

---

## 11. Unit 10: Critical Exam Traps & Checklist of Common Mistakes

| # | Fatal Exam Trap | Correct Rule / Avoidance Strategy |
|---|---|---|
| 1 | **Placing Foreign Key on the 1-side in 1:N relationships** | In a 1:N relationship, the Foreign Key **must** be placed in the table on the **N-side** (many-side). Placing it on the 1-side would require multi-valued entries or repeating rows, violating 1NF! |
| 2 | **Forgetting to include the Owner PK in Weak Entity tables** | A weak entity table cannot exist with only its partial key. Its primary key **must** be composite: $(\text{Owner\_PK}, \text{Partial\_Key})$. Both columns must be underlined. |
| 3 | **Treating Multi-Valued Attributes as simple table columns** | Multi-valued attributes (e.g., phone numbers, colors) **cannot** be stored as comma-separated strings or repeated columns. They must become a separate table with $\underline{(\text{Parent\_PK}, \text{Attr\_Value})}$. |
| 4 | **Forgetting the Composite Primary Key in N:M Junction Tables** | A junction table representing an N:M relationship must have a composite Primary Key made up of both foreign keys: $\underline{(\text{FK}_1, \text{FK}_2)}$. Underline both! |
| 5 | **Omitting relationship attributes in ER-to-Relational mapping** | Descriptive attributes of 1:N relationships move into the N-side table. Descriptive attributes of N:M relationships move into the Junction Table. |
| 6 | **Failing to justify cardinalities from both directions in Question A** | Never just state "It is 1:N". You must explain: (1) "For each instance of A, how many B?" AND (2) "For each instance of B, how many A?" Without two-way justification, points will be deducted. |
| 7 | **Confusing Total vs. Partial Participation** | Total participation means min cardinality is 1 (every instance must participate, drawn with double line). Partial means min cardinality is 0 (optional). |
| 8 | **Confusing 3NF and BCNF definitions** | In 3NF, $X \to Y$ is valid if $X$ is a superkey OR $Y$ is a prime attribute. In BCNF, $X$ **must** be a superkey without exception. |
| 9 | **Writing Relational Algebra Set Operations on Incompatible Relations** | $R \cup S$, $R \cap S$, and $R - S$ require $R$ and $S$ to be **union-compatible** (same number of attributes with identical compatible domains). Always use $\pi$ before set operations if column lists differ. |
| 10 | **Using WHERE instead of HAVING for aggregate condition filtering** | Aggregate conditions (e.g., `COUNT(*) > 3`, `AVG(salary) >= 2000`) **cannot** appear in `WHERE`. They must be placed in `HAVING` after `GROUP BY`. |
| 11 | **Assuming Transitive FDs are automatically 2NF violations** | A transitive dependency ($X \to Y$ where $X$ is not a candidate key) violates **3NF**, not 2NF. 2NF is violated only by *partial dependencies* (where LHS is a proper subset of a candidate key). |
| 12 | **Creating Circular Foreign Key Deadlocks** | Avoid creating mutual mandatory foreign key constraints between two tables without making at least one foreign key nullable or deferrable. |
| 13 | **Forgetting ON DELETE CASCADE on Weak Entities** | Because weak entities cannot exist without their owner, the foreign key referencing the owner entity must specify `ON DELETE CASCADE`. |
| 14 | **Forgetting to Underline Primary Keys in Question C tables** | The exam rubric strictly requires primary keys to be underlined. Always underline every single component of simple and composite primary keys. |
| 15 | **Confusing Cartesian Product with Natural Join in Relational Algebra** | $R \times S$ pairs every tuple of $R$ with every tuple of $S$ without matching keys. $R \bowtie S$ filters pairs where shared common attribute names match and eliminates redundant duplicate columns. |

---
*End of Complete Theoretical Exam Guide — Study this document alongside `test_prep.md` to achieve a 10/10 in Database Systems (Course 404).*
