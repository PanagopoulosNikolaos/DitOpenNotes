# Project 01: Multi-Function Digital Stopwatch and Precision Timer

## Project Overview
Design, model, synthesize, and verify a multi-function digital stopwatch and countdown timer in VHDL. The system targets an FPGA board (such as Xilinx Artix-7 or Intel Cyclone IV), featuring debounced user pushbuttons, clock division to $100\text{ Hz}$ ($0.01\text{ s}$ resolution), dual-mode BCD counters, and multiplexed 7-segment display driver logic.

---

## 1. System Architecture and Block Diagram

The project is structured into modular RTL components:

```text
               +-------------------------------------------+
               |             Top-Level System              |
               |                                           |
CLK (50 MHz) ->| [Clock Divider] ---> 100 Hz Tick          |
               |                           |               |
Btn_Start   -->| [Debounce & Sync]         v               |
Btn_Stop    -->| [FSM Controller] <-> [BCD Counter Array]  |
Btn_Reset   -->| (STOP, RUN, LAP)      (SS.ss display)     |
               |                           |               |
               |                           v               |
               |                  [7-Segment Multiplexer]  |
               |                   |                    |  |
               +-------------------|--------------------|--+
                                   v                    v
                               Seg[6..0]             An[3..0]
```

### 1.1 Hardware Specifications
* **System Master Clock**: $50\text{ MHz}$ oscillator input.
* **Resolution**: $0.01\text{ s}$ ($10\text{ ms}$ tick rate, requiring division by $500,000$).
* **Maximum Time Range**: $99.99\text{ seconds}$ across four 7-segment displays (`Digit 3: Ten Seconds`, `Digit 2: Seconds + Decimal Point`, `Digit 1: Tenths`, `Digit 0: Hundredths`).
* **Input Buttons**: `Start/Pause`, `Lap/Recall`, `Master_Reset` (Active-low debounced).

---

## 2. Component Design Requirements

### 2.1 Clock Frequency Divider (`clk_divider.vhd`)
Synthesize a synchronous modulo-$500,000$ counter that asserts an active-high single-cycle enable pulse `tick_100hz` every $10\text{ ms}$.

### 2.2 Switch Debouncer and Edge Detector (`debouncer.vhd`)
Eliminate mechanical switch bounce (typically $5\text{ ms} - 20\text{ ms}$) using a shift register sampler running at a $1\text{ kHz}$ sampling clock. Output clean, single-cycle rising-edge pulses for button events.

### 2.3 Cascaded BCD Decade Counter (`bcd_counter_array.vhd`)
Cascade four 4-bit synchronous BCD decade counters ($0 \dots 9$). Counter $i$ increments when `tick_100hz` is asserted and all preceding stages evaluate to $9$.

### 2.4 FSM Controller (`stopwatch_fsm.vhd`)
Implement a Moore FSM with states:
* `STATE_RESET`: Clears display and registers to zero.
* `STATE_RUNNING`: Enables counting on $100\text{ Hz}$ ticks.
* `STATE_PAUSED`: Holds current count values.
* `STATE_LAP`: Continues internal timing while freezing output display registers for viewing.

### 2.5 Time-Multiplexed 7-Segment Display Controller (`seven_seg_mux.vhd`)
Refresh the four display digits sequentially at $1\text{ kHz}$ to prevent optical flicker. Decode 4-bit BCD digits into active-low cathode signals (`CA` through `CG`) and sequence active-low anode drivers (`AN0` through `AN3`).

---

## 3. Verification and Deliverables

1. Synthesizable VHDL source files in `src/`:
   * `clk_divider.vhd`, `debouncer.vhd`, `bcd_counter.vhd`, `stopwatch_fsm.vhd`, `seven_seg_mux.vhd`, and `stopwatch_top.vhd`.
2. Hierarchical testbench in `tb/stopwatch_top_tb.vhd`:
   * Simulates full cycle: start timing, pause at $1.25\text{ s}$, resume, capture lap time, and reset.
3. Timing constraints file (`constraints.xdc` or `.qsf`) specifying pin assignments and $50\text{ MHz}$ clock constraints.
4. Comprehensive engineering report with state transition diagrams, RTL schematic captures, and simulation waveforms.

---

## 4. Evaluation Rubric
| Criterion | Description | Points |
|---|---|---|
| Architecture & Hierarchy | Modular decomposition and clean signal routing | 20 |
| FSM Logic & Modes | Flawless state transitions between Run, Pause, Lap, and Reset | 25 |
| Timing & Debounce Circuits | Robust glitch-free button filtering and precise clock division | 20 |
| Display Multiplexing | Proper BCD decoding and flicker-free anode sequencing | 15 |
| Testbench & Waveform Verification | Exhaustive automated test coverage and corner case testing | 20 |
| **Total** | | **100** |

