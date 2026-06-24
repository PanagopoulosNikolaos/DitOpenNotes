// Simple Regex Pattern Matcher

#include <stdio.h>
#include <string.h>
#include <stdbool.h>

bool matchPattern(const char *text, const char *pattern);

int main() {
    char text[1000], pattern[100];
    
    printf("Enter text: ");
    fgets(text, sizeof(text), stdin);
    text[strcspn(text, "\n")] = '\0';  // Remove trailing newline
    
    printf("Enter pattern (use ? for any single character, * for any sequence): ");
    fgets(pattern, sizeof(pattern), stdin);
    pattern[strcspn(pattern, "\n")] = '\0';  // Remove trailing newline
    
    if(matchPattern(text, pattern))
        printf("Pattern matches the text.\n");
    else
        printf("Pattern does not match the text.\n");
    
    return 0;
}

bool matchPattern(const char *text, const char *pattern) {
    // Base cases
    if(*pattern == '\0') return *text == '\0';
    
    // If next character in pattern is '*'
    if(pattern[1] == '*') {
        // Match zero or more of the current pattern character
        while(*text != '\0' && (*text == *pattern || *pattern == '.')) {
            if(matchPattern(text, pattern+2)) return true;
            text++;
        }
        return matchPattern(text, pattern+2);
    }
    
    // If current characters match or pattern has '?'
    if(*text != '\0' && (*pattern == '?' || *pattern == *text))
        return matchPattern(text+1, pattern+1);
    
    return false;
}
