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
