# Project 01: High-Performance Binary Record Management System

## Project Overview
Design, architect, and implement a modular, high-performance database management system in standard C for indexed binary student records. The system utilizes dynamic hash indexing in memory with binary record persistence on disk, supporting atomic transactions, sorted queries, and memory-leak-free lifecycle management.

---

## 1. Functional Requirements

### 1.1 Record Specification
```c
typedef struct {
    uint32_t student_id;
    char first_name[32];
    char last_name[32];
    char department[16];
    float gpa;
    uint32_t enrollment_year;
} StudentRecord;
```

### 1.2 Core Operations
1. **Record Insertion**:
   * Appends records to the binary file (`data/students.db`).
   * Updates an in-memory hash table index mapping `student_id` to file offset.
   * Rejects duplicate `student_id` entries.
2. **Key Search (`O(1)` in memory)**:
   * Looks up the file offset in the hash table index.
   * Seeks directly to the disk location using `fseek()` and reads the single record.
3. **Record Update**:
   * Updates GPA, department, or names in-place without rebuilding the database file.
4. **Record Deletion (Tombstone Pattern)**:
   * Marks records as inactive using a flag or tombstone value, then purges them during compaction.
5. **Database Compaction**:
   * Re-writes the database file to remove deleted records and defragment disk space.
6. **Sorted Export**:
   * Exports active student records sorted by GPA or last name into a CSV or formatted text report.

---

## 2. Architecture and Modularity

The project must be organized into distinct modules:
* `src/main.c`: Command-line interface and repl prompt.
* `src/storage.c` / `include/storage.h`: Binary file handling, seeking, byte-level reading/writing.
* `src/index.c` / `include/index.h`: In-memory hash table index implementation.
* `src/util.c` / `include/util.h`: Input validation, string sanitization, formatted display.
* `Makefile`: Targets for `all`, `debug`, `test`, `clean`, and `valgrind`.

---

## 3. Implementation Milestones

### Milestone 1: Storage Engine
* Implement `storageOpen()`, `storageAppend()`, `storageReadAt()`, and `storageClose()`.
* Unit test with 10,000 synthetic records.

### Milestone 2: Hash Index Engine
* Implement dynamic hash table with separate chaining or open addressing.
* Benchmark index lookup times against linear file scanning.

### Milestone 3: Interactive CLI & Report Generation
* Implement robust REPL supporting `INSERT`, `FIND <id>`, `UPDATE <id>`, `DELETE <id>`, `COMPACT`, and `REPORT`.

---

## 4. Evaluation and Grading Rubric
| Component | Criteria | Points |
|---|---|---|
| Architecture & Clean Modularization | Header separation, information hiding, Makefile build | 20 |
| Correct Binary Storage Mechanics | Reliable persistence, proper random-access seeks, byte alignment | 25 |
| Hash Index Efficiency | Correct constant-time lookup, dynamic bucket resizing | 20 |
| Memory Safety & Leak Prevention | Zero Valgrind warnings or memory leaks across stress test workloads | 20 |
| Error Resilience | Graceful handling of corrupted files, interrupted writes, invalid input | 15 |
| **Total** | | **100** |

