# Exam 3: Advanced Permissions and System Logic


***

## Questions

**Question 1: The Deletion Trap**
You are trying to delete a file `/tmp/cache/old_data.log`. The file has permissions `-r--r--r--` (read-only for everyone). The directory `/tmp/cache/` has permissions `drwx------`. You are the owner of both the directory and the file.
- Can you successfully delete the file `old_data.log`? 
- Explain why or why not based on the rules governing directory versus file permissions.

**Question 2: Forceful Removal**
You need to entirely wipe out a directory named `legacy_code/` and all of its nested contents, and you do not want to be prompted for confirmation at all. 
- What command achieves this? *(Note: Answer carefully, as this is one of the most dangerous commands in UNIX).*

**Question 3: Chaining Symbolic Operations**
Assume a file `app.log` starts with no permissions at all (`000`). You run the following command:
`chmod u+rw,g=r,o+x app.log`
- What is the resulting 3-digit octal number for the file's permissions?

**Question 4: Analyzing Weird States**
You run `ls -l` and notice a directory with the following permissions:
`dr-x-wxrw-  2 user staff 4096 Oct 24 weird_dir/`
Identify the exact functional problems with these permissions for each category:
- What is the owner prevented from doing?
- What is the group prevented from doing?
- Why is the "other" category's permission state effectively useless?

**Question 5: Complex Relative Adjustments**
The directory `weird_dir/` from the previous question currently has permissions `dr-x-wxrw-` (which equates to `536`).
- Using *only* relative symbolic adjustments (meaning you can only use `+` and `-` operators, not the `=` assign operator), write a single `chmod` command to fix the directory permissions to `755`. 
*(Hint: You will need to chain multiple adjustments together separated by commas).*
