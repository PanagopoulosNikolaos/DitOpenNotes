# Topic 13: The Preprocessor, Macros, and Headers

## 1. What the Preprocessor Does

Before compilation, the **preprocessor** performs textual transformations on the source: it includes files, expands macros, and conditionally selects code. All directives start with `#` and occupy their own line. The preprocessor knows nothing about C syntax — it works purely on tokens and text.

```bash
gcc -E main.c        # Show the fully preprocessed output
```

---

## 2. #include

```c
#include <stdio.h>     // Search the SYSTEM include directories first
#include "utils.h"     // Search the PROJECT directory first
```

* Angle brackets: standard library and installed system headers.
* Quotes: your own header files.
* Includes are literal text pastes — including the same header twice can duplicate definitions (solved by header guards, §6).

---

## 3. Object-Like Macros (#define)

```c
#define MAX_SIZE 100
#define PI 3.14159

int buffer[MAX_SIZE];          // Replaced by 100 before compilation
```

The preprocessor does a pure token substitution. Two classic rules follow:

1. **Parenthesize the whole value:** `#define AREA(w,h) ((w)*(h))` — `#define SUM 2+3` breaks `SUM * 10` into `2+3*10`.
2. Constant expressions computed by the compiler are usually better than macros for simple values.

---

## 4. Function-Like Macros

```c
#define SQUARE(x)   ((x) * (x))
#define MAX(a, b)   ((a) > (b) ? (a) : (b))

int y = SQUARE(4);          // ((4) * (4))
```

**Argument-evaluation pitfall:** macros paste their arguments textually, so arguments with side effects repeat:

```c
int n = 5;
int r = SQUARE(n++);        // ((n++) * (n++)) — n incremented twice, r undefined
```

Parenthesizing every parameter usage is mandatory: `#define BAD(x) x * x` makes `BAD(1 + 2)` become `1 + 2 * 1 + 2` = 5, not 9.

Prefer real `inline` functions or plain functions when type safety matters; macros cannot check types.

---

## 5. Conditional Compilation

Directives that include or exclude code depending on conditions — used for debug code, portability, and configuration:

```c
#define DEBUG 1

#ifdef DEBUG
    fprintf(stderr, "x = %d\n", x);     // Compiled only when DEBUG is defined
#endif

#ifndef VERSION
#define VERSION 2                            // Default if not given on command line
#endif

#if VERSION >= 2
    /* new code path */
#else
    /* legacy path */
#endif
```

Enable from the command line: `gcc -DDEBUG main.c` defines `DEBUG` without editing the file.

---

## 6. Headers and Header Guards

A **header file** (`.h`) declares the public interface; the implementation lives in a `.c` file:

```c
// math_utils.h
#ifndef MATH_UTILS_H          // Header guard: include at most once
#define MATH_UTILS_H

double average(double a, double b);
int    max_int(int a, int b);

#endif
```

```c
// math_utils.c
#include "math_utils.h"

double average(double a, double b) { return (a + b) / 2.0; }
int    max_int(int a, int b)       { return (a > b) ? a : b; }
```

The guard (`#ifndef/#define/#endif`) prevents "redefinition" errors when a header is included multiple times. Multi-file builds link the translation units together:

```bash
gcc main.c math_utils.c -o app     # Compile and link all sources
```

---

## 7. Other Useful Directives

| Directive | Purpose |
|-----------|---------|
| `#undef NAME` | Remove a macro definition |
| `#error "message"` | Force a compile error (e.g. unsupported platform) |
| `#pragma once` | Non-standard but widespread alternative to guards |
| `#` / `##` in macros | Stringify an argument / paste tokens together |

```c
#define STR(x)  #x                 // STR(hello) → "hello"
#define GLUE(a,b) a##b             // GLUE(a,1) → a1
```

---

## 8. Common Pitfalls

* Missing parentheses in macro definitions (precedence bugs).
* Side-effecting arguments to macros (`SQUARE(i++)`).
* Missing header guards causing duplicate-definition errors.
* Macro names colliding with variable names — by convention macros are `UPPER_SNAKE_CASE`.
* Relying on macro "functions" where a typed function would be safer.

---

## 9. Summary

* The preprocessor performs include, macro, and conditional text transformation before compilation.
* Parenthesize macros and their arguments; beware repeated side effects.
* Conditional compilation toggles code without editing sources (`-D` on the command line).
* Header guards make headers safe to include multiple times.
