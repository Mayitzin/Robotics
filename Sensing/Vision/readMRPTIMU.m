%READKITTIIMG reads calibrations from KITTI Dataset
% K = readKITTIimg(fileName) reads the information in a KITTI calibration
% file and returns its values in a cell array.
%
%   fileName is a string defining the name and location of the file.
%
%   Format:
%     [01] Time
%     [02] IMU_X_ACC
%     [03] IMU_Y_ACC
%     [04] IMU_Z_ACC
%     [05] IMU_YAW_VEL
%     [06] IMU_PITCH_VEL
%     [07] IMU_ROLL_VEL
%     [08] IMU_X_VEL
%     [09] IMU_Y_VEL
%     [10] IMU_Z_VEL
%     [11] IMU_YAW
%     [12] IMU_PITCH
%     [13] IMU_ROLL
%     [14] IMU_X
%     [15] IMU_Y
%     [16] IMU_Z 
%
%   Example of a valid path:
%       '.\images\KITTI_dataset_02\2011_09_26\calib_cam_to_cam.txt'
%
%   History:
%       22.05.2014. First implementation.
%
%   @author: Mario Garcia
%   Technische Universitaet Muenchen

function data = readMRPTIMU(fileName)

data = load(fileName);