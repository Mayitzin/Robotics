% History:
%     24.04.2014. First implementation.
%
% @author: Mario Garcia.
%     www.mayitzin.com

clear all; close all

% Define Hyperparameters
ls = 4;
sig_f = 1;
hyppar = [ls; sig_f];
% Noise Variance
sig_n = 0.3;

% Testing points
data = load('../Data/Trajectory01.txt');
x_test = (1:size(data,2)-1)';
y_test = abs(data(1,:))';
y_test = diff(y_test);
X = [x_test'; y_test'];


% Training Points
% NumPoints = 30;
% x_ind = randperm(length(x_test),NumPoints);
Y = X(:,1:8:end);

%% GP Regression
[post_mean, post_cov] = gp(X,Y,'RBF',hyppar,sig_n);
% Variance on each point
divls = diag(post_cov);
%% Bayesian Optimization (Expected Improvement)
EI = eximp(X,Y,post_mean,post_cov);

%% Plot
% Create Bounds and EI lines
ubound  = post_mean+divls.^2;
lbound  = post_mean-divls.^2;
ubound2 = post_mean + 2.*divls.^2;
lbound2 = post_mean - 2.*divls.^2;
xline = [x_test; flipud(x_test)];

% Plot Images
figure();
subplot(2,1,1)
    fill(xline, [ubound; flipud(lbound)], [0 0 1],...
        'FaceAlpha', 0.1, 'EdgeColor',[0.7 0.7 1]); hold on
    fill(xline, [ubound2; flipud(lbound2)], [0 0 1],...
        'FaceAlpha', 0.1, 'EdgeColor',[0.7 0.7 1])
    plot(Y(1,:), Y(2,:), 'ko')
    plot(x_test, post_mean, 'b-')
    xlabel('Camera Frame');
    ylabel('Velocity (Displacement Rate)'); hold off
subplot(2,1,2)
    fill(xline, [EI'; zeros(length(EI),1)], [1 0 0],...
        'FaceAlpha', 0.2, 'EdgeColor',[1 0.5 0.5])
    ylabel('Expected Improvement'); hold off




%% Recursive Improvement
trials = 4;
for i=1:trials
    % Hit enter to proceed
    pause();
    % Find Maximum of Expected Improvement
    [fnew,newpp] = max(EI);
    if any(X(1,newpp)==Y(1,:))
        msgbox('Extremum reached');
        subplot(2,1,1); hold on
        break;
    end
    newvals = X(:,newpp);
    Y = [Y newvals];
    % GP Regression
    [post_mean, post_cov] = gp(X,Y,'RBF',hyppar,sig_n);
    % Bayesian Optimization
    EI = eximp(X,Y,post_mean,post_cov);
    
    % ------ Plot ------
    xline = [x_test; flipud(x_test)];
    dicov = diag(post_cov);
    ubound  = post_mean + dicov.^2;
    lbound  = post_mean - dicov.^2;
    ubound2 = post_mean + 2.*dicov.^2;
    lbound2 = post_mean - 2.*dicov.^2;
    subplot(2,1,1)
        fill(xline, [ubound; flipud(lbound)], [0 0 1],...
            'FaceAlpha', 0.1, 'EdgeColor',[0.7 0.7 1]); hold on
        fill(xline, [ubound2; flipud(lbound2)], [0 0 1],...
            'FaceAlpha', 0.1, 'EdgeColor',[0.7 0.7 1])
        plot(Y(1,:), Y(2,:), 'ko')
        plot(x_test, post_mean, 'b-')
        if i<trials; hold off; end
    subplot(2,1,2)
        fill(xline, [EI'; zeros(length(EI),1)], [1 0 0],...
            'FaceAlpha', 0.2, 'EdgeColor',[1 0.5 0.5])
        ylabel('Expected Improvement')
end

% Extremum was found
[fmaxp,maxp] = max(post_mean);
subplot(2,1,1); plot(X(1,maxp),fmaxp,'rx');
disp(['Found: ', num2str(X(1,maxp)), '      ', num2str(fmaxp)]);