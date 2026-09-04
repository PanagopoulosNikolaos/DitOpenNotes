# Assignment 02: Synchronous FSM Traffic Light Controller

## Objective
Design and implement a synchronous Moore Finite State Machine (FSM) controlling a four-way traffic intersection with vehicle sensors and pedestrian crossing requests.

---

## System Requirements

### 1. Intersection Layout and Signals
The intersection consists of Main Street (North-South, $NS$) and Side Street (East-West, $EW$). Each direction controls three lamp outputs:
* $NS_{\text{red}}, NS_{\text{yellow}}, NS_{\text{green}}$
* $EW_{\text{red}}, EW_{\text{yellow}}, EW_{\text{green}}$

### 2. Sensor Inputs
* $C$: Vehicle sensor on Side Street ($C = 1$ when vehicle is present).
* $P$: Pedestrian crosswalk button ($P = 1$ when pedestrian requests crossing).
* $T_{\text{long}}$: Timer signal asserted after 30 clock cycles.
* $T_{\text{short}}$: Timer signal asserted after 5 clock cycles (for yellow transition).

### 3. State Behavior (Moore Model)
1. **State $S_0$ ($NS$ Green, $EW$ Red)**: Default state. Remains in $S_0$ as long as $C=0$ and $P=0$, or until $T_{\text{long}}$ is reached.
2. **State $S_1$ ($NS$ Yellow, $EW$ Red)**: Caution interval for Main Street. Remains for $T_{\text{short}}$ duration.
3. **State $S_2$ ($NS$ Red, $EW$ Green)**: Side street active. Remains until side sensor $C=0$ or $T_{\text{long}}$ expires.
4. **State $S_3$ ($NS$ Red, $EW$ Yellow)**: Caution interval for Side Street. Remains for $T_{\text{short}}$ duration, then transitions back to $S_0$.

---

## Deliverables
1. Complete state diagram and state transition table.
2. State assignment using both binary encoding and one-hot encoding.
3. Derivation of excitation equations for D flip-flops using Karnaugh maps.
4. Synthesizable VHDL implementation in `traffic_controller.vhd`.
5. Self-checking testbench in `traffic_controller_tb.vhd` demonstrating correct state sequencing and fail-safe behavior (preventing simultaneous green lights under any condition).

