#include <stdio.h>
#include <ctype.h>
#include <string.h> // For strlen in some exercises



// 1. Check if a character is alphanumeric
void exercise1_isalnum() {
    char c;
    printf("Exercise 1: isalnum()\n");
    printf("Enter a character: ");
    scanf(" %c", &c); // Note the space before %c to consume leftover newline
    if (isalnum(c)) {
        printf("'%c' is alphanumeric.\n", c);
    } else {
        printf("'%c' is not alphanumeric.\n", c);
    }
}

// 2. Check if a character is alphabetic
void exercise2_isalpha() {
    char c;
    printf("Exercise 2: isalpha()\n");
    printf("Enter a character: ");
    scanf(" %c", &c);
    if (isalpha(c)) {
        printf("'%c' is alphabetic.\n", c);
    } else {
        printf("'%c' is not alphabetic.\n", c);
    }
}

// 3. Check if a character is a control character
void exercise3_iscntrl() {
    // Note: Hard to demonstrate by direct input, let's test known control chars
    printf("Exercise 3: iscntrl()\n");
    char c1 = '\n'; // Newline
    char c2 = '\t'; // Tab
    char c3 = 'A';
    printf("Testing '\\n': %s\n", iscntrl(c1) ? "Is a control character" : "Not a control character");
    printf("Testing '\\t': %s\n", iscntrl(c2) ? "Is a control character" : "Not a control character");
    printf("Testing 'A': %s\n", iscntrl(c3) ? "Is a control character" : "Not a control character");
}

// 4. Check if a character is a digit
void exercise4_isdigit() {
    char c;
    printf("Exercise 4: isdigit()\n");
    printf("Enter a character: ");
    scanf(" %c", &c);
    if (isdigit(c)) {
        printf("'%c' is a digit.\n", c);
    } else {
        printf("'%c' is not a digit.\n", c);
    }
}

// 5. Check if a character has a graphical representation
void exercise5_isgraph() {
    char c;
    printf("Exercise 5: isgraph()\n");
    printf("Enter a character: ");
    scanf(" %c", &c);
    // isgraph is true for all printable characters except space
    if (isgraph(c)) {
        printf("'%c' has a graphical representation (and is not space).\n", c);
    } else {
        printf("'%c' does not have a graphical representation (or is space).\n", c);
    }
}

// 6. Check if a character is lowercase
void exercise6_islower() {
    char c;
    printf("Exercise 6: islower()\n");
    printf("Enter a character: ");
    scanf(" %c", &c);
    if (islower(c)) {
        printf("'%c' is a lowercase letter.\n", c);
    } else {
        printf("'%c' is not a lowercase letter.\n", c);
    }
}

// 7. Check if a character is printable (including space)
void exercise7_isprint() {
    char c;
    printf("Exercise 7: isprint()\n");
    printf("Enter a character: ");
    scanf(" %c", &c);
    if (isprint(c)) {
        printf("'%c' is a printable character (including space).\n", c);
    } else {
        printf("'%c' is not a printable character.\n", c);
    }
}

// 8. Check if a character is punctuation
void exercise8_ispunct() {
    char c;
    printf("Exercise 8: ispunct()\n");
    printf("Enter a character: ");
    scanf(" %c", &c);
    if (ispunct(c)) {
        printf("'%c' is a punctuation character.\n", c);
    } else {
        printf("'%c' is not a punctuation character.\n", c);
    }
}

// 9. Check if a character is whitespace
void exercise9_isspace() {
    char c;
    printf("Exercise 9: isspace()\n");
    printf("Enter a character (try space or tab): ");
    // Reading whitespace requires a different approach or testing known values
    getchar(); // Consume the newline from previous input if any
    c = getchar(); // Read the actual character, including whitespace
    if (isspace(c)) {
        printf("The entered character is whitespace.\n");
    } else {
        printf("'%c' is not a whitespace character.\n", c);
    }
     // Consume potential leftover newline from getchar()
    while (getchar() != '\n');
}

// 10. Check if a character is uppercase
void exercise10_isupper() {
    char c;
    printf("Exercise 10: isupper()\n");
    printf("Enter a character: ");
    scanf(" %c", &c);
    if (isupper(c)) {
        printf("'%c' is an uppercase letter.\n", c);
    } else {
        printf("'%c' is not an uppercase letter.\n", c);
    }
}

// 11. Check if a character is a hexadecimal digit
void exercise11_isxdigit() {
    char c;
    printf("Exercise 11: isxdigit()\n");
    printf("Enter a character: ");
    scanf(" %c", &c);
    if (isxdigit(c)) {
        printf("'%c' is a hexadecimal digit (0-9, a-f, A-F).\n", c);
    } else {
        printf("'%c' is not a hexadecimal digit.\n", c);
    }
}

// 12. Convert a character to lowercase
void exercise12_tolower() {
    char c, lower_c;
    printf("Exercise 12: tolower()\n");
    printf("Enter an uppercase character: ");
    scanf(" %c", &c);
    lower_c = tolower(c);
    printf("Lowercase version of '%c' is '%c'.\n", c, lower_c);
}

// 13. Convert a character to uppercase
void exercise13_toupper() {
    char c, upper_c;
    printf("Exercise 13: toupper()\n");
    printf("Enter a lowercase character: ");
    scanf(" %c", &c);
    upper_c = toupper(c);
    printf("Uppercase version of '%c' is '%c'.\n", c, upper_c);
}

// 14. Count digits in a string
void exercise14_count_digits() {
    char str[100];
    int count = 0;
    printf("Exercise 14: Count Digits in a String\n");
    printf("Enter a string: ");
    scanf(" %[^\n]", str); // Read string including spaces until newline
    for (int i = 0; str[i] != '\0'; i++) {
        if (isdigit(str[i])) {
            count++;
        }
    }
    printf("Number of digits in \"%s\": %d\n", str, count);
}

// 15. Count alphabetic characters in a string
void exercise15_count_alphas() {
    char str[100];
    int count = 0;
    printf("Exercise 15: Count Alphabetic Chars in a String\n");
    printf("Enter a string: ");
    scanf(" %[^\n]", str);
    for (int i = 0; str[i] != '\0'; i++) {
        if (isalpha(str[i])) {
            count++;
        }
    }
    printf("Number of alphabetic characters in \"%s\": %d\n", str, count);
}

// 16. Count whitespace characters in a string
void exercise16_count_spaces() {
    char str[100];
    int count = 0;
    printf("Exercise 16: Count Whitespace Chars in a String\n");
    printf("Enter a string: ");
    // Need to read carefully to include leading/trailing spaces
    getchar(); // Consume newline from previous input
    fgets(str, sizeof(str), stdin);
    // fgets might include the newline, remove it if present
    str[strcspn(str, "\n")] = 0;

    for (int i = 0; str[i] != '\0'; i++) {
        if (isspace(str[i])) {
            count++;
        }
    }
    printf("Number of whitespace characters in \"%s\": %d\n", str, count);
}

// 17. Convert a string to uppercase
void exercise17_convert_to_upper() {
    char str[100];
    printf("Exercise 17: Convert String to Uppercase\n");
    printf("Enter a string: ");
    scanf(" %[^\n]", str);
    for (int i = 0; str[i] != '\0'; i++) {
        str[i] = toupper(str[i]);
    }
    printf("Uppercase string: %s\n", str);
}

// 18. Convert a string to lowercase
void exercise18_convert_to_lower() {
    char str[100];
    printf("Exercise 18: Convert String to Lowercase\n");
    printf("Enter a string: ");
    scanf(" %[^\n]", str);
    for (int i = 0; str[i] != '\0'; i++) {
        str[i] = tolower(str[i]);
    }
    printf("Lowercase string: %s\n", str);
}

// 19. Remove punctuation from a string
void exercise19_remove_punctuation() {
    char str[100], result[100];
    int j = 0;
    printf("Exercise 19: Remove Punctuation from String\n");
    printf("Enter a string: ");
    scanf(" %[^\n]", str);
    for (int i = 0; str[i] != '\0'; i++) {
        if (!ispunct(str[i])) {
            result[j++] = str[i];
        }
    }
    result[j] = '\0'; // Null-terminate the result string
    printf("String without punctuation: %s\n", result);
}

// 20. Validate if input character is a digit
void exercise20_validate_input_digit() {
    char c;
    printf("Exercise 20: Validate Input is a Digit\n");
    printf("Enter a single character: ");
    scanf(" %c", &c);
    if (isdigit(c)) {
        printf("Valid input: '%c' is a digit.\n", c);
    } else {
        printf("Invalid input: '%c' is not a digit.\n", c);
    }
}


// --- Main Function ---

int main() {
    int choice;

    do {
        // Display Menu
        printf("\n--- ctype.h Exercises ---\n");
        printf(" 1. isalnum()      | 11. isxdigit()\n");
        printf(" 2. isalpha()      | 12. tolower()\n");
        printf(" 3. iscntrl()      | 13. toupper()\n");
        printf(" 4. isdigit()      | 14. Count Digits\n");
        printf(" 5. isgraph()      | 15. Count Alphas\n");
        printf(" 6. islower()      | 16. Count Spaces\n");
        printf(" 7. isprint()      | 17. String to Upper\n");
        printf(" 8. ispunct()      | 18. String to Lower\n");
        printf(" 9. isspace()      | 19. Remove Punctuation\n");
        printf("10. isupper()      | 20. Validate Digit Input\n");
        printf(" 0. Exit\n");
        printf("-----------------------\n");
        printf("Enter your choice (1-20, or 0 to exit): ");

        // Get user choice
        if (scanf("%d", &choice) != 1) {
             printf("Invalid input. Please enter a number.\n");
             // Clear invalid input
             while (getchar() != '\n');
             choice = -1; // Set choice to an invalid value to loop again
             continue;
        }

         // Consume the newline character left by scanf
        getchar();


        printf("\n"); // Add a newline for better formatting

        // Call the corresponding function
        switch (choice) {
            case 1:  exercise1_isalnum(); break;
            case 2:  exercise2_isalpha(); break;
            case 3:  exercise3_iscntrl(); break;
            case 4:  exercise4_isdigit(); break;
            case 5:  exercise5_isgraph(); break;
            case 6:  exercise6_islower(); break;
            case 7:  exercise7_isprint(); break;
            case 8:  exercise8_ispunct(); break;
            case 9:  exercise9_isspace(); break;
            case 10: exercise10_isupper(); break;
            case 11: exercise11_isxdigit(); break;
            case 12: exercise12_tolower(); break;
            case 13: exercise13_toupper(); break;
            case 14: exercise14_count_digits(); break;
            case 15: exercise15_count_alphas(); break;
            case 16: exercise16_count_spaces(); break;
            case 17: exercise17_convert_to_upper(); break;
            case 18: exercise18_convert_to_lower(); break;
            case 19: exercise19_remove_punctuation(); break;
            case 20: exercise20_validate_input_digit(); break;
            case 0:  printf("Exiting program.\n"); break;
            default: printf("Invalid choice. Please enter a number between 0 and 20.\n"); break;
        }
        printf("\n"); // Add a newline after the exercise output

    } while (choice != 0);

    return 0;
}
