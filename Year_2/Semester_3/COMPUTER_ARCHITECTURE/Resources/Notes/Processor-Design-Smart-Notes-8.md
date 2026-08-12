# Processor Design Process - Smart Notes

**Course:** Computer Architecture  
**Institution:** University of Ioannina - Department of Computer Science & Telecommunications  
**Semester:** 3rd Semester  
**Instructor:** Alexandros Bantaloukas-Artzimant MSc, PhD

---

## 1.0 Processor (CPU) - Fundamental Concepts

### 1.1 Definition and Operation

The CPU (Central Processing Unit) is the central processing unit that follows a predetermined set of instructions to execute specific functions on input data. These instructions form the basis of every computational process.

**Core Capabilities:**
- i. Reading values from memory
- ii. Executing arithmetic operations (addition, subtraction, etc.)
- iii. Storing results to different memory locations
- iv. Executing complex conditional operations
- v. Executing programs (operating systems, applications)

### 1.2 Programming Languages and Translation

> [!INFO] **Understanding Limitation**
> Processors understand **only binary code** (1s and 0s). Programs written in high-level languages (C++, Java, Python) are not directly executable.

**Translation Process:**

```mermaid
graph LR
    A[High-Level Code<br/>C++/Java/Python] --> B[Compiler]
    B --> C[Assembly Language]
    C --> D[Assembler]
    D --> E[Machine Code<br/>Binary 1s & 0s]
    E --> F[CPU Execution]
    
    style A fill:#e1f5ff
    style E fill:#ffe1e1
    style F fill:#e1ffe1
```

---

## 2.0 Instruction Set Architecture (ISA)

### 2.1 ISA Definition

The **ISA** (Instruction Set Architecture) is the set of instructions that a CPU is designed to understand and execute. It serves as the interface between software and hardware.

**Major ISAs:**
- i. **x86** (Intel, AMD - Desktop/Server)
- ii. **MIPS** (Embedded Systems)
- iii. **ARM** (Mobile Devices, IoT)
- iv. **RISC-V** (Open-Source, Research)
- v. **PowerPC** (Legacy Systems)

### 2.2 ISA Classification

| Category | Characteristics | Examples |
|----------|-----------------|----------|
| **Fixed-Length** | Each instruction has a predetermined number of bits | RISC-V, ARM, MIPS |
| **Variable-Length** | Different instruction lengths, greater flexibility | x86, x86-64 |

### 2.3 Example: RISC-V Encoding

> [!INFO] **RISC-V Instruction Format**
> Each RISC-V instruction is **32-bit** (fixed-length).

**Instruction Structure:**
```
[31-25] [24-20] [19-15] [14-12] [11-7] [6-0]
  funct7   rs2     rs1    funct3   rd   opcode
```

- **opcode (7-bit):** Specifies the instruction type
- **rd, rs1, rs2:** Indicate registers
- **funct3, funct7:** Determine the exact operation

**Assembly to Binary Translation:**

```mermaid
flowchart TD
    A[Assembly Instruction<br/>ADD x1, x2, x3] --> B[Decode Components]
    B --> C[opcode: 0110011]
    B --> D[rd: x1 = 00001]
    B --> E[rs1: x2 = 00010]
    B --> F[rs2: x3 = 00011]
    B --> G[funct3: 000]
    B --> H[funct7: 0000000]
    
    C --> I[32-bit Binary<br/>0000000 00011 00010 000 00001 0110011]
    D --> I
    E --> I
    F --> I
    G --> I
    H --> I
    
    style A fill:#ffecb3
    style I fill:#c8e6c9
```

---

## 3.0 Instruction Cycle Steps

### 3.1 Four-Phase Instruction Cycle

**Phase 1: Fetch**
- i. CPU fetches the instruction from memory
- ii. Uses the Program Counter (PC) for the address

**Phase 2: Decode**
- i. Identifies the instruction type
- ii. Classification: arithmetic, branch, memory

**Phase 3: Execute**
- i. Retrieves operands from registers or memory
- ii. Executes the operation from the ALU

**Phase 4: Write-Back**
- i. Stores the result in a register
- ii. Or writes to memory

```mermaid
sequenceDiagram
    participant PC as Program Counter
    participant MEM as Memory
    participant CU as Control Unit
    participant ALU as ALU
    participant REG as Registers
    
    PC->>MEM: 1. Fetch Instruction
    MEM-->>CU: Return Instruction
    CU->>CU: 2. Decode Instruction
    CU->>REG: 3a. Fetch Operands
    REG-->>ALU: Send Data
    ALU->>ALU: 3b. Execute Operation
    ALU-->>REG: 4. Write Result
    REG->>MEM: (Optional) Store to Memory
```

> [!INFO] **64-bit Processors**
> Modern processors are 64-bit, enabling handling of data values and addresses **up to 64 bits** ($2^{64}$ memory addresses).

---

## 4.0 Pipelining

### 4.1 Concept and Goal

**Definition:** Technique that divides the main instruction execution stages into **20+ smaller steps** to improve performance.

**Analogy:** Just as a pipe needs time to fill with liquid, the processor needs time to fill the pipeline with data. After filling, **continuous and steady processing flow** is achieved.

### 4.2 5-Stage Pipeline Example

```mermaid
gantt
    title CPU Pipeline - 5 Stages Execution
    dateFormat X
    axisFormat %L
    
    section Instruction 1
    Fetch    :a1, 0, 1
    Decode   :a2, 1, 1
    Execute  :a3, 2, 1
    Memory   :a4, 3, 1
    WriteBack:a5, 4, 1
    
    section Instruction 2
    Fetch    :b1, 1, 1
    Decode   :b2, 2, 1
    Execute  :b3, 3, 1
    Memory   :b4, 4, 1
    WriteBack:b5, 5, 1
    
    section Instruction 3
    Fetch    :c1, 2, 1
    Decode   :c2, 3, 1
    Execute  :c3, 4, 1
    Memory   :c4, 5, 1
    WriteBack:c5, 6, 1
    
    section Instruction 4
    Fetch    :d1, 3, 1
    Decode   :d2, 4, 1
    Execute  :d3, 5, 1
    Memory   :d4, 6, 1
    WriteBack:d5, 7, 1
```

**Advantages:**
- i. Parallel execution of multiple instructions
- ii. Improved throughput (instructions/second)
- iii. More efficient use of hardware resources

---

## 5.0 Superscalar Architecture

### 5.1 Definition and Characteristics

**Superscalar Architecture:** Architecture that allows **simultaneous execution of multiple instructions** at each point in time, utilizing all pipeline stages.

**Mechanism:**
- i. Detection of independent instructions
- ii. Scheduling of simultaneous execution
- iii. Avoidance of data hazards and dependencies

### 5.2 Simultaneous Multithreading (SMT)

**Technology:** Common application of superscalar architecture that allows a **single physical core** to execute **multiple threads** simultaneously.

**Example - Intel Hyper-Threading:**
- 1 physical core = 2 logical cores
- 8-core processor → 16 threads

```mermaid
graph TD
    A[Physical Core 1] --> B[Virtual Core 1A<br/>Thread 1]
    A --> C[Virtual Core 1B<br/>Thread 2]
    
    D[Physical Core 2] --> E[Virtual Core 2A<br/>Thread 3]
    D --> F[Virtual Core 2B<br/>Thread 4]
    
    G[Shared Execution Units] --> A
    G --> D
    
    style A fill:#bbdefb
    style D fill:#bbdefb
    style B fill:#c8e6c9
    style C fill:#c8e6c9
    style E fill:#c8e6c9
    style F fill:#c8e6c9
```

---

## 6.0 Memory Hierarchy

### 6.1 Memory Pyramid Structure

```mermaid
graph TD
    A["Registers<br/>~1KB | 1-2 cycles"] --> B["L1 Cache<br/>~100KB | 2-3 cycles"]
    B --> C["L2 Cache<br/>~500KB | 3-5 cycles"]
    C --> D["L3 Cache<br/>~10-15MB | 30-50 cycles"]
    D --> E["RAM<br/>~10GB | 50-200 cycles"]
    E --> F["SSD/HDD<br/>~TB | ~50,000 cycles"]
    
    style A fill:#f44336,color:#fff
    style B fill:#ff9800
    style C fill:#ffeb3b
    style D fill:#8bc34a
    style E fill:#2196f3,color:#fff
    style F fill:#9e9e9e,color:#fff
```

### 6.2 Hierarchy Principles

**As we "move down" the hierarchy:**

| Characteristic | Trend |
|----------------|-------|
| **Cost per bit** | ↓ Decreases |
| **Capacity** | ↑ Increases |
| **Access time** | ↑ Increases |
| **Access frequency** | ↓ Decreases |

**Cost Justification:**
- i. **Higher memories (Cache):** Use ~6 transistors/bit → high cost
- ii. **Lower memories (HDD/SSD):** Simpler architecture → low cost

### 6.3 Cache - Architecture

**Typical Layout in Multi-Core CPU:**

```mermaid
graph TB
    subgraph Core1[Core 1]
        L1I1[L1i Cache<br/>Instructions]
        L1D1[L1d Cache<br/>Data]
        L21[L2 Cache<br/>Unified]
    end
    
    subgraph Core2[Core 2]
        L1I2[L1i Cache<br/>Instructions]
        L1D2[L1d Cache<br/>Data]
        L22[L2 Cache<br/>Unified]
    end
    
    L3[L3 Cache - Shared<br/>All Cores]
    
    L21 --> L3
    L22 --> L3
    
    L3 --> RAM[Main Memory<br/>RAM]
    
    style L1I1 fill:#e1bee7
    style L1D1 fill:#e1bee7
    style L1I2 fill:#e1bee7
    style L1D2 fill:#e1bee7
    style L21 fill:#ce93d8
    style L22 fill:#ce93d8
    style L3 fill:#ba68c8
    style RAM fill:#9c27b0,color:#fff
```

**Characteristics:**
- i. **L1 Cache:** Split into Instruction (L1i) and Data (L1d) cache
- ii. **L2 Cache:** One per core, larger capacity
- iii. **L3 Cache:** Shared among **all cores**

### 6.4 Cache Access Pattern

**Data Search Process:**

```mermaid
flowchart TD
    A[CPU Request Data] --> B{Data in L1?}
    B -->|Yes - HIT| C[Return in 2-3 cycles<br/> Fast Access]
    B -->|No - MISS| D{Data in L2?}
    D -->|Yes - HIT| E[Return in 3-5 cycles<br/> Medium Speed]
    D -->|No - MISS| F{Data in L3?}
    F -->|Yes - HIT| G[Return in 30-50 cycles<br/> Slower]
    F -->|No - MISS| H[Access RAM<br/>50-200 cycles<br/> Penalty]
    
    style C fill:#4caf50,color:#fff
    style E fill:#8bc34a
    style G fill:#cddc39
    style H fill:#ff9800
```

### 6.5 Importance of Cache

**Role:**
- i. Storing **frequently used** instructions and data
- ii. Minimizing accesses to the slower RAM
- iii. Critical for performance - **without cache, performance collapses**

**Temporal Locality:** Data recently used is likely to be used again.

**Spatial Locality:** Data near the current address is likely to be needed soon.

### 6.6 Memory Latency Analysis

> [!INFO] **Experimental Data (Sandra 2013 SP3)**

**Key Findings:**
- i. **0-256KB:** Low latency (~5-10 cycles) - Data in L1/L2
- ii. **256KB-16MB:** Medium latency (~30-50 cycles) - L3 Cache
- iii. **16MB+:** Sharp increase (~100+ cycles) - RAM access

**Conclusion:** Cache ensures consistently low latency up to its capacity limit.

---

## 7.0 Cache Comparison in Modern Processors

### 7.1 Intel Core Comparison Table (2017-2018)

| Spec | i7-7820X | i7-8700K | i9-9900K | i7-9700K |
|------|----------|----------|----------|----------|
| **Release Date** | June 2017 | Oct 2017 | Oct 2018 | Oct 2018 |
| **Cores/Threads** | 8/16 | 6/12 | **8/16** | 8/8 |
| **Base Freq** | 3.6 GHz | 3.5 GHz | 3.6 GHz | 3.6 GHz |
| **Max Boost** | 4.3 GHz | 4.7 GHz | **5.0 GHz** | 4.9 GHz |
| **L2 Cache** | **8 MB** | 1.5 MB | 2 MB | 2 MB |
| **L3 Cache** | 11 MB | 12 MB | **16 MB** | 12 MB |
| **Memory Config** | **Quad-Channel** | Dual-Channel | Dual-Channel | Dual-Channel |
| **Max Memory** | DDR4-2666 | DDR4-2666 | DDR4-2666 | DDR4-2666 |
| **TDP** | 140W | 95W | 95W | 95W |
| **MSRP** | $600 | $360 | $500 | $374 |

**Key Observations:**
- i. **i9-9900K:** Top performance (5.0 GHz boost, 16 MB L3)
- ii. **i7-7820X:** Maximum L2 cache (8 MB), Quad-Channel memory
- iii. **Hyper-Threading:** i7-7820X, i7-8700K, i9-9900K support SMT

---

## 8.0 Branch Prediction

### 8.1 Branch Problem

**Scenario:**
```c
if (condition) {
    // Path A
} else {
    // Path B
}
```

**Challenge:** In a pipelined CPU, the next instruction must be fetched **before** the condition is computed. Which path to choose?

### 8.2 Speculative Execution

**Mechanism:**
- i. CPU **predicts** the most likely path
- ii. Begins executing instructions from the predicted path
- iii. **If correct:** Performance gain, continue execution
- iv. **If wrong:** Pipeline flush, restart from correct path

```mermaid
flowchart TD
    A[Branch Instruction] --> B[Branch Predictor]
    B --> C{Prediction}
    C -->|Predict Taken| D[Speculatively Execute<br/>Taken Path]
    C -->|Predict Not Taken| E[Speculatively Execute<br/>Not Taken Path]
    
    D --> F{Actual Outcome?}
    E --> F
    
    F -->|Correct | G[Continue Execution<br/>Keep Results]
    F -->|Wrong | H[Pipeline Flush<br/>Rollback State<br/>Restart Correct Path]
    
    style G fill:#4caf50,color:#fff
    style H fill:#f44336,color:#fff
```

### 8.3 Machine Learning in Prediction

**Prediction Algorithms:**
- i. Monitoring branch history
- ii. **Pattern learning** of behavior
- iii. Adaptation based on results

**Performance:** Modern processors achieve **>90% accuracy** in branch prediction.

---

## 9.0 CISC vs RISC Architectures

### 9.1 Design Philosophy

```mermaid
mindmap
  root((ISA<br/>Philosophies))
    CISC
      Complex Instructions
      Hardware Emphasis
      Multi-Cycle Instructions
      Built-in Memory Access
      Small Code Size
      x86, x86-64
    RISC
      Simple Instructions
      Software Emphasis
      Single-Cycle Instructions
      Separate Load/Store
      Large Code Size
      ARM, RISC-V, MIPS
```

### 9.2 Comparison Table

| Criterion | CISC | RISC |
|-----------|------|------|
| **Emphasis** | Hardware | Software |
| **Instruction Complexity** | Multi-cycle, complex | Single-cycle, simple |
| **Memory Access** | Embedded in instructions (LOAD+ADD) | Separate LOAD/STORE |
| **Code Size** | Small | Large |
| **Cycles/Instruction** | High | Low |
| **Registers** | Limited | Many (for speed) |
| **Transistor Usage** | Implementing complex instructions | More registers |
| **Examples** | Intel x86, AMD64 | ARM, RISC-V, MIPS, PowerPC |

### 9.3 Modern Trends

**Architectural Convergence:**
- i. Modern x86 processors use **micro-ops (u-ops)** RISC-like internally
- ii. ARM processors incorporate complex instructions (e.g. NEON SIMD)
- iii. Hybrid approaches for optimal performance

---

## 10.0 CPU Internal Structure

### 10.1 Basic Components

```mermaid
graph TB
    subgraph CPU[CPU Internal Structure]
        CU[Control Unit]
        ALU[Arithmetic Logic Unit]
        REG[Registers]
        BUS[Internal CPU Bus]
        
        subgraph ALU_SUB[ALU Components]
            SHIFT[Shifter]
            COMP[Complementer]
            ARITH[Arithmetic & Boolean Logic]
            FLAGS[Status Flags]
        end
    end
    
    CU -->|Control Paths| ALU
    CU -->|Control Paths| REG
    ALU --> BUS
    REG --> BUS
    BUS --> CU
    
    style CU fill:#64b5f6
    style ALU fill:#81c784
    style REG fill:#ffb74d
    style BUS fill:#e57373
```

### 10.2 Unit Details

**i. Arithmetic Logic Unit (ALU)**
- Arithmetic operations: $+, -, \times, \div$
- Logical operations: AND, OR, XOR, NOT
- Bit operations: Shift, Rotate
- Flags: Zero, Carry, Overflow, Negative

**ii. Registers**
- General Purpose Registers (GPR)
- Special Purpose: PC, SP, Status Register
- Temporary data storage

**iii. Control Unit**
- Coordination of all unit operations
- Control signal generation
- Timing and sequencing

---

## 11.0 Modern Platform Architecture

### 11.1 AMD Ryzen Threadripper X399

**Platform Characteristics:**

```mermaid
graph TD
    CPU[Ryzen Threadripper<br/>64 PCIe Lanes] --> DDR4[Quad-Channel DDR4<br/>4x DIMM Slots]
    CPU --> PCIeSlots[PCIe x16 Slots<br/>4 GPUs]
    CPU --> NVMeSlots[NVMe SSDs<br/>3x M.2 x4]
    CPU --> CHIPSET[X399 Chipset]
    
    CHIPSET --> SATA[8x SATA]
    CHIPSET --> USB[USB Ports<br/>3.1 Gen2, 3.1 Gen1, 2.0]
    CHIPSET --> PCIE[Additional PCIe<br/>x1/x4]
    CHIPSET --> NET[Dual Gigabit Ethernet]
    CHIPSET --> AUDIO[HD Audio Codec]
    CHIPSET --> WLAN[M.2 WLAN/Bluetooth]
    
    style CPU fill:#f44336,color:#fff
    style CHIPSET fill:#ff9800
    style DDR4 fill:#2196f3,color:#fff
```

**"No Dark" Philosophy Advantages:**
- **No Dark Lanes:** All PCIe lanes active
- **No Dark Channels:** Full use of Quad-Channel memory
- **No Dark Ports:** All ports functional simultaneously

### 11.2 AMD Ryzen Mobile Processors (2020)

**7nm "Zen 2" Technology:**

| Model | Cores/Threads | Cache | TDP | GPU | Use Case |
|-------|---------------|-------|-----|-----|----------|
| Ryzen 7 4800H | 8C/16T | 12 MB | 45W | Radeon 7 (1600MHz) | Gaming/Creation |
| Ryzen 5 4600H | 6C/12T | 11 MB | 45W | Radeon 6 (1500MHz) | Gaming |
| Ryzen 7 4800U | 8C/16T | 12 MB | **15W** | Radeon 8 (1750MHz) | **Ultrathin** |
| Ryzen 5 4600U | 6C/12T | 11 MB | 15W | Radeon 6 (1500MHz) | Mainstream |
| Ryzen 3 4300U | 4C/4T | 6 MB | 15W | Radeon 5 (1400MHz) | Entry-level |
| Athlon Gold 3150U | 2C/4T | 5 MB | 15W | Radeon 3 (1000MHz) | Budget |

**Key Features:**
- i. Wi-Fi 6 & Bluetooth 5 support
- ii. 4K HDR display compatibility
- iii. 7nm process → Low power consumption

---

## 12.0 CPU Manufacturing Process

### 12.1 Production Process

**Step 1: Silicon Extraction from Sand**

```mermaid
flowchart LR
    A[Sand<br/>SiO₂] --> B[Heating with Carbon<br/>C as Reducing Agent]
    B --> C[Pure Silicon<br/>Si - Electronic Grade]
    C --> D[Polycrystalline Silicon<br/><0.1% Impurities]
    
    style A fill:#ffd54f
    style D fill:#90a4ae
```

**Chemical Reaction:**
$$
\text{SiO}_2 + 2\text{C} \xrightarrow{\Delta} \text{Si} + 2\text{CO}
$$

**Step 2: Creating Monocrystalline Ingot**

- i. Polycrystalline silicon is melted
- ii. Cylindrical ingot formation (boule/ingot)
- iii. Purity >99.9%
- iv. Monocrystalline structure for uniform electrical properties

**Step 3: Slicing into Wafers**

```mermaid
flowchart TD
    A[Silicon Ingot<br/>Diameter: 200-300mm] --> B[Precision Sawing<br/>Diamond Blade]
    B --> C[Silicon Wafers<br/>Thickness: 0.5-0.8mm]
    C --> D[Hundreds of Wafers<br/>per Ingot]
    
    style A fill:#78909c
    style C fill:#b0bec5
```

**Step 4: Chemical-Mechanical Polishing (CMP)**

**Goal:** Mirror-quality surface

- i. **Smoothing:** Removing irregularities from cutting
- ii. **Cleaning:** Removing particles
- iii. **Quality improvement:** Readiness for photolithography

**Step 5: Photolithography - UV Exposure**

```mermaid
sequenceDiagram
    participant W as Wafer
    participant PR as Photoresist
    participant M as Photomask
    participant UV as UV Light
    
    W->>PR: Apply blue liquid photoresist
    PR->>PR: Spin coating (uniform layer)
    M->>W: Align photomask with pattern
    UV->>M: Expose through mask
    M->>PR: Transfer geometric pattern
    PR->>PR: Exposed areas become soluble
```

**Step 6: Washing and Etching**

- i. **Washing:** Chemical solvent removes exposed photoresist
- ii. **Etching:** Substrate removal according to pattern
- iii. **Repetition:** 20-30+ stages for multiple layers

```mermaid
flowchart TD
    A[Exposed Wafer] --> B[Developer Solution<br/>Remove Exposed Photoresist]
    B --> C[Etching Process<br/>Chemical/Plasma]
    C --> D[Pattern Transferred to Silicon]
    D --> E{More Layers?}
    E -->|Yes| F[Repeat Photolithography]
    E -->|No| G[Proceed to Doping & Metallization]
    F --> A
    
    style D fill:#81c784
    style G fill:#4caf50,color:#fff
```

### 12.2 Final Stages

**Doping:** Adding impurities (e.g. Phosphorus, Boron) to create p-n junctions

**Metallization:** Creating interconnections with copper/aluminum

**Testing & Dicing:**
- i. Electrical testing of each chip on wafer
- ii. Cutting into individual dies
- iii. Packaging (placement on substrate, heat spreader)

---

## 13.0 Key Types and Performance Metrics

### 13.1 Pipeline Performance

**Speedup Factor:**
$$
S = \frac{T_{\text{sequential}}}{T_{\text{pipelined}}} = \frac{n \times k}{k + (n-1)}
$$

Where:
- $n$ = number of instructions
- $k$ = number of pipeline stages

**For large $n$:**
$$
S_{\max} \approx k
$$

### 13.2 Cache Performance

**Average Memory Access Time (AMAT):**
$$
\text{AMAT} = T_{\text{cache}} + (\text{Miss Rate} \times T_{\text{miss penalty}})
$$

**Example:**
- $T_{\text{L1}} = 3$ cycles, Miss Rate = 5%, $T_{\text{RAM}} = 100$ cycles

$$
\text{AMAT} = 3 + (0.05 \times 100) = 8 \text{ cycles}
$$

### 13.3 Branch Prediction Accuracy

**Effective CPI (Cycles Per Instruction):**
$$
\text{CPI}_{\text{eff}} = \text{CPI}_{\text{ideal}} + (\text{Branch Freq} \times \text{Mispredict Rate} \times \text{Penalty})
$$

**Example:**
- Ideal CPI = 1, 20% branches, 10% mispredicts, Penalty = 10 cycles

$$
\text{CPI}_{\text{eff}} = 1 + (0.2 \times 0.1 \times 10) = 1.2
$$

---

## 14.0 Key Definitions - Glossary

| Term | Definition |
|------|------------|
| **ISA** | Instruction Set Architecture - Set of instructions understood by a CPU |
| **Pipeline** | Technique of dividing instruction execution into stages for parallel processing |
| **Cache Hit** | Finding requested data in cache memory |
| **Cache Miss** | Failure to find data in cache, requires access to lower level |
| **Latency** | Time required to access data (in cycles) |
| **Throughput** | Number of instructions completed per unit time |
| **Superscalar** | Architecture that executes >1 instructions per clock cycle |
| **SMT** | Simultaneous Multithreading - Multiple threads on a single physical core |
| **Speculative Execution** | Executing instructions based on prediction, before confirmation |
| **Photolithography** | Technique of transferring patterns to wafer using UV light |
| **Wafer** | Thin silicon disc where chips are manufactured |
| **CMP** | Chemical-Mechanical Polishing - Wafer polishing |

---

## 15.0 Core Design Principles

### 15.1 Memory Hierarchy Design Principles

**i. Locality Principles**
- **Temporal Locality:** Recently used data will be used again
- **Spatial Locality:** Data in adjacent addresses is likely needed

**ii. Inclusion Property**
```
L1 ⊆ L2 ⊆ L3 ⊆ RAM
```
Data at a higher level typically also exists at a lower level.

### 15.2 Pipeline Design Principles

**i. Balance Pipeline Stages**
- Equal execution time per stage
- Avoid bottlenecks

**ii. Hazard Management**
- **Data Hazards:** Forwarding, stalls
- **Control Hazards:** Branch prediction
- **Structural Hazards:** Resource duplication

### 15.3 Amdahl's Law

**Speedup Limit:**
$$
S_{\text{overall}} = \frac{1}{(1-P) + \frac{P}{S}}
$$

Where:
- $P$ = Fraction of code improved
- $S$ = Speedup of the improved section

**Conclusion:** Improvements in rare cases have minimal overall impact.

---

## 16.0 References & Resources

### 16.1 Educational Videos

**CPU Manufacturing:**
- Branch Education: "How It's Made - CPU"
- "How are Microchips Made, CPU Manufacturing Process Steps"

**CPU Operation:**
- Branch Education: "The Engineering that Runs the Digital World, How do CPUs Work?"

### 16.2 Supplementary Study

**Topics:**
- i. Out-of-Order Execution
- ii. Tomasulo's Algorithm
- iii. Cache Coherence Protocols (MESI, MOESI)
- iv. Virtual Memory & TLB
- v. SIMD/Vector Processing
- vi. GPU Architecture Fundamentals

---

## End of Smart Notes

> **Note:** These notes compile the content of the 8th lecture on the Processor Design Process. For deeper understanding, consult the educational videos and perform hands-on experiments with simulators (e.g. RISC-V simulator, cache simulators).