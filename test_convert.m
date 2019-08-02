clear all; close all

tank = 'R:\DA_and_Reward\gc214\dPP1\tdt files\12042019\Giulia-190412-083225'


tic
tmp = TDTbin2mat(tank, 'TYPE', {'streams'}, 'STORE', 'D1B2')
toc
% 
% tic
% tmp2 = TDTbin2mat(tank)
% toc
% 
tic
ttls = TDTbin2mat(tank, 'TYPE', {'streams'}, 'STORE', {'D1B2', 'D2B2'})
toc

