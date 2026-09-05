# Computer Architecture

## Course Overview
This course provides an in-depth foundation in computer architecture and organization. Topics include Instruction Set Architectures (ISA), MIPS assembly programming, single-cycle and multi-cycle processor datapaths, classic 5-stage pipelining, hazard detection and forwarding, memory hierarchies, cache organization and performance optimization, superscalar execution, and multicore parallel systems.

## Course Code
301 (COMPUTER ARCHITECTURE)

## Prerequisites
* Digital Electronics (Code: 205)
* Logic Design (Code: 104)

---

## Topics Covered
* **Instruction Set Architecture (ISA)**: RISC vs. CISC principles, MIPS instruction formats (R, I, J), register file conventions, memory addressing modes, and system call interfaces.
* **Computer Arithmetic**: Integer representation, two's complement ALU design, carry-lookahead addition, Booth's multiplication algorithm, and division algorithms.
* **Processor Datapath Design**: Single-cycle datapath and control unit synthesis, multi-cycle datapath with finite state machine (FSM) micro-operations.
* **Pipelining and Hazard Resolution**: Classic 5-stage RISC pipeline (IF, ID, EX, MEM, WB), structural hazards, data hazards (RAW, WAR, WAW), forwarding/bypassing units, stall insertion, and branch penalty minimization.
* **Memory Hierarchy and Caching**: Locality of reference (spatial and temporal), cache placement (direct-mapped, set-associative, fully associative), tag/index/offset decomposition, write policies (write-through vs. write-back, write-allocate vs. no-write-allocate), and Average Memory Access Time (AMAT) analysis.
* **Advanced Architectural Concepts**: Instruction-Level Parallelism (ILP), static vs. dynamic branch prediction (2-bit saturating counters), superscalar execution, out-of-order execution concepts (Tomasulo algorithm), multicore architectures, and cache coherence (MESI protocol).

---

## Learning Objectives
* Analyze and write low-level assembly subroutines utilizing standard MIPS calling conventions and stack frame management.
* Design single-cycle and pipelined processor datapaths capable of executing standard instruction subsets.
* Identify pipeline hazards and construct cycle-by-cycle execution timing diagrams incorporating data forwarding and branch delay slots.
* Calculate cache hit rates, miss penalties, and overall AMAT across various memory hierarchy configurations.
* Evaluate performance metrics (CPI, execution time, speedup) using Amdahl's Law and benchmark suites.

---

## Directory Structure

| Directory | Description |
|:---|:---|
| [`Lectures/`](Lectures/) | Structured theory modules covering ISA, pipelining, cache architectures, and multicore parallelism |
| [`Exercises/`](Exercises/) | Solved numerical drills on cache address mapping, AMAT calculation, and pipeline hazard forwarding |
| [`Examples/`](Examples/) | Executable MIPS assembly subroutines and embedded Arduino AVR hardware sketches |
| [`Assignments/`](Assignments/) | Laboratory coursework: Smart City embedded telemetry, MIPS integer calculator, and architecture reports |
| [`Tutorials/`](Tutorials/) | Hands-on guides for the MARS MIPS simulator and register-level AVR embedded interfacing |
| [`Projects/`](Projects/) | Capstone design specification for a cycle-accurate 5-stage pipelined datapath simulator |
| [`Exams/`](Exams/) | 100-point model practice examination with complete worked solutions and grading rubrics |
| [`Resources/`](Resources/) | Conceptual mindmap, deep-dive notes on processor design and technology trends, and reference bibliography |

---

## Tooling and Simulation Environment

### MIPS Assembly Simulation with MARS or SPIM

To assemble and execute MIPS programs via the command-line using SPIM:
```bash
spim -file Examples/examples_mips_assembly_subroutines.s
```

Or using the MARS jar simulator:
```bash
java -jar Mars.jar nc Examples/examples_mips_assembly_subroutines.s
```

### Embedded Arduino AVR Compilation
To compile embedded microcontroller sketches via Arduino CLI:
```bash
cd Examples/Arduino/Program_1
arduino-cli compile --fqbn arduino:avr:uno Program_1.ino
```
