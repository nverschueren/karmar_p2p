a=run('karramp')
b=a+run(a('HB1'),IPS=2,ICP=['c','PERIOD'],NMX=100,NPR=20)
# Continue Hopf bifurcation 
b1=run(b('HB1'),ICP=['I','c'],ILP=0,ISW=2,NMX=100)
hb=b1+run(b('HB1'),ICP=['I','c'],ILP=0,ISW=2,NMX=100,DS='-')
hb=relabel(hb)
# Continuation Homoclinic wrt I
hom=run(b,IRS=9,IPS=9,ICP=['c','I'],NMX=40,NPR=3,DSMAX=1e-2)
hom2=run(b,IRS=9,IPS=9,ICP=['c','I'],NMX=100,NPR=20,DSMAX=1e-1,DS='-')

# Continue Homoclinic wrt nB
#d=run(b,IRS=10,IPS=9,ICP=['c','nb'],NMX=200,NPR=20,DSMAX=1e-2)
#d=d+run(b,IRS=10,IPS=9,ICP=['c','nb'],NMX=200,NPR=20,DS=-0.01,DSMAX=1e-2)
# Continue Homoclinic wrt epsilon
#e=run(b,IRS=10,IPS=9,ICP=['epsilon','c'],NMX=200,NPR=20,DS=-0.001,DSMAX=1e-2)
#e=e+run(b,IRS=10,IPS=9,ICP=['epsilon','c'],NMX=100,NPR=20,DS=0.001,DSMAX=1e-2)
# Continue Homoclinic wrt D
#f=run(b,IRS=10,IPS=9,ICP=['D','c'],NMX=00,NPR=20)
#f=f+run(b,IRS=10,IPS=9,ICP=['D','c'],NMX=200,NPR=20,DS=-0.1,DSMAX=1e-2,RL0=0)
