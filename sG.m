function r=sG(p,u) % Karma
n=p.np; f=nodalf(p,u); par=u(p.nu+1:end); d1=par(1); del=par(6); dyy=par(7); 
u=u(1:p.nu); try; dbc=p.dbc; catch dbc=0; end
if p.dim==1
    K=kron([[par(1),0];[0,par(6)]],p.mat.K);
    r=K*u-p.mat.M*f-par(5)*p.mat.Kx*u;    
    if dbc; r(p.idx1+n)=u(p.idx1+n); end % DBcs for u2
else;   LL=par(1)*p.mat.Kxx+par(7)*p.mat.Kyy; 
    bK=[[LL, 0*LL]; [0*LL, del*LL]];    
    r=bK*u-p.mat.M*f-par(5)*p.mat.Kx*u;
    if dbc; r(p.idx1+n)=u(p.idx1+n); end % DBcs for u2
end
