#include <stdio.h>
#include <string.h>

/*
 * Exercise 17: Writing Structures to a Text File (CSV format)
 *
 * Objective:
 * Define a structure 'Employee' with 'id', 'name', and 'salary'.
 * Create an array of 'Employee' structures, populate it,
 * and write the data to a text file ('employees.csv') in CSV format.
 */

// Define a structure named Employee
struct Employee {
    int id;
    char name[50];
    float salary;
};

int main() {
    // Declare an array of struct Employee
    struct Employee employees[] = {
        {1001, "Alice Johnson", 60000.00},
        {1002, "Bob Williams", 75000.50},
        {1003, "Charlie Brown", 50000.00}
    };
    int num_employees = sizeof(employees) / sizeof(struct Employee);

    // Open a file in write mode (text file)
    FILE *fp = fopen("employees.csv", "w");
    if (fp == NULL) {
        perror("Error opening file");
        return 1;
    }

    // Write CSV header
    fprintf(fp, "ID,Name,Salary\n");

    // Write employee data to the file
    for (int i = 0; i < num_employees; i++) {
        fprintf(fp, "%d,%s,%.2f\n", employees[i].id, employees[i].name, employees[i].salary);
    }

    // Close the file
    fclose(fp);

    printf("%d employee records written to employees.csv successfully.\n", num_employees);

    return 0;
}
