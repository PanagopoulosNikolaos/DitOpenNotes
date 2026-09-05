# Computer Architecture: Curated Resources and Reference Guide

A curated reference guide of authoritative textbooks, ISA technical specifications, processor simulators, and hardware description tools for **Computer Architecture (Course Code: 301)**.

---

## 1. Foundational Textbooks

- **Computer Organization and Design: The Hardware/Software Interface (MIPS Edition)**  
  *Authors:* David A. Patterson and John L. Hennessy.  
  *Annotation:* The definitive undergraduate textbook on MIPS ISA, single-cycle and pipelined datapath synthesis, hazard detection, forwarding units, cache structures, and virtual memory.

- **Computer Architecture: A Quantitative Approach**  
  *Authors:* John L. Hennessy and David A. Patterson.  
  *Annotation:* Advanced treatise covering quantitative processor evaluation, instruction-level parallelism (ILP), superscalar execution, out-of-order execution (Tomasulo's algorithm), memory hierarchy optimization, and multiprocessor cache coherence (MESI).

- **Computer Organization and Architecture: Designing for Performance**  
  *Author:* William Stallings.  
  *Annotation:* Comprehensive exploration of CPU internal bus structures, memory hierarchy, cache replacement algorithms, and computer arithmetic unit design.

---

## 2. Emulators, Simulators, and Tooling

- **MARS (MIPS Assembler and Runtime Simulator)**  
  *URL:* `https://courses.missouristate.edu/KenVollmar/mars/`  
  *Description:* Lightweight Java-based GUI and command-line simulator for MIPS assembly programming. Provides interactive register viewing, memory dumping, breakpoint debugging, and system calls.

- **SPIM MIPS Simulator**  
  *URL:* `https://spimsimulator.sourceforge.net/`  
  *Description:* Standalone terminal simulator that reads and executes MIPS assembly source files with support for console standard input/output.

- **gem5 Simulation Infrastructure**  
  *URL:* `https://www.gem5.org/`  
  *Description:* Modular, cycle-accurate architectural simulator utilized extensively in academic research to model modern out-of-order superscalar pipelines, memory controllers, and multicore cache hierarchies.

- **Logisim-evolution & Digital Logic Simulators**  
  *URL:* `https://github.com/logisim-evolution/logisim-evolution`  
  *Description:* Visual gate-level digital logic simulator for modeling educational single-cycle and pipelined CPUs from fundamental multiplexers, ALUs, and registers.

---

## 3. Specifications and Technical Standards

- **MIPS32 Architecture for Programmers Volume II: The MIPS32 Instruction Set**  
  *Author:* MIPS Technologies / Wave Computing.  
  *Description:* Official technical reference detailing opcode bitfields, register constraints, exception behaviors, and operational semantics for all MIPS32 core instructions.

- **IEEE 754-2019 Standard for Floating-Point Arithmetic**  
  *Author:* IEEE Computer Society.  
  *Description:* Industry standard specifying single-precision (32-bit) and double-precision (64-bit) binary formats, subnormal values, infinities, NaNs, and rounding modes.

