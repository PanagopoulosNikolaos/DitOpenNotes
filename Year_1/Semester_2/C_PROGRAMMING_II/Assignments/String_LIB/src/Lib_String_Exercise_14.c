//  Longest Common Subsequence

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char* findLCS(char *str1, char *str2);

int main() {
    char str1[100], str2[100];
    char *lcs;
    
    printf("Enter first string: ");
    fgets(str1, sizeof(str1), stdin);
    str1[strcspn(str1, "\n")] = '\0';  // Remove trailing newline
    
    printf("Enter second string: ");
    fgets(str2, sizeof(str2), stdin);
    str2[strcspn(str2, "\n")] = '\0';  // Remove trailing newline
    
    lcs = findLCS(str1, str2);
    
    printf("Longest Common Subsequence: %s\n", lcs);
    
    free(lcs);
    return 0;
}

char* findLCS(char *str1, char *str2) {
    int len1 = strlen(str1);
    int len2 = strlen(str2);
    int i, j, index;
    char *result;
    
    // Create DP table
    int **dp = (int**)malloc((len1+1) * sizeof(int*));
    for(i = 0; i <= len1; i++) {
        dp[i] = (int*)malloc((len2+1) * sizeof(int));
    }
    
    // Fill the DP table
    for(i = 0; i <= len1; i++) {
        for(j = 0; j <= len2; j++) {
            if(i == 0 || j == 0)
                dp[i][j] = 0;
            else if(str1[i-1] == str2[j-1])
                dp[i][j] = dp[i-1][j-1] + 1;
            else
                dp[i][j] = (dp[i-1][j] > dp[i][j-1]) ? dp[i-1][j] : dp[i][j-1];
        }
    }
    
    // Extract the LCS
    int lcsLength = dp[len1][len2];
    result = (char*)malloc((lcsLength+1) * sizeof(char));
    result[lcsLength] = '\0';
    
    i = len1, j = len2, index = lcsLength;
    while(i > 0 && j > 0) {
        if(str1[i-1] == str2[j-1]) {
            result[--index] = str1[i-1];
            i--; j--;
        } else if(dp[i-1][j] > dp[i][j-1]) {
            i--;
        } else {
            j--;
        }
    }
    
    // Free the DP table
    for(i = 0; i <= len1; i++) {
        free(dp[i]);
    }
    free(dp);
    
    return result;
}
