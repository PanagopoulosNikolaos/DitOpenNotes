// Advanced String Tokenizer

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char** tokenizeString(char *str, char *delimiters, int *count);
void freeTokens(char **tokens, int count);

int main() {
    char input[1000];
    char delimiters[50];
    char **tokens;
    int count, i;
    
    printf("Enter a string: ");
    fgets(input, sizeof(input), stdin);
    input[strcspn(input, "\n")] = '\0';  // Remove trailing newline
    
    printf("Enter delimiters: ");
    fgets(delimiters, sizeof(delimiters), stdin);
    delimiters[strcspn(delimiters, "\n")] = '\0';  // Remove trailing newline
    
    tokens = tokenizeString(input, delimiters, &count);
    
    printf("\nFound %d tokens:\n", count);
    for(i = 0; i < count; i++) {
        printf("[%d]: \"%s\"\n", i+1, tokens[i]);
    }
    
    freeTokens(tokens, count);
    
    return 0;
}

char** tokenizeString(char *str, char *delimiters, int *count) {
    char *copy = strdup(str);  // Create a copy as strtok modifies the string
    char *token;
    char **result = NULL;
    int capacity = 10;
    
    *count = 0;
    result = (char**)malloc(capacity * sizeof(char*));
    
    token = strtok(copy, delimiters);
    while(token != NULL) {
        if(*count >= capacity) {
            capacity *= 2;
            result = (char**)realloc(result, capacity * sizeof(char*));
        }
        
        result[*count] = strdup(token);
        (*count)++;
        
        token = strtok(NULL, delimiters);
    }
    
    free(copy);
    return result;
}

void freeTokens(char **tokens, int count) {
    int i;
    for(i = 0; i < count; i++) {
        free(tokens[i]);
    }
    free(tokens);
}
