
filename_y = '/Users/alexanderbusser/Food_Security/features/data_y.csv'

Y = csvread(filename_y,1,4, [1 4 689 4]);




%Normalize [0 1]
maxVec = max(Y);
minVec = min(Y);
Y = log(Y); 
Y_T  = (Y - min(Y)) / ( max(Y) - min(Y) ) +0.000001; 

hist(price2ret(Y_T));

xlabel('Price increase in %', 'fontweight','bold','fontsize',16)
ylabel('# of Price increases','fontweight','bold','fontsize',16)
print('/Users/alexanderbusser/Food_Security/report1/img/model/p_increase_n', '-dpng') 

[Y_N, gnpcycle16] = hpfilter(Y_T,1200);

hist(price2ret(Y_N));

xlabel('Price increase in %', 'fontweight','bold','fontsize',16)
ylabel('# of Price increases','fontweight','bold','fontsize',16)
print('/Users/alexanderbusser/Food_Security/report1/img/model/p_increase_w', '-dpng') 


