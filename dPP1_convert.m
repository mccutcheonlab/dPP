
[folder, name, ext] = fileparts(which(mfilename('fullpath')));

folder = 'R:\DA_and_Reward\gc214\dPP1\'

tankfolder = strcat(folder, 'tdt files\');
savefolder = strcat(folder, 'matfiles\');

skipfiles = 1;
processfiles = 0;
nboxes = 2;

metafile = strcat(folder,'dPP1_expdetails.xlsx');
sheet = 'metafile';
[~,~,a] = xlsread(metafile,sheet);

TDTmasterconvert3(a, tankfolder, savefolder,...
     skipfiles, processfiles);

%%%
% for testing
% tic
% clear all; close all;
% tank = 'R:\DA_and_Reward\Shared\Scripts\THPH Tanks\Kate-170810-072909'
% data = TDTbin2mat(tank);
% toc
% 
% tic
% clear all; close all;
% tank = 'C:\Users\James Rig\Documents\Test data\Kate-170810-072909'
% data = TDTbin2mat(tank);
% toc

% 
% tank = 'R:\DA_and_Reward\Shared\Scripts\THPH Tanks\Kate-170810-072909';
% data = TDTbin2mat(tank);
% 
% tank = 'R:\DA_and_Reward\gc214\PPP3\tdtfiles\Giulia-180709-083142';
% data = TDTbin2mat(tank);
% 
% tank = 'R:\DA_and_Reward\gc214\PPP3\tdtfiles\Giulia-180709-100216';
% data = TDTbin2mat(tank);
