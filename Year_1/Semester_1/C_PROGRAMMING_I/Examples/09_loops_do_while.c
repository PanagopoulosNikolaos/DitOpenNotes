/*
 * -----------------------------------------------------------------------------
 *
 *  Exercise 9: Loops (do-while)
 *
 *  Task:
 *  Write a C program that repeatedly asks the user to guess a secret number
 *  (e.g., 7) until they guess it correctly.
 *
 *  Instructions:
 *  1. Include the stdio.h library.
 *  2. Define a constant for the secret number.
 *  3. In the main function, use a do-while loop to prompt the user for a
 *     guess.
 *  4. The loop should continue as long as the guess is incorrect.
 *  5. Once the correct number is guessed, print a congratulatory message.
 *
 * -----------------------------------------------------------------------------
 */

#include <stdio.h>

#define SECRET_NUMBER 7

int main() {
    int guess;

    // Use a do-while loop to ensure the user is prompted at least once
    do {
        // Prompt the user to enter their guess
        printf("Guess the secret number (between 1 and 10): ");
        scanf("%d", &guess);

        // Provide feedback if the guess is wrong
        if (guess != SECRET_NUMBER) {
            printf("Wrong guess! Try again.\n");
        }

    } while (guess != SECRET_NUMBER);

    // Congratulate the user for the correct guess
    printf("Congratulations! You guessed the secret number correctly.\n");

    return 0;
}
