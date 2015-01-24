%DRAW_LINES takes as input the parameters of a line in P2 or two points in
%   P2 passing through a line and plots the samples of the P2 line in R3.
%
%   draw_lines(X) takes the parameters of the vector X creating a line
%   such as its parameters are defined as X = [a b c]' and plots a plane
%   containing this line and the camera center.
%
%   draw_lines(X,Y) takes the parameters of the 3-vectors X and Y defining
%   two points in the form X = [x1 y1 z1] and Y = [x2 y2 z2], creates a
%   line in P2 passing through these 2 points, and plots a plane containing
%   these 2 points and the camera center.

function draw_lines(a,b)
    [X,Y] = meshgrid(-10:1:10);     % Creates values of X and Y for a plane
    
switch nargin
    case 1
        %% Give a line ----> shows intersecting plane
        p = [a; 1];
        %p = [a(1)./a(4) a(2)./a(4) a(3)./a(4) a(4)./a(4)]';
        
        dist = -p(3)./norm(p(1:3));
        %dist = -p(4);
        Z = -(p(1).*X + p(2).*Y + dist)./p(3);      % Z = -(Ax + By + d/n) / C
        surf(X,Y,Z,'edgecolor','none');             % Plots Plane, no grid
            colormap(gray);                         % Gray scale
            xlabel('X-Axis')
            ylabel('Y-Axis')
            zlabel('Z-Axis')
        hold on

    case 2
        %% Give 2 points ----> shows plane joining them
        % Easy way:
        % p = cross(a,b);
        p1 = [a(1)./a(3) a(2)./a(3) a(3)./a(3)]';   % Homogeneous Point 1
        p2 = [b(1)./b(3) b(2)./b(3) b(3)./b(3)]';   % Homogeneous Point 2
        p3 = [0 0 0]';                              % Camera Center (Origin)
        p = [cross((p1-p3),(p2-p3)); -p3'*cross(p1,p2)];	% Parameters of Plane
        
        Z = -(p(1).*X + p(2).*Y + p(4))./p(3);      % Z = -(Ax + By + D) / C
        surf(X,Y,Z,'edgecolor','none');             % Plots Plane, no grid
            colormap(gray);                         % Gray scale
            xlabel('X-Axis')
            ylabel('Y-Axis')
            zlabel('Z-Axis')
        hold on

    otherwise
        error('Insufficient arguments');
end

        x = min(X);                                 % Lists values of x for a line
        z = ones(length(x));                        % Line lies on Z = 1
        y = -(p(1).*x + p(3))./p(2);                % y = -(ax + c)/b
        plot3(x,y,z,'r');                           % Plots a 3D line in P2
        grid on
