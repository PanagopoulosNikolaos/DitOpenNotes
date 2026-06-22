# 6. UNIX I/O Redirection and Pipes

***

## Standard I/O Streams

In UNIX, every command-line program automatically opens three standard streams (files) when it runs:

| Stream Name                    | File Descriptor | Default Device  | Purpose                                                |
| ------------------------------ | --------------- | --------------- | ------------------------------------------------------ |
| **Standard Input (`stdin`)**   | 0               | Keyboard        | Where the program reads input from.                    |
| **Standard Output (`stdout`)** | 1               | Terminal Screen | Where the program sends its normal output.             |
| **Standard Error (`stderr`)**  | 2               | Terminal Screen | Where the program sends error and diagnostic messages. |

I/O Redirection allows you to detach these streams from their default devices and connect them to files or other programs.

***

## Output Redirection

### Overwrite Output (`>`)

Redirects `stdout` to a file. If the file does not exist, it is created. **If the file already exists, it is completely overwritten.**

**Syntax:**
```sh
command > filename
```

**Examples:**
```sh
echo "Hello, World!" > greeting.txt
ls -l > directory_listing.txt
```
*(The output is not printed to the screen; it goes directly into the file.)*

### Append Output (`>>`)

Redirects `stdout` to a file. **If the file exists, the new output is appended to the end of the file.** It does not overwrite the existing contents.

**Syntax:**
```sh
command >> filename
```

**Example:**
```sh
echo "New line of text" >> greeting.txt
```

***

## Error Redirection

By default, error messages bypass standard output redirection and still print to the screen. To capture errors in a file, you must redirect `stderr` specifically.

### Redirect `stderr` (`2>`)

**Syntax:**
```sh
command 2> error_log.txt
```

**Example:**
```sh
ls /nonexistent_directory 2> errors.txt
```

### Redirect both `stdout` and `stderr`

You can redirect both streams to the same file.

**Syntax:**
```sh
command > output_and_errors.txt 2>&1
```
*(This tells the shell to send descriptor 2 to wherever descriptor 1 is currently pointing.)*

Modern bash shells also support a shorthand for this:
```sh
command &> output_and_errors.txt
```

***

## Input Redirection

### Redirect `stdin` (`<`)

Feeds the contents of a file into a command as if it were typed on the keyboard.

**Syntax:**
```sh
command < input_file
```

**Example:**
```sh
wc -l < data.txt
```
*(Counts the lines in `data.txt`. Note: Unlike `wc -l data.txt`, using input redirection will only output the number, without printing the filename.)*

***

## Pipes (`|`)

Pipes are one of the most powerful features in UNIX. A pipe connects the `stdout` of one command directly to the `stdin` of another command. This allows you to chain small programs together to perform complex tasks without creating temporary files.

**Syntax:**
```sh
command1 | command2 | command3
```

**How it works:**
The output of `command1` becomes the input for `command2`. The output of `command2` becomes the input for `command3`. Only the final output is printed to the screen.

**Examples:**

1. **Viewing long output:**
   ```sh
   ls -l /etc | less
   ```
   *(Passes the long directory listing into `less` for easier scrolling.)*

2. **Counting files in a directory:**
   ```sh
   ls -1 | wc -l
   ```
   *(Lists files one per line, then passes that list to `wc -l` to count the lines.)*

3. **Finding specific processes:**
   ```sh
   ps aux | grep "python"
   ```
   *(Lists all running processes, then filters that list to show only lines containing "python".)*

4. **Complex chaining:**
   ```sh
   cat access.log | awk '{print $1}' | sort | uniq -c | sort -nr | head -10
   ```
   *(Reads a web server log, extracts IP addresses, sorts them, counts unique occurrences, sorts by highest count, and shows the top 10.)*
