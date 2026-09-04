# Project 01: Relational Database System Design and Implementation

## Project Overview
Design, normalize, implement, and benchmark a complete production-grade relational database management system for a commercial logistics and supply chain enterprise. The project traverses the entire lifecycle: conceptual ER modeling, formal schema mapping, normalization to 3NF/BCNF, constraint enforcement, synthetic dataset generation, indexing optimization, and transaction workload execution.

---

## Technical Specifications and Architecture

### 1. Domain Scope: Global Logistics & Fleet Operations
The system manages:
- Warehouses across international jurisdictions with spatial and capacity constraints.
- Multi-modal transport fleet (trucks, cargo planes, ships) with maintenance schedules and driver assignments.
- Customer cargo consignments, tracking waybills, customs declarations, and delivery milestones.
- Real-time sensor telemetry logs (temperature, GPS coordinates, shock alarms) during transit.

### 2. Conceptual & Relational Design Requirements
- Formulate an Enhanced Entity-Relationship (EER) diagram including specialization/generalization hierarchies (e.g., Vehicle subtypes).
- Map to relational schema ensuring zero transitive or partial key dependencies (guaranteeing 3NF minimum; target BCNF).
- Enforce declarative referential integrity (`RESTRICT`, `CASCADE`), check constraints, and surrogate vs natural key selections.

### 3. Query Optimization and Indexing
- Profile query plans using `EXPLAIN QUERY PLAN` or `EXPLAIN ANALYZE`.
- Construct composite B-Tree indexes, partial indexes, and covering indexes to optimize high-frequency join queries and aggregations.
- Implement at least two transactional procedures ensuring ACID compliance under concurrent updates.

---

## Project Milestones

| Milestone | Deliverable | Technical Verification |
|---|---|---|
| **Phase 1** | Requirements & ER Diagram | Formal ER/EER diagram and business rule dictionary |
| **Phase 2** | Relational Schema & 3NF Normalization | Relational schema definition, dependency proof, DDL script |
| **Phase 3** | Dataset Ingestion & Complex Views | Synthetic data generator populating $\ge 10,000$ rows; analytics queries |
| **Phase 4** | Indexing & Concurrency Benchmarks | Query execution plan comparison (Before vs After indexing); final project report |

---

## Grading Rubric

| Criterion | Metric | Weight |
|---|---|---|
| **ER Modeling & Conceptual Correctness** | Accurate entity relationships, cardinalities, and inheritance constraints | 25% |
| **Normalization Rigor** | Formal proof of candidate keys and adherence to 3NF/BCNF without data loss | 25% |
| **SQL Implementation & Integrity** | DDL constraints, triggers, transaction blocks, and complex analytic queries | 25% |
| **Query Tuning & Performance Analysis** | Measurable optimization using query plans and proper index utilization | 15% |
| **Technical Report** | Architecture diagrams, verification logs, and reproducibility | 10% |

