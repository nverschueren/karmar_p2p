function p=Karmainit(p,dom,nx,par,varargin)
p=stanparam(p); p.nc.neq=2; p.sw.sfem=-1;
p.sw.spjac=1; % use analytical Jacobian for spectral point cont (fold cont)
p.plot.auxdict={'D','\epsilon','nB','M','s','del','dyy','I'};

p.fuha.sG=@sG;
p.fuha.sGjac=@sGjac;
p.fuha.outfu=@karbra;

switch length(dom)
  case 1; lx=dom; p.pdeo=stanpdeo1D(lx,2*lx/nx); p.vol=2*lx; 
      p.plot.pcmp=[1 2]; p.plot.cl={'b','r'}; 
      p.dim=1;
      p.Om=2*lx;
  case 2; ny=round(dom(2)/dom(1)*nx); lx=dom(1); ly=dom(2); p.vol=4*lx*ly; 
      pde=stanpdeo2D(lx,ly,nx,ny,varargin{1}); p.pdeo=pde; p.plot.pstyle=-1; 
      p.dim=2;
      p.Om=4*lx*ly;
  case 3; lx=dom(1); ly=dom(2); lz=dom(3); h=2*lx/(nx-1);  p.vol=8*lx*ly*lz; 
      pde=stanpdeo3D(lx,ly,lz,h,varargin{1}); p.pdeo=pde; p.plot.pstyle=2; 
      p.plot.EdgeColor='none'; 
      p.dim=3;
end
p.np=p.pdeo.grid.nPoints; p.nu=p.np*p.nc.neq; p.nc.neig=30; p.nc.nsteps=50; 
p=setfemops(p); p.sol.xi=1/p.nu; p.file.smod=10; p.sw.para=2; p.sw.foldcheck=1; 
p.nc.ilam=1; p.sol.ds=-0.1; p.nc.dsmax=0.1; p.nc.lammin=0; p.sw.bifcheck=2; 
u=0*ones(p.np,1); v=0*ones(p.np,1); 
p.u=[u;v;par']; % initial solution guess with parameters
[po,tr,ed]=getpte(p); p.mesh.bp=po; p.mesh.be=ed; p.mesh.bt=tr; p.nc.ngen=1; 
p.plot.bpcmp=4; p.plot.axis='image'; p.plot.cm='hot'; p.plot.fancybd=2; 