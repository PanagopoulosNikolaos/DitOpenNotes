#include <stdio.h>
#include <string.h>

/*
 * Exercise 4: Nested Structures
 *
 * Objective:
 * Define a structure 'Address' with 'street', 'city', and 'zip_code'.
 * Then define a structure 'Person' with 'name', 'age', and an 'Address' structure as a member.
 * Create a 'Person' variable, assign values including the nested address, and print them.
 */

// Define Address structure
struct Address {
    char street[50];
    char city[50];
    char zip_code[10];
};

// Define Person structure with nested Address
struct Person {
    char name[50];
    int age;
    struct Address address; // Nested structure
};

int main() {
    // Declare a variable of type struct Person
    struct Person p1;

    // Assign values to the members of the Person structure
    strcpy(p1.name, "John Doe");
    p1.age = 30;

    // Assign values to the members of the nested Address structure
    strcpy(p1.address.street, "123 Main St");
    strcpy(p1.address.city, "Anytown");
    strcpy(p1.address.zip_code, "12345");

    struct Person p2;
   
    strcpy(p2.name, "Jane Smith");
    p2.age = 28;
    strcpy(p2.address.street, "456 Elm St");
    strcpy(p2.address.city, "Othertown");
    strcpy(p2.address.zip_code, "67890");

    

    // Print the values
    printf("Person Name: %s\n", p1.name);
    printf("Person Age: %d\n", p1.age);
    printf("Address: %s, %s, %s\n", p1.address.street, p1.address.city, p1.address.zip_code);
    // Print a line of dashes matching the length of the city name
    for (size_t i = 0; i < 50; ++i) {
        putchar('-');
    }
    putchar('\n');
    printf("Person Name: %s\n", p2.name);
    printf("Person Age: %d\n", p2.age);
    printf("Address: %s, %s, %s\n", p2.address.street, p2.address.city, p2.address.zip_code);

    return 0;
}
