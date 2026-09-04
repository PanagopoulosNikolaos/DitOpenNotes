# Project 01: Custom UNIX Shell Interpreter Implementation in C

## Project Overview
Design and implement a POSIX-compliant interactive command-line shell interpreter (`minish`) in C. The shell parses user input, executes foreground and background commands, supports inter-process pipelines (`cmd1 | cmd2`), manages standard I/O stream redirection (`<`, `>`, `>>`), and implements essential built-in commands without relying on external shell libraries.

---

## Architectural and Technical Specifications

### 1. The Core Shell Read-Eval-Print Loop (REPL)
The interpreter must execute in a continuous cycle:
1. **Prompt Display:** Display custom prompt including current working directory (e.g., `minish:/home/user$ `).
2. **Input Reading:** Read command line using `getline()` or `fgets()`, safely handling EOF (`Ctrl+D`) and arbitrary whitespace.
3. **Tokenization:** Lexically analyze line into an array of arguments (`char *argv[]`), separating command tokens and operators (`|`, `<`, `>`, `>>`, `&`).
4. **Execution Dispatch:** Check for shell built-ins; if external, fork child process and invoke `execvp()`.
5. **Job Monitoring:** Parent process waits for child completion via `waitpid()`, unless background flag `&` was specified.

### 2. Built-in Shell Commands
Implement directly within the shell parent process:
- `cd [dir]`: Change current working directory using `chdir()` system call. Supports `cd` (to home directory) and `cd ..`.
- `pwd`: Display current working directory path via `getcwd()`.
- `exit [code]`: Terminate shell process returning specified exit code.
- `help`: Display built-in command documentation.

### 3. I/O Redirection and Pipeline Engine
- **Input Redirection (`< filename`):** Child process opens file read-only and redirects to `stdin` via `dup2(fd, STDIN_FILENO)`.
- **Output Redirection (`> filename` and `>> filename`):** Open file with `O_CREAT | O_WRONLY | O_TRUNC` (or `O_APPEND`) with mode `0644` and redirect to `stdout` via `dup2(fd, STDOUT_FILENO)`.
- **Inter-Process Pipelines (`cmd1 | cmd2 | ... | cmdN`):**
  - Create $N-1$ pipes using `pipe()`.
  - Fork $N$ child processes, chaining the `stdout` of process $k$ to the `stdin` of process $k+1$.
  - Ensure all unused pipe file descriptor ends are closed across parent and children to prevent deadlocks and broken pipe errors.

### 4. Signal Handling
- Configure `sigaction()` to catch `SIGINT` (`Ctrl+C`) and `SIGTSTP` (`Ctrl+Z`).
- The shell itself must ignore `SIGINT` so that pressing `Ctrl+C` terminates only the currently running foreground child process without killing the shell.

---

## Project Milestones

| Milestone | Deliverables | Verification Strategy |
|---|---|---|
| **Phase 1** | REPL & Tokenizer | Basic command execution (`ls`, `whoami`, arguments) verified |
| **Phase 2** | Shell Built-in Commands | `cd`, `pwd`, `exit`, error handling verified |
| **Phase 3** | File Stream Redirection | Redirecting `< input.txt` and `> output.txt` verified with diff tests |
| **Phase 4** | Multi-Stage Pipelines & Signals | Multi-pipe execution (`cat file \| grep key \| wc -l`) and `Ctrl+C` trapping |

---

## Grading Rubric

| Criterion | Evaluation Metric | Weight |
|---|---|---|
| **Process Lifecycle Management** | Flawless `fork()`, `execvp()`, `waitpid()` handling; zero zombie or orphan processes | 25% |
| **Pipeline & Redirection Architecture** | Clean multi-stage pipe implementation with correct descriptor closure | 30% |
| **Built-in Commands & Signals** | Accurate `cd` state tracking, `getcwd()`, robust `SIGINT` handling | 20% |
| **Memory & Resource Safety** | Zero memory leaks under Valgrind, defensive error checking on all system calls | 15% |
| **Code Structure & Documentation** | Clean modular C code, descriptive comments, and test suite execution logs | 10% |

