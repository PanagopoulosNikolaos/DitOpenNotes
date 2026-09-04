# Tutorial 01: Analog Circuit Simulation with SPICE

## Context and Grounding
This tutorial provides a practical hands-on guide to computer-aided circuit simulation using SPICE (Simulation Program with Integrated Circuit Emphasis), specifically using NGSPICE and open-source command-line toolchains.

---

## 1. SPICE Netlist Architecture

A SPICE netlist is a plain text file describing circuit components, terminal node interconnections, and simulation control directives.

### 1.1 Fundamental Element Syntax
| Element | Syntax Pattern | Example |
|:---|:---|:---|
| Resistor | `R<name> <node_pos> <node_neg> <value>` | `R1 1 2 10k` |
| Capacitor | `C<name> <node_pos> <node_neg> <value>` | `C1 2 0 100u` |
| Inductor | `L<name> <node_pos> <node_neg> <value>` | `L1 1 2 10m` |
| Independent DC Voltage | `V<name> <node_pos> <node_neg> DC <val>` | `VCC 1 0 DC 15` |
| Sinusoidal AC Voltage | `V<name> <node_pos> <node_neg> SIN(<offset> <amplitude> <freq>)` | `VIN 1 0 SIN(0 5 50)` |
| Diode | `D<name> <anode> <cathode> <model>` | `D1 2 3 1N4148` |
| BJT Transistor | `Q<name> <collector> <base> <emitter> <model>` | `Q1 3 2 1 2N2222` |

* **Node 0** is always reserved as the universal circuit reference ground.
* First line of a SPICE file is always treated as the **title** (not an instruction).
* Netlist must terminate with the `.end` directive.

---

## 2. Core SPICE Simulation Directives

1. **Operating Point Analysis (`.op`)**:
   Computes steady-state DC voltages at all nodes and branch currents with capacitors opened and inductors shorted:
   ```spice
   .op
   ```
2. **DC Sweep Analysis (`.dc`)**:
   Sweeps a DC source across a specified voltage or current range:
   ```spice
   .dc VIN 0 10 0.1
   ```
3. **Transient Analysis (`.tran`)**:
   Computes time-domain response over interval $[0, t_{\text{stop}}]$ with timestep $t_{\text{step}}$:
   ```spice
   .tran 0.1ms 40ms
   ```
4. **AC Small-Signal Frequency Sweep (`.ac`)**:
   Calculates frequency response and Bode plots:
   ```spice
   .ac dec 10 10Hz 1MHz
   ```

---

## 3. Practical Example: Full-Wave Bridge Rectifier Netlist

Save the following text as `bridge_rectifier.cir`:

```spice
Full-Wave Bridge Rectifier with Capacitive Filter
* Secondary AC Transformer Input: 12V RMS = 16.97V peak at 50 Hz
VIN 1 2 SIN(0 16.97 50)

* Diode Bridge Configuration
D1 1 3 1N4007
D2 0 1 1N4007
D3 2 3 1N4007
D4 0 2 1N4007

* Smoothing Filter Capacitor and Load
C1 3 0 470u
RL 3 0 220

* Diode Model Definition
.model 1N4007 D(IS=7.027n RS=0.0341 N=1.8 BV=1000 IBV=0.05u CJO=44.4p)

* Simulation Command: 4 full AC cycles (80ms)
.tran 0.1ms 80ms

* Control block for interactive output
.control
run
plot V(3) V(1,2)
.endc
.end
```

### 3.1 Executing the Simulation
Invoke NGSPICE from your Linux terminal:
```bash
ngspice bridge_rectifier.cir
```
The resulting graphical window plots the AC differential input voltage $V(1,2)$ alongside the smoothed DC filtered output voltage $V(3)$.

