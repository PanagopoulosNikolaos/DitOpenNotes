# Topic 3: Basic Input and Output (stdio)

## 1. The Standard I/O Library

All standard input and output in C comes from `<stdio.h>`. Three standard streams are available to every program:

| Stream | Direction | Default Destination |
|--------|-----------|---------------------|
| `stdin` | Input | Keyboard |
| `stdout` | Output | Terminal display |
| `stderr` | Errors | Terminal display (unbuffered) |

---

## 2. Formatted Output: printf

`printf` takes a *format string* containing placeholders (format specifiers) and matching values:

```c
int age = 20;
double gpa = 3.75;
char initial = 'N';

printf("Age: %d, GPA: %.2f, Initial: %c\n", age, gpa, initial);
```

### Common Format Specifiers

| Specifier | Type | Example Output |
|-----------|------|----------------|
| `%d` / `%i` | `int` | `42` |
| `%u` | unsigned `int` | `42` |
| `%ld` | `long` | `1000000` |
| `%f` | `double` | `3.750000` |
| `%.2f` | `double`, 2 decimals | `3.75` |
| `%e` | scientific notation | `3.75e+00` |
| `%g` | shortest of `%e`/`%f` | `3.75` |
| `%c` | single `char` | `N` |
| `%s` | C string | `Hello` |
| `%p` | pointer address | `0x7ffee4...` |
| `%%` | a literal `%` | `%` |
| `%x` / `%o` | hex / octal | `2a` / `52` |

### Width, Precision, and Flags

```c
printf("%5d|\n",   42);     // "   42|"   — right-aligned in width 5
printf("%-5d|\n",  42);     // "42   |"   — left-aligned (minus flag)
printf("%05d\n",   42);     // "00042"    — zero-padded
printf("%10.3f\n", 3.14159);// "     3.142" — width 10, 3 decimals
```

---

## 3. Formatted Input: scanf

`scanf` reads from `stdin` and stores values **through pointers**, so arguments must be prefixed with `&` (address-of), except for arrays/strings:

```c
int age;
double height;
char name[50];

scanf("%d", &age);          // & needed for scalar variables
scanf("%lf", &height);      // NOTE: %lf for double in scanf (not %f)
scanf("%s", name);          // NO & for char arrays (they already act as pointers)
```

Key details:

* `%d` in `scanf` skips leading whitespace and reads digits until a non-digit.
* `%s` reads one whitespace-delimited word; it has **no length limit** here, which is a buffer-overflow risk (see Topic 15).
* `scanf` returns the number of items successfully read, or `EOF`. Always check the return value:

```c
if (scanf("%d", &value) != 1) {
    fprintf(stderr, "Invalid input.\n");
    return 1;
}
```

* Bad input (e.g. letters when `%d` is expected) leaves the offending characters **in the input buffer**; a common cleanup is `while (getchar() != '\n');`.

---

## 4. Character I/O: getchar and putchar

The simplest I/O functions work one character at a time:

```c
int c;                       // MUST be int, not char, to hold EOF

while ((c = getchar()) != EOF) {
    putchar(c);              // Echo every character typed
}
```

* `getchar()` returns the next character from `stdin`, or the special value `EOF` (typically `-1`) at end of input.
* Because `EOF` may equal `-1`, the receiving variable is declared as `int`.
* On the terminal, `EOF` is produced by Ctrl+D (Linux/macOS) or Ctrl+Z then Enter (Windows).

---

## 5. Unformatted String Output: puts

```c
puts("Hello");     // Prints the string and appends a newline automatically
```

`puts` is simpler and safer than `printf` when no formatting is needed.

---

## 6. How Terminal Input Really Works (Line Buffering)

By default, `stdin` is **line buffered**: the program receives nothing until the user presses Enter. The whole line sits in the input buffer, and each `scanf`/`getchar` call consumes only what it needs, leaving the rest for the next call. Understanding this explains most "my program skips a scanf" problems — a previous `scanf` left a `'\n'` in the buffer that the next `%c` immediately consumes.

```c
int number;
char letter;

scanf("%d", &number);
scanf(" %c", &letter);   // Leading space in the format skips leftover whitespace/newline
```

---

## 7. Common Pitfalls

| Pitfall | Fix |
|---------|-----|
| `%f` in `scanf` for `double` | Use `%lf` in `scanf` (`%f` is fine in `printf`) |
| Missing `&` in `scanf` | `scanf("%d", age)` crashes — pass `&age` |
| `%s` with unbounded length | Use `%49s` for a 50-byte buffer, or `fgets` |
| Ignoring `scanf`'s return value | Always validate before using the variable |
| `%c` consuming a leftover newline | Put a space before `%c` in the format string |

---

## 8. Summary

* `printf` formats output with specifiers; width and precision control alignment.
* `scanf` reads input through pointers and returns the count of parsed items.
* `getchar`/`putchar` handle character-at-a-time I/O and expose `EOF`.
* Input is line-buffered; leftover characters in the buffer cause most I/O surprises.
