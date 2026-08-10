## 1. Function Plotting

**Problem/Function:** Plot the sinusoidal wave, $$y = \sin(x)$$, for values of $$x$$ from -10 to 10. This example appears in the presentation for basic functions (Functions (Part A)).

**MATLAB/Octave Code:**
```matlab
x = [-10:0.1:10];
y = sin(x);
plot(x,y)
title("y=sin(x)")
xlabel("x")
ylabel("y(x)")
```

**Output:**
```
[Sinusoidal wave graph]
```

**Problem/Function:** Plot the function $$y = x^2 - 4x + 3$$ for values of $$x$$ from -2 to 6.

**MATLAB/Octave Code:**
```matlab
x = [-2:0.1:6];
y = x.^2 - 4*x + 3;
plot(x,y)
grid on
title("y = x^2 - 4x + 3")
xlabel("x")
ylabel("y(x)")
```

**Output:**
```
[Parabola graph with grid]
```

**Problem/Function:** Plot two functions on the same graph: $$y_1 = e^x$$ and $$y_2 = e^{-x}$$ for $$x$$ from -3 to 3.

**MATLAB/Octave Code:**
```matlab
x = [-3:0.1:3];
y1 = exp(x);
y2 = exp(-x);
plot(x,y1,'r-',x,y2,'b--')
legend('e^x','e^{-x}')
title("Exponential functions")
xlabel("x")
ylabel("y(x)")
```

**Output:**
```
[Graph with two exponential functions - red solid and blue dashed line]
```

## 2. Derivative

**Problem/Function:** Find the derivative of the function $$f(x) = 2\sin(x) + 3x^5$$. This example comes from the Derivative of a Function presentation.

**MATLAB/Octave Code:**
```matlab
pkg load symbolic
syms x
y = 2*sin(x) + 3*x^5
Dy = diff(y)
```

**Output:**
```
y = (sym)
    5
  3*x + 2*sin(x)

Dy = (sym)
    4
  15*x + 2*cos(x)
```

**Problem/Function:** Find the 3rd derivative of $$f(x) = 2\sin(x) + 3x^5$$ and then evaluate the result at $$x = π$$.

**MATLAB/Octave Code:**
```matlab
pkg load symbolic
syms x
y = 2*sin(x)+3*x^5;
D3y = diff(y,3,x)
D3y2 = subs(D3y,pi)
```

**Output:**
```
D3y = (sym)
      / 2      \
  2*|90*x - cos(x)|

D3y2 = (sym)
    2
  2 + 180*pi
```

**Problem/Function:** Find the derivative of the composite function $$f(x) = (3x^2 + 5)^9$$.

**MATLAB/Octave Code:**
```matlab
pkg load symbolic
syms x
y = (3*x^2+5)^9
Dy = diff(y)
```

**Output:**
```
y = (sym)
    / 2    \9
  |3*x + 5|

Dy = (sym)
          / 2    \8
  54*x*|3*x + 5|
```

**Problem/Function:** Find the derivative of $$f(x) = \ln(x^2 + 1) + \arctan(x)$$.

**MATLAB/Octave Code:**
```matlab
pkg load symbolic
syms x
y = log(x^2+1) + atan(x)
Dy = diff(y)
```

**Output:**
```
y = (sym)
  log(x^2 + 1) + atan(x)

Dy = (sym)
        2*x       1
     --------- + -----
      2          2
     x + 1      x + 1
```

## 3. Limits of Functions

**Problem/Function:** Compute the limit of the function $$f(x) = \frac{4x^2 - 9x + 1}{x + 7}$$ as $$x$$ approaches 3.

**MATLAB/Octave Code:**
```matlab
pkg load symbolic
syms x
y = (4*x^2-9*x+1)/(x+7);
limit(y,3)
```

**Output:**
```
ans = (sym) 1
```

**Problem/Function:** Compute the limit of $$f(x) = \frac{5}{x^3 + 8}$$ as $$x$$ approaches infinity.

**MATLAB/Octave Code:**
```matlab
pkg load symbolic
syms x
y1 = 5/(x^3+8);
limit(y1,inf)
```

**Output:**
```
ans = (sym) 0
```

**Problem/Function:** Compute the one-sided limit of $$f(x) = \frac{1}{x}$$ as $$x$$ approaches 0 from the right.

**MATLAB/Octave Code:**
```matlab
pkg load symbolic
syms x
f = 1/x;
limit(f,x,0,'right')
```

**Output:**
```
ans = Inf
```

**Problem/Function:** Compute the one-sided limit of $$f(x) = \frac{1}{x}$$ as $$x$$ approaches 0 from the left.

**MATLAB/Octave Code:**
```matlab
pkg load symbolic
syms x
f = 1/x;
limit(f,x,0,'left')
```

**Output:**
```
ans = -Inf
```

**Problem/Function:** Compute the limit of $$f(x) = \frac{\sin(x)}{x}$$ as $$x$$ approaches 0.

**MATLAB/Octave Code:**
```matlab
pkg load symbolic
syms x
f = sin(x)/x;
limit(f,x,0)
```

**Output:**
```
ans = (sym) 1
```

**Problem/Function:** Compute the limit of $$f(x) = \frac{x^2 - 4}{x - 2}$$ as $$x$$ approaches 2.

**MATLAB/Octave Code:**
```matlab
pkg load symbolic
syms x
f = (x^2-4)/(x-2);
limit(f,x,2)
```

**Output:**
```
ans = (sym) 4
```

## 4. Integral Calculus

**Problem/Function:** Compute the indefinite integral of $$f(x) = x^3 - x \cdot e^x$$.

**MATLAB/Octave Code:**
```matlab
pkg load symbolic
syms x
y = x^3 - x*exp(x)
int(y,x)
```

**Output:**
```
y = (sym)
    3        x
  x - x*e

ans = (sym)
    4
  x       x
  -- + (1 - x)*e
  4
```

**Problem/Function:** Compute the definite integral of $$f(x) = \frac{x+1}{\sqrt{x}}$$ from $$x=1$$ to $$x=4$$.

**MATLAB/Octave Code:**
```matlab
pkg load symbolic
syms x
int((x+1)/sqrt(x),1,4)
```

**Output:**
```
ans = (sym) 20/3
```

**Problem/Function:** Compute the indefinite integral of $$f(x) = \cos(2x) + 3x^2$$.

**MATLAB/Octave Code:**
```matlab
pkg load symbolic
syms x
y = cos(2*x) + 3*x^2;
int(y,x)
```

**Output:**
```
ans = (sym)
    3
   x + sin(2*x)/2
```

**Problem/Function:** Compute the definite integral of $$f(x) = e^{-x^2}$$ from $$x=0$$ to $$x=1$$.

**MATLAB/Octave Code:**
```matlab
pkg load symbolic
syms x
int(exp(-x^2),0,1)
```

**Output:**
```
ans = (sym)
  sqrt(pi)*erf(1)/2
```

## 5. Complex Numbers

**Problem:** Demonstrate basic arithmetic operations (addition, multiplication, division) with the complex numbers $$z = 3 + 2i$$ and $$w = 5 - 4i$$.

**MATLAB/Octave Code:**
```matlab
z = 3+2*i
w = 5-4*i
z+w
z*w
z/w
```

**Output:**
```
z = 3 + 2i
w = 5 - 4i
ans = 8 - 2i
ans = 23 - 2i
ans = 0.17073 + 0.53659i
```

**Problem:** Find the roots of the polynomial $$x^3 - 3x^2 + 5x - 3$$.

**MATLAB/Octave Code:**
```matlab
c = [1,-3,5,-3]
roots(c)
```

**Output:**
```
c = 1 -3 5 -3
ans =
 1.0000 + 1.4142i
 1.0000 - 1.4142i
 1.0000 + 0.0000i
```

**Problem:** Compute the modulus and argument of the complex number $$z = 4 + 3i$$.

**MATLAB/Octave Code:**
```matlab
z = 4+3*i;
abs(z)
angle(z)
```

**Output:**
```
ans = 5
ans = 0.64350
```

**Problem:** Convert the complex number from polar to Cartesian form: $$r = 5$$, $$θ = π/4$$.

**MATLAB/Octave Code:**
```matlab
r = 5;
theta = pi/4;
z = r * exp(1i * theta)
```

**Output:**
```
z = 3.5355 + 3.5355i
```

**Problem:** Compute the power $$(1 + i)^8$$.

**MATLAB/Octave Code:**
```matlab
z = 1+1*i;
z^8
```

**Output:**
```
ans = 16 + 0i
```