# Complete C Programming Guide

## 1. Getting Started with C

### Installation
- **Text editor**: Notepad or any code editor
- **Compiler**: GCC (GNU Compiler Collection)
- **IDE**: Code::Blocks (recommended for beginners)

### First Program
```c
#include <stdio.h>

int main() {
    printf("Hello World!");
    return 0;
}
```

**Compilation**: Save as `program.c`, compile with `gcc program.c -o program`, run with `./program`

---

## 2. Syntax

### Structure
```c
#include <stdio.h>    // Header file for input/output
int main() {          // Main function
    printf("Hello World!");  // Print statement
    return 0;         // Return value
}                     // Closing bracket
```

**Key Points**:
- `#include <stdio.h>`: Imports standard I/O library
- `main()`: Entry point of program
- Statements end with semicolon `;`
- Code blocks use curly braces `{}`

---

## 3. Output

### printf() Function
```c
printf("Hello World!");           // Basic output
printf("Hello\nWorld!");          // New line with \n
printf("Line 1\n");
printf("Line 2\n");
```

**Multiple printf()**:
```c
printf("Hello ");
printf("World!");  // Outputs: Hello World! (no automatic newline)
```

---

## 4. Comments

### Single-line Comments
```c
// This is a single-line comment
printf("Hello World!");
```

### Multi-line Comments
```c
/* This is a 
   multi-line comment 
   spanning multiple lines */
printf("Hello World!");
```

---

## 5. Variables

### Declaration and Assignment
```c
int myNum = 15;              // Integer
float myFloat = 5.99;        // Float
char myLetter = 'D';         // Character

// Declare then assign
int x;
x = 10;
```

### Format Specifiers for Output
```c
int age = 25;
float price = 19.99;
char grade = 'A';

printf("%d\n", age);         // %d for int
printf("%f\n", price);       // %f for float
printf("%c\n", grade);       // %c for char
```

---

## 6. Data Types

### Basic Data Types

| Type | Size | Description | Format Specifier |
|------|------|-------------|------------------|
| `int` | 2-4 bytes | Whole numbers | `%d` or `%i` |
| `float` | 4 bytes | Decimal numbers (6-7 digits) | `%f` |
| `double` | 8 bytes | Decimal numbers (15 digits) | `%lf` |
| `char` | 1 byte | Single character | `%c` |

### Example
```c
int myNum = 5;
float myFloat = 5.99;
double myDouble = 9.98;
char myLetter = 'D';

printf("%d\n", myNum);       // 5
printf("%f\n", myFloat);     // 5.990000
printf("%lf\n", myDouble);   // 9.980000
printf("%c\n", myLetter);    // D
```

---

## 7. Constants

### Using const Keyword
```c
const int MINUTES_PER_HOUR = 60;
const int MONTHS_IN_YEAR = 12;

// Cannot be changed
// MINUTES_PER_HOUR = 70;  // ERROR!
```

**Best Practice**: Use UPPERCASE for constants

---

## 8. Operators

### Arithmetic Operators
```c
int x = 100 + 50;     // Addition: 150
int y = 100 - 50;     // Subtraction: 50
int z = 100 * 50;     // Multiplication: 5000
int a = 100 / 50;     // Division: 2
int b = 100 % 50;     // Modulus (remainder): 0

int n = 10;
n++;                  // Increment: n = 11
n--;                  // Decrement: n = 10
```

### Assignment Operators
```c
int x = 10;
x += 5;              // x = x + 5 = 15
x -= 3;              // x = x - 3 = 12
x *= 2;              // x = x * 2 = 24
x /= 4;              // x = x / 4 = 6
x %= 4;              // x = x % 4 = 2
```

### Comparison Operators
```c
int x = 5;
int y = 3;

x == y;              // Equal to: 0 (false)
x != y;              // Not equal: 1 (true)
x > y;               // Greater than: 1 (true)
x < y;               // Less than: 0 (false)
x >= y;              // Greater or equal: 1 (true)
x <= y;              // Less or equal: 0 (false)
```

### Logical Operators
```c
int x = 5;
int y = 3;

(x > 3 && y < 10);   // AND: 1 (both true)
(x > 3 || y > 10);   // OR: 1 (one true)
!(x == y);           // NOT: 1 (reverse)
```

---

## 9. Booleans

### Using Booleans
```c
#include <stdbool.h>  // Required for bool type

bool isProgrammingFun = true;
bool isFishTasty = false;

printf("%d", isProgrammingFun);  // 1 (true)
printf("%d", isFishTasty);       // 0 (false)
```

### Comparing Values
```c
printf("%d", 10 > 9);    // 1 (true)
printf("%d", 10 == 10);  // 1 (true)
printf("%d", 10 < 9);    // 0 (false)
```

---

## 10. If...Else Statements

### if Statement
```c
if (20 > 18) {
    printf("20 is greater than 18");
}
```

### if...else Statement
```c
int time = 20;
if (time < 18) {
    printf("Good day.");
} else {
    printf("Good evening.");
}
```

### if...else if...else
```c
int time = 22;
if (time < 10) {
    printf("Good morning.");
} else if (time < 20) {
    printf("Good day.");
} else {
    printf("Good evening.");
}
```

### Ternary Operator
```c
int time = 20;
(time < 18) ? printf("Good day.") : printf("Good evening.");
```

---

## 11. Switch Statement

### Syntax
```c
int day = 4;

switch (day) {
    case 1:
        printf("Monday");
        break;
    case 2:
        printf("Tuesday");
        break;
    case 3:
        printf("Wednesday");
        break;
    case 4:
        printf("Thursday");
        break;
    case 5:
        printf("Friday");
        break;
    case 6:
        printf("Saturday");
        break;
    case 7:
        printf("Sunday");
        break;
    default:
        printf("Invalid day");
}
// Outputs: Thursday
```

**Important**: Always use `break` to prevent fall-through. `default` is optional but recommended.

---

## 12. While Loop

### Basic While Loop
```c
int i = 0;
while (i < 5) {
    printf("%d\n", i);
    i++;
}
// Outputs: 0 1 2 3 4
```

### Countdown Example
```c
int countdown = 3;
while (countdown > 0) {
    printf("%d\n", countdown);
    countdown--;
}
printf("Happy New Year!!\n");
// Outputs: 3 2 1 Happy New Year!!
```

### Do-While Loop
```c
int i = 0;
do {
    printf("%d\n", i);
    i++;
} while (i < 5);
```

---

## 13. For Loop

### Basic For Loop
```c
for (int i = 0; i < 5; i++) {
    printf("%d\n", i);
}
// Outputs: 0 1 2 3 4
```

### Even Numbers
```c
for (int i = 0; i <= 10; i += 2) {
    printf("%d\n", i);
}
// Outputs: 0 2 4 6 8 10
```

### Sum of Numbers
```c
int sum = 0;
for (int i = 1; i <= 5; i++) {
    sum += i;
}
printf("Sum: %d", sum);  // Sum: 15
```

### Countdown
```c
for (int i = 5; i > 0; i--) {
    printf("%d\n", i);
}
// Outputs: 5 4 3 2 1
```

---

## 14. Break and Continue

### Break Statement
```c
for (int i = 0; i < 10; i++) {
    if (i == 4) {
        break;  // Exit loop when i is 4
    }
    printf("%d\n", i);
}
// Outputs: 0 1 2 3
```

### Continue Statement
```c
for (int i = 0; i < 10; i++) {
    if (i == 4) {
        continue;  // Skip iteration when i is 4
    }
    printf("%d\n", i);
}
// Outputs: 0 1 2 3 5 6 7 8 9
```

### Combined Example
```c
for (int i = 0; i < 6; i++) {
    if (i == 2) continue;  // Skip 2
    if (i == 4) break;     // Stop at 4
    printf("%d\n", i);
}
// Outputs: 0 1 3
```

---

## 15. Arrays

### Declaration and Initialization
```c
int myNumbers[] = {25, 50, 75, 100};
```

### Accessing Elements
```c
int myNumbers[] = {25, 50, 75, 100};
printf("%d", myNumbers[0]);  // 25 (first element)
```

### Modifying Elements
```c
myNumbers[0] = 33;
printf("%d", myNumbers[0]);  // 33
```

### Set Array Size
```c
int myNumbers[4];
myNumbers[0] = 25;
myNumbers[1] = 50;
myNumbers[2] = 75;
myNumbers[3] = 100;
```

### Loop Through Array
```c
int myNumbers[] = {25, 50, 75, 100};
int length = sizeof(myNumbers) / sizeof(myNumbers[0]);

for (int i = 0; i < length; i++) {
    printf("%d\n", myNumbers[i]);
}
```

---

## 16. Strings

### String Declaration
```c
char greetings[] = "Hello World!";
printf("%s", greetings);  // Hello World!
```

### Access String Characters
```c
char greetings[] = "Hello World!";
printf("%c", greetings[0]);  // H (first character)
```

### Modify Strings
```c
char greetings[] = "Hello World!";
greetings[0] = 'J';
printf("%s", greetings);  // Jello World!
```

### Loop Through String
```c
char carName[] = "Volvo";
int length = sizeof(carName) / sizeof(carName[0]);

for (int i = 0; i < length; i++) {
    printf("%c\n", carName[i]);
}
```

### Character Array Method
```c
char greetings[] = {'H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', '!', '\0'};
printf("%s", greetings);  // Hello World!
```

**Note**: `\0` is the null terminator, required when creating strings this way.

---

## 17. User Input

### scanf() Function
```c
int myNum;
printf("Type a number: ");
scanf("%d", &myNum);
printf("Your number is: %d", myNum);
```

### Multiple Inputs
```c
int myNum;
char myChar;

printf("Type a number AND a character: ");
scanf("%d %c", &myNum, &myChar);

printf("Number: %d\n", myNum);
printf("Character: %c\n", myChar);
```

### String Input
```c
// Single word
char firstName[30];
printf("Enter your first name: ");
scanf("%s", firstName);
printf("Hello %s", firstName);

// Full line (multiple words)
char fullName[30];
printf("Type your full name: ");
fgets(fullName, sizeof(fullName), stdin);
printf("Hello %s", fullName);
```

**Important**: Use `fgets()` for multi-word strings, `scanf()` for single words.

---

## 18. Memory Address

### Getting Memory Address
```c
int myAge = 43;
printf("%p", &myAge);  // Outputs: 0x7ffe5367e044 (example)
```

**Key Points**:
- `&` is the reference operator
- Memory addresses are in hexadecimal format
- Memory addresses vary based on where variable is stored

---

## 19. Pointers

### Creating Pointers
```c
int myAge = 43;
int* ptr = &myAge;  // Pointer to myAge

printf("%d\n", myAge);   // 43 (value)
printf("%p\n", &myAge);  // 0x7ffe5367e044 (address)
printf("%p\n", ptr);     // 0x7ffe5367e044 (address via pointer)
```

### Dereference
```c
int myAge = 43;
int* ptr = &myAge;

printf("%p\n", ptr);   // Memory address
printf("%d\n", *ptr);  // 43 (value via pointer)
```

**Pointer Syntax**:
```c
int* ptr;  // Method 1
int *ptr;  // Method 2 (both valid)
```

---

## 20. Functions

### Basic Function
```c
void myFunction() {
    printf("I just got executed!");
}

int main() {
    myFunction();  // Call the function
    return 0;
}
```

### Function with Return Value
```c
int add(int x, int y) {
    return x + y;
}

int main() {
    int result = add(5, 3);
    printf("Result: %d", result);  // 8
    return 0;
}
```

---

## 21. Function Parameters

### Single Parameter
```c
void greet(char name[]) {
    printf("Hello %s\n", name);
}

int main() {
    greet("Alice");
    greet("Bob");
    return 0;
}
```

### Multiple Parameters
```c
void printInfo(char name[], int age) {
    printf("Hello %s. You are %d years old.\n", name, age);
}

int main() {
    printInfo("Alice", 25);
    printInfo("Bob", 30);
    return 0;
}
```

### Arrays as Parameters
```c
void printArray(int nums[5]) {
    for (int i = 0; i < 5; i++) {
        printf("%d\n", nums[i]);
    }
}

int main() {
    int myNumbers[5] = {10, 20, 30, 40, 50};
    printArray(myNumbers);
    return 0;
}
```

---

## 22. Variable Scope

### Local Scope
```c
void myFunction() {
    int x = 5;  // Local variable
    printf("%d", x);
}

int main() {
    myFunction();
    // printf("%d", x);  // ERROR: x not accessible here
    return 0;
}
```

### Global Scope
```c
int x = 5;  // Global variable

void myFunction() {
    printf("%d\n", x);  // Can access global x
}

int main() {
    myFunction();
    printf("%d\n", x);  // Can also access global x
    return 0;
}
```

### Local vs Global with Same Name
```c
int x = 5;  // Global

void myFunction() {
    int x = 22;  // Local (shadows global)
    printf("%d\n", x);  // 22
}

int main() {
    myFunction();
    printf("%d\n", x);  // 5
    return 0;
}
```

---

## 23. Function Declaration

### Separate Declaration and Definition
```c
// Function declaration
int add(int x, int y);

int main() {
    int result = add(5, 3);
    printf("Result: %d", result);
    return 0;
}

// Function definition
int add(int x, int y) {
    return x + y;
}
```

**Benefits**: Better code organization and readability

---

## 24. Math Functions

### Common Math Functions
```c
#include <stdio.h>
#include <math.h>

int main() {
    printf("%f\n", sqrt(16));       // 4.000000 (square root)
    printf("%f\n", pow(4, 3));      // 64.000000 (4^3)
    printf("%f\n", ceil(1.4));      // 2.000000 (round up)
    printf("%f\n", floor(1.4));     // 1.000000 (round down)
    return 0;
}
```

---

## 25. Inline Functions

### Inline Function Declaration
```c
inline int square(int x) {
    return x * x;
}

int main() {
    printf("%d", square(5));  // 25
    return 0;
}
```

**When to Use**:
- Small, frequently called functions
- Simple operations
- Avoid for large or recursive functions

---

## 26. Recursion

### Sum with Recursion
```c
int sum(int k) {
    if (k > 0) {
        return k + sum(k - 1);
    } else {
        return 0;
    }
}

int main() {
    int result = sum(10);
    printf("%d", result);  // 55
    return 0;
}
```

### Factorial with Recursion
```c
int factorial(int n) {
    if (n > 1) {
        return n * factorial(n - 1);
    } else {
        return 1;
    }
}

int main() {
    printf("Factorial of 5: %d", factorial(5));  // 120
    return 0;
}
```

### Countdown Example
```c
void countdown(int n) {
    if (n > 0) {
        printf("%d ", n);
        countdown(n - 1);
    }
}

int main() {
    countdown(5);  // 5 4 3 2 1
    return 0;
}
```

---

## 27. Function Pointers

### Basic Function Pointer
```c
int add(int a, int b) {
    return a + b;
}

int main() {
    int (*ptr)(int, int) = add;  // Function pointer
    int result = ptr(5, 3);
    printf("Result: %d", result);  // 8
    return 0;
}
```

### Function as Callback
```c
void greetMorning() {
    printf("Good morning!\n");
}

void greetEvening() {
    printf("Good evening!\n");
}

void greet(void (*func)()) {
    func();  // Call the function passed as parameter
}

int main() {
    greet(greetMorning);
    greet(greetEvening);
    return 0;
}
```

### Function Pointer Array
```c
void add() { printf("Add\n"); }
void subtract() { printf("Subtract\n"); }
void multiply() { printf("Multiply\n"); }

int main() {
    void (*operations[3])() = {add, subtract, multiply};
    
    for (int i = 0; i < 3; i++) {
        operations[i]();
    }
    return 0;
}
```

### Calculator with Function Pointers
```c
void add(int a, int b) { printf("Result: %d\n", a + b); }
void subtract(int a, int b) { printf("Result: %d\n", a - b); }
void multiply(int a, int b) { printf("Result: %d\n", a * b); }

int main() {
    int choice, x = 10, y = 5;
    void (*operations[3])(int, int) = {add, subtract, multiply};
    
    printf("0: Add, 1: Subtract, 2: Multiply\n");
    scanf("%d", &choice);
    
    if (choice >= 0 && choice < 3) {
        operations[choice](x, y);
    } else {
        printf("Invalid choice!\n");
    }
    return 0;
}
```

---

## Quick Reference

### Common Format Specifiers
- `%d` or `%i` - int
- `%f` - float
- `%lf` - double
- `%c` - char
- `%s` - string
- `%p` - pointer address

### Escape Sequences
- `\n` - newline
- `\t` - tab
- `\\` - backslash
- `\"` - double quote
- `\'` - single quote

### Compilation Commands
```bash
gcc program.c -o program     # Compile
./program                    # Run (Linux/Mac)
program.exe                  # Run (Windows)
gcc program.c -o program -lm # Compile with math library
```

---

## Best Practices

1. **Use meaningful variable names**: `age` instead of `a`
2. **Use constants for fixed values**: `const int MAX = 100;`
3. **Comment your code**: Explain complex logic
4. **Use local variables**: Minimize global variable usage
5. **Check array bounds**: Prevent buffer overflows
6. **Initialize variables**: Avoid undefined behavior
7. **Use proper indentation**: Makes code readable
8. **Break down complex functions**: Keep functions small and focused
9. **Always include return statements**: In non-void functions
10. **Free allocated memory**: Prevent memory leaks

---

**End of Guide**