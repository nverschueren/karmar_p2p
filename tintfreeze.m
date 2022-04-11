% adapted from tints to freeze the translation symmetry
function [p,t1,vel]=tintfreeze(p,t0,dt,nt,pmod,vel,vmod)
n=0; t=t0; par=p.u(p.nu+1:end); K=p.mat.K; Kx=p.mat.Kx; 
bK=[[par(1)*K 0*K];[0*K par(6)*K]]; Lam=p.mat.M+dt*bK; [L,U,P,Q,R]=lu(Lam);
while(n<nt) % integration loop
  f=nodalf(p,p.u); t=t+dt; 
  G=bK*p.u(1:p.nu)-p.mat.M*f; 
  ux=Kx*p.u(1:p.nu); utx=p.u0x; 
  cs=(utx'*G)/(utx'*ux); 
  g=p.mat.M*p.u(1:p.nu)+dt*(p.mat.M*f+cs*ux); 
  if (mod(n,vmod)==0);  vel=[vel [t; cs]]; end 
  p.u(1:p.nu)=Q*(U\(L\(P*(R\g)))); n=n+1;  t=t+dt; % time stepping
  if(mod(n,pmod)==0); 
      r=pderesi(p,p.u); r1=norm(r,'inf'); 
      plotsol(p,p.plot.ifig,p.plot.pcmp,p.plot.pstyle); 
    title(['t=' mat2str(t,3) ', r=' mat2str(r1,3)]); 
  end
end 
t1=t; 