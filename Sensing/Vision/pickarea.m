function Path = pickarea()
%     colormap(gray)
%     imshow(I1);
    hold on
    inputs = ginput(2);                     % Gets 2 points with the mouse
    point1 = inputs(1,:);
    point2 = inputs(2,:);
    % Creates a rectangle with the 2 points
        a = [point1(1,1) point1(1,2)];      % Point a
        b = [point2(1,1) point1(1,2)];      % Point b
        c = [point1(1,1) point2(1,2)];      % Point c
        d = [point2(1,1) point2(1,2)];      % Point d
    Path = [a; b; d; c; a];                 % Rectangle