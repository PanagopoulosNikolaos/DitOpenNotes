# Missing Contents — Database Notes

Gaps identified by comparing the note modules (`topic_1` through `topic_8_9`) against the official past exams and the synthetic practice exams. Each entry records the topic, its current status, why it matters, and the module where it belongs.

## Relational Algebra

### Division operator (÷)

- **Status:** Missing entirely — not covered in `topic_4` or `topic_8_9`.
- **Why it matters:** The "for all" queries in synthetic practice exams 3–8 require division (e.g., "passengers who have booked all flights departing ATH", "members who have borrowed all books by a publisher").
- **Target module:** `topic_4` (relational algebra section) or `topic_8_9`.
- **To add:** Formal definition, semantics, a worked example, and the equivalent SQL pattern.

## Database Architecture

### ANSI/SPARC three-schema architecture

- **Status:** Missing — `topic_1` only mentions "data independence" inside the DBMS-vs-file-system comparison table; there is no dedicated section on the three levels.
- **Why it matters:** Synthetic exam 2 (Question Δ) explicitly asks to compare the three-tier architecture with file-based systems.
- **Target module:** `topic_1`.
- **To add:** External / Conceptual / Internal levels and the mappings between them.

### Logical and physical data independence

- **Status:** Under-covered — only a passing row in `topic_1`'s comparison table, no explanation.
- **Why it matters:** The same synthetic exam 2 question requires explaining how the three-schema separation achieves each type of independence.
- **Target module:** `topic_1`.
- **To add:** Definitions of logical vs physical independence and which system change each one absorbs.

## E-R Model Refinements

### Participation constraints (total vs partial)

- **Status:** Under-covered — mentioned in one line in `topic_3` and one line in `topic_2`, but no dedicated section with notation.
- **Why it matters:** Every synthetic exam asks for "περιορισμός συμμετοχής (ολική/μερική)" with justification.
- **Target module:** `topic_3`.
- **To add:** Total vs partial participation, mandatory vs optional, single-line vs double-line ERD notation, and the effect on whether the mapped foreign key is `NOT NULL`.

### Relationship attributes (γνωρίσματα συσχέτισης)

- **Status:** Under-covered — shown only implicitly through N:M junction-table examples (`grade`, `enroll_date`); no dedicated section.
- **Why it matters:** Synthetic exams ask to identify relationship attributes (role name, salary, hours per week).
- **Target module:** `topic_3`.
- **To add:** Definition of relationship attributes, when they occur (mainly N:M and 1:N), and where they land in the relational schema.

### Multiple relationships between the same entity pair

- **Status:** Not covered — unary/binary/ternary degree is covered, but not two distinct relationships between the same two entities with role labels.
- **Why it matters:** Synthetic exam 3 (departure/arrival airports) and exam 8 (home/away teams) require role-labeled double relationships.
- **Target module:** `topic_3`.
- **To add:** Modeling two relationships between the same entity pair with distinct roles, and their mapping to two separate foreign keys.

## Relational Model Integrity

### ON DELETE / ON UPDATE referential actions

- **Status:** Under-covered — `topic_4` shows one passing example (`ON DELETE RESTRICT`, `ON UPDATE CASCADE`) but never explains the full set or when to choose each.
- **Why it matters:** Synthetic exams ask to justify `CASCADE` / `SET NULL` / `RESTRICT` for each foreign key.
- **Target module:** `topic_4`.
- **To add:** `CASCADE`, `SET NULL`, `RESTRICT` (plus `SET DEFAULT` / `NO ACTION`), with selection guidance per relationship type.

## Optional / Future

### Specialization / Generalization (ISA)

- **Status:** Not covered.
- **Why it matters:** Synthetic exam 6 hints at subtyping (media titles split into movies and series). Not explicitly requested by the papers, but useful for completeness.
- **Target module:** `topic_3`.
- **To add:** Supertype/subtype, total vs partial, and disjoint vs overlapping constraints.
