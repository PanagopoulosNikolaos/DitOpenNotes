# MIPS Assembly 
## Exercise 2


1. Describe the "programming block" (set of instructions) required for sending messages to the console (for user notification)

2. Describe the "programming block" required for data input from the keyboard (user)

3. Once data is retrieved from the keyboard, where is it stored?

4. When we want to display data, where should it be placed?

### Answers

1. **Print message:**
    System call code `4` is used in register `$v0` and the message address in `$a0`.
    ```mips
    li $v0, 4       # Code for print string
    la $a0, label   # Load message address
    syscall         # Execute
    ```

2. **Data input:**
    For integers, code `5` is used in `$v0`.
    ```mips
    li $v0, 5       # Code for read integer
    syscall         # Execute
    ```

3. **Data storage:**
    *   **Integers** are stored in register `$v0`.
    *   **Strings** are stored in memory, at the address previously specified in register `$a0`.

4. **Data placement for display:**
    Data must be transferred to register **`$a0`** (for integers/strings) or **`$f12`** (for floating-point numbers) before calling `syscall`.

---

## Calculator Program Documentation (MIPS Calculator)

### Description
The program implements a calculator in MIPS assembly language, designed to run on the QtSpim simulator. It allows the user to perform basic arithmetic operations and features a termination mechanism based on the student's Registration Number (AM).

### Functions
1.  **Data Input**: At startup, the program asks for the user's full name, registration number (AM), and current semester.
2.  **Program Flow**: The user first enters two numbers and then selects the desired operation.
3.  **Arithmetic Operations**:
    *   **Addition (1)**: Calculates a + b.
    *   **Subtraction (2)**: Calculates a - b.
    *   **Multiplication (3)**: Calculates a * b.
    *   **Division (4)**: Calculates a / b (with division-by-zero check).
    *   **Square (5)**: Calculates the square of the first number (a^2).

### Termination Mechanism
The program runs continuously (loop) until the user enters their **AM** in either of the two number input fields.

### Technical Details
*   **Registers**:
    *   `$s0`: Stores the AM for termination check.
    *   `$s1, $s2`: Stores the two input numbers.
    *   `$t0`: Operation selection.
*   **Structure**: The program uses subroutines (such as `print_binary_header`) to optimize result printing and reduce code size.
*   **Safety**: A check is performed before division to prevent system errors in case of a zero divisor.

![alt text](image.png)

### Automated execution/tests
```shell
chmod u+x run_tests.sh
./run_tests.sh
```
```shell
Running MIPS Calculator Tests...
SPIM Version 8.0 of January 8, 2010
Copyright 1990-2010, James R. Larus.
All Rights Reserved.
See the file README for a full copyright notice.
Loaded: /usr/lib/spim/exceptions.s
--- MIPS Calculator ---
Enter your full name: Enter your student registration number (AM): Enter your current semester: 
Enter the first number: Enter the second number: Choose operation (1: Add, 2: Sub, 3: Mul, 4: Div, 5: Square): Addition: 10 + 5 = 15
Enter the first number: Enter the second number: Choose operation (1: Add, 2: Sub, 3: Mul, 4: Div, 5: Square): Subtraction: 20 - 10 = 10
Enter the first number: Enter the second number: Choose operation (1: Add, 2: Sub, 3: Mul, 4: Div, 5: Square): Multiplication: 5 * 4 = 20
Enter the first number: Enter the second number: Choose operation (1: Add, 2: Sub, 3: Mul, 4: Div, 5: Square): Division: 100 / 10 = 10
Enter the first number: Enter the second number: Choose operation (1: Add, 2: Sub, 3: Mul, 4: Div, 5: Square): Square: 8^2 = 64
Enter the first number: 
AM detected. Terminating program...
Tests completed and temporary files cleaned up.
```

### Manual execution
```shell
spim -file calculator_spec.asm
```

```shell
--- MIPS Calculator ---
Enter your full name: Nikolaos Panagopoulos
Enter your student registration number (AM): 3323
Enter your current semester: 3

Enter the first number: 33
Enter the second number: 2
Choose operation (1: Add, 2: Sub, 3: Mul, 4: Div, 5: Square): 1
Addition: 33 + 2 = 35

Enter the first number: 44
Enter the second number: 1
Choose operation (1: Add, 2: Sub, 3: Mul, 4: Div, 5: Square): 2
Subtraction: 44 - 1 = 43

Enter the first number: 10
Enter the second number: 5
Choose operation (1: Add, 2: Sub, 3: Mul, 4: Div, 5: Square): 3
Multiplication: 10 * 5 = 50

Enter the first number: 40
Enter the second number: 8
Choose operation (1: Add, 2: Sub, 3: Mul, 4: Div, 5: Square): 4
Division: 40 / 8 = 5

Enter the first number: 8
Enter the second number: 0
Choose operation (1: Add, 2: Sub, 3: Mul, 4: Div, 5: Square): 5
Square: 8^2 = 64

Enter the first number: 3323
AM detected. Terminating program...
```
