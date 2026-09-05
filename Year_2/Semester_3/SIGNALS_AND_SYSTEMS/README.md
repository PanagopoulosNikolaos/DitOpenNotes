# Signals and Systems

## Course Overview
This course provides a comprehensive mathematical and computational treatment of continuous-time and discrete-time signals and systems. Topics include signal classifications, linearity, time-invariance, causality, BIBO stability, continuous-time and discrete-time convolution, impulse responses, differential/difference equations, Fourier series representations, Continuous-Time Fourier Transform (CTFT), Laplace transforms, and system transfer functions.

## Course Code
303 (SIGNALS AND SYSTEMS)

## Prerequisites
* Mathematical Analysis (Code: 101)
* Electromagnetics (Code: 201) / Electronics (Code: 105)

---

## Topics Covered
* **Signal Classification and Elementary Functions**: Continuous vs. discrete time, analog vs. digital, deterministic vs. random, even and odd signal decomposition, signal energy and power, unit impulse $\delta(t)$, unit step $u(t)$, and complex exponentials.
* **System Characteristics and Properties**: Mathematical operator representations, memory (static vs. dynamic), invertibility, causality, linearity (superposition and homogeneity), time-invariance, and Bounded-Input Bounded-Output (BIBO) stability.
* **Linear Time-Invariant (LTI) Systems**: Representation of continuous signals by impulses, the convolution integral $y(t) = x(t) * h(t)$, commutativity, distributivity, associativity, cascade/parallel system interconnections, and step responses.
* **Frequency Domain Representations**: Continuous-Time Fourier Series (CTFS), Dirichlet conditions, spectral plots, Continuous-Time Fourier Transform (CTFT), transform properties, duality, convolution property, and frequency response $H(j\omega)$.
* **The Laplace Transform**: Bilateral and unilateral Laplace transforms, Region of Convergence (ROC) properties, poles and zeros, system stability, solving linear constant-coefficient differential equations, and s-domain transfer functions.

---

## Learning Objectives
* Analyze and decompose complex signals into elementary signals, even/odd components, and harmonic series.
* Formulate rigorous mathematical proofs for system properties (linearity, time-invariance, causality, BIBO stability).
* Evaluate analytical piecewise convolution integrals and discrete convolution sums.
* Compute frequency responses and transform systems into the s-domain to analyze transient and steady-state responses.

---

## Directory Structure

| Directory | Description |
|:---|:---|
| [`Lectures/`](Lectures/) | Structured theory lecture modules and official lecture presentation slides |
| [`Exercises/`](Exercises/) | Solved mathematical problem sets on signal operations, system properties, and convolution |
| [`Examples/`](Examples/) | Interactive HTML5 visualizers for signal operations and LTI system properties |
| [`Assignments/`](Assignments/) | Graded coursework problem sets on system classification and analytical convolution integrals |
| [`Tutorials/`](Tutorials/) | Hands-on walkthroughs for graphical convolution and Python SciPy signal processing |
| [`Projects/`](Projects/) | Capstone design project: Discrete Audio Filtering and Convolution Reverb Engine |
| [`Exams/`](Exams/) | 100-point model practice examination with complete worked solutions and grading rubrics |
| [`Resources/`](Resources/) | Deep-dive study notes across lectures, conceptual mindmap, and curated DSP textbooks |

---

## Interactive Visualizers and Python Tooling

### Browser-Based Interactive Simulators
The [`Examples/`](Examples/) directory contains five interactive web applications for visual exploration of signal principles:
1. `01_InteractiveLearning.html`: Fundamental signal concepts and waveforms.
2. `02_InteractiveLearning.html`: Continuous-time signal transformations (time scaling, shifting, reflection).
3. `03_InteractiveLearning.html`: Continuous-time elementary signal synthesis and energy/power computation.
4. `04_InteractiveLearning.html`: Interactive system property verification (Linearity, Causality, Time-Invariance).
5. `05_InteractiveLearning.html`: LTI system convolution and impulse response animator.

To view any simulator, open the file in a modern web browser:
```bash
xdg-open Examples/01_InteractiveLearning.html
```
