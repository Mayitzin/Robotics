function EI = eximp(X,Y,means,post_cov,extrema)

if nargin<5
    extrema = 'max';
end

% Posterior Covariance
covs = diag(post_cov);
% Number of Observations
n = size(X,2);
% Get xplus
if strcmp(extrema,'max')
    fxp = max(Y(2,:));
elseif strcmp(extrema,'min')
    fxp = min(Y(2,:));
else
    error('No valid extremum was specified');
end
% Compute Expected Improvement
EI = zeros(1,n);
for i=1:n
    if covs(i)>0
        EI(i)=(means(i)-fxp)*normcdf(means(i),fxp,covs(i))...
              +covs(i)*normpdf(means(i),fxp,covs(i));
    elseif covs(i)==0
        EI(i)=0;
    end
end