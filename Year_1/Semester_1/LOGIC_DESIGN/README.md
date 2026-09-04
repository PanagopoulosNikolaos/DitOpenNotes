# Logic Design

## Course Overview
This course provides a comprehensive introduction to the principles, analysis, and synthesis of digital systems and digital logic circuits. Students learn positional number systems, Boolean algebra, logic minimization techniques, MSI combinational building blocks, and basic sequential circuit components.

## Course Code
104 (LOGIC DESIGN)

## Prerequisites
None (Introductory hardware and digital logic fundamentals)

---

## Topics Covered
* **Digital Systems and Number Representations**: Analog vs. digital signals, positional number bases (binary, octal, decimal, hexadecimal), radix and diminished radix complements, signed magnitude, 1's and 2's complements, binary codes (BCD, Gray, excess-3, ASCII).
* **Boolean Algebra and Logic Gates**: Postulates and theorems of Huntington, duality principle, De Morgan's laws, standard logic gates (AND, OR, NOT, NAND, NOR, XOR, XNOR), universal gate implementations.
* **Gate-Level Minimization**: Canonical forms (Sum of Minterms, Product of Maxterms), standard forms, 2-, 3-, 4-variable Karnaugh maps (K-maps), prime implicants and essential prime implicants, don't-care conditions, two-level and multi-level optimization.
* **Combinational Logic Circuits**: Analysis and design procedures, binary half and full adders, carry ripple adders, carry-lookahead adders, binary subtractors, BCD adders, magnitude comparators.
* **MSI Combinational Building Blocks**: Decoders, encoders, priority encoders, multiplexers (MUX), demultiplexers (DEMUX), designing arbitrary combinational functions using decoders and multiplexers.
* **Sequential Logic Fundamentals**: Latches (SR, D), flip-flops (D, JK, T), clocking, state tables, state diagrams, and basic register architectures.

---

## Learning Objectives
* Perform conversions and arithmetic in binary, octal, hexadecimal, and complement representations.
* Simplify arbitrary Boolean expressions using algebraic identities and Karnaugh maps.
* Design, implement, and verify multi-input, multi-output combinational logic networks.
* Utilize MSI modular components (multiplexers, decoders, full adders) to implement complex functions.
* Analyze timing behavior, propagation delays, and gate hazards in digital circuits.
* Model and verify digital systems using Logisim-evolution and interactive visual simulators.

---

## Directory Structure

| Directory | Description |
|:---|:---|
| [`Lectures/`](Lectures/) | Structured theory lecture modules and official slide presentations |
| [`Exercises/`](Exercises/) | Practice drills, minimization problems, and comprehensive solutions |
| [`Examples/`](Examples/) | Interactive HTML simulators for binary arithmetic, K-maps, decoders, and adders |
| [`Assignments/`](Assignments/) | Laboratory coursework assignments with hardware implementation specifications |
| [`Tutorials/`](Tutorials/) | Hands-on guides for K-map minimization and schematic capture in Logisim |
| [`Projects/`](Projects/) | Capstone design project (4-Bit Arithmetic Logic Unit) |
| [`Exams/`](Exams/) | Archival examination papers, scanned tests, and model practice exams |
| [`Resources/`](Resources/) | Detailed chapter notes, curriculum mindmaps, and technical references |

---

## Interactive Visual Simulators

The [`Examples/Assistance/`](Examples/Assistance/) directory contains ten interactive, browser-based HTML visualizers and simulators covering binary arithmetic, truth table generation, minterm/maxterm synthesis, K-map reduction, D flip-flop registers, finite-state machine converters, decoders, and full-adder multiplexers.
