/*
 * -----------------------------------------------------------------------------
 *
 *  Exercise 16: Unions
 *
 *  Task:
 *  Write a C program to demonstrate the use of a union. Define a union that
 *  can hold an integer, a float, and a character array, and show how the
 *  memory is shared among the members.
 *
 *  Instructions:
 *  1. Include the stdio.h and string.h libraries.
 *  2. Define a union `Data` with an integer `i`, a float `f`, and a
 *     character array `str`.
 *  3. In the main function, create a `Data` variable.
 *  4. Assign a value to each member of the union one by one and print the
 *     value and the memory occupied by the union after each assignment.
 *  5. Observe how the values of other members are affected when one member
 *     is assigned a new value.
 *
 * -----------------------------------------------------------------------------
 */

#include <stdio.h>
#include <string.h>

// Define the Data union
union Data {
    int i;
    float f;
    char str[20];
};

int main() {
    // Create a Data union variable
    union Data data;

    // Demonstrate the use of the union
    printf("Memory size occupied by data: %zu\n\n", sizeof(data));

    // Assign an integer value
    data.i = 10;
    printf("data.i: %d\n", data.i);
    // The other members are now invalid

    // Assign a float value
    data.f = 220.5;
    printf("data.f: %.2f\n", data.f);
    // The other members are now invalid

    // Assign a string value
    strcpy(data.str, "C Programming");
    printf("data.str: %s\n", data.str);
    // The other members are now invalid

    // Accessing other members after assigning to str will lead to garbage values
    printf("\nAfter assigning a string, let's see the other members:\n");
    printf("data.i: %d (Garbage Value)\n", data.i);
    printf("data.f: %.2f (Garbage Value)\n", data.f);


    return 0;
}
