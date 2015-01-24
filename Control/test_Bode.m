% Test Bode Parameters

clear all

% w = 20;
% G = (25*w^2+1)/(2500*w^2+1);
% A = 20*log10(G);

w = -10:0.1:10;
d = atand(w);
plot(w, d);


N = [15 10 1];
D = [50 1 0];

G = tf(N, D);

figure
h = bodeplot(G);

