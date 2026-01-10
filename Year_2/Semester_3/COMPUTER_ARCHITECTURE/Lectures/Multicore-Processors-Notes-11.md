# Κεφάλαιο 18: Υπολογιστές Πολλαπλών Πυρήνων - Smart Notes

---

## 1.0 Ζητήματα Απόδοσης Υλικού

### 1.1 Εκθετική Αύξηση Απόδοσης Μικροεπεξεργαστών

**i. Παράγοντες Βελτίωσης:**
- Βελτίωση στην οργάνωση αρχιτεκτονικής
- Αύξηση συχνότητας λειτουργίας

**ii. Τεχνικές Ενίσχυσης Παράλληλου Επεξεργαστή:**
- **Διασωλήνωση (Pipelining)**: Ταχύτερη επεξεργασία εντολών
- **Υπερβαθμωτή Αρχιτεκτονική (Superscalar)**: Αποδοτικότερη εκτέλεση πολλαπλών εντολών
- **Ταυτόχρονη Πολυνημάτωση (Simultaneous Multithreading - SMT)**: Καλύτερη αξιοποίηση πόρων

### 1.2 Νόμος του Moore

**i. Ιστορική Εξέλιξη Τεχνολογίας Κατασκευής:**

| Περίοδος | Μέγεθος Τεχνολογίας |
|----------|---------------------|
| 1971 | 10 μm |
| 1984 | 1 μm |
| 1990 | 600 nm |
| 2001 | 130 nm |
| 2005 | 65 nm |
| 2012 | 22 nm |
| 2018 | 7 nm |
| 2020 | 5 nm |
| 2023 | ~3 nm (M3 Apple) |
| 2024 | ~2 nm |

**ii. Σημασία:**
- Συνεχής μείωση μεγέθους τρανζίστορ επιτρέπει υψηλότερη πυκνότητα
- Αύξηση απόδοσης και μείωση κόστους

> [!INFO] **Οι Ορισμοί:**
>
> **MOSFET (Metal-Oxide-Semiconductor Field-Effect Transistor)**:
> - Βασικό στοιχείο μικροεπεξεργαστών και μνημών
> - Λειτουργεί ως διακόπτης ή ενισχυτής ηλεκτρικών σημάτων
> - Ο αριθμός MOSFETs = δείκτης υπολογιστικής ισχύος
>
> **Wafer Scale Engine (WSE)**:
> - Ολόκληρη η επιφάνεια ενός wafer πυριτίου χρησιμοποιείται για ένα chip
> - Εκατομμύρια πυρήνες, τεράστια μνήμη
> - Εφαρμογές: AI, Machine Learning, HPC
> - Παράδειγμα: Cerebras WSE-2 (2600 δισεκ. τρανζίστορ, 840,000 AI-πυρήνες)

### 1.3 Εξέλιξη Μικροεπεξεργαστών και Τεχνολογιών IC

| Έτος | Στοιχείο | Ονομασία | MOSFETs (δισεκ.) |
|------|---------|----------|-----------------|
| 2019 | IC Chip | Samsung V-NAND | 2000 |
| 2020 | GPU | AMD Instinct MI250X | 59 |
| 2020 | ML Processor | Colossus Mk2 GC200 | 59.4 |
| 2020 | IC Chip | Wafer Scale Engine 2 | 2600 |
| 2021 | Microprocessor | Apple M1 Max | 57 |

### 1.4 Κανόνας του Pollack

> [!INFO] **Θεώρημα Απόδοσης:**
>
> Η αύξηση απόδοσης ενός επεξεργαστή είναι περίπου ανάλογη με την τετραγωνική ρίζα της αύξησης πολυπλοκότητας:
>
> $$ \text{Απόδοση} \propto \sqrt{\text{Πολυπλοκότητα}} $$
>
> **Παράδειγμα**: Διπλασιασμός λογικών κυκλωμάτων πυρήνα → Αύξηση απόδοσης ~40%

**i. Προκλήσεις Σχεδίασης:**
- Αυξημένη δυσκολία κατασκευής
- Πολυπλοκότητα αποσφαλμάτωσης
- Περιορισμοί επέκτασης

### 1.5 Αύξηση Πολυπλοκότητας και Κατανάλωση Ενέργειας

**i. Πρόβλημα Ισχύος:**
- Κατανάλωση ενέργειας αυξάνεται εκθετικά με πυκνότητα τρανζίστορ
- Συχνότητα ρολογιού επιδεινώνει το πρόβλημα
- Πάνω από 20 δισεκ. τρανζίστορ σε σύγχρονα chips

**ii. Λύση: Πολλαπλοί Πυρήνες**
- Αντιμετώπιση υπερθέρμανσης
- Αύξηση απόδοσης
- Αποτελεσματική διαχείριση κρυφής μνήμης

```mermaid
graph TD
    A[Αύξηση Πυκνότητας Τρανζίστορ] --> B[Αύξηση Θερμότητας]
    A --> C[Δυσκολία Εκμετάλλευσης Μονού Πυρήνα]
    B --> D[Λύση: Πολλαπλοί Πυρήνες]
    C --> D
    D --> E[Μείωση Θερμότητας ανά Πυρήνα]
    D --> F[Καλύτερη Αξιοποίηση Cache]
    D --> G[Υψηλότερη Συνολική Απόδοση]
```

---

## 2.0 Θέματα Απόδοσης Λογισμικού

### 2.1 Νόμος του Amdahl

**i. Μαθηματική Διατύπωση:**

$$
S = \frac{1}{(1-f) + \frac{f}{N}}
$$

Όπου:
- $ S $: Αύξηση ταχύτητας (speedup)
- $ f $: Ποσοστό παράλληλου κώδικα
- $ (1-f) $: Ποσοστό σειριακού κώδικα
- $ N $: Αριθμός επεξεργαστών

**ii. Πρακτικό Παράδειγμα:**
- 10% σειριακός κώδικας σε σύστημα 8 επεξεργαστών
- Επίτευξη: Μόλις 4.7× απόδοση (όχι 8×)

> [!WARNING] **Κρίσιμη Παρατήρηση:**
>
> Ακόμα και μικρό ποσοστό σειριακού κώδικα περιορίζει σημαντικά την απόδοση παράλληλων συστημάτων.

**iii. Επιπλέον Επιβαρύνσεις Λογισμικού:**
- Επικοινωνία μεταξύ επεξεργαστών
- Κατανομή εργασίας στους πυρήνες
- Διατήρηση συνοχής κρυφής μνήμης

```mermaid
graph LR
    A[Πρόγραμμα] --> B["Σειριακό Τμήμα (1-f)"]
    A --> C["Παράλληλο Τμήμα (f)"]
    B --> D[Εκτέλεση σε 1 CPU]
    C --> E["Κατανομή σε N CPUs"]
    D --> F[Συνολικός Χρόνος]
    E --> F
    F --> G["Speedup = 1 / ((1-f) + f/N)"]

```

### 2.2 Επιτάχυνση με Σειριακά Τμήματα

| Αρ. Επεξεργαστών | 0% Σειριακό | 2% Σειριακό | 5% Σειριακό | 10% Σειριακό |
|------------------|-------------|-------------|-------------|--------------|
| 1 | 1.0× | 1.0× | 1.0× | 1.0× |
| 2 | 2.0× | 1.96× | 1.90× | 1.82× |
| 4 | 4.0× | 3.77× | 3.48× | 3.08× |
| 8 | 8.0× | 6.90× | 5.93× | 4.71× |

### 2.3 Επίδραση Overhead

**i. Επιβαρύνσεις συστήματος** (5%, 10%, 15%, 20%):
- Μείωση πραγματικής επίδοσης
- Καθυστερήσεις επικοινωνίας
- Συγχρονισμός νημάτων

**ii. Παρατήρηση από Benchmarks:**
- Single-threaded performance ανεξάρτητη από αριθμό πυρήνων
- Παράδειγμα: Intel i7-7700K (4/8) ≈ Ryzen Threadripper 1950X (16/32) σε μονονηματικά workloads

---

## 3.0 Παράγοντες Διαμόρφωσης Πολυπύρηνων Επεξεργαστών

### 3.1 Βασικοί Παράγοντες Σχεδίασης

**i. Αριθμός Επεξεργαστών:**
- Πλήθος πυρήνων στο chip

**ii. Επίπεδα Κρυφής Μνήμης:**
- L1, L2, L3 cache
- Ιεραρχία για βελτίωση ταχύτητας πρόσβασης

**iii. Ποσότητα Κοινόχρηστης Κρυφής Μνήμης:**
- Μέγεθος shared cache μεταξύ πυρήνων

**iv. Υποστήριξη Simultaneous Multithreading:**
- Ταυτόχρονη εκτέλεση πολλαπλών νημάτων ανά πυρήνα

**v. Τύποι Πυρήνων:**
- **Ομοιογενείς (Homogeneous)**: Ίδιοι πυρήνες
- **Ετερογενείς (Heterogeneous)**: Διαφορετικοί πυρήνες για εξειδικευμένες λειτουργίες

```mermaid
mindmap
  root((Πολυπύρηνες<br/>Αρχιτεκτονικές))
    Αριθμός Πυρήνων
      2-4 cores
      8-16 cores
      32+ cores
    Cache Hierarchy
      L1 Dedicated
      L2 Dedicated/Shared
      L3 Shared
    Threading
      SMT/Hyper-Threading
      Single Thread per Core
    Core Types
      Homogeneous
      Heterogeneous
        big.LITTLE
        Performance + Efficiency
```

---

## 4.0 Οργάνωση Κρυφής Μνήμης

### 4.1 Τύποι Διαμόρφωσης Cache

**i. Δεσμευμένη Κρυφή Μνήμη Επιπέδου 1 (L1):**
- Κάθε πυρήνας: Αποκλειστική L1
- Διαχωρισμός: L1-D (Data), L1-I (Instruction)
- Πρόσβαση στην κύρια μνήμη μέσω I/O

**ii. Δεσμευμένη Κρυφή Μνήμη Επιπέδου 2 (L2):**
- Κάθε πυρήνας: Αποκλειστική L1 + Δεσμευμένη L2
- Μεγαλύτερη χωρητικότητα ανά πυρήνα

**iii. Κοινόχρηστη Κρυφή Μνήμη Επιπέδου 2:**
- Πυρήνες μοιράζονται κοινή L2
- Μείωση αντιγραφής δεδομένων μεταξύ πυρήνων

**iv. Κοινόχρηστη Κρυφή Μνήμη Επιπέδου 3 (L3):**
- L1, L2: Δεσμευμένα ανά πυρήνα
- L3: Κοινόχρηστη για όλους τους πυρήνες
- Ενδιάμεσος χώρος πριν την κύρια μνήμη

```mermaid
graph TD
    subgraph "Dedicated L1"
        A["Core 1<br/>L1-I | L1-D"] 
        B["Core 2<br/>L1-I | L1-D"]
    end
    subgraph "Dedicated L2"
        C[Core 1 L2]
        D[Core 2 L2]
    end
    E[Shared L3 Cache]
    F[Main Memory]
    
    A --> C
    B --> D
    C --> E
    D --> E
    E --> F

```

### 4.2 Πλεονεκτήματα Κοινόχρηστης Cache

**i. Μειωμένοι Ρυθμοί Αστοχίας:**
- Συνολική μείωση miss rate

**ii. Κοινή Αποθήκευση Δεδομένων:**
- Δεδομένα που χρησιμοποιούνται από πολλούς πυρήνες αποθηκεύονται μία φορά
- Εξοικονόμηση πόρων

**iii. Δυναμική Κατανομή Μνήμης:**
- Αλγόριθμοι αντικατάστασης προσαρμόζουν την κατανομή
- Νήματα με χαμηλή τοπικότητα αποκτούν περισσότερο χώρο

**iv. Αποτελεσματική Επικοινωνία:**
- Επικοινωνία μέσω shared cache
- Εξάλειψη ανάγκης για εξωτερικά δίκτυα

---

## 5.0 Αρχιτεκτονικές Ετερογενών Συστημάτων

### 5.1 Πολλαπλοί Πυρήνες CPU/GPU

**i. Χαρακτηριστικά GPU:**
- Υποστήριξη χιλιάδων παράλληλων νημάτων
- Κατάλληλες για εφαρμογές μεγάλων δεδομένων (διανύσματα, πίνακες)
- Αρχική χρήση: Βελτίωση απόδοσης γραφικών
- Σύγχρονη χρήση: Επαναληπτικές πράξεις σε δομημένα δεδομένα

**ii. Τεχνολογίες:**
- **CUDA**: Πλατφόρμα παράλληλης επεξεργασίας (NVIDIA)
- **GPGPU**: General-Purpose computing on GPUs

> [!INFO] **Ιδεατή Μνήμη (Virtual Memory)**:
>
> Μηχανισμός διαχείρισης που παρέχει:
> - Εντύπωση μεγάλου συνεχούς χώρου μνήμης
> - Ανεξαρτησία από φυσική RAM
> - Τεχνικές: Σελιδοποίηση (paging), Τμηματοποίηση (segmentation)
> - Αποφυγή συγκρούσεων, διαχείριση μεγαλύτερων datasets

### 5.2 Αρχιτεκτονική Heterogeneous Systems

```mermaid
graph TD
    subgraph "On-Chip Network"
        CPU1[CPU Core 1]
        CPU2[CPU Core n]
        GPU1[GPU Core 1]
        GPU2[GPU Core m]
    end
    
    CPU1 --> ICN[Interconnection Network]
    CPU2 --> ICN
    GPU1 --> ICN
    GPU2 --> ICN
    
    ICN --> LLC1[Last Level Cache]
    ICN --> LLC2[Last Level Cache]
    ICN --> DRAM1[DRAM Controller]
    ICN --> DRAM2[DRAM Controller]
    
    DRAM1 --> MEM1[Main Memory]
    DRAM2 --> MEM2[Main Memory]
```

**i. Κοινή Ιδεατή Μνήμη:**
- Προσβάσιμη από CPU και GPU
- Σελίδες μεταφέρονται στη φυσική μνήμη όταν απαιτείται

**ii. Πολιτική Συνοχής:**
- Διατήρηση ενημερωμένων δεδομένων σε CPU/GPU caches

**iii. Ενιαία Διεπαφή Προγραμματισμού:**
- Αξιοποίηση σειριακής ισχύος CPU
- Αξιοποίηση παράλληλης ισχύος GPU

### 5.3 Σύγκριση Απόδοσης CPU/GPU

**Παράδειγμα: AMD A10 5800K**

| Παράμετρος | CPU | GPU |
|------------|-----|-----|
| Συχνότητα ρολογιού | 3.8 GHz | 0.8 GHz |
| Πυρήνες | 4 | 384 |
| FLOPS/πυρήνα/κύκλο | 8 | 2 |
| **GFLOPS** | **121.6** | **614.4** |

**i. Συμπεράσματα:**
- GPU: Χαμηλότερη συχνότητα, αλλά περισσότεροι πυρήνες
- GPU: 5× υψηλότερη συνολική απόδοση σε παράλληλες εργασίες
- CPU: Ευέλικτη για σειριακές διεργασίες
- GPU: Ενδεικνυόμενη για γραφικά, ML, επιστημονικούς υπολογισμούς

---

## 6.0 Αρχιτεκτονική ARM

### 6.1 Εισαγωγή στην ARM

**i. Advanced RISC Machine:**
- Αρχικά: Acorn RISC Machine
- Βάση: Αρχιτεκτονική RISC (Reduced Instruction Set Computing)
- Κατασκευή: Πολλοί κατασκευαστές μέσω αδειών ARM Holdings

**ii. Διάδοση:**
- Έως 2017: >100 δισεκ. ARM επεξεργαστές παραγόμενοι
- Πιο διαδεδομένη αρχιτεκτονική συνόλου εντολών

> [!INFO] **RISC (Reduced Instruction Set Computing)**:
>
> **Βασικά Χαρακτηριστικά:**
> - Μικρό και βελτιστοποιημένο σύνολο εντολών
> - Κάθε εντολή εκτελείται σε ~1 κύκλο ρολογιού
> - Ομοιομορφία εντολών (σταθερό μήκος/δομή)
> - Εστίαση στο λογισμικό (compiler)
> - Αποδοτική χρήση καταχωρητών
>
> **Σύγχρονες Αρχιτεκτονικές:** ARM, MIPS, RISC-V

### 6.2 Αρχιτεκτονική big.LITTLE

**i. Έννοια:**
- Συνδυασμός πυρήνων υψηλής απόδοσης (big) και χαμηλής κατανάλωσης (LITTLE)
- Παρόμοιες αρχιτεκτονικές ISA, διαφορετικά χαρακτηριστικά

**ii. Στόχοι:**
- Ισορροπία μεταξύ απόδοσης και ενεργειακής αποδοτικότητας
- Κυρίως για smartphones, tablets

```mermaid
graph TB
    subgraph "big.LITTLE Architecture"
        subgraph "High Performance Cluster"
            A15_1[Cortex-A15]
            A15_2[Cortex-A15]
            A15_3[Cortex-A15]
            A15_4[Cortex-A15]
        end
        subgraph "Low Power Cluster"
            A7_1[Cortex-A7]
            A7_2[Cortex-A7]
            A7_3[Cortex-A7]
            A7_4[Cortex-A7]
        end
        L2_BIG[L2 Cache Big]
        L2_LITTLE[L2 Cache LITTLE]
    end
    
    A15_1 --> L2_BIG
    A15_2 --> L2_BIG
    A15_3 --> L2_BIG
    A15_4 --> L2_BIG
    
    A7_1 --> L2_LITTLE
    A7_2 --> L2_LITTLE
    A7_3 --> L2_LITTLE
    A7_4 --> L2_LITTLE
    
    L2_BIG --> CCI[CCI-400<br/>Cache Coherency Interconnect]
    L2_LITTLE --> CCI
    
    CCI --> GIC[GIC-400<br/>Interrupt Controller]
    CCI --> MEM[Memory Controllers]
```

### 6.3 Σύγκριση Απόδοσης Cortex-A7 vs A15

| Χαρακτηριστικό | Cortex-A7 | Cortex-A15 |
|----------------|-----------|------------|
| Απόδοση ανά MHz | 1× | ~2× |
| Ενεργειακή Αποδοτικότητα | 3× καλύτερη | 1× |
| Διασωλήνωση | 8-10 στάδια | 15-24 στάδια |
| Εκτέλεση | In-order | Out-of-order |
| Εντολές/κύκλο | 2 (5 execution units) | 3 (8 execution units) |
| Ουρά εντολών | Ενιαία | Ξεχωριστή ανά unit |

**i. Cortex-A15:**
- Διπλάσια απόδοση ανά MHz
- Υψηλότερη κατανάλωση

**ii. Cortex-A7:**
- Τρεις φορές πιο αποδοτικός ενεργειακά για ίδιο φορτίο
- 4 σημεία λειτουργίας ισχύος + idle mode

### 6.4 Λειτουργικά Μοντέλα big.LITTLE

#### 6.4.1 Clustered Switching

```mermaid
sequenceDiagram
    participant Scheduler as Linux Scheduler
    participant High as High Cluster (A57)
    participant Low as Low Cluster (A53)
    
    Note over Scheduler: Workload Arrives
    alt High Performance Needed
        Scheduler->>High: Activate A57 Cluster
        Note over High: All 4 cores available
        Note over Low: A53 Cluster OFF
    else Low Performance Needed
        Scheduler->>Low: Activate A53 Cluster
        Note over Low: All 4 cores available
        Note over High: A57 Cluster OFF
    end
```

**i. Χαρακτηριστικά:**
- Επιλογή **μίας συστάδας** τη φορά
- High Cluster: Αν χρειάζεται ≥1 πυρήνας υψηλής απόδοσης
- Low Cluster: Διαφορετικά

#### 6.4.2 In-Kernel Switcher

```mermaid
graph LR
    A[Virtual Core 1] --> B{CPUfreq Switch}
    C[Virtual Core 2] --> D{CPUfreq Switch}
    E[Virtual Core 3] --> F{CPUfreq Switch}
    G[Virtual Core 4] --> H{CPUfreq Switch}
    
    B --> I[A15 Core 1]
    B --> J[A7 Core 1]
    D --> K[A15 Core 2]
    D --> L[A7 Core 2]
    F --> M[A15 Core 3]
    F --> N[A7 Core 3]
    H --> O[A15 Core 4]
    H --> P[A7 Core 4]
    
    I -.-> Q[Highest Performance]
    J -.-> R[Lowest Power]
```

**i. Χαρακτηριστικά:**
- 4 SMP εικονικοί πυρήνες
- CPUfreq switch ανά εικονικό πυρήνα
- Εναλλαγή μεταξύ A15/A7 δυναμικά

#### 6.4.3 Heterogeneous Multi-Processing (HMP)

**i. Χαρακτηριστικά:**
- **Όλοι οι 8 πυρήνες** (4× A15 + 4× A7) ταυτόχρονα ενεργοί
- Linux Scheduler: 8 μη-συμμετρικοί πυρήνες
- Δρομολόγηση σε big ή LITTLE ανάλογα με workload

```mermaid
flowchart TD
    A[Task Queue] --> B{Scheduler Analysis}
    B -->|Heavy Workload| C[Assign to big Core<br/>Cortex-A15]
    B -->|Light Workload| D[Assign to LITTLE Core<br/>Cortex-A7]
    B -->|Mixed Workload| E[Distribute Across<br/>All 8 Cores]
    
    C --> F[High Performance<br/>High Power]
    D --> G[Low Performance<br/>Low Power]
    E --> H[Balanced<br/>Power/Performance]
```

### 6.5 ARM DynamIQ

**i. Εισαγωγή:**
- Πυρήνες: Cortex-A75, Cortex-A55
- Ενισχυμένη υποστήριξη AI/ML

**ii. Βελτιώσεις:**
- **>50× AI performance boost** στην CPU (3-5 έτη)
- **10× ταχύτερη απόκριση** σε επιταχυντές
- Dedicated processor instructions για AI
- Καλυτερη πρόσβαση σε acceleration

### 6.6 ARM Cortex-X1

| Χαρακτηριστικό | Τιμή |
|----------------|------|
| Ημερομηνία Κυκλοφορίας | 2020 |
| Σχεδιαστής | ARM Ltd. |
| Max Clock Rate | 3.0 GHz (phones), 3.3 GHz (tablets/laptops) |
| Address Width | 40-bit |
| L1 Cache | 128 KiB (64 KiB I-cache + 64 KiB D-cache) ανά πυρήνα |
| L2 Cache | 512–1024 KiB ανά πυρήνα |
| L3 Cache | 512 KiB – 8 MiB (optional) |

**i. Χαρακτηριστικά:**
- Υπερκλιμάκωση εκτός σειράς
- Λήψη 5 εντολών ανά κύκλο
- Παράθυρο 224 καταχωρητών
- SIMD units: 4×128b

---

## 7.0 Apple M1 Pro/Max

### 7.1 Προδιαγραφές

| Χαρακτηριστικό | M1 Pro | M1 Max |
|----------------|--------|--------|
| Ημερομηνία | 18 Οκτωβρίου 2021 | 18 Οκτωβρίου 2021 |
| Εφαρμογή | MacBook Pro | MacBook Pro |
| Τεχνολογία | 5 nm | 5 nm |
| Μικροαρχιτεκτονική | Firestorm + Icestorm | Firestorm + Icestorm |
| Σετ Εντολών | ARMv8.4-A | ARMv8.4-A |
| Τρανζίστορ | 33.7 δισεκ. | 57 δισεκ. |
| CPU Cores | 8 ή 10 (6-8 perf + 2 efficiency) | 10 (8 perf + 2 efficiency) |
| GPU Cores | Έως 16 | Έως 32 |
| Neural Engine | 16 πυρήνες, 600 δισεκ. ops/sec | 16 πυρήνες, 600 δισεκ. ops/sec |

**i. GPU Δομή:**
- Κάθε πυρήνας GPU: 16 execution units
- Κάθε execution unit: 8 ALUs

```mermaid
graph TD
    M1[Apple M1 Max] --> CPU[CPU Complex]
    M1 --> GPU[GPU Complex]
    M1 --> NE[Neural Engine]
    M1 --> MEM[Unified Memory]
    
    CPU --> PERF[8× Performance Cores<br/>Firestorm]
    CPU --> EFF[2× Efficiency Cores<br/>Icestorm]
    
    GPU --> GPU_CORES[32 GPU Cores]
    GPU_CORES --> EX[16 Execution Units per Core]
    EX --> ALU[8 ALUs per Execution Unit]
    
    NE --> AI[16 Cores<br/>600B ops/sec]
    
    MEM --> SHARED[Shared by CPU/GPU/NE]
```

---

## 8.0 Σύγκριση CPU και GPU

### 8.1 Δομικές Διαφορές

| Χαρακτηριστικό | CPU | GPU |
|----------------|-----|-----|
| Αριθμός Πυρήνων | Λίγοι ισχυροί (4-64) | Πολλοί απλοί (>1000) |
| Κρυφή Μνήμη | Μεγάλη ανά πυρήνα | Μικρή ανά πυρήνα |
| Εκτέλεση | Out-of-order | In-order (SIMD) |
| Branch Prediction | Εξελιγμένη | Βασική |
| Παραλληλία | Thread-level | Massive data parallelism |

**i. CPU:**
- Λίγοι ισχυροί πυρήνες
- Μεγάλη κρυφή μνήμη
- Πρόβλεψη διακλαδώσεων
- Εκτέλεση εντολών εκτός σειράς

**ii. GPU:**
- Πολλοί μικροί, απλοί πυρήνες
- In-order execution
- **SIMD** (Single Instruction Multiple Data): Παράλληλη επεξεργασία δεδομένων κινητής υποδιαστολής
- Σύγχρονες υλοποιήσεις: >1000 πυρήνες
  - NVIDIA Tesla V100: 5,120 CUDA cores
  - NVIDIA H100: 18,176 cores

### 8.2 Εξέλιξη Απόδοσης GPU vs CPU

```mermaid
graph LR
    A[2008: GPU M1060<br/>0.5 TFLOPS] --> B[2010: GPU M2090<br/>1.0 TFLOPS]
    B --> C[2012: GPU K20<br/>1.5 TFLOPS]
    C --> D[2014: GPU K80<br/>2.5 TFLOPS]
    D --> E[2016: GPU P100<br/>4.0 TFLOPS]
    
    A2[2008: CPU<br/>~0.1 TFLOPS] --> B2[2016: CPU<br/>~0.5 TFLOPS]
    
    style E fill:#00ff00
    style B2 fill:#ff9999
```

**i. Σύγχρονες Επιδόσεις:**
- NVIDIA Tesla V100: 7.5 TFLOPS (double precision), 15 TFLOPS (single precision)
- NVIDIA H100 (2022): 33.5 TFLOPS (double precision)

> [!INFO] **TFLOPS (Tera Floating Point Operations Per Second)**:
>
> Μονάδα μέτρησης απόδοσης:
> - 1 TFLOPS = 1 τρισεκατομμύριο πράξεις κινητής υποδιαστολής/δευτερόλεπτο
> - Κρίσιμο για επιστημονικούς υπολογισμούς, προσομοιώσεις, AI
>
> **Single Precision (FP32 - 32 bits):**
> - 1 bit: πρόσημο
> - 8 bits: εκθέτης
> - 23 bits: κλασματικό μέρος
> - Ακρίβεια: ~7 δεκαδικά ψηφία
> - Χρήση: ML, γραφικά
>
> **Double Precision (FP64 - 64 bits):**
> - 1 bit: πρόσημο
> - 11 bits: εκθέτης
> - 52 bits: κλασματικό μέρος
> - Ακρίβεια: ~15 δεκαδικά ψηφία
> - Χρήση: Επιστημονικές προσομοιώσεις, χρηματοοικονομικά μοντέλα

---

## 9.0 Αρχιτεκτονική NVIDIA Fermi

### 9.1 Εισαγωγή

**i. Σημασία:**
- Πρώτη GPU αρχιτεκτονική για γραφικά **και** GPGPU
- Έτος κυκλοφορίας: ~2010

**ii. Βασικά Χαρακτηριστικά:**
- **64-bit διευθυνσιοδότηση μνήμης**: Διαχείριση μεγαλύτερων όγκων δεδομένων
- **Unified Memory**: Ευκολότερη συνεργασία CPU-GPU
- **CUDA βελτιώσεις**: Ανάλυση δεδομένων, εκπαίδευση νευρωνικών δικτύων
- **DirectX 11**: Δυναμικός φωτισμός, σκιές, πολύπλοκα εφέ
- Θεμέλια για GeForce GTX σειρά

```mermaid
graph TD
    HOST[Host Interface<br/>PCIe] --> GIGA[GigaThread<br/>Global Scheduler]
    
    GIGA --> SM1[SM 1]
    GIGA --> SM2[SM 2]
    GIGA --> SM3[SM ...]
    GIGA --> SM16[SM 16]
    
    SM1 --> L2[L2 Cache<br/>768 KB]
    SM2 --> L2
    SM3 --> L2
    SM16 --> L2
    
    L2 --> DRAM1[DRAM<br/>Interface 1]
    L2 --> DRAM2[DRAM<br/>Interface 2]
    L2 --> DRAM3[DRAM<br/>Interface ...]
    L2 --> DRAM6[DRAM<br/>Interface 6]
    
    DRAM1 --> MEM[GDDR5 Memory<br/>384-bit total]
```

### 9.2 Δομή Streaming Multiprocessor (SM)

**i. Περιεχόμενα ανά SM:**
- 2 στήλες × 32 πυρήνες CUDA = **64 CUDA cores**
- 16 μονάδες Load/Store (LD/ST)
- 4 Special Function Units (SFU)

**ii. Αρχείο Καταχωρητών:**
- 32K × 32-bit registers

**iii. Δρομολογητής Νημάτων:**
- Διπλός SIMD thread scheduler
- Διάσπαση νημάτων σε δέσμες 32 νημάτων (warps)
- Κάθε νήμα: Δικό του instruction counter + register set

**iv. Μονάδες Ειδικών Λειτουργιών (SFU):**
- Πράξεις: sin, cos, αντίστροφοι, τετραγωνική ρίζα
- Απόδοση: 1 κύκλος ρολογιού (8 κύκλοι για 32 παράλληλα νήματα)

**v. Shared Memory/L1 Cache:**
- 64 KB κοινόχρηστη ανά SM

> [!INFO] **Streaming Multiprocessors (SMs)**:
>
> Βασικές υπολογιστικές μονάδες GPU:
> - Πυρήνες υψηλής παράλληλης επεξεργασίας
> - Εκτέλεση μεγάλου αριθμού νημάτων ταυτόχρονα
>
> **Χαρακτηριστικά:**
> 1. **Πολλαπλή παράλληλη επεξεργασία**: Δεκάδες-εκατοντάδες νήματα
> 2. **Εξειδικευμένες μονάδες**: FP, LD/ST, SFU
> 3. **Τοπική κρυφή μνήμη**: Μείωση καθυστέρησης πρόσβασης
> 4. **Ευελιξία**: Γραφικά και GPGPU

### 9.3 Fermi Architecture Overview

| Στοιχείο | Προδιαγραφή |
|----------|-------------|
| Αριθμός SM | 16 |
| CUDA Cores ανά SM | 32 (2 στήλες × 16) |
| Συνολικοί CUDA Cores | 512 |
| LD/ST Units ανά SM | 16 |
| SFU ανά SM | 4 |
| L2 Cache | 768 KB (κοινόχρηστο) |
| Memory Interfaces | 6 × 64-bit = 384-bit |
| Memory Type | GDDR5 |

```mermaid
graph TB
    subgraph "Streaming Multiprocessor (SM)"
        ICACHE[Instruction Cache] --> SCHED1[SIMD Thread Scheduler 1]
        ICACHE --> SCHED2[SIMD Thread Scheduler 2]
        
        SCHED1 --> DISP1[Dispatch Unit 1]
        SCHED2 --> DISP2[Dispatch Unit 2]
        
        RF[Register File<br/>32,768 × 32-bit]
        
        DISP1 --> CORE1[16 CUDA Cores]
        DISP1 --> LDST1[LD/ST Units]
        DISP1 --> SFU1[SFU]
        
        DISP2 --> CORE2[16 CUDA Cores]
        DISP2 --> LDST2[LD/ST Units]
        DISP2 --> SFU2[SFU]
        
        CORE1 --> SHARED[64 KB Shared Memory/L1 Cache]
        CORE2 --> SHARED
        LDST1 --> SHARED
        LDST2 --> SHARED
    end
```

### 9.4 Parallel Processing Characteristics

**i. GigaThread Scheduler:**
- Διανομή thread blocks στους 16 SMs
- Κάθε SM: Δικός του local thread scheduler

**ii. Latency Hiding:**
- Πολλά νήματα συγκαλύπτουν καθυστερήσεις μνήμης
- Λεπτή νημάτωση (fine-grained threading)

**iii. CUDA Core Cooperation:**
- Πυρήνες συνεργάζονται ανά δύο για FP64 operations

### 9.5 Εξέλιξη Αρχιτεκτονικών NVIDIA

| Αρχιτεκτονική | FP32 Units/SM | FP64 Units/SM | Ειδικά Χαρακτηριστικά |
|---------------|---------------|---------------|-----------------------|
| **Tesla** | 8 | - | Πρώτη CUDA αρχιτεκτονική |
| **Fermi** | 32 | 16 | 64-bit addressing, Unified Memory |
| **Kepler** | 192 | 64 | Υψηλότερη παραλληλία |
| **Maxwell** | 128 | 4 | Ενεργειακή αποδοτικότητα |
| **Pascal** | 64 | 32 | FP16 support (2×FP16 per FP32 core) |
| **Volta/Turing** | 64 | 32 | **Tensor Cores** για AI |

**i. Volta & Turing Innovations:**
- **Tensor Cores**: Αφιερωμένες μονάδες AI/ML
- Ανάλυση προβλημάτων σε υπερυπολογιστές
- Επεξεργασία σε consumer GPUs

```mermaid
timeline
    title Εξέλιξη NVIDIA GPU Architectures
    2006 : Tesla - 8 FP32/SM
    2010 : Fermi - 32 FP32/SM : 64-bit addressing
    2012 : Kepler - 192 FP32/SM : Massive parallelism
    2014 : Maxwell - 128 FP32/SM : Energy efficiency
    2016 : Pascal - 64 FP32/SM : FP16 support
    2017 : Volta - Tensor Cores : AI acceleration
    2018 : Turing - RT Cores : Ray tracing
```

---

## 10.0 Συμπεράσματα και Τάσεις

### 10.1 Βασικές Αρχές Πολυπύρηνης Σχεδίασης

**i. Hardware Constraints:**
- Κανόνας Pollack: $ \text{Performance} \propto \sqrt{\text{Complexity}} $
- Power density αυξάνεται εκθετικά
- Λύση: Πολλαπλοί απλούστεροι πυρήνες

**ii. Software Constraints:**
- Νόμος Amdahl περιορίζει speedup
- Σειριακός κώδικας = bottleneck
- Overhead επικοινωνίας και συγχρονισμού

**iii. Memory Hierarchy:**
- L1: Dedicated, ταχύτερη
- L2: Dedicated ή Shared
- L3: Shared, μεγαλύτερη χωρητικότητα

### 10.2 Heterogeneous Computing

```mermaid
graph LR
    A[Workload] --> B{Task Analysis}
    B -->|Serial Tasks| C[CPU<br/>Few Strong Cores]
    B -->|Parallel Tasks| D[GPU<br/>Many Simple Cores]
    B -->|AI/ML Tasks| E[Neural Engine<br/>Specialized Units]
    
    C --> F[Unified Memory]
    D --> F
    E --> F
    
    F --> G[Optimized Performance]
```

**i. CPU Strengths:**
- Σειριακή απόδοση
- Branch prediction
- Out-of-order execution

**ii. GPU Strengths:**
- Massive parallelism (SIMD)
- Throughput optimization
- Floating-point operations

**iii. Specialized Accelerators:**
- Tensor Cores: AI/ML
- Neural Engines: On-device inference
- RT Cores: Ray tracing

### 10.3 Μελλοντικές Τάσεις

**i. Process Technology:**
- Από 10 μm (1971) → 2 nm (2024)
- Moore's Law συνεχίζει (με αργότερο ρυθμό)

**ii. Architectural Innovations:**
- ARM DynamIQ: >50× AI boost σε 3-5 έτη
- Wafer-scale chips: 2600 δισεκ. τρανζίστορ
- 3D stacking technologies

**iii. Software Adaptation:**
- Παραλληλοποίηση αλγορίθμων
- Heterogeneous programming models (CUDA, OpenCL)
- AI-driven workload optimization

---

## Παράρτημα: Βασικοί Τύποι

### Α.1 Νόμος του Amdahl

$$
S = \frac{1}{(1-f) + \frac{f}{N}}
$$

- $ S $: Speedup
- $ f $: Παράλληλο τμήμα προγράμματος
- $ N $: Αριθμός επεξεργαστών

### Α.2 Κανόνας Pollack

$$
\text{Performance} \propto \sqrt{\text{Complexity}}
$$

Διπλασιασμός πολυπλοκότητας → ~40% αύξηση απόδοσης

### Α.3 Υπολογισμός GFLOPS

$$
\text{GFLOPS} = \text{Cores} \times \text{Clock (GHz)} \times \frac{\text{FLOPS}}{\text{Core/Cycle}}
$$

**Παράδειγμα (AMD A10 GPU):**
$$
\text{GFLOPS} = 384 \times 0.8 \times 2 = 614.4 \text{ GFLOPS}
$$

---

## Αναφορές και Πηγές

- Πανεπιστήμιο Ιωαννίνων - Τμήμα Πληροφορικής & Τηλεπικοινωνιών
- Διδάσκων: Αλέξανδρος Μπανταλούκας-Αρτζμάντ (k.arjmand@uoi.gr)
- Επιμέλεια: Κωνσταντίνος Σακκάς (ksakkas@uoi.gr)
- Κεφάλαιο 18: Αρχιτεκτονική Υπολογιστών (3ο Εξάμηνο)