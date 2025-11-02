% -----------------------------------------------------------------------------
%
%  Exercise 4: Transpose, Inverse, and Determinant
%
%  Task:
%  Calculate the transpose, inverse, and determinant of a matrix.
%
%  Instructions:
%  1. Create a 3x3 matrix A.
%  2. Calculate its transpose.
%  3. Calculate its determinant.
%  4. Calculate its inverse.
%  5. Verify the inverse by multiplying A by its inverse (should result in
%     the identity matrix).
%
% -----------------------------------------------------------------------------

% To run this script, type its name in the Octave command window:
% >> 04_transpose_inverse_determinant

% Clear the workspace and command window
clear; clc;

% --- Solution ---

% 1. Create a 3x3 matrix
fprintf('Matrix A:\n');
% We need a non-singular matrix (determinant is not zero) for the inverse to exist.
A = [1, 2, 0; 2, 5, -1; 4, 10, -1]

% 2. Transpose
fprintf('\nTranspose of A (A'):\n');
A_transpose = A'
% Alternatively, use transpose(A)

% 3. Determinant
fprintf('\nDeterminant of A (det(A)):\n');
det_A = det(A)

if (det_A == 0)
    fprintf('\nWarning: Determinant is zero, the matrix is singular and has no inverse.\n');
else
    % 4. Inverse
    fprintf('\nInverse of A (inv(A)):\n');
    A_inv = inv(A)

    % 5. Verification
    fprintf('\nVerification (A * inv(A)):\n');
    % The result should be very close to the identity matrix.
    % Due to floating-point arithmetic, it might not be exactly perfect.
    verification = A * A_inv
endif
