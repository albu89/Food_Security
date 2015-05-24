function [ V ] = fill_zero( V )

V(V==0) = NaN;
V = inpaint_nans(V);


