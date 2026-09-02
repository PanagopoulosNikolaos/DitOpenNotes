#-------------------------------
#©Panagopoulos, Nikolaos, 2025.
#All rights reserved.
#-------------------------------

# MIPS Calculator Program

.data
    # Prompts for user information
    msg_welcome:        .asciiz "--- MIPS Calculator ---\n"
    prompt_name:        .asciiz "Enter your full name: "
    prompt_am:          .asciiz "Enter your student registration number (AM): "
    prompt_semester:    .asciiz "Enter your current semester: "
    
    # Prompts for calculator operations
    prompt_num1:        .asciiz "Enter the first number: "
    prompt_num2:        .asciiz "Enter the second number: "
    prompt_op:          .asciiz "Choose operation (1: Add, 2: Sub, 3: Mul, 4: Div, 5: Square): "
    
    # Result messages
    msg_add_prefix:     .asciiz "Addition: "
    msg_sub_prefix:     .asciiz "Subtraction: "
    msg_mul_prefix:     .asciiz "Multiplication: "
    msg_div_prefix:     .asciiz "Division: "
    msg_sqr_prefix:     .asciiz "Square: "
    
    msg_add_sym:        .asciiz " + "
    msg_sub_sym:        .asciiz " - "
    msg_mul_sym:        .asciiz " * "
    msg_div_sym:        .asciiz " / "
    msg_sqr_sym:        .asciiz "^2"
    msg_equals:         .asciiz " = "
    
    msg_exit_am:        .asciiz "\nAM detected. Terminating program...\n"
    msg_div_zero:       .asciiz "Error: Division by zero!\n"
    
    # Buffers for strings
    name_buffer:        .space 64
    semester_buffer:    .space 32

.text
.globl main

# Main entry point
# Register Usage:
# $s0: Student AM (stored for termination check)
# $s1: First input number
# $s2: Second input number
# $t0: Operation choice / Temporary
# $t1: Comparison values / Result temporary
main:
    # --- User Information Gathering ---
    
    # Print Welcome Header
    li $v0, 4
    la $a0, msg_welcome
    syscall

    # Prompt and read Name
    li $v0, 4
    la $a0, prompt_name
    syscall
    
    li $v0, 8
    la $a0, name_buffer
    li $a1, 64
    syscall
    
    # Prompt and read AM
    li $v0, 4
    la $a0, prompt_am
    syscall
    
    li $v0, 5
    syscall
    move $s0, $v0       # Store AM in $s0 for later comparison
    
    # Prompt and read Semester
    li $v0, 4
    la $a0, prompt_semester
    syscall
    
    li $v0, 8
    la $a0, semester_buffer
    li $a1, 32
    syscall

    # Print a newline to separate info from calculator
    li $v0, 11
    li $a0, 10
    syscall

# --- Main Calculator Loop ---
calc_loop:
    # 1. Get two numbers first
    # Prompt and read first number
    li $v0, 4
    la $a0, prompt_num1
    syscall
    li $v0, 5
    syscall
    move $s1, $v0
    beq $s1, $s0, exit_am   # AM check
    
    # Prompt and read second number
    li $v0, 4
    la $a0, prompt_num2
    syscall
    li $v0, 5
    syscall
    move $s2, $v0
    beq $s2, $s0, exit_am   # AM check

    # 2. Prompt for operation after numbers
    li $v0, 4
    la $a0, prompt_op
    syscall
    
    li $v0, 5
    syscall
    move $t0, $v0       # Operation choice in $t0
    
    # Branch to specific operation
    li $t1, 1
    beq $t0, $t1, do_add
    li $t1, 2
    beq $t0, $t1, do_sub
    li $t1, 3
    beq $t0, $t1, do_mul
    li $t1, 4
    beq $t0, $t1, do_div
    li $t1, 5
    beq $t0, $t1, do_square
    
    # If invalid choice, loop back
    j calc_loop

# --- Arithmetic Operations ---

do_add:
    la $a0, msg_add_prefix
    la $a1, msg_add_sym
    jal print_binary_header
    add $a0, $s1, $s2
    j print_final_val

do_sub:
    la $a0, msg_sub_prefix
    la $a1, msg_sub_sym
    jal print_binary_header
    sub $a0, $s1, $s2
    j print_final_val

do_mul:
    la $a0, msg_mul_prefix
    la $a1, msg_mul_sym
    jal print_binary_header
    mul $a0, $s1, $s2
    j print_final_val

do_div:
    beq $s2, $zero, div_zero_error
    la $a0, msg_div_prefix
    la $a1, msg_div_sym
    jal print_binary_header
    div $a0, $s1, $s2
    j print_final_val

do_square:
    li $v0, 4
    la $a0, msg_sqr_prefix
    syscall
    li $v0, 1
    move $a0, $s1
    syscall
    li $v0, 4
    la $a0, msg_sqr_sym
    syscall
    li $v0, 4
    la $a0, msg_equals
    syscall
    mul $a0, $s1, $s1
    j print_final_val

# --- Helper Labels ---

# Helper to print "Prefix: num1 Symbol num2 = "
# $a0: prefix string, $a1: symbol string
print_binary_header:
    move $t2, $a0       # Save prefix
    move $t3, $a1       # Save symbol
    li $v0, 4
    move $a0, $t2
    syscall
    li $v0, 1
    move $a0, $s1
    syscall
    li $v0, 4
    move $a0, $t3
    syscall
    li $v0, 1
    move $a0, $s2
    syscall
    li $v0, 4
    la $a0, msg_equals
    syscall
    jr $ra

print_final_val:
    li $v0, 1           # Print integer result in $a0
    syscall
    li $v0, 11          # Print newline
    li $a0, 10
    syscall
    j calc_loop

div_zero_error:
    li $v0, 4
    la $a0, msg_div_zero
    syscall
    j calc_loop

exit_am:
    li $v0, 4
    la $a0, msg_exit_am
    syscall
    j terminate

terminate:
    # Exit syscall
    li $v0, 10
    syscall
