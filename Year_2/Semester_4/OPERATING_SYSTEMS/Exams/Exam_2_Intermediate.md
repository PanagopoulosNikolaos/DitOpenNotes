# Exam 2: Intermediate File Management and Permission Scenarios

This exam increases the difficulty by combining flags and requiring a deeper understanding of how directory permissions differ from file permissions.

***

## Questions

**Question 1: Copying Safely**
You are in `/home/ice/work`. You want to copy the directory `/etc/config` and all its contents into your current directory. However, you want the system to prompt you before overwriting any files that might already exist in your current directory. 
- What command do you use?

**Question 2: Moving and Renaming**
You have a file named `report.txt` in your current directory. You want to rename it to `final_report.txt` and move it to the parent directory (`..`) at the exact same time. 
- What is the single command to do this?

**Question 3: Decoding Permissions**
A script file has the permission string `-rwxr-x--x`. 
- Break down exactly what actions the owner, the group, and others can perform on this file.
- What is the 3-digit octal equivalent of this permission string?

**Question 4: Directory Permissions**
A directory `shared_folder/` has the permissions `drw-rw-rw-`. A user in the group tries to enter the directory using `cd shared_folder` but gets a "Permission denied" error.
- Why can't the user enter the directory despite having read and write permissions?
- Write the numeric `chmod` command to fix the directory permissions so that everyone can enter and list files, but only the owner can create or delete files inside it.

**Question 5: Translating Modifiers**
You execute the command `chmod 640 secret.txt`.
- What is the final 10-character symbolic string representation of this file (e.g., `-rwx...`)?
- Using a single symbolic `chmod` command (using the `=` operator), how would you change the permissions of `secret.txt` from `640` directly to `755`?
