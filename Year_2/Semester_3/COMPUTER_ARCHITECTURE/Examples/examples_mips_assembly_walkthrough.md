# MIPS Assembly Subroutines: Architectural Walkthrough

This document provides an architectural walkthrough and stack memory layout analysis for the assembly implementations in [`examples_mips_assembly_subroutines.s`](examples_mips_assembly_subroutines.s).

---

## 1. Overview of Calling Conventions

In MIPS32 ABI (Application Binary Interface):
- **Arguments:** Passed in registers `$a0` through `$a3`. Any additional arguments are spilled onto the caller's stack frame.
- **Return Values:** Returned in `$v0` (and `$v1` for 64-bit results).
- **Temporary Registers (`$t0` - `$t9`):** Caller-saved. A called subroutine is free to overwrite them without preservation.
- **Saved Registers (`$s0` - `$s7`):** Callee-saved. If a subroutine modifies any `$s` register, it must save the original value on the stack during its prologue and restore it in its epilogue.
- **Return Address (`$ra`):** Contains the return address back to the caller. Leaf procedures can leave `$ra` untouched; non-leaf procedures must save `$ra` on the stack before invoking another subroutine via `jal`.

---

## 2. Subroutine Analysis & Memory Mechanics

### 2.1 Leaf Subroutine: `arraySum`
A **Leaf Subroutine** does not invoke any further procedures (`jal` is never called).
- **Stack Requirement:** Zero bytes. Because `$ra` is never overwritten, the return address remains intact in register `$ra`.
- **Register Allocation:** Uses temporary registers `$t0 - `$t3` for loop counters, offsets, and element loads.
- **Memory Addressing:** Implements word scaling via logical left shift:
  ```mips
  sll  $t1, $t0, 2      # Computes byte offset = index * 4
  addu $t2, $a0, $t1    # Address = array_base + byte_offset
  lw   $t3, 0($t2)      # Load 32-bit word
  ```

---

### 2.2 Non-Leaf Subroutine: `pythagoreanSum`
`pythagoreanSum` computes $a^2 + b^2$ by calling the helper subroutine `square` twice.

#### The Stack Frame (Activation Record)
Because `jal square` overwrites `$ra` with the return address inside `pythagoreanSum`, the original caller's return address would be destroyed if not saved to the stack. Furthermore, `$s0` and `$s1` are used to persist intermediate results across the function call.

```
High Memory
+-------------------------------+  <- Stack pointer at entry ($sp_old)
| Return Address to main ($ra)  |  12($sp)
+-------------------------------+
| Saved $s0 (stores a^2)        |  8($sp)
+-------------------------------+
| Saved $s1 (stores parameter b)|  4($sp)
+-------------------------------+
| Unused alignment padding      |  0($sp)
+-------------------------------+  <- Current Stack pointer ($sp_new)
Low Memory
```

#### Step-by-Step Flow:
1. **Prologue:** Allocate 16 bytes on the stack (`subu $sp, $sp, 16`) and store `$ra`, `$s0`, and `$s1`.
2. **First Call:** Compute $a^2$ via `jal square`. Save result from `$v0` into `$s0`.
3. **Second Call:** Move preserved parameter $b$ from `$s1` into `$a0`. Invoke `jal square`.
4. **Summation:** Add saved $a^2$ (`$s0`) to returned $b^2$ (`$v0`).
5. **Epilogue:** Restore `$s1`, `$s0`, `$ra` from the stack, deallocate the 16 bytes (`addu $sp, $sp, 16`), and return via `jr $ra`.

---

### 2.3 Recursive Subroutine: `factorial`
`factorial(n)` computes $n! = n \times (n - 1)!$ using recursive stack frame allocation.

#### Recursive Stack Growth ($n = 6$)
Each recursive invocation pushes an 8-byte frame storing its specific $n$ and the return address to the instruction directly following `jal factorial`.

```
Call factorial(6) -> Allocates 8 bytes [ra, n=6]
  Call factorial(5) -> Allocates 8 bytes [ra, n=5]
    Call factorial(4) -> Allocates 8 bytes [ra, n=4]
      Call factorial(3) -> Allocates 8 bytes [ra, n=3]
        Call factorial(2) -> Allocates 8 bytes [ra, n=2]
          Call factorial(1) -> Allocates 8 bytes [ra, n=1] -> Base Case (returns 1)
```

#### Unwinding Phase:
1. When $n \le 1$, the function sets `$v0 = 1$`, restores `$ra`, and returns without making a further call.
2. The caller ($n = 2$) restores its $n = 2$ from `0($sp)`, multiplies $2 \times 1 = 2$, and returns `$v0 = 2$`.
3. Successive frames restore $n$ and multiply until $n = 6$ computes $6 \times 120 = 720$.
4. Peak stack allocation: $6 \text{ frames} \times 8 \text{ bytes} = 48 \text{ bytes}$.

---

## 3. How to Run and Trace in Simulators

### 3.1 Executing via SPIM
```bash
spim -file examples_mips_assembly_subroutines.s
```

### 3.2 Executing via MARS
- Open MARS GUI:
  ```bash
  java -jar Mars.jar
  ```
- Open `examples_mips_assembly_subroutines.s` and assemble (`F3`).
- Set breakpoints on `arraySum`, `pythagoreanSum`, and `factorial`.
- Press `F5` to execute and inspect stack address changes in the Data Segment window at `0x7ffffffc`.

