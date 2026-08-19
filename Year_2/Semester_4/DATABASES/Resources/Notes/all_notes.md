---
# topic_1_introduction_and_basic_concepts.md
---

# Introduction & Basic Concepts
*Introduction & Basic Concepts*

---

## Table of Contents
*Table of Contents*

1. [Introduction](#introduction)
2. [Data, Information and Knowledge](#data-information-and-knowledge)
   - [Processing of Raw Data](#processing-of-raw-data)
   - [Production of Information](#production-of-information)
   - [Creation of Knowledge for Decision-Making](#creation-of-knowledge-for-decision-making)
3. [Information Systems (IS)](#information-systems-is)
   - [Hardware](#hardware)
   - [Software](#software)
   - [Data](#data)
   - [Processes](#processes)
   - [People](#people)
4. [Database Management Systems (DBMS)](#database-management-systems-dbms)
   - [Storage, Retrieval and Efficient Management](#storage-retrieval-and-efficient-management)
   - [Data Protection and Security Policies](#data-protection-and-security-policies)
   - [Concurrent Access](#concurrent-access)
   - [Minimization of Data Redundancy and Inconsistency](#minimization-of-data-redundancy-and-inconsistency)
5. [Database Architecture: ANSI/SPARC Three-Schema Architecture](#database-architecture-ansisparc-three-schema-architecture)
   - [External Level](#external-level)
   - [Conceptual Level](#conceptual-level)
   - [Internal Level](#internal-level)
   - [Mappings Between Levels](#mappings-between-levels)
   - [Logical and Physical Data Independence](#logical-and-physical-data-independence)
6. [Comparative Table: DBMS vs. File Processing Systems](#comparative-table-dbms-vs-file-processing-systems)
7. [Summary Table of Key Concepts](#summary-table-of-key-concepts)
8. [Key Takeaways](#key-takeaways)

---

## Introduction

Databases constitute the cornerstone of modern computing infrastructure, as every system that handles data — from e-commerce stores to medical records — relies on their principles. The need for structured, reliable and rapid access to large volumes of data led to the transition from traditional file-based systems to modern Database Management Systems (DBMS). Understanding the hierarchy Data → Information → Knowledge, the structure of Information Systems and the fundamental characteristics of a DBMS is necessary before any study of database design or queries.

---

## Data, Information and Knowledge
*Data, Information and Knowledge*

Understanding the difference between data, information and knowledge is fundamental. These three concepts form a hierarchy — each successive level moves from the raw and unstructured to the interpreted and actionable.

```text
  Raw facts / events
            |
            v
      [ DATA ]
            |
    Processing / Interpretation
            |
            v
     [ INFORMATION ]
            |
    Experience / Analysis / Context
            |
            v
       [ KNOWLEDGE ]
            |
    Application to decision-making
            |
            v
     [ DECISION / ACTION ]
```

### Processing of Raw Data
*Processing of Raw Data*

**Data** is a raw, uninterpreted fact or event that is recorded without context or meaning. It corresponds to numbers, characters, images, sounds or any other raw record.

- **Characteristics**: It has no meaning on its own; it is objective and unprocessed.
- **Examples**: `37`, `Athens`, `2024-05-01`, `912345678`, `85`.

**Analogy**: Imagine a library warehouse with thousands of papers scattered randomly on the floor. Each paper has a number or a word written on it — these are the data. We do not yet know what they mean.

**Key Distinction:** Data by themselves cannot be used for decision-making. Processing is needed for them to acquire meaning.

---

### Production of Information
*Production of Information*

**Information** is the result of processing, organizing or interpreting data in a way that gives meaning and usefulness to a recipient.

- **Characteristics**: It has context, purpose and meaning. It answers questions of the type "who", "what", "when", "where".
- **Example**: The data `85` (grade), `Nikolaos Panagopoulos` (student), `Databases` (course) together produce the information: "Student Nikolaos Panagopoulos received a grade of 85 in the course Databases."

| Data | Information |
|---|---|
| `85` | Student's grade in a specific course |
| `37` | Temperature in Celsius for today in Athens |
| `2024-05-01` | Exam date for the Databases course |

**Exam Note:** Information is not simply "more data" — it is data with **context and purpose**. This is the fundamental difference.

---

### Creation of Knowledge for Decision-Making
*Creation of Knowledge for Decision-Making*

**Knowledge** is the application of information through experience, analysis and context, enabling informed decision-making.

- **Characteristics**: It is contextual, dynamic and based on accumulated experience.
- **Example**: After analyzing the grades of many students (information), we know that "students who have not attended the laboratories fail the exams", so the decision is made to make attendance mandatory.

```text
  Data:   37, 38, 36, 39, 40  (temperatures)
       |
  Information: The temperature in Athens is increasing every summer
       |
  Knowledge:      Climate change affects the Mediterranean
       |
  Decision:    Implementation of measures to reduce CO2 emissions
```

---

## Information Systems (IS)
*Information Systems (IS)*

An **Information System (IS)** is an organized set of interconnected components that collects, stores, processes and disseminates information to support decision-making and the control of an organization.

**Analogy**: An IS acts like the nervous system of an organization — it collects signals (data) from the environment, processes them and sends commands (information) to the appropriate departments for action.

The five basic components of an IS are:

```text
  +--------------------------------------------------+
  |             INFORMATION SYSTEM (IS)              |
  +--------------------------------------------------+
  |                                                  |
  |  [ HARDWARE ]   [ SOFTWARE ]   [ DATA ]          |
  |  Hardware      Software         Data             |
  |                                                  |
  |      [ PROCESSES ]    [ PEOPLE ]                 |
  |         Processes           People               |
  |                                                  |
  +--------------------------------------------------+
```

### Hardware
*Hardware*

**Hardware** is the set of physical, tangible devices that make up the infrastructure of the information system.

- Servers, workstations, network devices (routers, switches).
- Storage media: HDD, SSD, NAS (Network-Attached Storage), cloud storage.
- Peripheral input/output devices (printers, scanners, monitors).

**Exam Note:** Hardware is the **physical layer** of the IS — without it, nothing else can function.

---

### Software
*Software*

**Software** is the set of programs, applications and operating systems that control the hardware and process the data.

- **System Software**: Operating systems (Linux, Windows Server), drivers.
- **Application Software**: ERP management software, CRM, web applications.
- **DBMS Software**: MySQL, PostgreSQL, Oracle Database, Microsoft SQL Server.

---

### Data
*Data*

In the context of IS, **Data** constitutes the core of the system — it is the raw material that is stored, organized, processed and retrieved.

- Structured data: Stored in tables with a clear schema.
- Semi-structured data: XML, JSON files.
- Unstructured data: Images, videos, email, text documents.

---

### Processes
*Processes*

**Processes** are the sets of rules, policies and procedural steps that define how data is collected, stored, processed and distributed within the organization.

- They include data entry procedures, backup procedures, and workflows.
- **Exam Note:** Without well-defined processes, even the best hardware and software cannot produce reliable results.

---

### People
*People — Users & Administrators*

**People** are one of the most critical components of the IS. They are divided into two main categories:

| Role | Description | Responsibilities |
|---|---|---|
| **Users** | Individuals who interact with the system on a daily basis | Data entry, executing queries, reading reports |
| **Administrators (DBA)** | Database Administrators — specialized technicians | Installation, configuration, maintenance, security, backup/restore |

The **Database Administrator (DBA)** is the role responsible for the smooth operation, performance, security and integrity of the database.

---

## Database Management Systems (DBMS)
*Database Management Systems*

A **Database Management System (DBMS)** is a set of software that enables the creation, maintenance, retrieval and management of databases in an efficient, secure and organized manner.

**Analogy**: A DBMS is like a librarian in a huge library: it knows where each book (data) is located, serves many users simultaneously, ensures there are no duplicate records of the same book, and guarantees that only authorized individuals have access to sensitive material.

```text
  +----------------------------------------------------------+
  |                   DBMS Architecture                      |
  +----------------------------------------------------------+
  |                                                          |
  |   [ Application ]                                        |
  |              |                                           |
  |              v                                           |
  |   [ DBMS Engine (Query Processor, Transaction Mgr) ]     |
  |              |                                           |
  |              v                                           |
  |   [ Stored Data (Disk) ]                                 |
  |                                                          |
  +----------------------------------------------------------+
```

The four basic characteristics of a DBMS are analyzed below:

### Storage, Retrieval and Efficient Management
*Storage, Retrieval and Efficient Management*

A DBMS provides mechanisms for:

- **Storage**: Data is stored in structured form (tables, indexes) on disk, in a way that allows fast access.
- **Retrieval**: Through the SQL query language, the user can retrieve specific data with precision.
- **Efficient Management**: The Query Optimizer selects the optimal execution plan for each query, minimizing response time.

```sql
-- Example of a data retrieval query
SELECT first_name, last_name, grade
FROM students
WHERE grade >= 50;
```

**Exam Note:** Efficient retrieval differentiates a DBMS from a simple file system. Indexes speed up searches by avoiding a full table scan.

---

### Data Protection and Security Policies
*Data Protection and Security Policies*

A DBMS has built-in security mechanisms:

- **Authentication**: Verification of user identity (username/password, roles).
- **Authorization**: Control of access rights per user or role (GRANT/REVOKE in SQL).
- **Encryption**: Encryption of data at rest and in transit.
- **Audit Logs**: Recording of all actions for auditing purposes.

```sql
-- Granting read permissions to a specific user
GRANT SELECT ON students TO 'professor_user'@'localhost';

-- Revoking permissions
REVOKE SELECT ON students FROM 'professor_user'@'localhost';
```

| Security Mechanism | Function |
|---|---|
| Authentication | Verification of user identity |
| Authorization (GRANT/REVOKE) | Definition of rights per user/role |
| Views | Restriction of data visibility |
| Encryption | Protection of data from unauthorized reading |
| Backup & Recovery | Data recovery after failure |

---

### Concurrent Access
*Concurrent Access*

**Concurrency Control** is the ability of the DBMS to allow multiple users to access and modify data **concurrently**, without inconsistencies arising.

**Analogy**: Imagine two bank tellers simultaneously serving two customers who want to withdraw from the same account. Without Concurrency Control, both tellers would see the initial balance and approve both withdrawals — even though the balance suffices only for one. The DBMS prevents this scenario.

Basic Concurrency Control mechanisms:

- **Transactions**: Grouping operations into atomic units.
- **Locking**: Locking records while they are being modified.
- **MVCC** (Multi-Version Concurrency Control): A technique that allows reading without waiting.

```text
  User A                  User B
  --------                 --------
  READ balance = 1000      READ balance = 1000
  WRITE balance = 500      WRITE balance = 700   <-- CONFLICT!
       |                         |
       +----[ Lock Manager ]-----+
       |         DBMS           |
  READ balance = 1000      WAIT...
  WRITE balance = 500      READ balance = 500    (after A commits)
  COMMIT                   WRITE balance = 200
                           COMMIT
```

**Key Distinction:** Traditional file systems do not have built-in Concurrency Control — this is a major advantage of DBMS.

---

### Minimization of Data Redundancy and Inconsistency
*Minimization of Data Redundancy and Inconsistency*

**Data Redundancy** occurs when the same data is stored in multiple locations. This leads to **Data Inconsistency** — different copies diverge from one another.

**Problem Example (File-Based System)**:
```text
  Student File:        | ID | Name        | Dept.     | Dept. Phone    |
  ----------------------|----|-------------|-----------|----------------|
                        |  1 | A. Papas    | CS        | 210-1234567    |
                        |  2 | B. Nikos    | CS        | 210-1234567    |

  Department File:     | Dept.   | Phone          |
  ---------------------|---------|---------------|
                        | CS      | 210-9999999   |  <-- INCONSISTENCY!
```

**Solution via DBMS — Normalization**:
```text
  Students Table:       | student_id | name     | dept_id |
                        |------------|----------|---------|
                        |     1      | A. Papas |   10    |
                        |     2      | B. Nikos |   10    |

  Departments Table:    | dept_id | dept_name | phone       |
                        |---------|-----------|------------|
                        |   10    | CS        | 210-1234567 |
```

Now the phone number is stored **only once**. If it changes, it is updated in a single place.

**Exam Note:** **Normalization** is the process of designing relational tables with the aim of minimizing redundancy and eliminating inconsistency. It is directly related to the Normal Forms: 1NF, 2NF, 3NF, BCNF.

---

## Database Architecture: ANSI/SPARC Three-Schema Architecture
*Database Architecture: ANSI/SPARC Three-Schema Architecture*

The **ANSI/SPARC three-schema architecture** (also called the **three-level architecture**) is the standard framework for describing the structure of a DBMS. It separates the database into **three levels of abstraction**, each serving a different user group, and defines **mappings** between them. This separation is the mechanism that delivers **data independence**.

```text
  +---------------------------------------------------------+
  |                     EXTERNAL LEVEL                      |
  |   (View 1)   (View 2)   (View 3)   ...   (View n)       |
  +-------------------------+-------------------------------+
                            |
                External / Conceptual Mapping
                            |
                            v
  +---------------------------------------------------------+
  |                   CONCEPTUAL LEVEL                      |
  |   (Logical schema: entities, relations, constraints)    |
  +-------------------------+-------------------------------+
                            |
                Conceptual / Internal Mapping
                            |
                            v
  +---------------------------------------------------------+
  |                    INTERNAL LEVEL                       |
  |   (Physical schema: files, indexes, storage structures) |
  +---------------------------------------------------------+
```

### External Level
*External Level (View Level)*

The **External Level** is the **highest** level — it describes **how each user group sees** the database. Each user or application interacts only with the portion of the database that concerns them, through **views**.

- Different users may have **different views** of the same data (a payroll clerk sees salaries, a receptionist sees only names and phones).
- Views can **hide** sensitive columns or rows, contributing to security.
- Implemented in SQL with `CREATE VIEW`.

### Conceptual Level
*Conceptual Level (Logical Level)*

The **Conceptual Level** is the **middle** level — it describes **what data is stored** and the relationships between them, for the entire database, **independently of physical storage details**.

- It corresponds to the **relational schema**: tables, attributes, primary/foreign keys and integrity constraints.
- It is the result of **Logical Design** (the E-R model converted to relations).
- There is exactly **one** conceptual schema for a database.

### Internal Level
*Internal Level (Physical Level)*

The **Internal Level** is the **lowest** level — it describes **how data is physically stored** on the storage media.

- It defines **file organizations, indexes (B-trees, hash indexes), record placement** and access paths.
- It is managed by the DBMS and is largely **invisible to users**.
- The **DBA** tunes this level to optimize performance.

### Mappings Between Levels
*Mappings Between Levels*

The three levels are connected by two types of mappings:

- **External/Conceptual Mapping**: connects each view to the conceptual schema.
- **Conceptual/Internal Mapping**: connects the conceptual schema to the physical schema.

These mappings are what enable **data independence**: a change at one level does not require changes at the level above it.

### Logical and Physical Data Independence
*Logical and Physical Data Independence*

**Data Independence** is the ability to change the schema at one level **without** having to change the schema at the next higher level. The three-schema architecture provides two types:

| Type | Definition | Absorbed change | Example |
|---|---|---|---|
| **Logical Data Independence** | The external schema is unaffected by changes in the **conceptual schema** | Adding/removing a table, column or constraint | Adding a `phone` column to `EMPLOYEES` — existing applications do not change |
| **Physical Data Independence** | The conceptual schema is unaffected by changes in the **internal (physical) schema** | Reorganizing files, adding/removing indexes, changing storage | Adding an index to speed up a query — tables and views do not change |

**Key Distinction:** Physical independence is **easier to achieve** and is handled entirely by the DBMS. Logical independence is **harder**, because changing the logical structure may invalidate existing views.

---

## Comparative Table: DBMS vs. File Processing Systems
*Comparative Table: DBMS vs. File Processing Systems*

| Feature | DBMS | File System |
|---|---|---|
| **Data Redundancy** | Minimized through normalization | High — multiple copies |
| **Data Inconsistency** | Prevented by integrity constraints | Frequent — different files diverge |
| **Concurrent Access** | Built-in Concurrency Control | Difficult or non-existent |
| **Data Security** | Detailed access control (GRANT/REVOKE) | Based only on the OS |
| **Data Independence** | High (logical & physical separation) | Low (data structure tied to the code) |
| **Recovery after Failure** | Automated via Transaction Logs | Manual, error-prone |
| **Data Integrity** | Enforced through constraints | The application carries the responsibility |
| **Query Support** | Powerful query language (SQL) | Requires custom code |
| **Scalability** | High — handles TB of data | Limited |

---

## Summary Table of Key Concepts
*Summary Table of Key Concepts*

| Concept | Definition | Key Characteristic |
|---|---|---|
| **Data** | Raw, uninterpreted fact or measurement | Objective, without context |
| **Information** | Processed data with meaning and context | Answers "who/what/when/where" |
| **Knowledge** | Information enriched with experience and analysis | Basis for decision-making |
| **IS (Information System)** | Set of Hardware + Software + Data + Processes + People | Supports organizational decisions |
| **DBMS** | Database management software | Storage, retrieval, security, concurrency |
| **DBA** | Database Administrator | Maintenance, security, DBMS performance |
| **Concurrency Control** | Management of concurrent access by multiple users | Prevents inconsistencies in concurrent transactions |
| **Data Redundancy** | Storage of the same data in multiple locations | Leads to Data Inconsistency |
| **Normalization** | Design process for reducing redundancy | Applies Normal Forms (1NF–BCNF) |
| **Transaction** | Atomic unit of work in the DBMS | Follows the ACID properties |
| **Three-Schema Architecture** | ANSI/SPARC separation into external, conceptual, internal levels | Enables data independence |
| **Logical Data Independence** | External schema unaffected by conceptual changes | Harder to achieve |
| **Physical Data Independence** | Conceptual schema unaffected by physical changes | Handled by the DBMS |

---

## Key Takeaways
*Key Takeaways*

- **Data → Information → Knowledge**: This hierarchy describes how raw facts are transformed into decision-making tools through processing and interpretation.
- An **Information System** consists of five interdependent components: Hardware, Software, Data, Processes, People — removing any one of them degrades the whole.
- A **DBMS** clearly outperforms traditional file systems in data independence, security, concurrency and integrity.
- **Concurrency Control** is critical in multi-user environments — without it, concurrent writes can lead to catastrophic data loss.
- **Data redundancy** is not simply a waste of space — it leads to inconsistency, maintenance difficulty and unreliable query results.
- **Normalization** is the basic technique for eliminating redundancy — it is directly linked to relational database design.
- The **DBA** (Database Administrator) is responsible for the security, maintenance and performance of the DBMS — this role is distinct from that of the ordinary user.
- **Security** in a DBMS is implemented at many levels: Authentication, Authorization (GRANT/REVOKE), Encryption and Audit Logs.
- **Key Distinction:** The difference between Data and Information is not quantitative but qualitative — context and interpretation are what transform data into information.
- DBMS are used in critical systems (banks, hospitals, e-commerce) precisely because they provide guarantees of **integrity, security and reliability** that simple file systems cannot offer.
- The **ANSI/SPARC three-schema architecture** splits the database into **External**, **Conceptual** and **Internal** levels, connected by mappings.
- **Logical data independence** isolates views from changes to the conceptual schema; **physical data independence** isolates the conceptual schema from changes to physical storage.
- **Key Distinction:** Logical independence is more difficult to guarantee than physical independence, because changing the logical structure can invalidate existing views.

---
# topic_2_database_lifecycle_and_design.md
---

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

---
# topic_3_entity_relationship_model.md
---

# Entity-Relationship Model (E-R)
*Entity-Relationship Model*

---

## Table of Contents
*Table of Contents*

1. [Introduction](#introduction)
2. [Entities](#entities)
   - [Strong Entities](#strong-entities)
   - [Weak Entities](#weak-entities)
   - [Comparative Table: Strong vs. Weak Entities](#comparative-table-strong-vs-weak-entities)
3. [Attributes](#attributes)
   - [Simple and Composite Attributes](#simple-and-composite-attributes)
   - [Single-Valued and Multi-Valued Attributes](#single-valued-and-multi-valued-attributes)
   - [Derived Attributes](#derived-attributes)
   - [Key Attributes](#key-attributes)
   - [Comparative Table of Attribute Types](#comparative-table-of-attribute-types)
4. [Relationships](#relationships)
   - [Degree of Relationship](#degree-of-relationship)
   - [Representation with Diamonds](#representation-with-diamonds)
5. [Cardinality Constraints](#cardinality-constraints)
   - [One-to-One](#one-to-one)
   - [One-to-Many](#one-to-many)
   - [Many-to-Many](#many-to-many)
   - [Comparative Table of Cardinality](#comparative-table-of-cardinality)
6. [Participation Constraints (Total vs Partial)](#participation-constraints-total-vs-partial)
7. [Relationship Attributes](#relationship-attributes)
8. [Multiple Relationships Between the Same Entity Pair](#multiple-relationships-between-the-same-entity-pair)
9. [Specialization / Generalization (ISA)](#specialization--generalization-isa)
10. [Complete ERD Example](#complete-erd-example)
11. [Summary Table of Key Concepts](#summary-table-of-key-concepts)
12. [Key Takeaways](#key-takeaways)

---

## Introduction

The **Entity-Relationship Model (E-R Model)** is the dominant tool of **Conceptual Design** in the life cycle of a database. It was developed by Peter Chen in 1976 and serves as a bridge between business requirements and the final implementation in the relational model. The E-R diagram (ERD) graphically captures the entities of the modeled world, their characteristics and the relationships between them, without committing to technical implementation details. Understanding the E-R model is a necessary prerequisite for the transition to the Relational Model and for writing correct SQL schemas.

---

## Entities
*Entities*

An **Entity** is any object — real or abstract — for which we want to store data in the database. Each entity represents a category (type), while each specific record is an **instance** of it.

**Analogy**: The entity type `STUDENT` is like the **mold** (casting), while the specific student "Nikolaos Panagopoulos" is the **cast object** (instance). The diagram defines the mold — the database stores the objects.

In the ERD, entities are represented as **rectangles** and are divided into two categories depending on whether their existence depends on another entity.

---

### Strong Entities
*Strong (Regular) Entities*

A **Strong Entity** is an entity that has **independent existence** — it does not depend on any other entity to exist and has its own **Primary Key** that uniquely identifies it.

**Characteristics**:
- Represented as a **simple rectangle** in the ERD.
- Has one or more attributes that form a Primary Key.
- Can exist independently of any other entity in the database.

**Example**: The entity `STUDENT` with Primary Key `AM` (Registration Number) is strong — every student exists independently.

```text
  +------------------+
  |     STUDENT      |   <-- Simple rectangle = Strong Entity
  +------------------+
  |  AM (PK)         |
  |  Surname         |
  |  Name            |
  |  Date of Birth   |
  +------------------+
```

**Exam Note:** Every Strong Entity **must** have a Primary Key. Without a Primary Key, an entity cannot be strong.

---

### Weak Entities
*Weak Entities*

A **Weak Entity** is an entity that **cannot exist independently** — it is existentially dependent on a strong entity (the **owner entity** or Identifying Entity). It does not have enough attributes to form a Primary Key on its own.

**Characteristics**:
- Represented as a **double rectangle** in the ERD.
- Its identification is done through a **Partial Key** (partial key — underlined with a dashed line) combined with the Primary Key of the owner entity.
- The relationship with the owner entity is called an **Identifying Relationship** and is represented by a **double rhombus**.
- If the owner entity is deleted, the weak entity is also deleted (cascading delete).

**Analogy**: The `DEPENDENTS` (dependents) of an employee (e.g. children entitled to an insurance plan) form a weak entity — it makes no sense to store children's data without the corresponding employee.

```text
  +==================+           +==================+
  ||   EMPLOYEE     ||           ||   DEPENDENT     ||   <-- Double rectangle
  +==================+           +==================+
  |  AFM (PK)        |           |  Name (Partial Key)|
  |  Surname         |           |  Date of Birth   |
  +==================+           |  Relationship     |
              |                  +==================+
              |    <<=======>>
              |  Identifying Relationship
              |  (Double Rhombus)
```

**Key Distinction:** A weak entity needs the **Partial Key + the PK of the parent entity** to form its complete identifier (Composite Key in the table).

---

### Comparative Table: Strong vs. Weak Entities

| Characteristic | Strong Entity | Weak Entity |
|---|---|---|
| **Existence** | Independent | Dependent on Identifying Entity |
| **Primary Key** | Has its own PK | Has only a Partial Key |
| **ERD Representation** | Simple rectangle | Double rectangle |
| **Relationship** | Simple rhombus | Double rhombus (Identifying Relationship) |
| **Parent deletion** | Not affected | Cascading delete |
| **Example** | `STUDENT`, `DEPARTMENT` | `DEPENDENT`, `BOOK_COPY` |

---

## Attributes
*Attributes*

An **Attribute** is a property or characteristic that describes an entity or a relationship. Each attribute corresponds to a column in the final relational table. In the ERD, attributes are represented as **ovals** connected by a line to the corresponding entity.

---

### Simple and Composite Attributes
*Simple and Composite Attributes*

A **Simple (Atomic) Attribute** is an attribute that **cannot be divided** into smaller, more fundamental attributes.

- **Examples**: `AFM`, `Age`, `Salary`, `AM`.
- Stored as **a single atomic value** in the database.

A **Composite Attribute** is an attribute that **consists of many constituent attributes**, each of which has independent meaning.

- **Example**: The `FullName` (full name) consists of `Name` (first name) + `Surname` (last name). The Address (`Street`, `Number`, `City`, `ZIP`) is a classic example of a composite attribute.

```text
  Composite Attribute: Address
  
           ( Address )         <-- Composite
          /      |      \
     (Street)  (No.)  (City)   <-- Simple sub-attributes
```

**Exam Note:** When converting to the relational model, composite attributes are usually **decomposed** into their constituent parts (e.g. `first_name`, `last_name` instead of `full_name`), for better search capabilities and normalization.

---

### Single-Valued and Multi-Valued Attributes
*Single-Valued and Multi-Valued Attributes*

A **Single-Valued Attribute** takes **exactly one value** for each entity instance.

- **Example**: `AFM` — every employee has a single AFM.

A **Multi-Valued Attribute** can take **many values** for a single entity instance. It is represented as a **double ellipse** in the ERD.

- **Example**: The `Phones` (phones) of an employee — one employee can have mobile, home and work phones.
- **Example**: The `Specialties` (specialties) of a doctor — a doctor can be both a Cardiologist and an Internist.

```text
  Single-valued:      Multi-valued:
  
   ( AFM )             (( Phones ))   <-- Double ellipse
```

**Key Distinction:** Multi-valued attributes **cannot be stored directly** in a relational table without violating 1NF (First Normal Form). The solution is to create a **separate table** for the multi-valued attribute, linked with a Foreign Key.

```sql
-- Converting a multi-valued attribute into a separate table
CREATE TABLE employee_phones (
    emp_afm   VARCHAR(9)  NOT NULL,
    phone_num VARCHAR(15) NOT NULL,
    PRIMARY KEY (emp_afm, phone_num),
    FOREIGN KEY (emp_afm) REFERENCES employees(afm)
);
```

---

### Derived Attributes
*Derived Attributes*

A **Derived Attribute** is an attribute whose value is **computed from other attributes** or data already present in the database. It is represented as a **dashed ellipse** in the ERD.

- **Example 1**: `Age` (age) — computed from `Birth_Date` (birth date) and the current date.
- **Example 2**: `Employment_Duration` (length of employment) — computed from `Hire_Date` (hire date) and today.
- **Example 3**: `Total_Department_Salary` (total department salary) — computed as the sum of the department's salaries.

```text
  Stored:              Derived:
  
  ( Birth_Date )  -->  (- - Age - -)   <-- Dashed ellipse
```

**Exam Note:** Derived attributes are usually **not stored** in the database — they are computed at query time to avoid redundancy. They are stored only if their computation is computationally expensive (e.g. with materialized views).

```sql
-- Example: Computing the derived attribute Age during the query
SELECT first_name,
       last_name,
       birth_date,
       TIMESTAMPDIFF(YEAR, birth_date, CURDATE()) AS age  -- Derived
FROM employees;
```

---

### Key Attributes
*Key Attributes*

A **Key Attribute** is an attribute (or set of attributes) that uniquely identifies each instance of an entity. In the ERD it is represented with an **underlined** name inside the ellipse.

- Corresponds to the **Primary Key** of the relational model.
- For weak entities, the **Partial Key** is used (dashed underline).

```text
  Key Attribute of a Strong Entity:       Weak Entity Partial Key:

   ( __AFM__ )                            ( _ _ Name _ _ )
```

---

### Comparative Table of Attribute Types

| Attribute Type | Definition | ERD Representation | Example |
|---|---|---|---|
| **Simple** | Indivisible, atomic | Simple ellipse | `AFM`, `Salary` |
| **Composite** | Consists of constituent attributes | Ellipse with sub-ellipses | `Address` |
| **Single-Valued** | One value per entity | Simple ellipse | `ID_Card` |
| **Multi-Valued** | Many values per entity | Double ellipse | `Phones` |
| **Derived** | Computed from other attributes | Dashed ellipse | `Age` |
| **Key** | Uniquely identifies an entity | Ellipse with underline | `AM`, `AFM` |
| **Partial Key** | Partial identification of a weak entity | Dashed underline | `Name` in `DEPENDENT` |

---

## Relationships
*Relationships*

A **Relationship** represents a **connection or interaction** between two or more entities. In the ERD, it is represented as a **rhombus (diamond)**, connected with lines to the involved entities.

Each relationship is characterized by:
- **Degree**: How many entities participate.
- **Cardinality**: How many instances of one entity are connected to how many instances of another.
- **Participation**: Total or partial — whether every entity instance must necessarily participate in the relationship.

---

### Degree of Relationship
*Degree of Relationship*

The **Degree** of a relationship is defined by the **number of entity types** that participate in it.

#### Unary / Recursive Relationship (Degree 1)

Connects **one entity with its own type** (self-relationship). Used for hierarchical structures within the same entity.

- **Example**: An `EMPLOYEE` (employee) supervises other `EMPLOYEES` (employees) (manager → subordinates).

```text
                    +-----------+
              +---->| EMPLOYEE  |<---+
              |     +-----------+    |
              |           |          |
              |     < Supervises >   |
              |           |          |
              +-----------+----------+
                  (Recursive Relationship)
```

#### Binary Relationship (Degree 2)

The most common — connects **two different entity types**.

- **Example**: `STUDENT` — `Registers` — `COURSE`.

```text
  +-----------+              +-----------+
  | STUDENT   |---< Registers >---| COURSE    |
  +-----------+              +-----------+
```

#### Ternary Relationship (Degree 3)

Connects **three entity types** simultaneously. Used when the relationship depends on all three entities — it cannot be represented with pairs of binary relationships.

- **Example**: `DOCTOR` — `PATIENT` — `MEDICINE` through the relationship `Prescribes` — which doctor prescribes which drug to which patient.

```text
         +-----------+
         |  DOCTOR   |
         +-----------+
               \
                \
           < Prescribes >
                /        \
               /            \
  +-----------+            +-----------+
  |  PATIENT  |            |  MEDICINE |
  +-----------+            +-----------+
```

| Degree | Name | Example |
|---|---|---|
| 1 | Unary / Recursive | `EMPLOYEE` supervises `EMPLOYEE` |
| 2 | Binary | `STUDENT` registers in `COURSE` |
| 3 | Ternary | `DOCTOR` prescribes `MEDICINE` to `PATIENT` |

---

### Representation with Diamonds
*Representation with Diamonds*

In the ERD, relationships are represented as rhombuses connected with lines to the involved entities:

- **Simple rhombus**: Normal relationship between strong entities.
- **Double rhombus**: Identifying Relationship between a strong and a weak entity.

```text
  Normal Relationship (Simple Rhombus):

  +------------+          +-----------+
  | DEPARTMENT |---< Employs >---| EMPLOYEE  |
  +------------+          +-----------+

  Identifying Relationship (Double Rhombus):

  +============+          +============+
  ||  EMPLOYEE  ||=<<= Has =>>==||  DEPENDENT ||
  +============+          +============+
```

**Exam Note:** The **double rhombus** is used **exclusively** for the Identifying Relationship that links a strong entity with a weak one. Every other relationship uses a simple rhombus.

---

## Cardinality Constraints
*Cardinality Constraints*

**Cardinality Constraints** define the **maximum number of instances** of one entity that can be connected to a single instance of another entity through a relationship. They constitute one of the most critical constraints in ER diagram design.

In the ERD they are written as labels `1`, `N` or `M` on the lines connecting entities with relationships.

---

### One-to-One
*One-to-One*

In a **1:1** relationship, each instance of entity A is connected to **at most one** instance of entity B, and vice versa.

**Analogy**: Every country has one prime minister and every prime minister governs one country.

**Database Example**: `EMPLOYEE` manages `DEPARTMENT` (every department has one manager, every manager manages one department).

```text
  +-----------+    1          1    +-----------+
  | EMPLOYEE  |---<Administers>---| DEPARTMENT|
  +-----------+                   +-----------+
```

**Implementation in the Relational Model**: The Foreign Key can be placed in either of the two tables. It is usually placed in the table with total participation.

```sql
-- 1:1 Implementation: dept_manager_afm in the DEPARTMENT table
CREATE TABLE departments (
    dept_id          INT         PRIMARY KEY,
    dept_name        VARCHAR(50) NOT NULL,
    dept_manager_afm VARCHAR(9)  UNIQUE,  -- UNIQUE ensures 1:1
    FOREIGN KEY (dept_manager_afm) REFERENCES employees(afm)
);
```

---

### One-to-Many
*One-to-Many*

In a **1:N** relationship, each instance of entity A is connected to **many** instances of entity B, but each instance of B is connected to **one and only one** instance of A.

**Analogy**: One professor teaches many courses, but each course (in a specific school) has one responsible professor.

**Database Example**: One `DEPARTMENT` employs many `EMPLOYEES`, but every `EMPLOYEE` belongs to one `DEPARTMENT`.

```text
  +-----------+    1          N    +-----------+
  | DEPARTMENT|---< Employs >---| EMPLOYEE  |
  +-----------+                   +-----------+
```

**Implementation in the Relational Model**: The Foreign Key is placed on the **"N" side** (in the table that has many records). This is the most common type of relationship.

```sql
-- 1:N Implementation: dept_id (FK) in the EMPLOYEE table
CREATE TABLE employees (
    afm       VARCHAR(9)  PRIMARY KEY,
    last_name VARCHAR(50) NOT NULL,
    dept_id   INT         NOT NULL,  -- Foreign Key on the N side
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);
```

**State table:**

| dept_id | dept_name | | afm       | last_name | dept_id |
|---------|-----------|---|-----------|-----------|---------|
| 10      | Accounting | | 111111111 | Papas     | 10      |
| 20      | Computer Science | | 222222222 | Nikos    | 10      |
| | | | 333333333 | Alexis    | 20      |

---

### Many-to-Many
*Many-to-Many*

In an **N:M** relationship, each instance of entity A is connected to **many** instances of entity B, and each instance of B is also connected to **many** instances of A.

**Analogy**: One student attends many courses, and each course is attended by many students.

**Database Example**: `STUDENT` — `Registers` — `COURSE`.

```text
  +-----------+    N          M    +-----------+
  | STUDENT   |---< Registers >---| COURSE    |
  +-----------+                   +-----------+
```

**Implementation in the Relational Model**: N:M relationships **cannot be implemented directly** in the relational model. It is necessary to create an **intermediate table (junction table / associative table)** that contains the Foreign Keys from both tables as a Composite Primary Key.

```text
  +-----------+       +--------------------+       +-----------+
  | STUDENT   |       |   REGISTRATION     |       |  COURSE   |
  +-----------+       +--------------------+       +-----------+
  | am (PK)   |<------| am (FK, PK)        |       | course_id |
  | eponymo   |       | course_id (FK, PK) |------>| (PK)      |
  | onoma     |       | enroll_date        |       | titlos    |
  +-----------+       | grade              |       +-----------+
                      +--------------------+
```

```sql
-- N:M Implementation: Intermediate REGISTRATION table
CREATE TABLE enrollments (
    student_am INT  NOT NULL,
    course_id  INT  NOT NULL,
    enroll_date DATE,
    grade       DECIMAL(4, 2),
    PRIMARY KEY (student_am, course_id),   -- Composite PK
    FOREIGN KEY (student_am) REFERENCES students(am),
    FOREIGN KEY (course_id)  REFERENCES courses(course_id)
);
```

**Exam Note:** Every N:M relationship **requires an intermediate table** in the conversion to the relational model. The intermediate table can also have **its own attributes** (e.g. `grade`, `enroll_date` in `REGISTRATION`), which belong to neither of the two entities but to the **relationship** itself.

---

### Comparative Table of Cardinality

| Cardinality | Description | Implementation in the Relational Model | Example |
|---|---|---|---|
| **1:1** | One A ↔ one B | FK in one of the two tables (with UNIQUE) | Employee ↔ Office |
| **1:N** | One A ↔ many B | FK in the table of the "N" side | Department → Employees |
| **N:M** | Many A ↔ many B | Intermediate table with Composite PK | Students ↔ Courses |

---

## Participation Constraints (Total vs Partial)
*Participation Constraints*

**Participation constraints** define the **minimum number** of relationship instances in which an entity instance **must** participate. They complement the **cardinality ratio**, which defines the maximum.

| Type | Meaning | ERD Notation | FK column in mapping |
|---|---|---|---|
| **Total (mandatory)** | **Every** instance of the entity **must** participate in the relationship | **Double line** connecting entity to relationship | `NOT NULL` |
| **Partial (optional)** | **Some** instances participate, others do not | **Single line** | `NULL` allowed |

**Analogy**: In a school, "every student is enrolled in a department" is total participation — there is no student without a department. "A student is the president of a club" is partial — only some students hold this role.

**Example**: In `DEPARTMENT` — `Employs` — `EMPLOYEE`:
- An `EMPLOYEE` **must** belong to exactly one `DEPARTMENT` → **total participation** (double line on the `EMPLOYEE` side).
- A `DEPARTMENT` **may or may not** have employees → **partial participation** (single line on the `DEPARTMENT` side).

```text
   +-----------+                   +-----------+
   | DEPARTMENT|---< Employs >=====| EMPLOYEE  |
   +-----------+                   +-----------+
        |                              ||
     single line                    double line
   (partial — may have            (total — every employee
    zero employees)                must have a department)
```

**Effect on mapping**: The foreign key `dept_id` in the `EMPLOYEE` table must be `NOT NULL` because of total participation; it would be allowed to be `NULL` only under partial participation.

**Key Distinction:** Cardinality answers "how **many** instances **can** participate" (maximum), while participation answers "**whether** every instance **must** participate" (minimum). Total participation combined with `1:N` produces a `NOT NULL` foreign key; total participation in `1:1` determines **where** the foreign key is placed.

---

## Relationship Attributes
*Relationship Attributes*

A **relationship attribute** is a property that belongs **to the relationship itself**, not to any single participating entity. It describes something about the **connection** between the entities.

- Occur **mainly in N:M** and sometimes in **1:N** relationships.
- In the ERD they are attached to the **rhombus**, not to an entity.
- In the relational mapping they land in the **junction table** (for N:M) or in the "many" side table (for 1:N).

**Examples**:
- `STUDENT` — `Registers` — `COURSE` (N:M): `grade` and `enroll_date` describe the registration, not the student or the course alone.
- `EMPLOYEE` — `Works_on` — `PROJECT` (N:M): `hours_per_week` describes how many hours that employee devotes to that project.
- `ACTOR` — `Plays_in` — `MOVIE` (N:M): `role_name` describes the role in that specific movie.

```text
   +-----------+              +-----------+
   |  STUDENT  |---< Registers >---|  COURSE   |
   +-----------+      |            +-----------+
                   ( grade )      <-- Relationship attributes
                   ( enroll_date )
```

```sql
-- Relationship attributes land in the junction table
CREATE TABLE enrollments (
    student_am INT          NOT NULL,
    course_id  INT          NOT NULL,
    grade      DECIMAL(4,2),
    enroll_date DATE,
    PRIMARY KEY (student_am, course_id),
    FOREIGN KEY (student_am) REFERENCES students(am),
    FOREIGN KEY (course_id)  REFERENCES courses(course_id)
);
```

**Exam Note:** When an attribute cannot logically belong to either entity alone (e.g. `grade` is not a property of the student nor of the course, but of the pair), it is a relationship attribute and must be placed in the junction table during mapping.

---

## Multiple Relationships Between the Same Entity Pair
*Multiple Relationships Between the Same Entity Pair*

The **same pair of entity types** can be connected by **two or more distinct relationships**, each carrying its own meaning and usually its own **role label**.

- Each relationship is modeled as a **separate rhombus** with a distinct name.
- In the ERD, **role labels** on the connecting lines clarify the different roles each entity plays.
- In the relational mapping, each relationship produces its **own foreign key(s)** — the two relationships map to **two separate FK columns** (or two junction tables for N:M).

**Example 1 — Airports**: The entity `FLIGHT` is connected to `AIRPORT` twice: once for the **departure** airport and once for the **arrival** airport.

```text
                    < Departure >  (role: departure_airport)
                  /               \
   +-----------+                   +-----------+
   |  FLIGHT   |                   |  AIRPORT  |
   +-----------+                   +-----------+
                  \               /
                    < Arrival >  (role: arrival_airport)
```

```sql
-- Mapping to two separate foreign keys
CREATE TABLE flights (
    flight_id             INT PRIMARY KEY,
    departure_airport_code VARCHAR(3) NOT NULL,
    arrival_airport_code   VARCHAR(3) NOT NULL,
    FOREIGN KEY (departure_airport_code) REFERENCES airports(code),
    FOREIGN KEY (arrival_airport_code)   REFERENCES airports(code)
);
```

**Example 2 — Sports**: `TEAM` participates in `MATCH` twice, as the **home** team and as the **away** team; the two roles map to `home_team_id` and `away_team_id`.

**Key Distinction:** Two roles of the same entity in one relationship is **not** the same as a recursive (unary) relationship. Here the entity pair is the same type pair, but each role is a distinct, named relationship that produces a distinct foreign key.

---

## Specialization / Generalization (ISA)
*Specialization / Generalization (ISA)*

**Specialization** (top-down) and **Generalization** (bottom-up) model **subtype relationships** between entity sets, known as **ISA hierarchies**. A **supertype** (parent) is split into **subtypes** (children) that inherit its attributes and add their own.

- **Specialization**: start from a general entity (e.g. `EMPLOYEE`) and define specialized subtypes (`SECRETARY`, `TECHNICIAN`, `MANAGER`).
- **Generalization**: start from specific entities (`CAR`, `MOTORCYCLE`) and abstract them into a general supertype (`VEHICLE`).
- In the ERD, the relationship is drawn with a **triangle** labeled **ISA**.
- The supertype's primary key becomes the primary key of each subtype (the subtype **does not** get a new, unrelated identifier).

**Example**: A `MEDIA_TITLE` supertype splits into the subtypes `MOVIE` and `SERIES`; both inherit `title_id`, `title`, `release_year`, while `MOVIE` adds `duration` and `SERIES` adds `season_count`.

```text
                      +-------------+
                      | MEDIA_TITLE |  <-- Supertype
                      +-------------+
                           /   \
                     ISA  /     \  ISA
                         v       v
                  +---------+ +---------+
                  |  MOVIE  | | SERIES  |  <-- Subtypes
                  +---------+ +---------+
```

**Constraints** (each is independent):

| Constraint | Question it answers | Options |
|---|---|---|
| **Total vs Partial** | Must **every** supertype instance belong to a subtype? | Total (double line) — every member has a subtype; Partial (single line) — some members remain generic |
| **Disjoint vs Overlapping** | Can an instance belong to **more than one** subtype? | Disjoint (d) — exactly one; Overlapping (o) — may belong to several |

**Mapping to the relational model** — three main options:
1. **One table per class** (supertype table plus one table per subtype, linked by the shared PK). Best for total, disjoint hierarchies.
2. **One table per subtype** (no supertype table; subtype tables duplicate inherited attributes). Suitable when the supertype has no standalone instances.
3. **Single table with a type discriminator** (one wide table with all attributes plus a `type` column). Simple but may produce many `NULL`s.

**Key Distinction:** Specialization/Generalization describes an **"is-a"** relationship (subtype *is a* supertype), in contrast to ordinary relationships which describe an **"has-a"/association** between distinct entities.

---

## Complete ERD Example
*Complete ERD Example*

The following diagram combines all the concepts analyzed — strong and weak entities, various attribute types, and all types of cardinality:

```text
                         ( __AFM__ )  ( Surname )  ( Name )
                              \           |           /
  ( Phones )                  \          |          /
       ||                  +============+
  (( Phones ))-----------|  EMPLOYEE  |
                            +============+
                                 |   \
                         1       |    \      N
                        (Belongs to)  (Manages)
                              |          \
                              v    1      v
                         +-----------+  +-----------+
                         | DEPARTMENT|  | DEPARTMENT|  (same entity)
                         +-----------+  +-----------+
                              |
                    (( Has )) <-- Identifying Relationship (Double Rhombus)
                              |
                         +============+
                         ||  DEPENDENT ||  <-- Weak Entity
                         +============+
                         | _ Name _   |  <-- Partial Key
                         | Relation   |
                         +============+


  STUDENT --- (N) --- < Registers > --- (M) --- COURSE
     |                       |
  ( __AM__ )          ( Registration Date )  <-- Relationship Attribute
  ( Surname )         ( Grade )
  (- Age -)  <-- Derived
```

---

## Summary Table of Key Concepts
*Summary Table of Key Concepts*

| Concept | Definition | Key Characteristic / Rule |
|---|---|---|
| **Entity** | Object for which data is stored | Represented as a rectangle in the ERD |
| **Strong Entity** | Independent existence, has its own PK | Simple rectangle |
| **Weak Entity** | Dependent existence, has only a Partial Key | Double rectangle, Identifying Relationship |
| **Attribute** | Property of an entity or relationship | Represented as an ellipse |
| **Simple Attribute** | Indivisible attribute | Atomic value |
| **Composite Attribute** | Consists of constituent attributes | Decomposed in the relational model |
| **Single-Valued Attribute** | One value per entity | Normal ellipse |
| **Multi-Valued Attribute** | Many values per entity | Double ellipse — requires a separate table |
| **Derived Attribute** | Computed from other attributes | Dashed ellipse — usually not stored |
| **Key Attribute** | Unique identification of an entity | Underlined in the ERD |
| **Partial Key** | Partial identification of a weak entity | Dashed underline |
| **Relationship** | Connection between entities | Represented as a rhombus |
| **Degree** | Number of entities in the relationship | Unary (1), Binary (2), Ternary (3) |
| **Cardinality 1:1** | One instance ↔ one instance | FK with UNIQUE constraint |
| **Cardinality 1:N** | One instance ↔ many instances | FK on the N side |
| **Cardinality N:M** | Many ↔ many | Intermediate table with Composite PK |
| **Identifying Relationship** | Identification relationship between weak and strong | Double rhombus |
| **Participation (Total)** | Every entity instance must participate | Double line — FK becomes `NOT NULL` |
| **Participation (Partial)** | Some instances participate | Single line — FK may be `NULL` |
| **Relationship Attribute** | Property of the relationship itself | Lands in the junction table (N:M) |
| **Multiple Relationships** | Same entity pair linked by two distinct relationships | Two separate foreign keys / junction tables |
| **Specialization/Generalization (ISA)** | Supertype/subtype hierarchy | Triangle labeled ISA — "is-a" relationship |

---

## Key Takeaways
*Key Takeaways*

- The **E-R Model** is the tool of conceptual design — it captures the logical structure of reality without technical implementation details.
- **Strong Entities** have independent existence and their own Primary Key (simple rectangle). **Weak Entities** depend existentially on another entity and are represented with a double rectangle.
- **Multi-Valued Attributes** (double ellipse) violate 1NF — they require a separate table in the relational model.
- **Derived Attributes** (dashed ellipse) are usually not stored — they are computed at query time.
- **Key Distinction:** The degree refers to the number of entities in the relationship, while the cardinality refers to the number of instances connected.
- **1:N** cardinality is the most common in database design — implemented with a Foreign Key in the table of the "many" side.
- Every **N:M relationship** is converted into an intermediate table (junction table) during the conversion to the relational model — the intermediate table can have its own attributes.
- The **Identifying Relationship** (double rhombus) is used exclusively to link a weak entity with a strong one — deleting the strong entity causes a cascading delete.
- **Exam Note:** In the ERD, the cardinality is always written next to the entities — "1" near the entity that participates with one instance, "N" or "M" near the entity that participates with many.
- Correct identification of entity types, attributes and cardinality in the E-R diagram **directly determines** the correctness of the relational schema and of the final SQL implementation.
- **Participation** answers "must every instance participate?" — **total** (double line) makes the mapped foreign key `NOT NULL`, **partial** (single line) allows `NULL`.
- **Relationship attributes** (e.g. `grade`, `hours_per_week`, `role_name`) belong to the relationship, not to a single entity, and land in the junction table when the relationship is N:M.
- The **same entity pair** can be connected by two distinct, role-labeled relationships (e.g. departure/arrival airports, home/away teams); each maps to its own foreign key.
- **Specialization/Generalization (ISA)** models subtype hierarchies with a triangle, and supports independent constraints: **total/partial** and **disjoint/overlapping**.

---
# topic_4_relational_model_and_relational_algebra.md
---

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

---
# topic_5_sql_data_definition_language_ddl.md
---

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

---
# topic_6_sql_data_manipulation_and_query_language_dml_dql.md
---

# SQL Language: Data Manipulation & Queries (DML & DQL)
*SQL Language: Data Manipulation & Data Query Language*

---

## Table of Contents
*Table of Contents*

1. [Introduction](#introduction)
2. [Data Manipulation (DML — Data Manipulation Language)](#data-manipulation-dml--data-manipulation-language)
   - [INSERT INTO](#insert-into)
   - [UPDATE ... SET ... WHERE](#update--set--where)
   - [DELETE FROM ... WHERE](#delete-from--where)
   - [Comparative Table: DML Commands](#comparative-table-dml-commands)
3. [Queries & Retrieval (DQL — Data Query Language)](#queries--retrieval-dql--data-query-language)
   - [Basic SELECT Structure](#basic-select-structure)
   - [Column Projection or Full Row Selection (*)](#column-projection-or-full-row-selection-)
   - [Filtering: Comparison Operators and Logical Operators](#filtering-comparison-operators-and-logical-operators)
4. [Comparative Table: DDL vs DML vs DQL](#comparative-table-ddl-vs-dml-vs-dql)
5. [Summary Table of Key Concepts](#summary-table-of-key-concepts)
6. [Key Takeaways](#key-takeaways)

---

## Introduction

Once **DDL** (Data Definition Language) defines the schema — the structure of the tables, the columns, and the keys — the next critical step is the **populating and manipulation of the data** these will contain. This role belongs to two complementary subsets of SQL: **DML (Data Manipulation Language)** and **DQL (Data Query Language)**. DML concerns **writing** — inserting, updating, and deleting records — while DQL concerns **reading** — retrieving information from the database through queries. Understanding both is essential: a database without data has no value, and data without the ability to search and filter is not useful.

---

## Data Manipulation (DML — Data Manipulation Language)
*Data Manipulation Language*

**DML** includes the SQL statements that **modify the data** inside an already existing table. In contrast to DDL, which changes the **structure** (schema), DML changes the **contents** (records). DML statements **do not** perform an implicit `COMMIT` by default — they can be used within **transactions** and undone with `ROLLBACK`, as long as an explicit `COMMIT` has not been issued.

**Analogy**: If the table is a blank sheet of paper (structure from DDL), DML is the **pen that writes, corrects, or erases** the data on it.

```text
  SQL Subsets:

  +---------------------------------------+
  |                  SQL                  |
  +----------+----------+-----------------+
  |   DDL    |   DML    |      DQL        |
  +----------+----------+-----------------+
  | CREATE   | INSERT   | SELECT          |
  | DROP     | UPDATE   |                 |
  | ALTER    | DELETE   |                 |
  +----------+----------+-----------------+
  | Structure| Data     | Retrieval       |
  +----------+----------+-----------------+
```

---

### INSERT INTO
*Inserting New Records/Tuples into a Table*

The `INSERT INTO` statement adds **one or more new records (rows/tuples)** to an existing table. Every new record must respect the constraints defined when the table was created — `NOT NULL`, `UNIQUE`, `FOREIGN KEY`, etc.

**Basic syntax — Explicit column definition (Recommended way):**

```sql
INSERT INTO table_name (column1, column2, ...)
VALUES (value1, value2, ...);
```

**Basic syntax — Without column definition (Full value order):**

```sql
INSERT INTO table_name
VALUES (value1, value2, ...);
```

**Example — Inserting a record into table `Foititis`:**

**Before:**

```text
  mysql> SELECT * FROM Foititis;
  Empty set (0.00 sec)
```

**Execution:**

```sql
-- Inserting a student with explicit column definition (safe method)
INSERT INTO Foititis (am, onoma, eponymo, email, hmerominia, dept_id)
VALUES (10001, 'Alexis', 'Nikolopoulos', 'alex@uni.gr', '2001-05-10', 1);
```

**After:**

```text
  mysql> SELECT * FROM Foititis;
  +-------+--------+--------------+-----------+------------+---------+
  | am    | onoma  | eponymo      | email     | hmerominia | dept_id |
  +-------+--------+--------------+-----------+------------+---------+
  | 10001 | Alexis | Nikolopoulos | alex@uni.gr| 2001-05-10 |       1 |
  +-------+--------+--------------+-----------+------------+---------+
  1 row in set (0.00 sec)
```

**Inserting multiple records in one statement:**

**Execution:**

```sql
-- Inserting multiple tuples simultaneously (more efficient than many individual INSERTs)
INSERT INTO Foititis (am, onoma, eponymo, email, hmerominia, dept_id)
VALUES
    (10002, 'Eleni',   'Papadopoulou', 'eleni@uni.gr',  '2002-09-15', 2),
    (10003, 'Nikos',   'Kostopoulos',  'nikos@uni.gr',  '2000-03-22', 1),
    (10004, 'Maria',   'Stavridou',    'maria@uni.gr',  '2003-01-30', 3);
```

**After:**

```text
  mysql> SELECT * FROM Foititis;
  +-------+--------+--------------+--------------+------------+---------+
  | am    | onoma  | eponymo      | email        | hmerominia | dept_id |
  +-------+--------+--------------+--------------+------------+---------+
  | 10001 | Alexis | Nikolopoulos | alex@uni.gr  | 2001-05-10 |       1 |
  | 10002 | Eleni  | Papadopoulou | eleni@uni.gr | 2002-09-15 |       2 |
  | 10003 | Nikos  | Kostopoulos  | nikos@uni.gr | 2000-03-22 |       1 |
  | 10004 | Maria  | Stavridou    | maria@uni.gr | 2003-01-30 |       3 |
  +-------+--------+--------------+--------------+------------+---------+
  4 rows in set (0.00 sec)
```

**Insertion omitting optional columns:**

```sql
-- The hmerominia column is not provided - it receives NULL automatically
INSERT INTO Foititis (am, onoma, eponymo, dept_id)
VALUES (10005, 'Giorgos', 'Antoniou', 1);
```

**Exam Note:** The syntax **without** a column definition (`INSERT INTO table VALUES (...)`) requires values for **every column** of the table, **in the exact order** in which they were defined at creation. Omitting even one value causes an error. The syntax **with** a column definition is always safer and more readable.

**Key Distinction:** `INSERT INTO` violates constraints in real time:

```sql
-- PRIMARY KEY violation (am=10001 already exists)
INSERT INTO Foititis (am, onoma, eponymo, dept_id)
VALUES (10001, 'Other', 'Student', 2);
-- ERROR 1062 (23000): Duplicate entry '10001' for key 'PRIMARY'

-- FOREIGN KEY violation (dept_id=99 does not exist in table Tmima)
INSERT INTO Foititis (am, onoma, eponymo, dept_id)
VALUES (10006, 'Test', 'Student', 99);
-- ERROR 1452: Cannot add or update a child row: a foreign key constraint fails
```

---

### UPDATE ... SET ... WHERE
*Updating/Modifying Existing Data*

The `UPDATE` statement **modifies values in existing records** of a table. The `SET` clause defines which column changes and to which value, while the `WHERE` clause determines **which rows** will be affected. Without `WHERE`, the statement affects **all** the rows of the table.

**Basic syntax:**

```sql
UPDATE table_name
SET    column1 = value1,
       column2 = value2,
       ...
WHERE  condition;
```

**Example — Updating the email of a specific student:**

**Before:**

```text
  mysql> SELECT am, onoma, email FROM Foititis WHERE am = 10001;
  +-------+--------+-------------+
  | am    | onoma  | email       |
  +-------+--------+-------------+
  | 10001 | Alexis | alex@uni.gr |
  +-------+--------+-------------+
```

**Execution:**

```sql
-- Updating the email of only the student with am=10001
UPDATE Foititis
SET    email = 'alexniko@newmail.gr'
WHERE  am = 10001;
```

**After:**

```text
  mysql> SELECT am, onoma, email FROM Foititis WHERE am = 10001;
  +-------+--------+--------------------+
  | am    | onoma  | email              |
  +-------+--------+--------------------+
  | 10001 | Alexis | alexniko@newmail.gr|
  +-------+--------+--------------------+
```

**Updating multiple columns simultaneously:**

**Before:**

```text
  mysql> SELECT am, eponymo, dept_id FROM Foititis WHERE am = 10003;
  +-------+--------------+---------+
  | am    | eponymo      | dept_id |
  +-------+--------------+---------+
  | 10003 | Kostopoulos  |       1 |
  +-------+--------------+---------+
```

**Execution:**

```sql
-- Simultaneous change of surname and department
UPDATE Foititis
SET    eponymo = 'Kostopoulos-New',
       dept_id = 2
WHERE  am = 10003;
```

**After:**

```text
  mysql> SELECT am, eponymo, dept_id FROM Foititis WHERE am = 10003;
  +-------+------------------+---------+
  | am    | eponymo          | dept_id |
  +-------+------------------+---------+
  | 10003 | Kostopoulos-New |       2 |
  +-------+------------------+---------+
```

**Updating multiple rows with a common condition:**

**Before:**

```text
  mysql> SELECT am, dept_id FROM Foititis;
  +-------+---------+
  | am    | dept_id |
  +-------+---------+
  | 10001 |       1 |
  | 10002 |       2 |
  | 10003 |       2 |  (after the previous update)
  | 10004 |       3 |
  +-------+---------+
```

**Execution:**

```sql
-- Moving ALL students of department 2 to department 4
UPDATE Foititis
SET    dept_id = 4
WHERE  dept_id = 2;
```

**After:**

```text
  mysql> SELECT am, dept_id FROM Foititis;
  +-------+---------+
  | am    | dept_id |
  +-------+---------+
  | 10001 |       1 |
  | 10002 |       4 |  <-- Changed
  | 10003 |       4 |  <-- Changed
  | 10004 |       3 |
  +-------+---------+
```

**Dangerous example — UPDATE without WHERE:**

```sql
-- WARNING: Without WHERE, ALL rows of the table are affected
UPDATE Foititis
SET    dept_id = 1;
-- Result: ALL students are moved to department 1
```

**Exam Note:** Omitting `WHERE` in an `UPDATE` statement is one of the most **common and destructive mistakes** — it affects every row of the table. Before any `UPDATE`, it is recommended to run a corresponding `SELECT` with the same `WHERE` condition to verify that the correct rows are selected.

---

### DELETE FROM ... WHERE
*Deleting Specific Records Based on a Condition*

The `DELETE FROM` statement **deletes records (rows/tuples)** from a table. The `WHERE` clause determines which rows will be deleted. Without `WHERE`, **all** records are deleted (the table's schema remains). Unlike `DROP TABLE`, the table **continues to exist** after `DELETE`.

**Basic syntax:**

```sql
DELETE FROM table_name
WHERE  condition;
```

**Example — Deleting a specific student:**

**Before:**

```text
  mysql> SELECT am, onoma, eponymo FROM Foititis;
  +-------+--------+-----------------+
  | am    | onoma  | eponymo         |
  +-------+--------+-----------------+
  | 10001 | Alexis | Nikolopoulos    |
  | 10002 | Eleni  | Papadopoulou    |
  | 10003 | Nikos  | Kostopoulos-New|
  | 10004 | Maria  | Stavridou       |
  +-------+--------+-----------------+
```

**Execution:**

```sql
-- Deleting only the student with am=10003
DELETE FROM Foititis
WHERE  am = 10003;
```

**After:**

```text
  mysql> SELECT am, onoma, eponymo FROM Foititis;
  +-------+--------+--------------+
  | am    | onoma  | eponymo      |
  +-------+--------+--------------+
  | 10001 | Alexis | Nikolopoulos |
  | 10002 | Eleni  | Papadopoulou |
  | 10004 | Maria  | Stavridou    |
  +-------+--------+--------------+
  3 rows in set (0.00 sec)
```

**Deletion with a compound condition:**

**Execution:**

```sql
-- Deleting students who belong to department 4
DELETE FROM Foititis
WHERE  dept_id = 4;
```

**Deleting all records (without WHERE):**

```sql
-- Deletes ALL records - the table remains empty (structure intact)
DELETE FROM Foititis;
```

**The code above has the same result as:**

```sql
-- TRUNCATE: Faster for clearing an entire table
-- (cannot be recovered with ROLLBACK - behaves like DDL)
TRUNCATE TABLE Foititis;
```

**Referential Integrity Violation during DELETE:**

```sql
-- Attempting to delete a department that has students
DELETE FROM Tmima
WHERE  dept_id = 1;
-- ERROR 1451: Cannot delete or update a parent row:
-- a foreign key constraint fails (Foititis.dept_id REFERENCES Tmima.dept_id)
```

**Comparative Table: `DELETE FROM` vs `DROP TABLE` vs `TRUNCATE`:**

| Characteristic | `DELETE FROM` | `DROP TABLE` | `TRUNCATE TABLE` |
|---|---|---|---|
| **SQL category** | DML | DDL | DDL (behavior) |
| **Table structure** | Remains | Deleted | Remains |
| **Data** | Selective / Full deletion | Full deletion | Full deletion |
| **WHERE possible?** | Yes | No | No |
| **ROLLBACK possible?** | Yes (within a transaction) | No | No |
| **Speed** | Slow (row by row) | Fast | Very fast |
| **AUTO_INCREMENT reset** | No | — | Yes |

**Key Distinction:** `DELETE FROM table` (without `WHERE`) and `TRUNCATE TABLE table` both empty the table of data. However, `DELETE` is DML and supports `ROLLBACK`, while `TRUNCATE` behaves like DDL (implicit `COMMIT`) and is faster because it does not log each deletion separately.

---

### Comparative Table: DML Commands
*Comparative Table: DML Commands*

| Command | Action | Requires WHERE? | Affects Rows | Affects Structure |
|---|---|---|---|---|
| `INSERT INTO` | Adds new records | No | New rows | No |
| `UPDATE ... SET` | Modifies existing values | Recommended (without → full update) | Existing rows | No |
| `DELETE FROM` | Deletes existing records | Recommended (without → full deletion) | Existing rows | No |

---

## Queries & Retrieval (DQL — Data Query Language)
*Data Query Language*

**DQL** (or more commonly referred to as part of DML) essentially includes the `SELECT` statement — the **most frequently used statement** of the entire SQL language. `SELECT` **does not modify** the data — it retrieves and presents information from one or more tables based on criteria. The relationship between `SELECT` and Relational Algebra is direct: `WHERE` corresponds to **Selection** ($\sigma$) and the column list to **Projection** ($\pi$).

**Analogy**: `SELECT` is like a **question** one asks a librarian — it defines what one wants to see (columns), from where (tables), and under what conditions (filters). The librarian returns results without changing anything in the books.

---

### Basic SELECT Structure
*Basic SELECT Structure*

The basic structure of a `SELECT` query consists of three fundamental clauses that answer three questions:

| Clause | Question it answers | Relational Algebra Correspondence |
|---|---|---|
| `SELECT` | **What** do I retrieve? (which columns) | Projection $\pi$ |
| `FROM` | **From where** do I retrieve? (which table) | Relation $R$ |
| `WHERE` | **Under what conditions**? (which rows) | Selection $\sigma$ |

**Basic syntax:**

```sql
SELECT column1, column2, ...
FROM   table_name
WHERE  condition;
```

**General query form — Correspondence with Relational Algebra:**

$$\pi_{\text{column1, column2}}(\sigma_{\text{condition}}(\text{table\_name}))$$

```sql
-- SQL equivalent
SELECT column1, column2
FROM   table_name
WHERE  condition;
```

**Example — Retrieving the first and last name of ALL students:**

**Table state:**

```text
  Foititis:
  +-------+--------+--------------+--------------+------------+---------+
  | am    | onoma  | eponymo      | email        | hmerominia | dept_id |
  +-------+--------+--------------+--------------+------------+---------+
  | 10001 | Alexis | Nikolopoulos | alex@uni.gr  | 2001-05-10 |       1 |
  | 10002 | Eleni  | Papadopoulou | eleni@uni.gr | 2002-09-15 |       4 |
  | 10004 | Maria  | Stavridou    | maria@uni.gr | 2003-01-30 |       3 |
  +-------+--------+--------------+--------------+------------+---------+
```

**Execution:**

```sql
-- Selecting specific columns from ALL rows
SELECT onoma, eponymo
FROM   Foititis;
```

**Result:**

```text
  +--------+--------------+
  | onoma  | eponymo      |
  +--------+--------------+
  | Alexis | Nikolopoulos |
  | Eleni  | Papadopoulou |
  | Maria  | Stavridou    |
  +--------+--------------+
  3 rows in set (0.00 sec)
```

**Using an alias (AS) to rename columns in the result:**

```sql
-- The alias changes only the column name in the result - it does not change the database
SELECT onoma    AS "Student Name",
       eponymo  AS "Surname",
       dept_id  AS "Department"
FROM   Foititis;
```

**Result:**

```text
  +----------------+--------------+-------+
  | Student Name   | Surname       | Dept. |
  +----------------+--------------+-------+
  | Alexis         | Nikolopoulos |     1 |
  | Eleni          | Papadopoulou |     4 |
  | Maria          | Stavridou    |     3 |
  +----------------+--------------+-------+
```

---

### Column Projection or Full Row Selection (*)
*Column Projection or Full Row Selection*

`SELECT` offers two basic options for the columns that are returned: **explicit selection of specific columns** or the use of the **wildcard `*`**, which returns all columns.

**`SELECT *` syntax — Selecting all columns:**

```sql
SELECT *
FROM   table_name;
```

**Example — Full projection of table `Foititis`:**

**Execution:**

```sql
SELECT *
FROM   Foititis;
```

**Result:**

```text
  +-------+--------+--------------+--------------+------------+---------+
  | am    | onoma  | eponymo      | email        | hmerominia | dept_id |
  +-------+--------+--------------+--------------+------------+---------+
  | 10001 | Alexis | Nikolopoulos | alex@uni.gr  | 2001-05-10 |       1 |
  | 10002 | Eleni  | Papadopoulou | eleni@uni.gr | 2002-09-15 |       4 |
  | 10004 | Maria  | Stavridou    | maria@uni.gr | 2003-01-30 |       3 |
  +-------+--------+--------------+--------------+------------+---------+
```

**Comparison of `SELECT *` vs Specific Columns:**

| Criterion | `SELECT *` | `SELECT col1, col2` |
|---|---|---|
| **Code readability** | Low (it is not clear what is expected) | High (clear intent) |
| **Performance** | Lower (unnecessary columns are transferred) | Higher (only the necessary data) |
| **Resilience to schema changes** | Vulnerable (new columns appear automatically) | Resilient (stable result) |
| **Use** | Quick exploration / debugging | Production code |

**Using `DISTINCT` — Avoiding duplicates:**

**Execution:**

```sql
-- Displays only the unique departments that have students
SELECT DISTINCT dept_id
FROM   Foititis;
```

**Result:**

```text
  +---------+
  | dept_id |
  +---------+
  |       1 |
  |       4 |
  |       3 |
  +---------+
  3 rows in set (0.00 sec)
```

**Exam Note:** `SELECT *` is useful for quick data exploration and debugging, but it is **avoided in production code** — it returns unnecessary data, affects performance, and can produce unexpected results if the schema changes.

---

### Filtering: Comparison Operators and Logical Operators
*Filtering: Comparison Operators and Logical Operators*

The `WHERE` clause filters rows based on **conditions** built with **Comparison Operators** and **Logical Operators**. Only the rows for which the condition evaluates to `TRUE` are included in the result.

**Comparison Operators:**

| Operator | Meaning | Example |
|---|---|---|
| `=` | Equality | `dept_id = 1` |
| `!=` or `<>` | Inequality | `dept_id != 2` |
| `>` | Greater than | `am > 10002` |
| `<` | Less than | `am < 10003` |
| `>=` | Greater than or equal | `am >= 10002` |
| `<=` | Less than or equal | `am <= 10003` |
| `BETWEEN a AND b` | Between two values (inclusive) | `am BETWEEN 10001 AND 10003` |
| `IN (v1, v2, ...)` | Belongs to a set of values | `dept_id IN (1, 3)` |
| `IS NULL` | The value is NULL | `email IS NULL` |
| `IS NOT NULL` | The value is not NULL | `hmerominia IS NOT NULL` |
| `LIKE 'pattern'` | Pattern matching (% = many characters, _ = one) | `eponymo LIKE 'Papa%'` |

**Logical Operators:**

| Operator | Meaning | Result `TRUE` |
|---|---|---|
| `AND` | Logical AND | Both conditions are `TRUE` |
| `OR` | Logical OR | At least one condition is `TRUE` |
| `NOT` | Negation | The condition is `FALSE` |

**Example 1 — Equality filter `=`:**

**Table state:**

```text
  Foititis (full):
  +-------+--------+--------------+------------+---------+
  | am    | onoma  | eponymo      | hmerominia | dept_id |
  +-------+--------+--------------+------------+---------+
  | 10001 | Alexis | Nikolopoulos | 2001-05-10 |       1 |
  | 10002 | Eleni  | Papadopoulou | 2002-09-15 |       4 |
  | 10004 | Maria  | Stavridou    | 2003-01-30 |       3 |
  +-------+--------+--------------+------------+---------+
```

**Execution:**

```sql
-- Retrieving students who belong to department 1
SELECT am, onoma, eponymo
FROM   Foititis
WHERE  dept_id = 1;
```

**Result:**

```text
  +-------+--------+--------------+
  | am    | onoma  | eponymo      |
  +-------+--------+--------------+
  | 10001 | Alexis | Nikolopoulos |
  +-------+--------+--------------+
  1 row in set (0.00 sec)
```

**Example 2 — The `>` operator (greater than):**

**Execution:**

```sql
-- Retrieving students with am greater than 10001
SELECT am, onoma, eponymo
FROM   Foititis
WHERE  am > 10001;
```

**Result:**

```text
  +-------+--------+--------------+
  | am    | onoma  | eponymo      |
  +-------+--------+--------------+
  | 10002 | Eleni  | Papadopoulou |
  | 10004 | Maria  | Stavridou    |
  +-------+--------+--------------+
```

**Example 3 — The `AND` operator (both conditions):**

**Execution:**

```sql
-- Students of department 1 who were born before 2002
SELECT am, onoma, hmerominia, dept_id
FROM   Foititis
WHERE  dept_id = 1
  AND  hmerominia < '2002-01-01';
```

**Result:**

```text
  +-------+--------+------------+---------+
  | am    | onoma  | hmerominia | dept_id |
  +-------+--------+------------+---------+
  | 10001 | Alexis | 2001-05-10 |       1 |
  +-------+--------+------------+---------+
```

**Example 4 — The `OR` operator (at least one condition):**

**Execution:**

```sql
-- Students who belong to department 1 OR department 3
SELECT am, onoma, dept_id
FROM   Foititis
WHERE  dept_id = 1
    OR dept_id = 3;
```

**Result:**

```text
  +-------+--------+---------+
  | am    | onoma  | dept_id |
  +-------+--------+---------+
  | 10001 | Alexis |       1 |
  | 10004 | Maria  |       3 |
  +-------+--------+---------+
```

**Equivalent to `IN`:**

```sql
-- Shorter notation for multiple OR values
SELECT am, onoma, dept_id
FROM   Foititis
WHERE  dept_id IN (1, 3);
```

**Example 5 — The `NOT` operator (negation):**

**Execution:**

```sql
-- Students who do NOT belong to department 1
SELECT am, onoma, dept_id
FROM   Foititis
WHERE  NOT dept_id = 1;
-- Equivalent: WHERE dept_id != 1  or  WHERE dept_id <> 1
```

**Result:**

```text
  +-------+-------+---------+
  | am    | onoma | dept_id |
  +-------+-------+---------+
  | 10002 | Eleni |       4 |
  | 10004 | Maria |       3 |
  +-------+-------+---------+
```

**Example 6 — Combination of `AND`, `OR`, and parentheses:**

```sql
-- Students who (belong to department 1 AND were born after 2000)
-- Or belong to department 3
SELECT am, onoma, eponymo, hmerominia, dept_id
FROM   Foititis
WHERE  (dept_id = 1 AND hmerominia > '2000-01-01')
    OR dept_id = 3;
```

**Exam Note:** When using `AND` and `OR` in the same `WHERE`, the **precedence order** is critical: `AND` is evaluated **before** `OR`. Using **parentheses** to explicitly define the evaluation order is considered best practice and prevents logical errors.

**Example 7 — The `LIKE` operator for pattern search:**

**Execution:**

```sql
-- Students whose surname starts with 'Papa'
SELECT am, onoma, eponymo
FROM   Foititis
WHERE  eponymo LIKE 'Papa%';
```

**Result:**

```text
  +-------+-------+--------------+
  | am    | onoma | eponymo      |
  +-------+-------+--------------+
  | 10002 | Eleni | Papadopoulou |
  +-------+-------+--------------+
```

**Example 8 — The `IS NULL` operator:**

```sql
-- Students for whom an email has not been recorded
SELECT am, onoma
FROM   Foititis
WHERE  email IS NULL;
```

**Relational Algebra — SQL correspondence (summary):**

| Relational Algebra | SQL |
|---|---|
| $\sigma_{\text{dept\_id}=1}(\text{Foititis})$ | `SELECT * FROM Foititis WHERE dept_id = 1` |
| $\pi_{\text{onoma, eponymo}}(\text{Foititis})$ | `SELECT onoma, eponymo FROM Foititis` |
| $\pi_{\text{onoma}}(\sigma_{\text{dept\_id}=1}(\text{Foititis}))$ | `SELECT onoma FROM Foititis WHERE dept_id = 1` |
| $\sigma_{\text{dept\_id}=1 \land \text{am}>10001}(\text{Foititis})$ | `SELECT * FROM Foititis WHERE dept_id = 1 AND am > 10001` |

---

## Comparative Table: DDL vs DML vs DQL
*Comparative Table: DDL vs DML vs DQL*

| Characteristic | DDL | DML | DQL |
|---|---|---|---|
| **Name** | Data Definition Language | Data Manipulation Language | Data Query Language |
| **Purpose** | Defining/modifying structures | Manipulating data | Retrieving data |
| **Main statements** | `CREATE`, `DROP`, `ALTER` | `INSERT`, `UPDATE`, `DELETE` | `SELECT` |
| **What it modifies** | Database schema (structure) | Data (records) | Nothing (read-only) |
| **Implicit COMMIT** | Yes (MySQL) | No | Not applicable |
| **ROLLBACK possible?** | No | Yes (within a transaction) | Not applicable |
| **Risk of loss** | High (DROP) | Medium (DELETE without WHERE) | None |
| **Relational Algebra correspondence** | Relation definition | Tuple modification | $\sigma$, $\pi$, $\bowtie$ |

---

## Summary Table of Key Concepts
*Summary Table of Key Concepts*

| Concept | Definition | Key Characteristic / Rule |
|---|---|---|
| **DML** (Data Manipulation Language) | Subset of SQL for manipulating data | `INSERT`, `UPDATE`, `DELETE` — supports `ROLLBACK` |
| **DQL** (Data Query Language) | Subset of SQL for retrieving data | `SELECT` — does not modify data |
| **INSERT INTO** | Inserts new records into a table | Respects constraints (PK, FK, NOT NULL) |
| **UPDATE ... SET** | Modifies values of existing records | Without `WHERE` updates ALL rows |
| **DELETE FROM** | Deletes records from a table | Without `WHERE` deletes ALL rows — structure remains |
| **SELECT** | Retrieves data from table(s) | The most frequent SQL statement — corresponds to $\pi$ + $\sigma$ |
| **FROM** | Defines the source table(s) | Mandatory clause of every `SELECT` |
| **WHERE** | Filters rows based on a condition | Corresponds to the Selection $\sigma$ of Relational Algebra |
| **SELECT \*** | Selects all columns | Useful for debugging — avoided in production code |
| **SELECT DISTINCT** | Returns unique values | Removes duplicate rows from the result |
| **The `=` operator** | Equality in `WHERE` | Differs from `IS NULL` — `= NULL` does not work |
| **The `>`/`<` operators** | Size comparison | Applies to numbers, dates, text (alphanumeric) |
| **The `AND` operator** | Logical AND | Higher precedence than `OR` — parentheses recommended |
| **The `OR` operator** | Logical OR | Returns rows where at least one condition is `TRUE` |
| **The `NOT` operator** | Logical negation | Inverts the result of the condition |
| **The `IN` operator** | Belongs to a set of values | Shorthand for multiple `OR` equalities |
| **The `LIKE` operator** | Pattern-based search | `%` = many characters, `_` = one character |
| **The `IS NULL` operator** | Check for a NULL value | `= NULL` is wrong — `IS NULL` is always used |
| **Alias (`AS`)** | Renames a column in the result | Does not change the schema — only the presentation |
| **`TRUNCATE TABLE`** | Quickly deletes ALL records | Behaves like DDL — does not support `ROLLBACK` |

---

## Key Takeaways
*Key Takeaways*

- **DML** (INSERT, UPDATE, DELETE) handles the **data** inside the tables — it does not change their structure/schema. Unlike DDL, DML statements **support** `ROLLBACK` within transactions.
- The `INSERT INTO` statement with **explicit column definition** (`INSERT INTO table (col1, col2) VALUES (v1, v2)`) is always safer than the syntax without columns — it does not depend on the column order and allows omitting optional fields.
- **Exam Note:** Without a `WHERE` clause, `UPDATE` updates and `DELETE` deletes **every row** of the table — this is one of the most common and destructive mistakes. Running a corresponding `SELECT` before the `UPDATE`/`DELETE` is best practice.
- `SELECT` corresponds to the **combination of Projection ($\pi$) and Selection ($\sigma$)** of Relational Algebra: the column list implements the Projection, the `WHERE` implements the Selection.
- The `WHERE` clause is built with **Comparison Operators** (`=`, `>`, `<`, `>=`, `<=`, `!=`) and **Logical Operators** (`AND`, `OR`, `NOT`). The precedence order is: `NOT` > `AND` > `OR` — using parentheses eliminates ambiguity.
- **Key Distinction:** `DELETE FROM table` (without `WHERE`) empties the data but **preserves the table's structure**, while `DROP TABLE` destroys both the data and the structure. `TRUNCATE TABLE` empties quickly like `DELETE` without `WHERE`, but behaves like DDL (does not support `ROLLBACK`).
- `SELECT *` is useful for quick exploration, but it is **avoided in production code** — it burdens performance and hides which columns are actually used.
- **Key Distinction:** For checking a NULL value, `IS NULL` or `IS NOT NULL` is **always** used — the `= NULL` syntax does not work correctly in SQL, because `NULL` is not a value but a state of the absence of a value.
- The `IN (v1, v2, ...)` operator is equivalent to multiple `OR` equalities and is preferred for **shorter and more readable code** when checking many values.
- **Exam Note:** `SELECT` (DQL) is the **only statement that does not modify** data — it is purely read-only. Every `INSERT`, `UPDATE`, and `DELETE` modifies the table and leaves a permanent mark (except with `ROLLBACK`).

---
# topic_7_practical_application_and_dev_environments.md
---

# Practical Application & Development Environments
*Practical Application & Development Environments*

---

## Table of Contents
*Table of Contents*

1. [Introduction](#introduction)
2. [Tools, Systems & Architecture](#tools-systems--architecture)
   - [MySQL Server](#mysql-server)
   - [MySQL Workbench](#mysql-workbench)
   - [XAMPP & phpMyAdmin](#xampp--phpmyadmin)
   - [Comparative Table: Management Tools](#comparative-table-management-tools)
3. [Implementation in Real-World Conditions](#implementation-in-real-world-conditions)
   - [Determining Appropriate Data Types](#determining-appropriate-data-types)
   - [Implementing Constraints (NOT NULL, UNIQUE, DEFAULT)](#implementing-constraints-not-null-unique-default)
   - [Connecting Tables via Foreign Keys (FOREIGN KEY ... REFERENCES)](#connecting-tables-via-foreign-keys-foreign-key--references)
   - [Managing "Many-to-Many" Relationships (Junction Table)](#managing-many-to-many-relationships-junction-table)
4. [Summary Table of Key Concepts](#summary-table-of-key-concepts)
5. [Key Takeaways](#key-takeaways)

---

## Introduction

The theoretical knowledge of data models, Relational Algebra, and SQL gains full value only when applied to real software. In the context of this course, the dominant implementation system is **MySQL** — one of the most widely used open-source **Relational Database Management Systems (RDBMS)** worldwide. This practical section covers both the **tools** (MySQL Server, MySQL Workbench, XAMPP, phpMyAdmin) and the **design decisions** the database administrator makes during implementation: choosing data types, defining constraints, declaring Foreign Keys, and handling N:M relationships through junction tables. The ability to translate an ER diagram or a Relational Schema into a functional MySQL database is a fundamental skill for every software engineer.

---

## Tools, Systems & Architecture
*Tools, Systems & Architecture*

The architecture of a MySQL system is based on the **client-server** model: the **MySQL Server** runs in the background as a service (service/daemon) that manages the data, while various **client tools** connect to it to run queries and administrative tasks.

```text
  MySQL Client-Server Architecture:

  +---------------------+        TCP/IP or Socket      +---------------------+
  |     CLIENT TOOLS    |  <-------------------------->  |    MySQL Server     |
  +---------------------+                               +---------------------+
  |  mysql CLI          |                               |  - Query Engine     |
  |  MySQL Workbench    |                               |  - Storage Engine   |
  |  phpMyAdmin         |                               |    (InnoDB)         |
  |  Application (PHP/  |                               |  - Buffer Pool      |
  |  Python/Java)       |                               |  - Log Files        |
  +---------------------+                               +---------------------+
                                                               |
                                                        +------+------+
                                                        |  Data      |
                                                        |  (Disk     |
                                                        |  Files)    |
                                                        +------------+
```

---

### MySQL Server
*The Backend Database Management System*

The **MySQL Server** is the core (backend) of the system — the process that **stores, organizes, and serves** the data. It runs continuously as a **service** of the operating system and listens for incoming connections from clients (by default on port **3306**). It has no graphical interface — interaction takes place through SQL statements sent by a client.

**Main features:**
- Supports multiple concurrent users (**Concurrency**) through transaction management.
- Primarily uses the **InnoDB Storage Engine**, which supports Foreign Keys, Transactions, and ACID guarantees.
- Manages access rights (**privileges**) per user and per database.

**Connecting via the command line (mysql CLI):**

```sql
-- Connecting as root user to the local MySQL Server
mysql -u root -p

-- After connecting, display the available databases
SHOW DATABASES;
```

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

**Exam Note:** The databases `information_schema`, `mysql`, `performance_schema`, and `sys` are **system databases** created automatically by the MySQL Server. They must never be modified manually.

---

### MySQL Workbench
*Graphical Database Management Environment / GUI Client*

**MySQL Workbench** is the official **graphical environment (GUI)** provided by Oracle for managing MySQL Server. It combines in a single tool:
- **SQL Editor**: Writing and executing SQL queries with syntax highlighting and autocompletion.
- **Visual Schema Designer (EER Diagram)**: Visual design and modification of database schemas — creating tables, defining relationships with drag-and-drop.
- **Server Administration**: Managing users, privileges, server status, and log files.
- **Data Export / Import**: Importing and exporting data in SQL dump, CSV, and other formats.

```text
  MySQL Workbench — Work Areas:

  +-----------------------------------------------------------+
  |                    MySQL Workbench                        |
  +------------------+----------------------------------------+
  |  Navigator       |                                        |
  |  +------------+  |   +--------------------------------+  |
  |  | Schemas    |  |   |       SQL Editor               |  |
  |  | - uni_db   |  |   |  SELECT * FROM Foititis;       |  |
  |  |   Tables   |  |   |  > Execute (Ctrl+Enter)        |  |
  |  |   Views    |  |   +--------------------------------+  |
  |  |   Procs    |  |   |       Result Grid              |  |
  |  +------------+  |   |  am | onoma | eponymo | ...    |  |
  |                  |   +--------------------------------+  |
  +------------------+----------------------------------------+
```

**Analogy**: MySQL Workbench is like an **airplane cockpit** — it provides all the information and controls in a graphical environment, while the MySQL Server is the engines that actually do the work.

---

### XAMPP & phpMyAdmin
*Web-Based Management Package and Services*

**XAMPP** (X = Cross-platform, A = Apache, M = MariaDB/MySQL, P = PHP, P = Perl) is an **installation package** that bundles in one installer:
- **Apache HTTP Server**: Web server for serving PHP applications.
- **MySQL / MariaDB**: Relational database server.
- **PHP**: Server-side scripting language.
- **phpMyAdmin**: Web-based tool for managing MySQL through a browser.

**phpMyAdmin** is a PHP application that runs on Apache and provides **full MySQL management through a web browser**, without installing additional software. It is ideal for web hosting environments where there is no direct CLI access.

```text
  XAMPP Stack — Architecture:

  Browser (Client)
       |
       | HTTP Request (e.g., http://localhost/phpmyadmin)
       v
  +--------------------+
  |   Apache Server    |  <-- Runs PHP scripts
  +--------------------+
       |
       | MySQL Protocol (port 3306)
       v
  +--------------------+
  |  MySQL / MariaDB   |  <-- Stores the data
  +--------------------+

  phpMyAdmin is a set of PHP files on Apache
  that act as a web-based MySQL client.
```

**Key Distinction:** XAMPP is often used for **local development (localhost)** of web applications, while in a production environment the components (Apache, MySQL, PHP) are installed and configured separately for security and performance reasons.

---

### Comparative Table: Management Tools
*Comparative Table: Management Tools*

| Characteristic | MySQL Server (CLI) | MySQL Workbench | phpMyAdmin |
|---|---|---|---|
| **Type** | CLI / Backend Service | Desktop GUI Client | Web-based GUI Client |
| **Interface** | Command line | Graphical (Desktop App) | Browser |
| **Installation** | Only | Separately (requires Server) | Part of XAMPP or standalone |
| **ER design** | No | Yes (Visual EER Designer) | Limited |
| **Suitable for** | Scripting, automation | Development, design | Web hosting, quick access |
| **Requires PHP/Apache** | No | No | Yes |
| **Import/Export** | mysqldump CLI | Yes (GUI) | Yes (GUI) |

---

## Implementation in Real-World Conditions
*Implementation in Real-World Conditions*

Implementing a Relational Schema in MySQL requires, beyond knowledge of SQL syntax, a series of **design decisions** that affect the integrity, performance, and maintainability of the database. The critical decisions concern: which **data type** fits each field, which **constraints** ensure data quality, and how the **relationships** between tables are implemented.

---

### Determining Appropriate Data Types
*Determining Appropriate Data Types*

The **data type** of each column defines the **kind and range of values** it can store. Choosing the correct type is critical: a type that is too large wastes storage space, while one that is too small may not fit the data and can cause an error or loss of information.

**Main categories of MySQL data types:**

| Category | Type | Storage / Range | Typical Use |
|---|---|---|---|
| **Integers** | `TINYINT` | 1 byte, -128 to 127 (or 0-255 UNSIGNED) | Boolean flags, small categories |
| | `SMALLINT` | 2 bytes, -32,768 to 32,767 | Small numbers |
| | `INT` / `INTEGER` | 4 bytes, ~-2.1 billion to 2.1 billion | IDs, quantities, counts |
| | `BIGINT` | 8 bytes, ~-9.2 · 10¹⁸ to 9.2 · 10¹⁸ | Very large numbers, timestamps |
| **Decimals** | `FLOAT` | 4 bytes | Approximate decimals |
| | `DOUBLE` | 8 bytes | Scientific calculations |
| | `DECIMAL(M,D)` | Variable | Monetary amounts (exact representation) |
| **Text** | `CHAR(N)` | Fixed N bytes (1-255) | Fixed-length codes (e.g., country ISO) |
| | `VARCHAR(N)` | Variable, up to N bytes (1-65535) | Names, emails, titles |
| | `TEXT` | Up to 65,535 bytes | Large texts (descriptions, comments) |
| **Date/Time** | `DATE` | 3 bytes, `YYYY-MM-DD` | Birth date, start date |
| | `DATETIME` | 8 bytes, `YYYY-MM-DD HH:MM:SS` | Event timestamp |
| | `TIMESTAMP` | 4 bytes, automatic UTC update | Last record modification |
| | `TIME` | 3 bytes, `HH:MM:SS` | Duration, schedule |
| **Boolean** | `BOOLEAN` / `TINYINT(1)` | 1 byte (0 = FALSE, 1 = TRUE) | Status flags |

**Example — Creating table `Foititis` with selected types:**

```sql
CREATE TABLE Foititis (
    -- INT: integer Registration Number, up to ~2 billion
    am           INT            NOT NULL,
    -- VARCHAR(50): variable-length text, up to 50 characters
    onoma        VARCHAR(50)    NOT NULL,
    eponymo      VARCHAR(50)    NOT NULL,
    -- VARCHAR(100): email may be longer
    email        VARCHAR(100),
    -- DATE: stores only the date without time
    hmerominia   DATE,
    -- INT: Foreign Key to dept_id of the Tmima table
    dept_id      INT            NOT NULL,
    PRIMARY KEY (am)
);
```

**Comparison of `CHAR` vs `VARCHAR`:**

| Characteristic | `CHAR(N)` | `VARCHAR(N)` |
|---|---|---|
| **Storage length** | Always N bytes (padded with spaces) | Actual length + 1-2 bytes overhead |
| **Performance** | Faster for fixed length | More efficient for variable length |
| **Suitable for** | Country codes (`GR`, `US`), tax ID | Names, emails, addresses |

**Exam Note:** For monetary amounts, `FLOAT` or `DOUBLE` is **never** used because of floating-point rounding errors. `DECIMAL(10, 2)` (e.g., 10 digits in total, 2 decimal places) is used for exact representation.

---

### Implementing Constraints (NOT NULL, UNIQUE, DEFAULT)
*Implementing Constraints*

**Constraints** are rules that MySQL enforces automatically on every `INSERT` or `UPDATE`, ensuring **data integrity**. They are defined at creation time (`CREATE TABLE`) or added later (`ALTER TABLE`).

**Main constraints:**

| Constraint | Purpose | Violation |
|---|---|---|
| `NOT NULL` | Prohibits NULL values in a column | `ERROR 1048: Column cannot be null` |
| `UNIQUE` | Ensures uniqueness of values (NULL allowed) | `ERROR 1062: Duplicate entry` |
| `DEFAULT value` | Sets a default value if none is given | — (does not cause an error) |
| `PRIMARY KEY` | `NOT NULL` + `UNIQUE` + index | `ERROR 1062` or `ERROR 1048` |
| `CHECK (expr)` | Verifies a logical condition (MySQL 8.0.16+) | `ERROR 3819: Check constraint violated` |

**Example — Table `Mathima` with multiple constraints:**

```sql
CREATE TABLE Mathima (
    -- PRIMARY KEY: NOT NULL + UNIQUE automatically
    mathima_id   INT           NOT NULL AUTO_INCREMENT,
    -- NOT NULL: the title is mandatory
    titlos       VARCHAR(100)  NOT NULL,
    -- UNIQUE: the course code must be unique
    kodikos      VARCHAR(10)   NOT NULL UNIQUE,
    -- DEFAULT: if no ECTS credits are given, they are considered 5
    ects         TINYINT       NOT NULL DEFAULT 5,
    -- NULL allowed: the description is optional
    perigrafi    TEXT,
    -- CHECK: the ECTS credits must be between 1 and 30
    CONSTRAINT chk_ects CHECK (ects BETWEEN 1 AND 30),
    PRIMARY KEY (mathima_id)
);
```

**Demonstration of constraint behavior:**

**Before:**
```text
  mysql> SELECT * FROM Mathima;
  Empty set (0.00 sec)
```

**Successful insertion (with DEFAULT):**
```sql
-- No value is given for ects - it receives DEFAULT 5
INSERT INTO Mathima (titlos, kodikos)
VALUES ('Databases', 'CS301');
```

**After:**
```text
  mysql> SELECT * FROM Mathima;
  +------------+------------------+---------+------+-----------+
  | mathima_id | titlos           | kodikos | ects | perigrafi |
  +------------+------------------+---------+------+-----------+
  |          1 | Databases        | CS301   |    5 | NULL      |
  +------------+------------------+---------+------+-----------+
```

**NOT NULL violation:**
```sql
-- No value is given for titlos (NOT NULL) - error
INSERT INTO Mathima (kodikos) VALUES ('CS302');
-- ERROR 1364 (HY000): Field 'titlos' doesn't have a default value
```

**UNIQUE violation:**
```sql
-- The code 'CS301' already exists - UNIQUE violation
INSERT INTO Mathima (titlos, kodikos)
VALUES ('Another Course', 'CS301');
-- ERROR 1062 (23000): Duplicate entry 'CS301' for key 'mathima.kodikos'
```

**CHECK violation:**
```sql
-- ects = 50 exceeds the CHECK constraint (1-30)
INSERT INTO Mathima (titlos, kodikos, ects)
VALUES ('Test Course', 'CS399', 50);
-- ERROR 3819 (HY000): Check constraint 'chk_ects' is violated.
```

**Key Distinction:** The `UNIQUE` constraint allows **multiple NULL values** in the same column (NULL is not considered equal to any value, nor to another NULL). In contrast, `PRIMARY KEY` **does not allow** any NULL value.

---

### Connecting Tables via Foreign Keys (FOREIGN KEY ... REFERENCES)
*Connecting Tables via Foreign Keys*

The **Foreign Key** is the mechanism by which MySQL enforces **Referential Integrity** between two tables. It ensures that every value in the FK column of the **child table** corresponds to an existing value in the **parent table**.

**Referential Integrity rules:**
- No record can be inserted into the child with an FK value that does not exist in the parent.
- No record can be deleted from the parent if child records reference it.

**FOREIGN KEY declaration syntax:**

```sql
-- Inline definition (for simple FKs)
CREATE TABLE child_table (
    fk_column   INT,
    FOREIGN KEY (fk_column) REFERENCES parent_table (pk_column)
);

-- Definition with a constraint name (recommended - more readable)
CREATE TABLE child_table (
    fk_column   INT,
    CONSTRAINT fk_child_parent
        FOREIGN KEY (fk_column)
        REFERENCES parent_table (pk_column)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);
```

**Example — Relationship `Foititis` → `Tmima` (N:1):**

```text
  Relational Schema:
  Tmima(<u>dept_id</u>, onoma_tmimatos, sxoli)
  Foititis(<u>am</u>, onoma, eponymo, email, hmerominia, #dept_id)

  ER Representation:
  +-------------+            1:N           +------------+
  |    TMIMA    |  <>---( Belongs to )---<  |  FOITITIS  |
  +-------------+                          +------------+
  | dept_id(PK) |                          | am (PK)    |
  | onoma_tmim. |                          | onoma      |
  | sxoli       |                          | eponymo    |
  +-------------+                          | dept_id(FK)|
                                           +------------+
```

**Creating tables with a FOREIGN KEY:**

```sql
-- Step 1: First the parent table
CREATE TABLE Tmima (
    dept_id        INT          NOT NULL AUTO_INCREMENT,
    onoma_tmimatos VARCHAR(100) NOT NULL,
    sxoli          VARCHAR(100) NOT NULL,
    PRIMARY KEY (dept_id)
);

-- Step 2: Then the child table with FK
CREATE TABLE Foititis (
    am           INT          NOT NULL,
    onoma        VARCHAR(50)  NOT NULL,
    eponymo      VARCHAR(50)  NOT NULL,
    email        VARCHAR(100) UNIQUE,
    hmerominia   DATE,
    dept_id      INT          NOT NULL,
    PRIMARY KEY (am),
    -- Defining the Foreign Key with an explicit constraint name
    CONSTRAINT fk_foititis_tmima
        FOREIGN KEY (dept_id)
        REFERENCES Tmima (dept_id)
        ON DELETE RESTRICT   -- Prevents deleting a department with students
        ON UPDATE CASCADE    -- If dept_id changes in Tmima, it is updated automatically
);
```

**Demonstration of Referential Integrity:**

**Inserting data:**
```sql
-- Inserting departments into the parent
INSERT INTO Tmima (onoma_tmimatos, sxoli)
VALUES ('Informatics', 'Sciences'),
       ('Mathematics',  'Sciences');
```

```text
  Tmima:
  +---------+-------------------+-------------------+
  | dept_id | onoma_tmimatos    | sxoli             |
  +---------+-------------------+-------------------+
  |       1 | Informatics      | Sciences         |
  |       2 | Mathematics      | Sciences         |
  +---------+-------------------+-------------------+
```

```sql
-- Successful insertion: dept_id=1 exists in Tmima
INSERT INTO Foititis (am, onoma, eponymo, dept_id)
VALUES (10001, 'Alexis', 'Nikolopoulos', 1);
```

**FK violation — insertion with a non-existent dept_id:**
```sql
-- FAILURE: dept_id=99 does not exist in the Tmima table
INSERT INTO Foititis (am, onoma, eponymo, dept_id)
VALUES (10002, 'Eleni', 'Papadopoulou', 99);
-- ERROR 1452 (23000): Cannot add or update a child row:
-- a foreign key constraint fails (`university_db`.`Foititis`,
-- CONSTRAINT `fk_foititis_tmima` FOREIGN KEY (`dept_id`)
-- REFERENCES `Tmima` (`dept_id`))
```

**FK violation — deleting a parent with dependent children:**
```sql
-- FAILURE: department 1 has students - ON DELETE RESTRICT
DELETE FROM Tmima WHERE dept_id = 1;
-- ERROR 1451 (23000): Cannot delete or update a parent row:
-- a foreign key constraint fails
```

**ON DELETE / ON UPDATE options:**

| Option | Behavior upon deletion/update of a parent record |
|---|---|
| `RESTRICT` (default) | Prevents the action — returns an error |
| `CASCADE` | Propagates the change automatically to the children |
| `SET NULL` | Sets the FK column to NULL (the column must allow NULL) |
| `NO ACTION` | Similar to RESTRICT (checked at the end of the transaction) |
| `SET DEFAULT` | Sets a DEFAULT value (rarely supported by InnoDB) |

**Exam Note:** The order of table creation matters: **first the parent, then the child**. Conversely, when **deleting**: **first the child, then the parent**. Also, MySQL requires the **InnoDB** Storage Engine (not MyISAM) to support Foreign Keys.

---

### Managing "Many-to-Many" Relationships (Junction Table)
*Managing Many-to-Many Relationships via Junction Table*

**N:M (Many-to-Many)** relationships cannot be implemented directly in the Relational Model. The solution is to **break them down into two 1:N relationships** through a **junction table (associative table / bridge table)**, which contains the Foreign Keys of both tables.

**The problem of the N:M relationship:**

Suppose a student enrolls in many courses, and each course has many students.

```text
  ER Diagram (N:M):
  +------------+     N:M          +------------+
  |  FOITITIS  |<>--( Registers )--<>|  MATHIMA   |
  +------------+    in            +------------+
  | am (PK)    |                  | mathima_id |
  | onoma      |                  | titlos     |
  +------------+                  +------------+

  PROBLEM: It cannot be implemented with a single FK column —
  neither can Foititis have many dept_id values,
  nor can Mathima have many am values in one column.
```

**Solution — Decomposition into two 1:N relationships through a junction table:**

```text
  After decomposition:

  +------------+   1:N   +-------------------+   N:1   +------------+
  |  FOITITIS  |<--------| EGGRAFI (Junction) |-------->|  MATHIMA   |
  +------------+         +-------------------+         +------------+
  | am (PK)    |         | am (FK, PK)       |         | mathima_id |
  | onoma      |         | mathima_id (FK,PK)|         | titlos     |
  +------------+         | hmerominia_eggraf |         +------------+
                          | vathmos           |
                          +-------------------+

  Relational Schema:
  Foititis(<u>am</u>, onoma, eponymo, dept_id)
  Mathima(<u>mathima_id</u>, titlos, kodikos, ects)
  Eggrafi(<u>am</u>, <u>mathima_id</u>, hmerominia_eggrafis, vathmos)
           ^FK→Foititis  ^FK→Mathima
```

**Creating the junction table `Eggrafi`:**

```sql
-- Step 1: Parent tables (Foititis and Mathima already exist)

-- Step 2: The intermediate table with a Composite Primary Key
CREATE TABLE Eggrafi (
    -- FK to Foititis
    am                  INT  NOT NULL,
    -- FK to Mathima
    mathima_id          INT  NOT NULL,
    -- Additional attributes of the relationship (relationship attributes)
    hmerominia_eggrafis DATE,
    vathmos             DECIMAL(4, 2),
    -- Composite Primary Key: the am+mathima_id combination is unique
    PRIMARY KEY (am, mathima_id),
    -- FK to Foititis
    CONSTRAINT fk_eggrafi_foititis
        FOREIGN KEY (am)
        REFERENCES Foititis (am)
        ON DELETE CASCADE,   -- If a student is deleted, their records are deleted
    -- FK to Mathima
    CONSTRAINT fk_eggrafi_mathima
        FOREIGN KEY (mathima_id)
        REFERENCES Mathima (mathima_id)
        ON DELETE RESTRICT   -- A course with enrolled students cannot be deleted
);
```

**Inserting data into the junction table:**

```sql
-- Student am=10001 enrolls in course mathima_id=1
INSERT INTO Eggrafi (am, mathima_id, hmerominia_eggrafis)
VALUES (10001, 1, '2024-10-01');

-- The same student enrolls in a second course
INSERT INTO Eggrafi (am, mathima_id, hmerominia_eggrafis)
VALUES (10001, 2, '2024-10-01');

-- Another student in the same course
INSERT INTO Eggrafi (am, mathima_id, hmerominia_eggrafis)
VALUES (10002, 1, '2024-10-02');
```

```text
  Eggrafi:
  +-------+------------+--------------------+---------+
  | am    | mathima_id | hmerominia_eggraf. | vathmos |
  +-------+------------+--------------------+---------+
  | 10001 |          1 | 2024-10-01         |    NULL |
  | 10001 |          2 | 2024-10-01         |    NULL |
  | 10002 |          1 | 2024-10-02         |    NULL |
  +-------+------------+--------------------+---------+
```

**Retrieving data via JOIN:**

```sql
-- Which courses does student am=10001 attend?
SELECT f.onoma, f.eponymo, m.titlos, m.kodikos, e.hmerominia_eggrafis
FROM   Eggrafi e
JOIN   Foititis f  ON e.am         = f.am
JOIN   Mathima  m  ON e.mathima_id = m.mathima_id
WHERE  e.am = 10001;
```

```text
  +--------+--------------+------------------+---------+--------------------+
  | onoma  | eponymo      | titlos           | kodikos | hmerominia_eggraf. |
  +--------+--------------+------------------+---------+--------------------+
  | Alexis | Nikolopoulos | Databases        | CS301   | 2024-10-01         |
  | Alexis | Nikolopoulos | Algorithms       | CS201   | 2024-10-01         |
  +--------+--------------+------------------+---------+--------------------+
```

**Preventing duplicate enrollment (the same student in the same course):**

```sql
-- Attempting a duplicate enrollment: am=10001, mathima_id=1 already exists
INSERT INTO Eggrafi (am, mathima_id)
VALUES (10001, 1);
-- ERROR 1062 (23000): Duplicate entry '10001-1' for key 'Eggrafi.PRIMARY'
-- The Composite PK prevents the duplicate enrollment automatically.
```

**Key Distinction:** In the junction table, the **Composite Primary Key** `(am, mathima_id)` plays a dual role: (1) it guarantees that every student-course combination appears **at most once**, and (2) it automatically acts as an **index** for faster lookups based on both fields.

---

## Summary Table of Key Concepts
*Summary Table of Key Concepts*

| Concept | Definition | Key Characteristic / Rule |
|---|---|---|
| **MySQL Server** | The backend RDBMS that stores and serves data | Runs as a service, listens on port 3306 |
| **MySQL Workbench** | Official desktop GUI client for MySQL | Includes SQL editor, Visual EER designer, server admin |
| **XAMPP** | Cross-platform package (Apache + MySQL/MariaDB + PHP) | For local development of web applications (localhost) |
| **phpMyAdmin** | Web-based GUI for MySQL through a browser | Runs as a PHP application on Apache |
| **InnoDB** | MySQL's storage engine | Supports Foreign Keys, Transactions, ACID |
| **Data Type** | Defines the kind and range of values of a column | Wrong type → wasted space or data loss |
| **NOT NULL** | Constraint that prohibits NULL values | Violation → `ERROR 1048` |
| **UNIQUE** | Constraint of value uniqueness (NULL allowed) | Violation → `ERROR 1062` |
| **DEFAULT** | Sets an automatic value if none is provided | Does not cause an error — applied silently |
| **FOREIGN KEY** | Column that references the Primary Key of another table | Enforces Referential Integrity |
| **ON DELETE CASCADE** | Propagates the deletion to child records | Caution: mass automatic deletion |
| **ON DELETE RESTRICT** | Prevents deletion of the parent if children exist | Default — the safest option |
| **Junction Table** | Intermediate table for implementing an N:M relationship | Carries a Composite PK of the two FKs |
| **Composite Primary Key** | PK composed of two or more columns | Used in the N:M junction table |
| **AUTO_INCREMENT** | Automatic increment of an integer PK | MySQL assigns the next available value |

---

## Key Takeaways
*Key Takeaways*

- The **MySQL Server** is the backend system that runs as a service; the tools (Workbench, phpMyAdmin, CLI) are merely **clients** that connect to it.
- **MySQL Workbench** offers visual schema design (EER Diagrams) and is the main development tool; **XAMPP/phpMyAdmin** targets web environments and quick access through a browser.
- Choosing the correct **data type** is critical: `INT` for IDs, `VARCHAR` for variable-length text, `DATE` for dates, `DECIMAL` (not `FLOAT`) for monetary amounts.
- The combination of `NOT NULL`, `UNIQUE`, and `DEFAULT` defines the data quality rules at the column level and is enforced automatically by the engine on every write.
- The `FOREIGN KEY ... REFERENCES` declaration with an **explicit constraint name** is best practice — it facilitates debugging when an FK violation error appears.
- **Referential Integrity** requires a strict order of table creation: **first the parent, then the child**; and the reverse for deletion.
- `ON DELETE CASCADE` is powerful but dangerous — deleting a parent record can automatically delete **dozens or thousands** of child records. `ON DELETE RESTRICT` is the safest default rule.
- **N:M relationships are never implemented directly** — they are always decomposed into two 1:N relationships through a **junction table** with a **Composite Primary Key**.
- The junction table can carry **additional attributes** of the relationship itself (e.g., enrollment date, grade) that do not belong to the original tables.
- MySQL requires the **InnoDB** storage engine (not MyISAM) to support Foreign Keys; the check is done with `SHOW CREATE TABLE table_name;`.

---
# topic_8_9_relational_algebra_joins_and_security_policies.md
---

# Relational Algebra, JOINs & Security Policies
*Relational Algebra, JOINs & Security Policies*

---

## Table of Contents
*Table of Contents*

1. [Introduction](#introduction)
2. [Cartesian Product](#cartesian-product)
3. [Natural Join](#natural-join)
4. [The Join Operation (JOIN)](#the-join-operation-join)
   - [Theta Join ($\theta$-Join)](#theta-join--join)
   - [Equality Join (Equi-Join)](#equality-join-equi-join)
   - [Inner Join](#inner-join)
   - [Outer Join](#outer-join)
5. [Nested Queries](#nested-queries)
6. [Security Threats & Cybersecurity](#security-threats--cybersecurity)
   - [Password Cracking](#password-cracking)
   - [Social Engineering](#social-engineering)
7. [Information Security Policies](#information-security-policies)
   - [Software Security](#software-security)
   - [Data Security](#data-security)
   - [Security Policy for Passwords](#security-policy-for-passwords)
8. [Summary Table of Key Concepts](#summary-table-of-key-concepts)
9. [Key Takeaways](#key-takeaways)
10. [Solved Exercises](#solved-exercises)
11. [Exam Tip: JOIN Mechanics & Safety Policies](#exam-tip-join-mechanics--safety-policies)

---

## Introduction

This document covers the advanced operations of **Relational Algebra**, focusing on the **Cartesian Product**, the **Natural Join**, and the various forms of **JOINs** in SQL. Furthermore, it examines the fundamental concepts of **Information Systems Security**, the methods of **Password Cracking**, the threat of **Social Engineering**, and the importance of **Security Policies** for safeguarding data. These concepts link the mathematical theory of databases with practical query design and security in real-world environments.

---

## Cartesian Product
*Cartesian Product*

The **Cartesian Product**, denoted by $R \times S$, is a binary operation of relational algebra that combines every tuple of a relation $R$ with every tuple of a relation $S$. The schema of the output relation includes all the attributes of both relations.

**Analogy**: It is similar to a restaurant menu that includes $3$ appetizers and $4$ main courses. The "everything-with-everything" combination produces $12$ possible meal choices, regardless of whether they match well in taste.

**Basic rules**:
- If relation $R$ has cardinality $|R| = m$ and relation $S$ has cardinality $|S| = n$, the result $R \times S$ will have $m \times n$ tuples.
- If an attribute-name conflict arises (e.g., the column `cust_name` in both tables), it is resolved by using the full relation name as a prefix: `Customer.cust_name` and `Deposit.cust_name`.

```text
Cartesian Product Schema:
Customer(cust_name, street, cust_city)   X   Deposit(br_name, acc_number, cust_name, balance)
  |
  v
Result(Customer.cust_name, street, cust_city, br_name, acc_number, Deposit.cust_name, balance)
```

| Characteristic | Cartesian Product |
|:---|:---|
| **Symbol** | $\times$ |
| **SQL Implementation** | `CROSS JOIN` or `FROM Table1, Table2` |
| **Cardinality** | $|R| \times \|S\|$ |
| **Duplicate Columns** | Both are retained with a table prefix |

---

## Natural Join
*Natural Join*

The **Natural Join**, denoted by $R \bowtie S$, joins two relations by automatically using equality on all common attributes (columns with the same name). In the result, the common column appears only once, avoiding duplication.

**Analogy**: It is like matching puzzle pieces. If we have a card with book details and a card with author details, we connect them only if the author's name matches exactly, discarding the unrelated cards.

**Mathematical Definition**:
$$
R \bowtie S = \sigma_{R.A_1 = S.A_1 \land \dots \land R.A_k = S.A_k}(R \times S)
$$
where $A_1, \dots, A_k$ are the common attributes of relations $R$ and $S$.

```text
Natural Join Schema:
R(A, B)   bowtie   S(B, C)
  |
  v
Result(A, B, C)  <-- The common attribute B appears only once
```

```sql
-- Natural Join in SQL
SELECT * 
FROM Customer 
NATURAL JOIN Deposit;
```

---

## The Join Operation (JOIN)
*The Join Operation*

The **Join** is the most frequently used table-combining operation. It allows specifying explicit join conditions, which may be based on equality or other comparison operators.

---

### Theta Join ($\theta$-Join)
*Theta Join*

The **Theta Join**, denoted by $R \bowtie_{\theta} S$, is the most general form of join. It combines tuples from $R$ and $S$ for which a general condition $\theta$ holds. This condition can involve operators such as $=, >, <, \neq, \geq, \leq$.

**Mathematical Definition**:
$$
R \bowtie_{\theta} S = \sigma_{\theta}(R \times S)
$$

---

### Equality Join (Equi-Join)
*Equi-Join*

The **Equi-Join** is a special case of the Theta Join where the condition $\theta$ involves exclusively equality operators ($=$). Unlike the natural join, the equi-join retains both join columns in the final result.

```sql
-- Equi-Join in SQL
SELECT * 
FROM Customer 
JOIN Deposit ON Customer.cust_name = Deposit.cust_name;
```

---

### Inner Join
*Inner Join*

The term `JOIN` in SQL is shorthand for the **Inner Join**. It returns only the records that have a matching value in both tables based on the `ON` condition.

**Analogy**: Given a list of students and a list of lab registrations, an Inner Join will return only the students who are registered in at least one lab.

```sql
-- Inner Join in SQL with ON
SELECT Customer.cust_name, Borrow.amount
FROM Customer
INNER JOIN Borrow ON Customer.cust_name = Borrow.cust_name;
```

---

### Outer Join
*Outer Join*

The **Outer Join** allows keeping the tuples that have no match in the joined relation, filling the empty fields with the value `NULL`.

#### Left Outer Join ($\⟕$)
It retains all the tuples of the left relation. If there is no match on the right, the right-side columns are filled with `NULL`.

```sql
SELECT * 
FROM Customer 
LEFT OUTER JOIN Deposit ON Customer.cust_name = Deposit.cust_name;
```

#### Right Outer Join ($\⟖$)
It retains all the tuples of the right relation. If there is no match on the left, the left-side columns are filled with `NULL`.

```sql
SELECT Borrow.loan_number, Borrow.amount, Customer.cust_name 
FROM Borrow 
RIGHT OUTER JOIN Customer ON Borrow.cust_name = Customer.cust_name;
```

---

### Comparative Table of JOIN Types

| JOIN Type | Join Condition | Common Column Retention | Unmatched Rows |
|:---|:---|:---|:---|
| **Theta Join ($\bowtie_{\theta}$)** | Any ($=, >, <, \dots$) | Yes (Duplicate columns) | No |
| **Equi-Join** | Only equality ($=$) | Yes (Duplicate columns) | No |
| **Natural Join ($\bowtie$)** | Automatic equality of common columns | No (Column merging) | No |
| **Left Outer Join ($\⟕$)** | Any equality condition | Yes (Duplicate columns) | Yes (From the left table) |
| **Right Outer Join ($\⟖$)** | Any equality condition | Yes (Duplicate columns) | Yes (From the right table) |

---

## Nested Queries
*Nested Queries*

Often, using a table join is not necessary, as the information can be retrieved with **Nested Queries (Subqueries)**. A subquery executes internally and returns a list of values used by the outer query (usually with the `IN` operator).

**Analogy**: It is like searching for books by specific authors. First, we run the inner search to find the IDs of authors born in Athens, and then we use that list to retrieve their books.

```sql
-- Nested query in SQL
SELECT acc_no 
FROM Deposit
WHERE br_name IN (
    SELECT br_name 
    FROM branch 
    WHERE Br_city = 'Athens'
);
```

---

## Security Threats & Cybersecurity
*Security Threats & Cybersecurity*

A **Threat** is defined as any event or action that can lead to loss, data destruction, or physical damage to the infrastructure of an Information System (IS).

**Categories of Threats**:
1. **Natural Disasters**: Fires, floods, earthquakes.
2. **Accidental Threats**: Human errors, hardware failure.
3. **Deliberate (Non-Physical) Threats**: Malicious software (Malware), DoS attacks, Phishing, etc.

---

### Password Cracking
*Password Cracking*

**Password Cracking** is the process of gaining unauthorized access by finding or decrypting passwords.

**Cracking techniques**:
- **Dictionary Attack**: Use of a predefined list of common words to compare against the hashes of the passwords.
- **Brute Force Attack**: Trying all possible combinations of characters and symbols using algorithms.
- **Rainbow Table Attack**: Use of pre-computed mapping tables (pre-computed hashes) to find the original value of a hash (e.g., MD5).
- **Guess**: Trying obvious passwords (e.g., `admin`, `123456`, `password`).
- **Spidering**: Collecting information from the company's websites and social networks to build targeted word lists.

| Technique | Mechanism | Advantage | Disadvantage |
|:---|:---|:---|:---|
| **Dictionary** | Testing ready-made words | Fast execution | Fails on random passwords |
| **Brute Force** | Testing all combinations | Guaranteed result | Requires enormous time |
| **Rainbow Table** | Search in pre-computed hashes | Almost instantaneous discovery | Requires enormous storage space |

---

### Social Engineering
*Social Engineering*

**Social Engineering** is the art of manipulating and deceiving the users of a system in order to extract confidential information (e.g., passwords).

**Analogy**: It is like a con artist pretending to be a technician from the water company to get into your house, instead of trying to break the door lock.

**The Social Engineering Cycle**:
```text
  +--------------------------------+
  |  1. Information Gathering      | (Gather Info)
  +--------------------------------+
                  |
                  v
  +--------------------------------+
  |    2. Plan Attack              | (Plan Attack)
  +--------------------------------+
                  |
                  v
  +--------------------------------+
  |    3. Acquire Tools            | (Acquire Tools)
  +--------------------------------+
                  |
                  v
  +--------------------------------+
  |          4. Attack             | (Attack)
  +--------------------------------+
                  |
                  v
  +--------------------------------+
  |  5. Use Acquired Knowledge     | (Use Knowledge)
  +--------------------------------+
```

**Common techniques**:
- **Phishing**: Sending fake emails that mimic trusted organizations to steal credentials.
- **Tailgating**: Physical entry into a secured area by closely following an authorized employee.
- **Familiarity Exploit**: Developing friendly relations with the victim before the attack.
- **Intimidating Circumstances**: Using threats or intimidation to coerce the user into providing information.
- **Exploiting Human Curiosity/Greed**: Luring users with promises of money or deliberately leaving infected USB flash drives in common areas.

---

## Information Security Policies
*Information Security Policies*

A **Security Policy** is a formal document that includes rules, guidelines, procedures, and roles for protecting an organization's Information Systems.

---

### Software Security
- Prohibition of installing software without a license or the security officer's approval.
- Software modifications must first be performed in a staging environment and then in production.
- Mandatory installation of anti-malware software on servers and workstations.
- Immediate isolation and cleaning of workstations in case of infection.

---

### Data Security
- Prohibition of sending unencrypted data over the internet.
- Maintaining regular backups and storing them in a safe, physically protected location.
- Protecting the physical storage media that contain confidential data.

---

### Security Policy for Passwords
- **Characteristics of a strong password**:
  - Length of at least $15$ characters.
  - Use of uppercase, lowercase, numbers, and symbols.
  - Must not be a dictionary word in any language and must not be based on personal information.
  - Must not be stored online or in plain-text files.
- **Management rules**:
  - Change of user passwords at least every $6$ months.
  - Prohibition of sharing passwords for accounts with high privileges.
  - Prohibition of disclosing a password by phone, email, to supervisors, colleagues, or security forms.

---

## Summary Table of Key Concepts
*Summary Table of Key Concepts*

| Concept | Definition | Critical Rule / Characteristic |
|:---|:---|:---|
| **Cartesian Product ($R \times S$)** | Combination of all tuples of $R$ with those of $S$ | Produces $\|R\| \times \|S\|$ records |
| **Natural Join ($R \bowtie S$)** | Join based on equality of common attributes | Merges the common columns into one |
| **Theta Join ($R \bowtie_{\theta} S$)** | Join based on a general condition $\theta$ | Implemented as $\sigma_{\theta}(R \times S)$ |
| **Left Outer Join ($\⟕$)** | Join that retains all left-side elements | Fills unmatched right-side entries with `NULL` |
| **Right Outer Join ($\⟖$)** | Join that retains all right-side elements | Fills unmatched left-side entries with `NULL` |
| **Threat** | Event that causes loss/damage to the IS | Can be natural, accidental, or deliberate |
| **Dictionary Attack** | Cracking attack with predefined words | Based on ready-made password dictionaries |
| **Social Engineering** | Manipulation of users to extract passwords | Exploits human trust/ignorance |
| **Security Policy** | Set of rules for protecting the IS | Constitutes a legal and operational obligation |

---

## Key Takeaways
*Key Takeaways*

- The **Cartesian Product** combines all elements of two tables, producing a large relation with duplicate columns.
- The **Natural Join** automatically performs an equality check on the common fields and retains the common column only once.
- **Outer Joins** prevent information loss for records without a match by introducing `NULL` values.
- **Nested Queries** offer an alternative method of data retrieval without using explicit joins.
- **Information Security** is threatened both by technical methods (Password Cracking) and by human weaknesses (Social Engineering).
- **Security Policies** must be strictly enforced at the software, data, and password-management levels (minimum 15 characters, change every 6 months).

---

## Solved Exercises

### Exercise 1: Cartesian Product Calculation
**Problem:**
The relations $R$ (Customers) and $S$ (Deposits) are given:
$$
R = \{ (\text{'Petrou'}, \text{'Athens'}), (\text{'Pavlou'}, \text{'Larisa'}) \}
$$
$$
S = \{ (1100, \text{'Petrou'}), (756, \text{'Pavlou'}) \}
$$
Compute the Cartesian Product $R \times S$ and draw the output table.

**Solution:**
1. We determine the schemas of the relations:
   - $R(\text{cust\_name}, \text{cust\_city})$
   - $S(\text{acc\_no}, \text{cust\_name})$
2. The schema of the result will be:
   - $Result(R.\text{cust\_name}, \text{cust\_city}, \text{acc\_no}, S.\text{cust\_name})$
3. We combine each row of $R$ with each row of $S$ (in total $2 \times 2 = 4$ rows):
   - Row 1: $(\text{'Petrou'}, \text{'Athens'})$ with $(1100, \text{'Petrou'})$
   - Row 2: $(\text{'Petrou'}, \text{'Athens'})$ with $(756, \text{'Pavlou'})$
   - Row 3: $(\text{'Pavlou'}, \text{'Larisa'})$ with $(1100, \text{'Petrou'})$
   - Row 4: $(\text{'Pavlou'}, \text{'Larisa'})$ with $(756, \text{'Pavlou'})$

*Result table:*
| R.cust_name | cust_city | acc_no | S.cust_name |
|:---|:---|:---|:---|
| Petrou | Athens | 1100 | Petrou |
| Petrou | Athens | 756 | Pavlou |
| Pavlou | Larisa | 1100 | Petrou |
| Pavlou | Larisa | 756 | Pavlou |

---

### Exercise 2: Natural Join Application
**Problem:**
Using the relations $R$ and $S$ from Exercise 1, compute the Natural Join $R \bowtie S$.

**Solution:**
1. We identify the common attribute of the two tables, which is `cust_name`.
2. From the Cartesian Product of Exercise 1, we keep only the rows where $R.\text{cust\_name} = S.\text{cust\_name}$:
   - Line 1: $\text{'Petrou'} = \text{'Petrou'}$ (Accepted)
   - Line 2: $\text{'Petrou'} \neq \text{'Pavlou'}$ (Rejected)
   - Line 3: $\text{'Pavlou'} \neq \text{'Petrou'}$ (Rejected)
   - Line 4: $\text{'Pavlou'} = \text{'Pavlou'}$ (Accepted)
3. We merge the common column `cust_name` into one.

*Result table:*
| cust_name | cust_city | acc_no |
|:---|:---|:---|
| Petrou | Athens | 1100 |
| Pavlou | Larisa | 756 |

---

### Exercise 3: Equi-Join SQL Translation
**Problem:**
Write the SQL query that performs the equi-join of the tables `Customer(cust_name, cust_city)` and `Deposit(acc_no, cust_name)` on the column `cust_name`, and show the structure of the result.

**Solution:**
1. The SQL query uses the `JOIN ... ON ...` syntax:
```sql
SELECT * 
FROM Customer 
JOIN Deposit ON Customer.cust_name = Deposit.cust_name;
```
2. The output retains both `cust_name` columns of the tables.

*Result table:*
| Customer.cust_name | cust_city | acc_no | Deposit.cust_name |
|:---|:---|:---|:---|
| Petrou | Athens | 1100 | Petrou |
| Pavlou | Larisa | 756 | Pavlou |

---

### Exercise 4: Left Outer Join Computation
**Problem:**
The following tables are given:
- `Customer(cust_name, cust_city)` with records: `('Petrou', 'Athens')`, `('Pavlou', 'Larisa')`, `('Antonis', 'Thessaloniki')`
- `Deposit(acc_no, cust_name)` with records: `(1100, 'Petrou')`, `(756, 'Pavlou')`

Compute the Left Outer Join of the tables `Customer` and `Deposit` on the column `cust_name`.

**Solution:**
1. The Left Outer Join retains all the records of the left table (`Customer`).
2. For the records `Petrou` and `Pavlou` there is a match in the `Deposit` table, so they are filled in normally.
3. For the record `Antonis` there is no corresponding record in `Deposit`. Consequently, the `Deposit` fields (`acc_no`, `Deposit.cust_name`) take the value `NULL`.

*Result table:*
| Customer.cust_name | cust_city | acc_no | Deposit.cust_name |
|:---|:---|:---|:---|
| Petrou | Athens | 1100 | Petrou |
| Pavlou | Larisa | 756 | Pavlou |
| Antonis | Thessaloniki | NULL | NULL |

---

### Exercise 5: Multiple Table Join Query
**Problem:**
The following tables are given:
- `Customer(cust_name, cust_city)`
- `Deposit(acc_no, br_name, cust_name, balance)`
- `Branch(br_name, br_city)`

Write an SQL query to find the names of customers and their balances who have a deposit in a branch located in a **different** city from their city of residence.

**Solution:**
1. We must join the `Customer` table with `Deposit` (via `cust_name`) and the `Deposit` table with `Branch` (via `br_name`).
2. We add the filtering condition `Customer.cust_city <> Branch.br_city`.

```sql
SELECT Customer.cust_name, Deposit.balance
FROM Customer
JOIN Deposit ON Customer.cust_name = Deposit.cust_name
JOIN Branch ON Deposit.br_name = Branch.br_name
WHERE Customer.cust_city <> Branch.br_city;
```

---

### Exercise 6: Right Outer Join Analysis
**Problem:**
The tables `Borrow(loan_number, amount, cust_name)` with record `(L-101, 1000, 'Giorgos')` and `Customer(cust_name, street, cust_city)` with records `('Giorgos', 'Patision 10', 'Athens')`, `('Maria', 'Trikoupi 12', 'Patra')` are given.

Compute the result of the Right Outer Join of `Borrow` with `Customer` on the column `cust_name`.

**Solution:**
1. The Right Outer Join retains all the records of the right table (`Customer`).
2. For `Giorgos` there is a match, so it is linked to the loan `L-101`.
3. For `Maria` there is no loan in the `Borrow` table. The `loan_number` and `amount` fields are filled with `NULL`.

*Result table:*
| loan_number | amount | cust_name | street | cust_city |
|:---|:---|:---|:---|:---|
| L-101 | 1000 | Giorgos | Patision 10 | Athens |
| NULL | NULL | Maria | Trikoupi 12 | Patra |

---

### Exercise 7: Nested Subquery Translation
**Problem:**
Convert the following join (JOIN) query into an equivalent query using a nested subquery:
```sql
SELECT DISTINCT Deposit.cust_name
FROM Deposit
JOIN Branch ON Deposit.br_name = Branch.br_name
WHERE Branch.br_city = 'Athens';
```

**Solution:**
1. The inner query (subquery) must retrieve the names of the branches (`br_name`) located in the city 'Athens'.
2. The outer query will select the names of customers from the `Deposit` table whose branch is included in the subquery's list.

```sql
SELECT DISTINCT cust_name
FROM Deposit
WHERE br_name IN (
    SELECT br_name
    FROM Branch
    WHERE br_city = 'Athens'
);
```

---

### Exercise 8: Natural Join vs. Theta Join Equivalence
**Problem:**
Prove mathematically using relational algebra that the Natural Join $R \bowtie S$ for the relations $R(A, B)$ and $S(B, C)$ is equivalent to a projection operation over a Theta Join.

**Solution:**
1. The Theta Join with an equality condition on the common attribute $B$ is defined as:
   $$ R \bowtie_{R.B = S.B} S = \sigma_{R.B = S.B}(R \times S) $$
   This relation has the attributes $(A, R.B, S.B, C)$.
2. The Natural Join $R \bowtie S$ has the attributes $(A, B, C)$, where the duplicate $B$ column has been merged.
3. To make the two expressions identical, we apply projection ($\pi$) to the result of the Theta Join to discard one of the two $B$ columns (e.g., $S.B$) and rename the other to $B$:
   $$ R \bowtie S = \pi_{A, R.B \text{ AS } B, C}(\sigma_{R.B = S.B}(R \times S)) $$
   Therefore, the Natural Join is a specialized form of Theta Join followed by a projection.

---

## Exam Tip: JOIN Mechanics & Safety Policies

> **[Key Insight]**
> **Exam Tip - JOINs**: In exams, when the difference between `NATURAL JOIN` and `JOIN ... ON` (Equi-join) is asked:
> 1. `NATURAL JOIN` automatically merges columns with the same name and returns the common column **only once**.
> 2. `JOIN ... ON` retains **both columns** in the result, adding the table name as a prefix. If the conversion of a natural join into a general join is requested, an explicit projection (`SELECT`) of the individual columns must be used to avoid duplication.
> 
> **Exam Tip - Security Policies**: In theory questions about password security, remember the following "golden rules":
> - Minimum password length: **15 characters** (not 8 or 10).
> - Change frequency: **Every 6 months** (at least).
> - **Entity Integrity** concerns exclusively the Primary Key (not NULL), while **Referential Integrity** concerns the Foreign Key (it must point to an existing record). Do not confuse them!

