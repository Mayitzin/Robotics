% Example of the functionality of the Harris Corner Detector

close all
clc

% Initial Parameters
n = 0;
alpha = 0.04;
s0 = 1.5;                           % initial scale value
k = 1.2;                            % scale step
t = 1000000;                        % threshold

% Read the image
I = imread('harrisn.bmp');          % Grayscale values of Image in I
%I = rgb2gray(I);                    % If in color, convert to grayscale

%% Harris-Corner detector starts
% Gaussian sigmas
sigma_I = s0.*k.^n;                 % F = sigma_I = s0*k^n
sigma_D = 0.7.*sigma_I;             % Sigma of Gaussian

% Gaussians
g_D = gauss2D(sigma_D);             % Gaussian of sigma_D
g_I = gauss2D(sigma_I);             % Gaussian of sigma_I

% Derivative masks
Dx = [-1 0 1; -1 0 1; -1 0 1];      % Derivative mask over X
Dy = Dx';                           % Derivative mask over Y

% Derivatives of Gaussians
d_Gx = conv2(g_D, Dx, 'same');
d_Gy = conv2(g_D, Dy, 'same');

% Convolution of Image with derivatives of Gaussians (Laplacians)
Lx = conv2(double(I), d_Gx, 'same');
Ly = conv2(double(I), d_Gy, 'same');

% Elements of Structure Tensor Matrix
Lx2 = Lx.^2;
Ly2 = Ly.^2;
Lxy = Lx.*Ly;

% Elements of Structure Tensor smoothed with Gaussian of sigma_I
Lx2 = conv2(Lx2, g_I, 'same');
Ly2 = conv2(Ly2, g_I, 'same');
Lxy = conv2(Lxy, g_I, 'same');

% Compute the Structure Tensor Matrix
R = zeros(size(I,1),size(I,2));
for y=1:size(I,1)
    for x=1:size(I,2)
        M = [Lx2(y,x) Lxy(y,x); Lxy(y,x) Ly2(y,x)];
        R(y,x) = det(M) - alpha*trace(M)^2;
        if R(y,x) < t               % apply thresholding
            R(y,x) = 0;
        end
    end
end

% Non-maxima suppresion
Te = nonmax(R);

% Get Location of resulting points
[Y, X] = find(Te);

%% Plotting
figure(1)
subplot(2,3,1)
    imagesc(I)
    title('Original Image')
subplot(2,3,2)
    imagesc(sqrt(Lx.^2 + Ly.^2))
    title('Gradients')
subplot(2,3,3)
    imagesc(Lxy)
    title('L_{xy}')
subplot(2,3,4)
    imagesc(R)
    title('Thresholded Image')
subplot(2,3,5)
    imagesc(Te)
    title('Non-Maxima Suppresion')
subplot(2,3,6)
    imshow(I)
    hold on
    plot(X,Y,'rx');                 % Detected corners with red crosses
    title('Detected points')
    colormap(gray)                  % Uses a gray-scale to show the image