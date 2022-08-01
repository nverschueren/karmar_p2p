close all; clear; run('~/berkeley_trabajo/newp2p/pde2path/setpde2path.m')
close all; keep pphome; 
%% init 
% 1/8/22 THis is an old file. It does not work because it is missing the
% parameters I(external current) and dyy. Use cmdsHU2.m instead!
% init_cond=load('campo.dat');
D=0.5; M=4; eps=0.05; nb=0.5;
dx=0.15; vel=-0.5451; del=1e-2; % diff.of 2nd compo 
p=[];lx=80;nx=500;  par=[D,eps,nb,M,vel,del]; p=Karmainit(p,lx,nx,par); 
p.nc.dsmax=0.5; p.sol.ds=-0.1; p=setfn(p,'front'); 
%% setting ICs (for freezing)  
x=getpte(p); x0=-30; x=(x-x0)'; al=0.2; bet=0.01; t1=0; 
u=3./(cosh(al*x)+10*exp(-10*al*x)); 
v=1./(cosh(bet*x)+10*exp(-10*bet*x)); 
p.u(1:p.nu)=[u; v]; plotsol(p); 
p.u0x=p.mat.M\(p.mat.Kx*p.u(1:p.nu)); % reference profile
%% converge to pulse via freezing
nt=1e5; pmod=round(nt/50); %nt=2e2; pmod=round(nt/10); 
vmod=pmod; dt=0.001; vel=[];  
[p,t1,vel]=tintfreeze(p,t1,dt,nt,pmod,vel,vmod); 
%% cont 
p=setfn(p,'p1'); p.u(p.nu+5)=vel(2,end); % use the 'freezing' velocity 
p.u0=p.u(1:p.nu); p.u0x=p.mat.M\(p.mat.Kx*p.u(1:p.nu)); % reset reference profile 
p.nc.nq=1;p.sw.qjac=1; p.fuha.qf=@qf;p.fuha.qfder=@qfder; % switch on constraints
p.nc.ilam=[2 5]; % set active pars to eps and vel  
figure(2); clf; p.sol.ds=-1e-3; p.sw.spcalc=1; 
r=pderesi(p,p.u); r1=norm(r,'inf'), q=qf(p,p.u)
plotsol(p); %plotsolu(p,r,10,1,1); plotsolu(p,r,11,2,1); 
%%
p=cont(p,20); % continue 
%%
fnr=3;% mclf(fnr);
cmp=0;
plotbra('p1',fnr,cmp,'labi',10); 
%%
plotsol('p1','pt0',1,[1 2],1,'cl',{'b','r'}); pause 
plotsol('p1','pt10',1,[1 2],1,'cl',{'b','r'}); pause 
plotsol('p1','pt20',1,[1 2],1,'cl',{'b','r'}); 
%% cont to larger eps; -this behaves funny, growing  plateau in u1 at eps=0.097 
% probably due to the th(u-1)/nb;  there might be more in this model than
% obvious at first sight 
p=loadp('p1','pt0','p1b'); p.sol.ds=0.001; p=cont(p,10); 
%% change to cont in del=d2 
p=swiparf('p1b','pt10','b2',[6 5]); p.sol.ds=-0.001; 
%% repeat (few steps, to see when u2 starts to grow to the left) 
p.dbc=1; % switching on DBCs for u2(-lx); works. 
p=cont(p,2); 