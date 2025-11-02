% -----------------------------------------------------------------------------
%
%  Exercise 10: Linear Regression - Cost Function
%
%  Task:
%  Implement the cost function (J) for linear regression. This function
%  measures how well the model's predictions match the actual data.
%
%  Formula:
%  J(θ) = (1 / (2*m)) * Σ( (h_θ(x_i) - y_i)^2 )
%  where h_θ(x) = X * θ
%
%  Instructions:
%  1. Use the feature matrix `X` and target vector `y` from the previous
%     exercise.
%  2. Initialize the parameter vector `theta` (θ) to zeros. For our two
%     features (plus intercept), theta will be 3x1.
%  3. Calculate the predictions `h` (hypothesis).
%  4. Calculate the squared errors between predictions and actual values.
%  5. Compute the total cost `J` using the formula.
%
% -----------------------------------------------------------------------------

% To run this script, type its name in the Octave command window:
% >> 10_ml_linear_regression_cost

% Clear the workspace and command window
clear; clc;

% --- Solution ---

% Load data from the previous exercise
% Feature Matrix X with intercept term, and Target Vector y
X = [1, 2100, 3; 1, 1600, 3; 1, 2400, 3; 1, 1416, 2; 1, 3000, 4];
y = [400000; 330000; 370000; 232000; 540000];
m = length(y); % Number of training examples

fprintf('Feature Matrix X:\n'); disp(X);
fprintf('Target Vector y:\n'); disp(y);

% 2. Initialize theta to zeros
% The number of thetas must match the number of columns in X
theta = zeros(3, 1);
fprintf('Initial theta:\n'); disp(theta);

% 3. Calculate the hypothesis (predictions)
% h is a vector of predicted y values for each training example
h = X * theta;
fprintf('Initial predictions (h = X * theta):\n'); disp(h);

% 4. Calculate squared errors
squared_errors = (h - y).^2;
fprintf('\nSquared errors ((h - y)^2):\n'); disp(squared_errors);

% 5. Compute the cost J
J = (1 / (2 * m)) * sum(squared_errors);

fprintf('\nCalculated Cost J with theta = [0; 0; 0] is: %f\n', J);
fprintf('(This large value shows that our initial model is very inaccurate, as expected).\n');
