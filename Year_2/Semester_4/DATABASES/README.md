# Database Systems

## Course Overview
This course provides a rigorous, in-depth study of relational database design, formal data models, relational algebra, Structured Query Language (SQL), and database management system (DBMS) internals. Topics include requirements analysis, conceptual modeling via Entity-Relationship (ER) diagrams with Crow's Foot notation, the formal 7-step mapping algorithm from ER diagrams to relational schemas, formal relational algebra (selection, projection, joins, set operations, division), SQL Data Definition Language (DDL) and Data Manipulation Language (DML), functional dependencies, closure calculation, normalization (1NF, 2NF, 3NF, BCNF), and transaction management (ACID properties, serializability, concurrency control).

## Course Code
404 (DATABASES)

## Prerequisites
* Data Structures and Algorithms (Code: 305)
* Discrete Mathematics (Code: 202)

---

## Topics Covered
* **Conceptual Modeling & ER Diagrams**: Entities (strong vs. weak), attributes (simple, composite, multi-valued, derived), primary keys, partial keys, relationship types, structural constraints (cardinality ratios 1:1, 1:N, M:N, participation total vs. partial), and Crow's Foot graphical notation.
* **ER to Relational Schema Mapping**: The formal 7-step algorithm: mapping regular entities, weak entities (foreign key inheritance), 1:1 relationships (foreign key vs. merged relation), 1:N relationships, M:N relationships (junction tables), multi-valued attributes (separate tables), and $N$-ary relationships.
* **Formal Relational Algebra**: Unary operators (Selection $\sigma$, Projection $\pi$, Renaming $\rho$), set operations (Union $\cup$, Intersection $\cap$, Set Difference $-$, Cartesian Product $\times$), binary joins (Theta Join $\bowtie_\theta$, Equi-Join, Natural Join $\ast$, Outer Joins $\leftouterjoin$, $\rightouterjoin$, $\fullouterjoin$), and Relational Division ($\div$).
* **SQL Language (DDL & DQL/DML)**: Table creation, primary/foreign key constraints (`ON DELETE CASCADE`, `ON DELETE SET NULL`), check constraints, complex multi-table queries, aggregation functions (`COUNT`, `SUM`, `AVG`, `MAX`, `MIN`), `GROUP BY`, `HAVING`, correlated subqueries, `EXISTS`/`NOT EXISTS`, and SQL views.
* **Functional Dependencies & Normalization**: Armstrong's Axioms (reflexivity, augmentation, transitivity), attribute closure computation ($X^+$), canonical covers, candidate key determination, First Normal Form (1NF), Second Normal Form (2NF - full functional dependency), Third Normal Form (3NF - transitive dependency elimination), and Boyce-Codd Normal Form (BCNF - superkey condition).
* **Transactions & Concurrency**: ACID properties (Atomicity, Consistency, Isolation, Durability), transaction states, conflict serializability, precedence graphs, Two-Phase Locking (2PL), and deadlock detection in DBMS.

---

## Learning Objectives
* Translate complex business requirements into normalized Entity-Relationship diagrams using standard Crow's Foot conventions.
* Apply the deterministic 7-step mapping algorithm to synthesize relational schemas that preserve referential integrity.
* Formulate expressive query expressions using formal relational algebra operators.
* Construct production-grade SQL DDL schemas and optimize analytical queries utilizing indexes, subqueries, and joins.
* Evaluate schema health by computing functional dependency closures and decomposing relations into 3NF and BCNF without losing dependencies or data.

---

## Directory Structure

| Directory | Description |
|:---|:---|
| [`Lectures/`](Lectures/) | Structured theory lecture modules and departmental presentation slide PDFs |
| [`Exercises/`](Exercises/) | Solved numerical drills on relational algebra, candidate key discovery, and BCNF decomposition |
| [`Examples/`](Examples/) | Executable SQL schema creation, data seeding, analytical queries, and walkthrough guides |
| [`Assignments/`](Assignments/) | Practical coursework projects covering ER domain modeling and SQL query optimization |
| [`Tutorials/`](Tutorials/) | Hands-on guides for SQLite command-line setup and advanced join optimization |
| [`Projects/`](Projects/) | Capstone design specification for an end-to-end enterprise relational database system |
| [`Exams/`](Exams/) | Past university examination papers, topic-focused practice drills, and realistic mock exams |
| [`Resources/`](Resources/) | Complete exam theory guides, topic study notes, mindmaps, and interactive web application |

---

## Tooling and Simulation Environment

### SQLite 3 In-Memory and File-Based Execution
To execute relational database scripts via the SQLite 3 CLI:
```bash
sqlite3 :memory: < Examples/examples_sql_schema_and_queries.sql
```

To run interactive queries against a persistent database:
```bash
sqlite3 university.db
.read Examples/examples_sql_schema_and_queries.sql
.mode column
.headers on
SELECT * FROM COURSES;
```

### Interactive ER Modeling Web Application
To launch the interactive ER modeling and scenario analysis tool:
```bash
cd Resources/app
python3 -m pip install -r requirements.txt
python3 main.py
```