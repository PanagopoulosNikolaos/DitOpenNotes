% -----------------------------------------------------------------------------
%
%  Exercise 5: Solving Systems of Linear Equations
%
%  Task:
%  Solve a system of linear equations Ax = b.
%
%  Instructions:
%  Consider the system:
%    x + 2y = 1
%    3x + 5y = 2
%  1. Represent this system in the form Ax = b, defining the matrix A and
%     the vector b.
%  2. Solve for x using the backslash operator (\), which is efficient and
%     numerically stable.
%  3. Solve for x by calculating the inverse of A and multiplying it by b.
%  4. Verify that both methods yield the same result.
%
% -----------------------------------------------------------------------------

% To run this script, type its name in the Octave command window:
% >> 05_solving_linear_systems

% Clear the workspace and command window
clear; clc;

% --- Solution ---

% The system of equations:
%   1*x1 + 2*x2 = 1
%   3*x1 + 5*x2 = 2

% 1. Define the coefficient matrix A and the constant vector b
fprintf('Coefficient Matrix A:\n');
A = [1, 2; 3, 5]

fprintf('\nConstant Vector b:\n');
b = [1; 2]

% 2. Solve using the backslash operator (A\b)
fprintf('\nSolving for x using the backslash operator (x = A \\ b):\n');
x_backslash = A \\ b

% 3. Solve using the inverse (inv(A) * b)
fprintf('\nSolving for x using the inverse (x = inv(A) * b):\n');
x_inverse = inv(A) * b

% 4. Verification
fprintf('\n--- Verification ---\n');
fprintf('Solution from backslash:\n');
disp(x_backslash);
fprintf('Solution from inverse:\n');
disp(x_inverse);

% Check if the results are close enough
if (norm(x_backslash - x_inverse) < 1e-9)
    fprintf('\nThe results from both methods are consistent.\n');
else
    fprintf('\nThe results from the two methods differ significantly.\n');
endif

fprintf('\nNote: The backslash operator (mldivide) is generally preferred over inv(A)*b for both speed and accuracy.\n');