function [ output ] = m_avg( input, w)
%UNTITLED5 Summary of this function goes here
%   Detailed explanation goes here

reg_val = input(:, 1);
reg_val = tsmovavg(reg_val,'s',w,1);
output = reg_val(w:end);
%output = [reg_val input(w:end,2)];

end

