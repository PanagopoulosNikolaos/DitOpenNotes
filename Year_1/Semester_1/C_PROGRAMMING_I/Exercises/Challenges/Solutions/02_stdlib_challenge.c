#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    srand(time(NULL));
    int random_number = rand() % 100 + 1;
    int guess;

    do {
        printf("Guess the number (1-100): ");
        scanf("%d", &guess);

        if (guess > random_number) {
            printf("Too high!\n");
        } else if (guess < random_number) {
            printf("Too low!\n");
        } else {
            printf("You got it!\n");
        }
    } while (guess != random_number);

    return 0;
}
