# Exam 4: Expert Challenge


***

## Questions

**Question 1: Understanding Umask**
Your system's default `umask` is currently set to `027`.
- If you create a brand new regular text file, what will be its exact numeric AND symbolic permissions?
- If you create a brand new directory, what will be its exact numeric AND symbolic permissions?
*(Show your math based on the default maximums for files and directories).*

**Question 2: Ownership Transfers**
You have written a deployment script named `deploy.sh`. You need to hand over ownership of this file to the system user `jenkins` and change its group ownership to `devops`.
- Write the single command to accomplish both changes simultaneously.

**Question 3: One-Shot Complex Permission Flip**
Consider a file `database.db` that currently has the permissions `653` (`-rw-r-x-wx`). 
You need to change the permissions such that:
- The owner loses write access but gains execute access.
- The group gains write access.
- Others lose all access.
Write the single symbolic `chmod` command (using `+` and `-`) to achieve this. What is the final numeric permission of the file?

**Question 4: Link Behaviors**
You need to create a symbolic (soft) link named `current_log` in your current directory that points to `/var/log/syslog`.
- What is the command to create this link?
- If you subsequently run `rm current_log`, does it delete the original `/var/log/syslog` file, or just the link?

**Question 5: The "Permission Denied" Mystery**
A junior developer complains about an access issue. They belong to the `other` category for a specific directory. 
They demonstrate that they can run `ls /var/www/html` and successfully see `index.html` listed in the output. 
However, when they type `cat /var/www/html/index.html`, they immediately get a "Permission denied" error. 

You inspect the file and see it has permissions `-rw-r--r--` (so `other` clearly has read access to the file).
- Based on UNIX permission rules, what specific permission bit is missing on the `/var/www/html` directory for the `other` category that is causing this error? Explain why.
