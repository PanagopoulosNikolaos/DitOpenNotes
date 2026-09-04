# Lecture 03: Structures, Unions, and File Stream I/O

## Context and Grounding
This lecture explores structured data aggregation and external persistence in C. It examines the internal memory alignment of composite structures (`struct`), shared-memory unions (`union`), and file system streams managed via standard C library stream buffers (`FILE *`).

---

## 1. Structures and Composite Types

A structure groups logically associated variables of diverse types into a single contiguous entity.

### 1.1 Declaration and Instantiation
```c
typedef struct {
    int student_id;
    char full_name[64];
    double grade_average;
} StudentRecord;
```

### 1.2 Structure Memory Alignment and Padding
Compilers insert padding bytes between fields to align members with word boundaries (typically 4 or 8 bytes on x86_64 architectures):
```c
struct Misaligned {
    char flag;      // 1 byte + 3 bytes padding
    int counter;    // 4 bytes
    char code;      // 1 byte + 7 bytes padding
    double score;   // 8 bytes
}; // Total size: 24 bytes (instead of 14 raw bytes)
```
* Best Practice: Declare members in order of descending byte size to minimize padding overhead.

### 1.3 Arrow Operator (`->`)
When accessing structure members via a pointer, the arrow operator (`ptr->member`) is syntactic sugar for dereferencing followed by member selection (`(*ptr).member`):
```c
StudentRecord record = {101, "Alexandros", 8.75};
StudentRecord *ptr = &record;

printf("ID: %d\n", ptr->student_id);
```

---

## 2. Unions

A union allocates storage such that all declared members occupy the identical memory location. The total size of a union corresponds to the size of its largest constituent member:

```c
typedef union {
    int int_val;
    float float_val;
    char raw_bytes[4];
} DataPacket;
```
* Modifying one union member overwrites the shared memory area used by other members.

---

## 3. File Stream I/O Operations

The C standard I/O library operates through abstract streams represented by the opaque `FILE` handle defined in `<stdio.h>`.

### 3.1 Stream Opening Modes
| Mode | Semantics | Existing File Behavior |
|:---|:---|:---|
| `"r"` | Open for reading text | File must exist; returns `NULL` if missing. |
| `"w"` | Open for writing text | Truncates existing file or creates new file. |
| `"a"` | Open for appending text | Preserves existing data, writes to end of file. |
| `"rb"` | Open for reading binary | Reads raw bytes without newline translation. |
| `"wb"` | Open for writing binary | Overwrites raw binary data. |

### 3.2 Formatted File I/O
```c
/**
 * Writes an array of student records to a formatted text file.
 *
 * Args:
 *   filename (const char *): Path to the target output file.
 *   records (const StudentRecord *): Contiguous buffer of student records.
 *   count (size_t): Number of records to serialize.
 *
 * Returns:
 *   int: 0 on success, -1 on stream open error.
 */
int writeStudentReport(const char *filename, const StudentRecord *records, size_t count) {
    if (filename == NULL || records == NULL) {
        return -1;
    }

    FILE *file_ptr = fopen(filename, "w");
    if (file_ptr == NULL) {
        perror("Failed to open file for writing");
        return -1;
    }

    for (size_t i = 0; i < count; ++i) {
        fprintf(file_ptr, "%d,%s,%.2f\n", 
                records[i].student_id, 
                records[i].full_name, 
                records[i].grade_average);
    }

    fclose(file_ptr);
    return 0;
}
```

### 3.3 Direct Block (Binary) I/O
Binary I/O transfers memory blocks directly to and from secondary storage without string parsing:
* `size_t fread(void *ptr, size_t size, size_t nmemb, FILE *stream)`: Reads up to `nmemb` elements of size `size`.
* `size_t fwrite(const void *ptr, size_t size, size_t nmemb, FILE *stream)`: Writes `nmemb` elements.

```c
// Serializing structure array directly to disk
FILE *bin_out = fopen("students.bin", "wb");
if (bin_out != NULL) {
    fwrite(records, sizeof(StudentRecord), count, bin_out);
    fclose(bin_out);
}
```

---

## 4. Error Checking and Stream State
* `feof(file_ptr)`: Returns non-zero only after an attempt to read past the end of the file. Do not use as the loop condition for reading!
* `ferror(file_ptr)`: Indicates whether an unrecoverable hardware or permissions I/O error occurred on the stream.
* Always close opened streams using `fclose` to flush write buffers and release file descriptor handles.

