
%% Data Collection
x = 4;
%Read File
filename_y = '/Users/alexanderbusser/Food_Security/features/data_y.csv'
Y = csvread(filename_y,1,x, [1 x 689 x]);

%Set number of features and define how far into the future prediction
n_feature = 30;
pred = 4; 

%Set the range
i_start = (1+30);
i_end = size(Y) - (30);


%% Data Transformation

%Linear Interpolation 
Y = fill_zero(Y);

%Normalize [0 1]
maxVec = max(Y);
minVec = min(Y);
Y_T = (Y - min(Y)) / ( max(Y) - min(Y) ) + 0.0000001; 


%Smoothing the function 
[Y_N, gnpcycle16] = hpfilter(Y_T,1600);


%% Create Features


% Feaures x-1, x-2 .... x-30
data = window(n_feature, pred, Y_N,i_start, i_end );


% 1 week Moving Average
w = 7;
base_set = window(1, pred, Y_N,i_start-(w-1), i_end );
ma_7 = m_avg(base_set, w); 

% 2 week Moving Average
w = 14;
base_set = window(1, pred, Y_N,i_start-(w-1), i_end );
ma_14 = m_avg(base_set, w); 


% 1 month Moving Average
w = 30; 
base_set = window(1, pred, Y_N,i_start-(w-1), i_end );
ma_30 = m_avg(base_set, w);

f_space = [data(:, 1:n_feature) ma_7 ma_14 ma_30 data(:,n_feature+1)];


%% Feature Selection - Top 10  

[RANKED, WEIGHT] = relieff(f_space(:,1:end-1), f_space(:,end),300);

%Get Index of 10 Best Features
[r c] = size(f_space);
F_index = [RANKED(1:10) c];
reg_model = f_space(:,F_index);

disp(RANKED(1:10));
disp(WEIGHT(RANKED(1:10)));

