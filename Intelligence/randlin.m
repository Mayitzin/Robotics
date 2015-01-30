%RANDLIN    Random lines with Outliers.
%   [Y,Yn] = randlin(X,n) returns an N-by-1 vector Y with the observations
%   of the random generated line, and another N-by-1 Yn vector that
%   corresponds to the noisy version of Y.
%
%   X is an N-by-1 vector that corresponds to the input variables of the
%   observations Y.
%
%   n is a constant indicating the number of outliers. Possible values are
%   percentages with range [0, 1), or integers indicating the number of
%   observations considered as outliers. If integers are used, the number
%   of outliers must not be greater than the number of observations.
%
%   [Y,Yn] = randlin(X,n,dist) generates outliers with a standard deviation
%   defined by dist. Default is 5.
%
%   [Y,Yn] = randlin(X,n,dist,sd) generates a noisy function with a
%   standard deviation defined by sd. Default is 0.3.
%
%   [Y,Yn] = randlin(X,n,dist,sd,deg) builds a polynomial line with its
%   degree defined by deg. Default is 1 (to create a simple line with a
%   slope).
%
%   @author: Mario Garcia
%   Technische Universitaet Muenchen.

function [Y, Yn] = randlin(X, n, sdOut, sdIn, deg)

if nargin<5
    deg = 1;
end
if nargin<4
    sdIn = 0.3;
end
if nargin<3
    sdOut = 5;
end

N = length(X);

% Create Random line
Y = polyrand(X, deg)';

% Number of Outliers.
if n<1
    n = round(n*100);
elseif n>N
    error('There are more outliers than observations');
elseif n<0
    error('The number of outliers must be positive semi-definite');
end

% Check if Outliers are properly defined
if sdOut<sdIn
    error('Outliers are closer to real values than the inliers.');
end

% Create Random data with Gaussian Distribution
sn = sdIn*(randn(length(X),1));
Yn = Y + sn;

% Substitute real data with Outliers.
XwO  = round(N*rand(n,1));
for k=1:length(XwO)
    i = XwO(k);
    if i<1
        i = 1;
    end
    Yn(i) = Y(i) + sdOut*(randn);
end