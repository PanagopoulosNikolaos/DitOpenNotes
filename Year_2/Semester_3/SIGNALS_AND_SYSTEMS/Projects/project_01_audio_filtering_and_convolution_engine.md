# Project 01: Discrete Audio Filtering and Convolution Reverb Engine

## Project Overview
Design and implement a signal processing pipeline in Python to analyze continuous-to-discrete sampled audio, simulate room acoustic impulse responses via direct time-domain convolution, and design digital FIR filters (low-pass and band-stop) to remove noise interference.

---

## Technical Specifications

### 1. Direct Time-Domain Convolution Engine
Implement an optimized time-domain convolution function:
$$
y[n] = \sum_{k=0}^{M-1} x[n - k] \cdot h[k]
$$
- Compare performance of naive nested-loop implementation against vectorized NumPy slicing and overlap-add FFT convolution.
- Verify exact numerical equivalence across implementations.

### 2. Acoustic Reverb Simulation
Simulate room impulse responses using an exponentially decaying comb filter model:
$$
h_{\text{reverb}}[n] = \delta[n] + \sum_{i=1}^{P} \alpha^i \delta[n - i \cdot D]
$$
where $\alpha \in (0, 1)$ is the acoustic absorption coefficient and $D$ is the echo delay in samples. Convolve dry audio samples with $h_{\text{reverb}}[n]$ to demonstrate acoustic coloration.

### 3. FIR Filter Design
- Design a low-pass filter using windowed-sinc methods with Hamming and Blackman windows to attenuate high-frequency sinusoidal noise injected into a clean audio signal.
- Generate time-domain waveform plots, impulse response spectra, and frequency response Magnitude/Phase plots using `scipy.signal.freqz`.

---

## Milestones and Deliverables

| Milestone | Target Objective | Deliverables |
|---|---|---|
| **Phase 1** | Audio I/O & Signal Ingestion | Python loader using `scipy.io.wavfile` or `soundfile`, time-domain plotting |
| **Phase 2** | Time-Domain Convolution Engine | Custom convolution function and runtime benchmark analysis |
| **Phase 3** | Reverb Modeling & Noise Generation | Synthetic impulse response generator and noisy audio dataset creation |
| **Phase 4** | Filter Synthesis & Documentation | FIR filter implementation, SNR evaluation before and after filtering, final report |

---

## Evaluation Rubric

| Assessment Criteria | Description | Weight |
|---|---|---|
| **Convolution Engine Correctness** | Accurate mathematical implementation and boundary condition handling | 30% |
| **Filter Design & DSP Theory** | Proper windowing, cutoff frequency selection, and frequency response analysis | 30% |
| **Acoustic Modeling Quality** | Valid impulse response model and audible reverberation rendering | 20% |
| **Code Structure & Visualization** | Clear plots (time-domain waveforms and frequency spectra), modular Python code | 20% |

