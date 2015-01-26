% Automatic creation of a 2D Gaussian mask
%
% This code creates a "Gaussian mask" (a.k.a. Gaussian Filter kernel)
% used to filter the image and remove noise.
%
% The size of the mask is 3*sigma x 3*sigma, where sigma is the variation
% of the Gaussian. The final Gaussian mask is normalized, that is:
%     sum(sum(Gn)) = 1
%
% For futher reference see:
%   [1] Szeliski, R. Computer Vision: Algorithms and Applications.
%       Springer, pages 115-118. 2010.
%
% History:
%     29.11.2012. First Implementation.
%     23.01.2015. Updated information for Octave.
%                 Added comments.
%
% TODO:
%     - Optional specification of mask dimensions.
%
% @author: Mario Garcia.
%     www.mayitzin.com

function [Gn] = gauss2D(s)
% Following creates the Gaussian mask
X = -floor(s.*3./2):floor(s.*3./2);            % X and Y values
Y = X;                          % Length of X and Y is 3xsigma

% Creation of Kernel
G = ones(length(X));            % Builds a matrix G same dimension as final mask
for j = 1:size(Y,2)             % Runs over row
    y = Y(1,j);                 % Takes each value in Y direction
    for i = 1:size(X,2)         % Jumps between columns
        x = X(1,i);             % Takes each value in X direction
        G(i,j) = exp(-(x.^2+y.^2)./(2.*s.^2));
    end
end

Gn = G./(sum(sum(G)));          % Normalization of Gaussian