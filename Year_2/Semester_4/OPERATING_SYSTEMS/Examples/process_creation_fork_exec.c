/**
 * Demonstrates process creation and program execution using fork, execvp, and waitpid.
 *
 * Spawns a child process to execute a system utility while the parent process
 * tracks the child state and inspects its termination exit status.
 */

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

/**
 * Creates a child process to run an external command.
 *
 * Args:
 *   command (char*): The command name or executable path.
 *   args (char**): Null-terminated array of argument strings.
 *
 * Returns:
 *   int: Exit status of the child process, or -1 on system failure.
 */
int executeChildProcess(char *command, char **args) {
    pid_t child_pid = fork();

    if (child_pid < 0) {
        // Fork fails when system process table is full or memory is exhausted.
        perror("fork failed");
        return -1;
    }

    if (child_pid == 0) {
        // Replaces child process image with the target executable.
        execvp(command, args);

        // Execvp returns only if execution encounters an error.
        perror("execvp failed");
        exit(EXIT_FAILURE);
    }

    // Parent waits for the specific child process to terminate.
    int child_status = 0;
    pid_t waited_pid = waitpid(child_pid, &child_status, 0);

    if (waited_pid == -1) {
        perror("waitpid failed");
        return -1;
    }

    // Evaluates normal termination and extracts return code.
    if (WIFEXITED(child_status)) {
        return WEXITSTATUS(child_status);
    }

    return -1;
}

int main(void) {
    printf("[Parent PID: %d] Launching child process...\n", getpid());

    char *command_args[] = {"echo", "Hello from child process via execvp!", NULL};
    int exit_code = executeChildProcess("echo", command_args);

    printf("[Parent PID: %d] Child finished with exit code: %d\n", getpid(), exit_code);
    return EXIT_SUCCESS;
}

