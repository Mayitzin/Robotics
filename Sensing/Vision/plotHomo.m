%plotHomo   Plot of homogeneous points.
%   plotHomo(X) plots the points of matrix X. It normalizes the matrix X by
%   adding a row of ones in the bottom of it, if it is not normalized. Then
%   plots the points in the second row against the points in the first row.
%   It automatically normalizes the third row in X, in case it has any.
%   
%   X must be a m-by-n matrix, where m < n, and m is either 2 or 3.
%
% History:
%     23.06.2012. First Implementation.
%     19.02.2015. Added comments.
%
% @author: Mario Garcia.
%     www.mayitzin.com

function plotHomo(X,c)

% Color specification
if nargin < 2
    c = 'blue';
end

% Matrix size verification
[m,n] = size(X);
if m<2
    error('Matrix dimension is too small. Missing coordinates.')
elseif (n == 2 || 3) && m>n
    X_n = X';
elseif m>3 && n
    error('Matrix dimension too big.')
end

% Matrix Normalization
if m == 2
    X_n = [X; ones(1,n)];
elseif m == 3
    X_n = [X(1,:)./X(3,:); X(2,:)./X(3,:); X(3,:)./X(3,:)];
end

% Plotting
plot(X_n(1,:), X_n(2,:),c); axis equal