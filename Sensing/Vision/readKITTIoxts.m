%READKITTIIMG reads calibrations from KITTI Dataset
% [A, v, times] = readKITTIoxts(Path) reads the information in a KITTI OXTs
% file and returns its values in matrices.
%
%   fileName is a string defining the name and location of the file.
%
%   K is a cell array with the four intrinstic matrices. One for each
%   camera used in the setup.
%
%   R is a cell array with the four rotation matrices. The first camera is
%   set to the origin and the rotations of the other three are with respect
%   to the first camera.
%
%   Rr is a cell array with the four rotation matrices used for the
%   rectified images. The first camera is set to the origin and the
%   rotations of the other three are with respect to the first camera.
%
%   T is a cell array with the four translation vectors. The first camera
%   is considered at the origin and the other three cameras are translated
%   with respect to this origin.
%
%   Example of a valid path:
%       '.\images\KITTI_dataset_02\oxts\'
%
%   History:
%       25.01.2014. First implementation.
%
%   @author: Mario Garcia
%   Technische Universitaet Muenchen

function [A v times] = readKITTIoxts(Path)

N = length(dir(Path))-2;

% Read Time Stamps
fileTimes = [Path, '..\timestamps.txt'];
fileID = fopen(fileTimes);
T = textscan(fileID, '%s %s');
fclose(fileID);
% Save times in an N-by-1 vector
timeCell = T{2};
times = zeros(N,1);
for n=1:N
    temp = cell2mat(textscan(timeCell{n}, '%f %f %f', 'delimiter', ':'));
    times(n) = temp(1).*3600 + temp(2).*60 + temp(3);
end

% Number the files
indices = cell(N,1);
for i=1:N
    if i<11
        indices{i} = ['000000000', num2str(i-1)];
    elseif i>=11 && i<101
        indices{i} = ['00000000', num2str(i-1)];
    elseif i>=101 && i<1001
        indices{i} = ['0000000', num2str(i-1)];
    elseif i>=1001 && i<10001
        indices{i} = ['000000', num2str(i-1)];
    else
        error('Index of images is out of boundaries');
    end
end

% Build path name for each file
fileNames = cell(N,1);
for n=1:N
    fileNames{n} = [Path, indices{n}, '.txt'];
end

% Read Data
A = zeros(30,N);
v = zeros(3,N);
for n=1:N
    A(:,n) = load(fileNames{n})';
    v(:,n) = A(9:11,n);
end