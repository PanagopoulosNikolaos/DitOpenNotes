# Tutorial 01: Signal Transformations and Graphical Convolution

This tutorial guides students through step-by-step transformations of the independent variable (time-shifting, time-reversal, time-scaling) and provides worked examples of graphical convolution.

---

## 1. Transformations of the Independent Variable

Given an arbitrary continuous-time signal $x(t)$, we often need to construct the modified signal $y(t) = x(a t + b)$.

### 1.1 Proper Order of Operations
To avoid common scaling errors, decompose $x(a t + b)$ into:
$$
x(a(t + \frac{b}{a}))
$$

1. **Method A (Shift then Scale):**
   - Step 1: Shift $x(t)$ by $b$ units to obtain $w(t) = x(t + b)$. (Left shift if $b > 0$, right shift if $b < 0$).
   - Step 2: Scale $w(t)$ by factor $a$ to obtain $y(t) = w(a t) = x(a t + b)$. (Compressed if $|a| > 1$, expanded if $|a| < 1$, reflected if $a < 0$).

2. **Method B (Scale then Shift):**
   - Step 1: Scale $x(t)$ by factor $a$ to obtain $v(t) = x(a t)$.
   - Step 2: Shift $v(t)$ by $\frac{b}{a}$ units: $y(t) = v(t + \frac{b}{a}) = x(a(t + \frac{b}{a})) = x(a t + b)$.

---

## 2. Worked Graphical Convolution Walkthrough

Compute $y(t) = x(t) * h(t)$ where:
- $x(t) = e^{-2t} [u(t) - u(t - 3)]$
- $h(t) = u(t) - u(t - 2)$

### Step 1: Inversion and Shift
Reflect $h(\tau)$ to get $h(-\tau)$ (non-zero for $-2 \le \tau \le 0$).  
Shift by $t$ to obtain $h(t - \tau)$ (non-zero for $t - 2 \le \tau \le t$).  
$x(\tau) = e^{-2\tau}$ is non-zero on interval $[0, 3]$.

### Step 2: Case-by-Case Piecewise Integration

#### Region 1: $t < 0$
The window $[t - 2, t]$ does not intersect $[0, 3]$.
$$y(t) = 0$$

#### Region 2: $0 \le t < 2$
The leading edge enters $[0, 3]$. Overlap is $\tau \in [0, t]$:
$$
y(t) = \int_{0}^{t} e^{-2\tau} \cdot 1 \, d\tau = \left[ -\frac{e^{-2\tau}}{2} \right]_0^t = \frac{1 - e^{-2t}}{2}
$$

#### Region 3: $2 \le t < 3$
The pulse of $h$ is entirely inside $[0, 3]$. Overlap is $\tau \in [t - 2, t]$:
$$
y(t) = \int_{t - 2}^{t} e^{-2\tau} \, d\tau = \left[ -\frac{e^{-2\tau}}{2} \right]_{t - 2}^t = \frac{e^{-2(t - 2)} - e^{-2t}}{2} = \frac{e^{4} - 1}{2} e^{-2t}
$$

#### Region 4: $3 \le t < 5$
The pulse begins exiting $[0, 3]$. Overlap is $\tau \in [t - 2, 3]$:
$$
y(t) = \int_{t - 2}^{3} e^{-2\tau} \, d\tau = \frac{e^{-2(t - 2)} - e^{-6}}{2}
$$

#### Region 5: $t \ge 5$
No overlap ($t - 2 \ge 3$).
$$y(t) = 0$$

---

## 3. Summary of Result

$$
y(t) = \begin{cases}
0, & t < 0 \\
\frac{1 - e^{-2t}}{2}, & 0 \le t < 2 \\
\frac{e^4 - 1}{2} e^{-2t}, & 2 \le t < 3 \\
\frac{e^{-2(t - 2)} - e^{-6}}{2}, & 3 \le t < 5 \\
0, & t \ge 5
\end{cases}
$$
Notice that $y(t)$ is continuous across all boundaries ($t = 0, 2, 3, 5$).

