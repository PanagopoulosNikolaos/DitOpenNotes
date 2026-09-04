# Assignment 02: Convolution Integral and LTI System Dynamics

## Objective
Assess rigorous analytical and computational evaluation of continuous-time convolution, cascade LTI system responses, impulse response derivation, and step response relationships.

---

## Problem Set

### Problem 1: Analytical Convolution Integral
Compute the convolution $y(t) = x(t) * h(t)$ for the following signals:
$$
x(t) = \begin{cases} t, & 0 \le t < 1 \\ 2 - t, & 1 \le t \le 2 \\ 0, & \text{otherwise} \end{cases}
$$
$$
h(t) = u(t) - u(t - 2)
$$
1. Clearly identify all critical time intervals.
2. Evaluate the integral for each piecewise interval.
3. Verify continuity at all interval boundary points.

### Problem 2: Interconnected LTI Systems
Consider the system block diagram below where $h_1(t) = e^{-t} u(t)$, $h_2(t) = \delta(t - 1)$, and $h_3(t) = u(t) - u(t - 3)$:

```
           +--------+
      +--->|  h1(t) |--->(+)----+
      |    +--------+     ^     |
x(t)--+                   |     +--->[ h3(t) ]---> y(t)
      |    +--------+     |
      +--->|  h2(t) |-----+
           +--------+
```

1. Determine the overall system impulse response $h_{\text{total}}(t)$ in terms of $h_1, h_2, h_3$.
2. State whether the overall interconnected system is (a) Causal, (b) BIBO Stable, and (c) Memoryless. Justify with mathematical proofs.

### Problem 3: Python Computational Verification
Write a Python script using `scipy.signal` to numerically evaluate and plot $y(t)$ from Problem 1. Compare the numerical waveform against your analytical equation and compute the root-mean-square error (RMSE).

