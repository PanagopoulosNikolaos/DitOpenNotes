# Phase 5.6: Multivariate Random Variables - Fundamentals

Multivariate random variables model scenarios where multiple outcomes are observed simultaneously from the same random experiment. We study joint, marginal, and conditional distributions for both discrete and continuous cases.

---

## 1. Joint and Marginal Distributions

### 1.1 Discrete Random Variables
Let $X$ and $Y$ be discrete random variables defined on the same sample space.

*   **Joint Probability Mass Function (Joint PMF):**
    $$p_{X,Y}(x, y) = P(X = x, Y = y)$$
    Subject to:
    $$\sum_{x} \sum_{y} p_{X,Y}(x, y) = 1$$
*   **Marginal PMFs:** To find the probability distribution of one variable alone, sum out the other variable:
    $$p_X(x) = \sum_{y} p_{X,Y}(x, y) \quad \text{and} \quad p_Y(y) = \sum_{x} p_{X,Y}(x, y)$$

### 1.2 Continuous Random Variables
Let $X$ and $Y$ be continuous random variables.

*   **Joint Probability Density Function (Joint PDF):**
    A function $f(x, y)$ such that:
    $$P((X, Y) \in A) = \iint_A f(x, y) \, dx \, dy$$
    Subject to:
    $$\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x, y) \, dx \, dy = 1 \quad \text{and} \quad f(x,y) \ge 0$$
*   **Marginal PDFs:** Integrate out the other variable:
    $$f_X(x) = \int_{-\infty}^{\infty} f(x, y) \, dy \quad \text{and} \quad f_Y(y) = \int_{-\infty}^{\infty} f(x, y) \, dx$$

---

## 2. Conditional Distributions

Conditional distributions describe the behavior of one random variable when the value of the other is known.

*   **Discrete Case:**
    $$p_{X|Y}(x | y) = P(X = x | Y = y) = \frac{p_{X,Y}(x, y)}{p_Y(y)} \quad (\text{provided } p_Y(y) > 0)$$
*   **Continuous Case:**
    $$f_{X|Y}(x | y) = \frac{f(x, y)}{f_Y(y)} \quad (\text{provided } f_Y(y) > 0)$$

---

## 3. Independence of Random Variables

Two random variables $X$ and $Y$ are independent if their joint distribution is the product of their marginal distributions for all values of $x$ and $y$.

*   **Discrete:** $p_{X,Y}(x, y) = p_X(x) \cdot p_Y(y)$
*   **Continuous:** $f(x, y) = f_X(x) \cdot f_Y(y)$

If this product relation fails for even a single coordinate in the domain, the variables are dependent.

---

## 4. Solved Exercises (9 Examples)

### Exercise 1: Discrete Joint PMF Table
**Problem:** The joint PMF of $X$ and $Y$ is given by the table below. Find the marginal PMF of $X$ and $Y$, and compute $P(X \le 1, Y \ge 1)$.

| $X \setminus Y$ | 0 | 1 | 2 |
| :--- | :--- | :--- | :--- |
| **0** | 0.1 | 0.2 | 0.05 |
| **1** | 0.15 | 0.1 | 0.15 |
| **2** | 0.05 | 0.1 | 0.1 |

**Solution:**
- **Step 1: Calculate marginals by summing rows and columns.**
  - Row sums (Marginal PMF of $X$):
    - $P(X=0) = 0.1 + 0.2 + 0.05 = 0.35$
    - $P(X=1) = 0.15 + 0.1 + 0.15 = 0.40$
    - $P(X=2) = 0.05 + 0.1 + 0.1 = ?$
- **Step 2: WIP State.**
  - $P(X=2) = 0.25$.
  - Column sums (Marginal PMF of $Y$):
    - $P(Y=0) = 0.1 + 0.15 + 0.05 = 0.30$
    - $P(Y=1) = 0.2 + 0.1 + 0.1 = 0.40$
    - $P(Y=2) = 0.05 + 0.15 + 0.1 = ?$
- **Step 3: Final Calculation.**
  - $P(Y=2) = 0.30$.
  - To find $P(X \le 1, Y \ge 1)$, sum cells where $X \in \{0, 1\}$ and $Y \in \{1, 2\}$:
    $$P(X \le 1, Y \ge 1) = p(0,1) + p(0,2) + p(1,1) + p(1,2)$$
    $$P(X \le 1, Y \ge 1) = 0.2 + 0.05 + 0.1 + 0.15 = 0.50.$$

---

### Exercise 2: Discrete Independence Check
**Problem:** Using the joint PMF table from Exercise 1, determine if $X$ and $Y$ are independent.

**Solution:**
- **Step 1: Check the independence condition $P(X=x, Y=y) = P(X=x)P(Y=y)$ for a specific cell.**
  Let's check the cell $(0,0)$.
  From the table: $P(X=0, Y=0) = 0.1$.
- **Step 2: WIP State.**
  From Exercise 1: $P(X=0) = 0.35$ and $P(Y=0) = 0.30$.
  $$P(X=0) \cdot P(Y=0) = 0.35 \cdot 0.30 = ?$$
- **Step 3: Final Calculation.**
  $$P(X=0) \cdot P(Y=0) = 0.105$$
  Since $0.1 \ne 0.105$, the independence condition fails.
  Therefore, $X$ and $Y$ are **dependent**.

---

### Exercise 3: Continuous Normalising Constant
**Problem:** Find the constant $c$ such that $f(x, y) = c(x + 2y)$ is a valid PDF on $0 < x < 1, 0 < y < 1$.

**Solution:**
- **Step 1: Set up the double integral equal to 1.**
  $$\int_{0}^{1} \int_{0}^{1} c(x + 2y) \, dy \, dx = 1$$
- **Step 2: WIP State.**
  Integrate with respect to $y$ first:
  $$\int_{0}^{1} \left[ c\left(xy + y^2\right) \right]_{0}^{1} \, dx = c \int_{0}^{1} (x + 1) \, dx$$
  Now integrate with respect to $x$:
  $$c \left[ \frac{x^2}{2} + x \right]_{0}^{1} = c \left( \frac{1}{2} + 1 \right) = c \cdot \frac{3}{2}$$
  Set this equal to 1:
  $$c \cdot \frac{3}{2} = 1 \implies c = ?$$
- **Step 3: Final Calculation.**
  $$c = \frac{2}{3}.$$

---

### Exercise 4: Continuous Marginal PDFs
**Problem:** For the joint PDF $f(x, y) = \frac{2}{3}(x + 2y)$ on $0 < x < 1, 0 < y < 1$, find the marginal PDFs of $X$ and $Y$.

**Solution:**
- **Step 1: Integrate out $y$ to find $f_X(x)$.**
  $$f_X(x) = \int_{0}^{1} \frac{2}{3}(x + 2y) \, dy = \frac{2}{3} \left[ xy + y^2 \right]_{0}^{1} = \frac{2}{3}(x + 1), \quad 0 < x < 1$$
- **Step 2: WIP State for $f_Y(y)$.**
  Integrate out $x$ to find $f_Y(y)$:
  $$f_Y(y) = \int_{0}^{1} \frac{2}{3}(x + 2y) \, dx = \frac{2}{3} \left[ \frac{x^2}{2} + 2xy \right]_{0}^{1} = \frac{2}{3}\left( \frac{1}{2} + ? \right)$$
- **Step 3: Final Calculation.**
  $$f_Y(y) = \frac{2}{3}\left( \frac{1}{2} + 2y \right) = \frac{1}{3} + \frac{4}{3}y, \quad 0 < y < 1.$$

---

### Exercise 5: Continuous Conditional PDF
**Problem:** Using the joint PDF from Exercise 4, find the conditional PDF of $X$ given $Y = y$, $f_{X|Y}(x | y)$.

**Solution:**
- **Step 1: Recall the conditional PDF formula.**
  $$f_{X|Y}(x | y) = \frac{f(x, y)}{f_Y(y)}$$
- **Step 2: WIP State.**
  From Exercise 4, $f_Y(y) = \frac{1 + 4y}{3}$ and $f(x, y) = \frac{2(x + 2y)}{3}$.
  Substitute these into the formula:
  $$f_{X|Y}(x | y) = \frac{\frac{2(x + 2y)}{3}}{\frac{1 + 4y}{3}} = \frac{2(x + 2y)}{?}$$
- **Step 3: Final Calculation.**
  $$f_{X|Y}(x | y) = \frac{2(x + 2y)}{1 + 4y}, \quad 0 < x < 1$$
  *(Note: For any fixed value of $y$, this is a valid 1D PDF for $X$ on $0 < x < 1$).*

---

### Exercise 6: Continuous Independence Check
**Problem:** Determine if $X$ and $Y$ with joint PDF $f(x, y) = 4xy$ for $0 < x < 1, 0 < y < 1$ are independent.

**Solution:**
- **Step 1: Find marginal PDFs.**
  $$f_X(x) = \int_{0}^{1} 4xy \, dy = \left[ 2xy^2 \right]_{0}^{1} = 2x, \quad 0 < x < 1$$
- **Step 2: WIP State.**
  $$f_Y(y) = \int_{0}^{1} 4xy \, dx = \left[ 2x^2y \right]_{0}^{1} = 2y, \quad 0 < y < 1$$
  Check if $f_X(x) \cdot f_Y(y) = f(x, y)$:
  $$f_X(x) \cdot f_Y(y) = 2x \cdot 2y = ?$$
- **Step 3: Final Calculation.**
  $$2x \cdot 2y = 4xy = f(x, y)$$
  Since the product of the marginals equals the joint PDF over the entire domain, $X$ and $Y$ are **independent**.
  *(Exam tip: If the joint PDF can be written as $g(x)h(y)$ and the domain is rectangular, the variables are always independent!).*

---

### Exercise 7: Non-Rectangular Domain (Gotcha Moment)
**Problem:** Let $f(x, y) = 8xy$ on the domain $0 < x < y < 1$. Are $X$ and $Y$ independent?

**Solution:**
- **Step 1: Analyze the domain boundary.**
  The domain is a triangle ($0 < x < y < 1$). The bounds of $x$ depend directly on $y$.
- **Step 2: WIP State.**
  Calculate the marginal of $X$ (integrate over $y$ from $x$ to 1):
  $$f_X(x) = \int_{x}^{1} 8xy \, dy = \left[ 4xy^2 \right]_{x}^{1} = 4x(1 - x^2), \quad 0 < x < 1$$
  Calculate the marginal of $Y$ (integrate over $x$ from 0 to $y$):
  $$f_Y(y) = \int_{0}^{y} 8xy \, dx = \left[ 4x^2y \right]_{0}^{y} = 4y^3, \quad 0 < y < 1$$
  Check product:
  $$f_X(x) \cdot f_Y(y) = 4x(1-x^2) \cdot 4y^3 = 16xy^3(1-x^2) \neq 8xy$$
- **Step 3: Final Calculation.**
  The variables are **dependent**.
  **Gotcha Rule:** If the domain is non-rectangular (e.g., $x < y$), the random variables are **always dependent**, regardless of the PDF formula, because the range of one variable is restricted by the value of the other.

---

### Exercise 8: Joint CDF to PDF
**Problem:** The joint CDF of $X$ and $Y$ is $F(x, y) = (1 - e^{-x})(1 - e^{-2y})$ for $x > 0, y > 0$. Find the joint PDF $f(x, y)$.

**Solution:**
- **Step 1: Set up the partial derivatives.**
  $$f(x, y) = \frac{\partial^2}{\partial x \partial y} F(x, y)$$
- **Step 2: WIP State.**
  Differentiate with respect to $x$ first:
  $$\frac{\partial}{\partial x} F(x, y) = e^{-x} (1 - e^{-2y})$$
  Now, differentiate this result with respect to $y$:
  $$\frac{\partial}{\partial y} \left( e^{-x} (1 - e^{-2y}) \right) = e^{-x} \cdot (2e^{-2y}) = ?$$
- **Step 3: Final Calculation.**
  $$f(x, y) = 2 e^{-x - 2y}, \quad x > 0, y > 0.$$

---

### Exercise 9: Probability on a Region
**Problem:** Let $X$ and $Y$ have joint PDF $f(x, y) = x + y$ on $0 < x < 1, 0 < y < 1$. Find $P(X + Y < 1)$.

**Solution:**
- **Step 1: Set up the bounds for integration.**
  The condition $x + y < 1$ translates to $y < 1 - x$.
  Thus, $x$ ranges from 0 to 1, and for a fixed $x$, $y$ ranges from 0 to $1 - x$.
- **Step 2: WIP State.**
  $$P(X + Y < 1) = \int_{0}^{1} \int_{0}^{1-x} (x + y) \, dy \, dx$$
  Integrate with respect to $y$:
  $$\int_{0}^{1-x} (x + y) \, dy = \left[ xy + \frac{y^2}{2} \right]_{0}^{1-x} = x(1-x) + \frac{(1-x)^2}{2} = x - x^2 + \frac{1 - 2x + x^2}{2} = \frac{1 - x^2}{2}$$
  Now integrate with respect to $x$:
  $$\int_{0}^{1} \frac{1 - x^2}{2} \, dx = \left[ \frac{x}{2} - \frac{x^3}{6} \right]_{0}^{1} = \frac{1}{2} - ?$$
- **Step 3: Final Calculation.**
  $$\text{Fraction} = \frac{1}{6}$$
  $$P(X + Y < 1) = \frac{1}{2} - \frac{1}{6} = \frac{1}{3} \approx 0.3333.$$
