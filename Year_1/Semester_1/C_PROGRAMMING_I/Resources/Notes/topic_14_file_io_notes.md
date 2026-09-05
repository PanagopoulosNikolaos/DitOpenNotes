# Topic 14: File I/O

## 1. Files and FILE Streams

C accesses files through the `<stdio.h>` library using a `FILE *` handle — a *stream* that abstracts reading and writing. Opening a file returns the handle; everything afterwards works through it:

```c
FILE *fp = fopen("data.txt", "r");
if (fp == NULL) {                     // fopen returns NULL on failure
    perror("fopen");                  // Prints why (e.g. No such file or directory)
    return 1;
}
/* ... use the file ... */
fclose(fp);                           // Always close: flushes buffers, releases resources
```

**Always check `fopen`'s result.** A NULL handle dereferenced is a crash.

---

## 2. Opening Modes

| Mode | Meaning | If File Exists | If File Missing |
|------|---------|----------------|-----------------|
| `"r"` | Read only | Opened at start | `fopen` fails |
| `"w"` | Write only | **Truncated to zero!** | Created |
| `"a"` | Append | Writes go to end | Created |
| `"r+"` | Read and write | Opened at start | `fopen` fails |
| `"w+"` | Read and write | Truncated | Created |
| `"a+"` | Read and append | Appends | Created |

Add `b` for binary files (`"rb"`, `"wb"`, ...) — on Linux it makes no difference, on Windows it prevents text-mode translation of `\n`.

---

## 3. Writing Text

```c
FILE *fp = fopen("scores.txt", "w");
if (!fp) { perror("fopen"); return 1; }

fprintf(fp, "Alice %d\n", 95);       // printf into a file
fputs("Plain text line\n", fp);      // No formatting, no auto newline
fputc('X', fp);                      // One character

fclose(fp);
```

---

## 4. Reading Text

```c
// Line by line (the standard safe pattern)
char line[256];
FILE *fp = fopen("scores.txt", "r");
if (!fp) { perror("fopen"); return 1; }

while (fgets(line, sizeof line, fp) != NULL) {   // NULL = end or error
    line[strcspn(line, "\n")] = '\0';            // Trim trailing newline
    printf("Read: %s\n", line);
}
fclose(fp);
```

```c
// Field by field (mixing scanf-like parsing)
int score; char name[50];
while (fscanf(fp, "%49s %d", name, &score) == 2) {   // Check item count!
    printf("%s scored %d\n", name, score);
}
```

Prefer `fgets` + `sscanf` for robust parsing: read a whole line, then parse it in memory. A failed `fscanf` mid-format can leave the stream position unpredictable.

---

## 5. Binary I/O: fread / fwrite

Binary mode moves raw bytes — compact and fast, but not human-readable and platform-dependent in layout:

```c
typedef struct { int id; double gpa; } Student;

// Write an array of records
FILE *out = fopen("students.bin", "wb");
Student list[3] = {{1, 3.5}, {2, 3.9}, {3, 2.8}};
fwrite(list, sizeof(Student), 3, out);       // (buffer, element size, count, stream)
fclose(out);

// Read them back
FILE *in = fopen("students.bin", "rb");
Student loaded[3];
size_t got = fread(loaded, sizeof(Student), 3, in);
printf("Read %zu records\n", got);
fclose(in);
```

Never read raw structs written on a different machine (endianness, padding may differ).

---

## 6. Detecting End of File and Errors

```c
int c;
while ((c = fgetc(fp)) != EOF) { ... }       // EOF from fgetc/fscanf/fgets

if (feof(fp))  { /* clean end of file */ }
if (ferror(fp)){ /* an actual read/write error */ }
```

`EOF` is only an *indicator* — after a read fails, call `feof`/`ferror` to learn whether it was a normal end or an error.

---

## 7. Common Pitfalls

| Pitfall | Fix |
|---------|-----|
| `"w"` mode destroying an existing file | Use `"r+"`/`"a"` when the file must survive |
| Not checking `fopen` | Always `if (!fp) { perror(...); }` |
| `fgets` keeps `'\n'` | Trim with `strcspn` |
| Using `scanf`-style parsing on untrusted data | Read lines with `fgets`, parse with `sscanf` |
| Writing structs with pointers inside | Pointers are meaningless on disk — serialize fields individually |
| Forgetting `fclose` | Data can stay unflushed; file handles leak |

---

## 8. Summary

* Files are accessed via `FILE *` handles with explicit modes (`r`, `w`, `a`, `+`, `b`).
* Text I/O: `fprintf`, `fputs`, `fgets`, `fscanf` — check return values everywhere.
* Binary I/O: `fread`/`fwrite` move whole records at native byte layout.
* Distinguish EOF from errors with `feof`/`ferror`, and always `fclose`.
