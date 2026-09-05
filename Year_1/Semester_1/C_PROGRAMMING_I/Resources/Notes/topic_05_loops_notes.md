# Topic 5: Loops and Iteration

## 1. Why Loops?

Loops repeat a block of code while a condition holds. They eliminate duplication and make it possible to process data of any size: arrays, file contents, user input sequences.

C provides three loop constructs: `for`, `while`, and `do-while`. All three are logically interchangeable; the choice is about clarity.

---

## 2. The while Loop (Entry-Condition)

Checks the condition **before** each iteration; the body may execute zero times:

```c
int i = 0;
while (i < 5) {
    printf("%d ", i);
    i++;                 // Must make progress toward the exit condition!
}
// Output: 0 1 2 3 4
```

Typical use cases: reading input until EOF, waiting for a sentinel value, event-driven loops where the number of iterations is unknown in advance.

```c
int value;
while (scanf("%d", &value) == 1) {   // Runs while valid integers keep coming
    process(value);
}
```

---

## 3. The do-while Loop (Exit-Condition)

Checks the condition **after** each iteration; the body always runs at least once:

```c
int choice;
do {
    printf("Enter 0 to quit: ");
    scanf("%d", &choice);
} while (choice != 0);
```

Note the required trailing semicolon. `do-while` is ideal for menus and input validation loops where the user must be prompted at least once.

---

## 4. The for Loop (Counted Iteration)

```c
for (initialization; condition; update) {
    body;
}
```

Execution order: initialization (once) → condition → body → update → condition → ...

```c
for (int i = 0; i < 10; i++) {   // i declared in the loop scope (C99)
    printf("%d ", i);
}
```

All three parts are optional; `for (;;)` is an intentional infinite loop, equivalent to `while (1)`. Multiple variables can be updated with the comma operator:

```c
for (int i = 0, j = 9; i < j; i++, j--) { /* converging pair */ }
```

**Which loop to choose?** Use `for` when the number of iterations is known (counting, iterating an array), `while` when only the condition is known, and `do-while` when the body must run first.

---

## 5. break and continue

* `break` exits the nearest enclosing loop (or `switch`) immediately.
* `continue` skips the rest of the current iteration and jumps to the next one (for `for` loops, the update expression still runs).

```c
for (int i = 0; i < 100; i++) {
    if (i % 2 == 0) {
        continue;            // Skip even numbers
    }
    if (i > 50) {
        break;               // Stop entirely past 50
    }
    printf("%d ", i);
}
```

Use `break`/`continue` sparingly — deeply nested breaks hurt readability.

---

## 6. Nested Loops

A loop inside a loop; the inner loop runs completely for every outer iteration. The classic example is a two-dimensional pattern:

```c
for (int row = 1; row <= 3; row++) {
    for (int col = 1; col <= row; col++) {
        printf("* ");
    }
    printf("\n");
}
/*
* 
* * 
* * * 
*/
```

Complexity note: nested loops multiply work — two loops of n iterations perform n × n operations (O(n²)).

---

## 7. Common Loop Patterns

| Pattern | Structure |
|---------|-----------|
| Counter loop | `for (i = 0; i < n; i++)` |
| Sentinel loop | `while (input != SENTINEL)` |
| Input validation | `do { prompt; read; } while (invalid)` |
| Accumulator | `total += x;` inside a loop |
| Search loop | loop until found, then `break` with a `found` flag |
| Array traversal | `for (i = 0; i < size; i++) a[i]` |

---

## 8. Common Pitfalls

* **Off-by-one errors:** using `<=` with `size` reads one past the array end. Arrays are indexed `0` to `size - 1`, so the condition is `i < size`.
* **Infinite loops:** forgetting the update (`while (i < 5)` with no `i++`) or writing `=` instead of `==` in the condition.
* **Floating-point loop counters:** accumulation error makes `i != 1.0` unreliable; loop over integers instead.
* **Modifying the loop variable inside the body** in ways that break the exit condition.
* **Loop bounds with `size_t`:** `for (size_t i = size - 1; i >= 0; i--)` is infinite because unsigned types never go below 0; count down with `i-- > 0` idioms or use signed types.

---

## 9. Summary

* `while` tests before the body, `do-while` after (body runs at least once), `for` bundles init/condition/update for counted iteration.
* `break` leaves the loop entirely; `continue` skips to the next iteration.
* Off-by-one and infinite-loop bugs are the dominant loop hazards — verify boundaries carefully.
