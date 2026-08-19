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
