# Assignment 01: Shell Scripting and Automated Web Log Processing

This coursework assignment evaluates practical competency in POSIX Bash shell scripting, pipeline filter chaining, regular expressions, exit code handling, and automated text log parsing.

---

## 1. Problem Specification

You are provided with an Apache Common Log Format access trace (`access.log`). Each entry follows the format:

```text
192.168.1.105 - - [04/Sep/2026:14:32:10 +0000] "GET /api/v1/users HTTP/1.1" 200 4520
```

Where fields correspond to:
1. `Client IP`
2. `Identd`
3. `Authuser`
4. `Timestamp`
5. `HTTP Request Method & Path`
6. `HTTP Status Code`
7. `Response Body Bytes`

---

## 2. Script Requirements

Develop a self-contained, executable Bash script named `log_analyzer.sh` that accepts command-line arguments:

```bash
./log_analyzer.sh [OPTIONS] <logfile>
```

### Supported Flags
- `-u, --unique-ips`: Output the total count of distinct client IP addresses that made requests.
- `-t, --top-ips <N>`: Output the top $N$ most frequent client IP addresses, formatted as:
  ```text
  COUNT    IP_ADDRESS
  ```
- `-e, --errors`: Filter and output all requests resulting in client or server HTTP errors (status codes $400 \le \text{status} \le 599$).
- `-b, --bandwidth`: Compute and output the sum of total bytes served across all successful requests (status code 200), converted to Megabytes ($1 \text{ MB} = 10^6 \text{ bytes}$).
- `-h, --help`: Display clear usage documentation and exit with status code 0.

### Defensive Scripting Constraints
1. Must verify that the specified log file exists and is readable; if not, output a clean error to `stderr` and exit with status `1`.
2. Must validate that argument $N$ for `--top-ips` is a positive integer.
3. Must use modular shell functions and adhere to clean indentation.
4. Must not generate temporary files in `/tmp` or the local directory.

---

## 3. Evaluation Rubric

| Criteria | Points |
|---|---|
| Correct argument parsing (`getopts` or custom `while/case` loop) and error handling | 20 |
| Correct extraction of unique IPs and top-$N$ rankings using pipeline filters | 30 |
| Correct HTTP error filtering and regex pattern precision | 25 |
| Bandwidth byte aggregation and unit conversion logic | 15 |
| Script structure, defensive programming, and zero external file residue | 10 |

