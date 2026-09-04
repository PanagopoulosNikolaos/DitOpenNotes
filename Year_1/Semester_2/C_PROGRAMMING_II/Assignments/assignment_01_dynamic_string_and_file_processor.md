# Assignment 01: Dynamic String Buffer and Log File Processor

## Objective
Design and implement a robust command-line text and log processing utility in C. This assignment evaluates proficiency in dynamic memory allocation (`malloc`, `realloc`, `free`), file I/O operations (`fopen`, `fgets`, `fprintf`), error validation, and memory leak elimination.

---

## Technical Specifications

### 1. Dynamic Line Buffer (`StringBuffer`)
Define an expandable string buffer structure:
```c
typedef struct {
    char *data;
    size_t length;
    size_t capacity;
} StringBuffer;
```
* Initial capacity: 16 bytes.
* Function `stringBufferInit(StringBuffer *sb)`: Allocates initial heap memory.
* Function `stringBufferAppend(StringBuffer *sb, const char *str)`: Appends characters, doubling capacity whenever `length + strlen(str) >= capacity`.
* Function `stringBufferFree(StringBuffer *sb)`: Releases allocated memory and resets pointers.

### 2. Log File Aggregator
The utility must accept input via CLI flags:
```bash
./logproc --input access.log --output report.txt --filter ERROR
```

The processor must:
1. Open the target log file specified by `--input`.
2. Read the file line-by-line using dynamically expanding buffers (handling lines of arbitrary length).
3. Filter lines matching the case-sensitive string supplied in `--filter`.
4. Output all matching lines along with computed summary statistics (total lines read, total matching lines, longest line length) to the file specified by `--output`.

### 3. Deliverables and Constraints
* Source files: `logproc.c`, `string_buffer.c`, `string_buffer.h`, and `Makefile`.
* Compilation flags: `-Wall -Wextra -Werror -std=c11 -pedantic`.
* Zero memory leaks when evaluated under `valgrind --leak-check=full`.
* Robust handling of non-existent input files, write-protected output destinations, and malformed command arguments.

---

## Evaluation Rubric
| Criterion | Description | Points |
|---|---|---|
| Dynamic Buffer Implementation | Correct geometric capacity expansion and zero buffer overflow | 25 |
| File Processing & Filtering | Accurate file stream handling, line tokenization, and output generation | 25 |
| Memory Management | Zero memory leaks or invalid reads under Valgrind | 25 |
| Error Handling & CLI Arguments | Comprehensive checks for arguments, file errors, and invalid inputs | 15 |
| Code Quality & Documentation | Google-style docstrings, modular code organization, Makefile | 10 |
| **Total** | | **100** |

