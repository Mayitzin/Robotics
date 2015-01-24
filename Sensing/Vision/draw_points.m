%DRAW_POINTS draws a point in P2
%   draw_points(X) takes as input the non-homogeneous representation of a
%   point in a vector of a form X = [a b]' and draws its P2 representation
%   in R3.
function draw_points(X)
X_h = [X; 1];
    x = [0 X_h(1,1)];
    y = [0 X_h(2,1)];
    z = [0 X_h(3,1)];
plot3(x,y,z,'r');