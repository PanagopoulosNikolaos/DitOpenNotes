
# Lecture 1 db.md
========================================================================================================================
# Introduction to Databases

This lecture introduces the fundamental concepts of databases and Database Management Systems (DBMS). It covers the evolution from traditional file systems to modern database architectures, explores different data types, and defines the core components of information systems and the relational model.

---

## 1. Core Definitions: Data, Information, and Knowledge

Understanding the distinction between data, information, and knowledge is foundational to the study of databases.

### 1.1. Data (Δεδομένα)
Data represents raw, unprocessed facts, quantities, characters, or symbols. 
*   **Formal Definition:** Invariants with potential meaning for someone who can interpret them.
*   **Characteristics:** Non-processed form, can be numbers, words, images, or records of observations.

### 1.2. Information (Πληροφορία)
Information is the result of processing data to make it understandable and useful for decision-making.
*   **Transformation:** $Data \xrightarrow{Processing} Information$.
*   **Goal:** To provide context and meaning to raw data.

### 1.3. Knowledge (Γνώση)
Knowledge is information that has been internalized and transformed into the capability for effective action.
*   **Context:** It involves interpretation, experience, and wisdom.
*   **Formal Definition:** "Information transformed into a capability for effective action" (Nonaka & Takeuchi, 1995).

---

## 2. Data Types and Forms

Data can be categorized based on its structure and volume.

### 2.1. Structural Categorization
| Category | Description | Examples |
| :--- | :--- | :--- |
| **Structured Data** | Organized in predefined fields and tables. | Databases, Excel sheets (strict). |
| **Semi-structured Data** | Has some structure but not rigid table form. | XML, HTML, JSON, Emails. |
| **Unstructured Data** | No specific format or organization. | Videos, Images, Text documents. |

### 2.2. Big Data
Big Data refers to extremely large datasets that exceed the processing capacity of traditional database systems.
*   **Origin:** The term was first used by NASA in 1997.
*   **Scale:** Measured in Terabytes (TB), Petabytes (PB), Exabytes (EB), and Zettabytes (ZB).
*   **Insight:** Used to reveal patterns, trends, and associations, especially in human behavior.

---

## 3. Information Systems (Πληροφοριακά Συστήματα)

An Information System (IS) is an organized set of components that interact to produce and manage information.

### 3.1. Five Core Components
1.  **People (Άνθρωποι):** Users, administrators, and developers.
2.  **Data (Δεδομένα):** The raw material processed by the system.
3.  **Software (Λογισμικό):** Programs that process the data.
4.  **Hardware (Υλικό):** Physical devices (servers, PCs, storage).
5.  **Processes (Διαδικασίες):** Steps taken to achieve a specific goal.

---

## 4. Evolution: From File Systems to Databases

Before DBMS, data was managed using simple text files (e.g., CSV). This approach had significant limitations.

### 4.1. Problems with File Systems
*   **Data Isolation (Απομόνωση):** Data is scattered in different files, making access difficult.
*   **Data Redundancy (Πλεονασμός):** The same information is stored multiple times in different files.
*   **Data Inconsistency (Ασυνέπεια):** Redundancy leads to conflicting information if one file is updated and another is not.

### 4.2. Database Management System (DBMS)
A DBMS is software that allows for the creation, management, storage, and retrieval of data in a database.
*   **Examples:** MySQL, PostgreSQL, Oracle Database, Microsoft SQL Server.
*   **Key Advantage:** Centralized control, reduction of redundancy, and improved data integrity.

---

## 5. The Relational Model Basics

The Relational Model organizes data into tables (relations).

### 5.1. Entities and Attributes
*   **Entity (Οντότητα):** An object or concept of interest for which we store data (e.g., STUDENT, COURSE).
*   **Attribute (Γνώρισμα):** A property or characteristic of an entity (e.g., Name, StudentID).

### 5.2. Relationships
Relationships define how entities are connected.
*   **One-to-Many (1:N):** One entity instance relates to many instances of another (e.g., one Student can have many Grades).

### 5.3. Metadata
Metadata is "data about data." It describes the structure, types, and constraints of the stored data.
*   **Examples:** Field names, data types (Integer, String), and character length limits.

---

## 6. Database Design Lifecycle

Designing a database involves several distinct phases:
1.  **Requirement Collection:** Defining user needs and functional requirements.
2.  **Conceptual Modeling:** Creating an Entity-Relationship (ER) diagram.
3.  **Logical Design:** Mapping the ER diagram to a Relational Model (tables).
4.  **Implementation:** Defining relations in SQL and inserting data.
5.  **Security Measures:** Designing security policies.

---

## Solved Exercises

### Exercise 1: Distinguishing Data and Information
**Problem:** Identify which of the following are Data and which are Information:
1. A list of temperatures: 22, 25, 19.
2. A graph showing that sales increased by 10% in May.
3. The string "John Doe".

**Solution:**
1. **Data:** Raw numbers without context.
2. **Information:** Processed data showing a trend.
3. **Data:** A raw name.

### Exercise 2: Categorizing Structure
**Problem:** Categorize the following as Structured, Semi-structured, or Unstructured:
1. A MySQL table of employees.
2. A YouTube video.
3. An XML configuration file.

**Solution:**
1. **Structured:** Organized in tables.
2. **Unstructured:** Media file with no fixed field structure.
3. **Semi-structured:** Has tags and hierarchy but isn't a flat table.

### Exercise 3: Identifying IS Components
**Problem:** In a library system, identify the five components of the Information System.

**Solution:**
1. **People:** Librarians and members.
2. **Data:** Book titles, authors, member details.
3. **Software:** The library management application.
4. **Hardware:** The computer at the desk and the barcode scanner.
5. **Processes:** The steps for borrowing a book.

### Exercise 4: File System Limitations
**Problem:** A company stores employee addresses in both the "Payroll" file and the "Insurance" file. What problem does this illustrate?

**Solution:**
*   **Problem:** Data Redundancy (Πλεονασμός). 
*   **Consequence:** If the employee moves and only the Payroll file is updated, it leads to **Data Inconsistency (Ασυνέπεια)**.

### Exercise 5: Entity and Attributes
**Problem:** Define an entity for a "Car" and list four potential attributes.

**Solution:**
*   **Entity:** CAR
*   **Attributes:**
    1. LicensePlate (String)
    2. Model (String)
    3. Year (Integer)
    4. Color (String)

### Exercise 6: One-to-Many Relationship
**Problem:** Describe a 1:N relationship between "Department" and "Employee".

**Solution:**
*   **Relationship:** One Department can have many Employees.
*   **Direction:** One-to-Many ($1:N$).
*   **Logic:** Every employee belongs to exactly one department, but a department hosts multiple employees.

### Exercise 7: Metadata Identification
**Problem:** Given a table column `Age (Integer, Range: 0-120)`, identify the metadata.

**Solution:**
*   **Name:** Age
*   **Type:** Integer
*   **Constraint:** Range 0-120

### Exercise 8: Database Design Steps
**Problem:** What is the result of the "Logical Design" phase?

**Solution:**
*   **Result:** The translation of the Conceptual Model (ER Diagram) into the Relational Model (specific tables, columns, and relations).

---

## Exam Tip: Common Pitfalls in Definitions

> **[Key Insight]**
> Many students confuse **Data Redundancy** with **Data Inconsistency**. 
> *   **Redundancy** is the *act* of storing the same data twice.
> *   **Inconsistency** is the *result* of having conflicting values for that data due to redundant storage.
> In exams, remember that Redundancy *leads to* Inconsistency.

========================================================================================================================

# Lecture 2 db.md
========================================================================================================================
# Database Environment and Architecture

This lecture explores the structural and operational environment of Database Management Systems (DBMS). It covers the three-schema architecture for data abstraction, transaction management (ACID properties), concurrency control, and the different roles involved in a database system.

---

## 1. The Three-Schema Architecture

The primary goal of a database system is to hide the complexity of data storage from the users through levels of abstraction.

### 1.1. Levels of Abstraction
1.  **Physical Level (Φυσικό επίπεδο):** The lowest level of abstraction. It describes *how* the data is actually stored on the physical media (e.g., file structures, indices, block sizes).
2.  **Conceptual Level (Εννοιολογικό επίπεδο):** The intermediate level. It describes *what* data is stored in the database and what relationships exist between them. This is the level where the Database Administrator (DBA) and designers operate.
3.  **External/View Level (Εποπτικό επίπεδο):** The highest level of abstraction. It describes only part of the database relevant to a specific user group. Each user group sees a "view" of the database, hiding irrelevant complexity.

### 1.2. Data Independence
Data independence is the ability to modify the schema at one level without affecting the schema at a higher level.
*   **Logical Data Independence:** Modifying the conceptual schema without needing to change external schemas or applications.
*   **Physical Data Independence:** Modifying the physical schema (e.g., changing storage devices) without needing to change the conceptual schema.

---

## 2. Transactions and Concurrency Control

A DBMS must ensure that data remains consistent even when multiple users access it simultaneously or if the system crashes.

### 2.1. Transaction (Συναλλαγή)
A transaction is an atomic sequence of database actions (read/write).
*   **Atomicity:** The "all or nothing" principle. A transaction must be completed entirely or not at all.
*   **Log Files (Log):** The DBMS maintains a log file recording all actions. It stores "old" and "new" values to allow for recovery (Undo/Redo) in case of failure.

### 2.2. Concurrency Control
Concurrency allows multiple users to access data at the same time.
*   **Serializability:** The DBMS ensures that the final result of concurrent transactions is equivalent to running them one after another (sequentially).
*   **Locking (Κλείδωμα):** A transaction must request a lock on a data item before accessing it. Locks are released upon completion.
*   **Deadlock (Αδιέξοδο):** A situation where two or more transactions are waiting for each other to release locks. The DBMS must detect this and abort one of the transactions.

---

## 3. Database Languages: SQL Components

SQL (Structured Query Language) is divided into specialized sub-languages based on the operation performed.

### 3.1. Data Definition Language (DDL)
Used to define the database structure (schema).
*   **Function:** Creates tables, defines data types, and sets constraints.
*   **Storage:** DDL statements are compiled into a **Data Dictionary** (or Metadata catalog).

### 3.2. Data Manipulation Language (DML)
Used for accessing and manipulating the data within the defined structure.
*   **Operations:** Retrieval (Select), Insertion (Insert), Deletion (Delete), and Modification (Update).
*   **Note:** Also referred to as a Query Language.

---

## 4. User Roles in a Database System

| Role | Responsibility |
| :--- | :--- |
| **Database Administrator (DBA)** | Managing access, security, performance, and maintenance. |
| **Database Designer** | Defining the structure (entities, relationships) and user views. |
| **Naive Users** | Interact via pre-built applications (e.g., bank tellers). |
| **Casual Users** | Use SQL queries to perform ad-hoc analysis. |
| **Analysts/Programmers** | Develop the applications that interface with the database. |

---

## Solved Exercises

### Exercise 1: Mapping Schema Levels
**Problem:** A user logs into a banking app and sees only their account balance. Which level of the three-schema architecture are they interacting with?

**Solution:**
*   **Answer:** External/View Level (Εποπτικό επίπεδο).
*   **Reason:** The user sees a specific subset of data (their balance) tailored to their role, while the complexity of other accounts and the physical storage is hidden.

### Exercise 2: Physical Data Independence
**Problem:** If the DBA moves the database from a Hard Disk Drive (HDD) to a Solid State Drive (SSD), does the SQL code of the applications need to change? Why?

**Solution:**
*   **Answer:** No.
*   **Reason:** This is due to **Physical Data Independence**. Changes at the physical storage level do not affect the conceptual or external levels.

### Exercise 3: Transaction Atomicity
**Problem:** During a bank transfer, \$100 is deducted from Account A, but the system crashes before adding it to Account B. What should the DBMS do?

**Solution:**
*   **Answer:** The DBMS must perform a **Rollback**.
*   **Reason:** According to the principle of **Atomicity**, if the entire transaction cannot complete, all its partial changes must be undone using the log file.

### Exercise 4: Identifying DDL vs. DML
**Problem:** Classify the following actions as DDL or DML:
1. Creating a new table named `Students`.
2. Changing a student's phone number in the database.
3. Adding a new column `Email` to the `Faculty` table.
4. Deleting a record of a retired professor.

**Solution:**
1. **DDL:** Defines structure.
2. **DML:** Manipulates data.
3. **DDL:** Modifies structure (schema).
4. **DML:** Deletes data.

### Exercise 5: Deadlock Resolution
**Problem:** Transaction T1 holds a lock on Resource A and waits for Resource B. Transaction T2 holds a lock on Resource B and waits for Resource A. What is this state called, and how is it resolved?

**Solution:**
*   **State:** Deadlock (Αδιέξοδο).
*   **Resolution:** The DBMS aborts one of the transactions (e.g., T1), releases its locks, and allows the other (T2) to proceed. The aborted transaction is then restarted.

### Exercise 6: Metadata and Data Dictionary
**Problem:** Where does the DBMS look to find out if the "Salary" column in the "Employees" table is an Integer or a Decimal?

**Solution:**
*   **Answer:** The Data Dictionary (or Data Catalog).
*   **Reason:** The Data Dictionary stores **Metadata**, which includes the definitions of all schemas and data types.

---

## Exam Tip: Schema vs. Instance

> **[Key Insight]**
> Understand the temporal difference between a Schema and an Instance:
> *   **Schema (Σχήμα):** The static design. It changes very rarely (e.g., once a year during a system upgrade).
> *   **Instance/Snapshot (Στιγμιότυπο):** The dynamic state. It changes every second as data is inserted or updated.
> In exams, if a question asks about "the state of the database at 10:00 AM," it refers to the **Instance**.

========================================================================================================================

# Lecture 3 db.md
========================================================================================================================
# Conceptual Design and the Entity-Relationship Model

This lecture focuses on Conceptual Database Design using the Entity-Relationship (ER) model. It covers the fundamental building blocks of data modeling: entities, attributes, and relationships, along with their constraints and representations.

---

## 1. Introduction to the ER Model

The Entity-Relationship (ER) model is a high-level conceptual data model. It was proposed by **Peter Chen in 1976** to provide a unified view of data.

### 1.1. Core Components
*   **Entities (Οντότητες):** Objects or concepts with independent existence. They can be physical (e.g., a person, a car) or conceptual (e.g., a university course, a bank transaction).
*   **Attributes (Γνωρίσματα):** Properties that describe an entity.
*   **Relationships (Συσχετίσεις):** Associations between two or more entities.

---

## 2. Classification of Attributes

Attributes provide the detailed description of entities. They are categorized based on their complexity and nature.

### 2.1. Structural Classification
*   **Simple (Απλά):** Cannot be divided into smaller parts (e.g., Age, Gender).
*   **Composite (Σύνθετα):** Can be divided into sub-parts (e.g., Address can be split into Street, City, ZIP).
*   **Single-valued (Μονότιμα):** Hold a single value for an entity instance (e.g., Social Security Number).
*   **Multi-valued (Πλειότιμα):** Can hold multiple values (e.g., a person can have multiple Phone Numbers or favorite Colors). Represented in braces `{...}`.
*   **Derived (Παραγόμενα):** Their value is calculated from other attributes (e.g., Age derived from DateOfBirth).
*   **Stored (Αποθηκευμένα):** The base attributes used to calculate derived ones.

### 2.2. Null Values
A **Null** value indicates that an attribute is not applicable or its value is unknown for a specific entity instance.

---

## 3. Relationships and Constraints

Relationships define how entities interact within the system.

### 3.1. Degree of Relationship (Βαθμός Συσχέτισης)
*   **Unary (Recursive):** A relationship between instances of the same entity type (e.g., an Employee *manages* other Employees).
*   **Binary:** A relationship between two different entity types (e.g., Student *enrolled in* Course). Most common type.
*   **Ternary:** A relationship involving three entity types (e.g., Professor *teaches* Student in a specific Classroom).

### 3.2. Cardinality Ratio (Λόγος Πληθικότητας)
Describes the maximum number of relationship instances that an entity can participate in.
*   **One-to-One (1:1):** Each instance of A relates to at most one instance of B (e.g., Manager *heads* Department).
*   **One-to-Many (1:N):** One instance of A relates to many of B, but B relates to one of A (e.g., Mother *has* Children).
*   **Many-to-Many (M:N):** Instances of both A and B can relate to multiple instances of the other (e.g., Student *registers for* Courses).

### 3.3. Participation Constraints (Συμμετοχή)
*   **Total Participation (Ολική):** Every entity instance must participate in the relationship (e.g., every Employee *must* work for a Department). Represented by a double line.
*   **Partial Participation (Μερική):** Some entity instances might not participate (e.g., not every Employee *manages* a Department).

---

## 4. Weak Entities (Ασθενείς Οντότητες)

A **Weak Entity** is an entity that does not have a primary key of its own and depends on an **Identifying Entity** (owner) for its existence.
*   **Partial Key (Μερικό Κλειδί):** An attribute that uniquely identifies weak entities related to the *same* owner instance.
*   **Representation:** Double rectangle for the entity and double diamond for the identifying relationship.

---

## 5. Keys and Identifiers

*   **Superkey:** A set of attributes that uniquely identifies an entity instance.
*   **Candidate Key:** A minimal superkey (no redundant attributes).
*   **Primary Key (Πρωτεύον Κλειδί):** The candidate key chosen by the designer to uniquely identify records. It cannot be null.
*   **Foreign Key (Ξένο Κλειδί):** An attribute in one table that points to the primary key of another table, establishing a link.

---

## Solved Exercises

### Exercise 1: Attribute Categorization
**Problem:** Categorize the following attributes for a "User" entity:
1. `FullName` (consisting of First and Last Name).
2. `EmailAddresses` (a user can have many).
3. `CurrentAge` (calculated from birth year).
4. `UserID`.

**Solution:**
1. **Composite:** Can be split.
2. **Multi-valued:** Allows multiple entries.
3. **Derived:** Calculated from another attribute.
4. **Simple/Key:** Atomic identifier.

### Exercise 2: Relationship Degree
**Problem:** Identify the degree of the following relationship: "A Project uses certain Parts supplied by specific Suppliers."

**Solution:**
*   **Answer:** Ternary ($3^{rd}$ degree).
*   **Reason:** It involves three entities: Project, Part, and Supplier.

### Exercise 3: Cardinality Ratio
**Problem:** In a library, one Book can be written by many Authors, and one Author can write many Books. What is the cardinality ratio?

**Solution:**
*   **Answer:** Many-to-Many ($M:N$).

### Exercise 4: Weak Entity Example
**Problem:** A "Dependent" (e.g., child of an employee) is stored in a corporate database. Why is "Dependent" likely a weak entity?

**Solution:**
*   **Reason:** A "Dependent" usually doesn't have a unique ID in the company's system; they are identified only through their relationship with a specific "Employee". If the employee leaves, the dependent's records are removed.

### Exercise 5: Participation Constraint
**Problem:** Every student must be assigned to at least one advisor. Is this total or partial participation?

**Solution:**
*   **Answer:** Total Participation.
*   **Reason:** Every instance of the "Student" entity is required to participate in the "AssignedTo" relationship.

### Exercise 6: Identifying Keys
**Problem:** A table `Cars` has `VIN`, `LicensePlate`, and `Color`. Which are candidate keys?

**Solution:**
*   **Answer:** `VIN` and `LicensePlate`.
*   **Reason:** Both are unique for every car. `Color` is not a key because many cars share the same color.

### Exercise 7: Composite Attribute Representation
**Problem:** How is a composite attribute like `Name(First, Last)` represented in a Chen ER diagram?

**Solution:**
*   **Answer:** An oval for `Name` connected to the entity, and two smaller ovals for `First` and `Last` connected to the `Name` oval.

### Exercise 8: Recursive Relationship
**Problem:** Define a recursive relationship for an entity `Course` where one course can be a prerequisite for another.

**Solution:**
*   **Relationship:** `Prerequisite`.
*   **Mechanism:** Both participants are from the `Course` entity set. One instance acts as the "Pre-req" and the other as the "Main Course".

---

## Exam Tip: Crow's Foot vs. Chen Notation

> **[Key Insight]**
> Be prepared to recognize different notations:
> *   **Chen Notation:** Uses diamonds for relationships and ovals for attributes. Cardinality is marked with $1$, $N$, or $M$ on the lines.
> *   **Crow's Foot Notation:** Relationships are lines with symbols at the ends (circles, bars, or "feet") to denote $0$, $1$, or "many". It is widely used in modern CASE tools.
> In exams, always check which notation is requested before drawing.

========================================================================================================================

# Lecture 4 db.md
========================================================================================================================
# Advanced ER Modeling and Case Study

This lecture provides an in-depth practical application of the Entity-Relationship (ER) model. It covers recursive relationships, relationship attributes, and a comprehensive case study of a "Project Company" to illustrate the transition from requirements to a conceptual schema.

---

## 1. Recursive Relationships (Μοναδιαία Συσχέτιση)

A recursive relationship occurs when an entity type participates more than once in a relationship type in different roles.

*   **Example:** An `Employee` entity set.
*   **Relationship:** `Supervises`.
*   **Roles:** One employee acts as the "Supervisor" (Προϊστάμενος) and others act as "Subordinates" (Υφιστάμενοι).
*   **Cardinality:** Usually $1:N$ (one supervisor manages many employees).

---

## 2. Weak Entities and Participation

Weak entities depend on another entity for identification and existence.

### 2.1. Identification Mechanism
*   **Owner Entity:** The strong entity that provides the identification (e.g., `Employee`).
*   **Identifying Relationship:** The relationship linking the weak entity to the owner (e.g., `Protects`).
*   **Partial Key:** An attribute that distinguishes weak entities belonging to the same owner (e.g., `DependentName`).

### 2.2. Participation Constraints
*   **Min/Max Notation:** $(0, 1)$ means optional participation (minimum 0, maximum 1), while $(1, N)$ means mandatory participation (minimum 1, maximum many).

---

## 3. Relationship Attributes

Attributes can sometimes belong to a relationship itself rather than to the participating entities. This is particularly common in Many-to-Many ($M:N$) relationships.

*   **Example:** `Employee` *Works_On* `Project`.
*   **Attribute:** `Hours`.
*   **Logic:** The number of hours depends on *both* which employee is working and *which* project they are working on.

---

## 4. Case Study: Project Company (Εταιρία Έργων)

A comprehensive walkthrough of designing a database for a company managing projects and employees.

### 4.1. Requirements Analysis
1.  **Departments:** Have a unique Name, Number, and Locations. Managed by one Employee (store start date).
2.  **Projects:** Controlled by a Department. Have a Name, Number, and one Location.
3.  **Employees:** Belong to one Department. Can work on multiple projects (store weekly hours). Have Name, SSN, Address, Salary, Gender, and BirthDate. Supervised by one other Employee.
4.  **Dependents:** Linked to an Employee. Store Name, Gender, BirthDate, and Relationship.

### 4.2. Identified Components
| Type | Name | Attributes |
| :--- | :--- | :--- |
| **Strong Entity** | `Employee` | **SSN**, Name(Fname, Lname), Address, Salary, Gender, Bdate. |
| **Strong Entity** | `Department` | **Number**, Name, Locations{}. |
| **Strong Entity** | `Project` | **Number**, Name, Location. |
| **Weak Entity** | `Dependent` | Name (Partial Key), Gender, Bdate, Relationship. |
| **Relationship** | `Works_For` | Employee (N) $\leftrightarrow$ Department (1). |
| **Relationship** | `Manages` | Employee (1) $\leftrightarrow$ Department (1). |
| **Relationship** | `Works_On` | Employee (M) $\leftrightarrow$ Project (N). Includes attribute: `Hours`. |
| **Relationship** | `Supervises` | Employee (1) $\leftrightarrow$ Employee (N). (Recursive). |

---

## Solved Exercises

### Exercise 1: Recursive Cardinality
**Problem:** Draw the $1:N$ recursive relationship "Supervises" for the `Employee` entity. Who is on the "1" side?

**Solution:**
*   **Answer:** The "Supervisor" role is on the "1" side.
*   **Reason:** In a standard hierarchy, one supervisor can manage many subordinates ($N$), but each subordinate has only one direct supervisor ($1$).

### Exercise 2: Relationship Attributes
**Problem:** In the relationship `Student` *Takes* `Exam`, where should the `Grade` attribute be placed?

**Solution:**
*   **Answer:** On the `Takes` relationship.
*   **Reason:** The grade doesn't belong solely to the student (they have many grades) nor to the exam (many students take it). It belongs to the specific instance of a student taking a specific exam.

### Exercise 3: Weak Entity Key Formation
**Problem:** How is a `Dependent` record uniquely identified in the final implementation?

**Solution:**
*   **Answer:** By combining the Primary Key of the `Employee` (SSN) with the Partial Key of the `Dependent` (Name).

### Exercise 4: Multi-valued Attribute
**Problem:** A Department has "Locations" listed as a multi-valued attribute. Why?

**Solution:**
*   **Reason:** Because a single department might operate in multiple physical locations (e.g., HQ in Athens, Branch in Patras).

### Exercise 5: Total vs. Partial in Management
**Problem:** In the `Manages` relationship (Employee $\leftrightarrow$ Department), is the participation of Employee total or partial?

**Solution:**
*   **Answer:** Partial.
*   **Reason:** Only a small percentage of employees are managers. Most employees do not participate in the "Manages" relationship.

### Exercise 6: Identifying Role Names
**Problem:** When is it mandatory to use role names (Supervisor, Subordinate) in an ER diagram?

**Solution:**
*   **Answer:** In recursive relationships.
*   **Reason:** To distinguish the different functions the same entity type plays in the relationship.

### Exercise 7: Min/Max Constraint Interpretation
**Problem:** What does $(1, 1)$ participation on the Employee side of the `Works_For` relationship mean?

**Solution:**
*   **Answer:** Every employee must work for exactly one department.
*   **Min 1:** Mandatory participation.
*   **Max 1:** Cannot belong to more than one department.

### Exercise 8: Tooling for ERDs
**Problem:** What are the three outputs the ERDPlus tool can generate?

**Solution:**
1.  ER Diagrams (ERDs).
2.  Relational Schemas (Tables).
3.  SQL DDL Statements.

---

## Exam Tip: Identifying Weak Entities

> **[Key Insight]**
> To identify a **Weak Entity** in a problem description, look for phrases like:
> *   "Records are deleted if the parent record is removed."
> *   "Identified by name *within* the department/project."
> *   "Does not have a unique identifier of its own."
> When drawing, remember the **Double Line** (Total Participation) and **Double Diamond** (Identifying Relationship) required for weak entities.

========================================================================================================================

# Lecture 5 db.md
========================================================================================================================
# Conceptual Modeling: Comprehensive Exercises

This lecture is dedicated to the practical application of Entity-Relationship (ER) modeling through two complex case studies: a Hospital Information System and a Supermarket Management System. These exercises consolidate concepts like specialization, weak entities, and relationship attributes.

---

## 1. Case Study 1: Hospital Information System

### 1.1. Requirements Analysis
*   **Infrastructure:** The hospital consists of **Clinics** (e.g., Cardiology) and **Laboratories** (e.g., Biochemical). 
    *   Clinics store: Name, Director, Number of Beds, and Number of Patients.
    *   Laboratories store: Name, Director, and multiple Phone Numbers.
*   **Personnel:** Staff is divided into **Doctors**, **Nurses**, and **Paramedical Staff**.
    *   Common attributes for all staff: Name, Surname, ID Number (AT).
    *   **Doctors:** Have a specialty (e.g., Internist), Employee ID (AM), and contact info (Address, City, Email, Phone). Each doctor belongs to exactly one Clinic and one Laboratory.
    *   **Nurses:** Have a specialty and contact info. Can work in multiple clinics but *not* in laboratories.
    *   **Paramedical Staff:** Have a specialty and Tax ID (AFM). Work exclusively in exactly one Laboratory.

### 1.2. Identified ER Components
| Component Type | Name | Details |
| :--- | :--- | :--- |
| **Entity** | `Clinic` | Attributes: Name (PK), Director, Beds, Patients. |
| **Entity** | `Laboratory` | Attributes: Name (PK), Director, {Phones} (Multi-valued). |
| **Entity** | `Doctor` | Attributes: **AM** (PK), Name, Surname, AT, Specialty, Address, City, Email, Phone. |
| **Entity** | `Nurse` | Attributes: Name, Surname, AT, Specialty, Address, City, Email, Phone. |
| **Entity** | `Paramedical` | Attributes: **AFM** (PK), Name, Surname, AT, Specialty. |
| **Relationship** | `Works_In` (Doctor) | Linked to Clinic (1) and Laboratory (1). |
| **Relationship** | `Employed_By` (Nurse) | Linked to Clinic (M:N). |
| **Relationship** | `Assigned_To` (Paramedical) | Linked to Laboratory (N:1). |

---

## 2. Case Study 2: Supermarket Management System

### 2.1. Requirements Analysis
*   **Supply Chain:** **Suppliers** provide **Products**. 
    *   Suppliers: Name, Address.
    *   Products: Name, Price, Code.
    *   *Constraint:* A supplier provides many products, and a product can come from many suppliers. The price is unique to each supplier-product pair.
*   **Internal Structure:** The market has **Departments**.
    *   Departments: Name, Code. Each has one Manager and many Employees.
    *   *Constraint:* A department is responsible for specific products. A product is sold by only one department.
*   **Human Resources:** **Employees** have a Name and Salary. Each works in exactly one department.
*   **Sales:** **Customers** and **Orders**.
    *   Customers: Surname, Name, ID (PK), Address, Account Balance.
    *   Orders: Code (PK), Date.
    *   *Constraint:* Customers place orders. An order consists of a list of products and their quantities.

### 2.2. Identified ER Components
| Component Type | Name | Details |
| :--- | :--- | :--- |
| **Entity** | `Supplier` | Attributes: **Name** (PK), Address. |
| **Entity** | `Product` | Attributes: **Code** (PK), Name. |
| **Entity** | `Department` | Attributes: **Code** (PK), Name. |
| **Entity** | `Employee` | Attributes: Name, Salary. |
| **Entity** | `Customer` | Attributes: **ID** (PK), Surname, Name, Address, Balance. |
| **Entity** | `Order` | Attributes: **Code** (PK), Date. |
| **Relationship** | `Provides` | Supplier (M) $\leftrightarrow$ Product (N). Attribute: `Price`. |
| **Relationship** | `Sold_By` | Product (N) $\leftrightarrow$ Department (1). |
| **Relationship** | `Works_At` | Employee (N) $\leftrightarrow$ Department (1). |
| **Relationship** | `Manages` | Employee (1) $\leftrightarrow$ Department (1). |
| **Relationship** | `Places` | Customer (1) $\leftrightarrow$ Order (N). |
| **Relationship** | `Contains` | Order (M) $\leftrightarrow$ Product (N). Attribute: `Quantity`. |

---

## Solved Exercises

### Exercise 1: Multi-valued vs. Separate Entity
**Problem:** In the Hospital case, why are Laboratory Phone Numbers multi-valued attributes rather than a separate "Phone" entity?

**Solution:**
*   **Answer:** Because the phone numbers do not have their own attributes and do not participate in relationships with other entities. They are simple descriptive values of the Laboratory.

### Exercise 2: Relationship Attributes in M:N
**Problem:** In the Supermarket case, why is "Price" an attribute of the `Provides` relationship and not the `Product` entity?

**Solution:**
*   **Answer:** Because different suppliers may sell the same product at different prices. The price is only determined when you specify *both* the product and the supplier.

### Exercise 3: Cardinality in Sales
**Problem:** What is the cardinality between `Customer` and `Order`? Why?

**Solution:**
*   **Answer:** $1:N$ (One-to-Many).
*   **Reason:** One customer can place many orders over time, but each specific order (identified by a unique order code) belongs to exactly one customer.

### Exercise 4: Specialization/Generalization
**Problem:** If we wanted to simplify the Hospital model, could we create a "Staff" superclass? What attributes would it have?

**Solution:**
*   **Answer:** Yes. 
*   **Attributes:** Name, Surname, AT, and Specialty (since all three types share these).

### Exercise 5: Total Participation in Management
**Problem:** In the Supermarket model, every Department must have a manager. How is this represented?

**Solution:**
*   **Answer:** A double line on the Department side of the `Manages` relationship.

### Exercise 6: Identifying Relationship Attributes
**Problem:** In Case 2, where is "Quantity" stored?

**Solution:**
*   **Answer:** On the `Contains` relationship between `Order` and `Product`. 
*   **Reason:** Quantity is specific to how many of a certain product are in a specific order.

### Exercise 7: Key Choice
**Problem:** For the `Customer` entity, why is `ID` a better primary key than `Surname`?

**Solution:**
*   **Answer:** Uniqueness. Multiple customers can have the same surname (e.g., "Papadopoulos"), but an ID card number is unique to one individual.

### Exercise 8: Handling Product Sales
**Problem:** Can a product be sold by two different departments in this model?

**Solution:**
*   **Answer:** No. 
*   **Reason:** The requirements state "a product can be sold by only one department," which implies a $N:1$ relationship between Product and Department.

---

## Exam Tip: Relationship Attributes vs. Entity Attributes

> **[Key Insight]**
> When deciding where to place an attribute, ask: "Does this value depend on one entity or the combination of two?"
> *   **Example:** `EmployeeSalary` depends only on the Employee (Entity attribute).
> *   **Example:** `HoursWorked` depends on both the Employee and the Project (Relationship attribute).
> In Many-to-Many relationships, descriptive attributes almost always belong to the **Relationship**.

========================================================================================================================

# Lecture 6 db.md
========================================================================================================================
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

========================================================================================================================

# Lecture 7 db.md
========================================================================================================================
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

========================================================================================================================

# Lab 1 notes.md
========================================================================================================================
# Βάσεις Δεδομένων — Εργαστήριο 1: Εισαγωγή στα ΣΔΒΔ

Εισαγωγή στα Συστήματα Διαχείρισης Σχεσιακών Βάσεων Δεδομένων (ΣΔΒΔ). Το εργαστήριο καλύπτει τη θεωρητική βάση των ΣΔΒΔ, την εγκατάσταση και παραμετροποίηση του MySQL, και την εξοικείωση με το γραφικό περιβάλλον MySQL Workbench και το phpMyAdmin (μέσω XAMPP).

---

## 1. Σύνολο Εργαστηριακών Θεμάτων

Τα παρακάτω θέματα καλύπτονται κατά τη διάρκεια του εξαμήνου:

| #  | Θέμα |
| :- | :--- |
| 1  | Βασικές εντολές SQL (`CREATE DATABASE`, `CREATE TABLE`, κ.λπ.) |
| 2  | Εισαγωγή, διαγραφή και ενημέρωση δεδομένων (`INSERT`, `DELETE`, `UPDATE`) |
| 3  | Δημιουργία διαγραμμάτων ER (Entity-Relationship) |
| 4  | Μετατροπή διαγράμματος ER σε πίνακες |
| 5  | Υλοποίηση συσχετίσεων και ξένων κλειδιών — σχέσεις 1-προς-πολλά και πολλά-προς-πολλά |
| 6  | Υλοποίηση ερωτημάτων SQL με χρήση ΣΔΒΔ |
| 7  | Πρακτική εφαρμογή σχεσιακής άλγεβρας μέσω SQL |

---

## 2. Σύστημα Διαχείρισης Βάσεων Δεδομένων (ΣΔΒΔ)

### Ορισμός

Ένα **Σύστημα Διαχείρισης Βάσεων Δεδομένων** (ΣΔΒΔ) — *Database Management System (DBMS)* — είναι λογισμικό που επιτρέπει:

- **Δημιουργία** βάσεων δεδομένων και πινάκων
- **Διαχείριση** των δεδομένων (εισαγωγή, ενημέρωση, διαγραφή)
- **Αποθήκευση** δεδομένων με δομημένο τρόπο
- **Ανάκτηση** δεδομένων μέσω ερωτημάτων

Το ΣΔΒΔ που χρησιμοποιείται στο εργαστήριο είναι η **MySQL**.

---

## 3. MySQL Server

### Περιοχές Εφαρμογής

Ο MySQL Server χρησιμοποιείται σε:

- **Desktop εφαρμογές** — Python, Java, C#
- **Web εφαρμογές** — PHP, Python, Node.js
- **Mobile εφαρμογές** — Android, iOS
- **Data Analysis / Machine Learning** — Python

### Εγκατάσταση

Τα απαραίτητα πακέτα βρίσκονται στο: `http://dev.mysql.com/downloads`

| Πακέτο | Σκοπός |
| :----- | :----- |
| **MySQL Community Server** | Εγκατάσταση του εξυπηρετητή (backend) |
| **MySQL Workbench** | Γραφικό περιβάλλον διαχείρισης (frontend) |

> **[Key Insight]** Το ενοποιημένο πακέτο εγκατάστασης (`http://dev.mysql.com/downloads/windows/installer`) εγκαθιστά και τα δύο παραπάνω ταυτόχρονα — προτείνεται για απλότητα.

### Root Password

Κατά την εγκατάσταση, στο βήμα *Accounts and Roles*, ορίζεται το password του root χρήστη. Για σκοπούς εργαστηρίου χρησιμοποιείται:

```text
password: root
```

> **[Environment Note: Production]** Σε παραγωγικό περιβάλλον απαγορεύεται αυστηρά η χρήση απλών passwords όπως `root`.

---

## 4. Προσθήκη MySQL στο PATH (Windows)

Η προσθήκη στο `PATH` επιτρέπει την εκτέλεση `mysql` από οποιοδήποτε terminal χωρίς πλήρη διαδρομή.

### Βήμα 1 — Εύρεση φακέλου εγκατάστασης

```text
C:\Program Files\MySQL\MySQL Server 8.0\bin
```

### Βήμα 2 — Προσθήκη στο Path

1. Πάτα `Win + R`, γράψε `sysdm.cpl`, πάτα `Enter`.
2. Καρτέλα **Advanced** → **Environment Variables**.
3. Στη λίστα *System Variables*, επιλογή `Path` → **Edit**.
4. Κλικ **New** και εισαγωγή:

```text
C:\Program Files\MySQL\MySQL Server 8.0\bin
```

5. **OK** σε όλα τα παράθυρα.

### Βήμα 3 — Σύνδεση μέσω Terminal

```sh
mysql -u root -p
```

```text
Enter password: ****
Welcome to the MySQL monitor. Commands end with ; or \g.
Your MySQL connection id is 23
Server version: 8.0.41 MySQL Community Server - GPL
```

Μετά τη σύνδεση ο χρήστης έχει δικαιώματα **διαχειριστή** (root).

---

## 5. MySQL Workbench

### Ορισμός

Το **MySQL Workbench** είναι ολοκληρωμένο γραφικό εργαλείο (GUI) για τη διαχείριση και ανάπτυξη βάσεων δεδομένων MySQL.

### Βασικές Λειτουργίες

| Λειτουργία | Περιγραφή |
| :--------- | :-------- |
| **Database Design & Modeling** | Σχεδιασμός σχημάτων, ER διαγράμματα |
| **SQL Development** | Σύνταξη και εκτέλεση SQL ερωτημάτων |
| **Database Administration** | Διαχείριση χρηστών, ρόλων, server status |

### Σύνδεση στο Workbench

- Σύνδεση με χρήστη `root` στο `localhost:3306`.
- Δυνατότητα δημιουργίας επιπλέον χρηστών με συγκεκριμένους **ρόλους** (καλύπτεται σε επόμενο εργαστήριο).

### Βασικά Μέρη του Workbench UI

| Στοιχείο | Λειτουργία |
| :------- | :--------- |
| **Διαχείριση (Management Panel)** | Επιλογές διαχείρισης MySQL Server (Startup, Logs, Options, Restore) |
| **Schemas (Βάσεις Δεδομένων)** | Λίστα με τις ΒΔ που διαχειρίζεται ο εξυπηρετητής |
| **Παράθυρο Εντολών** | Περιοχή σύνταξης SQL κώδικα |
| **Παράθυρο Αποτελεσμάτων** | Εμφάνιση αποτελεσμάτων εκτέλεσης ερωτήματος |
| **Μηνύματα Λάθους (Output)** | Log εκτέλεσης, σφάλματα, timing |

---

## 6. Περιβάλλον Εργαστηρίου — XAMPP & phpMyAdmin

### XAMPP

Το **XAMPP** είναι πακέτο λογισμικού που περιλαμβάνει Apache, MySQL, PHP. Χρησιμοποιείται ως εναλλακτικό περιβάλλον εργαστηρίου.

**Εκκίνηση:** Start Menu → `XAMPP Control Panel`

Modules που πρέπει να τρέχουν:
- **Apache** (για phpMyAdmin)
- **MySQL** (βάση δεδομένων)

### phpMyAdmin

Το **phpMyAdmin** είναι web-based διεπαφή διαχείρισης MySQL, προσβάσιμη μέσω browser στο `http://127.0.0.1`.

Βασικά tabs του phpMyAdmin:

| Tab | Λειτουργία |
| :-- | :--------- |
| **Βάσεις δεδομένων** | Λίστα και δημιουργία ΒΔ |
| **Κώδικας SQL** | Εκτέλεση SQL ερωτημάτων |
| **Κατάσταση** | Πληροφορίες εξυπηρετητή |
| **Λογαριασμοί χρήστη** | Διαχείριση χρηστών και δικαιωμάτων |
| **Εξαγωγή / Εισαγωγή** | Backup/Restore δεδομένων |
| **Ρυθμίσεις** | Παραμετροποίηση phpMyAdmin |

---

## Σημαντικές Εντολές — Quick Reference

```sql
-- Εμφάνιση όλων των βάσεων δεδομένων
SHOW DATABASES;

-- Επιλογή βάσης δεδομένων
USE <database_name>;

-- Εμφάνιση πινάκων της τρέχουσας ΒΔ
SHOW TABLES;
```

> **[Supplementary]** Κάθε εντολή SQL στο MySQL terminal πρέπει να τελειώνει με `;` ή `\g`. Η εντολή `\c` ακυρώνει την τρέχουσα είσοδο χωρίς εκτέλεση.

---

## Exam Tip: Διαφορά ΣΔΒΔ vs Βάση Δεδομένων

Συχνό λάθος σε εξετάσεις: σύγχυση μεταξύ **ΣΔΒΔ** και **Βάσης Δεδομένων**.

- **Βάση Δεδομένων (ΒΔ):** Το σύνολο των αποθηκευμένων δεδομένων (τα ίδια τα δεδομένα).
- **ΣΔΒΔ:** Το λογισμικό που διαχειρίζεται τη ΒΔ (π.χ. MySQL, PostgreSQL, Oracle).

**Παράδειγμα:** Η MySQL είναι ΣΔΒΔ. Η βάση `sakila` είναι μια Βάση Δεδομένων που διαχειρίζεται το MySQL.

========================================================================================================================

# Lab 2 notes.md
========================================================================================================================
# Βάσεις Δεδομένων — Εργαστήριο 2 Σημειώσεις

Οι σημειώσεις αυτές συνοψίζουν το περιεχόμενο του εργαστηρίου για τις βασικές εντολές SQL, τη διάκριση DDL/DML, τα βασικά στοιχεία σύνταξης και τη δημιουργία μιας απλής βάσης δεδομένων για ταινίες και ηθοποιούς. Το υλικό εστιάζει στη δημιουργία βάσης, πινάκων, επιλογή τύπων δεδομένων, χρήση πρωτεύοντος κλειδιού και βασικές εντολές επιθεώρησης του σχήματος.

---

## 1. Τι είναι η SQL

### Ορισμός

Η SQL (`Structured Query Language`) είναι η δομημένη γλώσσα ερωτημάτων που χρησιμοποιείται στα Συστήματα Διαχείρισης Βάσεων Δεδομένων (ΣΔΒΔ) για:

- δημιουργία δεδομένων και δομών,
- εισαγωγή, ενημέρωση και διαγραφή δεδομένων,
- διατύπωση ερωτημάτων ανάκτησης πληροφορίας.

### Ιστορικά στοιχεία

- Η αρχική μορφή της ονομαζόταν `SEQUEL` (`Structured English Query Language`).
- Σχεδιάστηκε από ερευνητική ομάδα της IBM στο πλαίσιο του `System R` το 1974.
- Η Oracle τη χρησιμοποίησε πρώτη φορά σε εμπορικό ΣΔΒΔ το 1979.

### Χαρακτηριστικά

Η SQL είναι δηλωτική γλώσσα υψηλού επιπέδου. Αυτό σημαίνει ότι ο χρήστης δηλώνει **τι** θέλει να γίνει και όχι **πώς** θα εκτελεστεί εσωτερικά.

### Αντιστοίχιση όρων

| Όρος SQL | Θεωρητική έννοια |
| :--- | :--- |
| Πίνακας | Σχέση |
| Γραμμή | Πλειάδα |
| Στήλη | Γνώρισμα |

### Πλεονεκτήματα SQL

- Υποστηρίζεται από κάθε σχεσιακό σύστημα.
- Τα ερωτήματα είναι σε μεγάλο βαθμό ανεξάρτητα από το συγκεκριμένο ΣΔΒΔ.
- Χρησιμοποιείται για όλες τις βασικές λειτουργίες ενός ΣΔΒΔ.
- Υποστηρίζεται από πολλές γλώσσες προγραμματισμού.
- Έχει σχετικά απλή σύνταξη.
- Αποδεσμεύει τον χρήστη από λεπτομέρειες υλοποίησης.

---

## 2. Κατηγορίες γλωσσών βάσεων δεδομένων

### DDL — Data Definition Language

Η `DDL` είναι η γλώσσα ορισμού δεδομένων. Με αυτήν ορίζουμε το σχήμα της βάσης δεδομένων.

### Τι κάνει η DDL

Με δηλώσεις DDL ορίζονται:

- βάσεις δεδομένων,
- πίνακες,
- πεδία,
- περιορισμοί.

### Data dictionary

Το αποτέλεσμα των δηλώσεων DDL αποθηκεύεται σε ειδικό αρχείο που λέγεται:

- `data dictionary`, ή
- `data directory`.

Το αρχείο αυτό περιέχει μεταδεδομένα, δηλαδή δεδομένα για τα δεδομένα. Πριν από οποιαδήποτε πρόσβαση στα αποθηκευμένα δεδομένα, το σύστημα συμβουλεύεται αυτό το αρχείο.

### DML — Data Manipulation Language

Η `DML` είναι η γλώσσα χειρισμού δεδομένων.

### Τι περιλαμβάνει ο χειρισμός δεδομένων

- Ανάκτηση αποθηκευμένης πληροφορίας.
- Εισαγωγή νέας πληροφορίας.
- Διαγραφή αποθηκευμένης πληροφορίας.
- Τροποποίηση αποθηκευμένης πληροφορίας.

Συχνά αναφέρεται και ως γλώσσα ερωτημάτων (`query language`), επειδή επιτρέπει τη διατύπωση ερωτημάτων προς το σύστημα.

---

## 3. Περιβάλλον εργασίας

Στο εργαστήριο χρησιμοποιείται το `XAMPP` και η διεπαφή για εκτέλεση SQL εντολών.

### Βασική ροή

1. Εκκίνηση `XAMPP`.
2. Άνοιγμα του περιβάλλοντος SQL.
3. Πληκτρολόγηση και εκτέλεση εντολών.

> **[Environment Note: Εργαστήριο]** Το υλικό δείχνει περιβάλλον Windows με XAMPP, αλλά οι εντολές SQL παραμένουν ίδιες ανεξάρτητα από το λειτουργικό σύστημα. Αυτό που αλλάζει είναι μόνο ο τρόπος εκκίνησης του εργαλείου.

---

## 4. Βασικά σύνταξης SQL

### Τερματισμός εντολών

Στη MySQL, το `;` στο τέλος κάθε εντολής λειτουργεί ως `delimiter`, δηλαδή δηλώνει το τέλος της εντολής και προκαλεί την εκτέλεσή της.

### Case sensitivity

Η SQL δεν είναι `case sensitive` ως προς τις εντολές. Παρόλα αυτά, είναι καλή πρακτική να γράφουμε:

- εντολές σε κεφαλαία,
- ονόματα πινάκων/στηλών με συνεπή μορφή,
- τον κώδικα μορφοποιημένο σε πολλές γραμμές για αναγνωσιμότητα.

### Παράδειγμα

```sql
SHOW DATABASES;
CREATE DATABASE Hollywood;
USE Hollywood;
```

---

## 5. Βασικές εντολές για βάσεις δεδομένων

### Σύνταξη και χρήση

| Εντολή | Ρόλος |
| :--- | :--- |
| `CREATE DATABASE <όνομα_ΒΔ>;` | Δημιουργεί νέα βάση δεδομένων |
| `CREATE SCHEMA <όνομα_ΒΔ>;` | Ισοδύναμη με `CREATE DATABASE` |
| `SHOW DATABASES;` | Εμφανίζει τις διαθέσιμες βάσεις |
| `SHOW SCHEMAS;` | Ισοδύναμη με `SHOW DATABASES` |
| `DROP DATABASE <όνομα_ΒΔ>;` | Διαγράφει βάση δεδομένων |
| `DROP SCHEMA <όνομα_ΒΔ>;` | Ισοδύναμη με `DROP DATABASE` |
| `USE <όνομα_ΒΔ>;` | Επιλέγει την ενεργή βάση |

### Παράδειγμα δημιουργίας και διαγραφής βάσης

```sql
SHOW DATABASES;
CREATE DATABASE test;
DROP DATABASE test;
CREATE DATABASE Hollywood;
USE Hollywood;
```

```text
- Εμφάνιση των διαθέσιμων βάσεων.
- Δημιουργία της test.
- Διαγραφή της test.
- Δημιουργία της Hollywood.
- Επιλογή της Hollywood ως ενεργής βάσης.
```

> **[Key Insight]** Η `USE Hollywood;` δεν δημιουργεί βάση. Απλώς δηλώνει ποια υπάρχουσα βάση θα χρησιμοποιείται από τις επόμενες εντολές.

---

## 6. Σχεδιασμός της βάσης HOLLYWOOD

### Πρόβλημα

Θέλουμε να κατασκευάσουμε μια βάση δεδομένων για:

- κινηματογραφικές ταινίες,
- ηθοποιούς του Hollywood.

Για λόγους απλότητας αποθηκεύονται μόνο στοιχεία για τις οντότητες `ACTORS` και `MOVIES`.

### Πίνακας ACTORS

Για κάθε ηθοποιό θέλουμε:

- `ID`: αριθμός ταυτότητας, μοναδικός,
- `NAME`: ονοματεπώνυμο,
- `BIRTHDATE`: ημερομηνία γέννησης,
- `BIRTHPLACE`: τόπος γέννησης,
- `OSCARS`: αριθμός βραβείων Oscar.

### Πίνακας MOVIES

Για κάθε ταινία θέλουμε:

- `TITLE`: τίτλος,
- `YEAR`: έτος παραγωγής,
- `DIRECTOR`: όνομα σκηνοθέτη,
- `BUDGET`: συνολικό κόστος,
- `TICKETS`: αριθμός εισιτηρίων.

### Σχεδιαστική παρατήρηση

Οι πίνακες `ACTORS` και `MOVIES` αποθηκεύουν δεδομένα μόνο για τις αντίστοιχες οντότητες. Δεν αποθηκεύεται ακόμη η σύνδεση μεταξύ ηθοποιών και ταινιών. Άρα δεν υπάρχει ακόμη πίνακας συσχέτισης, όπως π.χ. `PLAYS_IN` ή `CASTING`.

---

## 7. Τύποι δεδομένων και περιορισμοί

### Βασικοί τύποι δεδομένων

| Τύπος | Περιγραφή |
| :--- | :--- |
| `int` ή `integer` | Ακέραιος αριθμός |
| `real` | Πραγματικός αριθμός |
| `char` | Ένας χαρακτήρας |
| `varchar(n)` | Συμβολοσειρά μεταβλητού μήκους έως `n` χαρακτήρες |
| `date` | Ημερομηνία |

### `NOT NULL`

Ο περιορισμός `NOT NULL` δηλώνει ότι ένα πεδίο πρέπει υποχρεωτικά να έχει τιμή.

Παράδειγμα:

```sql
NAME varchar(20) NOT NULL
```

Αυτό σημαίνει ότι δεν επιτρέπεται εγγραφή ηθοποιού χωρίς όνομα.

### Παρατήρηση για ονόματα

Στα ονόματα πινάκων και πεδίων συνήθως αποφεύγονται οι ελληνικοί χαρακτήρες.

---

## 8. Η εντολή CREATE TABLE

### Γενική σύνταξη

```sql
CREATE TABLE <όνομα_πίνακα> (
    <όνομα_1ου_πεδίου> <τύπος_1ου_πεδίου>,
    <όνομα_2ου_πεδίου> <τύπος_2ου_πεδίου>,
    ...,
    <όνομα_νου_πεδίου> <τύπος_νου_πεδίου>,
    PRIMARY KEY (<όνομα_πεδίου>)
);
```

Η εντολή μπορεί να γραφτεί και σε μία γραμμή, αλλά η πολυγραμμική μορφή είναι πιο ευανάγνωστη.

### Πρωτεύον κλειδί

Πρωτεύον κλειδί (`primary key`) είναι ένα πεδίο ή συνδυασμός πεδίων που:

- προσδιορίζει μοναδικά κάθε γραμμή,
- δεν επιτρέπεται να έχει τιμή `NULL`.

### Ιδιότητες πρωτεύοντος κλειδιού

- Κάθε πίνακας πρέπει να έχει πρωτεύον κλειδί.
- Ένας πίνακας έχει μόνο **ένα** πρωτεύον κλειδί.
- Το πρωτεύον κλειδί δεν χρειάζεται να δηλωθεί και ως `NOT NULL`, επειδή αυτό επιβάλλεται αυτόματα.

### Παράδειγμα ορθού και λανθασμένου πεδίου

- Στον πίνακα `ACTORS`, κατάλληλο πρωτεύον κλειδί είναι το `ID`.
- Το `BIRTHDATE` δεν είναι κατάλληλο πρωτεύον κλειδί, επειδή δύο ηθοποιοί μπορούν να έχουν ίδια ημερομηνία γέννησης.

---

## 9. Δημιουργία των πινάκων ACTORS και MOVIES

### Πίνακας ACTORS

```sql
CREATE TABLE ACTORS (
    ID varchar(10),
    NAME varchar(20) NOT NULL,
    BIRTHDATE date,
    BIRTHPLACE varchar(20),
    OSCARS int,
    PRIMARY KEY (ID)
);
```

### Ανάλυση πεδίων ACTORS

| Πεδίο | Τύπος | Ρόλος |
| :--- | :--- | :--- |
| `ID` | `varchar(10)` | Μοναδικός αναγνωριστικός κωδικός ηθοποιού |
| `NAME` | `varchar(20) NOT NULL` | Ονοματεπώνυμο, υποχρεωτικό |
| `BIRTHDATE` | `date` | Ημερομηνία γέννησης |
| `BIRTHPLACE` | `varchar(20)` | Τόπος γέννησης |
| `OSCARS` | `int` | Πλήθος Oscar |

### Πίνακας MOVIES

```sql
CREATE TABLE MOVIES (
    TITLE varchar(50),
    YEAR date,
    DIRECTOR varchar(50),
    BUDGET int,
    TICKETS int,
    PRIMARY KEY (TITLE)
);
```

### Ανάλυση πεδίων MOVIES

| Πεδίο | Τύπος | Ρόλος |
| :--- | :--- | :--- |
| `TITLE` | `varchar(50)` | Τίτλος ταινίας |
| `YEAR` | `date` | Έτος παραγωγής όπως δίνεται στο υλικό |
| `DIRECTOR` | `varchar(50)` | Σκηνοθέτης |
| `BUDGET` | `int` | Κόστος παραγωγής |
| `TICKETS` | `int` | Αριθμός εισιτηρίων |

> **[Key Insight]** Στο υλικό το πεδίο `YEAR` ορίζεται ως `date`, αν και εννοιολογικά αντιστοιχεί σε έτος παραγωγής. Σε πιο αυστηρό σχεδιασμό θα μπορούσε να επιλεγεί άλλος τύπος ανάλογα με το μοντέλο δεδομένων.

---

## 10. Περιγραφή πίνακα με DESCRIBE

Για να εμφανίσουμε το σχήμα ενός πίνακα χρησιμοποιούμε:

```sql
DESCRIBE <όνομα_πίνακα>;
```

Παράδειγμα:

```sql
DESCRIBE ACTORS;
```

```text
Επιστρέφεται η περιγραφή του πίνακα, δηλαδή τα πεδία, οι τύποι τους, αν επιτρέπεται NULL, και πληροφορίες για κλειδιά.
```

---

## 11. Συγκεντρωτική ροή εργαστηρίου

### Βήματα

1. Ελέγχουμε ποιες βάσεις υπάρχουν.
2. Δημιουργούμε νέα βάση.
3. Επιλέγουμε τη βάση με `USE`.
4. Δημιουργούμε τους πίνακες με `CREATE TABLE`.
5. Ορίζουμε πρωτεύον κλειδί.
6. Ελέγχουμε το σχήμα με `DESCRIBE`.

### Συνολικό παράδειγμα

```sql
SHOW DATABASES;
CREATE DATABASE Hollywood;
USE Hollywood;

CREATE TABLE ACTORS (
    ID varchar(10),
    NAME varchar(20) NOT NULL,
    BIRTHDATE date,
    BIRTHPLACE varchar(20),
    OSCARS int,
    PRIMARY KEY (ID)
);

CREATE TABLE MOVIES (
    TITLE varchar(50),
    YEAR date,
    DIRECTOR varchar(50),
    BUDGET int,
    TICKETS int,
    PRIMARY KEY (TITLE)
);

DESCRIBE ACTORS;
DESCRIBE MOVIES;
```

---

## Solved Exercises

### Exercise 1: Δημιουργία βάσης

**Problem:** Να δημιουργηθεί βάση δεδομένων με όνομα `Hollywood` και να επιλεγεί ως ενεργή.

**Solution:**

1. Δημιουργούμε τη βάση με `CREATE DATABASE`.
2. Την επιλέγουμε με `USE`.

```sql
CREATE DATABASE Hollywood;
USE Hollywood;
```

```text
Η βάση Hollywood δημιουργείται και γίνεται η ενεργή βάση για τις επόμενες εντολές.
```

### Exercise 2: Εμφάνιση διαθέσιμων βάσεων

**Problem:** Να εμφανιστούν όλες οι υπάρχουσες βάσεις δεδομένων.

**Solution:**

1. Χρησιμοποιούμε την εντολή `SHOW DATABASES;`.

```sql
SHOW DATABASES;
```

```text
Εμφανίζεται η λίστα των διαθέσιμων βάσεων δεδομένων του συστήματος.
```

### Exercise 3: Διαγραφή πρόχειρης βάσης

**Problem:** Έχει δημιουργηθεί η βάση `test` και πρέπει να διαγραφεί.

**Solution:**

1. Εντοπίζουμε ότι η βάση υπάρχει.
2. Εκτελούμε `DROP DATABASE test;`.

```sql
DROP DATABASE test;
```

```text
Η βάση test διαγράφεται οριστικά.
```

### Exercise 4: Δήλωση υποχρεωτικού πεδίου

**Problem:** Να δηλωθεί το πεδίο `NAME` έτσι ώστε να μην επιτρέπεται κενή τιμή.

**Solution:**

1. Επιλέγουμε τύπο `varchar(20)`.
2. Προσθέτουμε τον περιορισμό `NOT NULL`.

```sql
NAME varchar(20) NOT NULL
```

```text
Το πεδίο NAME γίνεται υποχρεωτικό.
```

### Exercise 5: Επιλογή πρωτεύοντος κλειδιού

**Problem:** Ποιο πεδίο είναι καταλληλότερο ως πρωτεύον κλειδί στον πίνακα `ACTORS`, το `ID` ή το `BIRTHDATE`;

**Solution:**

1. Το πρωτεύον κλειδί πρέπει να είναι μοναδικό για κάθε γραμμή.
2. Το `BIRTHDATE` μπορεί να επαναλαμβάνεται.
3. Το `ID` είναι μοναδικό για κάθε ηθοποιό.

**Τελικό αποτέλεσμα:** Επιλέγουμε το `ID` ως `PRIMARY KEY`.

### Exercise 6: Δημιουργία πίνακα ACTORS

**Problem:** Να δημιουργηθεί ο πίνακας `ACTORS` με τα πεδία του εργαστηρίου.

**Solution:**

1. Ορίζουμε τα πεδία και τους τύπους τους.
2. Ορίζουμε `NOT NULL` στο `NAME`.
3. Θέτουμε `PRIMARY KEY (ID)`.

```sql
CREATE TABLE ACTORS (
    ID varchar(10),
    NAME varchar(20) NOT NULL,
    BIRTHDATE date,
    BIRTHPLACE varchar(20),
    OSCARS int,
    PRIMARY KEY (ID)
);
```

```text
Ο πίνακας ACTORS δημιουργείται με πρωτεύον κλειδί το ID.
```

### Exercise 7: Δημιουργία πίνακα MOVIES

**Problem:** Να δημιουργηθεί ο πίνακας `MOVIES` με πρωτεύον κλειδί τον τίτλο.

**Solution:**

1. Ορίζουμε τα πεδία `TITLE`, `YEAR`, `DIRECTOR`, `BUDGET`, `TICKETS`.
2. Θέτουμε πρωτεύον κλειδί το `TITLE`.

```sql
CREATE TABLE MOVIES (
    TITLE varchar(50),
    YEAR date,
    DIRECTOR varchar(50),
    BUDGET int,
    TICKETS int,
    PRIMARY KEY (TITLE)
);
```

```text
Ο πίνακας MOVIES δημιουργείται με πρωτεύον κλειδί το TITLE.
```

### Exercise 8: Περιγραφή πίνακα

**Problem:** Να εμφανιστεί το σχήμα του πίνακα `ACTORS`.

**Solution:**

1. Χρησιμοποιούμε την εντολή `DESCRIBE`.

```sql
DESCRIBE ACTORS;
```

```text
Εμφανίζονται τα πεδία του πίνακα ACTORS, οι τύποι δεδομένων και τα χαρακτηριστικά τους.
```

---

## Common Errors and Gotchas

### 1. Ξεχνάω το `USE`

Αν δεν εκτελεστεί `USE Hollywood;`, οι εντολές δημιουργίας πινάκων μπορεί να αποτύχουν ή να εκτελεστούν σε λάθος βάση.

### 2. Χρήση μη μοναδικού πεδίου ως `PRIMARY KEY`

Πεδία όπως ημερομηνία γέννησης δεν εγγυώνται μοναδικότητα.

### 3. Παράλειψη `;`

Στο περιβάλλον MySQL η εντολή δεν θεωρείται ολοκληρωμένη χωρίς τον delimiter.

### 4. Σύγχυση `CREATE DATABASE` και `USE`

Η `CREATE DATABASE` δημιουργεί τη βάση, ενώ η `USE` απλώς την επιλέγει.

### 5. Παρερμηνεία του `NOT NULL`

Το `NOT NULL` δεν σημαίνει μοναδικότητα. Δηλώνει μόνο ότι η τιμή δεν μπορεί να λείπει.

---

## Exam Tip: Τι να θυμάσαι

- `DDL` ορίζει τη δομή, `DML` χειρίζεται τα δεδομένα.
- Κάθε πίνακας πρέπει να έχει ένα πρωτεύον κλειδί.
- Το `PRIMARY KEY` είναι μοναδικό και όχι `NULL`.
- Το `NOT NULL` σημαίνει υποχρεωτική τιμή, όχι μοναδική τιμή.
- Η συνηθισμένη σειρά σε ασκήσεις είναι: `CREATE DATABASE` -> `USE` -> `CREATE TABLE` -> `DESCRIBE`.

---

## Προτεινόμενη βιβλιογραφία του υλικού

Το αρχικό υλικό παραπέμπει ενδεικτικά σε:

- βιβλία για Συστήματα Βάσεων Δεδομένων,
- τεκμηρίωση `MySQL`,
- `PostgreSQL Documentation`,
- `SQL Tutorial` από W3Schools,
- `ERD Plus Documentation`,
- σύγχρονα ακαδημαϊκά συγγράμματα Κάλλιπος.

========================================================================================================================

# Lab 3 notes.md
========================================================================================================================
# Βάσεις Δεδομένων — Εργαστήριο 4: SQL Notes

Οι σημειώσεις καλύπτουν τις βασικές εντολές SQL που παρουσιάζονται στο εργαστήριο: δημιουργία και επιλογή βάσης, δημιουργία πινάκων, μεταβολές στο σχήμα με `ALTER TABLE`, εισαγωγή δεδομένων με `INSERT INTO`, ανάκτηση δεδομένων με `SELECT`, τροποποίηση με `UPDATE` και `DELETE`, και σύνδεση πινάκων με ξένα κλειδιά. Το υλικό βασίζεται στο παράδειγμα της βάσης `Hollywood` με τους πίνακες `ACTORS`, `MOVIES` και `STARS`.

---

## 1. Concept Overview

Το εργαστήριο εστιάζει στις βασικές εντολές SQL για διαχείριση σχεσιακής βάσης δεδομένων και για χειρισμό πινάκων και εγγραφών. Η ροή της ύλης είναι πρακτική: πρώτα ορίζεται η βάση και οι πίνακες, μετά γίνονται αλλαγές στο σχήμα, έπειτα εισάγονται και προβάλλονται δεδομένα, και τέλος συνδέονται πίνακες μέσω ξένων κλειδιών.

---

## 2. Βασικές εντολές βάσης δεδομένων

### Σκοπός

Οι εντολές αυτές χρησιμοποιούνται για δημιουργία, εμφάνιση, διαγραφή και επιλογή ενεργής βάσης δεδομένων.

### Syntax Reference

```sql
CREATE DATABASE <όνομα_ΒΔ>;
CREATE SCHEMA <όνομα_ΒΔ>;
SHOW DATABASES;
SHOW SCHEMAS;
DROP DATABASE <όνομα_ΒΔ>;
DROP SCHEMA <όνομα_ΒΔ>;
USE <όνομα_ΒΔ>;
```

### Behavioral Description

- Η `CREATE DATABASE` δημιουργεί νέα βάση δεδομένων.
- Η `CREATE SCHEMA` χρησιμοποιείται εδώ ως ισοδύναμη της `CREATE DATABASE`.
- Οι `SHOW DATABASES` και `SHOW SCHEMAS` εμφανίζουν τις διαθέσιμες βάσεις.
- Οι `DROP DATABASE` και `DROP SCHEMA` διαγράφουν μια βάση.
- Η `USE` ορίζει ποια βάση είναι ενεργή ώστε οι επόμενες εντολές να εκτελούνται σε αυτή.

### Parameter Reference

| Όνομα | Τιμές / Τύπος | Required | Default | Περιγραφή |
| :--- | :--- | :---: | :---: | :--- |
| `<όνομα_ΒΔ>` | Αναγνωριστικό SQL | Ναι | Καμία | Το όνομα της βάσης δεδομένων που δημιουργείται, διαγράφεται ή επιλέγεται. |

---

## 3. Δημιουργία πινάκων με `CREATE TABLE`

### Syntax Reference

```sql
CREATE TABLE <όνομα_πίνακα> (
  <όνομα_πεδίου_1> <τύπος_1>,
  <όνομα_πεδίου_2> <τύπος_2>,
  ...,
  PRIMARY KEY (<πεδίο_ή_πεδία>)
);
```

### Behavioral Description

Η `CREATE TABLE` ορίζει το σχήμα ενός πίνακα: ονόματα πεδίων, τύπους δεδομένων, περιορισμούς και πρωτεύον κλειδί. Το πρωτεύον κλειδί ταυτοποιεί μοναδικά κάθε εγγραφή και δεν επιτρέπεται να είναι `NULL`.

### Παράδειγμα πινάκων του εργαστηρίου

```sql
CREATE TABLE ACTORS (
  ID varchar(10),
  NAME varchar(20) not null,
  BIRTHDATE date,
  BIRTHPLACE varchar(20),
  OSCARS int,
  PRIMARY KEY (ID)
);

CREATE TABLE MOVIES (
  TITLE varchar(50),
  YEAR date,
  DIRECTOR varchar(50),
  BUDGET int,
  TICKETS int,
  PRIMARY KEY (TITLE)
);
```

### Parameter Reference

| Όνομα | Τιμές / Τύπος | Required | Default | Περιγραφή |
| :--- | :--- | :---: | :---: | :--- |
| `<όνομα_πίνακα>` | Αναγνωριστικό SQL | Ναι | Καμία | Το όνομα του πίνακα. |
| `<όνομα_πεδίου>` | Αναγνωριστικό SQL | Ναι | Καμία | Το όνομα της στήλης. |
| `<τύπος>` | `varchar(n)`, `date`, `int`, `real` | Ναι | Καμία | Ο τύπος δεδομένων κάθε πεδίου. |
| `PRIMARY KEY (...)` | Ένα ή περισσότερα πεδία | Συνήθως ναι | Καμία | Μοναδικό αναγνωριστικό κάθε εγγραφής. |
| `NOT NULL` | Constraint | Όχι | Επιτρέπεται `NULL` | Απαγορεύει κενή τιμή στο πεδίο. |

### Key Insight

> **[Key Insight]** Το εργαστήριο χρησιμοποιεί αγγλικά ονόματα πινάκων και πεδίων, επειδή ελληνικοί χαρακτήρες συνήθως δεν γίνονται αποδεκτοί σε ονόματα πινάκων και πεδίων.

---

## 4. Επεξεργασία σχήματος με `ALTER TABLE`

### Σκοπός

Η `ALTER TABLE` αλλάζει υπάρχον πίνακα χωρίς να χρειάζεται να τον ξαναδημιουργήσουμε.

### Syntax Reference

```sql
ALTER TABLE <όνομα_πίνακα> ADD <όνομα_πεδίου> <τύπος>;
ALTER TABLE <όνομα_πίνακα> MODIFY <όνομα_πεδίου> <νέος_τύπος>;
ALTER TABLE <όνομα_πίνακα> DROP COLUMN <όνομα_πεδίου>;
ALTER TABLE <όνομα_πίνακα> CHANGE <παλιό_όνομα> <νέο_όνομα> <τύπος>;
DESCRIBE <όνομα_πίνακα>;
```

### Behavioral Description

- Η `ADD` προσθέτει νέα στήλη.
- Η `MODIFY` αλλάζει μόνο τον τύπο ενός πεδίου, όχι το όνομά του.
- Η `DROP COLUMN` διαγράφει στήλη και μπορεί να προκαλέσει απώλεια δεδομένων.
- Η `CHANGE` μετονομάζει πεδίο και δηλώνει ξανά τον τύπο του.
- Η `DESCRIBE` εμφανίζει το σχήμα του πίνακα.

### Παραδείγματα

```sql
USE Hollywood;
ALTER TABLE MOVIES ADD DURATION varchar(6);
ALTER TABLE MOVIES MODIFY DURATION int;
ALTER TABLE MOVIES DROP COLUMN DURATION;
ALTER TABLE ACTORS CHANGE BIRTHDATE DATE_OF_BIRTH DATE;
ALTER TABLE ACTORS CHANGE DATE_OF_BIRTH BIRTHDATE DATE;
DESCRIBE MOVIES;
```

### Parameter Reference

| Όνομα | Τιμές / Τύπος | Required | Default | Περιγραφή |
| :--- | :--- | :---: | :---: | :--- |
| `<όνομα_πίνακα>` | Αναγνωριστικό SQL | Ναι | Καμία | Ο πίνακας που αλλάζει. |
| `<όνομα_πεδίου>` | Αναγνωριστικό SQL | Ναι | Καμία | Το πεδίο που προστίθεται, αλλάζει ή διαγράφεται. |
| `<τύπος>` | SQL data type | Ναι | Καμία | Ο νέος ή αρχικός τύπος του πεδίου. |
| `<παλιό_όνομα>` | Αναγνωριστικό SQL | Ναι | Καμία | Το τρέχον όνομα του πεδίου. |
| `<νέο_όνομα>` | Αναγνωριστικό SQL | Ναι | Καμία | Το νέο όνομα του πεδίου. |

---

## 5. Εισαγωγή δεδομένων με `INSERT INTO`

### Syntax Reference

```sql
INSERT INTO <όνομα_πίνακα> VALUES (<λίστα_τιμών>);
INSERT INTO <όνομα_πίνακα> (<λίστα_πεδίων>) VALUES (<λίστα_τιμών>);
```

### Behavioral Description

Η `INSERT INTO` εισάγει μία και μόνο μία πλειάδα ανά εντολή. Αν δοθεί λίστα πεδίων, τιμές χρειάζονται μόνο για αυτά τα πεδία· όσα παραλείπονται παίρνουν `NULL`, αρκεί να μην είναι `NOT NULL` ή μέρος πρωτεύοντος κλειδιού.

### Κανόνες τιμών

- Τιμές `varchar` και `date` γράφονται μέσα σε μονά εισαγωγικά.
- Αριθμητικές τιμές όπως `int` και `real` δεν μπαίνουν σε εισαγωγικά.
- Η τιμή `NULL` γράφεται χωρίς εισαγωγικά.
- Το διαχωριστικό σε λίστες τιμών είναι το κόμμα.

### Παραδείγματα

```sql
INSERT INTO ACTORS VALUES ('A01', 'Brad Pitt', '1963-12-18', 'Oklahoma', NULL);
INSERT INTO ACTORS VALUES ('A02', 'Angelina Jolie', '1975-06-04', 'California', NULL);
INSERT INTO ACTORS VALUES ('A03', 'Leonardo DiCaprio', '1974-11-11', 'Los Angeles', NULL);
INSERT INTO ACTORS VALUES ('A04', 'Morgan Freeman', '1937-06-01', 'Tennessee', NULL);
INSERT INTO ACTORS VALUES ('A05', 'Meryl Streep', '1949-06-22', 'New Jersey', NULL);
INSERT INTO ACTORS (ID, NAME) VALUES ('A06', 'George Clooney');
```

### Parameter Reference

| Όνομα | Τιμές / Τύπος | Required | Default | Περιγραφή |
| :--- | :--- | :---: | :---: | :--- |
| `<όνομα_πίνακα>` | Αναγνωριστικό SQL | Ναι | Καμία | Ο πίνακας στον οποίο γίνεται εισαγωγή. |
| `<λίστα_πεδίων>` | Λίστα στηλών | Όχι | Όλα τα πεδία | Τα πεδία που θα πάρουν ρητή τιμή. |
| `<λίστα_τιμών>` | Λίστα τιμών SQL | Ναι | Καμία | Οι τιμές της νέας εγγραφής, με σωστή σειρά. |

---

## 6. Επισκόπηση δεδομένων με `SELECT`

### Syntax Reference

```sql
SELECT *
FROM <όνομα_πίνακα>;

SELECT <λίστα_πεδίων>
FROM <όνομα_πίνακα>;
```

### Behavioral Description

Η `SELECT` χρησιμοποιείται για προβολή δεδομένων. Το `*` σημαίνει ότι επιστρέφονται όλα τα πεδία κάθε γραμμής, ενώ με λίστα πεδίων επιστρέφονται μόνο οι ζητούμενες στήλες.

### Παραδείγματα

```sql
SELECT *
FROM ACTORS;

SELECT NAME, OSCARS
FROM ACTORS;
```

### Parameter Reference

| Όνομα | Τιμές / Τύπος | Required | Default | Περιγραφή |
| :--- | :--- | :---: | :---: | :--- |
| `<λίστα_πεδίων>` | `*` ή λίστα στηλών | Ναι | Καμία | Τα πεδία που θα εμφανιστούν. |
| `<όνομα_πίνακα>` | Αναγνωριστικό SQL | Ναι | Καμία | Ο πίνακας από τον οποίο γίνεται ανάκτηση. |

---

## 7. Τροποποίηση δεδομένων με `UPDATE` και `DELETE`

### `UPDATE`

#### Syntax Reference

```sql
UPDATE <όνομα_πίνακα>
SET <όνομα_πεδίου> = <νέα_τιμή>
WHERE <συνθήκη>;
```

#### Behavioral Description

Η `UPDATE` αλλάζει ήδη υπάρχουσες εγγραφές. Το `SET` ορίζει τι θα αλλάξει και το `WHERE` ποιες γραμμές επηρεάζονται. Αν παραλειφθεί το `WHERE`, αλλάζουν όλες οι γραμμές του πίνακα.

#### Παράδειγμα

```sql
UPDATE ACTORS
SET BIRTHDATE = '1968-08-15'
WHERE ID = 'A01';
```

### `DELETE`

#### Syntax Reference

```sql
DELETE FROM <όνομα_πίνακα>
WHERE <συνθήκη>;
```

#### Behavioral Description

Η `DELETE` διαγράφει γραμμές από πίνακα. Αν παραλειφθεί το `WHERE`, διαγράφονται όλες οι γραμμές του πίνακα, αλλά ο πίνακας συνεχίζει να υπάρχει.

#### Παραδείγματα

```sql
DELETE FROM ACTORS
WHERE ID = 'A01';

DELETE FROM ACTORS;
```

### Parameter Reference

| Εντολή | Όνομα | Τιμές / Τύπος | Required | Default | Περιγραφή |
| :--- | :--- | :--- | :---: | :---: | :--- |
| `UPDATE` | `<όνομα_πίνακα>` | Αναγνωριστικό SQL | Ναι | Καμία | Πίνακας που τροποποιείται. |
| `UPDATE` | `<όνομα_πεδίου>` | Στήλη | Ναι | Καμία | Το πεδίο που αλλάζει. |
| `UPDATE` | `<νέα_τιμή>` | SQL literal | Ναι | Καμία | Η νέα τιμή του πεδίου. |
| `UPDATE` | `<συνθήκη>` | Boolean condition | Όχι | Όλες οι γραμμές | Περιορίζει τις γραμμές που αλλάζουν. |
| `DELETE` | `<όνομα_πίνακα>` | Αναγνωριστικό SQL | Ναι | Καμία | Πίνακας από τον οποίο διαγράφονται γραμμές. |
| `DELETE` | `<συνθήκη>` | Boolean condition | Όχι | Όλες οι γραμμές | Περιορίζει ποιες γραμμές θα διαγραφούν. |

---

## 8. Σύνδεση πινάκων και ξένα κλειδιά

### Θεωρία

Όταν θέλουμε να συνδέσουμε ηθοποιούς με ταινίες, η σχέση είναι πολλών-προς-πολλά: ένας ηθοποιός μπορεί να εμφανίζεται σε πολλές ταινίες και κάθε ταινία μπορεί να έχει πολλούς ηθοποιούς. Για να εκφραστεί αυτή η σχέση, δημιουργούμε ενδιάμεσο πίνακα.

### Ορισμός ξένου κλειδιού

Ξένο κλειδί είναι ένα πεδίο ή συνδυασμός πεδίων ενός πίνακα που παίρνει τιμές οι οποίες υπάρχουν ήδη σε πεδίο άλλου πίνακα. Έτσι διατηρείται η αναφορική ακεραιότητα: δεν μπορούμε να βάλουμε τιμή που δεν υπάρχει στον πίνακα αναφοράς.

### Syntax Reference

```sql
FOREIGN KEY (<γνώρισμα_ξένο_κλειδί>)
REFERENCES <πίνακας_αναφοράς>(<γνώρισμα_αναφοράς>)
```

### Παράδειγμα πίνακα `STARS`

```sql
CREATE TABLE STARS (
  ID VARCHAR(10),
  TITLE VARCHAR(50),
  ROLE VARCHAR(30),
  CACHE REAL,
  PRIMARY KEY (ID, TITLE),
  FOREIGN KEY (ID) REFERENCES ACTORS(ID),
  FOREIGN KEY (TITLE) REFERENCES MOVIES(TITLE)
);
```

### Ερμηνεία του πίνακα `STARS`

- `ID`: ποιος ηθοποιός συμμετέχει.
- `TITLE`: σε ποια ταινία συμμετέχει.
- `ROLE`: ποιον ρόλο παίζει.
- `CACHE`: ποια είναι η αμοιβή του.
- `PRIMARY KEY (ID, TITLE)`: κάθε ζεύγος ηθοποιού–ταινίας είναι μοναδικό.

### Parameter Reference

| Όνομα | Τιμές / Τύπος | Required | Default | Περιγραφή |
| :--- | :--- | :---: | :---: | :--- |
| `<γνώρισμα_ξένο_κλειδί>` | Στήλη ή λίστα στηλών | Ναι | Καμία | Το πεδίο του τρέχοντος πίνακα που αναφέρεται αλλού. |
| `<πίνακας_αναφοράς>` | Αναγνωριστικό SQL | Ναι | Καμία | Ο πίνακας που περιέχει τις έγκυρες τιμές. |
| `<γνώρισμα_αναφοράς>` | Στήλη | Ναι | Καμία | Το πεδίο του πίνακα αναφοράς, συνήθως πρωτεύον κλειδί. |

---

## 9. Συνοπτικός πίνακας εντολών

| Εντολή | Σκοπός | Βασική μορφή |
| :--- | :--- | :--- |
| `CREATE DATABASE` | Δημιουργία βάσης | `CREATE DATABASE <όνομα_ΒΔ>;` |
| `USE` | Επιλογή ενεργής βάσης | `USE <όνομα_ΒΔ>;` |
| `CREATE TABLE` | Δημιουργία πίνακα | `CREATE TABLE <πίνακας> (...);` |
| `ALTER TABLE ... ADD` | Προσθήκη στήλης | `ALTER TABLE <πίνακας> ADD <πεδίο> <τύπος>;` |
| `ALTER TABLE ... MODIFY` | Αλλαγή τύπου πεδίου | `ALTER TABLE <πίνακας> MODIFY <πεδίο> <τύπος>;` |
| `ALTER TABLE ... DROP COLUMN` | Διαγραφή στήλης | `ALTER TABLE <πίνακας> DROP COLUMN <πεδίο>;` |
| `ALTER TABLE ... CHANGE` | Μετονομασία πεδίου | `ALTER TABLE <πίνακας> CHANGE <παλιό> <νέο> <τύπος>;` |
| `DESCRIBE` | Προβολή σχήματος | `DESCRIBE <πίνακας>;` |
| `INSERT INTO` | Εισαγωγή μίας γραμμής | `INSERT INTO <πίνακας> VALUES (...);` |
| `SELECT` | Προβολή δεδομένων | `SELECT ... FROM <πίνακας>;` |
| `UPDATE` | Τροποποίηση γραμμών | `UPDATE <πίνακας> SET ... WHERE ...;` |
| `DELETE` | Διαγραφή γραμμών | `DELETE FROM <πίνακας> WHERE ...;` |
| `FOREIGN KEY` | Σύνδεση πινάκων | `FOREIGN KEY (...) REFERENCES ...(... )` |

---

## 10. Solved Exercises

### Exercise 1: Δημιουργία και επιλογή βάσης

**Problem:** Να δημιουργηθεί η βάση `Hollywood` και να οριστεί ως ενεργή.

**Solution:**
1. Δημιουργούμε τη βάση με `CREATE DATABASE`.
2. Την επιλέγουμε με `USE`.

```sql
CREATE DATABASE Hollywood;
USE Hollywood;
```

```text
Η βάση Hollywood δημιουργείται και γίνεται η ενεργή βάση.
```

### Exercise 2: Δημιουργία πίνακα `ACTORS`

**Problem:** Να δημιουργηθεί πίνακας ηθοποιών με πρωτεύον κλειδί το `ID` και με `NAME` που δεν επιτρέπεται να είναι `NULL`.

**Solution:**
1. Ορίζουμε τα πεδία του πίνακα.
2. Θέτουμε `NOT NULL` στο `NAME`.
3. Θέτουμε `PRIMARY KEY (ID)`.

```sql
CREATE TABLE ACTORS (
  ID varchar(10),
  NAME varchar(20) not null,
  BIRTHDATE date,
  BIRTHPLACE varchar(20),
  OSCARS int,
  PRIMARY KEY (ID)
);
```

```text
Ο πίνακας ACTORS δημιουργείται με μοναδικό αναγνωριστικό το ID.
```

### Exercise 3: Προσθήκη νέου πεδίου σε υπάρχον πίνακα

**Problem:** Στον πίνακα `MOVIES` να προστεθεί πεδίο `DURATION`.

**Solution:**
1. Χρησιμοποιούμε `ALTER TABLE` γιατί ο πίνακας υπάρχει ήδη.
2. Προσθέτουμε το πεδίο με `ADD`.
3. Επιβεβαιώνουμε το νέο σχήμα με `DESCRIBE`.

```sql
ALTER TABLE MOVIES ADD DURATION varchar(6);
DESCRIBE MOVIES;
```

```text
Το πεδίο DURATION προστίθεται στο σχήμα του πίνακα MOVIES.
```

### Exercise 4: Αλλαγή τύπου πεδίου

**Problem:** Το `DURATION` να αλλάξει από `varchar(6)` σε `int`.

**Solution:**
1. Χρησιμοποιούμε `MODIFY` για αλλαγή τύπου.
2. Δεν αλλάζουμε το όνομα του πεδίου.
3. Ο νέος τύπος αποθηκεύει διάρκεια σε ακέραια λεπτά.

```sql
ALTER TABLE MOVIES MODIFY DURATION int;
```

```text
Το πεδίο DURATION παραμένει ίδιο ονομαστικά αλλά αλλάζει τύπο σε int.
```

### Exercise 5: Εισαγωγή πλήρους εγγραφής

**Problem:** Να εισαχθεί ο ηθοποιός Brad Pitt στον πίνακα `ACTORS`.

**Solution:**
1. Δίνουμε τιμή για όλα τα πεδία με τη σωστή σειρά.
2. Οι συμβολοσειρές και η ημερομηνία γράφονται σε μονά εισαγωγικά.
3. Επειδή δεν δίνεται αριθμός Oscar, το πεδίο παίρνει `NULL`.

```sql
INSERT INTO ACTORS VALUES ('A01', 'Brad Pitt', '1963-12-18', 'Oklahoma', NULL);
```

```text
Μία νέα γραμμή προστίθεται στον πίνακα ACTORS.
```

### Exercise 6: Εισαγωγή μερικών πεδίων μόνο

**Problem:** Να εισαχθεί ο `George Clooney` δίνοντας μόνο `ID` και `NAME`.

**Solution:**
1. Χρησιμοποιούμε τη μορφή `INSERT INTO <πίνακας> (<λίστα_πεδίων>) VALUES (...)`.
2. Δηλώνουμε μόνο τα πεδία που έχουν διαθέσιμες τιμές.
3. Τα υπόλοιπα πεδία γίνονται αυτόματα `NULL`.

```sql
INSERT INTO ACTORS (ID, NAME) VALUES ('A06', 'George Clooney');
```

```text
Η νέα εγγραφή εισάγεται και τα μη δηλωμένα πεδία μένουν κενά (NULL).
```

### Exercise 7: Προβολή όλων ή επιλεγμένων πεδίων

**Problem:** Να εμφανιστούν πρώτα όλα τα πεδία του `ACTORS` και μετά μόνο τα `NAME`, `OSCARS`.

**Solution:**
1. Για όλα τα πεδία χρησιμοποιούμε `*`.
2. Για συγκεκριμένες στήλες γράφουμε λίστα πεδίων.
3. Και στις δύο περιπτώσεις απαιτείται `FROM ACTORS`.

```sql
SELECT *
FROM ACTORS;

SELECT NAME, OSCARS
FROM ACTORS;
```

```text
Το πρώτο ερώτημα επιστρέφει όλο τον πίνακα, ενώ το δεύτερο μόνο τις στήλες NAME και OSCARS.
```

### Exercise 8: Στοχευμένη τροποποίηση εγγραφής

**Problem:** Να αλλάξει η ημερομηνία γέννησης του ηθοποιού με `ID = 'A01'` σε `1968-08-15`.

**Solution:**
1. Χρησιμοποιούμε `UPDATE` για υπάρχουσα γραμμή.
2. Το `SET` ορίζει τη νέα τιμή.
3. Το `WHERE ID = 'A01'` περιορίζει την αλλαγή μόνο σε μία εγγραφή.

```sql
UPDATE ACTORS
SET BIRTHDATE = '1968-08-15'
WHERE ID = 'A01';
```

```text
Τροποποιείται μόνο η γραμμή του ηθοποιού με ID A01.
```

### Exercise 9: Στοχευμένη διαγραφή εγγραφής

**Problem:** Να διαγραφεί ο ηθοποιός με `ID = 'A01'`.

**Solution:**
1. Χρησιμοποιούμε `DELETE FROM` για διαγραφή γραμμής.
2. Με `WHERE ID = 'A01'` στοχεύουμε μία μόνο εγγραφή.
3. Αν το `WHERE` παραλειφθεί, θα σβηστούν όλες οι γραμμές.

```sql
DELETE FROM ACTORS
WHERE ID = 'A01';
```

```text
Διαγράφεται μόνο η εγγραφή με ID A01.
```

### Exercise 10: Δημιουργία πίνακα συσχέτισης με ξένα κλειδιά

**Problem:** Να δημιουργηθεί πίνακας `STARS` που συνδέει ηθοποιούς και ταινίες και να περιέχει και το όνομα ρόλου και την αμοιβή.

**Solution:**
1. Δημιουργούμε πεδία για `ID`, `TITLE`, `ROLE`, `CACHE`.
2. Ορίζουμε σύνθετο πρωτεύον κλειδί `(ID, TITLE)` ώστε κάθε ζεύγος να είναι μοναδικό.
3. Δηλώνουμε `ID` ως ξένο κλειδί προς `ACTORS(ID)` και `TITLE` ως ξένο κλειδί προς `MOVIES(TITLE)`.

```sql
CREATE TABLE STARS (
  ID VARCHAR(10),
  TITLE VARCHAR(50),
  ROLE VARCHAR(30),
  CACHE REAL,
  PRIMARY KEY (ID, TITLE),
  FOREIGN KEY (ID) REFERENCES ACTORS(ID),
  FOREIGN KEY (TITLE) REFERENCES MOVIES(TITLE)
);
```

```text
Ο πίνακας STARS δημιουργείται και επιβάλλει σύνδεση μόνο με υπαρκτούς ηθοποιούς και υπαρκτές ταινίες.
```

---

## 11. Common Errors and Gotchas

### 1. Λάθος εισαγωγικά ή λάθος χρήση του `NULL`

- Λάθος: `"NULL"` ή `'NULL'` όταν θέλουμε πραγματικά κενή τιμή.
- Σωστό: `NULL` χωρίς εισαγωγικά.
- Αιτία: Με εισαγωγικά αποθηκεύεται η λέξη `NULL` ως κείμενο και όχι κενή τιμή.

### 2. Παράλειψη του `WHERE` σε `UPDATE`

- Πρόβλημα: Ενημερώνονται όλες οι γραμμές του πίνακα.
- Αιτία: Η `UPDATE` χωρίς `WHERE` δεν περιορίζει ποιες εγγραφές αλλάζουν.
- Λύση: Πάντα έλεγχος της συνθήκης πριν την εκτέλεση.

### 3. Παράλειψη του `WHERE` σε `DELETE`

- Πρόβλημα: Διαγράφονται όλες οι πλειάδες του πίνακα.
- Αιτία: Η `DELETE FROM <πίνακας>;` εφαρμόζεται παντού.
- Λύση: Να γράφεται πάντα σαφής συνθήκη εκτός αν ο στόχος είναι πλήρες άδειασμα πίνακα.

### 4. Σύγχυση ανάμεσα σε `MODIFY` και `CHANGE`

- `MODIFY`: αλλάζει τύπο πεδίου.
- `CHANGE`: αλλάζει όνομα πεδίου και δηλώνει ξανά τον τύπο.
- Πρακτικό αποτέλεσμα: Αν θέλεις μετονομασία, δεν αρκεί η `MODIFY`.

### 5. Παραβίαση ξένου κλειδιού

- Πρόβλημα: Προσπάθεια εισαγωγής τιμής σε ξένο κλειδί που δεν υπάρχει στον πίνακα αναφοράς.
- Αιτία: Η αναφορική ακεραιότητα απαιτεί ήδη υπάρχουσες τιμές.
- Λύση: Πρώτα εισάγουμε τις εγγραφές στους βασικούς πίνακες και μετά στον πίνακα συσχέτισης.

---

## 12. Exam Tip: Αναγνώριση μοτίβου εντολής

- Αν αλλάζει το σχήμα πίνακα, σκέψου `ALTER TABLE`.
- Αν μπαίνει νέα γραμμή, σκέψου `INSERT INTO`.
- Αν προβάλλονται δεδομένα, σκέψου `SELECT`.
- Αν αλλάζει υπάρχουσα τιμή, σκέψου `UPDATE`.
- Αν σβήνεται γραμμή, σκέψου `DELETE`.
- Αν συνδέονται δύο πίνακες, αναζήτησε πρωτεύον κλειδί και μετά όρισε ξένα κλειδιά.

---

## 13. Mini Checklist για εργαστήριο

1. Δημιούργησε ή επίλεξε τη σωστή βάση με `CREATE DATABASE` / `USE`.
2. Έλεγξε ότι κάθε πίνακας έχει σαφές `PRIMARY KEY`.
3. Στις εισαγωγές, πρόσεξε σειρά τιμών και σωστά εισαγωγικά.
4. Πριν από `UPDATE` ή `DELETE`, έλεγξε δύο φορές το `WHERE`.
5. Σε πίνακες συσχέτισης, όρισε σωστά και τα δύο `FOREIGN KEY`.

========================================================================================================================

# Lab 4 notes.md
========================================================================================================================
# vaseis_dedomenon_ergastirio_5_notes

Οι σημειώσεις καλύπτουν τις βασικές εντολές SQL που εμφανίζονται στο εργαστήριο: δημιουργία και επιλογή βάσης δεδομένων, δημιουργία πινάκων, πρωτεύοντα και ξένα κλειδιά, μεταβολές σχήματος με `ALTER TABLE`, καθώς και βασικό χειρισμό δεδομένων με `INSERT`, `UPDATE` και `DELETE`. Το παράδειγμα του υλικού βασίζεται στη βάση `Hollywood` και στους πίνακες `ACTORS`, `MOVIES` και `STARS`.

---

## 1. Concept Overview

Η SQL χρησιμοποιείται για δύο βασικές κατηγορίες ενεργειών στο παρόν υλικό:

- Ορισμό και μεταβολή του σχήματος της βάσης δεδομένων.
- Εισαγωγή, ενημέρωση και διαγραφή δεδομένων.

Η λογική του παραδείγματος είναι ότι:

- Ο πίνακας `ACTORS` αποθηκεύει στοιχεία ηθοποιών.
- Ο πίνακας `MOVIES` αποθηκεύει στοιχεία ταινιών.
- Ο πίνακας `STARS` συνδέει ηθοποιούς με ταινίες και αποθηκεύει επιπλέον γνωρίσματα της συμμετοχής τους, όπως τον ρόλο και την αμοιβή.

> **[Key Insight]**
> Ο πίνακας `STARS` υλοποιεί σχέση πολλών-προς-πολλά μεταξύ `ACTORS` και `MOVIES`. Ένας ηθοποιός μπορεί να παίζει σε πολλές ταινίες και μία ταινία μπορεί να έχει πολλούς ηθοποιούς.

---

## 2. Βασικές εντολές βάσης δεδομένων

### Syntax Reference

```sql
CREATE DATABASE <database_name>;
CREATE SCHEMA <database_name>;
SHOW DATABASES;
SHOW SCHEMAS;
DROP DATABASE <database_name>;
DROP SCHEMA <database_name>;
USE <database_name>;
```

### Behavioral Description

- `CREATE DATABASE` / `CREATE SCHEMA`: δημιουργεί νέα βάση δεδομένων.
- `SHOW DATABASES` / `SHOW SCHEMAS`: εμφανίζει τις διαθέσιμες βάσεις.
- `DROP DATABASE` / `DROP SCHEMA`: διαγράφει ολόκληρη βάση δεδομένων.
- `USE <database_name>`: ορίζει ποια βάση είναι ενεργή για τις επόμενες εντολές.

### Parameter Reference

| Name | Type/Values | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `<database_name>` | Έγκυρο όνομα βάσης | Ναι | Κανένα | Το όνομα της βάσης που δημιουργείται, επιλέγεται ή διαγράφεται. |

### Παράδειγμα

```sql
CREATE DATABASE Hollywood;
USE Hollywood;
SHOW DATABASES;
```

```text
Δημιουργείται η βάση Hollywood, ορίζεται ως ενεργή και στη λίστα βάσεων εμφανίζεται το Hollywood.
```

---

## 3. CREATE TABLE και πρωτεύοντα κλειδιά

### Syntax Reference

```sql
CREATE TABLE <table_name> (
    <field_1> <type_1> [constraints],
    <field_2> <type_2> [constraints],
    ...,
    PRIMARY KEY (<field_or_fields>)
);
```

### Behavioral Description

Η `CREATE TABLE` δημιουργεί έναν νέο πίνακα και ορίζει:

- τα ονόματα των στηλών,
- τους τύπους δεδομένων,
- τυχόν περιορισμούς όπως `NOT NULL`,
- το πρωτεύον κλειδί με `PRIMARY KEY`.

Το πρωτεύον κλειδί:

- αναγνωρίζει μοναδικά κάθε γραμμή,
- δεν επιτρέπεται να είναι `NULL`,
- μπορεί να αποτελείται από ένα ή περισσότερα πεδία.

### Parameter Reference

| Name | Type/Values | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `<table_name>` | Όνομα πίνακα | Ναι | Κανένα | Το όνομα του νέου πίνακα. |
| `<field_n>` | Όνομα πεδίου | Ναι | Κανένα | Στήλη του πίνακα. |
| `<type_n>` | `varchar(n)`, `int`, `date`, `real`, κ.ά. | Ναι | Κανένα | Τύπος δεδομένων της στήλης. |
| `constraints` | `NOT NULL`, κ.ά. | Όχι | Κανένα | Πρόσθετοι περιορισμοί στο πεδίο. |
| `PRIMARY KEY (...)` | Ένα ή περισσότερα πεδία | Ναι | Κανένα | Μοναδικός προσδιοριστής εγγραφών. |

### Παράδειγμα πίνακα `ACTORS`

```sql
CREATE TABLE ACTORS (
    ID varchar(10),
    NAME varchar(20) NOT NULL,
    BIRTHDATE date,
    BIRTHPLACE varchar(20),
    OSCARS int,
    PRIMARY KEY (ID)
);
```

```text
Δημιουργείται πίνακας ηθοποιών με πρωτεύον κλειδί το ID.
```

### Παράδειγμα πίνακα `MOVIES`

```sql
CREATE TABLE MOVIES (
    TITLE varchar(50),
    YEAR date,
    DIRECTOR varchar(50),
    BUDGET int,
    TICKETS int,
    PRIMARY KEY (TITLE)
);
```

```text
Δημιουργείται πίνακας ταινιών με πρωτεύον κλειδί το TITLE.
```

---

## 4. Ξένα κλειδιά και σύνδεση πινάκων

### Θεωρία

Ξένο κλειδί είναι ένα πεδίο ή συνδυασμός πεδίων ενός πίνακα, του οποίου οι τιμές πρέπει να υπάρχουν ήδη σε πεδίο άλλου πίνακα. Με αυτόν τον τρόπο εξασφαλίζεται αναφορική ακεραιότητα.

Στο παράδειγμα:

- το `ACTORS(ID)` είναι το πρωτεύον κλειδί των ηθοποιών,
- το `MOVIES(TITLE)` είναι το πρωτεύον κλειδί των ταινιών,
- ο πίνακας `STARS` περιέχει αυτά τα δύο πεδία ως ξένα κλειδιά.

### Syntax Reference

```sql
CREATE TABLE <table_name> (
    ...,
    FOREIGN KEY (<foreign_key_field>) REFERENCES <referenced_table>(<referenced_field>)
);
```

### Behavioral Description

- Το ξένο κλειδί επιτρέπει μόνο τιμές που υπάρχουν ήδη στον πίνακα αναφοράς.
- Αν μια τιμή δεν υπάρχει στον αναφερόμενο πίνακα, η εισαγωγή απορρίπτεται.
- Σε πίνακες συσχέτισης είναι συνηθισμένο να ορίζεται σύνθετο πρωτεύον κλειδί από τα ξένα κλειδιά.

### Parameter Reference

| Name | Type/Values | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `<foreign_key_field>` | Πεδίο τοπικού πίνακα | Ναι | Κανένα | Η στήλη που θα δείχνει σε άλλο πίνακα. |
| `<referenced_table>` | Όνομα πίνακα | Ναι | Κανένα | Ο πίνακας στον οποίο γίνεται αναφορά. |
| `<referenced_field>` | Πεδίο πίνακα αναφοράς | Ναι | Κανένα | Το πεδίο που πρέπει ήδη να περιέχει τις τιμές. |

### Παράδειγμα πίνακα `STARS`

```sql
CREATE TABLE STARS (
    ID VARCHAR(10),
    TITLE VARCHAR(50),
    ROLE VARCHAR(30),
    CACHE REAL,
    PRIMARY KEY (ID, TITLE),
    FOREIGN KEY (ID) REFERENCES ACTORS(ID),
    FOREIGN KEY (TITLE) REFERENCES MOVIES(TITLE)
);
```

```text
Δημιουργείται πίνακας συσχέτισης ηθοποιών-ταινιών. Κάθε γραμμή αντιστοιχεί σε μία συμμετοχή ηθοποιού σε μία ταινία.
```

> **[Key Insight]**
> Το σύνθετο πρωτεύον κλειδί `(ID, TITLE)` σημαίνει ότι ο ίδιος ηθοποιός δεν μπορεί να εμφανιστεί δύο φορές για την ίδια ταινία στον `STARS`.

---

## 5. ALTER TABLE

Η `ALTER TABLE` χρησιμοποιείται όταν ο πίνακας υπάρχει ήδη και θέλουμε να αλλάξουμε το σχήμα του.

### 5.1 Προσθήκη πεδίου

#### Syntax Reference

```sql
ALTER TABLE <table_name> ADD <field_name> <field_type>;
```

#### Example

```sql
ALTER TABLE MOVIES ADD DURATION varchar(6);
```

```text
Προστίθεται η στήλη DURATION στον πίνακα MOVIES.
```

### 5.2 Αλλαγή τύπου πεδίου

#### Syntax Reference

```sql
ALTER TABLE <table_name> MODIFY <field_name> <new_type>;
```

#### Behavioral Description

Η `MODIFY` αλλάζει μόνο τον τύπο του πεδίου και όχι το όνομά του.

#### Example

```sql
ALTER TABLE MOVIES MODIFY DURATION int;
```

```text
Η στήλη DURATION μετατρέπεται από varchar(6) σε int.
```

### 5.3 Διαγραφή πεδίου

#### Syntax Reference

```sql
ALTER TABLE <table_name> DROP COLUMN <field_name>;
```

#### Behavioral Description

Η διαγραφή στήλης συνεπάγεται απώλεια δεδομένων που βρίσκονται σε αυτήν τη στήλη.

#### Example

```sql
ALTER TABLE MOVIES DROP COLUMN DURATION;
```

```text
Η στήλη DURATION διαγράφεται από τον πίνακα MOVIES.
```

### 5.4 Μετονομασία πεδίου

#### Syntax Reference

```sql
ALTER TABLE <table_name> CHANGE <old_name> <new_name> <data_type>;
```

#### Example

```sql
ALTER TABLE ACTORS CHANGE BIRTHDATE DATE_OF_BIRTH DATE;
```

```text
Το πεδίο BIRTHDATE μετονομάζεται σε DATE_OF_BIRTH και δηλώνεται ο τύπος DATE.
```

### Parameter Reference

| Name | Type/Values | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `<table_name>` | Όνομα πίνακα | Ναι | Κανένα | Ο πίνακας που θα αλλάξει. |
| `<field_name>` | Όνομα πεδίου | Ναι | Κανένα | Το πεδίο που προστίθεται/μεταβάλλεται/διαγράφεται. |
| `<field_type>` | Τύπος SQL | Ναι στο `ADD` | Κανένα | Τύπος νέας στήλης. |
| `<new_type>` | Τύπος SQL | Ναι στο `MODIFY` | Κανένα | Νέος τύπος υπάρχουσας στήλης. |
| `<old_name>` | Παλιό όνομα | Ναι στο `CHANGE` | Κανένα | Το τρέχον όνομα της στήλης. |
| `<new_name>` | Νέο όνομα | Ναι στο `CHANGE` | Κανένα | Το νέο όνομα της στήλης. |
| `<data_type>` | Τύπος SQL | Ναι στο `CHANGE` | Κανένα | Ο τύπος που πρέπει να δηλωθεί ξανά. |

---

## 6. INSERT INTO

### Syntax Reference

```sql
INSERT INTO <table_name> VALUES (<value_1>, <value_2>, ...);
```

ή

```sql
INSERT INTO <table_name> (<field_list>) VALUES (<value_list>);
```

### Behavioral Description

- Κάθε `INSERT` εισάγει μία μόνο γραμμή σε έναν μόνο πίνακα.
- Αν χρησιμοποιηθεί η πλήρης μορφή με `VALUES (...)`, πρέπει να δοθεί τιμή για κάθε πεδίο.
- Αν δεν θέλουμε τιμή σε κάποιο πεδίο, γράφουμε `NULL`.
- Αν χρησιμοποιηθεί μορφή με λίστα πεδίων, όσα πεδία δεν δοθούν παίρνουν `NULL`.
- Τα πεδία `NOT NULL` και το πρωτεύον κλειδί πρέπει να πάρουν έγκυρη τιμή.

### Parameter Reference

| Name | Type/Values | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `<table_name>` | Όνομα πίνακα | Ναι | Κανένα | Ο πίνακας εισαγωγής. |
| `<field_list>` | Λίστα πεδίων | Όχι | Όλα τα πεδία | Ποια πεδία θα πάρουν ρητές τιμές. |
| `<value_list>` | Λίστα τιμών | Ναι | Κανένα | Οι τιμές που θα εισαχθούν. |

### Παραδείγματα

```sql
INSERT INTO ACTORS VALUES ('A02', 'Angelina Jolie', '1975-06-04', 'California', NULL);
INSERT INTO ACTORS VALUES ('A03', 'Leonardo DiCaprio', '1974-11-11', 'Los Angeles', NULL);
INSERT INTO ACTORS VALUES ('A04', 'Morgan Freeman', '1937-06-01', 'Tennessee', NULL);
INSERT INTO ACTORS VALUES ('A05', 'Meryl Streep', '1949-06-22', 'New Jersey', NULL);
```

```text
Εισάγονται τέσσερις διαφορετικές γραμμές στον πίνακα ACTORS, μία ανά εντολή INSERT.
```

```sql
INSERT INTO ACTORS (ID, NAME) VALUES ('A06', 'George Clooney');
```

```text
Εισάγεται νέα γραμμή όπου τα υπόλοιπα πεδία παίρνουν την τιμή NULL.
```

---

## 7. UPDATE και DELETE

### 7.1 UPDATE

#### Syntax Reference

```sql
UPDATE <table_name>
SET <field_name> = <new_value>
WHERE <condition>;
```

#### Behavioral Description

- Το `SET` δηλώνει ποια αλλαγή θέλουμε.
- Το `WHERE` δηλώνει σε ποιες γραμμές θα εφαρμοστεί.
- Αν παραλειφθεί το `WHERE`, η αλλαγή εφαρμόζεται σε όλες τις γραμμές του πίνακα.

#### Example

```sql
UPDATE ACTORS
SET BIRTHDATE = '1968-08-15'
WHERE ID = 'A01';
```

```text
Ενημερώνεται η ημερομηνία γέννησης μόνο του ηθοποιού με ID A01.
```

### 7.2 DELETE

#### Syntax Reference

```sql
DELETE FROM <table_name>
WHERE <condition>;
```

#### Behavioral Description

- Διαγράφει όσες γραμμές ικανοποιούν τη συνθήκη.
- Αν παραλειφθεί το `WHERE`, διαγράφονται όλες οι γραμμές.
- Ο πίνακας συνεχίζει να υπάρχει, αλλά μένει κενός.

#### Example

```sql
DELETE FROM ACTORS
WHERE ID = 'A01';
```

```text
Διαγράφεται μόνο η γραμμή του ηθοποιού με ID A01.
```

```sql
DELETE FROM ACTORS;
```

```text
Διαγράφονται όλες οι γραμμές του πίνακα ACTORS, αλλά ο πίνακας παραμένει στη βάση.
```

---

## 8. Common Errors and Gotchas

### 8.1 Παράλειψη `WHERE` σε `UPDATE`

**Σφάλμα:**

```sql
UPDATE ACTORS
SET BIRTHDATE = '1968-08-15';
```

**Τι συμβαίνει:** αλλάζει η ημερομηνία γέννησης σε όλες τις εγγραφές.

**Αντιμετώπιση:** πάντα έλεγχος ότι υπάρχει σωστή συνθήκη `WHERE` πριν την εκτέλεση.

### 8.2 Παράλειψη `WHERE` σε `DELETE`

**Σφάλμα:**

```sql
DELETE FROM ACTORS;
```

**Τι συμβαίνει:** σβήνονται όλα τα δεδομένα του πίνακα.

**Αντιμετώπιση:** πρώτα δοκιμή της συνθήκης με `SELECT`, μετά `DELETE`.

### 8.3 Εισαγωγή άκυρου ξένου κλειδιού

**Σφάλμα:** εισαγωγή εγγραφής σε `STARS` με `ID` ή `TITLE` που δεν υπάρχει ήδη.

**Τι συμβαίνει:** η εισαγωγή απορρίπτεται λόγω παραβίασης αναφορικής ακεραιότητας.

**Αντιμετώπιση:** πρώτα εισαγωγή στον γονικό πίνακα (`ACTORS` ή `MOVIES`), μετά στον `STARS`.

### 8.4 Μη παροχή τιμής σε `NOT NULL` πεδίο

**Σφάλμα:** εισαγωγή γραμμής χωρίς τιμή στο `NAME` του `ACTORS`.

**Τι συμβαίνει:** η εντολή αποτυγχάνει επειδή το πεδίο έχει περιορισμό `NOT NULL`.

**Αντιμετώπιση:** πάντα έλεγχος των περιορισμών πριν το `INSERT`.

---

## Solved Exercises

### Exercise 1: Δημιουργία και επιλογή βάσης

**Problem:** Να δημιουργηθεί η βάση `Hollywood` και να οριστεί ως ενεργή.

**Solution:**

1. Δημιουργούμε τη βάση με `CREATE DATABASE`.
2. Την ενεργοποιούμε με `USE`.

```sql
CREATE DATABASE Hollywood;
USE Hollywood;
```

```text
Η βάση Hollywood δημιουργείται και επιλέγεται ως ενεργή βάση εργασίας.
```

### Exercise 2: Δημιουργία πίνακα ηθοποιών

**Problem:** Να δημιουργηθεί ο πίνακας `ACTORS` με πρωτεύον κλειδί το `ID` και υποχρεωτικό το `NAME`.

**Solution:**

1. Ορίζουμε τα πεδία του πίνακα.
2. Βάζουμε `NOT NULL` στο `NAME`.
3. Ορίζουμε `PRIMARY KEY (ID)`.

```sql
CREATE TABLE ACTORS (
    ID varchar(10),
    NAME varchar(20) NOT NULL,
    BIRTHDATE date,
    BIRTHPLACE varchar(20),
    OSCARS int,
    PRIMARY KEY (ID)
);
```

```text
Ο πίνακας δημιουργείται και κάθε ηθοποιός ταυτοποιείται μοναδικά από το ID.
```

### Exercise 3: Δημιουργία πίνακα ταινιών

**Problem:** Να δημιουργηθεί ο πίνακας `MOVIES` με πρωτεύον κλειδί το `TITLE`.

**Solution:**

1. Ορίζουμε τα πέντε πεδία του πίνακα.
2. Θέτουμε πρωτεύον κλειδί στο `TITLE`.

```sql
CREATE TABLE MOVIES (
    TITLE varchar(50),
    YEAR date,
    DIRECTOR varchar(50),
    BUDGET int,
    TICKETS int,
    PRIMARY KEY (TITLE)
);
```

```text
Ο πίνακας MOVIES δημιουργείται με μοναδικό αναγνωριστικό τον τίτλο.
```

### Exercise 4: Δημιουργία πίνακα συσχέτισης

**Problem:** Να δημιουργηθεί πίνακας `STARS` που να συνδέει ηθοποιούς και ταινίες και να αποθηκεύει τον ρόλο και την αμοιβή.

**Solution:**

1. Χρειαζόμαστε πεδία `ID`, `TITLE`, `ROLE`, `CACHE`.
2. Το `ID` θα αναφέρεται στο `ACTORS(ID)`.
3. Το `TITLE` θα αναφέρεται στο `MOVIES(TITLE)`.
4. Για να μην υπάρχουν διπλές συμμετοχές για το ίδιο ζεύγος, ορίζουμε σύνθετο πρωτεύον κλειδί `(ID, TITLE)`.

```sql
CREATE TABLE STARS (
    ID VARCHAR(10),
    TITLE VARCHAR(50),
    ROLE VARCHAR(30),
    CACHE REAL,
    PRIMARY KEY (ID, TITLE),
    FOREIGN KEY (ID) REFERENCES ACTORS(ID),
    FOREIGN KEY (TITLE) REFERENCES MOVIES(TITLE)
);
```

```text
Ο πίνακας STARS δημιουργείται ως πίνακας συσχέτισης πολλών-προς-πολλά.
```

### Exercise 5: Προσθήκη και αλλαγή τύπου πεδίου

**Problem:** Να προστεθεί η στήλη `DURATION` στον πίνακα `MOVIES` και στη συνέχεια να αλλάξει ο τύπος της σε `int`.

**Solution:**

1. Αρχικά προσθέτουμε τη στήλη ως `varchar(6)`.
2. Μετά τη μετατρέπουμε σε `int`.
3. Ενδιάμεση κατάσταση: ο πίνακας έχει πλέον τη στήλη `DURATION`, αλλά αρχικά είναι συμβολοσειρά.
4. Τελική κατάσταση: η `DURATION` αποθηκεύει ακέραια λεπτά.

```sql
ALTER TABLE MOVIES ADD DURATION varchar(6);
ALTER TABLE MOVIES MODIFY DURATION int;
```

```text
Πρώτα προστίθεται η στήλη DURATION και στη συνέχεια αλλάζει ο τύπος της σε int.
```

### Exercise 6: Εισαγωγή πλήρους εγγραφής

**Problem:** Να εισαχθεί ο ηθοποιός Angelina Jolie με πλήρη στοιχεία, εκτός από τα Oscar που θα είναι άγνωστα.

**Solution:**

1. Χρησιμοποιούμε πλήρη μορφή `INSERT INTO ... VALUES (...)`.
2. Δίνουμε τιμή σε όλα τα πεδία με τη σωστή σειρά.
3. Για άγνωστο πλήθος Oscar, βάζουμε `NULL`.

```sql
INSERT INTO ACTORS VALUES ('A02', 'Angelina Jolie', '1975-06-04', 'California', NULL);
```

```text
Η εγγραφή της Angelina Jolie προστίθεται στον πίνακα ACTORS.
```

### Exercise 7: Εισαγωγή μερικών πεδίων

**Problem:** Να εισαχθεί ο George Clooney δίνοντας μόνο `ID` και `NAME`.

**Solution:**

1. Χρησιμοποιούμε τη μορφή `INSERT INTO <table> (<fields>) VALUES (...)`.
2. Δηλώνουμε μόνο τα πεδία που έχουν διαθέσιμες τιμές.
3. Τα υπόλοιπα πεδία παίρνουν `NULL`.

```sql
INSERT INTO ACTORS (ID, NAME) VALUES ('A06', 'George Clooney');
```

```text
Η εγγραφή προστίθεται και τα BIRTHDATE, BIRTHPLACE, OSCARS γίνονται NULL.
```

### Exercise 8: Ενημέρωση συγκεκριμένης εγγραφής

**Problem:** Να αλλάξει η ημερομηνία γέννησης του ηθοποιού με `ID = 'A01'` σε `1968-08-15`.

**Solution:**

1. Επιλέγουμε τον πίνακα `ACTORS`.
2. Με `SET` ορίζουμε τη νέα τιμή.
3. Με `WHERE ID = 'A01'` περιορίζουμε την αλλαγή σε μία μόνο γραμμή.

```sql
UPDATE ACTORS
SET BIRTHDATE = '1968-08-15'
WHERE ID = 'A01';
```

```text
Ενημερώνεται μόνο η εγγραφή με πρωτεύον κλειδί A01.
```

### Exercise 9: Διαγραφή συγκεκριμένης εγγραφής

**Problem:** Να διαγραφεί ο ηθοποιός με `ID = 'A01'`.

**Solution:**

1. Χρησιμοποιούμε `DELETE FROM ACTORS`.
2. Περιορίζουμε τη διαγραφή με `WHERE ID = 'A01'`.
3. Άρα επηρεάζεται μία μόνο εγγραφή.

```sql
DELETE FROM ACTORS
WHERE ID = 'A01';
```

```text
Η γραμμή του ηθοποιού A01 αφαιρείται από τον πίνακα ACTORS.
```

### Exercise 10: Επικίνδυνη καθολική διαγραφή

**Problem:** Τι συμβαίνει αν εκτελεστεί η εντολή `DELETE FROM ACTORS;` χωρίς `WHERE`;

**Solution:**

1. Η εντολή δεν περιέχει συνθήκη φιλτραρίσματος.
2. Άρα η διαγραφή εφαρμόζεται σε όλες τις γραμμές.
3. Ενδιάμεση λογική: ο πίνακας παραμένει ορισμένος στο σχήμα της βάσης, αλλά το περιεχόμενό του μηδενίζεται.
4. Τελικό αποτέλεσμα: δεν υπάρχει καμία εγγραφή στον `ACTORS`.

```sql
DELETE FROM ACTORS;
```

```text
Όλες οι εγγραφές του ACTORS διαγράφονται, αλλά ο πίνακας συνεχίζει να υπάρχει.
```

---

## Exam Tip: Αναγνώριση τύπου εντολής

- Αν αλλάζει το σχήμα της βάσης ή ενός πίνακα, σκέψου `CREATE`, `DROP`, `ALTER`.
- Αν αλλάζουν τα ίδια τα δεδομένα, σκέψου `INSERT`, `UPDATE`, `DELETE`.
- Σε `UPDATE` και `DELETE`, η πιο συχνή παγίδα εξετάσεων είναι η παράλειψη του `WHERE`.
- Σε σχέσεις πολλών-προς-πολλά, συνήθως χρειάζεται ενδιάμεσος πίνακας με δύο ξένα κλειδιά και συχνά σύνθετο πρωτεύον κλειδί.

========================================================================================================================
