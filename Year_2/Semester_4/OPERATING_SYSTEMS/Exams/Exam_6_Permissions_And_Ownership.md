# Exam 6: Advanced Permissions and Ownership

This exam tests your ability to interpret and manipulate file permissions using both symbolic and numeric notation, based on real exam scenarios.

***

## Questions

**Question 1: Symbolic Permissions**
You want to ensure that a file named `script.sh`, located in your current directory and owned by you, has read, write, and execute permissions for the owner, but everyone else has only read permissions. 
- Write the full UNIX command to achieve this using numeric (octal) notation.

**Question 2: Interpreting ls -l Output**
Suppose the output of the `ls -l` command includes the following line:
`-r--rwx-wx 1 alice admins 1024 May 12 10:00 project.dat`

Determine if the following statements are True or False:
(a) The user `alice` can modify the contents of `project.dat`.
(b) Any user belonging to the `admins` group can execute `project.dat`.
(c) Users who are neither `alice` nor in the `admins` group cannot read the file.
(d) The `admins` group can delete the file `project.dat` because they have write access to it.

**Question 3: Applying Execution Rights**
What command should you use to grant execute permissions to all users (owner, group, and others) for a program named `compiler` located in the `/usr/local/bin` directory, using the symbolic method?

**Question 4: Default Permissions**
If a user creates a new file, and their `umask` is set to `022`, what will be the default permissions of the newly created file in symbolic notation (e.g., `-rw-r--r--`)?

**Question 5: Changing Ownership**
Write the command to change the owner of the directory `global` and all of its contents to the user `bob`.

***
*Tip: Always analyze the 10-character permission string carefully!*
