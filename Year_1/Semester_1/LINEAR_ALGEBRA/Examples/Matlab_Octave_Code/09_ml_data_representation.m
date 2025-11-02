% -----------------------------------------------------------------------------
%
%  Exercise 9: Data Representation for Machine Learning
%
%  Task:
%  Understand how to represent a simple dataset using a feature matrix X and
%  a target vector y, a standard convention in machine learning.
%
%  Instructions:
%  Consider a dataset for predicting house prices. The features are
%  'size (sq. ft.)' and 'number of bedrooms'. The target is 'price ($')'.
%    Size | Bedrooms | Price
%    -------------------------
%    2100 |    3     | 400000
%    1600 |    3     | 330000
%    2400 |    3     | 370000
%    1416 |    2     | 232000
%    3000 |    4     | 540000
%
%  1. Create the feature matrix `X` where each row is a training example and
%     each column is a feature.
%  2. Create the target vector `y` containing the prices.
%  3. Add a column of ones to the feature matrix `X`. This is a common
%     practice to account for the intercept term (theta_0) in linear
%     regression.
%
% -----------------------------------------------------------------------------

% To run this script, type its name in the Octave command window:
% >> 09_ml_data_representation

% Clear the workspace and command window
clear; clc;

% --- Solution ---

% The raw data
data = [
    2100, 3, 400000;
    1600, 3, 330000;
    2400, 3, 370000;
    1416, 2, 232000;
    3000, 4, 540000
];

% 1. Create the feature matrix X (first two columns of data)
fprintf('Feature Matrix X (original):\n');
X = data(:, 1:2)

% 2. Create the target vector y (third column of data)
fprintf('\nTarget Vector y:\n');
y = data(:, 3)

% Get the number of training examples (number of rows in X)
m = size(X, 1);

% 3. Add a column of ones for the intercept term
fprintf('\nFeature Matrix X with intercept term:\n');
% Create a column vector of m ones and concatenate it with X
X = [ones(m, 1), X]

fprintf('\nThis new X matrix is ready to be used for linear regression.\n');
