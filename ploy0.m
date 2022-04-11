function ploy0(p,y0,wnr)

xy=getpte(p); 
%we are interested in a narrow channel in  y, so we pick a representative
%value in y and plot the profile in x
%y0=0;
indpro=find(abs(xy(2,:)-y0)<1e-4);
u1=p.u(1:p.np); v1=p.u(p.np+1:2*p.np);

% p.y0=y0; 
% p.indpro=indpro;

figure(wnr); clf;
subplot(2,1,1); plot(xy(1,indpro),u1(indpro),'.-'); xlabel('x'); ylabel('u')
title(strcat('y0=',num2str(y0)));
subplot(2,1,2); plot(xy(1,indpro),v1(indpro),'.-r');xlabel('x'); ylabel('v')



end