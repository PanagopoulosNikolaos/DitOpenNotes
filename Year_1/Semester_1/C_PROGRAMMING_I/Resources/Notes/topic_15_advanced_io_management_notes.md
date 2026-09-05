# Topic 15: Advanced I/O Management (Buffering, Seeking, Redirection)

## 1. How Streams Are Buffered

Every stdio stream is backed by a buffer. Instead of hitting the disk (or terminal) on every character, the library batches data:

| Buffering Mode | Applies To | Behavior |
|----------------|-----------|----------|
| **Full buffering** | Files on disk | Data flushes only when the buffer fills |
| **Line buffering** | Interactive terminals | Buffer flushes on every `'\n'` |
| **Unbuffered** | `stderr` | Every write goes out immediately |

Consequences every C programmer eventually hits:

* **Debug prints disappear:** output to a redirected/piped `stdout` is fully buffered, so `printf` messages may not appear before a crash. Force a flush:
  ```c
  printf("checkpoint 1\n");
  fflush(stdout);          // Push buffered data out now
  ```
* **Interleaving:** mixing `printf` (buffered) and `fprintf(stderr, ...)` (unbuffered) can produce out-of-order output — flush `stdout` before writing diagnostics.
* **Losing data:** calling `exit`/returning from `main` flushes streams, but `_exit` or a crash does not.

### setvbuf — Controlling the Buffer

```c
char mybuf[8192];
setvbuf(fp, mybuf, _IOFBF, sizeof mybuf);   // _IOFBF full, _IOLBF line, _IONBF none
setvbuf(stdout, NULL, _IONBF, 0);           // Make stdout unbuffered
```

Must be called **before any other operation** on the stream.

---

## 2. Random Access: fseek, ftell, rewind

Streams are normally sequential, but every open stream has a **file position indicator** that can be moved:

```c
long pos = ftell(fp);          // Current byte offset from the start

fseek(fp, 0L, SEEK_SET);       // Jump to the beginning
fseek(fp, 0L, SEEK_END);       // Jump to the end
fseek(fp, -10L, SEEK_CUR);     // 10 bytes back from the current position
rewind(fp);                    // Equivalent to fseek(fp, 0, SEEK_SET)

fseek(fp, offset, origin);     // origin: SEEK_SET | SEEK_CUR | SEEK_END
```

**Classic pattern — measure a file's size:**

```c
fseek(fp, 0L, SEEK_END);
long size = ftell(fp);
rewind(fp);
```

**Classic pattern — read the last record of a fixed-size binary file:**

```c
typedef struct { int id; double value; } Rec;

FILE *fp = fopen("data.bin", "rb");
fseek(fp, -(long)sizeof(Rec), SEEK_END);   // One record before the end
Rec last;
fread(&last, sizeof(Rec), 1, fp);
```

For portable large files use `fgetpos`/`fsetpos` or `off_t` with `_FILE_OFFSET_BITS=64`; `ftell`/`fseek` use `long`, which may be 4 bytes on some platforms.

---

## 3. stdin/stdout/stderr and Redirection

The three standard streams can be redirected by the shell — the program itself needs no changes:

```bash
./app < input.txt          # stdin comes from a file
./app > output.txt         # stdout goes to a file
./app 2> errors.log        # stderr goes to a file
./app > all.txt 2>&1       # Both into one file
./app | grep ERROR         # stdout piped to another program
```

Inside the program:

```c
fprintf(stderr, "Error: cannot open %s\n", path);   // Diagnostics → stderr
fprintf(stdout, "Result: %d\n", value);             // Data → stdout
```

Convention: **data on stdout, diagnostics on stderr.** That is what keeps pipelines composable.

`freopen` can even rewire a stream within the program:

```c
freopen("log.txt", "w", stdout);   // printf now writes to log.txt
```

---

## 4. Robust Line and Token Input Management

Building reliable input handling from the standard pieces:

```c
// Read a whole line of unknown length
char *readLine(FILE *in) {
    size_t cap = 64, len = 0;
    char *buf = malloc(cap);
    if (!buf) return NULL;
    int c;
    while ((c = fgetc(in)) != EOF && c != '\n') {
        if (len + 2 > cap) {                       // Grow geometrically
            cap *= 2;
            char *tmp = realloc(buf, cap);
            if (!tmp) { free(buf); return NULL; }
            buf = tmp;
        }
        buf[len++] = (char)c;
    }
    if (c == EOF && len == 0) { free(buf); return NULL; }  // Clean EOF
    buf[len] = '\0';
    return buf;
}
```

```c
// Bounded token scan from a line (avoid scanf overflow)
char cmd[16];
sscanf(line, "%15s", cmd);     // Field width = buffer size - 1
```

---

## 5. Error Handling and Cleanup Discipline

```c
FILE *fp = fopen("data.txt", "r");
if (!fp) { perror("data.txt"); return EXIT_FAILURE; }

if (ferror(fp)) {
    perror("read failed");
    fclose(fp);
    return EXIT_FAILURE;
}
fclose(fp);
```

Larger programs adopt a single-exit cleanup pattern:

```c
FILE *in = NULL;
char *line = NULL;
int status = EXIT_FAILURE;

in = fopen("data.txt", "r");
if (!in) goto cleanup;

line = readLine(in);
if (!line) goto cleanup;

status = EXIT_SUCCESS;      // Everything worked

cleanup:
    free(line);             // free(NULL) is safe
    if (in) fclose(in);
    return status;
```

---

## 6. Text vs. Binary — Choosing an I/O Strategy

| Criterion | Text | Binary |
|-----------|------|--------|
| Human readability | Yes | No |
| Size | Larger (formatted) | Compact |
| Random access | Awkward (variable-length lines) | Natural (`fseek` by record size) |
| Portability across platforms | Good | Layout/endianness dependent |
| Best for | Config, logs, CSV | Fixed records, images, large datasets |

---

## 7. Summary

* stdio buffers streams (full/line/unbuffered); `fflush` and `setvbuf` control when data actually moves.
* `fseek`/`ftell`/`rewind` give random access; fixed-size binary records make seeking straightforward.
* Redirect streams with the shell (`<`, `>`, `2>`, `|`) and keep stdout for data, stderr for messages.
* Robust input = dynamic line reading + bounded parsing + consistent cleanup.
