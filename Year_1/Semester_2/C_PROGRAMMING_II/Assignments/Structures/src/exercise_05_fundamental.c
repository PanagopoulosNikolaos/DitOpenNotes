#include <stdio.h>

/*
 * Exercise 5: Pointers to Structures
 *
 * Objective:
 * Define a structure 'Rectangle' with 'length' and 'width'.
 * Create a 'Rectangle' variable and a pointer to it.
 * Use the pointer to access and modify the structure members, then print the values.
 */

// Define a structure named Rectangle
struct Rectangle {
    int length;
    int width;
};

int main() {
    // Declare a variable of type struct Rectangle
    struct Rectangle rect1 = {10, 5};

    // Declare a pointer to struct Rectangle
    struct Rectangle *ptr_rect;

    // Assign the address of rect1 to the pointer
    ptr_rect = &rect1;

    // Access and print members using the pointer
    printf("Initial Rectangle: Length = %d, Width = %d\n", ptr_rect->length, ptr_rect->width);

    // Modify members using the pointer
    ptr_rect->length = 20;
    ptr_rect->width = 10;

    // Print modified members
    printf("Modified Rectangle: Length = %d, Width = %d\n", rect1.length, rect1.width);

    return 0;
}
