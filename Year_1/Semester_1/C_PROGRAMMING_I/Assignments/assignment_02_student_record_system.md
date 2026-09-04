# Assignment 02: Student Record Management System

## Objective
Implement an in-memory and file-persistent student database management utility in C. This assignment evaluates competency in structured data types (`struct`), pointer manipulation, formatted file I/O, linear search algorithms, and bubble/selection sorting.

---

## Technical Specifications

### 1. Data Schema
Define the student entity structure:
```c
#define MAX_NAME_LEN 64
#define MAX_STUDENTS 100

typedef struct {
    int student_id;
    char first_name[MAX_NAME_LEN];
    char last_name[MAX_NAME_LEN];
    double gpa;
    int semester;
} StudentRecord;

typedef struct {
    StudentRecord records[MAX_STUDENTS];
    size_t count;
} Database;
```

### 2. Functional Requirements
Provide an interactive text-based console menu supporting the following commands:
1. **Add Student**: Prompts for ID, first name, last name, GPA ($0.00 \le \text{GPA} \le 10.00$), and semester ($1 \le \text{sem} \le 8$). Validates uniqueness of ID.
2. **Search by ID**: Performs linear lookup matching target ID and displays record details.
3. **Sort Records by GPA**: Sorts stored records in descending order of GPA using in-place array sorting.
4. **Export to CSV**: Formats database into comma-separated values (`id,first_name,last_name,gpa,semester\n`) and saves to disk.
5. **Import from CSV**: Parses formatted CSV file into the database structure, rejecting malformed lines.
6. **Summary Statistics**: Computes database-wide average GPA, highest performing student, and grade distribution.

### 3. Constraints & Technical Criteria
* Strict modularity: `main.c`, `student_db.c`, `student_db.h`, `Makefile`.
* Compilation flags: `-Wall -Wextra -Werror -std=c11 -pedantic`.
* Defend against buffer overflows when reading user strings via `fgets` and strip trailing newlines safely.
* Zero memory corruption or dangling pointer references.

---

## Evaluation Rubric

| Criterion | Description | Points |
|:---|:---|:---:|
| Core CRUD Operations | Accurate addition, search, update, and deletion within bounds | 30 |
| File Persistence (CSV I/O) | Robust import and export parsing with error validation | 25 |
| Sorting & Analytics | Correct sorting algorithm and accurate statistical computations | 20 |
| Defensive Programming | Sanitizes user inputs, handles full array bounds and duplicate IDs | 15 |
| Documentation & Style | Strict adherence to Google docstrings, clean Make targets | 10 |
| **Total** | | **100** |

