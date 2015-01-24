%POLYREG returns the coefficients of a polynomial.
% w = polyreg(dataset, n) returns the coefficients for a polynomial,
%   whose observations are in an N-by-2 matrix 'dataset'
%
%   fileName is a string defining the name and location of the file.
%
%   History:
%       29.05.2013. First implementation.
%       20.06.2013. Added extra methods.
%       
%   @author: Mario Garcia
%   www.mayitzin.com

function [w, E] = polyreg(dataset, n, method)
% Check validity of input
if nargin < 3
    method = 'pinv';
end
if nargin < 2
    error('Not enough input values.');
end

% Complexity of Polynomial
M = n+1;

% Size of Dataset
N = size(dataset,1);

% Points extraction
x = dataset(:,1);
t = dataset(:,2);

%% Linear Regression
% w_0 = ones(N,1);        % 'dummy' bias

% Create Design Matrix (Phi)
Phi = ones(N,M-1);    % Pre-location of Phi
for i = 1:N
    for j = 0:(M-1)
        Phi(i,j+1) = x(i)^j;
    end
end

% Get parameters (weights)
if strcmp(method, 'pinv')
    w = pinv(Phi) * t;
elseif strcmp(method, 'backslash')
    w = (Phi'*Phi) \ Phi' * t;
elseif strcmp(method, 'svd')
    [U, S, V] = svd(Phi);
    w = (V * ( (S' * S) \ S') * U') * t;
else
    error('No proper method specified');
end

%% Sum-of-squares Error
E = 0;
for i=1:N
    e = (w'*Phi(i,:)' - t(i)').^2;
    E = E + e;
end
E = E/2;