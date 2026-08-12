Below is the improved exam. Improvements: unified notation legend at the beginning, cleaner structure, more precise wording, repetitions removed, and 2 new exercises added (Exercise 7: SQL Subqueries, Exercise 8: BCNF).

***

# All-In-One Exam: Advanced Database Design, Translation & SQL

> **Notation Legend (applies throughout):**
> `Entity/Table` | <u>Attribute</u> | **Primary Key** | <u>*Foreign Key*</u>

This exam consists of two parts:
- **Part A** — Advanced E-R design, translation to the Relational Model, identification of pitfalls (recursive relationships, weak entities).
- **Part B** — Relational Algebra, SQL (joins, groupings, subqueries), Normalization (2NF → 3NF → BCNF).

***

## PART A: Advanced E-R Design and Translation to the Relational Model

### Exercise 1: Extraction of Entities, Attributes, Keys and Relationships

Read the following specification describing the information system of a network of hospital units:

> *"A network of hospital units manages independent clinics. Each clinic carries a unique registration number, by which it is identified. Its name, its multiple telephone lines of communication (there may be more than one) and its address, which is decomposed into street, number and city, are also recorded.*
>
> *The medical staff is identified exclusively by its AMKA (Social Security Number). Each physician has a first name, a last name, a date of recruitment and a specialty. Each physician organically belongs to exactly one clinic, while a clinic is staffed by many physicians. Moreover, each clinic is headed by exactly one physician — for this assignment, a monthly management allowance is recorded. In parallel, an experienced physician may supervise (as a mentor) many junior physicians, creating a recursive relationship within the same entity.*
>
> *Patients are identified by their AMKA. Their full name, blood group and date of birth are kept. A physician may examine many patients and vice versa. For each examination, the date, the time and the medical diagnosis are recorded.*
>
> *The patients are accompanied by relatives, who have no autonomous existence in the system without the associated patient. For each relative, an ID number, a name and a phone number are recorded.*
>
> *Each clinic has hospitalization wards. Each ward has a ward number (unique only within the clinic) and a maximum capacity. Patients are hospitalized in wards — a patient may be hospitalized in many wards over time, and each ward hosts many patients. For each hospitalization, the admission date and the discharge date are recorded."*

**Required:** Analyze and record:
- The **Entities** (strong and weak) with their **Attributes** and their **Primary Keys**.
- All **Relationships** between entities with **cardinality** and any **relationship attributes**.

***

*solution:*

**Entities and Attributes:**

1. `Clinic` *(Strong)*
   - **registration_number**, <u>name</u>, <u>phones</u> *(Multivalued)*, <u>address</u> *(Composite: street, number, city)*

2. `Physician` *(Strong)*
   - **AMKA**, <u>first_name</u>, <u>last_name</u>, <u>recruitment_date</u>, <u>specialty</u>

3. `Patient` *(Strong)*
   - **AMKA**, <u>full_name</u>, <u>blood_group</u>, <u>birth_date</u>

4. `Relative` *(Weak — depends on `Patient`)*
   - **ID_number** *(Partial Key)*, <u>name</u>, <u>phone</u>

5. `Ward` *(Weak — depends on `Clinic`)*
   - **ward_number** *(Partial Key)*, <u>capacity</u>

**Relationships:**

| # | Relationship | Entities | Cardinality | Relationship Attributes |
|---|-------|-----------|-------------|-------------------|
| 1 | **Belongs** | `Clinic` — `Physician` | 1:N | — |
| 2 | **Heads** | `Clinic` — `Physician` | 1:1 | <u>management_allowance</u> |
| 3 | **Supervises** *(recursive)* | `Physician` — `Physician` | 1:N | — |
| 4 | **Examines** | `Physician` — `Patient` | M:N | <u>date</u>, <u>time</u>, <u>diagnosis</u> |
| 5 | **Accompanies** *(identifying)* | `Patient` — `Relative` | 1:N | — |
| 6 | **Has** *(identifying)* | `Clinic` — `Ward` | 1:N | — |
| 7 | **Is hospitalized** | `Patient` — `Ward` | M:N | <u>admission_date</u>, <u>discharge_date</u> |

***

### Exercise 2: E-R Diagram Design

Design the E-R diagram of Exercise 1 in **Mermaid.js**. Render with clarity:
- Weak entities and their identifying relationships.
- Recursive relationships.
- Relationship attributes (inline on the relationship).

***

*solution:*

![hospital-er-diagram-1](../assets/diagrams/hospital-er-diagram-1.png)

### Exercise 3: Translation to the Relational Model

Translate the diagram of Exercise 2 into tables. For each table, specify: Primary Keys, Foreign Keys, and the reason for existence of each intermediate table.

***

*solution:*

1. `Κλινική`(**αριθμός_μητρώου**, <u>όνομα</u>, <u>οδός</u>, <u>αριθμός</u>, <u>πόλη</u>, <u>*διευθυντής_ΑΜΚΑ*</u>, <u>επίδομα_διεύθυνσης</u>)
   - <u>*διευθυντής_ΑΜΚΑ*</u> → FK to `Ιατρός`. Encapsulates the "heads" relationship (1:1) together with the relationship attribute.

2. `Κλινική_Τηλέφωνα`(**αριθμός_μητρώου**, **τηλέφωνο**)
   - Represents the multivalued attribute. <u>*αριθμός_μητρώου*</u> → FK to `Κλινική`.

3. `Ιατρός`(**ΑΜΚΑ**, <u>όνομα</u>, <u>επώνυμο</u>, <u>ημερ_πρόσληψης</u>, <u>ειδικότητα</u>, <u>*κλινική_ΑΜ*</u>, <u>*μέντορας_ΑΜΚΑ*</u>)
   - <u>*κλινική_ΑΜ*</u> → FK to `Κλινική` ("belongs" relationship, 1:N).
   - <u>*μέντορας_ΑΜΚΑ*</u> → self-referencing FK to `Ιατρός` (recursive relationship 1:N, nullable).

4. `Ασθενής`(**ΑΜΚΑ**, <u>ονοματεπώνυμο</u>, <u>ομάδα_αίματος</u>, <u>ημερ_γέννησης</u>)

5. `Συγγενικό_Πρόσωπο`(**ασθενής_ΑΜΚΑ**, **ΑΔΤ**, <u>όνομα</u>, <u>τηλέφωνο</u>)
   - Composite PK due to the weak entity. <u>*ασθενής_ΑΜΚΑ*</u> → FK to `Ασθενής`.

6. `Θάλαμος`(**κλινική_ΑΜ**, **αριθμός_θαλάμου**, <u>χωρητικότητα</u>)
   - Composite PK due to the weak entity. <u>*κλινική_ΑΜ*</u> → FK to `Κλινική`.

7. `Εξέταση`(**ιατρός_ΑΜΚΑ**, **ασθενής_ΑΜΚΑ**, **ημερομηνία**, **ώρα**, <u>διάγνωση</u>)
   - Intermediate table for the M:N relationship. The composite PK ensures that the same pair (physician, patient) may have multiple examinations on different date/time.

8. `Νοσηλεία`(**ασθενής_ΑΜΚΑ**, **κλινική_ΑΜ**, **αριθμός_θαλάμου**, **ημερ_εισαγωγής**, <u>ημερ_εξιτηρίου</u>)
   - Intermediate table for the M:N relationship. The FK to `Θάλαμος` is composite (κλινική_ΑΜ + αριθμός_θαλάμου), so both parts are carried over. The **ημερ_εισαγωγής** in the key allows re-hospitalization in the same ward.

***
***

## PART B: Relational Algebra, SQL, and Normalization

**E-commerce schema (applies to Exercises 4–7):**

`Πελάτης`(**Κωδ_Πελάτη**, <u>Όνομα</u>, <u>Επώνυμο</u>, <u>Πόλη</u>)
`Παραγγελία`(**Κωδ_Παραγγελίας**, <u>Ημερομηνία</u>, <u>*Πελάτης_Κωδικός*</u>)
`Προϊόν`(**Κωδ_Προϊόντος**, <u>Περιγραφή</u>, <u>Τιμή</u>, <u>Κατηγορία</u>)
`Περιλαμβάνει`(**Κωδ_Παραγγελίας**, **Κωδ_Προϊόντος**, <u>Ποσότητα</u>)

***

### Exercise 4: Relational Algebra

Write the Relational Algebra expression that returns the <u>Name</u> and the <u>Last Name</u> of all customers who have purchased at least one product from the category `'Smartphones'`.

***

*solution:*

**Step by step:**

- **R1** = $\sigma$\_\{Κατηγορία = 'Smartphones'\}(`Προϊόν`) — Filtering of products
- **R2** = R1 ⨝ `Περιλαμβάνει` — Finding the orders that contain them
- **R3** = R2 ⨝ `Παραγγελία` — Finding the customer codes
- **R4** = R3 ⨝ `Πελάτης` — Bringing the names
- **Result** = $\pi$\_\{Όνομα, Επώνυμο\}(R4)

**In summary (single expression):**

$$\pi_{\text{Όνομα, Επώνυμο}}\bigl(\text{Πελάτης} \bowtie \text{Παραγγελία} \bowtie \text{Περιλαμβάνει} \bowtie \sigma_{\text{Κατηγορία}=\text{'Smartphones'}}(\text{Προϊόν})\bigr)$$

> **Observation:** The result may contain duplicates (the same customer may have purchased Smartphones in multiple orders). If uniqueness is required, it is applied implicitly by the semantics of Relational Algebra (sets), so no additional operation is required.

***

### Exercise 5: SQL — Joins, GROUP BY, HAVING

Write an SQL query that returns the <u>Name</u>, the <u>Last Name</u> and the **Total Purchase Amount** of each customer historically, **only** for customers with a total amount > 2500€. Sort descending by total amount.

> *The line amount = Quantity × Price.*

***

*solution:*

```sql
SELECT
    p.Όνομα,
    p.Επώνυμο,
    SUM(per.Ποσότητα * pro.Τιμή) AS Συνολικό_Ποσό
FROM
    Πελάτης       p
    INNER JOIN Παραγγελία    par ON p.Κωδ_Πελάτη       = par.Πελάτης_Κωδικός
    INNER JOIN Περιλαμβάνει per ON par.Κωδ_Παραγγελίας = per.Κωδ_Παραγγελίας
    INNER JOIN Προϊόν        pro ON per.Κωδ_Προϊόντος   = pro.Κωδ_Προϊόντος
GROUP BY
    p.Κωδ_Πελάτη, p.Όνομα, p.Επώνυμο
HAVING
    SUM(per.Ποσότητα * pro.Τιμή) > 2500
ORDER BY
    Συνολικό_Ποσό DESC;
```

> **Why `Κωδ_Πελάτη` in the `GROUP BY`;** The `GROUP BY` must include the PK so that customers with the same name/last name but a different code are not confused. The `HAVING` filters *after* the grouping, in contrast to the `WHERE`, which filters before.

***

### Exercise 6: Normalization Theory — 1NF → 3NF

Given the unnormalized table:

`Ανάθεση_Υπαλλήλου`(**Κωδ_Υπαλλήλου**, **Κωδ_Υποκαταστήματος**, <u>Όνομα_Υπαλλήλου</u>, <u>Βαθμίδα_Υπαλλήλου</u>, <u>Διεύθυνση_Υποκαταστήματος</u>, <u>Ώρες_Απασχόλησης</u>)

**Questions:**
1. Which **Functional Dependencies** hold;
2. In which **Normal Form** is the table and why;
3. Decompose it into **3NF**.

***

*solution:*

**1. Functional Dependencies:**
- **Κωδ_Υπαλλήλου** → <u>Όνομα_Υπαλλήλου</u>, <u>Βαθμίδα_Υπαλλήλου</u>
- **Κωδ_Υποκαταστήματος** → <u>Διεύθυνση_Υποκαταστήματος</u>
- {**Κωδ_Υπαλλήλου**, **Κωδ_Υποκαταστήματος**} → <u>Ώρες_Απασχόλησης</u>

**2. Normal Form:**
The table is in **1NF** (all fields are atomic), but **NOT in 2NF** due to **partial dependencies**: the <u>Όνομα_Υπαλλήλου</u> / <u>Βαθμίδα</u> depend only on the **Κωδ_Υπαλλήλου**, and the <u>Διεύθυνση_Υποκαταστήματος</u> only on the **Κωδ_Υποκαταστήματος** — not on the whole composite key.

**3. Decomposition into 3NF:**

- `Υπάλληλος`(**Κωδ_Υπαλλήλου**, <u>Όνομα_Υπαλλήλου</u>, <u>Βαθμίδα_Υπαλλήλου</u>)
- `Υποκατάστημα`(**Κωδ_Υποκαταστήματος**, <u>Διεύθυνση_Υποκαταστήματος</u>)
- `Ανάθεση`(**Κωδ_Υπαλλήλου**, **Κωδ_Υποκαταστήματος**, <u>Ώρες_Απασχόλησης</u>)

In each table, every non-key attribute depends **fully, directly and only** on the (entire) key → 3NF ✓.

***

### Exercise 7: SQL — Subqueries & EXISTS *(New)*

Using the same e-commerce schema, write an SQL query that returns the **Name** and the **Last Name** of customers who **have ordered from ALL product categories** that exist in the database.

> *Hint: Think about when a customer has NOT ordered from a category — and use `NOT EXISTS`.*

***

*solution:*

The classic way to express "for every X, Y holds" in SQL is through **double negation** (`NOT EXISTS ... NOT EXISTS`):

```sql
-- Πελάτες για τους οποίους ΔΕΝ υπάρχει κατηγορία
-- από την οποία ΔΕΝ έχουν αγοράσει
SELECT p.Όνομα, p.Επώνυμο
FROM Πελάτης p
WHERE NOT EXISTS (
    -- Κατηγορία που ο πελάτης ΔΕΝ έχει αγοράσει
    SELECT DISTINCT pro.Κατηγορία
    FROM Προϊόν pro
    WHERE NOT EXISTS (
        -- Έλεγχος αν ο πελάτης έχει αγοράσει από αυτή την κατηγορία
        SELECT 1
        FROM Παραγγελία       par
             INNER JOIN Περιλαμβάνει per ON par.Κωδ_Παραγγελίας = per.Κωδ_Παραγγελίας
             INNER JOIN Προϊόν        pi  ON per.Κωδ_Προϊόντος   = pi.Κωδ_Προϊόντος
        WHERE par.Πελάτης_Κωδικός = p.Κωδ_Πελάτη
          AND pi.Κατηγορία = pro.Κατηγορία
    )
);
```

**Alternative (with COUNT):**

```sql
SELECT p.Όνομα, p.Επώνυμο
FROM Πελάτης p
     INNER JOIN Παραγγελία    par ON p.Κωδ_Πελάτη         = par.Πελάτης_Κωδικός
     INNER JOIN Περιλαμβάνει per ON par.Κωδ_Παραγγελίας   = per.Κωδ_Παραγγελίας
     INNER JOIN Προϊόν        pro ON per.Κωδ_Προϊόντος     = pro.Κωδ_Προϊόντος
GROUP BY p.Κωδ_Πελάτη, p.Όνομα, p.Επώνυμο
HAVING COUNT(DISTINCT pro.Κατηγορία) = (SELECT COUNT(DISTINCT Κατηγορία) FROM Προϊόν);
```

> **Which one do we prefer;** The `COUNT` version is usually more readable and efficient. The `NOT EXISTS` version is the *semantically direct* translation of the "universal quantification" (∀) logic into SQL.

***

### Exercise 8: Normalization — BCNF *(New)*

Given the teaching table of a university (already in 3NF):

`Διδασκαλία`(**Φοιτητής**, **Μάθημα**, <u>Καθηγητής</u>)

The following additional information (semantic constraints) holds:
- Each **Καθηγητής** teaches exactly **one Μάθημα**.
- Each **Φοιτητής** in a **Μάθημα** may have many Καθηγητές (e.g., section leaders/laboratory).

**Questions:**
1. Which **Functional Dependencies** hold;
2. Why is the table **in 3NF but NOT in BCNF**;
3. Decompose it into **BCNF** and explain whether the decomposition is **lossless** but also whether it preserves dependencies (dependency-preserving).

***

*solution:*

**1. Functional Dependencies:**
- {**Φοιτητής**, **Μάθημα**} → <u>Καθηγητής</u> — (a student in a course has a specific professor)
- {**Φοιτητής**, **Καθηγητής**} → **Μάθημα** — (the professor teaches exactly one course)
- **Καθηγητής** → **Μάθημα** — (critical: each professor belongs to exactly one course)

The candidate keys are: `{Φοιτητής, Μάθημα}` and `{Φοιτητής, Καθηγητής}`.

**2. 3NF YES, BCNF NO:**
BCNF definition: for every non-trivial FD **X → Y**, **X must be a superkey**.

The dependency **Καθηγητής → Μάθημα** violates BCNF: **Καθηγητής** is not a superkey (it does not alone determine the student). However, it does not violate 3NF because **Μάθημα** is a *prime attribute* (part of some candidate key).

> **The classic "trick":** 3NF allows FDs from a non-superkey to a prime attribute. BCNF does not allow it at all.

**3. Decomposition into BCNF:**

- `Καθηγητής_Μάθημα`(**Καθηγητής**, <u>Μάθημα</u>)
- `Εγγραφή`(**Φοιτητής**, **Καθηγητής**)

**Lossless join check:** Yes — the two tables are connected through **Καθηγητής** (common attribute, superkey in `Καθηγητής_Μάθημα`) → it satisfies the lossless-join decomposition criterion.

**Dependency preservation check:** **NOT fully** — the dependency `{Φοιτητής, Μάθημα} → Καθηγητής` cannot be checked in a single table (it requires a join). This is the classic BCNF trade-off: **always lossless, but does not guarantee dependency preservation**.
