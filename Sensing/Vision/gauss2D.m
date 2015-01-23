%   Information
%   -----------
%   	Code 4 of 5
%       Exercise Sheet: 1
%       Tracking and Detection
%       WS 2012/13
%   Technische Universitaet Muenchen

function [Gn] = gauss2D(s)
% Following creates the Gaussian mask
X = -floor(s.*3./2):floor(s.*3./2);            % X and Y values
Y = X;                          % Length of X and Y is 3 times sigma

G = ones(length(X));            % Creates a matrix G same dimension as final mask
for j = 1:size(Y,2)             % Runs over row
    y = Y(1,j);                 % Takes each value in Y direction
    for i = 1:size(X,2)         % Jumps between columns
        x = X(1,i);             % Takes each value in X direction
        G(i,j) = exp(-(x.^2+y.^2)./(2.*s.^2));
    end
end

Gn = G./(sum(sum(G)));          % Normalization of Gaussian