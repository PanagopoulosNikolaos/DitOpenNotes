//  Anagram Checker


#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

int isAnagram(char *str1, char *str2);

int main() {
    char str1[100], str2[100];
    
    printf("Enter first string: ");
    fgets(str1, sizeof(str1), stdin);
    str1[strcspn(str1, "\n")] = '\0';  // Remove trailing newline
    
    printf("Enter second string: ");
    fgets(str2, sizeof(str2), stdin);
    str2[strcspn(str2, "\n")] = '\0';  // Remove trailing newline
    
    if(isAnagram(str1, str2))
        printf("\"%s\" and \"%s\" are anagrams.\n", str1, str2);
    else
        printf("\"%s\" and \"%s\" are not anagrams.\n", str1, str2);
    
    return 0;
}

int isAnagram(char *str1, char *str2) {
    int count1[26] = {0}, count2[26] = {0};
    int i;
    
    // Counting characters (ignoring non-alphabetic characters and case)
    for(i = 0; str1[i] != '\0'; i++) {
        if(isalpha(str1[i])) {
            count1[tolower(str1[i]) - 'a']++;
        }
    }
    
    for(i = 0; str2[i] != '\0'; i++) {
        if(isalpha(str2[i])) {
            count2[tolower(str2[i]) - 'a']++;
        }
    }
    
    // Comparing character counts
    for(i = 0; i < 26; i++) {
        if(count1[i] != count2[i])
            return 0;
    }
    
    return 1;
}
