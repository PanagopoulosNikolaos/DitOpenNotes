# C Programming Complete Guide

## C Files

### Creating Files

**FILE Pointer**: Use `FILE*` pointer and `fopen()` function to work with files.

```c
FILE *fptr;
fptr = fopen("filename.txt", "w");  // Creates file if doesn't exist
fclose(fptr);  // Always close files
```

**Modes**:
- `w` - Write (creates file if doesn't exist)
- `a` - Append (adds to end)
- `r` - Read

**Absolute Path** (Windows):
```c
fptr = fopen("C:\\directoryname\\filename.txt", "w");
```

### Writing to Files

**Write mode** (`w`) - Overwrites existing content:
```c
FILE *fptr = fopen("filename.txt", "w");
fprintf(fptr, "Some text");
fclose(fptr);
```

**Append mode** (`a`) - Adds to end without deleting:
```c
FILE *fptr = fopen("filename.txt", "a");
fprintf(fptr, "\nNew line");
fclose(fptr);
```

### Reading Files

**Basic read**:
```c
FILE *fptr = fopen("filename.txt", "r");
char myString[100];
fgets(myString, 100, fptr);  // Reads first line
printf("%s", myString);
fclose(fptr);
```

**Read all lines**:
```c
FILE *fptr = fopen("filename.txt", "r");
char myString[100];
while(fgets(myString, 100, fptr)) {
    printf("%s", myString);
}
fclose(fptr);
```

**NULL check** (good practice):
```c
FILE *fptr = fopen("filename.txt", "r");
if(fptr == NULL) {
    printf("Not able to open the file.\n");
    return 1;
}
// Process file
fclose(fptr);
```

---

## C Structures

### Basic Structure

**Declaration and usage**:
```c
struct Car {
    char brand[30];
    char model[30];
    int year;
};

int main() {
    struct Car car1 = {"BMW", "X5", 1999};
    printf("%s %s %d\n", car1.brand, car1.model, car1.year);
    return 0;
}
```

**String assignment** - Use `strcpy()`:
```c
struct Car car1;
strcpy(car1.brand, "Toyota");
```

**Copy structures**:
```c
struct Car s1 = {13, 'B', "Some text"};
struct Car s2 = s1;  // Copy all values
```

### Nested Structures

**Structure inside structure**:
```c
struct Owner {
    char firstName[30];
    char lastName[30];
};

struct Car {
    char brand[30];
    int year;
    struct Owner owner;  // Nested
};

int main() {
    struct Owner person = {"John", "Doe"};
    struct Car car1 = {"Toyota", 2010, person};
    printf("Owner: %s %s\n", car1.owner.firstName, car1.owner.lastName);
    return 0;
}
```

### Structures with Pointers

**Pointer to struct** - Use `->` operator:
```c
struct Car car = {"Toyota", 2020};
struct Car *ptr = &car;

// Access with ->
printf("Brand: %s\n", ptr->brand);
printf("Year: %d\n", ptr->year);
```

**Pass to function**:
```c
void updateYear(struct Car *c) {
    c->year = 2025;  // Modifies original
}

int main() {
    struct Car myCar = {"Toyota", 2020};
    updateYear(&myCar);
    printf("Year: %d\n", myCar.year);  // 2025
    return 0;
}
```

**Why use pointers?**
- Avoid copying large data (faster, less memory)
- Modify original values in functions
- Dynamic allocation with `malloc()`

### Unions

**Shared memory** - All members share same space:
```c
union myUnion {
    int myNum;
    char myLetter;
    char myString[30];
};

int main() {
    union myUnion u1;
    u1.myLetter = 'A';  // Only last value is valid
    printf("%c\n", u1.myLetter);  // Prints 'A'
    return 0;
}
```

**Size** - Equals largest member:
```c
union myUnion {
    int myNum;        // 4 bytes
    char myString[36]; // 36 bytes
};
// Size = 36 bytes (vs struct would be 40 bytes)
```

**When to use**: Store different types in same location, only one value at a time, save memory.

### typedef

**Simplify declarations**:
```c
// Without typedef
struct Car car1 = {"BMW", 1999};

// With typedef
typedef struct {
    char brand[30];
    int year;
} Car;

Car car2 = {"Ford", 1969};  // Shorter!
```

**Multiple nested structs**:
```c
typedef struct {
    char firstName[20];
    char lastName[20];
} Owner;

typedef struct {
    char brand[20];
    int year;
    Owner owner;
} Car;

typedef struct {
    char name[30];
    Car featuredCar;
} Dealership;
```

### Struct Padding

**Memory alignment** - Compiler adds padding bytes:
```c
struct Example {
    char a;  // 1 byte
    int b;   // 4 bytes
    char c;  // 1 byte
};
// Expected: 6 bytes, Actual: 12 bytes (with padding)
```

**Memory layout**:
| Member | Bytes | Notes |
|--------|-------|-------|
| a | 1 | Stored first |
| padding | 3 | Align `b` to 4-byte boundary |
| b | 4 | Aligned |
| c | 1 | Stored |
| padding | 3 | Total size multiple of 4 |

**Reduce padding** - Order by size:
```c
struct Example {
    int b;   // 4 bytes
    char a;  // 1 byte
    char c;  // 1 byte
};
// Size = 8 bytes (less padding)
```

**Struct vs Union padding**:
- **Struct**: Padding between members
- **Union**: No padding between (share same memory), size = largest member

---

## C Enums

### Basic Enum

**Declaration**:
```c
enum Level {
    LOW,     // 0
    MEDIUM,  // 1
    HIGH     // 2
};

int main() {
    enum Level myVar = MEDIUM;
    printf("%d", myVar);  // Prints 1
    return 0;
}
```

### Custom Values

**Assign specific values**:
```c
enum Level {
    LOW = 25,
    MEDIUM = 50,
    HIGH = 75
};
```

**Sequential values**:
```c
enum Level {
    LOW = 5,
    MEDIUM,  // 6
    HIGH     // 7
};
```

### Enum in Switch

```c
enum Level {
    LOW = 1,
    MEDIUM,
    HIGH
};

int main() {
    enum Level myVar = MEDIUM;
    switch (myVar) {
        case 1: printf("Low Level"); break;
        case 2: printf("Medium level"); break;
        case 3: printf("High level"); break;
    }
    return 0;
}
```

### typedef with Enum

**Shorter syntax**:
```c
// Without typedef
enum Day {MON, TUE, WED, THU, FRI, SAT, SUN};
enum Day today = WED;

// With typedef
typedef enum {MON, TUE, WED, THU, FRI, SAT, SUN} Day;
Day today = WED;  // Cleaner!
```

**When to use**: Fixed constant values (days, months, colors, states).

---

## C Memory Management

### Understanding Memory

**Memory sizes**:
```c
int myInt;      // 4 bytes
float myFloat;  // 4 bytes
double myDouble; // 8 bytes
char myChar;    // 1 byte

printf("%zu\n", sizeof(myInt));  // Prints 4
```

**Why important**: Manage memory to optimize performance, prevent leaks, avoid crashes.

**Key points**:
- Manual memory management (allocate, reallocate, free)
- Use pointers to work with memory directly
- Be careful with pointers (can damage data)

---

## C Errors

### Compile-Time Errors

**Missing semicolon**:
```c
int x = 5  // Error: expected ';'
printf("%d", x);
```

**Undeclared variable**:
```c
printf("%d", myVar);  // Error: 'myVar' undeclared
```

**Type mismatch**:
```c
int x = "Hello";  // Error: initialization makes integer from pointer
```

### Runtime Errors

**Division by zero**:
```c
int x = 10;
int y = 0;
int result = x / y;  // Runtime error
```

**Array out of bounds**:
```c
int numbers[3] = {1, 2, 3};
printf("%d\n", numbers[8]);  // Undefined behavior
```

**Using freed memory**:
```c
int* ptr = malloc(sizeof(int));
*ptr = 10;
free(ptr);
printf("%d\n", *ptr);  // Undefined behavior
```

### Good Practices

- Always initialize variables
- Use meaningful names
- Keep code clean and indented
- Keep functions short
- Check loops/conditions
- Read error messages carefully

---

## C Debugging

### Print Debugging

**Track execution**:
```c
int x = 10, y = 0;
printf("Before division\n");
int z = x / y;  // Crashes here
printf("After division\n");  // Never runs
```

### Check Values

```c
int result = x - y;
printf("Result: %d\n", result);  // Check if expected
```

### Safe Checks

**Prevent crashes**:
```c
int x = 10, y = 0;
if (y != 0) {
    int z = x / y;
    printf("Result: %d\n", z);
} else {
    printf("Error: Division by zero!\n");
}
```

**Array bounds**:
```c
int numbers[3] = {10, 20, 30};
int index = 5;
if (index >= 0 && index < 3) {
    printf("Value = %d\n", numbers[index]);
} else {
    printf("Error: Index out of bounds!\n");
}
```

### Debugger Tools

Use IDE debuggers (Visual Studio, VS Code, Code::Blocks) for:
- Breakpoints (pause execution)
- Step through code line-by-line
- Watch variables change

---

## C NULL

### NULL Pointer

**Special value** - Points to nothing:
```c
FILE *fptr = fopen("nothing.txt", "r");
if (fptr == NULL) {
    printf("Could not open file.\n");
    return 1;
}
fclose(fptr);
```

**Memory allocation failure**:
```c
int *numbers = (int*) malloc(100000000000000 * sizeof(int));
if (numbers == NULL) {
    printf("Memory allocation failed.\n");
    return 1;
}
free(numbers);
numbers = NULL;  // Good practice after free
```

**Key points**:
- Always check pointers before use
- Prevents crashes from invalid memory access
- Functions return NULL on failure

---

## C Error Handling

### Return Values

**Check NULL**:
```c
FILE *fptr = fopen("nothing.txt", "r");
if (fptr == NULL) {
    printf("Error opening file.\n");
    return 1;
}
fclose(fptr);
```

### perror()

**Detailed error message**:
```c
FILE *f = fopen("nothing.txt", "r");
if (f == NULL) {
    perror("Error opening file");
    return 1;
}
fclose(f);
// Output: Error opening file: No such file or directory
```

### errno and strerror()

**Error codes**:
```c
#include <errno.h>
#include <string.h>

FILE *f = fopen("nothing.txt", "r");
if (f == NULL) {
    printf("Error: %s\n", strerror(errno));
    return 1;
}
```

**Common error codes**:
| Code | Meaning |
|------|---------|
| ENOENT | No such file or directory |
| EACCES | Permission denied |
| ENOMEM | Not enough memory |
| EINVAL | Invalid argument |

**Check specific error**:
```c
if (errno == ENOENT) {
    printf("The file was not found.\n");
}
```

### exit()

**Stop program immediately**:
```c
#include <stdlib.h>

FILE *f = fopen("nothing.txt", "r");
if (f == NULL) {
    printf("Failed to open file.\n");
    exit(EXIT_FAILURE);  // or exit(1)
}
```

**Exit codes**:
- 0 or `EXIT_SUCCESS` - Success
- 1 or `EXIT_FAILURE` - Error

---

## C Input Validation

### Validate Number Range

```c
int number;
do {
    printf("Choose a number between 1 and 5: ");
    scanf("%d", &number);
    while (getchar() != '\n');  // Clear buffer
} while (number < 1 || number > 5);
printf("You chose: %d\n", number);
```

### Validate Text Input

```c
#include <string.h>

char name[100];
do {
    printf("Enter your name: ");
    fgets(name, sizeof(name), stdin);
    name[strcspn(name, "\n")] = 0;  // Remove newline
} while (strlen(name) == 0);
printf("Hello, %s\n", name);
```

### Validate Integer Input

```c
int number;
char input[100];
printf("Enter a number: ");
while (fgets(input, sizeof(input), stdin)) {
    if (sscanf(input, "%d", &number) == 1) {
        break;  // Valid integer
    } else {
        printf("Invalid input. Try again: ");
    }
}
printf("You entered: %d\n", number);
```

---

## C Date and Time

### Current Time

```c
#include <time.h>

time_t currentTime;
time(&currentTime);
printf("Current time: %s", ctime(&currentTime));
```

### Break Down Time

**Access individual parts**:
```c
time_t now = time(NULL);
struct tm *t = localtime(&now);

printf("Year: %d\n", t->tm_year + 1900);  // Add 1900
printf("Month: %d\n", t->tm_mon + 1);     // 0-11, add 1
printf("Day: %d\n", t->tm_mday);
printf("Hour: %d\n", t->tm_hour);
printf("Minute: %d\n", t->tm_min);
printf("Second: %d\n", t->tm_sec);
```

### Format Date/Time

```c
time_t now = time(NULL);
struct tm *t = localtime(&now);
char buffer[100];

strftime(buffer, sizeof(buffer), "%d-%m-%Y %H:%M:%S", t);
printf("Formatted time: %s\n", buffer);
```

**When to use**: Display time, log events, timestamps, measure duration, seed random numbers.

---

## C Random Numbers

### Basic Random

```c
#include <stdlib.h>

int r = rand();
printf("%d\n", r);
// Note: Same sequence every run without seed
```

### Seeding

**Use current time**:
```c
#include <time.h>

srand(time(NULL));  // Seed once at start
printf("%d\n", rand());
printf("%d\n", rand());
```

### Random Range

**0 to 9**:
```c
int x = rand() % 10;
```

**1 to 6 (dice)**:
```c
int dice = (rand() % 6) + 1;
```

**Example - Roll two dice**:
```c
srand(time(NULL));
int dice1 = (rand() % 6) + 1;
int dice2 = (rand() % 6) + 1;
printf("You rolled %d and %d (total = %d)\n", dice1, dice2, dice1 + dice2);
```

---

## C Macros

### #include

**Include files**:
```c
#include <stdio.h>     // Standard library
#include "myfile.h"    // Your files
```

### #define

**Simple macro**:
```c
#define PI 3.14

int main() {
    printf("Value of PI: %.2f\n", PI);
    return 0;
}
```

**Macro with parameters**:
```c
#define SQUARE(x) ((x) * (x))

int main() {
    printf("Square of 4: %d\n", SQUARE(4));
    return 0;
}
```

### Conditional Compilation

**#ifdef / #ifndef**:
```c
#define DEBUG

int main() {
    #ifdef DEBUG
        printf("Debug mode is ON\n");
    #endif
    return 0;
}
```

---

## C Code Organization

### Header Files

**Why use**:
- Declare functions from other files
- Share variables, constants, macros
- Organize into logical modules

### Create Header File

**calc.h**:
```c
#ifndef CALC_H
#define CALC_H

int add(int x, int y);
int subtract(int x, int y);

#endif
```

**Include guard** (`#ifndef`, `#define`, `#endif`) prevents multiple inclusion.

### Function Definitions

**calc.c**:
```c
#include "calc.h"

int add(int x, int y) {
    return x + y;
}

int subtract(int x, int y) {
    return x - y;
}
```

### Use in Main

**main.c**:
```c
#include <stdio.h>
#include "calc.h"

int main() {
    printf("5 + 5 = %d\n", add(5, 5));
    printf("6 - 4 = %d\n", subtract(6, 4));
    return 0;
}
```

### Compile Multiple Files

```bash
gcc main.c calc.c -o program
```

---

## C Storage Classes

### auto

**Default for local variables**:
```c
int main() {
    auto int x = 50;  // Same as: int x = 50;
    return 0;
}
```

### static

**Keeps value between calls**:
```c
void count() {
    static int myNum = 0;  // Retains value
    myNum++;
    printf("num = %d\n", myNum);
}

int main() {
    count();  // num = 1
    count();  // num = 2
    count();  // num = 3
    return 0;
}
```

**File scope** - Not visible outside file (for global vars/functions).

### register

**Suggest CPU register** (mostly obsolete):
```c
register int counter = 0;
```

### extern

**Declare from another file**:

**main.c**:
```c
extern int shared;  // Declared, defined elsewhere

int main() {
    printf("shared = %d\n", shared);
    return 0;
}
```

**data.c**:
```c
int shared = 50;  // Definition
```

Compile: `gcc main.c data.c -o program`

---

## C Bitwise Operators

### Operators

| Operator | Name | Description |
|----------|------|-------------|
| & | AND | Both bits must be 1 |
| \| | OR | Either bit can be 1 |
| ^ | XOR | Only one bit is 1 |
| ~ | NOT | Flips all bits |
| << | Left Shift | Multiply by powers of 2 |
| >> | Right Shift | Divide by powers of 2 |

### Examples

**Setup**:
```c
int a = 6;  // 0110
int b = 3;  // 0011
```

**AND (&)**:
```c
int result = a & b;  // 2 (0010)
```

**OR (|)**:
```c
int result = a | b;  // 7 (0111)
```

**XOR (^)**:
```c
int result = a ^ b;  // 5 (0101)
```

**NOT (~)**:
```c
int result = ~a;  // -7 (inverts bits)
```

**Left Shift (<<)**:
```c
int result = 3 << 2;  // 12 (3 * 2^2)
```

**Right Shift (>>)**:
```c
int result = 12 >> 2;  // 3 (12 / 2^2)
```

### Flags Example

**Permission flags**:
```c
#define READ  1  // 0001
#define WRITE 2  // 0010
#define EXEC  4  // 0100

int permissions = READ | WRITE;  // Can read and write

if (permissions & READ) {
    printf("Read allowed\n");
}
if (permissions & WRITE) {
    printf("Write allowed\n");
}
if (permissions & EXEC) {
    printf("Execute allowed\n");
}
```

---

## C Fixed-Width Integers

### Types

**Include** `<stdint.h>`:

| Type | Size | Range | Printf |
|------|------|-------|--------|
| int8_t | 8 bits | -128 to 127 | %d |
| uint8_t | 8 bits | 0 to 255 | %u |
| int16_t | 16 bits | -32,768 to 32,767 | %d |
| uint16_t | 16 bits | 0 to 65,535 | %u |
| int32_t | 32 bits | -2,147,483,648 to 2,147,483,647 | %d |
| uint32_t | 32 bits | 0 to 4,294,967,295 | %u |
| int64_t | 64 bits | -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 | %lld |
| uint64_t | 64 bits | 0 to 18,446,744,073,709,551,615 | %llu |

**u** = unsigned (non-negative only, double max positive value)

### Usage

```c
#include <stdint.h>

int8_t a = 100;
int16_t b = 30000;
int32_t c = 2000000;
int64_t d = 9000000000;

printf("%d\n", a);
printf("%d\n", b);
printf("%d\n", c);
printf("%lld\n", d);
```

### When to Use

**Essential for**:
- Embedded systems
- File formats (exact sizes matter)
- Network communication (consistency across machines)

**Example** - Battery level:
```c
uint8_t battery = 87;  // 0-100, saves memory
printf("Battery level is %u out of 100\n", battery);
```

---

## C Projects

### Why Build Projects

- Understand program structure
- Practice combining concepts
- Improve debugging skills
- Prepare for interviews

### Small Projects

**Hello Name**:
- Ask name and age
- Print: "Hi <name>! You will turn <age+1> next year."

**Shopping List**:
- Store 5 items in array
- Print list
- Search for items

### Medium Projects

- Guess a Number Game
- Calculate Student Average
- Simple Calculator

### Advanced Projects

- Address Book (structs + files)
- To-Do List (file handling)
- Quiz Game (functions + arrays)

### Example - Student Average

```c
char gradeFunction(double avg) {
    if (avg >= 90) return 'A';
    else if (avg >= 80) return 'B';
    else if (avg >= 70) return 'C';
    else if (avg >= 60) return 'D';
    else return 'F';
}

int main(void) {
    int count;
    double sum = 0, grade;
    
    printf("How many grades (1 to 5)? ");
    scanf("%d", &count);
    
    if (count < 1 || count > 5) {
        printf("Invalid number.\n");
        return 1;
    }
    
    for (int i = 1; i <= count; i++) {
        printf("Enter grade %d: ", i);
        scanf("%lf", &grade);
        sum += grade;
    }
    
    double avg = sum / count;
    printf("Average: %.2f\n", avg);
    printf("Letter grade: %c\n", gradeFunction(avg));
    
    return 0;
}
```

---

## C Keywords

| Keyword | Description |
|---------|-------------|
| break | Break out of loop/switch |
| case | Mark block in switch |
| char | Single character type |
| const | Unchangeable variable |
| continue | Next loop iteration |
| default | Default switch block |
| do | Do-while loop |
| double | 64-bit float |
| else | Conditional else |
| enum | Enumerated type |
| float | 32-bit float |
| for | For loop |
| goto | Jump to label |
| if | Conditional if |
| int | Integer type |
| long | At least 32-bit int |
| return | Return from function |
| short | 16-bit int |
| signed | Positive/negative values |
| sizeof | Memory size operator |
| static | Persistent variable |
| struct | Structure definition |
| switch | Multi-case selection |
| typedef | Custom type alias |
| unsigned | Positive values only |
| void | No return/generic pointer |
| while | While loop |

---

## Quick Reference - Standard Libraries

### <stdio.h>
File I/O, input/output: `printf()`, `scanf()`, `fopen()`, `fclose()`, `fprintf()`, `fgets()`, `perror()`

### <stdlib.h>
Memory, utilities: `malloc()`, `free()`, `rand()`, `srand()`, `exit()`, `EXIT_SUCCESS`, `EXIT_FAILURE`

### <string.h>
String operations: `strcpy()`, `strlen()`, `strcmp()`, `strcat()`, `strcspn()`, `strerror()`

### <math.h>
Mathematical functions: `sqrt()`, `pow()`, `sin()`, `cos()`, `abs()`

### <ctype.h>
Character handling: `isalpha()`, `isdigit()`, `tolower()`, `toupper()`

### <time.h>
Date/time: `time()`, `localtime()`, `ctime()`, `strftime()`, `struct tm`

### <errno.h>
Error codes: `errno`, `ENOENT`, `EACCES`, `ENOMEM`, `EINVAL`

### <stdint.h>
Fixed-width integers: `int8_t`, `uint8_t`, `int16_t`, `uint16_t`, `int32_t`, `uint32_t`, `int64_t`, `uint64_t`

---

## Best Practices Summary

1. **Always initialize variables**
2. **Check for NULL** after file operations and memory allocation
3. **Close files** with `fclose()`
4. **Free memory** with `free()` after `malloc()`
5. **Use meaningful names** for variables and functions
6. **Validate user input** before processing
7. **Handle errors** with proper checks and messages
8. **Keep functions short** and focused
9. **Use comments** to explain complex logic
10. **Test frequently** during development
11. **Use `const`** for values that shouldn't change
12. **Organize code** into multiple files for large projects
13. **Use typedef** to simplify complex types
14. **Check array bounds** before access
15. **Seed random generator** once at program start

---

**End of Guide**