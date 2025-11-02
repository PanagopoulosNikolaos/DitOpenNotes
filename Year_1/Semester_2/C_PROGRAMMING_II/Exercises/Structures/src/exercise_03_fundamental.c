#include <stdio.h>
#include <string.h>

/*
 * Exercise 3: Array of Structures
 *
 * Objective:
 * Define a structure 'Student' with 'name', 'id', and 'gpa'.
 * Create an array of 'Student' structures, populate it with data for a few students,
 * and print their information.
 */

// Define a structure named Student
struct Student {
    char name[50];
    int id;
    float gpa;
};

int main() {
    // Declare an array of struct Student
    struct Student students[3];

    // Populate the array with student data
    strcpy(students[0].name, "Alice");
    students[0].id = 101;
    students[0].gpa = 3.8;

    strcpy(students[1].name, "Bob");
    students[1].id = 102;
    students[1].gpa = 3.5;

    strcpy(students[2].name, "Charlie");
    students[2].id = 103;
    students[2].gpa = 3.9;

    // Print student information
    printf("Student Information:\n");
    for (int i = 0; i < 3; i++) {
        printf("Name: %s, ID: %d, GPA: %.2f\n", students[i].name, students[i].id, students[i].gpa);
    }

    return 0;
}
