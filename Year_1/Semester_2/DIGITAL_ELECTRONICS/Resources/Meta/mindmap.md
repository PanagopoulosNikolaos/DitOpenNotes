# Digital Electronics with VHDL - Mind Map

***

## 1. Number Systems & Binary Arithmetic (Simulator: `1_Binary_Arithmetic_Visualizer.html`)

### 1.1 Number Systems
- 1.1.1 Binary (Base 2), Octal (Base 8), Hexadecimal (Base 16)
- 1.1.2 Conversions between bases
- 1.1.3 BCD (Binary Coded Decimal)
- 1.1.4 Gray Code

### 1.2 Representation of Negative Numbers
- 1.2.1 Sign-Magnitude
- 1.2.2 1's Complement
- 1.2.3 2's Complement
- 1.2.4 n-bit value range: \([-2^{n-1},\ 2^{n-1}-1]\)

### 1.3 Binary Arithmetic
- 1.3.1 Addition: carry propagation
- 1.3.2 Subtraction with 2's complement
- 1.3.3 Multiplication and Division (shifts)
- 1.3.4 Overflow detection

### 1.4 Character Encoding
- 1.4.1 ASCII
- 1.4.2 Unicode (basics)
- 1.4.3 Error detection codes (Parity, Hamming)

***

## 2. Boolean Algebra & Logic Gates (Simulator: `2_Function_to_Truth_table.html`)

### 2.1 Basic Principles
- 2.1.1 Boolean Axioms
- 2.1.2 Properties: commutative, associative, distributive
- 2.1.3 De Morgan's Theorems: \(\overline{A \cdot B} = \bar{A} + \bar{B}\)
- 2.1.4 Duality Principle

### 2.2 Logic Gates
- 2.2.1 AND, OR, NOT (basic)
- 2.2.2 NAND, NOR (universal gates)
- 2.2.3 XOR, XNOR
- 2.2.4 Implementing any function with NAND or NOR

### 2.3 Truth Tables
- 2.3.1 Construction for n variables (\(2^n\) rows)
- 2.3.2 Recognizing minterm / maxterm
- 2.3.3 Don't care conditions (X)

### 2.4 Implementation Technologies
- 2.4.1 TTL (Transistor-Transistor Logic)
- 2.4.2 CMOS
- 2.4.3 Characteristics: fan-in, fan-out, noise margin, propagation delay

***

## 3. Canonical Forms - SOP / POS (Simulators: `3_Sum_of_Minterms_Visualizer.html`, `4_Product_of_Maxterms_Visualizer.html`)

### 3.1 Canonical SOP (Sum of Minterms)
- 3.1.1 Minterm: product of all variables
- 3.1.2 Notation: \(F = \sum m(i,j,...)\)
- 3.1.3 Construction from truth table (rows = 1)

### 3.2 Canonical POS (Product of Maxterms)
- 3.2.1 Maxterm: sum of all variables
- 3.2.2 Notation: \(F = \prod M(i,j,...)\)
- 3.2.3 Construction from truth table (rows = 0)

### 3.3 SOP ↔ POS Relationship
- 3.3.1 Complementary indices
- 3.3.2 Conversion via De Morgan
- 3.3.3 Standard vs canonical form

***

## 4. Boolean Simplification (Simulator: `5_Kmap_Visualizer.html`)

### 4.1 Karnaugh Map (K-Map)
- 4.1.1 Layout for 2, 3, 4 variables (Gray code ordering)
- 4.1.2 Grouping: 1, 2, 4, 8 cells (powers of 2)
- 4.1.3 Prime Implicants (PI)
- 4.1.4 Essential Prime Implicants (Essential PI)
- 4.1.5 Handling don't care conditions
- 4.1.6 5-variable K-Map

### 4.2 Quine-McCluskey Method (QMC)
- 4.2.1 Algorithmic simplification (suitable for >4 variables)
- 4.2.2 Covering table
- 4.2.3 Finding minimum cover

### 4.3 2-Level Implementation
- 4.3.1 AND-OR (SOP)
- 4.3.2 OR-AND (POS)
- 4.3.3 NAND-NAND, NOR-NOR equivalents

***

## 5. Combinational Circuits (Simulator: `6_function_to_diagram.html`)

### 5.1 Design Principles
- 5.1.1 Output depends only on current inputs
- 5.1.2 Methodology: specification → table → minimization → implementation
- 5.1.3 Static Hazards

### 5.2 Code Converters
- 5.2.1 BCD → 7-segment display
- 5.2.2 Binary ↔ Gray code
- 5.2.3 BCD ↔ Excess-3

### 5.3 Magnitude Comparators
- 5.3.1 1-bit, n-bit comparator
- 5.3.2 Outputs: A>B, A=B, A<B

***

## 6. Decoders, Encoders & Multiplexers (Simulator: `9_decoder_combinational_logic_simulator.html`)

### 6.1 Decoders
- 6.1.1 n-to-2ⁿ decoder
- 6.1.2 Implementing logic functions with decoder + OR
- 6.1.3 Enable input, cascading

### 6.2 Encoders
- 6.2.1 2ⁿ-to-n encoder
- 6.2.2 Priority encoder
- 6.2.3 Applications: interrupt handling

### 6.3 Multiplexers (MUX)
- 6.3.1 2ⁿ-to-1 MUX
- 6.3.2 Implementing any function with MUX
- 6.3.3 Cascading MUX for n variables
- 6.3.4 Demultiplexer (DEMUX)

***

## 7. Adders & Arithmetic Units (Simulator: `10_full_adder_mux_simulator.html`)

### 7.1 Half Adder
- 7.1.1 Inputs: A, B → Outputs: Sum, Carry
- 7.1.2 Sum = A XOR B, Carry = A AND B

### 7.2 Full Adder
- 7.2.1 Inputs: A, B, Cin → Outputs: Sum, Cout
- 7.2.2 Implementation with 2 half adders
- 7.2.3 VHDL modeling (behavioral, structural, dataflow)

### 7.3 Ripple Carry Adder
- 7.3.1 n-bit adder: cascaded FA connection
- 7.3.2 Delay: \(T = n \cdot T_{FA}\)

### 7.4 Carry Lookahead Adder (CLA)
- 7.4.1 Generate: \(G_i = A_i \cdot B_i\)
- 7.4.2 Propagate: \(P_i = A_i + B_i\)
- 7.4.3 Speed vs complexity

### 7.5 Subtractor
- 7.5.1 With 2's complement and adder

### 7.6 ALU (Arithmetic Logic Unit)
- 7.6.1 Combining arithmetic + logical operations
- 7.6.2 Operation selection with MUX

***

## 8. Flip-Flops, Registers & Counters (Simulator: `7_4bit_d_flipflop_register_simulator.html`)

### 8.1 Latches
- 8.1.1 SR Latch (NAND/NOR)
- 8.1.2 D Latch (level-triggered)
- 8.1.3 Forbidden state

### 8.2 Flip-Flops (Edge-triggered)
- 8.2.1 SR FF
- 8.2.2 D FF: Q(t+1) = D
- 8.2.3 JK FF: Q(t+1) = J·Q' + K'·Q
- 8.2.4 T FF: Q(t+1) = T XOR Q
- 8.2.5 Master-Slave JK FF
- 8.2.6 Asynchronous vs Synchronous (preset, clear)

### 8.3 Flip-Flop Conversions
- 8.3.1 Excitation tables
- 8.3.2 D→JK, JK→D, T→D, etc.

### 8.4 Registers
- 8.4.1 4-bit D FF register (parallel load)
- 8.4.2 Shift registers: SISO, SIPO, PISO, PIPO
- 8.4.3 Universal Shift Register
- 8.4.4 Applications: buffer, serial communication

### 8.5 Counters
- 8.5.1 Asynchronous (Ripple) counter
- 8.5.2 Synchronous counter
- 8.5.3 Mod-N counter (arbitrary sequence)
- 8.5.4 Ring Counter, Johnson Counter
- 8.5.5 Up/Down Counter

***

## 9. Sequential Circuits & FSM (Simulator: `8_interactive_state_table_converter.html`)

### 9.1 Sequential Circuit Theory
- 9.1.1 Output depends on inputs + current state
- 9.1.2 Synchronous vs Asynchronous
- 9.1.3 Moore vs Mealy models

### 9.2 FSM Representation
- 9.2.1 State Diagram
- 9.2.2 State Table
- 9.2.3 State Encoding (binary, one-hot, gray)

### 9.3 FSM Design
- 9.3.1 Analysis: circuit → table → diagram
- 9.3.2 Synthesis: specification → minimization → implementation
- 9.3.3 State Reduction
  - 9.3.3.1 Equivalent pairs method
  - 9.3.3.2 Implication Table

### 9.4 Excitation & Output Tables
- 9.4.1 Excitation table by FF type
- 9.4.2 K-Map for next-state equations
- 9.4.3 K-Map for output equations

### 9.5 FSM Examples
- 9.5.1 Sequence detector
- 9.5.2 Traffic controller
- 9.5.3 Synchronous mod-N counter

***

## 10. VHDL - Basics (Lecture 10)

### 10.1 Introduction to VHDL
- 10.1.1 Hardware Description Language (HDL): describing hardware, not programming
- 10.1.2 IEEE Std 1076 (1987, 1993, 2008)
- 10.1.3 Design flow: RTL → synthesis → place & route → bitstream

### 10.2 VHDL File Structure
- 10.2.1 Library / Use clauses: `LIBRARY ieee; USE ieee.std_logic_1164.ALL;`
- 10.2.2 Entity: interface definition (ports)
- 10.2.3 Architecture: behavior/structure description
- 10.2.4 Configuration (basics)

### 10.3 Data Types
- 10.3.1 `std_logic`: '0','1','Z','X','U','W','L','H','-'
- 10.3.2 `std_logic_vector(n downto 0)`
- 10.3.3 `integer`, `natural`, `positive`
- 10.3.4 `boolean`, `bit`, `bit_vector`
- 10.3.5 `signed`, `unsigned` (ieee.numeric_std)

### 10.4 Operators
- 10.4.1 Logical: `and`, `or`, `not`, `nand`, `nor`, `xor`, `xnor`
- 10.4.2 Arithmetic: `+`, `-`, `*`, `/`
- 10.4.3 Comparison: `=`, `/=`, `<`, `>`, `<=`, `>=`
- 10.4.4 Shift: `sll`, `srl`, `sla`, `sra`, `rol`, `ror`
- 10.4.5 Concatenation: `&`

### 10.5 Architecture Styles
- 10.5.1 **Behavioral**: `process`, `if-else`, `case`
- 10.5.2 **Dataflow**: concurrent assignment statements
- 10.5.3 **Structural**: component instantiation, port map

### 10.6 Concurrent Statements
- 10.6.1 Signal assignment: `Y <= A and B;`
- 10.6.2 `when-else` (conditional signal assignment)
- 10.6.3 `with-select` (selected signal assignment)
- 10.6.4 Component instantiation

### 10.7 Sequential Statements (Inside Process)
- 10.7.1 `if-then-elsif-else`
- 10.7.2 `case-when`
- 10.7.3 `for` loop, `while` loop
- 10.7.4 `wait` statement
- 10.7.5 Variable vs Signal assignment (`:=` vs `<=`)

### 10.8 Signals vs Variables
- 10.8.1 Signal: updated at the end of delta cycle
- 10.8.2 Variable: updated immediately
- 10.8.3 Pitfalls: multiple assignments to signal inside process

***

## 11. VHDL - Advanced (Lecture 11)

### 11.1 Combinational Circuit Modeling
- 11.1.1 Gates, MUX, decoder with `when-else` / `with-select`
- 11.1.2 Full adder: behavioral, dataflow, structural
- 11.1.3 Sensitivity list: all inputs for combinational
- 11.1.4 Unwanted latches (incomplete `if` without `else`)

### 11.2 Sequential Circuit Modeling
- 11.2.1 D FF with clock: `if rising_edge(clk)`
- 11.2.2 Synchronous vs Asynchronous reset/preset
- 11.2.3 Registers and shift registers
- 11.2.4 Counters (up, down, mod-N)
- 11.2.5 Sensitivity list: only `clk` (and `rst` if async)

### 11.3 FSM in VHDL
- 11.3.1 Type `type state_type is (S0, S1, S2,...)`
- 11.3.2 1-process, 2-process, 3-process styles
- 11.3.3 Moore vs Mealy implementation
- 11.3.4 One-hot encoding with `attribute`

### 11.4 Generics
- 11.4.1 `generic (N : integer := 8)` — parametric circuits
- 11.4.2 N-bit adder, N-bit register with generic
- 11.4.3 `generate` statement for structural repetition

### 11.5 Packages & Libraries
- 11.5.1 Defining constants, types, functions in package
- 11.5.2 `ieee.numeric_std`: unsigned/signed arithmetic
- 11.5.3 Difference `std_logic_arith` vs `numeric_std`

### 11.6 Subprograms
- 11.6.1 Functions: return value, no side effects
- 11.6.2 Procedures: multiple outputs, `in`/`out`/`inout`
- 11.6.3 Operator overloading

### 11.7 Testbenches
- 11.7.1 Entity without ports
- 11.7.2 Component instantiation of DUT
- 11.7.3 Clock generation: `clk <= not clk after 5 ns`
- 11.7.4 `assert` / `report` for automatic checking
- 11.7.5 Simulation vs Synthesis: non-synthesizable constructs

### 11.8 RTL Synthesis
- 11.8.1 Synthesizable subset of VHDL
- 11.8.2 Mapping: `process(clk)` → FF, `process(a,b)` → combinational logic
- 11.8.3 Timing constraints: setup/hold time
- 11.8.4 Critical path

***

## 12. FPGA & Synthesis (Lecture 12)

### 12.1 FPGA Architecture
- 12.1.1 LUT (Look-Up Table): implementing combinational logic
- 12.1.2 FF inside each slice/CLB
- 12.1.3 Block RAM (BRAM)
- 12.1.4 DSP blocks
- 12.1.5 I/O blocks (IOB)
- 12.1.6 Interconnect (routing resources)

### 12.2 CPLD vs FPGA
- 12.2.1 CPLD: non-volatile, smaller density
- 12.2.2 FPGA: SRAM-based, loses configuration without external memory
- 12.2.3 ASIC: full design, mass production

### 12.3 Design Flow
- 12.3.1 RTL Design (VHDL)
- 12.3.2 Simulation (functional)
- 12.3.3 Synthesis → netlist
- 12.3.4 Place & Route (PAR)
- 12.3.5 Timing Analysis (post-PAR simulation)
- 12.3.6 Bitstream generation & programming

### 12.4 Tools
- 12.4.1 Xilinx Vivado / ISE
- 12.4.2 Intel Quartus Prime
- 12.4.3 GHDL + GTKWave (open-source simulation)
- 12.4.4 ModelSim / QuestaSim

### 12.5 IP Cores
- 12.5.1 FIFO, PLL, memory controllers
- 12.5.2 Using Xilinx/Intel IP catalog
- 12.5.3 Component instantiation from IP

***

## Simulators ↔ Units Mapping

| Simulator | Unit |
|---|---|
| `1_Binary_Arithmetic_Visualizer.html` | §1: Number Systems & Arithmetic |
| `2_Function_to_Truth_table.html` | §2: Boolean Algebra & Truth Tables |
| `3_Sum_of_Minterms_Visualizer.html` | §3: Canonical SOP |
| `4_Product_of_Maxterms_Visualizer.html` | §3: Canonical POS |
| `5_Kmap_Visualizer.html` | §4: K-Map Simplification |
| `6_function_to_diagram.html` | §5: Combinational / Circuit Diagrams |
| `7_4bit_d_flipflop_register_simulator.html` | §8: D FF & Registers |
| `8_interactive_state_table_converter.html` | §9: FSM & State Tables |
| `9_decoder_combinational_logic_simulator.html` | §6: Decoders & Multiplexers |
| `10_full_adder_mux_simulator.html` | §7: Adders & ALU |
