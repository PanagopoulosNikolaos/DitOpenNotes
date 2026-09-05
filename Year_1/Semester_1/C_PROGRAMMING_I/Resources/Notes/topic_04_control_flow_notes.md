# Topic 4: Control Flow — Decisions

## 1. The if Statement

The most basic decision structure executes a block only when a condition is true (non-zero):

```c
int temperature = 35;

if (temperature > 30) {
    printf("It is hot.\n");
}
```

The parentheses around the condition are mandatory. The condition is evaluated as an integer: `0` is false, anything else is true.

---

## 2. if / else / else if

```c
int score = 78;

if (score >= 90) {
    printf("Grade: A\n");
} else if (score >= 80) {
    printf("Grade: B\n");
} else if (score >= 70) {
    printf("Grade: C\n");
} else {
    printf("Grade: F\n");
}
```

Conditions are tested **top to bottom**, and the first true branch wins — the rest are skipped. Ordering conditions from most to least specific avoids unreachable branches.

---

## 3. Nested Decisions

An `if` inside another `if` refines the logic:

```c
if (age >= 18) {
    if (hasID) {
        printf("Access granted.\n");
    } else {
        printf("Access denied: no ID.\n");
    }
}
```

**The dangling-else pitfall:** an `else` always pairs with the *nearest* unmatched `if`, not the visually aligned one. Braces make the pairing explicit and prevent this entire class of bugs:

```c
// Without braces this else belongs to the inner if:
if (a > 0)
    if (b > 0)
        printf("both positive\n");
else
    printf("which if does this belong to?\n");
```

---

## 4. The switch Statement

`switch` selects one branch based on an integer-valued expression:

```c
int choice;
printf("1) Load  2) Save  3) Exit\n");
scanf("%d", &choice);

switch (choice) {
    case 1:
        printf("Loading...\n");
        break;                 // break exits the switch
    case 2:
        printf("Saving...\n");
        break;
    case 3:
        printf("Bye!\n");
        break;
    default:                   // Runs when no case matches
        printf("Unknown option.\n");
        break;
}
```

Rules and details:

* The controlling expression must be an integer type (`int`, `char`, enum). `switch` cannot operate on strings or floating-point values.
* `case` labels must be **compile-time constants**.
* **Fall-through:** without `break`, execution continues into the next case. Sometimes this is exploited deliberately:

```c
switch (ch) {
    case 'a':
    case 'e':
    case 'i':
    case 'o':
    case 'u':
        printf("Vowel\n");
        break;
    default:
        printf("Not a vowel\n");
}
```

* `switch` is generally faster and clearer than a long `else if` chain of equality tests.

---

## 5. The Conditional Operator

For simple two-way choices embedded in an expression:

```c
int larger = (x > y) ? x : y;
printf("%s\n", (n % 2 == 0) ? "even" : "odd");
```

---

## 6. Comparison with Equality and Assignment

The classic bug:

```c
if (x = 5) { }    // ASSIGNS 5 to x; the result (5) is true — always runs!
if (x == 5) { }   // Correct comparison
```

Some programmers write `if (5 == x)` ("yoda condition") so that a typo produces a compile error, though modern compilers warn about this anyway.

---

## 7. Design Guidelines

* Use `if/else if` for **range** conditions (`score >= 90`).
* Use `switch` for **discrete equality** conditions (menu choices, character classes).
* Always brace bodies, even single statements — it prevents bugs when code is later extended.
* Handle impossible or unexpected inputs with a `default`/`else` branch.

---

## 8. Summary

* Conditions are integer expressions: non-zero means true.
* `else if` chains test ranges; the first true branch wins.
* `switch` works on integer expressions with compile-time case labels and requires `break` to avoid fall-through.
* `= vs ==` is one of the most common C bugs; treat compiler warnings seriously.
