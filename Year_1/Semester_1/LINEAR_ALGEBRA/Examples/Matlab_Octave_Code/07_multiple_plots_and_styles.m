% -----------------------------------------------------------------------------
%
%  Exercise 7: Multiple Plots and Styling
%
%  Task:
%  Plot multiple functions on the same graph with different line styles and
%  colors, and add a legend.
%
%  Instructions:
%  1. Create a vector `x` of values from 0 to 2*pi.
%  2. Create vectors for y1 = sin(x) and y2 = cos(x).
%  3. Plot y1 against x using a solid red line with circle markers.
%  4. On the same graph, plot y2 against x using a dashed blue line with
%     star markers.
%  5. Add a title and axis labels.
%  6. Add a legend to identify the two functions.
%
% -----------------------------------------------------------------------------

% To run this script, type its name in the Octave command window:
% >> 07_multiple_plots_and_styles

% Clear the workspace and command window
clear; clc;

% --- Solution ---

% 1. Create the x vector
x = 0:0.1:2*pi;

% 2. Create the y vectors
y1 = sin(x);
y2 = cos(x);

% 3. Create the plot
figure;

% The `hold on` command allows multiple plots on the same axes.
hold on;

% Plot y1 with a red solid line ('r-') and circle markers ('o')
plot(x, y1, 'r-o', 'LineWidth', 2);

% Plot y2 with a blue dashed line ('b--') and star markers ('*')
plot(x, y2, 'b--*', 'LineWidth', 2);

% `hold off` returns to the default behavior where a new plot clears the axes.
hold off;

% 5. Add labels and title
title('Sine and Cosine Waves');
xlabel('x (radians)');
ylabel('Function Value');
grid on;

% 6. Add a legend
% The labels in the legend correspond to the order of the plot commands.
legend('sin(x)', 'cos(x)');

fprintf('Plot created. Close the plot window to continue.\n');
