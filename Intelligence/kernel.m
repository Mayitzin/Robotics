%KERNEL evaluates de covariance of two variables with a preferred kernel.
%   K = kernel(kern, x1, x2, parameters) returns a covariance matrix K
%   built between variables x1 and x2 based in the kernel specified as a
%   string in 'kern'. The 'parameters' are the different hyperparameters
%   and depend on the specified kernel.
%
%   Options for kernel functions and their hyper

function K = kernel(kern, x1, x2, p1, p2)

% Stationary covariance
r = abs(x1-x2);

if strcmp(kern, 'SE')   % Squared Exponential
    if nargin>4; error('Too many input parameters'); end
    K = p1 .* exp(-(r.^2)./2);
elseif strcmp(kern, 'GenT') % Generalized T-Distribution
    if nargin>4; error('Too many input parameters'); end
    K = 1./(1+r.^p1);
elseif strcmp(kern, 'RBF')  % Radial Basis Function
    K = p1 .* exp(-(r.^2)./(2.*p2.^2));
elseif strcmp(kern, 'Matern5/2')    % ARD Matern 5/2
    K = p1.*(1+((sqrt(5).*r)/p2)...
        +((5*r.^2)/(3.*p2))).*exp(-((sqrt(5).*r)/p1));
else
    error('No valid kernel was specified')
end