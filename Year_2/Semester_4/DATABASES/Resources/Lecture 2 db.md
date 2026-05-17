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
