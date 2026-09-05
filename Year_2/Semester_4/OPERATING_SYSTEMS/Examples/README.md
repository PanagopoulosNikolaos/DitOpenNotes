# Operating Systems: Code Examples

This directory provides practical, runnable systems programming implementations in C and automated administration scripts in Bash.

---

## Directory Contents

| File | Language / Type | Description |
|:---|:---|:---|
| [`examples_posix_processes_and_pipes.c`](examples_posix_processes_and_pipes.c) | C (POSIX C11) | Process creation with `fork()`, inter-process communication using `pipe()`, file descriptor management, and process synchronization with `waitpid()` |
| [`examples_unix_shell_automation.sh`](examples_unix_shell_automation.sh) | Bash Shell | Production shell automation: file permission validation, log file aggregation pipelines (`grep`, `awk`, `sort`, `uniq`), and process telemetry |
| [`examples_posix_and_shell_walkthrough.md`](examples_posix_and_shell_walkthrough.md) | Markdown | Detailed walkthrough explaining IPC mechanisms, process lifecycle, signal handling, and shell stream pipelines |

---

## Quick Execution Commands

```bash
# Compile and run POSIX process demonstration
gcc -Wall -Wextra -std=c11 examples_posix_processes_and_pipes.c -o run_pipes
./run_pipes

# Run UNIX shell automation script
bash examples_unix_shell_automation.sh
```

