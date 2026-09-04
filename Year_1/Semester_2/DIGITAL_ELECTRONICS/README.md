# Digital Electronics

## Course Overview
This course provides a comprehensive foundation in digital electronics, switching theory, combinational and sequential logic design, finite state machine (FSM) synthesis, semiconductor memory devices, and hardware description language (VHDL) simulation for FPGA implementation.

## Course Code
205 (DIGITAL ELECTRONICS)

## Prerequisites
* Logic Design (Code: 104)
* Electronics (Code: 105)

---

## Topics Covered
* **Number Systems and Binary Arithmetic**: Two's complement representations, fixed/floating point formats, BCD codes, and arithmetic overflow detection.
* **Boolean Minimization & Hazard Analysis**: Multivariable Karnaugh maps, Quine-McCluskey tabular reduction, static and dynamic hazard elimination via consensus terms.
* **Combinational Building Blocks**: Ripple-carry adders, carry-lookahead adders (CLA), subtractors, magnitude comparators, decoders, priority encoders, multiplexers, and demultiplexers.
* **Synchronous Sequential Circuits**: Latches, edge-triggered flip-flops (SR, JK, D, T), master-slave configurations, setup and hold time margins, and clock skew.
* **Registers and Counters**: Parallel-in serial-out (PISO), universal shift registers, ripple counters, synchronous modulo-N up/down counters, and ring/Johnson counters.
* **Finite State Machines (FSMs)**: Mealy and Moore architectural models, state diagrams, implication tables for state reduction, state assignment, and excitation equation derivation.
* **Hardware Description Language (VHDL)**: Entity-architecture declarations, concurrent signal assignments, sequential processes, component instantiation, and testbench verification.

---

## Learning Objectives
* Analyze, synthesize, and optimize multi-level combinational switching networks free of timing hazards.
* Design synchronous sequential circuits and finite state machines from formal behavioral specifications.
* Calculate critical path propagation delays, setup/hold constraints, and maximum operating clock frequencies ($f_{\max}$).
* Model and verify digital hardware components in standard IEEE 1076 VHDL using simulation and waveform inspection tools.

---

## Directory Structure

| Directory | Description |
|:---|:---|
| [`Lectures/`](Lectures/) | Structured theory lecture modules and curriculum guides |
| [`Exercises/`](Exercises/) | Solved exercises on Boolean algebra, combinational logic, and sequential FSM synthesis |
| [`Examples/`](Examples/) | VHDL implementations, interactive browser visualizers, and Streamlit simulation suite |
| [`Assignments/`](Assignments/) | Laboratory design coursework with formal evaluation rubrics (ALU, Traffic Controller) |
| [`Tutorials/`](Tutorials/) | Hands-on walkthroughs for K-map minimization and GHDL/GTKWave simulation |
| [`Projects/`](Projects/) | Capstone term design project (Digital Stopwatch and Timer System) |
| [`Exams/`](Exams/) | Comprehensive model practice examination with complete worked solutions and grading rubric |
| [`Resources/`](Resources/) | Twelve granular chapter study notes, curriculum mindmaps, and textbook references |

---

## Interactive Visual Simulators and Tooling

### Browser-Based Visualizers
The [`Examples/Assistance/`](Examples/Assistance/) directory provides ten interactive browser visualizers for hands-on experimentation:
1. Binary Arithmetic Visualizer
2. Function to Truth Table Converter
3. Sum of Minterms Visualizer
4. Product of Maxterms Visualizer
5. Karnaugh Map Visualizer
6. Function to Gate Diagram Generator
7. 4-Bit D Flip-Flop Register Simulator
8. State Table to State Diagram Converter
9. Decoder Combinational Logic Simulator
10. Full Adder and Multiplexer Simulator

### VHDL Code Execution and Waveform Suite
The [`Examples/VHDL_CODE_EXEC/`](Examples/VHDL_CODE_EXEC/) directory provides a Streamlit-based web application for automated VHDL compilation, stimulus application, and interactive Plotly waveform generation.

To launch the suite:
```bash
cd Examples/VHDL_CODE_EXEC
./run_app.sh
```

---

## VHDL Simulation with GHDL and GTKWave

```bash
# Analyze VHDL design entity
ghdl -a Examples/01_combinational_adder_subtractor.vhd

# Elaborate top-level entity
ghdl -e adder_subtractor_4bit

# Run simulation and output waveform data
ghdl -r adder_subtractor_4bit --vcd=waveform.vcd

# View waveform in GTKWave
gtkwave waveform.vcd
```
