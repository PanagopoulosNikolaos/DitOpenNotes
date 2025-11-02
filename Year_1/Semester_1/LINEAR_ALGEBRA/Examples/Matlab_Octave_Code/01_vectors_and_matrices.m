% -----------------------------------------------------------------------------
%
%  Exercise 1: Vectors and Matrices
%
%  Task:
%  Learn the basics of creating row vectors, column vectors, and matrices in
%  Octave.
%
%  Instructions:
%  1. Create a row vector.
%  2. Create a column vector.
%  3. Create a 3x3 matrix.
%  4. Use the size() function to see the dimensions.
%
% -----------------------------------------------------------------------------

% To run this script in Octave, open Octave, navigate to the directory
% containing this file, and type the filename without the .m extension, like so:
% >> 01_vectors_and_matrices

% Clear the workspace and command window
clear; clc;

% --- Solution ---

% 1. Create a row vector (elements separated by spaces or commas)
fprintf('Creating a row vector v:\n');
v = [1 2 3]
% or v = [1, 2, 3]

% 2. Create a column vector (elements separated by semicolons)
fprintf('\nCreating a column vector u:\n');
u = [4; 5; 6]

% 3. Create a 3x3 matrix (rows separated by semicolons)
fprintf('\nCreating a 3x3 matrix A:\n');
A = [1, 2, 3; 4, 5, 6; 7, 8, 9]

% 4. Check the dimensions
fprintf('\nChecking dimensions:\n');
size_v = size(v)
size_u = size(u)
size_A = size(A)

fprintf('\nNote: A row vector is a 1xN matrix, and a column vector is an Nx1 matrix.\n');
