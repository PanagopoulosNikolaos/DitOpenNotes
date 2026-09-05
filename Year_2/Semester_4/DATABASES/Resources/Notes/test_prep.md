# Test Prep: Practice Questions & Complete Solved Exam Papers for Database Systems (Course 404)

This test preparation guide is organized into two sections:
- **Part I: Thematic Drill Units (Units 1–16)**: 160 exam-type practice questions covering every theoretical and computational sub-topic, each accompanied by rule notes and complete solutions.
- **Part II: Complete Solved Real Exam Papers**: Full 10/10 model solutions for [Past_Exam_1.md](../../Exams/Papers/Past_Exam_1.md), [Past_Exam_2.md](../../Exams/Papers/Past_Exam_2.md), and all 8 realistic scenario exam papers from [synth_realistic/](../../Exams/Papers/synth_realistic).

---

# Part I: Thematic Drill Units

## Unit 1: Entity Types & Weak Entities Identification

### Question 1.1
Define what constitutes a Weak Entity in the Entity-Relationship model and state the conditions required for an entity to be classified as weak.

> **Rule / Formula:**
> A Weak Entity is an entity type that does not possess sufficient attributes to form a primary key on its own. It is existence-dependent on an Identifying (Owner) Entity via an Identifying Relationship (1:N with total participation on the weak entity side). Its primary key is composite: $\text{PK} = \text{PK}(\text{Owner}) \cup \text{Partial Key}$.

**Solution:**
A weak entity is characterized by:
1. **Lack of a standalone primary key:** Its attributes cannot uniquely distinguish an entity instance across the entire database.
2. **Existence dependency:** It cannot exist if the owner entity instance does not exist.
3. **Identifying relationship:** It connects to its owner entity through an identifying relationship (drawn with a double diamond), where the weak entity participates totally (double line).
4. **Partial key (Discriminator):** It possesses a partial key (dashed underline in ER diagrams) that uniquely identifies weak entity instances only within the scope of a single owner instance.

---

### Question 1.2
In a hospital database, we record `DOCTOR` and `DEPENDENT`. A dependent has `first_name`, `gender`, `date_of_birth`, and `relationship`. Can `DEPENDENT` be a strong entity? Explain.

> **Rule / Formula:**
> Without an owner ID, `first_name` cannot globally identify dependents across multiple doctors.

**Solution:**
No, `DEPENDENT` is a weak entity. Multiple doctors may have family members with the exact same first name (e.g., "Maria"). Therefore, `first_name` is merely a partial key (discriminator). The full identity of a dependent is determined only when combined with the doctor's primary key (`Doctor_AMI`).

---

### Question 1.3
In a hotel database, each room has a `room_number`, `floor`, and `price`. Rooms exist within a `HOTEL` (`hotel_id`). What type of entity is `ROOM`?

> **Rule / Formula:**
> `room_number` repeats across different hotel properties (e.g., Room 101 exists in both Athens Hotel and Crete Hotel).

**Solution:**
`ROOM` is a weak entity. The `room_number` is only unique within a specific hotel property. `HOTEL` is the identifying owner entity. The primary key of `ROOM` in relational schema is composite: $(\underline{\text{Hotel\_ID}, \text{Room\_Number}})$.

---

### Question 1.4
In a streaming platform, a `TV_SERIES` has `EPISODE` instances with `season_number`, `episode_number`, and `title`. Identify the entity type and primary key of `EPISODE`.

> **Rule / Formula:**
> An episode cannot exist without its series. Partial key = `(season_number, episode_number)`.

**Solution:**
`EPISODE` is a weak entity whose owner is `TV_SERIES(ISAN)`. The primary key of `EPISODE` is:
$$\underline{\text{PK}(\text{EPISODE}) = (\text{Series\_ISAN}, \text{Season\_Number}, \text{Episode\_Number})}$$

---

### Question 1.5
How is a weak entity represented graphically in Chen ER notation versus Crow's Foot notation?

> **Rule / Formula:**
> - Chen ER: Double rectangle for weak entity, double diamond for identifying relationship, dashed underline for partial key.
> - Crow's Foot: Box with owner's foreign key incorporated into the primary key section (above the dividing line).

**Solution:**
*   **Chen ER:** Double-lined rectangle for the weak entity, double-lined diamond for the identifying relationship, and dashed underline under the discriminator attribute.
*   **Crow's Foot:** Entity rectangle where the foreign key referencing the owner is placed in the primary key compartment (solid line relationship denoting identifying relationship).

---

### Question 1.6
Can a weak entity be the identifying owner of another weak entity (multi-level weak entity hierarchy)? Provide an example.

> **Rule / Formula:**
> Yes. Multi-level weak entity chains inherit primary keys cumulatively from all ancestor owners.

**Solution:**
Yes. For example: `BUILDING(Building_ID)` $\to$ `ROOM(Building_ID, Room_No)` $\to$ `DESK(Building_ID, Room_No, Desk_No)`. Here, `DESK` is a weak entity owned by `ROOM`, which is itself a weak entity owned by `BUILDING`.

---

### Question 1.7
In an e-commerce database, an `ORDER` contains multiple `ORDER_LINE_ITEM` rows with `line_number`, `quantity`, and `unit_price`. Is `ORDER_LINE_ITEM` a weak entity?

> **Rule / Formula:**
> `line_number` (1, 2, 3...) resets for each order and requires `order_id` to form a valid primary key.

**Solution:**
Yes. `ORDER_LINE_ITEM` is a weak entity. The attribute `line_number` is a partial key. The full primary key is $(\underline{\text{Order\_ID}, \text{Line\_Number}})$.

---

### Question 1.8
If an entity $E$ has a globally unique attribute (such as a nationwide Social Security Number `AMKA`), can it ever be modeled as a weak entity?

> **Rule / Formula:**
> An entity with a globally unique key attribute has independent identity and must be modeled as a strong entity.

**Solution:**
No. If an entity possesses a globally unique candidate key, it does not require an owner entity to establish its identity. It must be modeled as a regular strong entity.

---

### Question 1.9
What referential integrity action (`ON DELETE`) must be specified on the foreign key of a weak entity referencing its owner?

> **Rule / Formula:**
> Weak entities cannot exist without their owner $\implies$ `ON DELETE CASCADE`.

**Solution:**
`ON DELETE CASCADE` must be specified. If an owner entity instance is deleted, all its dependent weak entity instances must automatically be deleted to prevent orphaned records.

---

### Question 1.10
In a university database, `STUDENT` has `student_id` and belongs to a `DEPARTMENT`. Is `STUDENT` a weak entity?

> **Rule / Formula:**
> `student_id` is globally unique across the university $\implies$ Strong entity with a foreign key.

**Solution:**
No, `STUDENT` is a strong entity because `student_id` uniquely identifies the student regardless of the department. The association with `DEPARTMENT` is a regular 1:N relationship, represented by a foreign key `dept_code` in the `STUDENT` table.

---

## Unit 2: Attribute Classification (Composite, Multi-Valued, Derived, Key)

### Question 2.1
Classify the attribute `Address` composed of `Street`, `Number`, `Postal_Code`, and `City`. How is it mapped to relational tables?

> **Rule / Formula:**
> Composite attributes are subdivided. In relational schema, only simple atomic components are created as columns.

**Solution:**
*   **Classification:** Composite, single-valued attribute.
*   **Relational Mapping:** The composite attribute is flattened into four distinct atomic columns in the parent table: `Street VARCHAR(50)`, `Number VARCHAR(10)`, `Postal_Code VARCHAR(10)`, `City VARCHAR(50)`.

---

### Question 2.2
A professor can have multiple contact phone numbers (e.g., office, mobile, home). Classify `Phone_Number` and describe its relational transformation.

> **Rule / Formula:**
> Multi-valued attributes cannot be stored in 1NF as multi-value cells. They require a separate table: $\underline{\text{PK} = (\text{Parent\_PK}, \text{Value})}$.

**Solution:**
*   **Classification:** Simple, multi-valued attribute.
*   **Relational Mapping:** Create a separate child table:
    ```
    Professor_Phone
    | Prof_ID | Phone_Number |
    |---------|--------------|
    ```
    Primary Key: $(\underline{\text{Prof\_ID}, \text{Phone\_Number}})$. Foreign Key: `Prof_ID REFERENCES Professor(Prof_ID) ON DELETE CASCADE`.

---

### Question 2.3
In a patient table, we store `Date_Of_Birth` and `Age`. Classify both attributes and explain how `Age` should be handled in a relational database.

> **Rule / Formula:**
> Derived attributes are calculated dynamically and should not be stored statically as redundant columns.

**Solution:**
*   `Date_Of_Birth`: Simple, single-valued, stored attribute.
*   `Age`: Simple, single-valued, derived attribute.
*   **Database Handling:** `Age` should not be stored as a physical column in the base table (to avoid update anomalies as time passes). It is computed dynamically via SQL expressions (e.g., `TIMESTAMPDIFF(YEAR, date_of_birth, CURDATE())`) or materialized via a database VIEW.

---

### Question 2.4
In an airline system, a flight route has `Scheduled_Departure` and `Scheduled_Arrival`. The route also defines `Flight_Duration`. Classify `Flight_Duration`.

> **Rule / Formula:**
> Derived attribute computed as: `Duration = Scheduled_Arrival - Scheduled_Departure`.

**Solution:**
`Flight_Duration` is a derived attribute. In ER diagrams, it is drawn as a dashed oval. In SQL DDL, it is represented as a generated column:
```sql
flight_duration INT GENERATED ALWAYS AS (TIMESTAMPDIFF(MINUTE, scheduled_departure, scheduled_arrival)) STORED
```

---

### Question 2.5
What is the difference between a Single-Valued attribute and an Atomic attribute?

> **Rule / Formula:**
> - Single-valued: At most one value per instance (opposite of multi-valued).
> - Atomic: Indivisible into smaller sub-components (opposite of composite).

**Solution:**
*   **Atomic:** Refers to structural divisibility. An atomic attribute cannot be broken down (e.g., `Salary`), whereas a composite attribute can (e.g., `Full_Name` $\to$ `First_Name`, `Last_Name`).
*   **Single-valued:** Refers to the cardinality of values. A single-valued attribute holds exactly one value per entity instance (e.g., `Birth_Date`), whereas a multi-valued attribute holds a set of values (e.g., `Degrees_Held`). An attribute can be composite and single-valued (e.g., `Address`).

---

### Question 2.6
An e-commerce product has `Available_Colors` (e.g., ["Red", "Blue", "Black"]). What is its attribute type and how is it mapped?

> **Rule / Formula:**
> Multi-valued attribute $\implies$ Separate relation `Product_Color(SKU, Color)`.

**Solution:**
*   **Type:** Multi-valued attribute.
*   **Schema:** `Product_Color(`$\underline{\text{SKU}, \text{Color}}$`)`, where `SKU` is a foreign key referencing `Product(SKU)`.

---

### Question 2.7
In a student entity, `Student_Name` is composite (`First_Name`, `Middle_Name`, `Last_Name`) and `Middle_Name` is optional (nullable). How is this modeled in SQL?

> **Rule / Formula:**
> Simple sub-attributes mapped with appropriate nullability constraints.

**Solution:**
```sql
first_name VARCHAR(50) NOT NULL,
middle_name VARCHAR(50) NULL,
last_name VARCHAR(50) NOT NULL
```

---

### Question 2.8
Identify all attribute types present in: `Employee(Emp_ID, Tax_ID, Name(First, Last), Hire_Date, {Phones}, Age)`.

> **Rule / Formula:**
> Classify each: Key, Composite, Multi-valued, Derived, Simple.

**Solution:**
1. `Emp_ID`, `Tax_ID`: Simple, single-valued, candidate key attributes.
2. `Name`: Composite, single-valued attribute (composed of `First`, `Last`).
3. `Hire_Date`: Simple, single-valued, stored attribute.
4. `{Phones}`: Multi-valued attribute.
5. `Age`: Derived attribute (from `Date_Of_Birth`).

---

### Question 2.9
Why does storing a multi-valued attribute directly inside a single relational table violate First Normal Form (1NF)?

> **Rule / Formula:**
> 1NF Definition: All attribute values must be atomic (indivisible scalars).

**Solution:**
Storing multiple values in a single cell (e.g., comma-separated `"12345, 67890"`) violates the 1NF atomicity requirement, prevents indexing on individual values, and makes SQL joins and pattern searching inefficient and error-prone.

---

### Question 2.10
If an entity has a composite primary key consisting of `(Department_Code, Course_Number)`, is each individual component a candidate key?

> **Rule / Formula:**
> A candidate key must satisfy uniqueness and minimality. Proper subsets of a composite key are not candidate keys.

**Solution:**
No. Neither `Department_Code` nor `Course_Number` is individually unique. Only their combined tuple `(Department_Code, Course_Number)` satisfies the uniqueness requirement.

---

## Unit 3: Keys, Candidate Keys & Superkeys

### Question 3.1
Define Superkey, Candidate Key, and Primary Key. State their hierarchical relationship.

> **Rule / Formula:**
> $\text{Primary Key} \subseteq \text{Candidate Keys} \subseteq \text{Superkeys}$.
> - Superkey: Any set of attributes that uniquely identifies a tuple.
> - Candidate Key: A minimal superkey (no proper subset is a superkey).
> - Primary Key: The specific candidate key chosen by the database designer.

**Solution:**
*   **Superkey:** Any attribute set $S \subseteq R$ such that no two distinct tuples in relation $R$ have identical values for $S$.
*   **Candidate Key:** A superkey $K$ that satisfies the **minimality condition**: removing any attribute from $K$ results in a set that is no longer a superkey.
*   **Primary Key:** The candidate key designated as the principal mechanism for identifying tuples in the relation.

---

### Question 3.2
Given relation `Doctor(AMI, AFM, ADT, First_Name, Last_Name, Salary)` where `AMI` (Medical License), `AFM` (Tax ID), and `ADT` (National ID) are each unique. List all Candidate Keys and Superkeys.

> **Rule / Formula:**
> Each unique attribute is a candidate key. Any superset containing at least one candidate key is a superkey.

**Solution:**
*   **Candidate Keys (3):** `{AMI}`, `{AFM}`, `{ADT}`.
*   **Superkeys:** Any combination containing `AMI`, `AFM`, or `ADT` (e.g., `{AMI}`, `{AFM}`, `{ADT}`, `{AMI, AFM}`, `{AMI, First_Name}`, `{AFM, Salary}`, `{AMI, AFM, ADT, First_Name, Last_Name, Salary}`). Total number of superkeys = $2^6 - 2^3 = 56$.

---

### Question 3.3
What are the criteria for selecting the Primary Key among multiple Candidate Keys?

> **Rule / Formula:**
> Choose the key that is: (1) short/compact, (2) immutable (never changes), (3) non-null, and (4) simple/numeric if possible.

**Solution:**
1. **Minimality of Storage:** Prefer single-attribute integer keys over wide alphanumeric strings.
2. **Immutability:** The key value should never or rarely change over time (e.g., an internal `Emp_ID` is preferred over an `Email` which might change).
3. **Simplicity:** Single-column keys are easier to reference as foreign keys than composite keys.
4. **Privacy / Security:** Avoid using sensitive data like National Tax ID as public primary keys.

---

### Question 3.4
What is a Surrogate Key versus a Natural Key?

> **Rule / Formula:**
> - Natural Key: Attribute that exists naturally in the real-world business domain (e.g., `ISBN`, `AFM`).
> - Surrogate Key: System-generated synthetic identifier with no business meaning (e.g., `AUTO_INCREMENT INT`, `UUID`).

**Solution:**
*   **Natural Key:** Formed from intrinsic real-world attributes (e.g., `Tax_ID`, `Vehicle_VIN`).
*   **Surrogate Key:** An artificial, unique sequential number or UUID generated by the DBMS (e.g., `id INT AUTO_INCREMENT PRIMARY KEY`). It provides insulation against changes in business rules.

---

### Question 3.5
Can a relation have zero Candidate Keys? Explain.

> **Rule / Formula:**
> In formal relational theory, relations are sets of distinct tuples $\implies$ At least the set of all attributes combined forms a superkey.

**Solution:**
No. In the formal relational model, duplicate tuples are not permitted. Therefore, the set of all attributes $R = \{A_1, A_2, \dots, A_n\}$ is always a superkey, and either $R$ or some minimal subset of $R$ must be a candidate key.

---

### Question 3.6
What is an Alternate (Secondary) Key?

> **Rule / Formula:**
> Any candidate key that was not chosen as the primary key.

**Solution:**
An Alternate Key is a candidate key not selected as the primary key. In SQL DDL, alternate keys are implemented using `UNIQUE NOT NULL` constraints.

---

### Question 3.7
In a relation `Enrollment(Student_ID, Course_ID, Academic_Year, Semester, Grade)`, what is the candidate key?

> **Rule / Formula:**
> A student can take the same course in different academic years/semesters (e.g., if repeating).

**Solution:**
The candidate key is the composite set:
$$\underline{\text{Candidate Key} = \{\text{Student\_ID}, \text{Course\_ID}, \text{Academic\_Year}, \text{Semester}\}}$$

---

### Question 3.8
Can a Primary Key contain `NULL` values? Why or why not?

> **Rule / Formula:**
> Entity Integrity Constraint: No primary key component may be NULL.

**Solution:**
No. By the **Entity Integrity Constraint**, primary key attributes must be `NOT NULL`. A `NULL` value represents unknown or inapplicable data, which violates the fundamental purpose of uniquely identifying a tuple.

---

### Question 3.9
Can an Alternate Key (defined with `UNIQUE`) contain `NULL` values in standard SQL?

> **Rule / Formula:**
> Standard SQL allows NULL in UNIQUE columns (unless explicitly declared NOT NULL), because NULL is not equal to NULL.

**Solution:**
Yes, standard SQL allows `NULL` values in columns with a `UNIQUE` constraint, unless the column is explicitly defined as `UNIQUE NOT NULL`.

---

### Question 3.10
If relation $R(A, B, C, D)$ has candidate keys $\{A, B\}$ and $\{A, C\}$, what are the Prime and Non-Prime attributes?

> **Rule / Formula:**
> - Prime attribute: An attribute that belongs to at least one candidate key.
> - Non-prime attribute: An attribute that does not belong to any candidate key.

**Solution:**
*   **Prime Attributes:** $A, B, C$ (since $A \in \{A,B\}$ and $\{A,C\}$; $B \in \{A,B\}$; $C \in \{A,C\}$).
*   **Non-Prime Attributes:** $D$.

---

## Unit 4: Relationship Degrees & Recursive Relationships

### Question 4.1
What is a Recursive (Unary) Relationship? Provide two distinct examples.

> **Rule / Formula:**
> A relationship where the same entity type participates multiple times in different semantic roles.

**Solution:**
A recursive relationship is an association among instances of the same entity type.
*   **Example 1 (1:N Supervision):** `EMPLOYEE` supervises junior `EMPLOYEE` (Roles: `Supervisor` [1], `Supervisee` [N]).
*   **Example 2 (N:M Prerequisites):** `COURSE` is prerequisite for `COURSE` (Roles: `Prerequisite_Course` [N], `Main_Course` [M]).

---

### Question 4.2
How is a 1:N recursive relationship `EMPLOYEE` (supervises) mapped to a relational table?

> **Rule / Formula:**
> Add a nullable self-referencing foreign key column in the same table.

**Solution:**
```sql
CREATE TABLE Employee (
    emp_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    supervisor_emp_id INT NULL,
    CONSTRAINT fk_supervisor FOREIGN KEY (supervisor_emp_id)
        REFERENCES Employee(emp_id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);
```

---

### Question 4.3
How is an N:M recursive relationship `COURSE` (has prerequisites) mapped to relational tables?

> **Rule / Formula:**
> Create a separate junction table with two foreign keys, both referencing the parent entity.

**Solution:**
```sql
CREATE TABLE Course_Prerequisite (
    course_code VARCHAR(10) NOT NULL,
    prereq_course_code VARCHAR(10) NOT NULL,
    CONSTRAINT pk_prereq PRIMARY KEY (course_code, prereq_course_code),
    CONSTRAINT fk_cp_main FOREIGN KEY (course_code)
        REFERENCES Course(course_code) ON DELETE CASCADE,
    CONSTRAINT fk_cp_prereq FOREIGN KEY (prereq_course_code)
        REFERENCES Course(course_code) ON DELETE CASCADE,
    CONSTRAINT chk_no_self_prereq CHECK (course_code <> prereq_course_code)
);
```

---

### Question 4.4
What is the difference between a Ternary Relationship and three independent Binary Relationships?

> **Rule / Formula:**
> A ternary relationship represents an atomic 3-way association that cannot be factored into pairwise binary relationships without losing semantic information.

**Solution:**
A ternary relationship $R(A, B, C)$ asserts that an instance of $A$, an instance of $B$, and an instance of $C$ are bound together simultaneously (e.g., `Doctor` prescribes `Medication` to `Patient`). Three binary relationships (`Doctor-Medication`, `Medication-Patient`, `Doctor-Patient`) would only indicate that a doctor prescribes a drug, a patient takes a drug, and a doctor treats a patient, but would fail to record *which doctor prescribed which drug to which patient*.

---

### Question 4.5
How is a Ternary Relationship mapped into relational tables?

> **Rule / Formula:**
> Create a separate relation containing the primary keys of all three participating entities as foreign keys.

**Solution:**
Create a junction table:
$$\text{Prescription}(\underline{\text{Doctor\_ID}, \text{Patient\_ID}, \text{Drug\_Code}}, \text{Date}, \text{Dosage})$$
Foreign Keys:
- `Doctor_ID REFERENCES Doctor(Doctor_ID)`
- `Patient_ID REFERENCES Patient(Patient_ID)`
- `Drug_Code REFERENCES Medication(Drug_Code)`

---

### Question 4.6
In a sports league database, a `MATCH` is played between two teams: `Home_Team` and `Away_Team`. How is this modeled in ER and Relational Schema?

> **Rule / Formula:**
> Two distinct 1:N relationships between `TEAM` and `MATCH` with different role names.

**Solution:**
*   **ER Model:** Entity `MATCH` is connected to entity `TEAM` via two binary 1:N relationships: `HOSTS` (Role: `Home_Team`) and `VISITS` (Role: `Away_Team`).
*   **Relational Table:**
    ```
    Match
    | Match_ID | Match_Date | Home_Team_ID | Away_Team_ID | Home_Score | Away_Score |
    |----------|------------|--------------|--------------|------------|------------|
    ```
    Foreign Keys:
    - `Home_Team_ID REFERENCES Team(Team_ID)`
    - `Away_Team_ID REFERENCES Team(Team_ID)`
    - `CHECK (Home_Team_ID <> Away_Team_ID)`

---

### Question 4.7
In a company database, an `EMPLOYEE` manages a `DEPARTMENT` (1:1), and an `EMPLOYEE` works in a `DEPARTMENT` (1:N). How are these two relationships modeled between the same pair of entities?

> **Rule / Formula:**
> Multiple distinct relationships can exist between the same two entity types if they have different meanings.

**Solution:**
These are modeled as two separate relationships:
1. `MANAGES` (1:1): `Department` has foreign key `Manager_Emp_ID REFERENCES Employee(Emp_ID) UNIQUE`.
2. `WORKS_IN` (1:N): `Employee` has foreign key `Dept_Code REFERENCES Department(Dept_Code)`.

---

### Question 4.8
Can a recursive relationship have descriptive attributes? Provide an example.

> **Rule / Formula:**
> Yes. Relationship attributes describe the association between the participating instances.

**Solution:**
Yes. In an organizational hierarchy where `EMPLOYEE` mentors junior `EMPLOYEE`, the recursive relationship `MENTORS` can have descriptive attributes such as `start_date` and `mentorship_evaluation_score`.

---

### Question 4.9
In an airline system, a `FLIGHT_ROUTE` connects an `Origin_Airport` and a `Destination_Airport`. Is this a recursive relationship on `AIRPORT`?

> **Rule / Formula:**
> Yes, it represents two associations from `AIRPORT` to `FLIGHT_ROUTE` with roles `Origin` and `Destination`.

**Solution:**
Yes. Entity `AIRPORT` participates in two distinct roles with `FLIGHT_ROUTE`: as the Departure/Origin airport and as the Arrival/Destination airport. The `FLIGHT_ROUTE` table stores two foreign keys: `Origin_IATA` and `Destination_IATA`, both referencing `Airport(IATA_Code)`.

---

### Question 4.10
How do you prevent an employee from being their own supervisor in SQL?

> **Rule / Formula:**
> Table-level `CHECK` constraint: `CHECK (emp_id <> supervisor_emp_id)`.

**Solution:**
```sql
CONSTRAINT chk_no_self_supervision CHECK (emp_id <> supervisor_emp_id)
```

---

## Unit 5: Cardinality Ratios & Participation Justifications

### Question 5.1
State the required two-step justification template for an exam question asking to justify the cardinality ratio between `CLINIC` and `DOCTOR` (where a doctor belongs to one clinic and a clinic employs multiple doctors).

> **Rule / Formula:**
> Must provide forward (A $\to$ B) and backward (B $\to$ A) evaluations.

**Solution:**
*   **Direction 1 (Clinic $\to$ Doctor):** One clinic employs one or many (1..N) doctors, because a medical clinic requires multiple physicians of various specializations to operate.
*   **Direction 2 (Doctor $\to$ Clinic):** One doctor belongs mandatorily to exactly one (1..1) clinic, as administrative policy assigns each physician to a single home clinic department.
*   **Conclusion:** The cardinality ratio is **1:N** from `CLINIC` to `DOCTOR`. `DOCTOR` has total participation (every doctor must belong to a clinic).

---

### Question 5.2
Justify the cardinality ratio for the relationship `DIRECTS` between `FACULTY` and `PROFESSOR`, where each faculty is headed by one professor and a professor can head at most one faculty.

> **Rule / Formula:**
> 1:1 Cardinality with Total participation on Faculty, Partial on Professor.

**Solution:**
*   **Direction 1 (Faculty $\to$ Professor):** Each faculty must have exactly one (1..1) professor acting as Dean/Director (Total participation: min = 1, max = 1).
*   **Direction 2 (Professor $\to$ Faculty):** A professor may direct at most one (0..1) faculty at any given time, but most professors do not direct a faculty (Partial participation: min = 0, max = 1).
*   **Conclusion:** The cardinality ratio is **1:1**.

---

### Question 5.3
Justify the cardinality ratio for `PARTICIPATES_IN` between `PROFESSOR` and `RESEARCH_PROJECT` (professors participate in projects; projects involve professors).

> **Rule / Formula:**
> N:M Cardinality with optional or mandatory participation.

**Solution:**
*   **Direction 1 (Professor $\to$ Project):** A professor may participate in zero, one, or many (0..N) research projects simultaneously across different departments.
*   **Direction 2 (Project $\to$ Professor):** A research project requires the collaborative work of one or many (1..M) researchers/professors.
*   **Conclusion:** The cardinality ratio is **N:M**. It requires a junction table with descriptive attribute `Weekly_Hours`.

---

### Question 5.4
What is the difference between Cardinality Ratio and Participation Constraint?

> **Rule / Formula:**
> - Cardinality Ratio specifies the **maximum** number of relationship instances (1 or Many).
> - Participation Constraint specifies the **minimum** number of relationship instances (0 for Partial, 1 for Total).

**Solution:**
*   **Cardinality Ratio (Max Cardinality):** Defines the upper bound on the number of relationship instances in which an entity can participate (1:1, 1:N, N:M).
*   **Participation Constraint (Min Cardinality):** Defines the lower bound. If min = 1, participation is **Total (Mandatory)** (represented by a double line). If min = 0, participation is **Partial (Optional)** (represented by a single line).

---

### Question 5.5
In `(min, max)` notation, what does `(0, 1)` and `(1, N)` signify when placed next to entity `DOCTOR` on relationship `SERVES_IN`?

> **Rule / Formula:**
> In `(min, max)` notation, the constraint $(m, M)$ next to entity $E$ specifies that each instance of $E$ participates in at least $m$ and at most $M$ relationship instances.

**Solution:**
*   `(0, 1)` next to `DOCTOR` means that a doctor may belong to at most 1 clinic, but membership is optional (min = 0).
*   `(1, N)` next to `DOCTOR` means that every doctor must belong to at least 1 clinic and may belong to multiple clinics (total participation, multi-clinic).

---

### Question 5.6
Why is participation of a weak entity in its identifying relationship always Total?

> **Rule / Formula:**
> A weak entity is existence-dependent on its owner $\implies \min = 1$ (Total).

**Solution:**
By definition, a weak entity cannot exist in the database without its identifying owner entity. Therefore, every instance of the weak entity must participate in at least one identifying relationship instance ($\min \ge 1$), making participation mandatorily total.

---

### Question 5.7
Given `CUSTOMER` places `ORDER`. State the cardinality and participation constraints.

> **Rule / Formula:**
> Customer (1) $\to$ Order (N). A customer may have 0 orders; an order must have 1 customer.

**Solution:**
*   `CUSTOMER`: Partial participation (a registered customer might not have placed an order yet, min = 0, max = N).
*   `ORDER`: Total participation (every order must belong to exactly one customer, min = 1, max = 1).
*   Cardinality: **1:N** (`CUSTOMER` $\to$ `ORDER`).

---

### Question 5.8
Given `AUTHOR` writes `BOOK`. State the cardinality and participation constraints.

> **Rule / Formula:**
> Books can have multiple co-authors; authors can write multiple books $\implies$ N:M.

**Solution:**
*   One author writes 1..N books (Total participation if only published authors are recorded).
*   One book is written by 1..M authors (Total participation).
*   Cardinality: **N:M**.

---

### Question 5.9
Given `HOTEL_ROOM` is booked via `RESERVATION`. A reservation can reserve multiple rooms, and a room can be booked over multiple distinct reservation dates. State the cardinality.

> **Rule / Formula:**
> Reservation $\xleftrightarrow{\text{N:M}}$ Room.

**Solution:**
The cardinality is **N:M**. A single reservation can book multiple rooms (e.g., group booking), and a room can be included in many reservations across different time intervals.

---

### Question 5.10
In a 1:1 relationship with partial participation on both sides (e.g., `PERSON` is married to `PERSON`), how is the relationship mapped?

> **Rule / Formula:**
> Place a Foreign Key with `UNIQUE` in either table, or create a separate lookup table.

**Solution:**
Add a Foreign Key `Spouse_ID REFERENCES Person(Person_ID) UNIQUE NULL` in the `Person` table, or create a separate table `Marriage(`$\underline{\text{Person1\_ID}}$, `Person2_ID UNIQUE, Marriage_Date)`.

---

## Unit 6: ER-to-Relational Mapping Rules (Strong, Weak, Multi-Valued)

### Question 6.1
Map the strong entity `FACULTY(Code, Name, Floor, Office_Phone)` to a relational table.

> **Rule / Formula:**
> Strong entity $\to$ Table with simple attributes; declare PK.

**Solution:**
```
Faculty
| Code | Name | Floor | Office_Phone |
|------|------|-------|--------------|

Primary Key: Code
Alternate Key: Name (UNIQUE)
```

---

### Question 6.2
Map the weak entity `DEPENDENT` (attributes: `Name`, `Gender`, `Birth_Date`, `Relationship`) owned by `PROFESSOR(Prof_ID)`.

> **Rule / Formula:**
> $\text{PK} = (\text{Prof\_ID}, \text{Name})$, $\text{FK} = \text{Prof\_ID}$.

**Solution:**
```
Dependent
| Prof_ID | Dependent_Name | Gender | Birth_Date | Relationship |
|---------|----------------|--------|------------|--------------|

Primary Key: (Prof_ID, Dependent_Name)
Foreign Key: Prof_ID REFERENCES Professor(Prof_ID) ON DELETE CASCADE ON UPDATE CASCADE
```

---

### Question 6.3
Map the entity `HOTEL(Hotel_ID, Name)` with multi-valued attribute `{Amenities}`.

> **Rule / Formula:**
> Multi-valued attribute mapped as a separate child relation.

**Solution:**
```
Hotel
| Hotel_ID | Name |
|----------|------|

Primary Key: Hotel_ID

Hotel_Amenity
| Hotel_ID | Amenity_Name |
|----------|--------------|

Primary Key: (Hotel_ID, Amenity_Name)
Foreign Key: Hotel_ID REFERENCES Hotel(Hotel_ID) ON DELETE CASCADE
```

---

### Question 6.4
Map the entity `EMPLOYEE(Emp_ID, Name(First, Last), Address(Street, No, City), Salary)`.

> **Rule / Formula:**
> Flatten composite attributes into atomic columns.

**Solution:**
```
Employee
| Emp_ID | First_Name | Last_Name | Street | Street_Number | City | Salary |
|--------|------------|-----------|--------|---------------|------|--------|

Primary Key: Emp_ID
```

---

### Question 6.5
Why is a derived attribute like `Total_Amount` omitted from base relational schema tables during conceptual-to-relational mapping?

> **Rule / Formula:**
> Storing derived attributes introduces data redundancy and risks inconsistency if underlying source data changes.

**Solution:**
Derived attributes can be computed at query time from stored base data (e.g., `SUM(quantity * unit_price)`). Storing them in physical tables violates normal design principles unless explicitly used as a materialized cache with trigger-based synchronization.

---

### Question 6.6
Map the weak entity `TV_EPISODE(Season_No, Episode_No, Title, Duration)` owned by `TV_SERIES(ISAN)`.

> **Rule / Formula:**
> Composite PK: `(Series_ISAN, Season_No, Episode_No)`.

**Solution:**
```
TV_Episode
| Series_ISAN | Season_No | Episode_No | Title | Duration_Minutes |
|-------------|-----------|------------|-------|------------------|

Primary Key: (Series_ISAN, Season_No, Episode_No)
Foreign Key: Series_ISAN REFERENCES TV_Series(ISAN) ON DELETE CASCADE
```

---

### Question 6.7
Map the entity `STUDENT(AM, Name)` with multi-valued composite attribute `{Previous_Degrees(Degree_Title, Institution, Year)}`.

> **Rule / Formula:**
> Multi-valued composite attribute becomes a table containing the parent PK plus all atomic components.

**Solution:**
```
Student_Previous_Degree
| Student_AM | Degree_Title | Institution | Graduation_Year |
|------------|--------------|-------------|-----------------|

Primary Key: (Student_AM, Degree_Title, Institution)
Foreign Key: Student_AM REFERENCES Student(AM) ON DELETE CASCADE
```

---

### Question 6.8
What happens if a weak entity has no partial key (e.g., anonymous logs)?

> **Rule / Formula:**
> The child table must use an auto-increment surrogate key or timestamp to form uniqueness.

**Solution:**
If no natural discriminator exists, the designer must introduce a surrogate key (e.g., `log_id INT AUTO_INCREMENT`) or use an exact timestamp `(Owner_ID, Log_Timestamp)` as the primary key.

---

### Question 6.9
Show the SQL DDL for mapping `FACULTY_LOCATION` (multi-valued attribute `Location` on `Faculty(Faculty_Code)`).

> **Rule / Formula:**
> `CREATE TABLE` with composite primary key and foreign key cascade.

**Solution:**
```sql
CREATE TABLE Faculty_Location (
    faculty_code VARCHAR(10) NOT NULL,
    location VARCHAR(100) NOT NULL,
    CONSTRAINT pk_faculty_location PRIMARY KEY (faculty_code, location),
    CONSTRAINT fk_fl_faculty FOREIGN KEY (faculty_code)
        REFERENCES Faculty(faculty_code) ON DELETE CASCADE ON UPDATE CASCADE
);
```

---

### Question 6.10
In relational mapping, why do we underline both components of a weak entity's primary key?

> **Rule / Formula:**
> Underlining denotes the complete primary key. In a composite key, every participating column must be underlined.

**Solution:**
Because neither attribute alone is unique; only their combined pair uniquely identifies a tuple in the relation.

---

## Unit 7: ER-to-Relational Mapping of 1:1, 1:N, and N:M Relationships

### Question 7.1
Map the 1:1 relationship `HEADS` between `FACULTY(Code, Name)` (Total) and `PROFESSOR(Prof_ID, Name)` (Partial) with attribute `Date_Assumed`.

> **Rule / Formula:**
> Place FK in the entity with Total Participation (`Faculty`).

**Solution:**
```
Faculty
| Code | Name | Director_Prof_ID | Date_Assumed |
|------|------|------------------|--------------|

Primary Key: Code
Foreign Key: Director_Prof_ID REFERENCES Professor(Prof_ID) ON DELETE RESTRICT ON UPDATE CASCADE
Candidate Key (Unique): Director_Prof_ID (Declared UNIQUE NOT NULL)
```

---

### Question 7.2
Map the 1:N relationship `OFFERS` between `FACULTY(Code)` (1-side) and `PROGRAM(Prog_ID, Title)` (N-side).

> **Rule / Formula:**
> Place FK in the table on the N-side (`Program`).

**Solution:**
```
Educational_Program
| Prog_ID | Title | Faculty_Code |
|---------|-------|--------------|

Primary Key: Prog_ID
Foreign Key: Faculty_Code REFERENCES Faculty(Code) ON DELETE RESTRICT ON UPDATE CASCADE
```

---

### Question 7.3
Map the N:M relationship `WORKS_ON` between `PROFESSOR(Prof_ID)` and `PROGRAM(Prog_ID)` with relationship attribute `Weekly_Hours`.

> **Rule / Formula:**
> Create a new Junction Table. $\text{PK} = (\text{Prof\_ID}, \text{Prog\_ID})$.

**Solution:**
```
Professor_Program
| Prof_ID | Prog_ID | Weekly_Hours |
|---------|---------|--------------|

Primary Key: (Prof_ID, Prog_ID)
Foreign Keys:
- Prof_ID REFERENCES Professor(Prof_ID) ON DELETE CASCADE
- Prog_ID REFERENCES Educational_Program(Prog_ID) ON DELETE CASCADE
```

---

### Question 7.4
In a 1:1 relationship where both sides have Partial Participation (e.g., `CITIZEN` owns `PASSPORT`), how should the foreign key be placed?

> **Rule / Formula:**
> Place FK in either table, declare it `UNIQUE NULL`.

**Solution:**
Place the Foreign Key in the table that is most frequently queried with the association (e.g., `Passport` contains `Citizen_ID UNIQUE NOT NULL REFERENCES Citizen(Citizen_ID)`).

---

### Question 7.5
What is the consequence of incorrectly placing the Foreign Key in the 1-side table of a 1:N relationship?

> **Rule / Formula:**
> Violates 1NF (requires repeating groups / multi-value cells) or forces redundant row duplication.

**Solution:**
Placing the foreign key on the 1-side would require storing a list of multiple foreign key IDs for each row (violating 1NF atomicity) or duplicating the 1-side row for every related N-side record (causing massive redundancy and update anomalies).

---

### Question 7.6
Map the 1:N relationship `HOSPITALIZES` between `PATIENT(AMKA)` and `ADMISSION(Admission_No, Admission_Date)` where `ADMISSION` is a weak entity.

> **Rule / Formula:**
> Weak entity already includes owner's PK in its composite key.

**Solution:**
```
Admission
| Patient_AMKA | Admission_No | Admission_Date | Room_No |
|--------------|--------------|----------------|---------|

Primary Key: (Patient_AMKA, Admission_No)
Foreign Key: Patient_AMKA REFERENCES Patient(AMKA) ON DELETE CASCADE
```

---

### Question 7.7
Map the N:M relationship `SUPPLIES` between `SUPPLIER(Supplier_ID)` and `PRODUCT(SKU)` with attributes `Supply_Cost` and `Lead_Time_Days`.

> **Rule / Formula:**
> Junction table `Supplier_Product` containing both FKs and descriptive attributes.

**Solution:**
```
Supplier_Product
| Supplier_ID | Product_SKU | Supply_Cost | Lead_Time_Days |
|-------------|-------------|-------------|----------------|

Primary Key: (Supplier_ID, Product_SKU)
Foreign Keys:
- Supplier_ID REFERENCES Supplier(Supplier_ID) ON DELETE CASCADE
- Product_SKU REFERENCES Product(SKU) ON DELETE CASCADE
```

---

### Question 7.8
When should an N:M relationship be promoted to an independent Entity in conceptual design?

> **Rule / Formula:**
> When the relationship itself participates in other relationships or possesses complex lifecycle states.

**Solution:**
When the association needs to be referenced by other entities (e.g., an `Order` between `Customer` and `Store` that itself has `Order_Items` and `Payments`), or when instances of the association have a complex lifecycle and independent status tracking.

---

### Question 7.9
In mapping an N:M relationship, what are the cascading deletion actions for the junction table?

> **Rule / Formula:**
> Both foreign keys in the junction table should specify `ON DELETE CASCADE`.

**Solution:**
If either parent entity instance is deleted, all corresponding bridge records in the junction table must be automatically deleted (`ON DELETE CASCADE`) to prevent orphaned relationship references.

---

### Question 7.10
Map a ternary relationship `TREATMENT(Doctor_ID, Patient_ID, Drug_ID, Date, Dosage)`.

> **Rule / Formula:**
> Junction table with composite primary key of all 3 foreign keys.

**Solution:**
```
Treatment
| Doctor_ID | Patient_ID | Drug_ID | Treatment_Date | Dosage |
|-----------|------------|---------|----------------|--------|

Primary Key: (Doctor_ID, Patient_ID, Drug_ID, Treatment_Date)
Foreign Keys:
- Doctor_ID REFERENCES Doctor(Doctor_ID)
- Patient_ID REFERENCES Patient(Patient_ID)
- Drug_ID REFERENCES Medication(Drug_ID)
```

---

## Unit 8: Relational Table Schemas & Foreign Key Referential Actions

### Question 8.1
Explain the four standard referential integrity options for `ON DELETE` and `ON UPDATE`: `RESTRICT`, `CASCADE`, `SET NULL`, and `NO ACTION`.

> **Rule / Formula:**
> - `CASCADE`: Propagate change/deletion to child rows.
> - `SET NULL`: Set child FK column to NULL.
> - `RESTRICT` / `NO ACTION`: Reject parent deletion/update if child rows exist.

**Solution:**
*   **`CASCADE`:** Automatically deletes or updates matching rows in the child table when the parent row is deleted or updated.
*   **`SET NULL`:** Sets the child table's foreign key column values to `NULL` when the parent row is deleted or updated (requires the FK column to be nullable).
*   **`RESTRICT`:** Rejects the delete or update operation on the parent table immediately if any referencing rows exist in the child table.
*   **`NO ACTION`:** Similar to `RESTRICT`, but deferred constraint checks are performed at the end of the transaction.

---

### Question 8.2
Given `DEPARTMENT(Dept_Code)` and `PROFESSOR(Prof_ID, Dept_Code)`. If a department is deleted, we do NOT want to delete professors, but set their department to unassigned. Write the Foreign Key constraint.

> **Rule / Formula:**
> Use `ON DELETE SET NULL`.

**Solution:**
```sql
ALTER TABLE Professor
ADD CONSTRAINT fk_prof_dept FOREIGN KEY (dept_code)
    REFERENCES Department(dept_code)
    ON DELETE SET NULL
    ON UPDATE CASCADE;
```

---

### Question 8.3
When must `ON DELETE SET NULL` NOT be used?

> **Rule / Formula:**
> When the foreign key column is part of the primary key or defined as `NOT NULL`.

**Solution:**
`ON DELETE SET NULL` cannot be used if the foreign key column is defined as `NOT NULL` or is part of a composite Primary Key (as in weak entities and junction tables), because Primary Key columns cannot be `NULL` (violates Entity Integrity).

---

### Question 8.4
In the tables below, identify which column is the Foreign Key, which is the referenced table, and state the primary key of each table:
```
Clinic
| Clinic_Code | Name | Director_ID |
|-------------|------|-------------|

Doctor
| Doctor_AMI | Name | Clinic_Code |
|------------|------|-------------|
```

> **Rule / Formula:**
> Identify PKs and cross-table FK references.

**Solution:**
*   `Clinic`: Primary Key = `Clinic_Code`. Foreign Key = `Director_ID REFERENCES Doctor(Doctor_AMI)`.
*   `Doctor`: Primary Key = `Doctor_AMI`. Foreign Key = `Clinic_Code REFERENCES Clinic(Clinic_Code)`.

---

### Question 8.5
How do you resolve a mutual circular foreign key dependency during database initialization (`Clinic` references `Doctor`, and `Doctor` references `Clinic`)?

> **Rule / Formula:**
> Create tables without one FK, then use `ALTER TABLE ADD CONSTRAINT` after both tables exist.

**Solution:**
1. Create `Doctor` table without `Clinic_Code` (or create `Clinic` without `Director_ID`).
2. Create `Clinic` table with `Director_ID` referencing `Doctor`.
3. Alter `Doctor` table: `ALTER TABLE Doctor ADD CONSTRAINT fk_doc_clinic FOREIGN KEY (clinic_code) REFERENCES Clinic(clinic_code)`.

---

### Question 8.6
What is the effect of `ON UPDATE CASCADE`?

> **Rule / Formula:**
> Changing a primary key value in a parent row automatically updates all matching foreign key values in child rows.

**Solution:**
If the primary key value of a parent record is modified (e.g., `Dept_Code` changes from `'CS'` to `'DIT'`), the DBMS automatically updates all corresponding foreign key references in child tables without requiring manual intervention.

---

### Question 8.7
Can a Foreign Key reference a non-primary key column in another table?

> **Rule / Formula:**
> Yes, provided the referenced column is defined with a `UNIQUE` constraint.

**Solution:**
Yes. A foreign key can reference any column (or set of columns) in another table, provided that the referenced column has a `UNIQUE` or `PRIMARY KEY` constraint defined on it.

---

### Question 8.8
Why is `ON DELETE CASCADE` appropriate for an `Order_Line_Item` table referencing `Orders`?

> **Rule / Formula:**
> An order line item has no meaning or existence without its parent order.

**Solution:**
Because line items represent dependent components of the order. If the entire order is cancelled and deleted from the database, all individual line items belonging to it should automatically be removed.

---

### Question 8.9
What happens if you attempt to delete a parent row that has child references under `ON DELETE RESTRICT`?

> **Rule / Formula:**
> The DBMS raises a referential integrity violation error and rolls back the delete operation.

**Solution:**
The database engine prevents the deletion and throws a foreign key constraint violation error (e.g., SQL Error 1451).

---

### Question 8.10
In tabular exam schema notation, how do we distinguish a simple Primary Key from a composite Primary Key?

> **Rule / Formula:**
> Underline all columns that participate in the key.

**Solution:**
For a simple primary key, a single column header is underlined. For a composite primary key, all column headers that together form the key are underlined.

---

## Unit 9: Relational Algebra - Fundamental Operators

### Question 9.1
Given relation $R(A, B, C)$. Write the relational algebra expression to select all tuples where $A > 10$ and $B = 'XYZ'$.

> **Rule / Formula:**
> Selection operator $\sigma_{\text{condition}}(R)$.

**Solution:**
$$\sigma_{A > 10 \land B = 'XYZ'}(R)$$

---

### Question 9.2
Given relation $R(A, B, C, D)$. Write the relational algebra expression to project only columns $A$ and $C$.

> **Rule / Formula:**
> Projection operator $\pi_{\text{attributes}}(R)$.

**Solution:**
$$\pi_{A, C}(R)$$

---

### Question 9.3
What condition must relations $R$ and $S$ satisfy in order to perform Union ($R \cup S$), Intersection ($R \cap S$), or Difference ($R - S$)?

> **Rule / Formula:**
> **Union Compatibility:** Same degree (number of attributes) and pairwise identical/compatible data types.

**Solution:**
$R$ and $S$ must be **Union-Compatible**:
1. $R$ and $S$ must have the exact same number of attributes ($\text{degree}(R) = \text{degree}(S)$).
2. The domains of the corresponding $i$-th attributes in $R$ and $S$ must be compatible ($\text{dom}(A_i) = \text{dom}(B_i)$ for all $i$).

---

### Question 9.4
Express Set Intersection ($R \cap S$) using only the fundamental operators ($\sigma, \pi, \cup, -, \times$).

> **Rule / Formula:**
> $R \cap S = R - (R - S)$.

**Solution:**
$$R \cap S = R - (R - S)$$

---

### Question 9.5
Given $R$ with $n_1$ tuples and $S$ with $n_2$ tuples. What is the number of tuples in the Cartesian Product $R \times S$?

> **Rule / Formula:**
> $|R \times S| = |R| \times |S| = n_1 \cdot n_2$.

**Solution:**
The Cartesian Product contains exactly $n_1 \cdot n_2$ tuples. If $R$ has degree $k_1$ and $S$ has degree $k_2$, the degree of $R \times S$ is $k_1 + k_2$.

---

### Question 9.6
Given schema `Student(AM, Name, GPA)` and `Department(Dept_Code, Dept_Name)`. Is `Student` $\cup$ `Department` a valid relational algebra expression? Why or why not?

> **Rule / Formula:**
> Check union compatibility.

**Solution:**
No, it is invalid because `Student` (degree 3) and `Department` (degree 2) have different degrees and incompatible attribute domains, violating union compatibility.

---

### Question 9.7
What is the purpose of the Rename Operator ($\rho$) in Relational Algebra?

> **Rule / Formula:**
> $\rho_{S(B_1, \dots, B_n)}(R)$ renames relation $R$ to $S$ and its attributes to $B_1, \dots, B_n$.

**Solution:**
The rename operator allows:
1. Naming intermediate result relations in complex queries.
2. Renaming attributes to avoid naming conflicts during self-joins or Cartesian products.
3. Enabling natural joins between relations having different original column names for the same logical domain.

---

### Question 9.8
Write the Relational Algebra expression to find the names of all employees who earn more than 2500 euros from `Employee(Emp_ID, Name, Salary)`.

> **Rule / Formula:**
> $\pi_{\text{Name}}(\sigma_{\text{Salary} > 2500}(\text{Employee}))$.

**Solution:**
$$\pi_{\text{Name}}(\sigma_{\text{Salary} > 2500}(\text{Employee}))$$

---

### Question 9.9
Does the projection operator $\pi$ preserve duplicate tuples in theoretical relational algebra?

> **Rule / Formula:**
> Relations are mathematical sets $\implies$ Duplicate tuples are automatically eliminated.

**Solution:**
No. In pure relational algebra, relations are sets, so duplicate tuples are automatically eliminated from the result of a projection.

---

### Question 9.10
State the commutativity properties of Selection and Cartesian Product: Does $\sigma_{c_1}(\sigma_{c_2}(R)) = \sigma_{c_2}(\sigma_{c_1}(R))$? Does $R \times S = S \times R$?

> **Rule / Formula:**
> - Selection is commutative: $\sigma_{c_1}(\sigma_{c_2}(R)) = \sigma_{c_2}(\sigma_{c_1}(R)) = \sigma_{c_1 \land c_2}(R)$.
> - Cartesian Product is commutative up to column reordering.

**Solution:**
*   Yes, selections commute: $\sigma_{c_1}(\sigma_{c_2}(R)) = \sigma_{c_2}(\sigma_{c_1}(R)) = \sigma_{c_1 \land c_2}(R)$.
*   Cartesian product is commutative up to attribute ordering: $R \times S \cong S \times R$.

---

## Unit 10: Relational Algebra - Joins, Outer Joins, Semi-Joins & Division

### Question 10.1
Define Theta Join, Equi-Join, and Natural Join in Relational Algebra.

> **Rule / Formula:**
> - Theta Join: $R \bowtie_\theta S = \sigma_\theta(R \times S)$.
> - Equi-Join: Theta join where condition $\theta$ contains only equality comparisons ($=$).
> - Natural Join: Equi-join on all identically named common attributes with duplicate columns projected out.

**Solution:**
*   **Theta Join ($R \bowtie_\theta S$):** Cartesian product followed by a selection condition $\theta$: $\sigma_\theta(R \times S)$.
*   **Equi-Join:** A theta join where the condition $\theta$ consists exclusively of equality operators (e.g., $R.A = S.A$).
*   **Natural Join ($R \bowtie S$):** An equi-join on all shared common attributes between $R$ and $S$, automatically eliminating duplicate join columns.

---

### Question 10.2
Given `Professor(Prof_ID, Name, Dept_Code)` and `Department(Dept_Code, Dept_Name)`. Write the Natural Join expression to list all professors with their department names.

> **Rule / Formula:**
> $R \bowtie S$ joins on common attribute `Dept_Code`.

**Solution:**
$$\pi_{\text{Prof\_ID}, \text{Name}, \text{Dept\_Name}}(\text{Professor} \bowtie \text{Department})$$

---

### Question 10.3
Explain the difference between Left Outer Join ($⟕$) and Inner Join ($\bowtie$).

> **Rule / Formula:**
> Left Outer Join preserves all tuples from the left relation, filling missing right-side values with NULL.

**Solution:**
An **Inner Join** retains only tuples that satisfy the join condition in both relations; unmatched tuples from either table are discarded. A **Left Outer Join** ($R ⟕ S$) preserves *all* tuples from the left relation $R$; if a tuple in $R$ has no matching tuple in $S$, the columns corresponding to $S$ are padded with `NULL`.

---

### Question 10.4
What is a Semi-Join ($R \ltimes S$)? How is it defined in terms of fundamental operators?

> **Rule / Formula:**
> $R \ltimes S = \pi_{\text{attrs}(R)}(R \bowtie S)$.

**Solution:**
A Semi-Join returns all tuples from $R$ for which there is at least one matching tuple in $S$, without including any columns from $S$:
$$R \ltimes S = \pi_{\text{attributes}(R)}(R \bowtie S)$$

---

### Question 10.5
Explain the Relational Division operator ($R \div S$). What classic exam query pattern does it solve?

> **Rule / Formula:**
> $R \div S$ solves universal quantification queries ("Find all entities that are associated with ALL items in set $S$").

**Solution:**
Relational Division ($R(X, Y) \div S(Y)$) returns all tuples $x \in \pi_X(R)$ such that for every tuple $y \in S$, the combined tuple $(x, y)$ exists in $R$. It is used for "for all" queries (e.g., "Find students who took *all* courses offered by CS").

---

### Question 10.6
Given schema `Student(AM, Name)`, `Course(Code, Dept)`, `Enrollment(AM, Code)`. Write the Relational Algebra expression to find students enrolled in ALL courses offered by the 'CS' department.

> **Rule / Formula:**
> 1. $S = \pi_{\text{Code}}(\sigma_{\text{Dept} = '\text{CS}'}(\text{Course}))$
> 2. $R = \pi_{\text{AM}, \text{Code}}(\text{Enrollment})$
> 3. $\text{Result} = \pi_{\text{Name}}(\text{Student} \bowtie (R \div S))$

**Solution:**
1. Target CS Courses: $C_{\text{CS}} = \pi_{\text{Code}}(\sigma_{\text{Dept} = '\text{CS}'}(\text{Course}))$
2. Student-Course Enrollments: $E = \pi_{\text{AM}, \text{Code}}(\text{Enrollment})$
3. Eligible Student IDs: $Q = E \div C_{\text{CS}}$
4. Final Result: $\pi_{\text{Name}}(\text{Student} \bowtie Q)$

---

### Question 10.7
How is Relational Division ($R(A, B) \div S(B)$) expressed using only basic operators ($\pi, \times, -$)?

> **Rule / Formula:**
> $R \div S = \pi_A(R) - \pi_A((\pi_A(R) \times S) - R)$.

**Solution:**
$$R \div S = \pi_A(R) - \pi_A\Big( (\pi_A(R) \times S) - R \Big)$$
*Explanation:* Find all possible $(a, s)$ pairs ($\pi_A(R) \times S$), subtract the actual pairs in $R$ to find missing associations, project the $A$ values that have missing associations, and subtract those from all $A$ values.

---

### Question 10.8
Write the Relational Algebra expression to find all professors who have NO dependents.

> **Rule / Formula:**
> Set difference: All professors minus professors who appear in `Dependent`.

**Solution:**
$$\pi_{\text{Prof\_ID}}(\text{Professor}) - \pi_{\text{Prof\_ID}}(\text{Dependent})$$

---

### Question 10.9
What is an Anti-Semi-Join ($R \ \overline{\ltimes} \ S$)?

> **Rule / Formula:**
> $R \ \overline{\ltimes} \ S = R - (R \ltimes S)$. Returns tuples in $R$ with NO match in $S$.

**Solution:**
An Anti-Semi-Join returns all tuples from relation $R$ that have **no** matching tuple in relation $S$. It corresponds to SQL's `WHERE NOT EXISTS`.

---

### Question 10.10
Given relations $R(A, B)$ and $S(B, C)$ where $R = \{(1, 2), (3, 4)\}$ and $S = \{(2, 5), (2, 6)\}$. Compute the Natural Join $R \bowtie S$.

> **Rule / Formula:**
> Match on common column $B$.

**Solution:**
*   Tuple $(1, 2)$ matches with $(2, 5)$ and $(2, 6)$ $\implies (1, 2, 5)$ and $(1, 2, 6)$.
*   Tuple $(3, 4)$ has no match in $S$ on $B = 4$.
*   Result: $R \bowtie S = \{(1, 2, 5), (1, 2, 6)\}$.

---

## Unit 11: SQL DDL & Table Constraints Definition

### Question 11.1
Write the complete SQL `CREATE TABLE` statement for `Department` with `dept_code` (PK), `dept_name` (Unique, Not Null), `building`, and `office_phone`.

> **Rule / Formula:**
> Use standard ANSI SQL DDL syntax with named constraints.

**Solution:**
```sql
CREATE TABLE Department (
    dept_code VARCHAR(10) NOT NULL,
    dept_name VARCHAR(100) NOT NULL,
    building VARCHAR(50) NOT NULL,
    office_phone VARCHAR(20) NULL,
    CONSTRAINT pk_department PRIMARY KEY (dept_code),
    CONSTRAINT uq_dept_name UNIQUE (dept_name)
);
```

---

### Question 11.2
Write the SQL DDL statement to add a Foreign Key constraint `fk_emp_dept` to an existing table `Employee` referencing `Department(dept_code)`.

> **Rule / Formula:**
> `ALTER TABLE TableName ADD CONSTRAINT ... FOREIGN KEY ... REFERENCES ...`.

**Solution:**
```sql
ALTER TABLE Employee
ADD CONSTRAINT fk_emp_dept FOREIGN KEY (dept_code)
    REFERENCES Department(dept_code)
    ON DELETE RESTRICT
    ON UPDATE CASCADE;
```

---

### Question 11.3
Write a SQL `CHECK` constraint ensuring that an employee's `salary` is strictly positive and `hire_date` is on or after January 1, 2000.

> **Rule / Formula:**
> `CHECK (condition1 AND condition2)`.

**Solution:**
```sql
CONSTRAINT chk_emp_validity CHECK (salary > 0.00 AND hire_date >= '2000-01-01')
```

---

### Question 11.4
What is the difference between `DROP TABLE`, `TRUNCATE TABLE`, and `DELETE FROM` in SQL?

> **Rule / Formula:**
> - `DROP`: Removes table definition and all data from data dictionary (DDL).
> - `TRUNCATE`: Removes all rows rapidly without row-by-row logging; retains schema (DDL).
> - `DELETE`: Removes rows matching WHERE clause with row logging and rollback support (DML).

**Solution:**
*   **`DROP TABLE` (DDL):** Completely destroys the table structure, its schema definition, constraints, and data from the database catalog. Cannot be rolled back in most DBMS.
*   **`TRUNCATE TABLE` (DDL):** Deallocates data pages to remove all rows instantly; resets auto-increment counters; retains the table structure. Cannot specify a `WHERE` clause.
*   **`DELETE FROM` (DML):** Deletes rows conditionally using a `WHERE` clause; fires delete triggers; logs each row deletion individually in transaction log; can be rolled back.

---

### Question 11.5
Write a SQL statement to create an index on `(last_name, first_name)` in the `Doctor` table. Why are composite indexes useful?

> **Rule / Formula:**
> `CREATE INDEX index_name ON Table(Col1, Col2)`.

**Solution:**
```sql
CREATE INDEX idx_doctor_name ON Doctor(last_name, first_name);
```
*Why useful:* Accelerates queries filtering or sorting by `last_name` alone or by both `last_name` and `first_name` using B-Tree index traversal.

---

### Question 11.6
Write the SQL DDL for creating a database VIEW named `V_Active_Professors` listing `prof_id`, `full_name`, and `dept_name` for professors earning > 2000.

> **Rule / Formula:**
> `CREATE VIEW view_name AS SELECT ...`.

**Solution:**
```sql
CREATE VIEW V_Active_Professors AS
SELECT 
    p.prof_id,
    CONCAT(p.first_name, ' ', p.last_name) AS full_name,
    d.dept_name,
    p.monthly_salary
FROM Professor p
INNER JOIN Department d ON p.dept_code = d.dept_code
WHERE p.monthly_salary > 2000.00;
```

---

### Question 11.7
How do you define a default value for a column in SQL? Provide an example.

> **Rule / Formula:**
> `column_name data_type DEFAULT default_value`.

**Solution:**
```sql
status VARCHAR(20) NOT NULL DEFAULT 'Active',
created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
```

---

### Question 11.8
What is the effect of the `CASCADE CONSTRAINTS` option when dropping a table in SQL?

> **Rule / Formula:**
> Automatically drops all foreign key constraints in child tables that reference the dropped table.

**Solution:**
`DROP TABLE Department CASCADE CONSTRAINTS;` automatically removes all foreign key references in child tables (e.g., `Professor`, `Course`) pointing to `Department`, preventing foreign key dependency errors during table deletion.

---

### Question 11.9
Can a single table have multiple `UNIQUE` constraints? Can it have multiple `PRIMARY KEY` constraints?

> **Rule / Formula:**
> Multiple UNIQUE constraints are permitted; exactly ONE PRIMARY KEY constraint is allowed per table.

**Solution:**
A table can have multiple `UNIQUE` constraints (e.g., one on `Tax_ID` and another on `Email`), but **only one** `PRIMARY KEY` constraint.

---

### Question 11.10
Write SQL DDL to create a junction table `Doctor_Clinic` with a composite primary key and check constraint ensuring `hours_per_week <= 40`.

> **Rule / Formula:**
> Junction table DDL template.

**Solution:**
```sql
CREATE TABLE Doctor_Clinic (
    doctor_ami INT NOT NULL,
    clinic_code VARCHAR(10) NOT NULL,
    hours_per_week DECIMAL(4, 1) NOT NULL DEFAULT 0.0,
    CONSTRAINT pk_doc_clinic PRIMARY KEY (doctor_ami, clinic_code),
    CONSTRAINT fk_dc_doc FOREIGN KEY (doctor_ami)
        REFERENCES Doctor(doctor_ami) ON DELETE CASCADE,
    CONSTRAINT fk_dc_clinic FOREIGN KEY (clinic_code)
        REFERENCES Clinic(clinic_code) ON DELETE CASCADE,
    CONSTRAINT chk_hours CHECK (hours_per_week >= 0.0 AND hours_per_week <= 40.0)
);
```

---

## Unit 12: SQL DML & DQL - Joins, Aggregations & Grouping

### Question 12.1
Explain the logical execution order of the following SQL query:
```sql
SELECT dept_code, AVG(salary) AS avg_sal
FROM Professor
WHERE hire_date >= '2020-01-01'
GROUP BY dept_code
HAVING COUNT(*) >= 3
ORDER BY avg_sal DESC;
```

> **Rule / Formula:**
> Logical Execution Order: `FROM` $\to$ `WHERE` $\to$ `GROUP BY` $\to$ `HAVING` $\to$ `SELECT` $\to$ `ORDER BY`.

**Solution:**
1. **`FROM Professor`:** Scans the base `Professor` table.
2. **`WHERE hire_date >= '2020-01-01'`:** Filters out individual professor rows hired before 2020.
3. **`GROUP BY dept_code`:** Partitions the remaining rows into buckets by `dept_code`.
4. **`HAVING COUNT(*) >= 3`:** Discards department groups having fewer than 3 qualifying professors.
5. **`SELECT dept_code, AVG(salary)`:** Computes the average salary for each qualifying department group.
6. **`ORDER BY avg_sal DESC`:** Sorts the final aggregate groups in descending order of average salary.

---

### Question 12.2
What is the difference between `COUNT(*)`, `COUNT(column_name)`, and `COUNT(DISTINCT column_name)`?

> **Rule / Formula:**
> - `COUNT(*)` counts all rows including NULLs.
> - `COUNT(column)` counts rows where `column` is NOT NULL.
> - `COUNT(DISTINCT column)` counts unique non-NULL values.

**Solution:**
*   `COUNT(*)`: Returns the total number of rows in the group, including rows with `NULL` attribute values.
*   `COUNT(salary)`: Returns the number of rows where the `salary` column is **not NULL**.
*   `COUNT(DISTINCT dept_code)`: Returns the count of unique, distinct non-NULL department codes.

---

### Question 12.3
Write a SQL query to find the department name, number of courses offered, and average ECTS credits for departments that offer at least 5 courses.

> **Rule / Formula:**
> `INNER JOIN`, `GROUP BY`, `HAVING COUNT(*) >= 5`.

**Solution:**
```sql
SELECT 
    d.dept_name,
    COUNT(c.course_code) AS total_courses,
    AVG(c.ects) AS avg_ects
FROM Department d
INNER JOIN Course c ON d.dept_code = c.dept_code
GROUP BY d.dept_code, d.dept_name
HAVING COUNT(c.course_code) >= 5
ORDER BY total_courses DESC;
```

---

### Question 12.4
Write a SQL query using `LEFT JOIN` to list all departments and the number of professors in each, including departments with zero professors.

> **Rule / Formula:**
> Use `LEFT JOIN` and `COUNT(p.prof_id)` (NOT `COUNT(*)`).

**Solution:**
```sql
SELECT 
    d.dept_code,
    d.dept_name,
    COUNT(p.prof_id) AS num_professors
FROM Department d
LEFT JOIN Professor p ON d.dept_code = p.dept_code
GROUP BY d.dept_code, d.dept_name;
```
*Note:* Using `COUNT(p.prof_id)` correctly yields `0` for empty departments, whereas `COUNT(*)` would incorrectly yield `1` due to the preserved NULL row.

---

### Question 12.5
Write a SQL query to find the second highest salary among all employees without using `LIMIT` or `OFFSET`.

> **Rule / Formula:**
> Correlated subquery or `MAX(salary) < (SELECT MAX(salary) ...)`.

**Solution:**
```sql
SELECT MAX(salary) AS second_highest_salary
FROM Employee
WHERE salary < (
    SELECT MAX(salary) 
    FROM Employee
);
```

---

### Question 12.6
Write a SQL `UPDATE` statement that gives a 10% salary raise to all professors in the 'Computer Science' department.

> **Rule / Formula:**
> `UPDATE Table SET Col = Expr WHERE ...`.

**Solution:**
```sql
UPDATE Professor
SET monthly_salary = monthly_salary * 1.10
WHERE dept_code = (
    SELECT dept_code 
    FROM Department 
    WHERE dept_name = 'Computer Science'
);
```

---

### Question 12.7
Write a SQL query to find all doctors who have treated patients in more than 3 distinct hospital clinics.

> **Rule / Formula:**
> `GROUP BY` and `HAVING COUNT(DISTINCT clinic_code) > 3`.

**Solution:**
```sql
SELECT 
    d.doctor_ami,
    d.first_name,
    d.last_name,
    COUNT(DISTINCT a.clinic_code) AS distinct_clinics
FROM Doctor d
INNER JOIN Admission a ON d.doctor_ami = a.attending_doctor_ami
GROUP BY d.doctor_ami, d.first_name, d.last_name
HAVING COUNT(DISTINCT a.clinic_code) > 3;
```

---

### Question 12.8
What happens when an aggregate function (`SUM`, `AVG`, `MIN`, `MAX`) encounters `NULL` values?

> **Rule / Formula:**
> Aggregate functions ignore (skip) NULL values, except for `COUNT(*)`.

**Solution:**
All aggregate functions (except `COUNT(*)`) automatically filter out and ignore `NULL` values when performing computations. For example, `AVG(val)` over values `[10, 20, NULL]` computes $\frac{10 + 20}{2} = 15.0$.

---

### Question 12.9
Write a SQL query to display each student's name along with their GPA classification: 'High Honors' (GPA $\ge 8.5$), 'Honors' (GPA between 6.5 and 8.49), and 'Pass' (GPA < 6.5).

> **Rule / Formula:**
> Use `CASE WHEN ... THEN ... ELSE ... END`.

**Solution:**
```sql
SELECT 
    student_am,
    first_name,
    last_name,
    gpa,
    CASE 
        WHEN gpa >= 8.5 THEN 'High Honors'
        WHEN gpa >= 6.5 THEN 'Honors'
        ELSE 'Pass'
    END AS academic_standing
FROM Student;
```

---

### Question 12.10
Why is `WHERE AVG(salary) > 2000` invalid in SQL?

> **Rule / Formula:**
> `WHERE` filters individual rows before grouping occurs. Aggregate conditions must go in `HAVING`.

**Solution:**
The `WHERE` clause filters individual records before any grouping or aggregation takes place. Because aggregate functions compute results over groups of rows, they can only be evaluated in the `HAVING` clause after the `GROUP BY` phase.

---

## Unit 13: SQL Subqueries, Correlated Subqueries & Set Operators

### Question 13.1
Write a SQL query using `NOT EXISTS` to find all students who have NEVER enrolled in any course.

> **Rule / Formula:**
> Correlated anti-join subquery.

**Solution:**
```sql
SELECT s.am, s.first_name, s.last_name
FROM Student s
WHERE NOT EXISTS (
    SELECT 1 
    FROM Enrollment e
    WHERE e.student_am = s.am
);
```

---

### Question 13.2
Explain how a Correlated Subquery differs from a Non-Correlated Subquery.

> **Rule / Formula:**
> - Non-correlated subquery executes once independently and passes its result to the outer query.
> - Correlated subquery references columns from the outer query and re-evaluates for every outer row.

**Solution:**
*   **Non-Correlated Subquery:** Independent query that can run on its own; executed exactly once by the DBMS optimizer, returning a constant value or set used by the outer query.
*   **Correlated Subquery:** References one or more columns from the outer query's current candidate row (e.g., `WHERE e.student_am = s.am`). It is evaluated conceptually once for every row processed by the outer query.

---

### Question 13.3
Write a SQL query to find professors whose salary is strictly greater than the average salary of their own department.

> **Rule / Formula:**
> Correlated subquery in `WHERE` comparing `salary > (SELECT AVG(salary) WHERE dept = p.dept)`.

**Solution:**
```sql
SELECT p.prof_id, p.first_name, p.last_name, p.dept_code, p.monthly_salary
FROM Professor p
WHERE p.monthly_salary > (
    SELECT AVG(p2.monthly_salary)
    FROM Professor p2
    WHERE p2.dept_code = p.dept_code
);
```

---

### Question 13.4
What is the difference between `UNION` and `UNION ALL` in SQL?

> **Rule / Formula:**
> `UNION` eliminates duplicate rows (requires sorting/hashing); `UNION ALL` preserves all rows including duplicates.

**Solution:**
*   `UNION`: Merges results of two queries and performs duplicate elimination (slower due to sorting/deduplication).
*   `UNION ALL`: Appends the result sets directly without checking for duplicates (much faster).

---

### Question 13.5
Write a SQL query using `INTERSECT` (or `INNER JOIN`) to find customer IDs who have placed orders in BOTH 2024 and 2025.

> **Rule / Formula:**
> Set intersection query.

**Solution:**
```sql
SELECT customer_id FROM Orders WHERE YEAR(order_date) = 2024
INTERSECT
SELECT customer_id FROM Orders WHERE YEAR(order_date) = 2025;
```
*Alternative (MySQL compatible):*
```sql
SELECT DISTINCT o1.customer_id
FROM Orders o1
INNER JOIN Orders o2 ON o1.customer_id = o2.customer_id
WHERE YEAR(o1.order_date) = 2024 AND YEAR(o2.order_date) = 2025;
```

---

### Question 13.6
Write a SQL query using `EXCEPT` (or `NOT IN`) to find books that have NEVER been checked out on loan.

> **Rule / Formula:**
> Set difference query.

**Solution:**
```sql
SELECT isbn FROM Book_Title
EXCEPT
SELECT isbn FROM Book_Loan;
```
*Alternative:*
```sql
SELECT b.isbn, b.title
FROM Book_Title b
WHERE b.isbn NOT IN (
    SELECT bl.isbn 
    FROM Book_Loan bl 
    WHERE bl.isbn IS NOT NULL
);
```

---

### Question 13.7
What is the danger of using `NOT IN` with a subquery that returns a `NULL` value?

> **Rule / Formula:**
> In three-valued SQL logic, `val NOT IN (1, 2, NULL)` evaluates to `UNKNOWN` for all values $\implies$ Returns 0 rows!

**Solution:**
If the subquery returns even a single `NULL` value, the condition `x NOT IN (SELECT ...)` evaluates to `UNKNOWN` (neither `TRUE` nor `FALSE`) for all candidate rows, causing the entire query to return an empty result set! Always include `WHERE column IS NOT NULL` in `NOT IN` subqueries or use `NOT EXISTS`.

---

### Question 13.8
Write a SQL query using the `ALL` operator to find the employee with the highest salary.

> **Rule / Formula:**
> `salary >= ALL (SELECT salary FROM Employee)`.

**Solution:**
```sql
SELECT emp_id, first_name, last_name, salary
FROM Employee
WHERE salary >= ALL (
    SELECT salary 
    FROM Employee
);
```

---

### Question 13.9
Write a SQL query using the `EXISTS` operator to find all suppliers who supply at least one product with retail price > 1000.

> **Rule / Formula:**
> Correlated subquery testing existence.

**Solution:**
```sql
SELECT s.supplier_id, s.company_name
FROM Supplier s
WHERE EXISTS (
    SELECT 1
    FROM Supplier_Product sp
    INNER JOIN Product p ON sp.product_sku = p.sku
    WHERE sp.supplier_id = s.supplier_id
      AND p.retail_price > 1000.00
);
```

---

### Question 13.10
Implement Relational Division in SQL: Find all students who have enrolled in ALL courses offered by the 'MATH' department.

> **Rule / Formula:**
> `GROUP BY student HAVING COUNT(courses) = (SELECT COUNT(*) FROM Course WHERE dept = 'MATH')`.

**Solution:**
```sql
SELECT e.student_am
FROM Enrollment e
INNER JOIN Course c ON e.course_code = c.course_code
WHERE c.dept_code = 'MATH'
GROUP BY e.student_am
HAVING COUNT(DISTINCT e.course_code) = (
    SELECT COUNT(*) 
    FROM Course 
    WHERE dept_code = 'MATH'
);
```

---

## Unit 14: Functional Dependencies, Attribute Closure $X^+$ & Candidate Keys

### Question 14.1
Given relation $R(A, B, C, D, E)$ and set of functional dependencies $F$:
$$F = \{ A \to B, \; BC \to D, \; E \to C \}$$
Compute the attribute closure of $\{A, E\}^+$.

> **Rule / Formula:**
> Apply the attribute closure algorithm iteratively until no new attributes are added.

**Solution:**
1. Initialization: $X^{(0)} = \{A, E\}$.
2. Iteration 1:
   - $A \to B$: Since $A \subseteq \{A, E\}$, add $B \implies X^{(1)} = \{A, E, B\}$.
   - $E \to C$: Since $E \subseteq \{A, E, B\}$, add $C \implies X^{(1)} = \{A, B, C, E\}$.
3. Iteration 2:
   - $BC \to D$: Since $BC \subseteq \{A, B, C, E\}$, add $D \implies X^{(2)} = \{A, B, C, D, E\}$.
4. All attributes in $R$ are present.
$$\mathbf{\{A, E\}^+ = \{A, B, C, D, E\}}$$
Therefore, $\{A, E\}$ is a Superkey (and a Candidate Key) of $R$.

---

### Question 14.2
Given relation $R(A, B, C, D)$ with functional dependencies:
$$F = \{ A \to B, \; B \to C, \; C \to D, \; D \to A \}$$
Find ALL Candidate Keys of $R$.

> **Rule / Formula:**
> Compute closures for single attributes: $A^+, B^+, C^+, D^+$.

**Solution:**
*   $A^+ = \{A, B, C, D\} = R \implies A$ is a candidate key.
*   $B^+ = \{B, C, D, A\} = R \implies B$ is a candidate key.
*   $C^+ = \{C, D, A, B\} = R \implies C$ is a candidate key.
*   $D^+ = \{D, A, B, C\} = R \implies D$ is a candidate key.
*   **Candidate Keys:** $\{A\}$, $\{B\}$, $\{C\}$, $\{D\}$.

---

### Question 14.3
Given $R(A, B, C, D, E)$ with $F = \{ AB \to C, \; C \to D, \; D \to E \}$. Find the Candidate Key(s).

> **Rule / Formula:**
> Attributes $A$ and $B$ never appear on the RHS of any FD $\implies AB$ must be in every candidate key.

**Solution:**
1. Attributes $A$ and $B$ do not appear on the RHS of any FD. Thus, $\{A, B\}$ must be present in every candidate key.
2. Compute $\{A, B\}^+$:
   - $\{A, B\}^{(0)} = \{A, B\}$
   - $AB \to C \implies \{A, B, C\}$
   - $C \to D \implies \{A, B, C, D\}$
   - $D \to E \implies \{A, B, C, D, E\} = R$.
3. Since $\{A, B\}^+ = R$ and no proper subset of $\{A, B\}$ can determine $R$ ($A^+ = \{A\}$, $B^+ = \{B\}$), **$\{A, B\}$ is the unique Candidate Key**.

---

### Question 14.4
State Armstrong's Axioms and prove the Decomposition Rule ($X \to YZ \implies X \to Y$ and $X \to Z$).

> **Rule / Formula:**
> Axioms: Reflexivity, Augmentation, Transitivity.

**Solution:**
*   **Proof:**
    1. Given $X \to YZ$.
    2. Since $Y \subseteq YZ$, by Reflexivity we have $YZ \to Y$.
    3. Applying Transitivity to $X \to YZ$ and $YZ \to Y$, we obtain $X \to Y$.
    4. Similarly, since $Z \subseteq YZ$, by Reflexivity $YZ \to Z$. Applying Transitivity yields $X \to Z$.

---

### Question 14.5
What is a Trivial Functional Dependency? Provide an example.

> **Rule / Formula:**
> $X \to Y$ is trivial if and only if $Y \subseteq X$.

**Solution:**
A functional dependency $X \to Y$ is trivial if the right-hand side is a subset of the left-hand side. For example, $\{A, B\} \to A$ is a trivial functional dependency because $A \subseteq \{A, B\}$. It is satisfied by all possible relation instances.

---

### Question 14.6
Given $R(A, B, C, D)$ with $F = \{ A \to B, \; B \to C, \; C \to A \}$. Is $D$ a prime attribute? What is the candidate key?

> **Rule / Formula:**
> Attribute $D$ does not appear in $F \implies D$ must be part of every candidate key.

**Solution:**
1. $D$ does not appear in any FD, so $D$ must be included in every candidate key.
2. Closures:
   - $\{A, D\}^+ = \{A, B, C, D\} = R \implies \{A, D\}$ is a candidate key.
   - $\{B, D\}^+ = \{B, C, A, D\} = R \implies \{B, D\}$ is a candidate key.
   - $\{C, D\}^+ = \{C, A, B, D\} = R \implies \{C, D\}$ is a candidate key.
3. **Prime Attributes:** $A, B, C, D$ (all attributes are prime!).
4. Candidate Keys: $\{A, D\}, \{B, D\}, \{C, D\}$.

---

### Question 14.7
Explain what a Minimal Cover (Canonical Cover) of a set of functional dependencies $F$ is.

> **Rule / Formula:**
> A minimal cover $F_{\min}$ is an equivalent set of FDs with: (1) single attributes on RHS, (2) no redundant (extraneous) attributes on LHS, (3) no redundant FDs.

**Solution:**
A minimal cover $F_{\min}$ satisfies three conditions:
1. **Singleton RHS:** Every FD in $F_{\min}$ has a single attribute on its right-hand side ($X \to A$).
2. **No Extraneous LHS Attributes:** For every $X \to A$ in $F_{\min}$, no proper subset $X' \subset X$ satisfies $(F - \{X \to A\}) \cup \{X' \to A\} \equiv F$.
3. **No Redundant FDs:** No FD can be deleted from $F_{\min}$ without altering the closure $(F_{\min})^+$.

---

### Question 14.8
Given $F = \{ A \to B, \; B \to C, \; A \to C \}$. Find the Minimal Cover.

> **Rule / Formula:**
> Test if $A \to C$ is redundant by computing $A^+$ under $F - \{A \to C\}$.

**Solution:**
1. RHS attributes are already singletons.
2. Check if $A \to C$ is redundant:
   - Remove $A \to C$: $F' = \{ A \to B, \; B \to C \}$.
   - Compute $A^+$ under $F'$: $A^+ = \{A, B, C\}$.
   - Since $C \in A^+$, $A \to C$ is derived via transitivity ($A \to B \to C$) and is redundant.
3. **Minimal Cover:** $F_{\min} = \{ A \to B, \; B \to C \}$.

---

### Question 14.9
Given $R(A, B, C)$ with $F = \{ A \to B, \; B \to C \}$. Is $A \to C$ in $F^+$?

> **Rule / Formula:**
> By transitivity, $A \to B$ and $B \to C \implies A \to C$.

**Solution:**
Yes. By the transitivity rule of Armstrong's Axioms, since $A$ determines $B$ and $B$ determines $C$, $A$ functionally determines $C$. Thus, $(A \to C) \in F^+$.

---

### Question 14.10
If $|R| = 100$ tuples and $X \to Y$ holds, can there be 100 distinct values of $X$ and only 1 value of $Y$? Can there be 1 value of $X$ and 100 distinct values of $Y$?

> **Rule / Formula:**
> $X \to Y$ means equal $X$ implies equal $Y$. Distinct $X$ may map to identical $Y$.

**Solution:**
*   **Case 1 (100 distinct $X$, 1 value of $Y$):** YES. Multiple different $X$ values can map to the exact same $Y$ value (many-to-one function).
*   **Case 2 (1 value of $X$, 100 distinct values of $Y$):** NO. If two tuples have the same $X$ value, they MUST have the exact same $Y$ value by the definition of functional dependency.

---

## Unit 15: Normalization (1NF, 2NF, 3NF, BCNF) & Lossless Decomposition

### Question 15.1
State the formal definitions of 1NF, 2NF, 3NF, and BCNF.

> **Rule / Formula:**
> - 1NF: Atomic attribute domains.
> - 2NF: 1NF + No non-prime attribute partially dependent on any candidate key.
> - 3NF: 2NF + For all non-trivial $X \to Y$, $X$ is superkey OR $Y$ is prime.
> - BCNF: For all non-trivial $X \to Y$, $X$ MUST be a superkey.

**Solution:**
*   **1NF:** A relation schema $R$ is in 1NF if all attribute values are atomic scalars (no repeating groups, multi-valued attributes, or nested relations).
*   **2NF:** $R$ is in 2NF if it is in 1NF and no non-prime attribute is partially dependent on any candidate key (every non-prime attribute is fully functionally dependent on every candidate key).
*   **3NF:** $R$ is in 3NF if for every non-trivial functional dependency $X \to Y$, either: (1) $X$ is a superkey of $R$, OR (2) $Y$ is a prime attribute (part of some candidate key).
*   **BCNF:** $R$ is in Boyce-Codd Normal Form if for every non-trivial functional dependency $X \to Y$, $X$ is a superkey of $R$.

---

### Question 15.2
Given relation `Student_Course(Student_ID, Course_ID, Student_Name, Course_Title, Grade)` with dependencies:
$$\{ \text{Student\_ID} \to \text{Student\_Name}, \; \text{Course\_ID} \to \text{Course\_Title}, \; (\text{Student\_ID}, \text{Course\_ID}) \to \text{Grade} \}$$
Identify the candidate key and explain which normal form this relation violates.

> **Rule / Formula:**
> Candidate Key = `(Student_ID, Course_ID)`. Partial dependencies violate 2NF.

**Solution:**
1. **Candidate Key:** `(Student_ID, Course_ID)`.
2. **Prime Attributes:** `Student_ID`, `Course_ID`. Non-prime: `Student_Name`, `Course_Title`, `Grade`.
3. **Analysis:**
   - $\text{Student\_ID} \to \text{Student\_Name}$: `Student_ID` is a proper subset of the candidate key, and `Student_Name` is non-prime $\implies$ **Partial Dependency**.
   - $\text{Course\_ID} \to \text{Course\_Title}$: `Course_ID` is a proper subset of the candidate key $\implies$ **Partial Dependency**.
4. **Conclusion:** Violates **2NF** (and thus 3NF and BCNF).
5. **2NF Decomposition:**
   - $R_1(\underline{\text{Student\_ID}}, \text{Student\_Name})$
   - $R_2(\underline{\text{Course\_ID}}, \text{Course\_Title})$
   - $R_3(\underline{\text{Student\_ID}, \text{Course\_ID}}, \text{Grade})$

---

### Question 15.3
Given relation `Employee(Emp_ID, Dept_Code, Dept_Name, Salary)` with dependencies:
$$\{ \text{Emp\_ID} \to (\text{Dept\_Code}, \text{Salary}), \; \text{Dept\_Code} \to \text{Dept\_Name} \}$$
Identify the normal form and decompose into 3NF.

> **Rule / Formula:**
> $\text{Emp\_ID} \to \text{Dept\_Code} \to \text{Dept\_Name}$ is a transitive dependency violating 3NF.

**Solution:**
1. **Candidate Key:** `Emp_ID`.
2. **2NF Check:** Primary key is single-attribute (`Emp_ID`), so no partial dependencies exist. It is in **2NF**.
3. **3NF Check:** In $\text{Dept\_Code} \to \text{Dept\_Name}$, `Dept_Code` is NOT a superkey, and `Dept_Name` is NOT a prime attribute. This is a **Transitive Dependency** violating **3NF**.
4. **3NF Decomposition:**
   - $R_1(\underline{\text{Emp\_ID}}, \text{Salary}, \text{Dept\_Code})$
   - $R_2(\underline{\text{Dept\_Code}}, \text{Dept\_Name})$

---

### Question 15.4
Given $R(A, B, C)$ with $F = \{ AB \to C, \; C \to B \}$.
Find all Candidate Keys, test if $R$ is in 3NF, and test if $R$ is in BCNF.

> **Rule / Formula:**
> Candidate keys: $\{A, B\}$ and $\{A, C\}$. Prime attributes: $A, B, C$.

**Solution:**
1. **Candidate Keys:**
   - $\{A, B\}^+ = \{A, B, C\} \implies \{A, B\}$ is a candidate key.
   - $\{A, C\}^+ = \{A, C, B\} \implies \{A, C\}$ is a candidate key.
2. **Prime Attributes:** $A, B, C$ (All attributes are prime!).
3. **3NF Test:**
   - $AB \to C$: $AB$ is a superkey (Satisfied).
   - $C \to B$: $C$ is not a superkey, BUT $B$ is a prime attribute (Satisfied).
   - **$R$ is in 3NF!**
4. **BCNF Test:**
   - For $C \to B$, $C$ is NOT a superkey.
   - **$R$ violates BCNF!**

---

### Question 15.5
State the Lossless-Join Decomposition Theorem for a binary decomposition $D = (R_1, R_2)$.

> **Rule / Formula:**
> $D = (R_1, R_2)$ is lossless if and only if $(R_1 \cap R_2) \to R_1$ OR $(R_1 \cap R_2) \to R_2$ in $F^+$.

**Solution:**
A decomposition of relation $R$ into two relations $R_1$ and $R_2$ is guaranteed to be a **Lossless-Join Decomposition** with respect to functional dependency set $F$ if and only if the intersection of their attributes $(R_1 \cap R_2)$ functionally determines at least one of the decomposed relations:
$$(R_1 \cap R_2) \to R_1 \quad \text{OR} \quad (R_1 \cap R_2) \to R_2$$
That is, the common attributes must form a superkey for $R_1$ or $R_2$.

---

### Question 15.6
Test whether decomposing $R(A, B, C)$ into $R_1(A, B)$ and $R_2(B, C)$ is lossless under $F = \{ A \to B, \; B \to C \}$.

> **Rule / Formula:**
> Common attributes: $R_1 \cap R_2 = \{B\}$. Check if $B \to R_1$ or $B \to R_2$.

**Solution:**
1. Intersection: $R_1 \cap R_2 = \{A, B\} \cap \{B, C\} = \{B\}$.
2. Compute closure of $\{B\}$: $B^+ = \{B, C\} = R_2$.
3. Since $(R_1 \cap R_2) \to R_2$ ($B \to BC$), the decomposition is **Lossless**.

---

### Question 15.7
Why is 3NF sometimes preferred over BCNF in practical enterprise database design?

> **Rule / Formula:**
> 3NF always guarantees both Lossless Join and Dependency Preservation. BCNF guarantees Lossless Join, but may lose functional dependencies.

**Solution:**
3NF synthesis guarantees that the decomposition is both **Lossless** and **Dependency-Preserving**. BCNF decomposition guarantees a lossless join, but can result in lost functional dependencies that would require expensive cross-table joins to enforce via constraints.

---

### Question 15.8
Decompose $R(A, B, C)$ with $F = \{ AB \to C, \; C \to B \}$ into BCNF.

> **Rule / Formula:**
> Decompose on the violating FD $C \to B$: $R_1(C, B)$ and $R_2(R - (B - C)) = R_2(A, C)$.

**Solution:**
1. Violating dependency: $C \to B$ ($C$ is not a superkey).
2. Decompose $R$ into:
   - $R_1(\underline{C}, B)$ with $\text{PK} = C$.
   - $R_2(\underline{A, C})$ with $\text{PK} = (A, C)$.
3. Both $R_1$ and $R_2$ are in BCNF. (Note: The original dependency $AB \to C$ is lost).

---

### Question 15.9
What is an Update Anomaly? Provide a concrete example.

> **Rule / Formula:**
> Data redundancy causing inconsistencies when data is modified in one tuple but not in duplicate tuples.

**Solution:**
If `Dept_Name` is stored alongside every employee in `Employee(Emp_ID, Dept_Code, Dept_Name)`, updating the department name requires updating every employee record in that department. If some rows are updated while others are missed, the database enters an inconsistent state.

---

### Question 15.10
What is a Deletion Anomaly? Provide a concrete example.

> **Rule / Formula:**
> Unintended loss of unrelated information when deleting a tuple.

**Solution:**
In `Student_Course(Student_ID, Course_Code, Course_Title)`, if only one student is enrolled in a specific course and that student drops the course (tuple is deleted), all information about the course itself (`Course_Title`) is unintentionally erased from the database.

---

## Unit 16: ACID Transactions, Serializability & Database Security

### Question 16.1
State and define the four ACID properties of database transactions.

> **Rule / Formula:**
> Atomicity, Consistency, Isolation, Durability.

**Solution:**
*   **Atomicity:** "All-or-nothing" execution. All transaction operations complete successfully and commit, or all effects are undone (rollback).
*   **Consistency:** A transaction transitions the database from one valid state to another valid state, preserving all integrity constraints.
*   **Isolation:** The concurrent execution of multiple transactions results in a system state equivalent to executing them sequentially.
*   **Durability:** Once a transaction commits, its modifications are permanently recorded in non-volatile storage and survive any subsequent system crashes.

---

### Question 16.2
Given schedule $S$:
$$S: R_1(A), \; W_1(A), \; R_2(A), \; W_2(A), \; R_1(B), \; W_1(B), \; \text{Commit}_1, \; \text{Commit}_2$$
Draw the Precedence Graph and determine if $S$ is Conflict Serializable.

> **Rule / Formula:**
> Directed edge $T_i \to T_j$ if an operation of $T_i$ precedes and conflicts with an operation of $T_j$.

**Solution:**
1. **Identify Conflicts:**
   - $W_1(A)$ precedes $R_2(A)$ on item $A \implies$ Edge $T_1 \to T_2$.
   - $W_1(A)$ precedes $W_2(A)$ on item $A \implies$ Edge $T_1 \to T_2$.
2. **Precedence Graph:**
   - Nodes: $\{T_1, T_2\}$
   - Directed Edges: $T_1 \to T_2$.
3. **Cycle Check:** The graph contains **no directed cycles**.
4. **Conclusion:** Schedule $S$ is **Conflict Serializable**. Equivalent serial order: $T_1 \to T_2$.

---

### Question 16.3
Given schedule $S$:
$$S: R_1(A), \; W_2(A), \; W_1(A), \; \text{Commit}_1, \; \text{Commit}_2$$
Is $S$ conflict serializable?

> **Rule / Formula:**
> Check for bidirectional edges creating a cycle.

**Solution:**
1. $R_1(A)$ precedes $W_2(A) \implies$ Edge $T_1 \to T_2$.
2. $W_2(A)$ precedes $W_1(A) \implies$ Edge $T_2 \to T_1$.
3. **Precedence Graph:** Contains a cycle: $T_1 \leftrightarrow T_2$.
4. **Conclusion:** Schedule $S$ is **NOT Conflict Serializable**.

---

### Question 16.4
Explain the Two-Phase Locking (2PL) protocol. What does it guarantee?

> **Rule / Formula:**
> - Growing Phase: Locks acquired, no locks released.
> - Shrinking Phase: Locks released, no locks acquired.
> Guarantees Conflict Serializability.

**Solution:**
*   **Growing Phase:** A transaction may acquire locks (shared or exclusive), but cannot release any lock.
*   **Shrinking Phase:** Once the transaction releases its first lock, it enters the shrinking phase and cannot acquire any new locks.
*   **Guarantee:** 2PL guarantees that any concurrent execution schedule is **Conflict Serializable**. (Strict 2PL additionally prevents cascading rollbacks by holding exclusive locks until commit).

---

### Question 16.5
What is a Deadlock in database transactions? Name two strategies for dealing with deadlocks.

> **Rule / Formula:**
> Deadlock: A set of transactions where each transaction is waiting for a lock held by another transaction in the set.

**Solution:**
A deadlock occurs when two or more transactions are in a circular wait state for locks held by one another.
*   **Deadlock Prevention (Wait-Die / Wound-Wait):** Uses transaction timestamps. In Wait-Die, older transactions wait for younger ones, while younger transactions die if they request a lock held by an older one.
*   **Deadlock Detection & Resolution:** DBMS maintains a Wait-For Graph (WFG). When a cycle is detected, the DBMS selects a victim transaction, rolls it back, and releases its locks.

---

### Question 16.6
What is a Dirty Read anomaly? Give an example schedule.

> **Rule / Formula:**
> Transaction $T_2$ reads uncommitted modifications of $T_1$, and $T_1$ subsequently aborts.

**Solution:**
*   **Example Schedule:**
    $$T_1: W_1(A=500) \to T_2: R_2(A=500) \to T_1: \text{Abort} \to T_2: \text{Commit}$$
*   $T_2$ read a balance of 500 that never legitimately existed in the database because $T_1$ rolled back.

---

### Question 16.7
How does SQL's `REPEATABLE READ` isolation level prevent Non-Repeatable Reads?

> **Rule / Formula:**
> By holding shared (read) locks until the transaction commits, preventing other transactions from modifying read rows.

**Solution:**
Under `REPEATABLE READ`, any row read by a transaction is locked with a shared read lock (or managed via snapshot MVCC versions) that is held until transaction termination. Other transactions cannot update or delete that row until the reading transaction commits.

---

### Question 16.8
Explain what SQL Injection is and provide the standard industry defense.

> **Rule / Formula:**
> Malicious SQL payload injected into unescaped string concatenation $\implies$ Use Prepared Statements / Parameterized Queries.

**Solution:**
*   **SQL Injection:** An attack where malicious SQL code is injected into input fields and executed by the backend database due to dynamic string concatenation (e.g., `' OR '1'='1`).
*   **Defense:** Use **Prepared Statements with Parameterized Placeholders** (`SELECT * FROM User WHERE username = ? AND password = ?`). The DBMS treats parameter values strictly as data, never as executable SQL commands.

---

### Question 16.9
Why is storing passwords with simple MD5 or SHA-256 hashes insecure, and what is the proper security approach?

> **Rule / Formula:**
> Vulnerable to Rainbow Table dictionary lookups $\implies$ Use salted, slow key derivation functions (bcrypt, Argon2, PBKDF2).

**Solution:**
Fast cryptographic hashes (MD5, SHA-256) can be computed billions of times per second on modern GPUs, making them vulnerable to precomputed **Rainbow Table** dictionary attacks.
*   **Secure Approach:** Use a slow, memory-hard adaptive hashing algorithm (e.g., **bcrypt**, **Argon2id**, **PBKDF2**) with a cryptographically secure random per-user **Salt** to guarantee uniqueness and defeat precomputation attacks.

---

### Question 16.10
Write SQL DCL commands to create a user `'nurse_jane'`, grant `SELECT` on `Patient` and `INSERT` on `Admission`, and then revoke `INSERT`.

> **Rule / Formula:**
> `GRANT privileges ON table TO user;` and `REVOKE privileges ON table FROM user;`.

**Solution:**
```sql
-- Create User
CREATE USER 'nurse_jane'@'%' IDENTIFIED BY 'StrongPassword123!';

-- Grant Privileges
GRANT SELECT ON Hospital_DB.Patient TO 'nurse_jane'@'%';
GRANT INSERT ON Hospital_DB.Admission TO 'nurse_jane'@'%';

-- Revoke Insert Privilege
REVOKE INSERT ON Hospital_DB.Admission FROM 'nurse_jane'@'%';
```

---

# Part II: Complete Solved Real Exam Papers

---

## Solved Paper 1: Educational Institution ([Past_Exam_1.md](../../Exams/Papers/Past_Exam_1.md))

### Problem Text Recap
*An educational institution maintains information about professors, faculties, and educational programs. Each faculty has a unique code, name, a director professor (with date assumed office), and multi-location facilities. Each faculty offers many programs (unique number, title, venue). For each professor: first name, last name, ID number (PK), specialty, address, monthly salary, gender, birth date. Each professor belongs to a faculty, participates in multiple programs (weekly hours recorded), and has dependent family members (name, gender, birth date, relationship).*

---

### Question A (4 Points): Conceptual Analysis

#### 1. Entities & Types
*   **`FACULTY` (Strong Entity):** Independent administrative department. Key: `Faculty_Code`.
*   **`PROFESSOR` (Strong Entity):** Independent faculty member. Key: `ID_Number`.
*   **`EDUCATIONAL_PROGRAM` (Strong Entity):** Distinct program offering. Key: `Program_Number`.
*   **`DEPENDENT` (Weak Entity):** Family members of a professor. Existence-dependent on `PROFESSOR`. Discriminator (partial key): `Dependent_Name`. Identifying entity: `PROFESSOR`.

#### 2. Attributes & Classifications
*   **`FACULTY`:** `Faculty_Code` (Simple, Single-valued, Key), `Faculty_Name` (Simple, Single-valued, Candidate Key), `Location` (Simple, Multi-valued).
*   **`PROFESSOR`:** `ID_Number` (Simple, Single-valued, Primary Key), `First_Name` (Simple, Single-valued), `Last_Name` (Simple, Single-valued), `Specialty` (Simple, Single-valued), `Address` (Composite: `Street`, `Number`, `City`, `Postal_Code`), `Monthly_Salary` (Simple, Single-valued), `Gender` (Simple, Single-valued), `Date_Of_Birth` (Simple, Single-valued).
*   **`EDUCATIONAL_PROGRAM`:** `Program_Number` (Simple, Single-valued, Primary Key), `Title` (Simple, Single-valued, Candidate Key), `Venue` (Simple, Single-valued).
*   **`DEPENDENT`:** `Dependent_Name` (Simple, Single-valued, Partial Key), `Gender` (Simple, Single-valued), `Date_Of_Birth` (Simple, Single-valued), `Relationship` (Simple, Single-valued).

#### 3. Keys Specification
*   `FACULTY`: Candidate Keys: `{Faculty_Code}`, `{Faculty_Name}`. Primary Key: $\underline{\text{Faculty\_Code}}$.
*   `PROFESSOR`: Candidate Key & Primary Key: $\underline{\text{ID\_Number}}$.
*   `EDUCATIONAL_PROGRAM`: Candidate Keys: `{Program_Number}`, `{Title}`. Primary Key: $\underline{\text{Program\_Number}}$.
*   `DEPENDENT`: Partial Key: `Dependent_Name`. Primary Key: $\underline{(\text{Prof\_ID\_Number}, \text{Dependent\_Name})}$.

#### 4. Relationships & Cardinality Justifications
1. **`HEADS` / `DIRECTS` (`FACULTY` $\xleftrightarrow{\text{1:1}}$ `PROFESSOR`):**
   *   *Faculty $\to$ Professor:* Each faculty must have exactly one (1..1) professor as Director (Total participation on `FACULTY`).
   *   *Professor $\to$ Faculty:* A professor may direct at most one (0..1) faculty (Partial participation on `PROFESSOR`).
   *   *Cardinality:* **1:1**. Descriptive Attribute: `Date_Assumed_Office`.
2. **`OFFERS` (`FACULTY` $\xrightarrow{\text{1:N}}$ `EDUCATIONAL_PROGRAM`):**
   *   *Faculty $\to$ Program:* A faculty offers one or many (1..N) educational programs.
   *   *Program $\to$ Faculty:* Each educational program belongs mandatorily to exactly one (1..1) faculty.
   *   *Cardinality:* **1:N** (Total participation on `EDUCATIONAL_PROGRAM`).
3. **`BELONGS_TO` (`PROFESSOR` $\xrightarrow{\text{N:1}}$ `FACULTY`):**
   *   *Professor $\to$ Faculty:* Each professor belongs to exactly one (1..1) faculty.
   *   *Faculty $\to$ Professor:* A faculty employs many (1..N) professors.
   *   *Cardinality:* **1:N** (`FACULTY` $\to$ `PROFESSOR`).
4. **`TEACHES_IN` (`PROFESSOR` $\xleftrightarrow{\text{N:M}}$ `EDUCATIONAL_PROGRAM`):**
   *   *Professor $\to$ Program:* A professor may teach in multiple (0..N) programs.
   *   *Program $\to$ Professor:* A program involves multiple (1..M) professors.
   *   *Cardinality:* **N:M**. Descriptive Attribute: `Weekly_Hours`.
5. **`HAS_DEPENDENT` (`PROFESSOR` $\xrightarrow{\text{1:N}}$ `DEPENDENT`):**
   *   *Professor $\to$ Dependent:* A professor may have zero or many (0..N) dependents.
   *   *Dependent $\to$ Professor:* A dependent belongs to exactly one (1..1) professor.
   *   *Cardinality:* **1:N (Identifying Relationship)**.

---

### Question B (3 Points): E-R Diagram

```mermaid
erDiagram
    FACULTY ||--o| PROFESSOR : "HEADS (1:1)"
    FACULTY ||--|{ PROFESSOR : "EMPLOYS (1:N)"
    FACULTY ||--|{ EDUCATIONAL_PROGRAM : "OFFERS (1:N)"
    PROFESSOR }|--|{ EDUCATIONAL_PROGRAM : "TEACHES_IN (N:M)"
    PROFESSOR ||--o{ DEPENDENT : "HAS_DEPENDENT (1:N Weak)"

    FACULTY {
        string faculty_code PK
        string faculty_name UK
        date date_assumed_office
    }
    PROFESSOR {
        string id_number PK
        string first_name
        string last_name
        string specialty
        string street
        string street_number
        string city
        string postal_code
        decimal monthly_salary
        string gender
        date date_of_birth
        string faculty_code FK
    }
    EDUCATIONAL_PROGRAM {
        string program_number PK
        string title UK
        string venue
        string faculty_code FK
    }
    DEPENDENT {
        string prof_id_number PK_FK
        string dependent_name PK
        string gender
        date date_of_birth
        string relationship
    }
```

---

### Question C (3 Points): Relational Table Schema

**Faculty**
| Faculty_Code | Faculty_Name | Director_Prof_ID | Date_Assumed_Office |
|---|---|---|---|

*   **Primary Key:** $\underline{\text{Faculty\_Code}}$
*   **Foreign Keys:**
    *   `Director_Prof_ID REFERENCES Professor(ID_Number) ON DELETE RESTRICT ON UPDATE CASCADE`
*   **Alternate Key:** `Faculty_Name (UNIQUE)`

**Faculty_Location**
| Faculty_Code | Location |
|---|---|

*   **Primary Key:** $\underline{(\text{Faculty\_Code}, \text{Location})}$
*   **Foreign Keys:**
    *   `Faculty_Code REFERENCES Faculty(Faculty_Code) ON DELETE CASCADE ON UPDATE CASCADE`

**Professor**
| ID_Number | First_Name | Last_Name | Specialty | Street | Number | City | Postal_Code | Monthly_Salary | Gender | Date_Of_Birth | Faculty_Code |
|---|---|---|---|---|---|---|---|---|---|---|---|

*   **Primary Key:** $\underline{\text{ID\_Number}}$
*   **Foreign Keys:**
    *   `Faculty_Code REFERENCES Faculty(Faculty_Code) ON DELETE RESTRICT ON UPDATE CASCADE`

**Educational_Program**
| Program_Number | Title | Venue | Faculty_Code |
|---|---|---|---|

*   **Primary Key:** $\underline{\text{Program\_Number}}$
*   **Foreign Keys:**
    *   `Faculty_Code REFERENCES Faculty(Faculty_Code) ON DELETE RESTRICT ON UPDATE CASCADE`
*   **Alternate Key:** `Title (UNIQUE)`

**Professor_Program**
| Prof_ID_Number | Program_Number | Weekly_Hours |
|---|---|---|

*   **Primary Key:** $\underline{(\text{Prof\_ID\_Number}, \text{Program\_Number})}$
*   **Foreign Keys:**
    *   `Prof_ID_Number REFERENCES Professor(ID_Number) ON DELETE CASCADE ON UPDATE CASCADE`
    *   `Program_Number REFERENCES Educational_Program(Program_Number) ON DELETE CASCADE ON UPDATE CASCADE`

**Dependent**
| Prof_ID_Number | Dependent_Name | Gender | Date_Of_Birth | Relationship |
|---|---|---|---|---|

*   **Primary Key:** $\underline{(\text{Prof\_ID\_Number}, \text{Dependent\_Name})}$
*   **Foreign Keys:**
    *   `Prof_ID_Number REFERENCES Professor(ID_Number) ON DELETE CASCADE ON UPDATE CASCADE`

---

## Solved Paper 2: Research Institute ([Past_Exam_2.md](../../Exams/Papers/Past_Exam_2.md))

### Question A (5 Points): Conceptual Analysis

#### 1. Entities & Types
*   **`RESEARCH_UNIT` (Strong Entity):** Primary organizational research laboratory. Key: `Unit_Code`.
*   **`RESEARCHER` (Strong Entity):** Individual scientist. Key: `ID_Number`.
*   **`RESEARCH_PROJECT` (Strong Entity):** Specific grant/funded project. Key: `Project_Number`.
*   **`DEPENDENT` (Weak Entity):** Family members of researchers. Identifying entity: `RESEARCHER`. Discriminator: `Dependent_Name`.

#### 2. Attributes & Classifications
*   **`RESEARCH_UNIT`:** `Unit_Code` (Simple, Single-valued, PK), `Unit_Name` (Simple, Single-valued, Candidate Key), `Location` (Simple, Multi-valued).
*   **`RESEARCHER`:** `ID_Number` (Simple, Single-valued, PK), `First_Name`, `Last_Name`, `Scientific_Field`, `Address` (Composite), `Monthly_Salary`, `Gender`, `Date_Of_Birth`.
*   **`RESEARCH_PROJECT`:** `Project_Number` (Simple, Single-valued, PK), `Title` (Simple, Single-valued, Candidate Key), `Venue` (Simple, Single-valued).
*   **`DEPENDENT`:** `Dependent_Name` (Partial Key), `Gender`, `Date_Of_Birth`, `Relationship`.

#### 3. Keys Specification
*   `RESEARCH_UNIT`: Candidate Keys: `{Unit_Code}`, `{Unit_Name}`. Final Primary Key: $\underline{\text{Unit\_Code}}$.
*   `RESEARCHER`: Candidate Key & Primary Key: $\underline{\text{ID\_Number}}$.
*   `RESEARCH_PROJECT`: Candidate Keys: `{Project_Number}`, `{Title}`. Final Primary Key: $\underline{\text{Project\_Number}}$.
*   `DEPENDENT`: Primary Key: $\underline{(\text{Researcher\_ID}, \text{Dependent\_Name})}$.

#### 4. Relationships & Detailed Cardinality Justification
*   **`DIRECTS` (`RESEARCH_UNIT` $\xleftrightarrow{\text{1:1}}$ `RESEARCHER`):** 1:1 ratio. Each unit is managed by exactly one lead researcher (Total on `RESEARCH_UNIT`). A researcher leads at most one unit (Partial on `RESEARCHER`). Attribute: `Date_Assumed_Office`.
*   **`IMPLEMENTS` (`RESEARCH_UNIT` $\xrightarrow{\text{1:N}}$ `RESEARCH_PROJECT`):** 1:N ratio. Each unit implements many projects; each project is hosted by one unit (Total on `RESEARCH_PROJECT`).
*   **`AFFILIATED_WITH` (`RESEARCHER` $\xrightarrow{\text{N:1}}$ `RESEARCH_UNIT`):** 1:N ratio. Each researcher belongs to one home unit; a unit employs multiple researchers.
*   **`PARTICIPATES_IN` (`RESEARCHER` $\xleftrightarrow{\text{N:M}}$ `RESEARCH_PROJECT`):** N:M ratio. Researchers participate in multiple projects (including external ones); projects employ multiple researchers. Descriptive attribute: `Weekly_Hours`.
*   **`HAS_DEPENDENT` (`RESEARCHER` $\xrightarrow{\text{1:N}}$ `DEPENDENT`):** 1:N identifying relationship.

---

### Question B (5 Points): E-R Diagram

```mermaid
erDiagram
    RESEARCH_UNIT ||--o| RESEARCHER : "IS_SCIENTIFICALLY_HEADED_BY (1:1)"
    RESEARCH_UNIT ||--|{ RESEARCHER : "EMPLOYS (1:N)"
    RESEARCH_UNIT ||--|{ RESEARCH_PROJECT : "IMPLEMENTS (1:N)"
    RESEARCHER }|--|{ RESEARCH_PROJECT : "WORKS_ON (N:M)"
    RESEARCHER ||--o{ DEPENDENT : "HAS_DEPENDENT (1:N Weak)"

    RESEARCH_UNIT {
        string unit_code PK
        string unit_name UK
        date date_assumed_office
    }
    RESEARCHER {
        string id_number PK
        string first_name
        string last_name
        string scientific_field
        string street
        string street_number
        string city
        string postal_code
        decimal monthly_salary
        string gender
        date date_of_birth
        string unit_code FK
    }
    RESEARCH_PROJECT {
        string project_number PK
        string title UK
        string venue
        string unit_code FK
    }
    DEPENDENT {
        string researcher_id PK_FK
        string dependent_name PK
        string gender
        date date_of_birth
        string relationship
    }
```

---

## Solved Paper 3: University Hospital Management System ([synth_realistic_1](../../Exams/Papers/synth_realistic/exam_paper_synthetic_and_realistic_1.md))

### Questions A & B: Conceptual Analysis & ER Diagram
*   **Entities:** `CLINIC` (Strong), `DOCTOR` (Strong), `PATIENT` (Strong), `MEDICATION` (Strong), `HOSPITALIZATION` (Weak, owned by `PATIENT`), `DEPENDENT` (Weak, owned by `DOCTOR`).
*   **Special Attributes:** `DOCTOR.Phones` (Multi-valued), `CLINIC.Locations` (Multi-valued), `PATIENT.Age` (Derived from `Date_Of_Birth`).
*   **Recursive Relationship:** `DOCTOR` supervises junior `DOCTOR` (1:N self-referencing).
*   **Ternary / Treatment Relationship:** `HOSPITALIZATION` $\xleftrightarrow{\text{N:M}}$ `MEDICATION` prescribed by `DOCTOR` with attributes `Dosage`, `Frequency_Per_24H`, `Start_Date`, `End_Date`.

---

### Question C: Relational Table Schema

**Clinic**
| Clinic_Code | Clinic_Name | Floor | Phone | Director_Doctor_AMI | Date_Assumed |
|---|---|---|---|---|---|

*   $\underline{\text{Clinic\_Code}}$ (PK), `Director_Doctor_AMI REFERENCES Doctor(AMI) UNIQUE NOT NULL`.

**Clinic_Location**
| Clinic_Code | Location_Building |
|---|---|

*   $\underline{(\text{Clinic\_Code}, \text{Location\_Building})}$ (PK), `Clinic_Code REFERENCES Clinic(Clinic_Code) ON DELETE CASCADE`.

**Doctor**
| AMI | AFM | First_Name | Last_Name | Specialty | Rank_Title | Monthly_Salary | Hire_Date | Street | Number | Postal_Code | City | Clinic_Code | Supervisor_Doctor_AMI |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

*   $\underline{\text{AMI}}$ (PK), `AFM (UNIQUE)`, `Clinic_Code REFERENCES Clinic(Clinic_Code)`, `Supervisor_Doctor_AMI REFERENCES Doctor(AMI) ON DELETE SET NULL`.

**Doctor_Phone**
| Doctor_AMI | Phone_Number |
|---|---|

*   $\underline{(\text{Doctor\_AMI}, \text{Phone\_Number})}$ (PK), `Doctor_AMI REFERENCES Doctor(AMI) ON DELETE CASCADE`.

**Dependent**
| Doctor_AMI | Dependent_Name | Gender | Date_Of_Birth | Relationship |
|---|---|---|---|---|

*   $\underline{(\text{Doctor\_AMI}, \text{Dependent\_Name})}$ (PK), `Doctor_AMI REFERENCES Doctor(AMI) ON DELETE CASCADE`.

**Patient**
| AMKA | ADT | First_Name | Last_Name | Date_Of_Birth | Gender | Blood_Type |
|---|---|---|---|---|---|---|

*   $\underline{\text{AMKA}}$ (PK), `ADT (UNIQUE)`.

**Hospitalization**
| Patient_AMKA | Admission_No | Admission_Timestamp | Discharge_Timestamp | Room_No | Initial_Diagnosis | Clinic_Code |
|---|---|---|---|---|---|---|

*   $\underline{(\text{Patient\_AMKA}, \text{Admission\_No})}$ (PK), `Patient_AMKA REFERENCES Patient(AMKA) ON DELETE CASCADE`, `Clinic_Code REFERENCES Clinic(Clinic_Code)`.

**Medication**
| EOF_Code | Trade_Name | Active_Ingredient | Unit_Of_Measure |
|---|---|---|---|

*   $\underline{\text{EOF\_Code}}$ (PK).

**Treatment_Prescription**
| Patient_AMKA | Admission_No | EOF_Code | Prescribing_Doctor_AMI | Dosage | Frequency_24H | Start_Date | End_Date |
|---|---|---|---|---|---|---|---|

*   $\underline{(\text{Patient\_AMKA}, \text{Admission\_No}, \text{EOF\_Code}, \text{Start\_Date})}$ (PK), Foreign Keys to `Hospitalization`, `Medication`, and `Doctor`.

---

## Solved Paper 4: University Academic System ([synth_realistic_2](../../Exams/Papers/synth_realistic/exam_paper_synthetic_and_realistic_2.md))

### Relational Schema Summary
*   **Department:** $\underline{\text{Dept\_Code}}$, `Dept_Name (UQ)`, `Building`, `Phone`, `Chair_Prof_AM (FK, UQ)`, `Appointment_Date`.
*   **Department_Location:** $\underline{(\text{Dept\_Code}, \text{Location\_Building})}$ (PK).
*   **Professor:** $\underline{\text{AM}}$ (PK), `AFM (UQ)`, `First_Name`, `Last_Name`, `Academic_Rank`, `Salary`, `Hire_Date`, `Street`, `Number`, `Postal_Code`, `City`, `Dept_Code (FK)`, `Mentor_Prof_AM (FK)`.
*   **Professor_Phone:** $\underline{(\text{Prof\_AM}, \text{Phone\_Number})}$ (PK).
*   **Dependent:** $\underline{(\text{Prof\_AM}, \text{Dependent\_Name})}$ (PK).
*   **Student:** $\underline{\text{AM}}$ (PK), `ADT (UQ)`, `First_Name`, `Last_Name`, `DoB`, `Gender`, `Admission_Year`, `Dept_Code (FK)`.
*   **Course:** $\underline{\text{Course\_Code}}$ (PK), `Title`, `ECTS`, `Category`, `Semester_Intended`, `Dept_Code (FK)`.
*   **Course_Prerequisite:** $\underline{(\text{Course\_Code}, \text{Prereq\_Course\_Code})}$ (PK).
*   **Teaching_Assignment:** $\underline{(\text{Prof\_AM}, \text{Course\_Code}, \text{Academic\_Year}, \text{Semester})}$ (PK).
*   **Student_Enrollment:** $\underline{(\text{Student\_AM}, \text{Course\_Code}, \text{Academic\_Year}, \text{Semester})}$ (PK), `Final_Grade`, `Exam_Date`.

---

## Solved Paper 5: Commercial Airline Fleet ([synth_realistic_3](../../Exams/Papers/synth_realistic/exam_paper_synthetic_and_realistic_3.md))

### Relational Schema Summary
*   **Airport:** $\underline{\text{IATA\_Code}}$ (PK), `Airport_Name`, `City`, `Country`, `TimeZone_Offset`, `Manager_Emp_ID (FK, UQ)`, `Manager_Start_Date`.
*   **Airport_Runway:** $\underline{(\text{IATA\_Code}, \text{Runway\_ID})}$ (PK).
*   **Flight_Route:** $\underline{\text{Flight\_Number}}$ (PK), `Origin_IATA (FK)`, `Destination_IATA (FK)`, `Sched_Dep_Time`, `Sched_Arr_Time`.
*   **Aircraft:** $\underline{\text{Tail\_Number}}$ (PK), `Serial_No (UQ)`, `Model`, `Manufacturer`, `Seating_Capacity`, `Year_Built`.
*   **Aircraft_Maintenance:** $\underline{(\text{Tail\_Number}, \text{Maintenance\_Event\_No})}$ (PK), `Inspection_Date`, `Type`, `Facility`.
*   **Flight_Instance:** $\underline{(\text{Flight\_Number}, \text{Flight\_Date})}$ (PK), `Actual_Dep`, `Actual_Arr`, `Gate`, `Assigned_Tail_Number (FK)`, `Status`.
*   **Crew_Member:** $\underline{\text{Emp\_ID}}$ (PK), `AFM (UQ)`, `First_Name`, `Last_Name`, `Role`, `License_No`, `Flight_Hours`, `Hire_Date`, `Mentor_Emp_ID (FK)`.
*   **Crew_Phone:** $\underline{(\text{Emp\_ID}, \text{Phone\_Number})}$ (PK).
*   **Flight_Crew_Assignment:** $\underline{(\text{Flight\_Number}, \text{Flight\_Date}, \text{Emp\_ID})}$ (PK).
*   **Passenger:** $\underline{\text{Passport\_No}}$ (PK), `ADT (UQ)`, `First_Name`, `Last_Name`, `DoB`, `Nationality`, `Email`, `Phone`.
*   **Booking_Ticket:** $\underline{\text{ETicket\_No}}$ (PK), `PNR_Code (UQ)`, `Booking_Date`, `Seat_No`, `Travel_Class`, `Fare`, `Payment_Status`, `Flight_Number (FK)`, `Flight_Date (FK)`, `Passenger_Passport (FK)`.

---

## Solved Paper 6: Luxury Hotel Resort Chain ([synth_realistic_4](../../Exams/Papers/synth_realistic/exam_paper_synthetic_and_realistic_4.md))

### Relational Schema Summary
*   **Hotel_Property:** $\underline{\text{Hotel\_Code}}$ (PK), `Hotel_Name`, `Star_Rating`, `Street`, `Number`, `Postal_Code`, `City`, `Country`, `Phone`, `Manager_Emp_ID (FK, UQ)`, `Manager_Start_Date`.
*   **Hotel_Amenity:** $\underline{(\text{Hotel\_Code}, \text{Amenity\_Name})}$ (PK).
*   **Hotel_Room (Weak):** $\underline{(\text{Hotel\_Code}, \text{Room\_Number})}$ (PK), `Floor`, `Category_Type`, `Base_Nightly_Rate`, `Max_Occupancy`.
*   **Employee:** $\underline{\text{Emp\_ID}}$ (PK), `AFM (UQ)`, `First_Name`, `Last_Name`, `Role_Dept`, `Salary`, `Hire_Date`, `Hotel_Code (FK)`, `Supervisor_Emp_ID (FK)`.
*   **Employee_Phone:** $\underline{(\text{Emp\_ID}, \text{Phone\_Number})}$ (PK).
*   **Guest:** $\underline{\text{Passport\_Or\_ADT}}$ (PK), `AFM (UQ)`, `First_Name`, `Last_Name`, `DoB`, `Nationality`, `Email`, `Phone`.
*   **Booking_Reservation:** $\underline{\text{Booking\_ID}}$ (PK), `Reservation_Date`, `CheckIn_Date`, `CheckOut_Date`, `Total_Cost`, `Status`, `Guest_ID (FK)`.
*   **Reservation_Room:** $\underline{(\text{Booking\_ID}, \text{Hotel\_Code}, \text{Room\_Number})}$ (PK).
*   **Service:** $\underline{\text{Service\_Code}}$ (PK), `Service_Name`, `Description`, `Unit_Price`.
*   **Service_Charge:** $\underline{\text{Charge\_ID}}$ (PK), `Booking_ID (FK)`, `Service_Code (FK)`, `Delivery_Timestamp`, `Quantity`, `Billed_Amount`.

---

## Solved Paper 7: E-Commerce Retail Platform ([synth_realistic_5](../../Exams/Papers/synth_realistic/exam_paper_synthetic_and_realistic_5.md))

### Relational Schema Summary
*   **Product_Category:** $\underline{\text{Category\_Code}}$ (PK), `Category_Name`, `Description`, `Parent_Category_Code (FK, Recursive)`, `Manager_Emp_ID (FK, UQ)`, `Appointment_Date`.
*   **Product:** $\underline{\text{SKU}}$ (PK), `Title`, `Brand`, `Retail_Price`, `Stock_Quantity`, `Warranty_Months`, `Category_Code (FK)`.
*   **Product_Color:** $\underline{(\text{SKU}, \text{Color\_Finish})}$ (PK).
*   **Supplier:** $\underline{\text{Supplier\_ID}}$ (PK), `AFM (UQ)`, `Business_Name`, `Representative_Name`, `Street`, `Number`, `Postal_Code`, `City`, `Country`, `Email`.
*   **Supplier_Phone:** $\underline{(\text{Supplier\_ID}, \text{Phone\_Number})}$ (PK).
*   **Supplier_Product:** $\underline{(\text{Supplier\_ID}, \text{Product\_SKU})}$ (PK), `Wholesale_Cost`, `Lead_Time_Days`.
*   **Customer:** $\underline{\text{Customer\_ID}}$ (PK), `AFM (UQ)`, `First_Name`, `Last_Name`, `DoB`, `Reg_Date`, `Email (UQ)`, `Mobile_Phone`.
*   **Customer_Shipping_Address:** $\underline{(\text{Customer\_ID}, \text{Address\_ID})}$ (PK), `Street`, `Number`, `Postal_Code`, `City`, `Country`.
*   **Customer_Order:** $\underline{\text{Order\_Number}}$ (PK), `Order_Timestamp`, `Customer_ID (FK)`, `Delivery_Address_ID (FK)`, `Status`, `Total_Cost`.
*   **Order_Line_Item (Weak):** $\underline{(\text{Order\_Number}, \text{Line\_Number})}$ (PK), `Product_SKU (FK)`, `Quantity`, `Unit_Sale_Price`, `Discount_Rate`.
*   **Payment_Transaction:** $\underline{\text{Transaction\_ID}}$ (PK), `Order_Number (FK)`, `Method`, `Payment_Timestamp`, `Settled_Amount`, `Auth_Code`.

---

## Solved Paper 8: Digital Video Streaming Platform ([synth_realistic_6](../../Exams/Papers/synth_realistic/exam_paper_synthetic_and_realistic_6.md))

### Relational Schema Summary
*   **Media_Title:** $\underline{\text{ISAN}}$ (PK), `Original_Title`, `Release_Year`, `Maturity_Rating`, `Primary_Genre`, `Synopsis`, `Title_Type ('Movie'/'Series')`, `Runtime_Minutes (Null for Series)`.
*   **Media_Dubbing_Language:** $\underline{(\text{ISAN}, \text{Language\_Code})}$ (PK).
*   **Media_Subtitle_Language:** $\underline{(\text{ISAN}, \text{Language\_Code})}$ (PK).
*   **TV_Series_Episode (Weak):** $\underline{(\text{Series\_ISAN}, \text{Season\_No}, \text{Episode\_No})}$ (PK), `Title`, `Duration_Minutes`, `Premiere_Date`.
*   **Contributor:** $\underline{\text{Contributor\_ID}}$ (PK), `First_Name`, `Last_Name`, `DoB`, `Nationality`, `Bio`.
*   **Media_Cast_Crew:** $\underline{(\text{ISAN}, \text{Contributor\_ID}, \text{Role\_Name})}$ (PK), `Billing_Order`, `Character_Name`.
*   **Subscriber:** $\underline{\text{Subscriber\_ID}}$ (PK), `AFM (UQ)`, `Email (UQ)`, `Reg_Date`, `Tier`, `Monthly_Price`.
*   **Viewing_Profile (Weak):** $\underline{(\text{Subscriber\_ID}, \text{Profile\_Name})}$ (PK), `Avatar_Icon`, `Maturity_Filter`, `Preferred_Language`.
*   **Playback_Session:** $\underline{\text{Session\_ID}}$ (PK), `Subscriber_ID (FK)`, `Profile_Name (FK)`, `Target_ISAN (FK)`, `Season_No (FK, Null)`, `Episode_No (FK, Null)`, `Start_Timestamp`, `Duration_Watched_Min`, `Device_Type`, `Completed_Flag`.
*   **User_Review:** $\underline{(\text{Subscriber\_ID}, \text{Profile\_Name}, \text{ISAN})}$ (PK), `Submission_Timestamp`, `Star_Rating (1-5)`, `Commentary`, `Helpful_Score`.

---

## Solved Paper 9: Metropolitan Municipal Library ([synth_realistic_7](../../Exams/Papers/synth_realistic/exam_paper_synthetic_and_realistic_7.md))

### Relational Schema Summary
*   **Library_Branch:** $\underline{\text{Branch\_ID}}$ (PK), `Branch_Name (UQ)`, `Street`, `Number`, `Postal_Code`, `Neighborhood`, `Phone`, `Seating_Capacity`, `Head_Librarian_ID (FK, UQ)`, `Appointment_Date`.
*   **Branch_Opening_Hours:** $\underline{(\text{Branch\_ID}, \text{Day\_Of\_Week})}$ (PK), `Open_Time`, `Close_Time`.
*   **Book_Title:** $\underline{\text{ISBN}}$ (PK), `Title`, `Publisher`, `Pub_Year`, `Subject_Classification`, `Page_Count`.
*   **Author:** $\underline{\text{Author\_ID}}$ (PK), `Full_Name`, `Nationality`, `Birth_Year`.
*   **Book_Author:** $\underline{(\text{ISBN}, \text{Author\_ID})}$ (PK).
*   **Book_Copy (Weak/Inventory):** $\underline{\text{Copy\_Barcode}}$ (PK), `ISBN (FK)`, `Branch_ID (FK)`, `Shelf_Condition`, `Acquisition_Date`, `Call_Number_Shelf_Tag`, `Availability_Status`.
*   **Library_Member:** $\underline{\text{Member\_Card\_No}}$ (PK), `AFM (UQ)`, `First_Name`, `Last_Name`, `DoB`, `Reg_Date`, `Exp_Date`, `Email (UQ)`, `Phone`, `Street`, `Number`, `Postal_Code`, `City`.
*   **Circulation_Loan:** $\underline{\text{Loan\_ID}}$ (PK), `Member_Card_No (FK)`, `Copy_Barcode (FK)`, `Checkout_Timestamp`, `Due_Date`, `Actual_Return_Date`, `Overdue_Fee_Paid`.
*   **Hold_Reservation:** $\underline{\text{Reservation\_ID}}$ (PK), `Member_Card_No (FK)`, `Target_ISBN (FK)`, `Pickup_Branch_ID (FK)`, `Request_Timestamp`, `Queue_Position`, `Fulfillment_Status`.

---

## Solved Paper 10: Professional Sports League Federation ([synth_realistic_8](../../Exams/Papers/synth_realistic/exam_paper_synthetic_and_realistic_8.md))

### Relational Schema Summary
*   **Sports_Team:** $\underline{\text{Team\_ID}}$ (PK), `Official_Name (UQ)`, `Home_City`, `Founding_Year`, `Stadium_Name`, `Seating_Capacity`, `Head_Coach_ID (FK, UQ)`, `Coach_Contract_Start`.
*   **Team_Color:** $\underline{(\text{Team\_ID}, \text{Color\_Name})}$ (PK).
*   **Coach:** $\underline{\text{Coach\_ID}}$ (PK), `AFM (UQ)`, `Full_Name`, `DoB`, `Nationality`, `Certification_Tier`, `Mobile_Phone`.
*   **Athlete:** $\underline{\text{Athlete\_Reg\_No}}$ (PK), `ADT (UQ)`, `First_Name`, `Last_Name`, `DoB`, `Height_CM`, `Weight_KG`, `Nationality`, `Primary_Position`, `Current_Team_ID (FK)`, `Jersey_Number`, `Contract_Start`, `Contract_End`, `Annual_Salary`.
*   **League_Match:** $\underline{\text{Match\_ID}}$ (PK), `Round_Number`, `Match_DateTime`, `Venue_Stadium`, `Referee_Name`, `Home_Team_ID (FK)`, `Away_Team_ID (FK)`, `Home_Score`, `Away_Score`, `CHECK (Home_Team_ID <> Away_Team_ID)`.
*   **Match_Event (Weak):** $\underline{(\text{Match\_ID}, \text{Event\_No})}$ (PK), `Match_Minute`, `Event_Type ('Goal', 'Yellow_Card', 'Red_Card', 'Sub', 'Penalty')`, `Athlete_Reg_No (FK)`.
*   **Athlete_Injury_Record (Weak):** $\underline{(\text{Athlete\_Reg\_No}, \text{Incident\_No})}$ (PK), `Incident_Date`, `Diagnosis_Type`, `Estimated_Recovery_Weeks`, `Clearance_Date`.

---

*End of test_prep.md — Complete preparation file with 160 thematic practice drill questions and 10 fully solved exam papers for Database Systems (Course 404).*
