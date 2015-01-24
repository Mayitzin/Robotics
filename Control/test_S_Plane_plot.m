% Test S-Plane plotting

clear all

% Handmade by me
% syms s roots
% K = 5;
% 
% S = zeros(3,K*10+1);
% for k = 0:0.1:K
%     equation = s^3 + 4*s^2 + k*s + 1 == 0;
%     S(:,uint8(k*10+1)) = solve(equation);
% end
% 
% hold on
% plot(real(S(1,:)), imag(S(1,:)), 'Color', 'red')
% plot(real(S(2,:)), imag(S(2,:)), 'Color', 'blue')
% plot(real(S(3,:)), imag(S(3,:)), 'Color', 'green')
% axis on
% grid on
% xlabel('Real')
% ylabel('Imaginary')


% With Matlab

Output = [1];
Input = [1 2 -2];

H = tf(Output, Input)

% Plots
% rlocus(H)
% sgrid
pzmap(H)
grid on
% iopzmap(H)