/*
 * -----------------------------------------------------------------------------
 *
 *  Exercise 20: ctype Library
 *
 *  Task:
 *  Write a C program that uses functions from the ctype.h library to check
 *  the type of a character (alphabetic, digit, uppercase, lowercase, etc.)
 *  and to convert a character to uppercase or lowercase.
 *
 *  Instructions:
 *  1. Include the stdio.h and ctype.h libraries.
 *  2. In the main function, prompt the user to enter a character.
 *  3. Use functions like isalpha(), isdigit(), isupper(), islower(), etc.,
 *     to check the properties of the entered character and print the results.
 *  4. Use toupper() and tolower() to convert the character and print the
 *     converted characters.
 *
 * -----------------------------------------------------------------------------
 */

#include <stdio.h>
#include <ctype.h>

int main() {
    char ch;

    // Prompt the user to enter a character
    printf("Enter a character: ");
    scanf(" %c", &ch);

    // Check character properties using ctype functions
    if (isalpha(ch)) {
        printf("'%c' is an alphabetic character.\n", ch);
    } else {
        printf("'%c' is not an alphabetic character.\n", ch);
    }

    if (isdigit(ch)) {
        printf("'%c' is a digit.\n", ch);
    } else {
        printf("'%c' is not a digit.\n", ch);
    }

    if (isupper(ch)) {
        printf("'%c' is an uppercase letter.\n", ch);
    } else {
        printf("'%c' is not an uppercase letter.\n", ch);
    }

    if (islower(ch)) {
        printf("'%c' is a lowercase letter.\n", ch);
    }
    else {
        printf("'%c' is not a lowercase letter.\n", ch);
    }

    if (isspace(ch)) {
        printf("'%c' is a whitespace character.\n", ch);
    } else {
        printf("'%c' is not a whitespace character.\n", ch);
    }

    // Convert character case
    printf("\n--- Character Case Conversion ---\n");
    printf("Uppercase version of '%c': %c\n", ch, toupper(ch));
    printf("Lowercase version of '%c': %c\n", ch, tolower(ch));

    return 0;
}