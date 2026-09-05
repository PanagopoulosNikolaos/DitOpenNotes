# Signals and Systems - Lectures 01-06 Mindmap

## Section 1: Lecture 01 - Introduction and Course Organization
- a. Course Overview and Scope
- b. Core Definitions and Examples of Signals
- c. Applications and Fields of Engineering
- d. Mathematical Properties of Signals
- e. Continuous-Time (CT) vs. Discrete-Time (DT) Representation
- f. Course Objectives and Key Concepts
- g. Syllabus and Weekly Timeline
- h. Grading Policy, Exams, and Textbook References

## Section 2: Lecture 02 - Basic Signal Concepts
- a. Formal Definition of Signals and Systems
- b. Signal Dimensionality (1D, 2D, 3D, Multidimensional)
- c. Casing and Mathematical Representation of Sinusoidal Signals
- d. Signal Classification and Categories
  - i. Continuous-Time vs. Discrete-Time (x(t) vs. x[n])
  - ii. Analog vs. Digital (Continuous vs. Discrete Amplitude)
  - iii. Analog-to-Digital Conversion Process (Sampling, Quantization, Coding)
- e. Signal Energy and Power Calculations
  - i. Calculations over Finite Time Intervals
  - ii. Calculations over Infinite Time Horizons
  - iii. Energy Signals vs. Power Signals
- f. Transformations of Independent and Dependent Variables
  - i. Time-Domain Transformations (Time Shifting, Time Reversal, Time Scaling)
  - ii. Combined Time Transformations (x(at+b))
  - iii. Amplitude transformations (Amplitude Shifting, Amplitude Scaling)
  - iv. Signal Arithmetic (Addition and Multiplication)
- g. Characteristic Parameters of Continuous-Time Signals (Mean Value, RMS Value, Instantaneous Power)
- h. Signal Properties
  - i. Deterministic vs. Stochastic (Random) Signals
  - ii. Causal vs. Non-causal Signals
  - iii. Bounded Amplitude (Bounded Signals)
  - iv. Finite vs. Infinite Duration
  - v. Even and Odd Signals (Symmetry, Decompositions, and Multiplication Properties)
  - vi. Periodic Signals (Period, Frequency, and Angular Frequency)

## Section 3: Lecture 03 - Continuous-Time Signals (Basic & Elementary Signals)
- a. Recap of Classifications, Transformations, and Symmetries
- b. Conditions for Periodicity of the Sum of Periodic Signals
- c. Unit Step Function (Heaviside Function)
  - i. Definition and Discontinuity at t=0
  - ii. Alternative Limit Definition
  - iii. Amplitude Scaling and Shifting Properties
- d. Signum Function (sgn(t))
- e. Unit Impulse Function (Dirac Delta Function)
  - i. Definition and Area Property
  - ii. Graphical Representation
  - iii. Amplitude Scaling and Time Shifting
  - iv. Approximation Limits of Impulses
- f. Mathematical Relations between Step and Impulse Functions
- g. Fundamental Properties of the Dirac Delta Function
  - i. Sifting Property
  - ii. Time Scaling Property
- h. Unit Ramp Function (r(t)) and its Derivative Relationships
- i. Exponential Signals
  - i. Real Exponentials (Decaying vs. Growing) and Time Constants
  - ii. Euler's Formulas and Complex Exponentials Relationship
  - iii. Complex Exponential Signals (Euler Identity, Sines/Cosines Representation)
- j. Sinusoidal Signals and Phase Relationships
- k. Damped Sinusoids
- l. Rectangular Pulse Function and Unit Step Generation
- m. Periodic Rectangular Pulses (Pulse Trains)
- n. Triangular Pulse Function
- o. Sampling Function (Sinc Function) and Integral Properties
- p. Impulse Train (Comb Function)

## Section 4: Lecture 04 - Continuous-Time Systems
- a. Representing Arbitrary Signals as Integrals of Shifted Impulses
- b. Definition and Block Diagram representation of Systems
- c. System Classification by Input-Output Count (SISO, MISO, SIMO, MIMO)
- d. System Classification by Signal Nature (Continuous-Time vs. Discrete-Time, Deterministic vs. Stochastic)
- e. System State and State of Rest
- f. Linear Systems
  - i. Homogeneity (Scaling) Property
  - ii. Additivity Property
  - iii. Superposition Principle
  - iv. Methods for Linearity Testing and Counter-examples
- g. Time-Invariant Systems
  - i. Definition of Time-Invariance
  - ii. Methods for Time-Invariance Testing and Counter-examples

## Section 5: Lecture 05 - Linear Time-Invariant (LTI) Systems
- a. Recap of System Linearity and Time-Invariance
- b. Static (Memoryless) vs. Dynamic Systems
  - i. Memoryless Systems (Resistor Example)
  - ii. Systems with Memory (Capacitor Integrator Example)
  - iii. Memory Length (Finite vs. Infinite Memory)
- c. Causal vs. Non-causal Systems
  - i. Definition of Causality in Time
  - ii. Causal Physical Real-Time Systems vs. Non-real-time recorded processing
- d. System Stability (Bounded-Input Bounded-Output Stability - BIBO)
  - i. Definition of BIBO Stability
  - ii. Physical Analogy of Stability (Marble in a Bowl vs. on a Dome)
  - iii. Stability Proofs and Testing Methods
- e. Importance of Linear Time-Invariant (LTI) Systems
- f. Impulse Response
  - i. Definition for LTI Systems (h(t) = S[delta(t)])
  - ii. Definition for Linear Time-Varying Systems (h(t, tau))
- g. The Convolution Integral
  - i. Derivation and Formulation
  - ii. Output Representation for Causal LTI Systems
  - iii. Output Representation for Causal Inputs

## Section 6: Lecture 06 - Convolution
- a. Summary of Impulse Response and Convolution Integral Definition
- b. Steps for Analytical and Graphical Convolution Computation
  - i. Time Reversal (Reflection)
  - ii. Time Shifting (Sliding)
  - iii. Multiplication (Overlap Product)
  - iv. Integration (Area Calculation)
- c. Step-by-Step Walkthrough of Convolution Example
  - i. Case 1: No Overlap (t < 0)
  - ii. Case 2: Partial Overlap Entering (0 <= t < 1)
  - iii. Case 3: Full Overlap (1 <= t < 2)
  - iv. Case 4: Partial Overlap Exiting (2 <= t < 3)
  - v. Case 5: No Overlap Exited (t >= 3)
- d. Convolution Tables of Common Signal Pairs
- e. Properties of Convolution
  - i. Commutative Property
  - ii. Associative Property
  - iii. Distributive Property
  - iv. Identity and Shifting Properties (Convolution with Delta Functions)
  - v. Homogeneity Property
  - vi. Width Property (Convolution Duration = Sum of Individual Durations)
