clear; run('~/berkeley_trabajo/newp2p/pde2path/setpde2path.m')
close all; keep pphome; 
%% 2d
keep pphome
p=[];
lx=70;
ly=5;
D=0.5; M=4; eps=0.05; nb=0.5;
dx=0.15; vel=-0.5451; del=1e-2; 
par=[D,eps,nb,M,vel,del];
nx=35;
sw.sym=2;
p=Karmainit(p,[lx,ly],nx,par,sw); % init with criss-cross mesh


%% 1d
keep pphome;
D=0.5; M=4; eps=0.05; nb=0.5;
dx=0.15;
vel=-0.5451;
del=1e-2; % diff.of 2nd compo 
dy=0.1;
p=[];lx=80;nx=500;  par=[dx,eps,nb,M,vel,del,dy]; p=Karmainit(p,lx,nx,par); 
p.nc.dsmax=0.5; p.sol.ds=-0.1; p=setfn(p,'front'); 