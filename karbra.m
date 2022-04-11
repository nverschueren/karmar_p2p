function out=karbra(p,u)
M=getM(p);
n=p.np;

g


out=[u(p.nu+1:end); % parameters: 8{1:'D',2:'\eps',3:'nB',4:'M',5:'s',6:'del',7:'dyy',8:'I'};
     sqrt(u(1:n)'*(M(1:n,1:n)*u(1:n)))/sqrt(p.Om); %L2-Norm 9 
     max(u(1:n)); %10: max u, not v!
     min(u(1:n)); %11 min u, not v!
     sqrt(trapz(xy(1,indpro)',u1(indpro).^2))/sqrt(max(xy(1,indpro)))];  %12: L-2 norm u(x) when y=y0