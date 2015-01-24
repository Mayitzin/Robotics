function draw_plane(l1,l2)
[X,Y] = meshgrid(-10:10,-10:10);

a1 = l1(1)./l1(4);
b1 = l1(2)./l1(4);
c1 = l1(3)./l1(4);
d1 = l1(4)./l1(4);
Z1 = -(a1.*X + b1.*Y + d1)./c1;
surf(X,Y,Z1);
hold on

a2 = l2(1)./l2(4);
b2 = l2(2)./l2(4);
c2 = l2(3)./l2(4);
d2 = l2(4)./l2(4);
Z2 = -(a2.*X + b2.*Y + d2)./c2;
surf(X,Y,Z2);
hold on

colormap(gray);

    x = min(X);
    y = (a2.*c1.*x - a1.*c2.*x + c1.*d2 - c2.*d1)./(b1.*c2 - b2.*c1);
    z = -(a1.*x + b1*y + d1)./c1;
plot3(x,y,z,'r');
grid on
hold on

xlabel('X-Axis')
ylabel('Y-Axis')
zlabel('Z-Axis')