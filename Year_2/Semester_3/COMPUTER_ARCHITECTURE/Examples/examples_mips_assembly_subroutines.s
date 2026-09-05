#------------------------------------------------------------------------------
# Title: MIPS Assembly Subroutine Demonstrations
# Description: Demonstrates leaf subroutines, non-leaf subroutines with stack
#              frame allocation, and recursive subroutines according to standard
#              MIPS calling conventions.
# Simulator: MARS / SPIM
#------------------------------------------------------------------------------

.data
    # Formatting and banner messages
    msg_banner:     .asciiz "========================================\n MIPS Assembly Subroutines Demonstration\n========================================\n"
    msg_leaf:       .asciiz "\n[1] Leaf Subroutine: arraySum\n"
    msg_leaf_res:   .asciiz "    Sum of array elements: "

    msg_nonleaf:    .asciiz "\n[2] Non-Leaf Subroutine: pythagoreanSum (a^2 + b^2)\n"
    msg_nonleaf_a:  .asciiz "    Inputs: a = 5, b = 12\n"
    msg_nonleaf_res:.asciiz "    Result (5^2 + 12^2): "

    msg_recurse:    .asciiz "\n[3] Recursive Subroutine: factorial(n)\n"
    msg_recurse_n:  .asciiz "    Computing factorial(6)...\n"
    msg_recurse_res:.asciiz "    Result 6!: "

    newline:        .asciiz "\n"

    # Sample dataset for arraySum
    sample_array:   .word 12, 25, 37, 44, 19, 83, -10, 5
    sample_len:     .word 8

.text
.globl main

# =============================================================================
# Main Program Driver
# =============================================================================
main:
    # Print welcome banner
    li   $v0, 4
    la   $a0, msg_banner
    syscall

    # -------------------------------------------------------------------------
    # Demonstration 1: Leaf Subroutine (arraySum)
    # -------------------------------------------------------------------------
    li   $v0, 4
    la   $a0, msg_leaf
    syscall

    la   $a0, sample_array      # $a0 = base address of array
    lw   $a1, sample_len        # $a1 = array length (8)
    jal  arraySum               # Invoke leaf subroutine

    move $s0, $v0               # Preserve returned sum

    li   $v0, 4
    la   $a0, msg_leaf_res
    syscall

    li   $v0, 1
    move $a0, $s0               # Print accumulated sum
    syscall

    li   $v0, 4
    la   $a0, newline
    syscall

    # -------------------------------------------------------------------------
    # Demonstration 2: Non-Leaf Subroutine (pythagoreanSum)
    # -------------------------------------------------------------------------
    li   $v0, 4
    la   $a0, msg_nonleaf
    syscall

    li   $v0, 4
    la   $a0, msg_nonleaf_a
    syscall

    li   $a0, 5                 # Parameter a = 5
    li   $a1, 12                # Parameter b = 12
    jal  pythagoreanSum         # Invoke non-leaf subroutine

    move $s1, $v0               # Preserve result (5^2 + 12^2 = 169)

    li   $v0, 4
    la   $a0, msg_nonleaf_res
    syscall

    li   $v0, 1
    move $a0, $s1
    syscall

    li   $v0, 4
    la   $a0, newline
    syscall

    # -------------------------------------------------------------------------
    # Demonstration 3: Recursive Subroutine (factorial)
    # -------------------------------------------------------------------------
    li   $v0, 4
    la   $a0, msg_recurse
    syscall

    li   $v0, 4
    la   $a0, msg_recurse_n
    syscall

    li   $a0, 6                 # Parameter n = 6
    jal  factorial              # Invoke recursive subroutine

    move $s2, $v0               # Preserve result (6! = 720)

    li   $v0, 4
    la   $a0, msg_recurse_res
    syscall

    li   $v0, 1
    move $a0, $s2
    syscall

    li   $v0, 4
    la   $a0, newline
    syscall

    # -------------------------------------------------------------------------
    # Clean Program Termination
    # -------------------------------------------------------------------------
    li   $v0, 10                # Syscall 10: Exit program
    syscall


# =============================================================================
# Subroutine 1: arraySum (Leaf Subroutine)
# Computes the arithmetic sum of elements in a 32-bit integer array.
# Args:
#   $a0 (int*): Pointer to array base address.
#   $a1 (int):  Number of elements in array.
# Returns:
#   $v0 (int):  Sum of all array elements.
# Register Usage:
#   $t0: Current element loop counter i.
#   $t1: Word offset (i * 4).
#   $t2: Effective address of array[i].
#   $t3: Loaded value array[i].
# =============================================================================
arraySum:
    li   $v0, 0                 # Accumulator: sum = 0
    li   $t0, 0                 # Loop counter: i = 0

arraySum_loop:
    beq  $t0, $a1, arraySum_done # If i == length, terminate loop

    sll  $t1, $t0, 2            # Word byte offset = i * 4
    addu $t2, $a0, $t1          # Effective address = base + offset
    lw   $t3, 0($t2)            # Load array[i]

    addu $v0, $v0, $t3          # sum += array[i]
    addi $t0, $t0, 1            # i++
    j    arraySum_loop

arraySum_done:
    jr   $ra                    # Leaf return: $ra unmodified


# =============================================================================
# Subroutine 2: pythagoreanSum (Non-Leaf Subroutine)
# Computes (a^2 + b^2) by invoking helper subroutine 'square' for each term.
# Args:
#   $a0 (int): Value a.
#   $a1 (int): Value b.
# Returns:
#   $v0 (int): Result of a^2 + b^2.
# Stack Frame Layout (16 bytes allocated):
#   12($sp): Saved return address $ra
#   8($sp):  Saved callee register $s0 (stores a^2)
#   4($sp):  Saved parameter b in $s1
#   0($sp):  Padding for 8-byte stack alignment
# =============================================================================
pythagoreanSum:
    # Subroutine Prologue
    subu $sp, $sp, 16           # Allocate stack frame
    sw   $ra, 12($sp)           # Save return address to caller
    sw   $s0, 8($sp)            # Preserve $s0
    sw   $s1, 4($sp)            # Preserve $s1

    move $s1, $a1               # Save argument b in $s1 before nested call

    # Step 1: Compute square(a)
    jal  square                 # Calls square($a0), result returned in $v0
    move $s0, $v0               # $s0 = a^2

    # Step 2: Compute square(b)
    move $a0, $s1               # $a0 = b
    jal  square                 # Calls square($a0), result returned in $v0

    # Step 3: Add results
    addu $v0, $s0, $v0          # $v0 = a^2 + b^2

    # Subroutine Epilogue
    lw   $s1, 4($sp)            # Restore $s1
    lw   $s0, 8($sp)            # Restore $s0
    lw   $ra, 12($sp)           # Restore original return address
    addu $sp, $sp, 16           # Deallocate stack frame
    jr   $ra                    # Return to caller


# =============================================================================
# Subroutine 3: square (Helper Leaf Subroutine)
# Computes x^2.
# Args:
#   $a0 (int): Number x.
# Returns:
#   $v0 (int): Result x * x.
# =============================================================================
square:
    mul  $v0, $a0, $a0          # $v0 = x * x
    jr   $ra


# =============================================================================
# Subroutine 4: factorial (Recursive Subroutine)
# Computes n! = n * factorial(n - 1) with base case 0! = 1.
# Args:
#   $a0 (int): Non-negative integer n.
# Returns:
#   $v0 (int): Value of n!.
# Stack Frame Layout (8 bytes allocated per recursive invocation):
#   4($sp): Saved return address $ra
#   0($sp): Saved current parameter n
# =============================================================================
factorial:
    # Subroutine Prologue
    subu $sp, $sp, 8            # Allocate 8 bytes for this frame
    sw   $ra, 4($sp)            # Save return address
    sw   $a0, 0($sp)            # Save parameter n

    # Base Case Evaluation: if n <= 1 return 1
    ble  $a0, 1, factorial_base

    # Recursive Step: compute factorial(n - 1)
    addi $a0, $a0, -1           # Set argument to n - 1
    jal  factorial              # Recursive call: $v0 = factorial(n - 1)

    # Unwind and Multiply: $v0 = n * factorial(n - 1)
    lw   $a0, 0($sp)            # Restore n for this frame
    mul  $v0, $a0, $v0          # $v0 = n * (n - 1)!
    j    factorial_epilogue

factorial_base:
    li   $v0, 1                 # 0! = 1, 1! = 1

factorial_epilogue:
    lw   $ra, 4($sp)            # Restore return address
    addu $sp, $sp, 8            # Deallocate stack frame
    jr   $ra                    # Return to previous invocation or caller

