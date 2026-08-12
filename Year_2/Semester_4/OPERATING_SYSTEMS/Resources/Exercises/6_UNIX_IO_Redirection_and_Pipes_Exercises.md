# Exercises — UNIX I/O Redirection and Pipes

**Based on:** `6_UNIX_IO_Redirection_and_Pipes.md`  
**Number of exercises:** 30

---

## Part A — Theory

### Exercise 1
Describe the three standard I/O streams in UNIX: stdin, stdout, stderr. What are their file descriptors?

---

### Exercise 2
Explain the difference between `>` and `>>`. Give an example for each.

---

### Exercise 3
Why are error messages (stderr) not redirected automatically when using `command > file`?

---

### Exercise 4
Explain the notation `2>&1`. What does `2>` mean?

---

### Exercise 5
What is the difference between `wc -l data.txt` and `wc -l < data.txt` in terms of output?

---

### Exercise 6
Explain the function of the pipe (`|`). Why is it considered a powerful tool in the UNIX philosophy?

---

### Exercise 7
Mark **T** (True) or **F** (False):

1. stdin has file descriptor 0.
2. The `>` redirection replaces the contents of an existing file.
3. `ls /nonexistent 2> errors.txt` saves only the errors.
4. The pipe creates a temporary file on disk to transfer data.
5. The short form `command &> file` redirects stdout and stderr.

---

## Part B — Laboratory

### Exercise 8
Give the command to save the output `Hello, World!` to the file `greeting.txt` (using `echo`).

---

### Exercise 9
Give the command to save the output of `ls -l` to `directory_listing.txt`.

---

### Exercise 10
The file `greeting.txt` already exists. Give the command to **append** the line `New line of text` to its end, without replacing the existing content.

---

### Exercise 11
Give the command so that the errors of `ls /nonexistent_directory` are saved to `errors.txt`.

---

### Exercise 12
Give the command so that **both** the normal output **and** the errors of `find / -name "*.conf"` are saved to `output_and_errors.txt` (classic `2>&1` notation).

---

### Exercise 13
Give the command to count the lines of `data.txt` using input redirection.

---

### Exercise 14
Give the command to view the output of `ls -l /etc` through `less`.

---

### Exercise 15
Give the command to count the number of files in the current directory (one entry per line).

---

### Exercise 16
Give the command to find processes containing the word `python` (using `ps` and `grep`).

---

### Exercise 17
Give the command to save to `lines.out` the number of words and characters of the **last 5 lines** of `file.txt`.

---

### Exercise 18
Give the command to sort the contents of `names.txt` and save the result to `sorted_names.txt`.

---

### Exercise 19
Give the command to display the 10 most frequent words in `document.txt` (hint: `tr`, `sort`, `uniq -c`, `sort -nr`, `head`).

---

### Exercise 20
Give the command so that `date` writes the current date to `log.txt` and simultaneously displays it on the screen (hint: `tee`).

---

## Part C — Complex Questions

### Exercise 21
Analyze the complex command:

```sh
cat access.log | awk '{print $1}' | sort | uniq -c | sort -nr | head -10
```

What does each stage of the pipeline do?

---

### Exercise 22
What will happen if the following is executed:

```sh
echo "first" > file.txt
echo "second" > file.txt
```

What is the difference if the second `>` is replaced with `>>`?

---

### Exercise 23
The command `grep "error" log.txt > results.txt 2> grep_errors.txt` what does it save to each file?

---

### Exercise 24
Why is the "chaining programs" philosophy of UNIX ideally implemented with pipes instead of temporary files?

---

### Exercise 25
Circle the correct answer: Which command counts lines **without** displaying the file name in the output?

- a) `wc -l data.txt`  
- b) `wc -l < data.txt`  
- c) `cat data.txt | wc`  
- d) b) and c)

---

### Exercise 26
Draw a flow diagram for: `ls -l | grep ".txt" | wc -l`

---

### Exercise 27
A student wants to save the output of `cal 2026` to `calendar.txt` and any errors to `cal_errors.txt`. Give the command.

---

### Exercise 28
Mark **T** or **F**:

1. In a pipeline, the output of the last command is displayed on the screen unless it is redirected.
2. `2>&1` must be placed after `>` for the correct redirection of both streams.
3. Input redirection `<` feeds a file as stdin.
4. stderr has file descriptor 3.
5. `command &> file` is equivalent to `command > file 2>&1` in bash.

---

### Exercise 29
Describe step by step what happens when `sort < unsorted.txt | head -5 > top5.txt` is executed.

---

### Exercise 30
Give one command (or pipeline) that: (1) reads `grades.txt`, (2) sorts the lines numerically, (3) displays the 3 smallest values, (4) saves the result to `bottom3.txt`.
