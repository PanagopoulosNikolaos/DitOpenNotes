% -----------------------------------------------------------------------------
%
%  Exercise 2: Basic Matrix Operations
%
%  Task:
%  Perform basic arithmetic operations like addition, subtraction, scalar
%  multiplication, and matrix multiplication.
%
%  Instructions:
%  1. Create two 2x2 matrices, A and B.
%  2. Calculate their sum (A + B).
%  3. Calculate their difference (A - B).
%  4. Multiply matrix A by a scalar (e.g., 3).
%  5. Calculate the matrix product (A * B).
%  6. Perform element-wise multiplication (A .* B).
%
% -----------------------------------------------------------------------------

% To run this script, type its name in the Octave command window:
% >> 02_matrix_operations

% Clear the workspace and command window
clear; clc;

% --- Solution ---

% 1. Create two 2x2 matrices
fprintf('Matrix A:\n');
A = [1, 2; 3, 4]

fprintf('\nMatrix B:\n');
B = [5, 6; 7, 8]

% 2. Addition
fprintf('\nSum (A + B):\n');
sum_AB = A + B

% 3. Subtraction
fprintf('\nDifference (A - B):\n');
diff_AB = A - B

% 4. Scalar Multiplication
fprintf('\nScalar Multiplication (3 * A):\n');
scalar_mult_A = 3 * A

% 5. Matrix Multiplication
fprintf('\nMatrix Product (A * B):\n');
matrix_prod_AB = A * B

% 6. Element-wise Multiplication
fprintf('\nElement-wise Product (A .* B):\n');
element_prod_AB = A .* B

fprintf('\nNote the difference between matrix multiplication (*) and element-wise multiplication (.*).\n');
