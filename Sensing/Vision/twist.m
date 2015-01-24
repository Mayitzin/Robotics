function exi = twist(xi)

% Check for correct size
if ((size(xi,1) ~= 6) || (size(xi,2) ~= 1))
    error('Twist corrdinates must be of 6-by-1 Dimension')
end

% "De-stack" the vectors v and w
v = xi(1:3);
w = xi(4:6);

% Skewed and normalized w
w_s = [ 0 -w(3) w(2); w(3) 0 -w(1); -w(2) w(1) 0 ];
w_n = norm(w);

% Check value of normalized w
if (w_n == 0)
    R = eye(3);
    T = v;
else
    R = rodrigues(w);
    T = ((eye(3)-R)*w_s*v + w*w'*v)./(w_n);
end

exi = [R T; zeros(1,3) 1];