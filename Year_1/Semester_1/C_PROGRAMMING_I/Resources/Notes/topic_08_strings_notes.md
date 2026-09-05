# Topic 8: Strings in C

## 1. What Is a C String?

C has no built-in string type. A string is a **`char` array terminated by the null character `'\0'`** (byte value 0):

```c
char word[6] = {'H', 'e', 'l', 'l', 'o', '\0'};
char word2[] = "Hello";        // Compiler adds the '\0' → size 6
char *word3  = "Hello";        // Pointer to a string literal (read-only)
```

The terminator is what lets every string function find the end: a string's length is the number of characters *before* `'\0'`. Therefore a string of n visible characters needs n + 1 bytes of storage.

---

## 2. Declaration and Initialization

```c
char name[20];                     // 19 usable characters + terminator
char city[] = "Athens";            // Size auto-set to 7
char prompt[64] = "Enter value: "; // Fits in a larger buffer, rest is '\0'
```

**Literal vs. buffer:** `"Hello"` written as a literal is stored in read-only memory; a `char` array is writable. Assigning to an element of a literal through a `char *` is undefined behavior:

```c
char *s = "abc";
s[0] = 'x';          // UNDEFINED — literals are not writable
char t[] = "abc";
t[0] = 'x';          // Fine — t is a writable copy
```

Strings can only be assigned at initialization. For later assignment use `strcpy`, never `=` (that would copy the pointer, not the text).

---

## 3. Reading Strings

```c
char buffer[32];

scanf("%31s", buffer);      // One word, limited to 31 chars + '\0'
scanf(" %31[^\n]", buffer); // One whole line including spaces
fgets(buffer, sizeof buffer, stdin);   // Preferred: reads a whole line safely
```

`fgets` keeps the trailing `'\n'` if there is room — trim it:

```c
buffer[strcspn(buffer, "\n")] = '\0';
```

Never use `gets()` — it has no length limit and was removed from the language in C11.

---

## 4. The <string.h> Library

| Function | Purpose |
|----------|---------|
| `strlen(s)` | Length **excluding** `'\0'` (size_t result) |
| `strcpy(dst, src)` | Copy src into dst (unsafe if dst too small) |
| `strncpy(dst, src, n)` | Copy at most n chars (may not terminate!) |
| `strcat(dst, src)` | Append src to dst |
| `strncat(dst, src, n)` | Append at most n chars (always terminates) |
| `strcmp(a, b)` | Compare: `<0` if a<b, `0` if equal, `>0` if a>b |
| `strncmp(a, b, n)` | Compare first n characters |
| `strchr(s, c)` | Pointer to first occurrence of char c |
| `strstr(s, sub)` | Pointer to first occurrence of substring |
| `strspn` / `strcspn` | Length of initial segment in / not in a set |

```c
char full[64] = "Hello";
strcat(full, ", world");             // "Hello, world"
if (strcmp(pass, "secret") == 0) { /* match */ }
size_t len = strlen(full);           // 12
```

**Beware `strcpy`/`strcat` overflow:** both trust the destination size. Prefer the bounded variants and always size buffers as `max_text_length + 1`.

---

## 5. Printing and Conversion

```c
printf("%s", name);
printf("%10s", name);    // Right-aligned width 10
printf("%-10s", name);   // Left-aligned

// Conversions (stdlib.h / stdio.h)
int n = atoi("123");                 // Quick, no error reporting
long v = strtol(text, NULL, 10);     // Robust: detects errors, any base
sprintf(out, "x=%d", n);             // Print INTO a string (mind the buffer)
snprintf(out, sizeof out, "x=%d", n);// Bounded version — always prefer this
```

---

## 6. String as Pointer Arithmetic

Since a string is an array of chars, the same decay rules apply:

```c
char *p = "Hello";
p++;                     // Now points at 'e'
printf("%s\n", p);       // "ello" — printing starts where p points
```

Passing a substring is simply passing `s + k`.

---

## 7. Common Patterns

```c
// Count vowels
int vowels = 0;
for (size_t i = 0; s[i] != '\0'; i++)
    if (strchr("aeiou", tolower((unsigned char)s[i]))) vowels++;

// Tokenize a line (mutates the buffer!)
char *token = strtok(line, " ");
while (token) {
    use(token);
    token = strtok(NULL, " ");
}

// Character classification (ctype.h)
isdigit(c), isalpha(c), isspace(c), isupper(c), tolower(c), toupper(c)
```

---

## 8. Common Pitfalls

| Pitfall | Consequence |
|---------|-------------|
| Forgetting space for `'\0'` | Functions read past the buffer |
| `strcpy` into a too-small array | Buffer overflow (classic security bug) |
| `strncpy` without manual termination | Strings that never end |
| Comparing strings with `==` | Compares **addresses**, not text — use `strcmp` |
| Writing to a string literal | Undefined behavior / crash |
| `strlen` result vs `size_t` comparisons mixing signedness | Subtle loop bugs |

---

## 9. Summary

* A C string is a char array ending in `'\0'`; the terminator must always be planned for.
* Use `fgets` (not `gets`, not bare `scanf("%s")`) for safe line input.
* `<string.h>` provides length, copy, append, compare, and search functions; the bounded variants are safer.
* Compare strings with `strcmp` — `==` compares pointers.
