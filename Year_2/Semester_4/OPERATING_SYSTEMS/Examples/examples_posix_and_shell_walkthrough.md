# Operating Systems: POSIX Processes, Pipes, and Shell Automation Walkthrough

This guide accompanies [`examples_posix_processes_and_pipes.c`](examples_posix_processes_and_pipes.c) and [`examples_unix_shell_automation.sh`](examples_unix_shell_automation.sh) to illustrate core systems programming and UNIX shell scripting techniques.

---

## 1. POSIX Process Management & IPC (`examples_posix_processes_and_pipes.c`)

### System Architecture
The C program demonstrates inter-process communication (IPC) between parent and child processes using unidirectional POSIX pipes:

```text
Parent Process ─────────────────── pipe() fd[1] (Write End)
      │                                    │
    fork()                                 ▼ Data Stream ("Telemetry Message")
      │                                    │
Child Process  ─────────────────── pipe() fd[0] (Read End)
```

### Key System Calls Covered
- `pipe(int pipefd[2])`: Creates a unidirectional data channel in kernel space. `pipefd[0]` is read, `pipefd[1]` is write.
- `fork()`: Clones the calling process. Returns 0 in child, child PID in parent, or -1 on failure.
- `close(int fd)`: Unused pipe endpoints MUST be closed to ensure EOF detection when the writer finishes.
- `waitpid(pid_t pid, int *status, int options)`: Reaps zombie processes and inspects child exit codes (`WIFEXITED`, `WEXITSTATUS`).

### Compilation & Execution
```bash
# Compile with strict warnings
gcc -Wall -Wextra -pedantic -std=c11 examples_posix_processes_and_pipes.c -o run_pipes

# Execute binary
./run_pipes
```

---

## 2. UNIX Shell Automation (`examples_unix_shell_automation.sh`)

### Script Capabilities
- **File System Auditing**: Inspects file permissions, counts files by extension, and analyzes storage footprints.
- **Log Processing Pipeline**: Parses timestamped log files using `grep`, `awk`, `sort`, and `uniq -c` to generate error frequency tables.
- **Process Monitoring**: Inspects active processes, filters CPU/memory utilization, and identifies anomalous process states.

### Execution
```bash
# Make executable and run
chmod +x examples_unix_shell_automation.sh
./examples_unix_shell_automation.sh
```

