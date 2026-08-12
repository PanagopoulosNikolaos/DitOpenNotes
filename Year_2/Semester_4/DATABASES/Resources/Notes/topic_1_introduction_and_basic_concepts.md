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
5. [Comparative Table: DBMS vs. File Processing Systems](#comparative-table-dbms-vs-file-processing-systems)
6. [Summary Table of Key Concepts](#summary-table-of-key-concepts)
7. [Key Takeaways](#key-takeaways)

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
