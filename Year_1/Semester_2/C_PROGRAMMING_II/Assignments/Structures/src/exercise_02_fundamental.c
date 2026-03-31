#include <stdio.h>
#include <string.h> // Required for strcpy

/*
 * Exercise 2: Structure with Typedef
 *
 * Objective:
 * Define a structure 'Book' with 'title', 'author', and 'year' using 'typedef'.
 * Create a 'Book' variable, assign values, and print them.
 */

// Define a structure named Book using typedef
typedef struct {
    char title[100];
    char author[100];
    int year;
} Book;

int main() {
    // Declare a variable of type Book
    Book b1;

    // Assign values to the members of the structure
    strcpy(b1.title, "The C Programming Language");
    strcpy(b1.author, "Brian Kernighan");
    b1.year = 1978;

    // Print the values
    printf("Book Title: %s\n", b1.title);
    printf("Book Author: %s\n", b1.author);
    printf("Publication Year: %d\n", b1.year);

    return 0;
}
