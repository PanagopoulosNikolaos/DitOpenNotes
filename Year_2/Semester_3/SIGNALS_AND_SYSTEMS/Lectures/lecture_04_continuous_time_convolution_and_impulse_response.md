# Lecture 04: Continuous-Time Convolution and Graphical Evaluation

This lecture provides the formal four-step analytical and graphical methodology for computing the continuous convolution integral, solves canonical examples (rectangular pulses, exponential signals), and examines the relationship between impulse response and step response.

---

## 1. The Graphical Convolution Algorithm

The convolution integral is given by:
$$
y(t) = \int_{-\infty}^{\infty} x(\tau) h(t - \tau) \, d\tau
$$

To evaluate $y(t)$ for any arbitrary continuous functions:

```
Step 1: Coordinate Transformation    ---> Express signals as functions of dummy variable tau: x(tau), h(tau)
Step 2: Time-Reversal (Reflection)   ---> Invert h(tau) about the vertical axis to obtain h(-tau)
Step 3: Parameterized Time-Shift     ---> Shift h(-tau) by parameter t to obtain h(t - tau)
Step 4: Multiplication & Integration ---> Multiply x(tau) and h(t - tau), determine non-zero overlap intervals,
                                          and integrate over tau for each distinct range of t
```

---

## 2. Canonical Example 1: Convolution of Two Rectangular Pulses

Let:
$$
x(t) = u(t) - u(t - T_1), \quad h(t) = u(t) - u(t - T_2) \quad (\text{assume } T_1 \le T_2)
$$

### Interval Analysis:
- $x(\tau)$ is non-zero for $0 \le \tau \le T_1$.
- $h(t - \tau)$ is non-zero for $0 \le t - \tau \le T_2 \iff t - T_2 \le \tau \le t$.

```
Interval 1: t < 0
No overlap between [0, T1] and [t - T2, t] ---> y(t) = 0

Interval 2: 0 <= t < T1
Overlap is [0, t]:
y(t) = \int_{0}^{t} (1 \cdot 1) d\tau = t

Interval 3: T1 <= t < T2
Overlap is [0, T1]:
y(t) = \int_{0}^{T_1} 1 d\tau = T_1  (Constant flat top)

Interval 4: T2 <= t < T1 + T2
Overlap is [t - T2, T1]:
y(t) = \int_{t - T_2}^{T_1} 1 d\tau = T_1 - (t - T_2) = T_1 + T_2 - t

Interval 5: t >= T1 + T2
No overlap ---> y(t) = 0
```

*Result:* The convolution of two rectangular pulses of lengths $T_1$ and $T_2$ yields a **trapezoidal pulse** of total duration $T_1 + T_2$ (or a triangular pulse if $T_1 = T_2$).

---

## 3. Canonical Example 2: First-Order RC Circuit Response

Let input $x(t) = u(t)$ be applied to a system with impulse response $h(t) = e^{-a t} u(t)$ ($a > 0$).

For $t < 0$: No overlap between $u(\tau)$ and $u(t - \tau) \implies y(t) = 0$.  
For $t \ge 0$:
$$
y(t) = \int_{0}^{t} 1 \cdot e^{-a(t - \tau)} \, d\tau = e^{-a t} \int_{0}^{t} e^{a \tau} \, d\tau = e^{-a t} \left[ \frac{e^{a \tau}}{a} \right]_{0}^{t} = \frac{e^{-a t}}{a} (e^{a t} - 1) = \frac{1 - e^{-a t}}{a}
$$

Combined closed-form expression:
$$
y(t) = \frac{1}{a} \left(1 - e^{-a t}\right) u(t)
$$

---

## 4. The Step Response $s(t)$

The **Step Response** $s(t)$ is the output of an LTI system when the input is the unit step function $u(t)$:
$$
s(t) = h(t) * u(t) = \int_{-\infty}^{\infty} h(\tau) u(t - \tau) \, d\tau = \int_{-\infty}^{t} h(\tau) \, d\tau
$$

By the Fundamental Theorem of Calculus, the impulse response is the time derivative of the step response:
$$
h(t) = \frac{d s(t)}{dt}
$$

*Engineering Importance:* In physical laboratories, an ideal Dirac delta impulse cannot be generated due to infinite amplitude. Instead, engineers measure the system's step response $s(t)$ using a square-wave generator and differentiate the recorded response to obtain $h(t)$.

---

## 5. Summary

- Convolution evaluation involves reflecting, shifting, multiplying, and integrating across piecewise time intervals.
- The duration of the convolution of two finite-length signals of durations $L_1$ and $L_2$ is strictly $L_1 + L_2$.
- Step response $s(t)$ integrates $h(t)$, and differentiating $s(t)$ recovers the impulse response.

