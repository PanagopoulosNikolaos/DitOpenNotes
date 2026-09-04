# Lecture 02: File Handling and Input/Output

## Context and Grounding
This lecture note establishes the concepts, functions, and error-handling patterns for persistent stream I/O in C. It provides the theoretical foundation for the 15 exercises implemented in `Exercises/File_Handling/src/`.

---

## 1. File Streams and Operating System Abstraction

In C, file interactions are abstracted through streams represented by `FILE*` control blocks defined in `<stdio.h>`. Streams maintain operational state including:
* Current position indicator
* Error indicators (`ferror`)
* End-of-file indicators (`feof`)
* Associated buffer memory

### 1.1 Stream Modes
| Mode | Action | Existing File | Stream Pointer Position |
|---|---|---|---|
| `"r"` | Read | Must exist | Beginning |
| `"w"` | Write | Overwritten / Created | Beginning |
| `"a"` | Append | Created if absent | End of file |
| `"rb"`, `"wb"`, `"ab"` | Binary variants | Explicitly bypass newline translation | Respective locations |
| `"r+"`, `"w+"`, `"a+"` | Update (Read + Write) | Governed by base mode | Respective locations |

---

## 2. Text vs. Binary Stream Processing

### 2.1 Text I/O Functions
Text streams format character sequences and translate newline markers across operating systems (`\n` vs `\r\n`).

* `fgetc(FILE *stream)` / `fputc(int c, FILE *stream)`: Character-by-character processing.
* `fgets(char *str, int n, FILE *stream)`: Safe line reading up to $n-1$ characters; retains newline.
* `fprintf(FILE *stream, const char *format, ...)`: Formatted text output.
* `fscanf(FILE *stream, const char *format, ...)`: Formatted parsing from text streams.

### 2.2 Binary I/O Functions
Binary streams transfer uninterpreted byte sequences directly between memory buffers and storage.

```c
size_t fread(void *ptr, size_t size, size_t count, FILE *stream);
size_t fwrite(const void *ptr, size_t size, size_t count, FILE *stream);
```

Both functions return the number of complete elements successfully transferred. If the returned count is less than `count`, inspect `feof(stream)` and `ferror(stream)` to diagnose the condition.

---

## 3. Direct Access and Stream Navigation

Arbitrary stream positioning enables database-like record access in binary files without scanning sequentially.

* `int fseek(FILE *stream, long offset, int whence)`: Repositions the file indicator.
  * `SEEK_SET`: Offset relative to file beginning.
  * `SEEK_CUR`: Offset relative to current position.
  * `SEEK_END`: Offset relative to end of file.
* `long ftell(FILE *stream)`: Returns current byte offset from start.
* `void rewind(FILE *stream)`: Sets file indicator to 0 and clears error flags.

### 3.1 Random-Access Record Pattern
```c
typedef struct {
    int id;
    char name[32];
    double gpa;
} StudentRecord;

/* Read record at index k */
int readRecord(FILE *fp, int k, StudentRecord *record) {
    if (fseek(fp, (long)(k * sizeof(StudentRecord)), SEEK_SET) != 0) {
        return 0; /* Seek error */
    }
    return fread(record, sizeof(StudentRecord), 1, fp) == 1;
}
```

---

## 4. Robust Error Handling and Resource Hygiene

Every file operation must verify stream validity:
1. Always test if `fopen()` returns `NULL`.
2. Do not use `while (!feof(fp))` as a loop condition because `feof` only sets after an attempted read fails past the end. Instead, check the return value of the read function (`fgets`, `fread`, `fscanf`).
3. Always close open descriptors with `fclose()`.

