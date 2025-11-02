#include <stdio.h>

/*
 * Exercise 8: Union within a Structure
 *
 * Objective:
 * Define a structure 'Data' that contains an integer 'type' and a union 'value'
 * that can hold either an 'int' or a 'float'.
 * Create 'Data' variables, assign different types of values, and print them based on the 'type' field.
 */

// Define a union
union Value {
    int i_val;
    float f_val;
};

// Define a structure that includes the union
struct Data {
    int type; // 0 for int, 1 for float
    union Value value;
};

int main() {
    struct Data d1, d2;

    // Assign an integer value
    d1.type = 0;
    d1.value.i_val = 123;

    // Assign a float value
    d2.type = 1;
    d2.value.f_val = 45.67f;// (float)(45.67F)

    // Print values based on type
    printf("Data 1:\n");
    if (d1.type == 0) {
        printf("Type: Integer, Value: %d\n", d1.value.i_val);
    } else {
        printf("Type: Float, Value: %.2f\n", d1.value.f_val);
    }

    printf("\nData 2:\n");
    if (d2.type == 0) {
        printf("Type: Integer, Value: %d\n", d2.value.i_val);
    } else {
        printf("Type: Float, Value: %.2f\n", d2.value.f_val);
    }

    return 0;
}
