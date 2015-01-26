%CNV returns the convoluted image J, given its original and a kernel.
%   cnv(IMAGE,H,BORDER) gets the image and applies a convolution with the
%   given M-by-N matrix H to obtain the filtered image J.
%
%   IMAGE is an M-by-N array containing the gray scale values of the
%   image to be filtered, where M is the height of the Image in pixels
%   and N is the width of the Image in pixels.
%
%   H must be an M-by-N array with odd dimensions.
%
%   BORDER is a string that specifies the method to use as the Padding
%   configuration at the borders of the image. The accepted values
%   corresponding to these user-specified parameters are:
%
%   'zero'      Creates a set of zeros around the image. The thickness of
%               the border depends on the size of the mask H.
%
%   'clamp'     Extends the values at the border lines of the image. The
%               thickness of the border depends on the size of the mask H.
%
%   'mirror'    Mirrors the values at the border lines of the image along
%               the corners of the image. The thickness of the border
%               depends on the size of the mask H.
%
% For futher reference see:
%   [1] Szeliski, R. Computer Vision: Algorithms and Applications.
%       Springer, pages 111-115. 2010.
%
%   History:
%       05.12.2012. First implementation.
%       26.01.2015. Added Comments and References.
%                   Set mirrored border as default.
%
% @author: Mario Garcia.
%     www.mayitzin.com

function J = cnv(I,H,border)

% Default value
if nargin<3
    border = 'mirror';
end

% Convolution Mask (Rotated 180deg)
H = rot90(H,2)./sum(sum(H));    % Rotates and normalizes the kernel mask

% Defines the variables to use:
[m_H, n_H] = size(H);           % Dimensions of Kernel
[m_I, n_I] = size(I);           % Dimensions of Image

%% Padding of Image
thick = floor(length(H)./2);	% Defines the thickness of the border

switch border
    case 'zero'
        I1 = [zeros(thick,n_I); I; zeros(thick,n_I)];               % Adds upper and lower borders
        I2 = [zeros(size(I1,1),thick) I1 zeros(size(I1,1),thick)];	% Adds left and right borders

    case 'clamp'
        I1 = I;                           % Temporarily stores I to I1
        for bud = 1:thick
            I1 = [I(1,:); I1; I(m_I,:)];	% Inserts upper and lower borders
        end
        I2 = I1;                          % Temporarily stores I1 to I2
        for blr = 1:thick
            I2 = [I1(:,1) I2 I1(:,size(I1,2))];	% Inserts left and right borders
        end

    case 'mirror'
        I1 = I;                           % Temporarily stores I to I1
        for t = 1:thick
            I1 = [I(t,:); I1; I(size(I,1)-t+1,:)];	% Inserts borders according to thickness
        end
        I2 = I1;
        for t = 1:thick
            I2 = [I1(:,t) I2 I1(:,size(I1,2)-t+1)];	% Inserts borders according to thickness
        end
    otherwise
        error('Please select a valid Padding')  % Shows error if no valid padding was given
end

%% Convolution
[m_I2, n_I2] = size(I2);                    % Dimensions of bordered Image
J = ones(m_I,n_I);                          % Preallocated Matrix
for j = 1:(n_I2 - n_H)+1                    % Runs over row
    for i = 1:(m_I2 - m_H)+1                % Runs through column
        M = round(sum(sum(double(H).*double(I2(i:i+m_H-1,j:j+n_H-1)))));	% Magic! (Convolution)
        J(i,j) = M;                         % Each value into J Matrix
    end
end