#include <stdio.h>

/*
 * Exercise 1: Basic Structure Definition and Usage
 *
 * Objective:
 * Define a structure 'Point' with 'x' and 'y' coordinates.
 * Create a 'Point' variable, assign values (e.g., 10 and 20), and print them.
 */

// Define a structure named Point
struct Point {
    int x;
    int y;
};

int main() {
    // Declare a variable of type struct Point
    struct Point p1;

    // Assign values to the members of the structure
    p1.x = 10;
    p1.y = 20;

    // Print the values
    printf("Point coordinates: (%d, %d)\n", p1.x, p1.y);

    return 0;
}
