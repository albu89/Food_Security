function [ trn_data ] = window(w_length, pred, Y, i_start, i_end)
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here

%If w_length = ( then we have x, x-1, x-2, x-3, x-4, x-5, x-6, x-7 )

[data_length, test] = size(Y(i_start:i_end));
%data_length = data_length - (i_star +i_end);
disp(data_length)
features = zeros(data_length  , w_length);
[r, c] = size(features); 
trn_data = zeros(r,c+1); 
pred_value = zeros(r,1); 



%Create X features 
count = 1;
for i = 1:(w_length)
    a = i; 
    b = (data_length-1) + i;
    features(:,i) = Y(i_start-w_length +a  :b+i_start-w_length ) ; 
    if w_length == i
        trn_data = [features Y(i_start - w_length+ a + pred:i_start - w_length + b+pred)];
        count = count+1;    
    end
    
end


