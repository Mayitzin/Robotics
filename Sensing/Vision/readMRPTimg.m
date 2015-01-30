%READMRPTIMG reads images from MRPT Dataset
% images = readMRPTimg(D, N, camera, maindir) reads a series of images from
% an MRPT dataset and returns them in a cell array.
%
%   D is an integer defining which Dataset is intended to be used.
%
%   N is the number of images to be read. Default reads all images in the
%   folder.
%
%   camera is a string defining which Camera is used. Possible options are
%   'left' for the left camera and 'right' for the right camera. Default
%   camera is 'left'.
%
%   maindir is a string defining the main directory. Default is the local
%   directory.
%
%   Example of a valid path:
%       './images/MRPT_dataset_01/list_of_images.txt'
%
%   History:
%       16.02.2014. First implementation.
%
%   @author: Mario Garcia
%   Technische Universitaet Muenchen

function images = readMRPTimg(D, N, camera, maindir)

% Check selected MRPT Dataset
if D>9
    a = 'images/MRPT_dataset_';
elseif D<=9
    a = 'images/MRPT_dataset_0';
elseif D<0
    error('You do not have the specified dataset. Check your directory');
end

% Set Default values
if nargin<4
    maindir = './';
end
if nargin<3
    camera = 'left';
end
if nargin<2
    fpath = [a, num2str(D), '/'];
    N = length(dir(fpath))-2;
end

% Build path name for each image
filePath = [maindir, a, num2str(D), '/list_of_images2.txt'];

% file = './images/MRPT_dataset_01/list_of_images.txt';
% disp('Retreiving list of images...');
lista = importdata(filePath, ' ');
if N > length(lista)/2
    error('You want more images than the existing.')
end

images = cell(N, 1);

% Read images from files.
step = 2;
if strcmp('left', camera)
    for i=1:N
        images{i} = double(rgb2gray(imread(lista{i*step-1})));
    end
elseif strcmp('right', camera)
    for i=1:N
        images{i} = double(rgb2gray(imread(lista{i*step})));
    end
else
    error('No valid camera was specified')
end