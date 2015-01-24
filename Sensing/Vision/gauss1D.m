function [Gx,Gy,X] = gauss1D(s)
X = -floor(s.*3./2):floor(s.*3./2);
Gx = zeros(1,size(X,2));    % Prelocation of Matrix
for i = 1:size(X,2)         % Jumps between columns
    x = X(i);               % Takes each value in X direction
    Gx(i) = exp(-(x.^2)./(2.*s.^2));
end
Gx = Gx./sum(Gx);           % Normalization of Gaussian

% 1D Gaussian in Y
Gy = Gx';