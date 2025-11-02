#include <stdio.h>

/*
 * Exercise 7: Structures with Bit Fields
 *
 * Objective:
 * Define a structure 'Permissions' using bit fields for read, write, and execute permissions.
 * Create a 'Permissions' variable, set some permissions, and print them.
 */

// Define a structure named Permissions using bit fields
struct Permissions {
    unsigned int read : 1;    // 1 bit for read permission
    unsigned int write : 1;   // 1 bit for write permission
    unsigned int execute : 1; // 1 bit for execute permission
};

int main() {
    // Declare a variable of type struct Permissions
    struct Permissions file_perms;

    // Set permissions
    file_perms.read = 1;
    file_perms.write = 0;
    file_perms.execute = 1;

    // Print permissions
    printf("File Permissions:\n");
    printf("Read: %d\n", file_perms.read);
    printf("Write: %d\n", file_perms.write);
    printf("Execute: %d\n", file_perms.execute);

    return 0;
}
