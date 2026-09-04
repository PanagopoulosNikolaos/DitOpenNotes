# Tutorial 01: Matrix Computations in GNU Octave and MATLAB

## Context and Grounding
This tutorial provides a hands-on guide to computer-aided matrix manipulation and numerical linear algebra using GNU Octave (an open-source high-level programming environment compatible with MATLAB).

---

## 1. Environment Setup and Basic Syntax

Launch the interactive GNU Octave terminal:
```bash
octave --no-gui
```

### 1.1 Vector and Matrix Instantiation
```matlab
% Row vector (spaces or commas between elements)
v = [1, 2, 3];

% Column vector (semicolons delineate rows)
u = [4; 5; 6];

% 3x3 Matrix
A = [1, 2, 3; 
     4, 5, 6; 
     7, 8, 0];

% Inspect dimensions
disp(size(A)); % Outputs: [3, 3]
```

### 1.2 Matrix vs. Element-Wise Operations
* **Standard Matrix Multiplication (`*`)**: Requires inner dimensions to match ($m \times p$ multiplied by $p \times n$).
  ```matlab
  C = A * u; % Matrix-vector multiplication (3x1 result)
  ```
* **Element-Wise Operations (`.*`, `./`, `.^`)**: Operations applied element-by-element across identical dimensions.
  ```matlab
  M = A .* A; % Squares each entry of A individually
  ```
* **Transpose (`'`)**:
  ```matlab
  A_trans = A';
  ```

---

## 2. Solving Linear Systems: The Backslash Operator (`\`)

To solve the system $A \mathbf{x} = \mathbf{b}$ for unknown $\mathbf{x}$:

```matlab
A = [2, 1, -1; 
    -3, -1, 2; 
    -2, 1, 2];
b = [8; -11; -3];

% Solve using Gaussian elimination with partial pivoting:
x = A \ b;
disp(x);
```
* The backslash operator `A \ b` is numerically superior to computing `inv(A) * b` because it employs $LU$ decomposition without incurring rounding instabilities.

---

## 3. Essential Linear Algebra Functions

| Function | Operational Semantics | Example |
|:---|:---|:---|
| `det(A)` | Computes scalar determinant of square matrix $A$. | `d = det(A);` |
| `inv(A)` | Computes matrix inverse $A^{-1}$. | `A_inv = inv(A);` |
| `rank(A)` | Computes rank (count of linearly independent rows/columns). | `r = rank(A);` |
| `rref(A)` | Produces Reduced Row Echelon Form of augmented matrix. | `[R, pivots] = rref([A, b]);` |
| `null(A)` | Constructs an orthonormal basis for the null space $\text{Null}(A)$. | `N = null(A);` |
| `orth(A)` | Constructs an orthonormal basis for the column space $\text{Col}(A)$.| `Q = orth(A);` |
| `eig(A)` | Computes eigenvalues and eigenvectors ($A V = V D$). | `[V, D] = eig(A);` |

---

## 4. Practical Script Walkthrough: Eigenvalues and Verification

Save the following code as `eigen_demo.m`:

```matlab
% Clear workspace and console
clear; clc;

% Define symmetric test matrix
A = [4, 1, -2; 
     1, 2,  0; 
    -2, 0,  3];

% Compute eigenvectors (V) and diagonal eigenvalue matrix (D)
[V, D] = eig(A);

fprintf("Eigenvalues:\n");
disp(diag(D));

fprintf("Normalized Eigenvector Columns:\n");
disp(V);

% Verify spectral decomposition: A == V * D * V'
A_reconstructed = V * D * V';
error_norm = norm(A - A_reconstructed);
fprintf("Reconstruction residual norm: %e\n", error_norm);
```

Execute from command line:
```bash
octave eigen_demo.m
```
Expected output confirms that the residual error norm is on the order of machine epsilon ($10^{-15}$), verifying numerical correctness.

