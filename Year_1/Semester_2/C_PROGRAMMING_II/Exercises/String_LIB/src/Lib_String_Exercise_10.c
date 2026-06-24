// Word Frequency Counter

#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

#define MAX_WORDS 1000
#define MAX_WORD_LEN 50

typedef struct {
    char word[MAX_WORD_LEN];
    int count;
} WordFreq;

int main() {
    char text[5000];
    WordFreq wordList[MAX_WORDS];
    char *token;
    int uniqueWords = 0, i, j, found;
    
    printf("Enter a paragraph of text:\n");
    fgets(text, sizeof(text), stdin);
    
    // Convert to lowercase
    for(i = 0; text[i]; i++)
        text[i] = tolower(text[i]);
    
    // Tokenize and count frequencies
    token = strtok(text, " ,.!?;\n\t");
    while(token != NULL && uniqueWords < MAX_WORDS) {
        if(strlen(token) > 0) {
            found = 0;
            for(j = 0; j < uniqueWords; j++) {
                if(strcmp(wordList[j].word, token) == 0) {
                    wordList[j].count++;
                    found = 1;
                    break;
                }
            }
            
            if(!found) {
                strcpy(wordList[uniqueWords].word, token);
                wordList[uniqueWords].count = 1;
                uniqueWords++;
            }
        }
        token = strtok(NULL, " ,.!?;\n\t");
    }
    
    // Sort by frequency (bubble sort)
    for(i = 0; i < uniqueWords-1; i++) {
        for(j = 0; j < uniqueWords-i-1; j++) {
            if(wordList[j].count < wordList[j+1].count) {
                WordFreq temp = wordList[j];
                wordList[j] = wordList[j+1];
                wordList[j+1] = temp;
            }
        }
    }
    
    printf("\nWord frequency analysis:\n");
    printf("%-20s %s\n", "Word", "Frequency");
    printf("-----------------------------\n");
    for(i = 0; i < uniqueWords; i++) {
        printf("%-20s %d\n", wordList[i].word, wordList[i].count);
    }
    
    return 0;
}
