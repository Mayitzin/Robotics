% Evaluator of polyonomial regression with random parameters.
%
% This script creates a random polynomial, builds the curve with added
% random Gaussian noise, and evaluates it to estimate its parameters.
%
% The estimation is made with the customized function "polyreg", which
% works similarly to "polyfit", but is created to compare several methods
% of polynomial regressions. See script of polyreg for further details.
%
% The final results are shown in a graph with the real function (dashed
% black), its noisy observations (red stars) and the reconstructed
% curve (solid blue) created with the estimated parameters.
%
% In the Command Window a table is shown with the real parameters, the
% estimated parameters and their error (simply their difference).
%
% History:
%     09.07.2013. First implementation.
%     24.01.2015. Updated comments.
%                 Improved visualization of Parameters.
%     30.01.2015. New Testing function.
%
% @author: Mario Garcia
%     www.mayitzin.com

close all
clc

% Parameters
coeff_deg  = 5;           % Coefficient degree
param_orig = 2.*rand(1,coeff_deg+1)-1;  % Random parameters from -1 to 1

% Define ranges for real and observed points
X = -5:0.1:5;
Y_real = 0.02.*sin(X).*exp(X);        % Real function
noise  = 0.1*randn(1,length(Y_real));
Z = Y_real+noise;

% Polynomial Regression
w = polyreg([X' Z'], coeff_deg, 'pinv');
Y_est = polyval(fliplr(w'), X);

% Plotting
figure()
    plot(X, Y_real, 'k--', ...
         X, Z, 'r*', ...
         X, Y_est, 'b-')
    legend('Real', 'Observations', 'Estimated')