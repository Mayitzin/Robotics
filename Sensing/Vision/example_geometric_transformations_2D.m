% Example of the Geometric Transformations in 2D.
%
% This code plots each geometric transformation of any given 2D figure.
% It shows them in subplots, where the blue images are the original ones
% and the red ones are the transformed images.
%
% Requires Files:
% - plotHomo.m
%
% For futher reference see:
%   [1] Hartley, R. and Zisserman, A. Multiple View Geometry in Computer
%       Vision. Cambridge University Press. 2nd Ed. pages 39-44. 2004.
%   [2] Szeliski, R. Computer Vision: Algorithms and Applications.
%       Springer, pages 35-38. 2010.
%
% History:
%     23.06.2012. First Implementation.
%     19.02.2015. Added comments.
%
% @author: Mario Garcia.
%     www.mayitzin.com

close all
p = [0 0; 1 0; 1 1; 0 1; 0.5 1.6; 1 1; 0 0; 0 1; 1 0]'; % Original Points
p_h = [p; ones(1,size(p,2))];
t = [3,-4]';                                    % Translation vector
deg = 20;                                       % Rotation in degrees

% ============ 1. Euclidean Transformations ==============

% 1.a. Translation
t_h = [eye(size(t,1)), t ; zeros(1,size(t,1)), 1];  % Homogeneous vector
T1 = t_h * p_h;                                 % Transformation Matrix

% 1.b. Rotation
r = [cosd(deg) -sind(deg);
     sind(deg)  cosd(deg)];                     % Rotation Matrix
r_h = [r, zeros(2,1);
       zeros(1,2), 1];                          % Homogeneous Rotation
T2 = r_h * p_h;                                 % Transformation Matrix

% 1.c. Rotation then Translation
T3 = t_h * r_h * p_h;                           % T (R p)

% 1.d. Translation then Rotation
T4 = r_h * t_h * p_h;                           % R (T p)

% ============ 2. Affine Transformations ==============

% 2.a. Stretching (Parallel lines remain).
A = [1    2   0;
     0.5  3   0;
     0    0   1] * p_h;

% 2.b. Some random numbers in the upper left diagonal.
PA = [1    -2     1;
      0    1.5 -0.5;
      0    0      1] * p_h;

% ============ 3. Projective Transformations ==============

% 3.a. Modified only last row.
B = [1    0    0;
     0    1    0;
     0.3  0.5  1] * p_h;

% 3.b. Isotropic scaling. Nothing changes because 9th element is not 1.
C = [4  0  0;
     0  4  0;
     0  0  4] * p_h;

% ============ PLOTTING ==============

subplot(3,3,1);
    plotHomo(p_h,'b');
    title('Translation')
    hold on
    plotHomo(T1,'r');
    hold off
subplot(3,3,2);
    plotHomo(p_h,'b');
    title('Rotation')
    hold on
    plotHomo(T2,'r');
    hold off
subplot(3,3,3);
    plotHomo(p_h,'b');
    title('Rotation > Translation')
    hold on
    plotHomo(T3,'r');
    hold off
subplot(3,3,4);
    plotHomo(p_h,'b');
    title('Translation > Rotation')
    hold on
    plotHomo(T4,'r');
    hold off
subplot(3,3,5);
    plotHomo(p_h,'b');
    title('Stretch')
    hold on
    plotHomo(A,'r');
    hold off
subplot(3,3,6);
    plotHomo(p_h,'b');
    title('New Points')
    hold on
    plotHomo(PA,'r');
    hold off
subplot(3,3,7);
    plotHomo(p_h,'b');
    title('Perspective')
    hold on
    plotHomo(B,'r');
    hold off
subplot(3,3,8);
    plotHomo(p_h,'b');
    title('Isotropic Scaling')
    hold on
    plotHomo(C,'r');
    hold off