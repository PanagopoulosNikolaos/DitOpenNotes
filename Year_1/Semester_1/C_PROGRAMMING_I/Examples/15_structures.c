/*
 * Exercise 15: Structures
 */

#include <stdio.h>
#include <string.h>

/**
 * Represents academic student records.
 */
struct Student {
    char name[50];
    int roll_number;
    float marks;
};

/**
 * Instantiates and displays student record structure.
 *
 * Args:
 *     None.
 *
 * Returns:
 *     int: Exit status code 0 on successful execution.
 */
int main(void) {
    struct Student student1;

    // Populates fields of structure instance.
    strncpy(student1.name, "John Doe", sizeof(student1.name) - 1);
    student1.name[sizeof(student1.name) - 1] = '\0';
    student1.roll_number = 101;
    student1.marks = 92.5f;

    printf("Student Name: %s\n", student1.name);
    printf("Roll Number: %d\n", student1.roll_number);
    printf("Marks: %.2f\n", student1.marks);

    return 0;
}
