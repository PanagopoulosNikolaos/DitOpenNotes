# C — Standard Library and Systems Programming

The C standard library provides core functionality for file access, memory management, mathematical computation, and system calls. Through these libraries, C programs interact directly with operating system abstractions such as files, processes, signals, and environment variables. This file covers standard headers, stream-based file I/O, process management, signal handling, and differences in execution models between C and C++.

---

## 1. Standard Library Headers Reference

C separates platform-independent functionality into dedicated headers.

| Header | Primary Purpose | Common Symbols |
| :--- | :--- | :--- |
| `<stdio.h>` | Input/Output Streams | `printf`, `scanf`, `fopen`, `fread`, `fwrite`, `FILE` |
| `<stdlib.h>` | General Utilities, Memory | `malloc`, `free`, `exit`, `getenv`, `system` |
| `<string.h>` | Byte/String Manipulation | `strlen`, `strcpy`, `memset`, `memcpy` |
| `<math.h>` | Mathematical Computations | `sin`, `cos`, `sqrt`, `pow` (requires linking `-lm`) |

---

## 2. File Input/Output and Buffering

File operations in C utilize the `FILE` structure, which wraps raw file descriptors with buffering.

### 2.1 File Open Modes Reference Table

| Mode | Operations Allowed | File Exists Behavior | File Missing Behavior |
| :--- | :--- | :--- | :--- |
| `"r"` | Read | Opens at beginning | Returns `NULL` (Error) |
| `"w"` | Write | Truncates to 0 length | Creates file |
| `"a"` | Append | Writes only at end | Creates file |
| `"r+"` | Read and Write | Opens at beginning | Returns `NULL` (Error) |
| `"w+"` | Read and Write | Truncates to 0 length | Creates file |
| `"a+"` | Read and Write | Writes only at end | Creates file |

---

### 2.2 API Reference: Stream File Operations

```text
FILE *fopen(const char *filename, const char *mode);
size_t fread(void *ptr, size_t size, size_t count, FILE *stream);
size_t fwrite(const void *ptr, size_t size, size_t count, FILE *stream);
int fflush(FILE *stream);
int fclose(FILE *stream);
```

### 2.3 I/O Buffering

C streams are buffered to reduce the overhead of system calls.
- **Fully Buffered:** Accumulates data until the buffer is full before executing a write system call (default for files).
- **Line Buffered:** Flushes output whenever a newline character (`'\n'`) is encountered (default for `stdout`).
- **Unbuffered:** Writes immediately to the output device (default for `stderr`).

---

## 3. Process Control, Signals, and Environment

For POSIX-compliant systems programming, C exposes process and signal structures.

### 3.1 Process and Signal Reference Table

| API | Header | Purpose | Return Value / Behavior |
| :--- | :--- | :--- | :--- |
| `fork` | `<unistd.h>` | Creates a clone child process | Child returns $0$; parent returns child PID |
| `execve` | `<unistd.h>` | Replaces process image with new program | Does not return on success; $-1$ on failure |
| `wait` | `<sys/wait.h>` | Suspends process until a child terminates | Returns PID of terminated child |
| `signal` | `<signal.h>` | Registers a handler function for a signal | Returns previous handler, or `SIG_ERR` |
| `getenv` | `<stdlib.h>` | Retrieves environment variable value | Pointer to string value, or `NULL` |

---

## 4. C vs. C++ Language Differences

Although C++ began as a superset of C, the two languages have diverged. C++ introduces features such as object-oriented structures and RAII that change execution semantics.

| Property | C | C++ |
| :--- | :--- | :--- |
| **Paradigm** | Procedural (Functions + Data) | Multi-paradigm (OOP, Templates, RAII) |
| **Resource Management** | Manual (`malloc`/`free`) | Resource Acquisition Is Initialization (RAII) |
| **Implicit `void*` cast** | Allowed (`int* p = malloc(...)`) | Forbidden (Requires explicit cast) |
| **Exceptions** | Error codes, `setjmp`/`longjmp` | Try/Catch blocks |
| **Function Overloading** | Not supported | Supported (Requires name mangling) |

---

## Solved Exercises

### Exercise 1: Copy File in Blocks

**Problem:** Implement a program using `fopen`, `fread`, `fwrite`, and `fclose` that copies a binary file in chunks of $512$ bytes.

**Solution:**

```c
#include <stdio.h>
#include <stdlib.h>

void copy_file(const char *src, const char *dest) {
    FILE *in = fopen(src, "rb");
    if (in == NULL) {
        perror("Error opening source file");
        return;
    }
    
    FILE *out = fopen(dest, "wb");
    if (out == NULL) {
        perror("Error opening destination file");
        fclose(in);
        return;
    }
    
    unsigned char buffer[512];
    size_t bytes_read;
    
    while ((bytes_read = fread(buffer, 1, sizeof(buffer), in)) > 0) {
        fwrite(buffer, 1, bytes_read, out);
    }
    
    fclose(in);
    fclose(out);
}

int main(void) {
    copy_file("source.bin", "copy.bin");
    return 0;
}
```

---

### Exercise 2: stdout vs. stderr Buffering

**Problem:** Determine what is printed first by this program and explain why.

```c
#include <stdio.h>
#include <unistd.h>

int main(void) {
    printf("Hello ");
    fprintf(stderr, "World");
    sleep(1);
    printf("\n");
    return 0;
}
```

**Solution:**
1. `printf("Hello ")` writes to `stdout`. Because `stdout` is line-buffered, and no newline (`'\n'`) is present, `"Hello "` is buffered in memory.
2. `fprintf(stderr, "World")` writes to `stderr`. Since `stderr` is unbuffered, `"World"` is written to the terminal immediately.
3. The program sleeps for 1 second.
4. `printf("\n")` encounters a newline. The buffer of `stdout` is flushed, printing `"Hello \n"`.
5. **Output sequence:** `"World"` is printed immediately, followed by a 1-second pause, and then `"Hello "` is printed.

```text
WorldHello 
```

---

### Exercise 3: POSIX Fork Execution Paths

**Problem:** Predict the total number of lines printed and trace the execution paths of this code.

```c
#include <stdio.h>
#include <unistd.h>

int main(void) {
    fork();
    fork();
    printf("Process\n");
    return 0;
}
```

**Solution:**
1. Let the initial parent process be $P_0$.
2. The first `fork()` spawns child $P_1$. Now $2$ active processes exist ($P_0$ and $P_1$).
3. The second `fork()` is reached by both $P_0$ and $P_1$.
   - $P_0$ spawns grandchild $P_2$.
   - $P_1$ spawns grandchild $P_3$.
4. Now $4$ processes run concurrently ($P_0$, $P_1$, $P_2$, $P_3$).
5. Each process executes the next statement `printf("Process\n")` independently.
6. The terminal prints $4$ lines containing `"Process"`.

```text
Process
Process
Process
Process
```

---

### Exercise 4: Safe Signal Registration

**Problem:** Write a program that registers a handler for `SIGINT` (Ctrl+C) to print a message and exit cleanly.

**Solution:**

```c
#include <stdio.h>
#include <stdlib.h>
#include <signal.h>

void sigint_handler(int sig_num) {
    // Note: Calling printf in a signal handler is technically unsafe 
    // because printf is not async-signal-safe. We use it here for demonstration.
    (void)sig_num; // Suppress unused parameter warning
    printf("\nReceived SIGINT. Cleaning up.\n");
    exit(0);
}

int main(void) {
    if (signal(SIGINT, sigint_handler) == SIG_ERR) {
        perror("Signal registration failed");
        return 1;
    }
    
    printf("Waiting for Ctrl+C...\n");
    while (1) {
        // Busy loop simulating program execution
    }
    return 0;
}
```

---

### Exercise 5: Environment Variable Modification

**Problem:** Write a program that reads the `PATH` variable, prints it, and exits.

**Solution:**

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    char *path = getenv("PATH");
    if (path != NULL) {
        printf("PATH = %s\n", path);
    } else {
        printf("PATH variable not set.\n");
    }
    return 0;
}
```

---

### Exercise 6: Math Library Compilation Linkage

**Problem:** Compile a math program using `<math.h>` and explain why compilation fails if the linker flag is omitted.

**Solution:**
1. File `math_test.c`:
   ```c
   #include <stdio.h>
   #include <math.h>
   int main(void) {
       double res = sqrt(2.0);
       printf("%f\n", res);
       return 0;
   }
   ```
2. Running `gcc math_test.c -o test` fails during linking with:
   `undefined reference to 'sqrt'`.
3. **Reason:** The math function symbols are defined in the separate shared math library `libm`.
4. **Fix:** Link the math library explicitly using the `-lm` flag: `gcc math_test.c -lm -o test`.

---

### Exercise 7: Implicit void* Cast differences between C and C++

**Problem:** Explain why this line compiles in C but fails in C++.

```c
int *arr = malloc(10 * sizeof(int));
```

**Solution:**
1. `malloc` returns a pointer of type `void*`.
2. In C, `void*` is implicitly converted to any other pointer type, making this assignment valid.
3. In C++, implicit conversions from `void*` to typed pointers are prohibited. This ensures type safety but breaks compatibility.
4. **Fix for C++:** Cast the returned pointer explicitly, or use `new`:
   ```cpp
   int *arr = (int*)malloc(10 * sizeof(int));
   // Or standard C++ allocation:
   int *arr2 = new int[10];
   ```

---

### Exercise 8: File End-of-File Detection Gotcha

**Problem:** Explain why using `while (!feof(file))` to read data from a stream leads to printing the last line twice.

**Solution:**
1. The `feof()` function returns true only **after** a read operation attempts to read past the end of the file.
2. If a file contains one character `"A"`, and the loop is:
   ```c
   while (!feof(file)) {
       char c = fgetc(file);
       printf("%c", c);
   }
   ```
3. First iteration: `fgetc` reads `'A'`. `feof` is still false.
4. Second iteration: `fgetc` tries to read. It hits EOF and returns constant `-1` (`EOF`). `feof` flag is set to true. However, the loop continues and prints `EOF` (rendered as garbage or duplicate value).
5. **Fix:** Check the return value of the read function directly.

```c
int c;
while ((c = fgetc(file)) != EOF) {
    printf("%c", c);
}
```

---

## Common Errors and Gotchas

### 1. Missing Binary Mode Flag on Windows
* **Cause:** Opening binary files with `"w"` or `"r"` instead of `"wb"` or `"rb"`. On Windows platforms, text mode converts LF (`\n`) to CRLF (`\r\n`) in the stream, corrupting binary files.
* **Resolution:** Always use the `"b"` suffix modifier when opening non-text files.

### 2. Leaking File Descriptors
* **Cause:** Forgetting to call `fclose` on a file pointer. Operating systems limit the number of open file descriptors per process; running out causes subsequent `fopen` calls to fail.
* **Resolution:** Close every file descriptor on all exit paths, including error blocks.

### 3. Mixing Line Buffering and Direct Writing
* **Cause:** Using `printf("Loading...")` without a newline or `fflush` before running a long computation. The user sees no output until the program terminates or buffers flush.
* **Resolution:** Call `fflush(stdout);` explicitly to force writing when no newline is present.

---

## Exam Tip: C vs. C++ Linkage Compatibility

**Linkage Traps:**
When compiling C code within a C++ project, function calls fail at link time due to C++ name mangling.
- **Mangled Names:** C++ encodes function arguments into the symbol name to support function overloading (e.g. `foo(int)` becomes `_Z3fooi`). C compiles symbols without mangling (`foo` remains `foo`).
- **Resolution:** Wrap C declarations in C++ headers with `extern "C"` to disable name mangling:
  ```cpp
  #ifdef __cplusplus
  extern "C" {
  #endif
  
  void c_function(int x);
  
  #ifdef __cplusplus
  }
  #endif
  ```
