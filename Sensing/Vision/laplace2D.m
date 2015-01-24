%laplace2D creates a matrix of a 2D Laplacian

function [Lp] = laplace2D(s, w)

% Following creates the Gaussian mask
if nargin == 1
    wide = s.*5;
else
    wide = w;
end

X = -floor(wide./2):floor(wide./2);            % X and Y values
Y = X;                          % Length of X and Y is 3 times sigma

G = ones(length(X));            % Pre-location of G
for j = 1:size(Y,2)             % Runs over row
    y = Y(1,j);                 % Takes each value in Y direction
    for i = 1:size(X,2)         % Jumps between columns
        x = X(1,i);             % Takes each value in X direction
        e = exp(-(x.^2+y.^2)./(2.*s.^2));
        G(i,j) = -(1/(pi*s^4))*(1-((x^2+y^2)/(2*s^2)))*e;
    end
end

Lp = G./abs(sum(sum(G)));       % Normalization of Gaussian