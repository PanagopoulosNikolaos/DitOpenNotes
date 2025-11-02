% -----------------------------------------------------------------------------
%
%  Exercise 12: Linear Regression - Normal Equation
%
%  Task:
%  Solve for the optimal `theta` in one step using the Normal Equation,
%  without the need for feature scaling or iterations.
%
%  Formula:
%  θ = (X' * X)^(-1) * X' * y
%
%  Instructions:
%  1. Use the original (unscaled) feature matrix `X` with the intercept term.
%  2. Use the target vector `y`.
%  3. Calculate `theta` using the normal equation formula.
%  4. Use the calculated `theta` to make a prediction and compare it with
%     the result from gradient descent.
%
% -----------------------------------------------------------------------------

% To run this script, type its name in the Octave command window:
% >> 12_ml_normal_equation

% Clear the workspace and command window
clear; clc;

% --- Solution ---

% 1. Load original (unscaled) data with intercept term
X = [1, 2100, 3; 1, 1600, 3; 1, 2400, 3; 1, 1416, 2; 1, 3000, 4];
y = [400000; 330000; 370000; 232000; 540000];

fprintf('Original Feature Matrix X:\n'); disp(X);

% 3. Calculate theta using the Normal Equation
fprintf('\nCalculating theta using the Normal Equation...\n');

% The formula is pinv(X' * X) * X' * y, where pinv is the pseudoinverse,
% which is more robust than inv.
theta_normal = pinv(X' * X) * X' * y;

fprintf('\nOptimal theta found:\n');
disp(theta_normal);

% --- Making a Prediction ---
fprintf('\n--- Prediction Example ---\n');
% Predict the price for a 1650 sq-ft, 3 br house

% We use the unscaled features here because theta was trained on unscaled data
new_features = [1, 1650, 3];

% Predict the price
predicted_price = new_features * theta_normal;

fprintf('Predicted price for a 1650 sq-ft, 3 bedroom house: $%.2f\n', predicted_price);

fprintf('\nNote: This result should be very close to the one from gradient descent.\n');
fprintf('The Normal Equation is great for smaller datasets but can be slow for\n');
fprintf('very large feature matrices (calculating the inverse is computationally expensive).\n');