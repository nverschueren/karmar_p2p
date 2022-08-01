close all; clear;
run('~/berkeley_trabajo/newp2p/pde2path/setpde2path.m'); % adapt to your own
keep pphome; 
%% 2d
p=[]; lx=40; ly=15;
D=0.5; M=4; eps=0.05; nb=0.5; vel=-0.5451; del=0.1; dyy=0.5; 
Inten=0; %Intensity parameter on the rhs of the function for the 1st comp.
par=[D,eps,nb,M,vel,del,dyy,Inten];
nx=150; sw.sym=1;
p=Karmainit(p,[lx,ly],nx,par,sw); % init with criss-cross mesh
plotsol(p,1,1,0); p=setfn(p,'2d0'); 

%% setting ICs (for freezing)  
po=getpte(p); x=po(1,:); y=po(2,:); x0=-25; x=(x-x0)'; al=0.2; bet=0.01; t1=0; 
u=3./(cosh(al*x)+10*exp(-10*al*x)); 
v=1./(cosh(bet*x)+10*exp(-10*bet*x)); 
p.u(1:p.nu)=[u; v]; plotsol(p); 
p.u0x=p.mat.M\(p.mat.Kx*p.u(1:p.nu)); % reference profile
%% converge to pulse via freezing
nt=2e4; pmod=round(nt/50); vmod=pmod; dt=0.0025; vel=[];  
[p,t1,vel]=tintfreeze2d(p,t1,dt,nt,pmod,vel,vmod); p0=p; 
%%  setting the phase conditions
p=p0;
p=setfn(p,'p2'); p.u(p.nu+5)=vel(2,end); % use the 'freezing' velocity 
p.u0=p.u(1:p.nu); p.u0x=p.mat.M\(p.mat.Kx*p.u(1:p.nu)); % reset reference profile 
p.nc.nq=1;p.sw.qjac=1; p.fuha.qf=@qf;p.fuha.qfder=@qfder; % switch on constraints
p.nc.ilam=[2 5]; % set active pars to eps and vel  
figure(2); clf; p.sol.ds=-1e-3; p.sw.spcalc=1; 
r=pderesi(p,p.u); r1=norm(r,'inf'), q=qf(p,p.u)
plotsol(p); %plotsolu(p,r,10,1,1); plotsolu(p,r,11,2,1); 
%% cont
p.plot.bpcmp=0; p=cont(p,2); 
%% some useful commands to identify bdries ... 
p.pdeo.grid.identifyBoundarySegment(4);  p.pdeo.grid.p(:,p.idx1)
%% cont to del=0
p=swiparf('p2','pt2','b2',[6 5]); p.sol.ds=-0.01; p.dbc=1; 
p.usrlam=[0];
p=cont(p,10); 
% %% 1d
% keep pphome;
% D=0.5; M=4; eps=0.05; nb=0.5;
% dx=0.15;
% vel=-0.5451;
% del=1e-2; % diff.of 2nd compo 
% dy=0.1;
% p=[];lx=80;nx=500;  par=[dx,eps,nb,M,vel,del,dy]; p=Karmainit(p,lx,nx,par); 
% p.nc.dsmax=0.5; p.sol.ds=-0.1; p=setfn(p,'front');

%% 
close all
p=swiparf('b2','pt6','dyt',[7 5]);
p.file.smod=2;
p=cont(p,10)
%% lets have a look
close all; keep pphome
plotbra('dyt','labi',2,'cmp',0)
%% components:
%0 (or default) L_2-Norm, 
%1-8 parameters:
%{1:'D',2:'\eps',3:'nB',4:'M',5:'s',6:'del',7:'dyy',8:'I'};
% 9: L_2 Norm of u only (not v)
% 10: max of u (not v)
% 11: min of u (not v)
% 12: L_2-Norm of u(x) when y=y0 (y0=0 for now).

plotbra('dyt','labi',2,'cmp',9)
p=loadp('dyt','pt8')
plotsol(p)
ploy0(p,0,12)
