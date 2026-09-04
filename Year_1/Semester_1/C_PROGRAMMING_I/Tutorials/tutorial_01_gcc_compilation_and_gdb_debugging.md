# Tutorial 01: GCC Compilation Pipeline and GDB Interactive Debugging

## Context and Grounding
This tutorial provides an operational guide to compiling C source code with standard compiler diagnostic flags and diagnosing logic errors, segmentation faults, and runtime crashes using the GNU Debugger (`gdb`).

---

## 1. Mastering GCC Compiler Flags

When building academic and production C software, always invoke GCC with strict diagnostic flags:

```bash
gcc -Wall -Wextra -Werror -std=c11 -pedantic -g3 -O0 program.c -o program
```

### 1.1 Critical Flag Reference
| Flag | Functional Behavior |
|:---|:---|
| `-std=c11` | Adheres strictly to the ISO C11 language standard. |
| `-Wall` | Enables standard compiler warning diagnostics. |
| `-Wextra` | Enables additional diagnostic warnings (e.g., unused parameters, sign comparisons). |
| `-Werror` | Promotes all compiler warnings to compilation-terminating errors. |
| `-pedantic` | Enforces strict ISO C conformance, flagging non-standard compiler extensions. |
| `-g3` | Generates detailed debugging symbols including preprocessor macro expansions for GDB. |
| `-O0` | Disables optimizations, ensuring instruction order directly mirrors source line order. |

### 1.2 Inspecting Compilation Stages
```bash
# Preprocessing only (expands macros and includes)
gcc -E program.c -o program.i

# Compilation only (generates assembly text)
gcc -S program.i -o program.s

# Assembly only (generates relocatable machine object file)
gcc -c program.s -o program.o

# Linking (links object file with standard C runtime to create binary)
gcc program.o -o program
```

---

## 2. Interactive Debugging with GDB

### 2.1 Starting GDB
Launch your debugging-instrumented executable under GDB:
```bash
gdb ./program
```

### 2.2 Essential GDB Commands Reference
| Command | Shortcut | Purpose |
|:---|:---|:---|
| `run [args]` | `r` | Starts program execution with optional command line arguments. |
| `break [location]` | `b` | Sets a breakpoint at a function name or line number (e.g., `b main`, `b 42`). |
| `next` | `n` | Executes the next line of code, stepping **over** function calls. |
| `step` | `s` | Executes the next line of code, stepping **into** function calls. |
| `continue` | `c` | Resumes execution until the next breakpoint or program termination. |
| `print [expr]` | `p` | Prints the current value of a variable or evaluates an expression (`p *ptr`). |
| `display [expr]` | `disp`| Prints the specified expression automatically at every execution step. |
| `backtrace` | `bt` | Prints the stack trace showing all active call frames when crashed. |
| `frame [num]` | `f` | Selects and inspects the specified activation frame from the backtrace. |
| `quit` | `q` | Exits the GDB interactive session. |

---

## 3. Walkthrough: Debugging an Off-By-One Segmentation Fault

Consider the following buggy program (`faulty.c`):
```c
#include <stdio.h>

/**
 * Calculates sum of elements in an array.
 *
 * Args:
 *   data (const int *): Input array buffer.
 *   size (int): Number of elements in array.
 *
 * Returns:
 *   int: Sum of elements.
 */
int computeSum(const int *data, int size) {
    int total = 0;
    // Bug: Condition i <= size causes out-of-bounds array access
    for (int i = 0; i <= size; ++i) {
        total += data[i];
    }
    return total;
}

int main(void) {
    int sample[3] = {10, 20, 30};
    int result = computeSum(sample, 3);
    printf("Result: %d\n", result);
    return 0;
}
```

### 3.1 Debugging Session Trace
1. Compile with debugging symbols:
   ```bash
   gcc -g3 -O0 faulty.c -o faulty
   ```
2. Launch in GDB and set breakpoint at `computeSum`:
   ```text
   $ gdb ./faulty
   (gdb) break computeSum
   Breakpoint 1 at 0x1149: file faulty.c, line 15.
   (gdb) run
   Starting program: ./faulty 

   Breakpoint 1, computeSum (data=0x7fffffffe340, size=3) at faulty.c:15
   15          int total = 0;
   (gdb) next
   17          for (int i = 0; i <= size; ++i) {
   (gdb) print size
   $1 = 3
   (gdb) print i
   $2 = 0
   (gdb) next
   18              total += data[i];
   (gdb) print data[0]
   $3 = 10
   (gdb) continue
   ```
3. Inspecting the loop predicate confirms that when `i == 3`, `data[3]` accesses unallocated memory past the 3-element buffer `sample[3]`.
4. Fix: Modify loop condition to `i < size`.

