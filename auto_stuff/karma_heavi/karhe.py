a=run('karhe')
#Continue Hopf bifurcations
hb=run(a('HB1'),ISW=2,ICP=['c','I'],NMX=100,NPR=100,DSMAX=1e-2)
hb=hb+run(a('HB1'),ISW=2,ICP=['c','I'],NMX=600,NPR=100,DS='-',DSMAX=1e-2)
# Continue homoclinic
b=run(a('HB1'),IPS=2,ICP=['c','PERIOD'],NMX=400,NPR=20)
hom=run(b,IRS=20,IPS=9,ICP=['c','I'],NMX=100,NPR=50,DSMAX=1e-2,NTST=150)
hom=hom+run(b,IRS=20,IPS=9,ICP=['c','I'],NMX=400,NPR=100,DS='-',DSMAX=1e-2,NTST=150)
