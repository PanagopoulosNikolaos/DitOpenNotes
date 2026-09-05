# Year 2 - Semester 4

Welcome to the comprehensive academic course archive for **Year 2, Semester 4** of the Department of Informatics and Telecommunications at the University of Ioannina.

---

## Curriculum Overview

Semester 4 deepens core computing competencies across programming language foundations, operating system kernels and systems programming, telecommunication network architectures, relational database management systems, and probabilistic statistical modeling.

| Code | Course Name | ECTS | Category | Primary Focus |
|:---|:---|:---:|:---|:---|
| **401** | [Principles of Programming Languages](PROGRAMMING_LANGUAGES_PRINCIPLES) | 6 | Mandatory | Language paradigms (pure functional Haskell, declarative logic Prolog, multi-paradigm Python), formal BNF/EBNF grammars, static/dynamic typing, lexical vs. dynamic scoping, parameter passing modes, runtime stack activation records, and garbage collection |
| **402** | [Operating Systems](OPERATING_SYSTEMS) | 6 | Mandatory | Kernel architectures, process lifecycles and context switching, CPU scheduling algorithms, concurrency primitives (semaphores, mutexes), deadlock prevention/avoidance, virtual memory management, paging, page replacement, POSIX IPC, and UNIX shell scripting |
| **403** | [Computer Networks](COMPUTER_NETWORKS) | 6 | Mandatory | Layered architectures (OSI & TCP/IP), network edge vs. core, packet switching vs. circuit switching, nodal delay modeling, CIDR addressing, IP subnetting, routing protocols (RIP, OSPF, BGP), reliable transport protocols (TCP flow/congestion control, UDP), and socket programming |
| **404** | [Databases](DATABASES) | 6 | Mandatory | Conceptual data modeling, Entity-Relationship (ER) diagrams with Crow's Foot notation, 7-step mapping algorithm to relational schemas, relational algebra operators, SQL DDL/DML, functional dependencies, normalization (1NF through BCNF), and ACID transaction management |
| **405** | [Probability and Statistics](PROBABILITY_STATISTICS) | 6 | Mandatory | Axiomatic probability theory, conditional probability, Bayes' Theorem, discrete (Binomial, Poisson) and continuous (Normal, Exponential) distributions, Central Limit Theorem, point/interval estimation, hypothesis testing, and statistical computing in R |

---

## Standard Course Directory Structure

Each course directory adheres strictly to the department's standardized academic curriculum organization:

```text
Course_Directory/
├── README.md               # Course syllabus, prerequisites, outcomes, and directory index
├── Lectures/               # Structured theory lecture modules and slide notes
├── Exercises/              # Comprehensive problem sets and step-by-step solved drills
├── Examples/               # Executable code, simulation models, and interactive demonstrations
├── Assignments/            # Practical laboratory project assignments and rubrics
├── Tutorials/              # Hands-on tooling guides (GHCi, SWI-Prolog, GCC, SQLite, Wireshark, R)
├── Projects/               # Comprehensive capstone term design projects
├── Exams/                  # Past examination papers, model practice exams, and rubrics
│   ├── Papers/             # Transcribed exam papers with worked solutions
│   └── images/             # Original scanned test papers and reference figures
└── Resources/              # Study notes, textbooks, curriculum mindmaps, and web applications
    ├── Meta/               # Curriculum topic mindmaps and instructions
    ├── Notes/              # Granular chapter study notes and comprehensive guides
    ├── app/                # Interactive web applications for visual exploration
    └── resources.md        # Curated bibliography, official standards, and external links
```

---

## Getting Started

1. **Tooling Environment**:
   * **Principles of Programming Languages**: Glasgow Haskell Compiler (`ghc` / `runghc`), SWI-Prolog interpreter (`swipl`), and Python 3.10+ runtime with JupyterLab.
   * **Operating Systems**: Modern C compiler (`gcc` or `clang`) supporting POSIX.1-2008 standards, GNU Debugger (`gdb`), GNU Make, Valgrind (`valgrind`), and standard GNU Bash.
   * **Computer Networks**: Python 3 socket networking modules, Wireshark packet dissector (`wireshark` / `tshark`), and Cisco Packet Tracer for network topology modeling.
   * **Databases**: SQLite 3 command-line interface (`sqlite3`), PostgreSQL client/server tooling, and NiceGUI for interactive relational modeling.
   * **Probability and Statistics**: R runtime environment (`R` / `Rscript`), RStudio, and Python 3 with scientific libraries (NumPy, SciPy, Matplotlib).
2. **Recommended Study Order**: Begin each subject by mastering core theoretical concepts in `Lectures/` and `Resources/Notes/`, then execute and experiment with code in `Examples/`, followed by practicing numerical problem sets in `Exercises/`.
3. **Assessment Preparation**: Complete laboratory and coursework deliverables in `Assignments/` and self-evaluate exam readiness using the comprehensive practice exams and past papers in `Exams/`.