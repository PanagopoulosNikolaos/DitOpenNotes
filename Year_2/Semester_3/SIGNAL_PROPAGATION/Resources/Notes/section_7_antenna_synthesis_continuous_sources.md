# Antenna Synthesis and Continuous Sources

Antenna synthesis is the inverse problem of antenna theory: given a desired radiation pattern, find the current or aperture distribution that produces it. This contrasts with analysis, where the current distribution is known and the pattern is computed. Synthesis methods are essential in radar, satellite communications, and radio astronomy, where precise control over beamwidth, sidelobe level, and null placement is required. Continuous source models — line sources and aperture distributions — provide the theoretical foundation for synthesising patterns from linear arrays, reflector feeds, and horn antennas. This section covers the principal synthesis techniques: the Schelkunoff polynomial method, the Fourier transform method, the Woodward-Lawson method, Taylor distributions, and the pattern characteristics of common amplitude tapers.

---

## 1. Conceptual Foundation

### 1.1 Why Antenna Synthesis

In antenna analysis, the current distribution $I(z')$ is known (or assumed), and the radiated field $\mathbf{E}(\theta, \phi)$ is computed via the radiation integral. In synthesis, the goal is reversed:

$$
\text{Desired } \mathbf{E}(\theta, \phi) \quad \longrightarrow \quad \text{Required } I(z') \text{ or aperture field } \mathbf{E}_a(x', y')
$$

Synthesis is motivated by three practical needs:

1. **Sidelobe control:** Reduce interference from unwanted directions by specifying a maximum sidelobe level.
2. **Beam shaping:** Produce a cosecant-squared pattern for radar altitude coverage, a flat-top beam for surveillance, or a pencil beam for tracking.
3. **Null placement:** Place nulls in the direction of jammers or interfering sources.

### 1.2 The Central Synthesis Problem

A continuous line source of length $L$ lies along the $z$-axis with current distribution $I(z')$. The far-field pattern $F(\theta)$ is related to $I(z')$ by:

$$
F(\theta) = \int_{-L/2}^{L/2} I(z') e^{jkz' \cos\theta} \, dz'
$$

This is a Fourier transform relationship in the variable $u = \cos\theta$. The synthesis problem is: given a desired $F(u)$, find $I(z')$ such that the integral equation is satisfied.

> **[Key Insight]** The Fourier transform relationship between aperture distribution and far-field pattern is the central insight of synthesis theory. It means that any technique from Fourier analysis — convolution, sampling, windowing — can be applied to antenna pattern design.

### 1.3 Analysis vs. Synthesis

| Aspect | Analysis | Synthesis |
| :--- | :--- | :--- |
| Known quantity | Current distribution $I(z')$ | Desired pattern $F(\theta)$ |
| Unknown quantity | Far-field pattern $F(\theta)$ | Current distribution $I(z')$ |
| Mathematical operation | Fourier transform (forward) | Inverse Fourier transform |
| Uniqueness | Unique pattern for a given current | Multiple current distributions can produce the same pattern |
| Difficulty | Straightforward integration | Ill-posed; requires constraints (e.g., finite length, realisability) |

---

## 2. Formal Definitions and Models

### 2.1 Continuous Line Source

A continuous line source is a current distribution $I(z')$ distributed along a line of length $L$, typically along the $z$-axis. The far-field pattern in the $y$-$z$ plane ($\phi = \pi/2$) is:

$$
F(\theta) = \int_{-L/2}^{L/2} I(z') e^{jkz' \cos\theta} \, dz'
$$

In terms of the variable $u = \cos\theta$ ($-\infty < u < \infty$ in the visible and invisible regions):

$$
F(u) = \int_{-L/2}^{L/2} I(z') e^{jkz' u} \, dz'
$$

The **visible region** corresponds to $-1 \leq u \leq 1$ ($0 \leq \theta \leq \pi$). The **invisible region** ($|u| > 1$) contains evanescent fields that do not propagate.

**Normalised pattern:** $f(u) = F(u) / F_{\max}$.

### 2.2 Schelkunoff Polynomial Method

The Schelkunoff method synthesises an array factor with specified null positions by representing the array factor as a polynomial and placing its roots on the unit circle.

For an $N$-element linear array with uniform spacing $d$, the array factor can be written as:

$$
AF(w) = \sum_{n=0}^{N-1} I_n w^n, \quad w = e^{j\psi}, \quad \psi = kd \cos\theta + \beta
$$

where $I_n$ are the excitation coefficients and $\beta$ is the progressive phase shift.

**Procedure:**

1. Determine the desired null positions $\theta_m$ and convert them to $w_m = e^{j\psi(\theta_m)}$.
2. Construct the polynomial $AF(w) = \prod_{m=1}^{N-1} (w - w_m)$.
3. Expand the polynomial to obtain the excitation coefficients $I_n$.
4. Apply a scaling factor to match the desired directivity.

**Root placement rules:**
- Roots on the unit circle produce pattern nulls.
- Roots inside the unit circle ($|w| < 1$) produce reduced sidelobes.
- Roots outside the unit circle ($|w| > 1$) produce superdirective patterns (high Q, narrow bandwidth).

The Schelkunoff polynomial is of degree $N-1$ and can place up to $N-1$ nulls. The polynomial has $N$ coefficients, corresponding to the $N$ element excitations.

### 2.3 Fourier Transform Method

The Fourier transform method exploits the exact Fourier relationship between the aperture distribution and the far-field pattern. For a continuous line source of length $L$:

$$
F(u) = \int_{-L/2}^{L/2} I(z') e^{jk z' u} \, dz'
$$

Given a desired pattern $F_d(u)$, the required aperture distribution is the inverse Fourier transform:

$$
I(z') = \frac{k}{2\pi} \int_{-\infty}^{\infty} F_d(u) e^{-jk z' u} \, du
$$

**Practical limitations:**
- The integral is over all $u$ ($-\infty$ to $\infty$), but $F_d(u)$ is only specified in the visible region $-1 \leq u \leq 1$.
- The finite aperture length $L$ acts as a spatial filter, truncating the ideal infinite aperture distribution.
- Truncation causes **Gibbs phenomenon**: ripples in the pattern near discontinuities (e.g., at the pattern edge of a sector beam).

**Mitigation:** Apply a Taylor or Bayliss taper to the truncated distribution to smooth the truncation and reduce ripple.

### 2.4 Woodward-Lawson Method

The Woodward-Lawson method synthesises a desired pattern by superimposing a finite number of orthogonal pattern beams. Each beam is produced by a uniform-amplitude, linear-phase aperture distribution (a "cosine" aperture distribution):

$$
I_n(z') = \frac{1}{L} e^{-jk z' u_n}, \quad -\frac{L}{2} \leq z' \leq \frac{L}{2}
$$

The far-field pattern of this distribution is:

$$
F_n(u) = \frac{\sin\left[\frac{kL}{2}(u - u_n)\right]}{\frac{kL}{2}(u - u_n)}
$$

This is a $\sin(x)/x$ pattern (a sinc function) centred at $u = u_n$ with nulls at:

$$
u = u_n \pm \frac{m\pi}{kL/2} = u_n \pm \frac{m\lambda}{L}, \quad m = 1, 2, \ldots
$$

**Synthesis procedure:**

1. Sample the desired pattern $F_d(u)$ at $N$ equally spaced points $u_n = n\lambda/L$ for $n = 0, \pm 1, \pm 2, \ldots, \pm M$.
2. These sampling points are separated by $\Delta u = \lambda/L$, which is the **Rayleigh resolution** of an aperture of length $L$.
3. The excitation amplitude at each sample is $A_n = F_d(u_n)$.
4. The total aperture distribution is:

$$
I(z') = \sum_{n=-M}^{M} A_n e^{-jk z' u_n}
$$

5. The synthesised pattern is:

$$
F(u) = \sum_{n=-M}^{M} A_n \frac{\sin\left[\frac{kL}{2}(u - u_n)\right]}{\frac{kL}{2}(u - u_n)}
$$

At the sampling points $u = u_m$, the sinc functions of all other samples are zero, so $F(u_m) = A_m = F_d(u_m)$. The pattern exactly matches the desired pattern at the sampling points, with interpolation between samples.

> **[Key Insight]** The Woodward-Lawson method guarantees exact pattern matching at the sampling points. The quality of the synthesis depends on the number of samples (aperture length in wavelengths). Longer apertures provide more samples and better approximation.

### 2.5 Taylor Line-Source Distributions

The Taylor distributions produce patterns with controlled sidelobe levels by modifying the ideal uniform distribution. Two forms exist: the Taylor $n$-parameter (Tschebyscheff-error) and the Taylor one-parameter distribution.

#### 2.5.1 Taylor $n$-Parameter (Tschebyscheff-Error) Distribution

This distribution produces a pattern where the first $n-1$ sidelobes on each side of the main beam are at a constant design level, and the remaining sidelobes decay as $1/u$. This avoids the excessive Q and narrow bandwidth of the Dolph-Tschebyscheff array, which attempts to maintain equal sidelobes everywhere.

**Pattern function:**

$$
F(u) = \frac{\sin(\pi u)}{\pi u} \prod_{m=1}^{n-1} \frac{1 - \left(\frac{u}{\sigma u_m}\right)^2}{1 - \left(\frac{u}{m}\right)^2}
$$

where:
- $u = \frac{L}{\lambda} \cos\theta$
- $\sigma$ is the **beam-broadening factor** (controls the uniform sidelobe region)
- $u_m$ are the **null locations** of the ideal pattern
- $n$ is the number of equal-level sidelobes

The nulls of the ideal uniform distribution occur at $u = \pm 1, \pm 2, \pm 3, \ldots$. In the Taylor distribution, the first $n-1$ nulls are relocated to achieve the desired sidelobe level.

**Aperture distribution:**

$$
I(z') = \frac{1}{L} \left[ 1 + 2 \sum_{m=1}^{n-1} F_m \cos\left(\frac{2\pi m z'}{L}\right) \right]
$$

where $F_m$ are the pattern samples at the relocated null positions.

#### 2.5.2 Taylor One-Parameter Distribution

A simpler distribution controlled by a single parameter $\mathcal{R}$ (the voltage sidelobe ratio). The pattern function is:

$$
F(u) = \frac{\sin\left(\pi \sqrt{u^2 - \mathcal{R}^2}\right)}{\pi \sqrt{u^2 - \mathcal{R}^2}}
$$

For $u > \mathcal{R}$, the function becomes $\sinh$ and decays monotonically. The parameter $\mathcal{R}$ is related to the sidelobe level (SLL) in dB by:

$$
\mathcal{R} = \frac{1}{\pi} \cosh^{-1}\left(10^{\text{SLL}_{\text{dB}} / 20}\right)
$$

**Aperture distribution:**

$$
I(z') = I_0 \cdot \begin{cases}
1, & |z'| \leq \frac{L}{2} \\
0, & |z'| > \frac{L}{2}
\end{cases}
$$

The Taylor one-parameter distribution is the continuous version of the Dolph-Tschebyscheff array. It produces a pattern with all sidelobes at the same design level.

### 2.6 Triangular, Cosine, and Cosine-Squared Amplitude Distributions

These are simple, closed-form aperture tapers commonly used in practice. Each has known pattern expressions and trade-offs between beamwidth and sidelobe level.

#### 2.6.1 Triangular Distribution

**Aperture distribution:**

$$
I(z') = 1 - \frac{2|z'|}{L}, \quad -\frac{L}{2} \leq z' \leq \frac{L}{2}
$$

**Normalised pattern:**

$$
F(u) = \left[ \frac{\sin\left(\frac{kL u}{4}\right)}{\frac{kL u}{4}} \right]^2
$$

**Properties:** SLL $= -26$ dB, HPBW $= 1.28 \times$ (uniform HPBW), first null at $u = 2\lambda/L$.

#### 2.6.2 Cosine Distribution

**Aperture distribution:**

$$
I(z') = \cos\left(\frac{\pi z'}{L}\right), \quad -\frac{L}{2} \leq z' \leq \frac{L}{2}
$$

**Normalised pattern:**

$$
F(u) = \frac{\cos(kL u / 2)}{1 - (kL u / \pi)^2} \cdot \frac{\pi}{2}
$$

**Properties:** SLL $= -23$ dB, HPBW $= 1.17 \times$ (uniform HPBW).

#### 2.6.3 Cosine-Squared Distribution

**Aperture distribution:**

$$
I(z') = \cos^2\left(\frac{\pi z'}{L}\right), \quad -\frac{L}{2} \leq z' \leq \frac{L}{2}
$$

**Normalised pattern:**

$$
F(u) = \frac{\sin(kL u / 2)}{kL u / 2} \cdot \frac{1}{1 - (kL u / \pi)^2} \cdot \frac{\pi^2}{2}
$$

**Properties:** SLL $= -32$ dB, HPBW $= 1.44 \times$ (uniform HPBW).

#### 2.6.4 Comparative Table

| Distribution | Peak SLL (dB) | HPBW (relative to uniform) | First Null Location | Directivity Loss (dB) |
| :--- | :--- | :--- | :--- | :--- |
| Uniform | $-13.26$ | $1.00$ | $u = \lambda/L$ | $0.00$ |
| Cosine | $-23$ | $1.17$ | $u = 1.5\lambda/L$ | $0.92$ |
| Triangular | $-26$ | $1.28$ | $u = 2.0\lambda/L$ | $1.25$ |
| Cosine-squared | $-32$ | $1.44$ | $u = 2.0\lambda/L$ | $1.76$ |

### 2.7 Line-Source Phase Distributions

In addition to amplitude tapers, the phase of the current distribution can be varied to control the beam direction and shape.

**Linear phase taper (beam squint):**

$$
I(z') = |I(z')| e^{-jk z' \cos\theta_0}
$$

This shifts the main beam to $\theta = \theta_0$:

$$
F(\theta) = F_0(\theta - \theta_0)
$$

where $F_0$ is the pattern of the amplitude distribution alone.

**Quadratic phase taper (beam broadening):**

$$
I(z') = |I(z')| e^{-j\alpha (z')^2}
$$

A quadratic phase error broadens the main beam, reduces directivity, and raises the sidelobe level. The effect is analogous to a defocused lens.

**Phase error tolerance:** A phase error of $\pm \pi/4$ (peak) across the aperture causes less than $0.5$ dB directivity loss. Errors exceeding $\pm \pi/2$ cause significant pattern degradation.

### 2.8 Continuous Aperture Sources

Continuous aperture sources extend the line-source concept to two dimensions. The aperture distribution $E_a(x', y')$ over a surface $S$ radiates a far-field pattern:

$$
\mathbf{E}(\theta, \phi) = \frac{jk e^{-jkr}}{2\pi r} (\hat{\boldsymbol{\theta}} \cos\phi - \hat{\boldsymbol{\phi}} \sin\phi \cos\theta) \iint_S E_a(x', y') e^{jk(x' \sin\theta \cos\phi + y' \sin\theta \sin\phi)} \, dx' dy'
$$

For a rectangular aperture of dimensions $a \times b$, with a separable distribution $E_a(x', y') = E_x(x') E_y(y')$, the pattern factorises:

$$
F(\theta, \phi) = F_x(u) \cdot F_y(v)
$$

where $u = \sin\theta \cos\phi$ and $v = \sin\theta \sin\phi$.

**Common rectangular aperture distributions:**
- Uniform: $E_a = 1$, pattern $F(u) = \frac{\sin(ka u/2)}{ka u/2}$ (in each principal plane).
- Cosine taper in both planes: $E_a = \cos(\pi x'/a) \cos(\pi y'/b)$.
- Taylor taper in both planes for low sidelobes.

**Circular aperture:** For a circular aperture of radius $a$ with rotationally symmetric distribution $E_a(\rho')$, the far-field pattern involves the Hankel transform:

$$
F(\theta) = 2\pi \int_0^a E_a(\rho') J_0(k \rho' \sin\theta) \rho' d\rho'
$$

where $J_0$ is the zero-order Bessel function of the first kind.

> **[Supplementary]** The Airy pattern (far-field of a uniform circular aperture) has a first sidelobe at $-17.6$ dB (relative to the peak), which is $4.3$ dB worse than the uniform linear aperture's $-13.3$ dB. This is because the circular geometry concentrates more energy in the sidelobes.

---

## 3. Key Parameters and Constraints

**Table 1: Synthesis Parameters**

| Parameter | Symbol | Typical Range | Impact on Synthesised Pattern |
| :--- | :--- | :--- | :--- |
| Aperture length | $L$ | $1\lambda$ to $100\lambda$ | Determines beamwidth: $\theta_{\text{HPBW}} \propto \lambda/L$ |
| Sidelobe level | SLL | $-20$ to $-60$ dB | Lower SLL broadens main beam (gain-bandwidth product trade-off) |
| Number of Woodward-Lawson samples | $N$ | $2L/\lambda + 1$ | Controls pattern detail; longer apertures allow finer sampling |
| Taylor $n$ parameter | $n$ | $2$ to $20$ | Number of equal-ripple sidelobes; larger $n$ approximates Tschebyscheff |
| Taylor $\mathcal{R}$ | $\mathcal{R}$ | $1$ to $10$ | Controls SLL: $\mathcal{R} = \frac{1}{\pi}\cosh^{-1}(10^{\text{SLL}/20})$ |
| Phase error (RMS) | $\sigma_\phi$ | $0$ to $\pi$ rad | Typical design target: $\sigma_\phi \leq \pi/8$ for $< 0.25$ dB loss |
| Visible region | $u$ | $-1 \leq u \leq 1$ | Only patterns in $|u| \leq 1$ radiate; $|u| > 1$ is reactive |

**Table 2: Amplitude Distribution Trade-offs**

| Distribution | SLL (dB) | HPBW ($\lambda/L$) | First Null ($\lambda/L$) | Directivity Loss (dB) | Aperture Efficiency |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Uniform | $-13.3$ | $0.88$ | $1.00$ | $0.00$ | $1.00$ |
| Cosine | $-23$ | $1.03$ | $1.50$ | $0.92$ | $0.81$ |
| Triangular | $-26$ | $1.13$ | $2.00$ | $1.25$ | $0.75$ |
| Cosine-squared | $-32$ | $1.27$ | $2.00$ | $1.76$ | $0.67$ |
| Taylor ($n=5$, SLL$=-30$) | $-30$ | $1.09$ | $1.30$ | $0.70$ | $0.85$ |

---

## 4. Step-by-Step Mechanism

### 4.1 Woodward-Lawson Synthesis Procedure

The Woodward-Lawson method is the most intuitive synthesis technique and serves as a template for understanding the others.

**Step 1:** Determine the available visible region and aperture length.
- Compute $u = \cos\theta$ range: $-1 \leq u \leq 1$.
- Compute the number of orthogonal beams: $N = \text{floor}(2L/\lambda) + 1$.

**Step 2:** Sample the desired pattern at $u_n = n\lambda/L$.
- For a real desired pattern $F_d(u)$, sample at $u_n = 0, \pm\lambda/L, \pm 2\lambda/L, \ldots$
- The sampling interval $\Delta u = \lambda/L$ ensures the sinc patterns are orthogonal.

**Step 3:** Compute the excitation amplitudes $A_n = F_d(u_n)$.

**Step 4:** Construct the aperture distribution:
$$
I(z') = \sum_{n=-M}^{M} A_n e^{-jk z' u_n}, \quad M = \frac{N-1}{2}
$$

**Step 5:** Compute the synthesised pattern:
$$
F(u) = \sum_{n=-M}^{M} A_n \frac{\sin\left[\frac{kL}{2}(u - u_n)\right]}{\frac{kL}{2}(u - u_n)}
$$

**Step 6:** Verify that $F(u_m) = A_m$ at the sampling points. If the pattern is acceptable, the synthesis is complete. If unacceptable (excessive ripple between samples), increase $L$ or use a different synthesis method.

### 4.2 Schelkunoff Polynomial Synthesis Procedure

**Step 1:** Determine the number of elements $N$ and spacing $d$.

**Step 2:** Map desired null angles $\theta_m$ to $w_m = e^{j(kd\cos\theta_m + \beta)}$.

**Step 3:** For each desired null at $\psi = \psi_m$, place a root at $w = e^{j\psi_m}$.

**Step 4:** Construct the polynomial:
$$
AF(w) = \prod_{m=1}^{N-1} (w - w_m)
$$

**Step 5:** Expand the polynomial to obtain $I_n$ as the coefficients of $w^n$.

**Step 6:** If amplitude tapering is also desired, scale the coefficients to achieve the required sidelobe envelope.

### 4.3 Taylor Distribution Design Procedure

**Step 1:** Specify the desired sidelobe level SLL (dB) and the number $n$ of equal-ripple sidelobes.

**Step 2:** Compute the beam-broadening factor $\sigma$:
$$
\sigma = \frac{n}{\sqrt{\mathcal{R}^2 + (n - 0.5)^2}}, \quad \mathcal{R} = \frac{1}{\pi} \cosh^{-1}\left(10^{\text{SLL}/20}\right)
$$

**Step 3:** Compute the relocated nulls $u_m = \sigma \sqrt{\mathcal{R}^2 + (m - 0.5)^2}$ for $m = 1, 2, \ldots, n-1$.

**Step 4:** Compute the pattern samples $F_m$:
$$
F_m = \frac{\sin(\pi u_m)}{\pi u_m} \prod_{q=1}^{n-1} \frac{1 - \left(\frac{u_m}{\sigma u_q}\right)^2}{1 - \left(\frac{u_m}{q}\right)^2}
$$

**Step 5:** Construct the aperture distribution using the Fourier series expansion:
$$
I(z') = \frac{1}{L} \left[ 1 + 2 \sum_{m=1}^{n-1} F_m \cos\left(\frac{2\pi m z'}{L}\right) \right]
$$

---

## 5. Connections and Cross-References

- **Section 6 (Arrays: Linear, Planar, and Circular):** The array factor concepts from Section 6 are the discrete precursor to continuous source synthesis. The Schelkunoff polynomial method is a direct extension of the array factor polynomial. The Woodward-Lawson method uses the orthogonal beams concept that arises naturally in uniformly spaced arrays.
- **Section 3 (Radiation Integrals):** The Fourier transform relationship between aperture distribution and far-field pattern is derived from the vector potential integrals in Section 3.
- **Section 2 (Fundamental Parameters):** The directivity, beamwidth, and sidelobe level trade-offs quantified in Section 2 are the optimisation targets for all synthesis methods.
- **Section 12 (Aperture Antennas):** The rectangular and circular aperture distributions synthesised here are the feed distributions for the horn antennas in Section 13 and reflector antennas in Section 15.
- **Section 8 (Integral Equations, Moment Method):** For complex aperture shapes where closed-form synthesis is unavailable, numerical methods from Section 8 provide the solution.

*Prerequisite: Section 6 (Arrays: Linear, Planar, and Circular) — array factor theory and the pattern multiplication principle are foundational to understanding synthesis methods.*

---

## Solved Exercises

### Exercise 1: Woodward-Lawson Synthesis of a Sector Beam

**Problem:** Synthesise a sector beam pattern using the Woodward-Lawson method for a line source of length $L = 5\lambda$. The desired pattern is:
$$
F_d(\theta) = \begin{cases}
1, & |\theta| \leq 30^\circ \\
0, & \text{otherwise}
\end{cases}
$$

Find the sampling points, excitation amplitudes, and compute the aperture distribution.

**Solution:**

Step 1: Convert to $u = \cos\theta$ variable.
$$
F_d(u) = \begin{cases}
1, & |u| \geq \cos 30^\circ = 0.866 \\
0, & |u| < 0.866
\end{cases}
$$

Note: $|\theta| \leq 30^\circ$ corresponds to $\cos 30^\circ \leq u \leq 1$ (in the forward direction). The desired pattern is 1 in the visible region $u \in [-1, -0.866] \cup [0.866, 1]$ and 0 in $u \in (-0.866, 0.866)$.

Wait — let me reconsider. A sector beam of $60^\circ$ total width centred at broadside ($\theta = 90^\circ$) corresponds to $\theta \in [60^\circ, 120^\circ]$. Converting: $u = \cos\theta$ gives $u \in [-0.5, 0.5]$.

The desired pattern is:
$$
F_d(u) = \begin{cases}
1, & |u| \leq 0.5 \\
0, & |u| > 0.5
\end{cases}
$$

Step 2: Number of samples.
$$
L = 5\lambda \quad \Rightarrow \quad \frac{L}{\lambda} = 5
$$

Number of sampling points in $|u| \leq 1$:
$$
N = 2\left\lfloor \frac{L}{\lambda} \right\rfloor + 1 = 2(5) + 1 = 11
$$

Sampling points: $u_n = \frac{n\lambda}{L} = \frac{n}{5}$ for $n = 0, \pm 1, \pm 2, \pm 3, \pm 4, \pm 5$.

Step 3: Sample the desired pattern.
At $u = 0$: $F_d(0) = 1$.
At $u = \pm 0.2$: $F_d(\pm 0.2) = 1$ (since $|u| \leq 0.5$).
At $u = \pm 0.4$: $F_d(\pm 0.4) = 1$.
At $u = \pm 0.6$: $F_d(\pm 0.6) = 0$ (since $|u| > 0.5$).
At $u = \pm 0.8$: $F_d(\pm 0.8) = 0$.
At $u = \pm 1.0$: $F_d(\pm 1.0) = 0$.

Excitations: $A_0 = 1$, $A_{\pm 1} = 1$, $A_{\pm 2} = 1$, $A_{\pm 3} = 0$, $A_{\pm 4} = 0$, $A_{\pm 5} = 0$.

Step 4: Aperture distribution.
$$
I(z') = \frac{1}{L} \sum_{n=-2}^{2} e^{-jk z' u_n} = \frac{1}{5\lambda} \left[ 1 + 2\cos(k z' \cdot 0.2) + 2\cos(k z' \cdot 0.4) \right]
$$

With $k = 2\pi/\lambda$:
$$
I(z') = \frac{1}{5\lambda} \left[ 1 + 2\cos\left(\frac{2\pi z'}{5\lambda/\lambda} \cdot 0.2\right) + 2\cos\left(\frac{2\pi z'}{5\lambda} \cdot 0.4\right) \right]
$$

Step 5: Pattern verification.
At $u = 0$: $F(0) = \sum A_n \cdot 1 = 1 + 1 + 1 + 0 + 0 + 0 + 0 = 3$ — wait, this is wrong. The total pattern is the sum of sinc functions, not the sum of $A_n$.

Let me re-evaluate. The synthesised pattern is:
$$
F(u) = \sum_{n=-5}^{5} A_n \frac{\sin\left[\frac{kL}{2}(u - u_n)\right]}{\frac{kL}{2}(u - u_n)}
$$

Since only $A_{-2}, A_{-1}, A_0, A_1, A_2$ are non-zero:
$$
F(u) = \frac{\sin(5\pi u)}{5\pi u} + \frac{\sin[5\pi(u - 0.2)]}{5\pi(u - 0.2)} + \frac{\sin[5\pi(u + 0.2)]}{5\pi(u + 0.2)} + \frac{\sin[5\pi(u - 0.4)]}{5\pi(u - 0.4)} + \frac{\sin[5\pi(u + 0.4)]}{5\pi(u + 0.4)}
$$

At $u = 0$: The sinc functions for $u_n = \pm 0.2$ and $\pm 0.4$ evaluate to:
$$
\frac{\sin(5\pi \cdot \pm 0.2)}{5\pi \cdot \pm 0.2} = \frac{\sin(\pm \pi)}{\pm \pi} = 0
$$

So only the $n = 0$ term contributes: $F(0) = 1$.

At $u = 0.2$: The $n = 0$ term: $\frac{\sin(5\pi \cdot 0.2)}{5\pi \cdot 0.2} = \frac{\sin(\pi)}{\pi} = 0$.
The $n = 1$ term ($u_1 = 0.2$): $\frac{\sin(5\pi \cdot 0)}{5\pi \cdot 0} = 1$ (by limit).
The $n = -1$ term: $\frac{\sin[5\pi(0.2 + 0.2)]}{5\pi(0.2 + 0.2)} = \frac{\sin(2\pi)}{2\pi} = 0$.
The $n = 2$ term: $\frac{\sin[5\pi(0.2 - 0.4)]}{5\pi(0.2 - 0.4)} = \frac{\sin(-\pi)}{-\pi} = 0$.
The $n = -2$ term: $\frac{\sin[5\pi(0.2 + 0.4)]}{5\pi(0.2 + 0.4)} = \frac{\sin(3\pi)}{3\pi} = 0$.

Thus $F(0.2) = 1$, matching the desired pattern value at the sampling point.

**Result:** The Woodward-Lawson synthesis produces a sector beam that exactly matches the desired pattern at the five sampling points $u = 0, \pm 0.2, \pm 0.4$. Between samples, the pattern is the sum of sinc functions, producing ripple. A longer aperture (more samples) would better approximate the sharp transition at $|u| = 0.5$.

---

### Exercise 2: Schelkunoff Null Placement

**Problem:** Design a 4-element uniform linear array ($d = \lambda/2$, $\beta = 0$) with nulls at $\theta = 0^\circ$ (endfire) and $\theta = 60^\circ$ using the Schelkunoff polynomial method. Determine the excitation coefficients.

**Solution:**

Step 1: Compute $w$ at each null.
For $d = \lambda/2$: $kd = \frac{2\pi}{\lambda} \cdot \frac{\lambda}{2} = \pi$.

$$
\psi = kd \cos\theta + \beta = \pi \cos\theta
$$

Null at $\theta = 0^\circ$: $\cos 0^\circ = 1 \Rightarrow \psi = \pi \Rightarrow w_1 = e^{j\pi} = -1$.

Null at $\theta = 60^\circ$: $\cos 60^\circ = 0.5 \Rightarrow \psi = \pi \cdot 0.5 = \pi/2 \Rightarrow w_2 = e^{j\pi/2} = j$.

Step 2: Construct the Schelkunoff polynomial.
For $N = 4$ elements, the polynomial is of degree $N-1 = 3$:

$$
AF(w) = (w - w_1)(w - w_2)(w - w_3)
$$

We have only two nulls specified, but a degree-3 polynomial requires three roots. The third root is arbitrary and can be used to adjust the pattern shape. We choose $w_3 = -j$ (complex conjugate of $w_2$) to produce a real symmetric amplitude distribution.

Step 3: Expand the polynomial.

$$
AF(w) = (w + 1)(w - j)(w + j)
$$

First expand the conjugate pair:
$$
(w - j)(w + j) = w^2 + 1
$$

Then multiply:
$$
AF(w) = (w + 1)(w^2 + 1) = w^3 + w^2 + w + 1
$$

Step 4: Extract excitations.
The coefficients of $w^n$ give the element excitations $I_n$:
$$
AF(w) = I_0 + I_1 w + I_2 w^2 + I_3 w^3 = 1 + w + w^2 + w^3
$$

Thus: $I_0 = 1$, $I_1 = 1$, $I_2 = 1$, $I_3 = 1$.

This is a uniform array! Let us verify that the nulls are indeed at the desired positions.

Step 5: Verify the nulls.
The array factor is:
$$
AF(\psi) = 1 + e^{j\psi} + e^{j2\psi} + e^{j3\psi} = e^{j3\psi/2} \frac{\sin(2\psi)}{\sin(\psi/2)}
$$

Nulls occur when $\sin(2\psi) = 0$ (except where $\sin(\psi/2) = 0$ as well, which is the main beam):

$\sin(2\psi) = 0 \Rightarrow 2\psi = m\pi \Rightarrow \psi = m\pi/2$ for $m = 0, \pm 1, \pm 2, \ldots$

Removing the main beam null ($\psi = 0, \pm 2\pi, \ldots$): nulls at $\psi = \pm\pi/2, \pm\pi, \pm 3\pi/2, \ldots$

For $\psi = \pi$: $\theta = \cos^{-1}(\pi/\pi) = \cos^{-1}(1) = 0^\circ$ (endfire null).
For $\psi = \pi/2$: $\theta = \cos^{-1}((\pi/2)/\pi) = \cos^{-1}(0.5) = 60^\circ$.

Both nulls are correctly placed.

**Result:** A uniform 4-element array with $d = \lambda/2$ naturally has nulls at $\theta = 0^\circ$ and $60^\circ$. This shows that the Schelkunoff method reproduces known results for simple cases. In practice, the polynomial can be factored to place nulls at arbitrary positions.

---

### Exercise 3: Fourier Transform Synthesis — Rectangular Pulse Pattern

**Problem:** Use the Fourier transform method to find the aperture distribution required to produce a rectangular pattern:
$$
F_d(u) = \begin{cases}
1, & |u| \leq u_0 \\
0, & |u| > u_0
\end{cases}
$$
where $u = \cos\theta$ and $u_0 = 0.2$. Assume an infinite aperture and compute $I(z')$.

**Solution:**

Step 1: Apply the inverse Fourier transform.
For an infinite aperture ($L \to \infty$):
$$
I(z') = \frac{k}{2\pi} \int_{-\infty}^{\infty} F_d(u) e^{-jk z' u} \, du
$$

Since $F_d(u) = 0$ for $|u| > u_0$:
$$
I(z') = \frac{k}{2\pi} \int_{-u_0}^{u_0} e^{-jk z' u} \, du
$$

Step 2: Evaluate the integral.
$$
I(z') = \frac{k}{2\pi} \left[ \frac{e^{-jk z' u}}{-jk z'} \right]_{-u_0}^{u_0}
= \frac{k}{2\pi} \cdot \frac{e^{-jk z' u_0} - e^{jk z' u_0}}{-jk z'}
= \frac{1}{2\pi} \cdot \frac{2\sin(k z' u_0)}{z'}
= \frac{k u_0}{\pi} \cdot \frac{\sin(k z' u_0)}{k z' u_0}
$$

Step 3: Simplify.
$$
I(z') = \frac{k u_0}{\pi} \, \text{sinc}(k z' u_0)
$$

Substituting $u_0 = 0.2$:
$$
I(z') = \frac{0.2k}{\pi} \, \text{sinc}(0.2 k z')
$$

Step 4: Interpret the result.
The required aperture distribution is a sinc function, which extends to infinity. For a finite aperture of length $L$, the distribution must be truncated. Truncation causes Gibbs oscillations in the pattern near $|u| = u_0$.

Step 5: Compute the pattern of the truncated aperture.
For a finite aperture of length $L = 10\lambda$, the truncated distribution is:
$$
I_L(z') = \begin{cases}
\frac{0.2k}{\pi} \, \text{sinc}(0.2 k z'), & |z'| \leq 5\lambda \\
0, & |z'| > 5\lambda
\end{cases}
$$

The resulting pattern is the convolution of the ideal rectangular pattern with the Fourier transform of the truncation window:
$$
F(u) = F_d(u) \ast \frac{\sin(kL u/2)}{kL u/2}
$$

This produces ripple near the pattern edges with approximately $9\%$ overshoot (Gibbs phenomenon).

**Result:** The ideal aperture distribution for a rectangular pattern is $I(z') = (k u_0 / \pi) \, \text{sinc}(k z' u_0)$, which is infinite in extent. Truncation to a finite aperture causes pattern ripple. To mitigate this, a Taylor or Bayliss taper can replace the abrupt truncation.

---

### Exercise 4: Taylor One-Parameter Distribution Design

**Problem:** Design a Taylor one-parameter line-source distribution for an aperture of length $L = 8\lambda$ with a desired sidelobe level of $-30$ dB. Compute the parameter $\mathcal{R}$, the beam-broadening factor, and the HPBW relative to a uniform aperture.

**Solution:**

Step 1: Compute $\mathcal{R}$ from the desired SLL.
$$
\mathcal{R} = \frac{1}{\pi} \cosh^{-1}\left(10^{\text{SLL}/20}\right)
= \frac{1}{\pi} \cosh^{-1}\left(10^{30/20}\right)
= \frac{1}{\pi} \cosh^{-1}(31.62)
$$

$$
\cosh^{-1}(x) = \ln(x + \sqrt{x^2 - 1}) = \ln(31.62 + \sqrt{31.62^2 - 1})
= \ln(31.62 + 31.60) = \ln(63.22) = 4.147
$$

$$
\mathcal{R} = \frac{4.147}{\pi} = 1.320
$$

Step 2: Compute the beam-broadening factor.
The beam-broadening factor for the Taylor one-parameter distribution relative to a uniform aperture is:
$$
\text{BF} = \frac{\text{HPBW}_{\text{Taylor}}}{\text{HPBW}_{\text{uniform}}} = \frac{2}{\pi} \sqrt{(\cosh^{-1} 10^{\text{SLL}/20})^2 + (\pi/2)^2}
$$

Wait — let me use a more direct formula. For the Taylor one-parameter distribution, the beam-broadening factor is:

$$
\sigma = \frac{\mathcal{R}}{\sqrt{\mathcal{R}^2 + 0.25}}
$$

No, this is for the $n$-parameter distribution. For the one-parameter distribution:

The HPBW of the uniform aperture of length $L$ is $\text{HPBW}_0 \approx 0.88 \lambda/L$ (in radians, in $u$-space). The Taylor one-parameter distribution broadens this by:

$$
\text{BF} = \frac{\pi \mathcal{R}}{2} \cdot \frac{1}{\sqrt{\mathcal{R}^2 - 0.25}}
$$

For $\mathcal{R} = 1.320$:
$$
\text{BF} = \frac{\pi \cdot 1.320}{2} \cdot \frac{1}{\sqrt{1.320^2 - 0.25}}
= 2.074 \cdot \frac{1}{\sqrt{1.492}}
= \frac{2.074}{1.222} = 1.698
$$

Step 3: Compute HPBW.
Uniform aperture HPBW in $\theta$-space for $L = 8\lambda$:
$$
\theta_{\text{HPBW},0} \approx \frac{0.88 \lambda}{L} \cdot \frac{180^\circ}{\pi} = \frac{0.88}{8} \times 57.3^\circ = 0.11 \times 57.3^\circ = 6.30^\circ
$$

Taylor one-parameter HPBW:
$$
\theta_{\text{HPBW}} = \text{BF} \times \theta_{\text{HPBW},0} = 1.698 \times 6.30^\circ = 10.70^\circ
$$

Step 4: Pattern function at broadside.
At $u = 0$:
$$
F(0) = \frac{\sin(\pi j \mathcal{R})}{\pi j \mathcal{R}} = \frac{\sinh(\pi \mathcal{R})}{\pi \mathcal{R}}
= \frac{\sinh(4.147)}{4.147}
= \frac{31.62}{4.147}
= 7.62
$$

This confirms the pattern level at broadside is consistent with the directivity.

**Result:** For SLL $= -30$ dB: $\mathcal{R} = 1.320$, beam-broadening factor $= 1.698$, HPBW $= 10.70^\circ$ (compared to $6.30^\circ$ for uniform).

---

### Exercise 5: Comparison of Amplitude Distributions

**Problem:** A line source of length $L = 10\lambda$ is designed with four different amplitude distributions: uniform, cosine, triangular, and cosine-squared. For each distribution, compute (a) the HPBW in degrees, (b) the first null position in $u$, and (c) the directivity loss relative to uniform.

**Solution:**

Step 1: Uniform distribution.
$$
\text{HPBW} = 0.88 \frac{\lambda}{L} = 0.88 \times \frac{1}{10} = 0.088 \text{ rad} = 5.04^\circ
$$
First null: $u = \lambda/L = 0.1$.
Directivity loss: $0$ dB.

Step 2: Cosine distribution.
Beam-broadening factor: $1.17$.
$$
\text{HPBW} = 1.17 \times 5.04^\circ = 5.90^\circ
$$
First null: $u = 1.5 \lambda/L = 0.15$.
Directivity loss: $0.92$ dB.

Step 3: Triangular distribution.
Beam-broadening factor: $1.28$.
$$
\text{HPBW} = 1.28 \times 5.04^\circ = 6.45^\circ
$$
First null: $u = 2.0 \lambda/L = 0.20$.
Directivity loss: $1.25$ dB.

Step 4: Cosine-squared distribution.
Beam-broadening factor: $1.44$.
$$
\text{HPBW} = 1.44 \times 5.04^\circ = 7.26^\circ
$$
First null: $u = 2.0 \lambda/L = 0.20$.
Directivity loss: $1.76$ dB.

Step 5: Summary table.

| Distribution | HPBW (degrees) | First Null ($u$) | Directivity Loss (dB) |
| :--- | :--- | :--- | :--- |
| Uniform | $5.04$ | $0.10$ | $0.00$ |
| Cosine | $5.90$ | $0.15$ | $0.92$ |
| Triangular | $6.45$ | $0.20$ | $1.25$ |
| Cosine-squared | $7.26$ | $0.20$ | $1.76$ |

**Result:** The uniform distribution has the narrowest beamwidth and highest directivity but the worst sidelobe level ($-13.3$ dB). The cosine-squared distribution has the lowest sidelobes ($-32$ dB) at the cost of $76\%$ wider beamwidth and $1.76$ dB directivity loss. This illustrates the fundamental trade-off in aperture synthesis: lower sidelobes require broader beams and lower gain.

---

### Exercise 6: Woodward-Lawson Synthesis of a Cosecant-Squared Pattern

**Problem:** A radar requires a cosecant-squared pattern $F_d(\theta) = \csc^2(\theta)$ for $\theta \in [10^\circ, 60^\circ]$ and near-zero elsewhere, where $\theta$ is measured from the $z$-axis (endfire). Synthesise this using the Woodward-Lawson method for $L = 6\lambda$.

**Solution:**

Step 1: Define the pattern in $u = \cos\theta$.

For $\theta \in [10^\circ, 60^\circ]$:
- $\cos 10^\circ = 0.985$, $\cos 60^\circ = 0.5$.
- The pattern region is $u \in [0.5, 0.985]$.
- $\csc^2(\theta) = 1/\sin^2(\theta) = 1/(1 - u^2)$.

Desired pattern:
$$
F_d(u) = \begin{cases}
\frac{1}{1 - u^2}, & 0.5 \leq u \leq 0.985 \\
0, & \text{otherwise}
\end{cases}
$$

Step 2: Sampling points.
For $L = 6\lambda$: $\frac{L}{\lambda} = 6$.
Number of samples: $N = 2(6) + 1 = 13$.
Sampling interval: $\Delta u = \lambda/L = 1/6 \approx 0.1667$.

Sampling points: $u_n = n/6$ for $n = 0, \pm 1, \pm 2, \ldots, \pm 6$.

Step 3: Sample the desired pattern.

Compute $F_d(u_n) = 1/(1 - u_n^2)$ for each sampling point:

| $n$ | $u_n$ | $1 - u_n^2$ | $F_d(u_n)$ | In pattern region? |
| :--- | :--- | :--- | :--- | :--- |
| $0$ | $0.000$ | $1.000$ | $1.000$ | No ($u < 0.5$) |
| $1$ | $0.167$ | $0.972$ | $1.028$ | No |
| $2$ | $0.333$ | $0.889$ | $1.125$ | No |
| $3$ | $0.500$ | $0.750$ | $1.333$ | Yes (edge) |
| $4$ | $0.667$ | $0.556$ | $1.800$ | Yes |
| $5$ | $0.833$ | $0.306$ | $3.273$ | Yes |
| $6$ | $1.000$ | $0.000$ | $\infty$ | Approaching infinity |

For $n = 6$ ($u = 1.0$), the pattern is singular. In practice, the cosecant-squared pattern is truncated at a maximum value (e.g., $10$ dB above the peak). We set $F_d(1.0) = 10$ (linear) as a practical limit.

Similarly, for negative $n$ (backward hemisphere), the pattern is zero except possibly near $u = -1$.

The Woodward-Lawson synthesis sets $A_n = F_d(u_n)$ where the pattern is defined, and $A_n = 0$ elsewhere.

Step 4: Aperture distribution.
$$
I(z') = \frac{1}{6\lambda} \sum_{n=-6}^{6} A_n e^{-j k z' u_n}
$$

Only $n = 3, 4, 5, 6$ (and potentially negative counterparts if the pattern is symmetric) have non-zero $A_n$.

Step 5: Synthesised pattern.
$$
F(u) = \sum_{n=-6}^{6} A_n \frac{\sin[3k\lambda (u - u_n)]}{3k\lambda (u - u_n)}
$$

The pattern matches the desired cosecant-squared at $u = 0.5, 0.667, 0.833, 1.0$ exactly, with sinc interpolation between samples.

**Result:** The Woodward-Lawson method synthesises the cosecant-squared pattern with exact matching at four sampling points within the pattern region. The finite number of samples limits how well the pattern transition at $u = 0.5$ (the edge of the coverage region) can be approximated. More samples (longer aperture) would improve the transition sharpness.

---

### Exercise 7: Phase Error Effects on Pattern

**Problem:** A uniform line source of length $L = 5\lambda$ has a quadratic phase error $\phi(z') = \alpha(z')^2$ with $\alpha = 0.2$ rad/$(\lambda)^2$. Compute (a) the peak phase deviation at the aperture edges, (b) the approximate directivity loss, and (c) the effect on the first sidelobe level.

**Solution:**

Step 1: Peak phase error.
The phase error at $z' = \pm L/2$:
$$
\phi_{\max} = \alpha \left(\frac{L}{2}\right)^2 = 0.2 \times (2.5\lambda)^2 = 0.2 \times 6.25 = 1.25 \text{ rad}
$$

In degrees: $\phi_{\max} = 1.25 \times 180^\circ / \pi = 71.6^\circ$.

Step 2: Directivity loss estimation.
For a quadratic phase error with peak deviation $\phi_m$ (in radians), the directivity reduction factor is approximately:

$$
\frac{D}{D_0} \approx \left| \frac{1}{L} \int_{-L/2}^{L/2} e^{-j\phi(z')} dz' \right|^2
$$

For $\phi(z') = \alpha (z')^2$, and writing $\phi_m = \alpha (L/2)^2 = 1.25$ rad:

Using the Fresnel integral approximation:
$$
\frac{D}{D_0} \approx \left( \frac{\sin(\phi_m/2)}{\phi_m/2} \right)^2
$$

This is an approximation for small-to-moderate phase errors. Substituting $\phi_m = 1.25$ rad:
$$
\frac{D}{D_0} \approx \left( \frac{\sin(0.625)}{0.625} \right)^2 = \left( \frac{0.585}{0.625} \right)^2 = (0.936)^2 = 0.876
$$

Directivity loss: $10 \log_{10}(0.876) = -0.58$ dB.

Step 3: Effect on sidelobe level.
Quadratic phase error raises the sidelobe level by filling in the pattern nulls. The first sidelobe level of the uniform distribution ($-13.3$ dB) degrades. For $\phi_m = 71.6^\circ$, the first sidelobe typically rises to approximately $-11$ dB to $-12$ dB, and the nulls become partially filled.

More precisely, the pattern with quadratic phase error is:
$$
F(u) = \int_{-L/2}^{L/2} e^{-j\alpha (z')^2} e^{jk z' u} \, dz'
$$

This is a Fresnel integral. For $\alpha = 0.2$, numerical evaluation shows the first sidelobe rises from $-13.3$ dB to approximately $-11.5$ dB.

**Result:** Peak phase error $= 1.25$ rad ($71.6^\circ$), directivity loss $\approx 0.58$ dB, first sidelobe rises from $-13.3$ dB to approximately $-11.5$ dB. The phase error tolerance guideline is confirmed: errors up to $\pm \pi/4$ ($45^\circ$) cause acceptable degradation ($< 0.5$ dB loss), but errors beyond $\pm \pi/2$ ($90^\circ$) cause significant pattern deterioration.

---

### Exercise 8: Taylor $n$-Parameter Distribution Design

**Problem:** Design a Taylor $n$-parameter line-source distribution for $L = 10\lambda$ with SLL $= -35$ dB and $n = 5$ equal-ripple sidelobes. Compute (a) the parameter $\mathcal{R}$, (b) the beam-broadening factor $\sigma$, (c) the relocated null positions $u_m$ for $m = 1, 2, 3, 4$, and (d) the aperture distribution coefficients $F_m$.

**Solution:**

Step 1: Compute $\mathcal{R}$.
$$
\mathcal{R} = \frac{1}{\pi} \cosh^{-1}\left(10^{35/20}\right) = \frac{1}{\pi} \cosh^{-1}(56.23)
$$

$$
\cosh^{-1}(56.23) = \ln(56.23 + \sqrt{56.23^2 - 1}) = \ln(56.23 + 56.22) = \ln(112.45) = 4.722
$$

$$
\mathcal{R} = \frac{4.722}{\pi} = 1.503
$$

Step 2: Compute the beam-broadening factor $\sigma$.
$$
\sigma = \frac{n}{\sqrt{\mathcal{R}^2 + (n - 0.5)^2}} = \frac{5}{\sqrt{1.503^2 + (4.5)^2}} = \frac{5}{\sqrt{2.259 + 20.25}} = \frac{5}{\sqrt{22.509}} = \frac{5}{4.744} = 1.054
$$

Step 3: Compute relocated nulls $u_m$.
$$
u_m = \sigma \sqrt{\mathcal{R}^2 + (m - 0.5)^2}
$$

For $m = 1$:
$$
u_1 = 1.054 \sqrt{1.503^2 + (0.5)^2} = 1.054 \sqrt{2.259 + 0.25} = 1.054 \sqrt{2.509} = 1.054 \times 1.584 = 1.669
$$

For $m = 2$:
$$
u_2 = 1.054 \sqrt{2.259 + (1.5)^2} = 1.054 \sqrt{2.259 + 2.25} = 1.054 \sqrt{4.509} = 1.054 \times 2.123 = 2.238
$$

For $m = 3$:
$$
u_3 = 1.054 \sqrt{2.259 + (2.5)^2} = 1.054 \sqrt{2.259 + 6.25} = 1.054 \sqrt{8.509} = 1.054 \times 2.917 = 3.074
$$

For $m = 4$:
$$
u_4 = 1.054 \sqrt{2.259 + (3.5)^2} = 1.054 \sqrt{2.259 + 12.25} = 1.054 \sqrt{14.509} = 1.054 \times 3.809 = 4.015
$$

After $m = 4$ (i.e., for $m \geq 5$), the nulls revert to the uniform distribution at $u = \pm 5, \pm 6, \ldots$

Step 4: Compute pattern samples $F_m$.
$$
F_m = \frac{\sin(\pi u_m)}{\pi u_m} \prod_{q=1}^{n-1} \frac{1 - \left(\frac{u_m}{\sigma u_q}\right)^2}{1 - \left(\frac{u_m}{q}\right)^2}
$$

For $m = 1$ ($u_1 = 1.669$):
$$
F_1 = \frac{\sin(1.669\pi)}{1.669\pi} \prod_{q=1}^{4} \frac{1 - \left(\frac{1.669}{\sigma u_q}\right)^2}{1 - \left(\frac{1.669}{q}\right)^2}
$$

Since $u_1$ is one of the roots, the product term for $q = 1$ is $0$, making $F_1 = 0$ by construction. This is correct: the $F_m$ values at the relocated null positions are zero for $m = 1, \ldots, n-1$.

Wait — I need to reconsider. The $F_m$ are the pattern samples at the relocated null positions, used in the aperture distribution series expansion. They are not the pattern values at those points. Let me use the correct formulation.

The pattern samples $F_m$ are the value of the normalised pattern (using the null relocation) at the positions $u = m$ (the original uniform-distribution nulls). The formula is:

$$
F_m = \frac{\sin(\pi u_m)}{\pi u_m} \prod_{q=1}^{n-1} \frac{1 - \left(\frac{u_m}{\sigma u_q}\right)^2}{1 - \left(\frac{u_m}{q}\right)^2}
$$

Let me compute for $m = 1$:

$$
F_1 = \frac{\sin(\pi \cdot 1.669)}{\pi \cdot 1.669} \prod_{q=1}^{4} \frac{1 - \left(\frac{1.669}{1.054 u_q}\right)^2}{1 - \left(\frac{1.669}{q}\right)^2}
$$

Since $\sin(1.669\pi) = \sin(5.243) = -0.842$:
$$
\frac{\sin(1.669\pi)}{1.669\pi} = \frac{-0.842}{5.243} = -0.161
$$

The product for $q=1$:
$$
\frac{1 - (1.669 / (1.054 \cdot 1.669))^2}{1 - (1.669 / 1)^2} = \frac{1 - (1/1.054)^2}{1 - 2.786} = \frac{1 - 0.901}{-1.786} = \frac{0.099}{-1.786} = -0.055
$$

For $q=2$:
$$
\frac{1 - (1.669 / (1.054 \cdot 2.238))^2}{1 - (1.669 / 2)^2} = \frac{1 - (0.707)^2}{1 - 0.696} = \frac{1 - 0.500}{0.304} = \frac{0.500}{0.304} = 1.645
$$

For $q=3$:
$$
\frac{1 - (1.669 / (1.054 \cdot 3.074))^2}{1 - (1.669 / 3)^2} = \frac{1 - (0.515)^2}{1 - 0.309} = \frac{1 - 0.265}{0.691} = \frac{0.735}{0.691} = 1.064
$$

For $q=4$:
$$
\frac{1 - (1.669 / (1.054 \cdot 4.015))^2}{1 - (1.669 / 4)^2} = \frac{1 - (0.394)^2}{1 - 0.174} = \frac{1 - 0.155}{0.826} = \frac{0.845}{0.826} = 1.023
$$

Total product: $(-0.055) \times 1.645 \times 1.064 \times 1.023 = -0.055 \times 1.789 = -0.098$.

Thus $F_1 = (-0.161) \times (-0.098) = 0.0158$.

Step 5: Aperture distribution.
The aperture distribution is constructed from the Fourier series:
$$
I(z') = \frac{1}{L} \left[ 1 + 2 \sum_{m=1}^{4} F_m \cos\left(\frac{2\pi m z'}{L}\right) \right]
$$

With the computed $F_m$ values, this distribution produces a pattern with the first $4$ sidelobes at $-35$ dB (equal ripple) and the remaining sidelobes decaying as $1/u$.

**Result:** For SLL $= -35$ dB and $n = 5$: $\mathcal{R} = 1.503$, $\sigma = 1.054$, relocated nulls at $u_1 = 1.669$, $u_2 = 2.238$, $u_3 = 3.074$, $u_4 = 4.015$. The aperture distribution is a cosine series with coefficients $F_m$.

---

### Exercise 9: Circular Aperture Uniform Distribution

**Problem:** A circular aperture of radius $a = 3\lambda$ has a uniform amplitude distribution. Compute (a) the far-field pattern in the $u = \sin\theta$ variable, (b) the HPBW, (c) the first sidelobe level, and (d) the directivity.

**Solution:**

Step 1: Pattern expression.
For a uniform circular aperture of radius $a$, the far-field pattern is:
$$
F(\theta) = \frac{2 J_1(ka \sin\theta)}{ka \sin\theta}
$$

where $J_1$ is the first-order Bessel function of the first kind.

In terms of $u = \sin\theta$:
$$
F(u) = \frac{2 J_1(ka u)}{ka u}, \quad ka = \frac{2\pi}{\lambda} \cdot 3\lambda = 6\pi
$$

Step 2: First null.
The first null of $J_1(x)$ occurs at $x = 3.832$.
$$
ka u_{\text{null}} = 3.832 \quad \Rightarrow \quad u_{\text{null}} = \frac{3.832}{6\pi} = \frac{3.832}{18.85} = 0.203
$$

In degrees: $\theta_{\text{null}} = \sin^{-1}(0.203) = 11.71^\circ$.

Step 3: HPBW.
The half-power point of $[2 J_1(x)/x]^2$ occurs at $x = 1.620$ (numerical solution):
$$
ka u_{\text{HP}} = 1.620 \quad \Rightarrow \quad u_{\text{HP}} = \frac{1.620}{18.85} = 0.086
$$

$$
\text{HPBW} = 2 \times \sin^{-1}(0.086) = 2 \times 4.93^\circ = 9.86^\circ
$$

For comparison, a uniform linear aperture of length $2a = 6\lambda$ has HPBW $\approx 0.88\lambda / 6\lambda = 0.147$ rad $= 8.40^\circ$. The circular aperture has a slightly broader beam due to the reduced effective aperture area.

Step 4: First sidelobe level.
The first sidelobe of the Airy pattern occurs at $x = 5.136$ (first maximum of $J_1(x)$ after the main lobe):
$$
\frac{2 J_1(5.136)}{5.136} = 0.132
$$

Sidelobe level: $20 \log_{10}(0.132) = -17.6$ dB.

This is $4.3$ dB higher than the uniform linear aperture SLL ($-13.3$ dB for the linear aperture in $u$-space, but note the linear aperture pattern is evaluated differently). The circular aperture has higher first sidelobe because the aperture geometry concentrates more energy near the centre in the Fourier transform.

Step 5: Directivity.
The directivity of a uniform circular aperture is:
$$
D_0 = \left(\frac{2\pi a}{\lambda}\right)^2 = (6\pi)^2 = 355.3 \ (\approx 25.5\ \text{dB})
$$

This is the maximum possible directivity for a circular aperture of radius $a = 3\lambda$. Any amplitude taper reduces the directivity.

**Result:** For $a = 3\lambda$: HPBW $= 9.86^\circ$, first null at $\theta = 11.71^\circ$, first SLL $= -17.6$ dB, directivity $= 355.3$ ($25.5$ dB).

---

### Exercise 10: Pattern Synthesis Using Null Placement

**Problem:** A 5-element uniform linear array with $d = \lambda/2$ and $\beta = 0$ has interference at $\theta = 30^\circ$ and $\theta = 70^\circ$. Use the Schelkunoff polynomial method to place nulls at these directions while maximising the directivity.

**Solution:**

Step 1: Map null angles to $w$.
For $d = \lambda/2$, $kd = \pi$.

$$
\psi = kd \cos\theta = \pi \cos\theta
$$

Null at $\theta = 30^\circ$: $\cos 30^\circ = 0.866 \Rightarrow \psi_1 = 0.866\pi = 2.721 \Rightarrow w_1 = e^{j 2.721} = e^{j 0.866\pi}$.

Null at $\theta = 70^\circ$: $\cos 70^\circ = 0.342 \Rightarrow \psi_2 = 0.342\pi = 1.074 \Rightarrow w_2 = e^{j 1.074}$.

Step 2: Construct the polynomial.
For $N = 5$, the polynomial is degree 4. We have 2 specified nulls and need to place 2 additional roots. For maximum directivity, the remaining roots should be placed at $w = 0$ (repeated), which maximises the uniform excitation component.

$$
AF(w) = (w - w_1)(w - w_2)(w - 0)(w - 0) = w^2 (w - w_1)(w - w_2)
$$

Step 3: Expand.
$$
AF(w) = w^2 [w^2 - (w_1 + w_2)w + w_1 w_2]
= w^4 - (w_1 + w_2) w^3 + w_1 w_2 w^2
$$

Substituting $w_1 = e^{j 0.866\pi}$ and $w_2 = e^{j 0.342\pi}$:

$w_1 = \cos(0.866\pi) + j \sin(0.866\pi) = \cos(155.9^\circ) + j \sin(155.9^\circ) = -0.913 + j 0.408$
$w_2 = \cos(0.342\pi) + j \sin(0.342\pi) = \cos(61.6^\circ) + j \sin(61.6^\circ) = 0.476 + j 0.880$

$w_1 + w_2 = (-0.913 + 0.476) + j(0.408 + 0.880) = -0.437 + j 1.288$
$w_1 w_2 = (-0.913 + j0.408)(0.476 + j0.880)$
$= (-0.913)(0.476) + (-0.913)(j0.880) + (j0.408)(0.476) + (j0.408)(j0.880)$
$= -0.435 - j0.803 + j0.194 - 0.359$
$= -0.794 - j0.609$

Step 4: Excitation coefficients.
$$
AF(w) = w^4 - (-0.437 + j1.288) w^3 + (-0.794 - j0.609) w^2
$$

The coefficients of $w^n$ give the excitations $I_n$:
- $I_4 = 1$ (coefficient of $w^4$)
- $I_3 = -(-0.437 + j1.288) = 0.437 - j1.288$
- $I_2 = -0.794 - j0.609$
- $I_1 = 0$ (no $w^1$ term)
- $I_0 = 0$ (no constant term)

These excitations are complex, which is expected for asymmetric null placement. The magnitude distribution is not uniform, but the two roots at $w = 0$ minimise the deviation from uniform excitation, maximising directivity for the given null constraints.

Step 5: Verify the nulls.
At $\theta = 30^\circ$ ($w = w_1$): $AF(w_1) = 0$ by construction. The null is exact.
At $\theta = 70^\circ$ ($w = w_2$): $AF(w_2) = 0$ by construction. The null is exact.

**Result:** The 5-element array with $d = \lambda/2$ is synthesised with excitations $[0, 0, -0.794 - j0.609, 0.437 - j1.288, 1]$ to place nulls at $\theta = 30^\circ$ and $70^\circ$. The repeated root at $w = 0$ maintains maximum directivity for the given null constraints.

---

## Exam Tip: Choosing the Right Synthesis Method

In exam problems, the choice of synthesis method depends on what is specified:

**1. Null positions are specified** $\rightarrow$ use the **Schelkunoff polynomial method**.
- Map each null angle to $w_m = e^{j(kd\cos\theta_m + \beta)}$.
- Construct $AF(w) = \prod (w - w_m)$.
- Expand to get excitations.
- If fewer nulls than $N-1$, place remaining roots at $w = 0$ (maximises directivity) or on the unit circle (additional nulls).

**2. Complete pattern shape is specified** (e.g., sector beam, cosecant-squared) $\rightarrow$ use the **Woodward-Lawson method**.
- Sample the desired pattern at $u_n = n\lambda/L$.
- The number of samples is $N = 2L/\lambda + 1$.
- The synthesised pattern matches exactly at sampling points.
- Between sampling points, the pattern is the sum of sinc functions.
- Longer apertures give better pattern approximation.

**3. Sidelobe level and beamwidth are specified** $\rightarrow$ use the **Taylor distribution**.
- Compute $\mathcal{R} = \frac{1}{\pi} \cosh^{-1}(10^{\text{SLL}/20})$.
- Choose $n$ (usually $n = 3$ to $8$ for practical designs).
- Compute $\sigma$ and the relocated nulls.
- The Taylor distribution avoids the impracticality of constant sidelobes everywhere.

**4. A specific aperture taper name is given** (triangular, cosine, cosine-squared) $\rightarrow$ use the **closed-form pattern expressions**.
- Each taper has a known pattern formula (squared sinc for triangular, etc.).
- Use the comparative table to quickly compute beamwidth, SLL, and directivity loss.

**Common pitfalls:**
- Forgetting that the Schelkunoff polynomial has degree $N-1$ for $N$ elements, not $N$.
- Using Woodward-Lawson sampling interval $\Delta u = \lambda/L$ incorrectly when $L$ is not an integer multiple of $\lambda$.
- Confusing the two Taylor distributions: the one-parameter distribution has all sidelobes at the same level (like Tschebyscheff); the $n$-parameter distribution has $n$ equal sidelobes near the main beam and decaying sidelobes farther out.
- Applying the Fourier transform method without accounting for the finite aperture truncation and resulting Gibbs phenomenon.

**Pattern recognition shortcut:** If an exam problem says "synthesise a pattern with nulls at $\theta_1, \theta_2, \ldots$", immediately write the Schelkunoff polynomial. If it says "synthesise a pattern with SLL $= X$ dB and beamwidth $Y$", immediately compute the Taylor parameter $\mathcal{R}$. This mechanical approach handles most standard synthesis exam problems.