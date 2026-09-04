# Core C Programming Practice Drills and Solutions

This drill document provides 15 progressive programming problems across fundamental C concepts, accompanied by complete model implementations and explanatory breakdowns.

---

## Section 1: Control Flow and Arithmetic

### Exercise 1: Prime Number Validator
**Problem:** Write a function `isPrime` that determines whether a positive integer $n$ is prime ($n > 1$).
**Model Implementation:**
```c
#include <stdbool.h>

/**
 * Evaluates whether an integer is prime.
 *
 * Args:
 *   n (int): The positive integer to evaluate.
 *
 * Returns:
 *   bool: True if n is prime, false otherwise.
 */
bool isPrime(int n) {
    if (n <= 1) return false;
    if (n <= 3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;

    for (int i = 5; i * i <= n; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0) {
            return false;
        }
    }
    return true;
}
```

### Exercise 2: Fibonacci Generator
**Problem:** Write a function that populates an array with the first $N$ terms of the Fibonacci sequence ($F_0 = 0, F_1 = 1, F_n = F_{n-1} + F_{n-2}$).
**Model Implementation:**
```c
#include <stddef.h>

/**
 * Computes and stores the first n Fibonacci numbers.
 *
 * Args:
 *   buffer (unsigned long long *): Output destination array.
 *   n (size_t): Count of terms to generate.
 *
 * Returns:
 *   void.
 */
void generateFibonacci(unsigned long long *buffer, size_t n) {
    if (buffer == NULL || n == 0) return;

    buffer[0] = 0;
    if (n > 1) {
        buffer[1] = 1;
        for (size_t i = 2; i < n; ++i) {
            buffer[i] = buffer[i - 1] + buffer[i - 2];
        }
    }
}
```

---

## Section 2: Arrays and Strings

### Exercise 3: String Palindrome Checker
**Problem:** Write a function that checks whether a string is a palindrome, ignoring casing and whitespace.
**Model Implementation:**
```c
#include <stdbool.h>
#include <ctype.h>
#include <string.h>

/**
 * Verifies if a given string is an alphanumeric palindrome.
 *
 * Args:
 *   str (const char *): Input string to inspect.
 *
 * Returns:
 *   bool: True if palindrome, false otherwise.
 */
bool isPalindrome(const char *str) {
    if (str == NULL) return false;

    int left = 0;
    int right = (int)strlen(str) - 1;

    while (left < right) {
        while (left < right && !isalnum((unsigned char)str[left])) left++;
        while (left < right && !isalnum((unsigned char)str[right])) right--;

        if (tolower((unsigned char)str[left]) != tolower((unsigned char)str[right])) {
            return false;
        }
        left++;
        right--;
    }
    return true;
}
```

---

## Section 3: Pointers and Memory

### Exercise 4: In-Place Integer Array Reversal
**Problem:** Implement an in-place array reversal using pointers without auxiliary arrays.
**Model Implementation:**
```c
#include <stddef.h>

/**
 * Reverses an array of integers using pointer iteration.
 *
 * Args:
 *   arr (int *): Starting pointer of array.
 *   len (size_t): Number of elements in array.
 *
 * Returns:
 *   void.
 */
void reverseIntegers(int *arr, size_t len) {
    if (arr == NULL || len <= 1) return;

    int *p_start = arr;
    int *p_end = arr + len - 1;

    while (p_start < p_end) {
        int temp = *p_start;
        *p_start = *p_end;
        *p_end = temp;
        p_start++;
        p_end--;
    }
}
```

---

## Section 4: Structures and File I/O

### Exercise 5: Text File Word Counter
**Problem:** Write a program that reads a text file and counts the total number of words separated by whitespace.
**Model Implementation:**
```c
#include <stdio.h>
#include <ctype.h>
#include <stdbool.h>

/**
 * Counts the number of whitespace-delimited words in a file.
 *
 * Args:
 *   filepath (const char *): Target file system path.
 *
 * Returns:
 *   long: Word count, or -1 if file failed to open.
 */
long countFileWords(const char *filepath) {
    if (filepath == NULL) return -1;

    FILE *fp = fopen(filepath, "r");
    if (fp == NULL) return -1;

    long word_count = 0;
    bool in_word = false;
    int ch;

    while ((ch = fgetc(fp)) != EOF) {
        if (isspace(ch)) {
            in_word = false;
        } else if (!in_word) {
            in_word = true;
            word_count++;
        }
    }

    fclose(fp);
    return word_count;
}
```

