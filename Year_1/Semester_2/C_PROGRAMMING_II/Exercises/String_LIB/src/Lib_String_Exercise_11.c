// Caesar Cipher Encryption/Decryption

#include <stdio.h>
#include <string.h>
#include <ctype.h>

void encrypt(char *text, int shift);
void decrypt(char *text, int shift);

int main() {
    char text[1000];
    int shift, choice;
    
    printf("Enter text: ");
    fgets(text, sizeof(text), stdin);
    text[strcspn(text, "\n")] = '\0';  // Remove trailing newline
    
    printf("Enter shift value (1-25): ");
    scanf("%d", &shift);
    
    printf("Choose operation:\n");
    printf("1. Encrypt\n");
    printf("2. Decrypt\n");
    scanf("%d", &choice);
    
    if(choice == 1)
        encrypt(text, shift);
    else if(choice == 2)
        decrypt(text, shift);
    else
        printf("Invalid choice!\n");
    
    printf("Result: %s\n", text);
    
    return 0;
}

void encrypt(char *text, int shift) {
    int i;
    char c;
    
    for(i = 0; text[i] != '\0'; i++) {
        c = text[i];
        
        if(isalpha(c)) {
            if(islower(c)) {
                c = ((c - 'a') + shift) % 26 + 'a';
            } else {
                c = ((c - 'A') + shift) % 26 + 'A';
            }
            text[i] = c;
        }
    }
}

void decrypt(char *text, int shift) {
    encrypt(text, 26 - (shift % 26));
}
