# 12. FPGA & Synthesis

This chapter completes the digital system design cycle, from VHDL description to actual FPGA implementation. Understanding FPGA architecture, the synthesis flow, and tools is essential for converting VHDL code into digital hardware.

---

## 1. FPGA Architecture

### 1.1 LUT (Look-Up Table)

The basic unit for implementing combinational logic. Each LUT stores a truth table:
- **4-input LUT:** $2^4 = 16$ entries
- **6-input LUT:** $2^6 = 64$ entries

> **[Key Insight]** Every combinational function can be implemented with one LUT, if the number of inputs is $\leq k$ (where $k$ is the number of inputs to the LUT).

### 1.2 Flip-Flops inside Slice/CLB

Each Configurable Logic Block (CLB) or slice contains:
- 1-2 LUTs
- Flip-flops (D-FF)
- MUX, carry logic, Wide Function Generator

### 1.3 Block RAM (BRAM)

Optional hardware memory:
- **Xilinx:** 18Kb or 36Kb blocks
- **Intel/Altera:** M9K, M20K blocks
- Can be connected into larger memories

### 1.4 DSP Blocks

Specialized multipliers/adders:
- 18x18 or 25x18 multiplication
- Suitable for DSP algorithms, FIR filters

### 1.5 I/O Blocks (IOB)

Interface between the FPGA and the external world:
- Support for multiple I/O speeds
- Differential I/O standards (LVDS)
- Pull-up/Pull-down resistors

### 1.6 Interconnect (Routing Resources)

Network connecting CLBs:
- Complex router
- Routing delay can exceed logic delay

---

## 2. CPLD vs FPGA vs ASIC

### 2.1 CPLD (Complex Programmable Logic Device)

- **Memory:** Non-volatile (EEPROM/Flash)
- **Density:** Smaller
- **Speed:** Less predictable delay
- **Suitable for:** Simple combinational circuits, glue logic

### 2.2 FPGA (Field-Programmable Gate Array)

- **Memory:** SRAM-based (loses configuration without external memory)
- **Density:** High (millions of logic elements)
- **Flexibility:** Very high
- **Suitable for:** Complex systems, prototypes, DSP

### 2.3 ASIC (Application-Specific IC)

- **Full design:** Custom layout
- **Mass production:** High development cost, low unit cost
- **Performance:** Better (speed, power)

| Characteristic | CPLD | FPGA | ASIC |
|:---|:---:|:---:|:---:|
| Reconfigurable | Yes | Yes | No |
| Non-volatile | Yes | No | N/A |
| Density | Low | High | Very high |
| Development cost | Low | Medium | Very high |
| Time-to-market | Fast | Fast | Slow |

---

## 3. Design Flow

### 3.1 RTL Design (VHDL)

Writing VHDL code that describes functionality at RTL level (Register Transfer Level).

### 3.2 Simulation (Functional)

Checking logical behavior without timing (no timing delays).

### 3.3 Synthesis → Netlist

Converting VHDL to netlist: list of gates and connections (gate-level).

**Synthesis stages:**
1. Parsing and code validation
2. Optimization (Boolean, K-Map, technology mapping)
3. Mapping to technology (LUTs, FFs, BRAMs)
4. Netlist generation

### 3.4 Place & Route (PAR)

- **Place:** Placing logic in specific CLBs/BRAMs/DSPs
- **Route:** Connecting units via interconnect

### 3.5 Timing Analysis (Post-PAR)

Checking that all timing constraints are met:
- **Setup constraint:** $t_{clk} > t_{combinational} + t_{setup}$
- **Hold constraint:** $t_{hold} < t_{clk} - t_{combinational}$

### 3.6 Bitstream Generation & Programming

The final binary image loaded into the FPGA:
- Xilinx: `.bit` (binary), `.rbt` (text)
- Intel: `.sof` (SRAM Object File), `.pof` (Programmer Object File)

---

## 4. Tools

### 4.1 Xilinx Vivado / ISE

- Vivado: newer, modern, Zynq/MicroBlaze support
- ISE: older, Spartan/older families

### 4.2 Intel Quartus Prime

- Lite Edition: free
- Pro Edition: professional

### 4.3 GHDL + GTKWave

- **GHDL:** Open-source VHDL simulator (analysis + elaboration)
- **GTKWave:** Open-source waveform viewer
- Suitable for development without commercial tools

### 4.4 ModelSim / QuestaSim

- Commercial simulator
- Supports VHDL/Verilog/SystemVerilog
- Coverage analysis, assertions

---

## 5. IP Cores

### 5.1 IP Core Types

- **FIFO:** First-In-First-Out buffer
- **PLL:** Phase-Locked Loop (clock generation)
- **Memory controllers:** DDR, BRAM controllers
- **UART/SPI/I2C:** Serial communication

### 5.2 Using IP Catalog

In Vivado: IP Catalog → add IP → configuration → instantiation.

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

### Exercise 1: LUT Calculation

**Problem:** How many 4-input LUTs are needed for a 4-bit XOR?

**Solution:**

A 4-bit XOR is a combinational function with 8 inputs ($A_3A_2A_1A_0 \oplus B_3B_2B_1B_0$). If we split into 4 separate 1-bit XORs, we need 4 LUTs (one for each $A_i \oplus B_i$).

### Exercise 2: FPGA Resource Estimation

**Problem:** A circuit has 100 gates, 50 FFs, 4 BRAMs. How many resources are needed?

**Solution:**

- 100 LUTs (each gate ~1 LUT) + 50 FFs + 4 BRAM blocks
- For Xilinx Artix-7: 20K LUTs, 35K FFs → sufficient space

### Exercise 3: Timing Constraint

**Problem:** A circuit has combinational delay 8ns and FF setup time 1ns. What is the maximum clock frequency?

**Solution:**
$$
f_{max} = \frac{1}{t_{comb} + t_{setup}} = \frac{1}{8 + 1} = 111.1 \text{ MHz}
$$

### Exercise 4: Synthesis Flow

**Problem:** Describe the flow from VHDL to bitstream.

**Solution:**
1. VHDL source → Synthesis (optimization, technology mapping)
2. Synthesis → Netlist (gate-level)
3. Netlist + Constraints → Place & Route
4. PAR → Timing analysis (verify setup/hold)
5. PAR → Bitstream generation
6. Bitstream → FPGA programming (via JTAG, USB)

### Exercise 5: CPLD vs FPGA Selection

**Problem:** A project needs 500 gates, non-volatile configuration. Selection?

**Solution:**

CPLD: non-volatile, sufficient for 500 gates. FPGA would not fit because it requires external memory for configuration.

### Exercise 6: GHDL Simulation

**Problem:** How is simulation performed with GHDL?

**Solution:**
```bash
ghdl -a my_design.vhd          -- Analysis
ghdl -e my_design              -- Elaboration
ghdl -r my_design --vcd=out.vcd -- Run + waveform
gtkwave out.vcd                -- View waveform
```

### Exercise 7: IP Core FIFO

**Problem:** When is a FIFO IP core used?

**Solution:**

- Clock domain crossing (between two different clocks)
- Data buffering (when the source is faster than the receiver)
- Async FIFO with grey code pointers for safety

### Exercise 8: Critical Path Improvement

**Problem:** The critical path is 15ns. How can it be reduced?

**Solution:**

1. **Pipelining:** Add FF registers midway
2. **Logic restructuring:** Boolean simplification
3. **Retiming:** Moving FFs for balance
4. **Faster technology:** Switching FPGA family
5. **Parallelism:** Replacing serial logic with parallel

---

## Exam Tip: Choosing Tools for the Exam

In an exam:
- If asked to describe the design flow: refer to the 6 stages (RTL → Sim → Synthesis → PAR → Timing → Bitstream)
- If asked to choose between FPGA/CPLD/ASIC: depends on complexity, cost, whether you want reconfiguration
- If asked to check timing: use $f_{max} = 1/(t_{comb} + t_{setup} + t_{clk-to-q})$
