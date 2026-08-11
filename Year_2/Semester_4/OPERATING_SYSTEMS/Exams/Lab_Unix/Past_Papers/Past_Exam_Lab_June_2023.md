# Laboratory Examination - June 2023

## Question 1 (0.5)
Your current directory in a Unix system is `/local/home/student/project1`. You want to create a directory named `student1` inside the directory `/local/home/teacher`. Provide the complete UNIX command to achieve this using a relative path.

## Question 2 (0.5)
Your current directory in a UNIX connection is `/home/paul/data`. Provide the complete UNIX command to set `/home/peter/files` as the current directory using a relative path.

## Question 3 (0.5)
What will happen if the command `ls -Ral .` is executed on a UNIX system?

## Question 4 (0.5)
What command would you use to delete all files in your current directory that start with `grade`, end with `.tmp`, and consist of exactly 15 characters total?

## Question 5 (1)
You want to ensure that the file `photo` in the current directory, which belongs to you, has read, write, and execute permissions for you, while all others have only write permission. What would be the complete Unix command you need to execute using numeric (octal) permission specification?

## Question 6 (0.5)
What command line would you use to save to the file `lines.out` the number of words and characters belonging to the last 5 lines of the file `file.txt` (which contains various text lines) (Hint: you need to use piping and output redirection).

## Question 7 (0.5)
What command would you use to move the directory `global` located in the current directory along with all its contents to the `/local` directory?

## Question 8 (1)
(Warning!!! There is negative grading for wrong answers. One wrong answer cancels one correct one.)
Assuming that the output of the command `ls -l` shows the following line:
`-r--rwxw-x 1 ray green 12 March 15 11:54 grades`

Complete which of the following statements are true or false.
(a) `green` can modify `grades` (True/False) : ________
(b) `ray` can modify the contents of `grades` (True/False) : ________
(c) Only someone who does not belong to the group (group) of `grades` can see its contents (True/False) : ________
(d) Only the file group and owner can modify `grades` (True/False) : ________

## Question 9 (0.5)
What commands must you use to grant the necessary permissions to ensure that any user can execute the program with filename `mail` located in the `/computer` directory? You will use the symbolic (B) method of specifying permissions.

## Question 10 (0.5)
Explain whether executing the command `rm a[bcd]ef` would delete the files named `abcdef`, `abdfce`, or `abfedc`. Assume they are in the current directory.

## Question 11 (1)
Explain what will happen if we execute the command `chmod 761 tmp` (It is not sufficient to mention only what the chmod command does in general).

## Question 12 (1)
What command would you use to display sorted only files that start with the character `a` and end with `.txt` in your current directory?

## Question 13 (1)
You have written a program that reads temperatures from the keyboard for a city, with each temperature on a different line, and then finds the maximum among them and displays it as output. The program is executed with the command `maxtemp`. In a file `temps` you have placed 5 temperatures, one on each line, consisting of two numeric digits. What complete command would you give to save the maximum temperature of the 5 temperatures to the file `maxtemps.txt`?

## Question 14 (1)
What command would you use to create a symbolic link to the file `/local/host/files` in the `links` directory located in `/local` using a relative path?

## Question 15 (0.5)
Explain what a Unix system would try to do if we attempt to execute the following command on one line: `cp cp head`.