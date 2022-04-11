function [f1u,f1v,f2u,f2v]=njac(p,u) % Jacobian for Schnakenberg
%u1=u(1:p.np); u2=u(p.np+1:2*p.np); 
par=u(p.nu+1:end); u1=u(1:p.nu/2); u2=u(p.nu/2+1:p.nu);
f1u=-1+2*(3/2-u2.^par(4)).*(2*u1-3/4*u1.^2);
f1v=-2*par(4)*u2.^(par(4)-1).*(u1.^2-1/4*u1.^3); 
f2u=par(2)/par(3)*heaviside(u1-1); 
f2v=-par(2)*ones(p.np,1); 