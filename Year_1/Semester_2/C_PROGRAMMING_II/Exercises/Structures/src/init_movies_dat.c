#include <stdio.h>
#include <string.h>

// Define a structure named Movie (same as Exercise 20)
struct Movie {
    int id;
    char title[100];
    int year;
};

int main() {
    struct Movie movies[] = {
        {101, "The Matrix", 1999},
        {102, "Inception", 2010},
        {103, "Interstellar", 2014},
        {104, "Dune", 2021}
    };
    int num_movies = sizeof(movies) / sizeof(struct Movie);

    FILE *fp = fopen("movies.dat", "wb");
    if (fp == NULL) {
        perror("Error opening movies.dat for writing");
        return 1;
    }

    fwrite(movies, sizeof(struct Movie), num_movies, fp);
    fclose(fp);

    printf("%d movies written to movies.dat successfully.\n", num_movies);
    printf("You can now run exercise_20_file_handling.c to search for records.\n");

    return 0;
}
