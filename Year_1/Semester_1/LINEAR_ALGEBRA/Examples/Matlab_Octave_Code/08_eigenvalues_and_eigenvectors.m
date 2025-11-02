% -----------------------------------------------------------------------------
%
%  Exercise 8: Eigenvalues and Eigenvectors
%
%  Task:
%  Calculate the eigenvalues and eigenvectors of a square matrix.
%
%  Instructions:
%  1. Create a 2x2 square matrix A.
%  2. Use the `eig` function to find its eigenvalues and eigenvectors.
%  3. The `eig` function returns two matrices: V (eigenvectors as columns)
%     and D (eigenvalues on the diagonal).
%  4. Verify the relationship Av = 
%v for the first eigenvalue-eigenvector
%     pair, where A is the matrix, v is an eigenvector, and 
% is its
%     corresponding eigenvalue.
%
% -----------------------------------------------------------------------------

% To run this script, type its name in the Octave command window:
% >> 08_eigenvalues_and_eigenvectors

% Clear the workspace and command window
clear; clc;

% --- Solution ---

% 1. Create a 2x2 matrix
fprintf('Matrix A:\n');
A = [1, 2; 2, 1]

% 2. Calculate eigenvalues and eigenvectors
fprintf('\nCalculating eigenvalues and eigenvectors...\n');
% [V, D] = eig(A)
% V will contain the eigenvectors as its columns.
% D will be a diagonal matrix containing the eigenvalues.
[V, D] = eig(A)

% 3. Extract the eigenvalues and eigenvectors
fprintf('\nEigenvectors (columns of V):\n');
disp(V);

fprintf('Eigenvalues (diagonal of D):\n');
% The eigenvalues are the diagonal elements of D
eigenvalues = diag(D)

% 4. Verification
fprintf('\n--- Verification for the first eigenvalue-eigenvector pair ---\n');

% Get the first eigenvector (first column of V)
v1 = V(:, 1)

% Get the first eigenvalue (first diagonal element of D)
lambda1 = D(1, 1)

fprintf('\nCalculating A * v1:\n');
Av1 = A * v1

fprintf('\nCalculating lambda1 * v1:\n');
lambda1_v1 = lambda1 * v1

% Check if Av1 and lambda1_v1 are approximately equal
if (norm(Av1 - lambda1_v1) < 1e-9)
    fprintf('\nVerification successful: Av = 
%v holds true for the first pair.\n');
else
    fprintf('\nVerification failed.\n');
endif
