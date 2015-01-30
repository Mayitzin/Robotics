%POLYRAND generates a random polynomial function
%   [Y, p] returns the polynomial function Y and its parameters p, where
%   the vector X contains the input parameters and the constant d defines
%   the degree of the polynomial to build.
%
%   @author: Mario Garcia.
%   Technische Universitaet Muenchen.

function [Y, p] = polyrand(X, d)

p = 2.*(rand(d+1,1)) - ones(d+1,1);

Y = polyval(p, X);