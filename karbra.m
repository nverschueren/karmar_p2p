function out=karbra(p,u)
M=getM(p);
n=p.np;

xy=getpte(p); 
%we are interested in a narrow channel in  y, so we pick a representative
%value in y and plot the profile in x
y0=0;
indpro=find(abs(xy(2,:)-y0)<1e-4);
u1=p.u(1:p.np); v1=p.u(p.np+1:2*p.np);

% p.y0=y0; 
% p.indpro=indpro;

figure(10); clf;
subplot(2,1,1); plot(xy(1,indpro),u1(indpro),'.-'); xlabel('x'); ylabel('u')
title(strcat('y0=',num2str(y0)));
subplot(2,1,2); plot(xy(1,indpro),v1(indpro),'.-r');xlabel('x'); ylabel('v')



out=[u(p.nu+1:end); % parameters: 8{1:'D',2:'\eps',3:'nB',4:'M',5:'s',6:'del',7:'dyy',8:'I'};
     sqrt(u(1:n)'*(M(1:n,1:n)*u(1:n)))/sqrt(p.Om); %L2-Norm 9 
     max(u(1:n)); %10: max u, not v!
     min(u(1:n)); %11 min u, not v!
     sqrt(trapz(xy(1,indpro)',u1(indpro).^2))/sqrt(max(xy(1,indpro)))];  %12: L-2 norm u(x) when y=y0