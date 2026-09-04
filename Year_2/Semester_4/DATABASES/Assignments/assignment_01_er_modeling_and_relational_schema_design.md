# Assignment 01: Conceptual ER Modeling and Relational Schema Translation

This assignment tests students on conceptual data modeling for an enterprise domain, translating business requirements into a formal Entity-Relationship (ER) diagram, and mapping the diagram into a fully constrained relational database schema.

---

## 1. Domain Specification: Regional Hospital Healthcare System

A regional healthcare provider requires a database management system to manage its clinics, medical doctors, registered patients, and diagnostic treatments.

### Business Rules and Invariants
1. **Clinics:** Each clinic has a unique clinic identifier (`clinic_id`), an official name, an emergency phone number, and a physical location address (street, city, zip code).
2. **Doctors:** Each doctor has a unique medical license number (`doctor_id`), full name, clinical specialty, and date of hire.
   - Each doctor is assigned to work at exactly one primary clinic.
   - A clinic employs many doctors, but must employ at least one doctor.
3. **Clinic Directors:** Each clinic is directed by exactly one doctor. A doctor can direct at most one clinic. The start date of the directorship appointment must be recorded.
4. **Patients:** Each patient has a unique social security number (`ssn`), full name, date of birth, and home contact number.
5. **Appointments:** A patient schedules appointments with doctors.
   - An appointment is uniquely identified by its date and time combination for a given doctor.
   - An appointment involves exactly one patient and exactly one doctor.
   - During an appointment, the consulting doctor may prescribe zero, one, or multiple diagnostic medications/treatments.
   - The diagnosis notes and fee charged must be stored.
6. **Patient Emergency Contacts (Weak Entity):** Each patient may specify one or more emergency contacts. An emergency contact has a contact name, relationship to patient, and phone number. Emergency contacts are dependent on the patient for identification.

---

## 2. Deliverables and Format

### Part 1: Conceptual ER Design (40 Points)
- Identify all entity types, distinguishing between strong and weak entities.
- Identify all relationship types, explicitly specifying cardinality ratios ($1:1$, $1:N$, $M:N$) and participation constraints (total vs. partial).
- Document and explain any design assumptions made.

### Part 2: Relational Schema Mapping (40 Points)
Apply the formal 7-step mapping algorithm to produce relational table schemas:
- Represent each table in standard relational notation:
  $$\text{Table}(\underline{\text{primary\_key}}, \text{attribute}_1, \text{foreign\_key} \uparrow \text{TargetTable})$$
- Underline primary keys.
- Clearly annotate foreign keys and referenced tables.
- Identify all junction tables created and their composite primary keys.

### Part 3: DDL Implementation Script (20 Points)
Write a clean, runnable SQL script (`schema.sql`) creating all tables with primary keys, foreign keys, `ON DELETE` referential integrity clauses, and column domain constraints.

---

## 3. Evaluation Rubric

| Criteria | Points |
|---|---|
| Correct identification of entities, attributes, and weak entities | 25 |
| Accurate cardinality and participation constraint definitions | 25 |
| Rigorous application of ER-to-relational mapping algorithm | 30 |
| DDL constraint precision (`NOT NULL`, `CHECK`, `FOREIGN KEY` actions) | 20 |

