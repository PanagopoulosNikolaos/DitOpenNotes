# Phase 5.8: Distributions of Functions of Multiple Random Variables

This file details the techniques for finding the probability distribution of a new random variable $Z$ which is defined as a function of multiple random variables, $Z = g(X, Y)$.

---

## 1. The CDF Method (First Principles)

Like the single-variable case, the CDF method is highly reliable and works by finding the region of the joint PDF that satisfies the inequality $g(X, Y) \le z$.

$$F_Z(z) = P(g(X, Y) \le z) = \iint_{g(x,y) \le z} f(x, y) \, dx \, dy$$

Once $F_Z(z)$ is found, the PDF is obtained by differentiating: $f_Z(z) = F'_Z(z)$.

---

## 2. Convolution (Sum of Independent Variables)

If $X$ and $Y$ are independent, the distribution of their sum $Z = X + Y$ is called the **convolution** of their individual distributions.

*   **Discrete Case:**
    $$p_Z(z) = P(X + Y = z) = \sum_{x} p_X(x) \cdot p_Y(z - x)$$
*   **Continuous Case:**
    $$f_Z(z) = \int_{-\infty}^{\infty} f_X(x) \cdot f_Y(z - x) \, dx$$

---

## 3. The bivariate Change of Variables (Jacobian Method)

If we have two random variables $X_1, X_2$ with joint PDF $f_{X_1, X_2}(x_1, x_2)$, and we define two new variables:
$$Y_1 = g_1(X_1, X_2) \quad \text{and} \quad Y_2 = g_2(X_1, X_2)$$

If this transformation is a one-to-one (bijective) mapping, we can solve for $X_1$ and $X_2$ in terms of $Y_1, Y_2$:
$$X_1 = h_1(Y_1, Y_2) \quad \text{and} \quad X_2 = h_2(Y_1, Y_2)$$

The joint PDF of $Y_1$ and $Y_2$ is:
$$f_{Y_1, Y_2}(y_1, y_2) = f_{X_1, X_2}(h_1(y_1, y_2), h_2(y_1, y_2)) \cdot |J|$$

where $J$ is the Jacobian determinant of the inverse transformation:
$$J = \det \begin{pmatrix} \frac{\partial x_1}{\partial y_1} & \frac{\partial x_1}{\partial y_2} \\ \frac{\partial x_2}{\partial y_1} & \frac{\partial x_2}{\partial y_2} \end{pmatrix} = \frac{\partial x_1}{\partial y_1} \frac{\partial x_2}{\partial y_2} - \frac{\partial x_1}{\partial y_2} \frac{\partial x_2}{\partial y_1}$$

> **Exam Shortcut:** If you only want the distribution of a single function $Y_1 = g_1(X_1, X_2)$, you can define a dummy variable (e.g., $Y_2 = X_1$ or $Y_2 = X_2$), apply the 2D Jacobian method to find $f_{Y_1, Y_2}(y_1, y_2)$, and then integrate out $Y_2$ to find the marginal PDF $f_{Y_1}(y_1)$.

---

## 4. Order Statistics: Min and Max of Independent Variables

Let $X_1, X_2, \dots, X_n$ be independent, identically distributed (i.i.d.) random variables with CDF $F_X(x)$ and PDF $f_X(x)$.

### 4.1 Distribution of the Maximum ($Y_{max} = \max(X_1, \dots, X_n)$)
For the maximum to be less than $y$, **all** individual variables must be less than $y$:
$$F_{Y_{max}}(y) = P(X_1 \le y, \dots, X_n \le y) = [F_X(y)]^n$$
Differentiating gives the PDF:
$$f_{Y_{max}}(y) = n \cdot [F_X(y)]^{n-1} \cdot f_X(y)$$

### 4.2 Distribution of the Minimum ($Y_{min} = \min(X_1, \dots, X_n)$)
For the minimum to be greater than $y$, **all** individual variables must be greater than $y$:
$$P(Y_{min} > y) = P(X_1 > y, \dots, X_n > y) = [1 - F_X(y)]^n$$
$$F_{Y_{min}}(y) = 1 - [1 - F_X(y)]^n$$
Differentiating gives the PDF:
$$f_{Y_{min}}(y) = n \cdot [1 - F_X(y)]^{n-1} \cdot f_X(y)$$

---

## 5. Solved Exercises (9 Examples)

### Exercise 1: Sum of Two Independent Uniform Variables (Convolution)
**Problem:** Let $X \sim U(0, 1)$ and $Y \sim U(0, 1)$ be independent. Find the PDF of $Z = X + Y$.

**Solution:**
- **Step 1: Set up the convolution integral.**
  The PDFs are $f_X(x) = 1$ for $0 < x < 1$ and $f_Y(y) = 1$ for $0 < y < 1$.
  $$f_Z(z) = \int_{-\infty}^{\infty} f_X(x) f_Y(z-x) \, dx = \int_{0}^{1} 1 \cdot f_Y(z-x) \, dx$$
- **Step 2: WIP State.**
  The term $f_Y(z-x)$ is 1 only when $0 < z - x < 1 \implies z - 1 < x < z$.
  We split the analysis into two cases based on the value of $z \in (0, 2)$:
  - **Case 1: $0 < z \le 1$.**
    Here, the overlap region is $0 < x < z$.
    $$f_Z(z) = \int_{0}^{z} 1 \, dx = z$$
  - **Case 2: $1 < z < 2$.**
    Here, the overlap region is $z - 1 < x < 1$.
    $$f_Z(z) = \int_{z-1}^{1} 1 \, dx = 1 - (z-1) = ?$$
- **Step 3: Final Calculation.**
  - Case 2 value $= 2 - z$.
  - This results in a triangular PDF:
    $$f_Z(z) = \begin{cases} z, & 0 < z \le 1 \\ 2 - z, & 1 < z < 2 \\ 0, & \text{otherwise} \end{cases}$$

---

### Exercise 2: Ratio of Two Independent Exponentials (CDF Method)
**Problem:** Let $X \sim Exp(1)$ and $Y \sim Exp(1)$ be independent. Find the PDF of $Z = \frac{Y}{X}$.

**Solution:**
- **Step 1: Write down the CDF of $Z$ for $z > 0$.**
  $$F_Z(z) = P\left(\frac{Y}{X} \le z\right) = P(Y \le zX)$$
- **Step 2: WIP State.**
  Integrate over the region $y \le zx$ in the first quadrant:
  $$F_Z(z) = \int_{0}^{\infty} \int_{0}^{zx} e^{-x} e^{-y} \, dy \, dx = \int_{0}^{\infty} e^{-x} \left( 1 - e^{-zx} \right) \, dx$$
  $$F_Z(z) = \int_{0}^{\infty} \left( e^{-x} - e^{-(1+z)x} \right) \, dx = 1 - \frac{1}{?}$$
- **Step 3: Final Calculation.**
  - Integral of $e^{-(1+z)x}$ is $\frac{1}{1+z}$.
  - $F_Z(z) = 1 - \frac{1}{1+z} = \frac{z}{1+z}$.
  Differentiating with respect to $z$:
  $$f_Z(z) = \frac{d}{dz}\left(1 - (1+z)^{-1}\right) = (1+z)^{-2} = \frac{1}{(1+z)^2}, \quad z > 0.$$

---

### Exercise 3: Dummy Variable and 2D Jacobian Method
**Problem:** Let $X_1, X_2$ be independent random variables with joint PDF $f(x_1, x_2) = e^{-x_1 - x_2}$ for $x_1 > 0, x_2 > 0$. Find the joint PDF of $Y_1 = X_1 + X_2$ and $Y_2 = \frac{X_1}{X_2}$.

**Solution:**
- **Step 1: Solve for the inverse transformation.**
  We have:
  - $y_1 = x_1 + x_2$
  - $y_2 = \frac{x_1}{x_2} \implies x_1 = y_2 x_2$
  Substitute $x_1$ into $y_1$:
  $y_1 = y_2 x_2 + x_2 = x_2(1 + y_2) \implies x_2 = \frac{y_1}{1 + y_2}$.
  Then:
  $x_1 = \frac{y_1 y_2}{1 + y_2}$.
- **Step 2: WIP State for the Jacobian.**
  Compute partial derivatives:
  - $\frac{\partial x_1}{\partial y_1} = \frac{y_2}{1+y_2}$, $\frac{\partial x_1}{\partial y_2} = \frac{y_1(1+y_2) - y_1 y_2}{(1+y_2)^2} = \frac{y_1}{(1+y_2)^2}$
  - $\frac{\partial x_2}{\partial y_1} = \frac{1}{1+y_2}$, $\frac{\partial x_2}{\partial y_2} = -\frac{y_1}{(1+y_2)^2}$
  Determinant:
  $$J = \det \begin{pmatrix} \frac{y_2}{1+y_2} & \frac{y_1}{(1+y_2)^2} \\ \frac{1}{1+y_2} & -\frac{y_1}{(1+y_2)^2} \end{pmatrix} = \left(\frac{y_2}{1+y_2}\right)\left(-\frac{y_1}{(1+y_2)^2}\right) - \left(\frac{y_1}{(1+y_2)^2}\right)\left(\frac{1}{1+y_2}\right)$$
  $$J = \frac{-y_1 y_2 - y_1}{(1+y_2)^3} = \frac{-y_1(y_2 + 1)}{(1+y_2)^3} = -\frac{y_1}{?}$$
- **Step 3: Final Calculation.**
  - Denominator $= (1 + y_2)^2$.
  - $|J| = \frac{y_1}{(1+y_2)^2}$.
  Apply the transformation formula:
  $$f_{Y_1, Y_2}(y_1, y_2) = e^{-(x_1 + x_2)} \cdot |J| = e^{-y_1} \cdot \frac{y_1}{(1 + y_2)^2}, \quad y_1 > 0, y_2 > 0.$$

---

### Exercise 4: Marginal PDF from Joint Jacobian Result
**Problem:** Using the joint PDF of $Y_1, Y_2$ found in Exercise 3, find the marginal PDF of $Y_1$ and $Y_2$ to show they are independent.

**Solution:**
- **Step 1: Integrate out $y_2$ to find the marginal of $Y_1$.**
  $$f_{Y_1}(y_1) = \int_{0}^{\infty} y_1 e^{-y_1} \frac{1}{(1 + y_2)^2} \, dy_2 = y_1 e^{-y_1} \left[ -\frac{1}{1 + y_2} \right]_{0}^{\infty} = y_1 e^{-y_1}, \quad y_1 > 0$$
- **Step 2: WIP State.**
  Integrate out $y_1$ to find the marginal of $Y_2$:
  $$f_{Y_2}(y_2) = \int_{0}^{\infty} \frac{1}{(1 + y_2)^2} y_1 e^{-y_1} \, dy_1 = \frac{1}{(1 + y_2)^2} \int_{0}^{\infty} y_1 e^{-y_1} \, dy_1$$
  Notice that $\int_{0}^{\infty} y_1 e^{-y_1} \, dy_1$ is $\Gamma(2) = 1! = 1$.
  So $f_{Y_2}(y_2) = \frac{1}{(1 + y_2)^2}$ for $y_2 > 0$.
  Check product:
  $$f_{Y_1}(y_1) f_{Y_2}(y_2) = y_1 e^{-y_1} \cdot \frac{1}{(1+y_2)^2} = ?$$
- **Step 3: Final Calculation.**
  - Product $= f_{Y_1, Y_2}(y_1, y_2)$.
  Thus, $Y_1$ and $Y_2$ are independent random variables.

---

### Exercise 5: Minimum of Independent Exponentials
**Problem:** Let $X_1, X_2, \dots, X_n$ be i.i.d. random variables with $X_i \sim Exp(\lambda)$. Find the distribution of $W = \min(X_1, \dots, X_n)$.

**Solution:**
- **Step 1: Recall the continuous minimum CDF formula.**
  $$F_W(w) = 1 - [1 - F_X(w)]^n$$
- **Step 2: WIP State.**
  For $X_i \sim Exp(\lambda)$, the CDF is $F_X(w) = 1 - e^{-\lambda w}$.
  Substitute this into the formula:
  $$F_W(w) = 1 - \left[1 - \left(1 - e^{-\lambda w}\right)\right]^n = 1 - \left[e^{-\lambda w}\right]^n = 1 - e^{-?}$$
- **Step 3: Final Calculation.**
  - Exponent $= n\lambda w$.
  - $F_W(w) = 1 - e^{-n\lambda w}$.
  This is the CDF of an Exponential distribution with rate parameter $n\lambda$.
  Thus, $\min(X_1, \dots, X_n) \sim Exp(n\lambda)$.
  *(Exam shortcut: The minimum of $n$ independent Exponentials is always Exponential, and its rate is simply the sum of the individual rates!).*

---

### Exercise 6: Maximum of Independent Uniforms
**Problem:** Let $X_1, X_2, \dots, X_n$ be i.i.d. $U(0, 1)$ random variables. Find the PDF of $Y = \max(X_1, \dots, X_n)$.

**Solution:**
- **Step 1: Write down the CDF of $U(0, 1)$.**
  $F_X(x) = x$ for $0 < x < 1$.
- **Step 2: WIP State.**
  Apply maximum CDF formula:
  $$F_Y(y) = [F_X(y)]^n = y^n, \quad 0 < y < 1$$
  Differentiate to obtain PDF:
  $$f_Y(y) = \frac{d}{dy}\left(y^n\right) = ?$$
- **Step 3: Final Calculation.**
  $$f_Y(y) = n y^{n-1}, \quad 0 < y < 1.$$

---

### Exercise 7: Distribution of a Product (Continuous)
**Problem:** Let $X$ and $Y$ be independent random variables, both distributed as $U(0, 1)$. Find the PDF of their product $Z = XY$.

**Solution:**
- **Step 1: Set up the CDF equation for $0 < z < 1$.**
  $$F_Z(z) = P(XY \le z) = \iint_{xy \le z} 1 \, dx \, dy$$
- **Step 2: WIP State.**
  Split the unit square region:
  - If $x \le z$, then $y$ can take any value in $[0, 1]$.
  - If $x > z$, then $y$ must be $\le z/x$.
  $$F_Z(z) = \int_{0}^{z} \left( \int_{0}^{1} 1 \, dy \right) \, dx + \int_{z}^{1} \left( \int_{0}^{z/x} 1 \, dy \right) \, dx$$
  $$F_Z(z) = \int_{0}^{z} 1 \, dx + \int_{z}^{1} \frac{z}{x} \, dx = z + z \left[ \ln(x) \right]_{z}^{1} = z + z(0 - \ln(z)) = z - z\ln(z)$$
  Now, differentiate with respect to $z$:
  $$f_Z(z) = \frac{d}{dz}\left(z - z\ln(z)\right) = 1 - \left( 1 \cdot \ln(z) + z \cdot \frac{1}{z} \right) = ?$$
- **Step 3: Final Calculation.**
  $$f_Z(z) = 1 - \ln(z) - 1 = -\ln(z), \quad 0 < z < 1.$$

---

### Exercise 8: Sum of Independent Normal Variables (MGF Method)
**Problem:** Let $X \sim N(\mu_1, \sigma_1^2)$ and $Y \sim N(\mu_2, \sigma_2^2)$ be independent. Prove that $W = X + Y \sim N(\mu_1 + \mu_2, \sigma_1^2 + \sigma_2^2)$ using MGFs.

**Solution:**
- **Step 1: Set up MGF product.**
  $$M_W(t) = M_X(t) \cdot M_Y(t)$$
- **Step 2: WIP State.**
  $$M_X(t) = e^{\mu_1 t + \frac{1}{2}\sigma_1^2 t^2}, \quad M_Y(t) = e^{\mu_2 t + \frac{1}{2}\sigma_2^2 t^2}$$
  $$M_W(t) = e^{\mu_1 t + \frac{1}{2}\sigma_1^2 t^2} \cdot e^{\mu_2 t + \frac{1}{2}\sigma_2^2 t^2} = e^{?}$$
- **Step 3: Final Calculation.**
  $$M_W(t) = e^{(\mu_1 + \mu_2)t + \frac{1}{2}(\sigma_1^2 + \sigma_2^2)t^2}$$
  By uniqueness of the MGF, this represents a Normal distribution:
  $$W \sim N(\mu_1 + \mu_2, \sigma_1^2 + \sigma_2^2).$$

---

### Exercise 9: Box-Muller Transform (Advanced Jacobian)
**Problem:** Let $U_1, U_2$ be independent $U(0, 1)$ variables. Define:
$$Z_0 = \sqrt{-2\ln U_1} \cos(2\pi U_2) \quad \text{and} \quad Z_1 = \sqrt{-2\ln U_1} \sin(2\pi U_2)$$
Find the joint PDF of $Z_0$ and $Z_1$.

**Solution:**
- **Step 1: Solve for $U_1, U_2$.**
  Squaring and adding:
  $$Z_0^2 + Z_1^2 = -2\ln U_1 \implies U_1 = e^{-\frac{Z_0^2 + Z_1^2}{2}}$$
  Dividing:
  $$\frac{Z_1}{Z_0} = \tan(2\pi U_2) \implies U_2 = \frac{1}{2\pi} \arctan\left(\frac{Z_1}{Z_0}\right)$$
- **Step 2: WIP State for the Jacobian.**
  Compute the Jacobian $J$ of the transformation from $(Z_0, Z_1)$ to $(U_1, U_2)$:
  $$J = \det \begin{pmatrix} \frac{\partial u_1}{\partial z_0} & \frac{\partial u_1}{\partial z_1} \\ \frac{\partial u_2}{\partial z_0} & \frac{\partial u_2}{\partial z_1} \end{pmatrix}$$
  After differentiation and simplification:
  $$|J| = \frac{1}{2\pi} e^{-\frac{z_0^2 + z_1^2}{2}}$$
  Since $U_1, U_2$ are independent $U(0, 1)$, their joint PDF is $f(u_1, u_2) = 1$.
  Apply transformation:
  $$f_{Z_0, Z_1}(z_0, z_1) = 1 \cdot |J| = ?$$
- **Step 3: Final Calculation.**
  $$f_{Z_0, Z_1}(z_0, z_1) = \left( \frac{1}{\sqrt{2\pi}} e^{-z_0^2/2} \right) \cdot \left( \frac{1}{\sqrt{2\pi}} e^{-z_1^2/2} \right)$$
  This factors into the product of two standard normal PDFs, proving that $Z_0$ and $Z_1$ are independent standard normal variables!
