function [J] = medianfilter(I,region)

[m_I, n_I] = size(I);               % Dimensions of Image
n = floor(region./2);               % Size of desired region
J = I;                              % Matrix the same size as final image

for j = 1:(n_I - n)                    % Runs over row
	for i = 1:(m_I - n)                % Runs through column
        M = sort(sort(I(j:j+n,i:i+n),1),2);
        J(j,i) = M(ceil(size(M,1)./2),ceil(size(M,2)./2));	% Adds every value to the new J Matrix
	end
end