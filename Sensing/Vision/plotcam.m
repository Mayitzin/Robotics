%PLOTCAM    Plot cameras in 3-D space.
%   plotcam(M) takes the matrix of the extrinsic parameters of the camera
%   model and plots the camera at the corresponding pose specified by the
%   parameters in the matrix.
%
%   M is the 3-by-4 matrix [R|T] containing the 6 parameters needed to
%   specify the pose of the camera in 3-D space.
%
% History:
%     12.05.2012. First Implementation.
%     13.07.2015. Fixed references and comments.
%
% @author: Mario Garcia
%     www.mayitzin.com

function plotcam(M)

if size(M)==[3 4]           % [R|T] is given as a 3-by-4 matrix
    % 3D structure of Camera (for visual purposes)
    Cam = [ 0    0   0  1;
          -0.5  0.5  1  1;
          -0.5 -0.5  1  1;
            0    0   0  1;
           0.5  0.5  1  1;
           0.5 -0.5  1  1;
          -0.5 -0.5  1  1;
            0    0   0  1;
           0.5 -0.5  1  1;
           0.5  0.5  1  1;
          -0.5  0.5  1  1]';
    % Transformed position and Orientation
    Camt = M*Cam;
    plot3(Camt(1,:), Camt(2,:), Camt(3,:));
    
else                        % Error if dimensions are not correct
    error('Extrinsic calibration must be a 3-by-4 matrix')
end
    hold on; grid on
    scatter3(M(1,4), M(2,4), M(3,4), 'red');