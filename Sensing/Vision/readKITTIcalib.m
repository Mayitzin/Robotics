%READKITTIIMG reads calibrations from KITTI Dataset
% K = readKITTIimg(fileName) reads the information in a KITTI calibration
% file and returns its values in a cell array.
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
%       '.\images\KITTI_dataset_02\2011_09_26\calib_cam_to_cam.txt'
%
%   History:
%       25.01.2014. First implementation.
%
%   @author: Mario Garcia
%   Technische Universitaet Muenchen

function [K R Rr T] = readKITTIcalib(fileName)

% Length of the file (Number of lines)
L = 34;

% Read Calibrations
file = fopen(fileName);

% Array for lines
lines = cell(L,1);

% Arrays and initial values to store data
K  = cell(4,1);   k  = 1;
R  = cell(4,1);   r  = 1;
Rr = cell(4,1);   rr = 1;
T  = cell(4,1);   t  = 1;
% Read and store data
for l=1:L
    % Read each line of text
    lines{l} = fgetl(file);
    
    % Get values of Intrinsic Matrices (K)
    if strncmp(lines{l},'K',1)
        Kt = textscan(lines{l}, '%s %f %f %f %f %f %f %f %f %f');
        K{k} = reshape(cell2mat(Kt(2:10)), 3, 3)';
        k = k+1;
    end
    % Get values of Extrinsic Matrices (R)
    if strncmp(lines{l},'R_0',3)
        Rt = textscan(lines{l}, '%s %f %f %f %f %f %f %f %f %f');
        R{r} = reshape(cell2mat(Rt(2:10)), 3, 3)';
        r = r+1;
    end
    % Get values of Extrinsic Matrices (R) of rectified images
    if strncmp(lines{l},'R_r',3)
        Rt = textscan(lines{l}, '%s %f %f %f %f %f %f %f %f %f');
        Rr{rr} = reshape(cell2mat(Rt(2:10)), 3, 3)';
        rr = rr+1;
    end
    % Get values of Translation (T)
    if strncmp(lines{l},'T',1)
        Tt = textscan(lines{l}, '%s %f %f %f');
        T{t} = reshape(cell2mat(Tt(2:4)), 3, 1);
        t = t+1;
    end
end

% Close File
fclose(file);