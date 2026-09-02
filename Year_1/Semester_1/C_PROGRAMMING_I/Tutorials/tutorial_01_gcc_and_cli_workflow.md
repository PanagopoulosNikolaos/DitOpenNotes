# Εργαστηριακός Οδηγός 1: Μεταγλώττιση με τον GCC και Ροή Εργασίας Τερματικού

## 1. Εισαγωγή στον Μεταγλωττιστή GCC

Ο μεταγλωττιστής GCC (GNU Compiler Collection) αποτελεί το βασικό εργαλείο μεταγλώττισης κώδικα C σε περιβάλλοντα Linux και Unix.

### Βασική Εντολή Μεταγλώττισης
```bash
gcc -Wall -Wextra -std=c11 -O2 main.c -o my_program
```

### Σημαίες Μεταγλώττισης (Flags)
* `-Wall`: Ενεργοποιεί όλες τις τυπικές προειδοποιήσεις (warnings) για δυνητικά σφάλματα.
* `-Wextra`: Ενεργοποιεί πρόσθετες χρήσιμες προειδοποιήσεις.
* `-std=c11`: Καθορίζει το πρότυπο ISO C11.
* `-g`: Προσθέτει σύμβολα αποσφαλμάτωσης για χρήση με το εργαλείο GDB.
* `-o <name>`: Ορίζει το όνομα του παραγόμενου εκτελέσιμου αρχείου.

---

## 2. Μεταγλώττιση Πολλαπλών Αρχείων και Makefiles

Όταν ένα έργο αποτελείται από πολλαπλά αρχεία `.c` και `.h`, χρησιμοποιούμε `Makefile` για αυτοματοποίηση της διαδικασίας.

### Παράδειγμα `Makefile`
```makefile
CC = gcc
CFLAGS = -Wall -Wextra -std=c11 -g
TARGET = program
OBJS = main.o utils.o

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CC) $(OBJS) -o $(TARGET)

main.o: main.c utils.h
	$(CC) $(CFLAGS) -c main.c

utils.o: utils.c utils.h
	$(CC) $(CFLAGS) -c utils.c

clean:
	rm -f $(OBJS) $(TARGET)
```
