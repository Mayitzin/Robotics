%SKEW creates a skew matrix out of a given vector x.
%   skew(x) needs a 3-vector x to create the skew matrix S.
function S = skew(x)
S = [ 0 -x(3) x(2); x(3) 0 -x(1); -x(2) x(1) 0 ];