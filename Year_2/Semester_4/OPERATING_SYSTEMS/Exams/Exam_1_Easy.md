# Exam 1: Terminal Basics & Introduction to Permissions

Welcome to Exam 1. This test covers standard navigation, file operations, and the basics of UNIX permissions. 

***

## Questions

**Question 1: Navigation**
You are currently in `/home/user/docs`. 
- What command navigates you to `/var/log` using an absolute path? 
- What command navigates you to `/var/log` using a relative path?

**Question 2: Directory Creation**
You are starting a new project and need to create a nested directory structure: `project/src/lib` in your current directory. 
- Write the single command that achieves this without throwing an error if the parent directories do not exist.

**Question 3: Numeric Permissions**
You check a file's permissions and see `-rw-r--r--`. 
- What is the octal (numeric) equivalent of this permission string?

**Question 4: Symbolic Permissions**
You have just created a bash script named `script.sh`. 
- Using symbolic notation (`u`, `g`, `o`), write the command to add execute permission for the owner and the group, while leaving others unchanged.

**Question 5: Applying Permissions**
You have a sensitive file `data.txt` that currently has permissions set to `777`. 
- Write the numeric command to change its permissions so that the owner can read and write, the group can only read, and others have no access whatsoever.

***
*Tip: Write your answers down and test them in your Linux terminal to verify if they work as expected!*
