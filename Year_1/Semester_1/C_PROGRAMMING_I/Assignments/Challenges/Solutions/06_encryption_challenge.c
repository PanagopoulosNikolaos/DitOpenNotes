#include <stdio.h>

/**
 * Encrypts a plaintext message using the Caesar cipher algorithm.
 *
 * Args:
 *     None.
 *
 * Returns:
 *     int: Exit status code 0 on successful execution.
 */
int main(void) {
    char message[100];
    int key;

    printf("Enter a message to encrypt: ");
    if (fgets(message, sizeof(message), stdin) == NULL) {
        return 1;
    }

    printf("Enter key: ");
    if (scanf("%d", &key) != 1) {
        return 1;
    }

    // Normalizes shift to standard alphabet range [0, 25].
    int shift = (key % 26 + 26) % 26;

    for (int i = 0; message[i] != '\0'; ++i) {
        char ch = message[i];

        if (ch >= 'a' && ch <= 'z') {
            message[i] = (char)('a' + (ch - 'a' + shift) % 26);
        } else if (ch >= 'A' && ch <= 'Z') {
            message[i] = (char)('A' + (ch - 'A' + shift) % 26);
        }
    }

    printf("Encrypted message: %s", message);

    return 0;
}
