%ANGLE2MATRIX   Converts the axis-angle representation into a matrix
%   angle2matrix(t,theta) uses the Rodrigues formula (Axis-Angle) for a
%   rotation matrix. First creates a skewed matrix from the rotation axis t
%   and takes the angle theta by which a point rotates. Finally uses the
%   Rodrigues rotation formula to get the rotation matrix.
%
% For futher reference see:
%   [1] Hartley, R. and Zisserman, A. Multiple View Geometry in Computer
%       Vision. Cambridge University Press. 2nd Ed. Page 585. 2004.
%   [2] Corke, Peter. Robotics, Vision and Control: Fundamental Algorithms in
%       MATLAB. Springer. Pages 33-35. 2011.
%
%   History:
%       11.09.2012. First implementation.
%       27.06.2015. Updated information.
%
% @author: Mario Garcia.
%     www.mayitzin.com

function a2m = angle2matrix(t,theta)
v = t/norm(t);
a2m = eye(3) + sind(theta)*skew(v) + (1 - cosd(theta))*skew(v)*skew(v);