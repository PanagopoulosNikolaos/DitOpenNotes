# Practice Exam 01: Database Systems (Course 404)

This practice examination tests proficiency across conceptual Entity-Relationship design, relational schema mapping, formal relational algebra queries, SQL query formulation, and normalization theory (candidate keys, 3NF synthesis).

**Duration:** 2 Hours  
**Total Points:** 100 Points  

---

## Part A: Conceptual ER Modeling and Schema Mapping (35 Points)

### Scenario
A university research institute manages scientific projects, researchers, publications, and grant funding bodies:
- **Researchers:** Identified by `researcher_id`. Stores full name, email, academic rank, and primary office room.
- **Projects:** Identified by `project_code`. Stores project title, start date, end date, and total grant budget.
  - A project is led by exactly one Principal Investigator (PI), who must be a researcher. A researcher may lead zero, one, or multiple projects.
  - Multiple researchers work on a project. A researcher may work on multiple projects. For each researcher working on a project, the weekly hours contributed must be recorded.
- **Grants:** A project receives funding from one or more external Grant Agencies. Each agency has an `agency_id`, name, and contact country. An agency awards multiple grants. Each grant award specifies an `award_number` (unique within that agency), awarded amount, and approval date. (Grant is a weak entity dependent on Agency).
- **Publications:** Identified by `doi`. Stores paper title, publication year, and journal name. A publication can be produced by one or more projects, and acknowledges their support.

### Question 1 (20 Points)
Identify all entity types (strong and weak), relationship types, attribute lists, key attributes, cardinality ratios ($1:1$, $1:N$, $M:N$), and participation constraints (total vs. partial).

### Question 2 (15 Points)
Apply the 7-step ER-to-Relational mapping algorithm to produce the complete relational database schema. Write each table with its name, attributes, underlined primary keys, and foreign keys.

---

## Part B: Relational Algebra and Formal Queries (20 Points)

Given relational schemas:
- $\text{Student}(\underline{\text{sid}}, \text{name}, \text{major}, \text{gpa})$
- $\text{Course}(\underline{\text{cid}}, \text{cname}, \text{dept}, \text{credits})$
- $\text{Enrolled}(\underline{\text{sid} \uparrow \text{Student}, \text{cid} \uparrow \text{Course}}, \text{grade})$

Write formal Relational Algebra expressions for:
### Question 3 (10 Points)
Find the names and GPAs of all students majoring in `'CS'` who have earned a grade of at least `8.5` in a course offered by the `'CS'` department.

### Question 4 (10 Points)
Find the student IDs and names of students who have enrolled in **all** courses offered by the `'CS'` department.

---

## Part C: SQL Data Definition and Complex Queries (25 Points)

### Question 5 (10 Points)
Write SQL DDL to create the $\text{Enrolled}$ table, ensuring:
- Composite primary key on $(\text{sid}, \text{cid})$.
- Foreign keys with `ON DELETE CASCADE`.
- A check constraint enforcing that `grade` is between `0.0` and `10.0`.

### Question 6 (15 Points)
Write an SQL query to retrieve the department name, course title, and the number of students enrolled for every course that has strictly more than 3 enrolled students, ordered by total students descending.

---

## Part D: Functional Dependencies and Normalization (20 Points)

### Question 7 (20 Points)
Given relation $R(A, B, C, D, E)$ with functional dependencies:

$$
F = \{ A \to BC, \ CD \to E, \ B \to D, \ E \to A \}
$$

1. Calculate the attribute closure $B^+$.
2. Find all candidate keys of $R$.
3. Determine the highest normal form (1NF, 2NF, 3NF, or BCNF) of $R$. Justify your answer.

---

## Complete Solution and Grading Guide

### Solution to Part A

#### Question 1: ER Components
- **Entities:**
  - Strong: $\text{Researcher}(\underline{\text{researcher\_id}}, \text{name}, \text{email}, \text{rank}, \text{office})$
  - Strong: $\text{Project}(\underline{\text{project\_code}}, \text{title}, \text{start\_date}, \text{end\_date}, \text{budget})$
  - Strong: $\text{Agency}(\underline{\text{agency\_id}}, \text{name}, \text{country})$
  - Weak: $\text{Grant}(\underline{\text{award\_number}}, \text{amount}, \text{approval\_date})$ [Identifying entity: $\text{Agency}$]
  - Strong: $\text{Publication}(\underline{\text{doi}}, \text{title}, \text{year}, \text{journal})$
- **Relationships:**
  - $\text{Leads}$: $1:N$ between $\text{Researcher}$ ($1$) and $\text{Project}$ ($N$). Total participation for $\text{Project}$ (every project has a PI).
  - $\text{Works\_On}$: $M:N$ between $\text{Researcher}$ and $\text{Project}$. Attribute: `weekly_hours`.
  - $\text{Funds}$: $1:N$ between $\text{Agency}$ and $\text{Grant}$ (identifying relationship).
  - $\text{Finances}$: $1:N$ between $\text{Grant}$ and $\text{Project}$.
  - $\text{Produces}$: $M:N$ between $\text{Project}$ and $\text{Publication}$.
*(20 Points)*

#### Question 2: Relational Schema Mapping
1. $\text{Researcher}(\underline{\text{researcher\_id}}, \text{name}, \text{email}, \text{rank}, \text{office})$
2. $\text{Agency}(\underline{\text{agency\_id}}, \text{name}, \text{country})$
3. $\text{Grant}(\underline{\text{agency\_id} \uparrow \text{Agency}, \text{award\_number}}, \text{amount}, \text{approval\_date})$
4. $\text{Project}(\underline{\text{project\_code}}, \text{title}, \text{start\_date}, \text{end\_date}, \text{budget}, \text{pi\_id} \uparrow \text{Researcher}, \text{agency\_id} \uparrow \text{Grant}, \text{award\_number} \uparrow \text{Grant})$
5. $\text{ProjectResearcher}(\underline{\text{project\_code} \uparrow \text{Project}, \text{researcher\_id} \uparrow \text{Researcher}}, \text{weekly\_hours})$
6. $\text{Publication}(\underline{\text{doi}}, \text{title}, \text{year}, \text{journal})$
7. $\text{ProjectPublication}(\underline{\text{project\_code} \uparrow \text{Project}, \text{doi} \uparrow \text{Publication}})$
*(15 Points)*

---

### Solution to Part B

#### Question 3
$$
\pi_{\text{name}, \text{gpa}}\left( \sigma_{\text{major} = \text{'CS'} \land \text{grade} \ge 8.5 \land \text{dept} = \text{'CS'}}(\text{Student} \bowtie \text{Enrolled} \bowtie \text{Course}) \right)
$$
*(10 Points)*

#### Question 4
Using Relational Division:
Let $C_{\text{CS}} = \pi_{\text{cid}}(\sigma_{\text{dept} = \text{'CS'}}(\text{Course}))$.
Quotient: $Q = \pi_{\text{sid}, \text{cid}}(\text{Enrolled}) \div C_{\text{CS}}$.
Result:
$$
\pi_{\text{sid}, \text{name}}(\text{Student} \bowtie Q)
$$
*(10 Points)*

---

### Solution to Part C

#### Question 5
```sql
CREATE TABLE enrolled (
    sid INTEGER NOT NULL,
    cid VARCHAR(10) NOT NULL,
    grade NUMERIC(3, 1) NOT NULL CHECK (grade BETWEEN 0.0 AND 10.0),
    PRIMARY KEY (sid, cid),
    FOREIGN KEY (sid) REFERENCES student(sid) ON DELETE CASCADE,
    FOREIGN KEY (cid) REFERENCES course(cid) ON DELETE CASCADE
);
```
*(10 Points)*

#### Question 6
```sql
SELECT c.dept, c.cname, COUNT(e.sid) AS total_enrolled
FROM course c
JOIN enrolled e ON c.cid = e.cid
GROUP BY c.cid, c.dept, c.cname
HAVING COUNT(e.sid) > 3
ORDER BY total_enrolled DESC;
```
*(15 Points)*

---

### Solution to Part D

#### Question 7
1. **$B^+$ Calculation:**
   $B^{(0)} = \{ B \}$. Since $B \to D$, $B^{(1)} = \{ B, D \}$. No further FDs apply.
   $$B^+ = \{ B, D \}$$
   *(5 Points)*
2. **Candidate Keys:**
   - $A^+ = \{ A, B, C, D, E \} = R \implies A$ is a candidate key.
   - Since $E \to A$, $E^+ = \{ E, A, B, C, D \} = R \implies E$ is a candidate key.
   - Since $CD \to E$, $(CD)^+ \supseteq E^+ = R$.
     Can $C$ or $D$ be reduced? Since $B \to D$, $(BC)^+ \supseteq (CD)^+ = R$.
   - Candidate keys: $\{ A \}, \{ E \}, \{ CD \}, \{ BC \}$.
   *(8 Points)*
3. **Normal Form Analysis:**
   - Prime attributes: $\{ A, B, C, D, E \}$ (every attribute belongs to at least one candidate key).
   - In 2NF: No non-prime attribute exists, so partial dependencies on candidate keys cannot occur. 2NF is satisfied.
   - In 3NF: For every FD $X \to Y$, either $X$ is a superkey or every attribute in $Y$ is prime. Since all attributes in $R$ are prime, **3NF is satisfied**.
   - In BCNF: Consider $B \to D$. $B^+ = \{ B, D \} \neq R$, so $B$ is not a superkey. Therefore, **BCNF is violated**.
   - **Highest Normal Form: 3NF**.
   *(7 Points)*

