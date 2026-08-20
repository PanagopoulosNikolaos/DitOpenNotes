**Databases - Midterm Exam / Progress Test**
**Department of Informatics and Telecommunications**
**Academic Year 2025-2026**

---

### Scenario Description (Topic)

A large university hospital is designing a new database management system for comprehensive operational tracking, including clinics, physicians, patients, admissions/hospitalizations, and administered medical treatments.

1. **Clinics:**
   Each clinic is characterized by a unique clinic code (e.g., `K01`, `K02`), a unique name (e.g., "Cardiology", "Neurology"), the floor on which it is housed, and the administrative office telephone number. Each clinic is mandatorily directed by a specific physician (Clinic Director), for whom the date of taking office is recorded. A physician can direct at most one clinic. Additionally, each clinic may have specialized wings/facilities located in various buildings across the hospital complex (multiple locations).

2. **Medical Staff (Doctors):**
   For each physician, the following data are recorded: unique medical license number (AMI), Tax Identification Number (AFM), first name, last name, medical specialty, rank/title (e.g., Attending Physician A', Attending Physician B', Department Chair), monthly base salary, hiring date, and residential address (composed of street, number, postal code, and city). A physician may have more than one contact telephone number (e.g., internal extension, mobile). Each physician belongs mandatorily to exactly one clinic, while multiple physicians serve in each clinic. Furthermore, an experienced physician may supervise and guide junior resident physicians (each resident has one direct supervisor physician, whereas a supervisor may guide multiple residents).

3. **Dependents:**
   For insurance and tax purposes, the institution records the dependent family members of physicians. For each dependent member, the following are kept: first name, gender, date of birth, and family relationship (e.g., child, spouse). The name of the dependent is unique only within the context of the family of the specific physician.

4. **Patients:**
   For each patient, the following are recorded: unique Social Security Number (AMKA), National ID Number (ADT), first name, last name, date of birth, gender, blood type, and current age (which is calculated dynamically from the date of birth).

5. **Admissions / Hospitalizations:**
   Each time a patient is admitted to the hospital, a new hospitalization incident is recorded. For each hospitalization, the following are recorded: a sequential admission number for the specific patient, admission date and time, discharge date and time (if completed), room number, initial diagnosis, and the clinic in which the hospitalization takes place. A patient may have multiple hospitalizations over time, but each hospitalization pertains exclusively to one patient and is conducted within a single clinic.

6. **Treatments & Medications:**
   The hospital maintains a formulary catalog of medications. Each drug has a unique national medication code (EOF), commercial trade name, active pharmaceutical ingredient, and unit of measurement (e.g., mg, ml). During a hospitalization, an attending physician prescribes and administers medications to the admitted patient. For each drug administration during a specific hospitalization, the following are recorded: dosage, intake frequency per 24 hours, start date, and end date of the treatment regimen.

---

### Exam Questions

#### A (4 points): Conceptual Analysis

In the text above, identify and document:

1. The **entities** (and their type: strong or weak; for weak entities indicate the identifying entity).
2. The **attributes** of each entity (and their type: simple, composite, single-valued, multi-valued, derived).
3. The **keys** (how many each entity has, their type, and your final choice for the primary key; for weak entities the partial key).
4. The **relationships** and the **cardinality ratio** (1:1, 1:N, N:M), with full justification.

#### B (3 points): E-R Diagram

Draw the **Entity-Relationship (E-R)** diagram for this database. You are free (within the framework defined by the above specifications) to make any choices you consider appropriate, providing the rationale you consider correct.

#### C (3 points): Table Structure

Then show the structure of the tables with which the database will be implemented according to the diagram you drew. The tables must be written in tabular format, with **underlining of the primary key** and clear indication of the **foreign keys** (and the tables/columns to which they refer).

**Good luck!**
