function f=nodalf(p,u) % for Schnakenberg 
u1=u(1:p.np); u2=u(p.np+1:2*p.np); par=u(p.nu+1:end); % lam,sig,d 
f1=-u1+2*(3/2-u2.^par(4)).*(u1.^2-1/4*u1.^3)+par(8); %+ inten 
f2=par(2).*(1./par(3).*max(0,u1-1)-u2); 
f=[f1; f2]; 