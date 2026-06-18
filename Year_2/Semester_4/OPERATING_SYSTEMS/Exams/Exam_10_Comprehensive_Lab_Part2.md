# Exam 10: Comprehensive Lab Part 2 - Analysis and Permissions


***

## Questions

**Question 1: Extracting File Information**
Write a command to extract the first 10 lines of the file `data.csv`, then sort those lines alphabetically, and finally display them on the screen. (Use piping).

**Question 2: Permission Analysis**
A directory `reports` has the permissions `drwxr-xr--`. A user named `john`, who is not the owner and not in the group associated with the directory, attempts to run the command `ls reports`. 
- Will the command succeed? Explain why or why not.

**Question 3: Modifying Permissions Numerically**
A file `database.db` currently has permissions `-rw-rw-r--`. 
- Provide the single numeric `chmod` command to change the permissions such that the owner has full rights (read, write, execute), the group has read and execute, and others have no rights.

**Question 4: Advanced Wildcards**
Explain what the following command does: `cp *[0-9]*.jpg ~/images/`
- What kind of files will be copied, and where will they be placed?

**Question 5: Searching Inside Files**
Write a command to search for the exact string "Failed password" inside all files in the current directory and its subdirectories, displaying the line number alongside the matching text.

***
*Tip: Breaking down piped commands step-by-step is the easiest way to ensure your logic is sound.*

