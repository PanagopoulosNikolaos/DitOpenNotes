/*
 * -----------------------------------------------------------------------------
 *
 *  Exercise 15: Structures
 *
 *  Task:
 *  Write a C program that defines a structure to store information about a
 *  student (name, roll number, and marks). Then, create a student variable,
 *  assign values to its members, and display the information.
 *
 *  Instructions:
 *  1. Include the stdio.h and string.h libraries.
 *  2. Define a structure `Student` with the following members:
 *     - `name` (character array)
 *     - `rollNumber` (integer)
 *     - `marks` (float)
 *  3. In the main function, create a variable of type `struct Student`.
 *  4. Assign values to the members of the student variable.
 *  5. Print the student's information.
 *
 * -----------------------------------------------------------------------------
 */

#include <stdio.h>
#include <string.h>

// Define the Student structure
struct Student {
    char name[50];
    int rollNumber;
    float marks;
};

int main() {
    // Create a Student variable
    struct Student student1;

    // Assign values to the members of student1
    strcpy(student1.name, "John Doe");
    student1.rollNumber = 101;
    student1.marks = 85.5;

    // Display the student's information
    printf("Student Information:\n");
    printf("Name: %s\n", student1.name);
    printf("Roll Number: %d\n", student1.rollNumber);
    printf("Marks: %.2f\n", student1.marks);

    return 0;
}

