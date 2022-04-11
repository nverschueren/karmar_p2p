function Gu=sGjac(p,u)
par=u(p.nu+1:end); n=p.np; d1=par(1); del=par(6); dyy=par(7); 
[f1u,f1v,f2u,f2v]=njac(p,u); % (nodal) Jacobian of 'nonlin' 
Fu=[[spdiags(f1u,0,n,n),spdiags(f1v,0,n,n)];
    [spdiags(f2u,0,n,n),spdiags(f2v,0,n,n)]];
try; dbc=p.dbc; catch dbc=0; end
if p.dim==1
    Ks=p.mat.K; K=[par(1)*Ks 0*Ks; 0*Ks par(6)*Ks];
    Gu=K-p.mat.M*Fu-par(5)*p.mat.Kx;   
    if dbc; Gu(n+1,:)=0; Gu(n+1,n+1)=1; end
else LL=par(1)*p.mat.Kxx+par(7)*p.mat.Kyy; 
    bK=[[LL, 0*LL]; [0*LL, del*LL]];    
    Gu=bK-p.mat.M*Fu-par(5)*p.mat.Kx;
    if dbc; for i=1:length(p.idx1); 
        Gu(n+p.idx1(i),:)=0; Gu(n+p.idx1(i),n+p.idx1(i))=1; 
        end 
    end
end