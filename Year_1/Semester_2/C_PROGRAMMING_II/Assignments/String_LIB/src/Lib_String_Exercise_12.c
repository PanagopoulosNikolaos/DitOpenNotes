// Smart Palindrome Checker

#include <stdio.h>
#include <string.h>
#include <ctype.h>

int isPalindrome(char *text);

int main() {
    char text[1000];
    
    printf("Enter a string to check if it's a palindrome: ");
    fgets(text, sizeof(text), stdin);
    text[strcspn(text, "\n")] = '\0';  // Remove trailing newline
    
    if(isPalindrome(text))
        printf("\"%s\" is a palindrome.\n", text);
    else
        printf("\"%s\" is not a palindrome.\n", text);
    
    return 0;
}

int isPalindrome(char *text) {
    char clean[1000];
    int i, j = 0;
    
    // Remove non-alphanumeric characters and convert to lowercase
    for(i = 0; text[i] != '\0'; i++) {
        if(isalnum(text[i]))
            clean[j++] = tolower(text[i]);
    }
    clean[j] = '\0';
    
    // Check if palindrome
    for(i = 0, j = strlen(clean) - 1; i < j; i++, j--) {
        if(clean[i] != clean[j])
            return 0;
    }
    
    return 1;
}
