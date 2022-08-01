function plox0(p,x0,wnr)

xy=getpte(p); 
%we are interested in a channel of dimensions Lx x Ly. This functions 
% takes x0 as a fix value along the x axis and then print the profile of the solution
%  profiles along the y direction
%x0=0;
indpro=find(abs(xy(1,:)-x0)<0.1);
u1=p.u(1:p.np); v1=p.u(p.np+1:2*p.np);

% p.y0=y0; 
% p.indpro=indpro;

figure(wnr); clf;
subplot(2,1,1); plot(xy(2,indpro),u1(indpro),'.-'); xlabel('x'); ylabel('u')
title(strcat('x0=',num2str(x0)));
subplot(2,1,2); plot(xy(2,indpro),v1(indpro),'.-r');xlabel('x'); ylabel('v')



end