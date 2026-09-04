# File Streams and Binary I/O Operations in C

## Overview
Standard C provides stream-based input/output abstractions through the `<stdio.h>` library, differentiating between character-oriented text streams and exact byte-level binary streams.

---

## 1. Stream Architecture and FILE Pointers

The `FILE` structure encapsulates operating system file descriptor handles, internal transfer buffers, current byte positions, and end-of-file/error flags:
```c
FILE *fp = fopen("records.db", "rb+");
if (fp == NULL) {
    perror("Failed to open binary records database");
    return 1;
}
```

Standard file modes:
* `"r"` / `"rb"`: Open existing file for reading.
* `"w"` / `"wb"`: Create new file or truncate existing file for writing.
* `"a"` / `"ab"`: Append to end of file.
* `"+"`: Extended read/write update mode (`"r+"`, `"w+"`, `"a+"`).

---

## 2. Block-Level Binary Operations

### 2.1 Reading and Writing Structures
Binary I/O preserves memory image bytes directly to disk using `fwrite` and `fread`:
```c
typedef struct {
    uint32_t id;
    char name[32];
    double balance;
} AccountRecord;

/* Writing a record */
AccountRecord rec = {101, "Alice", 2450.75};
size_t written = fwrite(&rec, sizeof(AccountRecord), 1, fp);
if (written != 1) {
    perror("Error writing record");
}

/* Reading a record */
AccountRecord read_rec;
size_t read_count = fread(&read_rec, sizeof(AccountRecord), 1, fp);
if (read_count != 1 && ferror(fp)) {
    perror("Error reading record");
}
```

---

## 3. Direct File Positioning (`fseek`, `ftell`, `rewind`)

Binary records can be accessed with $O(1)$ random access:
```c
/* Seek to the k-th record (0-indexed) */
long record_offset = (long)(k * sizeof(AccountRecord));
fseek(fp, record_offset, SEEK_SET);

/* Obtain current stream position */
long current_pos = ftell(fp);

/* Return stream to beginning */
rewind(fp);
```

Position origins:
* `SEEK_SET`: Relative to beginning of file.
* `SEEK_CUR`: Relative to current file pointer offset.
* `SEEK_END`: Relative to end of file.

