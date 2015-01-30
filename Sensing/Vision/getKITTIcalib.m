%GETKITTICALIB reads calibrations from KITTI Dataset
% K = getKITTIcalib(fileName) reads the information in a KITTI calibration
% file and returns its values in a cell array.
%
%   fileName is a string defining the name and location of the file.
%
%   P is a cell array with the two camera matrices given in the calibration
%   files.
%
%   Example of a valid path:
%       '.\images\KITTI_dataset_01\calib\000037.txt'
%
%   History:
%       12.04.2014. First implementation.
%
%   @author: Mario Garcia
%   Technische Universitaet Muenchen

function [P K] = getKITTIcalib(fileName)

% Length of the file (Number of lines)
L = 2;

% Read Calibrations
file = fopen(fileName);

% Array for lines
lines = cell(L,1);

% Arrays and initial values to store data
P  = cell(2,1);   p = 1;
% Read and store data
for l=1:L
    % Read each line of text
    lines{l} = fgetl(file);
    
    % Get values of Camera Matrices (P)
    if strncmp(lines{l},'P',1)
        Kt = textscan(lines{l}, '%s %f %f %f %f %f %f %f %f %f %f %f %f');
        P{p} = reshape(cell2mat(Kt(2:13)), 4, 3)';
        p = p+1;
    end
end

% Close File
fclose(file);

% Get Calibration from Camera Matrix 1
K = P{1}(1:3,1:3);