function getplane(p1n,p2n)
[X,Y] = meshgrid(-8:8,-8:8);

p1 = [p1n(1)./p1n(3) p1n(2)./p1n(3) p1n(3)./p1n(3)]';   % Homogeneous Point 1
p2 = [p2n(1)./p2n(3) p2n(2)./p2n(3) p2n(3)./p2n(3)]';   % Homogeneous Point 2
p3 = [0 0 0]';                                          % Camera Center (Origin)

p = [cross((p1-p3),(p2-p3)); -p3'*cross(p1,p2)];        % Parameters of Plane
Z = -(p(1).*X + p(2).*Y + p(4))./p(3);                  % Z of Plane

surf(X,Y,Z,'edgecolor','none');                         % Plots Plane, no grid
    colormap(gray);                                     % Gray scale
    xlabel('X-Axis')
    ylabel('Y-Axis')
    zlabel('Z-Axis')
hold on

surf(X,Y,ones(length(min(X))));                         % Plots Projection Plane P2

% Following is just extra visualization:
% Given points in R3:
points = [p1n p2n];
scatter3(points(1,:),points(2,:),points(3,:),10,'b')

% Projected points in P2:
pp = [p1 p2];
scatter3(pp(1,:),pp(2,:),pp(3,:),10,'r')

% Lines from Camera Center (Origin) to points in R3:
    xp1 = [0 p1n(1)];
    yp1 = [0 p1n(2)];
    zp1 = [0 p1n(3)];
plot3(xp1,yp1,zp1,'r');
    xp2 = [0 p2n(1)];
    yp2 = [0 p2n(2)];
    zp2 = [0 p2n(3)];
plot3(xp2,yp2,zp2,'r');

% Line in P2 between projected points:
plot3([pp(1,1) pp(1,2)],[pp(2,1) pp(2,2)],[1 1],'r');

% Visualize the Camera Center (Origin):
scatter3(0,0,0,10,'g')
    x1 = [0 max(max(X))./4];
    y1 = [0 0];
    z1 = [0 0];
plot3(x1,y1,z1,'g');
    x2 = [0 0];
    y2 = [0 max(max(X))./4];
    z2 = [0 0];
plot3(x2,y2,z2,'g');
    x3 = [0 0];
    y3 = [0 0];
    z3 = [0 max(max(X))./4];
plot3(x3,y3,z3,'g');