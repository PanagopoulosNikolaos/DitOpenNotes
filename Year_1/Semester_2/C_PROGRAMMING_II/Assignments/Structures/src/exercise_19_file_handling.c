#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
 * Exercise 19: Deleting a Specific Record from a Binary File
 *
 * Objective:
 * Define a structure 'Task' with 'task_id', 'description', and 'status'.
 * Write a program that reads a binary file of 'Task' records,
 * allows the user to specify a 'task_id' to delete,
 * and then rewrites the file without that record.
 */

// Define a structure named Task
struct Task {
    int task_id;
    char description[100];
    int status; // 0 for pending, 1 for completed
};

int main() {
    FILE *fp_read, *fp_write;
    struct Task task;
    int target_id;
    int found = 0;

    printf("Enter Task ID to delete: ");
    scanf("%d", &target_id);

    fp_read = fopen("tasks.dat", "rb");
    if (fp_read == NULL) {
        perror("Error opening tasks.dat for reading");
        return 1;
    }

    fp_write = fopen("temp_tasks.dat", "wb");
    if (fp_write == NULL) {
        perror("Error opening temp_tasks.dat for writing");
        fclose(fp_read);
        return 1;
    }

    while (fread(&task, sizeof(struct Task), 1, fp_read) == 1) {
        if (task.task_id == target_id) {
            found = 1;
            printf("Task ID %d deleted.\n", target_id);
        } else {
            fwrite(&task, sizeof(struct Task), 1, fp_write);
        }
    }

    fclose(fp_read);
    fclose(fp_write);

    if (!found) {
        printf("Task ID %d not found.\n", target_id);
    }

    // Replace original file with temporary file
    remove("tasks.dat");
    rename("temp_tasks.dat", "tasks.dat");

    return 0;
}
