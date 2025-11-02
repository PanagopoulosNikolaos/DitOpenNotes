% -----------------------------------------------------------------------------
%
%  Exercise 11: Linear Regression - Gradient Descent
%
%  Task:
%  Implement the gradient descent algorithm to find the optimal `theta`
%  values that minimize the cost function J.
%
%  Gradient Descent Update Rule (repeated for a number of iterations):
%  θ_j := θ_j - α * (1/m) * Σ( (h_θ(x_i) - y_i) * x_ij )
%  Vectorized form: θ := θ - α * (1/m) * X' * (X*θ - y)
%
%  Instructions:
%  1. Use the X and y from the previous exercise.
%  2. Initialize `theta`, `alpha` (learning rate), and `num_iters`.
%  3. Create a loop that runs for `num_iters`.
%  4. Inside the loop, calculate the new `theta` using the vectorized update
%     rule.
%  5. Store the cost J in a vector at each iteration to plot it later and
%     verify that it is decreasing.
%  6. Plot the convergence of the cost function.
%
% -----------------------------------------------------------------------------

% To run this script, type its name in the Octave command window:
% >> 11_ml_gradient_descent

% Clear the workspace and command window
clear; clc;

% --- Solution ---

% Load data
X = [1, 2100, 3; 1, 1600, 3; 1, 2400, 3; 1, 1416, 2; 1, 3000, 4];
y = [400000; 330000; 370000; 232000; 540000];
m = length(y);

% Note: Features are on different scales. For gradient descent to work well,
% we need to perform feature scaling.

fprintf('Performing feature scaling...\n');
% Get the original features (excluding the intercept)
X_features = X(:, 2:3);

% For each feature, subtract the mean and divide by the standard deviation
mu = mean(X_features);
sigma = std(X_features);
X_scaled = (X_features - mu) ./ sigma;

% Add the intercept term back to the scaled features
X = [ones(m, 1), X_scaled];
fprintf('Scaled Feature Matrix X:\n'); disp(X);

% 2. Initialize parameters
theta = zeros(3, 1);
alpha = 0.01; % Learning rate
num_iters = 1500; % Number of iterations

% Vector to store the cost in each iteration
J_history = zeros(num_iters, 1);

% 3. Run Gradient Descent
for iter = 1:num_iters
    % Calculate predictions
    h = X * theta;

    % Calculate the error
    error = h - y;

    % Calculate the gradient
    gradient = (1/m) * (X' * error);

    % Update theta
    theta = theta - alpha * gradient;

    % 5. Store the cost J at this iteration
    J_history(iter) = (1 / (2 * m)) * sum((h - y).^2);
end

fprintf('\nGradient descent finished.\n');
fprintf('Optimal theta found:\n');
disp(theta);

% 6. Plot the cost function over iterations
figure;
plot(1:num_iters, J_history, '-b', 'LineWidth', 2);
title('Cost Function Convergence');
xlabel('Number of Iterations');
ylabel('Cost J');
grid on;

fprintf('\nPlotting cost function convergence. Close the plot window to continue.\n');

% --- Making a Prediction ---
fprintf('\n--- Prediction Example ---\n');
% Predict the price for a 1650 sq-ft, 3 br house

% First, scale the new features using the same mu and sigma from the training data
new_features = [1650, 3];
new_features_scaled = (new_features - mu) ./ sigma;

% Add the intercept term
new_features_final = [1, new_features_scaled];

% Predict the price
predicted_price = new_features_final * theta;

fprintf('Predicted price for a 1650 sq-ft, 3 bedroom house: $%.2f\n', predicted_price);
