#include <stdio.h>

/**
 * Converts a non-negative decimal integer to binary and prints it.
 *
 * Args:
 *     n (int): Integer to convert to binary.
 *
 * Returns:
 *     void: Outputs binary bit sequence directly to stdout.
 */
void decToBinary(int n) {
    int binary_num[32];
    int i = 0;

    if (n == 0) {
        printf("0\n");
        return;
    }

    // Extracts binary digits into array in reverse order.
    while (n > 0) {
        binary_num[i] = n % 2;
        n = n / 2;
        i++;
    }

    // Prints bits in correct MSB-to-LSB sequence.
    for (int j = i - 1; j >= 0; j--) {
        printf("%d", binary_num[j]);
    }
    printf("\n");
}

/**
 * Prompts user for a decimal integer and displays its binary form.
 *
 * Args:
 *     None.
 *
 * Returns:
 *     int: Exit status code 0 on success, 1 on input error.
 */
int main(void) {
    int number;

    printf("Enter a decimal number: ");
    if (scanf("%d", &number) != 1) {
        return 1;
    }

    printf("Binary: ");
    decToBinary(number);

    return 0;
}
