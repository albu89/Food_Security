
filename_x = '/Users/alexanderbusser/Food_Security/features/wheat/wheat_daily_volume.csv'
filename_y = '/Users/alexanderbusser/Food_Security/features/data_y.csv'

index = 46:601; 
t = (2012:1:2014)';




X = csvread( filename_x, 1,1);
Y = csvread(filename_y,1,1, [1 1 689 1]);

maxVec = max(Y);
minVec = min(Y);
Y_N = ((Y-minVec)./(maxVec-minVec) - 0.5 ) *2;

%Splitting into Train and Test 
%[XTr, yTr, XTe, yTe] = split(Y,X, 0.8);

%Splitt Train further into Train and Validation
%[XVal, yVal, XTr, yTr] = split(yTr,XTr, 0.5);

trn_data = zeros(460, 5);
chk_data = zeros(80, 5);


trn_data(:,1) = Y_N(126:585); 
trn_data(:,2) = Y_N(130:589);
trn_data(:,3) = Y_N(134:593);
trn_data(:,4) = Y_N(138:597);
trn_data(:,5) = Y_N(142:601);


chk_data(:, 1) =  Y_N(586:665);
chk_data(:, 2) =  Y_N(590:669);
chk_data(:, 3) =  Y_N(594:673);
chk_data(:, 4) =  Y_N(598:677);
chk_data(:, 5) =  Y_N(602:681);


%Generate FIS Matrix

fismat = genfis1(trn_data);


%Anfis Model 

%[trn_fismat,trn_error] = anfis([trn_data; chk_data], fismat); 
iterations = 100; 
numep=100;
[fis,trn_error,stepsize,chkFis,chk_error] = anfis(trn_data, fismat,[10],[],chk_data);




% error curves plot

epoch_n = 10;
plot([trn_error chk_error ]);
hold on; plot([trn_error chk_error], 'o'); hold off;
xlabel('Epochs','fontsize',10);
ylabel('RMSE (Root Mean Squared Error)','fontsize',10);
title('Error Curves','fontsize',10);



input = [trn_data(:, 1:4); chk_data(:, 1:4)];
anfis_output = evalfis(input, fis);
index = 142:681;

plot(index, [Y_N(index) anfis_output]);
xlabel('Time (sec)','fontsize',10);
dateFormat = t;
dateaxis('x', 12, '03/03/1999') 



