#include <stdio.h>
#include <string.h>

// Define a structure named Task (same as Exercise 19)
struct Task {
    int task_id;
    char description[100];
    int status; // 0 for pending, 1 for completed
};

int main() {
    struct Task tasks[] = {
        {1, "Buy groceries", 0},
        {2, "Finish C exercises", 0},
        {3, "Call mom", 1},
        {4, "Pay bills", 0}
    };
    int num_tasks = sizeof(tasks) / sizeof(struct Task);

    FILE *fp = fopen("tasks.dat", "wb");
    if (fp == NULL) {
        perror("Error opening tasks.dat for writing");
        return 1;
    }

    fwrite(tasks, sizeof(struct Task), num_tasks, fp);
    fclose(fp);

    printf("%d tasks written to tasks.dat successfully.\n", num_tasks);
    printf("You can now run exercise_19_file_handling.c to delete records.\n");

    return 0;
}
