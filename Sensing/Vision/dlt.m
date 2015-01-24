function H = dlt(X1,X2)

[N, n1] = size(X1);                     % Number of points

if n1 <= 2                              % If set of corrdinates has 2 columns (not normalized)
    X1 = [X1 ones(N,1)];                % Adds ones for Z coordinate (w_i)
    X2 = [X2 ones(N,1)];                % Adds ones for Z coordinate (w'_i)
end

%% Computation of Matrix A_i
A = zeros(2*N,9);
O = [0 0 0];
for i = 1:N
    X = X1(i,:);                        % Coordinates of points of first image
    x = X2(i,1);                        % X coordinate of second image
    y = X2(i,2);                        % Y coordinate of second image
    w = X2(i,3);                        % Z coordinate of second image
       A(2*i-1,:) = [O    -w.*X  y.*X]; % Creates elements of matrix A_i
       A(2*i  ,:) = [w.*X   O   -x.*X];
end

%% Solutions for h and get H
[S,D,V] = svd(A);                       % SVD of A ---> "h" are the last column of V
H = reshape(V(:,9),3,3)';               % Rearranges h-elements in a 3-by-3 matrix H
% H = H./H(3,3);                          % H is up-to scale