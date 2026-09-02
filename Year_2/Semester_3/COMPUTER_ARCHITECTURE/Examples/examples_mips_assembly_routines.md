# Παραδείγματα: Υλοποίηση Συναρτήσεων και Διαχείριση Στοίβας σε MIPS

## Παράδειγμα 1: Αναστροφή Συμβολοσειράς στη Θέση της (In-Place String Reverse)

### Περιγραφή
Συνάρτηση σε MIPS Assembly που δέχεται ως είσοδο τη διεύθυνση μιας τερματιζόμενης με `\0` συμβολοσειράς στον καταχωρητή `$a0` και την αντιστρέφει επιτόπου (in-place).

### Πλήρης Κώδικας MIPS
```assembly
.data
    str: .asciiz "Computer Architecture DIT"

.text
.globl main

main:
    la   $a0, str
    jal  reverse_string

    # Εκτύπωση αντεστραμμένου string
    li   $v0, 4
    la   $a0, str
    syscall

    # Έξοδος
    li   $v0, 10
    syscall

# Συνάρτηση reverse_string
# Είσοδος: $a0 = διεύθυνση αρχής string
reverse_string:
    move $t0, $a0        # $t0: δείκτης αρχής (start pointer)
    move $t1, $a0        # $t1: δείκτης τέλους (end pointer)

find_end:
    lb   $t2, 0($t1)
    beqz $t2, end_found  # Βρέθηκε το '\0'
    addi $t1, $t1, 1
    j    find_end

end_found:
    addi $t1, $t1, -1    # $t1 δείχνει στον τελευταίο έγκυρο χαρακτήρα

reverse_loop:
    bge  $t0, $t1, done_reverse # Αν start >= end, ολοκληρώθηκε

    # Ανταλλαγή χαρακτήρων
    lb   $t3, 0($t0)
    lb   $t4, 0($t1)
    sb   $t4, 0($t0)
    sb   $t3, 0($t1)

    addi $t0, $t0, 1     # start++
    addi $t1, $t1, -1    # end--
    j    reverse_loop

done_reverse:
    jr   $ra
```

---

## Παράδειγμα 2: Αναδρομικός Υπολογισμός Ακολουθίας Fibonacci με Διαχείριση Στοίβας (Stack Frame)

### Περιγραφή
Υλοποίηση της αναδρομικής συνάρτησης $F(n)$:
$$F(0) = 0, \quad F(1) = 1, \quad F(n) = F(n-1) + F(n-2)$$

### Πλήρης Κώδικας MIPS
```assembly
# Συνάρτηση fibonacci
# Είσοδος: $a0 = n
# Έξοδος:   $v0 = F(n)

fib:
    # Δέσμευση χώρου στη στοίβα (12 bytes για $ra, $s0, $s1)
    addi $sp, $sp, -12
    sw   $ra, 8($sp)
    sw   $s0, 4($sp)
    sw   $s1, 0($sp)

    move $s0, $a0        # $s0 = n

    # Βασικές περιπτώσεις: αν n == 0 επιστρέφει 0, αν n == 1 επιστρέφει 1
    li   $v0, 0
    beq  $s0, $zero, fib_exit

    li   $v0, 1
    beq  $s0, 1, fib_exit

    # Κλήση fib(n-1)
    addi $a0, $s0, -1
    jal  fib
    move $s1, $v0        # $s1 = fib(n-1)

    # Κλήση fib(n-2)
    addi $a0, $s0, -2
    jal  fib             # $v0 = fib(n-2)

    # Άθροιση αποτελεσμάτων
    add  $v0, $s1, $v0   # $v0 = fib(n-1) + fib(n-2)

fib_exit:
    # Αποκατάσταση καταχωρητών και αποδέσμευση στοίβας
    lw   $s1, 0($sp)
    lw   $s0, 4($sp)
    lw   $ra, 8($sp)
    addi $sp, $sp, 12
    jr   $ra
```

