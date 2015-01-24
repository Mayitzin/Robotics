function H = dltnorm(X1,X2)

N = length(X1);                     % Number of points

%% Normalization of Points
X1 = [X1 ones(N,1)];                % Adds ones for Z coordinate (w_i)
X2 = [X2 ones(N,1)];                % Adds ones for Z coordinate (w'_i)

n = size(X1,2);                     % Width of first set of points

% Obtaining the centroid of points in each image
X1_avg = mean(X1,1);                % Coordinates of centroid in first image
X2_avg = mean(X2,1);                % Coordinates of centroid in second image

% Average distance of the shifted points to the centroid
avg1 = 0;
avg2 = 0;
for i=1:n
    avg1 = sqrt((X1(i,1)-X1_avg(1,1)).^2 + (X1(i,2)-X1_avg(1,2)).^2) + avg1;
    avg2 = sqrt((X2(i,1)-X2_avg(1,1)).^2 + (X2(i,2)-X2_avg(1,2)).^2) + avg2;
end
d1_avg = avg1/N;
d2_avg = avg2/N;

% Average distance to origin is = sqrt(2)
s1 = sqrt(2)/d1_avg;
s2 = sqrt(2)/d2_avg;

% Similarity Transformations
T = [s1  0   -s1*X1_avg(1,1);       % Similarity Transformation of first image
     0   s1  -s1*X1_avg(1,2);       % Changes coordinate system and scales
     0   0          1      ];
U = [s2  0   -s2*X2_avg(1,1);       % Similarity Transformation of second image
     0   s2  -s2*X2_avg(1,2);       % Changes coordinate system and scales
     0   0          1      ];

% Transformation is applied to each of the two set of points independently
X1 = (T*X1')';
X2 = (U*X2')';

%% Normal Computation of DLT
Hn = dlt(X1,X2);

%% Denormalization of H~
H = U\Hn*T;
H = H./H(3,3);