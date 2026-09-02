# Ψηφιακά Ηλεκτρονικά με VHDL - Νοητικός Χάρτης

***

## 1. Συστήματα Αριθμών & Δυαδική Αριθμητική (Simulator: `1_Binary_Arithmetic_Visualizer.html`)

### 1.1 Συστήματα Αριθμών
- 1.1.1 Δυαδικό (Βάση 2), Οκταδικό (Βάση 8), Δεκαεξαδικό (Βάση 16)
- 1.1.2 Μετατροπές μεταξύ βάσεων
- 1.1.3 BCD (Binary Coded Decimal)
- 1.1.4 Κώδικας Gray

### 1.2 Παράσταση Αρνητικών Αριθμών
- 1.2.1 Πρόσημο-Μέτρο (Sign-Magnitude)
- 1.2.2 Συμπλήρωμα ως προς 1 (1's complement)
- 1.2.3 Συμπλήρωμα ως προς 2 (2's complement)
- 1.2.4 Εύρος τιμών n-bit: \([-2^{n-1},\ 2^{n-1}-1]\)

### 1.3 Δυαδική Αριθμητική
- 1.3.1 Πρόσθεση: carry propagation
- 1.3.2 Αφαίρεση με 2's complement
- 1.3.3 Πολλαπλασιασμός και διαίρεση (ολισθήσεις)
- 1.3.4 Overflow ανίχνευση

### 1.4 Κωδικοποίηση Χαρακτήρων
- 1.4.1 ASCII
- 1.4.2 Unicode (βασικά)
- 1.4.3 Κώδικες ανίχνευσης σφαλμάτων (Parity, Hamming)

***

## 2. Άλγεβρα Boole & Λογικές Πύλες (Simulator: `2_Function_to_Truth_table.html`)

### 2.1 Βασικές Αρχές
- 2.1.1 Αξιώματα Boole
- 2.1.2 Ιδιότητες: αντιμεταθετική, προσεταιριστική, κατανεμητική
- 2.1.3 Θεωρήματα De Morgan: \(\overline{A \cdot B} = \bar{A} + \bar{B}\)
- 2.1.4 Αρχή δυισμού

### 2.2 Λογικές Πύλες
- 2.2.1 AND, OR, NOT (βασικές)
- 2.2.2 NAND, NOR (καθολικές πύλες)
- 2.2.3 XOR, XNOR
- 2.2.4 Υλοποίηση οποιασδήποτε συνάρτησης με NAND ή NOR

### 2.3 Πίνακες Αλήθειας
- 2.3.1 Κατασκευή για n μεταβλητές (\(2^n\) γραμμές)
- 2.3.2 Αναγνώριση minterm / maxterm
- 2.3.3 Συνθήκες don't care (X)

### 2.4 Τεχνολογίες Υλοποίησης
- 2.4.1 TTL (Transistor-Transistor Logic)
- 2.4.2 CMOS
- 2.4.3 Χαρακτηριστικά: fan-in, fan-out, noise margin, propagation delay

***

## 3. Κανονικές Μορφές - SOP / POS (Simulators: `3_Sum_of_Minterms_Visualizer.html`, `4_Product_of_Maxterms_Visualizer.html`)

### 3.1 Κανονική SOP (Sum of Minterms)
- 3.1.1 Minterm: γινόμενο όλων των μεταβλητών
- 3.1.2 Παράσταση: \(F = \sum m(i,j,...)\)
- 3.1.3 Κατασκευή από πίνακα αλήθειας (γραμμές = 1)

### 3.2 Κανονική POS (Product of Maxterms)
- 3.2.1 Maxterm: άθροισμα όλων των μεταβλητών
- 3.2.2 Παράσταση: \(F = \prod M(i,j,...)\)
- 3.2.3 Κατασκευή από πίνακα αλήθειας (γραμμές = 0)

### 3.3 Σχέση SOP ↔ POS
- 3.3.1 Συμπληρωματικοί δείκτες
- 3.3.2 Μετατροπή μέσω De Morgan
- 3.3.3 Τυπική vs κανονική μορφή

***

## 4. Απλοποίηση Boole (Simulator: `5_Kmap_Visualizer.html`)

### 4.1 Χάρτης Karnaugh (K-Map)
- 4.1.1 Διάταξη 2, 3, 4 μεταβλητών (Gray code ordering)
- 4.1.2 Ομαδοποίηση: 1, 2, 4, 8 κελιά (δυνάμεις του 2)
- 4.1.3 Πρωταρχικοί συνεπαγωγείς (Prime Implicants - PI)
- 4.1.4 Απαραίτητοι συνεπαγωγείς (Essential PI)
- 4.1.5 Χειρισμός don't care conditions
- 4.1.6 5-μεταβλητός K-Map

### 4.2 Μέθοδος Quine-McCluskey (QMC)
- 4.2.1 Αλγοριθμική απλοποίηση (κατάλληλη για >4 μεταβλητές)
- 4.2.2 Πίνακας κάλυψης (covering table)
- 4.2.3 Εύρεση ελάχιστης κάλυψης

### 4.3 Υλοποίηση 2 Επιπέδων
- 4.3.1 AND-OR (SOP)
- 4.3.2 OR-AND (POS)
- 4.3.3 NAND-NAND, NOR-NOR ισοδύναμα

***

## 5. Συνδυαστικά Κυκλώματα (Simulator: `6_function_to_diagram.html`)

### 5.1 Αρχές Σχεδίασης
- 5.1.1 Έξοδος εξαρτάται μόνο από τρέχουσες εισόδους
- 5.1.2 Μεθοδολογία: προδιαγραφή → πίνακας → ελαχιστοποίηση → υλοποίηση
- 5.1.3 Στατικοί κίνδυνοι (Hazards)

### 5.2 Μετατροπείς Κωδικών
- 5.2.1 BCD → 7-segment display
- 5.2.2 Binary ↔ Gray code
- 5.2.3 BCD ↔ Excess-3

### 5.3 Συγκριτές Μεγέθους
- 5.3.1 1-bit, n-bit συγκριτής
- 5.3.2 Έξοδοι: A>B, A=B, A<B

***

## 6. Αποκωδικοποιητές, Κωδικοποιητές & Πολυπλέκτες (Simulator: `9_decoder_combinational_logic_simulator.html`)

### 6.1 Αποκωδικοποιητές (Decoders)
- 6.1.1 n-to-2ⁿ decoder
- 6.1.2 Υλοποίηση λογικών συναρτήσεων με decoder + OR
- 6.1.3 Enable εισαγωγή, cascading

### 6.2 Κωδικοποιητές (Encoders)
- 6.2.1 2ⁿ-to-n encoder
- 6.2.2 Priority encoder
- 6.2.3 Εφαρμογές: interrupt handling

### 6.3 Πολυπλέκτες (MUX)
- 6.3.1 2ⁿ-to-1 MUX
- 6.3.2 Υλοποίηση οποιασδήποτε συνάρτησης με MUX
- 6.3.3 Cascading MUX για n μεταβλητές
- 6.3.4 Αποπολυπλέκτης (DEMUX)

***

## 7. Αθροιστές & Αριθμητικές Μονάδες (Simulator: `10_full_adder_mux_simulator.html`)

### 7.1 Ημιαθροιστής (Half Adder)
- 7.1.1 Είσοδοι: A, B → Έξοδοι: Sum, Carry
- 7.1.2 Sum = A XOR B, Carry = A AND B

### 7.2 Πλήρης Αθροιστής (Full Adder)
- 7.2.1 Είσοδοι: A, B, Cin → Έξοδοι: Sum, Cout
- 7.2.2 Υλοποίηση με 2 ημιαθροιστές
- 7.2.3 VHDL μοντελοποίηση (behavioral, structural, dataflow)

### 7.3 Παράλληλος Αθροιστής Ripple Carry
- 7.3.1 n-bit adder: αλυσιδωτή σύνδεση FA
- 7.3.2 Καθυστέρηση: \(T = n \cdot T_{FA}\)

### 7.4 Carry Lookahead Adder (CLA)
- 7.4.1 Generate: \(G_i = A_i \cdot B_i\)
- 7.4.2 Propagate: \(P_i = A_i + B_i\)
- 7.4.3 Ταχύτητα vs πολυπλοκότητα

### 7.5 Αφαιρέτης
- 7.5.1 Με 2's complement και αθροιστή

### 7.6 ALU (Arithmetic Logic Unit)
- 7.6.1 Συνδυασμός αριθμητικών + λογικών λειτουργιών
- 7.6.2 Επιλογή λειτουργίας με MUX

***

## 8. Flip-Flops, Καταχωρητές & Μετρητές (Simulator: `7_4bit_d_flipflop_register_simulator.html`)

### 8.1 Αστάτες (Latches)
- 8.1.1 SR Latch (NAND/NOR)
- 8.1.2 D Latch (level-triggered)
- 8.1.3 Ανεπιθύμητη κατάσταση (forbidden state)

### 8.2 Flip-Flops (Edge-triggered)
- 8.2.1 SR FF
- 8.2.2 D FF: Q(t+1) = D
- 8.2.3 JK FF: Q(t+1) = J·Q' + K'·Q
- 8.2.4 T FF: Q(t+1) = T XOR Q
- 8.2.5 Master-Slave JK FF
- 8.2.6 Asynchronous vs Synchronous (preset, clear)

### 8.3 Μετατροπές Flip-Flops
- 8.3.1 Πίνακες διέγερσης (excitation tables)
- 8.3.2 D→JK, JK→D, T→D κ.λπ.

### 8.4 Καταχωρητές (Registers)
- 8.4.1 4-bit D FF register (parallel load)
- 8.4.2 Shift registers: SISO, SIPO, PISO, PIPO
- 8.4.3 Universal Shift Register
- 8.4.4 Εφαρμογές: buffer, serial communication

### 8.5 Μετρητές (Counters)
- 8.5.1 Ασύγχρονος (Ripple) μετρητής
- 8.5.2 Σύγχρονος μετρητής
- 8.5.3 Μετρητής mod-N (произвольная последовательность)
- 8.5.4 Ring Counter, Johnson Counter
- 8.5.5 Up/Down Counter

***

## 9. Ακολουθιακά Κυκλώματα & FSM (Simulator: `8_interactive_state_table_converter.html`)

### 9.1 Θεωρία Ακολουθιακών Κυκλωμάτων
- 9.1.1 Έξοδος εξαρτάται από εισόδους + τρέχουσα κατάσταση
- 9.1.2 Σύγχρονα vs Ασύγχρονα
- 9.1.3 Moore vs Mealy μοντέλα

### 9.2 Παράσταση FSM
- 9.2.1 Διάγραμμα καταστάσεων (State Diagram)
- 9.2.2 Πίνακας καταστάσεων (State Table)
- 9.2.3 Κωδικοποίηση καταστάσεων (binary, one-hot, gray)

### 9.3 Σχεδίαση FSM
- 9.3.1 Ανάλυση: κύκλωμα → πίνακας → διάγραμμα
- 9.3.2 Σύνθεση: προδιαγραφή → ελαχιστοποίηση → υλοποίηση
- 9.3.3 Ελαχιστοποίηση καταστάσεων (State Reduction)
  - 9.3.3.1 Μέθοδος ισοδύναμων ζευγών
  - 9.3.3.2 Πίνακας ισοδυναμίας (Implication Table)

### 9.4 Πίνακες Διέγερσης & Εξόδου
- 9.4.1 Excitation table ανά τύπο FF
- 9.4.2 K-Map για εξισώσεις επόμενης κατάστασης
- 9.4.3 K-Map για εξισώσεις εξόδου

### 9.5 Παραδείγματα FSM
- 9.5.1 Ανιχνευτής ακολουθίας (sequence detector)
- 9.5.2 Ελεγκτής κυκλοφορίας
- 9.5.3 Σύγχρονος μετρητής mod-N

***

## 10. VHDL - Βασικά (Διάλεξη 10)

### 10.1 Εισαγωγή στη VHDL
- 10.1.1 Hardware Description Language (HDL): περιγραφή υλικού, όχι προγραμματισμός
- 10.1.2 IEEE Std 1076 (1987, 1993, 2008)
- 10.1.3 Ροή σχεδίασης: RTL → σύνθεση → place & route → bitstream

### 10.2 Δομή Αρχείου VHDL
- 10.2.1 Library / Use clauses: `LIBRARY ieee; USE ieee.std_logic_1164.ALL;`
- 10.2.2 Entity: ορισμός διεπαφής (ports)
- 10.2.3 Architecture: περιγραφή συμπεριφοράς/δομής
- 10.2.4 Configuration (βασικά)

### 10.3 Τύποι Δεδομένων
- 10.3.1 `std_logic`: '0','1','Z','X','U','W','L','H','-'
- 10.3.2 `std_logic_vector(n downto 0)`
- 10.3.3 `integer`, `natural`, `positive`
- 10.3.4 `boolean`, `bit`, `bit_vector`
- 10.3.5 `signed`, `unsigned` (ieee.numeric_std)

### 10.4 Τελεστές
- 10.4.1 Λογικοί: `and`, `or`, `not`, `nand`, `nor`, `xor`, `xnor`
- 10.4.2 Αριθμητικοί: `+`, `-`, `*`, `/`
- 10.4.3 Σύγκρισης: `=`, `/=`, `<`, `>`, `<=`, `>=`
- 10.4.4 Ολίσθησης: `sll`, `srl`, `sla`, `sra`, `rol`, `ror`
- 10.4.5 Συνένωσης: `&`

### 10.5 Στυλ Αρχιτεκτονικής
- 10.5.1 **Behavioral** (συμπεριφορικό): `process`, `if-else`, `case`
- 10.5.2 **Dataflow** (ροή δεδομένων): ταυτόχρονες εντολές ανάθεσης
- 10.5.3 **Structural** (δομικό): component instantiation, port map

### 10.6 Ταυτόχρονες Εντολές (Concurrent Statements)
- 10.6.1 Signal assignment: `Y <= A and B;`
- 10.6.2 `when-else` (conditional signal assignment)
- 10.6.3 `with-select` (selected signal assignment)
- 10.6.4 Component instantiation

### 10.7 Ακολουθιακές Εντολές (Sequential Statements - εντός Process)
- 10.7.1 `if-then-elsif-else`
- 10.7.2 `case-when`
- 10.7.3 `for` loop, `while` loop
- 10.7.4 `wait` statement
- 10.7.5 Variable vs Signal ανάθεση (`:=` vs `<=`)

### 10.8 Σήματα vs Μεταβλητές
- 10.8.1 Signal: ενημερώνεται στο τέλος του delta cycle
- 10.8.2 Variable: ενημερώνεται άμεσα
- 10.8.3 Παγίδες: πολλαπλές αναθέσεις σε signal εντός process

***

## 11. VHDL - Προχωρημένο (Διάλεξη 11)

### 11.1 Μοντελοποίηση Συνδυαστικών Κυκλωμάτων
- 11.1.1 Πύλες, MUX, decoder με `when-else` / `with-select`
- 11.1.2 Full adder: behavioral, dataflow, structural
- 11.1.3 Sensitivity list: όλες οι είσοδοι για combinational
- 11.1.4 Ανεπιθύμητα latches (ελλιπής `if` χωρίς `else`)

### 11.2 Μοντελοποίηση Ακολουθιακών Κυκλωμάτων
- 11.2.1 D FF με ρολόι: `if rising_edge(clk)`
- 11.2.2 Σύγχρονο vs Ασύγχρονο reset/preset
- 11.2.3 Καταχωρητές και shift registers
- 11.2.4 Μετρητές (up, down, mod-N)
- 11.2.5 Sensitivity list: μόνο `clk` (και `rst` αν async)

### 11.3 FSM σε VHDL
- 11.3.1 Τύπος `type state_type is (S0, S1, S2,...)`
- 11.3.2 1-process, 2-process, 3-process στυλ
- 11.3.3 Moore vs Mealy υλοποίηση
- 11.3.4 One-hot encoding με `attribute`

### 11.4 Γενικοί Σχεδιασμοί (Generics)
- 11.4.1 `generic (N : integer := 8)` — παραμετρικά κυκλώματα
- 11.4.2 N-bit adder, N-bit register με generic
- 11.4.3 `generate` statement για δομικές επαναλήψεις

### 11.5 Πακέτα & Βιβλιοθήκες (Packages)
- 11.5.1 Ορισμός constants, types, functions σε package
- 11.5.2 `ieee.numeric_std`: unsigned/signed αριθμητική
- 11.5.3 Διαφορά `std_logic_arith` vs `numeric_std`

### 11.6 Subprograms
- 11.6.1 Functions: επιστρέφουν τιμή, χωρίς side effects
- 11.6.2 Procedures: πολλαπλές έξοδοι, `in`/`out`/`inout`
- 11.6.3 Overloading τελεστών

### 11.7 Testbenches
- 11.7.1 Entity χωρίς ports
- 11.7.2 Component instantiation του DUT
- 11.7.3 Παραγωγή ρολογιού: `clk <= not clk after 5 ns`
- 11.7.4 `assert` / `report` για αυτόματο έλεγχο
- 11.7.5 Simulation vs Synthesis: non-synthesizable constructs

### 11.8 RTL Σύνθεση
- 11.8.1 Synthesizable subset της VHDL
- 11.8.2 Αντιστοίχιση: `process(clk)` → FF, `process(a,b)` → combinational logic
- 11.8.3 Timing constraints: setup/hold time
- 11.8.4 Κρίσιμο μονοπάτι (critical path)

***

## 12. FPGA & Σύνθεση (Διάλεξη 12)

### 12.1 Αρχιτεκτονική FPGA
- 12.1.1 LUT (Look-Up Table): υλοποίηση συνδυαστικής λογικής
- 12.1.2 FF μέσα σε κάθε slice/CLB
- 12.1.3 Block RAM (BRAM)
- 12.1.4 DSP blocks
- 12.1.5 I/O blocks (IOB)
- 12.1.6 Interconnect (routing resources)

### 12.2 CPLD vs FPGA
- 12.2.1 CPLD: non-volatile, μικρότερη πυκνότητα
- 12.2.2 FPGA: SRAM-based, χάνει configuration χωρίς εξωτερική μνήμη
- 12.2.3 ASIC: πλήρης σχεδίαση, μαζική παραγωγή

### 12.3 Ροή Σχεδίασης
- 12.3.1 RTL Design (VHDL)
- 12.3.2 Simulation (functional)
- 12.3.3 Synthesis → netlist
- 12.3.4 Place & Route (PAR)
- 12.3.5 Timing Analysis (post-PAR simulation)
- 12.3.6 Bitstream generation & programming

### 12.4 Εργαλεία
- 12.4.1 Xilinx Vivado / ISE
- 12.4.2 Intel Quartus Prime
- 12.4.3 GHDL + GTKWave (open-source simulation)
- 12.4.4 ModelSim / QuestaSim

### 12.5 IP Cores
- 12.5.1 FIFO, PLL, memory controllers
- 12.5.2 Χρήση Xilinx/Intel IP catalog
- 12.5.3 Component instantiation από IP

***

## Αντιστοίχιση Simulators ↔ Ενότητες

| Simulator | Ενότητα |
|---|---|
| `1_Binary_Arithmetic_Visualizer.html` | §1: Συστήματα Αριθμών & Αριθμητική |
| `2_Function_to_Truth_table.html` | §2: Άλγεβρα Boole & Πίνακες Αλήθειας |
| `3_Sum_of_Minterms_Visualizer.html` | §3: Κανονική SOP |
| `4_Product_of_Maxterms_Visualizer.html` | §3: Κανονική POS |
| `5_Kmap_Visualizer.html` | §4: K-Map Απλοποίηση |
| `6_function_to_diagram.html` | §5: Συνδυαστικά / Διαγράμματα Κυκλωμάτων |
| `7_4bit_d_flipflop_register_simulator.html` | §8: D FF & Καταχωρητές |
| `8_interactive_state_table_converter.html` | §9: FSM & Πίνακες Καταστάσεων |
| `9_decoder_combinational_logic_simulator.html` | §6: Αποκωδικοποιητές & Πολυπλέκτες |
| `10_full_adder_mux_simulator.html` | §7: Αθροιστές & ALU |