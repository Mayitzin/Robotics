%GETPLANE returns estimates the parameters of a plane.
%   cnv(IMAGE,H,BORDER) gets the image and applies a convolution with the
%   given M-by-N matrix H to obtain the filtered image J.
%
% For futher reference see:
%   [1] Hartley, R. and Zisserman, A. Multiple View Geometry in Computer
%       Vision. Cambridge University Press. 2nd Ed. pages 66-67. 2004.
%
%   History:
%       11.09.2012. First implementation.
%       26.01.2015. Added Comments and References.
%                   Visualization is optional.
%                   Third point is the Origin, when only two are given.
%
% @author: Mario Garcia.
%     www.mayitzin.com

function p = getplane(x1n,x2n,x3n,visual)

% Default values
if nargin<4
    visual = 'True'; end
if nargin<3
    x3n = [0 0 0 1]'; end
% Normalize if points are in 4-element vector
if length(x1n)==4
    x1n = [x1n(1)./x1n(4) x1n(2)./x1n(4) x1n(3)./x1n(4)]'; end
if length(x2n)==4
    x2n = [x2n(1)./x2n(4) x2n(2)./x2n(4) x2n(3)./x2n(4)]'; end
if length(x3n)==4
    x3n = [x3n(1)./x3n(4) x3n(2)./x3n(4) x3n(3)./x3n(4)]'; end

% Prelocation of Plane
[X,Y] = meshgrid(-2:0.1:2,-2:0.1:2);

% Computation of parameters of Plane
p = [cross((x1n-x3n),(x2n-x3n)); -x3n'*cross(x1n,x2n)];

%% Visualization
if strcmp(visual,'True')
    figure();            % New Window to show plots
    hold off
    % Solve to get Z (Coordinates in Z)
    a = p(1);
    b = p(2);
    c = p(3);
    d = p(4);
    Z = -(a.*X + b.*Y + d)./c;
    % Plot the Surface
    surf(X,Y,Z,'edgecolor','none');  % Plots Plane, no grid
        colormap(gray);              % Gray scale
        xlabel('X-Axis')
        ylabel('Y-Axis')
        zlabel('Z-Axis')
    hold on

    % Points in P2:
    pp = [x1n x2n x3n];
    scatter3(pp(1,:),pp(2,:),pp(3,:),10,'r','filled')

    % Visualize the Camera Center (Origin)
    scatter3(0,0,0,10,'k','filled')
        x1 = [0 max(max(X))./4];
        y1 = [0 0];
        z1 = [0 0];
    plot3(x1,y1,z1,'r');
        x2 = [0 0];
        y2 = [0 max(max(X))./4];
        z2 = [0 0];
    plot3(x2,y2,z2,'g');
        x3 = [0 0];
        y3 = [0 0];
        z3 = [0 max(max(X))./4];
    plot3(x3,y3,z3,'b');
end