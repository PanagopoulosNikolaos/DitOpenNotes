#include <stdio.h>
#include <string.h>

/*
 * Exercise 13: Writing Multiple Structures to a File (Binary)
 *
 * Objective:
 * Define a structure 'Student' with 'id', 'name', and 'grade'.
 * Create an array of 'Student' structures, populate it with data for a few students,
 * and write the entire array to a binary file.
 */

// Define a structure named Student
struct Student {
    int id;
    char name[50];
    char grade;
};

int main() {
    // Declare an array of struct Student
    struct Student students[] = {
        {1, "Alice", 'A'},
        {2, "Bob", 'B'},
        {3, "Charlie", 'C'}
    };
    int num_students = sizeof(students) / sizeof(struct Student);

    // Open a file in binary write mode
    FILE *fp = fopen("students.dat", "wb");
    if (fp == NULL) {
        perror("Error opening file");
        return 1;
    }

    // Write the array of structures to the file
    fwrite(students, sizeof(struct Student), num_students, fp);

    // Close the file
    fclose(fp);

    printf("%d student records written to students.dat successfully.\n", num_students);

    return 0;
}
