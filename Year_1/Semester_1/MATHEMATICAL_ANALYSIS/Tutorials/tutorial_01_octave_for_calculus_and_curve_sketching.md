# Tutorial 01: Curve Sketching and Calculus Computations in GNU Octave

## Context and Grounding
This tutorial provides a practical laboratory walkthrough for visualizing functions, tracing derivatives, determining roots, and evaluating numerical integrals using GNU Octave.

---

## 1. Defining Mathematical Functions in Octave

### 1.1 Anonymous Function Handles
The idiomatic method for defining real-valued functions in Octave is via anonymous function handles with vectorized operators:
```matlab
% Define f(x) = (x^3 - 3*x) / (x^2 + 1)
% Crucial: Use element-wise operators (.*, ./, .^) so f accepts vector inputs
f = @(x) (x.^3 - 3.*x) ./ (x.^2 + 1);
```

### 1.2 Evaluating Across Discrete Domains
```matlab
% Create a uniform evaluation grid from -5 to +5 with step 0.01
x_vals = -5:0.01:5;
y_vals = f(x_vals);
```

---

## 2. Comprehensive 2D Curve Sketching

Save the following script as `curve_sketch.m`:

```matlab
clear; clc; close all;

% Target function: f(x) = x * exp(-x^2 / 2)
f = @(x) x .* exp(-x.^2 ./ 2);

% Analytical first derivative: f'(x) = (1 - x^2) * exp(-x^2 / 2)
df = @(x) (1 - x.^2) .* exp(-x.^2 ./ 2);

% Domain grid
x = -4:0.01:4;
y = f(x);
dy = df(x);

figure('Name', 'Calculus Curve Analysis');

% Subplot 1: Function Curve and Extrema
subplot(2, 1, 1);
plot(x, y, 'b-', 'LineWidth', 2);
hold on; grid on;

% Critical points occur where f'(x) = 0 => x = -1 (local min) and x = +1 (local max)
plot(-1, f(-1), 'ro', 'MarkerSize', 8, 'MarkerFaceColor', 'r');
plot(1, f(1), 'go', 'MarkerSize', 8, 'MarkerFaceColor', 'g');

title('Function f(x) = x \cdot e^{-x^2 / 2}');
xlabel('x'); ylabel('f(x)');
legend('f(x)', 'Local Min (-1, -0.607)', 'Local Max (1, +0.607)', 'Location', 'northeast');

% Subplot 2: Derivative Curve
subplot(2, 1, 2);
plot(x, dy, 'r--', 'LineWidth', 1.5);
hold on; grid on;
plot([-4, 4], [0, 0], 'k:'); % Zero reference axis

title("First Derivative f'(x)");
xlabel('x'); ylabel("f'(x)");
legend("f'(x)", 'Zero Slope Axis');
```

Execute in terminal:
```bash
octave curve_sketch.m
```

---

## 3. Numerical Integration in GNU Octave

Octave provides high-precision adaptive Gauss-Lobatto quadrature routines via `integral` and `quad`:

### 3.1 Evaluating Definite Integrals
To evaluate:
$$\int_0^{\pi} x \sin(x) \, dx = [\sin x - x \cos x]_0^\pi = \pi \approx 3.14159265$$

In Octave:
```matlab
% Define integrand
integrand = @(x) x .* sin(x);

% Compute definite integral over [0, pi]
[result, err_est] = integral(integrand, 0, pi);

fprintf("Computed Integral: %.8f\n", result);
fprintf("Analytical Value:  %.8f\n", pi);
fprintf("Absolute Error:    %e\n", abs(result - pi));
```

---

## 4. Root Finding: Newton-Raphson Method
Find roots of $g(x) = x^3 - 2x - 5 = 0$ using `fzero`:
```matlab
g = @(x) x.^3 - 2.*x - 5;
root_val = fzero(g, 2.0); % Initial guess = 2.0
fprintf("Found root: %.6f\n", root_val); % 2.094551
```

