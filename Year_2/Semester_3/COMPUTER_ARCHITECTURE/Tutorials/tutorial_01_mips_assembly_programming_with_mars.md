# Tutorial 01: MIPS Assembly Programming with the MARS Simulator

This tutorial provides a practical, hands-on guide to writing, assembling, debugging, and tracing MIPS32 assembly programs using the MARS (MIPS Assembler and Runtime Simulator) environment.

---

## 1. Introduction and Environment Setup

MARS is an interactive simulation environment written in Java designed for learning MIPS assembly programming.

### 1.1 Prerequisites and Launching
Ensure Java Runtime Environment (JRE 8 or newer) is installed:
```bash
java -version
```

- **Graphical Mode (GUI):**
  ```bash
  java -jar Mars.jar
  ```
- **Command-Line Batch Execution (Headless CLI):**
  The `nc` flag suppresses copyright banners, suitable for automated testing:
  ```bash
  java -jar Mars.jar nc program.s
  ```

---

## 2. MARS Interface and Architecture Inspector

```
+-------------------------------------------------------------------------+
| MARS Menu & Toolbar: Assemble (F3), Go (F5), Step (F7), Reset           |
+----------------------------------------------------+--------------------+
| Edit / Execute Tabs                                | Registers Pane     |
| - Text Segment: [Address | Machine Code | Source]  | $zero, $at, $v0... |
| - Data Segment: [0x10010000 static memory]         | $s0-$s7, $t0-$t9   |
| - Messages / Run I/O Console                       | $sp, $fp, $ra, PC  |
+----------------------------------------------------+--------------------+
```

### 2.1 The Two Primary Panes
1. **Edit Tab:** Source code editor with syntax highlighting for directives (`.data`, `.text`, `.word`, `.asciiz`) and instructions.
2. **Execute Tab:** Active after pressing **Assemble (F3)**:
   - **Text Segment:** Displays memory address (starting at `0x00400000`), raw 32-bit machine code in hex, basic disassembled MIPS instructions, and original source statements.
   - **Data Segment:** Displays memory words starting at base address `0x10010000`. Select between ASCII, decimal, or hexadecimal representation.
   - **Registers Tab:** Real-time visual tracking of general-purpose registers (`$0` to `$31`), `PC`, `HI`, and `LO`. Modified registers are highlighted in green during single-stepping.

---

## 3. MIPS System Call (`syscall`) Service Table

To interact with the operating system console and memory allocator, load the service code into `$v0` and invoke `syscall`:

| Service Code (`$v0`) | Operation | Input Arguments | Output Values |
|:---:|:---|:---|:---|
| **1** | Print Integer | `$a0` = integer to print | None |
| **4** | Print String | `$a0` = address of null-terminated string | None |
| **5** | Read Integer | None | `$v0` = integer read from console |
| **8** | Read String | `$a0` = buffer address, `$a1` = maximum buffer length | String read into buffer |
| **9** | Sbrk (Heap Allocate) | `$a0` = number of bytes to allocate | `$v0` = pointer to allocated memory |
| **10** | Exit Program | None | Terminate execution cleanly |
| **11** | Print Character | `$a0` = ASCII character byte | None |

---

## 4. Hands-On Walkthrough: Array Traversal and Maximum Finder

The following complete MIPS assembly program declares an array in `.data`, invokes a subroutine to find the maximum value, and prints the result:

```mips
# array_max.s - Demonstrates array iteration and subroutine call in MARS
.data
    array:      .word 18, 42, -5, 99, 23, 71, 0, -12
    length:     .word 8
    msg_result: .asciiz "The maximum element is: "
    newline:    .asciiz "\n"

.text
.globl main

main:
    # 1. Prepare subroutine arguments
    la $a0, array       # $a0 = base address of array
    lw $a1, length      # $a1 = number of elements (8)

    # 2. Call find_max subroutine
    jal find_max        # Jump and link ($ra = PC + 4)
    move $s0, $v0       # Save returned maximum in $s0

    # 3. Print output message
    li $v0, 4           # Syscall 4: Print String
    la $a0, msg_result
    syscall

    # 4. Print maximum integer
    li $v0, 1           # Syscall 1: Print Integer
    move $a0, $s0
    syscall

    # 5. Print newline
    li $v0, 4
    la $a0, newline
    syscall

    # 6. Exit cleanly
    li $v0, 10          # Syscall 10: Exit
    syscall

# -------------------------------------------------------------
# find_max: Finds maximum integer in a contiguous array
# Args:
#   $a0: Pointer to array base
#   $a1: Element count (assumed >= 1)
# Returns:
#   $v0: Maximum value found
# -------------------------------------------------------------
find_max:
    lw   $v0, 0($a0)        # Initialize max with array[0]
    li   $t0, 1             # Loop index i = 1

max_loop:
    beq  $t0, $a1, max_done # If i == length, exit loop

    # Calculate address offset: offset = i * 4
    sll  $t1, $t0, 2        # $t1 = i << 2
    addu $t2, $a0, $t1      # $t2 = base + offset
    lw   $t3, 0($t2)        # $t3 = array[i]

    # Compare array[i] with current max ($v0)
    ble  $t3, $v0, skip_update
    move $v0, $t3           # Update max: $v0 = array[i]

skip_update:
    addi $t0, $t0, 1        # Increment index: i++
    j    max_loop

max_done:
    jr   $ra                # Return to caller
```

---

## 5. Step-by-Step Debugging Procedure in MARS

1. **Open File:** Press `Ctrl+O` and select `array_max.s`.
2. **Assemble:** Press `F3` (or menu *Run $\to$ Assemble*). The view switches to the Execute tab.
3. **Set Breakpoint:** In the Text Segment table, locate line `find_max` (`0x00400030`) and check the **Bkpt** checkbox.
4. **Run to Breakpoint:** Press `F5`. The program executes until hitting `find_max`.
5. **Inspect Registers:** Look at the right register pane:
   - `$a0` contains `0x10010000` (base of `array`).
   - `$a1` contains `0x00000008`.
   - `$ra` contains `0x00400010` (return address back in `main`).
6. **Single Step (F7):** Press `F7` repeatedly to step through `max_loop`. Notice `$t0` incrementing and `$v0` updating to 42 and subsequently 99.

---

## 6. Common Pitfalls and Troubleshooting

1. **Infinite Execution / Bus Error:** Omitting `li $v0, 10; syscall` causes the CPU to execute instructions past `main` directly into subroutines or uninitialized memory words.
2. **Unaligned Memory Access (`lw`/`sw`):** Attempting to load a 32-bit word from an address where the lowest two bits are not `00` triggers an unaligned memory trap. Always scale word offsets by 4 (`sll $t0, $t0, 2`).
3. **Return Address Clobbering:** In non-leaf functions that call subroutines with `jal`, the caller's return address in `$ra` is overwritten. Always push `$ra` onto the stack frame at entry and pop it before `jr $ra`.

