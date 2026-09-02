/**
 * Demonstrates Inter-Process Communication using POSIX anonymous pipes.
 *
 * Establishes a unidirectional communication channel between a parent process
 * and its child process using pipe, fork, read, and write system calls.
 */

#define _DEFAULT_SOURCE

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

#define BUFFER_SIZE 256

/**
 * Executes unidirectional IPC communication between parent and child.
 *
 * Returns:
 *   int: 0 on success, -1 on failure.
 */
int executePipeCommunication(void) {
    int pipe_fd[2]; // pipe_fd[0]: Read end, pipe_fd[1]: Write end.

    if (pipe(pipe_fd) == -1) {
        perror("pipe creation failed");
        return -1;
    }

    pid_t child_pid = fork();

    if (child_pid < 0) {
        perror("fork failed");
        close(pipe_fd[0]);
        close(pipe_fd[1]);
        return -1;
    }

    if (child_pid == 0) {
        // Child acts as reader: closes unused write end.
        close(pipe_fd[1]);

        char received_message[BUFFER_SIZE];
        ssize_t bytes_read = read(pipe_fd[0], received_message, sizeof(received_message) - 1);

        if (bytes_read >= 0) {
            received_message[bytes_read] = '\0';
            printf("[Child PID: %d] Received from pipe: \"%s\"\n", getpid(), received_message);
        } else {
            perror("child read error");
        }

        close(pipe_fd[0]);
        exit(EXIT_SUCCESS);
    } else {
        // Parent acts as writer: closes unused read end.
        close(pipe_fd[0]);

        const char *outgoing_message = "Operating Systems IPC via POSIX Pipe";
        printf("[Parent PID: %d] Transmitting message to child: \"%s\"\n", getpid(), outgoing_message);

        ssize_t bytes_written = write(pipe_fd[1], outgoing_message, strlen(outgoing_message));
        if (bytes_written == -1) {
            perror("parent write error");
        }

        close(pipe_fd[1]);

        // Waits for child process to finish reading and exit.
        wait(NULL);
    }

    return 0;
}

int main(void) {
    if (executePipeCommunication() != 0) {
        return EXIT_FAILURE;
    }

    printf("Pipe communication verified successfully.\n");
    return EXIT_SUCCESS;
}

