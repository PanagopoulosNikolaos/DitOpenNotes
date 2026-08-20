**Databases - Midterm Exam / Progress Test**
**Department of Informatics and Telecommunications**
**Academic Year 2025-2026**

---

### Scenario Description (Topic)

A public university is developing a comprehensive database management system to handle academic departments, faculty members, students, course offerings, and semester enrollments.

1. **Academic Departments:**
   Each department is characterized by a unique department code (e.g., `CS`, `MATH`), a unique department name (e.g., "Computer Science and Telecommunications", "Mathematics"), the central building in which it is housed, and the secretariat telephone number. Each department is mandatorily chaired by a specific professor (Department Chair), for whom the appointment date is recorded. A professor may chair at most one department. Furthermore, each department manages specialized teaching and research laboratory facilities located across multiple campus buildings (multiple locations).

2. **Faculty Members (Professors):**
   For each professor, the following data are recorded: unique faculty registration number (AM), Tax Identification Number (AFM), first name, last name, academic rank (e.g., Assistant Professor, Associate Professor, Full Professor), monthly salary, date of appointment, and residential address (street, number, postal code, city). A professor may possess multiple contact phone numbers (e.g., office extension, mobile). Each professor belongs mandatorily to exactly one department, while multiple professors serve in each department. Additionally, an experienced senior professor may act as a formal academic advisor/mentor to junior faculty members (each junior faculty member has one assigned mentor, while a mentor may guide multiple junior faculty members).

3. **Dependents:**
   For health insurance and tax deduction purposes, the university maintains records of professors' dependent family members: first name, gender, date of birth, and relationship (e.g., child, spouse). The name of the dependent is unique only within the family of the specific professor.

4. **Students:**
   For each student, the following data are recorded: unique Student Registration Number (AM), National ID Number (ADT), first name, last name, date of birth, gender, admission year, and current study semester (which is calculated dynamically based on the admission year). Each student belongs mandatorily to a single department.

5. **Courses:**
   Each course is characterized by a unique course code (e.g., `CS101`, `CS204`), course title, ECTS credits, course category (e.g., "Compulsory Core", "Elective"), intended semester of study, and the department offering it. A course may have prerequisite courses (a course may require one or more prerequisite courses to be taken beforehand, while a course can serve as a prerequisite for multiple other courses).

6. **Teaching Assignments & Enrollments:**
   Each semester, professors are assigned to teach specific courses (a professor may teach multiple courses, and a course may be co-taught by multiple professors). Students enroll in courses each academic semester. For each student course enrollment, the following are recorded: academic year, semester (Winter/Spring), final exam score (0.0–10.0), and examination date.

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
