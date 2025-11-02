% -----------------------------------------------------------------------------
%
%  Exercise 3: Special Matrices and Indexing
%
%  Task:
%  Create special matrices (identity, zeros, ones) and learn how to access
%  and modify matrix elements.
%
%  Instructions:
%  1. Create a 3x3 identity matrix.
%  2. Create a 2x4 matrix of all zeros.
%  3. Create a 3x2 matrix of all ones.
%  4. Create a 4x4 matrix with random values between 0 and 1.
%  5. Access and display the element in the 2nd row, 3rd column of a matrix.
%  6. Change the value of that element.
%  7. Select and display the entire first row of a matrix.
%  8. Select and display the entire third column of a matrix.
%
% -----------------------------------------------------------------------------

% To run this script, type its name in the Octave command window:
% >> 03_special_matrices_and_indexing

% Clear the workspace and command window
clear; clc;

% --- Solution ---

% 1. Identity Matrix
fprintf('3x3 Identity Matrix:\n');
I = eye(3)

% 2. Zeros Matrix
fprintf('\n2x4 Zeros Matrix:\n');
Z = zeros(2, 4)

% 3. Ones Matrix
fprintf('\n3x2 Ones Matrix:\n');
O = ones(3, 2)

% 4. Random Matrix
fprintf('\n4x4 Random Matrix:\n');
R = rand(4, 4)

% --- Indexing ---

fprintf('\n--- Indexing Example using Matrix A ---\n');
A = [11, 12, 13, 14; 21, 22, 23, 24; 31, 32, 33, 34]

% 5. Access an element (row, column)
fprintf('\nElement at (2, 3) of A:\n');
element_2_3 = A(2, 3)

% 6. Change the value of an element
fprintf('\nChanging element at (2, 3) to 99...\n');
A(2, 3) = 99;
fprintf('Matrix A after change:\n');
disp(A);

% 7. Select a row (use : for all columns)
fprintf('\nFirst row of A:\n');
first_row = A(1, :)

% 8. Select a column (use : for all rows)
fprintf('\nThird column of A:\n');
third_col = A(:, 3)
