//Wildcard Pattern Matchin
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

bool isMatch(const char *text, const char *pattern);

int main() {
    char text[1000], pattern[100];
    
    printf("Enter text: ");
    fgets(text, sizeof(text), stdin);
    text[strcspn(text, "\n")] = '\0';  // Remove trailing newline
    
    printf("Enter wildcard pattern (* matches any sequence, ? matches single char): ");
    fgets(pattern, sizeof(pattern), stdin);
    pattern[strcspn(pattern, "\n")] = '\0';  // Remove trailing newline
    
    if(isMatch(text, pattern))
        printf("The pattern matches the text.\n");
    else
        printf("The pattern does not match the text.\n");
    
    return 0;
}

bool isMatch(const char *text, const char *pattern) {
    int textLen = strlen(text);
    int patternLen = strlen(pattern);
    
    // Create a DP table
    bool dp[textLen+1][patternLen+1];
    memset(dp, false, sizeof(dp));
    
    // Empty pattern matches empty string
    dp[0][0] = true;
    
    // Handle patterns like "*", "*a", "a*", etc.
    for(int j = 1; j <= patternLen; j++) {
        if(pattern[j-1] == '*')
            dp[0][j] = dp[0][j-1];
    }
    
    // Fill the DP table
    for(int i = 1; i <= textLen; i++) {
        for(int j = 1; j <= patternLen; j++) {
            if(pattern[j-1] == '*') {
                // * can match zero or more characters
                dp[i][j] = dp[i][j-1] || dp[i-1][j];
            } else if(pattern[j-1] == '?' || text[i-1] == pattern[j-1]) {
                // ? matches any single character or exact match
                dp[i][j] = dp[i-1][j-1];
            } else {
                dp[i][j] = false;
            }
        }
    }
    
    return dp[textLen][patternLen];
}
