# VHDL Code Execution and Waveform Generation Suite

## Overview
This interactive environment provides automated compilation, testbench generation, simulation, and timing waveform visualization for digital circuits modeled in VHDL.

---

## Key Features

1. **VHDL Simulation Engine**:
   * Simulates standard digital circuits including SR Latches, D Flip-Flops, and JK Flip-Flops.
   * Generates input stimulus vectors and parses simulation outputs into digital waveform traces.
2. **Interactive Streamlit Interface**:
   * Dynamic code editor with syntax verification.
   * Real-time waveform rendering powered by Plotly.
   * Circuit schematic generation from entity pinouts.
3. **Database and History Management**:
   * Persists user simulations, test vectors, and generated waveforms into local storage (`db.json`).

---

## Execution Instructions

Ensure Streamlit and required dependencies are installed:
```bash
pip install -r requirements.txt
```

Launch the application:
```bash
./run_app.sh
# or directly via:
streamlit run app.py
```