function [XTr, yTr, XTe, yTe] = split(y, X, prop)
% split the data into train and test given a proportion
		setSeed(1);
    N = size(y,1);
		% generate random indices
		%idx = randperm(N);
    Ntr = floor(prop * N);
		% select few as training and others as testing
		%idxTr = idx(1:Ntr);
		%idxTe = idx(Ntr+1:end);
		% create train-test split
    XTr = X(1:Ntr);
    yTr = y(1:Ntr);
    XTe = X(Ntr+1:end);
    yTe = y(Ntr+1:end);
end

function setSeed(seed)
% set seed
	global RNDN_STATE  RND_STATE
	RNDN_STATE = randn('state');
	randn('state',seed);
	RND_STATE = rand('state');
	%rand('state',seed);
	rand('twister',seed);
end
