/**
 * Demonstrates POSIX inter-process communication using anonymous pipes.
 *
 * Implements a parent-child pipeline equivalent to 'ls | wc -l' using
 * fork(), pipe(), dup2(), and execvp() system calls.
 */

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

/**
 * Creates child pipeline to execute 'ls -1 | wc -l'.
 *
 * Returns:
 *   int: Exit status code (0 on success, 1 on failure).
 */
int runPipelineDemo(void) {
    int pipe_fd[2]; // pipe_fd[0] = read end, pipe_fd[1] = write end

    if (pipe(pipe_fd) == -1) {
        perror("pipe allocation failed");
        return 1;
    }

    pid_t pid1 = fork();
    if (pid1 < 0) {
        perror("fork 1 failed");
        return 1;
    }

    if (pid1 == 0) {
        // First child process: runs 'ls -1' and outputs to pipe write end
        close(pipe_fd[0]); // Closes unused read end in producer
        dup2(pipe_fd[1], STDOUT_FILENO); // Replaces stdout with pipe write end
        close(pipe_fd[1]); // Closes duplicate descriptor after redirection

        char *args[] = {"ls", "-1", NULL};
        execvp("ls", args);
        perror("execvp ls failed");
        exit(1);
    }

    pid_t pid2 = fork();
    if (pid2 < 0) {
        perror("fork 2 failed");
        return 1;
    }

    if (pid2 == 0) {
        // Second child process: reads from pipe read end and runs 'wc -l'
        close(pipe_fd[1]); // Closes unused write end in consumer
        dup2(pipe_fd[0], STDIN_FILENO); // Replaces stdin with pipe read end
        close(pipe_fd[0]); // Closes duplicate descriptor after redirection

        char *args[] = {"wc", "-l", NULL};
        execvp("wc", args);
        perror("execvp wc failed");
        exit(1);
    }

    // Parent process: closes both ends so children observe EOF correctly
    close(pipe_fd[0]);
    close(pipe_fd[1]);

    // Awaits termination of both child processes to prevent zombie entries
    waitpid(pid1, NULL, 0);
    waitpid(pid2, NULL, 0);

    return 0;
}

int main(void) {
    printf("Executing POSIX pipe demonstration (ls -1 | wc -l):\n");
    return runPipelineDemo();
}

