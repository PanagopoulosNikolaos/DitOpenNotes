# Project 01: Job Shop Scheduling Problem (JSSP) Simulator

## Project Overview
Design and implement an object-oriented simulation engine in modern C++ to solve the Job Shop Scheduling Problem (JSSP). This project bridges core object-oriented principles (polymorphic dispatch, RAII, design patterns) with combinatorial optimization.

---

## Technical Domain Specification

In the Job Shop Scheduling Problem:
- A set of $n$ jobs $\mathcal{J} = \{J_1, J_2, \dots, J_n\}$ must be processed across $m$ distinct machines $\mathcal{M} = \{M_1, M_2, \dots, M_m\}$.
- Each job $J_i$ consists of an ordered sequence of operations $O_{i, 1}, O_{i, 2}, \dots, O_{i, k}$.
- Each operation specifies a dedicated target machine and a processing duration $p_{i, j} > 0$.
- **Constraints:**
  1. Each machine can process at most one operation at any point in time (No preemption).
  2. The operations of a given job must execute sequentially in prescribed technological order.
- **Objective:** Minimize the **Makespan** $C_{\max} = \max_{i} C_i$, where $C_i$ is the completion time of job $i$.

---

## Object-Oriented Architecture

```
                       +-------------------+
                       |    IScheduler     | <--- Abstract Strategy Interface
                       +-------------------+
                                 ^
         +-----------------------+-----------------------+
         |                       |                       |
+-----------------+     +-----------------+     +-----------------+
|  FIFOScheduler  |     |   SPTScheduler  |     | GeneticScheduler|
+-----------------+     +-----------------+     +-----------------+

         * Has-A
+--------------------+ 1      * +--------------------+ 1      * +--------------------+
|     JobShop        | -------- |       Job          | -------- |     Operation      |
+--------------------+          +--------------------+          +--------------------+
         | 1
         | *
+--------------------+
|      Machine       |
+--------------------+
```

### Core Design Requirements
1. **Encapsulation & Immutability:** `Operation` and `Job` attributes must be strictly encapsulated with const-correct accessors.
2. **Strategy Pattern:** Decouple schedule generation algorithms behind a polymorphic `IScheduler` interface. Implement at least two distinct dispatching heuristics:
   - **FIFO (First-In, First-Out):** Prioritizes operations based on job arrival or sequence index.
   - **SPT (Shortest Processing Time):** Prioritizes operations with minimal duration $p_{i, j}$.
3. **Observer Pattern / Telemetry:** Implement an event observer that listens for operation dispatch, machine idle transitions, and makespan completion events to generate Gantt chart outputs.
4. **Memory Safety:** Manage all polymorphic schedules and simulation components using `std::unique_ptr` and `std::shared_ptr` with zero memory leaks.

---

## Project Milestones

| Milestone | Target Objective | Deliverables |
|---|---|---|
| **Phase 1** | Domain Model & Parser | Input file parser (reading standard Taillard / OR-Library JSSP benchmark formats) and basic entity classes |
| **Phase 2** | Event-Driven Simulation Engine | Machine state queue tracking and non-preemptive operation scheduling logic |
| **Phase 3** | Heuristic Strategy Implementations | Polymorphic `FIFOScheduler` and `SPTScheduler` implementations |
| **Phase 4** | Gantt Chart Generation & Analysis | ASCII or SVG Gantt chart generator, makespan comparison report, and clean Valgrind memory log |

---

## Grading Rubric

| Assessment Criteria | Description | Weight |
|---|---|---|
| **OOP Design & Patterns** | Effective use of Strategy, Factory, and Observer patterns with clean class hierarchies | 30% |
| **Simulation Correctness** | Accurate enforcement of machine precedence and job sequencing constraints | 30% |
| **Memory Management & RAII** | Zero leaks in Valgrind, proper use of smart pointers and Rule of Five | 20% |
| **Performance & Benchmarking** | Execution efficiency on large benchmark instances (e.g., Taillard 20x20 instances) | 20% |

