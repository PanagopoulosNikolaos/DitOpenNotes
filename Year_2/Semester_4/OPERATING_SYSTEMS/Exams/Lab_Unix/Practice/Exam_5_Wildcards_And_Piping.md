# Exam 5: Wildcards and Command Piping

***

## Questions

**Question 1: File Deletion with Wildcards**
You are in a directory containing numerous files. You need to delete all files that start with `backup`, end with `.log`, and are exactly 14 characters long.
- What is the single command to accomplish this using wildcards?

**Question 2: Counting Lines and Piping**
You have a large text file named `syslog.txt`. You want to find out how many words are in the last 15 lines of this file and save the result to a new file named `wordcount.out`.
- Provide the full command line using piping and output redirection.

**Question 3: Listing Specific Files**
Explain what happens when you execute the following command in a UNIX system: `ls -Ral .`

**Question 4: Complex Pattern Matching**
Explain if the command `rm d[a-c]t[12]a` will delete the following files (assume they exist in the current directory): `data1a`, `dct2a`, `dat12a`, `dbt3a`. Provide a brief justification for each.

**Question 5: Appending Output**
You want to search for the word "Error" inside `server.log` and append the matched lines to an existing file named `errors.txt` without overwriting its current contents.
- What command should you use?

***
*Tip: Remember the difference between `>` and `>>` when redirecting output!*
