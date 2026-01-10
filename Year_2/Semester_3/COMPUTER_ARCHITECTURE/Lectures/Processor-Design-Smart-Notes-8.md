# Διαδικασία Σχεδίασης Επεξεργαστών - Smart Notes

**Course:** Αρχιτεκτονική Υπολογιστών  
**Institution:** Πανεπιστήμιο Ιωαννίνων - Τμήμα Πληροφορικής & Τηλεπικοινωνιών  
**Semester:** 3ο Εξάμηνο  
**Instructor:** Αλέξανδρος Μπανταλούκας-Αρτζμάντ MSc, PhD

---

## 1.0 Επεξεργαστής (CPU) - Θεμελιώδεις Έννοιες

### 1.1 Ορισμός και Λειτουργία

Η CPU (Central Processing Unit) αποτελεί την κεντρική μονάδα επεξεργασίας που ακολουθεί ένα προκαθορισμένο σύνολο οδηγιών για την εκτέλεση συγκεκριμένων λειτουργιών επί δεδομένων εισόδου. Οι οδηγίες αυτές αποτελούν τη βάση κάθε υπολογιστικής διεργασίας.

**Βασικές Δυνατότητες:**
- i. Ανάγνωση τιμής από μνήμη
- ii. Εκτέλεση αριθμητικών πράξεων (πρόσθεση, αφαίρεση κ.λπ.)
- iii. Αποθήκευση αποτελεσμάτων σε διαφορετική θέση μνήμης
- iv. Εκτέλεση σύνθετων λειτουργιών με όρους (conditional operations)
- v. Εκτέλεση προγραμμάτων (λειτουργικά συστήματα, εφαρμογές)

### 1.2 Γλώσσες Προγραμματισμού και Μετάφραση

> [!INFO] **Περιορισμός Κατανόησης**
> Οι επεξεργαστές κατανοούν **μόνο δυαδικό κώδικα** (1 και 0). Προγράμματα γραμμένα σε γλώσσες υψηλού επιπέδου (C++, Java, Python) δεν είναι άμεσα εκτελέσιμα.

**Διαδικασία Μετάφρασης:**

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

### 2.1 Ορισμός ISA

Το **ISA** (Instruction Set Architecture) αποτελεί το σύνολο των εντολών που μία CPU έχει σχεδιαστεί να κατανοεί και να εκτελεί. Λειτουργεί ως η διεπαφή μεταξύ λογισμικού και υλικού.

**Κύρια ISA:**
- i. **x86** (Intel, AMD - Desktop/Server)
- ii. **MIPS** (Embedded Systems)
- iii. **ARM** (Mobile Devices, IoT)
- iv. **RISC-V** (Open-Source, Research)
- v. **PowerPC** (Legacy Systems)

### 2.2 Κατηγοριοποίηση ISA

| Κατηγορία | Χαρακτηριστικά | Παραδείγματα |
|-----------|----------------|--------------|
| **Σταθερού Μήκους** | Κάθε εντολή έχει προκαθορισμένο αριθμό bits | RISC-V, ARM, MIPS |
| **Μεταβλητού Μήκους** | Διαφορετικό μήκος εντολών, μεγαλύτερη ευελιξία | x86, x86-64 |

### 2.3 Παράδειγμα: RISC-V Encoding

> [!INFO] **RISC-V Instruction Format**
> Κάθε εντολή RISC-V είναι **32-bit** (σταθερού μήκους).

**Δομή Εντολής:**
```
[31-25] [24-20] [19-15] [14-12] [11-7] [6-0]
  funct7   rs2     rs1    funct3   rd   opcode
```

- **opcode (7-bit):** Καθορίζει τον τύπο της εντολής
- **rd, rs1, rs2:** Υποδεικνύουν καταχωρητές
- **funct3, funct7:** Προσδιορίζουν την ακριβή λειτουργία

**Μετάφραση Assembly σε Binary:**

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

## 3.0 Βήματα Εκτέλεσης Εντολής (Instruction Cycle)

### 3.1 Τετραφασικός Κύκλος Εντολής

**Φάση 1: Fetch (Ανάκτηση)**
- i. Η CPU ανακτά την εντολή από τη μνήμη
- ii. Χρησιμοποιεί το Program Counter (PC) για τη διεύθυνση

**Φάση 2: Decode (Αποκωδικοποίηση)**
- i. Αναγνωρίζει τον τύπο εντολής
- ii. Κατηγοριοποίηση: αριθμητική, διακλάδωση, μνήμης

**Φάση 3: Execute (Εκτέλεση)**
- i. Ανάκτηση τελεστέων από καταχωρητές ή μνήμη
- ii. Εκτέλεση πράξης από την ALU

**Φάση 4: Write-Back (Εγγραφή Αποτελέσματος)**
- i. Αποθήκευση αποτελέσματος σε καταχωρητή
- ii. Ή εγγραφή στη μνήμη

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

> [!INFO] **64-bit Επεξεργαστές**
> Οι σύγχρονοι επεξεργαστές είναι 64-bit, επιτρέποντας διαχείριση τιμών δεδομένων και διευθύνσεων **έως 64 bits** ($2^{64}$ διευθύνσεις μνήμης).

---

## 4.0 Διασωλήνωση (Pipelining)

### 4.1 Έννοια και Στόχος

**Ορισμός:** Τεχνική που χωρίζει τα βασικά στάδια εκτέλεσης εντολής σε **20+ μικρότερα βήματα** για βελτίωση απόδοσης.

**Αναλογία:** Όπως ένας σωλήνας χρειάζεται χρόνο να γεμίσει με υγρό, έτσι και ο επεξεργαστής χρειάζεται χρόνο να γεμίσει το pipeline με δεδομένα. Μετά το γέμισμα, επιτυγχάνεται **συνεχής και σταθερή ροή** επεξεργασίας.

### 4.2 Παράδειγμα 5-Stage Pipeline

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

**Πλεονεκτήματα:**
- i. Παράλληλη εκτέλεση πολλαπλών εντολών
- ii. Βελτίωση throughput (εντολές/δευτερόλεπτο)
- iii. Αποδοτικότερη χρήση hardware resources

---

## 5.0 Υπερκλιμακωτή Αρχιτεκτονική (Superscalar)

### 5.1 Ορισμός και Χαρακτηριστικά

**Superscalar Architecture:** Αρχιτεκτονική που επιτρέπει την **ταυτόχρονη εκτέλεση πολλαπλών εντολών** σε κάθε χρονική στιγμή, αξιοποιώντας όλα τα στάδια της διασωλήνωσης.

**Μηχανισμός:**
- i. Ανίχνευση ανεξάρτητων εντολών
- ii. Προγραμματισμός ταυτόχρονης εκτέλεσης
- iii. Αποφυγή data hazards και dependencies

### 5.2 Simultaneous Multithreading (SMT)

**Τεχνολογία:** Κοινή εφαρμογή υπερκλιμακωτής αρχιτεκτονικής που επιτρέπει σε **έναν φυσικό πυρήνα** να εκτελεί **πολλαπλά threads** ταυτόχρονα.

**Παράδειγμα - Intel Hyper-Threading:**
- 1 φυσικός πυρήνας = 2 λογικοί πυρήνες
- Επεξεργαστής 8 πυρήνων → 16 threads

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

## 6.0 Ιεραρχία Μνήμης

### 6.1 Δομή Πυραμίδας Μνήμης

```mermaid
graph TD
    A["Καταχωρητές<br/>~1KB | 1-2 cycles"] --> B["L1 Cache<br/>~100KB | 2-3 cycles"]
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

### 6.2 Αρχές Ιεραρχίας

**Καθώς "κατεβαίνουμε" την ιεραρχία:**

| Χαρακτηριστικό | Τάση |
|----------------|------|
| **Κόστος ανά bit** | ↓ Μειώνεται |
| **Χωρητικότητα** | ↑ Αυξάνεται |
| **Χρόνος προσπέλασης** | ↑ Μεγαλώνει |
| **Συχνότητα προσπέλασης** | ↓ Μειώνεται |

**Αιτιολόγηση Κόστους:**
- i. **Ανώτερες μνήμες (Cache):** Χρησιμοποιούν ~6 transistors/bit → υψηλό κόστος
- ii. **Κατώτερες μνήμες (HDD/SSD):** Απλούστερη αρχιτεκτονική → χαμηλό κόστος

### 6.3 Κρυφή Μνήμη (Cache) - Αρχιτεκτονική

**Τυπική Διάταξη σε Multi-Core CPU:**

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

**Χαρακτηριστικά:**
- i. **L1 Cache:** Διαχωρισμός σε Instruction (L1i) και Data (L1d) cache
- ii. **L2 Cache:** Μία ανά πυρήνα, μεγαλύτερη χωρητικότητα
- iii. **L3 Cache:** Κοινόχρηστη μεταξύ **όλων των πυρήνων**

### 6.4 Cache Access Pattern

**Διαδικασία Αναζήτησης Δεδομένων:**

```mermaid
flowchart TD
    A[CPU Request Data] --> B{Data in L1?}
    B -->|Yes - HIT| C[Return in 2-3 cycles<br/>✓ Fast Access]
    B -->|No - MISS| D{Data in L2?}
    D -->|Yes - HIT| E[Return in 3-5 cycles<br/>✓ Medium Speed]
    D -->|No - MISS| F{Data in L3?}
    F -->|Yes - HIT| G[Return in 30-50 cycles<br/>✓ Slower]
    F -->|No - MISS| H[Access RAM<br/>50-200 cycles<br/>✗ Penalty]
    
    style C fill:#4caf50,color:#fff
    style E fill:#8bc34a
    style G fill:#cddc39
    style H fill:#ff9800
```

### 6.5 Σημασία της Cache

**Ρόλος:**
- i. Αποθήκευση **συχνά χρησιμοποιούμενων** εντολών και δεδομένων
- ii. Ελαχιστοποίηση προσβάσεων στη βραδύτερη RAM
- iii. Κρίσιμη για απόδοση - **χωρίς cache η απόδοση καταρρέει**

**Temporal Locality:** Δεδομένα που χρησιμοποιήθηκαν πρόσφατα πιθανόν να ξαναχρησιμοποιηθούν.

**Spatial Locality:** Δεδομένα κοντινά στη μνήμη πιθανόν να χρειαστούν σύντομα.

### 6.6 Memory Latency Analysis

> [!INFO] **Πειραματικά Δεδομένα (Sandra 2013 SP3)**

**Βασικά Ευρήματα:**
- i. **0-256KB:** Χαμηλό latency (~5-10 cycles) - Δεδομένα στην L1/L2
- ii. **256KB-16MB:** Μεσαίο latency (~30-50 cycles) - L3 Cache
- iii. **16MB+:** Απότομη αύξηση (~100+ cycles) - RAM access

**Συμπέρασμα:** Η cache εξασφαλίζει σταθερά χαμηλό latency έως το όριο χωρητικότητάς της.

---

## 7.0 Σύγκριση Cache σε Σύγχρονους Επεξεργαστές

### 7.1 Πίνακας Σύγκρισης Intel Core (2017-2018)

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

**Βασικές Παρατηρήσεις:**
- i. **i9-9900K:** Κορυφαία απόδοση (5.0 GHz boost, 16 MB L3)
- ii. **i7-7820X:** Μέγιστη L2 cache (8 MB), Quad-Channel μνήμη
- iii. **Hyper-Threading:** Οι i7-7820X, i7-8700K, i9-9900K υποστηρίζουν SMT

---

## 8.0 Πρόβλεψη Διακλάδωσης (Branch Prediction)

### 8.1 Πρόβλημα Διακλαδώσεων

**Σενάριο:**
```c
if (condition) {
    // Path A
} else {
    // Path B
}
```

**Πρόκληση:** Σε pipelined CPU, η επόμενη εντολή πρέπει να φορτωθεί **πριν** υπολογιστεί η συνθήκη. Ποιο μονοπάτι να διαλέξει;

### 8.2 Κερδοσκοπική Εκτέλεση (Speculative Execution)

**Μηχανισμός:**
- i. Η CPU **προβλέπει** την πιθανότερη διαδρομή
- ii. Ξεκινά εκτέλεση εντολών από το προβλεπόμενο μονοπάτι
- iii. **Αν σωστό:** Κέρδος απόδοσης, συνέχεια εκτέλεσης
- iv. **Αν λάθος:** Pipeline flush, επανεκκίνηση από σωστό μονοπάτι

```mermaid
flowchart TD
    A[Branch Instruction] --> B[Branch Predictor]
    B --> C{Prediction}
    C -->|Predict Taken| D[Speculatively Execute<br/>Taken Path]
    C -->|Predict Not Taken| E[Speculatively Execute<br/>Not Taken Path]
    
    D --> F{Actual Outcome?}
    E --> F
    
    F -->|Correct ✓| G[Continue Execution<br/>Keep Results]
    F -->|Wrong ✗| H[Pipeline Flush<br/>Rollback State<br/>Restart Correct Path]
    
    style G fill:#4caf50,color:#fff
    style H fill:#f44336,color:#fff
```

### 8.3 Machine Learning στην Πρόβλεψη

**Αλγόριθμοι Πρόβλεψης:**
- i. Παρακολούθηση ιστορικού διακλαδώσεων
- ii. **Μάθηση μοτίβων** συμπεριφοράς
- iii. Προσαρμογή βάσει αποτελεσμάτων

**Απόδοση:** Σύγχρονοι επεξεργαστές επιτυγχάνουν **>90% ακρίβεια** στην πρόβλεψη διακλαδώσεων.

---

## 9.0 CISC vs RISC Architectures

### 9.1 Φιλοσοφία Σχεδίασης

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

### 9.2 Πίνακας Σύγκρισης

| Κριτήριο | CISC | RISC |
|----------|------|------|
| **Έμφαση** | Υλικό (Hardware) | Λογισμικό (Software) |
| **Πολυπλοκότητα Εντολών** | Πολλαπλών κύκλων, πολύπλοκες | Ενός κύκλου, απλές |
| **Memory Access** | Ενσωματωμένο σε εντολές (LOAD+ADD) | Ξεχωριστά LOAD/STORE |
| **Μέγεθος Κώδικα** | Μικρό | Μεγάλο |
| **Κύκλοι/Εντολή** | Υψηλό | Χαμηλό |
| **Καταχωρητές** | Περιορισμένοι | Πολλοί (για ταχύτητα) |
| **Χρήση Transistors** | Υλοποίηση πολύπλοκων εντολών | Περισσότεροι καταχωρητές |
| **Παραδείγματα** | Intel x86, AMD64 | ARM, RISC-V, MIPS, PowerPC |

### 9.3 Σύγχρονες Τάσεις

**Σύγκλιση Αρχιτεκτονικών:**
- i. Σύγχρονοι x86 επεξεργαστές χρησιμοποιούν **μικροεντολές (μ-ops)** RISC-like εσωτερικά
- ii. ARM επεξεργαστές ενσωματώνουν πολύπλοκες εντολές (π.χ. NEON SIMD)
- iii. Υβριδικές προσεγγίσεις για βέλτιστη απόδοση

---

## 10.0 Εσωτερική Δομή CPU

### 10.1 Βασικά Συστατικά

```mermaid
graph TB
    subgraph CPU[CPU Internal Structure]
        CU[Control Unit<br/>Μονάδα Ελέγχου]
        ALU[Arithmetic Logic Unit]
        REG[Registers<br/>Καταχωρητές]
        BUS[Internal CPU Bus<br/>Εσωτερικός Δίαυλος]
        
        subgraph ALU_SUB[ALU Components]
            SHIFT[Shifter<br/>Ολισθητής]
            COMP[Complementer<br/>Συμπληρωτής]
            ARITH[Arithmetic & Boolean Logic]
            FLAGS[Status Flags<br/>Σημαίες Κατάστασης]
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

### 10.2 Λεπτομέρειες Μονάδων

**i. Arithmetic Logic Unit (ALU)**
- Αριθμητικές πράξεις: $+, -, \times, \div$
- Λογικές πράξεις: AND, OR, XOR, NOT
- Bit operations: Shift, Rotate
- Σημαίες: Zero, Carry, Overflow, Negative

**ii. Καταχωρητές (Registers)**
- General Purpose Registers (GPR)
- Special Purpose: PC, SP, Status Register
- Προσωρινή αποθήκευση δεδομένων

**iii. Μονάδα Ελέγχου (Control Unit)**
- Συντονισμός λειτουργίας όλων των μονάδων
- Δημιουργία control signals
- Timing και sequencing

---

## 11.0 Σύγχρονη Αρχιτεκτονική Πλατφόρμας

### 11.1 AMD Ryzen Threadripper X399

**Χαρακτηριστικά Πλατφόρμας:**

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

**Πλεονεκτήματα "No Dark" Φιλοσοφίας:**
- **No Dark Lanes:** Όλα τα PCIe lanes ενεργά
- **No Dark Channels:** Πλήρης χρήση Quad-Channel μνήμης
- **No Dark Ports:** Όλες οι θύρες λειτουργικές ταυτόχρονα

### 11.2 AMD Ryzen Mobile Processors (2020)

**Τεχνολογία 7nm "Zen 2":**

| Μοντέλο | Cores/Threads | Cache | TDP | GPU | Use Case |
|---------|---------------|-------|-----|-----|----------|
| Ryzen 7 4800H | 8C/16T | 12 MB | 45W | Radeon 7 (1600MHz) | Gaming/Creation |
| Ryzen 5 4600H | 6C/12T | 11 MB | 45W | Radeon 6 (1500MHz) | Gaming |
| Ryzen 7 4800U | 8C/16T | 12 MB | **15W** | Radeon 8 (1750MHz) | **Ultrathin** |
| Ryzen 5 4600U | 6C/12T | 11 MB | 15W | Radeon 6 (1500MHz) | Mainstream |
| Ryzen 3 4300U | 4C/4T | 6 MB | 15W | Radeon 5 (1400MHz) | Entry-level |
| Athlon Gold 3150U | 2C/4T | 5 MB | 15W | Radeon 3 (1000MHz) | Budget |

**Βασικά Χαρακτηριστικά:**
- i. Υποστήριξη Wi-Fi 6 & Bluetooth 5
- ii. 4K HDR display compatibility
- iii. 7nm process → Χαμηλή κατανάλωση ισχύος

---

## 12.0 Κατασκευή CPU (Manufacturing Process)

### 12.1 Διαδικασία Παραγωγής

**Βήμα 1: Εξαγωγή Πυριτίου από Άμμο**

```mermaid
flowchart LR
    A[Άμμος<br/>SiO₂] --> B[Θέρμανση με Άνθρακα<br/>C as Reducing Agent]
    B --> C[Καθαρό Πυρίτιο<br/>Si - Electronic Grade]
    C --> D[Polycrystalline Silicon<br/><0.1% Impurities]
    
    style A fill:#ffd54f
    style D fill:#90a4ae
```

**Χημική Αντίδραση:**
$$
\text{SiO}_2 + 2\text{C} \xrightarrow{\Delta} \text{Si} + 2\text{CO}
$$

**Βήμα 2: Δημιουργία Monocrystalline Ingot**

- i. Το πολυκρυσταλλικό πυρίτιο τήκεται
- ii. Σχηματισμός κυλινδρικού πλινθίου (boule/ingot)
- iii. Καθαρότητα >99.9%
- iv. Μονοκρυσταλλική δομή για ομοιόμορφες ηλεκτρικές ιδιότητες

**Βήμα 3: Τεμαχισμός σε Wafers**

```mermaid
flowchart TD
    A[Silicon Ingot<br/>Diameter: 200-300mm] --> B[Precision Sawing<br/>Diamond Blade]
    B --> C[Silicon Wafers<br/>Thickness: 0.5-0.8mm]
    C --> D[Hundreds of Wafers<br/>per Ingot]
    
    style A fill:#78909c
    style C fill:#b0bec5
```

**Βήμα 4: Chemical-Mechanical Polishing (CMP)**

**Στόχος:** Επιφάνεια ποιότητας καθρέφτη

- i. **Εξομάλυνση:** Αφαίρεση ανωμαλιών από κοπή
- ii. **Απολύμανση:** Αφαίρεση σωματιδίων
- iii. **Βελτίωση ποιότητας:** Ετοιμότητα για φωτολιθογραφία

**Βήμα 5: Photolithography - Έκθεση σε UV**

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

**Βήμα 6: Πλύση και Χάραξη (Etching)**

- i. **Πλύση:** Χημικός διαλύτης αφαιρεί εκτεθειμένο photoresist
- ii. **Χάραξη:** Αφαίρεση υποστρώματος σύμφωνα με το μοτίβο
- iii. **Επανάληψη:** 20-30+ στάδια για πολλαπλά στρώματα

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

### 12.2 Τελικά Στάδια

**Doping:** Προσθήκη ακαθαρσιών (π.χ. Phosphorus, Boron) για δημιουργία p-n junctions

**Metallization:** Δημιουργία διασυνδέσεων με χαλκό/αλουμίνιο

**Testing & Dicing:**
- i. Ηλεκτρικός έλεγχος κάθε chip στο wafer
- ii. Κοπή σε μεμονωμένα dies
- iii. Packaging (τοποθέτηση σε substrate, heat spreader)

---

## 13.0 Βασικοί Τύποι και Μετρικές Απόδοσης

### 13.1 Απόδοση Pipeline

**Speedup Factor:**
$$
S = \frac{T_{\text{sequential}}}{T_{\text{pipelined}}} = \frac{n \times k}{k + (n-1)}
$$

Όπου:
- $n$ = αριθμός εντολών
- $k$ = αριθμός σταδίων pipeline

**Για μεγάλο $n$:**
$$
S_{\max} \approx k
$$

### 13.2 Cache Performance

**Average Memory Access Time (AMAT):**
$$
\text{AMAT} = T_{\text{cache}} + (\text{Miss Rate} \times T_{\text{miss penalty}})
$$

**Παράδειγμα:**
- $T_{\text{L1}} = 3$ cycles, Miss Rate = 5%, $T_{\text{RAM}} = 100$ cycles

$$
\text{AMAT} = 3 + (0.05 \times 100) = 8 \text{ cycles}
$$

### 13.3 Branch Prediction Accuracy

**Effective CPI (Cycles Per Instruction):**
$$
\text{CPI}_{\text{eff}} = \text{CPI}_{\text{ideal}} + (\text{Branch Freq} \times \text{Mispredict Rate} \times \text{Penalty})
$$

**Παράδειγμα:**
- Ideal CPI = 1, 20% branches, 10% mispredicts, Penalty = 10 cycles

$$
\text{CPI}_{\text{eff}} = 1 + (0.2 \times 0.1 \times 10) = 1.2
$$

---

## 14.0 Βασικοί Ορισμοί - Γλωσσάριο

| Όρος | Ορισμός |
|------|---------|
| **ISA** | Instruction Set Architecture - Σύνολο εντολών που κατανοεί μία CPU |
| **Pipeline** | Τεχνική διαίρεσης εκτέλεσης εντολής σε στάδια για παράλληλη επεξεργασία |
| **Cache Hit** | Εύρεση ζητούμενων δεδομένων στην cache μνήμη |
| **Cache Miss** | Αποτυχία εύρεσης δεδομένων στην cache, απαιτείται πρόσβαση σε χαμηλότερο επίπεδο |
| **Latency** | Χρόνος που απαιτείται για την προσπέλαση δεδομένων (σε cycles) |
| **Throughput** | Αριθμός εντολών που ολοκληρώνονται ανά μονάδα χρόνου |
| **Superscalar** | Αρχιτεκτονική που εκτελεί >1 εντολές ανά κύκλο ρολογιού |
| **SMT** | Simultaneous Multithreading - Πολλαπλά threads σε έναν φυσικό πυρήνα |
| **Speculative Execution** | Εκτέλεση εντολών με βάση πρόβλεψη, πριν την επιβεβαίωση |
| **Photolithography** | Τεχνική μεταφοράς μοτίβων σε wafer με χρήση UV φωτός |
| **Wafer** | Λεπτή φέτα πυριτίου όπου κατασκευάζονται τα chips |
| **CMP** | Chemical-Mechanical Polishing - Στίλβωση wafer |

---

## 15.0 Βασικές Αρχές Σχεδιασμού

### 15.1 Memory Hierarchy Design Principles

**i. Locality Principles**
- **Temporal Locality:** Πρόσφατα χρησιμοποιημένα δεδομένα θα ξαναχρησιμοποιηθούν
- **Spatial Locality:** Δεδομένα σε γειτονικές διευθύνσεις πιθανόν να χρειαστούν

**ii. Inclusion Property**
```
L1 ⊆ L2 ⊆ L3 ⊆ RAM
```
Τα δεδομένα σε υψηλότερο επίπεδο συνήθως υπάρχουν και σε χαμηλότερο.

### 15.2 Pipeline Design Principles

**i. Balance Pipeline Stages**
- Ίσος χρόνος εκτέλεσης ανά στάδιο
- Αποφυγή bottlenecks

**ii. Hazard Management**
- **Data Hazards:** Forwarding, stalls
- **Control Hazards:** Branch prediction
- **Structural Hazards:** Resource duplication

### 15.3 Amdahl's Law

**Όριο Επιτάχυνσης:**
$$
S_{\text{overall}} = \frac{1}{(1-P) + \frac{P}{S}}
$$

Όπου:
- $P$ = Ποσοστό κώδικα που βελτιώνεται
- $S$ = Speedup του βελτιωμένου τμήματος

**Συμπέρασμα:** Βελτιώσεις σε σπάνιες περιπτώσεις έχουν μικρή συνολική επίδραση.

---

## 16.0 Αναφορές & Πόροι

### 16.1 Εκπαιδευτικά Βίντεο

**CPU Manufacturing:**
- Branch Education: "How It's Made - CPU"
- "How are Microchips Made, CPU Manufacturing Process Steps"

**CPU Operation:**
- Branch Education: "The Engineering that Runs the Digital World, How do CPUs Work?"

### 16.2 Συμπληρωματική Μελέτη

**Θεματικές Περιοχές:**
- i. Out-of-Order Execution
- ii. Tomasulo's Algorithm
- iii. Cache Coherence Protocols (MESI, MOESI)
- iv. Virtual Memory & TLB
- v. SIMD/Vector Processing
- vi. GPU Architecture Fundamentals

---

## 📚 Τέλος Smart Notes

> **Σημείωση:** Αυτές οι σημειώσεις συνθέτουν το περιεχόμενο της 8ης διάλεξης για τη Διαδικασία Σχεδίασης Επεξεργαστών. Για βαθύτερη κατανόηση, συμβουλευτείτε τα εκπαιδευτικά βίντεο και πραγματοποιήστε hands-on πειράματα με simulators (π.χ. RISC-V simulator, cache simulators).
