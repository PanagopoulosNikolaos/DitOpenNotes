% -----------------------------------------------------------------------------
%
%  Exercise 6: Basic 2D Plotting
%
%  Task:
%  Create a simple 2D plot of a sine wave.
%
%  Instructions:
%  1. Create a vector `x` of values from 0 to 2*pi with a small step
%     (e.g., 0.1).
%  2. Create a vector `y` where y = sin(x).
%  3. Create a plot of y versus x.
%  4. Add a title, x-axis label, and y-axis label to the plot.
%  5. Add a grid to the plot.
%  6. Save the plot to a file (e.g., 'sine_wave.png').
%
%  Note:
%  When you run this script, a plot window will open. You may need to close
%  it manually for the script to finish.
%
% -----------------------------------------------------------------------------

% To run this script, type its name in the Octave command window:
% >> 06_plotting_basics

% Clear the workspace and command window
clear; clc;

% --- Solution ---

% 1. Create the x vector (from 0 to 2*pi)
% The syntax is start:step:end
x = 0:0.1:2*pi;

% 2. Create the y vector
y = sin(x);

% 3. Create the plot
% The `figure` command opens a new plot window.
figure;
plot(x, y);

% 4. Add labels and title
title('Sine Wave from 0 to 2*pi');
xlabel('x (radians)');
ylabel('sin(x)');

% 5. Add a grid
grid on;

% 6. Save the plot to a file
fprintf('\nSaving plot to sine_wave.png...\n');
print('sine_wave.png', '-dpng');

fprintf('Plot saved successfully. Close the plot window to continue.\n');

% The `pause` command can be used to wait for user input before closing.
% pause;
