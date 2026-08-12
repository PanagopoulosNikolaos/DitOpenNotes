# Database Life Cycle & Database Design
*Database Life Cycle & Database Design*

---

## Table of Contents
*Table of Contents*

1. [Introduction](#introduction)
2. [Step 1: Requirements Collection & Analysis](#step-1-requirements-collection-analysis)
   - [Defining User and Organizational Needs](#defining-user-and-organizational-needs)
   - [Documenting Business Functions and Specifications](#documenting-business-functions-and-specifications)
3. [Step 2: Conceptual Design](#step-2-conceptual-design)
   - [Creating the Entity-Relationship Model](#creating-the-entity-relationship-model)
   - [Schematic Visualization of the Logical Structure](#schematic-visualization-of-the-logical-structure)
4. [Step 3: Logical Design](#step-3-logical-design)
   - [Transition to the Relational Data Model](#transition-to-the-relational-data-model)
   - [Converting the Conceptual Model into Dependent Tables](#converting-the-conceptual-model-into-dependent-tables)
5. [Step 4: Physical Design & Implementation](#step-4-physical-design-implementation)
   - [Internal File Organization in the System](#internal-file-organization-in-the-system)
   - [SQL Programming and Physical Structure Creation](#sql-programming-and-physical-structure-creation)
6. [Comparative Table: The 4 Steps of the Database Life Cycle](#comparative-table-the-4-steps-of-the-database-life-cycle)
7. [Summary Table of Key Concepts](#summary-table-of-key-concepts)
8. [Key Takeaways](#key-takeaways)

---

## Introduction

The **Database Life Cycle (DBLC)** is the structured, iterative process of designing, developing and maintaining a database, from the initial needs analysis to the full physical implementation. The existence of a standardized cycle ensures that the database meets the real business requirements, is structurally sound and can be implemented efficiently on the chosen system. Failure to follow this process leads to data redundancy, inconsistencies and non-scalable schemas. The study of the life cycle is the foundation for understanding the ER Model, the Relational Model and SQL, which are analyzed in the following topics.

---

## Step 1: Requirements Collection & Analysis
*Step 1: Requirements Collection & Analysis*

The first step is the **foundation** of the entire design process. Without a clear and complete understanding of the needs of the organization and its users, any data model produced later will be incomplete or wrong. In this step, the designer is not yet concerned with technical details (tables, data types), but with **understanding what the system must do**.

**Analogy**: It is like the architect who, before designing a building, talks with the future occupants to learn how many rooms they need, what use they will have, which people will have access and what the practical needs of daily operation are.

```text
  +--------------------------------------------------+
  |          STEP 1: REQUIREMENTS ANALYSIS           |
  +--------------------------------------------------+
  |                                                  |
  |  Interviews                                      |
  |  With Users  --->  [ Requirements Document ]     |
  |                              |                   |
  |  Analysis         Functional Requirements        |
  |  of Business    Non-Functional Requirements      |
  |  Processes            Data Constraints           |
  |                                                  |
  +--------------------------------------------------+
```

### Defining User and Organizational Needs
*Defining User and Organizational Needs*

**Requirements Analysis** is the systematic collection and documentation of the needs of all stakeholders — users, administrators and the organization — who will use or be affected by the database.

The basic requirements collection techniques include:

- **Interviews**: Direct communication with end users and department heads to understand their needs.
- **Observation**: Monitoring the existing workflow to identify weaknesses.
- **Analysis of Existing Documents**: Studying the forms, reports and files that the organization already uses.
- **Questionnaires**: Systematic collection of opinions from a large number of users.

Requirements are divided into two categories:

| Category | Definition | Examples |
|---|---|---|
| **Functional Requirements** | What the system must do | Storing orders, customer search, generating reports |
| **Non-functional Requirements** | How it must do it | Response time < 2 sec, 500 concurrent users, 99.9% availability |

**Exam Note:** Requirements analysis is a purely **conceptual phase** — no decision about technology, DBMS or table structure is made at this stage.

---

### Documenting Business Functions and Specifications
*Documenting Business Functions and Specifications*

**Business Functions** are the processes performed by the organization that create, modify or use data. Documenting them defines the scope of the database.

**Example — University System**:

```text
  BUSINESS OPERATIONS:
  
  1. Student Registration
     - What data is created? Student file, registration number
     - Which users are involved? Secretariat (entry), Student (read)
  
  2. Course Enrollment
     - What data is created? Enrollment per semester, student-course mapping
     - Which users are involved? Student (enrollment), Professor (check)
  
  3. Grade Entry
     - What data is created? Grade per student per course
     - Which users are involved? Professor (entry), Secretariat (verification)
```

The result of this phase is a **Requirements Specification Document** that contains:

- A list of all **entities** that must be stored (e.g. Student, Course, Professor).
- A list of **relationships** between them (e.g. "a student attends a course").
- **Data constraints** (e.g. the grade must be between 0 and 10).
- The required **operations** (CRUD: Create, Read, Update, Delete).

---

## Step 2: Conceptual Design
*Step 2: Conceptual Design*

Conceptual design converts the requirements collected in Step 1 into a **high-level, technology-independent model** that describes the logical structure of the data. The designer is not yet concerned with a specific DBMS or SQL — the model produced must be understandable by both technical and non-technical stakeholders.

**Analogy**: Conceptual design is like the blueprint of a building — it shows the rooms, doors and connections without yet specifying the type of cement or the electrical installation.

### Creating the Entity-Relationship Model
*Creating the Entity-Relationship Model*

The **Entity-Relationship Model (ER Model)** is a conceptual data modeling tool that represents the data of an organization as a set of **entities**, **attributes** and **relationships** between them.

The three basic structural components of the ER Model:

| Component | Symbol (Chen Notation) | Description |
|---|---|---|
| **Entity** | Rectangle | Something with independent existence for which data is stored |
| **Attribute** | Ellipse | Characteristic/property of an entity |
| **Relationship** | Rhombus | Connection/interaction between two or more entities |

**Exam Note:** The ER Model is **technology-independent** — it does not refer to a specific DBMS, language or storage structure. It is designed to communicate the logical structure, not the implementation.

---

### Schematic Visualization of the Logical Structure
*Schematic Visualization of the Logical Structure*

The production of the **ER Diagram (ERD)** is the main deliverable of this phase. The ERD graphically represents all entities, their attributes and the relationships between them.

**ERD Example — University System**:

```text
  +----------------+                    +----------------+
  |   STUDENT     |                    |    COURSE      |
  +----------------+       N:M          +----------------+
  | am (PK)        |<>---( Enrolls )-->| course_id (PK) |
  | onoma          |                    | titlos         |
  | eponymo        |                    | didaktikes_mon |
  | email          |                    +----------------+
  +----------------+                            |
          |                                    1:N
          |                                     |
         1:N                           +----------------+
          |                            |   DEPARTMENT   |
          |                            +----------------+
  +----------------+                   | dept_id (PK)   |
  |  REGISTRATION  |                   | onoma_tmimatos |
  +----------------+                   +----------------+
  | am (FK)        |
  | course_id (FK) |
  | vathmos        |
  | etosvathmos    |
  +----------------+
```

The characteristics captured in the ERD are:

- **Cardinality**: 1:1, 1:N, N:M — the number of instances of each entity that participate in the relationship.
- **Participation**: Total (every instance participates) or partial (not mandatory).
- **Keys**: The attributes that uniquely identify each instance.

**Key Distinction:** The ERD is the "bridge" between requirements analysis (Step 1) and logical design (Step 3). It is the model shared with clients/users for validation before proceeding to logical design.

---

## Step 3: Logical Design
*Step 3: Logical Design*

Logical design translates the conceptual model (ERD) into the **Relational Data Model**, which is the basis for the subsequent implementation with SQL. In this step, the designer begins to think in terms of tables, columns and keys, while applying **Normalization** to eliminate redundancy.

**Analogy**: If the ERD is the architectural plan, logical design is its conversion into detailed structural drawings that guide construction.

### Transition to the Relational Data Model
*Transition to the Relational Data Model*

The **Relational Data Model** is a data organization model based on the concept of the **relation** — a mathematical term that practically corresponds to a **table** with rows (tuples/rows) and columns (attributes/columns).

The rules for converting ER to the Relational Model are:

| ER Model Component | Mapping to the Relational Model |
|---|---|
| **Strong Entity** | New table with Primary Key |
| **Weak Entity** | New table with a composite Primary Key (own PK + FK of the parent entity) |
| **1:1 Relationship** | Foreign Key in one of the two tables |
| **1:N Relationship** | Foreign Key on the N side |
| **N:M Relationship** | New intermediate table (junction/bridge table) with Foreign Keys from both tables |
| **Simple Attribute** | Column in the table |
| **Multivalued Attribute** | Separate table with FK to the original table |
| **Derived Attribute** | Usually not stored — computed via a Query |

**Exam Note:** The rule for **N:M** relationships is extremely important — the Relational Model **does not directly support** many-to-many relationships. An intermediate table is always required.

---

### Converting the Conceptual Model into Dependent Tables
*Converting the Conceptual Model into Dependent Tables*

The conversion of the ERD of the university example into the Relational Model:

```text
  ER DIAGRAM (Step 2):
  STUDENT ---( N:M Enrolls )--- COURSE

  RELATIONAL MODEL (Step 3):
  
  Foititis(<u>am</u>, onoma, eponymo, email, dept_id#)
  Mathima(<u>course_id</u>, titlos, didaktikes_mon, dept_id#)
  Dilosi(<u>am#, course_id#</u>, vathmos, etosvathmos)
         \_______________________________________/
              Intermediate table for N:M
```

In the relational schema, the convention used is:
- `<u>field</u>` — Primary Key (underlined)
- `field#` — Foreign Key

**Normalization** is applied in this step to ensure that each table:

1. Is in **First Normal Form (1NF)**: Every column contains atomic values.
2. Is in **Second Normal Form (2NF)**: No non-key attribute depends partially on the PK.
3. Is in **Third Normal Form (3NF)**: No non-key attribute depends transitively on the PK.

```text
  2NF VIOLATION (Example):
  Order_Product(order_id, product_id, product_price, quantity)
                     [__________________PK_________________]
  
  Problem: product_price depends ONLY on product_id,
             not on the combination (order_id, product_id).
  
  SOLUTION — Decomposition:
  Order_Product(order_id, product_id#, quantity)
  Product(product_id, product_price, description)
```

---

## Step 4: Physical Design & Implementation
*Step 4: Physical Design & Implementation*

Physical design concerns the **translation** of the logical schema (Step 3) into specific storage structures and SQL code for a **specific DBMS** (e.g. MySQL, PostgreSQL). In this step, decisions are made about performance, storage and security.

**Analogy**: Physical design is the actual **construction** of the building based on the technical drawings — materials are chosen, walls are placed and systems are installed.

### Internal File Organization in the System
*Internal File Organization in the System*

**Internal Data Organization** refers to the way the DBMS stores data on disk at the file level. These decisions directly affect data retrieval performance.

Basic organization techniques:

| Organization Technique | Description | Suitable Use |
|---|---|---|
| **Heap File** (unordered organization) | Records stored without a specific order | Bulk data loading, infrequent search |
| **Sequential File** | Records sorted by a key | Range queries |
| **Hash File** | Uses a hash function for direct record lookup | Equality queries |
| **B-Tree / B+Tree Index** | Tree structure for very fast search | Indexing in OLTP systems |

**Indexes** are a basic optimization tool:

```text
  TABLE without Index:            TABLE with Index (B+Tree):
  
  am  | name    | grade         Index on "am":
  ----|---------|-------             Root: [500]
   1  | Alexis  |   7.5              /              \
  ...                              [250]            [750]
  250 | Eleni   |   8.0           /   \            /    \
  ...                            ...  ...         ...    ...
  500 | Nikos   |   6.0
  ...
  999 | Maria   |   9.0
  
  Search am=500: Scan 999 records   Search am=500: 3 steps (log n)
```

**Exam Note:** Creating an Index speeds up searches (`SELECT`) but slows down insertions/modifications (`INSERT/UPDATE`) because the tree structure must be updated. The balance between read and write performance is a critical physical design decision.

---

### SQL Programming and Physical Structure Creation
*SQL Programming and Physical Structure Creation*

In this final sub-step, the logical schema is converted into **executable SQL code** (DDL — Data Definition Language) that creates the actual structures in the DBMS.

**DDL Example — Creating a University Database**:

**Initial state** (no tables exist):

```text
  mysql> SHOW TABLES;
  Empty set (0.00 sec)
```

**Executing the DDL**:

```sql
-- Creating a university database
CREATE DATABASE university_db;
USE university_db;

-- Creating the Department table (does not depend on another table - created first)
CREATE TABLE Tmima (
    dept_id   INT           NOT NULL,
    onoma     VARCHAR(100)  NOT NULL,
    tilefono  VARCHAR(15),
    CONSTRAINT pk_tmima PRIMARY KEY (dept_id)
);

-- Creating the Student table (depends on Department via Foreign Key)
CREATE TABLE Foititis (
    am        INT           NOT NULL,
    onoma     VARCHAR(50)   NOT NULL,
    eponymo   VARCHAR(50)   NOT NULL,
    email     VARCHAR(100)  UNIQUE,
    dept_id   INT           NOT NULL,
    CONSTRAINT pk_foititis  PRIMARY KEY (am),
    CONSTRAINT fk_foititis_tmima FOREIGN KEY (dept_id)
        REFERENCES Tmima(dept_id)
);

-- Creating the Course table
CREATE TABLE Mathima (
    course_id       INT          NOT NULL,
    titlos          VARCHAR(150) NOT NULL,
    didaktikes_mon  INT          DEFAULT 3,
    dept_id         INT          NOT NULL,
    CONSTRAINT pk_mathima PRIMARY KEY (course_id),
    CONSTRAINT fk_mathima_tmima FOREIGN KEY (dept_id)
        REFERENCES Tmima(dept_id)
);

-- Creating the intermediate Enrollment table (for the N:M Student-Course relationship)
CREATE TABLE Dilosi (
    am          INT   NOT NULL,
    course_id   INT   NOT NULL,
    vathmos     DECIMAL(4,2),
    etosvathmos YEAR,
    CONSTRAINT pk_dilosi PRIMARY KEY (am, course_id),
    CONSTRAINT fk_dilosi_foititis FOREIGN KEY (am)
        REFERENCES Foititis(am),
    CONSTRAINT fk_dilosi_mathima  FOREIGN KEY (course_id)
        REFERENCES Mathima(course_id)
);
```

**State after execution**:

```text
  mysql> SHOW TABLES;
  +-------------------------+
  | Tables_in_university_db |
  +-------------------------+
  | Dilosi                  |
  | Foititis                |
  | Mathima                 |
  | Tmima                   |
  +-------------------------+
  4 rows in set (0.00 sec)
```

**Creating an Index to improve performance**:

```sql
-- Creating an index on eponymo for fast search of students by surname
CREATE INDEX idx_foititis_eponymo ON Foititis(eponymo);

-- Composite index for searching enrollments by year
CREATE INDEX idx_dilosi_etos ON Dilosi(etosvathmos, am);
```

**Key Distinction:** The order of table creation is critical when Foreign Keys exist — the **referenced table** must be created **before** the table that references it. In the example: `Tmima → Foititis/Mathima → Dilosi`.

---

## Comparative Table: The 4 Steps of the Database Life Cycle
*Comparative Table: The 4 Steps of the Database Life Cycle*

| Step | Phase | Input | Output | Tools / Techniques |
|---|---|---|---|---|
| **Step 1** | Requirements Collection & Analysis | Interviews, documents, observation | Requirements Specification Document | Interviews, questionnaires, UML Use Cases |
| **Step 2** | Conceptual Design | Requirements Document | ER Diagram (ERD) | Chen Notation, Crow's Foot Notation |
| **Step 3** | Logical Design | ERD | Relational Schema | ER-to-Relational conversion rules, Normalization |
| **Step 4** | Physical Design & Implementation | Relational Schema | SQL DDL scripts, physical storage structures | SQL, Indexes, Partitioning, Query Optimization |

```text
  DATABASE LIFE CYCLE:
  
  [ Requirements ]
       |
       | Step 1: Analysis
       v
  [ Requirements Document ]
       |
       | Step 2: Conceptual Design
       v
  [ ER Diagram ]
       |
       | Step 3: Logical Design
       v
  [ Relational Schema ]
       |
       | Step 4: Physical Design & Implementation
       v
  [ Operational Database ]
       |
       | Maintenance / Evolution
       |-----> Return to Step 1 (New Requirements)
```

**Exam Note:** The life cycle is **iterative** — new requirements or changes in the organization lead to a restart of the process, especially steps 1 and 2.

---

## Summary Table of Key Concepts
*Summary Table of Key Concepts*

| Concept | Definition | Key Characteristic / Rule |
|---|---|---|
| **DB Life Cycle** (DBLC) | Iterative process of designing, developing and maintaining a DB | Consists of 4 main steps |
| **Requirements Analysis** | Collection and documentation of user and organizational needs | Conceptual phase — not about technical implementation |
| **Functional Requirements** | What the system must do | Define the CRUD operations |
| **Non-functional Requirements** | How the system must behave | Response time, availability, scalability |
| **ER Model** | Conceptual model with Entities, Attributes and Relationships | Technology-independent |
| **ERD** | Graphical representation of the ER Model | Uses rectangles, ellipses, rhombuses |
| **Relational Model** | Organization of data into tables (relations) | Table = Relation, Row = Tuple, Column = Attribute |
| **Normalization** | Process of eliminating redundancy and dependencies | Applied in logical design (1NF, 2NF, 3NF) |
| **Junction Table** | Intermediate table for representing an N:M relationship | Necessary — the relational model does not directly support N:M |
| **DDL** (Data Definition Language) | Subset of SQL for defining DB structures | `CREATE TABLE`, `ALTER TABLE`, `DROP TABLE` |
| **Index** | Data structure that speeds up searches | Speeds up SELECT, slows down INSERT/UPDATE |
| **Heap File** | Unordered storage of records without sorting | Suitable for bulk inserts |
| **B+Tree Index** | Balanced tree structure for indexing | O(log n) search time |
| **Referential Integrity** | Referential integrity via Foreign Keys | The referenced table is created first |

---

## Key Takeaways
*Key Takeaways*

- The **Database Life Cycle** follows 4 distinct steps: Requirements Analysis → Conceptual Design → Logical Design → Physical Design & Implementation.
- **Step 1 (Requirements Analysis)** is entirely conceptual — no technical decision is made, only the needs of the organization are understood.
- **Step 2 (Conceptual Design)** produces the **ER Diagram** — a technology-independent model that captures Entities, Attributes and Relationships.
- **Step 3 (Logical Design)** converts the ERD into a **Relational Schema** by applying the conversion rules and Normalization (1NF/2NF/3NF).
- **N:M relationships** in the ER Model are **always** converted into an intermediate table (junction table) in the Relational Model — this is a fundamental rule.
- **Step 4 (Physical Design)** implements the schema with SQL DDL for a specific DBMS, making decisions about Indexes, file types and performance optimization.
- The **order of table creation** with Foreign Keys is critical: the referenced table must be created **first** so that referential integrity is not violated.
- **Indexes** speed up searches (O(log n) with B+Tree), but burden insertions/updates — this balance is a central physical design decision.
- The life cycle is **iterative**: new business needs lead to a restart from Step 1.
- **Key Distinction:** Conceptual design concerns **what** is stored, logical design **how** it is organized, and physical design **where** and **with what performance** it is stored.
