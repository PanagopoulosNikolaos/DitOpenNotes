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
