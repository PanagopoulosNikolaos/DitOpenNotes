# Lecture 01: The Relational Model and Conceptual Database Design

This lecture covers database systems architecture, conceptual data modeling using the Entity-Relationship (ER) model, structural constraints (cardinality ratios and participation constraints), and the formal 7-step mapping algorithm from ER diagrams to relational schemas.

---

## 1. Database Systems Architecture

A Database Management System (DBMS) is specialized system software facilitating the definition, construction, manipulation, and sharing of databases among various users and applications.

### 1.1 The ANSI/SPARC Three-Schema Architecture

```
[ External Level ]   User View 1     User View 2     User View 3
                           \              |              /
                      Logical / Conceptual Data Independence
                             \            |            /
[ Conceptual Level ]          [ Community Conceptual Schema ]
                                          |
                              Physical Data Independence
                                          |
[ Internal Level ]            [ Physical Storage Schema ]
```

- **External Level (Views):** Describes the part of the database that a particular user group is interested in, hiding the rest of the database.
- **Conceptual Level:** Describes the structure of the whole database for a community of users (entities, data types, relationships, user operations, constraints).
- **Internal Level:** Describes the physical storage structure of the database (indexes, record formats, file structures).

---

## 2. Conceptual Data Modeling: The ER Model

Conceptual modeling captures real-world requirements independently of physical implementation.

### 2.1 Core Elements of the ER Model
- **Entities:** Distinct real-world objects or concepts (e.g., `Student`, `Course`, `Department`).
- **Attributes:** Properties describing entities (e.g., `student_id`, `name`, `birth_date`).
  - *Simple / Atomic:* Cannot be divided further.
  - *Composite:* Composed of smaller sub-parts (e.g., `Address` $\to$ `Street`, `City`, `PostalCode`).
  - *Single-valued vs. Multivalued:* An entity has one value vs. a set of values (e.g., `phone_numbers`).
  - *Derived:* Computed from other attributes (e.g., `age` derived from `birth_date`).
- **Key Attributes:** An attribute whose values are distinct for each individual entity in an entity set (underlined in ER diagrams).

### 2.2 Relationship Types and Constraints
- **Relationship:** An association among two or more entities.
- **Cardinality Ratios:**
  - $1:1$ (One-to-One): An employee manages at most one department; a department has at most one manager.
  - $1:N$ (One-to-Many): A department employs many employees; each employee belongs to exactly one department.
  - $M:N$ (Many-to-Many): A student enrolls in many courses; a course has many enrolled students.
- **Participation Constraints:**
  - **Total Participation (Existence Dependency):** Every entity in the entity set must participate in at least one relationship instance (represented by a double line).
  - **Partial Participation:** Some entities may not participate in the relationship (single line).

### 2.3 Weak Entity Types
Entities that do not have key attributes of their own.
- Identified by being related to a parent **identifying entity type** via an **identifying relationship** (represented by double rectangles and double diamonds).
- Possesses a **partial key** (discriminator), underlined with a dashed line.

---

## 3. The 7-Step ER-to-Relational Mapping Algorithm

Transforming an ER conceptual schema into a relational schema follows a formal, deterministic procedure:

| Step | ER Construct | Relational Schema Mapping Transformation | Primary Key Selection |
|---|---|---|---|
| **Step 1** | Regular Entity $E$ | Create relation $R$ containing all atomic attributes of $E$. Flatten composite attributes into atomic components. | Primary key of $E$ becomes Primary Key of $R$. |
| **Step 2** | Weak Entity $W$ | Create relation $R$ containing all atomic attributes of $W$, plus the primary key of the identifying entity as a Foreign Key. | Compound Primary Key: (Identifying PK + Partial Key). |
| **Step 3** | $1:1$ Relationship | Foreign Key approach: Choose one entity relation (preferably with total participation) and insert the primary key of the other relation as a Foreign Key. | Same as the host entity relation. |
| **Step 4** | $1:N$ Relationship | Foreign Key approach: Identify relation $S$ representing the $N$-side entity type. Insert the primary key of the $1$-side relation as a Foreign Key in $S$. | Primary key of the $N$-side relation. |
| **Step 5** | $M:N$ Relationship | Relationship Relation (Junction table) approach: Create a new relation $R$. Include the primary keys of both participating entity types as Foreign Keys, plus any relationship attributes. | Compound Primary Key combining both foreign keys. |
| **Step 6** | Multivalued Attribute $A$ | Create a new relation $R$. Include attribute $A$ plus the primary key of the parent entity as a Foreign Key. | Compound Primary Key: (Parent PK + Attribute $A$). |
| **Step 7** | $N$-ary Relationship ($N > 2$) | Create a new relation $R$. Include primary keys of all participating entity types as Foreign Keys, plus relationship attributes. | Composite key of the foreign keys of entities on the "many" sides. |

