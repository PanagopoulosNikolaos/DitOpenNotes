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
