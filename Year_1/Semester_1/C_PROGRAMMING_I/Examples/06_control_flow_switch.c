/*
 * Exercise 06: Control Flow (switch)
 */

#include <stdio.h>

/**
 * Maps an integer input (1-7) to the corresponding day of the week.
 *
 * Args:
 *     None.
 *
 * Returns:
 *     int: Exit status code 0 on success, 1 on input error.
 */
int main(void) {
    int day;

    printf("Enter a number (1-7): ");
    if (scanf("%d", &day) != 1) {
        return 1;
    }

    // Selects calendar day using discrete case dispatch.
    switch (day) {
        case 1: printf("Monday\n"); break;
        case 2: printf("Tuesday\n"); break;
        case 3: printf("Wednesday\n"); break;
        case 4: printf("Thursday\n"); break;
        case 5: printf("Friday\n"); break;
        case 6: printf("Saturday\n"); break;
        case 7: printf("Sunday\n"); break;
        default: printf("Invalid day number.\n"); break;
    }

    return 0;
}
