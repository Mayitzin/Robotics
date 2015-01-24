%ANGLE2MATRIX   Converts the axis-angle representation into a matrix
%   angle2matrix(t,theta) uses the Rodrigues formula (Axis-Angle) for a
%   rotation matrix. First creates a skewed matrix from the rotation axis t
%   and takes the angle theta by which a point rotates. Finally uses the
%   Rodrigues rotation formula to get the rotation matrix.
function a2m = angle2matrix(t,theta)
v = t/norm(t);
a2m = eye(3) + sind(theta)* skew(v) + (1 - cosd(theta))* skew(v)*skew(v);
%a2m = eye(3) + sind(theta)* skew(t) + (1 - cosd(theta))* skew(t)'*skew(t);