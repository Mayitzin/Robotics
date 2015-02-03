% This example will generate a linear equation system with 3 random
% equations, then will plot their planes and the intersecting point of
% the planes to show the solution of the equation system, if any.
%
% Requires Files:
% - drawPlane.m
%
% For futher reference see:
%   [1] Garcia, M. A fancy visualization of planes intersecting.
%       http://mayitzin.com/?s=planes+intersecting.
%   [2] Hartley, R. and Zisserman, A. Multiple View Geometry in Computer
%       Vision. Cambridge University Press. 2nd Ed. pages 67-68. 2004.
%
%   History:
%       03.07.2013. First implementation.
%       02.02.2015. Added comments and references.
%
% @author: Mario Garcia.
%     www.mayitzin.com

close all

% Generate random parameters and values
P = rand(3);      % 3-by-3 matrix P with parameters of each plane
d = rand(3,1);

% Solve for x
x = P\d;

% Graph Planes and Solution
hold on
drawPlane(P(1,:), d(1), [0.9 0.7 0.7])  % First plane (Pink)
drawPlane(P(2,:), d(2), [0.7 0.9 0.7])  % Second plane (Green)
drawPlane(P(3,:), d(3), [0.7 0.7 0.9])  % Third plane (Blue)
scatter3(x(1), x(2), x(3))
    xlabel('x')
    ylabel('y')
    zlabel('z')
    grid on

% Display results in Command Window
disp('Equation System:')

for i=1:3
    disp(['  ', num2str(P(i,1)), 'x + ', num2str(P(i,2)), 'y + ',...
        num2str(P(i,3)), 'z = ', num2str(d(i))])
end

disp('The intersecting point (solution) lies on:')
disp(['  x = ', num2str(x(1))])
disp(['  y = ', num2str(x(2))])
disp(['  z = ', num2str(x(3))])