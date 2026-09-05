# Mindmap: Computer Architecture & Organization

This conceptual mindmap charts the taxonomy of modern computer architecture, instruction set design, CPU pipelining, memory hierarchies, and parallel processing systems.

```mermaid
mindmap
  root((Computer Architecture))
    Instruction Set Architecture
      RISC vs CISC Principles
      MIPS Instruction Formats
        R-Type Register Arithmetic
        I-Type Immediate & Memory
        J-Type Jump Direct
      Register File Conventions
        v0-v1 Return Values
        a0-a3 Arguments
        t0-t9 Temporaries
        s0-s7 Saved Across Calls
        sp Stack Pointer
        ra Return Address
      Addressing Modes
        Register Direct
        Base-Displacement
        PC-Relative Branching
        Pseudodirect Jump
    Computer Arithmetic
      Two's Complement Representation
      Carry-Lookahead Addition
      Booth's Multiplication Algorithm
      Restoring and Non-Restoring Division
      IEEE 754 Floating-Point Standard
    Processor Datapath
      Single-Cycle Datapath
        ALU and Register File
        Data & Instruction Memory
        Control Unit Logic Synthesis
        Critical Path Propagation Delay
      Multi-Cycle Datapath
        Shared Execution Functional Units
        Finite State Machine FSM Control
    Pipelining & Hazards
      Classic 5-Stage Pipeline
        IF Instruction Fetch
        ID Instruction Decode
        EX Execute Address Compute
        MEM Memory Access
        WB Write Back
      Hazard Resolution
        Structural Hazards
        Data Hazards RAW, WAR, WAW
          Forwarding Bypassing Unit
          Load-Use Interlock Stalling
        Control Hazards Branch Penalty
          Static Branch Prediction
          Dynamic 2-Bit Saturating Predictor
          Branch Delay Slots
    Memory Hierarchy
      Principle of Locality
        Temporal Locality
        Spatial Locality
      Cache Architecture
        Direct-Mapped Cache
        N-Way Set-Associative Cache
        Fully Associative Cache
      Address Decomposition
        Tag Bits Comparator
        Index Bits Set Selector
        Byte Offset Within Block
      Write Policies
        Write-Through vs Write-Back
        Write-Allocate vs No-Write-Allocate
      Performance Evaluation
        Hit Time & Miss Penalty
        Average Memory Access Time AMAT
        Multilevel Caches L1, L2, L3
    Parallelism & Multicore
      Instruction-Level Parallelism ILP
        Superscalar Execution
        Out-of-Order Tomasulo Algorithm
        Reorder Buffer Speculation
      Multiprocessor Systems
        Shared Memory UMA vs NUMA
        Cache Coherence MESI Protocol
        Amdahl's Law Speedup Bounds
```

