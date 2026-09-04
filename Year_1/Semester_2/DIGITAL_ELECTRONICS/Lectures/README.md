# Digital Electronics: Lectures and Course Modules

This directory organizes the theoretical lecture notes, structured curriculum guides, and architectural breakdowns for **Digital Electronics (Course Code: 205)**.

---

## Core Lecture Syllabus

The course curriculum covers the principles of binary logic, combinational minimization, medium-scale integration (MSI) modules, synchronous sequential synthesis, finite state machines, and hardware description language (VHDL) simulation.

| Module | Document | Primary Focus |
|:---|:---|:---|
| **Lecture 01** | [`lecture_01_boolean_algebra_and_logic_gates.md`](lecture_01_boolean_algebra_and_logic_gates.md) | Axiomatic Boolean algebra, de Morgan's laws, universal logic gates, and canonical SOP/POS |
| **Lecture 02** | [`lecture_02_combinational_circuit_design.md`](lecture_02_combinational_circuit_design.md) | Karnaugh maps, multi-output minimization, decoders, multiplexers, and arithmetic adders/subtractors |
| **Lecture 03** | [`lecture_03_sequential_circuits_and_fsm.md`](lecture_03_sequential_circuits_and_fsm.md) | Latches, edge-triggered flip-flops (SR, JK, D, T), registers, synchronous counters, and Mealy/Moore FSMs |

---

## In-Depth Chapter Study Notes

For comprehensive chapter-by-chapter derivations, circuit schematics, and VHDL code walkthroughs, consult the granular study notes in the [`Resources/Notes/`](../Resources/Notes/) directory:

* [`01_number_systems_binary_arithmetic.md`](../Resources/Notes/01_number_systems_binary_arithmetic.md) — Two's complement, fixed/floating point, and arithmetic overflow
* [`02_boolean_algebra_logic_gates.md`](../Resources/Notes/02_boolean_algebra_logic_gates.md) — Switching algebra postulates, gate schematics, and electrical characteristics
* [`03_canonical_forms_sop_pos.md`](../Resources/Notes/03_canonical_forms_sop_pos.md) — Minterm and maxterm expansions, standard algebraic forms
* [`04_boolean_simplification.md`](../Resources/Notes/04_boolean_simplification.md) — 4- and 5-variable K-maps, Quine-McCluskey tabulation, hazard elimination
* [`05_combinational_circuits.md`](../Resources/Notes/05_combinational_circuits.md) — Half/full adders, ripple carry, carry-lookahead, and comparators
* [`06_decoders_encoders_multiplexers.md`](../Resources/Notes/06_decoders_encoders_multiplexers.md) — Priority encoders, 3-to-8 decoders, multiplexer tree expansions
* [`07_asynchronous_arithmetic_units.md`](../Resources/Notes/07_asynchronous_arithmetic_units.md) — ALU design, status flags, and bit-slice architectures
* [`08_flipflops_registers_counters.md`](../Resources/Notes/08_flipflops_registers_counters.md) — Master-slave timing, setup and hold margins, shift registers
* [`09_sequential_circuits_fsm.md`](../Resources/Notes/09_sequential_circuits_fsm.md) — State diagrams, excitation tables, state reduction, and Moore/Mealy models
* [`10_vhdl_basics.md`](../Resources/Notes/10_vhdl_basics.md) — Entity declarations, concurrent statements, and structural architectures
* [`11_vhdl_advanced.md`](../Resources/Notes/11_vhdl_advanced.md) — Sequential processes, generics, component instantiation, and testbenches
* [`12_fpga_synthesis.md`](../Resources/Notes/12_fpga_synthesis.md) — Lookup tables (LUTs), configurable logic blocks (CLBs), and timing closure

---

## Recommended Study Path

1. Review the foundational concepts in **Lecture 01** and **Notes 01–03**.
2. Solve the combinational logic drills in [`Exercises/exercises_boolean_algebra_and_combinational_logic.md`](../Exercises/exercises_boolean_algebra_and_combinational_logic.md).
3. Test circuit configurations using the interactive browser visualizers in [`Examples/Assistance/`](../Examples/Assistance/).
4. Progress to sequential logic and FSM design in **Lecture 03** and **Notes 08–09**, followed by hands-on VHDL simulation in [`Tutorials/tutorial_02_vhdl_simulation_with_ghdl_and_gtkwave.md`](../Tutorials/tutorial_02_vhdl_simulation_with_ghdl_and_gtkwave.md).