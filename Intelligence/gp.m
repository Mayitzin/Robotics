function [pmf pcf] = gp(X,Xs,kern,params,noise)

if nargin<5
    noise = 0;
end
if strcmp(kern,'RBF')
    if length(params)~=2
        error('Two hyperparameters must be specified for an RBF kernel');
    end
elseif strcmp(kern,'GenT')
    if length(params)>1
        error('One hyperparameter must be specified for a Generalized T-Distribution kernel');
    end
end

% Define Hyperparameters
ls = params(1);
sig_f = params(2);
sig_n = noise;
% Testing points
x_test = X(1,:)';
% Prelocate Pairs of points
[xx1   xx2]   = meshgrid(Xs(1,:), Xs(1,:));
[xxs1  xxs2]  = meshgrid(Xs(1,:), x_test);
[xsxs1 xsxs2] = meshgrid(x_test, x_test);
% Calculate elements of Covariance Matrix
Kxx   = kernel(kern, xx1,   xx2,   sig_f, ls);
Kxxs  = kernel(kern, xxs1,  xxs2,  sig_f, ls);
Kxsxs = kernel(kern, xsxs1, xsxs2, sig_f, ls);
Kxx_n = Kxx + sig_n^2.*eye(size(Kxx));
% Cholesky decomposition of noisy K(X,X)
L = chol(Kxx_n);
% Posterior Mean
pmf = (Kxxs/L)/L' * Xs(2,:)';
% Posterior Covariance
pcf = Kxsxs - (Kxxs/L)/L' * Kxxs';