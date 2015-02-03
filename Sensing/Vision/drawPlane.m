function drawPlane(P, d, color)

[x,y] = meshgrid(-10:10);           % A 2D grid with values from -10 to 10
z = -(1/P(3))*(P(1)*x + P(2)*y - d);

surf(x, y, z, 'edgecolor', 'none', 'FaceColor', color);