# 12. FPGA & Σύνθεση

Το κεφάλαιο αυτό κλείνει τον κύκλο σχεδίασης ψηφιακών συστημάτων, από τη VHDL περιγραφή έως την πραγματική υλοποίηση σε FPGA. Η κατανόηση της αρχιτεκτονικής FPGA, της ροής σύνθεσης και των εργαλείων είναι απαραίτητη για τη μετατροπή κώδικα VHDL σε ψηφιακό υλικό.

---

## 1. Αρχιτεκτονική FPGA

### 1.1 LUT (Look-Up Table)

Η βασική μονάδα για υλοποίηση συνδυαστικής λογικής. Κάθε LUT αποθηκεύει truth table:
- **4-input LUT:** $2^4 = 16$ entries
- **6-input LUT:** $2^6 = 64$ entries

> **[Key Insight]** Κάθε συνδυαστική συνάρτηση μπορεί να υλοποιηθεί με μία LUT, αν ο αριθμός των εισόδων είναι $\leq k$ (όπου $k$ είναι ο αριθμός εισόδων της LUT).

### 1.2 Flip-Flops μέσα σε Slice/CLB

Κάθε Configurable Logic Block (CLB) ή slice περιλαμβάνει:
- 1-2 LUTs
- Flip-flops (D-FF)
- MUX, carry logic, Wide Function Generator

### 1.3 Block RAM (BRAM)

Προαιρετική μνήμη υλικού:
- **Xilinx:** 18Kb ή 36Kb blocks
- **Intel/Altera:** M9K, M20K blocks
- Μπορούν να συνδεθούν σε μεγαλύτερες μνήμες

### 1.4 DSP Blocks

Εξειδικευμένοι πολλαπλασιαστές/αθροιστές:
- 18x18 ή 25x18 πολλαπλασιασμός
- Κατάλληλοι για DSP αλγορίθμους, FIR filters

### 1.5 I/O Blocks (IOB)

Διεπαφή μεταξύ του FPGA και του εξωτερικού κόσμου:
- Υποστήριξη πολλαπλών ταχυτήτων I/O
- Differential I/O standards (LVDS)
- Pull-up/Pull-down resistors

### 1.6 Interconnect (Routing Resources)

Δίκτυο αλληλοσύνδεσης μεταξύ των CLBs:
- Πολύπλοκος δρομολογητής
- Ο χρόνος διέλευσης (routing delay) μπορεί να υπερβεί τον λογικό χρόνο

---

## 2. CPLD vs FPGA vs ASIC

### 2.1 CPLD (Complex Programmable Logic Device)

- **Μνήμη:** Non-volatile (EEPROM/Flash)
- **Πυκνότητα:** Μικρότερη
- **Ταχύτητα:** Πιο απρόβλεπτη καθυστέρηση
- **Κατάλληλος για:** Απλά συνδυαστικά κυκλώματα, glue logic

### 2.2 FPGA (Field-Programmable Gate Array)

- **Μνήμη:** SRAM-based (χάνει configuration χωρίς εξωτερική μνήμη)
- **Πυκνότητα:** Υψηλή (εκατομμύρια λογικές πόρτες)
- **Flexibility:** Πολύ υψηλή
- **Κατάλληλος για:** Πολύπλοκα συστήματα, prototypes, DSP

### 2.3 ASIC (Application-Specific IC)

- **Πλήρης σχεδίαση:** Custom layout
- **Μαζική παραγωγή:** Υψηλό κόστος ανάπτυξης, χαμηλό κόστος ανά μονάδα
- **Απόδοση:** Καλύτερη (ταχύτητα, κατανάλωση)

| Χαρακτηριστικό | CPLD | FPGA | ASIC |
|:---|:---:|:---:|:---:|
| Reconfigurable | Ναι | Ναι | Όχι |
| Non-volatile | Ναι | Όχι | Ν/Α |
| Πυκνότητα | Χαμηλή | Υψηλή | Πολύ υψηλή |
| Κόστος ανάπτυξης | Χαμηλό | Μέτριο | Πολύ υψηλό |
| Time-to-market | Ταχύ | Ταχύ | Αργό |

---

## 3. Ροή Σχεδίασης

### 3.1 RTL Design (VHDL)

Σύνταξη κώδικα VHDL που περιγράφει τη λειτουργία σε επίπεδο RTL (Register Transfer Level).

### 3.2 Simulation (Functional)

Έλεγχος λογικής συμπεριφοράς χωρίς χρονισμό (no timing delays).

### 3.3 Synthesis → Netlist

Μετατροπή VHDL σε netlist: λίστα πυλών και συνδέσεων (gate-level).

**Στάδια synthesis:**
1. Parsing και επικύρωση κώδικα
2. Optimization (Boolean, K-Map, technology mapping)
3. Mapping σε τεχνολογία (LUTs, FFs, BRAMs)
4. Παραγωγή netlist

### 3.4 Place & Route (PAR)

- **Place:** Τοποθέτηση λογικών σε συγκεκριμένες CLBs/BRAMs/DSPs
- **Route:** Σύνδεση μεταξύ των μονάδων μέσω interconnect

### 3.5 Timing Analysis (Post-PAR)

Έλεγχος ότι όλα τα timing constraints εκπληρώνονται:
- **Setup constraint:** $t_{clk} > t_{combinational} + t_{setup}$
- **Hold constraint:** $t_{hold} < t_{clk} - t_{combinational}$

### 3.6 Bitstream Generation & Programming

Η τελική δυαδική εικόνα που φορτώνεται στο FPGA:
- Xilinx: `.bit` (δυαδικό), `.rbt` (text)
- Intel: `.sof` (SRAM Object File), `.pof` (Programmer Object File)

---

## 4. Εργαλεία

### 4.1 Xilinx Vivado / ISE

- Vivado: νεότερο, σύγχρονο, Zynq/MicroBlaze support
- ISE: παλαιότερο, Spartan/older families

### 4.2 Intel Quartus Prime

- Lite Edition: δωρεάν
- Pro Edition: επαγγελματικό

### 4.3 GHDL + GTKWave

- **GHDL:** Open-source VHDL simulator (analysis + elaboration)
- **GTKWave:** Open-source waveform viewer
- Κατάλληλο για ανάπτυξη χωρίς εμπόριο εργαλεία

### 4.4 ModelSim / QuestaSim

- Εμπορικό simulator
- Υποστήριξη VHDL/Verilog/SystemVerilog
- Coverage analysis, assertions

---

## 5. IP Cores

### 5.1 Τύποι IP Cores

- **FIFO:** First-In-First-Out buffer
- **PLL:** Phase-Locked Loop (clock generation)
- **Memory controllers:** DDR, BRAM controllers
- **UART/SPI/I2C:** Serial communication

### 5.2 Χρήση IP Catalog

Στο Vivado: IP Catalog → προσθήκη IP → configuration → instantiation.

### 5.3 Component Instantiation

```vhdl
-- Instance of IP core
blk_mem: entity work.blk_mem_gen_0
    port map (
        clka  => clk,
        ena   => '1',
        wea   => "1",
        addra => addr,
        dina  => data_in,
        douta => data_out
    );
```

---

## Solved Exercises

### Exercise 1: LUT Υπολογισμός

**Problem:** Πόσες 4-input LUTs απαιτούνται για 4-bit XOR;

**Solution:**

Η 4-bit XOR είναι μία συνδυαστική συνάρτηση 8 εισόδων ($A_3A_2A_1A_0 \oplus B_3B_2B_1B_0$). Αν διαμερίσουμε σε 4 ξεχωριστές 1-bit XOR, χρειαζόμαστε 4 LUTs (κάθε μία για $A_i \oplus B_i$).

### Exercise 2: FPGA Resource Estimation

**Problem:** Ένα κύκλωμα έχει 100 πύλες, 50 FFs, 4 BRAMs. Πόσα resources χρειάζεται;

**Solution:**

- 100 LUTs (κάθε πύλη ~1 LUT) + 50 FFs + 4 BRAM blocks
- Για Xilinx Artix-7: 20K LUTs, 35K FFs → αρκετός χώρος

### Exercise 3: Timing Constraint

**Problem:** Ένα κύκλωμα έχει combinational delay 8ns και FF setup time 1ns. Ποια είναι η μέγιστη συχνότητα ρολογιού;

**Solution:**
$$
f_{max} = \frac{1}{t_{comb} + t_{setup}} = \frac{1}{8 + 1} = 111.1 \text{ MHz}
$$

### Exercise 4: Synthesis Flow

**Problem:** Να περιγραφεί η ροή από VHDL έως bitstream.

**Solution:**
1. VHDL source → Synthesis (optimization, technology mapping)
2. Synthesis → Netlist (gate-level)
3. Netlist + Constraints → Place & Route
4. PAR → Timing analysis (επιβεβαίωση setup/hold)
5. PAR → Bitstream generation
6. Bitstream → FPGA programming (via JTAG, USB)

### Exercise 5: CPLD vs FPGA επιλογή

**Problem:** Ένα project χρειάζεται 500 πύλες, non-volatile configuration. Επιλογή;

**Solution:**

CPLD: non-volatile, αρκετός για 500 πύλες. FPGA δεν ταίριαζε επειδή απαιτεί εξωτερική μνήμη για configuration.

### Exercise 6: GHDL Simulation

**Problem:** Πώς εκτελείται simulation με GHDL;

**Solution:**
```bash
ghdl -a my_design.vhd          -- Analysis
ghdl -e my_design              -- Elaboration
ghdl -r my_design --vcd=out.vcd -- Run + waveform
gtkwave out.vcd                -- View waveform
```

### Exercise 7: IP Core FIFO

**Problem:** Πότε χρησιμοποιείται FIFO IP core;

**Solution:**

- Clock domain crossing (μεταξύ δύο διαφορετικών ρολογίων)
- Data buffering (όταν η πηγή είναι ταχύτερη από τον παραλήπτη)
- Async FIFO με grey code pointers για ασφάλεια

### Exercise 8: Critical Path Βελτίωση

**Problem:** Το critical path είναι 15ns. Πώς μπορεί να μειωθεί;

**Solution:**

1. **Pipelining:** Προσθήκη FF registers μεσοδιαστατικά
2. **Logic restructuring:** Απλοποίηση Boolean
3. **Retiming:** Μετακίνηση FFs για ισορροπία
4. **Faster technology:** Εναλλαγή FPGA family
5. **Parallelism:** Αντικατάσταση σειριακής λογικής με παράλληλη

---

## Exam Tip: Επιλογη Εργαλειου για Εξεταση

Σε εξέταση:
- Αν σας ζητηθεί να περιγράψετε τη ροή σχεδίασης: αναφερθείτε στα 6 στάδια (RTL → Sim → Synthesis → PAR → Timing → Bitstream)
- Αν σας ζητηθεί να επιλέξετε μεταξύ FPGA/CPLD/ASIC: εξαρτάται από πολυπλοκότητα, κόστος, αν θέλετε reconfiguration
- Αν σας ζητηθεί να ελέγξετε timing: χρησιμοποιήστε $f_{max} = 1/(t_{comb} + t_{setup} + t_{clk-to-q})$