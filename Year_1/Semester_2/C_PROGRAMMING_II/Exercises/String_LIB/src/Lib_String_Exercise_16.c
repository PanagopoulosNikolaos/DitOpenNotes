// Number to Words Converter

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include <stdbool.h>

void numberToWords(char *input);
void processThreeDigits(int num, char *result);

const char *ones[] = {"", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", 
                      "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"};
const char *tens[] = {"", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"};
const char *scales[] = {"", "thousand", "million", "billion"};

int main() {
    char input[100];
    
    printf("Enter a text with numbers: ");
    fgets(input, sizeof(input), stdin);
    input[strcspn(input, "\n")] = '\0';  // Remove trailing newline
    
    numberToWords(input);
    
    return 0;
}

void numberToWords(char *input) {
    char *temp = strdup(input);
    char *token, *start, output[1000] = "";
    int i, len;
    
    // Tokenize by spaces
    token = strtok(temp, " ");
    while(token != NULL) {
        // Check if token is a number
        len = strlen(token);
        bool isNumber = true;
        for(i = 0; i < len; i++) {
            if(!isdigit(token[i])) {
                isNumber = false;
                break;
            }
        }
        
        if(isNumber && len <= 10) {
            int num = atoi(token);
            char result[200] = "";
            
            if(num == 0) {
                strcat(result, "zero");
            } else {
                int scale = 0;
                while(num > 0) {
                    int threeDigits = num % 1000;
                    if(threeDigits > 0) {
                        char buffer[100] = "";
                        processThreeDigits(threeDigits, buffer);
                        if(scale > 0) {
                            strcat(buffer, " ");
                            strcat(buffer, scales[scale]);
                        }
                        if(result[0] != '\0') {
                            strcat(buffer, " ");
                        }
                        memmove(result + strlen(buffer), result, strlen(result) + 1);
                        memcpy(result, buffer, strlen(buffer));
                    }
                    num /= 1000;
                    scale++;
                }
            }
            
            strcat(output, result);
        } else {
            strcat(output, token);
        }
        
        strcat(output, " ");
        token = strtok(NULL, " ");
    }
    
    printf("Text with numbers in words: %s\n", output);
    free(temp);
}

void processThreeDigits(int num, char *result) {
    if(num >= 100) {
        sprintf(result + strlen(result), "%s hundred", ones[num/100]);
        num %= 100;
        if(num > 0) {
            strcat(result, " ");
        }
    }
    
    if(num >= 20) {
        strcat(result, tens[num/10]);
        num %= 10;
        if(num > 0) {
            strcat(result, "-");
            strcat(result, ones[num]);
        }
    } else if(num > 0) {
        strcat(result, ones[num]);
    }
}
