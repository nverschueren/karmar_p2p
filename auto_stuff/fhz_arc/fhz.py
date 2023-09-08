# The parameters (s)peed and p are allow to vary. Starting from (p,s)=(0,1), we perform continuation on p until we find a Hopf bifurcation (HB)
a=run('fhn')
# We compute the curve in the (p,s) space where the Hopf bifurcation takes place (cf. Fig 1 of Champneys et al 2007 SIADS)
b=run(a('HB1'),ISW=2,ICP=[1,2],UZSTOP={'p':[0,0.63],'s':[0.3,1.5]},NMX=80,NPR=8)
#go along the same branch but in the opposite direction
b=run(b('UZ1'),DS='-',DSMAX=5e-2,NMX=200,UZR={'s':[1.4],'p':[0.61]})
#Now we select a particular horizontal line and do continuation in p for a fixed (s)peed, as shown in the figure, there should be 2 HB (2 intersections with the parabola)
c=run(b('UZ1'),ISW=1,ICP=['p','s'],NMX=40,UZSTOP={})
c=run(c,IRS=20,DS='-',NMX=200,NPR=30)
#plot b+c




