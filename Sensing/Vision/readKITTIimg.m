%READKITTIIMG reads images from KITTI Dataset
% images = readKITTIimg(D, N, camera, maindir) reads a series of images
% from a KITTI dataset and returns them in a cell array.
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
%       '.\images\KITTI_dataset_02\image_00\data\0000000007.png'
%
%   History:
%       25.01.2014. First implementation.
%       26.01.2014. Includes first image (0000000000.png).
%                   Default reading gets all images.
%
%   @author: Mario Garcia
%   Technische Universitaet Muenchen

function images = readKITTIimg(D, N, camera, maindir)

% Check selected KITTI Dataset
if D>9
    a = 'images\KITTI_dataset_';
elseif D<=9
    a = 'images\KITTI_dataset_0';
elseif D<0
    error('You do not have a valid dataset. Please check your directory');
end

% Set Default values
if nargin<4
    maindir = '.\';
end
if nargin<3
    camera = 'left';
end
if nargin<2
    fpath = [a, num2str(D), '\image_00\data\'];
    N = length(dir(fpath))-2;
end

%% Build paths
% Select a Camera to use
if strcmp(camera, 'left')
    b = 0;
elseif strcmp(camera, 'right')
    b = 1;
else
    error('Not valid camera was selected');
end
% Number the images
indices = cell(N,1);
for i=1:N
    if i<11
        indices{i} = ['000000000', num2str(i-1)];
    elseif i>=11 && i<101
        indices{i} = ['00000000', num2str(i-1)];
    elseif i>=101 && i<1001
        indices{i} = ['0000000', num2str(i-1)];
    else
        error('Index of images is out of boundaries');
    end
end
% Build path name for each image
ImgNames = cell(N,1);
for n=1:N
    ImgNames{n} = [maindir, a, num2str(D), '\image_0', num2str(b), '\data\', indices{n}, '.png'];
end

%% Read Images
images = cell(N,1);
for i=1:N
    images{i} = double(imread(ImgNames{i}));
end